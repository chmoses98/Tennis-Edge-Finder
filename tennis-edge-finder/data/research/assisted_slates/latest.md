# ASSISTED SLATE -- 2026-10-24T10:33Z (`SL-20261024T103345Z-aa8ac285`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

108 open matches not seen started, 458 markets. Skipped: {"no_play_confirmed": 1, "first_ball_already_observed": 5, "scheduled_start_over_24h_past": 1, "no_match_winner_listed": 1}. Sources: shadow board 2026-10-24T05:27:09.374717+00:00, Model 4 2026-10-24T05:27:24.381133+00:00, Gen-1 ledger 2026-10-24T05:27:05.557008+00:00, external 2026-10-24T10:11:28.353889+00:00, capture 20261024T101832Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-10-24 10:47Z**
* Recommended RUN TENNIS time: **2026-10-24 10:02Z**  (**OVERDUE -- run now**)
* Final price/status check time: **2026-10-24 10:37Z**
* Number of matches in window: 7 (Anastasia Zakharova vs Ruien Zhang, Joel Schwaerzler vs Titouan Droguet, Tommy Paul vs Taylor Fritz, Yihan Qu vs Teodora Kostovic, Sebastian Baez vs Giovanni Mpetshi Perricard, Alex Molcan vs Hamad Medjedovic ...)

* **12 main-tour match(es) have NO verified start status** (STATUS_AMBIGUOUS): BET blocked until a live status check.

Slate built 2026-10-24T10:33Z. Refresh due by: 2026-10-24 10:02Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 32, "HIGH_REVIEW": 29, "NORMAL": 204, "REVIEW": 52, "UNPRICED": 141}; match winners: {"EXTREME": 18, "HIGH_REVIEW": 15, "NORMAL": 63, "REVIEW": 16, "UNPRICED": 104}; quote freshness at build: {"FRESH": 317}.

## Francesco Forti vs Oriol Roca Batalla -- ATP Challenger Florence QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-23 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-23T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106177:209506:2026-10-23`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesco Forti (`KXATPCHALLENGERMATCH-26OCT23FORROC-FOR`) | -- / 0.01 (29512) | -- | 55.4% | 56.5% | 53.0% [47.5%-55.5%] | -- | -- | -- | -- | WATCH | -- | UNPRICED | FRESH | A / ADEQUATE | INSUFFICIENT_INPUTS | VERIFIED |
| Oriol Roca Batalla (`KXATPCHALLENGERMATCH-26OCT23FORROC-ROC`) | 0.99 / -- (0) | -- | 44.6% | 43.5% | 47.0% [44.5%-52.5%] | -- | -- | -- | -- | PASS | -- | UNPRICED | FRESH | A / ADEQUATE | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 1932.0, B 2870.0; serve-point win A 63.2%, B 37.9%; Elo A 1495.2, B 1504.8; model uncertainty 0.0404
* Form inputs: days since last match A 11, B 11; matches on record A 373, B 981; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose +0.020, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE

## Mats Hermans / Max Houkes vs Juan Jose Bianchi / Jakub Vrba -- ATP Challenger Florence QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-23 13:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-23T13:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT23HERHOUBIAVRB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Jose Bianchi / Jakub Vrba (`KXATPCHALLENGERDOUBLES-26OCT23HERHOUBIAVRB-BIAVRB`) | 0.19 / 0.20 (50) | 19.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mats Hermans / Max Houkes (`KXATPCHALLENGERDOUBLES-26OCT23HERHOUBIAVRB-HERHOU`) | 0.78 / 0.81 (1078) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Jacob Fearnley vs Pablo Carreno Busta -- ATP Vienna Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 12:00Z
* Current expected start: 2026-10-24 09:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 08:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105807:207985:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pablo Carreno Busta (`KXATPMATCH-26OCT24FEACAR-CAR`) | 0.34 / 0.35 (855) | 34.5% | 40.1% | 38.4% | 44.4% [39.9%-51.0%] | 39.1% | -- | 39.1% | MODEL_LONE_OUTLIER | WATCH | +5.6 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Jacob Fearnley (`KXATPMATCH-26OCT24FEACAR-FEA`) | 0.65 / 0.66 (6) | 65.5% | 59.9% | 61.6% | 55.6% [49.0%-60.1%] | 60.9% | -- | 60.9% | MODEL_LONE_OUTLIER | PASS | -5.6 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 4197.0, B 3944.0; serve-point win A 62.4%, B 39.5%; Elo A 1781.1, B 1841.3; model uncertainty 0.0555
* Form inputs: days since last match A 3, B 12; matches on record A 185, B 959; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.030, surface_dev_loose +0.020, surface_dev_tight -0.015
* Derivatives listed: 6 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 6 carry a model probability
  * `KXATPSETWINNER-26OCT24FEACAR-2-FEA` Will Jacob Fearnley win set 2 in the Jacob Fearnley vs Pablo Carreno Busta match: 0.01/0.04 mid 2.5%, model 56.6% (projection_v2.0 (prediction ledger)) -- gap +54.1 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24FEACAR-2-CAR` Will Pablo Carreno Busta win set 2 in the Jacob Fearnley vs Pablo Carreno Busta match: 0.95/0.99 mid 97.0%, model 43.4% (projection_v2.0 (prediction ledger)) -- gap -53.6 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24FEACAR-FEA21` Will Jacob Fearnley win the Jacob Fearnley vs Pablo Carreno Busta match by a set score of 2-1?: 0.59/0.64 mid 61.5%, model 27.8% (projection_v2.0 (prediction ledger)) -- gap -33.7 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24FEACAR-FEA20` Will Jacob Fearnley win the Jacob Fearnley vs Pablo Carreno Busta match by a set score of 2-0?: 0.02/0.06 mid 4.0%, model 32.1% (projection_v2.0 (prediction ledger)) -- gap +28.1 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24FEACAR-CAR21` Will Pablo Carreno Busta win the Jacob Fearnley vs Pablo Carreno Busta match by a set score of 2-1?: 0.31/0.37 mid 34.0%, model 21.3% (projection_v2.0 (prediction ledger)) -- gap -12.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STATUS_AMBIGUOUS; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE

