# ASSISTED SLATE -- 2026-10-29T00:37Z (`SL-20261029T003732Z-11fa6081`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

333 open matches not seen started, 889 markets. Skipped: {"scheduled_start_over_24h_past": 3, "no_match_winner_listed": 1, "first_ball_already_observed": 2}. Sources: shadow board 2026-10-28T23:09:46.593898+00:00, Model 4 2026-10-28T23:11:36.317329+00:00, Gen-1 ledger 2026-10-28T23:09:42.200562+00:00, external 2026-10-28T23:54:16.751676+00:00, capture 20261028T235039Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-10-29 01:30Z**
* Recommended RUN TENNIS time: **2026-10-29 00:45Z**
* Final price/status check time: **2026-10-29 01:20Z**
* Number of matches in window: 1 (Alycia Parks vs Kimberly Birrell)

* **1 main-tour match(es) have NO verified start status** (STATUS_AMBIGUOUS): BET blocked until a live status check.

Slate built 2026-10-29T00:37Z. Refresh due by: 2026-10-29 00:45Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 43, "HIGH_REVIEW": 76, "NORMAL": 364, "REVIEW": 99, "UNPRICED": 307}; match winners: {"EXTREME": 35, "HIGH_REVIEW": 63, "NORMAL": 211, "REVIEW": 57, "UNPRICED": 300}; quote freshness at build: {"FRESH": 582}.

## Leylah Fernandez vs Elise Mertens -- WTA Tokyo R16

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-28 04:30Z
* Current expected start: 2026-10-28 04:30Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: 2026-10-28 03:45Z

* Status notes: NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-28T04:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:210722:220367:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leylah Fernandez (`KXWTAMATCH-26OCT27FERMER-FER`) | 0.47 / 0.48 (2898) | 47.5% | 46.9% | 34.4% | 38.3% [36.3%-43.3%] | -- | -- | -- | -- | PASS | -0.7 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elise Mertens (`KXWTAMATCH-26OCT27FERMER-MER`) | 0.52 / 0.53 (14786) | 52.5% | 53.1% | 65.6% | 61.7% [56.7%-63.7%] | -- | -- | -- | -- | SHADOW_BET | +0.7 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4828.0, B 3838.0; serve-point win A 59.3%, B 40.1%; Elo A 1978.3, B 1978.5; model uncertainty 0.0348
* Form inputs: days since last match A 1, B 2; matches on record A 406, B 807; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.020, surface_dev_loose -0.005, surface_dev_tight +0.010
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT27FERMER-23` Over 22.5 games: 0.47/0.48 mid 47.5%, model 57.9% (projection_v2.0 (prediction ledger)) -- gap +10.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT27FERMER-28` Over 27.5 games: 0.23/0.37 mid 30.0%, model 36.9% (projection_v2.0 (prediction ledger)) -- gap +6.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT27FERMER-18` Over 17.5 games: 0.79/0.88 mid 83.5%, model 90.2% (projection_v2.0 (prediction ledger)) -- gap +6.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT27FERMER-1-FER` Will Leylah Annie Fernandez win set 1 in the Leylah Annie Fernandez vs Elise Mertens match: 0.48/0.51 mid 49.5%, model 47.9% (projection_v2.0 (prediction ledger)) -- gap -1.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT27FERMER-1-MER` Will Elise Mertens win set 1 in the Leylah Annie Fernandez vs Elise Mertens match: 0.49/0.52 mid 50.5%, model 52.1% (projection_v2.0 (prediction ledger)) -- gap +1.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Petr Bar Biryukov vs Fajing Sun -- ATP Challenger Ningbo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-28T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111806:209951:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Petr Bar Biryukov (`KXATPCHALLENGERMATCH-26OCT27BARSUN-BAR`) | 0.34 / 0.35 (1253) | 34.5% | 40.5% | 31.4% | 35.7% [33.6%-38.4%] | -- | -- | -- | -- | PASS | +6.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Fajing Sun (`KXATPCHALLENGERMATCH-26OCT27BARSUN-SUN`) | 0.65 / 0.66 (7687) | 65.5% | 59.5% | 68.6% | 64.3% [61.6%-66.4%] | -- | -- | -- | -- | PASS | -6.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4232.0, B 4200.0; serve-point win A 68.1%, B 29.9%; Elo A 1539.3, B 1556.5; model uncertainty 0.0242
* Form inputs: days since last match A 11, B 9; matches on record A 242, B 526; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.004, surface_dev_loose -0.004, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Naoya Honda vs Liam Broady -- ATP Challenger Ningbo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-28T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106281:211897:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liam Broady (`KXATPCHALLENGERMATCH-26OCT27HONBRO-BRO`) | 0.80 / 0.81 (8471) | 80.5% | 75.8% | 87.5% | 85.6% [84.7%-86.7%] | -- | -- | -- | -- | SHADOW_BET | -4.8 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Naoya Honda (`KXATPCHALLENGERMATCH-26OCT27HONBRO-HON`) | 0.20 / 0.21 (3434) | 20.5% | 24.2% | 12.4% | 14.4% [13.3%-15.3%] | -- | -- | -- | -- | PASS | +3.8 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1551.0, B 4440.0; serve-point win A 58.2%, B 36.4%; Elo A 1354.9, B 1639.6; model uncertainty 0.0101
* Form inputs: days since last match A 44, B 9; matches on record A 70, B 947; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.006, surface_dev_loose -0.006, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Tristan Schoolkate vs Jie Cui -- ATP Challenger Ningbo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-28T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200666:209262:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jie Cui (`KXATPCHALLENGERMATCH-26OCT27SCHCUI-CUI`) | 0.34 / 0.35 (34) | 34.5% | 36.4% | 39.6% | 37.7% [34.5%-39.1%] | -- | -- | -- | -- | PASS | +1.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tristan Schoolkate (`KXATPCHALLENGERMATCH-26OCT27SCHCUI-SCH`) | 0.64 / 0.65 (4) | 64.5% | 63.6% | 60.4% | 62.3% [60.9%-65.5%] | -- | -- | -- | -- | PASS | -0.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6055.0, B 3672.0; serve-point win A 68.8%, B 34.1%; Elo A 1701.7, B 1581.1; model uncertainty 0.0231
* Form inputs: days since last match A 9, B 9; matches on record A 421, B 334; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.014, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Yi Zhou vs Jake Delaney -- ATP Challenger Ningbo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-28T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:117359:212044:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jake Delaney (`KXATPCHALLENGERMATCH-26OCT27ZHODEL-DEL`) | 0.17 / 0.18 (44) | 17.5% | 19.8% | 25.7% | 24.2% [23.4%-25.6%] | -- | -- | -- | -- | SHADOW_BET | +2.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yi Zhou (`KXATPCHALLENGERMATCH-26OCT27ZHODEL-ZHO`) | 0.82 / 0.83 (6377) | 82.5% | 80.2% | 74.3% | 75.8% [74.4%-76.5%] | -- | -- | -- | -- | PASS | -2.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3697.0, B 3181.0; serve-point win A 72.0%, B 35.1%; Elo A 1641.8, B 1414.5; model uncertainty 0.0107
* Form inputs: days since last match A 9, B 9; matches on record A 180, B 340; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.000, surface_dev_loose +0.007, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Asylkozhaev / Bessonov vs Omarkhanov / Shin -- M15 Fergana R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28ASYBESOMASHI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Asylkozhaev / Bessonov (`KXITFDOUBLES-26OCT28ASYBESOMASHI-ASYBES`) | 0.50 / 0.95 (7) | 72.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Omarkhanov / Shin (`KXITFDOUBLES-26OCT28ASYBESOMASHI-OMASHI`) | 0.08 / 0.42 (5) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Caripi / Longwe-Smit vs Hopp / Thomson -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28CARLONHOPTHO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Caripi / Longwe-Smit (`KXITFDOUBLES-26OCT28CARLONHOPTHO-CARLON`) | 0.04 / 0.91 (5) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hopp / Thomson (`KXITFDOUBLES-26OCT28CARLONHOPTHO-HOPTHO`) | 0.05 / 0.91 (5) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Uzhylovskyi / Ho Yap vs Chang / Taguchi -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28UZHHOYCHATAG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chang / Taguchi (`KXITFDOUBLES-26OCT28UZHHOYCHATAG-CHATAG`) | 0.51 / 0.95 (28) | 73.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Uzhylovskyi / Ho Yap (`KXITFDOUBLES-26OCT28UZHHOYCHATAG-UZHHOY`) | 0.04 / 0.09 (27) | 6.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Gonzalo Bueno vs Carlos Maria Zarate -- ATP Challenger Guayaquil R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-28T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208293:212785:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gonzalo Bueno (`KXATPCHALLENGERMATCH-26OCT28BUEZAR-BUE`) | 0.67 / 0.69 (280) | 68.0% | -- | 51.0% | 59.9% [55.8%-65.3%] | -- | -- | -- | -- | PASS | -8.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carlos Maria Zarate (`KXATPCHALLENGERMATCH-26OCT28BUEZAR-ZAR`) | 0.31 / 0.33 (5) | 32.0% | -- | 48.9% | 40.1% [34.7%-44.2%] | -- | -- | -- | -- | WATCH | +8.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4710.0, B 2826.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0478
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Bilicic / Wriedt vs Degroot / Simons -- M15 Pembroke R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28BILWRIDEGSIM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bilicic / Wriedt (`KXITFDOUBLES-26OCT28BILWRIDEGSIM-BILWRI`) | 0.03 / 0.94 (4) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Degroot / Simons (`KXITFDOUBLES-26OCT28BILWRIDEGSIM-DEGSIM`) | 0.10 / 0.90 (3) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dobek / Van Orderlain vs Bicknell / Cicma -- M15 Pembroke R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28DOBVANBICCIC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bicknell / Cicma (`KXITFDOUBLES-26OCT28DOBVANBICCIC-BICCIC`) | 0.02 / 0.93 (4) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dobek / Van Orderlain (`KXITFDOUBLES-26OCT28DOBVANBICCIC-DOBVAN`) | 0.10 / 0.92 (3) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Theo Papamalamis vs Alex Rybakov -- M25 Norman OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126206:210494:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theo Papamalamis (`KXITFMATCH-26OCT28PAPRYB-PAP`) | 0.99 / -- (0) | -- | 45.1% | 53.6% | 41.8% [31.2%-46.4%] | 46.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | FRESH | C / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |
| Alex Rybakov (`KXITFMATCH-26OCT28PAPRYB-RYB`) | -- / 0.01 (78621) | -- | 54.9% | 46.4% | 58.2% [53.6%-68.8%] | 53.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | FRESH | C / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 1714.0, B 3082.0; serve-point win A 59.0%, B 40.1%; Elo A 1462.3, B 1614.4; model uncertainty 0.0761
* Form inputs: days since last match A 296, B 9; matches on record A 89, B 499; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oskar Brostrom Poulsen / Nikola Slavic vs Miguel Angel Reyes-Varela / Reese Stalder -- ATP Challenger Sioux Falls R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 23:50Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-28T23:50:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28POUSLAREYSTA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oskar Brostrom Poulsen / Nikola Slavic (`KXATPCHALLENGERDOUBLES-26OCT28POUSLAREYSTA-POUSLA`) | 0.15 / 0.80 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Miguel Angel Reyes-Varela / Reese Stalder (`KXATPCHALLENGERDOUBLES-26OCT28POUSLAREYSTA-REYSTA`) | 0.14 / 0.79 (950) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## LUCCA LIU vs Ryan Colby -- M15 Mazatlan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210242:213175:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ryan Colby (`KXITFMATCH-26OCT28LIUCOL-COL`) | 0.11 / 0.18 (22) | 14.5% | 53.7% | 45.8% | 54.2% [51.6%-57.3%] | 52.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +39.2 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| LUCCA LIU (`KXITFMATCH-26OCT28LIUCOL-LIU`) | 0.82 / 0.83 (1) | 82.5% | 46.3% | 54.2% | 45.8% [42.7%-48.4%] | 47.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -36.2 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 620.0, B 1404.0; serve-point win A 54.8%, B 44.5%; Elo A 1281.6, B 1337.1; model uncertainty 0.0285
* Form inputs: days since last match A 226, B 184; matches on record A 16, B 39; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28LIUCOL-COL  (YES = Ryan Colby)
Model: 54%
Kalshi: 14%
Gap: +39 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elijah Strode vs Maxwell McKennon -- M15 Mazatlan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208297:210565:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maxwell McKennon (`KXITFMATCH-26OCT28STRMCK-MCK`) | 0.52 / 0.62 (47) | 57.0% | 67.8% | 68.5% | 66.7% [65.2%-68.2%] | -- | -- | -- | -- | PASS | +10.8 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elijah Strode (`KXITFMATCH-26OCT28STRMCK-STR`) | 0.35 / 0.41 (33) | 38.0% | 32.2% | 31.6% | 33.3% [31.8%-34.8%] | -- | -- | -- | -- | PASS | -5.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 869.0, B 3096.0; serve-point win A 65.6%, B 30.6%; Elo A 1288.4, B 1399.2; model uncertainty 0.0152
* Form inputs: days since last match A 471, B 184; matches on record A 57, B 140; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Fiona Ferro vs Adriana Reami -- WTA 125K Queretaro R16

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-29 03:10Z
* Current expected start: 2026-10-29 00:25Z
* Source: COURT_PROGRESSION: preceding match on Estadio Mexcovery in progress (set 2 of best-of-3); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: 2026-10-28 23:40Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA125 (WTA_125) · Clay · scheduled 2026-10-29T03:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:211539:222299:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fiona Ferro (`KXWTACHALLENGERMATCH-26OCT28FERREA-FER`) | 0.94 / 0.95 (11111) | 94.5% | 95.2% | 91.7% | 90.7% [89.0%-91.9%] | 94.0% | -- | 94.0% | MODEL_LONE_OUTLIER | PASS | +0.7 pp | NORMAL | FRESH | B / LIMITED | ALL_AGREE | VERIFIED |
| Adriana Reami (`KXWTACHALLENGERMATCH-26OCT28FERREA-REA`) | 0.05 / 0.06 (3989) | 5.5% | 4.8% | 8.3% | 9.3% [8.1%-11.0%] | 6.0% | -- | 6.0% | MODEL_LONE_OUTLIER | SHADOW_BET | -0.7 pp | NORMAL | FRESH | B / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 2631.0, B 549.0; serve-point win A 59.8%, B 52.7%; Elo A 1777.5, B 1388.8; model uncertainty 0.0145
* Form inputs: days since last match A 1, B 1; matches on record A 573, B 186; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.016, surface_dev_loose +0.009, surface_dev_tight -0.007
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; STATUS_AMBIGUOUS

## Alycia Parks vs Kimberly Birrell -- WTA Tokyo R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-28 04:30Z
* Current expected start: 2026-10-29 01:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: 2026-10-29 00:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1260_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-28T04:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214040:219917:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kimberly Birrell (`KXWTAMATCH-26OCT27PARBIR-BIR`) | 0.61 / 0.62 (20359) | 61.5% | 58.7% | 57.8% | 59.3% [58.3%-60.3%] | -- | -- | -- | -- | PASS | -2.8 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alycia Parks (`KXWTAMATCH-26OCT27PARBIR-PAR`) | 0.39 / 0.40 (22850) | 39.5% | 41.3% | 42.2% | 40.7% [39.7%-41.7%] | -- | -- | -- | -- | PASS | +1.8 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5263.0, B 5020.0; serve-point win A 57.8%, B 40.5%; Elo A 1781.0, B 1874.5; model uncertainty 0.0102
* Form inputs: days since last match A 2, B 3; matches on record A 442, B 478; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.005, surface_dev_loose +0.005, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT27PARBIR-22` Over 21.5 games: 0.50/0.52 mid 51.0%, model 63.6% (projection_v2.0 (prediction ledger)) -- gap +12.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT27PARBIR-27` Over 26.5 games: 0.26/0.33 mid 29.5%, model 40.3% (projection_v2.0 (prediction ledger)) -- gap +10.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT27PARBIR-17` Over 16.5 games: 0.82/0.94 mid 88.0%, model 94.6% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT27PARBIR-1-PAR` Will Alycia Parks win set 1 in the Alycia Parks vs Kimberly Birrell match: 0.40/0.43 mid 41.5%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap +2.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT27PARBIR-2-BIR` Will Kimberly Birrell win set 2 in the Alycia Parks vs Kimberly Birrell match: 0.58/0.59 mid 58.5%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap -2.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT27PARBIR-2-PAR` Will Alycia Parks win set 2 in the Alycia Parks vs Kimberly Birrell match: 0.39/0.44 mid 41.5%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap +2.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT27PARBIR-1-BIR` Will Kimberly Birrell win set 1 in the Alycia Parks vs Kimberly Birrell match: 0.57/0.59 mid 58.0%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap -2.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Matteo Covato vs Gerardo Delgado -- M15 Mazatlan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28COVDEL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Covato (`KXITFMATCH-26OCT28COVDEL-COV`) | 0.90 / 0.92 (151) | 91.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gerardo Delgado (`KXITFMATCH-26OCT28COVDEL-DEL`) | 0.08 / 0.10 (256) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rafael De Alba vs Oswaldo Alejandro Reyes Tirado -- M15 Mazatlan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208908:213783:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rafael De Alba (`KXITFMATCH-26OCT28DEAREY-DEA`) | 0.45 / 0.73 (49) | 59.0% | 50.5% | 50.0% | 47.4% [46.9%-51.1%] | -- | -- | -- | -- | PASS | -8.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oswaldo Alejandro Reyes Tirado (`KXITFMATCH-26OCT28DEAREY-REY`) | 0.28 / 0.50 (37) | 39.0% | 49.5% | 50.0% | 52.6% [48.9%-53.1%] | -- | -- | -- | -- | PASS | +10.5 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1439.0, B 411.0; serve-point win A 56.7%, B 43.4%; Elo A 1198.5, B 1215.7; model uncertainty 0.0211
* Form inputs: days since last match A 184, B 184; matches on record A 35, B 9; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Frazier Rengifo vs Jesse Flores -- M15 Mazatlan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132374:200105:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jesse Flores (`KXITFMATCH-26OCT28RENFLO-FLO`) | 0.60 / 0.73 (72) | 66.5% | 67.2% | 64.9% | 61.6% [60.1%-63.5%] | -- | -- | -- | -- | PASS | +0.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Frazier Rengifo (`KXITFMATCH-26OCT28RENFLO-REN`) | 0.24 / 0.34 (2) | 29.0% | 32.8% | 35.1% | 38.5% [36.5%-39.9%] | -- | -- | -- | -- | PASS | +3.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 468.0, B 2047.0; serve-point win A 59.9%, B 36.6%; Elo A 1234.6, B 1309.5; model uncertainty 0.0171
* Form inputs: days since last match A 184, B 184; matches on record A 29, B 190; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jenson Brooksby vs Dylan Dietrich -- ATP Challenger Sioux Falls R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-29T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202385:210157:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jenson Brooksby (`KXATPCHALLENGERMATCH-26OCT28BRODIE-BRO`) | 0.65 / 0.68 (25) | 66.5% | 68.3% | 38.6% | 59.0% [51.0%-66.1%] | -- | -- | -- | -- | WATCH | +1.8 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dylan Dietrich (`KXATPCHALLENGERMATCH-26OCT28BRODIE-DIE`) | 0.31 / 0.35 (68) | 33.0% | 31.7% | 61.4% | 41.0% [33.9%-49.0%] | -- | -- | -- | -- | PASS | -1.3 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3795.0, B 1479.0; serve-point win A 65.0%, B 38.8%; Elo A 1850.5, B 1640.5; model uncertainty 0.0756
* Form inputs: days since last match A 9, B 30; matches on record A 294, B 66; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.024, surface_dev_loose -0.020, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Frusina / Papamalamis vs Kalina / Jeff Planinsek -- M25 Norman OK R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28FRUPAPKALJEF:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Frusina / Papamalamis (`KXITFDOUBLES-26OCT28FRUPAPKALJEF-FRUPAP`) | 0.26 / 0.76 (3) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kalina / Jeff Planinsek (`KXITFDOUBLES-26OCT28FRUPAPKALJEF-KALJEF`) | 0.19 / 0.68 (4) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ingrid Neel / Giuliana Olmos vs Tereza Mihalikova / Olivia Nicholls -- WTA Tokyo QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-29 04:30Z
* Current expected start: 2026-10-29 02:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: 2026-10-29 01:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-29T04:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28NEEOLMMIHNIC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tereza Mihalikova / Olivia Nicholls (`KXWTADOUBLES-26OCT28NEEOLMMIHNIC-MIHNIC`) | 0.49 / 0.50 (500) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ingrid Neel / Giuliana Olmos (`KXWTADOUBLES-26OCT28NEEOLMMIHNIC-NEEOLM`) | 0.49 / 0.51 (19) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Rodrigo Alujas vs Tarun Karra -- M15 Mazatlan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 02:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T02:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212286:213598:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rodrigo Alujas (`KXITFMATCH-26OCT28ALUKAR-ALU`) | 0.86 / 0.88 (229) | 87.0% | 80.7% | 75.0% | 72.0% [71.0%-75.1%] | -- | -- | -- | -- | PASS | -6.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tarun Karra (`KXITFMATCH-26OCT28ALUKAR-KAR`) | 0.12 / 0.14 (356) | 13.0% | 19.4% | 25.0% | 28.0% [24.9%-29.0%] | -- | -- | -- | -- | PASS | +6.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2335.0, B 201.0; serve-point win A 59.8%, B 46.7%; Elo A 1295.7, B 1132.3; model uncertainty 0.0207
* Form inputs: days since last match A 191, B 226; matches on record A 83, B 8; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ian Lucca Cervantes Tomas vs Joaquin Guilleme -- M15 Mazatlan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 02:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T02:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212486:213603:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ian Lucca Cervantes Tomas (`KXITFMATCH-26OCT28CERGUI-CER`) | 0.20 / 0.23 (151) | 21.5% | 27.2% | 30.6% | 28.8% [26.6%-30.6%] | -- | -- | -- | -- | PASS | +5.7 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Joaquin Guilleme (`KXITFMATCH-26OCT28CERGUI-GUI`) | 0.79 / 0.80 (1) | 79.5% | 72.8% | 69.4% | 71.2% [69.4%-73.4%] | -- | -- | -- | -- | PASS | -6.7 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 529.0, B 925.0; serve-point win A 56.8%, B 38.5%; Elo A 1159.9, B 1323.6; model uncertainty 0.0202
* Form inputs: days since last match A 401, B 289; matches on record A 24, B 17; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ellen Perez / Demi Schuurs vs Storm Hunter / Maya Joint -- WTA Tokyo QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-29 07:00Z
* Current expected start: 2026-10-29 04:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: 2026-10-29 03:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-29T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29PERSCHHUNJOI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Storm Hunter / Maya Joint (`KXWTADOUBLES-26OCT29PERSCHHUNJOI-HUNJOI`) | 0.50 / 0.53 (287) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ellen Perez / Demi Schuurs (`KXWTADOUBLES-26OCT29PERSCHHUNJOI-PERSCH`) | 0.46 / 0.49 (428) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Gabriela Dabrowski / Luisa Stefani vs Hao-Ching Chan / Miyu (1994) Kato -- WTA Tokyo QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 04:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-30T04:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-29T04:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28DABSTECHAKAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hao-Ching Chan / Miyu (1994) Kato (`KXWTADOUBLES-26OCT28DABSTECHAKAT-CHAKAT`) | 0.17 / 0.23 (293) | 20.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gabriela Dabrowski / Luisa Stefani (`KXWTADOUBLES-26OCT28DABSTECHAKAT-DABSTE`) | 0.77 / 0.81 (66) | 79.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Asia Muhammad / Shuai Zhang vs Sara Errani / Jasmine Paolini -- WTA Tokyo QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 04:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-30T04:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-29T04:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28MUHZHAERRPAO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Errani / Jasmine Paolini (`KXWTADOUBLES-26OCT28MUHZHAERRPAO-ERRPAO`) | 0.59 / 0.65 (331) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Asia Muhammad / Shuai Zhang (`KXWTADOUBLES-26OCT28MUHZHAERRPAO-MUHZHA`) | 0.35 / 0.39 (48) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jil Teichmann vs Zeynep Sonmez -- WTA Guangzhou R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-28 08:00Z
* Current expected start: 2026-10-29 05:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: 2026-10-29 04:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1260_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-28T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213525:220309:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zeynep Sonmez (`KXWTAMATCH-26OCT28TEISON-SON`) | 0.67 / 0.68 (30227) | 67.5% | 64.2% | 68.4% | 65.0% [62.5%-66.5%] | -- | -- | -- | -- | PASS | -3.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jil Teichmann (`KXWTAMATCH-26OCT28TEISON-TEI`) | 0.33 / 0.34 (9131) | 33.5% | 35.8% | 31.6% | 35.0% [33.5%-37.5%] | -- | -- | -- | -- | PASS | +2.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2567.0, B 4355.0; serve-point win A 54.3%, B 42.9%; Elo A 1766.8, B 1834.7; model uncertainty 0.0197
* Form inputs: days since last match A 1, B 1; matches on record A 583, B 430; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.010, surface_dev_loose -0.010, surface_dev_tight +0.010
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT28TEISON-22` Over 21.5 games: 0.45/0.46 mid 45.5%, model 60.6% (projection_v2.0 (prediction ledger)) -- gap +15.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT28TEISON-27` Over 26.5 games: 0.25/0.37 mid 31.0%, model 37.6% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT28TEISON-17` Over 16.5 games: 0.82/0.91 mid 86.5%, model 92.6% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT28TEISON-2-SON` Will Zeynep Sonmez win set 2 in the Jil Teichmann vs Zeynep Sonmez match: 0.61/0.66 mid 63.5%, model 59.6% (projection_v2.0 (prediction ledger)) -- gap -3.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT28TEISON-2-TEI` Will Jil Teichmann win set 2 in the Jil Teichmann vs Zeynep Sonmez match: 0.34/0.39 mid 36.5%, model 40.4% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT28TEISON-1-SON` Will Zeynep Sonmez win set 1 in the Jil Teichmann vs Zeynep Sonmez match: 0.62/0.64 mid 63.0%, model 59.6% (projection_v2.0 (prediction ledger)) -- gap -3.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT28TEISON-1-TEI` Will Jil Teichmann win set 1 in the Jil Teichmann vs Zeynep Sonmez match: 0.36/0.38 mid 37.0%, model 40.4% (projection_v2.0 (prediction ledger)) -- gap +3.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Claire Liu vs Katerina Siniakova -- WTA Guangzhou R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-29 08:00Z
* Current expected start: 2026-10-29 05:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: 2026-10-29 04:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-29T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211701:214906:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Claire Liu (`KXWTAMATCH-26OCT29LIUSIN-LIU`) | 0.38 / 0.39 (8950) | 38.5% | 29.2% | 29.3% | 29.3% [28.4%-31.6%] | 39.8% | -- | 39.8% | MODEL_LONE_OUTLIER | PASS | -9.3 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Katerina Siniakova (`KXWTAMATCH-26OCT29LIUSIN-SIN`) | 0.61 / 0.62 (5944) | 61.5% | 70.8% | 70.7% | 70.7% [68.4%-71.6%] | 60.2% | -- | 60.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +9.3 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3837.0, B 4278.0; serve-point win A 53.4%, B 42.5%; Elo A 1772.0, B 1928.6; model uncertainty 0.0162
* Form inputs: days since last match A 1, B 0; matches on record A 458, B 726; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT29LIUSIN-26` Over 25.5 games: 0.27/0.35 mid 31.0%, model 40.3% (projection_v2.0 (prediction ledger)) -- gap +9.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT29LIUSIN-21` Over 20.5 games: 0.54/0.55 mid 54.5%, model 63.0% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT29LIUSIN-1-LIU` Will Claire Liu win set 1 in the Claire Liu vs Katerina Siniakova match: 0.41/0.43 mid 42.0%, model 35.7% (projection_v2.0 (prediction ledger)) -- gap -6.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT29LIUSIN-1-SIN` Will Katerina Siniakova win set 1 in the Claire Liu vs Katerina Siniakova match: 0.57/0.59 mid 58.0%, model 64.3% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT29LIUSIN-16` Over 15.5 games: 0.86/0.94 mid 90.0%, model 95.9% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT29LIUSIN-2-LIU` Will Claire Liu win set 2 in the Claire Liu vs Katerina Siniakova match: 0.38/0.43 mid 40.5%, model 35.7% (projection_v2.0 (prediction ledger)) -- gap -4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT29LIUSIN-2-SIN` Will Katerina Siniakova win set 2 in the Claire Liu vs Katerina Siniakova match: 0.57/0.62 mid 59.5%, model 64.3% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Terence Atmane vs Taro Daniel -- ATP Challenger Seoul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-29T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106121:209279:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Terence Atmane (`KXATPCHALLENGERMATCH-26OCT28ATMDAN-ATM`) | 0.60 / 0.61 (1296) | 60.5% | 66.3% | 53.8% | 57.6% [55.7%-60.4%] | 59.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Taro Daniel (`KXATPCHALLENGERMATCH-26OCT28ATMDAN-DAN`) | 0.38 / 0.39 (128) | 38.5% | 33.7% | 46.2% | 42.4% [39.6%-44.3%] | 40.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -4.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5304.0, B 4509.0; serve-point win A 69.1%, B 34.4%; Elo A 1805.6, B 1666.3; model uncertainty 0.0235
* Form inputs: days since last match A 5, B 11; matches on record A 437, B 1067; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.019, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Herman Hoeyeraal vs Philip Sekulic -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208382:210340:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Herman Hoeyeraal (`KXITFMATCH-26OCT28HOESEK-HOE`) | -- / 0.01 (51451) | -- | 17.8% | 28.7% | 21.2% [19.4%-23.5%] | -- | -- | -- | -- | PASS | -- | UNPRICED | FRESH | C / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |
| Philip Sekulic (`KXITFMATCH-26OCT28HOESEK-SEK`) | 0.99 / -- (0) | -- | 82.2% | 71.3% | 78.8% [76.5%-80.6%] | -- | -- | -- | -- | WATCH | -- | UNPRICED | FRESH | C / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 1265.0, B 4045.0; serve-point win A 60.3%, B 32.3%; Elo A 1277.8, B 1560.3; model uncertainty 0.0206
* Form inputs: days since last match A 114, B 36; matches on record A 32, B 272; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.011, surface_dev_loose +0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tai Leonard Sach vs Ymerali Ibraimi -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212740:214192:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ymerali Ibraimi (`KXITFMATCH-26OCT28SACIBR-IBR`) | -- / 0.01 (208004) | -- | 27.4% | 17.7% | 30.8% [25.1%-38.4%] | -- | -- | -- | -- | PASS | -- | UNPRICED | FRESH | D / POOR | INSUFFICIENT_INPUTS | VERIFIED |
| Tai Leonard Sach (`KXITFMATCH-26OCT28SACIBR-SAC`) | 0.99 / -- (0) | -- | 72.6% | 82.3% | 69.2% [61.7%-74.9%] | -- | -- | -- | -- | PASS | -- | UNPRICED | FRESH | D / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 2265.0, B 660.0; serve-point win A 62.7%, B 42.0%; Elo A 1397.6, B 1311.9; model uncertainty 0.066
* Form inputs: days since last match A 233, B 219; matches on record A 74, B 11; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.000, surface_dev_loose +0.009, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stefanos Sakellaridis vs Coleman Wong -- ATP Challenger Seoul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-29T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208852:209409:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefanos Sakellaridis (`KXATPCHALLENGERMATCH-26OCT28SAKWON-SAK`) | 0.37 / 0.38 (9137) | 37.5% | 38.6% | 46.2% | 44.2% [42.3%-46.2%] | -- | 38.2% | 38.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +1.1 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Coleman Wong (`KXATPCHALLENGERMATCH-26OCT28SAKWON-WON`) | 0.62 / 0.63 (3396) | 62.5% | 61.4% | 53.8% | 55.8% [53.8%-57.7%] | -- | 62.5% | 62.5% | MODEL_LONE_OUTLIER | PASS | -1.1 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4875.0, B 5943.0; serve-point win A 65.7%, B 31.9%; Elo A 1643.9, B 1745.2; model uncertainty 0.0191
* Form inputs: days since last match A 9, B 9; matches on record A 383, B 336; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.019, surface_dev_loose -0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Harrison Satara vs Blake Ellis -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:134329:214483:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Blake Ellis (`KXITFMATCH-26OCT28SATELL-ELL`) | 0.99 / -- (0) | -- | 80.2% | 49.0% | 77.0% [72.1%-81.6%] | -- | -- | -- | -- | PASS | -- | UNPRICED | FRESH | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |
| Harrison Satara (`KXITFMATCH-26OCT28SATELL-SAT`) | -- / 0.01 (11243) | -- | 19.8% | 51.0% | 22.9% [18.4%-27.9%] | -- | -- | -- | -- | PASS | -- | UNPRICED | FRESH | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 310.0, B 2473.0; serve-point win A 61.6%, B 31.5%; Elo A 1317.4, B 1570.8; model uncertainty 0.0476
* Form inputs: days since last match A 219, B 44; matches on record A 5, B 391; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.015, surface_dev_loose +0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anton Shepp vs Zane Stevens -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209394:213204:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anton Shepp (`KXITFMATCH-26OCT28SHESTE-SHE`) | 0.67 / 0.68 (17537) | 67.5% | 86.9% | 91.2% | 80.8% [76.6%-84.8%] | -- | -- | -- | -- | PASS | +19.4 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zane Stevens (`KXITFMATCH-26OCT28SHESTE-STE`) | 0.32 / 0.33 (9045) | 32.5% | 13.2% | 8.8% | 19.1% [15.2%-23.4%] | -- | -- | -- | -- | PASS | -19.4 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2073.0, B 477.0; serve-point win A 68.6%, B 40.4%; Elo A 1440.8, B 1238.6; model uncertainty 0.0409
* Form inputs: days since last match A 38, B 352; matches on record A 69, B 11; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28SHESTE-SHE  (YES = Anton Shepp)
Model: 87%
Kalshi: 68%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sho Shimabukuro vs Jay Friend -- ATP Challenger Seoul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-29T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28SHIHAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jay Friend (`KXATPCHALLENGERMATCH-26OCT28SHIHAR-HAR`) | 0.45 / 0.47 (8202) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sho Shimabukuro (`KXATPCHALLENGERMATCH-26OCT28SHIHAR-SHI`) | 0.53 / 0.54 (345) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Vaidehee Chaudhari vs Lucia Gale -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28CHAGAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vaidehee Chaudhari (`KXITFWMATCH-26OCT28CHAGAL-CHA`) | 0.97 / 0.98 (32979) | 97.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lucia Gale (`KXITFWMATCH-26OCT28CHAGAL-GAL`) | 0.02 / 0.03 (9961) | 2.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Malkin / Carolina Millan Acosta vs Guadalupe Regalado Macias / Senties -- W50 Morelia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28MALCARGUASEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Guadalupe Regalado Macias / Senties (`KXITFWDOUBLES-26OCT28MALCARGUASEN-GUASEN`) | 0.05 / 0.58 (1) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Malkin / Carolina Millan Acosta (`KXITFWDOUBLES-26OCT28MALCARGUASEN-MALCAR`) | 0.36 / 0.91 (2) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hikaru Sato vs Renee Alame -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221141:266383:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Renee Alame (`KXITFWMATCH-26OCT28SATALA-ALA`) | 0.24 / 0.25 (9851) | 24.5% | 13.0% | 23.8% | 21.0% [18.8%-22.1%] | -- | -- | -- | -- | PASS | -11.5 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hikaru Sato (`KXITFWMATCH-26OCT28SATALA-SAT`) | 0.75 / 0.76 (32483) | 75.5% | 87.0% | 76.2% | 79.0% [77.9%-81.2%] | -- | -- | -- | -- | PASS | +11.5 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1807.0, B 291.0; serve-point win A 60.7%, B 47.9%; Elo A 1465.8, B 1228.7; model uncertainty 0.0166
* Form inputs: days since last match A 191, B 261; matches on record A 175, B 9; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.004, surface_dev_loose +0.007, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Belle Thompson vs Dayeon Back -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220432:259858:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dayeon Back (`KXITFWMATCH-26OCT28THOBAC-BAC`) | 0.92 / 0.93 (3328) | 92.5% | 91.6% | 92.4% | 90.0% [86.1%-92.0%] | -- | -- | -- | -- | WATCH | -0.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Belle Thompson (`KXITFWMATCH-26OCT28THOBAC-THO`) | 0.07 / 0.08 (2127) | 7.5% | 8.4% | 7.6% | 10.0% [8.0%-13.9%] | -- | -- | -- | -- | PASS | +0.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1699.0, B 3370.0; serve-point win A 47.7%, B 42.0%; Elo A 1312.7, B 1649.3; model uncertainty 0.0295
* Form inputs: days since last match A 219, B 35; matches on record A 114, B 295; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.005, surface_dev_loose -0.009, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Naomi Osaka vs Mia Pohankova -- WTA Tokyo R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-29 04:30Z
* Current expected start: 2026-10-29 05:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: 2026-10-29 04:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+60_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-29T04:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211768:266376:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naomi Osaka (`KXWTAMATCH-26OCT28OSAPOH-OSA`) | 0.79 / 0.80 (41097) | 79.5% | 75.5% | 71.6% | 77.3% [73.7%-83.8%] | 77.5% | -- | 77.5% | MODEL_LONE_OUTLIER | PASS | -4.0 pp | NORMAL | FRESH | B / ADEQUATE | ALL_AGREE | VERIFIED |
| Mia Pohankova (`KXWTAMATCH-26OCT28OSAPOH-POH`) | 0.20 / 0.21 (9) | 20.5% | 24.5% | 28.4% | 22.7% [16.2%-26.4%] | 22.5% | -- | 22.5% | ALL_THREE_DISAGREE | PASS | +4.0 pp | NORMAL | FRESH | B / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 2986.0, B 1596.0; serve-point win A 64.7%, B 40.8%; Elo A 2137.0, B 1860.0; model uncertainty 0.0506
* Form inputs: days since last match A 1, B 1; matches on record A 517, B 63; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.022, surface_pool_high -0.024, surface_dev_loose -0.005, surface_dev_tight +0.001
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT28OSAPOH-22` Over 21.5 games: 0.44/0.46 mid 45.0%, model 60.2% (projection_v2.0 (prediction ledger)) -- gap +15.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT28OSAPOH-27` Over 26.5 games: 0.25/0.27 mid 26.0%, model 37.1% (projection_v2.0 (prediction ledger)) -- gap +11.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT28OSAPOH-17` Over 16.5 games: 0.79/0.94 mid 86.5%, model 94.3% (projection_v2.0 (prediction ledger)) -- gap +7.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT28OSAPOH-1-OSA` Will Naomi Osaka win set 1 in the Naomi Osaka vs Mia Pohankova match: 0.72/0.74 mid 73.0%, model 67.8% (projection_v2.0 (prediction ledger)) -- gap -5.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT28OSAPOH-1-POH` Will Mia Pohankova win set 1 in the Naomi Osaka vs Mia Pohankova match: 0.26/0.28 mid 27.0%, model 32.2% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT28OSAPOH-2-POH` Will Mia Pohankova win set 2 in the Naomi Osaka vs Mia Pohankova match: 0.25/0.29 mid 27.0%, model 32.2% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT28OSAPOH-2-OSA` Will Naomi Osaka win set 2 in the Naomi Osaka vs Mia Pohankova match: 0.70/0.75 mid 72.5%, model 67.8% (projection_v2.0 (prediction ledger)) -- gap -4.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Cazacu / Uta vs Dahlberg / Velcz -- M25 Norman OK R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T05:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28CAZUTADAHVEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cazacu / Uta (`KXITFDOUBLES-26OCT28CAZUTADAHVEL-CAZUTA`) | 0.01 / 0.12 (43) | 6.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dahlberg / Velcz (`KXITFDOUBLES-26OCT28CAZUTADAHVEL-DAHVEL`) | 0.68 / 0.92 (3) | 80.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Chavez / Melero Kretzer vs Montsi / Nhavene -- M25 Norman OK R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T05:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28CHAMELMONNHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chavez / Melero Kretzer (`KXITFDOUBLES-26OCT28CHAMELMONNHA-CHAMEL`) | 0.11 / 0.25 (2) | 18.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Montsi / Nhavene (`KXITFDOUBLES-26OCT28CHAMELMONNHA-MONNHA`) | 0.67 / 0.81 (2) | 74.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nahum / Ounmuang vs Laskevich / Mamedova -- W35 Norman OK R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T05:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28NAHOUNLASMAM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Laskevich / Mamedova (`KXITFWDOUBLES-26OCT28NAHOUNLASMAM-LASMAM`) | 0.54 / 0.56 (1) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nahum / Ounmuang (`KXITFWDOUBLES-26OCT28NAHOUNLASMAM-NAHOUN`) | 0.42 / 0.47 (727) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Enzo Aguiard vs Jeremy Beale -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200003:212174:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Enzo Aguiard (`KXITFMATCH-26OCT28AGUBEA-AGU`) | 0.65 / 0.69 (154) | 67.0% | 63.6% | 87.8% | 58.1% [54.1%-64.1%] | 67.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Jeremy Beale (`KXITFMATCH-26OCT28AGUBEA-BEA`) | 0.29 / 0.33 (100) | 31.0% | 36.4% | 12.2% | 41.9% [35.9%-45.9%] | 32.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1732.0, B 133.0; serve-point win A 62.2%, B 40.5%; Elo A 1500.5, B 1467.2; model uncertainty 0.05
* Form inputs: days since last match A 44, B 1122; matches on record A 58, B 207; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Isaac Becroft vs Moerani Bouzige -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207728:208653:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isaac Becroft (`KXITFMATCH-26OCT28BECBOU-BEC`) | 0.60 / 0.65 (56) | 62.5% | 30.7% | 33.2% | 33.7% [32.3%-37.0%] | 62.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -31.8 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Moerani Bouzige (`KXITFMATCH-26OCT28BECBOU-BOU`) | 0.34 / 0.38 (101) | 36.0% | 69.3% | 66.8% | 66.3% [63.0%-67.7%] | 37.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +33.3 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1698.0, B 3261.0; serve-point win A 59.6%, B 36.4%; Elo A 1311.2, B 1424.3; model uncertainty 0.0235
* Form inputs: days since last match A 184, B 44; matches on record A 106, B 315; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28BECBOU-BOU  (YES = Moerani Bouzige)
Model: 69%
Kalshi: 36%
Gap: +33 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.009, surface_dev_loose -0.009, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matthew Dellavedova vs Lachlan Vickery -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202354:212956:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthew Dellavedova (`KXITFMATCH-26OCT28DELVIC-DEL`) | 0.93 / 0.95 (564) | 94.0% | 91.3% | 88.2% | 84.8% [84.1%-85.8%] | 90.7% | -- | 90.7% | KALSHI_LONE_OUTLIER | PASS | -2.7 pp | NORMAL | FRESH | F / POOR | ALL_AGREE | VERIFIED |
| Lachlan Vickery (`KXITFMATCH-26OCT28DELVIC-VIC`) | 0.06 / 0.07 (630) | 6.5% | 8.7% | 11.8% | 15.2% [14.2%-15.9%] | 9.3% | -- | 9.3% | KALSHI_LONE_OUTLIER | PASS | +2.2 pp | NORMAL | FRESH | F / POOR | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3884.0, B 133.0; serve-point win A 64.1%, B 46.4%; Elo A 1455.0, B 1158.7; model uncertainty 0.0088
* Form inputs: days since last match A 36, B 254; matches on record A 451, B 10; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.006, surface_dev_loose +0.004, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sam Ryan Ziegann vs Chase Ferguson -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207994:208160:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chase Ferguson (`KXITFMATCH-26OCT28RYAFER-FER`) | 0.64 / 0.69 (59) | 66.5% | 73.5% | 71.1% | 75.7% [74.5%-77.3%] | 67.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +7.0 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sam Ryan Ziegann (`KXITFMATCH-26OCT28RYAFER-RYA`) | 0.30 / 0.34 (254) | 32.0% | 26.5% | 28.9% | 24.3% [22.7%-25.5%] | 33.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.5 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1167.0, B 3171.0; serve-point win A 59.9%, B 35.1%; Elo A 1190.8, B 1420.1; model uncertainty 0.0142
* Form inputs: days since last match A 51, B 212; matches on record A 87, B 111; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose -0.008, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matias Soto vs Mauricio Schtulmann Gasca -- M15 Mazatlan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207130:214271:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mauricio Schtulmann Gasca (`KXITFMATCH-26OCT28SOTSCH-SCH`) | 0.03 / 0.04 (1373) | 3.5% | 15.9% | 23.8% | 21.1% [20.7%-21.9%] | -- | -- | -- | -- | PASS | +12.4 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matias Soto (`KXITFMATCH-26OCT28SOTSCH-SOT`) | 0.93 / 0.97 (1238) | 95.0% | 84.1% | 76.2% | 78.9% [78.1%-79.3%] | -- | -- | -- | -- | PASS | -10.9 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4186.0, B 64.0; serve-point win A 63.5%, B 44.2%; Elo A 1586.6, B 1360.7; model uncertainty 0.0061
* Form inputs: days since last match A 9, B 205; matches on record A 288, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tahlia Kokkinis vs Alana Subasic -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260667:261049:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tahlia Kokkinis (`KXITFWMATCH-26OCT28KOKSUB-KOK`) | 0.64 / 0.65 (1802) | 64.5% | 71.1% | 66.5% | 62.5% [57.9%-65.0%] | 72.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.6 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alana Subasic (`KXITFWMATCH-26OCT28KOKSUB-SUB`) | 0.35 / 0.36 (3007) | 35.5% | 28.9% | 33.6% | 37.5% [35.0%-42.1%] | 28.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -6.6 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1935.0, B 2964.0; serve-point win A 57.8%, B 46.4%; Elo A 1514.8, B 1463.4; model uncertainty 0.0352
* Form inputs: days since last match A 162, B 184; matches on record A 101, B 101; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Funa Kozaki vs Monique Barry -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216260:222667:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Monique Barry (`KXITFWMATCH-26OCT28KOZBAR-BAR`) | 0.50 / 0.63 (46) | 56.5% | 31.9% | 41.0% | 39.5% [36.4%-43.6%] | 59.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -24.6 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Funa Kozaki (`KXITFWMATCH-26OCT28KOZBAR-KOZ`) | 0.39 / 0.47 (3) | 43.0% | 68.1% | 59.0% | 60.5% [56.4%-63.6%] | 40.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +25.1 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 166.0, B 1840.0; serve-point win A 56.5%, B 47.1%; Elo A 1405.1, B 1331.5; model uncertainty 0.0361
* Form inputs: days since last match A 191, B 219; matches on record A 222, B 209; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28KOZBAR-KOZ  (YES = Funa Kozaki)
Model: 68%
Kalshi: 43%
Gap: +25 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.031, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eva Lopez vs Erika Sema -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:202454:270357:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eva Lopez (`KXITFWMATCH-26OCT28LOPSEM-LOP`) | 0.05 / 0.08 (61) | 6.5% | 15.5% | 13.0% | 22.1% [19.9%-22.9%] | 5.9% | -- | 5.9% | MODEL_LONE_OUTLIER | PASS | +9.0 pp | NORMAL | FRESH | F / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Erika Sema (`KXITFWMATCH-26OCT28LOPSEM-SEM`) | 0.93 / 0.95 (1) | 94.0% | 84.5% | 87.0% | 77.9% [77.1%-80.1%] | 94.1% | -- | 94.1% | MODEL_LONE_OUTLIER | PASS | -9.5 pp | NORMAL | FRESH | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 148.0, B 1873.0; serve-point win A 51.7%, B 40.6%; Elo A 1274.2, B 1485.0; model uncertainty 0.0148
* Form inputs: days since last match A 345, B 184; matches on record A 3, B 930; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose -0.007, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## I Wen Wan vs Yuno Kitahara -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:263881:267449:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuno Kitahara (`KXITFWMATCH-26OCT28WANKIT-KIT`) | 0.33 / 0.35 (10) | 34.0% | 79.6% | 78.2% | 72.3% [69.5%-75.7%] | 37.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +45.6 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| I Wen Wan (`KXITFWMATCH-26OCT28WANKIT-WAN`) | 0.64 / 0.68 (15) | 66.0% | 20.4% | 21.8% | 27.7% [24.3%-30.5%] | 62.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -45.6 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 553.0, B 2068.0; serve-point win A 49.0%, B 44.8%; Elo A 1276.4, B 1428.6; model uncertainty 0.0314
* Form inputs: days since last match A 240, B 191; matches on record A 26, B 119; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28WANKIT-KIT  (YES = Yuno Kitahara)
Model: 80%
Kalshi: 34%
Gap: +46 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.009, surface_dev_loose -0.004, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuki Bhambri / Ray Ho vs Thijmen Loof / Kaito Uesugi -- ATP Challenger Seoul QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 06:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-29T06:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28BHARAYLOOUES:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuki Bhambri / Ray Ho (`KXATPCHALLENGERDOUBLES-26OCT28BHARAYLOOUES-BHARAY`) | 0.06 / 0.95 (216) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Thijmen Loof / Kaito Uesugi (`KXATPCHALLENGERDOUBLES-26OCT28BHARAYLOOUES-LOOUES`) | 0.06 / 0.95 (216) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Alibek Kachmazov vs Seongchan Hong -- ATP Challenger Seoul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 06:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-29T06:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28KACHON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Seongchan Hong (`KXATPCHALLENGERMATCH-26OCT28KACHON-HON`) | 0.40 / 0.41 (64) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alibek Kachmazov (`KXATPCHALLENGERMATCH-26OCT28KACHON-KAC`) | 0.58 / 0.60 (9678) | 59.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Finn Reynolds / James Watt vs Alafia Ayeni / Andre Ilagan -- ATP Challenger Seoul QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 06:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-29T06:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28REYWATAVEILA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alafia Ayeni / Andre Ilagan (`KXATPCHALLENGERDOUBLES-26OCT28REYWATAVEILA-AVEILA`) | 0.06 / 0.94 (350) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Finn Reynolds / James Watt (`KXATPCHALLENGERDOUBLES-26OCT28REYWATAVEILA-REYWAT`) | 0.06 / 0.94 (850) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Fanny Stollar / Fang-Hsien Wu vs I-Hsuan Cho / Yi Tsen Cho -- WTA Guangzhou QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-29 08:00Z
* Current expected start: 2026-10-29 06:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: 2026-10-29 05:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29STOFANCHOCHO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I-Hsuan Cho / Yi Tsen Cho (`KXWTADOUBLES-26OCT29STOFANCHOCHO-CHOCHO`) | 0.35 / 0.39 (346) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fanny Stollar / Fang-Hsien Wu (`KXWTADOUBLES-26OCT29STOFANCHOCHO-STOFAN`) | 0.59 / 0.64 (752) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Maria Timofeeva vs Xinran Sun -- WTA Guangzhou R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-29 08:00Z
* Current expected start: 2026-10-29 06:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: 2026-10-29 05:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-90_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-29T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:221237:270082:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xinran Sun (`KXWTAMATCH-26OCT29TIMSUN-SUN`) | 0.36 / 0.37 (1497) | 36.5% | 28.6% | 61.1% | 43.1% [27.0%-54.8%] | 39.1% | -- | 39.1% | ALL_THREE_DISAGREE | WATCH | -7.9 pp | NORMAL | FRESH | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Maria Timofeeva (`KXWTAMATCH-26OCT29TIMSUN-TIM`) | 0.63 / 0.64 (30011) | 63.5% | 71.4% | 38.9% | 56.9% [45.2%-73.0%] | 60.9% | -- | 60.9% | ALL_THREE_DISAGREE | PASS | +7.9 pp | NORMAL | FRESH | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3737.0, B 1001.0; serve-point win A 55.3%, B 48.9%; Elo A 1821.3, B 1686.8; model uncertainty 0.1391
* Form inputs: days since last match A 2, B 1; matches on record A 361, B 26; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.042, surface_pool_high -0.042, surface_dev_loose -0.016, surface_dev_tight +0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT29TIMSUN-21` Over 20.5 games: 0.50/0.51 mid 50.5%, model 62.0% (projection_v2.0 (prediction ledger)) -- gap +11.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT29TIMSUN-26` Over 25.5 games: 0.26/0.40 mid 33.0%, model 39.3% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT29TIMSUN-16` Over 15.5 games: 0.84/0.95 mid 89.5%, model 95.3% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT29TIMSUN-2-SUN` Will Xinran Sun win set 2 in the Maria Timofeeva vs Xinran Sun match: 0.37/0.42 mid 39.5%, model 35.3% (projection_v2.0 (prediction ledger)) -- gap -4.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT29TIMSUN-2-TIM` Will Maria Timofeeva win set 2 in the Maria Timofeeva vs Xinran Sun match: 0.58/0.63 mid 60.5%, model 64.7% (projection_v2.0 (prediction ledger)) -- gap +4.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT29TIMSUN-1-SUN` Will Xinran Sun win set 1 in the Maria Timofeeva vs Xinran Sun match: 0.38/0.40 mid 39.0%, model 35.3% (projection_v2.0 (prediction ledger)) -- gap -3.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT29TIMSUN-1-TIM` Will Maria Timofeeva win set 1 in the Maria Timofeeva vs Xinran Sun match: 0.60/0.62 mid 61.0%, model 64.7% (projection_v2.0 (prediction ledger)) -- gap +3.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: LOW_DATA_QUALITY; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alvarez / LIU vs De Alba / Sau Franco -- M15 Mazatlan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28ALVLIUDEASAU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alvarez / LIU (`KXITFDOUBLES-26OCT28ALVLIUDEASAU-ALVLIU`) | 0.22 / 0.71 (1) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| De Alba / Sau Franco (`KXITFDOUBLES-26OCT28ALVLIUDEASAU-DEASAU`) | 0.14 / 0.78 (1) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Cooper / McKennon vs Flores / Quesada Perez -- M15 Mazatlan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28COOMCKFLOQUE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cooper / McKennon (`KXITFDOUBLES-26OCT28COOMCKFLOQUE-COOMCK`) | 0.37 / 0.75 (100) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Flores / Quesada Perez (`KXITFDOUBLES-26OCT28COOMCKFLOQUE-FLOQUE`) | 0.20 / 0.57 (58) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Lucca Cervantes Tomas / Alejandro Reyes Tirado vs Alujas / Salvestre -- M15 Mazatlan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28LUCALEALUSAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alujas / Salvestre (`KXITFDOUBLES-26OCT28LUCALEALUSAL-ALUSAL`) | 0.48 / 0.82 (138) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lucca Cervantes Tomas / Alejandro Reyes Tirado (`KXITFDOUBLES-26OCT28LUCALEALUSAL-LUCALE`) | 0.12 / 0.45 (45) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Markus Malaszszak vs Hugo Hashimoto -- M15 Yanagawa City R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212308:213074:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Hashimoto (`KXITFMATCH-26OCT28MALHAS-HAS`) | 0.77 / 0.78 (493) | 77.5% | 48.8% | 51.6% | 48.9% [48.9%-49.5%] | 74.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -28.7 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Markus Malaszszak (`KXITFMATCH-26OCT28MALHAS-MAL`) | 0.22 / 0.24 (138) | 23.0% | 51.2% | 48.4% | 51.0% [50.5%-51.1%] | 25.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +28.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1157.0, B 204.0; serve-point win A 57.5%, B 42.7%; Elo A 1255.9, B 1247.2; model uncertainty 0.0027
* Form inputs: days since last match A 184, B 212; matches on record A 40, B 5; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28MALHAS-MAL  (YES = Markus Malaszszak)
Model: 51%
Kalshi: 23%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hikaru Shiraishi vs Yu Tanaka -- M15 Yanagawa City R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202113:212092:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hikaru Shiraishi (`KXITFMATCH-26OCT28SHITAN-SHI`) | 0.59 / 0.63 (124) | 61.0% | 81.1% | 87.2% | 77.7% [73.3%-81.8%] | 60.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +20.1 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yu Tanaka (`KXITFMATCH-26OCT28SHITAN-TAN`) | 0.36 / 0.39 (332) | 37.5% | 18.9% | 12.8% | 22.3% [18.2%-26.7%] | 39.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -18.6 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2976.0, B 455.0; serve-point win A 63.2%, B 43.6%; Elo A 1438.1, B 1256.0; model uncertainty 0.0422
* Form inputs: days since last match A 44, B 485; matches on record A 210, B 10; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28SHITAN-SHI  (YES = Hikaru Shiraishi)
Model: 81%
Kalshi: 61%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.004, surface_dev_tight -0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kosuke Shibano vs Taiyo Yamanaka -- M15 Yanagawa City R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208277:213624:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kosuke Shibano (`KXITFMATCH-26OCT28SHIYAM-SHI`) | 0.17 / 0.20 (1067) | 18.5% | 33.4% | 28.8% | 35.3% [31.9%-37.8%] | 19.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +14.9 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Taiyo Yamanaka (`KXITFMATCH-26OCT28SHIYAM-YAM`) | 0.79 / 0.80 (125) | 79.5% | 66.6% | 71.2% | 64.7% [62.2%-68.0%] | 80.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.9 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 684.0, B 2208.0; serve-point win A 57.5%, B 39.2%; Elo A 1195.7, B 1281.4; model uncertainty 0.0291
* Form inputs: days since last match A 191, B 163; matches on record A 18, B 184; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.019, surface_dev_loose -0.014, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuta Tomida vs Yua Taka -- M15 Yanagawa City R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212196:212616:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yua Taka (`KXITFMATCH-26OCT28TOMTAK-TAK`) | 0.33 / 0.36 (356) | 34.5% | 36.1% | 30.8% | 43.7% [37.5%-49.0%] | 34.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.6 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuta Tomida (`KXITFMATCH-26OCT28TOMTAK-TOM`) | 0.64 / 0.65 (92) | 64.5% | 63.9% | 69.2% | 56.3% [51.0%-62.5%] | 65.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.6 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1470.0, B 485.0; serve-point win A 58.3%, B 44.4%; Elo A 1221.5, B 1205.9; model uncertainty 0.0571
* Form inputs: days since last match A 191, B 261; matches on record A 44, B 21; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose +0.021, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jumpei Yamasaki vs Noritaka Koizumi -- M15 Yanagawa City R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126135:212476:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Noritaka Koizumi (`KXITFMATCH-26OCT28YAMKOI-KOI`) | 0.27 / 0.29 (676) | 28.0% | 30.6% | 22.3% | 39.0% [33.8%-42.9%] | 29.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jumpei Yamasaki (`KXITFMATCH-26OCT28YAMKOI-YAM`) | 0.70 / 0.73 (193) | 71.5% | 69.4% | 77.7% | 61.0% [57.1%-66.2%] | 70.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1642.0, B 190.0; serve-point win A 64.1%, B 39.9%; Elo A 1349.8, B 1285.6; model uncertainty 0.0454
* Form inputs: days since last match A 184, B 212; matches on record A 360, B 8; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.019, surface_dev_loose +0.009, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Finn Bass / Scott Duncan vs Akira Santillan / Baoluo Zheng -- ATP Challenger Ningbo QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-29T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29BASDUNSANZHE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Finn Bass / Scott Duncan (`KXATPCHALLENGERDOUBLES-26OCT29BASDUNSANZHE-BASDUN`) | 0.06 / 0.68 (154) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Akira Santillan / Baoluo Zheng (`KXATPCHALLENGERDOUBLES-26OCT29BASDUNSANZHE-SANZHE`) | 0.32 / 0.95 (216) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Taisei Ichikawa / Yuta Shimizu vs Ognjen Milic / Mili Poljicak -- ATP Challenger Ningbo QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-29T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29ICHSHIMILPOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Taisei Ichikawa / Yuta Shimizu (`KXATPCHALLENGERDOUBLES-26OCT29ICHSHIMILPOL-ICHSHI`) | 0.06 / 0.95 (216) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ognjen Milic / Mili Poljicak (`KXATPCHALLENGERDOUBLES-26OCT29ICHSHIMILPOL-MILPOL`) | 0.06 / 0.95 (216) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Garcia / Carmen Zamburek vs Dominguez Garcia / Alessia Monteleone -- W50 Morelia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28GARCARDOMALE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dominguez Garcia / Alessia Monteleone (`KXITFWDOUBLES-26OCT28GARCARDOMALE-DOMALE`) | 0.05 / 0.06 (26) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Garcia / Carmen Zamburek (`KXITFWDOUBLES-26OCT28GARCARDOMALE-GARCAR`) | 0.87 / 0.96 (45) | 91.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Pruchya Isaro / Ji Sung Nam vs Jay Friend / Rei Sakamoto -- ATP Challenger Seoul QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-29T07:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29ISANAMHARSAK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jay Friend / Rei Sakamoto (`KXATPCHALLENGERDOUBLES-26OCT29ISANAMHARSAK-HARSAK`) | 0.06 / 0.95 (216) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pruchya Isaro / Ji Sung Nam (`KXATPCHALLENGERDOUBLES-26OCT29ISANAMHARSAK-ISANAM`) | 0.06 / 0.95 (216) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Dong Ju Kim / Uisung Park vs Blake Bayldon / Thomas Fancutt -- ATP Challenger Seoul QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-29T07:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29KIMPARBAYFAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Blake Bayldon / Thomas Fancutt (`KXATPCHALLENGERDOUBLES-26OCT29KIMPARBAYFAN-BAYFAN`) | 0.06 / 0.95 (216) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dong Ju Kim / Uisung Park (`KXATPCHALLENGERDOUBLES-26OCT29KIMPARBAYFAN-KIMPAR`) | 0.06 / 0.95 (216) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Hoole / Pham vs Dong / Leonard Sach -- M25 Tamworth QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28HOOPHADONLEO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dong / Leonard Sach (`KXITFDOUBLES-26OCT28HOOPHADONLEO-DONLEO`) | 0.37 / 0.78 (3) | 57.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hoole / Pham (`KXITFDOUBLES-26OCT28HOOPHADONLEO-HOOPHA`) | 0.16 / 0.64 (1) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Satara / Stevens vs Hoeyeraal / Padgham -- M25 Tamworth QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28SATSTEHOEPAD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hoeyeraal / Padgham (`KXITFDOUBLES-26OCT28SATSTEHOEPAD-HOEPAD`) | 0.65 / 0.80 (125) | 72.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Satara / Stevens (`KXITFDOUBLES-26OCT28SATSTEHOEPAD-SATSTE`) | 0.15 / 0.31 (36) | 23.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Yujia Huang vs Yushan Shao -- W35 Kunshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264207:269253:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yujia Huang (`KXITFWMATCH-26OCT28HUASHA-HUA`) | 0.70 / 0.73 (13) | 71.5% | 51.2% | 52.1% | 55.3% [54.2%-56.4%] | 70.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -20.3 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yushan Shao (`KXITFWMATCH-26OCT28HUASHA-SHA`) | 0.26 / 0.30 (36) | 28.0% | 48.8% | 47.9% | 44.7% [43.6%-45.8%] | 29.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +20.8 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1640.0, B 1123.0; serve-point win A 55.4%, B 44.9%; Elo A 1447.1, B 1398.2; model uncertainty 0.0106
* Form inputs: days since last match A 24, B 22; matches on record A 88, B 29; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28HUASHA-SHA  (YES = Yushan Shao)
Model: 49%
Kalshi: 28%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yufei Ren vs Yu Jun Lin -- W35 Kunshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260913:268787:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yu Jun Lin (`KXITFWMATCH-26OCT28RENLIN-LIN`) | 0.38 / 0.39 (1133) | 38.5% | 13.3% | 16.1% | 19.6% [17.8%-22.3%] | 38.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -25.2 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yufei Ren (`KXITFWMATCH-26OCT28RENLIN-REN`) | 0.59 / 0.60 (225) | 59.5% | 86.7% | 83.9% | 80.4% [77.7%-82.2%] | 61.5% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +27.2 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3240.0, B 515.0; serve-point win A 57.7%, B 50.6%; Elo A 1578.1, B 1346.6; model uncertainty 0.0223
* Form inputs: days since last match A 30, B 11; matches on record A 186, B 14; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28RENLIN-REN  (YES = Yufei Ren)
Model: 87%
Kalshi: 60%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.007, surface_dev_loose +0.011, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daria Zelinskaya vs Chengyiyi Yuan -- W35 Kunshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215134:239158:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chengyiyi Yuan (`KXITFWMATCH-26OCT28ZELYUA-YUA`) | 0.68 / 0.71 (14) | 69.5% | 42.3% | 37.6% | 41.2% [38.1%-47.4%] | 70.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -27.2 pp | EXTREME (DATA_WARNING) | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daria Zelinskaya (`KXITFWMATCH-26OCT28ZELYUA-ZEL`) | 0.29 / 0.31 (41) | 30.0% | 57.7% | 62.4% | 58.8% [52.6%-61.9%] | 29.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +27.7 pp | EXTREME (DATA_WARNING) | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2491.0, B 2947.0; serve-point win A 58.3%, B 43.1%; Elo A 1503.1, B 1478.6; model uncertainty 0.0461
* Form inputs: days since last match A 108, B 31; matches on record A 171, B 239; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28ZELYUA-ZEL  (YES = Daria Zelinskaya)
Model: 58%
Kalshi: 30%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Wushuang Zheng vs Daria KHOMUTSIANSKAYA -- W35 Kunshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213821:222944:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daria KHOMUTSIANSKAYA (`KXITFWMATCH-26OCT28ZHEKHO-KHO`) | 0.63 / 0.66 (369) | 64.5% | 77.7% | 98.7% | 93.1% [74.3%-96.8%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +13.2 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Wushuang Zheng (`KXITFWMATCH-26OCT28ZHEKHO-ZHE`) | 0.35 / 0.37 (359) | 36.0% | 22.3% | 1.3% | 6.9% [3.2%-25.7%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.7 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2161.0, B 3178.0; serve-point win A 52.2%, B 42.0%; Elo A 1552.0, B 1665.8; model uncertainty 0.1124
* Form inputs: days since last match A 22, B 282; matches on record A 302, B 171; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.002, surface_dev_loose -0.011, surface_dev_tight +0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elena Rybakina vs Yulia Putintseva -- WTA Tokyo R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-28 04:30Z
* Current expected start: 2026-10-29 08:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: 2026-10-29 07:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1650_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-28T04:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:201709:214981:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yulia Putintseva (`KXWTAMATCH-26OCT27RYBPUT-PUT`) | 0.13 / 0.14 (16600) | 13.5% | 12.2% | 10.6% | 10.8% [10.1%-12.0%] | -- | -- | -- | -- | PASS | -1.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elena Rybakina (`KXWTAMATCH-26OCT27RYBPUT-RYB`) | 0.86 / 0.87 (11415) | 86.5% | 87.8% | 89.4% | 89.2% [88.0%-89.9%] | -- | -- | -- | -- | SHADOW_BET | +1.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6087.0, B 4366.0; serve-point win A 64.8%, B 44.3%; Elo A 2251.3, B 1900.2; model uncertainty 0.0094
* Form inputs: days since last match A 3, B 1; matches on record A 593, B 862; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.007, surface_dev_loose +0.004, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT27RYBPUT-20` Over 19.5 games: 0.47/0.48 mid 47.5%, model 60.5% (projection_v2.0 (prediction ledger)) -- gap +13.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT27RYBPUT-15` Over 14.5 games: 0.88/0.95 mid 91.5%, model 97.9% (projection_v2.0 (prediction ledger)) -- gap +6.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT27RYBPUT-25` Over 24.5 games: 0.22/0.34 mid 28.0%, model 34.3% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT27RYBPUT-1-RYB` Will Elena Rybakina win set 1 in the Elena Rybakina vs Yulia Putintseva match: 0.81/0.83 mid 82.0%, model 78.2% (projection_v2.0 (prediction ledger)) -- gap -3.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT27RYBPUT-1-PUT` Will Yulia Putintseva win set 1 in the Elena Rybakina vs Yulia Putintseva match: 0.18/0.19 mid 18.5%, model 21.8% (projection_v2.0 (prediction ledger)) -- gap +3.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT27RYBPUT-2-PUT` Will Yulia Putintseva win set 2 in the Elena Rybakina vs Yulia Putintseva match: 0.17/0.22 mid 19.5%, model 21.8% (projection_v2.0 (prediction ledger)) -- gap +2.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT27RYBPUT-2-RYB` Will Elena Rybakina win set 2 in the Elena Rybakina vs Yulia Putintseva match: 0.78/0.83 mid 80.5%, model 78.2% (projection_v2.0 (prediction ledger)) -- gap -2.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Anna Bondar vs Kaitlin Quevedo -- WTA Guangzhou R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-28 08:00Z
* Current expected start: 2026-10-29 08:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: 2026-10-29 07:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1440_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-28T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214388:259733:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Bondar (`KXWTAMATCH-26OCT28BONQUE-BON`) | 0.53 / 0.54 (709) | 53.5% | 50.9% | 53.1% | 51.5% [49.5%-52.6%] | -- | -- | -- | -- | PASS | -2.6 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kaitlin Quevedo (`KXWTAMATCH-26OCT28BONQUE-QUE`) | 0.46 / 0.47 (15899) | 46.5% | 49.1% | 46.9% | 48.4% [47.4%-50.5%] | -- | -- | -- | -- | PASS | +2.6 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5196.0, B 3270.0; serve-point win A 59.4%, B 40.8%; Elo A 1746.7, B 1770.4; model uncertainty 0.0156
* Form inputs: days since last match A 2, B 1; matches on record A 724, B 229; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.021, surface_dev_loose -0.010, surface_dev_tight +0.010
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT28BONQUE-23` Over 22.5 games: 0.44/0.45 mid 44.5%, model 57.9% (projection_v2.0 (prediction ledger)) -- gap +13.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT28BONQUE-18` Over 17.5 games: 0.77/0.87 mid 82.0%, model 90.1% (projection_v2.0 (prediction ledger)) -- gap +8.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT28BONQUE-28` Over 27.5 games: 0.25/0.37 mid 31.0%, model 36.7% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT28BONQUE-1-BON` Will Anna Bondar win set 1 in the Anna Bondar vs Kaitlin Quevedo match: 0.53/0.56 mid 54.5%, model 50.6% (projection_v2.0 (prediction ledger)) -- gap -3.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT28BONQUE-1-QUE` Will Kaitlin Quevedo win set 1 in the Anna Bondar vs Kaitlin Quevedo match: 0.44/0.47 mid 45.5%, model 49.4% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT28BONQUE-2-BON` Will Anna Bondar win set 2 in the Anna Bondar vs Kaitlin Quevedo match: 0.51/0.57 mid 54.0%, model 50.6% (projection_v2.0 (prediction ledger)) -- gap -3.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT28BONQUE-2-QUE` Will Kaitlin Quevedo win set 2 in the Anna Bondar vs Kaitlin Quevedo match: 0.43/0.49 mid 46.0%, model 49.4% (projection_v2.0 (prediction ledger)) -- gap +3.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Polina Kudermetova / Maria Timofeeva vs Eri Hozumi / Andreja Klepac -- WTA Guangzhou QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-29 08:00Z
* Current expected start: 2026-10-29 08:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: 2026-10-29 07:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29KUDTIMHOZKLE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eri Hozumi / Andreja Klepac (`KXWTADOUBLES-26OCT29KUDTIMHOZKLE-HOZKLE`) | 0.58 / 0.61 (668) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Polina Kudermetova / Maria Timofeeva (`KXWTADOUBLES-26OCT29KUDTIMHOZKLE-KUDTIM`) | 0.39 / 0.41 (28) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Arevalo / Delgado vs Matta / Peck -- M15 Mazatlan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28AREDELMATPEC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arevalo / Delgado (`KXITFDOUBLES-26OCT28AREDELMATPEC-AREDEL`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matta / Peck (`KXITFDOUBLES-26OCT28AREDELMATPEC-MATPEC`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sora Fukuda vs Takuya Kumasaka -- M15 Yanagawa City R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126335:207998:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sora Fukuda (`KXITFMATCH-26OCT28FUKKUM-FUK`) | 0.34 / 0.37 (322) | 35.5% | 52.4% | 56.7% | 52.1% [49.0%-55.1%] | 36.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +16.9 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Takuya Kumasaka (`KXITFMATCH-26OCT28FUKKUM-KUM`) | 0.61 / 0.65 (114) | 63.0% | 47.6% | 43.3% | 47.9% [44.9%-51.0%] | 63.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.4 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1862.0, B 3065.0; serve-point win A 60.6%, B 39.9%; Elo A 1391.3, B 1411.9; model uncertainty 0.0308
* Form inputs: days since last match A 184, B 79; matches on record A 277, B 226; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28FUKKUM-FUK  (YES = Sora Fukuda)
Model: 52%
Kalshi: 36%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.031, surface_pool_high -0.031, surface_dev_loose +0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hyu Kawanishi vs Shinji Hazawa -- M15 Yanagawa City R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206923:213213:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shinji Hazawa (`KXITFMATCH-26OCT28KAW2HAZ2-HAZ2`) | 0.50 / 0.54 (175) | 52.0% | 65.8% | 59.6% | 57.6% [55.1%-59.6%] | 52.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.8 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hyu Kawanishi (`KXITFMATCH-26OCT28KAW2HAZ2-KAW2`) | 0.45 / 0.47 (158) | 46.0% | 34.2% | 40.4% | 42.4% [40.4%-44.9%] | 47.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.8 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 267.0, B 3455.0; serve-point win A 59.8%, B 37.0%; Elo A 1311.5, B 1358.1; model uncertainty 0.0224
* Form inputs: days since last match A 212, B 184; matches on record A 5, B 227; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.005, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ko Suzuki vs Yuto Oki -- M15 Yanagawa City R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:120545:212639:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuto Oki (`KXITFMATCH-26OCT28SUZOKI-OKI`) | 0.83 / 0.86 (878) | 84.5% | 75.8% | 75.1% | 67.1% [64.2%-69.9%] | 83.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ko Suzuki (`KXITFMATCH-26OCT28SUZOKI-SUZ`) | 0.14 / 0.16 (411) | 15.0% | 24.2% | 24.9% | 32.9% [30.1%-35.8%] | 17.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +9.2 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 489.0, B 1766.0; serve-point win A 56.3%, B 38.3%; Elo A 1174.4, B 1280.4; model uncertainty 0.0285
* Form inputs: days since last match A 338, B 212; matches on record A 136, B 42; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.028, surface_pool_high +0.024, surface_dev_loose -0.015, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Takahata / TANGE vs Cheng CHEN / Connel -- M15 Yanagawa City QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28TAKTANCHECON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cheng CHEN / Connel (`KXITFDOUBLES-26OCT28TAKTANCHECON-CHECON`) | 0.47 / 0.65 (3) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Takahata / TANGE (`KXITFDOUBLES-26OCT28TAKTANCHECON-TAKTAN`) | 0.29 / 0.46 (46) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Back / Yamazaki vs Liu / Uchijima -- W35 Sydney QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28BACYAMLIUUCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Back / Yamazaki (`KXITFWDOUBLES-26OCT28BACYAMLIUUCH-BACYAM`) | 0.70 / 0.91 (2) | 80.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Liu / Uchijima (`KXITFWDOUBLES-26OCT28BACYAMLIUUCH-LIUUCH`) | 0.05 / 0.24 (3) | 14.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Anchisa Chanta vs Arina Varaksina -- W15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223005:255662:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anchisa Chanta (`KXITFWMATCH-26OCT28CHAVAR-CHA`) | 0.72 / 0.76 (635) | 74.0% | 89.9% | 94.1% | 89.3% [86.9%-91.4%] | 72.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +15.9 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Arina Varaksina (`KXITFWMATCH-26OCT28CHAVAR-VAR`) | 0.25 / 0.28 (28) | 26.5% | 10.1% | 5.9% | 10.7% [8.6%-13.1%] | 27.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -16.4 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2474.0, B 586.0; serve-point win A 57.2%, B 52.4%; Elo A 1599.6, B 1277.4; model uncertainty 0.0223
* Form inputs: days since last match A 184, B 191; matches on record A 171, B 27; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28CHAVAR-CHA  (YES = Anchisa Chanta)
Model: 90%
Kalshi: 74%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.002, surface_pool_high -0.008, surface_dev_loose +0.005, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hosoki / Nishimoto vs Sato / Tse -- W35 Sydney QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28HOSNISSATTSE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hosoki / Nishimoto (`KXITFWDOUBLES-26OCT28HOSNISSATTSE-HOSNIS`) | 0.18 / 0.35 (38) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sato / Tse (`KXITFWDOUBLES-26OCT28HOSNISSATTSE-SATTSE`) | 0.58 / 0.76 (3) | 67.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Khan / McKenzie vs Chaudhari / Hoedt -- W35 Sydney QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28KHAMCKCHAHOE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chaudhari / Hoedt (`KXITFWDOUBLES-26OCT28KHAMCKCHAHOE-CHAHOE`) | 0.79 / 0.91 (2) | 85.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Khan / McKenzie (`KXITFWDOUBLES-26OCT28KHAMCKCHAHOE-KHAMCK`) | 0.05 / 0.16 (29) | 10.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alexandra Malova vs Aditi Rawat -- W15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28MALRAW:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandra Malova (`KXITFWMATCH-26OCT28MALRAW-MAL`) | 0.84 / 0.89 (3) | 86.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aditi Rawat (`KXITFWMATCH-26OCT28MALRAW-RAW`) | 0.10 / 0.13 (23) | 11.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jeong Moon vs Kamonwan Yodpetch -- W15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222213:259907:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jeong Moon (`KXITFWMATCH-26OCT28MOOYOD-MOO`) | 0.14 / 0.16 (772) | 15.0% | 29.0% | 42.6% | 43.1% [42.6%-44.1%] | 16.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +14.1 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kamonwan Yodpetch (`KXITFWMATCH-26OCT28MOOYOD-YOD`) | 0.84 / 0.88 (791) | 86.0% | 71.0% | 57.4% | 56.9% [55.9%-57.4%] | 83.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.1 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1191.0, B 1037.0; serve-point win A 51.0%, B 44.8%; Elo A 1280.5, B 1326.6; model uncertainty 0.008
* Form inputs: days since last match A 219, B 184; matches on record A 51, B 72; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aruzhan Sagandykova vs Violet Apisah -- W15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221802:270061:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Violet Apisah (`KXITFWMATCH-26OCT28SAGAPI-API`) | 0.66 / 0.67 (20) | 66.5% | 31.4% | 31.6% | 45.8% [43.7%-46.8%] | -- | -- | -- | -- | PASS | -35.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Aruzhan Sagandykova (`KXITFWMATCH-26OCT28SAGAPI-SAG`) | 0.33 / 0.34 (20) | 33.5% | 68.6% | 68.4% | 54.2% [53.2%-56.3%] | -- | -- | -- | -- | PASS | +35.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1744.0, B 122.0; serve-point win A 57.3%, B 46.3%; Elo A 1403.7, B 1379.7; model uncertainty 0.0157
* Form inputs: days since last match A 32, B 2820; matches on record A 45, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28SAGAPI-SAG  (YES = Aruzhan Sagandykova)
Model: 69%
Kalshi: 34%
Gap: +35 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Saily Prashantkumar Thakkar vs Nagi Hanatani -- W15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211544:263658:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nagi Hanatani (`KXITFWMATCH-26OCT28THAHAN-HAN`) | 0.87 / 0.90 (3646) | 88.5% | 83.8% | 48.9% | 65.6% [63.1%-71.3%] | 85.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Saily Prashantkumar Thakkar (`KXITFWMATCH-26OCT28THAHAN-THA`) | 0.10 / 0.11 (28) | 10.5% | 16.2% | 51.1% | 34.4% [28.7%-36.9%] | 14.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 301.0, B 1219.0; serve-point win A 48.8%, B 43.8%; Elo A 1183.5, B 1328.0; model uncertainty 0.0407
* Form inputs: days since last match A 184, B 184; matches on record A 11, B 446; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.029, surface_pool_high +0.020, surface_dev_loose -0.010, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Masamichi Imamura / Ryuki Matsuda vs Cheng-Peng Hsieh / Kaichi Uchida -- ATP Challenger Ningbo QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-29T08:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29IMAMATHSIUCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cheng-Peng Hsieh / Kaichi Uchida (`KXATPCHALLENGERDOUBLES-26OCT29IMAMATHSIUCH-HSIUCH`) | 0.05 / 0.95 (216) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Masamichi Imamura / Ryuki Matsuda (`KXATPCHALLENGERDOUBLES-26OCT29IMAMATHSIUCH-IMAMAT`) | 0.05 / 0.95 (216) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Becroft / Shepp vs Beale / Vujic -- M25 Tamworth QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28BECSHEBEAVUJ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Beale / Vujic (`KXITFDOUBLES-26OCT28BECSHEBEAVUJ-BEAVUJ`) | 0.11 / 0.50 (50) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Becroft / Shepp (`KXITFDOUBLES-26OCT28BECSHEBEAVUJ-BECSHE`) | 0.49 / 0.84 (1) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Meng Yi Chen vs Junhan Zhang -- W35 Kunshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221903:260694:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Meng Yi Chen (`KXITFWMATCH-26OCT28CHEZHA-CHE`) | 0.17 / 0.19 (9) | 18.0% | 42.0% | 42.1% | 46.3% [44.2%-48.4%] | 19.5% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +24.0 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Junhan Zhang (`KXITFWMATCH-26OCT28CHEZHA-ZHA`) | 0.81 / 0.83 (264) | 82.0% | 58.0% | 57.9% | 53.7% [51.6%-55.8%] | 80.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -24.0 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1394.0, B 2226.0; serve-point win A 56.2%, B 42.3%; Elo A 1382.4, B 1384.4; model uncertainty 0.0209
* Form inputs: days since last match A 233, B 30; matches on record A 162, B 95; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28CHEZHA-CHE  (YES = Meng Yi Chen)
Model: 42%
Kalshi: 18%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.011, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tiana Tian Deng vs Sijia Wei -- W35 Kunshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221096:260528:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tiana Tian Deng (`KXITFWMATCH-26OCT28DENWEI-DEN`) | 0.15 / 0.18 (28) | 16.5% | 6.6% | 17.9% | 10.5% [9.4%-12.3%] | 17.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sijia Wei (`KXITFWMATCH-26OCT28DENWEI-WEI`) | 0.78 / 0.85 (30) | 81.5% | 93.5% | 82.1% | 89.5% [87.7%-90.6%] | 82.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +11.9 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 853.0, B 2150.0; serve-point win A 48.4%, B 40.3%; Elo A 1288.7, B 1716.7; model uncertainty 0.0147
* Form inputs: days since last match A 114, B 23; matches on record A 41, B 308; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.005, surface_dev_loose -0.005, surface_dev_tight +0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Priska Madelyn Nugroho vs Yuhan Wang -- W35 Kunshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221187:264205:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Priska Madelyn Nugroho (`KXITFWMATCH-26OCT28NUGWAN-NUG`) | 0.52 / 0.55 (82) | 53.5% | 64.5% | 60.0% | 64.6% [63.1%-67.0%] | 56.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +11.0 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuhan Wang (`KXITFWMATCH-26OCT28NUGWAN-WAN`) | 0.44 / 0.46 (46) | 45.0% | 35.5% | 40.0% | 35.4% [33.0%-36.9%] | 43.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.5 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2457.0, B 1724.0; serve-point win A 56.0%, B 46.8%; Elo A 1567.2, B 1428.1; model uncertainty 0.0198
* Form inputs: days since last match A 212, B 27; matches on record A 235, B 44; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yidi Yang vs JiaYi Wang -- W35 Kunshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215820:265692:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| JiaYi Wang (`KXITFWMATCH-26OCT28YANWAN-WAN`) | 0.36 / 0.37 (7) | 36.5% | 41.1% | 59.0% | 50.5% [42.1%-54.8%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +4.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yidi Yang (`KXITFWMATCH-26OCT28YANWAN-YAN`) | 0.61 / 0.62 (65) | 61.5% | 58.9% | 41.0% | 49.5% [45.2%-57.9%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3495.0, B 2216.0; serve-point win A 55.4%, B 46.3%; Elo A 1589.5, B 1510.1; model uncertainty 0.0636
* Form inputs: days since last match A 24, B 29; matches on record A 317, B 72; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.011, surface_dev_loose -0.016, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Shaheed Alam vs Maxime Janvier -- M15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126125:207180:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shaheed Alam (`KXITFMATCH-26OCT28ALAJAN-ALA`) | 0.03 / 0.04 (177) | 3.5% | 8.2% | 14.2% | 11.6% [10.6%-12.6%] | -- | -- | -- | -- | PASS | +4.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maxime Janvier (`KXITFMATCH-26OCT28ALAJAN-JAN`) | 0.92 / 0.96 (63) | 94.0% | 91.8% | 85.8% | 88.4% [87.4%-89.4%] | -- | -- | -- | -- | PASS | -2.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 112.0, B 4068.0; serve-point win A 56.0%, B 33.1%; Elo A 1109.9, B 1467.8; model uncertainty 0.0099
* Form inputs: days since last match A 443, B 44; matches on record A 17, B 773; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kosuke Ogura vs Madhwin Kamath -- M15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202124:209979:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Madhwin Kamath (`KXITFMATCH-26OCT28OGUKAM-KAM`) | 0.18 / 0.20 (146) | 19.0% | 44.3% | 34.0% | 39.8% [35.4%-43.9%] | -- | -- | -- | -- | WATCH | +25.3 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kosuke Ogura (`KXITFMATCH-26OCT28OGUKAM-OGU`) | 0.73 / 0.83 (1) | 78.0% | 55.7% | 66.0% | 60.2% [56.1%-64.6%] | -- | -- | -- | -- | PASS | -22.3 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3125.0, B 843.0; serve-point win A 61.2%, B 40.0%; Elo A 1235.7, B 1186.8; model uncertainty 0.0421
* Form inputs: days since last match A 191, B 184; matches on record A 245, B 53; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28OGUKAM-KAM  (YES = Madhwin Kamath)
Model: 44%
Kalshi: 19%
Gap: +25 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.019, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lidia Podgorichani vs Yeri Hong -- W15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259946:270097:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yeri Hong (`KXITFWMATCH-26OCT28PODHON-HON`) | 0.65 / 0.69 (510) | 67.0% | 54.2% | 86.4% | 66.6% [63.6%-71.8%] | 65.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.8 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lidia Podgorichani (`KXITFWMATCH-26OCT28PODHON-POD`) | 0.32 / 0.33 (37) | 32.5% | 45.8% | 13.6% | 33.4% [28.2%-36.4%] | 34.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.2 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 317.0, B 172.0; serve-point win A 52.6%, B 46.6%; Elo A 1211.6, B 1309.3; model uncertainty 0.0409
* Form inputs: days since last match A 184, B 184; matches on record A 27, B 4; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stevens / Thompson vs Katsumi / Kozaki -- W35 Sydney QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28STETHOKATKOZ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katsumi / Kozaki (`KXITFWDOUBLES-26OCT28STETHOKATKOZ-KATKOZ`) | 0.35 / 0.53 (53) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stevens / Thompson (`KXITFWDOUBLES-26OCT28STETHOKATKOZ-STETHO`) | 0.41 / 0.59 (60) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Yingqun Sun vs Remika Ohashi -- W15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260957:264029:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Remika Ohashi (`KXITFWMATCH-26OCT28SUNOHA-OHA`) | 0.21 / 0.24 (36) | 22.5% | 34.1% | 26.6% | 41.0% [36.0%-45.8%] | 23.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +11.6 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yingqun Sun (`KXITFWMATCH-26OCT28SUNOHA-SUN`) | 0.75 / 0.79 (638) | 77.0% | 65.9% | 73.4% | 59.0% [54.2%-64.0%] | 76.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.1 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1826.0, B 421.0; serve-point win A 56.8%, B 46.3%; Elo A 1387.9, B 1357.0; model uncertainty 0.0488
* Form inputs: days since last match A 184, B 191; matches on record A 99, B 44; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sevil Yuldasheva vs Thasaporn Naklo -- W15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:219874:220597:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thasaporn Naklo (`KXITFWMATCH-26OCT28YULNAK-NAK`) | 0.85 / 0.87 (287) | 86.0% | 83.7% | 75.1% | 79.1% [77.6%-80.3%] | 83.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.3 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sevil Yuldasheva (`KXITFWMATCH-26OCT28YULNAK-YUL`) | 0.14 / 0.15 (29) | 14.5% | 16.3% | 24.9% | 20.9% [19.7%-22.4%] | 17.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +1.8 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 808.0, B 2173.0; serve-point win A 51.4%, B 41.2%; Elo A 1209.3, B 1456.9; model uncertainty 0.0133
* Form inputs: days since last match A 184, B 184; matches on record A 155, B 166; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.004, surface_dev_loose -0.007, surface_dev_tight +0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Fukuda / Okabe vs Hashimoto / Fu Wong -- M15 Yanagawa City QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29FUKOKAHASFUW:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fukuda / Okabe (`KXITFDOUBLES-26OCT29FUKOKAHASFUW-FUKOKA`) | 0.36 / 0.56 (56) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hashimoto / Fu Wong (`KXITFDOUBLES-26OCT29FUKOKAHASFUW-HASFUW`) | 0.38 / 0.58 (59) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Katayama / Tanaka vs Kawachi / Yamanaka -- M15 Yanagawa City QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29KATTANKAWYAM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katayama / Tanaka (`KXITFDOUBLES-26OCT29KATTANKAWYAM-KATTAN`) | 0.56 / 0.74 (96) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kawachi / Yamanaka (`KXITFDOUBLES-26OCT29KATTANKAWYAM-KAWYAM`) | 0.21 / 0.38 (40) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Komagata / Koyama vs Koizumi / Taka -- M15 Yanagawa City QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29KOMKOYKOITAK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Koizumi / Taka (`KXITFDOUBLES-26OCT29KOMKOYKOITAK-KOITAK`) | 0.26 / 0.47 (47) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Komagata / Koyama (`KXITFDOUBLES-26OCT29KOMKOYKOITAK-KOMKOY`) | 0.45 / 0.67 (75) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Dmitrii Burtsev vs Dmitry Bessonov -- M15 Fergana R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 10:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29BURBES:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dmitry Bessonov (`KXITFMATCH-26OCT29BURBES-BES`) | 0.73 / 0.75 (232) | 74.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dmitrii Burtsev (`KXITFMATCH-26OCT29BURBES-BUR`) | 0.24 / 0.26 (4) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuttana Charoenphon vs Ali Habib -- M15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 10:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207772:209921:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuttana Charoenphon (`KXITFMATCH-26OCT29CHAHAB-CHA`) | 0.40 / 0.43 (211) | 41.5% | 36.0% | 26.2% | 38.8% [32.0%-44.9%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.5 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ali Habib (`KXITFMATCH-26OCT29CHAHAB-HAB`) | 0.56 / 0.59 (95) | 57.5% | 64.0% | 73.8% | 61.2% [55.1%-68.0%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.5 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 488.0, B 1324.0; serve-point win A 58.1%, B 39.1%; Elo A 1181.0, B 1227.8; model uncertainty 0.0642
* Form inputs: days since last match A 184, B 184; matches on record A 78, B 94; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.020, surface_dev_loose -0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kirill Filaretov vs Amir Omarkhanov -- M15 Fergana R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 10:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212788:212877:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kirill Filaretov (`KXITFMATCH-26OCT29FILOMA-FIL`) | 0.25 / 0.26 (33) | 25.5% | 19.9% | 33.2% | 30.9% [30.4%-31.0%] | -- | -- | -- | -- | PASS | -5.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amir Omarkhanov (`KXITFMATCH-26OCT29FILOMA-OMA`) | 0.69 / 0.73 (2) | 71.0% | 80.1% | 66.8% | 69.1% [69.0%-69.6%] | -- | -- | -- | -- | PASS | +9.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 65.0, B 2497.0; serve-point win A 54.7%, B 38.9%; Elo A 1265.8, B 1405.3; model uncertainty 0.0029
* Form inputs: days since last match A 324, B 11; matches on record A 2, B 76; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## M Rifqi Fitriadi vs Kristjan Tamm -- M15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 10:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29FITTAM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M Rifqi Fitriadi (`KXITFMATCH-26OCT29FITTAM-FIT`) | 0.52 / 0.54 (9) | 53.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kristjan Tamm (`KXITFMATCH-26OCT29FITTAM-TAM`) | 0.44 / 0.47 (569) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Adhithya Ganesan vs Alexander Watanabe Eriksson -- M15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 10:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212258:213397:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adhithya Ganesan (`KXITFMATCH-26OCT29GANWAT-GAN`) | 0.87 / 0.90 (771) | 88.5% | 79.7% | 56.2% | 67.0% [66.0%-68.8%] | 86.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexander Watanabe Eriksson (`KXITFMATCH-26OCT29GANWAT-WAT`) | 0.10 / 0.12 (131) | 11.0% | 20.3% | 43.8% | 33.0% [31.2%-34.0%] | 13.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +9.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2730.0, B 103.0; serve-point win A 63.1%, B 43.3%; Elo A 1381.1, B 1250.3; model uncertainty 0.014
* Form inputs: days since last match A 296, B 457; matches on record A 95, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuichiro Inui vs Thantub Suksumrarn -- M15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 10:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144955:209171:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuichiro Inui (`KXITFMATCH-26OCT29INUSUK-INU`) | 0.19 / 0.21 (156) | 20.0% | 27.2% | 27.8% | 27.4% [25.8%-29.4%] | 21.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +7.2 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Thantub Suksumrarn (`KXITFMATCH-26OCT29INUSUK-SUK`) | 0.79 / 0.80 (158) | 79.5% | 72.8% | 72.2% | 72.6% [70.6%-74.2%] | 78.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.7 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1370.0, B 1818.0; serve-point win A 61.1%, B 34.1%; Elo A 1112.9, B 1281.6; model uncertainty 0.0178
* Form inputs: days since last match A 198, B 184; matches on record A 145, B 105; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.017, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maxim Shin vs Calvin Mueller -- M15 Fergana R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 10:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209166:210535:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Calvin Mueller (`KXITFMATCH-26OCT29SHIMUE-MUE`) | 0.80 / 0.81 (30) | 80.5% | 60.4% | 64.9% | 63.0% [61.6%-64.4%] | 76.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -20.1 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maxim Shin (`KXITFMATCH-26OCT29SHIMUE-SHI`) | 0.18 / 0.19 (1120) | 18.5% | 39.6% | 35.1% | 37.0% [35.6%-38.4%] | 23.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +21.1 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1523.0, B 1075.0; serve-point win A 60.4%, B 37.5%; Elo A 1229.1, B 1312.1; model uncertainty 0.014
* Form inputs: days since last match A 184, B 184; matches on record A 86, B 24; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT29SHIMUE-SHI  (YES = Maxim Shin)
Model: 40%
Kalshi: 18%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Digvijay Pratap Singh vs Muzammil Murtaza -- M15 Fergana R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 10:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29SINMUR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Muzammil Murtaza (`KXITFMATCH-26OCT29SINMUR-MUR`) | 0.06 / 0.07 (317) | 6.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Digvijay Pratap Singh (`KXITFMATCH-26OCT29SINMUR-SIN`) | 0.90 / 0.94 (1) | 92.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daisuke Sumizawa vs Seonyong Han -- M15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 10:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200671:213555:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Seonyong Han (`KXITFMATCH-26OCT29SUMHAN-HAN`) | 0.65 / 0.69 (424) | 67.0% | 32.8% | 53.1% | 38.4% [36.9%-40.9%] | -- | -- | -- | -- | PASS | -34.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daisuke Sumizawa (`KXITFMATCH-26OCT29SUMHAN-SUM`) | 0.31 / 0.34 (265) | 32.5% | 67.2% | 46.9% | 61.6% [59.1%-63.1%] | -- | -- | -- | -- | PASS | +34.7 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1327.0, B 346.0; serve-point win A 62.7%, B 40.8%; Elo A 1265.2, B 1158.5; model uncertainty 0.0197
* Form inputs: days since last match A 212, B 282; matches on record A 202, B 8; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT29SUMHAN-SUM  (YES = Daisuke Sumizawa)
Model: 67%
Kalshi: 32%
Gap: +35 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.005, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Li / Xi Wu vs Huang / Zelinskaya -- W35 Kunshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 10:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29LIXXIWHUAZEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Huang / Zelinskaya (`KXITFWDOUBLES-26OCT29LIXXIWHUAZEL-HUAZEL`) | 0.78 / 0.91 (2) | 84.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Li / Xi Wu (`KXITFWDOUBLES-26OCT29LIXXIWHUAZEL-LIXXIW`) | 0.06 / 0.15 (29) | 10.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Panshina / Zolotareva vs Jeong / Wang -- W35 Kunshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 10:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29PANZOLJEOWAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jeong / Wang (`KXITFWDOUBLES-26OCT29PANZOLJEOWAN-JEOWAN`) | 0.06 / 0.17 (30) | 11.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Panshina / Zolotareva (`KXITFWDOUBLES-26OCT29PANZOLJEOWAN-PANZOL`) | 0.78 / 0.91 (2) | 84.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Yusuke Kusuhara / Shunsuke Nakagawa vs Jake Delaney / Aoran Wang -- ATP Challenger Ningbo QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 10:50Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-29T10:50:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29KUSNAKDELWAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jake Delaney / Aoran Wang (`KXATPCHALLENGERDOUBLES-26OCT29KUSNAKDELWAN-DELWAN`) | 0.06 / 0.95 (216) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yusuke Kusuhara / Shunsuke Nakagawa (`KXATPCHALLENGERDOUBLES-26OCT29KUSNAKDELWAN-KUSNAK`) | 0.06 / 0.95 (216) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Valentin Vacherot vs Rafael Jodar -- ATP Basel R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-29 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-29 11:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: 2026-10-29 10:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (TOUR_500_250) · Hard · scheduled 2026-10-29T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200473:212588:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rafael Jodar (`KXATPMATCH-26OCT29VACJOD-JOD`) | 0.71 / 0.72 (2186) | 71.5% | 74.1% | 68.0% | 68.5% [67.6%-68.9%] | 71.8% | -- | 71.8% | MODEL_LONE_OUTLIER | PASS | +2.6 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Valentin Vacherot (`KXATPMATCH-26OCT29VACJOD-VAC`) | 0.28 / 0.29 (59236) | 28.5% | 25.9% | 32.0% | 31.5% [31.1%-32.4%] | 28.2% | -- | 28.2% | MODEL_LONE_OUTLIER | SHADOW_BET | -2.6 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4676.0, B 5268.0; serve-point win A 62.6%, B 32.2%; Elo A 1885.1, B 2026.1; model uncertainty 0.0065
* Form inputs: days since last match A 2, B 1; matches on record A 423, B 141; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.001, surface_dev_tight +0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT29VACJOD-JOD21` Will Rafael Jodar win the Valentin Vacherot vs Rafael Jodar match by a set score of 2-1?: 0.01/0.29 mid 15.0%, model 29.6% (projection_v2.0 (prediction ledger)) -- gap +14.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT29VACJOD-JOD7` Will Rafael Jodar win at least 6.5 more games than Valentin Vacherot?: 0.02/0.36 mid 19.0%, model 8.8% (projection_v2.0 (prediction ledger)) -- gap -10.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT29VACJOD-23` Over 22.5 games: 0.47/0.49 mid 48.0%, model 56.7% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT29VACJOD-28` Over 27.5 games: 0.31/0.34 mid 32.5%, model 37.1% (projection_v2.0 (prediction ledger)) -- gap +4.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29VACJOD-JOD20` Will Rafael Jodar win the Valentin Vacherot vs Rafael Jodar match by a set score of 2-0?: 0.47/0.51 mid 49.0%, model 44.5% (projection_v2.0 (prediction ledger)) -- gap -4.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT29VACJOD-JOD4` Will Rafael Jodar win at least 3.5 more games than Valentin Vacherot?: 0.50/0.51 mid 50.5%, model 46.3% (projection_v2.0 (prediction ledger)) -- gap -4.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29VACJOD-2-VAC` Will Valentin Vacherot win set 2 in the Valentin Vacherot vs Rafael Jodar match: 0.25/0.34 mid 29.5%, model 33.3% (projection_v2.0 (prediction ledger)) -- gap +3.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29VACJOD-VAC21` Will Valentin Vacherot win the Valentin Vacherot vs Rafael Jodar match by a set score of 2-1?: 0.07/0.15 mid 11.0%, model 14.8% (projection_v2.0 (prediction ledger)) -- gap +3.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT29VACJOD-18` Over 17.5 games: 0.86/0.91 mid 88.5%, model 92.3% (projection_v2.0 (prediction ledger)) -- gap +3.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT29VACJOD-VAC2` Will Valentin Vacherot win at least 1.5 more games than Rafael Jodar?: 0.20/0.24 mid 22.0%, model 19.9% (projection_v2.0 (prediction ledger)) -- gap -2.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29VACJOD-2-JOD` Will Rafael Jodar win set 2 in the Valentin Vacherot vs Rafael Jodar match: 0.60/0.70 mid 65.0%, model 66.7% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29VACJOD-VAC20` Will Valentin Vacherot win the Valentin Vacherot vs Rafael Jodar match by a set score of 2-0?: 0.09/0.15 mid 12.0%, model 11.1% (projection_v2.0 (prediction ledger)) -- gap -0.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29VACJOD-1-VAC` Will Valentin Vacherot win set 1 in the Valentin Vacherot vs Rafael Jodar match: 0.32/0.34 mid 33.0%, model 33.3% (projection_v2.0 (prediction ledger)) -- gap +0.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT29VACJOD-1-JOD` Will Rafael Jodar win set 1 in the Valentin Vacherot vs Rafael Jodar match: 0.66/0.67 mid 66.5%, model 66.7% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; WIDE_SPREAD

## Lilli Tagger vs Magda Linette -- WTA Guangzhou R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-29 08:00Z
* Current expected start: 2026-10-29 11:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: 2026-10-29 10:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+180_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-29T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202663:260172:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Magda Linette (`KXWTAMATCH-26OCT29TAGLIN-LIN`) | 0.29 / 0.30 (139) | 29.5% | 40.2% | 33.1% | 42.4% [38.4%-50.0%] | 30.9% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +10.7 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lilli Tagger (`KXWTAMATCH-26OCT29TAGLIN-TAG`) | 0.70 / 0.71 (6900) | 70.5% | 59.8% | 66.9% | 57.6% [50.0%-61.6%] | 69.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -10.7 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2552.0, B 4278.0; serve-point win A 61.8%, B 40.2%; Elo A 1812.1, B 1879.0; model uncertainty 0.0581
* Form inputs: days since last match A 1, B 1; matches on record A 133, B 912; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose -0.000, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT29TAGLIN-22` Over 21.5 games: 0.50/0.52 mid 51.0%, model 65.2% (projection_v2.0 (prediction ledger)) -- gap +14.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT29TAGLIN-1-LIN` Will Magda Linette win set 1 in the Lilli Tagger vs Magda Linette match: 0.33/0.36 mid 34.5%, model 43.5% (projection_v2.0 (prediction ledger)) -- gap +8.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT29TAGLIN-1-TAG` Will Lilli Tagger win set 1 in the Lilli Tagger vs Magda Linette match: 0.64/0.67 mid 65.5%, model 56.5% (projection_v2.0 (prediction ledger)) -- gap -8.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT29TAGLIN-27` Over 26.5 games: 0.27/0.40 mid 33.5%, model 41.6% (projection_v2.0 (prediction ledger)) -- gap +8.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT29TAGLIN-17` Over 16.5 games: 0.83/0.94 mid 88.5%, model 95.7% (projection_v2.0 (prediction ledger)) -- gap +7.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Edoardo Cherie Ligniere vs Jan Hrazdil -- M15 Fergana R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210754:212122:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Edoardo Cherie Ligniere (`KXITFMATCH-26OCT29CHEHRA-CHE`) | 0.62 / 0.63 (5) | 62.5% | 49.1% | 56.8% | 52.6% [52.1%-53.7%] | 64.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.4 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jan Hrazdil (`KXITFMATCH-26OCT29CHEHRA-HRA`) | 0.36 / 0.37 (76) | 36.5% | 50.9% | 43.2% | 47.4% [46.3%-47.9%] | 35.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +14.4 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 266.0, B 1017.0; serve-point win A 57.3%, B 42.6%; Elo A 1192.7, B 1177.9; model uncertainty 0.008
* Form inputs: days since last match A 184, B 219; matches on record A 17, B 72; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aryan Lakshmanan vs Aristarkh Safonov -- M15 Fergana R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210011:212767:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aryan Lakshmanan (`KXITFMATCH-26OCT29LAKSAF-LAK`) | 0.53 / 0.57 (93) | 55.0% | 34.3% | 42.5% | 34.3% [32.7%-35.3%] | -- | -- | -- | -- | PASS | -20.7 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aristarkh Safonov (`KXITFMATCH-26OCT29LAKSAF-SAF`) | 0.36 / 0.42 (44) | 39.0% | 65.7% | 57.5% | 65.7% [64.7%-67.3%] | -- | -- | -- | -- | PASS | +26.7 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 548.0, B 401.0; serve-point win A 61.4%, B 35.4%; Elo A 1145.6, B 1274.7; model uncertainty 0.013
* Form inputs: days since last match A 219, B 184; matches on record A 18, B 44; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT29LAKSAF-SAF  (YES = Aristarkh Safonov)
Model: 66%
Kalshi: 39%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kazuki Nakajima vs Pranav Karthik -- M15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29NAKKAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pranav Karthik (`KXITFMATCH-26OCT29NAKKAR-KAR`) | 0.75 / 0.76 (217) | 75.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kazuki Nakajima (`KXITFMATCH-26OCT29NAKKAR-NAK`) | 0.23 / 0.25 (7) | 24.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Grigory Shebekin vs Akhmadjon Toshmukhamedov -- M15 Fergana R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29SHETOS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Grigory Shebekin (`KXITFMATCH-26OCT29SHETOS-SHE`) | 0.86 / 0.95 (19) | 90.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Akhmadjon Toshmukhamedov (`KXITFMATCH-26OCT29SHETOS-TOS`) | 0.05 / 0.06 (26) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ashley Chua / En Tong Lim vs Kim / An Lin -- W15 Singapore QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29ASHENTKIMANL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ashley Chua / En Tong Lim (`KXITFWDOUBLES-26OCT29ASHENTKIMANL-ASHENT`) | 0.22 / 0.36 (10) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kim / An Lin (`KXITFWDOUBLES-26OCT29ASHENTKIMANL-KIMANL`) | 0.42 / 0.73 (1) | 57.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Im / Kim vs Guo / Yang -- W35 Kunshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29IMXKIMGUOYAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Guo / Yang (`KXITFWDOUBLES-26OCT29IMXKIMGUOYAN-GUOYAN`) | 0.26 / 0.48 (48) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Im / Kim (`KXITFWDOUBLES-26OCT29IMXKIMGUOYAN-IMXKIM`) | 0.47 / 0.67 (75) | 57.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Luo / Ren vs Madelyn Nugroho / Zheng -- W35 Kunshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29LUORENMADZHE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luo / Ren (`KXITFWDOUBLES-26OCT29LUORENMADZHE-LUOREN`) | 0.18 / 0.36 (39) | 27.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Madelyn Nugroho / Zheng (`KXITFWDOUBLES-26OCT29LUORENMADZHE-MADZHE`) | 0.60 / 0.77 (108) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Hanatani / Lu vs Apisah / Ning Chanya Ng -- W15 Singapore QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29HANLUXAPININ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Apisah / Ning Chanya Ng (`KXITFWDOUBLES-26OCT29HANLUXAPININ-APININ`) | 0.06 / 0.91 (2) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hanatani / Lu (`KXITFWDOUBLES-26OCT29HANLUXAPININ-HANLUX`) | 0.06 / 0.91 (2) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Malova / Varaksina vs Chanta / Naklo -- W15 Singapore QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29MALVARCHANAK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chanta / Naklo (`KXITFWDOUBLES-26OCT29MALVARCHANAK-CHANAK`) | 0.06 / 0.91 (2) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Malova / Varaksina (`KXITFWDOUBLES-26OCT29MALVARCHANAK-MALVAR`) | 0.06 / 0.91 (2) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Cameron Norrie vs Daniil Medvedev -- ATP Vienna R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-29 15:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-29 12:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: 2026-10-29 11:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (TOUR_500_250) · Clay · scheduled 2026-10-29T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:106421:111815:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniil Medvedev (`KXATPMATCH-26OCT29NORMED-MED`) | 0.81 / 0.82 (13) | 81.5% | 69.9% | 74.3% | 70.9% [68.6%-73.0%] | 80.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.6 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Cameron Norrie (`KXATPMATCH-26OCT29NORMED-NOR`) | 0.18 / 0.19 (39984) | 18.5% | 30.1% | 25.7% | 29.1% [27.0%-31.4%] | 19.1% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +11.6 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5400.0, B 6370.0; serve-point win A 59.4%, B 36.5%; Elo A 1887.6, B 1933.4; model uncertainty 0.0219
* Form inputs: days since last match A 1, B 3; matches on record A 678, B 875; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.018, surface_dev_loose +0.017, surface_dev_tight -0.012
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT29NORMED-MED20` Will Daniil Medvedev win the Cameron Norrie vs Daniil Medvedev match by a set score of 2-0?: 0.58/0.60 mid 59.0%, model 40.4% (projection_v2.0 (prediction ledger)) -- gap -18.6 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29NORMED-MED21` Will Daniil Medvedev win the Cameron Norrie vs Daniil Medvedev match by a set score of 2-1?: 0.01/0.28 mid 14.5%, model 29.4% (projection_v2.0 (prediction ledger)) -- gap +14.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT29NORMED-MED5` Will Daniil Medvedev win at least 4.5 more games than Cameron Norrie?: 0.46/0.47 mid 46.5%, model 32.7% (projection_v2.0 (prediction ledger)) -- gap -13.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT29NORMED-22` Over 21.5 games: 0.48/0.50 mid 49.0%, model 62.7% (projection_v2.0 (prediction ledger)) -- gap +13.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29NORMED-2-MED` Will Daniil Medvedev win set 2 in the Cameron Norrie vs Daniil Medvedev match: 0.02/0.98 mid 50.0%, model 63.6% (projection_v2.0 (prediction ledger)) -- gap +13.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT29NORMED-2-NOR` Will Cameron Norrie win set 2 in the Cameron Norrie vs Daniil Medvedev match: 0.02/0.98 mid 50.0%, model 36.4% (projection_v2.0 (prediction ledger)) -- gap -13.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT29NORMED-MED2` Will Daniil Medvedev win at least 1.5 more games than Cameron Norrie?: 0.74/0.80 mid 77.0%, model 63.4% (projection_v2.0 (prediction ledger)) -- gap -13.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT29NORMED-MED8` Will Daniil Medvedev win at least 7.5 more games than Cameron Norrie?: 0.03/0.32 mid 17.5%, model 4.9% (projection_v2.0 (prediction ledger)) -- gap -12.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29NORMED-1-MED` Will Daniil Medvedev win set 1 in the Cameron Norrie vs Daniil Medvedev match: 0.74/0.76 mid 75.0%, model 63.6% (projection_v2.0 (prediction ledger)) -- gap -11.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT29NORMED-1-NOR` Will Cameron Norrie win set 1 in the Cameron Norrie vs Daniil Medvedev match: 0.24/0.26 mid 25.0%, model 36.4% (projection_v2.0 (prediction ledger)) -- gap +11.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT29NORMED-27` Over 26.5 games: 0.27/0.31 mid 29.0%, model 39.4% (projection_v2.0 (prediction ledger)) -- gap +10.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29NORMED-NOR20` Will Cameron Norrie win the Cameron Norrie vs Daniil Medvedev match by a set score of 2-0?: 0.02/0.09 mid 5.5%, model 13.3% (projection_v2.0 (prediction ledger)) -- gap +7.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29NORMED-NOR21` Will Cameron Norrie win the Cameron Norrie vs Daniil Medvedev match by a set score of 2-1?: 0.06/0.38 mid 22.0%, model 16.9% (projection_v2.0 (prediction ledger)) -- gap -5.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT29NORMED-17` Over 16.5 games: 0.89/0.93 mid 91.0%, model 95.0% (projection_v2.0 (prediction ledger)) -- gap +4.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tommy Paul vs Luciano Darderi -- ATP Vienna R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-29 15:00Z
* Current expected start: 2026-10-29 12:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: 2026-10-29 11:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-150_MIN

ATP (TOUR_500_250) · Clay · scheduled 2026-10-29T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126205:209260:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luciano Darderi (`KXATPMATCH-26OCT29PAUDAR-DAR`) | 0.21 / 0.22 (1482) | 21.5% | 42.7% | 40.0% | 41.5% [38.6%-44.5%] | 21.4% | -- | 21.4% | MODEL_LONE_OUTLIER | WATCH | +21.2 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Tommy Paul (`KXATPMATCH-26OCT29PAUDAR-PAU`) | 0.78 / 0.79 (5232) | 78.5% | 57.3% | 60.0% | 58.5% [55.5%-61.4%] | 78.6% | -- | 78.6% | MODEL_LONE_OUTLIER | PASS | -21.2 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 6095.0, B 6361.0; serve-point win A 63.5%, B 38.0%; Elo A 2000.7, B 1994.2; model uncertainty 0.0295
* Form inputs: days since last match A 1, B 2; matches on record A 730, B 438; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT29PAUDAR-DAR  (YES = Luciano Darderi)
Model: 43%
Kalshi: 22%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: EXTERNAL_MARKET_REJECTION, UNKNOWN
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.029, surface_pool_high -0.030, surface_dev_loose -0.020, surface_dev_tight +0.019
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT29PAUDAR-PAU5` Will Tommy Paul win at least 4.5 more games than Luciano Darderi?: 0.47/0.48 mid 47.5%, model 21.7% (projection_v2.0 (prediction ledger)) -- gap -25.8 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT29PAUDAR-PAU2` Will Tommy Paul win at least 1.5 more games than Luciano Darderi?: 0.72/0.79 mid 75.5%, model 50.0% (projection_v2.0 (prediction ledger)) -- gap -25.5 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29PAUDAR-1-DAR` Will Luciano Darderi win set 1 in the Tommy Paul vs Luciano Darderi match: 0.26/0.27 mid 26.5%, model 45.1% (projection_v2.0 (prediction ledger)) -- gap +18.6 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT29PAUDAR-1-PAU` Will Tommy Paul win set 1 in the Tommy Paul vs Luciano Darderi match: 0.72/0.74 mid 73.0%, model 54.9% (projection_v2.0 (prediction ledger)) -- gap -18.1 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT29PAUDAR-22` Over 21.5 games: 0.50/0.52 mid 51.0%, model 67.8% (projection_v2.0 (prediction ledger)) -- gap +16.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29PAUDAR-PAU20` Will Tommy Paul win the Tommy Paul vs Luciano Darderi match by a set score of 2-0?: 0.26/0.62 mid 44.0%, model 30.1% (projection_v2.0 (prediction ledger)) -- gap -13.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT29PAUDAR-27` Over 26.5 games: 0.28/0.33 mid 30.5%, model 43.4% (projection_v2.0 (prediction ledger)) -- gap +12.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT29PAUDAR-PAU8` Will Tommy Paul win at least 7.5 more games than Luciano Darderi?: 0.01/0.29 mid 15.0%, model 2.4% (projection_v2.0 (prediction ledger)) -- gap -12.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29PAUDAR-PAU21` Will Tommy Paul win the Tommy Paul vs Luciano Darderi match by a set score of 2-1?: 0.09/0.27 mid 18.0%, model 27.2% (projection_v2.0 (prediction ledger)) -- gap +9.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29PAUDAR-DAR21` Will Luciano Darderi win the Tommy Paul vs Luciano Darderi match by a set score of 2-1?: 0.02/0.59 mid 30.5%, model 22.4% (projection_v2.0 (prediction ledger)) -- gap -8.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29PAUDAR-2-DAR` Will Luciano Darderi win set 2 in the Tommy Paul vs Luciano Darderi match: 0.02/0.98 mid 50.0%, model 45.1% (projection_v2.0 (prediction ledger)) -- gap -4.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT29PAUDAR-2-PAU` Will Tommy Paul win set 2 in the Tommy Paul vs Luciano Darderi match: 0.02/0.98 mid 50.0%, model 54.9% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT29PAUDAR-17` Over 16.5 games: 0.91/0.95 mid 93.0%, model 96.9% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29PAUDAR-DAR20` Will Luciano Darderi win the Tommy Paul vs Luciano Darderi match by a set score of 2-0?: 0.02/0.41 mid 21.5%, model 20.4% (projection_v2.0 (prediction ledger)) -- gap -1.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sagandykova / Yodpetch vs Nie / Zhou -- W15 Singapore QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29SAGYODNIEZHO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nie / Zhou (`KXITFWDOUBLES-26OCT29SAGYODNIEZHO-NIEZHO`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sagandykova / Yodpetch (`KXITFWDOUBLES-26OCT29SAGYODNIEZHO-SAGYOD`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alex Michelsen vs Arthur Fils -- ATP Basel R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-29 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-29 13:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: 2026-10-29 12:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (TOUR_500_250) · Hard · scheduled 2026-10-29T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:209950:210506:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arthur Fils (`KXATPMATCH-26OCT29MICFIL-FIL`) | 0.66 / 0.67 (41563) | 66.5% | 58.9% | 58.7% | 59.2% [56.3%-63.0%] | 65.8% | -- | 65.8% | MARKETS_AGREE | PASS | -7.6 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Alex Michelsen (`KXATPMATCH-26OCT29MICFIL-MIC`) | 0.34 / 0.35 (37005) | 34.5% | 41.1% | 41.3% | 40.8% [37.0%-43.7%] | 34.2% | -- | 34.2% | MARKETS_AGREE | SHADOW_BET | +6.6 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5733.0, B 4398.0; serve-point win A 64.7%, B 33.5%; Elo A 1961.6, B 2040.3; model uncertainty 0.0333
* Form inputs: days since last match A 1, B 1; matches on record A 317, B 336; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.028, surface_pool_high +0.029, surface_dev_loose +0.000, surface_dev_tight -0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT29MICFIL-FIL21` Will Arthur Fils win the Alex Michelsen vs Arthur Fils match by a set score of 2-1?: 0.02/0.28 mid 15.0%, model 27.6% (projection_v2.0 (prediction ledger)) -- gap +12.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29MICFIL-2-MIC` Will Alex Michelsen win set 2 in the Alex Michelsen vs Arthur Fils match: 0.16/0.49 mid 32.5%, model 44.0% (projection_v2.0 (prediction ledger)) -- gap +11.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT29MICFIL-23` Over 22.5 games: 0.51/0.52 mid 51.5%, model 62.7% (projection_v2.0 (prediction ledger)) -- gap +11.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29MICFIL-MIC21` Will Alex Michelsen win the Alex Michelsen vs Arthur Fils match by a set score of 2-1?: 0.02/0.20 mid 11.0%, model 21.7% (projection_v2.0 (prediction ledger)) -- gap +10.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT29MICFIL-FIL3` Will Arthur Fils win at least 2.5 more games than Alex Michelsen?: 0.52/0.54 mid 53.0%, model 42.8% (projection_v2.0 (prediction ledger)) -- gap -10.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT29MICFIL-FIL6` Will Arthur Fils win at least 5.5 more games than Alex Michelsen?: 0.10/0.24 mid 17.0%, model 9.7% (projection_v2.0 (prediction ledger)) -- gap -7.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29MICFIL-MIC20` Will Alex Michelsen win the Alex Michelsen vs Arthur Fils match by a set score of 2-0?: 0.01/0.24 mid 12.5%, model 19.4% (projection_v2.0 (prediction ledger)) -- gap +6.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29MICFIL-FIL20` Will Arthur Fils win the Alex Michelsen vs Arthur Fils match by a set score of 2-0?: 0.02/0.48 mid 25.0%, model 31.4% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29MICFIL-1-FIL` Will Arthur Fils win set 1 in the Alex Michelsen vs Arthur Fils match: 0.60/0.63 mid 61.5%, model 56.0% (projection_v2.0 (prediction ledger)) -- gap -5.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT29MICFIL-1-MIC` Will Alex Michelsen win set 1 in the Alex Michelsen vs Arthur Fils match: 0.37/0.40 mid 38.5%, model 44.0% (projection_v2.0 (prediction ledger)) -- gap +5.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT29MICFIL-18` Over 17.5 games: 0.85/0.94 mid 89.5%, model 94.9% (projection_v2.0 (prediction ledger)) -- gap +5.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT29MICFIL-28` Over 27.5 games: 0.31/0.43 mid 37.0%, model 42.2% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29MICFIL-2-FIL` Will Arthur Fils win set 2 in the Alex Michelsen vs Arthur Fils match: 0.44/0.78 mid 61.0%, model 56.0% (projection_v2.0 (prediction ledger)) -- gap -5.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT29MICFIL-MIC2` Will Alex Michelsen win at least 1.5 more games than Arthur Fils?: 0.22/0.36 mid 29.0%, model 33.5% (projection_v2.0 (prediction ledger)) -- gap +4.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Gijs Brouwer vs Koray Kirci -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:133835:134405:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gijs Brouwer (`KXITFMATCH-26OCT29BROKIR-BRO`) | 0.68 / 0.77 (100) | 72.5% | 86.2% | 73.1% | 83.4% [79.1%-88.5%] | -- | -- | -- | -- | PASS | +13.7 pp | REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Koray Kirci (`KXITFMATCH-26OCT29BROKIR-KIR`) | 0.18 / 0.25 (33) | 21.5% | 13.8% | 26.9% | 16.7% [11.5%-20.8%] | -- | -- | -- | -- | PASS | -7.7 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1950.0, B 736.0; serve-point win A 62.4%, B 45.9%; Elo A 1610.4, B 1278.1; model uncertainty 0.0467
* Form inputs: days since last match A 51, B 93; matches on record A 513, B 242; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.030, surface_pool_high -0.042, surface_dev_loose +0.000, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Francisco Cabral / James Tracy vs Henry Bernet / Dominic Stricker -- ATP Basel QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-29T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29CABTRABERSTR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Henry Bernet / Dominic Stricker (`KXATPDOUBLES-26OCT29CABTRABERSTR-BERSTR`) | 0.25 / 0.26 (402) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Francisco Cabral / James Tracy (`KXATPDOUBLES-26OCT29CABTRABERSTR-CABTRA`) | 0.74 / 0.75 (341) | 74.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Yurii Dzhavakian vs Niklas Waldner -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:122113:209118:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yurii Dzhavakian (`KXITFMATCH-26OCT29DZHWAL-DZH`) | 0.49 / 0.70 (83) | 59.5% | 71.4% | 74.4% | 76.8% [75.2%-78.8%] | -- | -- | -- | -- | PASS | +11.9 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Niklas Waldner (`KXITFMATCH-26OCT29DZHWAL-WAL`) | 0.26 / 0.45 (45) | 35.5% | 28.6% | 25.7% | 23.2% [21.2%-24.8%] | -- | -- | -- | -- | PASS | -6.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5142.0, B 1299.0; serve-point win A 63.1%, B 41.3%; Elo A 1383.3, B 1149.0; model uncertainty 0.018
* Form inputs: days since last match A 184, B 102; matches on record A 436, B 71; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.012, surface_dev_loose +0.011, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Michel Hopp vs Alexander Vasilev -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210424:211651:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michel Hopp (`KXITFMATCH-26OCT29HOPVAS-HOP`) | 0.36 / 0.40 (26) | 38.0% | 42.0% | 58.5% | 52.1% [47.4%-55.3%] | 40.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +4.0 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexander Vasilev (`KXITFMATCH-26OCT29HOPVAS-VAS`) | 0.57 / 0.62 (43) | 59.5% | 58.0% | 41.5% | 47.9% [44.7%-52.6%] | 59.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.5 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2320.0, B 1101.0; serve-point win A 53.8%, B 44.7%; Elo A 1346.6, B 1369.1; model uncertainty 0.0398
* Form inputs: days since last match A 198, B 37; matches on record A 83, B 44; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.011, surface_dev_loose -0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Karim Ibrahim vs Amr Elsayed -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209871:210456:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amr Elsayed (`KXITFMATCH-26OCT29IBRELS-ELS`) | 0.63 / 0.76 (100) | 69.5% | 71.8% | 83.1% | 79.2% [72.2%-81.8%] | -- | -- | -- | -- | PASS | +2.3 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Karim Ibrahim (`KXITFMATCH-26OCT29IBRELS-IBR`) | 0.20 / 0.36 (9) | 28.0% | 28.2% | 16.9% | 20.8% [18.2%-27.8%] | -- | -- | -- | -- | PASS | +0.2 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 2455.0, B 3030.0; serve-point win A 62.9%, B 32.5%; Elo A 1227.6, B 1388.9; model uncertainty 0.048
* Form inputs: days since last match A 184, B 40; matches on record A 90, B 252; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.009, surface_dev_tight +0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kevin Krawietz / Tim Putz vs Marc Polmans / Jan Zielinski -- ATP Basel QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-29T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29KRAPUTPOLZIE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kevin Krawietz / Tim Putz (`KXATPDOUBLES-26OCT29KRAPUTPOLZIE-KRAPUT`) | 0.25 / 0.70 (1283) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marc Polmans / Jan Zielinski (`KXATPDOUBLES-26OCT29KRAPUTPOLZIE-POLZIE`) | 0.25 / 0.70 (1283) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Valentin Lapalu vs Alexander Chang -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209516:212959:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Chang (`KXITFMATCH-26OCT29LAPCHA-CHA`) | 0.63 / 0.83 (147) | 73.0% | 56.3% | 64.8% | 56.5% [53.6%-59.9%] | -- | -- | -- | -- | PASS | -16.7 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valentin Lapalu (`KXITFMATCH-26OCT29LAPCHA-LAP`) | 0.10 / 0.30 (35) | 20.0% | 43.7% | 35.2% | 43.5% [40.1%-46.4%] | -- | -- | -- | -- | PASS | +23.7 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 790.0, B 562.0; serve-point win A 62.2%, B 36.5%; Elo A 1230.5, B 1253.8; model uncertainty 0.0316
* Form inputs: days since last match A 205, B 422; matches on record A 63, B 10; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT29LAPCHA-LAP  (YES = Valentin Lapalu)
Model: 44%
Kalshi: 20%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.000, surface_dev_loose +0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Thando Longwe-Smit vs Ioannis Xilas -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207927:209354:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thando Longwe-Smit (`KXITFMATCH-26OCT29LONXIL-LON`) | 0.08 / 0.13 (152) | 10.5% | 14.7% | 10.9% | 13.0% [11.7%-15.0%] | 12.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.2 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ioannis Xilas (`KXITFMATCH-26OCT29LONXIL-XIL`) | 0.85 / 0.91 (330) | 88.0% | 85.3% | 89.1% | 87.0% [85.0%-88.3%] | 87.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.7 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1098.0, B 2979.0; serve-point win A 53.8%, B 38.2%; Elo A 1208.1, B 1508.4; model uncertainty 0.017
* Form inputs: days since last match A 38, B 107; matches on record A 38, B 147; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.006, surface_dev_loose -0.006, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Javier Munoz Fuster vs Benjamin Pietri -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202125:214499:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Javier Munoz Fuster (`KXITFMATCH-26OCT29MUNPIE-MUN`) | 0.04 / 0.06 (206) | 5.0% | 32.4% | 20.7% | 45.9% [42.8%-47.9%] | -- | -- | -- | -- | PASS | +27.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Benjamin Pietri (`KXITFMATCH-26OCT29MUNPIE-PIE`) | 0.89 / 0.97 (543) | 93.0% | 67.6% | 79.3% | 54.1% [52.1%-57.2%] | -- | -- | -- | -- | PASS | -25.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 43.0, B 1540.0; serve-point win A 57.6%, B 38.9%; Elo A 1266.4, B 1291.0; model uncertainty 0.0257
* Form inputs: days since last match A 219, B 51; matches on record A 1, B 233; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT29MUNPIE-MUN  (YES = Javier Munoz Fuster)
Model: 32%
Kalshi: 5%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.021, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniel Verbeek vs Jannik Maute -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210339:211490:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jannik Maute (`KXITFMATCH-26OCT29VERMAU-MAU`) | 0.53 / 0.62 (115) | 57.5% | 45.0% | 56.8% | 50.5% [50.0%-51.6%] | -- | -- | -- | -- | PASS | -12.5 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daniel Verbeek (`KXITFMATCH-26OCT29VERMAU-VER`) | 0.38 / 0.41 (100) | 39.5% | 55.0% | 43.2% | 49.5% [48.4%-50.0%] | -- | -- | -- | -- | PASS | +15.5 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 790.0, B 181.0; serve-point win A 57.2%, B 43.7%; Elo A 1135.5, B 1138.3; model uncertainty 0.0079
* Form inputs: days since last match A 184, B 198; matches on record A 28, B 29; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT29VERMAU-VER  (YES = Daniel Verbeek)
Model: 55%
Kalshi: 40%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.011, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eva Bennemann vs Daria Egorova -- W50 Istanbul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:266622:266864:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eva Bennemann (`KXITFWMATCH-26OCT29BENEGO-BEN`) | 0.35 / 0.36 (321) | 35.5% | 46.9% | 39.9% | 41.5% [39.9%-44.1%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +11.4 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daria Egorova (`KXITFWMATCH-26OCT29BENEGO-EGO`) | 0.60 / 0.65 (21) | 62.5% | 53.1% | 60.1% | 58.5% [55.9%-60.1%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2212.0, B 2142.0; serve-point win A 51.1%, B 48.3%; Elo A 1632.8, B 1672.8; model uncertainty 0.0211
* Form inputs: days since last match A 15, B 29; matches on record A 67, B 86; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rikke De Koning vs Anja Wildgruber -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222668:252584:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rikke De Koning (`KXITFWMATCH-26OCT29DEKWIL-DEK`) | 0.57 / 0.73 (1) | 65.0% | 59.1% | 58.5% | 50.0% [45.2%-54.8%] | -- | -- | -- | -- | PASS | -5.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anja Wildgruber (`KXITFWMATCH-26OCT29DEKWIL-WIL`) | 0.29 / 0.33 (37) | 31.0% | 40.9% | 41.5% | 50.0% [45.2%-54.8%] | -- | -- | -- | -- | WATCH | +9.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1253.0, B 2380.0; serve-point win A 53.2%, B 48.5%; Elo A 1256.5, B 1305.7; model uncertainty 0.0481
* Form inputs: days since last match A 184, B 184; matches on record A 139, B 348; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.048, surface_pool_high -0.048, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anastasia Efremova vs Kristina Dmitruk -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220808:267540:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kristina Dmitruk (`KXITFWMATCH-26OCT29EFRDMI-DMI`) | 0.83 / 0.97 (279) | 90.0% | 93.2% | 84.8% | 86.0% [84.2%-88.3%] | -- | -- | -- | -- | PASS | +3.2 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anastasia Efremova (`KXITFWMATCH-26OCT29EFRDMI-EFR`) | 0.03 / 0.12 (19) | 7.5% | 6.8% | 15.2% | 14.0% [11.7%-15.8%] | -- | -- | -- | -- | PASS | -0.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 611.0, B 1766.0; serve-point win A 47.7%, B 41.1%; Elo A 1345.5, B 1675.9; model uncertainty 0.0204
* Form inputs: days since last match A 198, B 282; matches on record A 14, B 214; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.022, surface_pool_high +0.018, surface_dev_loose -0.009, surface_dev_tight +0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maria Golovina vs Dunja Maric -- W50 Istanbul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260017:261015:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Golovina (`KXITFWMATCH-26OCT29GOLMAR-GOL`) | 0.55 / 0.59 (49) | 57.0% | 61.4% | 74.8% | 67.0% [59.5%-71.3%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +4.4 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dunja Maric (`KXITFWMATCH-26OCT29GOLMAR-MAR`) | 0.37 / 0.44 (100) | 40.5% | 38.6% | 25.2% | 33.0% [28.7%-40.5%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2344.0, B 1430.0; serve-point win A 55.2%, B 47.0%; Elo A 1551.0, B 1483.0; model uncertainty 0.0588
* Form inputs: days since last match A 184, B 184; matches on record A 97, B 108; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Karla Popovic vs Kamilla Bartone -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:210500:221886:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kamilla Bartone (`KXITFWMATCH-26OCT29POPBAR-BAR`) | 0.54 / 0.63 (4) | 58.5% | 52.9% | 23.5% | 43.1% [33.0%-58.5%] | -- | -- | -- | -- | PASS | -5.6 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Karla Popovic (`KXITFWMATCH-26OCT29POPBAR-POP`) | 0.35 / 0.36 (39) | 35.5% | 47.1% | 76.5% | 56.9% [41.5%-67.0%] | -- | -- | -- | -- | WATCH | +11.6 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1204.0, B 1376.0; serve-point win A 53.8%, B 45.7%; Elo A 1454.1, B 1529.0; model uncertainty 0.1275
* Form inputs: days since last match A 184, B 198; matches on record A 82, B 228; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.016, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mu Jie Tzeng vs Aya El Sayed -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29TZEELS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aya El Sayed (`KXITFWMATCH-26OCT29TZEELS-ELS`) | 0.30 / 0.74 (400) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mu Jie Tzeng (`KXITFWMATCH-26OCT29TZEELS-TZE`) | 0.24 / 0.67 (7) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ksenia Zaytseva vs Viktoria Hruncakova -- W50 Istanbul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214149:257874:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Viktoria Hruncakova (`KXITFWMATCH-26OCT29ZAYHRU-HRU`) | 0.54 / 0.58 (62) | 56.0% | 67.4% | 59.0% | 61.6% [60.5%-63.6%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +11.4 pp | REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ksenia Zaytseva (`KXITFWMATCH-26OCT29ZAYHRU-ZAY`) | 0.42 / 0.44 (161) | 43.0% | 32.6% | 41.0% | 38.4% [36.4%-39.5%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -10.4 pp | REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1357.0, B 3899.0; serve-point win A 52.3%, B 44.3%; Elo A 1564.7, B 1669.1; model uncertainty 0.0152
* Form inputs: days since last match A 29, B 13; matches on record A 158, B 723; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.020, surface_dev_loose -0.000, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexandre Aubriot vs Miles Jones -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 13:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207404:208147:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandre Aubriot (`KXITFMATCH-26OCT29AUBJON-AUB`) | 0.43 / 0.47 (131) | 45.0% | 35.8% | 23.2% | 30.5% [26.1%-38.7%] | 46.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.2 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Miles Jones (`KXITFMATCH-26OCT29AUBJON-JON`) | 0.51 / 0.55 (35) | 53.0% | 64.2% | 76.8% | 69.5% [61.3%-74.0%] | 53.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +11.2 pp | REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2915.0, B 2182.0; serve-point win A 56.9%, B 40.3%; Elo A 1336.7, B 1391.3; model uncertainty 0.0634
* Form inputs: days since last match A 198, B 191; matches on record A 297, B 132; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high -0.000, surface_dev_loose -0.004, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lorusso / Kumar Sinha vs Blando / Blando -- M15 Singapore QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29LORKUMBLABLA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Blando / Blando (`KXITFDOUBLES-26OCT29LORKUMBLABLA-BLABLA`) | 0.13 / 0.36 (39) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lorusso / Kumar Sinha (`KXITFDOUBLES-26OCT29LORKUMBLABLA-LORKUM`) | 0.57 / 0.79 (119) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Ogura / Tamm vs Alam / Mischker -- M15 Singapore QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29OGUTAMALAMIS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alam / Mischker (`KXITFDOUBLES-26OCT29OGUTAMALAMIS-ALAMIS`) | 0.04 / 0.23 (32) | 13.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ogura / Tamm (`KXITFDOUBLES-26OCT29OGUTAMALAMIS-OGUTAM`) | 0.70 / 0.96 (11) | 83.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Rifqi Fitriadi / Han vs Inui / Sumizawa -- M15 Singapore QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29RIFHANINUSUM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Inui / Sumizawa (`KXITFDOUBLES-26OCT29RIFHANINUSUM-INUSUM`) | 0.22 / 0.34 (61) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rifqi Fitriadi / Han (`KXITFDOUBLES-26OCT29RIFHANINUSUM-RIFHAN`) | 0.59 / 0.78 (1) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Storch / Van Herzeele vs Masabayashi / Suksumrarn -- M15 Singapore QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29STOVANMASSUK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Masabayashi / Suksumrarn (`KXITFDOUBLES-26OCT29STOVANMASSUK-MASSUK`) | 0.65 / 0.84 (156) | 74.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Storch / Van Herzeele (`KXITFDOUBLES-26OCT29STOVANMASSUK-STOVAN`) | 0.11 / 0.30 (35) | 20.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Nikoloz Basilashvili vs Carlos Alcaraz -- ATP Vienna R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-29 15:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-29 14:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: 2026-10-29 13:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (TOUR_500_250) · Clay · scheduled 2026-10-29T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105932:207989:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlos Alcaraz (`KXATPMATCH-26OCT29BASALC-ALC`) | 0.89 / 0.90 (7264) | 89.5% | 95.4% | 97.1% | 97.0% [96.1%-97.3%] | 84.8% | -- | 84.8% | ALL_THREE_DISAGREE | SHADOW_BET | +5.9 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Nikoloz Basilashvili (`KXATPMATCH-26OCT29BASALC-BAS`) | 0.11 / 0.12 (2157) | 11.5% | 4.6% | 2.9% | 3.0% [2.7%-3.9%] | 15.2% | -- | 15.2% | ALL_THREE_DISAGREE | PASS | -6.9 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5076.0, B 5488.0; serve-point win A 54.8%, B 32.0%; Elo A 1761.6, B 2345.3; model uncertainty 0.0062
* Form inputs: days since last match A 3, B 1; matches on record A 967, B 477; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.001, surface_pool_high +0.002, surface_dev_loose -0.003, surface_dev_tight +0.003
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPSETWINNER-26OCT29BASALC-2-ALC` Will Carlos Alcaraz win set 2 in the Nikoloz Basilashvili vs Carlos Alcaraz match: 0.03/0.97 mid 50.0%, model 87.1% (projection_v2.0 (prediction ledger)) -- gap +37.1 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT29BASALC-2-BAS` Will Nikoloz Basilashvili win set 2 in the Nikoloz Basilashvili vs Carlos Alcaraz match: 0.03/0.97 mid 50.0%, model 12.9% (projection_v2.0 (prediction ledger)) -- gap -37.1 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29BASALC-BAS20` Will Nikoloz Basilashvili win the Nikoloz Basilashvili vs Carlos Alcaraz match by a set score of 2-0?: 0.02/0.38 mid 20.0%, model 1.7% (projection_v2.0 (prediction ledger)) -- gap -18.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29BASALC-BAS21` Will Nikoloz Basilashvili win the Nikoloz Basilashvili vs Carlos Alcaraz match by a set score of 2-1?: 0.02/0.38 mid 20.0%, model 2.9% (projection_v2.0 (prediction ledger)) -- gap -17.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29BASALC-ALC20` Will Carlos Alcaraz win the Nikoloz Basilashvili vs Carlos Alcaraz match by a set score of 2-0?: 0.62/0.68 mid 65.0%, model 75.8% (projection_v2.0 (prediction ledger)) -- gap +10.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT29BASALC-ALC6` Will Carlos Alcaraz win at least 5.5 more games than Nikoloz Basilashvili?: 0.40/0.50 mid 45.0%, model 54.2% (projection_v2.0 (prediction ledger)) -- gap +9.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT29BASALC-21` Over 20.5 games: 0.45/0.50 mid 47.5%, model 39.0% (projection_v2.0 (prediction ledger)) -- gap -8.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT29BASALC-26` Over 25.5 games: 0.24/0.29 mid 26.5%, model 19.8% (projection_v2.0 (prediction ledger)) -- gap -6.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT29BASALC-ALC3` Will Carlos Alcaraz win at least 2.5 more games than Nikoloz Basilashvili?: 0.79/0.90 mid 84.5%, model 90.4% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29BASALC-ALC21` Will Carlos Alcaraz win the Nikoloz Basilashvili vs Carlos Alcaraz match by a set score of 2-1?: 0.01/0.27 mid 14.0%, model 19.6% (projection_v2.0 (prediction ledger)) -- gap +5.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29BASALC-1-ALC` Will Carlos Alcaraz win set 1 in the Nikoloz Basilashvili vs Carlos Alcaraz match: 0.81/0.83 mid 82.0%, model 87.1% (projection_v2.0 (prediction ledger)) -- gap +5.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT29BASALC-1-BAS` Will Nikoloz Basilashvili win set 1 in the Nikoloz Basilashvili vs Carlos Alcaraz match: 0.16/0.19 mid 17.5%, model 12.9% (projection_v2.0 (prediction ledger)) -- gap -4.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT29BASALC-16` Over 15.5 games: 0.91/0.95 mid 93.0%, model 90.1% (projection_v2.0 (prediction ledger)) -- gap -2.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Beknazarov / Zinatulin vs Burtsev / Filaretov -- M15 Fergana QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29BEKZINBURFIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Beknazarov / Zinatulin (`KXITFDOUBLES-26OCT29BEKZINBURFIL-BEKZIN`) | 0.05 / 0.95 (1) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Burtsev / Filaretov (`KXITFDOUBLES-26OCT29BEKZINBURFIL-BURFIL`) | 0.05 / 0.95 (1) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Duhan / Murtaza vs Arcon / Seleznev -- M15 Fergana QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29DUHMURARCSEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arcon / Seleznev (`KXITFDOUBLES-26OCT29DUHMURARCSEL-ARCSEL`) | 0.05 / 0.25 (33) | 15.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Duhan / Murtaza (`KXITFDOUBLES-26OCT29DUHMURARCSEL-DUHMUR`) | 0.70 / 0.96 (11) | 83.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Axel Garcian vs Constantin Bittoun Kouzmine -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144970:209247:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Constantin Bittoun Kouzmine (`KXITFMATCH-26OCT29GARBIT-BIT`) | 0.36 / 0.59 (60) | 47.5% | 45.2% | 47.9% | 46.3% [45.3%-46.9%] | -- | -- | -- | -- | PASS | -2.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Axel Garcian (`KXITFMATCH-26OCT29GARBIT-GAR`) | 0.35 / 0.59 (60) | 47.0% | 54.8% | 52.1% | 53.7% [53.1%-54.7%] | -- | -- | -- | -- | PASS | +7.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2369.0, B 3712.0; serve-point win A 57.9%, B 43.0%; Elo A 1397.1, B 1356.2; model uncertainty 0.0077
* Form inputs: days since last match A 401, B 44; matches on record A 174, B 437; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Volodymyr Iakubenko vs Marat Salbiev -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212246:214324:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Volodymyr Iakubenko (`KXITFMATCH-26OCT29IAKSAL-IAK`) | 0.75 / 0.76 (106) | 75.5% | 61.7% | 51.0% | 56.1% [55.6%-56.7%] | -- | -- | -- | -- | PASS | -13.8 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marat Salbiev (`KXITFMATCH-26OCT29IAKSAL-SAL`) | 0.16 / 0.26 (12) | 21.0% | 38.3% | 49.0% | 43.9% [43.3%-44.4%] | -- | -- | -- | -- | PASS | +17.3 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1388.0, B 81.0; serve-point win A 61.5%, B 40.8%; Elo A 1301.7, B 1259.1; model uncertainty 0.0052
* Form inputs: days since last match A 191, B 338; matches on record A 47, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT29IAKSAL-SAL  (YES = Marat Salbiev)
Model: 38%
Kalshi: 21%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.005, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sergey Petrov vs David Eichenseher -- M15 Fergana R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212631:213815:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| David Eichenseher (`KXITFMATCH-26OCT29PETEIC-EIC`) | 0.28 / 0.32 (128) | 30.0% | 35.9% | 30.6% | 37.0% [34.3%-39.9%] | 30.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.9 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sergey Petrov (`KXITFMATCH-26OCT29PETEIC-PET`) | 0.67 / 0.71 (100) | 69.0% | 64.1% | 69.5% | 62.9% [60.1%-65.7%] | 69.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.9 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 661.0, B 1106.0; serve-point win A 63.4%, B 39.4%; Elo A 1263.3, B 1191.7; model uncertainty 0.028
* Form inputs: days since last match A 191, B 184; matches on record A 13, B 30; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Benoit Torcq vs Joaquin Benoit -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29TORBEN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joaquin Benoit (`KXITFMATCH-26OCT29TORBEN-BEN`) | 0.50 / 0.66 (70) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Benoit Torcq (`KXITFMATCH-26OCT29TORBEN-TOR`) | 0.35 / 0.43 (60) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Borys Zgola vs Aaron Funk -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210169:212630:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aaron Funk (`KXITFMATCH-26OCT29ZGOFUN-FUN`) | 0.50 / 0.64 (14) | 57.0% | 75.0% | 38.8% | 61.7% [60.8%-62.9%] | -- | -- | -- | -- | PASS | +18.1 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Borys Zgola (`KXITFMATCH-26OCT29ZGOFUN-ZGO`) | 0.29 / 0.43 (100) | 36.0% | 24.9% | 61.2% | 38.3% [37.0%-39.2%] | -- | -- | -- | -- | PASS | -11.1 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 63.0, B 1147.0; serve-point win A 61.9%, B 32.7%; Elo A 1102.3, B 1191.5; model uncertainty 0.011
* Form inputs: days since last match A 219, B 205; matches on record A 14, B 39; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT29ZGOFUN-FUN  (YES = Aaron Funk)
Model: 75%
Kalshi: 57%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.004, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hania Abouelsaad vs Kaat Coppez -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220394:266467:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hania Abouelsaad (`KXITFWMATCH-26OCT29ABOCOP-ABO`) | 0.38 / 0.48 (48) | 43.0% | 47.6% | 40.4% | 47.9% [44.1%-51.6%] | -- | -- | -- | -- | PASS | +4.6 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kaat Coppez (`KXITFWMATCH-26OCT29ABOCOP-COP`) | 0.51 / 0.62 (5) | 56.5% | 52.4% | 59.6% | 52.1% [48.4%-55.9%] | -- | -- | -- | -- | PASS | -4.1 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 897.0, B 759.0; serve-point win A 49.8%, B 49.7%; Elo A 1303.1, B 1298.8; model uncertainty 0.0374
* Form inputs: days since last match A 254, B 184; matches on record A 56, B 70; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.021, surface_dev_loose -0.016, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ekaterina Dotsenko vs Anna Kubareva -- W50 Istanbul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29DOTKUB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Dotsenko (`KXITFWMATCH-26OCT29DOTKUB-DOT`) | 0.60 / 0.61 (54) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anna Kubareva (`KXITFWMATCH-26OCT29DOTKUB-KUB`) | 0.36 / 0.39 (47) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Polina Kuharenko vs Alisa Ziatdinova -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:263626:270317:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Kuharenko (`KXITFWMATCH-26OCT29KUHZIA-KUH`) | 0.81 / 0.86 (3) | 83.5% | 90.2% | 89.4% | 77.2% [75.5%-78.4%] | -- | -- | -- | -- | PASS | +6.7 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alisa Ziatdinova (`KXITFWMATCH-26OCT29KUHZIA-ZIA`) | 0.11 / 0.15 (63) | 13.0% | 9.8% | 10.6% | 22.8% [21.6%-24.4%] | -- | -- | -- | -- | PASS | -3.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1767.0, B 165.0; serve-point win A 59.7%, B 50.0%; Elo A 1462.7, B 1269.4; model uncertainty 0.0141
* Form inputs: days since last match A 233, B 338; matches on record A 55, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.016, surface_dev_loose +0.008, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Katarina Kuzmova vs Kristina Novak -- W50 Istanbul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216038:221382:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katarina Kuzmova (`KXITFWMATCH-26OCT29KUZNOV-KUZ`) | 0.81 / 0.84 (227) | 82.5% | 89.7% | 92.6% | 89.0% [84.8%-91.8%] | 80.5% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +7.2 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kristina Novak (`KXITFWMATCH-26OCT29KUZNOV-NOV`) | 0.16 / 0.20 (119) | 18.0% | 10.3% | 7.4% | 11.0% [8.2%-15.2%] | 19.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.7 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4079.0, B 994.0; serve-point win A 63.3%, B 46.4%; Elo A 1646.6, B 1325.7; model uncertainty 0.0352
* Form inputs: days since last match A 36, B 17; matches on record A 486, B 141; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.009, surface_dev_loose +0.004, surface_dev_tight -0.002
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Viktoriia Sedenkova vs Zuzanna Bednarz -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29SEDBED:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zuzanna Bednarz (`KXITFWMATCH-26OCT29SEDBED-BED`) | 0.74 / 0.97 (279) | 85.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Viktoriia Sedenkova (`KXITFWMATCH-26OCT29SEDBED-SED`) | 0.04 / 0.20 (31) | 12.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Beatris Spasova vs Nastasja Schunk -- W50 Istanbul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221315:221768:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nastasja Schunk (`KXITFWMATCH-26OCT29SPASCH-SCH`) | 0.91 / 0.97 (279) | 94.0% | 96.1% | 91.7% | 90.5% [87.5%-92.9%] | -- | -- | -- | -- | PASS | +2.1 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Beatris Spasova (`KXITFWMATCH-26OCT29SPASCH-SPA`) | 0.04 / 0.05 (10) | 4.5% | 3.9% | 8.3% | 9.6% [7.1%-12.5%] | -- | -- | -- | -- | WATCH | -0.6 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 520.0, B 2120.0; serve-point win A 46.9%, B 39.8%; Elo A 1166.2, B 1548.5; model uncertainty 0.0271
* Form inputs: days since last match A 240, B 41; matches on record A 195, B 249; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.024, surface_pool_high +0.030, surface_dev_loose +0.000, surface_dev_tight +0.002
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Taylor Fritz vs Denis Shapovalov -- ATP Basel R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-29 17:10Z
* Current expected start: 2026-10-29 14:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: 2026-10-29 13:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-29T17:10:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126203:133430:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Taylor Fritz (`KXATPMATCH-26OCT29FRISHA-FRI`) | 0.71 / 0.73 (2157) | 72.0% | 67.3% | 71.2% | 70.0% [69.1%-70.9%] | 70.1% | -- | 70.1% | MODEL_LONE_OUTLIER | PASS | -4.7 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Denis Shapovalov (`KXATPMATCH-26OCT29FRISHA-SHA`) | 0.27 / 0.29 (1324) | 28.0% | 32.7% | 28.8% | 30.0% [29.1%-30.9%] | 29.9% | -- | 29.9% | MODEL_LONE_OUTLIER | PASS | +4.7 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 6643.0, B 4653.0; serve-point win A 68.0%, B 35.6%; Elo A 2052.9, B 1933.0; model uncertainty 0.0087
* Form inputs: days since last match A 3, B 24; matches on record A 764, B 580; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.009, surface_dev_loose -0.008, surface_dev_tight +0.008
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT29FRISHA-FRI21` Will Taylor Fritz win the Taylor Fritz vs Denis Shapovalov match by a set score of 2-1?: 0.01/0.31 mid 16.0%, model 29.2% (projection_v2.0 (prediction ledger)) -- gap +13.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29FRISHA-2-FRI` Will Taylor Fritz win set 2 in the Taylor Fritz vs Denis Shapovalov match: 0.01/0.98 mid 49.5%, model 61.7% (projection_v2.0 (prediction ledger)) -- gap +12.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT29FRISHA-1-FRI` Will Taylor Fritz win set 1 in the Taylor Fritz vs Denis Shapovalov match: 0.03/0.97 mid 50.0%, model 61.7% (projection_v2.0 (prediction ledger)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT29FRISHA-1-SHA` Will Denis Shapovalov win set 1 in the Taylor Fritz vs Denis Shapovalov match: 0.03/0.97 mid 50.0%, model 38.3% (projection_v2.0 (prediction ledger)) -- gap -11.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT29FRISHA-2-SHA` Will Denis Shapovalov win set 2 in the Taylor Fritz vs Denis Shapovalov match: 0.02/0.98 mid 50.0%, model 38.3% (projection_v2.0 (prediction ledger)) -- gap -11.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29FRISHA-FRI20` Will Taylor Fritz win the Taylor Fritz vs Denis Shapovalov match by a set score of 2-0?: 0.02/0.51 mid 26.5%, model 38.1% (projection_v2.0 (prediction ledger)) -- gap +11.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT29FRISHA-20` Over 19.5 games: 0.69/0.81 mid 75.0%, model 82.5% (projection_v2.0 (prediction ledger)) -- gap +7.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT29FRISHA-FRI3` Will Taylor Fritz win at least 2.5 more games than Denis Shapovalov?: 0.56/0.59 mid 57.5%, model 50.7% (projection_v2.0 (prediction ledger)) -- gap -6.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT29FRISHA-25` Over 24.5 games: 0.43/0.50 mid 46.5%, model 52.7% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT29FRISHA-FRI6` Will Taylor Fritz win at least 5.5 more games than Denis Shapovalov?: 0.14/0.22 mid 18.0%, model 12.2% (projection_v2.0 (prediction ledger)) -- gap -5.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29FRISHA-SHA20` Will Denis Shapovalov win the Taylor Fritz vs Denis Shapovalov match by a set score of 2-0?: 0.02/0.38 mid 20.0%, model 14.6% (projection_v2.0 (prediction ledger)) -- gap -5.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT29FRISHA-30` Over 29.5 games: 0.23/0.35 mid 29.0%, model 32.8% (projection_v2.0 (prediction ledger)) -- gap +3.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29FRISHA-SHA21` Will Denis Shapovalov win the Taylor Fritz vs Denis Shapovalov match by a set score of 2-1?: 0.02/0.38 mid 20.0%, model 18.1% (projection_v2.0 (prediction ledger)) -- gap -1.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT29FRISHA-SHA2` Will Denis Shapovalov win at least 1.5 more games than Taylor Fritz?: 0.22/0.27 mid 24.5%, model 25.8% (projection_v2.0 (prediction ledger)) -- gap +1.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## N. Sriram Balaji / Evan King vs Andriy Poritskyy / Vadym Ursu -- ATP Challenger Brest QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-29T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29BALKINPORURS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N. Sriram Balaji / Evan King (`KXATPCHALLENGERDOUBLES-26OCT29BALKINPORURS-BALKIN`) | 0.06 / 0.94 (100) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Andriy Poritskyy / Vadym Ursu (`KXATPCHALLENGERDOUBLES-26OCT29BALKINPORURS-PORURS`) | 0.06 / 0.94 (850) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Niccolo Ciavarella vs Sven Corbinais -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210684:211457:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Niccolo Ciavarella (`KXITFMATCH-26OCT29CIACOR-CIA`) | 0.42 / 0.44 (121) | 43.0% | 72.5% | 80.0% | 61.1% [54.8%-67.1%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +29.5 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sven Corbinais (`KXITFMATCH-26OCT29CIACOR-COR`) | 0.51 / 0.58 (64) | 54.5% | 27.5% | 20.0% | 38.9% [32.9%-45.2%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -27.0 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1338.0, B 528.0; serve-point win A 55.5%, B 49.0%; Elo A 1228.8, B 1204.8; model uncertainty 0.0618
* Form inputs: days since last match A 184, B 247; matches on record A 100, B 24; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT29CIACOR-CIA  (YES = Niccolo Ciavarella)
Model: 72%
Kalshi: 43%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.021, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## James Hopper / Mark Whitehouse vs Ivan Liutarevich / Joshua Paris -- ATP Challenger Brest QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-29T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29HOPWHILIUPAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| James Hopper / Mark Whitehouse (`KXATPCHALLENGERDOUBLES-26OCT29HOPWHILIUPAR-HOPWHI`) | 0.06 / 0.94 (850) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ivan Liutarevich / Joshua Paris (`KXATPCHALLENGERDOUBLES-26OCT29HOPWHILIUPAR-LIUPAR`) | 0.06 / 0.94 (850) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Nicolas Jadoun vs Christian Djonov -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211645:212171:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Christian Djonov (`KXITFMATCH-26OCT29JADDJO-DJO`) | 0.26 / 0.47 (47) | 36.5% | 40.4% | 43.9% | 40.9% [38.9%-42.4%] | -- | -- | -- | -- | PASS | +3.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nicolas Jadoun (`KXITFMATCH-26OCT29JADDJO-JAD`) | 0.47 / 0.70 (83) | 58.5% | 59.6% | 56.1% | 59.1% [57.6%-61.1%] | -- | -- | -- | -- | PASS | +1.1 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2054.0, B 1032.0; serve-point win A 62.0%, B 39.9%; Elo A 1267.1, B 1192.6; model uncertainty 0.0172
* Form inputs: days since last match A 205, B 191; matches on record A 92, B 28; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.010, surface_dev_loose +0.019, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Louis Larue vs Benito Sanchez Martinez -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209917:211646:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Louis Larue (`KXITFMATCH-26OCT29LARSAN-LAR`) | 0.06 / 0.08 (128) | 7.0% | 18.1% | 14.0% | 23.8% [19.5%-26.9%] | -- | -- | -- | -- | WATCH | +11.1 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Benito Sanchez Martinez (`KXITFMATCH-26OCT29LARSAN-SAN`) | 0.87 / 0.94 (10) | 90.5% | 81.9% | 86.0% | 76.2% [73.1%-80.5%] | -- | -- | -- | -- | PASS | -8.6 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1651.0, B 681.0; serve-point win A 53.6%, B 39.5%; Elo A 1266.6, B 1423.3; model uncertainty 0.0368
* Form inputs: days since last match A 198, B 23; matches on record A 45, B 38; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.012, surface_pool_high +0.008, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nikita Mashtakov vs Gilberto Ravasio -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213923:tml:MW62:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikita Mashtakov (`KXITFMATCH-26OCT29MASRAV-MAS`) | 0.80 / 0.95 (19) | 87.5% | 82.1% | 84.2% | 80.0% [77.9%-83.0%] | -- | -- | -- | -- | PASS | -5.4 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gilberto Ravasio (`KXITFMATCH-26OCT29MASRAV-RAV`) | 0.05 / 0.15 (35) | 10.0% | 17.9% | 15.8% | 20.0% [17.1%-22.1%] | -- | -- | -- | -- | PASS | +7.9 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 306.0, B 633.0; serve-point win A 57.1%, B 49.8%; Elo A 1415.8, B 1182.8; model uncertainty 0.0251
* Form inputs: days since last match A 37, B 184; matches on record A 5, B 16; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.007, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aziz Ouakaa vs Nicolas Garcia Longo -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200297:212834:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Garcia Longo (`KXITFMATCH-26OCT29OUAGAR-GAR`) | 0.07 / 0.11 (100) | 9.0% | 32.6% | 31.2% | 30.7% [28.9%-32.2%] | 12.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +23.6 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aziz Ouakaa (`KXITFMATCH-26OCT29OUAGAR-OUA`) | 0.89 / 0.91 (2) | 90.0% | 67.4% | 68.8% | 69.3% [67.8%-71.1%] | 87.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -22.6 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3444.0, B 1254.0; serve-point win A 57.9%, B 45.5%; Elo A 1357.4, B 1209.5; model uncertainty 0.0164
* Form inputs: days since last match A 79, B 289; matches on record A 439, B 34; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT29OUAGAR-GAR  (YES = Nicolas Garcia Longo)
Model: 33%
Kalshi: 9%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.009, surface_dev_loose +0.018, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pablo Perez Ramos vs Dan Brand -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29PERBRA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dan Brand (`KXITFMATCH-26OCT29PERBRA-BRA`) | 0.35 / 0.38 (132) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pablo Perez Ramos (`KXITFMATCH-26OCT29PERBRA-PER`) | 0.59 / 0.64 (41) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## William Rejchtman Vinciguerra vs Nicolas Tepmahc -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208168:212478:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| William Rejchtman Vinciguerra (`KXITFMATCH-26OCT29REJTEP-REJ`) | 0.45 / 0.47 (100) | 46.0% | 33.4% | 15.6% | 26.0% [19.7%-35.7%] | -- | -- | -- | -- | PASS | -12.6 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nicolas Tepmahc (`KXITFMATCH-26OCT29REJTEP-TEP`) | 0.50 / 0.54 (43) | 52.0% | 66.6% | 84.4% | 74.0% [64.3%-80.3%] | -- | -- | -- | -- | WATCH | +14.6 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1195.0, B 3348.0; serve-point win A 56.0%, B 40.7%; Elo A 1266.1, B 1365.3; model uncertainty 0.0803
* Form inputs: days since last match A 93, B 184; matches on record A 37, B 237; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.013, surface_dev_loose -0.008, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Francesca Gandolfi vs Mailuodi Lei -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260984:264985:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesca Gandolfi (`KXITFWMATCH-26OCT29GANLEI-GAN`) | 0.72 / 0.73 (203) | 72.5% | 88.8% | 57.5% | 73.1% [72.2%-73.1%] | -- | -- | -- | -- | PASS | +16.3 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Mailuodi Lei (`KXITFWMATCH-26OCT29GANLEI-LEI`) | 0.27 / 0.28 (1426) | 27.5% | 11.2% | 42.5% | 26.9% [26.9%-27.8%] | -- | -- | -- | -- | PASS | -16.3 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1436.0, B 0.0; serve-point win A 57.2%, B 51.9%; Elo A 1382.7, B 1212.4; model uncertainty 0.0046
* Form inputs: days since last match A 108, B 1115; matches on record A 41, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT29GANLEI-GAN  (YES = Francesca Gandolfi)
Model: 89%
Kalshi: 72%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sara Husar vs Kayo Nishimura -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260613:267739:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Husar (`KXITFWMATCH-26OCT29HUSNIS-HUS`) | 0.06 / 0.08 (41) | 7.0% | 4.8% | 6.7% | 11.1% [9.7%-11.9%] | -- | -- | -- | -- | PASS | -2.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kayo Nishimura (`KXITFWMATCH-26OCT29HUSNIS-NIS`) | 0.89 / 0.93 (72) | 91.0% | 95.2% | 93.3% | 88.9% [88.1%-90.3%] | -- | -- | -- | -- | PASS | +4.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 132.0, B 2288.0; serve-point win A 44.7%, B 42.9%; Elo A 1195.4, B 1542.8; model uncertainty 0.0114
* Form inputs: days since last match A 303, B 184; matches on record A 6, B 161; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.008, surface_dev_loose -0.003, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Victoire Lansaman vs Anna Shkutova -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:266812:270216:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Victoire Lansaman (`KXITFWMATCH-26OCT29LANSHK-LAN`) | 0.26 / 0.27 (6) | 26.5% | 35.8% | 32.9% | 42.6% [38.9%-44.7%] | 28.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +9.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anna Shkutova (`KXITFWMATCH-26OCT29LANSHK-SHK`) | 0.71 / 0.73 (33) | 72.0% | 64.2% | 67.1% | 57.4% [55.3%-61.1%] | 71.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 155.0, B 401.0; serve-point win A 51.8%, B 45.5%; Elo A 1221.5, B 1264.0; model uncertainty 0.0288
* Form inputs: days since last match A 226, B 184; matches on record A 10, B 9; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Baotong Xu vs Sofia Camila Rojas -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29XUXROJ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Camila Rojas (`KXITFWMATCH-26OCT29XUXROJ-ROJ`) | 0.79 / 0.81 (21) | 80.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Baotong Xu (`KXITFWMATCH-26OCT29XUXROJ-XUX`) | 0.15 / 0.18 (420) | 16.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniel Altmaier vs Jiri Lehecka -- ATP Basel R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-28 16:00Z
* Current expected start: 2026-10-29 15:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: 2026-10-29 14:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1380_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-28T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:127157:208103:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Altmaier (`KXATPMATCH-26OCT28ALTLEH-ALT`) | 0.16 / 0.17 (17717) | 16.5% | 18.9% | 14.5% | 16.0% [14.6%-17.4%] | -- | -- | -- | -- | PASS | +2.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jiri Lehecka (`KXATPMATCH-26OCT28ALTLEH-LEH`) | 0.83 / 0.84 (2300) | 83.5% | 81.1% | 85.5% | 84.0% [82.6%-85.4%] | -- | -- | -- | -- | PASS | -2.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5885.0, B 5638.0; serve-point win A 63.8%, B 28.9%; Elo A 1741.8, B 1981.9; model uncertainty 0.0139
* Form inputs: days since last match A 2, B 1; matches on record A 731, B 460; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.006, surface_dev_loose -0.014, surface_dev_tight +0.014
* Derivatives listed: 6 (GAME_SPREAD, MATCH_WINNER, TOTAL_GAMES); 6 carry a model probability
  * `KXATPGTOTAL-26OCT28ALTLEH-26` Over 25.5 games: 0.33/0.37 mid 35.0%, model 42.7% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT28ALTLEH-21` Over 20.5 games: 0.59/0.68 mid 63.5%, model 70.2% (projection_v2.0 (prediction ledger)) -- gap +6.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT28ALTLEH-LEH5` Will Jiri Lehecka win at least 4.5 more games than Daniel Altmaier?: 0.36/0.37 mid 36.5%, model 32.6% (projection_v2.0 (prediction ledger)) -- gap -3.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT28ALTLEH-LEH2` Will Jiri Lehecka win at least 1.5 more games than Daniel Altmaier?: 0.77/0.80 mid 78.5%, model 74.9% (projection_v2.0 (prediction ledger)) -- gap -3.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT28ALTLEH-16` Over 15.5 games: 0.96/0.99 mid 97.5%, model 99.0% (projection_v2.0 (prediction ledger)) -- gap +1.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nino Ehrenschneider vs Georgii Kravchenko -- M25 Malta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206662:209510:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nino Ehrenschneider (`KXITFMATCH-26OCT29EHRKRA-EHR`) | 0.32 / 0.35 (139) | 33.5% | 35.7% | 32.3% | 34.7% [33.7%-37.0%] | 35.6% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +2.2 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Georgii Kravchenko (`KXITFMATCH-26OCT29EHRKRA-KRA`) | 0.68 / 0.69 (396) | 68.5% | 64.3% | 67.7% | 65.3% [63.0%-66.3%] | 64.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.2 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3493.0, B 3083.0; serve-point win A 60.5%, B 36.6%; Elo A 1374.1, B 1444.6; model uncertainty 0.0163
* Form inputs: days since last match A 184, B 16; matches on record A 129, B 390; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.005, surface_dev_loose -0.009, surface_dev_tight +0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Funk / Maute vs Ianin / Ibrahim -- M15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29FUNMAUIANIBR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Funk / Maute (`KXITFDOUBLES-26OCT29FUNMAUIANIBR-FUNMAU`) | 0.19 / 0.44 (44) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ianin / Ibrahim (`KXITFDOUBLES-26OCT29FUNMAUIANIBR-IANIBR`) | 0.48 / 0.74 (96) | 61.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Kaan Oktay / Stepanov vs Bittoun Kouzmine / Blazka -- M15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29KAASTEBITBLA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bittoun Kouzmine / Blazka (`KXITFDOUBLES-26OCT29KAASTEBITBLA-BITBLA`) | 0.72 / 0.96 (11) | 84.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kaan Oktay / Stepanov (`KXITFDOUBLES-26OCT29KAASTEBITBLA-KAASTE`) | 0.04 / 0.21 (31) | 12.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jan Sadzik vs Pavlos Tsitsipas -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210409:214087:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jan Sadzik (`KXITFMATCH-26OCT29SADTSI-SAD`) | 0.41 / 0.44 (6) | 42.5% | 57.8% | 82.5% | 63.8% [60.1%-67.0%] | 43.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +15.3 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pavlos Tsitsipas (`KXITFMATCH-26OCT29SADTSI-TSI`) | 0.54 / 0.58 (224) | 56.0% | 42.2% | 17.5% | 36.1% [33.0%-39.9%] | 56.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.8 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 276.0, B 1989.0; serve-point win A 63.3%, B 38.3%; Elo A 1250.5, B 1177.4; model uncertainty 0.0348
* Form inputs: days since last match A 429, B 184; matches on record A 3, B 86; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT29SADTSI-SAD  (YES = Jan Sadzik)
Model: 58%
Kalshi: 42%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.009, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Robert Strombachs vs Samuel De Felipe Garcia -- M25 Malta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206645:207669:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Samuel De Felipe Garcia (`KXITFMATCH-26OCT29STRDEF-DEF`) | 0.06 / 0.07 (132) | 6.5% | 5.3% | 16.7% | 9.6% [9.0%-10.4%] | -- | -- | -- | -- | PASS | -1.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Robert Strombachs (`KXITFMATCH-26OCT29STRDEF-STR`) | 0.90 / 0.95 (4) | 92.5% | 94.7% | 83.3% | 90.4% [89.5%-91.0%] | -- | -- | -- | -- | PASS | +2.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3313.0, B 273.0; serve-point win A 68.2%, B 44.6%; Elo A 1526.7, B 1116.2; model uncertainty 0.007
* Form inputs: days since last match A 44, B 415; matches on record A 461, B 6; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.002, surface_dev_loose +0.002, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Esther Adeshina vs Valentini Grammatikopoulou -- W35 Malta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:204394:221959:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Esther Adeshina (`KXITFWMATCH-26OCT29ADEGRA-ADE`) | 0.38 / 0.39 (80) | 38.5% | 45.5% | 47.9% | 47.9% [37.4%-52.7%] | -- | -- | -- | -- | WATCH | +7.0 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valentini Grammatikopoulou (`KXITFWMATCH-26OCT29ADEGRA-GRA`) | 0.56 / 0.59 (7) | 57.5% | 54.5% | 52.1% | 52.1% [47.3%-62.6%] | -- | -- | -- | -- | PASS | -3.0 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3059.0, B 2942.0; serve-point win A 51.4%, B 47.8%; Elo A 1488.6, B 1508.1; model uncertainty 0.0765
* Form inputs: days since last match A 126, B 107; matches on record A 115, B 724; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.048, surface_pool_high +0.048, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Grace Bernstein vs Coco Bosman -- W15 Taby R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223421:270311:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Grace Bernstein (`KXITFWMATCH-26OCT29BERBOS-BER`) | 0.43 / 0.49 (23) | 46.0% | 32.4% | 37.7% | 42.2% [41.6%-43.3%] | -- | -- | -- | -- | PASS | -13.6 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Coco Bosman (`KXITFWMATCH-26OCT29BERBOS-BOS`) | 0.49 / 0.53 (6) | 51.0% | 67.6% | 62.3% | 57.8% [56.7%-58.4%] | -- | -- | -- | -- | PASS | +16.6 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 129.0, B 2097.0; serve-point win A 56.8%, B 39.7%; Elo A 1303.1, B 1352.6; model uncertainty 0.0083
* Form inputs: days since last match A 113, B 184; matches on record A 3, B 69; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT29BERBOS-BOS  (YES = Coco Bosman)
Model: 68%
Kalshi: 51%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Francesca Curmi vs Clara Vlasselaer -- W75 Poitiers R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221003:221014:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesca Curmi (`KXITFWMATCH-26OCT29CURVLA-CUR`) | 0.86 / 0.88 (26) | 87.0% | 80.0% | 77.2% | 73.5% [69.0%-78.3%] | 83.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.0 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Clara Vlasselaer (`KXITFWMATCH-26OCT29CURVLA-VLA`) | 0.11 / 0.14 (473) | 12.5% | 20.0% | 22.8% | 26.5% [21.7%-31.0%] | 16.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +7.5 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2628.0, B 1490.0; serve-point win A 61.7%, B 44.7%; Elo A 1633.4, B 1481.5; model uncertainty 0.0465
* Form inputs: days since last match A 11, B 184; matches on record A 324, B 332; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.049, surface_pool_high -0.044, surface_dev_loose +0.008, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Iveta Dapkute vs Micol Salvadori -- W15 Taby R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:210158:266406:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iveta Dapkute (`KXITFWMATCH-26OCT29DAPSAL-DAP`) | 0.75 / 0.81 (85) | 78.0% | 79.2% | 43.1% | 69.0% [66.1%-71.3%] | 76.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.2 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Micol Salvadori (`KXITFWMATCH-26OCT29DAPSAL-SAL`) | 0.18 / 0.19 (730) | 18.5% | 20.8% | 56.9% | 31.0% [28.7%-33.9%] | 24.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 792.0, B 242.0; serve-point win A 54.6%, B 51.4%; Elo A 1404.3, B 1228.4; model uncertainty 0.0259
* Form inputs: days since last match A 184, B 198; matches on record A 203, B 28; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.019, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Milana Maslenkova vs Astrid Wanja Brune Olsen -- W15 Taby R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214934:219872:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Astrid Wanja Brune Olsen (`KXITFWMATCH-26OCT29MASBRU-BRU`) | 0.84 / 0.89 (51) | 86.5% | 70.0% | 77.8% | 69.5% [65.2%-73.6%] | -- | -- | -- | -- | PASS | -16.5 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Milana Maslenkova (`KXITFWMATCH-26OCT29MASBRU-MAS`) | 0.09 / 0.13 (367) | 11.0% | 30.0% | 22.2% | 30.5% [26.4%-34.8%] | -- | -- | -- | -- | WATCH | +19.0 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 972.0, B 1262.0; serve-point win A 48.6%, B 47.5%; Elo A 1216.3, B 1314.8; model uncertainty 0.0423
* Form inputs: days since last match A 205, B 184; matches on record A 147, B 171; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT29MASBRU-MAS  (YES = Milana Maslenkova)
Model: 30%
Kalshi: 11%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.028, surface_pool_high +0.024, surface_dev_loose +0.009, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alyssa Reguer vs Vittoria Paganetti -- W35 Malta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:234474:260510:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vittoria Paganetti (`KXITFWMATCH-26OCT29REGPAG-PAG`) | 0.69 / 0.75 (48) | 72.0% | 74.2% | 51.6% | 59.6% [56.9%-68.1%] | -- | -- | -- | -- | PASS | +2.2 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alyssa Reguer (`KXITFWMATCH-26OCT29REGPAG-REG`) | 0.23 / 0.27 (8) | 25.0% | 25.8% | 48.4% | 40.4% [31.9%-43.1%] | -- | -- | -- | -- | PASS | +0.8 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2738.0, B 2038.0; serve-point win A 48.9%, B 46.3%; Elo A 1371.4, B 1523.2; model uncertainty 0.0557
* Form inputs: days since last match A 184, B 148; matches on record A 233, B 91; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.005, surface_dev_loose +0.026, surface_dev_tight -0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Federica Urgesi vs Isis Louise Van den Broek -- W35 Malta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223415:264227:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Federica Urgesi (`KXITFWMATCH-26OCT29URGVAN-URG`) | 0.66 / 0.70 (49) | 68.0% | 61.5% | 56.4% | 54.3% [51.6%-56.4%] | -- | -- | -- | -- | PASS | -6.5 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Isis Louise Van den Broek (`KXITFWMATCH-26OCT29URGVAN-VAN`) | 0.26 / 0.34 (29) | 30.0% | 38.5% | 43.6% | 45.7% [43.6%-48.4%] | -- | -- | -- | -- | PASS | +8.5 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2635.0, B 1856.0; serve-point win A 53.9%, B 48.3%; Elo A 1586.9, B 1579.5; model uncertainty 0.0239
* Form inputs: days since last match A 37, B 184; matches on record A 169, B 103; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.027, surface_dev_loose +0.016, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Klara Veldman vs Klara Blazkova -- W15 Taby R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223418:270456:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Klara Blazkova (`KXITFWMATCH-26OCT29VELBLA-BLA`) | 0.17 / 0.22 (25) | 19.5% | 39.8% | 58.4% | 48.9% [47.9%-50.5%] | 21.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +20.3 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Klara Veldman (`KXITFWMATCH-26OCT29VELBLA-VEL`) | 0.76 / 0.80 (162) | 78.0% | 60.2% | 41.6% | 51.1% [49.5%-52.1%] | 78.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -17.8 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1299.0, B 94.0; serve-point win A 56.4%, B 45.6%; Elo A 1331.3, B 1319.9; model uncertainty 0.0133
* Form inputs: days since last match A 184, B 240; matches on record A 141, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT29VELBLA-BLA  (YES = Klara Blazkova)
Model: 40%
Kalshi: 20%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.011, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lara Wagner vs Weronika Ewald -- W35 Malta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29WAGEWA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Weronika Ewald (`KXITFWMATCH-26OCT29WAGEWA-EWA`) | 0.85 / 0.94 (50) | 89.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lara Wagner (`KXITFWMATCH-26OCT29WAGEWA-WAG`) | 0.06 / 0.09 (20) | 7.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maximo Gonzalez / Andres Molteni vs Ignacio Buse / Luciano Darderi -- ATP Vienna R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-29 18:10Z
* Current expected start: 2026-10-29 15:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: 2026-10-29 14:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-29T18:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29GONMOLBUSDAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ignacio Buse / Luciano Darderi (`KXATPDOUBLES-26OCT29GONMOLBUSDAR-BUSDAR`) | 0.26 / 0.34 (30) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maximo Gonzalez / Andres Molteni (`KXATPDOUBLES-26OCT29GONMOLBUSDAR-GONMOL`) | 0.62 / 0.70 (63) | 66.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Giovanni Ciocca vs Lilian Marmousez -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208421:214317:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giovanni Ciocca (`KXITFMATCH-26OCT29CIOMAR-CIO`) | 0.04 / 0.05 (224) | 4.5% | 6.0% | 5.4% | 9.8% [6.9%-13.3%] | -- | -- | -- | -- | PASS | +1.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lilian Marmousez (`KXITFMATCH-26OCT29CIOMAR-MAR`) | 0.92 / 0.96 (24) | 94.0% | 94.0% | 94.6% | 90.2% [86.7%-93.2%] | -- | -- | -- | -- | PASS | +0.0 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 297.0, B 2574.0; serve-point win A 53.4%, B 34.6%; Elo A 1185.9, B 1554.5; model uncertainty 0.0321
* Form inputs: days since last match A 184, B 156; matches on record A 6, B 272; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.029, surface_pool_high +0.035, surface_dev_loose -0.002, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tuncay Duran vs Mahmoud chetouane -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210513:214156:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mahmoud chetouane (`KXITFMATCH-26OCT29DURCHE-CHE`) | 0.04 / 0.05 (222) | 4.5% | 13.8% | 6.2% | 19.5% [13.1%-27.9%] | -- | -- | -- | -- | PASS | +9.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tuncay Duran (`KXITFMATCH-26OCT29DURCHE-DUR`) | 0.91 / 0.96 (24) | 93.5% | 86.2% | 93.8% | 80.5% [72.1%-86.9%] | -- | -- | -- | -- | PASS | -7.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2111.0, B 395.0; serve-point win A 67.0%, B 41.6%; Elo A 1429.3, B 1238.3; model uncertainty 0.074
* Form inputs: days since last match A 86, B 303; matches on record A 111, B 8; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.017, surface_dev_loose +0.009, surface_dev_tight -0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jones / Jones vs Brand / Sadzik -- M15 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29JONJONBRASAD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brand / Sadzik (`KXITFDOUBLES-26OCT29JONJONBRASAD-BRASAD`) | 0.05 / 0.95 (1) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jones / Jones (`KXITFDOUBLES-26OCT29JONJONBRASAD-JONJON`) | 0.05 / 0.95 (1) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Toufik Sahtali vs Kris van Wyk -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144748:200086:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Toufik Sahtali (`KXITFMATCH-26OCT29SAHVAN-SAH`) | 0.53 / 0.57 (100) | 55.0% | 78.0% | 87.4% | 80.3% [69.7%-84.1%] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +23.0 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kris van Wyk (`KXITFMATCH-26OCT29SAHVAN-VAN`) | 0.39 / 0.42 (36) | 40.5% | 22.0% | 12.6% | 19.7% [15.9%-30.3%] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -18.5 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3339.0, B 2875.0; serve-point win A 57.4%, B 48.4%; Elo A 1404.3, B 1319.6; model uncertainty 0.072
* Form inputs: days since last match A 184, B 191; matches on record A 92, B 324; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT29SAHVAN-SAH  (YES = Toufik Sahtali)
Model: 78%
Kalshi: 55%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.007, surface_dev_loose +0.015, surface_dev_tight -0.019
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cagla Buyukakcay vs Lidia Encheva -- W50 Istanbul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:201666:260565:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cagla Buyukakcay (`KXITFWMATCH-26OCT29BUYENC-BUY`) | 0.29 / 0.32 (51) | 30.5% | 40.1% | 19.9% | 37.9% [31.4%-51.1%] | 31.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +9.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lidia Encheva (`KXITFWMATCH-26OCT29BUYENC-ENC`) | 0.67 / 0.71 (126) | 69.0% | 59.9% | 80.1% | 62.1% [48.9%-68.6%] | 68.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1622.0, B 2702.0; serve-point win A 50.2%, B 47.9%; Elo A 1565.5, B 1495.4; model uncertainty 0.0983
* Form inputs: days since last match A 21, B 14; matches on record A 1042, B 152; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.015, surface_dev_loose -0.035, surface_dev_tight +0.031
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ariadna Garcia-Patron Canals vs Chenting Zhu -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264064:266543:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ariadna Garcia-Patron Canals (`KXITFWMATCH-26OCT29GARZHU-GAR`) | 0.04 / 0.05 (19) | 4.5% | 7.3% | 23.0% | 18.1% [17.1%-20.0%] | -- | -- | -- | -- | PASS | +2.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Chenting Zhu (`KXITFWMATCH-26OCT29GARZHU-ZHU`) | 0.91 / 0.97 (279) | 94.0% | 92.7% | 77.0% | 81.9% [80.0%-82.9%] | -- | -- | -- | -- | PASS | -1.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 864.0, B 2166.0; serve-point win A 47.0%, B 42.1%; Elo A 1200.6, B 1492.8; model uncertainty 0.0145
* Form inputs: days since last match A 352, B 28; matches on record A 24, B 99; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.004, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lina Gjorcheska vs Raluca Georgiana Serban -- W50 Istanbul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29GJOSER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lina Gjorcheska (`KXITFWMATCH-26OCT29GJOSER-GJO`) | 0.49 / 0.52 (43) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Raluca Georgiana Serban (`KXITFWMATCH-26OCT29GJOSER-SER`) | 0.47 / 0.51 (41) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lekomtseva / Tupitsyna vs Egorova / Zaytseva -- W50 Istanbul QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29LEKTUPEGOZAY:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Egorova / Zaytseva (`KXITFWDOUBLES-26OCT29LEKTUPEGOZAY-EGOZAY`) | 0.05 / 0.95 (1) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lekomtseva / Tupitsyna (`KXITFWDOUBLES-26OCT29LEKTUPEGOZAY-LEKTUP`) | 0.05 / 0.95 (1) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sabine Rutlauka vs Cindy Langlais -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223404:265207:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cindy Langlais (`KXITFWMATCH-26OCT29RUTLAN-LAN`) | 0.41 / 0.46 (4) | 43.5% | 28.1% | 38.4% | 30.5% [28.7%-32.4%] | 46.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.4 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sabine Rutlauka (`KXITFWMATCH-26OCT29RUTLAN-RUT`) | 0.53 / 0.55 (14) | 54.0% | 71.9% | 61.6% | 69.5% [67.6%-71.3%] | 53.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +17.9 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1315.0, B 854.0; serve-point win A 54.4%, B 49.9%; Elo A 1476.3, B 1299.2; model uncertainty 0.0186
* Form inputs: days since last match A 184, B 184; matches on record A 93, B 38; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT29RUTLAN-RUT  (YES = Sabine Rutlauka)
Model: 72%
Kalshi: 54%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.009, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nina Sozaonova vs Mariia Lazarenko -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29SOZLAZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mariia Lazarenko (`KXITFWMATCH-26OCT29SOZLAZ-LAZ`) | 0.77 / 0.79 (231) | 78.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nina Sozaonova (`KXITFWMATCH-26OCT29SOZLAZ-SOZ`) | 0.21 / 0.22 (309) | 21.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marie Vogt vs Nahjime Dho -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223100:270164:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nahjime Dho (`KXITFWMATCH-26OCT29VOGDHO-DHO`) | 0.04 / 0.07 (46) | 5.5% | 13.3% | 7.4% | 24.7% [19.6%-31.5%] | -- | -- | -- | -- | PASS | +7.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marie Vogt (`KXITFWMATCH-26OCT29VOGDHO-VOG`) | 0.88 / 0.97 (279) | 92.5% | 86.7% | 92.6% | 75.3% [68.5%-80.5%] | -- | -- | -- | -- | PASS | -5.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2280.0, B 464.0; serve-point win A 56.6%, B 51.7%; Elo A 1415.5, B 1287.0; model uncertainty 0.0597
* Form inputs: days since last match A 17, B 303; matches on record A 164, B 9; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.051, surface_pool_high -0.049, surface_dev_loose +0.013, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arthur Fery vs Lorenzo Musetti -- ATP Vienna R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-29 15:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-29 16:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: 2026-10-29 15:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (TOUR_500_250) · Clay · scheduled 2026-10-29T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207518:209259:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arthur Fery (`KXATPMATCH-26OCT29FERMUS-FER`) | 0.26 / 0.27 (147) | 26.5% | 20.2% | 24.6% | 20.8% [18.2%-23.5%] | 29.4% | -- | 29.4% | KALSHI_LONE_OUTLIER | PASS | -6.2 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Lorenzo Musetti (`KXATPMATCH-26OCT29FERMUS-MUS`) | 0.72 / 0.74 (30613) | 73.0% | 79.8% | 75.4% | 79.2% [76.5%-81.8%] | 70.6% | -- | 70.6% | KALSHI_LONE_OUTLIER | SHADOW_BET | +6.8 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4544.0, B 5110.0; serve-point win A 58.6%, B 34.8%; Elo A 1761.2, B 2129.7; model uncertainty 0.0263
* Form inputs: days since last match A 2, B 3; matches on record A 265, B 488; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.007, surface_dev_loose -0.025, surface_dev_tight +0.027
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPSETWINNER-26OCT29FERMUS-2-FER` Will Arthur Fery win set 2 in the Arthur Fery vs Lorenzo Musetti match: 0.02/0.98 mid 50.0%, model 28.9% (projection_v2.0 (prediction ledger)) -- gap -21.1 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT29FERMUS-2-MUS` Will Lorenzo Musetti win set 2 in the Arthur Fery vs Lorenzo Musetti match: 0.02/0.98 mid 50.0%, model 71.1% (projection_v2.0 (prediction ledger)) -- gap +21.1 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29FERMUS-FER21` Will Arthur Fery win the Arthur Fery vs Lorenzo Musetti match by a set score of 2-1?: 0.07/0.38 mid 22.5%, model 11.9% (projection_v2.0 (prediction ledger)) -- gap -10.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29FERMUS-FER20` Will Arthur Fery win the Arthur Fery vs Lorenzo Musetti match by a set score of 2-0?: 0.12/0.20 mid 16.0%, model 8.4% (projection_v2.0 (prediction ledger)) -- gap -7.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT29FERMUS-FER2` Will Arthur Fery win at least 1.5 more games than Lorenzo Musetti?: 0.19/0.26 mid 22.5%, model 15.4% (projection_v2.0 (prediction ledger)) -- gap -7.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29FERMUS-MUS21` Will Lorenzo Musetti win the Arthur Fery vs Lorenzo Musetti match by a set score of 2-1?: 0.18/0.29 mid 23.5%, model 29.2% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT29FERMUS-23` Over 22.5 games: 0.44/0.46 mid 45.0%, model 49.6% (projection_v2.0 (prediction ledger)) -- gap +4.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT29FERMUS-MUS4` Will Lorenzo Musetti win at least 3.5 more games than Arthur Fery?: 0.52/0.54 mid 53.0%, model 57.1% (projection_v2.0 (prediction ledger)) -- gap +4.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29FERMUS-1-MUS` Will Lorenzo Musetti win set 1 in the Arthur Fery vs Lorenzo Musetti match: 0.66/0.68 mid 67.0%, model 71.1% (projection_v2.0 (prediction ledger)) -- gap +4.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT29FERMUS-1-FER` Will Arthur Fery win set 1 in the Arthur Fery vs Lorenzo Musetti match: 0.32/0.33 mid 32.5%, model 28.9% (projection_v2.0 (prediction ledger)) -- gap -3.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29FERMUS-MUS20` Will Lorenzo Musetti win the Arthur Fery vs Lorenzo Musetti match by a set score of 2-0?: 0.44/0.53 mid 48.5%, model 50.5% (projection_v2.0 (prediction ledger)) -- gap +2.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT29FERMUS-28` Over 27.5 games: 0.27/0.32 mid 29.5%, model 30.9% (projection_v2.0 (prediction ledger)) -- gap +1.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT29FERMUS-MUS7` Will Lorenzo Musetti win at least 6.5 more games than Arthur Fery?: 0.15/0.19 mid 17.0%, model 15.8% (projection_v2.0 (prediction ledger)) -- gap -1.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT29FERMUS-18` Over 17.5 games: 0.84/0.90 mid 87.0%, model 86.5% (projection_v2.0 (prediction ledger)) -- gap -0.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Anavatan / Mert Ozdemir vs Brouwer / Verbeek -- M15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29ANAMERBROVER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anavatan / Mert Ozdemir (`KXITFDOUBLES-26OCT29ANAMERBROVER-ANAMER`) | 0.38 / 0.63 (67) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Brouwer / Verbeek (`KXITFDOUBLES-26OCT29ANAMERBROVER-BROVER`) | 0.31 / 0.56 (56) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Kharlamov / Shebekin vs Hrazdil / Lakshmanan -- M15 Fergana QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29KHASHEHRALAK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hrazdil / Lakshmanan (`KXITFDOUBLES-26OCT29KHASHEHRALAK-HRALAK`) | 0.30 / 0.55 (55) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kharlamov / Shebekin (`KXITFDOUBLES-26OCT29KHASHEHRALAK-KHASHE`) | 0.39 / 0.64 (69) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Sharma / Singh vs Aregger / Waldner -- M15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29SHASINAREWAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aregger / Waldner (`KXITFDOUBLES-26OCT29SHASINAREWAL-AREWAL`) | 0.15 / 0.39 (40) | 27.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sharma / Singh (`KXITFDOUBLES-26OCT29SHASINAREWAL-SHASIN`) | 0.53 / 0.78 (113) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Elizaveta Anikina vs Vlada Mincheva -- W15 Taby R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29ANIMIN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elizaveta Anikina (`KXITFWMATCH-26OCT29ANIMIN-ANI`) | 0.52 / 0.68 (1) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vlada Mincheva (`KXITFWMATCH-26OCT29ANIMIN-MIN`) | 0.22 / 0.40 (1) | 31.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Atay / Medvedeva vs Bosman / Nozdrachova -- W15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29ATAMEDBOSNOZ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Atay / Medvedeva (`KXITFWDOUBLES-26OCT29ATAMEDBOSNOZ-ATAMED`) | 0.06 / 0.95 (16) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bosman / Nozdrachova (`KXITFWDOUBLES-26OCT29ATAMEDBOSNOZ-BOSNOZ`) | 0.06 / 0.95 (2) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Vladlena Bokova vs Iva Marinkovic -- W15 Taby R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29BOKMAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vladlena Bokova (`KXITFWMATCH-26OCT29BOKMAR-BOK`) | 0.03 / 0.94 (1) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Iva Marinkovic (`KXITFWMATCH-26OCT29BOKMAR-MAR`) | 0.06 / 0.94 (1) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alicia Dudeney vs Ivana Sebestova -- W75 Glasgow R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220740:260206:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alicia Dudeney (`KXITFWMATCH-26OCT29DUDSEB-DUD`) | 0.93 / 0.95 (281) | 94.0% | 92.2% | 91.7% | 88.2% [81.8%-91.5%] | -- | -- | -- | -- | PASS | -1.8 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ivana Sebestova (`KXITFWMATCH-26OCT29DUDSEB-SEB`) | 0.05 / 0.06 (588) | 5.5% | 7.8% | 8.3% | 11.8% [8.5%-18.2%] | -- | -- | -- | -- | PASS | +2.3 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3238.0, B 946.0; serve-point win A 59.9%, B 50.7%; Elo A 1665.7, B 1358.3; model uncertainty 0.0485
* Form inputs: days since last match A 20, B 38; matches on record A 94, B 277; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.022, surface_pool_high +0.020, surface_dev_loose -0.008, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ella Haavisto vs Laetitia Pulchartova -- W15 Taby R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216107:219965:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ella Haavisto (`KXITFWMATCH-26OCT29HAAPUL-HAA`) | 0.77 / 0.82 (288) | 79.5% | 74.1% | 64.1% | 65.1% [58.5%-72.2%] | 81.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.4 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Laetitia Pulchartova (`KXITFWMATCH-26OCT29HAAPUL-PUL`) | 0.16 / 0.17 (2) | 16.5% | 25.9% | 35.9% | 34.9% [27.8%-41.5%] | 18.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +9.4 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1672.0, B 287.0; serve-point win A 55.6%, B 49.2%; Elo A 1414.5, B 1301.4; model uncertainty 0.0685
* Form inputs: days since last match A 240, B 205; matches on record A 139, B 169; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.067, surface_pool_high -0.066, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Caijsa Wilda Hennemann vs Julita Saner -- W15 Taby R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215926:216385:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Caijsa Wilda Hennemann (`KXITFWMATCH-26OCT29HENSAN-HEN`) | 0.89 / 0.95 (2) | 92.0% | 90.1% | 89.1% | 82.3% [75.3%-87.3%] | -- | -- | -- | -- | PASS | -1.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Julita Saner (`KXITFWMATCH-26OCT29HENSAN-SAN`) | 0.05 / 0.09 (47) | 7.0% | 9.9% | 10.9% | 17.7% [12.7%-24.7%] | -- | -- | -- | -- | PASS | +2.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2350.0, B 382.0; serve-point win A 57.0%, B 52.6%; Elo A 1608.5, B 1362.9; model uncertainty 0.0597
* Form inputs: days since last match A 184, B 191; matches on record A 313, B 250; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.050, surface_pool_high -0.070, surface_dev_loose +0.003, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Suzan Lamens vs Angella Okutoyi -- W75 Glasgow R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215480:222454:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Suzan Lamens (`KXITFWMATCH-26OCT29LAMOKU-LAM`) | 0.81 / 0.84 (146) | 82.5% | 62.7% | 25.6% | 44.1% [33.4%-65.1%] | 79.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -19.8 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Angella Okutoyi (`KXITFWMATCH-26OCT29LAMOKU-OKU`) | 0.15 / 0.16 (495) | 15.5% | 37.3% | 74.4% | 55.9% [34.9%-66.6%] | 20.6% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +21.8 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3938.0, B 1838.0; serve-point win A 54.2%, B 48.2%; Elo A 1724.8, B 1587.6; model uncertainty 0.1586
* Form inputs: days since last match A 23, B 296; matches on record A 545, B 109; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT29LAMOKU-OKU  (YES = Angella Okutoyi)
Model: 37%
Kalshi: 16%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.005, surface_dev_loose +0.011, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mathilde Lollia vs Margaux Maquet -- W75 Poitiers R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220875:221443:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mathilde Lollia (`KXITFWMATCH-26OCT29LOLMAQ-LOL`) | 0.40 / 0.42 (27) | 41.0% | 21.8% | 10.1% | 19.7% [13.2%-38.0%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -19.2 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Margaux Maquet (`KXITFWMATCH-26OCT29LOLMAQ-MAQ`) | 0.55 / 0.60 (34) | 57.5% | 78.2% | 89.9% | 80.3% [62.1%-86.8%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +20.7 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2163.0, B 1564.0; serve-point win A 52.0%, B 42.1%; Elo A 1429.9, B 1539.6; model uncertainty 0.1236
* Form inputs: days since last match A 13, B 198; matches on record A 177, B 78; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT29LOLMAQ-MAQ  (YES = Margaux Maquet)
Model: 78%
Kalshi: 57%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.027, surface_pool_high -0.021, surface_dev_loose -0.028, surface_dev_tight +0.026
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eliz Maloney vs Daniela Vismane -- W75 Glasgow R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215144:216340:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eliz Maloney (`KXITFWMATCH-26OCT29MALVIS-MAL`) | 0.57 / 0.62 (31) | 59.5% | 44.1% | 79.4% | 46.3% [36.0%-58.9%] | 59.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.4 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daniela Vismane (`KXITFWMATCH-26OCT29MALVIS-VIS`) | 0.36 / 0.38 (242) | 37.0% | 55.9% | 20.6% | 53.7% [41.1%-64.0%] | 40.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +18.9 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 886.0, B 336.0; serve-point win A 55.6%, B 43.2%; Elo A 1415.2, B 1493.1; model uncertainty 0.1146
* Form inputs: days since last match A 205, B 184; matches on record A 211, B 354; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT29MALVIS-VIS  (YES = Daniela Vismane)
Model: 56%
Kalshi: 37%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.031, surface_pool_high +0.042, surface_dev_loose +0.016, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Veronika Podrez vs Manon Leonard -- W75 Poitiers R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215807:247669:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Manon Leonard (`KXITFWMATCH-26OCT29PODLEO-LEO`) | 0.35 / 0.38 (32) | 36.5% | 20.6% | 21.7% | 26.2% [23.7%-31.1%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.9 pp | HIGH_REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Veronika Podrez (`KXITFWMATCH-26OCT29PODLEO-POD`) | 0.61 / 0.64 (30) | 62.5% | 79.4% | 78.3% | 73.8% [68.9%-76.3%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +16.9 pp | HIGH_REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3466.0, B 3201.0; serve-point win A 58.5%, B 47.7%; Elo A 1719.9, B 1624.9; model uncertainty 0.0373
* Form inputs: days since last match A 34, B 135; matches on record A 227, B 348; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT29PODLEO-POD  (YES = Veronika Podrez)
Model: 79%
Kalshi: 62%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.027, surface_dev_loose +0.009, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alex Michelsen / Botic Van de Zandschulp vs Theo Arribage / Albano Olivetti -- ATP Basel QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-29 13:00Z
* Current expected start: 2026-10-29 16:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: 2026-10-29 15:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-29T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29MICVANARROLI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theo Arribage / Albano Olivetti (`KXATPDOUBLES-26OCT29MICVANARROLI-ARROLI`) | 0.39 / 0.94 (1200) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alex Michelsen / Botic Van de Zandschulp (`KXATPDOUBLES-26OCT29MICVANARROLI-MICVAN`) | 0.06 / 0.61 (45) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Alexander Zverev vs Tallon Griekspoor -- ATP Vienna R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-29 15:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-29 16:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: 2026-10-29 15:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (TOUR_500_250) · Clay · scheduled 2026-10-29T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:100644:134868:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tallon Griekspoor (`KXATPMATCH-26OCT29ZVEGRI-GRI`) | 0.21 / 0.22 (803) | 21.5% | 15.1% | 11.4% | 12.3% [11.7%-13.6%] | 22.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexander Zverev (`KXATPMATCH-26OCT29ZVEGRI-ZVE`) | 0.78 / 0.79 (46022) | 78.5% | 84.9% | 88.6% | 87.6% [86.4%-88.3%] | 77.5% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +6.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 8099.0, B 5028.0; serve-point win A 71.3%, B 37.2%; Elo A 2160.4, B 1871.1; model uncertainty 0.0095
* Form inputs: days since last match A 11, B 3; matches on record A 936, B 691; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.002, surface_pool_high +0.000, surface_dev_loose +0.006, surface_dev_tight -0.007
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT29ZVEGRI-ZVE20` Will Alexander Zverev win the Alexander Zverev vs Tallon Griekspoor match by a set score of 2-0?: 0.05/0.57 mid 31.0%, model 56.9% (projection_v2.0 (prediction ledger)) -- gap +25.9 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29ZVEGRI-GRI21` Will Tallon Griekspoor win the Alexander Zverev vs Tallon Griekspoor match by a set score of 2-1?: 0.07/0.51 mid 29.0%, model 9.1% (projection_v2.0 (prediction ledger)) -- gap -19.9 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29ZVEGRI-GRI20` Will Tallon Griekspoor win the Alexander Zverev vs Tallon Griekspoor match by a set score of 2-0?: 0.02/0.44 mid 23.0%, model 6.0% (projection_v2.0 (prediction ledger)) -- gap -17.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29ZVEGRI-2-ZVE` Will Alexander Zverev win set 2 in the Alexander Zverev vs Tallon Griekspoor match: 0.37/0.89 mid 63.0%, model 75.4% (projection_v2.0 (prediction ledger)) -- gap +12.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT29ZVEGRI-ZVE2` Will Alexander Zverev win at least 1.5 more games than Tallon Griekspoor?: 0.67/0.73 mid 70.0%, model 79.5% (projection_v2.0 (prediction ledger)) -- gap +9.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT29ZVEGRI-ZVE5` Will Alexander Zverev win at least 4.5 more games than Tallon Griekspoor?: 0.28/0.29 mid 28.5%, model 37.9% (projection_v2.0 (prediction ledger)) -- gap +9.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29ZVEGRI-2-GRI` Will Tallon Griekspoor win set 2 in the Alexander Zverev vs Tallon Griekspoor match: 0.09/0.58 mid 33.5%, model 24.6% (projection_v2.0 (prediction ledger)) -- gap -8.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT29ZVEGRI-22` Over 21.5 games: 0.67/0.71 mid 69.0%, model 60.4% (projection_v2.0 (prediction ledger)) -- gap -8.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29ZVEGRI-ZVE21` Will Alexander Zverev win the Alexander Zverev vs Tallon Griekspoor match by a set score of 2-1?: 0.11/0.29 mid 20.0%, model 28.0% (projection_v2.0 (prediction ledger)) -- gap +8.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29ZVEGRI-1-GRI` Will Tallon Griekspoor win set 1 in the Alexander Zverev vs Tallon Griekspoor match: 0.26/0.28 mid 27.0%, model 24.6% (projection_v2.0 (prediction ledger)) -- gap -2.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT29ZVEGRI-1-ZVE` Will Alexander Zverev win set 1 in the Alexander Zverev vs Tallon Griekspoor match: 0.72/0.74 mid 73.0%, model 75.4% (projection_v2.0 (prediction ledger)) -- gap +2.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT29ZVEGRI-27` Over 26.5 games: 0.33/0.38 mid 35.5%, model 34.1% (projection_v2.0 (prediction ledger)) -- gap -1.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT29ZVEGRI-17` Over 16.5 games: 0.96/0.99 mid 97.5%, model 96.2% (projection_v2.0 (prediction ledger)) -- gap -1.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Leo Borg vs Cezar Cretu -- M25 Malta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206470:209863:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leo Borg (`KXITFMATCH-26OCT29BORCRE-BOR`) | 0.24 / 0.27 (100) | 25.5% | 45.9% | 56.8% | 54.2% [45.8%-59.4%] | 27.6% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +20.4 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Cezar Cretu (`KXITFMATCH-26OCT29BORCRE-CRE`) | 0.70 / 0.76 (180) | 73.0% | 54.1% | 43.2% | 45.8% [40.6%-54.2%] | 72.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -18.9 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3869.0, B 4025.0; serve-point win A 57.3%, B 42.0%; Elo A 1470.5, B 1482.5; model uncertainty 0.0677
* Form inputs: days since last match A 184, B 16; matches on record A 287, B 422; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT29BORCRE-BOR  (YES = Leo Borg)
Model: 46%
Kalshi: 26%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.016, surface_dev_loose +0.052, surface_dev_tight -0.047
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Manas Dhamne vs Aleksandr Braynin -- M25 Malta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202089:211768:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aleksandr Braynin (`KXITFMATCH-26OCT29DHABRA-BRA`) | 0.20 / 0.22 (417) | 21.0% | 27.1% | 34.2% | 33.8% [29.2%-35.7%] | -- | -- | -- | -- | WATCH | +6.1 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Manas Dhamne (`KXITFMATCH-26OCT29DHABRA-DHA`) | 0.75 / 0.79 (24) | 77.0% | 72.9% | 65.8% | 66.2% [64.3%-70.8%] | -- | -- | -- | -- | PASS | -4.1 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3842.0, B 3428.0; serve-point win A 60.5%, B 44.1%; Elo A 1479.3, B 1350.3; model uncertainty 0.0326
* Form inputs: days since last match A 51, B 198; matches on record A 148, B 231; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.019, surface_dev_loose -0.005, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Garrett Johns vs Leyton Rivera -- M25 Malta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208143:208864:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Garrett Johns (`KXITFMATCH-26OCT29JOHRIV-JOH`) | 0.85 / 0.92 (105) | 88.5% | 87.7% | 85.2% | 86.7% [85.2%-87.7%] | 87.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.8 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Leyton Rivera (`KXITFMATCH-26OCT29JOHRIV-RIV`) | 0.09 / 0.11 (6) | 10.0% | 12.3% | 14.8% | 13.3% [12.3%-14.8%] | 12.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.3 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4190.0, B 1841.0; serve-point win A 64.3%, B 44.7%; Elo A 1515.3, B 1155.8; model uncertainty 0.0126
* Form inputs: days since last match A 65, B 184; matches on record A 270, B 81; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.006, surface_dev_loose +0.008, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Roan Jones vs Viktor Durasovic -- M25 Sheffield QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126340:210422:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Viktor Durasovic (`KXITFMATCH-26OCT29JONDUR-DUR`) | 0.72 / 0.75 (9) | 73.5% | 91.7% | 80.0% | 85.5% [83.7%-87.6%] | 73.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +18.2 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Roan Jones (`KXITFMATCH-26OCT29JONDUR-JON`) | 0.25 / 0.26 (100) | 25.5% | 8.3% | 20.1% | 14.5% [12.4%-16.3%] | 26.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -17.2 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 195.0, B 3973.0; serve-point win A 54.6%, B 34.6%; Elo A 1224.8, B 1544.6; model uncertainty 0.0198
* Form inputs: days since last match A 443, B 16; matches on record A 6, B 730; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT29JONDUR-DUR  (YES = Viktor Durasovic)
Model: 92%
Kalshi: 74%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.018, surface_dev_loose -0.003, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oliver Tarvet vs Mika Petkovic -- M25 Sheffield QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210472:213001:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mika Petkovic (`KXITFMATCH-26OCT29TARPET-PET`) | 0.15 / 0.17 (487) | 16.0% | 20.3% | 22.0% | 19.8% [18.1%-22.0%] | 19.5% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +4.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oliver Tarvet (`KXITFMATCH-26OCT29TARPET-TAR`) | 0.81 / 0.84 (1) | 82.5% | 79.7% | 78.0% | 80.2% [78.0%-82.0%] | 80.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1816.0, B 3316.0; serve-point win A 63.6%, B 42.8%; Elo A 1714.8, B 1441.2; model uncertainty 0.0197
* Form inputs: days since last match A 23, B 30; matches on record A 88, B 102; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.004, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Josy Daems vs Emily Victoria Eigelsbach -- W15 Essen QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260539:270401:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Josy Daems (`KXITFWMATCH-26OCT29DAEEIG-DAE`) | 0.58 / 0.62 (19) | 60.0% | 79.7% | 64.1% | 67.1% [64.6%-70.3%] | -- | -- | -- | -- | PASS | +19.7 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Emily Victoria Eigelsbach (`KXITFWMATCH-26OCT29DAEEIG-EIG`) | 0.34 / 0.39 (4) | 36.5% | 20.3% | 35.9% | 32.9% [29.7%-35.4%] | -- | -- | -- | -- | PASS | -16.2 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2580.0, B 237.0; serve-point win A 56.8%, B 49.5%; Elo A 1484.9, B 1355.1; model uncertainty 0.0285
* Form inputs: days since last match A 226, B 101; matches on record A 103, B 4; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT29DAEEIG-DAE  (YES = Josy Daems)
Model: 80%
Kalshi: 60%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.024, surface_pool_high -0.025, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Clarissa Gai vs Anja Stankovic -- W35 Malta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220596:244087:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Clarissa Gai (`KXITFWMATCH-26OCT29GAISTA-GAI`) | 0.03 / 0.19 (30) | 11.0% | 14.3% | 37.5% | 22.0% [20.5%-23.2%] | -- | -- | -- | -- | PASS | +3.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anja Stankovic (`KXITFWMATCH-26OCT29GAISTA-STA`) | 0.74 / 0.97 (329) | 85.5% | 85.7% | 62.5% | 78.0% [76.8%-79.5%] | -- | -- | -- | -- | PASS | +0.2 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 244.0, B 2297.0; serve-point win A 51.2%, B 40.8%; Elo A 1257.6, B 1499.8; model uncertainty 0.0137
* Form inputs: days since last match A 366, B 247; matches on record A 33, B 192; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.004, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Emma Sophie Glaser vs Emma Slavikova -- W15 Essen QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29GLASLA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emma Sophie Glaser (`KXITFWMATCH-26OCT29GLASLA-GLA`) | 0.54 / 0.58 (261) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Emma Slavikova (`KXITFWMATCH-26OCT29GLASLA-SLA`) | 0.38 / 0.45 (39) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pia Lovric vs Antonina Sushkova -- W35 Malta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222458:266849:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pia Lovric (`KXITFWMATCH-26OCT29LOVSUS-LOV`) | 0.57 / 0.61 (57) | 59.0% | 72.8% | 51.1% | 68.1% [64.7%-73.1%] | -- | -- | -- | -- | PASS | +13.8 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Antonina Sushkova (`KXITFWMATCH-26OCT29LOVSUS-SUS`) | 0.38 / 0.41 (33) | 39.5% | 27.3% | 48.9% | 31.9% [26.9%-35.3%] | -- | -- | -- | -- | PASS | -12.2 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1631.0, B 527.0; serve-point win A 52.9%, B 51.6%; Elo A 1467.6, B 1288.5; model uncertainty 0.0423
* Form inputs: days since last match A 17, B 254; matches on record A 300, B 11; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.000, surface_dev_loose -0.010, surface_dev_tight +0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maryia Magro vs Angelica Raggi -- W35 Malta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216051:270309:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maryia Magro (`KXITFWMATCH-26OCT29MAGRAG-MAG`) | 0.03 / 0.05 (48) | 4.0% | 7.6% | 35.3% | 21.0% [18.1%-22.6%] | -- | -- | -- | -- | PASS | +3.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Angelica Raggi (`KXITFWMATCH-26OCT29MAGRAG-RAG`) | 0.93 / 0.97 (210) | 95.0% | 92.3% | 64.7% | 79.0% [77.4%-81.9%] | -- | -- | -- | -- | PASS | -2.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 165.0, B 2349.0; serve-point win A 45.8%, B 43.5%; Elo A 1259.9, B 1503.9; model uncertainty 0.0224
* Form inputs: days since last match A 317, B 191; matches on record A 3, B 320; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.016, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lian Tran vs Tilwith Di Girolami -- W15 Essen QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220560:228910:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tilwith Di Girolami (`KXITFWMATCH-26OCT29TRADIG-DIG`) | 0.56 / 0.58 (45) | 57.0% | 51.3% | 81.2% | 60.1% [44.7%-70.4%] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -5.7 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lian Tran (`KXITFWMATCH-26OCT29TRADIG-TRA`) | 0.42 / 0.46 (8) | 44.0% | 48.7% | 18.8% | 40.0% [29.6%-55.3%] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.7 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1204.0, B 1533.0; serve-point win A 52.7%, B 47.0%; Elo A 1505.4, B 1440.2; model uncertainty 0.1287
* Form inputs: days since last match A 184, B 184; matches on record A 307, B 202; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Novak Djokovic vs Jan-Lennard Struff -- ATP Basel R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-29 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-29 17:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: 2026-10-29 16:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (TOUR_500_250) · Hard · scheduled 2026-10-29T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:104925:105526:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Novak Djokovic (`KXATPMATCH-26OCT29DJOSTR-DJO`) | 0.75 / 0.76 (82) | 75.5% | 85.7% | 78.1% | 82.7% [80.8%-85.4%] | 74.5% | -- | 74.5% | MODEL_LONE_OUTLIER | SHADOW_BET | +10.2 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Jan-Lennard Struff (`KXATPMATCH-26OCT29DJOSTR-STR`) | 0.24 / 0.25 (24190) | 24.5% | 14.3% | 21.9% | 17.3% [14.6%-19.1%] | 25.5% | -- | 25.5% | MODEL_LONE_OUTLIER | PASS | -10.2 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4375.0, B 5412.0; serve-point win A 72.3%, B 36.6%; Elo A 2254.7, B 1818.1; model uncertainty 0.0229
* Form inputs: days since last match A 19, B 3; matches on record A 1503, B 1071; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.006, surface_dev_loose -0.001, surface_dev_tight +0.007
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT29DJOSTR-STR21` Will Jan-Lennard Struff win the Novak Djokovic vs Jan-Lennard Struff match by a set score of 2-1?: 0.08/0.75 mid 41.5%, model 8.6% (projection_v2.0 (prediction ledger)) -- gap -32.9 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29DJOSTR-2-DJO` Will Novak Djokovic win set 2 in the Novak Djokovic vs Jan-Lennard Struff match: 0.02/0.98 mid 50.0%, model 76.2% (projection_v2.0 (prediction ledger)) -- gap +26.2 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT29DJOSTR-2-STR` Will Jan-Lennard Struff win set 2 in the Novak Djokovic vs Jan-Lennard Struff match: 0.02/0.98 mid 50.0%, model 23.8% (projection_v2.0 (prediction ledger)) -- gap -26.2 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT29DJOSTR-DJO7` Will Novak Djokovic win at least 6.5 more games than Jan-Lennard Struff?: 0.07/0.42 mid 24.5%, model 10.2% (projection_v2.0 (prediction ledger)) -- gap -14.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29DJOSTR-DJO20` Will Novak Djokovic win the Novak Djokovic vs Jan-Lennard Struff match by a set score of 2-0?: 0.40/0.53 mid 46.5%, model 58.0% (projection_v2.0 (prediction ledger)) -- gap +11.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT29DJOSTR-STR2` Will Jan-Lennard Struff win at least 1.5 more games than Novak Djokovic?: 0.17/0.22 mid 19.5%, model 10.0% (projection_v2.0 (prediction ledger)) -- gap -9.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29DJOSTR-DJO21` Will Novak Djokovic win the Novak Djokovic vs Jan-Lennard Struff match by a set score of 2-1?: 0.02/0.38 mid 20.0%, model 27.6% (projection_v2.0 (prediction ledger)) -- gap +7.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT29DJOSTR-DJO4` Will Novak Djokovic win at least 3.5 more games than Jan-Lennard Struff?: 0.48/0.50 mid 49.0%, model 56.4% (projection_v2.0 (prediction ledger)) -- gap +7.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29DJOSTR-1-DJO` Will Novak Djokovic win set 1 in the Novak Djokovic vs Jan-Lennard Struff match: 0.68/0.71 mid 69.5%, model 76.2% (projection_v2.0 (prediction ledger)) -- gap +6.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT29DJOSTR-1-STR` Will Jan-Lennard Struff win set 1 in the Novak Djokovic vs Jan-Lennard Struff match: 0.29/0.32 mid 30.5%, model 23.8% (projection_v2.0 (prediction ledger)) -- gap -6.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29DJOSTR-STR20` Will Jan-Lennard Struff win the Novak Djokovic vs Jan-Lennard Struff match by a set score of 2-0?: 0.10/0.13 mid 11.5%, model 5.7% (projection_v2.0 (prediction ledger)) -- gap -5.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT29DJOSTR-29` Over 28.5 games: 0.27/0.32 mid 29.5%, model 28.8% (projection_v2.0 (prediction ledger)) -- gap -0.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT29DJOSTR-19` Over 18.5 games: 0.83/0.87 mid 85.0%, model 84.8% (projection_v2.0 (prediction ledger)) -- gap -0.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT29DJOSTR-24` Over 23.5 games: 0.42/0.44 mid 43.0%, model 42.9% (projection_v2.0 (prediction ledger)) -- gap -0.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jake Fellows vs Simone Massellani -- M15 Selva Gardena QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212654:214436:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jake Fellows (`KXITFMATCH-26OCT29FELMAS-FEL`) | 0.26 / 0.30 (124) | 28.0% | 65.5% | 59.3% | 73.5% [72.7%-74.4%] | 28.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +37.5 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Simone Massellani (`KXITFMATCH-26OCT29FELMAS-MAS`) | 0.68 / 0.72 (206) | 70.0% | 34.5% | 40.7% | 26.5% [25.6%-27.3%] | 71.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -35.5 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 104.0, B 263.0; serve-point win A 59.6%, B 43.5%; Elo A 1422.8, B 1236.9; model uncertainty 0.0086
* Form inputs: days since last match A 184, B 16; matches on record A 2, B 7; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT29FELMAS-FEL  (YES = Jake Fellows)
Model: 65%
Kalshi: 28%
Gap: +37 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Giovanni Oradini vs Andrea Colombo -- M15 Selva Gardena QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132831:149267:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrea Colombo (`KXITFMATCH-26OCT29ORACOL-COL`) | 0.24 / 0.29 (244) | 26.5% | 21.3% | 23.2% | 21.3% [20.2%-23.5%] | 28.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.2 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Giovanni Oradini (`KXITFMATCH-26OCT29ORACOL-ORA`) | 0.72 / 0.73 (163) | 72.5% | 78.7% | 76.8% | 78.7% [76.5%-79.8%] | 72.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +6.2 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2852.0, B 1312.0; serve-point win A 67.6%, B 38.8%; Elo A 1436.6, B 1200.6; model uncertainty 0.0164
* Form inputs: days since last match A 37, B 184; matches on record A 337, B 31; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose -0.005, surface_dev_tight +0.002
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tessa Johanna Brockmann vs Elena Malygina -- W75 Glasgow R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216116:260598:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tessa Johanna Brockmann (`KXITFWMATCH-26OCT29BROMAL-BRO`) | 0.42 / 0.45 (60) | 43.5% | 44.9% | 26.2% | 33.5% [28.8%-46.3%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elena Malygina (`KXITFWMATCH-26OCT29BROMAL-MAL`) | 0.53 / 0.56 (21) | 54.5% | 55.1% | 73.9% | 66.5% [53.7%-71.2%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3426.0, B 2298.0; serve-point win A 54.5%, B 44.5%; Elo A 1598.4, B 1620.4; model uncertainty 0.0873
* Form inputs: days since last match A 15, B 33; matches on record A 169, B 440; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.010, surface_dev_loose -0.024, surface_dev_tight +0.029
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Iushchenko / Turkmen vs Bennemann / Schunk -- W50 Istanbul QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29IUSTURBENSCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bennemann / Schunk (`KXITFWDOUBLES-26OCT29IUSTURBENSCH-BENSCH`) | 0.05 / 0.96 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Iushchenko / Turkmen (`KXITFWDOUBLES-26OCT29IUSTURBENSCH-IUSTUR`) | 0.05 / 0.96 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kubareva / Yashina vs Sedysheva / Smirnova -- W50 Istanbul QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29KUBYASSEDSMI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kubareva / Yashina (`KXITFWDOUBLES-26OCT29KUBYASSEDSMI-KUBYAS`) | 0.05 / 0.96 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sedysheva / Smirnova (`KXITFWDOUBLES-26OCT29KUBYASSEDSMI-SEDSMI`) | 0.05 / 0.96 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kuzmova / Novak vs Golovina / Milovanova -- W50 Istanbul QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29KUZNOVGOLMIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Golovina / Milovanova (`KXITFWDOUBLES-26OCT29KUZNOVGOLMIL-GOLMIL`) | 0.06 / 0.95 (2) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kuzmova / Novak (`KXITFWDOUBLES-26OCT29KUZNOVGOLMIL-KUZNOV`) | 0.06 / 0.95 (16) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Amelia Rajecki vs Ella Seidel -- W75 Glasgow R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221945:230870:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amelia Rajecki (`KXITFWMATCH-26OCT29RAJSEI-RAJ`) | 0.33 / 0.38 (40) | 35.5% | 23.5% | 58.6% | 43.9% [30.6%-50.5%] | 36.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -12.0 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ella Seidel (`KXITFWMATCH-26OCT29RAJSEI-SEI`) | 0.61 / 0.65 (39) | 63.0% | 76.5% | 41.4% | 56.1% [49.5%-69.4%] | 63.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.5 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2501.0, B 4408.0; serve-point win A 58.5%, B 35.8%; Elo A 1537.8, B 1748.3; model uncertainty 0.0996
* Form inputs: days since last match A 29, B 57; matches on record A 142, B 283; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.010, surface_dev_loose +0.015, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valentina Steiner vs Fiona Crawley -- W75 Glasgow R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220680:260296:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fiona Crawley (`KXITFWMATCH-26OCT29STECRA-CRA`) | 0.69 / 0.76 (329) | 72.5% | 83.4% | 66.6% | 74.0% [71.3%-76.1%] | 72.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +10.9 pp | REVIEW | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valentina Steiner (`KXITFWMATCH-26OCT29STECRA-STE`) | 0.26 / 0.27 (27) | 26.5% | 16.6% | 33.4% | 26.0% [23.9%-28.7%] | 28.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.9 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1525.0, B 2695.0; serve-point win A 49.7%, B 43.0%; Elo A 1511.4, B 1754.6; model uncertainty 0.0239
* Form inputs: days since last match A 34, B 19; matches on record A 78, B 131; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose -0.009, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Horwood / Lawlor vs Bozemoj / Pel -- M25 Sheffield SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29HORLAWBOZPEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bozemoj / Pel (`KXITFDOUBLES-26OCT29HORLAWBOZPEL-BOZPEL`) | 0.04 / 0.96 (11) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Horwood / Lawlor (`KXITFDOUBLES-26OCT29HORLAWBOZPEL-HORLAW`) | 0.04 / 0.96 (11) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Matt Ponchet vs Martin Krumich -- M25 Sheffield QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209322:210328:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martin Krumich (`KXITFMATCH-26OCT29PONKRU-KRU`) | 0.84 / 0.91 (100) | 87.5% | 84.4% | 79.5% | 82.2% [79.8%-86.0%] | -- | -- | -- | -- | PASS | -3.1 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matt Ponchet (`KXITFMATCH-26OCT29PONKRU-PON`) | 0.06 / 0.12 (128) | 9.0% | 15.6% | 20.5% | 17.8% [14.0%-20.2%] | -- | -- | -- | -- | WATCH | +6.6 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1205.0, B 5586.0; serve-point win A 58.5%, B 33.5%; Elo A 1253.5, B 1542.4; model uncertainty 0.0309
* Form inputs: days since last match A 233, B 23; matches on record A 56, B 371; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.024, surface_dev_loose -0.009, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Victoria Pohle vs Leticia Solakov -- W15 Essen QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260433:267630:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Victoria Pohle (`KXITFWMATCH-26OCT29POHSOL-POH`) | 0.60 / 0.63 (38) | 61.5% | 86.1% | 61.1% | 64.6% [63.6%-67.1%] | 62.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +24.6 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Leticia Solakov (`KXITFWMATCH-26OCT29POHSOL-SOL`) | 0.35 / 0.39 (33) | 37.0% | 13.9% | 38.9% | 35.4% [32.9%-36.4%] | 37.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -23.1 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1323.0, B 216.0; serve-point win A 56.5%, B 51.6%; Elo A 1367.6, B 1256.1; model uncertainty 0.0174
* Form inputs: days since last match A 198, B 247; matches on record A 46, B 5; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT29POHSOL-POH  (YES = Victoria Pohle)
Model: 86%
Kalshi: 62%
Gap: +25 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lola Radivojevic vs Gina Marie Dittmann -- W75 Poitiers R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222273:236957:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gina Marie Dittmann (`KXITFWMATCH-26OCT29RADDIT-DIT`) | 0.11 / 0.14 (59) | 12.5% | 15.8% | 17.5% | 20.4% [18.9%-23.8%] | 15.5% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +3.4 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lola Radivojevic (`KXITFWMATCH-26OCT29RADDIT-RAD`) | 0.85 / 0.89 (372) | 87.0% | 84.2% | 82.5% | 79.6% [76.2%-81.1%] | 84.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.9 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3394.0, B 1885.0; serve-point win A 61.3%, B 46.4%; Elo A 1605.3, B 1412.4; model uncertainty 0.0243
* Form inputs: days since last match A 22, B 205; matches on record A 294, B 115; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.015, surface_dev_loose +0.010, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bacaloni / Knani vs Hammes / Sanchez Martinez -- M15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29BACKNAHAMSAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bacaloni / Knani (`KXITFDOUBLES-26OCT29BACKNAHAMSAN-BACKNA`) | 0.05 / 0.14 (29) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hammes / Sanchez Martinez (`KXITFDOUBLES-26OCT29BACKNAHAMSAN-HAMSAN`) | 0.81 / 0.96 (16) | 88.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Alberto Bronzetti vs James MacKinlay -- M25 Malta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208216:208905:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alberto Bronzetti (`KXITFMATCH-26OCT29BROMAC-BRO`) | 0.31 / 0.71 (3) | 51.0% | 82.7% | 82.1% | 67.5% [65.1%-70.2%] | -- | -- | -- | -- | PASS | +31.7 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| James MacKinlay (`KXITFMATCH-26OCT29BROMAC-MAC`) | 0.38 / 0.52 (2) | 45.0% | 17.3% | 17.9% | 32.5% [29.8%-34.8%] | -- | -- | -- | -- | PASS | -27.7 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 922.0, B 153.0; serve-point win A 63.4%, B 43.9%; Elo A 1273.3, B 1157.1; model uncertainty 0.0252
* Form inputs: days since last match A 212, B 478; matches on record A 54, B 7; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT29BROMAC-BRO  (YES = Alberto Bronzetti)
Model: 83%
Kalshi: 51%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Facek / Panik vs Djonov / Tepmahc -- M15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29FACPANDJOTEP:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Djonov / Tepmahc (`KXITFDOUBLES-26OCT29FACPANDJOTEP-DJOTEP`) | 0.45 / 0.71 (86) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Facek / Panik (`KXITFDOUBLES-26OCT29FACPANDJOTEP-FACPAN`) | 0.24 / 0.49 (49) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Maximilian Figl vs Lorenzo Bocchi -- M15 Selva Gardena QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200595:211904:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Bocchi (`KXITFMATCH-26OCT29FIGBOC-BOC`) | 0.73 / 0.79 (188) | 76.0% | 73.9% | 76.8% | 74.8% [71.9%-76.4%] | 75.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.1 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maximilian Figl (`KXITFMATCH-26OCT29FIGBOC-FIG`) | 0.22 / 0.23 (5) | 22.5% | 26.1% | 23.2% | 25.2% [23.6%-28.1%] | 24.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.6 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1358.0, B 2132.0; serve-point win A 58.3%, B 36.7%; Elo A 1191.5, B 1362.7; model uncertainty 0.0225
* Form inputs: days since last match A 184, B 184; matches on record A 60, B 308; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.017, surface_dev_loose -0.016, surface_dev_tight +0.017
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Philip Henning vs Dmitry Popko -- M25 Malta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:122078:202475:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Philip Henning (`KXITFMATCH-26OCT29HENPOP-HEN`) | 0.61 / 0.64 (30) | 62.5% | 59.0% | 80.2% | 73.6% [62.2%-78.8%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -3.5 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dmitry Popko (`KXITFMATCH-26OCT29HENPOP-POP`) | 0.31 / 0.38 (132) | 34.5% | 41.0% | 19.8% | 26.4% [21.2%-37.9%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.5 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3868.0, B 3275.0; serve-point win A 61.5%, B 40.3%; Elo A 1598.6, B 1545.9; model uncertainty 0.083
* Form inputs: days since last match A 16, B 114; matches on record A 215, B 828; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.026, surface_pool_high +0.029, surface_dev_loose +0.008, surface_dev_tight -0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Wojciech Marek vs Manuel Plunger -- M15 Selva Gardena QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207457:211708:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wojciech Marek (`KXITFMATCH-26OCT29MARPLU-MAR`) | 0.54 / 0.58 (148) | 56.0% | 64.0% | 58.2% | 63.2% [62.8%-64.1%] | 56.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +8.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Manuel Plunger (`KXITFMATCH-26OCT29MARPLU-PLU`) | 0.39 / 0.45 (136) | 42.0% | 36.0% | 41.8% | 36.8% [35.9%-37.2%] | 43.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 160.0, B 306.0; serve-point win A 61.0%, B 41.8%; Elo A 1326.2, B 1230.7; model uncertainty 0.0069
* Form inputs: days since last match A 1549, B 499; matches on record A 84, B 39; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Neos / Tsitsipas vs Blanchar / De Felipe Garcia -- M25 Malta QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29NEOTSIBLADEF:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Blanchar / De Felipe Garcia (`KXITFDOUBLES-26OCT29NEOTSIBLADEF-BLADEF`) | 0.04 / 0.96 (11) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Neos / Tsitsipas (`KXITFDOUBLES-26OCT29NEOTSIBLADEF-NEOTSI`) | 0.04 / 0.96 (11) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Vladyslav Orlov vs Daniel Masur -- M25 Malta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:109054:200550:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Masur (`KXITFMATCH-26OCT29ORLMAS-MAS`) | 0.73 / 0.78 (208) | 75.5% | 73.2% | 77.5% | 76.3% [73.1%-78.9%] | 76.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.3 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Vladyslav Orlov (`KXITFMATCH-26OCT29ORLMAS-ORL`) | 0.22 / 0.24 (110) | 23.0% | 26.8% | 22.5% | 23.7% [21.1%-26.9%] | 24.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.8 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3570.0, B 4231.0; serve-point win A 59.0%, B 36.2%; Elo A 1391.2, B 1563.3; model uncertainty 0.0292
* Form inputs: days since last match A 184, B 37; matches on record A 550, B 772; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.026, surface_dev_tight +0.032
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dibenedetto / Gandolfi vs Shkutova / Struvay -- W15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29DIBGANSHKSTR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dibenedetto / Gandolfi (`KXITFWDOUBLES-26OCT29DIBGANSHKSTR-DIBGAN`) | 0.05 / 0.96 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Shkutova / Struvay (`KXITFWDOUBLES-26OCT29DIBGANSHKSTR-SHKSTR`) | 0.05 / 0.96 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ewald / Sramkova vs Adeshina / Grammatikopoulou -- W35 Malta QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29EWASRAADEGRA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adeshina / Grammatikopoulou (`KXITFWDOUBLES-26OCT29EWASRAADEGRA-ADEGRA`) | 0.54 / 0.80 (125) | 67.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ewald / Sramkova (`KXITFWDOUBLES-26OCT29EWASRAADEGRA-EWASRA`) | 0.13 / 0.38 (40) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Chelsea Fontenel vs Joy De Zeeuw -- W35 Malta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:239454:260226:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joy De Zeeuw (`KXITFWMATCH-26OCT29FONDEZ-DEZ`) | 0.50 / 0.56 (56) | 53.0% | 53.8% | 36.8% | 44.3% [41.3%-53.7%] | -- | -- | -- | -- | PASS | +0.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Chelsea Fontenel (`KXITFWMATCH-26OCT29FONDEZ-FON`) | 0.41 / 0.45 (45) | 43.0% | 46.2% | 63.2% | 55.7% [46.3%-58.7%] | -- | -- | -- | -- | PASS | +3.2 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2027.0, B 2042.0; serve-point win A 59.1%, B 40.2%; Elo A 1365.0, B 1406.8; model uncertainty 0.062
* Form inputs: days since last match A 191, B 394; matches on record A 114, B 70; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.010, surface_dev_tight -0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Komano / Xu vs Husar / Srutwa -- W15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29KOMXUXHUSSRU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Husar / Srutwa (`KXITFWDOUBLES-26OCT29KOMXUXHUSSRU-HUSSRU`) | 0.05 / 0.96 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Komano / Xu (`KXITFWDOUBLES-26OCT29KOMXUXHUSSRU-KOMXUX`) | 0.05 / 0.96 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sada Nahimana vs Harmony Tan -- W75 Poitiers R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211552:216367:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sada Nahimana (`KXITFWMATCH-26OCT29NAHTAN-NAH`) | 0.11 / 0.15 (138) | 13.0% | 17.2% | 8.8% | 14.1% [11.2%-22.6%] | -- | -- | -- | -- | PASS | +4.2 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Harmony Tan (`KXITFWMATCH-26OCT29NAHTAN-TAN`) | 0.86 / 0.88 (98) | 87.0% | 82.8% | 91.1% | 85.9% [77.4%-88.8%] | -- | -- | -- | -- | PASS | -4.2 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2636.0, B 3731.0; serve-point win A 53.9%, B 38.9%; Elo A 1540.8, B 1710.5; model uncertainty 0.0569
* Form inputs: days since last match A 161, B 14; matches on record A 369, B 652; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.006, surface_pool_high +0.003, surface_dev_loose -0.029, surface_dev_tight +0.028
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Olivia Hansen / Roots vs Grekul / Norin -- W15 Taby QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29OLIROOGRENOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Grekul / Norin (`KXITFWDOUBLES-26OCT29OLIROOGRENOR-GRENOR`) | 0.21 / 0.46 (46) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Olivia Hansen / Roots (`KXITFWDOUBLES-26OCT29OLIROOGRENOR-OLIROO`) | 0.48 / 0.74 (96) | 61.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Ben Shelton vs Jerome Kym -- ATP Basel R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-29 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-29 18:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: 2026-10-29 17:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (TOUR_500_250) · Hard · scheduled 2026-10-29T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208843:210097:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jerome Kym (`KXATPMATCH-26OCT29SHEKYM-KYM`) | 0.26 / 0.27 (39283) | 26.5% | 20.3% | 32.5% | 26.1% [22.4%-28.4%] | 26.7% | -- | 26.7% | MODEL_LONE_OUTLIER | PASS | -6.2 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Ben Shelton (`KXATPMATCH-26OCT29SHEKYM-SHE`) | 0.74 / 0.75 (53884) | 74.5% | 79.7% | 67.5% | 73.9% [71.6%-77.6%] | 73.4% | -- | 73.4% | MODEL_LONE_OUTLIER | PASS | +5.2 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 6529.0, B 3871.0; serve-point win A 73.5%, B 33.6%; Elo A 2080.2, B 1736.9; model uncertainty 0.03
* Form inputs: days since last match A 1, B 1; matches on record A 316, B 278; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.007, surface_dev_loose -0.000, surface_dev_tight +0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT29SHEKYM-SHE20` Will Ben Shelton win the Ben Shelton vs Jerome Kym match by a set score of 2-0?: 0.06/0.50 mid 28.0%, model 50.5% (projection_v2.0 (prediction ledger)) -- gap +22.5 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29SHEKYM-SHE21` Will Ben Shelton win the Ben Shelton vs Jerome Kym match by a set score of 2-1?: 0.02/0.29 mid 15.5%, model 29.2% (projection_v2.0 (prediction ledger)) -- gap +13.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29SHEKYM-KYM20` Will Jerome Kym win the Ben Shelton vs Jerome Kym match by a set score of 2-0?: 0.02/0.41 mid 21.5%, model 8.4% (projection_v2.0 (prediction ledger)) -- gap -13.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29SHEKYM-2-SHE` Will Ben Shelton win set 2 in the Ben Shelton vs Jerome Kym match: 0.35/0.83 mid 59.0%, model 71.1% (projection_v2.0 (prediction ledger)) -- gap +12.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT29SHEKYM-SHE3` Will Ben Shelton win at least 2.5 more games than Jerome Kym?: 0.54/0.55 mid 54.5%, model 60.8% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT29SHEKYM-KYM2` Will Jerome Kym win at least 1.5 more games than Ben Shelton?: 0.17/0.23 mid 20.0%, model 14.4% (projection_v2.0 (prediction ledger)) -- gap -5.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29SHEKYM-2-KYM` Will Jerome Kym win set 2 in the Ben Shelton vs Jerome Kym match: 0.11/0.58 mid 34.5%, model 28.9% (projection_v2.0 (prediction ledger)) -- gap -5.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29SHEKYM-KYM21` Will Jerome Kym win the Ben Shelton vs Jerome Kym match by a set score of 2-1?: 0.02/0.15 mid 8.5%, model 11.9% (projection_v2.0 (prediction ledger)) -- gap +3.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29SHEKYM-1-SHE` Will Ben Shelton win set 1 in the Ben Shelton vs Jerome Kym match: 0.67/0.69 mid 68.0%, model 71.1% (projection_v2.0 (prediction ledger)) -- gap +3.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT29SHEKYM-1-KYM` Will Jerome Kym win set 1 in the Ben Shelton vs Jerome Kym match: 0.31/0.32 mid 31.5%, model 28.9% (projection_v2.0 (prediction ledger)) -- gap -2.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT29SHEKYM-25` Over 24.5 games: 0.50/0.52 mid 51.0%, model 50.2% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT29SHEKYM-30` Over 29.5 games: 0.32/0.33 mid 32.5%, model 33.0% (projection_v2.0 (prediction ledger)) -- gap +0.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT29SHEKYM-SHE6` Will Ben Shelton win at least 5.5 more games than Jerome Kym?: 0.09/0.14 mid 11.5%, model 11.9% (projection_v2.0 (prediction ledger)) -- gap +0.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT29SHEKYM-20` Over 19.5 games: 0.82/0.86 mid 84.0%, model 84.1% (projection_v2.0 (prediction ledger)) -- gap +0.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## De Carvalho / van Wyk vs Bouchelaghem / Goran Verwerft -- M15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29DECVANBOUGOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bouchelaghem / Goran Verwerft (`KXITFDOUBLES-26OCT29DECVANBOUGOR-BOUGOR`) | 0.60 / 0.85 (166) | 72.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| De Carvalho / van Wyk (`KXITFDOUBLES-26OCT29DECVANBOUGOR-DECVAN`) | 0.08 / 0.33 (37) | 20.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Ouakaa / Sahtali vs Corbinais / Alexandru Teglas -- M15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29OUASAHCORALE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Corbinais / Alexandru Teglas (`KXITFDOUBLES-26OCT29OUASAHCORALE-CORALE`) | 0.04 / 0.28 (34) | 16.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ouakaa / Sahtali (`KXITFDOUBLES-26OCT29OUASAHCORALE-OUASAH`) | 0.65 / 0.96 (11) | 80.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Aikawa / Vismane vs Hodzic / Sebestova -- W75 Glasgow QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29AIKVISHODSEB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aikawa / Vismane (`KXITFWDOUBLES-26OCT29AIKVISHODSEB-AIKVIS`) | 0.05 / 0.96 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hodzic / Sebestova (`KXITFWDOUBLES-26OCT29AIKVISHODSEB-HODSEB`) | 0.05 / 0.97 (116) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Christie / Silva vs Dada-Mascoll / Okutoyi -- W75 Glasgow QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29CHRSILDADOKU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Christie / Silva (`KXITFWDOUBLES-26OCT29CHRSILDADOKU-CHRSIL`) | 0.21 / 0.92 (30) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dada-Mascoll / Okutoyi (`KXITFWDOUBLES-26OCT29CHRSILDADOKU-DADOKU`) | 0.06 / 0.79 (0) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Laura Hietaranta vs Mona Barthel -- W75 Glasgow R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:201621:222397:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mona Barthel (`KXITFWMATCH-26OCT29HIEBAR-BAR`) | 0.87 / 0.91 (610) | 89.0% | 87.5% | 85.5% | 83.7% [79.3%-86.3%] | 86.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.5 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Laura Hietaranta (`KXITFWMATCH-26OCT29HIEBAR-HIE`) | 0.09 / 0.12 (804) | 10.5% | 12.5% | 14.5% | 16.3% [13.7%-20.7%] | 13.3% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +2.0 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2514.0, B 4076.0; serve-point win A 53.7%, B 37.5%; Elo A 1472.0, B 1704.2; model uncertainty 0.0349
* Form inputs: days since last match A 191, B 16; matches on record A 244, B 944; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.006, surface_dev_loose -0.026, surface_dev_tight +0.030
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lazarenko / Rutlauka vs Maria Mihail / Moneva -- W15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29LAZRUTMARMON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lazarenko / Rutlauka (`KXITFWDOUBLES-26OCT29LAZRUTMARMON-LAZRUT`) | 0.89 / 0.96 (32) | 92.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maria Mihail / Moneva (`KXITFWDOUBLES-26OCT29LAZRUTMARMON-MARMON`) | 0.05 / 0.07 (26) | 6.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Leonard / Monnot vs Jorge / Jorge -- W75 Poitiers QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29LEOMONJORJOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jorge / Jorge (`KXITFWDOUBLES-26OCT29LEOMONJORJOR-JORJOR`) | 0.87 / 0.96 (30) | 91.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Leonard / Monnot (`KXITFWDOUBLES-26OCT29LEOMONJORJOR-LEOMON`) | 0.05 / 0.09 (27) | 7.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Flavio Cobolli vs Matteo Berrettini -- ATP Vienna R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-28 15:30Z
* Current expected start: 2026-10-29 19:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-29 00:10Z
* Recommended handicap-by time: 2026-10-29 18:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1650_MIN

ATP (TOUR_500_250) · Clay · scheduled 2026-10-28T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126610:207925:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Berrettini (`KXATPMATCH-26OCT28COBBER-BER`) | 0.49 / 0.50 (7360) | 49.5% | 50.3% | 49.5% | 49.0% [47.1%-51.5%] | -- | -- | -- | -- | PASS | +0.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Flavio Cobolli (`KXATPMATCH-26OCT28COBBER-COB`) | 0.51 / 0.52 (31823) | 51.5% | 49.7% | 50.5% | 51.0% [48.5%-52.9%] | -- | -- | -- | -- | PASS | -1.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6575.0, B 4151.0; serve-point win A 66.2%, B 33.7%; Elo A 1977.5, B 1971.4; model uncertainty 0.0219
* Form inputs: days since last match A 1, B 2; matches on record A 455, B 563; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.015, surface_dev_loose +0.019, surface_dev_tight -0.024
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT28COBBER-COB21` Will Flavio Cobolli win the Flavio Cobolli vs Matteo Berrettini match by a set score of 2-1?: 0.02/0.28 mid 15.0%, model 24.9% (projection_v2.0 (prediction ledger)) -- gap +9.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT28COBBER-30` Over 29.5 games: 0.24/0.28 mid 26.0%, model 35.2% (projection_v2.0 (prediction ledger)) -- gap +9.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT28COBBER-25` Over 24.5 games: 0.48/0.49 mid 48.5%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap +7.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT28COBBER-2-COB` Will Flavio Cobolli win set 2 in the Flavio Cobolli vs Matteo Berrettini match: 0.15/0.74 mid 44.5%, model 49.8% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT28COBBER-20` Over 19.5 games: 0.78/0.83 mid 80.5%, model 84.8% (projection_v2.0 (prediction ledger)) -- gap +4.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT28COBBER-BER20` Will Matteo Berrettini win the Flavio Cobolli vs Matteo Berrettini match by a set score of 2-0?: 0.27/0.31 mid 29.0%, model 25.2% (projection_v2.0 (prediction ledger)) -- gap -3.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT28COBBER-COB20` Will Flavio Cobolli win the Flavio Cobolli vs Matteo Berrettini match by a set score of 2-0?: 0.26/0.30 mid 28.0%, model 24.8% (projection_v2.0 (prediction ledger)) -- gap -3.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT28COBBER-BER5` Will Matteo Berrettini win at least 4.5 more games than Flavio Cobolli?: 0.14/0.19 mid 16.5%, model 13.7% (projection_v2.0 (prediction ledger)) -- gap -2.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT28COBBER-BER21` Will Matteo Berrettini win the Flavio Cobolli vs Matteo Berrettini match by a set score of 2-1?: 0.20/0.26 mid 23.0%, model 25.1% (projection_v2.0 (prediction ledger)) -- gap +2.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT28COBBER-2-BER` Will Matteo Berrettini win set 2 in the Flavio Cobolli vs Matteo Berrettini match: 0.20/0.77 mid 48.5%, model 50.2% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT28COBBER-BER2` Will Matteo Berrettini win at least 1.5 more games than Flavio Cobolli?: 0.42/0.45 mid 43.5%, model 42.2% (projection_v2.0 (prediction ledger)) -- gap -1.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT28COBBER-COB2` Will Flavio Cobolli win at least 1.5 more games than Matteo Berrettini?: 0.42/0.43 mid 42.5%, model 41.6% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT28COBBER-1-COB` Will Flavio Cobolli win set 1 in the Flavio Cobolli vs Matteo Berrettini match: 0.48/0.51 mid 49.5%, model 49.8% (projection_v2.0 (prediction ledger)) -- gap +0.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT28COBBER-1-BER` Will Matteo Berrettini win set 1 in the Flavio Cobolli vs Matteo Berrettini match: 0.49/0.51 mid 50.0%, model 50.2% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## bautista de la Pena vs Fermin Tenti -- M15 João Pessoa R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-29T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202275:214016:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bautista de la Pena (`KXITFMATCH-26OCT29DELTEN-DEL`) | 0.32 / 0.33 (37) | 32.5% | 22.4% | 11.4% | 20.5% [14.1%-29.0%] | 40.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -10.1 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Fermin Tenti (`KXITFMATCH-26OCT29DELTEN-TEN`) | 0.57 / 0.65 (48) | 61.0% | 77.6% | 88.6% | 79.5% [71.0%-85.9%] | 59.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +16.6 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 803.0, B 1735.0; serve-point win A 52.7%, B 41.5%; Elo A 1120.6, B 1292.1; model uncertainty 0.0745
* Form inputs: days since last match A 226, B 114; matches on record A 15, B 367; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT29DELTEN-TEN  (YES = Fermin Tenti)
Model: 78%
Kalshi: 61%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.004, surface_dev_loose -0.018, surface_dev_tight +0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Juan Pablo Ficovich vs Dante Pagani -- M15 João Pessoa R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-29T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126663:213677:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Pablo Ficovich (`KXITFMATCH-26OCT29FICPAG-FIC`) | 0.63 / 0.89 (32) | 76.0% | 86.3% | 75.0% | 81.2% [79.3%-83.0%] | -- | -- | -- | -- | PASS | +10.3 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dante Pagani (`KXITFMATCH-26OCT29FICPAG-PAG`) | 0.07 / 0.30 (35) | 18.5% | 13.7% | 25.0% | 18.8% [17.0%-20.6%] | -- | -- | -- | -- | PASS | -4.8 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4206.0, B 964.0; serve-point win A 60.8%, B 47.5%; Elo A 1579.8, B 1287.0; model uncertainty 0.0184
* Form inputs: days since last match A 9, B 184; matches on record A 723, B 23; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.007, surface_dev_loose +0.001, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ignacio Monzon vs Rocco Valente -- M15 João Pessoa R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-29T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:133820:212260:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ignacio Monzon (`KXITFMATCH-26OCT29MONVAL-MON`) | 0.61 / 0.85 (22) | 73.0% | 82.3% | 80.5% | 80.2% [78.2%-82.3%] | -- | -- | -- | -- | PASS | +9.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rocco Valente (`KXITFMATCH-26OCT29MONVAL-VAL`) | 0.11 / 0.32 (36) | 21.5% | 17.7% | 19.5% | 19.8% [17.7%-21.8%] | -- | -- | -- | -- | PASS | -3.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3341.0, B 719.0; serve-point win A 59.6%, B 47.4%; Elo A 1356.6, B 1123.4; model uncertainty 0.0207
* Form inputs: days since last match A 114, B 226; matches on record A 427, B 38; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.007, surface_dev_loose +0.007, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valentina Abril Bruno vs Angela Morena Medinaceli Lobos -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29BRUMED:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valentina Abril Bruno (`KXITFWMATCH-26OCT29BRUMED-BRU`) | 0.87 / 0.93 (2) | 90.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Angela Morena Medinaceli Lobos (`KXITFWMATCH-26OCT29BRUMED-MED`) | 0.04 / 0.09 (20) | 6.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Paola Lopez vs Emily Zornada -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-29T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:266374:270329:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Paola Lopez (`KXITFWMATCH-26OCT29LOPZOR-LOP`) | 0.47 / 0.50 (19) | 48.5% | 34.1% | 22.2% | 39.4% [37.4%-40.5%] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -14.4 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Emily Zornada (`KXITFWMATCH-26OCT29LOPZOR-ZOR`) | 0.46 / 0.51 (66) | 48.5% | 66.0% | 77.8% | 60.6% [59.5%-62.6%] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +17.4 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 943.0, B 106.0; serve-point win A 50.4%, B 46.5%; Elo A 1234.7, B 1300.7; model uncertainty 0.0156
* Form inputs: days since last match A 191, B 212; matches on record A 81, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT29LOPZOR-ZOR  (YES = Emily Zornada)
Model: 66%
Kalshi: 48%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Diana Martynov vs Jenny Lim -- W75 Poitiers R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221157:247647:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jenny Lim (`KXITFWMATCH-26OCT29MARLIM-LIM`) | 0.60 / 0.69 (87) | 64.5% | 63.1% | 76.9% | 70.3% [59.5%-74.8%] | 65.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.4 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Diana Martynov (`KXITFWMATCH-26OCT29MARLIM-MAR`) | 0.31 / 0.36 (56) | 33.5% | 36.9% | 23.1% | 29.6% [25.2%-40.5%] | 34.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.4 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1861.0, B 2154.0; serve-point win A 52.8%, B 44.7%; Elo A 1465.8, B 1542.2; model uncertainty 0.0764
* Form inputs: days since last match A 52, B 198; matches on record A 329, B 185; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.014, surface_dev_loose -0.009, surface_dev_tight +0.019
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofia Meabe vs Ana Julieta Lopez Ocampos -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-29T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:266446:269888:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ana Julieta Lopez Ocampos (`KXITFWMATCH-26OCT29MEALOP-LOP`) | 0.09 / 0.11 (5) | 10.0% | 15.8% | 68.6% | 32.4% [31.4%-33.4%] | -- | -- | -- | -- | PASS | +5.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sofia Meabe (`KXITFWMATCH-26OCT29MEALOP-MEA`) | 0.87 / 0.89 (65) | 88.0% | 84.2% | 31.4% | 67.6% [66.6%-68.6%] | -- | -- | -- | -- | PASS | -3.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 235.0, B 0.0; serve-point win A 55.8%, B 51.7%; Elo A 1346.8, B 1218.6; model uncertainty 0.01
* Form inputs: days since last match A 282, B 723; matches on record A 18, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ciric / Giraldi vs Braynin / Kravchenko -- M25 Malta QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29CIRGIRBRAKRA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Braynin / Kravchenko (`KXITFDOUBLES-26OCT29CIRGIRBRAKRA-BRAKRA`) | 0.04 / 0.96 (11) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ciric / Giraldi (`KXITFDOUBLES-26OCT29CIRGIRBRAKRA-CIRGIR`) | 0.04 / 0.96 (11) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Maric / Radovanovic vs Delicata / Stamatopoulos -- M25 Malta QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29MARRADDELSTA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Delicata / Stamatopoulos (`KXITFDOUBLES-26OCT29MARRADDELSTA-DELSTA`) | 0.15 / 0.39 (40) | 27.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maric / Radovanovic (`KXITFDOUBLES-26OCT29MARRADDELSTA-MARRAD`) | 0.55 / 0.80 (125) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Cassani / Genovese vs Lovric / Stankovic -- W35 Malta QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 19:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29CASGENLOVSTA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cassani / Genovese (`KXITFWDOUBLES-26OCT29CASGENLOVSTA-CASGEN`) | 0.05 / 0.14 (29) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lovric / Stankovic (`KXITFWDOUBLES-26OCT29CASGENLOVSTA-LOVSTA`) | 0.81 / 0.97 (116) | 89.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Gardiner / Romanova vs Malygina / Rajecki -- W75 Glasgow QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 19:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29GARROMMALRAJ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gardiner / Romanova (`KXITFWDOUBLES-26OCT29GARROMMALRAJ-GARROM`) | 0.05 / 0.07 (26) | 6.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Malygina / Rajecki (`KXITFWDOUBLES-26OCT29GARROMMALRAJ-MALRAJ`) | 0.87 / 0.97 (116) | 92.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Hannah Klugman vs Sofya Lansere -- W75 Glasgow R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216139:263872:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hannah Klugman (`KXITFWMATCH-26OCT29KLULAN-KLU`) | 0.71 / 0.76 (75) | 73.5% | 45.3% | 38.4% | 43.6% [40.5%-49.5%] | -- | -- | -- | -- | PASS | -28.2 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sofya Lansere (`KXITFWMATCH-26OCT29KLULAN-LAN`) | 0.18 / 0.28 (9) | 23.0% | 54.7% | 61.6% | 56.4% [50.5%-59.5%] | -- | -- | -- | -- | PASS | +31.7 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1658.0, B 3253.0; serve-point win A 53.0%, B 46.1%; Elo A 1636.2, B 1643.0; model uncertainty 0.0449
* Form inputs: days since last match A 121, B 26; matches on record A 78, B 351; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT29KLULAN-LAN  (YES = Sofya Lansere)
Model: 55%
Kalshi: 23%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.021, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marie Dittmann / Otzipka vs Marcinkevica / Partaud -- W75 Poitiers QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 19:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29MAROTZMARPAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marie Dittmann / Otzipka (`KXITFWDOUBLES-26OCT29MAROTZMARPAR-MAROTZ`) | 0.05 / 0.96 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marcinkevica / Partaud (`KXITFWDOUBLES-26OCT29MAROTZMARPAR-MARPAR`) | 0.05 / 0.96 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Paganetti / Urgesi vs Easwaramurthi / Magro -- W35 Malta QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 19:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29PAGURGEASMAG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Easwaramurthi / Magro (`KXITFWDOUBLES-26OCT29PAGURGEASMAG-EASMAG`) | 0.05 / 0.06 (26) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Paganetti / Urgesi (`KXITFWDOUBLES-26OCT29PAGURGEASMAG-PAGURG`) | 0.89 / 0.97 (116) | 93.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Tian / ZAPARYNIUK vs Fehr / Perera Vega -- W35 Malta QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 19:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29TIAZAPFEHPER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fehr / Perera Vega (`KXITFWDOUBLES-26OCT29TIAZAPFEHPER-FEHPER`) | 0.05 / 0.75 (9) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tian / ZAPARYNIUK (`KXITFWDOUBLES-26OCT29TIAZAPFEHPER-TIAZAP`) | 0.18 / 0.92 (30) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nicolas Bruna vs Bastian Malla -- M15 João Pessoa R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-29T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:109334:202220:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Bruna (`KXITFMATCH-26OCT29BRUMAL-BRU`) | 0.10 / 0.36 (39) | 23.0% | 17.2% | 13.1% | 15.1% [12.6%-18.9%] | -- | -- | -- | -- | PASS | -5.8 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Bastian Malla (`KXITFMATCH-26OCT29BRUMAL-MAL`) | 0.56 / 0.84 (156) | 70.0% | 82.8% | 86.9% | 84.9% [81.1%-87.4%] | -- | -- | -- | -- | PASS | +12.8 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1663.0, B 1148.0; serve-point win A 55.1%, B 37.6%; Elo A 1175.9, B 1450.1; model uncertainty 0.0317
* Form inputs: days since last match A 184, B 198; matches on record A 130, B 430; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high -0.000, surface_dev_loose -0.003, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Fryer / McKay vs Gannon / Nirundorn -- M25 Sheffield SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29FRYMCKGANNIR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fryer / McKay (`KXITFDOUBLES-26OCT29FRYMCKGANNIR-FRYMCK`) | 0.04 / 0.96 (11) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gannon / Nirundorn (`KXITFDOUBLES-26OCT29FRYMCKGANNIR-GANNIR`) | 0.04 / 0.96 (11) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Oscar Jose Gutierrez vs Leonardo Storck Franca -- M15 João Pessoa R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-29T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:121264:214148:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oscar Jose Gutierrez (`KXITFMATCH-26OCT29GUTSTO-GUT`) | 0.56 / 0.60 (48) | 58.0% | 72.6% | 66.4% | 63.4% [62.3%-65.5%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +14.6 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Leonardo Storck Franca (`KXITFMATCH-26OCT29GUTSTO-STO`) | 0.38 / 0.42 (11) | 40.0% | 27.4% | 33.6% | 36.5% [34.5%-37.7%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.6 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2766.0, B 159.0; serve-point win A 59.0%, B 45.6%; Elo A 1315.8, B 1225.7; model uncertainty 0.0161
* Form inputs: days since last match A 198, B 345; matches on record A 606, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jose Escurra Isnardi / Vitor Scramin do Lago vs Lima / Schenekenberg -- M15 João Pessoa QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29JOSVITLIMSCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jose Escurra Isnardi / Vitor Scramin do Lago (`KXITFDOUBLES-26OCT29JOSVITLIMSCH-JOSVIT`) | 0.28 / 0.54 (54) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lima / Schenekenberg (`KXITFDOUBLES-26OCT29JOSVITLIMSCH-LIMSCH`) | 0.40 / 0.67 (75) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Ayana Akli vs Hiromi Abe -- W75 Toronto R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221362:264149:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hiromi Abe (`KXITFWMATCH-26OCT29AKLABE-ABE`) | 0.48 / 0.51 (6) | 49.5% | 52.8% | 53.7% | 52.6% [50.5%-54.8%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.3 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ayana Akli (`KXITFWMATCH-26OCT29AKLABE-AKL`) | 0.47 / 0.52 (52) | 49.5% | 47.2% | 46.3% | 47.3% [45.2%-49.5%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.3 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2838.0, B 2555.0; serve-point win A 55.0%, B 44.5%; Elo A 1612.6, B 1619.2; model uncertainty 0.0212
* Form inputs: days since last match A 37, B 226; matches on record A 123, B 200; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.021, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Angelina Abendroth / Angelique Abendroth vs Schuknecht / Schweika -- W15 Essen SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29ANGANGSCHSCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Angelina Abendroth / Angelique Abendroth (`KXITFWDOUBLES-26OCT29ANGANGSCHSCH-ANGANG`) | 0.05 / 0.96 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Schuknecht / Schweika (`KXITFWDOUBLES-26OCT29ANGANGSCHSCH-SCHSCH`) | 0.05 / 0.96 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Melissa Boyden vs Josefina Estevez -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-29T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222274:260717:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Melissa Boyden (`KXITFWMATCH-26OCT29BOYEST-BOY`) | 0.03 / 0.11 (28) | 7.0% | 34.9% | 26.4% | 38.4% [32.4%-45.7%] | -- | -- | -- | -- | PASS | +27.9 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Josefina Estevez (`KXITFWMATCH-26OCT29BOYEST-EST`) | 0.83 / 0.97 (279) | 90.0% | 65.0% | 73.6% | 61.6% [54.3%-67.6%] | -- | -- | -- | -- | PASS | -24.9 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 765.0, B 732.0; serve-point win A 47.5%, B 49.6%; Elo A 1254.1, B 1294.6; model uncertainty 0.0666
* Form inputs: days since last match A 198, B 289; matches on record A 91, B 55; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT29BOYEST-BOY  (YES = Melissa Boyden)
Model: 35%
Kalshi: 7%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.020, surface_dev_loose -0.015, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Teah Chavez vs Lea Ma -- W75 Toronto R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221220:260374:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Teah Chavez (`KXITFWMATCH-26OCT29CHAMAX-CHA`) | 0.22 / 0.25 (7) | 23.5% | 10.2% | 19.8% | 19.1% [17.2%-20.9%] | -- | -- | -- | -- | PASS | -13.3 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lea Ma (`KXITFWMATCH-26OCT29CHAMAX-MAX`) | 0.73 / 0.76 (2) | 74.5% | 89.8% | 80.2% | 80.9% [79.1%-82.8%] | -- | -- | -- | -- | PASS | +15.3 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 494.0, B 2727.0; serve-point win A 53.4%, B 36.9%; Elo A 1366.2, B 1614.7; model uncertainty 0.0187
* Form inputs: days since last match A 92, B 45; matches on record A 22, B 168; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT29CHAMAX-MAX  (YES = Lea Ma)
Model: 90%
Kalshi: 74%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.018, surface_dev_loose -0.003, surface_dev_tight +0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gniewkowska / Lazar vs Daems / Reusch -- W15 Essen QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29GNILAZDAEREU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daems / Reusch (`KXITFWDOUBLES-26OCT29GNILAZDAEREU-DAEREU`) | 0.05 / 0.96 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gniewkowska / Lazar (`KXITFWDOUBLES-26OCT29GNILAZDAEREU-GNILAZ`) | 0.05 / 0.96 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Adla Lopez vs Emery Combs -- W15 Sumter SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:262884:270089:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emery Combs (`KXITFWMATCH-26OCT29LOPCOM-COM`) | 0.37 / 0.65 (71) | 51.0% | 81.2% | 57.4% | 64.6% [64.5%-64.6%] | -- | -- | -- | -- | PASS | +30.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Adla Lopez (`KXITFWMATCH-26OCT29LOPCOM-LOP`) | 0.30 / 0.57 (58) | 43.5% | 18.8% | 42.6% | 35.4% [35.4%-35.5%] | -- | -- | -- | -- | PASS | -24.7 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 528.0; serve-point win A 51.3%, B 42.1%; Elo A 1282.3, B 1384.8; model uncertainty 0.0002
* Form inputs: days since last match A 1374, B 191; matches on record A 2, B 8; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT29LOPCOM-COM  (YES = Emery Combs)
Model: 81%
Kalshi: 51%
Gap: +30 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Clemence Mercier vs Valentina Ryser -- W75 Toronto R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220489:260855:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Clemence Mercier (`KXITFWMATCH-26OCT29MERRYS-MER`) | 0.18 / 0.94 (4) | 56.0% | 9.0% | 42.2% | 19.4% [15.1%-24.2%] | -- | -- | -- | -- | PASS | -47.0 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valentina Ryser (`KXITFWMATCH-26OCT29MERRYS-RYS`) | 0.12 / 0.85 (3) | 48.5% | 91.0% | 57.8% | 80.5% [75.8%-84.9%] | -- | -- | -- | -- | PASS | +42.5 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 263.0, B 3017.0; serve-point win A 53.2%, B 36.5%; Elo A 1329.2, B 1611.7; model uncertainty 0.0454
* Form inputs: days since last match A 380, B 50; matches on record A 26, B 392; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT29MERRYS-RYS  (YES = Valentina Ryser)
Model: 91%
Kalshi: 48%
Gap: +42 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.026, surface_dev_loose -0.003, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luna Morini vs Alisa Danilova -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-29T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206161:221064:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alisa Danilova (`KXITFWMATCH-26OCT29MORDAN-DAN`) | 0.05 / 0.95 (1) | 50.0% | 43.9% | 16.8% | 38.4% [38.4%-38.4%] | -- | -- | -- | -- | PASS | -6.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Luna Morini (`KXITFWMATCH-26OCT29MORDAN-MOR`) | 0.04 / 0.96 (1) | 50.0% | 56.1% | 83.2% | 61.6% [61.6%-61.6%] | -- | -- | -- | -- | PASS | +6.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 466.0; serve-point win A 53.3%, B 47.9%; Elo A 1263.9, B 1180.2; model uncertainty 0.0001
* Form inputs: days since last match A 3117, B 184; matches on record A 1, B 31; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luciana Moyano vs Sofia Simon Padros -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-29T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:237454:270327:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luciana Moyano (`KXITFWMATCH-26OCT29MOYSIM-MOY`) | 0.05 / 0.96 (22) | 50.5% | 92.2% | 89.1% | 77.8% [77.4%-79.0%] | -- | -- | -- | -- | PASS | +41.7 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sofia Simon Padros (`KXITFWMATCH-26OCT29MOYSIM-SIM`) | 0.04 / 0.96 (1) | 50.0% | 7.8% | 10.9% | 22.2% [21.0%-22.6%] | -- | -- | -- | -- | PASS | -42.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2452.0, B 54.0; serve-point win A 55.5%, B 55.1%; Elo A 1454.4, B 1244.6; model uncertainty 0.0081
* Form inputs: days since last match A 184, B 359; matches on record A 106, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT29MOYSIM-MOY  (YES = Luciana Moyano)
Model: 92%
Kalshi: 50%
Gap: +42 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mia Robinson vs Yael Saffar -- W15 Sumter SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:269950:270469:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mia Robinson (`KXITFWMATCH-26OCT29ROBSAF-ROB`) | 0.05 / 0.95 (1) | 50.0% | 39.2% | 51.6% | 47.9% [47.9%-47.9%] | -- | -- | -- | -- | PASS | -10.8 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yael Saffar (`KXITFWMATCH-26OCT29ROBSAF-SAF`) | 0.04 / 0.96 (1) | 50.0% | 60.8% | 48.4% | 52.1% [52.1%-52.1%] | -- | -- | -- | -- | PASS | +10.8 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 288.0; serve-point win A 52.3%, B 45.6%; Elo A 1340.3, B 1353.0; model uncertainty 0.0
* Form inputs: days since last match A 716, B 191; matches on record A 3, B 4; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Malwina Rowinska vs Chiara Di Genova -- W15 Sumter SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221414:260764:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chiara Di Genova (`KXITFWMATCH-26OCT29ROWDIG-DIG`) | 0.07 / 0.95 (1) | 51.0% | 67.7% | 80.1% | 67.6% [66.6%-70.9%] | -- | -- | -- | -- | PASS | +16.7 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Malwina Rowinska (`KXITFWMATCH-26OCT29ROWDIG-ROW`) | 0.06 / 0.94 (108) | 50.0% | 32.3% | 19.9% | 32.4% [29.1%-33.4%] | -- | -- | -- | -- | PASS | -17.7 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 297.0, B 146.0; serve-point win A 50.2%, B 46.3%; Elo A 1193.6, B 1310.8; model uncertainty 0.0217
* Form inputs: days since last match A 205, B 527; matches on record A 27, B 69; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT29ROWDIG-DIG  (YES = Chiara Di Genova)
Model: 68%
Kalshi: 51%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amelie Smejkalova vs Kallista Liu -- W15 Sumter SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223359:264180:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kallista Liu (`KXITFWMATCH-26OCT29SMELIU-LIU`) | 0.36 / 0.63 (67) | 49.5% | 38.9% | 42.0% | 38.9% [37.4%-41.0%] | -- | -- | -- | -- | PASS | -10.6 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amelie Smejkalova (`KXITFWMATCH-26OCT29SMELIU-SME`) | 0.31 / 0.59 (60) | 45.0% | 61.1% | 58.0% | 61.1% [59.0%-62.6%] | -- | -- | -- | -- | PASS | +16.1 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 297.0, B 1064.0; serve-point win A 52.2%, B 49.9%; Elo A 1371.4, B 1290.6; model uncertainty 0.0179
* Form inputs: days since last match A 352, B 205; matches on record A 68, B 41; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT29SMELIU-SME  (YES = Amelie Smejkalova)
Model: 61%
Kalshi: 45%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.021, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Abanda / Vickery vs Hesse / Nahimana -- W75 Poitiers QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29ABAVICHESNAH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Abanda / Vickery (`KXITFWDOUBLES-26OCT29ABAVICHESNAH-ABAVIC`) | 0.17 / 0.44 (44) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hesse / Nahimana (`KXITFWDOUBLES-26OCT29ABAVICHESNAH-HESNAH`) | 0.50 / 0.78 (113) | 64.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Tomas Farjat vs Joao Victor Couto Loureiro -- M15 João Pessoa R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29FARCOU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joao Victor Couto Loureiro (`KXITFMATCH-26OCT29FARCOU-COU`) | 0.51 / 0.80 (125) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tomas Farjat (`KXITFMATCH-26OCT29FARCOU-FAR`) | 0.13 / 0.41 (42) | 27.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Karla Bartel vs Scarlett Fagan -- W15 Sumter SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29BARFAG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karla Bartel (`KXITFWMATCH-26OCT29BARFAG-BAR`) | 0.31 / 0.55 (10) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Scarlett Fagan (`KXITFWMATCH-26OCT29BARFAG-FAG`) | 0.41 / 0.66 (10) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Reese Brantmeier vs Clervie Ngounoue -- W75 Toronto R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29BRANGO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Reese Brantmeier (`KXITFWMATCH-26OCT29BRANGO-BRA`) | 0.13 / 0.95 (1) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Clervie Ngounoue (`KXITFWMATCH-26OCT29BRANGO-NGO`) | 0.09 / 0.93 (4) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lani Chang vs Celia Anson Sanchez -- W15 Sumter SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29CHAANS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Celia Anson Sanchez (`KXITFWMATCH-26OCT29CHAANS-ANS`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lani Chang (`KXITFWMATCH-26OCT29CHAANS-CHA`) | 0.06 / 0.96 (1) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kylie Collins vs Connie Ma -- W100 New Braunfels TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29COLMAX:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kylie Collins (`KXITFWMATCH-26OCT29COLMAX-COL`) | 0.27 / 0.37 (40) | 32.0% | -- | -- | -- [-----] | 35.6% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Connie Ma (`KXITFWMATCH-26OCT29COLMAX-MAX`) | 0.63 / 0.68 (44) | 65.5% | -- | -- | -- [-----] | 64.4% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kayla Cross vs Carson Tanguilig -- W75 Toronto R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29CROTAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kayla Cross (`KXITFWMATCH-26OCT29CROTAN-CRO`) | 0.05 / 0.83 (22) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Carson Tanguilig (`KXITFWMATCH-26OCT29CROTAN-TAN`) | 0.11 / 0.97 (279) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carlota Moreno vs Anita Sahdiieva -- W15 Sumter SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29MORSAH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlota Moreno (`KXITFWMATCH-26OCT29MORSAH-MOR`) | 0.05 / 0.96 (22) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anita Sahdiieva (`KXITFWMATCH-26OCT29MORSAH-SAH`) | 0.06 / 0.97 (279) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arantxa Rus vs Kristina Liutova -- W100 New Braunfels TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29RUSLIU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kristina Liutova (`KXITFWMATCH-26OCT29RUSLIU-LIU`) | 0.69 / 0.95 (11) | 82.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arantxa Rus (`KXITFWMATCH-26OCT29RUSLIU-RUS`) | 0.12 / 0.24 (32) | 18.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alice Soulie vs Allison Wang -- W15 Sumter SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29SOUWAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alice Soulie (`KXITFWMATCH-26OCT29SOUWAN-SOU`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Allison Wang (`KXITFWMATCH-26OCT29SOUWAN-WAN`) | 0.03 / 0.97 (279) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Allura Zamarripa vs Akasha Urhobo -- W100 New Braunfels TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29ZAMURH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Akasha Urhobo (`KXITFWMATCH-26OCT29ZAMURH-URH`) | 0.17 / 0.96 (22) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Allura Zamarripa (`KXITFWMATCH-26OCT29ZAMURH-ZAM`) | 0.04 / 0.88 (52) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Micah Braswell vs Nikita Filin -- M25 Las Vegas NV R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29BRAFIL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Micah Braswell (`KXITFMATCH-26OCT29BRAFIL-BRA`) | 0.07 / 0.96 (22) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nikita Filin (`KXITFMATCH-26OCT29BRAFIL-FIL`) | 0.06 / 0.96 (223) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cundom / Tenti vs Garay / Pagani -- M15 João Pessoa QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29CUNTENGARPAG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cundom / Tenti (`KXITFDOUBLES-26OCT29CUNTENGARPAG-CUNTEN`) | 0.59 / 0.87 (192) | 73.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Garay / Pagani (`KXITFDOUBLES-26OCT29CUNTENGARPAG-GARPAG`) | 0.07 / 0.34 (37) | 20.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Aidan Kim vs Luca Preda -- M25 Las Vegas NV R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29KIMPRE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aidan Kim (`KXITFMATCH-26OCT29KIMPRE-KIM`) | 0.06 / 0.96 (264) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luca Preda (`KXITFMATCH-26OCT29KIMPRE-PRE`) | 0.06 / 0.95 (159) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tanishk Konduri vs Felix Corwin -- M25 Las Vegas NV R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29KONCOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felix Corwin (`KXITFMATCH-26OCT29KONCOR-COR`) | 0.06 / 0.96 (264) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tanishk Konduri (`KXITFMATCH-26OCT29KONCOR-KON`) | 0.06 / 0.96 (244) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Preston Stearns vs Alejandro Arcila -- M25 Las Vegas NV R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29STEARC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alejandro Arcila (`KXITFMATCH-26OCT29STEARC-ARC`) | 0.06 / 0.96 (22) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Preston Stearns (`KXITFMATCH-26OCT29STEARC-STE`) | 0.06 / 0.95 (159) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Di Genova / Robinson vs Liu / Williams -- W15 Sumter SC QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29DIGROBLIUWIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Di Genova / Robinson (`KXITFWDOUBLES-26OCT29DIGROBLIUWIL-DIGROB`) | 0.05 / 0.96 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Liu / Williams (`KXITFWDOUBLES-26OCT29DIGROBLIUWIL-LIUWIL`) | 0.05 / 0.97 (116) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Caroline Dolehide vs Ella McDonald -- W100 New Braunfels TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29DOLMCD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Caroline Dolehide (`KXITFWMATCH-26OCT29DOLMCD-DOL`) | 0.05 / 0.96 (22) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ella McDonald (`KXITFWMATCH-26OCT29DOLMCD-MCD`) | 0.04 / 0.97 (279) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gilheany / Smejkalova vs Combs / De Los Reyes -- W15 Sumter SC QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29GILSMECOMDEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Combs / De Los Reyes (`KXITFWDOUBLES-26OCT29GILSMECOMDEL-COMDEL`) | 0.05 / 0.97 (138) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gilheany / Smejkalova (`KXITFWDOUBLES-26OCT29GILSMECOMDEL-GILSME`) | 0.05 / 0.97 (116) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Koreshkova / Simunyu vs Matis / Nicole Singeorzan -- W15 Sumter SC QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29KORSIMMATNIC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Koreshkova / Simunyu (`KXITFWDOUBLES-26OCT29KORSIMMATNIC-KORSIM`) | 0.05 / 0.96 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matis / Nicole Singeorzan (`KXITFWDOUBLES-26OCT29KORSIMMATNIC-MATNIC`) | 0.05 / 0.96 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sol Ailin Larraya Guidi vs Maria Jose Sanchez Uribe -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29LARSAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sol Ailin Larraya Guidi (`KXITFWMATCH-26OCT29LARSAN-LAR`) | 0.63 / 0.71 (58) | 67.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maria Jose Sanchez Uribe (`KXITFWMATCH-26OCT29LARSAN-SAN`) | 0.25 / 0.34 (69) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Meabe / Zornada vs Daniela Duarte / DELFINA VEGA GUDINO -- W15 Neuquén QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29MEAZORDANDEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniela Duarte / DELFINA VEGA GUDINO (`KXITFWDOUBLES-26OCT29MEAZORDANDEL-DANDEL`) | 0.05 / 0.96 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Meabe / Zornada (`KXITFWDOUBLES-26OCT29MEAZORDANDEL-MEAZOR`) | 0.05 / 0.96 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Julieta Pareja vs Barbora Palicova -- W100 New Braunfels TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29PARPAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barbora Palicova (`KXITFWMATCH-26OCT29PARPAL-PAL`) | 0.05 / 0.96 (22) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Julieta Pareja (`KXITFWMATCH-26OCT29PARPAL-PAR`) | 0.04 / 0.97 (279) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Katherine Sebov vs Thara Gowda -- W75 Toronto R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29SEBGOW:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thara Gowda (`KXITFWMATCH-26OCT29SEBGOW-GOW`) | 0.09 / 0.95 (3) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Katherine Sebov (`KXITFWMATCH-26OCT29SEBGOW-SEB`) | 0.09 / 0.96 (3) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sysoeva / Van Zyl vs Haile / Saffar -- W15 Sumter SC QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29SYSVANHAISAF:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Haile / Saffar (`KXITFWDOUBLES-26OCT29SYSVANHAISAF-HAISAF`) | 0.05 / 0.97 (138) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sysoeva / Van Zyl (`KXITFWDOUBLES-26OCT29SYSVANHAISAF-SYSVAN`) | 0.05 / 0.97 (116) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Marine Szostak vs Clara Burel -- W75 Poitiers R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29SZOBUR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Clara Burel (`KXITFWMATCH-26OCT29SZOBUR-BUR`) | 0.90 / 0.97 (420) | 93.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marine Szostak (`KXITFWMATCH-26OCT29SZOBUR-SZO`) | 0.03 / 0.06 (22) | 4.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