## Marcos Giron vs Yannick Hanfmann -- ATP Basel Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 11:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 09:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 08:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105870:106218:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcos Giron (`KXATPMATCH-26OCT24GIRHAN-GIR`) | 0.55 / 0.56 (26298) | 55.5% | 56.5% | 43.2% | 47.6% [45.2%-50.5%] | 41.7% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +1.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yannick Hanfmann (`KXATPMATCH-26OCT24GIRHAN-HAN`) | 0.43 / 0.44 (0) | 43.5% | 43.5% | 56.8% | 52.4% [49.5%-54.8%] | 58.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4256.0, B 4359.0; serve-point win A 67.3%, B 34.1%; Elo A 1805.2, B 1728.0; model uncertainty 0.0266
* Form inputs: days since last match A 4, B 15; matches on record A 708, B 656; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.024, surface_pool_high +0.024, surface_dev_loose +0.000, surface_dev_tight +0.005
* Derivatives listed: 4 (EXACT_SET_SCORE, MATCH_WINNER); 4 carry a model probability
  * `KXATPEXACTMATCH-26OCT24GIRHAN-GIR21` Will Marcos Giron win the Marcos Giron vs Yannick Hanfmann match by a set score of 2-1?: 0.54/0.58 mid 56.0%, model 27.0% (projection_v2.0 (prediction ledger)) -- gap -29.0 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24GIRHAN-HAN21` Will Yannick Hanfmann win the Marcos Giron vs Yannick Hanfmann match by a set score of 2-1?: 0.42/0.46 mid 44.0%, model 22.6% (projection_v2.0 (prediction ledger)) -- gap -21.4 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; STATUS_AMBIGUOUS; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE

## Miomir Kecmanovic vs Rinky Hijikata -- ATP Basel Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 11:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 09:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 08:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200175:208014:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rinky Hijikata (`KXATPMATCH-26OCT24KECHIJ-HIJ`) | 0.87 / 0.88 (48231) | 87.5% | 46.5% | 38.1% | 41.0% [39.6%-43.5%] | 40.6% | -- | 40.6% | MODEL_LONE_OUTLIER | PASS | -41.0 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Miomir Kecmanovic (`KXATPMATCH-26OCT24KECHIJ-KEC`) | 0.12 / 0.13 (46017) | 12.5% | 53.5% | 61.9% | 59.0% [56.5%-60.4%] | 59.4% | -- | 59.4% | MARKETS_AGREE | PASS | +41.0 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 5277.0, B 5199.0; serve-point win A 63.4%, B 37.3%; Elo A 1776.8, B 1789.2; model uncertainty 0.0196
* Form inputs: days since last match A 5, B 4; matches on record A 608, B 435; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT24KECHIJ-KEC  (YES = Miomir Kecmanovic)
Model: 53%
Kalshi: 12%
Gap: +41 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: SUPPORTS_MODEL_DIRECTION
Data quality: A (ADEQUATE)
Reasons: EXTERNAL_MARKET_CONFIRMATION, UNKNOWN
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.005
* Derivatives listed: 6 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 6 carry a model probability
  * `KXATPEXACTMATCH-26OCT24KECHIJ-HIJ20` Will Rinky Hijikata win the Miomir Kecmanovic vs Rinky Hijikata match by a set score of 2-0?: 0.81/0.85 mid 83.0%, model 22.7% (projection_v2.0 (prediction ledger)) -- gap -60.3 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24KECHIJ-2-KEC` Will Miomir Kecmanovic win set 2 in the Miomir Kecmanovic vs Rinky Hijikata match: 0.16/0.18 mid 17.0%, model 52.3% (projection_v2.0 (prediction ledger)) -- gap +35.3 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24KECHIJ-2-HIJ` Will Rinky Hijikata win set 2 in the Miomir Kecmanovic vs Rinky Hijikata match: 0.81/0.84 mid 82.5%, model 47.7% (projection_v2.0 (prediction ledger)) -- gap -34.8 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24KECHIJ-HIJ21` Will Rinky Hijikata win the Miomir Kecmanovic vs Rinky Hijikata match by a set score of 2-1?: 0.05/0.07 mid 6.0%, model 23.8% (projection_v2.0 (prediction ledger)) -- gap +17.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24KECHIJ-KEC21` Will Miomir Kecmanovic win the Miomir Kecmanovic vs Rinky Hijikata match by a set score of 2-1?: 0.10/0.12 mid 11.0%, model 26.1% (projection_v2.0 (prediction ledger)) -- gap +15.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; STATUS_AMBIGUOUS; ONE_SIDED_OR_NO_QUOTE

## Ushna Suhail vs yasaman yazdani -- Billie Jean King Cup Qualifiers UNK

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 09:00Z
* Current expected start: 2026-10-24 09:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: 2026-10-24 08:15Z

* Status notes: NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

OTHER (TEAM) · surface ? · scheduled 2026-10-24T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT24SUHYAZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ushna Suhail (`KXWTAMATCH-26OCT24SUHYAZ-SUH`) | 0.22 / 0.37 (10) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| yasaman yazdani (`KXWTAMATCH-26OCT24SUHYAZ-YAZ`) | 0.60 / 0.72 (10) | 66.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Nayara Usama Ali vs Anna Abualhaj -- Billie Jean King Cup Qualifiers UNK

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 09:00Z
* Current expected start: 2026-10-24 09:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: 2026-10-24 08:15Z

* Status notes: NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

OTHER (TEAM) · surface ? · scheduled 2026-10-24T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT24USAABU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Abualhaj (`KXWTAMATCH-26OCT24USAABU-ABU`) | 0.61 / 0.74 (23) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nayara Usama Ali (`KXWTAMATCH-26OCT24USAABU-USA`) | 0.26 / 0.39 (12) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Kinley Yangden vs Khadija Gassama -- Billie Jean King Cup Qualifiers UNK

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 09:00Z
* Current expected start: 2026-10-24 09:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: 2026-10-24 08:15Z

* Status notes: NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

OTHER (TEAM) · surface ? · scheduled 2026-10-24T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT24YANGAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Khadija Gassama (`KXWTAMATCH-26OCT24YANGAS-GAS`) | 0.85 / 0.88 (2) | 86.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kinley Yangden (`KXWTAMATCH-26OCT24YANGAS-YAN`) | 0.13 / 0.17 (73) | 15.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Vit Kopriva vs Lukas Neumayer -- ATP Vienna Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 12:30Z
* Current expected start: 2026-10-24 09:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 08:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200240:209903:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vit Kopriva (`KXATPMATCH-26OCT24KOPNEU-KOP`) | 0.32 / 0.33 (181) | 32.5% | 56.9% | 51.0% | 54.6% [53.1%-57.1%] | 53.2% | -- | 53.2% | MODEL_LONE_OUTLIER | PASS | +24.4 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Lukas Neumayer (`KXATPMATCH-26OCT24KOPNEU-NEU`) | 0.67 / 0.68 (0) | 67.5% | 43.1% | 49.0% | 45.4% [42.9%-46.9%] | 46.8% | -- | 46.8% | MODEL_LONE_OUTLIER | PASS | -24.4 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 4886.0, B 4653.0; serve-point win A 61.9%, B 39.4%; Elo A 1682.3, B 1568.4; model uncertainty 0.0203
* Form inputs: days since last match A 12, B 12; matches on record A 698, B 376; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT24KOPNEU-KOP  (YES = Vit Kopriva)
Model: 57%
Kalshi: 32%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_MODEL
Data quality: A (ADEQUATE)
Reasons: LOW_DISPLAYED_LIQUIDITY, EXTERNAL_MARKET_CONFIRMATION
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.005, surface_dev_loose -0.005, surface_dev_tight +0.005
* Derivatives listed: 6 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 6 carry a model probability
  * `KXATPEXACTMATCH-26OCT24KOPNEU-NEU20` Will Lukas Neumayer win the Vit Kopriva vs Lukas Neumayer match by a set score of 2-0?: 0.32/0.48 mid 40.0%, model 20.6% (projection_v2.0 (prediction ledger)) -- gap -19.4 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24KOPNEU-KOP21` Will Vit Kopriva win the Vit Kopriva vs Lukas Neumayer match by a set score of 2-1?: 0.30/0.39 mid 34.5%, model 27.1% (projection_v2.0 (prediction ledger)) -- gap -7.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24KOPNEU-2-NEU` Will Lukas Neumayer win set 2 in the Vit Kopriva vs Lukas Neumayer match: 0.37/0.42 mid 39.5%, model 45.4% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24KOPNEU-NEU21` Will Lukas Neumayer win the Vit Kopriva vs Lukas Neumayer match by a set score of 2-1?: 0.22/0.31 mid 26.5%, model 22.5% (projection_v2.0 (prediction ledger)) -- gap -4.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24KOPNEU-2-KOP` Will Vit Kopriva win set 2 in the Vit Kopriva vs Lukas Neumayer match: 0.56/0.60 mid 58.0%, model 54.6% (projection_v2.0 (prediction ledger)) -- gap -3.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STATUS_AMBIGUOUS; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tenzin Wangsel Lhaden vs Hind Al-Mudahka -- Billie Jean King Cup Qualifiers UNK

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 10:00Z
* Current expected start: 2026-10-24 10:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: 2026-10-24 09:15Z

* Status notes: NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

OTHER (TEAM) · surface ? · scheduled 2026-10-24T10:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT24LHAALM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hind Al-Mudahka (`KXWTAMATCH-26OCT24LHAALM-ALM`) | 0.26 / 0.31 (3) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tenzin Wangsel Lhaden (`KXWTAMATCH-26OCT24LHAALM-LHA`) | 0.73 / 0.78 (4) | 75.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Mahin Qureshi vs Meshkatolzahra Safi -- Billie Jean King Cup Qualifiers UNK

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 10:00Z
* Current expected start: 2026-10-24 10:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: 2026-10-24 09:15Z

* Status notes: NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

OTHER (TEAM) · surface ? · scheduled 2026-10-24T10:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT24QURSAF:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mahin Qureshi (`KXWTAMATCH-26OCT24QURSAF-QUR`) | 0.16 / 0.89 (2) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Meshkatolzahra Safi (`KXWTAMATCH-26OCT24QURSAF-SAF`) | 0.14 / 0.87 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Aishath Karin Saizan vs Noor Sayej -- Billie Jean King Cup Qualifiers UNK

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 10:00Z
* Current expected start: 2026-10-24 10:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: 2026-10-24 09:15Z

* Status notes: NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

OTHER (TEAM) · surface ? · scheduled 2026-10-24T10:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT24SAISAY:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aishath Karin Saizan (`KXWTAMATCH-26OCT24SAISAY-SAI`) | 0.12 / 0.62 (1) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Noor Sayej (`KXWTAMATCH-26OCT24SAISAY-SAY`) | 0.18 / 0.68 (1) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nikoloz Basilashvili vs Stefanos Tsitsipas -- ATP Almaty SF

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 13:00Z
* Current expected start: 2026-10-24 10:10Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 09:25Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-170_MIN; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105932:126774:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikoloz Basilashvili (`KXATPMATCH-26OCT24BASTSI-BAS`) | 0.50 / 0.54 (179) | 52.0% | 18.9% | 27.5% | 24.0% [20.4%-26.3%] | 33.1% | 31.8% | 32.4% | MODEL_LONE_OUTLIER | PASS | -33.1 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Stefanos Tsitsipas (`KXATPMATCH-26OCT24BASTSI-TSI`) | 0.46 / 0.50 (34) | 48.0% | 81.1% | 72.5% | 76.0% [73.7%-79.6%] | 66.9% | 69.2% | 68.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +33.1 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 3254.0, B 5234.0; serve-point win A 64.1%, B 28.5%; Elo A 1696.5, B 1953.8; model uncertainty 0.0298
* Form inputs: days since last match A 1, B 1; matches on record A 915, B 804; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT24BASTSI-TSI  (YES = Stefanos Tsitsipas)
Model: 81%
Kalshi: 48%
Gap: +33 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: SUPPORTS_MODEL_DIRECTION
Data quality: A (ADEQUATE)
Reasons: EXTERNAL_MARKET_CONFIRMATION, UNKNOWN
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.023, surface_dev_loose +0.016, surface_dev_tight -0.009
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPSETWINNER-26OCT24BASTSI-1-BAS` Will Nikoloz Basilashvili win set 1 in the Nikoloz Basilashvili vs Stefanos Tsitsipas match: 0.79/0.87 mid 83.0%, model 27.8% (projection_v2.0 (prediction ledger)) -- gap -55.2 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BASTSI-1-TSI` Will Stefanos Tsitsipas win set 1 in the Nikoloz Basilashvili vs Stefanos Tsitsipas match: 0.14/0.20 mid 17.0%, model 72.2% (projection_v2.0 (prediction ledger)) -- gap +55.2 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24BASTSI-TSI20` Will Stefanos Tsitsipas win the Nikoloz Basilashvili vs Stefanos Tsitsipas match by a set score of 2-0?: 0.08/0.16 mid 12.0%, model 52.1% (projection_v2.0 (prediction ledger)) -- gap +40.1 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24BASTSI-BAS2` Will Nikoloz Basilashvili win at least 1.5 more games than Stefanos Tsitsipas?: 0.49/0.50 mid 49.5%, model 13.6% (projection_v2.0 (prediction ledger)) -- gap -35.9 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24BASTSI-TSI4` Will Stefanos Tsitsipas win at least 3.5 more games than Nikoloz Basilashvili?: 0.16/0.24 mid 20.0%, model 50.2% (projection_v2.0 (prediction ledger)) -- gap +30.2 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24BASTSI-BAS20` Will Nikoloz Basilashvili win the Nikoloz Basilashvili vs Stefanos Tsitsipas match by a set score of 2-0?: 0.29/0.38 mid 33.5%, model 7.7% (projection_v2.0 (prediction ledger)) -- gap -25.8 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24BASTSI-28` Over 27.5 games: 0.47/0.55 mid 51.0%, model 35.3% (projection_v2.0 (prediction ledger)) -- gap -15.7 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24BASTSI-23` Over 22.5 games: 0.63/0.72 mid 67.5%, model 55.5% (projection_v2.0 (prediction ledger)) -- gap -12.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BASTSI-2-BAS` Will Nikoloz Basilashvili win set 2 in the Nikoloz Basilashvili vs Stefanos Tsitsipas match: 0.37/0.41 mid 39.0%, model 27.8% (projection_v2.0 (prediction ledger)) -- gap -11.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BASTSI-2-TSI` Will Stefanos Tsitsipas win set 2 in the Nikoloz Basilashvili vs Stefanos Tsitsipas match: 0.59/0.63 mid 61.0%, model 72.2% (projection_v2.0 (prediction ledger)) -- gap +11.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24BASTSI-TSI21` Will Stefanos Tsitsipas win the Nikoloz Basilashvili vs Stefanos Tsitsipas match by a set score of 2-1?: 0.35/0.39 mid 37.0%, model 29.0% (projection_v2.0 (prediction ledger)) -- gap -8.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24BASTSI-BAS21` Will Nikoloz Basilashvili win the Nikoloz Basilashvili vs Stefanos Tsitsipas match by a set score of 2-1?: 0.17/0.21 mid 19.0%, model 11.2% (projection_v2.0 (prediction ledger)) -- gap -7.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24BASTSI-TSI7` Will Stefanos Tsitsipas win at least 6.5 more games than Nikoloz Basilashvili?: 0.04/0.19 mid 11.5%, model 8.2% (projection_v2.0 (prediction ledger)) -- gap -3.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24BASTSI-18` Over 17.5 games: 0.90/0.95 mid 92.5%, model 93.1% (projection_v2.0 (prediction ledger)) -- gap +0.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STATUS_AMBIGUOUS; WIDE_SPREAD

## Harriet Dart vs Cheuk Ying Shek -- WTA Guangzhou Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 10:10Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 09:25Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211279:263941:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Harriet Dart (`KXWTAMATCH-26OCT23DARSHE-DAR`) | 0.83 / 0.84 (13422) | 83.5% | 85.7% | 70.9% | 79.7% [74.9%-86.0%] | -- | 94.3% | 94.3% | MODEL_LONE_OUTLIER | PASS | +2.2 pp | NORMAL | FRESH | C / LIMITED | EXTERNAL_OUTLIER | VERIFIED |
| Cheuk Ying Shek (`KXWTAMATCH-26OCT23DARSHE-SHE`) | 0.16 / 0.17 (21660) | 16.5% | 14.3% | 29.1% | 20.3% [14.0%-25.1%] | -- | 7.0% | 7.0% | MODEL_LONE_OUTLIER | WATCH | -2.2 pp | NORMAL | FRESH | C / LIMITED | EXTERNAL_OUTLIER | VERIFIED |

* Serve evidence (points): A 4244.0, B 1558.0; serve-point win A 57.1%, B 50.9%; Elo A 1787.6, B 1461.7; model uncertainty 0.0558
* Form inputs: days since last match A 4, B 193; matches on record A 676, B 47; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.019, surface_dev_loose +0.004, surface_dev_tight -0.008
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT23DARSHE-1-DAR` Will Harriet Dart win set 1 in the Harriet Dart vs Cheuk Ying Shek match: 0.60/0.63 mid 61.5%, model 76.2% (projection_v2.0 (prediction ledger)) -- gap +14.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT23DARSHE-1-SHE` Will Cheuk Ying Shek win set 1 in the Harriet Dart vs Cheuk Ying Shek match: 0.36/0.37 mid 36.5%, model 23.8% (projection_v2.0 (prediction ledger)) -- gap -12.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT23DARSHE-2-DAR` Will Harriet Dart win set 2 in the Harriet Dart vs Cheuk Ying Shek match: 0.80/0.81 mid 80.5%, model 76.2% (projection_v2.0 (prediction ledger)) -- gap -4.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT23DARSHE-2-SHE` Will Cheuk Ying Shek win set 2 in the Harriet Dart vs Cheuk Ying Shek match: 0.19/0.20 mid 19.5%, model 23.8% (projection_v2.0 (prediction ledger)) -- gap +4.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; STATUS_AMBIGUOUS

## Kayla Day vs Shuai Zhang -- WTA Tokyo Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 04:30Z
* Current expected start: 2026-10-24 10:22Z
* Source: COURT_PROGRESSION: preceding match on Indoor Court in progress (set 2 of best-of-3); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 09:37Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+352_MIN; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T04:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:201533:215037:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kayla Day (`KXWTAMATCH-26OCT23DAYZHA-DAY`) | 0.45 / 0.46 (14490) | 45.5% | 52.7% | 60.8% | 53.6% [45.3%-56.7%] | 45.7% | 44.9% | 45.3% | MODEL_LONE_OUTLIER | WATCH | +7.2 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Shuai Zhang (`KXWTAMATCH-26OCT23DAYZHA-ZHA`) | 0.55 / 0.56 (3591) | 55.5% | 47.3% | 39.2% | 46.4% [43.3%-54.7%] | 54.3% | 55.0% | 54.6% | MODEL_LONE_OUTLIER | PASS | -8.2 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3639.0, B 3846.0; serve-point win A 58.9%, B 41.6%; Elo A 1748.9, B 1845.2; model uncertainty 0.0572
* Form inputs: days since last match A 1, B 3; matches on record A 481, B 1068; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.010, surface_dev_tight -0.010
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT23DAYZHA-1-DAY` Will Kayla Day win set 1 in the Kayla Day vs Shuai Zhang match: 0.44/0.48 mid 46.0%, model 51.8% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23DAYZHA-2-DAY` Will Kayla Day win set 2 in the Kayla Day vs Shuai Zhang match: 0.44/0.49 mid 46.5%, model 51.8% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23DAYZHA-2-ZHA` Will Shuai Zhang win set 2 in the Kayla Day vs Shuai Zhang match: 0.51/0.56 mid 53.5%, model 48.2% (projection_v2.0 (prediction ledger)) -- gap -5.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23DAYZHA-1-ZHA` Will Shuai Zhang win set 1 in the Kayla Day vs Shuai Zhang match: 0.51/0.55 mid 53.0%, model 48.2% (projection_v2.0 (prediction ledger)) -- gap -4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; THIN_DISPLAYED_SIZE

## Linda Fruhvirtova vs Mei Yamaguchi -- WTA Guangzhou Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 10:40Z
* Current expected start: 2026-10-24 10:22Z
* Source: COURT_PROGRESSION: preceding match on Court 6 in progress (set 2 of best-of-3); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 09:37Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-18_MIN; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T10:40:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215614:222258:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Linda Fruhvirtova (`KXWTAMATCH-26OCT24FRUYAM-FRU`) | 0.77 / 0.79 (485) | 78.0% | -- | 65.5% | 68.8% [66.9%-69.8%] | 76.2% | 78.1% | 76.2% | MODEL_LONE_OUTLIER | PASS | -9.2 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Mei Yamaguchi (`KXWTAMATCH-26OCT24FRUYAM-YAM`) | 0.20 / 0.23 (363) | 21.5% | -- | 34.5% | 31.2% [30.2%-33.1%] | 23.8% | 21.4% | 23.8% | KALSHI_LONE_OUTLIER | SHADOW_BET | +9.7 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4353.0, B 3409.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0142
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.009, surface_dev_loose +0.005, surface_dev_tight -0.009
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; STATUS_AMBIGUOUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kyoka Okamura vs Sayaka Ishii -- WTA Tokyo Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 12:15Z
* Current expected start: 2026-10-24 10:22Z
* Source: COURT_PROGRESSION: preceding match on Center in progress (set 2 of best-of-3); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 09:37Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-113_MIN; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-24T12:15:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT24OKAISH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sayaka Ishii (`KXWTAMATCH-26OCT24OKAISH-ISH`) | 0.33 / 0.35 (2453) | 34.0% | -- | -- | -- [-----] | 33.1% | 34.2% | 33.7% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kyoka Okamura (`KXWTAMATCH-26OCT24OKAISH-OKA`) | 0.66 / 0.67 (5724) | 66.5% | -- | -- | -- [-----] | 66.9% | 66.1% | 66.5% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; STATUS_AMBIGUOUS; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Juan Manuel Cerundolo vs Zachary Svajda -- ATP Basel Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 11:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 10:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 09:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207678:208260:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Manuel Cerundolo (`KXATPMATCH-26OCT24CERSVA-CER`) | 0.41 / 0.42 (4983) | 41.5% | 51.6% | 48.0% | 48.5% [46.6%-51.0%] | 42.5% | 41.1% | 42.5% | MODEL_LONE_OUTLIER | SHADOW_BET | +10.1 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Zachary Svajda (`KXATPMATCH-26OCT24CERSVA-SVA`) | 0.57 / 0.59 (4992) | 58.0% | 48.4% | 52.0% | 51.5% [49.0%-53.4%] | 57.5% | 58.7% | 57.5% | MODEL_LONE_OUTLIER | PASS | -9.6 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5318.0, B 3677.0; serve-point win A 65.0%, B 35.4%; Elo A 1750.6, B 1764.3; model uncertainty 0.0222
* Form inputs: days since last match A 4, B 14; matches on record A 507, B 321; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.020, surface_dev_loose -0.015, surface_dev_tight +0.010
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT24CERSVA-SVA20` Will Zachary Svajda win the Juan Manuel Cerundolo vs Zachary Svajda match by a set score of 2-0?: 0.34/0.38 mid 36.0%, model 23.9% (projection_v2.0 (prediction ledger)) -- gap -12.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24CERSVA-CER21` Will Juan Manuel Cerundolo win the Juan Manuel Cerundolo vs Zachary Svajda match by a set score of 2-1?: 0.15/0.19 mid 17.0%, model 25.5% (projection_v2.0 (prediction ledger)) -- gap +8.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24CERSVA-2-CER` Will Juan Manuel Cerundolo win set 2 in the Juan Manuel Cerundolo vs Zachary Svajda match: 0.41/0.46 mid 43.5%, model 51.1% (projection_v2.0 (prediction ledger)) -- gap +7.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24CERSVA-2-SVA` Will Zachary Svajda win set 2 in the Juan Manuel Cerundolo vs Zachary Svajda match: 0.54/0.59 mid 56.5%, model 48.9% (projection_v2.0 (prediction ledger)) -- gap -7.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24CERSVA-1-CER` Will Juan Manuel Cerundolo win set 1 in the Juan Manuel Cerundolo vs Zachary Svajda match: 0.42/0.46 mid 44.0%, model 51.1% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24CERSVA-1-SVA` Will Zachary Svajda win set 1 in the Juan Manuel Cerundolo vs Zachary Svajda match: 0.55/0.57 mid 56.0%, model 48.9% (projection_v2.0 (prediction ledger)) -- gap -7.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24CERSVA-SVA21` Will Zachary Svajda win the Juan Manuel Cerundolo vs Zachary Svajda match by a set score of 2-1?: 0.20/0.24 mid 22.0%, model 24.4% (projection_v2.0 (prediction ledger)) -- gap +2.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24CERSVA-CER20` Will Juan Manuel Cerundolo win the Juan Manuel Cerundolo vs Zachary Svajda match by a set score of 2-0?: 0.23/0.25 mid 24.0%, model 26.1% (projection_v2.0 (prediction ledger)) -- gap +2.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; STATUS_AMBIGUOUS; THIN_DISPLAYED_SIZE

## Jaime Faria vs Mika Brunold -- ATP Basel Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 11:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 10:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 09:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:209983:210262:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mika Brunold (`KXATPMATCH-26OCT24FARBRU-BRU`) | 0.47 / 0.49 (7801) | 48.0% | 29.0% | 44.5% | 29.8% [17.4%-34.8%] | 47.8% | 47.7% | 47.7% | MODEL_LONE_OUTLIER | PASS | -18.9 pp | HIGH_REVIEW | FRESH | F / POOR | EXTERNAL_STALE | VERIFIED |
| Jaime Faria (`KXATPMATCH-26OCT24FARBRU-FAR`) | 0.53 / 0.54 (40133) | 53.5% | 71.0% | 55.5% | 70.2% [65.2%-82.6%] | 52.2% | 52.4% | 52.4% | MODEL_LONE_OUTLIER | PASS | +17.4 pp | HIGH_REVIEW | FRESH | F / POOR | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4786.0, B 1536.0; serve-point win A 65.1%, B 39.2%; Elo A 1778.3, B 1510.5; model uncertainty 0.0871
* Form inputs: days since last match A 5, B 684; matches on record A 313, B 128; data quality F

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT24FARBRU-FAR  (YES = Jaime Faria)
Model: 71%
Kalshi: 54%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: EXTERNAL_STALE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.004, surface_dev_loose -0.018, surface_dev_tight +0.018
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT24FARBRU-BRU20` Will Mika Brunold win the Jaime Faria vs Mika Brunold match by a set score of 2-0?: 0.27/0.30 mid 28.5%, model 12.7% (projection_v2.0 (prediction ledger)) -- gap -15.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data POOR
  * `KXATPSETWINNER-26OCT24FARBRU-1-BRU` Will Mika Brunold win set 1 in the Jaime Faria vs Mika Brunold match: 0.48/0.51 mid 49.5%, model 35.6% (projection_v2.0 (prediction ledger)) -- gap -13.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT24FARBRU-1-FAR` Will Jaime Faria win set 1 in the Jaime Faria vs Mika Brunold match: 0.49/0.52 mid 50.5%, model 64.4% (projection_v2.0 (prediction ledger)) -- gap +13.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT24FARBRU-2-BRU` Will Mika Brunold win set 2 in the Jaime Faria vs Mika Brunold match: 0.47/0.52 mid 49.5%, model 35.6% (projection_v2.0 (prediction ledger)) -- gap -13.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT24FARBRU-2-FAR` Will Jaime Faria win set 2 in the Jaime Faria vs Mika Brunold match: 0.48/0.53 mid 50.5%, model 64.4% (projection_v2.0 (prediction ledger)) -- gap +13.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPEXACTMATCH-26OCT24FARBRU-FAR20` Will Jaime Faria win the Jaime Faria vs Mika Brunold match by a set score of 2-0?: 0.26/0.30 mid 28.0%, model 41.4% (projection_v2.0 (prediction ledger)) -- gap +13.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data POOR
  * `KXATPEXACTMATCH-26OCT24FARBRU-FAR21` Will Jaime Faria win the Jaime Faria vs Mika Brunold match by a set score of 2-1?: 0.20/0.23 mid 21.5%, model 29.5% (projection_v2.0 (prediction ledger)) -- gap +8.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
  * `KXATPEXACTMATCH-26OCT24FARBRU-BRU21` Will Mika Brunold win the Jaime Faria vs Mika Brunold match by a set score of 2-1?: 0.17/0.21 mid 19.0%, model 16.4% (projection_v2.0 (prediction ledger)) -- gap -2.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; STATUS_AMBIGUOUS; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE

## Adolfo Daniel Vallejo vs Lorenzo Sonego -- ATP Vienna Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 13:10Z
* Current expected start: 2026-10-24 10:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 09:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T13:10:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:132283:209226:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Sonego (`KXATPMATCH-26OCT24VALSON-SON`) | 0.51 / 0.53 (6450) | 52.0% | 46.8% | 60.4% | 60.4% [58.4%-61.8%] | 50.0% | 51.3% | 50.6% | MODEL_LONE_OUTLIER | SHADOW_BET | -5.2 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Adolfo Daniel Vallejo (`KXATPMATCH-26OCT24VALSON-VAL`) | 0.48 / 0.49 (23333) | 48.5% | 53.2% | 39.6% | 39.6% [38.2%-41.6%] | 50.0% | 48.3% | 49.2% | MODEL_LONE_OUTLIER | PASS | +4.7 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5092.0, B 4551.0; serve-point win A 63.9%, B 36.7%; Elo A 1707.5, B 1781.5; model uncertainty 0.0168
* Form inputs: days since last match A 14, B 5; matches on record A 211, B 690; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high +0.000, surface_dev_loose -0.014, surface_dev_tight +0.019
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT24VALSON-SON20` Will Lorenzo Sonego win the Adolfo Daniel Vallejo vs Lorenzo Sonego match by a set score of 2-0?: 0.29/0.33 mid 31.0%, model 22.9% (projection_v2.0 (prediction ledger)) -- gap -8.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24VALSON-VAL21` Will Adolfo Daniel Vallejo win the Adolfo Daniel Vallejo vs Lorenzo Sonego match by a set score of 2-1?: 0.17/0.22 mid 19.5%, model 26.0% (projection_v2.0 (prediction ledger)) -- gap +6.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24VALSON-1-SON` Will Lorenzo Sonego win set 1 in the Adolfo Daniel Vallejo vs Lorenzo Sonego match: 0.50/0.54 mid 52.0%, model 47.9% (projection_v2.0 (prediction ledger)) -- gap -4.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24VALSON-SON21` Will Lorenzo Sonego win the Adolfo Daniel Vallejo vs Lorenzo Sonego match by a set score of 2-1?: 0.18/0.22 mid 20.0%, model 23.9% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24VALSON-1-VAL` Will Adolfo Daniel Vallejo win set 1 in the Adolfo Daniel Vallejo vs Lorenzo Sonego match: 0.47/0.50 mid 48.5%, model 52.1% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24VALSON-2-SON` Will Lorenzo Sonego win set 2 in the Adolfo Daniel Vallejo vs Lorenzo Sonego match: 0.49/0.54 mid 51.5%, model 47.9% (projection_v2.0 (prediction ledger)) -- gap -3.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24VALSON-2-VAL` Will Adolfo Daniel Vallejo win set 2 in the Adolfo Daniel Vallejo vs Lorenzo Sonego match: 0.46/0.51 mid 48.5%, model 52.1% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24VALSON-VAL20` Will Adolfo Daniel Vallejo win the Adolfo Daniel Vallejo vs Lorenzo Sonego match by a set score of 2-0?: 0.26/0.31 mid 28.5%, model 27.2% (projection_v2.0 (prediction ledger)) -- gap -1.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STATUS_AMBIGUOUS

## Anastasia Zakharova vs Ruien Zhang -- WTA Guangzhou Q1

**START STATUS: START_IMMINENT**
* Nominal schedule: 2026-10-24 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 10:47Z
* Source: COURT_PROGRESSION: preceding match on Center Court in progress (set 1 of best-of-3); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 10:02Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:220435:263869:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasia Zakharova (`KXWTAMATCH-26OCT23ZAKZHA-ZAK`) | 0.91 / 0.92 (8496) | 91.5% | 87.7% | 89.9% | 89.4% [87.7%-90.1%] | 89.1% | 94.0% | 91.5% | MODEL_LONE_OUTLIER | PASS | -3.8 pp | NORMAL | FRESH | B / ADEQUATE | ALL_AGREE | VERIFIED |
| Ruien Zhang (`KXWTAMATCH-26OCT23ZAKZHA-ZHA`) | 0.09 / 0.10 (5659) | 9.5% | 12.3% | 10.1% | 10.6% [9.9%-12.3%] | 10.9% | 8.7% | 10.9% | MODEL_LONE_OUTLIER | WATCH | +2.8 pp | NORMAL | FRESH | B / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4628.0, B 1375.0; serve-point win A 61.5%, B 47.4%; Elo A 1813.0, B 1448.5; model uncertainty 0.012
* Form inputs: days since last match A 2, B 18; matches on record A 481, B 107; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.007, surface_dev_loose +0.007, surface_dev_tight -0.010
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT23ZAKZHA-1-ZHA` Will Ruien Zhang win set 1 in the Anastasia Zakharova vs Ruien Zhang match: 0.12/0.15 mid 13.5%, model 21.9% (projection_v2.0 (prediction ledger)) -- gap +8.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23ZAKZHA-1-ZAK` Will Anastasia Zakharova win set 1 in the Anastasia Zakharova vs Ruien Zhang match: 0.85/0.86 mid 85.5%, model 78.1% (projection_v2.0 (prediction ledger)) -- gap -7.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23ZAKZHA-2-ZAK` Will Anastasia Zakharova win set 2 in the Anastasia Zakharova vs Ruien Zhang match: 0.85/0.86 mid 85.5%, model 78.1% (projection_v2.0 (prediction ledger)) -- gap -7.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23ZAKZHA-2-ZHA` Will Ruien Zhang win set 2 in the Anastasia Zakharova vs Ruien Zhang match: 0.14/0.16 mid 15.0%, model 21.9% (projection_v2.0 (prediction ledger)) -- gap +6.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE

## Joel Schwaerzler vs Titouan Droguet -- ATP Vienna Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 13:40Z
* Current expected start: 2026-10-24 11:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 10:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T13:40:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208169:212082:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Titouan Droguet (`KXATPMATCH-26OCT24SCHDRO-DRO`) | 0.72 / 0.73 (21872) | 72.5% | 73.8% | 74.0% | 74.0% [73.2%-75.5%] | -- | 72.5% | 72.5% | MODEL_LONE_OUTLIER | PASS | +1.3 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Joel Schwaerzler (`KXATPMATCH-26OCT24SCHDRO-SCH`) | 0.27 / 0.28 (5584) | 27.5% | 26.2% | 26.0% | 26.0% [24.5%-26.8%] | -- | 27.1% | 27.1% | MODEL_LONE_OUTLIER | PASS | -1.3 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3799.0, B 5236.0; serve-point win A 64.0%, B 30.8%; Elo A 1607.9, B 1798.5; model uncertainty 0.0117
* Form inputs: days since last match A 19, B 4; matches on record A 147, B 394; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.008, surface_dev_loose -0.007, surface_dev_tight -0.001
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT24SCHDRO-DRO21` Will Titouan Droguet win the Joel Schwaerzler vs Titouan Droguet match by a set score of 2-1?: 0.20/0.25 mid 22.5%, model 29.6% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24SCHDRO-DRO20` Will Titouan Droguet win the Joel Schwaerzler vs Titouan Droguet match by a set score of 2-0?: 0.48/0.49 mid 48.5%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap -4.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24SCHDRO-SCH21` Will Joel Schwaerzler win the Joel Schwaerzler vs Titouan Droguet match by a set score of 2-1?: 0.10/0.14 mid 12.0%, model 14.9% (projection_v2.0 (prediction ledger)) -- gap +2.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24SCHDRO-SCH20` Will Joel Schwaerzler win the Joel Schwaerzler vs Titouan Droguet match by a set score of 2-0?: 0.12/0.16 mid 14.0%, model 11.2% (projection_v2.0 (prediction ledger)) -- gap -2.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24SCHDRO-2-SCH` Will Joel Schwaerzler win set 2 in the Joel Schwaerzler vs Titouan Droguet match: 0.29/0.34 mid 31.5%, model 33.5% (projection_v2.0 (prediction ledger)) -- gap +2.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24SCHDRO-2-DRO` Will Titouan Droguet win set 2 in the Joel Schwaerzler vs Titouan Droguet match: 0.66/0.69 mid 67.5%, model 66.5% (projection_v2.0 (prediction ledger)) -- gap -1.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24SCHDRO-1-DRO` Will Titouan Droguet win set 1 in the Joel Schwaerzler vs Titouan Droguet match: 0.65/0.67 mid 66.0%, model 66.5% (projection_v2.0 (prediction ledger)) -- gap +0.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24SCHDRO-1-SCH` Will Joel Schwaerzler win set 1 in the Joel Schwaerzler vs Titouan Droguet match: 0.33/0.35 mid 34.0%, model 33.5% (projection_v2.0 (prediction ledger)) -- gap -0.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE

## Tommy Paul vs Taylor Fritz -- ATP Lyon SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 13:00Z
* Current expected start: 2026-10-24 11:12Z
* Source: COURT_PROGRESSION: preceding match on Court Central Auvergne-Rhone-Alpes in progress (set 1 of best-of-5); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 10:27Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-108_MIN

ATP (TOUR_500_250) · Clay · scheduled 2026-10-24T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126203:126205:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Taylor Fritz (`KXATPMATCH-26OCT24PAUFRI-FRI`) | 0.62 / 0.63 (27814) | 62.5% | 41.2% | 52.9% | 49.0% [46.6%-51.4%] | 63.2% | 62.7% | 63.0% | MODEL_LONE_OUTLIER | PASS | -21.3 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Tommy Paul (`KXATPMATCH-26OCT24PAUFRI-PAU`) | 0.36 / 0.37 (363) | 36.5% | 58.8% | 47.1% | 51.0% [48.5%-53.4%] | 36.8% | 37.3% | 37.1% | MODEL_LONE_OUTLIER | SHADOW_BET | +22.3 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5709.0, B 6022.0; serve-point win A 67.5%, B 34.3%; Elo A 1995.2, B 1884.4; model uncertainty 0.0242
* Form inputs: days since last match A 3, B 2; matches on record A 721, B 740; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT24PAUFRI-PAU  (YES = Tommy Paul)
Model: 59%
Kalshi: 36%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: EXTERNAL_MARKET_REJECTION, UNKNOWN
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.015, surface_dev_loose +0.024, surface_dev_tight -0.024
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT24PAUFRI-PAU2` Will Tommy Paul win at least 1.5 more games than Taylor Fritz?: 0.27/0.31 mid 29.0%, model 50.7% (projection_v2.0 (prediction ledger)) -- gap +21.7 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24PAUFRI-FRI3` Will Taylor Fritz win at least 2.5 more games than Tommy Paul?: 0.46/0.47 mid 46.5%, model 26.3% (projection_v2.0 (prediction ledger)) -- gap -20.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24PAUFRI-FRI20` Will Taylor Fritz win the Tommy Paul vs Taylor Fritz match by a set score of 2-0?: 0.36/0.40 mid 38.0%, model 19.4% (projection_v2.0 (prediction ledger)) -- gap -18.6 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24PAUFRI-2-PAU` Will Tommy Paul win set 2 in the Tommy Paul vs Taylor Fritz match: 0.38/0.42 mid 40.0%, model 55.9% (projection_v2.0 (prediction ledger)) -- gap +15.9 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24PAUFRI-2-FRI` Will Taylor Fritz win set 2 in the Tommy Paul vs Taylor Fritz match: 0.57/0.62 mid 59.5%, model 44.1% (projection_v2.0 (prediction ledger)) -- gap -15.4 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24PAUFRI-1-PAU` Will Tommy Paul win set 1 in the Tommy Paul vs Taylor Fritz match: 0.41/0.42 mid 41.5%, model 55.9% (projection_v2.0 (prediction ledger)) -- gap +14.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24PAUFRI-1-FRI` Will Taylor Fritz win set 1 in the Tommy Paul vs Taylor Fritz match: 0.57/0.59 mid 58.0%, model 44.1% (projection_v2.0 (prediction ledger)) -- gap -13.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24PAUFRI-PAU20` Will Tommy Paul win the Tommy Paul vs Taylor Fritz match by a set score of 2-0?: 0.18/0.21 mid 19.5%, model 31.2% (projection_v2.0 (prediction ledger)) -- gap +11.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24PAUFRI-PAU21` Will Tommy Paul win the Tommy Paul vs Taylor Fritz match by a set score of 2-1?: 0.16/0.20 mid 18.0%, model 27.6% (projection_v2.0 (prediction ledger)) -- gap +9.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24PAUFRI-29` Over 28.5 games: 0.29/0.34 mid 31.5%, model 39.4% (projection_v2.0 (prediction ledger)) -- gap +7.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24PAUFRI-FRI6` Will Taylor Fritz win at least 5.5 more games than Tommy Paul?: 0.08/0.15 mid 11.5%, model 4.2% (projection_v2.0 (prediction ledger)) -- gap -7.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24PAUFRI-24` Over 23.5 games: 0.50/0.51 mid 50.5%, model 56.2% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24PAUFRI-FRI21` Will Taylor Fritz win the Tommy Paul vs Taylor Fritz match by a set score of 2-1?: 0.22/0.26 mid 24.0%, model 21.7% (projection_v2.0 (prediction ledger)) -- gap -2.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24PAUFRI-19` Over 18.5 games: 0.88/0.92 mid 90.0%, model 91.6% (projection_v2.0 (prediction ledger)) -- gap +1.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nicolas Barrientos / David Pel vs Sadio Doumbia / Bart Stevens -- ATP Brussels SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 15:00Z
* Current expected start: 2026-10-24 11:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 10:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-24T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24BARPELDOUSTE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Barrientos / David Pel (`KXATPDOUBLES-26OCT24BARPELDOUSTE-BARPEL`) | 0.43 / 0.46 (377) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sadio Doumbia / Bart Stevens (`KXATPDOUBLES-26OCT24BARPELDOUSTE-DOUSTE`) | 0.54 / 0.56 (623) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Yihan Qu vs Teodora Kostovic -- WTA Guangzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 11:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 10:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:264086:267439:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Teodora Kostovic (`KXWTAMATCH-26OCT23YIHKOS-KOS`) | 0.84 / 0.86 (7670) | 85.0% | 97.0% | 92.0% | 94.6% [93.9%-95.4%] | -- | 84.8% | 84.8% | MODEL_LONE_OUTLIER | PASS | +12.0 pp | REVIEW | FRESH | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Yihan Qu (`KXWTAMATCH-26OCT23YIHKOS-YIH`) | 0.14 / 0.15 (363) | 14.5% | 3.0% | 8.0% | 5.4% [4.6%-6.1%] | -- | 15.5% | 15.5% | MODEL_LONE_OUTLIER | PASS | -11.5 pp | REVIEW | FRESH | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 377.0, B 3286.0; serve-point win A 50.3%, B 35.3%; Elo A 1192.8, B 1710.9; model uncertainty 0.0075
* Form inputs: days since last match A 6, B 8; matches on record A 16, B 114; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.007, surface_dev_loose -0.003, surface_dev_tight +0.001
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT23YIHKOS-1-KOS` Will Teodora Kostovic win set 1 in the Yihan Qu vs Teodora Kostovic match: 0.75/0.77 mid 76.0%, model 89.6% (projection_v2.0 (prediction ledger)) -- gap +13.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXWTASETWINNER-26OCT23YIHKOS-1-YIH` Will Yihan Qu win set 1 in the Yihan Qu vs Teodora Kostovic match: 0.20/0.24 mid 22.0%, model 10.4% (projection_v2.0 (prediction ledger)) -- gap -11.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXWTASETWINNER-26OCT23YIHKOS-2-KOS` Will Teodora Kostovic win set 2 in the Yihan Qu vs Teodora Kostovic match: 0.76/0.82 mid 79.0%, model 89.6% (projection_v2.0 (prediction ledger)) -- gap +10.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXWTASETWINNER-26OCT23YIHKOS-2-YIH` Will Yihan Qu win set 2 in the Yihan Qu vs Teodora Kostovic match: 0.18/0.23 mid 20.5%, model 10.4% (projection_v2.0 (prediction ledger)) -- gap -10.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data POOR
* Warnings: SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE

## Sebastian Baez vs Giovanni Mpetshi Perricard -- ATP Basel Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 11:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 12:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 11:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:202104:208659:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sebastian Baez (`KXATPMATCH-26OCT24BAEMPE-BAE`) | 0.38 / 0.40 (23234) | 39.0% | 52.0% | 59.3% | 57.5% [56.1%-58.4%] | 40.6% | 38.8% | 39.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +13.0 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Giovanni Mpetshi Perricard (`KXATPMATCH-26OCT24BAEMPE-MPE`) | 0.60 / 0.62 (25211) | 61.0% | 48.0% | 40.7% | 42.5% [41.6%-43.9%] | 59.4% | 61.4% | 60.4% | MODEL_LONE_OUTLIER | PASS | -13.0 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4992.0, B 3847.0; serve-point win A 69.2%, B 31.2%; Elo A 1715.5, B 1698.8; model uncertainty 0.0116
* Form inputs: days since last match A 4, B 7; matches on record A 494, B 309; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose -0.005, surface_dev_tight +0.000
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT24BAEMPE-MPE20` Will Giovanni Mpetshi Perricard win the Sebastian Baez vs Giovanni Mpetshi Perricard match by a set score of 2-0?: 0.35/0.37 mid 36.0%, model 23.7% (projection_v2.0 (prediction ledger)) -- gap -12.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BAEMPE-2-BAE` Will Sebastian Baez win set 2 in the Sebastian Baez vs Giovanni Mpetshi Perricard match: 0.38/0.44 mid 41.0%, model 51.3% (projection_v2.0 (prediction ledger)) -- gap +10.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BAEMPE-2-MPE` Will Giovanni Mpetshi Perricard win set 2 in the Sebastian Baez vs Giovanni Mpetshi Perricard match: 0.56/0.62 mid 59.0%, model 48.6% (projection_v2.0 (prediction ledger)) -- gap -10.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BAEMPE-1-BAE` Will Sebastian Baez win set 1 in the Sebastian Baez vs Giovanni Mpetshi Perricard match: 0.41/0.44 mid 42.5%, model 51.3% (projection_v2.0 (prediction ledger)) -- gap +8.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BAEMPE-1-MPE` Will Giovanni Mpetshi Perricard win set 1 in the Sebastian Baez vs Giovanni Mpetshi Perricard match: 0.55/0.58 mid 56.5%, model 48.6% (projection_v2.0 (prediction ledger)) -- gap -7.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24BAEMPE-BAE21` Will Sebastian Baez win the Sebastian Baez vs Giovanni Mpetshi Perricard match by a set score of 2-1?: 0.16/0.21 mid 18.5%, model 25.7% (projection_v2.0 (prediction ledger)) -- gap +7.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24BAEMPE-BAE20` Will Sebastian Baez win the Sebastian Baez vs Giovanni Mpetshi Perricard match by a set score of 2-0?: 0.18/0.23 mid 20.5%, model 26.4% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24BAEMPE-MPE21` Will Giovanni Mpetshi Perricard win the Sebastian Baez vs Giovanni Mpetshi Perricard match by a set score of 2-1?: 0.20/0.25 mid 22.5%, model 24.3% (projection_v2.0 (prediction ledger)) -- gap +1.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE

## Alex Molcan vs Hamad Medjedovic -- ATP Vienna Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 14:20Z
* Current expected start: 2026-10-24 12:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 11:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-140_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T14:20:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144684:209098:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hamad Medjedovic (`KXATPMATCH-26OCT24MOLMED-MED`) | 0.59 / 0.61 (8514) | 60.0% | 46.1% | 40.8% | 43.6% [41.7%-45.6%] | 60.9% | 59.9% | 60.4% | MODEL_LONE_OUTLIER | PASS | -13.9 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Alex Molcan (`KXATPMATCH-26OCT24MOLMED-MOL`) | 0.39 / 0.41 (29293) | 40.0% | 53.9% | 59.2% | 56.4% [54.4%-58.3%] | 39.1% | 40.0% | 39.6% | MODEL_LONE_OUTLIER | SHADOW_BET | +13.9 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3131.0, B 3309.0; serve-point win A 65.6%, B 35.1%; Elo A 1748.0, B 1741.5; model uncertainty 0.0193
* Form inputs: days since last match A 17, B 4; matches on record A 508, B 285; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.010, surface_dev_loose +0.014, surface_dev_tight -0.009
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT24MOLMED-MED20` Will Hamad Medjedovic win the Alex Molcan vs Hamad Medjedovic match by a set score of 2-0?: 0.36/0.40 mid 38.0%, model 22.5% (projection_v2.0 (prediction ledger)) -- gap -15.5 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MOLMED-2-MOL` Will Alex Molcan win set 2 in the Alex Molcan vs Hamad Medjedovic match: 0.39/0.42 mid 40.5%, model 52.6% (projection_v2.0 (prediction ledger)) -- gap +12.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MOLMED-1-MOL` Will Alex Molcan win set 1 in the Alex Molcan vs Hamad Medjedovic match: 0.41/0.43 mid 42.0%, model 52.6% (projection_v2.0 (prediction ledger)) -- gap +10.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MOLMED-MOL21` Will Alex Molcan win the Alex Molcan vs Hamad Medjedovic match by a set score of 2-1?: 0.14/0.18 mid 16.0%, model 26.2% (projection_v2.0 (prediction ledger)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MOLMED-1-MED` Will Hamad Medjedovic win set 1 in the Alex Molcan vs Hamad Medjedovic match: 0.56/0.59 mid 57.5%, model 47.4% (projection_v2.0 (prediction ledger)) -- gap -10.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MOLMED-2-MED` Will Hamad Medjedovic win set 2 in the Alex Molcan vs Hamad Medjedovic match: 0.55/0.60 mid 57.5%, model 47.4% (projection_v2.0 (prediction ledger)) -- gap -10.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MOLMED-MOL20` Will Alex Molcan win the Alex Molcan vs Hamad Medjedovic match by a set score of 2-0?: 0.20/0.23 mid 21.5%, model 27.7% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MOLMED-MED21` Will Hamad Medjedovic win the Alex Molcan vs Hamad Medjedovic match by a set score of 2-1?: 0.19/0.24 mid 21.5%, model 23.6% (projection_v2.0 (prediction ledger)) -- gap +2.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE

## En-Shuo Liang vs Tereza Valentova -- WTA Tokyo Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 08:00Z
* Current expected start: 2026-10-24 12:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 11:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+240_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215314:238184:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| En-Shuo Liang (`KXWTAMATCH-26OCT24LIAVAL-LIA`) | 0.13 / 0.14 (4894) | 13.5% | -- | 18.0% | 19.0% [16.3%-21.6%] | 14.7% | 13.3% | 13.3% | MARKETS_AGREE | SHADOW_BET | +5.5 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Tereza Valentova (`KXWTAMATCH-26OCT24LIAVAL-VAL`) | 0.86 / 0.87 (1466) | 86.5% | -- | 82.0% | 81.0% [78.4%-83.7%] | 85.3% | 86.9% | -- | INSUFFICIENT_INPUTS | PASS | -5.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2476.0, B 3231.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0268
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.027, surface_pool_high +0.026, surface_dev_loose -0.004, surface_dev_tight -0.000
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: SCHEDULED_START_PASSED; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Henry Bernet vs Daniel Altmaier -- ATP Basel Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 11:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 12:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 11:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:127157:148679:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Altmaier (`KXATPMATCH-26OCT24BERALT-ALT`) | 0.55 / 0.56 (4531) | 55.5% | 62.9% | 48.5% | 63.8% [53.9%-76.5%] | 55.6% | 56.2% | 55.9% | MODEL_LONE_OUTLIER | WATCH | +7.4 pp | NORMAL | FRESH | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Henry Bernet (`KXATPMATCH-26OCT24BERALT-BER`) | 0.43 / 0.44 (301) | 43.5% | 37.1% | 51.5% | 36.2% [23.5%-46.1%] | 44.4% | 44.5% | 44.4% | MODEL_LONE_OUTLIER | PASS | -6.4 pp | NORMAL | FRESH | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1360.0, B 5258.0; serve-point win A 64.9%, B 32.4%; Elo A 1515.4, B 1714.1; model uncertainty 0.1134
* Form inputs: days since last match A 12, B 2; matches on record A 34, B 707; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.066, surface_pool_high +0.080, surface_dev_loose +0.019, surface_dev_tight -0.023
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT24BERALT-BER20` Will Henry Bernet win the Henry Bernet vs Daniel Altmaier match by a set score of 2-0?: 0.23/0.27 mid 25.0%, model 17.1% (projection_v2.0 (prediction ledger)) -- gap -7.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24BERALT-ALT21` Will Daniel Altmaier win the Henry Bernet vs Daniel Altmaier match by a set score of 2-1?: 0.20/0.24 mid 22.0%, model 28.5% (projection_v2.0 (prediction ledger)) -- gap +6.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BERALT-2-BER` Will Henry Bernet win set 2 in the Henry Bernet vs Daniel Altmaier match: 0.13/0.81 mid 47.0%, model 41.3% (projection_v2.0 (prediction ledger)) -- gap -5.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BERALT-1-ALT` Will Daniel Altmaier win set 1 in the Henry Bernet vs Daniel Altmaier match: 0.52/0.55 mid 53.5%, model 58.7% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BERALT-1-BER` Will Henry Bernet win set 1 in the Henry Bernet vs Daniel Altmaier match: 0.45/0.48 mid 46.5%, model 41.3% (projection_v2.0 (prediction ledger)) -- gap -5.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BERALT-2-ALT` Will Daniel Altmaier win set 2 in the Henry Bernet vs Daniel Altmaier match: 0.19/0.89 mid 54.0%, model 58.7% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24BERALT-BER21` Will Henry Bernet win the Henry Bernet vs Daniel Altmaier match by a set score of 2-1?: 0.17/0.21 mid 19.0%, model 20.0% (projection_v2.0 (prediction ledger)) -- gap +1.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24BERALT-ALT20` Will Daniel Altmaier win the Henry Bernet vs Daniel Altmaier match by a set score of 2-0?: 0.32/0.35 mid 33.5%, model 34.4% (projection_v2.0 (prediction ledger)) -- gap +0.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Fabian Marozsan vs Sebastian Sorger -- ATP Vienna Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 14:50Z
* Current expected start: 2026-10-24 12:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 11:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-140_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T14:50:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:206681:210285:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fabian Marozsan (`KXATPMATCH-26OCT24MARSOR-MAR`) | 0.82 / 0.84 (20588) | 83.0% | 86.7% | 75.9% | 88.1% [84.0%-91.7%] | 81.8% | 83.4% | 82.6% | MODEL_LONE_OUTLIER | WATCH | +3.7 pp | NORMAL | FRESH | B / LIMITED | ALL_AGREE | VERIFIED |
| Sebastian Sorger (`KXATPMATCH-26OCT24MARSOR-SOR`) | 0.16 / 0.17 (282) | 16.5% | 13.3% | 24.1% | 11.9% [8.3%-16.0%] | 18.2% | 16.8% | 17.5% | MODEL_LONE_OUTLIER | PASS | -3.2 pp | NORMAL | FRESH | B / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4525.0, B 572.0; serve-point win A 67.5%, B 41.3%; Elo A 1780.4, B 1368.9; model uncertainty 0.0387
* Form inputs: days since last match A 4, B 47; matches on record A 440, B 154; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.024, surface_dev_loose -0.000, surface_dev_tight -0.000
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT24MARSOR-MAR21` Will Fabian Marozsan win the Fabian Marozsan vs Sebastian Sorger match by a set score of 2-1?: 0.18/0.23 mid 20.5%, model 27.2% (projection_v2.0 (prediction ledger)) -- gap +6.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPEXACTMATCH-26OCT24MARSOR-MAR20` Will Fabian Marozsan win the Fabian Marozsan vs Sebastian Sorger match by a set score of 2-0?: 0.61/0.64 mid 62.5%, model 59.5% (projection_v2.0 (prediction ledger)) -- gap -3.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPSETWINNER-26OCT24MARSOR-2-SOR` Will Sebastian Sorger win set 2 in the Fabian Marozsan vs Sebastian Sorger match: 0.19/0.24 mid 21.5%, model 22.9% (projection_v2.0 (prediction ledger)) -- gap +1.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPEXACTMATCH-26OCT24MARSOR-SOR20` Will Sebastian Sorger win the Fabian Marozsan vs Sebastian Sorger match by a set score of 2-0?: 0.06/0.07 mid 6.5%, model 5.2% (projection_v2.0 (prediction ledger)) -- gap -1.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPSETWINNER-26OCT24MARSOR-1-SOR` Will Sebastian Sorger win set 1 in the Fabian Marozsan vs Sebastian Sorger match: 0.23/0.24 mid 23.5%, model 22.9% (projection_v2.0 (prediction ledger)) -- gap -0.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPEXACTMATCH-26OCT24MARSOR-SOR21` Will Sebastian Sorger win the Fabian Marozsan vs Sebastian Sorger match by a set score of 2-1?: 0.06/0.09 mid 7.5%, model 8.1% (projection_v2.0 (prediction ledger)) -- gap +0.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPSETWINNER-26OCT24MARSOR-1-MAR` Will Fabian Marozsan win set 1 in the Fabian Marozsan vs Sebastian Sorger match: 0.76/0.78 mid 77.0%, model 77.1% (projection_v2.0 (prediction ledger)) -- gap +0.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT24MARSOR-2-MAR` Will Fabian Marozsan win set 2 in the Fabian Marozsan vs Sebastian Sorger match: 0.75/0.79 mid 77.0%, model 77.1% (projection_v2.0 (prediction ledger)) -- gap +0.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED

## Sandro Kopp vs Filippo Romano -- ATP Challenger Florence SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-24T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207491:211542:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sandro Kopp (`KXATPCHALLENGERMATCH-26OCT24KOPROM-KOP`) | 0.50 / 0.53 (148) | 51.5% | 41.7% | 45.0% | 47.0% [45.1%-50.0%] | -- | 51.4% | 51.4% | MARKETS_AGREE | PASS | -9.8 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Filippo Romano (`KXATPCHALLENGERMATCH-26OCT24KOPROM-ROM`) | 0.47 / 0.50 (172) | 48.5% | 58.3% | 55.0% | 53.0% [50.0%-54.9%] | -- | 48.1% | 48.1% | MARKETS_AGREE | SHADOW_BET | +9.8 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2600.0, B 1962.0; serve-point win A 63.2%, B 35.1%; Elo A 1417.3, B 1425.4; model uncertainty 0.0247
* Form inputs: days since last match A 12, B 12; matches on record A 332, B 95; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.019, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Daniil Medvedev vs Alexander Bublik -- ATP Almaty SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 16:00Z
* Current expected start: 2026-10-24 13:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 12:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:106421:122330:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Bublik (`KXATPMATCH-26OCT24MEDBUB-BUB`) | 0.34 / 0.35 (20802) | 34.5% | 32.1% | 30.5% | 30.5% [29.6%-32.1%] | 35.4% | 35.4% | 35.4% | MODEL_LONE_OUTLIER | PASS | -2.4 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Daniil Medvedev (`KXATPMATCH-26OCT24MEDBUB-MED`) | 0.65 / 0.66 (115862) | 65.5% | 67.9% | 69.5% | 69.5% [67.8%-70.4%] | 64.6% | 64.6% | 64.6% | MODEL_LONE_OUTLIER | SHADOW_BET | +2.4 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5908.0, B 5279.0; serve-point win A 68.3%, B 35.5%; Elo A 2100.7, B 1950.5; model uncertainty 0.0126
* Form inputs: days since last match A 2, B 11; matches on record A 859, B 705; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose -0.000, surface_dev_tight +0.001
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT24MEDBUB-29` Over 28.5 games: 0.28/0.32 mid 30.0%, model 37.0% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24MEDBUB-MED6` Will Daniil Medvedev win at least 5.5 more games than Alexander Bublik?: 0.12/0.26 mid 19.0%, model 12.2% (projection_v2.0 (prediction ledger)) -- gap -6.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MEDBUB-MED21` Will Daniil Medvedev win the Daniil Medvedev vs Alexander Bublik match by a set score of 2-1?: 0.22/0.26 mid 24.0%, model 29.2% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24MEDBUB-MED3` Will Daniil Medvedev win at least 2.5 more games than Alexander Bublik?: 0.47/0.48 mid 47.5%, model 51.2% (projection_v2.0 (prediction ledger)) -- gap +3.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MEDBUB-BUB20` Will Alexander Bublik win the Daniil Medvedev vs Alexander Bublik match by a set score of 2-0?: 0.17/0.19 mid 18.0%, model 14.3% (projection_v2.0 (prediction ledger)) -- gap -3.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24MEDBUB-24` Over 23.5 games: 0.50/0.51 mid 50.5%, model 53.5% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MEDBUB-BUB21` Will Alexander Bublik win the Daniil Medvedev vs Alexander Bublik match by a set score of 2-1?: 0.14/0.17 mid 15.5%, model 17.8% (projection_v2.0 (prediction ledger)) -- gap +2.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MEDBUB-1-BUB` Will Alexander Bublik win set 1 in the Daniil Medvedev vs Alexander Bublik match: 0.39/0.40 mid 39.5%, model 37.8% (projection_v2.0 (prediction ledger)) -- gap -1.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MEDBUB-1-MED` Will Daniil Medvedev win set 1 in the Daniil Medvedev vs Alexander Bublik match: 0.59/0.62 mid 60.5%, model 62.2% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MEDBUB-2-MED` Will Daniil Medvedev win set 2 in the Daniil Medvedev vs Alexander Bublik match: 0.59/0.62 mid 60.5%, model 62.2% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MEDBUB-2-BUB` Will Alexander Bublik win set 2 in the Daniil Medvedev vs Alexander Bublik match: 0.37/0.40 mid 38.5%, model 37.8% (projection_v2.0 (prediction ledger)) -- gap -0.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT24MEDBUB-19` Over 18.5 games: 0.89/0.90 mid 89.5%, model 89.9% (projection_v2.0 (prediction ledger)) -- gap +0.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24MEDBUB-BUB2` Will Alexander Bublik win at least 1.5 more games than Daniil Medvedev?: 0.24/0.27 mid 25.5%, model 25.1% (projection_v2.0 (prediction ledger)) -- gap -0.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MEDBUB-MED20` Will Daniil Medvedev win the Daniil Medvedev vs Alexander Bublik match by a set score of 2-0?: 0.38/0.40 mid 39.0%, model 38.6% (projection_v2.0 (prediction ledger)) -- gap -0.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Marco Trungelliti vs Alexander Ritschard -- ATP Challenger Lisbon SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-24T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105477:106310:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Ritschard (`KXATPCHALLENGERMATCH-26OCT24TRURIT-RIT`) | 0.71 / 0.72 (30901) | 71.5% | 48.5% | 46.4% | 45.9% [44.4%-46.9%] | 46.9% | 46.5% | 46.5% | MODEL_LONE_OUTLIER | PASS | -23.0 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Marco Trungelliti (`KXATPCHALLENGERMATCH-26OCT24TRURIT-TRU`) | 0.28 / 0.29 (42586) | 28.5% | 51.5% | 53.6% | 54.1% [53.1%-55.6%] | 53.1% | 53.2% | 53.2% | MODEL_LONE_OUTLIER | PASS | +23.0 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4942.0, B 1877.0; serve-point win A 60.3%, B 40.0%; Elo A 1773.3, B 1736.4; model uncertainty 0.0128
* Form inputs: days since last match A 12, B 47; matches on record A 987, B 519; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT24TRURIT-TRU  (YES = Marco Trungelliti)
Model: 52%
Kalshi: 28%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: EXTERNAL_STALE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.015, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Karla Popovic vs Sandra Samir -- W15 Sharm ElSheikh SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:210500:211529:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karla Popovic (`KXITFWMATCH-26OCT24POPSAM-POP`) | 0.04 / 0.05 (231) | 4.5% | -- | 51.6% | 42.5% [32.9%-48.9%] | -- | -- | -- | -- | PASS | +38.0 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sandra Samir (`KXITFWMATCH-26OCT24POPSAM-SAM`) | 0.95 / 0.96 (179) | 95.5% | -- | 48.4% | 57.5% [51.1%-67.1%] | -- | -- | -- | -- | WATCH | -38.0 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1204.0, B 4604.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0802
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT24POPSAM-POP  (YES = Karla Popovic)
Model: 43%
Kalshi: 4%
Gap: +38 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.031, surface_pool_high +0.021, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mattia Nannelli / Leonardo Rossi vs Jacopo Bilardo / Giorgio Ricca -- ATP Challenger Florence QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 13:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-24T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24NANROSBILRIC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jacopo Bilardo / Giorgio Ricca (`KXATPCHALLENGERDOUBLES-26OCT24NANROSBILRIC-BILRIC`) | 0.60 / 0.85 (171) | 72.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mattia Nannelli / Leonardo Rossi (`KXATPCHALLENGERDOUBLES-26OCT24NANROSBILRIC-NANROS`) | 0.12 / 0.38 (993) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Aleksandar Kovacevic vs James Duckworth -- ATP Basel Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 11:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 13:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 12:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105902:206499:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| James Duckworth (`KXATPMATCH-26OCT24KOVDUC-DUC`) | 0.38 / 0.39 (1584) | 38.5% | 44.0% | 56.5% | 54.6% [51.9%-57.9%] | 40.6% | 39.9% | 40.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +5.5 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Aleksandar Kovacevic (`KXATPMATCH-26OCT24KOVDUC-KOV`) | 0.61 / 0.62 (25985) | 61.5% | 56.0% | 43.5% | 45.4% [42.1%-48.1%] | 59.4% | 60.3% | 59.8% | MODEL_LONE_OUTLIER | PASS | -5.5 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4778.0, B 5151.0; serve-point win A 70.6%, B 30.7%; Elo A 1756.5, B 1745.6; model uncertainty 0.0303
* Form inputs: days since last match A 4, B 1; matches on record A 400, B 900; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.032, surface_pool_high +0.028, surface_dev_loose +0.005, surface_dev_tight -0.005
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT24KOVDUC-2-KOV` Will Aleksandar Kovacevic win set 2 in the Aleksandar Kovacevic vs James Duckworth match: 0.21/0.60 mid 40.5%, model 54.0% (projection_v2.0 (prediction ledger)) -- gap +13.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24KOVDUC-2-DUC` Will James Duckworth win set 2 in the Aleksandar Kovacevic vs James Duckworth match: 0.21/0.56 mid 38.5%, model 46.0% (projection_v2.0 (prediction ledger)) -- gap +7.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24KOVDUC-DUC21` Will James Duckworth win the Aleksandar Kovacevic vs James Duckworth match by a set score of 2-1?: 0.16/0.20 mid 18.0%, model 22.9% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24KOVDUC-1-DUC` Will James Duckworth win set 1 in the Aleksandar Kovacevic vs James Duckworth match: 0.40/0.44 mid 42.0%, model 46.0% (projection_v2.0 (prediction ledger)) -- gap +4.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24KOVDUC-1-KOV` Will Aleksandar Kovacevic win set 1 in the Aleksandar Kovacevic vs James Duckworth match: 0.56/0.60 mid 58.0%, model 54.0% (projection_v2.0 (prediction ledger)) -- gap -4.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24KOVDUC-KOV21` Will Aleksandar Kovacevic win the Aleksandar Kovacevic vs James Duckworth match by a set score of 2-1?: 0.21/0.25 mid 23.0%, model 26.8% (projection_v2.0 (prediction ledger)) -- gap +3.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24KOVDUC-DUC20` Will James Duckworth win the Aleksandar Kovacevic vs James Duckworth match by a set score of 2-0?: 0.20/0.24 mid 22.0%, model 21.2% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24KOVDUC-KOV20` Will Aleksandar Kovacevic win the Aleksandar Kovacevic vs James Duckworth match by a set score of 2-0?: 0.23/0.37 mid 30.0%, model 29.2% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Remy Bertola vs Jakub Paul -- ATP Basel Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 16:40Z
* Current expected start: 2026-10-24 14:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 13:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN

ATP (TOUR_500_250) · surface ? · scheduled 2026-10-24T16:40:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT24BERPAU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Remy Bertola (`KXATPMATCH-26OCT24BERPAU-BER`) | 0.70 / 0.72 (418) | 71.0% | -- | -- | -- [-----] | -- | 69.9% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jakub Paul (`KXATPMATCH-26OCT24BERPAU-PAU`) | 0.28 / 0.30 (27) | 29.0% | -- | -- | -- [-----] | -- | 30.4% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Francisco Cerundolo vs Tallon Griekspoor -- ATP Brussels SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 17:00Z
* Current expected start: 2026-10-24 14:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 13:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:134868:202103:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francisco Cerundolo (`KXATPMATCH-26OCT24CERGRI-CER`) | 0.60 / 0.61 (28882) | 60.5% | 59.1% | 64.7% | 61.5% [58.7%-62.9%] | 60.9% | 60.6% | 60.8% | MODEL_LONE_OUTLIER | PASS | -1.4 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Tallon Griekspoor (`KXATPMATCH-26OCT24CERGRI-GRI`) | 0.39 / 0.40 (7958) | 39.5% | 40.9% | 35.3% | 38.5% [37.1%-41.3%] | 39.1% | 39.4% | 39.2% | MODEL_LONE_OUTLIER | PASS | +1.4 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5642.0, B 4445.0; serve-point win A 67.1%, B 34.8%; Elo A 1873.6, B 1873.8; model uncertainty 0.021
* Form inputs: days since last match A 15, B 3; matches on record A 553, B 679; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.019, surface_dev_loose -0.005, surface_dev_tight -0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT24CERGRI-25` Over 24.5 games: 0.45/0.46 mid 45.5%, model 54.9% (projection_v2.0 (prediction ledger)) -- gap +9.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24CERGRI-30` Over 29.5 games: 0.26/0.27 mid 26.5%, model 34.4% (projection_v2.0 (prediction ledger)) -- gap +7.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24CERGRI-CER5` Will Francisco Cerundolo win at least 4.5 more games than Tallon Griekspoor?: 0.23/0.28 mid 25.5%, model 18.3% (projection_v2.0 (prediction ledger)) -- gap -7.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24CERGRI-CER20` Will Francisco Cerundolo win the Francisco Cerundolo vs Tallon Griekspoor match by a set score of 2-0?: 0.37/0.40 mid 38.5%, model 31.4% (projection_v2.0 (prediction ledger)) -- gap -7.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24CERGRI-CER21` Will Francisco Cerundolo win the Francisco Cerundolo vs Tallon Griekspoor match by a set score of 2-1?: 0.20/0.24 mid 22.0%, model 27.6% (projection_v2.0 (prediction ledger)) -- gap +5.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24CERGRI-GRI21` Will Tallon Griekspoor win the Francisco Cerundolo vs Tallon Griekspoor match by a set score of 2-1?: 0.15/0.19 mid 17.0%, model 21.6% (projection_v2.0 (prediction ledger)) -- gap +4.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24CERGRI-CER2` Will Francisco Cerundolo win at least 1.5 more games than Tallon Griekspoor?: 0.55/0.56 mid 55.5%, model 51.0% (projection_v2.0 (prediction ledger)) -- gap -4.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24CERGRI-20` Over 19.5 games: 0.76/0.84 mid 80.0%, model 84.0% (projection_v2.0 (prediction ledger)) -- gap +4.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24CERGRI-GRI2` Will Tallon Griekspoor win at least 1.5 more games than Francisco Cerundolo?: 0.28/0.31 mid 29.5%, model 33.3% (projection_v2.0 (prediction ledger)) -- gap +3.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24CERGRI-2-GRI` Will Tallon Griekspoor win set 2 in the Francisco Cerundolo vs Tallon Griekspoor match: 0.39/0.42 mid 40.5%, model 43.9% (projection_v2.0 (prediction ledger)) -- gap +3.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24CERGRI-1-GRI` Will Tallon Griekspoor win set 1 in the Francisco Cerundolo vs Tallon Griekspoor match: 0.40/0.43 mid 41.5%, model 43.9% (projection_v2.0 (prediction ledger)) -- gap +2.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24CERGRI-1-CER` Will Francisco Cerundolo win set 1 in the Francisco Cerundolo vs Tallon Griekspoor match: 0.56/0.60 mid 58.0%, model 56.1% (projection_v2.0 (prediction ledger)) -- gap -1.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24CERGRI-2-CER` Will Francisco Cerundolo win set 2 in the Francisco Cerundolo vs Tallon Griekspoor match: 0.56/0.60 mid 58.0%, model 56.1% (projection_v2.0 (prediction ledger)) -- gap -1.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24CERGRI-GRI20` Will Tallon Griekspoor win the Francisco Cerundolo vs Tallon Griekspoor match by a set score of 2-0?: 0.19/0.21 mid 20.0%, model 19.3% (projection_v2.0 (prediction ledger)) -- gap -0.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Flavio Cobolli vs Lorenzo Musetti -- ATP Lyon SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 16:10Z
* Current expected start: 2026-10-24 14:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 13:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-130_MIN

ATP (TOUR_500_250) · Clay · scheduled 2026-10-24T16:10:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207518:207925:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Flavio Cobolli (`KXATPMATCH-26OCT24COBMUS-COB`) | 0.53 / 0.54 (12253) | 53.5% | 36.0% | 39.4% | 37.0% [35.6%-38.5%] | 54.3% | 54.8% | 54.5% | MODEL_LONE_OUTLIER | PASS | -17.5 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Lorenzo Musetti (`KXATPMATCH-26OCT24COBMUS-MUS`) | 0.46 / 0.47 (88779) | 46.5% | 64.0% | 60.6% | 63.0% [61.6%-64.4%] | 45.7% | 44.9% | 45.3% | ALL_THREE_DISAGREE | SHADOW_BET | +17.5 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 6397.0, B 4401.0; serve-point win A 60.2%, B 37.0%; Elo A 1959.6, B 2103.9; model uncertainty 0.0145
* Form inputs: days since last match A 2, B 3; matches on record A 443, B 468; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT24COBMUS-MUS  (YES = Lorenzo Musetti)
Model: 64%
Kalshi: 46%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: EXTERNAL_MARKET_REJECTION, UNKNOWN
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.009, surface_dev_tight -0.009
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT24COBMUS-COB2` Will Flavio Cobolli win at least 1.5 more games than Lorenzo Musetti?: 0.47/0.48 mid 47.5%, model 29.4% (projection_v2.0 (prediction ledger)) -- gap -18.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24COBMUS-COB20` Will Flavio Cobolli win the Flavio Cobolli vs Lorenzo Musetti match by a set score of 2-0?: 0.31/0.33 mid 32.0%, model 16.4% (projection_v2.0 (prediction ledger)) -- gap -15.6 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24COBMUS-MUS2` Will Lorenzo Musetti win at least 1.5 more games than Flavio Cobolli?: 0.43/0.44 mid 43.5%, model 57.2% (projection_v2.0 (prediction ledger)) -- gap +13.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24COBMUS-2-MUS` Will Lorenzo Musetti win set 2 in the Flavio Cobolli vs Lorenzo Musetti match: 0.45/0.48 mid 46.5%, model 59.5% (projection_v2.0 (prediction ledger)) -- gap +13.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24COBMUS-1-MUS` Will Lorenzo Musetti win set 1 in the Flavio Cobolli vs Lorenzo Musetti match: 0.46/0.48 mid 47.0%, model 59.5% (projection_v2.0 (prediction ledger)) -- gap +12.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24COBMUS-1-COB` Will Flavio Cobolli win set 1 in the Flavio Cobolli vs Lorenzo Musetti match: 0.51/0.54 mid 52.5%, model 40.5% (projection_v2.0 (prediction ledger)) -- gap -12.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24COBMUS-2-COB` Will Flavio Cobolli win set 2 in the Flavio Cobolli vs Lorenzo Musetti match: 0.50/0.53 mid 51.5%, model 40.5% (projection_v2.0 (prediction ledger)) -- gap -11.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24COBMUS-MUS20` Will Lorenzo Musetti win the Flavio Cobolli vs Lorenzo Musetti match by a set score of 2-0?: 0.25/0.29 mid 27.0%, model 35.4% (projection_v2.0 (prediction ledger)) -- gap +8.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24COBMUS-MUS21` Will Lorenzo Musetti win the Flavio Cobolli vs Lorenzo Musetti match by a set score of 2-1?: 0.19/0.22 mid 20.5%, model 28.7% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24COBMUS-MUS5` Will Lorenzo Musetti win at least 4.5 more games than Flavio Cobolli?: 0.21/0.24 mid 22.5%, model 27.8% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24COBMUS-23` Over 22.5 games: 0.52/0.53 mid 52.5%, model 57.4% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24COBMUS-28` Over 27.5 games: 0.33/0.34 mid 33.5%, model 37.1% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24COBMUS-COB21` Will Flavio Cobolli win the Flavio Cobolli vs Lorenzo Musetti match by a set score of 2-1?: 0.19/0.22 mid 20.5%, model 19.5% (projection_v2.0 (prediction ledger)) -- gap -1.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24COBMUS-18` Over 17.5 games: 0.89/0.93 mid 91.0%, model 90.8% (projection_v2.0 (prediction ledger)) -- gap -0.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE

## Corentin Moutet vs Tomas Machac -- ATP Vienna Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 17:00Z
* Current expected start: 2026-10-24 14:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 13:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144895:207830:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tomas Machac (`KXATPMATCH-26OCT24MOUMAC-MAC`) | 0.57 / 0.59 (15156) | 58.0% | 56.0% | 45.4% | 50.0% [48.0%-55.1%] | 58.3% | 57.4% | 57.8% | MODEL_LONE_OUTLIER | PASS | -2.0 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Corentin Moutet (`KXATPMATCH-26OCT24MOUMAC-MOU`) | 0.42 / 0.43 (2868) | 42.5% | 44.0% | 54.6% | 50.0% [44.9%-52.0%] | 41.7% | 42.8% | 42.2% | MODEL_LONE_OUTLIER | WATCH | +1.6 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4376.0, B 3720.0; serve-point win A 60.6%, B 38.3%; Elo A 1823.8, B 1918.6; model uncertainty 0.0357
* Form inputs: days since last match A 3, B 2; matches on record A 586, B 445; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight -0.015
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT24MOUMAC-MAC21` Will Tomas Machac win the Corentin Moutet vs Tomas Machac match by a set score of 2-1?: 0.02/0.24 mid 13.0%, model 26.8% (projection_v2.0 (prediction ledger)) -- gap +13.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MOUMAC-MOU21` Will Corentin Moutet win the Corentin Moutet vs Tomas Machac match by a set score of 2-1?: 0.02/0.20 mid 11.0%, model 22.9% (projection_v2.0 (prediction ledger)) -- gap +11.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MOUMAC-MAC20` Will Tomas Machac win the Corentin Moutet vs Tomas Machac match by a set score of 2-0?: 0.02/0.38 mid 20.0%, model 29.1% (projection_v2.0 (prediction ledger)) -- gap +9.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MOUMAC-MOU20` Will Corentin Moutet win the Corentin Moutet vs Tomas Machac match by a set score of 2-0?: 0.02/0.25 mid 13.5%, model 21.2% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MOUMAC-2-MAC` Will Tomas Machac win set 2 in the Corentin Moutet vs Tomas Machac match: 0.20/0.78 mid 49.0%, model 54.0% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MOUMAC-1-MOU` Will Corentin Moutet win set 1 in the Corentin Moutet vs Tomas Machac match: 0.44/0.46 mid 45.0%, model 46.0% (projection_v2.0 (prediction ledger)) -- gap +1.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MOUMAC-1-MAC` Will Tomas Machac win set 1 in the Corentin Moutet vs Tomas Machac match: 0.53/0.55 mid 54.0%, model 54.0% (projection_v2.0 (prediction ledger)) -- gap -0.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MOUMAC-2-MOU` Will Corentin Moutet win set 2 in the Corentin Moutet vs Tomas Machac match: 0.21/0.71 mid 46.0%, model 46.0% (projection_v2.0 (prediction ledger)) -- gap +0.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Amit Vales vs Ioannis Xilas -- M15 Heraklion SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-24T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209354:211707:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amit Vales (`KXITFMATCH-26OCT24VALXIL-VAL`) | 0.63 / 0.64 (9260) | 63.5% | -- | 59.9% | 48.9% [42.8%-53.7%] | 46.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -14.6 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ioannis Xilas (`KXITFMATCH-26OCT24VALXIL-XIL`) | 0.36 / 0.37 (7151) | 36.5% | -- | 40.2% | 51.0% [46.3%-57.2%] | 53.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +14.6 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 397.0, B 992.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0545
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.036, surface_pool_high +0.031, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Popovic / Shinikova vs Alhussein Abdel Aziz / Samir -- W15 Sharm ElSheikh F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-24T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24POPSHIALHSAM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alhussein Abdel Aziz / Samir (`KXITFWDOUBLES-26OCT24POPSHIALHSAM-ALHSAM`) | 0.01 / 0.75 (1) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Popovic / Shinikova (`KXITFWDOUBLES-26OCT24POPSHIALHSAM-POPSHI`) | 0.05 / 0.71 (1) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Svyatoslav Gulin vs Elmer Moller -- ATP Challenger Lisbon SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 14:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-24T14:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209284:210425:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Svyatoslav Gulin (`KXATPCHALLENGERMATCH-26OCT24GULMOL-GUL`) | 0.30 / 0.31 (4693) | 30.5% | 30.8% | 36.0% | 29.8% [25.4%-32.6%] | 32.9% | 31.3% | 31.3% | MODEL_LONE_OUTLIER | PASS | +0.3 pp | NORMAL | FRESH | B / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Elmer Moller (`KXATPCHALLENGERMATCH-26OCT24GULMOL-MOL`) | 0.69 / 0.70 (4050) | 69.5% | 69.2% | 64.0% | 70.2% [67.5%-74.6%] | 67.1% | 69.0% | 69.0% | MODEL_LONE_OUTLIER | PASS | -0.3 pp | NORMAL | FRESH | B / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 1071.0, B 3763.0; serve-point win A 53.7%, B 42.6%; Elo A 1529.5, B 1719.7; model uncertainty 0.0356
* Form inputs: days since last match A 12, B 12; matches on record A 188, B 287; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.022, surface_pool_high +0.019, surface_dev_loose -0.000, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Dorji / Tsheyang Wangmo vs Al-Mudahka / Khalifa -- Billie Jean King Cup Qualifiers UNK

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 14:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TEAM) · surface ? · scheduled 2026-10-24T14:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24DORTSHALMKHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Al-Mudahka / Khalifa (`KXITFWDOUBLES-26OCT24DORTSHALMKHA-ALMKHA`) | 0.01 / 0.99 (632) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dorji / Tsheyang Wangmo (`KXITFWDOUBLES-26OCT24DORTSHALMKHA-DORTSH`) | 0.01 / 0.99 (1282) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Karin Saizan / Usama Ali vs Abualhaj / Sayej -- Billie Jean King Cup Qualifiers UNK

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 14:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TEAM) · surface ? · scheduled 2026-10-24T14:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24KARUSAABUSAY:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Abualhaj / Sayej (`KXITFWDOUBLES-26OCT24KARUSAABUSAY-ABUSAY`) | 0.01 / 0.99 (640) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Karin Saizan / Usama Ali (`KXITFWDOUBLES-26OCT24KARUSAABUSAY-KARUSA`) | 0.01 / 0.99 (1290) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Qureshi / Suhail vs sagheb tehrani / Soltani -- Billie Jean King Cup Qualifiers UNK

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 14:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TEAM) · surface ? · scheduled 2026-10-24T14:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24QURSUHSAGSOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Qureshi / Suhail (`KXITFWDOUBLES-26OCT24QURSUHSAGSOL-QURSUH`) | 0.01 / 0.99 (1390) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| sagheb tehrani / Soltani (`KXITFWDOUBLES-26OCT24QURSUHSAGSOL-SAGSOL`) | 0.01 / 0.99 (540) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Robin Bertrand vs Liam Gavrielides -- M15 Monastir SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-24T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209850:209887:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Robin Bertrand (`KXITFMATCH-26OCT24BERGAV-BER`) | 0.01 / 0.02 (1299) | 1.5% | 65.0% | 49.5% | 61.1% [54.1%-70.8%] | 68.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +63.5 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Liam Gavrielides (`KXITFMATCH-26OCT24BERGAV-GAV`) | 0.98 / 0.99 (657) | 98.5% | 35.0% | 50.5% | 38.9% [29.2%-45.9%] | 31.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -63.5 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2130.0, B 402.0; serve-point win A 62.6%, B 40.4%; Elo A 1543.6, B 1443.8; model uncertainty 0.0834
* Form inputs: days since last match A 159, B 264; matches on record A 313, B 127; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT24BERGAV-BER  (YES = Robin Bertrand)
Model: 65%
Kalshi: 2%
Gap: +63 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.058, surface_pool_high -0.070, surface_dev_loose -0.020, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eliakim Coulibaly vs Thomas Faurel -- M25 Luanda SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209131:212225:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eliakim Coulibaly (`KXITFMATCH-26OCT24COUFAU-COU`) | 0.96 / 0.97 (5854) | 96.5% | 50.4% | 48.5% | 54.6% [52.6%-60.1%] | 52.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -46.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Thomas Faurel (`KXITFMATCH-26OCT24COUFAU-FAU`) | 0.03 / 0.04 (7084) | 3.5% | 49.6% | 51.5% | 45.4% [39.9%-47.4%] | 47.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +46.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1477.0, B 1707.0; serve-point win A 61.0%, B 39.1%; Elo A 1572.6, B 1495.9; model uncertainty 0.0376
* Form inputs: days since last match A 698, B 26; matches on record A 248, B 54; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT24COUFAU-FAU  (YES = Thomas Faurel)
Model: 50%
Kalshi: 4%
Gap: +46 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ferdinand Livet Novkirichka vs Kasra Rahmani -- M15 Monastir SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-24T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212071:212935:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ferdinand Livet Novkirichka (`KXITFMATCH-26OCT24LIVRAH-LIV`) | 0.02 / 0.04 (3597) | 3.0% | 30.0% | 50.0% | 47.0% [47.0%-47.0%] | 25.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +27.0 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Kasra Rahmani (`KXITFMATCH-26OCT24LIVRAH-RAH`) | 0.97 / 0.98 (5176) | 97.5% | 70.0% | 50.0% | 53.0% [53.0%-53.0%] | 74.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -27.5 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 59.9%, B 35.9%; Elo A 1253.1, B 1273.4; model uncertainty 0.0
* Form inputs: days since last match A 880, B 705; matches on record A 1, B 9; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT24LIVRAH-LIV  (YES = Ferdinand Livet Novkirichka)
Model: 30%
Kalshi: 3%
Gap: +27 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tiphanie Lemaitre vs Elena Milovanovic -- W35 Monastir SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-24T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220429:espn:espn:13746:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tiphanie Lemaitre (`KXITFWMATCH-26OCT24LEMMIL-LEM`) | 0.04 / 0.05 (3688) | 4.5% | -- | 40.5% | 55.3% [47.9%-62.6%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +50.8 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elena Milovanovic (`KXITFWMATCH-26OCT24LEMMIL-MIL`) | 0.95 / 0.96 (224) | 95.5% | -- | 59.5% | 44.7% [37.4%-52.1%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -50.8 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 2475.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0736
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT24LEMMIL-LEM  (YES = Tiphanie Lemaitre)
Model: 55%
Kalshi: 4%
Gap: +51 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.074, surface_pool_high +0.073, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kayo Nishimura vs Marie Vogt -- W35 Monastir SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-24T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223100:260613:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kayo Nishimura (`KXITFWMATCH-26OCT24NISVOG-NIS`) | 0.69 / 0.70 (4265) | 69.5% | -- | 25.1% | 34.8% [30.5%-46.8%] | 52.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -34.6 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marie Vogt (`KXITFWMATCH-26OCT24NISVOG-VOG`) | 0.30 / 0.31 (4614) | 30.5% | -- | 74.9% | 65.1% [53.2%-69.5%] | 47.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +34.6 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2288.0, B 2280.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0815
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT24NISVOG-VOG  (YES = Marie Vogt)
Model: 65%
Kalshi: 30%
Gap: +35 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.020, surface_dev_tight +0.025
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Katerina Zajickova vs Daria Lopatetska -- W15 Karlovy Vary F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24ZAJLOP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daria Lopatetska (`KXITFWMATCH-26OCT24ZAJLOP-LOP`) | 0.26 / 0.27 (2722) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Katerina Zajickova (`KXITFWMATCH-26OCT24ZAJLOP-ZAJ`) | 0.73 / 0.74 (5789) | 73.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Michele Ribecai / Gabriele Volpi vs Dominik Recek / Daniel Siniakov -- ATP Challenger Florence QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 15:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-24T15:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24RIBVOLRECSIN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dominik Recek / Daniel Siniakov (`KXATPCHALLENGERDOUBLES-26OCT24RIBVOLRECSIN-RECSIN`) | 0.07 / 0.93 (64) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Michele Ribecai / Gabriele Volpi (`KXATPCHALLENGERDOUBLES-26OCT24RIBVOLRECSIN-RIBVOL`) | 0.06 / 0.29 (28) | 17.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Paul Jubb vs Oliver Tarvet -- M25 Redbridge F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206703:210472:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Paul Jubb (`KXITFMATCH-26OCT24JUBTAR-JUB`) | 0.10 / 0.12 (26) | 11.0% | 30.1% | 33.7% | 36.0% [33.2%-38.0%] | 24.7% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +19.1 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oliver Tarvet (`KXITFMATCH-26OCT24JUBTAR-TAR`) | 0.87 / 0.89 (69) | 88.0% | 69.9% | 66.3% | 64.0% [62.0%-66.8%] | 75.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -18.1 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2131.0, B 1422.0; serve-point win A 59.5%, B 36.4%; Elo A 1604.2, B 1687.5; model uncertainty 0.0238
* Form inputs: days since last match A 61, B 19; matches on record A 326, B 69; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT24JUBTAR-JUB  (YES = Paul Jubb)
Model: 30%
Kalshi: 11%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Thiago Agustin Tirante vs Adrian Mannarino -- ATP Vienna Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 19:00Z
* Current expected start: 2026-10-24 16:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 15:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T19:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105173:202058:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Mannarino (`KXATPMATCH-26OCT24TIRMAN-MAN`) | 0.43 / 0.44 (20228) | 43.5% | 41.3% | 35.7% | 40.8% [38.9%-43.7%] | 43.4% | 42.6% | 43.0% | MODEL_LONE_OUTLIER | PASS | -2.2 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Thiago Agustin Tirante (`KXATPMATCH-26OCT24TIRMAN-TIR`) | 0.58 / 0.59 (3692) | 58.5% | 58.7% | 64.3% | 59.2% [56.3%-61.1%] | 56.6% | 57.5% | 57.0% | MARKETS_AGREE | PASS | +0.2 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4804.0, B 4318.0; serve-point win A 67.0%, B 34.8%; Elo A 1735.0, B 1776.7; model uncertainty 0.0238
* Form inputs: days since last match A 5, B 1; matches on record A 450, B 1276; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.019, surface_dev_loose +0.009, surface_dev_tight -0.009
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT24TIRMAN-2-TIR` Will Thiago Agustin Tirante win set 2 in the Thiago Agustin Tirante vs Adrian Mannarino match: 0.09/0.90 mid 49.5%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24TIRMAN-TIR21` Will Thiago Agustin Tirante win the Thiago Agustin Tirante vs Adrian Mannarino match by a set score of 2-1?: 0.19/0.24 mid 21.5%, model 27.5% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24TIRMAN-MAN20` Will Adrian Mannarino win the Thiago Agustin Tirante vs Adrian Mannarino match by a set score of 2-0?: 0.23/0.28 mid 25.5%, model 19.5% (projection_v2.0 (prediction ledger)) -- gap -6.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24TIRMAN-2-MAN` Will Adrian Mannarino win set 2 in the Thiago Agustin Tirante vs Adrian Mannarino match: 0.09/0.90 mid 49.5%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap -5.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24TIRMAN-MAN21` Will Adrian Mannarino win the Thiago Agustin Tirante vs Adrian Mannarino match by a set score of 2-1?: 0.16/0.21 mid 18.5%, model 21.8% (projection_v2.0 (prediction ledger)) -- gap +3.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24TIRMAN-TIR20` Will Thiago Agustin Tirante win the Thiago Agustin Tirante vs Adrian Mannarino match by a set score of 2-0?: 0.26/0.39 mid 32.5%, model 31.2% (projection_v2.0 (prediction ledger)) -- gap -1.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24TIRMAN-1-MAN` Will Adrian Mannarino win set 1 in the Thiago Agustin Tirante vs Adrian Mannarino match: 0.43/0.47 mid 45.0%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24TIRMAN-1-TIR` Will Thiago Agustin Tirante win set 1 in the Thiago Agustin Tirante vs Adrian Mannarino match: 0.53/0.57 mid 55.0%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap +0.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Isik Kosaner / Massellani vs Bertrand / van Wyk -- M15 Monastir F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-24T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24ISIMASBERVAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bertrand / van Wyk (`KXITFDOUBLES-26OCT24ISIMASBERVAN-BERVAN`) | 0.08 / 0.89 (2) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Isik Kosaner / Massellani (`KXITFDOUBLES-26OCT24ISIMASBERVAN-ISIMAS`) | 0.03 / 0.69 (1) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jack Loge vs Daniel Domingos -- M25 Luanda SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211504:213637:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Domingos (`KXITFMATCH-26OCT24LOGDOM-DOM`) | 0.10 / 0.13 (90) | 11.5% | 18.6% | 47.9% | 31.1% [31.0%-31.2%] | 13.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jack Loge (`KXITFMATCH-26OCT24LOGDOM-LOG`) | 0.86 / 0.90 (33) | 88.0% | 81.4% | 52.1% | 68.9% [68.8%-69.0%] | 86.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 467.0, B 0.0; serve-point win A 63.0%, B 43.9%; Elo A 1378.5, B 1237.8; model uncertainty 0.0013
* Form inputs: days since last match A 82, B 698; matches on record A 89, B 5; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## De Zeeuw / Louise Van den Broek vs Liu / Moccia -- W35 Loule F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-24T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24DEZLOULIUMOC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| De Zeeuw / Louise Van den Broek (`KXITFWDOUBLES-26OCT24DEZLOULIUMOC-DEZLOU`) | 0.56 / 0.64 (10) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Liu / Moccia (`KXITFWDOUBLES-26OCT24DEZLOULIUMOC-LIUMOC`) | 0.36 / 0.40 (45) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Kumru / Paszun vs Vogt / Yashina -- W35 Monastir F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-24T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24KUMPASVOGYAS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kumru / Paszun (`KXITFWDOUBLES-26OCT24KUMPASVOGYAS-KUMPAS`) | 0.09 / 0.79 (1) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vogt / Yashina (`KXITFWDOUBLES-26OCT24KUMPASVOGYAS-VOGYAS`) | 0.06 / 0.76 (50) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Arthur Fils vs Jan-Lennard Struff -- ATP Brussels SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 19:30Z
* Current expected start: 2026-10-24 16:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 15:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T19:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105526:209950:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arthur Fils (`KXATPMATCH-26OCT24FILSTR-FIL`) | 0.81 / 0.82 (66070) | 81.5% | 85.5% | 81.7% | 81.7% [78.5%-83.0%] | 80.9% | 81.0% | 80.9% | MODEL_LONE_OUTLIER | PASS | +4.0 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Jan-Lennard Struff (`KXATPMATCH-26OCT24FILSTR-STR`) | 0.18 / 0.20 (33467) | 19.0% | 14.5% | 18.3% | 18.3% [17.0%-21.5%] | 19.1% | 18.9% | 19.0% | MODEL_LONE_OUTLIER | PASS | -4.5 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4268.0, B 4793.0; serve-point win A 71.3%, B 37.4%; Elo A 2036.2, B 1782.6; model uncertainty 0.0224
* Form inputs: days since last match A 12, B 3; matches on record A 331, B 1056; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.006, surface_dev_loose +0.012, surface_dev_tight -0.019
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT24FILSTR-FIL8` Will Arthur Fils win at least 7.5 more games than Jan-Lennard Struff?: 0.06/0.27 mid 16.5%, model 4.4% (projection_v2.0 (prediction ledger)) -- gap -12.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24FILSTR-FIL21` Will Arthur Fils win the Arthur Fils vs Jan-Lennard Struff match by a set score of 2-1?: 0.19/0.25 mid 22.0%, model 27.7% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24FILSTR-FIL5` Will Arthur Fils win at least 4.5 more games than Jan-Lennard Struff?: 0.43/0.44 mid 43.5%, model 39.0% (projection_v2.0 (prediction ledger)) -- gap -4.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24FILSTR-18` Over 17.5 games: 0.84/0.89 mid 86.5%, model 90.3% (projection_v2.0 (prediction ledger)) -- gap +3.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24FILSTR-STR20` Will Jan-Lennard Struff win the Arthur Fils vs Jan-Lennard Struff match by a set score of 2-0?: 0.07/0.11 mid 9.0%, model 5.8% (projection_v2.0 (prediction ledger)) -- gap -3.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24FILSTR-28` Over 27.5 games: 0.27/0.29 mid 28.0%, model 31.1% (projection_v2.0 (prediction ledger)) -- gap +3.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24FILSTR-FIL2` Will Arthur Fils win at least 1.5 more games than Jan-Lennard Struff?: 0.76/0.79 mid 77.5%, model 80.3% (projection_v2.0 (prediction ledger)) -- gap +2.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24FILSTR-23` Over 22.5 games: 0.47/0.49 mid 48.0%, model 49.8% (projection_v2.0 (prediction ledger)) -- gap +1.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24FILSTR-FIL20` Will Arthur Fils win the Arthur Fils vs Jan-Lennard Struff match by a set score of 2-0?: 0.57/0.62 mid 59.5%, model 57.8% (projection_v2.0 (prediction ledger)) -- gap -1.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24FILSTR-2-FIL` Will Arthur Fils win set 2 in the Arthur Fils vs Jan-Lennard Struff match: 0.73/0.77 mid 75.0%, model 76.0% (projection_v2.0 (prediction ledger)) -- gap +1.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24FILSTR-2-STR` Will Jan-Lennard Struff win set 2 in the Arthur Fils vs Jan-Lennard Struff match: 0.23/0.27 mid 25.0%, model 24.0% (projection_v2.0 (prediction ledger)) -- gap -1.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24FILSTR-STR21` Will Jan-Lennard Struff win the Arthur Fils vs Jan-Lennard Struff match by a set score of 2-1?: 0.07/0.12 mid 9.5%, model 8.8% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24FILSTR-1-STR` Will Jan-Lennard Struff win set 1 in the Arthur Fils vs Jan-Lennard Struff match: 0.23/0.26 mid 24.5%, model 24.0% (projection_v2.0 (prediction ledger)) -- gap -0.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24FILSTR-1-FIL` Will Arthur Fils win set 1 in the Arthur Fils vs Jan-Lennard Struff match: 0.76/0.77 mid 76.5%, model 76.0% (projection_v2.0 (prediction ledger)) -- gap -0.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sonja Zhenikhova vs Andrea Obradovic -- W15 Bol SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24ZHEOBR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrea Obradovic (`KXITFWMATCH-26OCT24ZHEOBR-OBR`) | 0.02 / 0.88 (1) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sonja Zhenikhova (`KXITFWMATCH-26OCT24ZHEOBR-ZHE`) | 0.34 / 0.92 (2) | 63.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Karol Drzewiecki / Piotr Matuszewski vs Tiago Pereira / Benjamin Winter Lopez -- ATP Challenger Lisbon F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-24T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24DRZMATPERWIN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karol Drzewiecki / Piotr Matuszewski (`KXATPCHALLENGERDOUBLES-26OCT24DRZMATPERWIN-DRZMAT`) | 0.43 / 0.57 (88) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tiago Pereira / Benjamin Winter Lopez (`KXATPCHALLENGERDOUBLES-26OCT24DRZMATPERWIN-PERWIN`) | 0.42 / 0.57 (88) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jodie Anna Burrage vs Hannah Klugman -- W100 Wrexham SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24BURKLU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jodie Anna Burrage (`KXITFWMATCH-26OCT24BURKLU-BUR`) | 0.47 / 0.48 (3) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hannah Klugman (`KXITFWMATCH-26OCT24BURKLU-KLU`) | 0.50 / 0.52 (138) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mia Horvit vs Tara Wuerth -- W15 Bol SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24HORWUE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mia Horvit (`KXITFWMATCH-26OCT24HORWUE-HOR`) | 0.05 / 0.45 (10) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tara Wuerth (`KXITFWMATCH-26OCT24HORWUE-WUE`) | 0.65 / 0.94 (17) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Laura Mair vs Aran Teixido Garcia -- W35 Loule SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24MAITEI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Laura Mair (`KXITFWMATCH-26OCT24MAITEI-MAI`) | 0.48 / 0.51 (21) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aran Teixido Garcia (`KXITFWMATCH-26OCT24MAITEI-TEI`) | 0.49 / 0.52 (160) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Viacheslav Bielinskyi vs Nico Hipfl -- M15 Bol SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24BIEHIP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Viacheslav Bielinskyi (`KXITFMATCH-26OCT24BIEHIP-BIE`) | 0.02 / 0.97 (100) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nico Hipfl (`KXITFMATCH-26OCT24BIEHIP-HIP`) | 0.34 / 0.97 (100) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arthur Nagel vs Maximilian Marterer -- M25 Sarreguemines SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:109739:211621:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maximilian Marterer (`KXITFMATCH-26OCT24NAGMAR-MAR`) | 0.71 / 0.73 (44) | 72.0% | 95.3% | 65.6% | 95.8% [95.3%-96.1%] | 72.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +23.4 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Arthur Nagel (`KXITFMATCH-26OCT24NAGMAR-NAG`) | 0.27 / 0.28 (7) | 27.5% | 4.7% | 34.4% | 4.2% [3.9%-4.7%] | 28.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -22.9 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 69.0, B 3762.0; serve-point win A 57.0%, B 29.5%; Elo A 1268.9, B 1833.6; model uncertainty 0.0041
* Form inputs: days since last match A 40, B 516; matches on record A 44, B 672; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT24NAGMAR-MAR  (YES = Maximilian Marterer)
Model: 95%
Kalshi: 72%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Geoffrey Blancaneaux vs Imanol Lopez Morillo -- M15 Bol SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 17:50Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T17:50:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24BLALOP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Geoffrey Blancaneaux (`KXITFMATCH-26OCT24BLALOP-BLA`) | 0.13 / 0.97 (122) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Imanol Lopez Morillo (`KXITFMATCH-26OCT24BLALOP-LOP`) | 0.02 / 0.97 (100) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bertimon / Blancaneaux vs Bielinskyi / Simundza -- M15 Bol SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-24T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24BERBLABIESIM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bertimon / Blancaneaux (`KXITFDOUBLES-26OCT24BERBLABIESIM-BERBLA`) | 0.05 / 0.95 (38) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bielinskyi / Simundza (`KXITFDOUBLES-26OCT24BERBLABIESIM-BIESIM`) | 0.05 / 0.95 (38) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Weronika Falkowska vs Federica Urgesi -- W35 Loule SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216579:223415:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Weronika Falkowska (`KXITFWMATCH-26OCT24FALURG-FAL`) | 0.48 / 0.51 (95) | 49.5% | -- | 58.4% | 54.2% [47.3%-57.4%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +4.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Federica Urgesi (`KXITFWMATCH-26OCT24FALURG-URG`) | 0.48 / 0.51 (49) | 49.5% | -- | 41.6% | 45.8% [42.6%-52.7%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2031.0, B 2635.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0501
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.011, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Suzan Lamens vs Elsa Jacquemot -- W100 Wrexham SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215480:221039:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elsa Jacquemot (`KXITFWMATCH-26OCT24LAMJAC-JAC`) | 0.47 / 0.49 (42) | 48.0% | -- | 48.9% | 46.8% [44.1%-47.9%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Suzan Lamens (`KXITFWMATCH-26OCT24LAMJAC-LAM`) | 0.50 / 0.52 (13) | 51.0% | -- | 51.1% | 53.2% [52.1%-55.9%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3938.0, B 4592.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0186
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Philip Henning vs Adrien Gobat -- M25 Sarreguemines SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202475:210254:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrien Gobat (`KXITFMATCH-26OCT24HENGOB-GOB`) | 0.35 / 0.36 (35) | 35.5% | 32.6% | 40.4% | 36.0% [35.1%-37.0%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Philip Henning (`KXITFMATCH-26OCT24HENGOB-HEN`) | 0.65 / 0.66 (276) | 65.5% | 67.4% | 59.6% | 64.0% [63.0%-64.9%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1821.0, B 307.0; serve-point win A 63.3%, B 40.2%; Elo A 1522.4, B 1417.5; model uncertainty 0.0092
* Form inputs: days since last match A 12, B 593; matches on record A 143, B 109; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mariam Bolkvadze vs Harmony Tan -- W50 Cherbourg-en-Cotentin SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211552:213734:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mariam Bolkvadze (`KXITFWMATCH-26OCT24BOLTAN-BOL`) | 0.40 / 0.41 (381) | 40.5% | -- | 27.8% | 38.4% [34.4%-45.2%] | 40.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.1 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Harmony Tan (`KXITFWMATCH-26OCT24BOLTAN-TAN`) | 0.59 / 0.61 (25) | 60.0% | -- | 72.2% | 61.6% [54.8%-65.6%] | 59.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.6 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1814.0, B 3731.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.054
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.021, surface_dev_loose -0.000, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Felipe Meligeni Alves vs Valerio Aboian -- ATP Challenger Cali SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-24T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200335:209254:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valerio Aboian (`KXATPCHALLENGERMATCH-26OCT24MELABO-ABO`) | 0.23 / 0.25 (3349) | 24.0% | 31.8% | 35.9% | 33.0% [31.2%-34.0%] | -- | 23.0% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +7.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Felipe Meligeni Alves (`KXATPCHALLENGERMATCH-26OCT24MELABO-MEL`) | 0.75 / 0.77 (3021) | 76.0% | 68.2% | 64.1% | 67.0% [66.0%-68.8%] | -- | 76.7% | -- | INSUFFICIENT_INPUTS | PASS | -7.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2750.0, B 2578.0; serve-point win A 61.8%, B 41.8%; Elo A 1678.9, B 1516.1; model uncertainty 0.0139
* Form inputs: days since last match A 12, B 12; matches on record A 511, B 298; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Christie / Silva vs Britton / Klugman -- W100 Wrexham SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-24T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24CHRSILBRIKLU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Britton / Klugman (`KXITFWDOUBLES-26OCT24CHRSILBRIKLU-BRIKLU`) | 0.06 / 0.69 (0) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Christie / Silva (`KXITFWDOUBLES-26OCT24CHRSILBRIKLU-CHRSIL`) | 0.31 / 0.62 (1) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ana Sofia Sanchez vs Barbara Gatica -- W15 Campina Grande SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-24T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:204419:211903:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barbara Gatica (`KXITFWMATCH-26OCT24SANGAT-GAT`) | 0.62 / 0.63 (35) | 62.5% | -- | 43.6% | 56.4% [53.2%-61.6%] | 60.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Ana Sofia Sanchez (`KXITFWMATCH-26OCT24SANGAT-SAN`) | 0.36 / 0.38 (19) | 37.0% | -- | 56.4% | 43.6% [38.4%-46.8%] | 39.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 3191.0, B 633.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0421
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.027, surface_pool_high -0.026, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Katarina Zavatska vs Manon Leonard -- W50 Cherbourg-en-Cotentin SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215290:215807:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Manon Leonard (`KXITFWMATCH-26OCT24ZAVLEO-LEO`) | 0.52 / 0.55 (29) | 53.5% | -- | 50.5% | 50.5% [41.5%-55.9%] | 53.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Katarina Zavatska (`KXITFWMATCH-26OCT24ZAVLEO-ZAV`) | 0.43 / 0.47 (28) | 45.0% | -- | 49.5% | 49.5% [44.1%-58.5%] | 46.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +4.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4227.0, B 3201.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0717
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.043, surface_pool_high -0.053, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maria Florencia Urrutia vs Justina Maria Gonzalez Daniele -- W15 Campina Grande SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-24T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220447:260708:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Justina Maria Gonzalez Daniele (`KXITFWMATCH-26OCT24URRGON-GON`) | 0.46 / 0.51 (55) | 48.5% | -- | 50.0% | 47.3% [43.1%-48.9%] | -- | -- | -- | -- | PASS | -1.2 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Florencia Urrutia (`KXITFWMATCH-26OCT24URRGON-URR`) | 0.48 / 0.51 (10) | 49.5% | -- | 50.0% | 52.7% [51.1%-56.9%] | -- | -- | -- | -- | PASS | +3.2 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2454.0, B 2911.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0293
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gustavo Heide vs Matheus Pucinelli de Almeida -- ATP Challenger Cali SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 20:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-24T20:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24HEIPDA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gustavo Heide (`KXATPCHALLENGERMATCH-26OCT24HEIPDA-HEI`) | 0.58 / 0.59 (2033) | 58.5% | 64.0% | -- | -- [-----] | 58.4% | 59.2% | 59.2% | MODEL_LONE_OUTLIER | -- | +5.5 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | AMBIGUOUS |
| Matheus Pucinelli de Almeida (`KXATPCHALLENGERMATCH-26OCT24HEIPDA-PDA`) | 0.41 / 0.42 (2598) | 41.5% | 36.0% | -- | -- [-----] | 41.6% | 41.2% | 41.2% | MODEL_LONE_OUTLIER | -- | -5.5 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 61.5%, B 41.2%; Elo A 1742.0, B 1598.3; model uncertainty None
* Form inputs: days since last match A 19, B 19; matches on record A 281, B 371; data quality A
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Oliver Ojakaar vs Rodrigo Fernandes -- M15 Ithaca SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210312:212075:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rodrigo Fernandes (`KXITFMATCH-26OCT24OJAFER-FER`) | 0.35 / 0.36 (86) | 35.5% | 23.3% | 24.7% | 26.3% [24.2%-27.3%] | 34.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.2 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oliver Ojakaar (`KXITFMATCH-26OCT24OJAFER-OJA`) | 0.63 / 0.65 (465) | 64.0% | 76.7% | 75.3% | 73.7% [72.7%-75.8%] | 65.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +12.7 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 188.0, B 311.0; serve-point win A 63.0%, B 42.6%; Elo A 1378.5, B 1201.1; model uncertainty 0.0157
* Form inputs: days since last match A 631, B 712; matches on record A 44, B 29; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jack Anthrop vs Rafael Ymer -- M15 Ithaca SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210294:212165:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jack Anthrop (`KXITFMATCH-26OCT24ANTYME-ANT`) | 0.86 / 0.89 (772) | 87.5% | 89.4% | 78.8% | 79.5% [79.0%-80.6%] | 87.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Rafael Ymer (`KXITFMATCH-26OCT24ANTYME-YME`) | 0.11 / 0.14 (158) | 12.5% | 10.6% | 21.2% | 20.5% [19.4%-21.0%] | 12.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 204.0, B 75.0; serve-point win A 68.8%, B 41.2%; Elo A 1417.2, B 1184.7; model uncertainty 0.0082
* Form inputs: days since last match A 404, B 740; matches on record A 59, B 7; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alan Magadan / Rodrigo Pacheco Mendez vs Federico Zeballos / Marcelo Zormann -- ATP Challenger Cali F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-24T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24MAGPACZEBZOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alan Magadan / Rodrigo Pacheco Mendez (`KXATPCHALLENGERDOUBLES-26OCT24MAGPACZEBZOR-MAGPAC`) | 0.05 / 0.95 (223) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Federico Zeballos / Marcelo Zormann (`KXATPCHALLENGERDOUBLES-26OCT24MAGPACZEBZOR-ZEBZOR`) | 0.05 / 0.95 (223) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Reese Brantmeier vs Hiromi Abe -- W75 Saguenay SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221362:222034:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hiromi Abe (`KXITFWMATCH-26OCT24BRAABE-ABE`) | 0.26 / 0.29 (64) | 27.5% | -- | 79.8% | 58.4% [56.4%-61.4%] | 26.4% | -- | 26.4% | MODEL_LONE_OUTLIER | PASS | +30.9 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Reese Brantmeier (`KXITFWMATCH-26OCT24BRAABE-BRA`) | 0.70 / 0.71 (86) | 70.5% | -- | 20.2% | 41.6% [38.6%-43.6%] | 73.6% | -- | 73.6% | MODEL_LONE_OUTLIER | PASS | -28.9 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 133.0, B 2555.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0253
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT24BRAABE-ABE  (YES = Hiromi Abe)
Model: 58%
Kalshi: 28%
Gap: +31 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Madison Brengle vs Ella McDonald -- W50 Austin F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:201483:259591:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Madison Brengle (`KXITFWMATCH-26OCT24BREMCD-BRE`) | 0.51 / 0.52 (258) | 51.5% | -- | 51.6% | 63.1% [59.6%-71.3%] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +11.7 pp | REVIEW | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ella McDonald (`KXITFWMATCH-26OCT24BREMCD-MCD`) | 0.46 / 0.49 (79) | 47.5% | -- | 48.4% | 36.9% [28.7%-40.4%] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -10.7 pp | REVIEW | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2464.0, B 1341.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0589
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.005, surface_dev_loose -0.020, surface_dev_tight +0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alevtina Ibragimova vs Polina Iatcenko -- WTA Guangzhou Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-25 05:00Z
* Current expected start: 2026-10-24 23:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-24 22:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-360_MIN

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-25T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT24IBRIAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Iatcenko (`KXWTAMATCH-26OCT24IBRIAT-IAT`) | 0.62 / 0.65 (380) | 63.5% | -- | -- | -- [-----] | -- | 62.7% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alevtina Ibragimova (`KXWTAMATCH-26OCT24IBRIAT-IBR`) | 0.35 / 0.38 (92) | 36.5% | -- | -- | -- [-----] | -- | 37.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dahlberg / Velcz vs Cox / Ojakaar -- M15 Ithaca F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-24T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24DAHVELCOXOJA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cox / Ojakaar (`KXITFDOUBLES-26OCT24DAHVELCOXOJA-COXOJA`) | 0.08 / 0.53 (53) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dahlberg / Velcz (`KXITFDOUBLES-26OCT24DAHVELCOXOJA-DAHVEL`) | 0.08 / 0.64 (69) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Sander Jong vs Darwin Blanch -- ATP Challenger Fort Worth SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-24T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24JONBLA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Darwin Blanch (`KXATPCHALLENGERMATCH-26OCT24JONBLA-BLA`) | 0.73 / 0.75 (3200) | 74.0% | -- | -- | -- [-----] | 73.1% | 74.7% | 74.7% | MARKETS_AGREE | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sander Jong (`KXATPCHALLENGERMATCH-26OCT24JONBLA-JON`) | 0.25 / 0.27 (4189) | 26.0% | -- | -- | -- [-----] | 26.9% | 26.5% | 26.5% | MARKETS_AGREE | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Ariana Arseneault vs Yuki Naito -- W75 Saguenay SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216044:220502:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ariana Arseneault (`KXITFWMATCH-26OCT24ARSNAI-ARS`) | 0.55 / 0.56 (803) | 55.5% | -- | 48.4% | 42.6% [38.4%-45.2%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.9 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuki Naito (`KXITFWMATCH-26OCT24ARSNAI-NAI`) | 0.41 / 0.44 (150) | 42.5% | -- | 51.6% | 57.4% [54.8%-61.6%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +14.9 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2049.0, B 2186.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0339
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Henrique Chabalgoity / Fontes Damorim vs Farjat / Martinez -- M15 Maceio F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 23:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-24T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24HENFONFARMAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Farjat / Martinez (`KXITFDOUBLES-26OCT24HENFONFARMAR-FARMAR`) | 0.08 / 0.62 (65) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Henrique Chabalgoity / Fontes Damorim (`KXITFDOUBLES-26OCT24HENFONFARMAR-HENFON`) | 0.08 / 0.53 (53) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Bayerlova / Gimbrere vs Brantmeier / Tanguilig -- W75 Saguenay F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-25T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24BAYGIMBRATAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bayerlova / Gimbrere (`KXITFWDOUBLES-26OCT24BAYGIMBRATAN-BAYGIM`) | 0.08 / 0.43 (43) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Brantmeier / Tanguilig (`KXITFWDOUBLES-26OCT24BAYGIMBRATAN-BRATAN`) | 0.08 / 0.73 (92) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Fairclough / Christine Lutkemeyer vs Fouad / Justine Hejtmanek -- W35 Bakersfield CA SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-25T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24FAICHRFOUJUS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fairclough / Christine Lutkemeyer (`KXITFWDOUBLES-26OCT24FAICHRFOUJUS-FAICHR`) | 0.05 / 0.95 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fouad / Justine Hejtmanek (`KXITFWDOUBLES-26OCT24FAICHRFOUJUS-FOUJUS`) | 0.05 / 0.95 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mediorreal Arias / Sofia Sanchez vs Garcia Vidal / Konishi Camargo Silva -- W15 Campina Grande F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-25T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24MEDSOFGARKON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Garcia Vidal / Konishi Camargo Silva (`KXITFWDOUBLES-26OCT24MEDSOFGARKON-GARKON`) | 0.16 / 0.40 (41) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mediorreal Arias / Sofia Sanchez (`KXITFWDOUBLES-26OCT24MEDSOFGARKON-MEDSOF`) | 0.08 / 0.75 (100) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jenson Brooksby vs Gabriel Debru -- ATP Challenger Fort Worth SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 00:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-25T00:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24BRODEB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jenson Brooksby (`KXATPCHALLENGERMATCH-26OCT24BRODEB-BRO`) | 0.82 / 0.83 (3933) | 82.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gabriel Debru (`KXATPCHALLENGERMATCH-26OCT24BRODEB-DEB`) | 0.17 / 0.18 (1952) | 17.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Joao Victor Couto Loureiro vs Kaua Lorenzo Santos Gava -- M15 Maceio SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 00:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-25T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208533:211732:2026-10-25`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joao Victor Couto Loureiro (`KXITFMATCH-26OCT24COUSAN-COU`) | 0.55 / 0.58 (34) | 56.5% | 54.9% | 38.0% | 40.9% [40.9%-40.9%] | -- | -- | -- | -- | PASS | -1.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Kaua Lorenzo Santos Gava (`KXITFMATCH-26OCT24COUSAN-SAN`) | 0.40 / 0.44 (80) | 42.0% | 45.1% | 62.0% | 59.1% [59.1%-59.1%] | -- | -- | -- | -- | PASS | +3.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 509.0, B 49.0; serve-point win A 62.4%, B 38.6%; Elo A 1147.4, B 1211.3; model uncertainty 0.0002
* Form inputs: days since last match A 698, B 761; matches on record A 92, B 5; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aliaksandra Sasnovich vs Kamilla Rakhimova -- WTA Tokyo Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-25 04:00Z
* Current expected start: 2026-10-25 01:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-25 00:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-150_MIN

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-25T04:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT24SASRAK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kamilla Rakhimova (`KXWTAMATCH-26OCT24SASRAK-RAK`) | 0.43 / 0.46 (342) | 44.5% | -- | -- | -- [-----] | -- | 44.5% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aliaksandra Sasnovich (`KXWTAMATCH-26OCT24SASRAK-SAS`) | 0.54 / 0.57 (512) | 55.5% | -- | -- | -- [-----] | -- | 55.0% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Heather Watson vs Alycia Parks -- WTA Tokyo Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-25 04:00Z
* Current expected start: 2026-10-25 01:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-25 00:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-150_MIN

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-25T04:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT24WATPAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alycia Parks (`KXWTAMATCH-26OCT24WATPAR-PAR`) | 0.53 / 0.55 (76) | 54.0% | -- | -- | -- [-----] | -- | 50.5% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Heather Watson (`KXWTAMATCH-26OCT24WATPAR-WAT`) | 0.45 / 0.47 (357) | 46.0% | -- | -- | -- [-----] | -- | 49.3% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH

## Lorenzo Gagliardo vs Pedro Sakamoto -- M15 Maceio SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-25T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106203:207682:2026-10-25`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Gagliardo (`KXITFMATCH-26OCT24GAGSAK-GAG`) | 0.33 / 0.38 (38) | 35.5% | 22.5% | 54.6% | 18.9% [15.4%-22.5%] | -- | -- | -- | -- | PASS | -13.0 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Pedro Sakamoto (`KXITFMATCH-26OCT24GAGSAK-SAK`) | 0.61 / 0.64 (152) | 62.5% | 77.5% | 45.4% | 81.2% [77.5%-84.6%] | -- | -- | -- | -- | PASS | +15.0 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 202.0, B 1912.0; serve-point win A 58.1%, B 36.0%; Elo A 1266.3, B 1566.6; model uncertainty 0.0354
* Form inputs: days since last match A 768, B 26; matches on record A 77, B 670; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT24GAGSAK-SAK  (YES = Pedro Sakamoto)
Model: 78%
Kalshi: 62%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hanna Chang vs Connie Ma -- W35 Bakersfield CA SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-25T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24CHAMAX:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hanna Chang (`KXITFWMATCH-26OCT24CHAMAX-CHA`) | 0.15 / 0.22 (32) | 18.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Connie Ma (`KXITFWMATCH-26OCT24CHAMAX-MAX`) | 0.77 / 0.83 (130) | 80.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lan Mi vs Jenna DeFalco -- W35 Bakersfield CA SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-25T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24MIXDEF:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jenna DeFalco (`KXITFWMATCH-26OCT24MIXDEF-DEF`) | 0.51 / 0.54 (32) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lan Mi (`KXITFWMATCH-26OCT24MIXDEF-MIX`) | 0.44 / 0.49 (78) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ashlyn Krueger vs Katerina Siniakova -- WTA Osaka F

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-25 07:30Z
* Current expected start: 2026-10-25 04:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-25 03:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-25T07:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT25KRUSIN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ashlyn Krueger (`KXWTAMATCH-26OCT25KRUSIN-KRU`) | 0.10 / 0.92 (12) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Katerina Siniakova (`KXWTAMATCH-26OCT25KRUSIN-SIN`) | 0.09 / 0.92 (12) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Blake Ellis vs Isaac Becroft -- M25 Tamworth F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-25T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24ELLBEC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isaac Becroft (`KXITFMATCH-26OCT24ELLBEC-BEC`) | 0.05 / 0.95 (3) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Blake Ellis (`KXITFMATCH-26OCT24ELLBEC-ELL`) | 0.04 / 0.96 (3) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hikaru Sato vs I Wen Wan -- W35 Sydney F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-25T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24SATWAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hikaru Sato (`KXITFWMATCH-26OCT24SATWAN-SAT`) | 0.61 / 0.63 (2) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| I Wen Wan (`KXITFWMATCH-26OCT24SATWAN-WAN`) | 0.37 / 0.38 (17) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cristina Bucsa / Nicole Melichar-Martinez vs Desirae Krawczyk / Fanny Stollar -- WTA Ningbo F

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-25 09:30Z
* Current expected start: 2026-10-25 06:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: 2026-10-25 05:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-25T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT25BUCMELKRASTO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cristina Bucsa / Nicole Melichar-Martinez (`KXWTADOUBLES-26OCT25BUCMELKRASTO-BUCMEL`) | 0.05 / 0.95 (100) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Desirae Krawczyk / Fanny Stollar (`KXWTADOUBLES-26OCT25BUCMELKRASTO-KRASTO`) | 0.05 / 0.95 (100) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Becroft / Shepp vs Talic / Vickery -- M25 Tamworth SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-25T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24BECSHETALVIC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Becroft / Shepp (`KXITFDOUBLES-26OCT24BECSHETALVIC-BECSHE`) | 0.05 / 0.92 (30) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Talic / Vickery (`KXITFDOUBLES-26OCT24BECSHETALVIC-TALVIC`) | 0.05 / 0.95 (38) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Hugo Hashimoto vs Yuto Oki -- M15 Tanagura F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-25T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24HASOKI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Hashimoto (`KXITFMATCH-26OCT24HASOKI-HAS`) | 0.50 / 0.55 (141) | 52.5% | -- | -- | -- [-----] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yuto Oki (`KXITFMATCH-26OCT24HASOKI-OKI`) | 0.40 / 0.49 (3) | 44.5% | -- | -- | -- [-----] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luca Staeheli vs Mikalai Haliak -- M15 Shenzhen F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-25T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24STAHAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mikalai Haliak (`KXITFMATCH-26OCT24STAHAL-HAL`) | 0.20 / 0.34 (8) | 27.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luca Staeheli (`KXITFMATCH-26OCT24STAHAL-STA`) | 0.65 / 0.70 (67) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daria KHOMUTSIANSKAYA vs Xinxin Yao -- W35 Qian Daohu F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-25T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24KHOYAO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daria KHOMUTSIANSKAYA (`KXITFWMATCH-26OCT24KHOYAO-KHO`) | 0.52 / 0.57 (64) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xinxin Yao (`KXITFWMATCH-26OCT24KHOYAO-YAO`) | 0.33 / 0.47 (47) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lucas Miedler / Neil Oberleitner vs Yuki Bhambri / Ryan Seggerman -- ATP Almaty F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-24 10:07Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-25T04:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-25T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT25MIEOBEBHASEG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuki Bhambri / Ryan Seggerman (`KXATPDOUBLES-26OCT25MIEOBEBHASEG-BHASEG`) | 0.05 / 0.95 (156) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lucas Miedler / Neil Oberleitner (`KXATPDOUBLES-26OCT25MIEOBEBHASEG-MIEOBE`) | 0.05 / 0.95 (156) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
