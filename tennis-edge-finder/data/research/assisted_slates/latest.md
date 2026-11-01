# ASSISTED SLATE -- 2026-11-01T03:07Z (`SL-20261101T030746Z-6cdca989`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

181 open matches not seen started, 766 markets. Skipped: {"scheduled_start_over_24h_past": 1, "first_ball_already_observed": 3}. Sources: shadow board 2026-10-31T22:30:43.472890+00:00, Model 4 2026-10-31T22:31:07.388008+00:00, Gen-1 ledger 2026-10-31T22:30:38.359793+00:00, external 2026-11-01T02:44:27.700024+00:00, capture 20261101T024205Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-11-01 03:14Z**
* Recommended RUN TENNIS time: **2026-11-01 02:29Z**  (**OVERDUE -- run now**)
* Final price/status check time: **2026-11-01 03:04Z**
* Number of matches in window: 2 (Emerson Jones vs Alexandra Shubladze, Himeno Sakatsume vs Elena Pridankina)

* **30 main-tour match(es) have NO verified start status** (START_UNKNOWN): BET blocked until a live status check.

Slate built 2026-11-01T03:07Z. Refresh due by: 2026-11-01 02:29Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 15, "HIGH_REVIEW": 42, "NORMAL": 406, "REVIEW": 89, "UNPRICED": 214}; match winners: {"EXTREME": 13, "HIGH_REVIEW": 21, "NORMAL": 155, "REVIEW": 19, "UNPRICED": 154}; quote freshness at build: {"FRESH": 552}.

## Emerson Jones vs Alexandra Shubladze -- WTA Hong Kong Q3

**START STATUS: START_IMMINENT** -- BET BLOCKED
* Nominal schedule: 2026-11-01 06:10Z
* Current expected start: 2026-11-01 03:14Z
* Source: COURT_PROGRESSION: preceding match on Court 2 in progress (set 1 of best-of-3); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: 2026-11-01 02:29Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-176_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-11-01T06:10:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:260168:263644:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emerson Jones (`KXWTAMATCH-26OCT31JONSHU-JON`) | 0.40 / 0.41 (1752) | 40.5% | 49.0% | 29.2% | 37.5% [33.5%-46.3%] | -- | 45.5% | 45.5% | MODEL_LONE_OUTLIER | PASS | +8.5 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Alexandra Shubladze (`KXWTAMATCH-26OCT31JONSHU-SHU`) | 0.59 / 0.60 (1121) | 59.5% | 51.0% | 70.8% | 62.5% [53.7%-66.5%] | -- | 54.4% | 54.4% | MODEL_LONE_OUTLIER | WATCH | -8.5 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 3547.0, B 3247.0; serve-point win A 54.5%, B 45.3%; Elo A 1797.8, B 1752.8; model uncertainty 0.0641
* Form inputs: days since last match A 0, B 0; matches on record A 154, B 208; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose -0.010, surface_dev_tight +0.005
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT31JONSHU-1-JON` Will Emerson Jones win set 1 in the Emerson Jones vs Alexandra Shubladze match: 0.42/0.45 mid 43.5%, model 49.4% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT31JONSHU-2-JON` Will Emerson Jones win set 2 in the Emerson Jones vs Alexandra Shubladze match: 0.41/0.46 mid 43.5%, model 49.4% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT31JONSHU-1-SHU` Will Alexandra Shubladze win set 1 in the Emerson Jones vs Alexandra Shubladze match: 0.55/0.57 mid 56.0%, model 50.6% (projection_v2.0 (prediction ledger)) -- gap -5.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT31JONSHU-2-SHU` Will Alexandra Shubladze win set 2 in the Emerson Jones vs Alexandra Shubladze match: 0.54/0.57 mid 55.5%, model 50.6% (projection_v2.0 (prediction ledger)) -- gap -4.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE

## Himeno Sakatsume vs Elena Pridankina -- WTA Hong Kong Q3

**START STATUS: START_IMMINENT** -- BET BLOCKED
* Nominal schedule: 2026-11-01 06:10Z
* Current expected start: 2026-11-01 03:14Z
* Source: COURT_PROGRESSION: preceding match on Court 1 in progress (set 1 of best-of-3); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: 2026-11-01 02:29Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-176_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-11-01T06:10:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:221124:239389:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elena Pridankina (`KXWTAMATCH-26OCT31SAKPRI-PRI`) | 0.50 / 0.51 (5130) | 50.5% | 48.7% | 36.0% | 38.6% [35.5%-46.3%] | -- | 50.2% | -- | INSUFFICIENT_INPUTS | PASS | -1.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Himeno Sakatsume (`KXWTAMATCH-26OCT31SAKPRI-SAK`) | 0.50 / 0.51 (4231) | 50.5% | 51.3% | 64.0% | 61.5% [53.7%-64.5%] | -- | 49.5% | -- | INSUFFICIENT_INPUTS | PASS | +0.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3693.0, B 3685.0; serve-point win A 56.5%, B 43.8%; Elo A 1761.4, B 1724.5; model uncertainty 0.0538
* Form inputs: days since last match A 0, B 0; matches on record A 419, B 290; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.020, surface_dev_loose -0.005, surface_dev_tight +0.010
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT31SAKPRI-1-PRI` Will Elena Pridankina win set 1 in the Himeno Sakatsume vs Elena Pridankina match: 0.49/0.52 mid 50.5%, model 49.1% (projection_v2.0 (prediction ledger)) -- gap -1.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT31SAKPRI-1-SAK` Will Himeno Sakatsume win set 1 in the Himeno Sakatsume vs Elena Pridankina match: 0.48/0.51 mid 49.5%, model 50.9% (projection_v2.0 (prediction ledger)) -- gap +1.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT31SAKPRI-2-SAK` Will Himeno Sakatsume win set 2 in the Himeno Sakatsume vs Elena Pridankina match: 0.47/0.52 mid 49.5%, model 50.9% (projection_v2.0 (prediction ledger)) -- gap +1.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT31SAKPRI-2-PRI` Will Elena Pridankina win set 2 in the Himeno Sakatsume vs Elena Pridankina match: 0.47/0.50 mid 48.5%, model 49.1% (projection_v2.0 (prediction ledger)) -- gap +0.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS

## Gabriela Dabrowski / Luisa Stefani vs Sara Errani / Jasmine Paolini -- WTA Tokyo F

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-01 07:10Z
* Current expected start: 2026-11-01 04:50Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: 2026-11-01 04:05Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-01T07:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV01DABSTEERRPAO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriela Dabrowski / Luisa Stefani (`KXWTADOUBLES-26NOV01DABSTEERRPAO-DABSTE`) | 0.71 / 0.72 (333) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sara Errani / Jasmine Paolini (`KXWTADOUBLES-26NOV01DABSTEERRPAO-ERRPAO`) | 0.28 / 0.30 (3) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Yanki Erel vs Yan Cheng Chen -- ATP Challenger Taipei Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-01T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207129:212460:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yan Cheng Chen (`KXATPCHALLENGERMATCH-26OCT31ERECHE-CHE`) | 0.07 / 0.08 (10849) | 7.5% | 4.2% | 1.7% | 5.2% [3.3%-7.0%] | -- | 6.1% | -- | INSUFFICIENT_INPUTS | PASS | -3.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yanki Erel (`KXATPCHALLENGERMATCH-26OCT31ERECHE-ERE`) | 0.92 / 0.93 (7300) | 92.5% | 95.8% | 98.3% | 94.8% [93.0%-96.7%] | -- | 93.7% | -- | INSUFFICIENT_INPUTS | PASS | +3.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3713.0, B 550.0; serve-point win A 67.5%, B 46.0%; Elo A 1603.6, B 1164.0; model uncertainty 0.0187
* Form inputs: days since last match A 32, B 201; matches on record A 396, B 19; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.003, surface_dev_loose +0.006, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY

## Masamichi Imamura vs Luca Staeheli -- ATP Challenger Taipei Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-01T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:201987:207664:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Masamichi Imamura (`KXATPCHALLENGERMATCH-26OCT31IMASTA-IMA`) | 0.87 / 0.88 (43954) | 87.5% | 59.7% | 51.0% | 56.3% [54.2%-58.4%] | 39.1% | -- | 39.1% | MODEL_LONE_OUTLIER | SHADOW_BET | -27.8 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Luca Staeheli (`KXATPCHALLENGERMATCH-26OCT31IMASTA-STA`) | 0.12 / 0.13 (45717) | 12.5% | 40.3% | 48.9% | 43.7% [41.6%-45.8%] | 60.9% | -- | 60.9% | MODEL_LONE_OUTLIER | PASS | +27.8 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 3332.0, B 2411.0; serve-point win A 57.8%, B 44.1%; Elo A 1476.6, B 1379.1; model uncertainty 0.0208
* Form inputs: days since last match A 32, B 33; matches on record A 250, B 123; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT31IMASTA-STA  (YES = Luca Staeheli)
Model: 40%
Kalshi: 12%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: SUPPORTS_MODEL_DIRECTION
Data quality: A (ADEQUATE)
Reasons: EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## I-Hsuan Cho / Yi Tsen Cho vs Polina Kudermetova / Maria Timofeeva -- WTA Guangzhou F

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-01 11:30Z
* Current expected start: 2026-11-01 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: 2026-11-01 05:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-01T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV01CHOCHOKUDTIM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I-Hsuan Cho / Yi Tsen Cho (`KXWTADOUBLES-26NOV01CHOCHOKUDTIM-CHOCHO`) | 0.57 / 0.59 (188) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Polina Kudermetova / Maria Timofeeva (`KXWTADOUBLES-26NOV01CHOCHOKUDTIM-KUDTIM`) | 0.40 / 0.41 (124) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Leylah Fernandez vs Diana Shnaider -- WTA Tokyo F

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-01 06:00Z
* Current expected start: 2026-11-01 06:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 07:46Z
* Recommended handicap-by time: 2026-11-01 05:15Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-01T04:00:00+00:00 as not a valid time; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-11-01T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:220367:223670:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leylah Fernandez (`KXWTAMATCH-26OCT31FERSHN-FER`) | 0.39 / 0.40 (4913) | 39.5% | 47.0% | 52.1% | 51.0% [45.3%-53.1%] | -- | 38.5% | 38.5% | MODEL_LONE_OUTLIER | SHADOW_BET | +7.5 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Diana Shnaider (`KXWTAMATCH-26OCT31FERSHN-SHN`) | 0.60 / 0.61 (4864) | 60.5% | 53.0% | 47.9% | 49.0% [46.9%-54.7%] | -- | 61.6% | 61.6% | MODEL_LONE_OUTLIER | PASS | -7.5 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4828.0, B 4846.0; serve-point win A 59.2%, B 40.2%; Elo A 1987.0, B 1986.3; model uncertainty 0.0389
* Form inputs: days since last match A 0, B 0; matches on record A 408, B 327; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.021, surface_dev_loose +0.005, surface_dev_tight +0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT31FERSHN-21` Over 20.5 games: 0.58/0.59 mid 58.5%, model 70.0% (projection_v2.0 (prediction ledger)) -- gap +11.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT31FERSHN-26` Over 25.5 games: 0.33/0.44 mid 38.5%, model 46.5% (projection_v2.0 (prediction ledger)) -- gap +8.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT31FERSHN-2-FER` Will Leylah Annie Fernandez win set 2 in the Leylah Annie Fernandez vs Diana Shnaider match: 0.41/0.43 mid 42.0%, model 48.0% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT31FERSHN-16` Over 15.5 games: 0.91/0.94 mid 92.5%, model 98.1% (projection_v2.0 (prediction ledger)) -- gap +5.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT31FERSHN-2-SHN` Will Diana Shnaider win set 2 in the Leylah Annie Fernandez vs Diana Shnaider match: 0.57/0.58 mid 57.5%, model 52.0% (projection_v2.0 (prediction ledger)) -- gap -5.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT31FERSHN-1-FER` Will Leylah Annie Fernandez win set 1 in the Leylah Annie Fernandez vs Diana Shnaider match: 0.42/0.45 mid 43.5%, model 48.0% (projection_v2.0 (prediction ledger)) -- gap +4.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT31FERSHN-1-SHN` Will Diana Shnaider win set 1 in the Leylah Annie Fernandez vs Diana Shnaider match: 0.55/0.57 mid 56.0%, model 52.0% (projection_v2.0 (prediction ledger)) -- gap -4.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Frazier Rengifo vs Rodrigo Alujas -- M15 Mazatlan F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-01T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT31RENALU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rodrigo Alujas (`KXITFMATCH-26OCT31RENALU-ALU`) | 0.46 / 0.47 (6303) | 46.5% | 61.5% | -- | -- [-----] | -- | -- | -- | -- | -- | +15.0 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Frazier Rengifo (`KXITFMATCH-26OCT31RENALU-REN`) | 0.53 / 0.54 (5609) | 53.5% | 38.5% | -- | -- [-----] | -- | -- | -- | -- | -- | -15.0 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 55.4%, B 42.3%; Elo A 1234.6, B 1295.7; model uncertainty None
* Form inputs: days since last match A 187, B 194; matches on record A 29, B 83; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT31RENALU-ALU  (YES = Rodrigo Alujas)
Model: 62%
Kalshi: 46%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Finn Reynolds / James Watt vs Blake Bayldon / Thomas Fancutt -- ATP Challenger Seoul F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-01T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT31REYWATBAYFAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Blake Bayldon / Thomas Fancutt (`KXATPCHALLENGERDOUBLES-26OCT31REYWATBAYFAN-BAYFAN`) | 0.19 / 0.39 (100) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Finn Reynolds / James Watt (`KXATPCHALLENGERDOUBLES-26OCT31REYWATBAYFAN-REYWAT`) | 0.56 / 0.80 (10) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Dimitris Sakellaridis vs Yuta Shimizu -- ATP Challenger Taipei Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 06:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-01T06:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202122:212029:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dimitris Sakellaridis (`KXATPCHALLENGERMATCH-26OCT31SAKSHI-SAK`) | 0.25 / 0.26 (4188) | 25.5% | 18.3% | 28.2% | 23.6% [20.9%-25.2%] | -- | 23.3% | -- | INSUFFICIENT_INPUTS | PASS | -7.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuta Shimizu (`KXATPCHALLENGERMATCH-26OCT31SAKSHI-SHI`) | 0.75 / 0.76 (258) | 75.5% | 81.7% | 71.8% | 76.4% [74.8%-79.1%] | -- | 74.7% | -- | INSUFFICIENT_INPUTS | WATCH | +6.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3291.0, B 4178.0; serve-point win A 54.6%, B 38.4%; Elo A 1289.8, B 1587.1; model uncertainty 0.0214
* Form inputs: days since last match A 12, B 32; matches on record A 144, B 468; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose -0.008, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Akira Santillan vs Evan Zhu -- ATP Challenger Taipei Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 06:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-01T06:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:117361:200632:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Akira Santillan (`KXATPCHALLENGERMATCH-26OCT31SANZHU-SAN`) | 0.60 / 0.61 (3935) | 60.5% | 76.9% | 80.1% | 79.1% [76.8%-80.1%] | -- | 60.6% | 60.6% | MODEL_LONE_OUTLIER | WATCH | +16.4 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Evan Zhu (`KXATPCHALLENGERMATCH-26OCT31SANZHU-ZHU`) | 0.38 / 0.40 (2573) | 39.0% | 23.1% | 19.9% | 20.9% [19.9%-23.2%] | -- | 39.2% | 39.2% | MODEL_LONE_OUTLIER | PASS | -15.9 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3641.0, B 3487.0; serve-point win A 65.5%, B 40.3%; Elo A 1536.0, B 1340.7; model uncertainty 0.0165
* Form inputs: days since last match A 12, B 32; matches on record A 596, B 418; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT31SANZHU-SAN  (YES = Akira Santillan)
Model: 77%
Kalshi: 60%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Yiming Dang vs Valeria Savinykh -- W100 Incheon R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:202443:222330:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yiming Dang (`KXITFWMATCH-26OCT31DANSAV-DAN`) | 0.27 / 0.29 (46) | 28.0% | 18.4% | 36.9% | 22.3% [17.5%-26.1%] | -- | -- | -- | -- | PASS | -9.6 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valeria Savinykh (`KXITFWMATCH-26OCT31DANSAV-SAV`) | 0.67 / 0.70 (101) | 68.5% | 81.6% | 63.1% | 77.7% [73.9%-82.5%] | -- | -- | -- | -- | PASS | +13.1 pp | REVIEW | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1108.0, B 1181.0; serve-point win A 50.8%, B 42.5%; Elo A 1291.9, B 1611.5; model uncertainty 0.0428
* Form inputs: days since last match A 33, B 32; matches on record A 90, B 735; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.008, surface_dev_loose -0.008, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ye Ryeong Jo vs Meiqi Guo -- W100 Incheon R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-01T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT31JOXGUO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Meiqi Guo (`KXITFWMATCH-26OCT31JOXGUO-GUO`) | 0.89 / 0.93 (3) | 91.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ye Ryeong Jo (`KXITFWMATCH-26OCT31JOXGUO-JOX`) | 0.06 / 0.13 (20) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dain Lee vs Anchisa Chanta -- W100 Incheon R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-01T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT31LEECHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anchisa Chanta (`KXITFWMATCH-26OCT31LEECHA-CHA`) | 0.90 / 0.93 (5) | 91.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dain Lee (`KXITFWMATCH-26OCT31LEECHA-LEE`) | 0.07 / 0.10 (209) | 8.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Christian Langmo vs Khumoyun Sultanov -- ATP Challenger Taipei Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 07:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T07:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01LANSUL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Christian Langmo (`KXATPCHALLENGERMATCH-26NOV01LANSUL-LAN`) | 0.34 / 0.35 (146) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Khumoyun Sultanov (`KXATPCHALLENGERMATCH-26NOV01LANSUL-SUL`) | 0.64 / 0.65 (2150) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Yosuke Watanuki vs Dominik Palan -- ATP Challenger Taipei Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 07:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-01T07:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:133297:208158:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dominik Palan (`KXATPCHALLENGERMATCH-26NOV01WATPAL-PAL`) | 0.10 / 0.11 (3125) | 10.5% | 17.1% | 36.6% | 27.9% [23.9%-31.2%] | -- | 10.9% | 10.9% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.6 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Yosuke Watanuki (`KXATPCHALLENGERMATCH-26NOV01WATPAL-WAT`) | 0.90 / 0.91 (5921) | 90.5% | 82.9% | 63.4% | 72.1% [68.8%-76.1%] | -- | 88.8% | -- | INSUFFICIENT_INPUTS | PASS | -7.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3158.0, B 3127.0; serve-point win A 69.8%, B 38.0%; Elo A 1682.9, B 1364.3; model uncertainty 0.0366
* Form inputs: days since last match A 19, B 12; matches on record A 449, B 348; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Terence Atmane vs Coleman Wong -- ATP Challenger Seoul F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-01T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209279:209409:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Terence Atmane (`KXATPCHALLENGERMATCH-26NOV01ATMWON-ATM`) | 0.51 / 0.52 (1349) | 51.5% | 52.2% | 43.4% | 46.7% [44.8%-50.5%] | -- | 52.1% | 52.1% | MARKETS_AGREE | PASS | +0.7 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Coleman Wong (`KXATPCHALLENGERMATCH-26NOV01ATMWON-WON`) | 0.48 / 0.49 (3714) | 48.5% | 47.8% | 56.6% | 53.3% [49.5%-55.2%] | -- | 48.1% | 48.1% | MARKETS_AGREE | WATCH | -0.7 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5304.0, B 5943.0; serve-point win A 69.2%, B 31.3%; Elo A 1805.6, B 1745.2; model uncertainty 0.0281
* Form inputs: days since last match A 8, B 12; matches on record A 437, B 336; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose +0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Yu Jun Lin vs Wushuang Zheng -- W35 Kunshan F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213821:268787:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yu Jun Lin (`KXITFWMATCH-26OCT31LINZHE-LIN`) | 0.80 / 0.81 (26549) | 80.5% | 23.7% | 63.6% | 32.5% [23.5%-40.5%] | 40.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -56.8 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Wushuang Zheng (`KXITFWMATCH-26OCT31LINZHE-ZHE`) | 0.20 / 0.21 (25023) | 20.5% | 76.3% | 36.4% | 67.5% [59.5%-76.5%] | 59.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +55.8 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 515.0, B 2161.0; serve-point win A 51.9%, B 42.7%; Elo A 1346.6, B 1552.0; model uncertainty 0.0849
* Form inputs: days since last match A 14, B 25; matches on record A 14, B 302; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT31LINZHE-ZHE  (YES = Wushuang Zheng)
Model: 76%
Kalshi: 20%
Gap: +56 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.024, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aliona Falei vs Rada Zolotareva -- WTA Chennai Q3

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-01 11:30Z (day placeholder, not a start time)
* Current expected start: 2026-11-01 08:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: 2026-11-01 07:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-11-01T11:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:221434:260951:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aliona Falei (`KXWTAMATCH-26NOV01FALZOL-FAL`) | 0.65 / 0.66 (17) | 65.5% | 68.8% | 78.0% | 75.5% [70.2%-77.6%] | -- | 65.0% | 65.0% | MODEL_LONE_OUTLIER | PASS | +3.3 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Rada Zolotareva (`KXWTAMATCH-26NOV01FALZOL-ZOL`) | 0.33 / 0.34 (196) | 33.5% | 31.2% | 22.0% | 24.4% [22.4%-29.8%] | -- | 35.4% | 35.4% | MODEL_LONE_OUTLIER | PASS | -2.3 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3528.0, B 1811.0; serve-point win A 56.8%, B 46.8%; Elo A 1746.9, B 1584.1; model uncertainty 0.0366
* Form inputs: days since last match A 0, B 0; matches on record A 289, B 97; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.017, surface_pool_high +0.008, surface_dev_loose +0.020, surface_dev_tight -0.026
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26NOV01FALZOL-2-FAL` Will Aliona Falei win set 2 in the Aliona Falei vs Rada Zolotareva match: 0.02/0.98 mid 50.0%, model 62.8% (projection_v2.0 (prediction ledger)) -- gap +12.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01FALZOL-2-ZOL` Will Rada Zolotareva win set 2 in the Aliona Falei vs Rada Zolotareva match: 0.02/0.98 mid 50.0%, model 37.2% (projection_v2.0 (prediction ledger)) -- gap -12.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01FALZOL-1-FAL` Will Aliona Falei win set 1 in the Aliona Falei vs Rada Zolotareva match: 0.61/0.64 mid 62.5%, model 62.8% (projection_v2.0 (prediction ledger)) -- gap +0.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01FALZOL-1-ZOL` Will Rada Zolotareva win set 1 in the Aliona Falei vs Rada Zolotareva match: 0.36/0.38 mid 37.0%, model 37.2% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; WIDE_SPREAD

## Viktoria Morvayova vs Weronika Falkowska -- WTA Chennai Q3

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-01 11:30Z (day placeholder, not a start time)
* Current expected start: 2026-11-01 08:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: 2026-11-01 07:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-11-01T11:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215077:216579:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Weronika Falkowska (`KXWTAMATCH-26NOV01MORFAL-FAL`) | 0.52 / 0.53 (637) | 52.5% | 53.7% | 53.1% | 53.6% [51.0%-55.2%] | -- | 53.0% | 53.0% | MODEL_LONE_OUTLIER | PASS | +1.2 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Viktoria Morvayova (`KXWTAMATCH-26NOV01MORFAL-MOR`) | 0.47 / 0.48 (708) | 47.5% | 46.3% | 46.9% | 46.4% [44.8%-48.9%] | -- | 47.9% | 47.9% | MODEL_LONE_OUTLIER | PASS | -1.2 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3267.0, B 2031.0; serve-point win A 58.1%, B 41.2%; Elo A 1556.2, B 1576.2; model uncertainty 0.0207
* Form inputs: days since last match A 18, B 26; matches on record A 465, B 372; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose -0.015, surface_dev_tight +0.021
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26NOV01MORFAL-2-FAL` Will Weronika Falkowska win set 2 in the Viktoria Morvayova vs Weronika Falkowska match: 0.02/0.98 mid 50.0%, model 52.5% (projection_v2.0 (prediction ledger)) -- gap +2.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01MORFAL-2-MOR` Will Viktoria Morvayova win set 2 in the Viktoria Morvayova vs Weronika Falkowska match: 0.02/0.98 mid 50.0%, model 47.5% (projection_v2.0 (prediction ledger)) -- gap -2.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01MORFAL-1-FAL` Will Weronika Falkowska win set 1 in the Viktoria Morvayova vs Weronika Falkowska match: 0.51/0.54 mid 52.5%, model 52.5% (projection_v2.0 (prediction ledger)) -- gap -0.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01MORFAL-1-MOR` Will Viktoria Morvayova win set 1 in the Viktoria Morvayova vs Weronika Falkowska match: 0.46/0.49 mid 47.5%, model 47.5% (projection_v2.0 (prediction ledger)) -- gap +0.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; WIDE_SPREAD

## Kyoka Okamura vs Momoko Kobori -- WTA Chennai Q3

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-01 11:30Z (day placeholder, not a start time)
* Current expected start: 2026-11-01 08:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: 2026-11-01 07:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-11-01T11:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211846:215468:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Momoko Kobori (`KXWTAMATCH-26NOV01OKAKOB-KOB`) | 0.32 / 0.33 (608) | 32.5% | 40.0% | 63.4% | 50.5% [41.6%-56.3%] | -- | 32.7% | -- | INSUFFICIENT_INPUTS | WATCH | +7.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kyoka Okamura (`KXWTAMATCH-26NOV01OKAKOB-OKA`) | 0.66 / 0.67 (76) | 66.5% | 60.0% | 36.6% | 49.5% [43.7%-58.4%] | -- | 68.4% | -- | INSUFFICIENT_INPUTS | PASS | -6.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2971.0, B 1427.0; serve-point win A 57.6%, B 44.3%; Elo A 1648.8, B 1569.0; model uncertainty 0.0734
* Form inputs: days since last match A 0, B 14; matches on record A 629, B 372; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.011, surface_dev_tight +0.005
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26NOV01OKAKOB-2-KOB` Will Momoko Kobori win set 2 in the Kyoka Okamura vs Momoko Kobori match: 0.02/0.98 mid 50.0%, model 43.3% (projection_v2.0 (prediction ledger)) -- gap -6.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01OKAKOB-2-OKA` Will Kyoka Okamura win set 2 in the Kyoka Okamura vs Momoko Kobori match: 0.02/0.98 mid 50.0%, model 56.7% (projection_v2.0 (prediction ledger)) -- gap +6.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01OKAKOB-1-KOB` Will Momoko Kobori win set 1 in the Kyoka Okamura vs Momoko Kobori match: 0.36/0.38 mid 37.0%, model 43.3% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01OKAKOB-1-OKA` Will Kyoka Okamura win set 1 in the Kyoka Okamura vs Momoko Kobori match: 0.61/0.64 mid 62.5%, model 56.7% (projection_v2.0 (prediction ledger)) -- gap -5.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; WIDE_SPREAD

## Lilli Tagger vs Harriet Dart -- WTA Guangzhou F

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-01 11:30Z (day placeholder, not a start time)
* Current expected start: 2026-11-01 08:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: 2026-11-01 07:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-11-01T11:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211279:260172:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Harriet Dart (`KXWTAMATCH-26NOV01TAGDAR-DAR`) | 0.22 / 0.23 (14686) | 22.5% | 39.5% | 51.6% | 50.0% [48.4%-52.1%] | -- | 23.3% | 23.3% | MODEL_LONE_OUTLIER | WATCH | +17.0 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Lilli Tagger (`KXWTAMATCH-26NOV01TAGDAR-TAG`) | 0.77 / 0.78 (70976) | 77.5% | 60.5% | 48.4% | 50.0% [47.9%-51.6%] | -- | 76.7% | 76.7% | MODEL_LONE_OUTLIER | PASS | -17.0 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2552.0, B 4244.0; serve-point win A 58.4%, B 43.6%; Elo A 1820.0, B 1804.9; model uncertainty 0.0184
* Form inputs: days since last match A 2, B 0; matches on record A 134, B 682; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26NOV01TAGDAR-DAR  (YES = Harriet Dart)
Model: 40%
Kalshi: 22%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: EXTERNAL_MARKET_REJECTION, UNKNOWN
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.011, surface_dev_loose -0.016, surface_dev_tight +0.011
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV01TAGDAR-21` Over 20.5 games: 0.48/0.50 mid 49.0%, model 67.5% (projection_v2.0 (prediction ledger)) -- gap +18.5 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV01TAGDAR-2-DAR` Will Harriet Dart win set 2 in the Lilli Tagger vs Harriet Dart match: 0.26/0.29 mid 27.5%, model 43.0% (projection_v2.0 (prediction ledger)) -- gap +15.5 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01TAGDAR-2-TAG` Will Lilli Tagger win set 2 in the Lilli Tagger vs Harriet Dart match: 0.69/0.73 mid 71.0%, model 57.0% (projection_v2.0 (prediction ledger)) -- gap -14.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01TAGDAR-1-DAR` Will Harriet Dart win set 1 in the Lilli Tagger vs Harriet Dart match: 0.28/0.31 mid 29.5%, model 43.0% (projection_v2.0 (prediction ledger)) -- gap +13.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26NOV01TAGDAR-26` Over 25.5 games: 0.26/0.36 mid 31.0%, model 44.3% (projection_v2.0 (prediction ledger)) -- gap +13.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV01TAGDAR-1-TAG` Will Lilli Tagger win set 1 in the Lilli Tagger vs Harriet Dart match: 0.69/0.71 mid 70.0%, model 57.0% (projection_v2.0 (prediction ledger)) -- gap -13.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26NOV01TAGDAR-16` Over 15.5 games: 0.83/0.94 mid 88.5%, model 97.3% (projection_v2.0 (prediction ledger)) -- gap +8.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tin Chen vs Mitsuki Wei Kang Leong -- ATP Challenger Taipei Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 08:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-01T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144844:211324:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tin Chen (`KXATPCHALLENGERMATCH-26NOV01CHELEO-CHE`) | 0.10 / 0.11 (1629) | 10.5% | 10.6% | 30.3% | 19.0% [18.3%-20.5%] | -- | 12.0% | -- | INSUFFICIENT_INPUTS | PASS | +0.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Mitsuki Wei Kang Leong (`KXATPCHALLENGERMATCH-26NOV01CHELEO-LEO`) | 0.89 / 0.90 (69) | 89.5% | 89.4% | 69.7% | 81.0% [79.5%-81.7%] | -- | 86.5% | -- | INSUFFICIENT_INPUTS | PASS | -0.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 3674.0; serve-point win A 55.4%, B 34.9%; Elo A 1186.6, B 1437.9; model uncertainty 0.0111
* Form inputs: days since last match A 1279, B 47; matches on record A 7, B 204; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.007, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Jake Delaney vs Kai-I Wang -- ATP Challenger Taipei Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 08:50Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-01T08:50:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:117359:212459:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jake Delaney (`KXATPCHALLENGERMATCH-26NOV01DELWAN-DEL`) | 0.84 / 0.85 (5436) | 84.5% | 79.8% | 65.0% | 77.5% [75.3%-79.2%] | -- | 85.8% | -- | INSUFFICIENT_INPUTS | PASS | -4.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kai-I Wang (`KXATPCHALLENGERMATCH-26NOV01DELWAN-WAN`) | 0.14 / 0.15 (253) | 14.5% | 20.2% | 35.0% | 22.4% [20.8%-24.7%] | -- | 14.2% | -- | INSUFFICIENT_INPUTS | PASS | +5.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3181.0, B 551.0; serve-point win A 67.8%, B 39.0%; Elo A 1414.5, B 1161.6; model uncertainty 0.0198
* Form inputs: days since last match A 12, B 243; matches on record A 340, B 18; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.004, surface_dev_loose +0.001, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY

## Petr Bar Biryukov vs Yaroslav Demin -- ATP Challenger Ningbo F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-01T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209951:211596:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Petr Bar Biryukov (`KXATPCHALLENGERMATCH-26NOV01BARDEM-BAR`) | 0.39 / 0.40 (13100) | 39.5% | 46.6% | 33.8% | 42.4% [39.2%-51.4%] | -- | 39.7% | 39.7% | MODEL_LONE_OUTLIER | WATCH | +7.1 pp | NORMAL | FRESH | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Yaroslav Demin (`KXATPCHALLENGERMATCH-26NOV01BARDEM-DEM`) | 0.60 / 0.61 (22) | 60.5% | 53.4% | 66.2% | 57.6% [48.6%-60.8%] | -- | 60.6% | 60.6% | MODEL_LONE_OUTLIER | PASS | -7.1 pp | NORMAL | FRESH | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4232.0, B 2769.0; serve-point win A 67.6%, B 31.7%; Elo A 1539.3, B 1479.2; model uncertainty 0.0614
* Form inputs: days since last match A 14, B 215; matches on record A 242, B 121; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.005, surface_dev_loose -0.023, surface_dev_tight +0.028
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Seo Yun Choi vs Aruzhan Sagandykova -- W100 Incheon R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264114:270061:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Seo Yun Choi (`KXITFWMATCH-26OCT31CHOSAG-CHO`) | 0.33 / 0.36 (30) | 34.5% | 47.1% | 57.4% | 48.9% [45.7%-51.1%] | -- | -- | -- | -- | WATCH | +12.7 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aruzhan Sagandykova (`KXITFWMATCH-26OCT31CHOSAG-SAG`) | 0.60 / 0.61 (65) | 60.5% | 52.8% | 42.6% | 51.1% [48.9%-54.3%] | -- | -- | -- | -- | PASS | -7.7 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 983.0, B 1744.0; serve-point win A 53.0%, B 46.4%; Elo A 1360.1, B 1403.7; model uncertainty 0.0267
* Form inputs: days since last match A 187, B 35; matches on record A 28, B 45; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.011, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## hyerin sim vs Ekaterina Ovcharenko -- W100 Incheon R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-01T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT31SIMOVC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Ovcharenko (`KXITFWMATCH-26OCT31SIMOVC-OVC`) | 0.88 / 0.92 (1) | 90.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| hyerin sim (`KXITFWMATCH-26OCT31SIMOVC-SIM`) | 0.09 / 0.10 (3) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mei Yamaguchi vs Zhibek Kulambayeva -- WTA Chennai Q3

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-01 12:40Z
* Current expected start: 2026-11-01 09:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: 2026-11-01 08:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-190_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-11-01T12:40:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214992:215614:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zhibek Kulambayeva (`KXWTAMATCH-26NOV01YAMKUL-KUL`) | 0.34 / 0.36 (124) | 35.0% | 39.8% | 60.5% | 48.4% [42.6%-53.2%] | -- | 34.8% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +4.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mei Yamaguchi (`KXWTAMATCH-26NOV01YAMKUL-YAM`) | 0.63 / 0.65 (883) | 64.0% | 60.2% | 39.5% | 51.6% [46.8%-57.4%] | -- | 65.3% | -- | INSUFFICIENT_INPUTS | PASS | -3.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3409.0, B 2176.0; serve-point win A 56.0%, B 46.0%; Elo A 1579.4, B 1446.3; model uncertainty 0.0529
* Form inputs: days since last match A 6, B 18; matches on record A 352, B 435; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.027, surface_pool_high +0.026, surface_dev_loose +0.026, surface_dev_tight -0.016
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26NOV01YAMKUL-2-KUL` Will Zhibek Kulambayeva win set 2 in the Mei Yamaguchi vs Zhibek Kulambayeva match: 0.02/0.98 mid 50.0%, model 43.2% (projection_v2.0 (prediction ledger)) -- gap -6.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01YAMKUL-2-YAM` Will Mei Yamaguchi win set 2 in the Mei Yamaguchi vs Zhibek Kulambayeva match: 0.02/0.98 mid 50.0%, model 56.8% (projection_v2.0 (prediction ledger)) -- gap +6.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01YAMKUL-1-KUL` Will Zhibek Kulambayeva win set 1 in the Mei Yamaguchi vs Zhibek Kulambayeva match: 0.37/0.40 mid 38.5%, model 43.2% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01YAMKUL-1-YAM` Will Mei Yamaguchi win set 1 in the Mei Yamaguchi vs Zhibek Kulambayeva match: 0.60/0.62 mid 61.0%, model 56.8% (projection_v2.0 (prediction ledger)) -- gap -4.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; WIDE_SPREAD

## M Rifqi Fitriadi vs Maxime Janvier -- M15 Singapore F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-01T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT31FITJAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M Rifqi Fitriadi (`KXITFMATCH-26OCT31FITJAN-FIT`) | 0.35 / 0.36 (359) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maxime Janvier (`KXITFMATCH-26OCT31FITJAN-JAN`) | 0.64 / 0.67 (554) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Violet Apisah vs Thasaporn Naklo -- W15 Singapore F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220597:221802:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Violet Apisah (`KXITFWMATCH-26OCT31APINAK-API`) | 0.58 / 0.61 (423) | 59.5% | 22.1% | 31.1% | 38.5% [37.0%-39.5%] | 59.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -37.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Thasaporn Naklo (`KXITFWMATCH-26OCT31APINAK-NAK`) | 0.41 / 0.42 (236) | 41.5% | 77.9% | 68.9% | 61.5% [60.5%-63.0%] | 40.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +36.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 122.0, B 2173.0; serve-point win A 52.0%, B 42.2%; Elo A 1379.7, B 1456.9; model uncertainty 0.0127
* Form inputs: days since last match A 2823, B 187; matches on record A 2, B 166; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT31APINAK-NAK  (YES = Thasaporn Naklo)
Model: 78%
Kalshi: 42%
Gap: +36 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kasidit Samrej vs Koki Matsuda -- ATP Challenger Taipei Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 09:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-01T09:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208937:211628:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Koki Matsuda (`KXATPCHALLENGERMATCH-26NOV01SAMMAT-MAT`) | 0.42 / 0.43 (20) | 42.5% | 33.4% | 33.7% | 33.7% [32.8%-35.0%] | -- | 42.2% | 42.2% | MODEL_LONE_OUTLIER | PASS | -9.1 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Kasidit Samrej (`KXATPCHALLENGERMATCH-26NOV01SAMMAT-SAM`) | 0.57 / 0.58 (6448) | 57.5% | 66.6% | 66.3% | 66.3% [65.0%-67.2%] | -- | 58.3% | 58.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +9.1 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4024.0, B 2832.0; serve-point win A 66.6%, B 36.9%; Elo A 1577.7, B 1462.9; model uncertainty 0.011
* Form inputs: days since last match A 12, B 12; matches on record A 294, B 146; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.009, surface_dev_loose +0.009, surface_dev_tight -0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Rinky Hijikata vs Vit Kopriva -- ATP Paris Q3

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-01 10:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: 2026-11-01 09:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200240:208014:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rinky Hijikata (`KXATPMATCH-26NOV01HIJKOP-HIJ`) | 0.68 / 0.69 (8152) | 68.5% | 59.6% | 54.1% | 56.6% [55.6%-58.7%] | -- | 67.8% | 67.8% | MODEL_LONE_OUTLIER | PASS | -8.9 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Vit Kopriva (`KXATPMATCH-26NOV01HIJKOP-KOP`) | 0.31 / 0.33 (6437) | 32.0% | 40.4% | 45.9% | 43.4% [41.3%-44.4%] | -- | 31.8% | 31.8% | MODEL_LONE_OUTLIER | SHADOW_BET | +8.4 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 6001.0, B 5742.0; serve-point win A 61.5%, B 40.4%; Elo A 1805.7, B 1675.9; model uncertainty 0.0152
* Form inputs: days since last match A 3, B 7; matches on record A 466, B 725; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.015, surface_dev_loose +0.015, surface_dev_tight -0.005
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26NOV01HIJKOP-HIJ21` Will Rinky Hijikata win the Rinky Hijikata vs Vit Kopriva match by a set score of 2-1?: 0.01/0.29 mid 15.0%, model 27.8% (projection_v2.0 (prediction ledger)) -- gap +12.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01HIJKOP-2-HIJ` Will Rinky Hijikata win set 2 in the Rinky Hijikata vs Vit Kopriva match: 0.13/0.80 mid 46.5%, model 56.4% (projection_v2.0 (prediction ledger)) -- gap +9.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01HIJKOP-1-HIJ` Will Rinky Hijikata win set 1 in the Rinky Hijikata vs Vit Kopriva match: 0.63/0.65 mid 64.0%, model 56.4% (projection_v2.0 (prediction ledger)) -- gap -7.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01HIJKOP-1-KOP` Will Vit Kopriva win set 1 in the Rinky Hijikata vs Vit Kopriva match: 0.35/0.37 mid 36.0%, model 43.6% (projection_v2.0 (prediction ledger)) -- gap +7.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01HIJKOP-HIJ20` Will Rinky Hijikata win the Rinky Hijikata vs Vit Kopriva match by a set score of 2-0?: 0.20/0.51 mid 35.5%, model 31.9% (projection_v2.0 (prediction ledger)) -- gap -3.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01HIJKOP-2-KOP` Will Vit Kopriva win set 2 in the Rinky Hijikata vs Vit Kopriva match: 0.13/0.80 mid 46.5%, model 43.6% (projection_v2.0 (prediction ledger)) -- gap -2.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01HIJKOP-KOP21` Will Vit Kopriva win the Rinky Hijikata vs Vit Kopriva match by a set score of 2-1?: 0.11/0.36 mid 23.5%, model 21.4% (projection_v2.0 (prediction ledger)) -- gap -2.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01HIJKOP-KOP20` Will Vit Kopriva win the Rinky Hijikata vs Vit Kopriva match by a set score of 2-0?: 0.11/0.23 mid 17.0%, model 19.0% (projection_v2.0 (prediction ledger)) -- gap +2.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Thiago Agustin Tirante vs Mattia Bellucci -- ATP Paris Q3

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-01 10:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: 2026-11-01 09:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:202058:208233:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mattia Bellucci (`KXATPMATCH-26NOV01TIRBEL-BEL`) | 0.62 / 0.63 (23739) | 62.5% | 57.9% | 49.0% | 51.5% [50.5%-53.4%] | -- | 61.8% | 61.8% | MODEL_LONE_OUTLIER | PASS | -4.6 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Thiago Agustin Tirante (`KXATPMATCH-26NOV01TIRBEL-TIR`) | 0.37 / 0.38 (1728) | 37.5% | 42.1% | 51.0% | 48.5% [46.6%-49.5%] | -- | 38.2% | 38.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +4.6 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5742.0, B 5542.0; serve-point win A 65.5%, B 32.9%; Elo A 1737.0, B 1811.0; model uncertainty 0.0145
* Form inputs: days since last match A 7, B 9; matches on record A 490, B 431; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose +0.000, surface_dev_tight -0.005
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26NOV01TIRBEL-TIR21` Will Thiago Agustin Tirante win the Thiago Agustin Tirante vs Mattia Bellucci match by a set score of 2-1?: 0.07/0.19 mid 13.0%, model 22.1% (projection_v2.0 (prediction ledger)) -- gap +9.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01TIRBEL-2-BEL` Will Mattia Bellucci win set 2 in the Thiago Agustin Tirante vs Mattia Bellucci match: 0.13/0.80 mid 46.5%, model 55.3% (projection_v2.0 (prediction ledger)) -- gap +8.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01TIRBEL-BEL20` Will Mattia Bellucci win the Thiago Agustin Tirante vs Mattia Bellucci match by a set score of 2-0?: 0.01/0.47 mid 24.0%, model 30.6% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01TIRBEL-BEL21` Will Mattia Bellucci win the Thiago Agustin Tirante vs Mattia Bellucci match by a set score of 2-1?: 0.15/0.27 mid 21.0%, model 27.3% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01TIRBEL-1-TIR` Will Thiago Agustin Tirante win set 1 in the Thiago Agustin Tirante vs Mattia Bellucci match: 0.38/0.39 mid 38.5%, model 44.7% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01TIRBEL-1-BEL` Will Mattia Bellucci win set 1 in the Thiago Agustin Tirante vs Mattia Bellucci match: 0.59/0.62 mid 60.5%, model 55.3% (projection_v2.0 (prediction ledger)) -- gap -5.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01TIRBEL-TIR20` Will Thiago Agustin Tirante win the Thiago Agustin Tirante vs Mattia Bellucci match by a set score of 2-0?: 0.16/0.28 mid 22.0%, model 20.0% (projection_v2.0 (prediction ledger)) -- gap -2.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01TIRBEL-2-TIR` Will Thiago Agustin Tirante win set 2 in the Thiago Agustin Tirante vs Mattia Bellucci match: 0.13/0.80 mid 46.5%, model 44.7% (projection_v2.0 (prediction ledger)) -- gap -1.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Prathyusha Rachapudi vs Ashmitha Easwaramurthi -- WTA 125K Luanda Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z
* Current expected start: 2026-11-01 10:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: 2026-11-01 09:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26NOV01RACEAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ashmitha Easwaramurthi (`KXWTACHALLENGERMATCH-26NOV01RACEAS-EAS`) | 0.10 / 0.11 (98) | 10.5% | 15.4% | -- | -- [-----] | -- | 11.6% | -- | INSUFFICIENT_INPUTS | -- | +4.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Prathyusha Rachapudi (`KXWTACHALLENGERMATCH-26NOV01RACEAS-RAC`) | 0.89 / 0.90 (129) | 89.5% | 84.6% | -- | -- [-----] | -- | 88.4% | -- | INSUFFICIENT_INPUTS | -- | -4.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 57.6%, B 50.0%; Elo A 1158.9, B 994.4; model uncertainty None
* Form inputs: days since last match A 187, B 41; matches on record A 124, B 293; data quality C
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY

## Alibek Kachmazov vs Chun-Chien Hou -- ATP Challenger Taipei Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-01T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208230:213114:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chun-Chien Hou (`KXATPCHALLENGERMATCH-26NOV01KACHOU-HOU`) | 0.06 / 0.07 (763) | 6.5% | 3.5% | 4.5% | 4.7% [3.6%-5.8%] | -- | 6.0% | 6.0% | MARKETS_AGREE | PASS | -3.0 pp | NORMAL | FRESH | F / POOR | ALL_AGREE | VERIFIED |
| Alibek Kachmazov (`KXATPCHALLENGERMATCH-26NOV01KACHOU-KAC`) | 0.92 / 0.93 (1) | 92.5% | 96.5% | 95.5% | 95.3% [94.2%-96.4%] | -- | 92.5% | -- | INSUFFICIENT_INPUTS | PASS | +4.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3660.0, B 552.0; serve-point win A 69.0%, B 45.3%; Elo A 1629.5, B 1114.4; model uncertainty 0.0112
* Form inputs: days since last match A 194, B 341; matches on record A 358, B 11; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.001, surface_dev_loose +0.006, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; THIN_DISPLAYED_SIZE

## eunchae Kim vs Erika Sema -- W100 Incheon R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:202454:260093:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| eunchae Kim (`KXITFWMATCH-26NOV01KIMSEM-KIM`) | 0.25 / 0.26 (34) | 25.5% | 25.4% | 32.9% | 28.6% [26.9%-29.5%] | -- | -- | -- | -- | PASS | -0.1 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Erika Sema (`KXITFWMATCH-26NOV01KIMSEM-SEM`) | 0.68 / 0.73 (150) | 70.5% | 74.6% | 67.1% | 71.4% [70.5%-73.2%] | -- | -- | -- | -- | PASS | +4.1 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 197.0, B 1873.0; serve-point win A 49.8%, B 45.3%; Elo A 1317.7, B 1485.0; model uncertainty 0.0135
* Form inputs: days since last match A 187, B 187; matches on record A 46, B 930; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.018, surface_pool_high +0.005, surface_dev_loose -0.004, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lucas Miedler / Neil Oberleitner vs Ryan Seggerman / Learner Tien -- ATP Vienna F

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-01 13:30Z
* Current expected start: 2026-11-01 10:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: 2026-11-01 09:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-01T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01MIEOBESEGTIE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucas Miedler / Neil Oberleitner (`KXATPDOUBLES-26NOV01MIEOBESEGTIE-MIEOBE`) | 0.60 / 0.63 (23) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ryan Seggerman / Learner Tien (`KXATPDOUBLES-26NOV01MIEOBESEGTIE-SEGTIE`) | 0.36 / 0.38 (109) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Alexander Donski vs Omar Jasika -- ATP Challenger Taipei Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 10:50Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-01T10:50:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:117357:200574:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Donski (`KXATPCHALLENGERMATCH-26NOV01DONJAS-DON`) | 0.42 / 0.43 (2124) | 42.5% | 48.5% | 53.9% | 50.0% [48.0%-52.0%] | -- | 43.9% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +6.0 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Omar Jasika (`KXATPCHALLENGERMATCH-26NOV01DONJAS-JAS`) | 0.57 / 0.58 (2594) | 57.5% | 51.5% | 46.1% | 50.0% [48.0%-52.0%] | -- | 56.2% | -- | INSUFFICIENT_INPUTS | PASS | -6.0 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2695.0, B 3991.0; serve-point win A 64.5%, B 35.2%; Elo A 1449.8, B 1501.6; model uncertainty 0.0198
* Form inputs: days since last match A 89, B 32; matches on record A 296, B 516; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Juan Manuel Cerundolo vs Miomir Kecmanovic -- ATP Paris Q3

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-01 11:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: 2026-11-01 10:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200175:207678:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Manuel Cerundolo (`KXATPMATCH-26NOV01CERKEC-CER`) | 0.54 / 0.55 (11363) | 54.5% | 48.4% | 46.5% | 46.5% [46.0%-47.0%] | -- | 55.8% | 55.8% | MODEL_LONE_OUTLIER | PASS | -6.1 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Miomir Kecmanovic (`KXATPMATCH-26NOV01CERKEC-KEC`) | 0.45 / 0.46 (2333) | 45.5% | 51.6% | 53.5% | 53.5% [53.0%-54.0%] | -- | 44.5% | 44.5% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.1 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 6168.0, B 5445.0; serve-point win A 63.6%, B 36.1%; Elo A 1741.5, B 1772.3; model uncertainty 0.005
* Form inputs: days since last match A 5, B 7; matches on record A 545, B 617; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose -0.005, surface_dev_tight +0.005
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26NOV01CERKEC-KEC20` Will Miomir Kecmanovic win the Juan Manuel Cerundolo vs Miomir Kecmanovic match by a set score of 2-0?: 0.01/0.31 mid 16.0%, model 26.1% (projection_v2.0 (prediction ledger)) -- gap +10.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01CERKEC-KEC21` Will Miomir Kecmanovic win the Juan Manuel Cerundolo vs Miomir Kecmanovic match by a set score of 2-1?: 0.09/0.26 mid 17.5%, model 25.5% (projection_v2.0 (prediction ledger)) -- gap +8.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01CERKEC-CER20` Will Juan Manuel Cerundolo win the Juan Manuel Cerundolo vs Miomir Kecmanovic match by a set score of 2-0?: 0.01/0.37 mid 19.0%, model 23.9% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01CERKEC-2-KEC` Will Miomir Kecmanovic win set 2 in the Juan Manuel Cerundolo vs Miomir Kecmanovic match: 0.13/0.80 mid 46.5%, model 51.1% (projection_v2.0 (prediction ledger)) -- gap +4.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01CERKEC-1-CER` Will Juan Manuel Cerundolo win set 1 in the Juan Manuel Cerundolo vs Miomir Kecmanovic match: 0.51/0.54 mid 52.5%, model 48.9% (projection_v2.0 (prediction ledger)) -- gap -3.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01CERKEC-1-KEC` Will Miomir Kecmanovic win set 1 in the Juan Manuel Cerundolo vs Miomir Kecmanovic match: 0.46/0.49 mid 47.5%, model 51.1% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01CERKEC-CER21` Will Juan Manuel Cerundolo win the Juan Manuel Cerundolo vs Miomir Kecmanovic match by a set score of 2-1?: 0.17/0.27 mid 22.0%, model 24.5% (projection_v2.0 (prediction ledger)) -- gap +2.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01CERKEC-2-CER` Will Juan Manuel Cerundolo win set 2 in the Juan Manuel Cerundolo vs Miomir Kecmanovic match: 0.13/0.80 mid 46.5%, model 48.9% (projection_v2.0 (prediction ledger)) -- gap +2.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Digvijay Pratap Singh vs Aristarkh Safonov -- M15 Fergana F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-01T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01SINSAF:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aristarkh Safonov (`KXITFMATCH-26NOV01SINSAF-SAF`) | 0.15 / 0.16 (882) | 15.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Digvijay Pratap Singh (`KXITFMATCH-26NOV01SINSAF-SIN`) | 0.84 / 0.87 (306) | 85.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Heerae Im vs Nagi Hanatani -- W100 Incheon R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211544:260091:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nagi Hanatani (`KXITFWMATCH-26NOV01IMXHAN-HAN`) | 0.53 / 0.57 (22) | 55.0% | 41.4% | 18.1% | 38.9% [30.0%-51.1%] | -- | -- | -- | -- | PASS | -13.6 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Heerae Im (`KXITFWMATCH-26NOV01IMXHAN-IMX`) | 0.43 / 0.44 (159) | 43.5% | 58.6% | 81.9% | 61.1% [48.9%-70.0%] | -- | -- | -- | -- | PASS | +15.1 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 568.0, B 1219.0; serve-point win A 52.5%, B 49.1%; Elo A 1336.6, B 1328.0; model uncertainty 0.1053
* Form inputs: days since last match A 187, B 187; matches on record A 61, B 446; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV01IMXHAN-IMX  (YES = Heerae Im)
Model: 59%
Kalshi: 44%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.031, surface_pool_high +0.025, surface_dev_loose +0.005, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alafia Ayeni vs Kaichi Uchida -- ATP Challenger Taipei Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 11:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-01T11:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111187:200366:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alafia Ayeni (`KXATPCHALLENGERMATCH-26NOV01AVEUCH-AVE`) | 0.49 / 0.50 (1025) | 49.5% | 53.6% | 51.0% | 49.5% [43.1%-53.0%] | -- | 49.6% | 49.6% | MODEL_LONE_OUTLIER | PASS | +4.1 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | AMBIGUOUS |
| Kaichi Uchida (`KXATPCHALLENGERMATCH-26NOV01AVEUCH-UCH`) | 0.49 / 0.51 (3059) | 50.0% | 46.4% | 49.0% | 50.5% [47.0%-56.9%] | -- | 50.7% | 50.7% | MODEL_LONE_OUTLIER | PASS | -3.6 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | AMBIGUOUS |

* Serve evidence (points): A 3164.0, B 4205.0; serve-point win A 65.2%, B 35.5%; Elo A 1471.0, B 1485.1; model uncertainty 0.0493
* Form inputs: days since last match A 54, B 12; matches on record A 318, B 834; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.030, surface_pool_high +0.035, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Sebastian Baez vs Tomas Machac -- ATP Paris Q3

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-01 11:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: 2026-11-01 10:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:202104:207830:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sebastian Baez (`KXATPMATCH-26NOV01BAEMAC-BAE`) | 0.16 / 0.17 (2585) | 16.5% | 31.0% | 39.4% | 35.0% [32.2%-36.9%] | -- | 17.7% | 17.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +14.5 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Tomas Machac (`KXATPMATCH-26NOV01BAEMAC-MAC`) | 0.83 / 0.84 (19455) | 83.5% | 69.0% | 60.6% | 65.0% [63.1%-67.8%] | -- | 82.7% | 82.7% | MODEL_LONE_OUTLIER | PASS | -14.5 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5268.0, B 4045.0; serve-point win A 58.9%, B 37.2%; Elo A 1712.8, B 1912.3; model uncertainty 0.0236
* Form inputs: days since last match A 7, B 5; matches on record A 506, B 458; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.009, surface_dev_loose -0.005, surface_dev_tight +0.009
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26NOV01BAEMAC-2-MAC` Will Tomas Machac win set 2 in the Sebastian Baez vs Tomas Machac match: 0.13/0.80 mid 46.5%, model 63.0% (projection_v2.0 (prediction ledger)) -- gap +16.5 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01BAEMAC-MAC21` Will Tomas Machac win the Sebastian Baez vs Tomas Machac match by a set score of 2-1?: 0.11/0.24 mid 17.5%, model 29.4% (projection_v2.0 (prediction ledger)) -- gap +11.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01BAEMAC-1-BAE` Will Sebastian Baez win set 1 in the Sebastian Baez vs Tomas Machac match: 0.26/0.27 mid 26.5%, model 37.0% (projection_v2.0 (prediction ledger)) -- gap +10.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01BAEMAC-1-MAC` Will Tomas Machac win set 1 in the Sebastian Baez vs Tomas Machac match: 0.72/0.74 mid 73.0%, model 63.0% (projection_v2.0 (prediction ledger)) -- gap -10.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01BAEMAC-2-BAE` Will Sebastian Baez win set 2 in the Sebastian Baez vs Tomas Machac match: 0.13/0.80 mid 46.5%, model 37.0% (projection_v2.0 (prediction ledger)) -- gap -9.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01BAEMAC-MAC20` Will Tomas Machac win the Sebastian Baez vs Tomas Machac match by a set score of 2-0?: 0.02/0.61 mid 31.5%, model 39.6% (projection_v2.0 (prediction ledger)) -- gap +8.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01BAEMAC-BAE21` Will Sebastian Baez win the Sebastian Baez vs Tomas Machac match by a set score of 2-1?: 0.07/0.21 mid 14.0%, model 17.3% (projection_v2.0 (prediction ledger)) -- gap +3.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01BAEMAC-BAE20` Will Sebastian Baez win the Sebastian Baez vs Tomas Machac match by a set score of 2-0?: 0.07/0.19 mid 13.0%, model 13.7% (projection_v2.0 (prediction ledger)) -- gap +0.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Benjamin Bonzi vs Yannick Hanfmann -- ATP Paris Q3

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-01 11:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: 2026-11-01 10:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105870:126127:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Benjamin Bonzi (`KXATPMATCH-26NOV01BONHAN-BON`) | 0.54 / 0.55 (5526) | 54.5% | 58.1% | 41.4% | 44.2% [43.3%-46.2%] | -- | 55.1% | 55.1% | MODEL_LONE_OUTLIER | PASS | +3.6 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Yannick Hanfmann (`KXATPMATCH-26NOV01BONHAN-HAN`) | 0.44 / 0.46 (8403) | 45.0% | 41.9% | 58.6% | 55.8% [53.8%-56.7%] | -- | 45.1% | 45.1% | MODEL_LONE_OUTLIER | SHADOW_BET | -3.1 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5634.0, B 5488.0; serve-point win A 67.8%, B 33.8%; Elo A 1823.5, B 1788.7; model uncertainty 0.0143
* Form inputs: days since last match A 10, B 3; matches on record A 800, B 705; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight +0.005
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26NOV01BONHAN-2-BON` Will Benjamin Bonzi win set 2 in the Benjamin Bonzi vs Yannick Hanfmann match: 0.12/0.80 mid 46.0%, model 55.4% (projection_v2.0 (prediction ledger)) -- gap +9.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01BONHAN-HAN20` Will Yannick Hanfmann win the Benjamin Bonzi vs Yannick Hanfmann match by a set score of 2-0?: 0.22/0.33 mid 27.5%, model 19.9% (projection_v2.0 (prediction ledger)) -- gap -7.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01BONHAN-BON20` Will Benjamin Bonzi win the Benjamin Bonzi vs Yannick Hanfmann match by a set score of 2-0?: 0.13/0.37 mid 25.0%, model 30.7% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01BONHAN-HAN21` Will Yannick Hanfmann win the Benjamin Bonzi vs Yannick Hanfmann match by a set score of 2-1?: 0.09/0.27 mid 18.0%, model 22.0% (projection_v2.0 (prediction ledger)) -- gap +4.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01BONHAN-BON21` Will Benjamin Bonzi win the Benjamin Bonzi vs Yannick Hanfmann match by a set score of 2-1?: 0.09/0.38 mid 23.5%, model 27.4% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01BONHAN-1-BON` Will Benjamin Bonzi win set 1 in the Benjamin Bonzi vs Yannick Hanfmann match: 0.52/0.54 mid 53.0%, model 55.4% (projection_v2.0 (prediction ledger)) -- gap +2.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01BONHAN-1-HAN` Will Yannick Hanfmann win set 1 in the Benjamin Bonzi vs Yannick Hanfmann match: 0.45/0.48 mid 46.5%, model 44.6% (projection_v2.0 (prediction ledger)) -- gap -1.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01BONHAN-2-HAN` Will Yannick Hanfmann win set 2 in the Benjamin Bonzi vs Yannick Hanfmann match: 0.12/0.80 mid 46.0%, model 44.6% (projection_v2.0 (prediction ledger)) -- gap -1.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Abigayel Vosloo vs Saumya Vig -- WTA 125K Luanda Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-01 14:10Z
* Current expected start: 2026-11-01 11:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: 2026-11-01 10:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · surface ? · scheduled 2026-11-01T14:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26NOV01VOSVIG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Saumya Vig (`KXWTACHALLENGERMATCH-26NOV01VOSVIG-VIG`) | 0.41 / 0.42 (187) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Abigayel Vosloo (`KXWTACHALLENGERMATCH-26NOV01VOSVIG-VOS`) | 0.58 / 0.59 (20) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Henry Bernet / Dominic Stricker vs Theo Arribage / Albano Olivetti -- ATP Basel F

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-01 15:00Z
* Current expected start: 2026-11-01 12:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: 2026-11-01 11:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-01T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01BERSTRARROLI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theo Arribage / Albano Olivetti (`KXATPDOUBLES-26NOV01BERSTRARROLI-ARROLI`) | 0.67 / 0.70 (36) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Henry Bernet / Dominic Stricker (`KXATPDOUBLES-26NOV01BERSTRARROLI-BERSTR`) | 0.28 / 0.31 (232) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Leonardo Borrelli vs Nico Hipfl -- ATP Challenger Taranto Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211503:212606:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leonardo Borrelli (`KXATPCHALLENGERMATCH-26NOV01BORHIP-BOR`) | 0.17 / 0.19 (1) | 18.0% | 22.5% | 14.1% | 24.1% [17.5%-31.5%] | -- | 18.7% | -- | INSUFFICIENT_INPUTS | PASS | +4.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nico Hipfl (`KXATPCHALLENGERMATCH-26NOV01BORHIP-HIP`) | 0.79 / 0.82 (2) | 80.5% | 77.5% | 85.9% | 75.9% [68.5%-82.5%] | -- | 81.0% | -- | INSUFFICIENT_INPUTS | PASS | -3.0 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 828.0, B 866.0; serve-point win A 60.5%, B 33.5%; Elo A 1141.6, B 1272.9; model uncertainty 0.0702
* Form inputs: days since last match A 215, B 54; matches on record A 19, B 45; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE

## Mika Brunold vs Michal Krajci -- ATP Challenger Bratislava II Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-01T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209983:211756:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mika Brunold (`KXATPCHALLENGERMATCH-26NOV01BRUKRA-BRU`) | 0.87 / 0.90 (145) | 88.5% | 85.8% | 81.9% | 83.8% [81.8%-86.7%] | -- | 86.5% | -- | INSUFFICIENT_INPUTS | PASS | -2.7 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Michal Krajci (`KXATPCHALLENGERMATCH-26NOV01BRUKRA-KRA`) | 0.09 / 0.12 (5) | 10.5% | 14.2% | 18.1% | 16.2% [13.3%-18.2%] | -- | 13.3% | -- | INSUFFICIENT_INPUTS | PASS | +3.7 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4071.0, B 3159.0; serve-point win A 65.1%, B 43.2%; Elo A 1658.9, B 1320.8; model uncertainty 0.0246
* Form inputs: days since last match A 5, B 159; matches on record A 238, B 120; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.012, surface_pool_high -0.013, surface_dev_loose +0.025, surface_dev_tight -0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE

## Manas Dhamne vs Loann Massard -- ATP Challenger Taranto Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210604:211768:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Manas Dhamne (`KXATPCHALLENGERMATCH-26NOV01DHAMAS-DHA`) | 0.65 / 0.68 (128) | 66.5% | 64.2% | 53.1% | 59.7% [56.6%-67.8%] | -- | 66.4% | -- | INSUFFICIENT_INPUTS | PASS | -2.3 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Loann Massard (`KXATPCHALLENGERMATCH-26NOV01DHAMAS-MAS`) | 0.31 / 0.34 (48) | 32.5% | 35.8% | 46.9% | 40.3% [32.2%-43.4%] | -- | 33.5% | -- | INSUFFICIENT_INPUTS | PASS | +3.3 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3842.0, B 3485.0; serve-point win A 62.2%, B 40.7%; Elo A 1549.6, B 1372.0; model uncertainty 0.056
* Form inputs: days since last match A 54, B 222; matches on record A 148, B 152; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER

## Rafael Izquierdo Luque vs Ziga Sesko -- ATP Challenger Taranto Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202258:212949:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rafael Izquierdo Luque (`KXATPCHALLENGERMATCH-26NOV01IZQSES-IZQ`) | 0.31 / 0.36 (26) | 33.5% | 61.5% | 54.1% | 56.7% [56.2%-57.2%] | -- | 38.4% | -- | INSUFFICIENT_INPUTS | PASS | +28.0 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ziga Sesko (`KXATPCHALLENGERMATCH-26NOV01IZQSES-SES`) | 0.63 / 0.69 (4) | 66.0% | 38.5% | 45.9% | 43.3% [42.8%-43.8%] | -- | 61.6% | -- | INSUFFICIENT_INPUTS | PASS | -27.5 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1966.0, B 731.0; serve-point win A 60.7%, B 41.6%; Elo A 1386.7, B 1333.9; model uncertainty 0.0052
* Form inputs: days since last match A 187, B 60; matches on record A 83, B 28; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV01IZQSES-IZQ  (YES = Rafael Izquierdo Luque)
Model: 62%
Kalshi: 34%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE

## Leonardo Rossi vs Alessio Balestrieri -- ATP Challenger Taranto Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01ROSBAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alessio Balestrieri (`KXATPCHALLENGERMATCH-26NOV01ROSBAL-BAL`) | 0.34 / 0.39 (95) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Leonardo Rossi (`KXATPCHALLENGERMATCH-26NOV01ROSBAL-ROS`) | 0.61 / 0.64 (1077) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Faris Zakaria vs Niels Visker -- ATP Challenger Bratislava II Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01ZAKVIS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Niels Visker (`KXATPCHALLENGERMATCH-26NOV01ZAKVIS-VIS`) | 0.78 / 0.82 (1) | 80.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Faris Zakaria (`KXATPCHALLENGERMATCH-26NOV01ZAKVIS-ZAK`) | 0.15 / 0.20 (9) | 17.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Alex de Minaur vs Carlos Alcaraz -- ATP Vienna F

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-01 16:00Z
* Current expected start: 2026-11-01 13:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: 2026-11-01 12:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Clay · scheduled 2026-11-01T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200282:207989:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlos Alcaraz (`KXATPMATCH-26NOV01DEALC-ALC`) | 0.81 / 0.82 (248435) | 81.5% | 81.0% | 79.3% | 82.5% [79.9%-84.4%] | 78.6% | -- | 78.6% | KALSHI_LONE_OUTLIER | PASS | -0.5 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Alex de Minaur (`KXATPMATCH-26NOV01DEALC-DE`) | 0.18 / 0.19 (7744) | 18.5% | 19.0% | 20.7% | 17.5% [15.6%-20.1%] | 21.4% | -- | 21.4% | KALSHI_LONE_OUTLIER | PASS | +0.5 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 6479.0, B 5488.0; serve-point win A 56.3%, B 37.0%; Elo A 1947.4, B 2346.8; model uncertainty 0.0225
* Form inputs: days since last match A 1, B 1; matches on record A 692, B 479; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.013, surface_dev_loose -0.017, surface_dev_tight +0.018
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26NOV01DEALC-ALC21` Will Carlos Alcaraz win the Alex de Minaur vs Carlos Alcaraz match by a set score of 2-1?: 0.21/0.23 mid 22.0%, model 29.0% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01DEALC-ALC20` Will Carlos Alcaraz win the Alex de Minaur vs Carlos Alcaraz match by a set score of 2-0?: 0.57/0.59 mid 58.0%, model 51.9% (projection_v2.0 (prediction ledger)) -- gap -6.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01DEALC-ALC2` Will Carlos Alcaraz win at least 1.5 more games than Alex de Minaur?: 0.67/0.79 mid 73.0%, model 76.1% (projection_v2.0 (prediction ledger)) -- gap +3.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01DEALC-2-DE` Will Alex de Minaur win set 2 in the Alex de Minaur vs Carlos Alcaraz match: 0.24/0.26 mid 25.0%, model 27.9% (projection_v2.0 (prediction ledger)) -- gap +2.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV01DEALC-22` Over 21.5 games: 0.50/0.52 mid 51.0%, model 53.9% (projection_v2.0 (prediction ledger)) -- gap +2.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01DEALC-DE21` Will Alex de Minaur win the Alex de Minaur vs Carlos Alcaraz match by a set score of 2-1?: 0.08/0.10 mid 9.0%, model 11.2% (projection_v2.0 (prediction ledger)) -- gap +2.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01DEALC-ALC5` Will Carlos Alcaraz win at least 4.5 more games than Alex de Minaur?: 0.44/0.45 mid 44.5%, model 46.7% (projection_v2.0 (prediction ledger)) -- gap +2.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01DEALC-2-ALC` Will Carlos Alcaraz win set 2 in the Alex de Minaur vs Carlos Alcaraz match: 0.72/0.76 mid 74.0%, model 72.1% (projection_v2.0 (prediction ledger)) -- gap -1.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV01DEALC-17` Over 16.5 games: 0.84/0.94 mid 89.0%, model 90.9% (projection_v2.0 (prediction ledger)) -- gap +1.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01DEALC-27` Over 26.5 games: 0.24/0.38 mid 31.0%, model 32.3% (projection_v2.0 (prediction ledger)) -- gap +1.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01DEALC-1-ALC` Will Carlos Alcaraz win set 1 in the Alex de Minaur vs Carlos Alcaraz match: 0.72/0.74 mid 73.0%, model 72.1% (projection_v2.0 (prediction ledger)) -- gap -0.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01DEALC-1-DE` Will Alex de Minaur win set 1 in the Alex de Minaur vs Carlos Alcaraz match: 0.26/0.28 mid 27.0%, model 27.9% (projection_v2.0 (prediction ledger)) -- gap +0.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01DEALC-DE20` Will Alex de Minaur win the Alex de Minaur vs Carlos Alcaraz match by a set score of 2-0?: 0.07/0.10 mid 8.5%, model 7.8% (projection_v2.0 (prediction ledger)) -- gap -0.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01DEALC-ALC8` Will Carlos Alcaraz win at least 7.5 more games than Alex de Minaur?: 0.03/0.17 mid 10.0%, model 9.9% (projection_v2.0 (prediction ledger)) -- gap -0.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Adolfo Daniel Vallejo vs Lorenzo Sonego -- ATP Paris Q3

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-01 12:00Z
* Current expected start: 2026-11-01 13:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: 2026-11-01 12:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+60_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:132283:209226:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Sonego (`KXATPMATCH-26NOV01VALSON-SON`) | 0.56 / 0.57 (1240) | 56.5% | 46.2% | 54.0% | 55.0% [53.5%-56.0%] | 57.5% | -- | 57.5% | MODEL_LONE_OUTLIER | PASS | -10.3 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Adolfo Daniel Vallejo (`KXATPMATCH-26NOV01VALSON-VAL`) | 0.43 / 0.44 (13505) | 43.5% | 53.8% | 46.0% | 45.0% [44.0%-46.5%] | 42.5% | -- | 42.5% | MODEL_LONE_OUTLIER | SHADOW_BET | +10.3 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5609.0, B 4676.0; serve-point win A 63.7%, B 37.1%; Elo A 1709.1, B 1769.7; model uncertainty 0.0124
* Form inputs: days since last match A 7, B 6; matches on record A 229, B 701; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose -0.010, surface_dev_tight +0.015
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26NOV01VALSON-SON20` Will Lorenzo Sonego win the Adolfo Daniel Vallejo vs Lorenzo Sonego match by a set score of 2-0?: 0.34/0.44 mid 39.0%, model 22.5% (projection_v2.0 (prediction ledger)) -- gap -16.5 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01VALSON-VAL21` Will Adolfo Daniel Vallejo win the Adolfo Daniel Vallejo vs Lorenzo Sonego match by a set score of 2-1?: 0.01/0.28 mid 14.5%, model 26.2% (projection_v2.0 (prediction ledger)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01VALSON-1-SON` Will Lorenzo Sonego win set 1 in the Adolfo Daniel Vallejo vs Lorenzo Sonego match: 0.56/0.58 mid 57.0%, model 47.4% (projection_v2.0 (prediction ledger)) -- gap -9.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01VALSON-1-VAL` Will Adolfo Daniel Vallejo win set 1 in the Adolfo Daniel Vallejo vs Lorenzo Sonego match: 0.42/0.44 mid 43.0%, model 52.6% (projection_v2.0 (prediction ledger)) -- gap +9.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01VALSON-2-VAL` Will Adolfo Daniel Vallejo win set 2 in the Adolfo Daniel Vallejo vs Lorenzo Sonego match: 0.15/0.80 mid 47.5%, model 52.6% (projection_v2.0 (prediction ledger)) -- gap +5.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01VALSON-SON21` Will Lorenzo Sonego win the Adolfo Daniel Vallejo vs Lorenzo Sonego match by a set score of 2-1?: 0.16/0.38 mid 27.0%, model 23.6% (projection_v2.0 (prediction ledger)) -- gap -3.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01VALSON-VAL20` Will Adolfo Daniel Vallejo win the Adolfo Daniel Vallejo vs Lorenzo Sonego match by a set score of 2-0?: 0.17/0.38 mid 27.5%, model 27.6% (projection_v2.0 (prediction ledger)) -- gap +0.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01VALSON-2-SON` Will Lorenzo Sonego win set 2 in the Adolfo Daniel Vallejo vs Lorenzo Sonego match: 0.15/0.80 mid 47.5%, model 47.4% (projection_v2.0 (prediction ledger)) -- gap -0.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Darja Suvirdjonkova vs Emma van Poppel -- WTA 125K Luanda Q2

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-01 16:00Z
* Current expected start: 2026-11-01 13:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: 2026-11-01 12:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · surface ? · scheduled 2026-11-01T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26NOV01SUVVAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Darja Suvirdjonkova (`KXWTACHALLENGERMATCH-26NOV01SUVVAN-SUV`) | 0.31 / 0.94 (2) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Emma van Poppel (`KXWTACHALLENGERMATCH-26NOV01SUVVAN-VAN`) | 0.06 / 0.60 (100) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Guido Andreozzi / Manuel Guinard vs Adam Pavlasek / Patrik Rikl -- ATP Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-01T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01ANDGUIPAVRIK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Guido Andreozzi / Manuel Guinard (`KXATPDOUBLES-26NOV01ANDGUIPAVRIK-ANDGUI`) | 0.06 / 0.94 (3) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Adam Pavlasek / Patrik Rikl (`KXATPDOUBLES-26NOV01ANDGUIPAVRIK-PAVRIK`) | 0.06 / 0.94 (3) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Theo Arribage / Albano Olivetti vs Julian Cash / Lloyd Glasspool -- ATP Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-01T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01ARROLICASGLA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theo Arribage / Albano Olivetti (`KXATPDOUBLES-26NOV01ARROLICASGLA-ARROLI`) | 0.05 / 0.88 (2) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Julian Cash / Lloyd Glasspool (`KXATPDOUBLES-26NOV01ARROLICASGLA-CASGLA`) | 0.07 / 0.94 (2) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Simone Bolelli / Andrea Vavassori vs Jakob Schnaitter / Mark Wallner -- ATP Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-01T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01BOLVAVSCHWAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Simone Bolelli / Andrea Vavassori (`KXATPDOUBLES-26NOV01BOLVAVSCHWAL-BOLVAV`) | 0.16 / 0.93 (9) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jakob Schnaitter / Mark Wallner (`KXATPDOUBLES-26NOV01BOLVAVSCHWAL-SCHWAL`) | 0.07 / 0.78 (1) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ignacio Buse vs Zizou Bergs -- ATP Paris R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200267:209860:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zizou Bergs (`KXATPMATCH-26NOV01BUSBER-BER`) | 0.71 / 0.73 (33615) | 72.0% | 68.0% | 67.6% | 66.2% [64.8%-67.6%] | -- | -- | -- | -- | PASS | -4.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ignacio Buse (`KXATPMATCH-26NOV01BUSBER-BUS`) | 0.27 / 0.28 (2294) | 27.5% | 32.0% | 32.4% | 33.8% [32.4%-35.2%] | -- | -- | -- | -- | PASS | +4.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5678.0, B 5846.0; serve-point win A 60.3%, B 36.0%; Elo A 1755.2, B 1841.6; model uncertainty 0.0138
* Form inputs: days since last match A 4, B 4; matches on record A 287, B 572; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.005, surface_dev_loose -0.014, surface_dev_tight +0.009
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPSETWINNER-26NOV01BUSBER-2-BER` Will Zizou Bergs win set 2 in the Ignacio Buse vs Zizou Bergs match: 0.13/0.80 mid 46.5%, model 62.2% (projection_v2.0 (prediction ledger)) -- gap +15.7 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01BUSBER-BER21` Will Zizou Bergs win the Ignacio Buse vs Zizou Bergs match by a set score of 2-1?: 0.01/0.29 mid 15.0%, model 29.2% (projection_v2.0 (prediction ledger)) -- gap +14.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01BUSBER-28` Over 27.5 games: 0.11/0.34 mid 22.5%, model 36.5% (projection_v2.0 (prediction ledger)) -- gap +14.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01BUSBER-18` Over 17.5 games: 0.60/0.95 mid 77.5%, model 90.6% (projection_v2.0 (prediction ledger)) -- gap +13.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01BUSBER-BER7` Will Zizou Bergs win at least 6.5 more games than Ignacio Buse?: 0.08/0.36 mid 22.0%, model 9.8% (projection_v2.0 (prediction ledger)) -- gap -12.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01BUSBER-BER20` Will Zizou Bergs win the Ignacio Buse vs Zizou Bergs match by a set score of 2-0?: 0.01/0.54 mid 27.5%, model 38.7% (projection_v2.0 (prediction ledger)) -- gap +11.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01BUSBER-23` Over 22.5 games: 0.44/0.47 mid 45.5%, model 56.5% (projection_v2.0 (prediction ledger)) -- gap +11.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01BUSBER-2-BUS` Will Ignacio Buse win set 2 in the Ignacio Buse vs Zizou Bergs match: 0.13/0.80 mid 46.5%, model 37.8% (projection_v2.0 (prediction ledger)) -- gap -8.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV01BUSBER-BER4` Will Zizou Bergs win at least 3.5 more games than Ignacio Buse?: 0.49/0.52 mid 50.5%, model 43.5% (projection_v2.0 (prediction ledger)) -- gap -7.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01BUSBER-1-BER` Will Zizou Bergs win set 1 in the Ignacio Buse vs Zizou Bergs match: 0.64/0.67 mid 65.5%, model 62.2% (projection_v2.0 (prediction ledger)) -- gap -3.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01BUSBER-BUS20` Will Ignacio Buse win the Ignacio Buse vs Zizou Bergs match by a set score of 2-0?: 0.01/0.21 mid 11.0%, model 14.3% (projection_v2.0 (prediction ledger)) -- gap +3.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01BUSBER-BUS2` Will Ignacio Buse win at least 1.5 more games than Zizou Bergs?: 0.21/0.37 mid 29.0%, model 25.7% (projection_v2.0 (prediction ledger)) -- gap -3.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01BUSBER-1-BUS` Will Ignacio Buse win set 1 in the Ignacio Buse vs Zizou Bergs match: 0.34/0.36 mid 35.0%, model 37.8% (projection_v2.0 (prediction ledger)) -- gap +2.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01BUSBER-BUS21` Will Ignacio Buse win the Ignacio Buse vs Zizou Bergs match by a set score of 2-1?: 0.01/0.37 mid 19.0%, model 17.8% (projection_v2.0 (prediction ledger)) -- gap -1.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ignacio Buse / Luciano Darderi vs Benjamin Bonzi / Arthur Rinderknech -- ATP Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-01T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01BUSDARBONRIN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Benjamin Bonzi / Arthur Rinderknech (`KXATPDOUBLES-26NOV01BUSDARBONRIN-BONRIN`) | 0.06 / 0.94 (3) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ignacio Buse / Luciano Darderi (`KXATPDOUBLES-26NOV01BUSDARBONRIN-BUSDAR`) | 0.06 / 0.94 (3) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Robert Cash / Brandon Nakashima vs Valentin Vacherot / Luca Van Assche -- ATP Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-01T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01CASNAKVACVAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Robert Cash / Brandon Nakashima (`KXATPDOUBLES-26NOV01CASNAKVACVAN-CASNAK`) | 0.06 / 0.93 (2) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Valentin Vacherot / Luca Van Assche (`KXATPDOUBLES-26NOV01CASNAKVACVAN-VACVAN`) | 0.06 / 0.93 (2) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Francisco Cerundolo / Tomas Martin Etcheverry vs Marc Polmans / Jan Zielinski -- ATP Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-01T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01CERETCPOLZIE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francisco Cerundolo / Tomas Martin Etcheverry (`KXATPDOUBLES-26NOV01CERETCPOLZIE-CERETC`) | 0.07 / 0.93 (11) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marc Polmans / Jan Zielinski (`KXATPDOUBLES-26NOV01CERETCPOLZIE-POLZIE`) | 0.07 / 0.93 (11) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Alejandro Davidovich Fokina vs Moise Kouame -- ATP Paris R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200221:213608:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alejandro Davidovich Fokina (`KXATPMATCH-26NOV01DAVKOU-DAV`) | 0.62 / 0.69 (15) | 65.5% | 84.1% | 77.7% | 82.0% [79.6%-86.5%] | -- | -- | -- | -- | WATCH | +18.6 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Moise Kouame (`KXATPMATCH-26NOV01DAVKOU-KOU`) | 0.35 / 0.36 (2270) | 35.5% | 15.9% | 22.3% | 18.0% [13.5%-20.4%] | -- | -- | -- | -- | PASS | -19.6 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5501.0, B 3247.0; serve-point win A 65.8%, B 42.0%; Elo A 1995.3, B 1625.1; model uncertainty 0.0348
* Form inputs: days since last match A 13, B 10; matches on record A 568, B 83; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26NOV01DAVKOU-DAV  (YES = Alejandro Davidovich Fokina)
Model: 84%
Kalshi: 66%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, NO_EXTERNAL_REFERENCE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.022, surface_pool_high -0.021, surface_dev_loose -0.000, surface_dev_tight +0.003
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26NOV01DAVKOU-1-DAV` Will Alejandro Davidovich Fokina win set 1 in the Alejandro Davidovich Fokina vs Moise Kouame match: 0.13/0.80 mid 46.5%, model 74.7% (projection_v2.0 (prediction ledger)) -- gap +28.2 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01DAVKOU-2-DAV` Will Alejandro Davidovich Fokina win set 2 in the Alejandro Davidovich Fokina vs Moise Kouame match: 0.13/0.80 mid 46.5%, model 74.7% (projection_v2.0 (prediction ledger)) -- gap +28.2 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01DAVKOU-1-KOU` Will Moise Kouame win set 1 in the Alejandro Davidovich Fokina vs Moise Kouame match: 0.13/0.80 mid 46.5%, model 25.3% (projection_v2.0 (prediction ledger)) -- gap -21.2 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01DAVKOU-2-KOU` Will Moise Kouame win set 2 in the Alejandro Davidovich Fokina vs Moise Kouame match: 0.13/0.80 mid 46.5%, model 25.3% (projection_v2.0 (prediction ledger)) -- gap -21.2 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01DAVKOU-DAV20` Will Alejandro Davidovich Fokina win the Alejandro Davidovich Fokina vs Moise Kouame match by a set score of 2-0?: 0.01/0.77 mid 39.0%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap +16.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01DAVKOU-KOU20` Will Moise Kouame win the Alejandro Davidovich Fokina vs Moise Kouame match by a set score of 2-0?: 0.01/0.43 mid 22.0%, model 6.4% (projection_v2.0 (prediction ledger)) -- gap -15.6 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01DAVKOU-DAV21` Will Alejandro Davidovich Fokina win the Alejandro Davidovich Fokina vs Moise Kouame match by a set score of 2-1?: 0.01/0.75 mid 38.0%, model 28.2% (projection_v2.0 (prediction ledger)) -- gap -9.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01DAVKOU-KOU21` Will Moise Kouame win the Alejandro Davidovich Fokina vs Moise Kouame match by a set score of 2-1?: 0.01/0.21 mid 11.0%, model 9.6% (projection_v2.0 (prediction ledger)) -- gap -1.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Novak Djokovic vs Valentin Vacherot -- ATP Paris R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:104925:200473:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Novak Djokovic (`KXATPMATCH-26NOV01DJOVAC-DJO`) | 0.65 / 0.68 (69) | 66.5% | 73.7% | 71.6% | 76.6% [74.3%-82.5%] | -- | -- | -- | -- | SHADOW_BET | +7.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valentin Vacherot (`KXATPMATCH-26NOV01DJOVAC-VAC`) | 0.31 / 0.33 (2700) | 32.0% | 26.3% | 28.4% | 23.4% [17.5%-25.7%] | -- | -- | -- | -- | PASS | -5.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4375.0, B 4676.0; serve-point win A 70.9%, B 34.4%; Elo A 2250.1, B 1896.6; model uncertainty 0.041
* Form inputs: days since last match A 2, B 1; matches on record A 1505, B 425; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.028, surface_pool_high -0.022, surface_dev_loose -0.008, surface_dev_tight +0.016
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 8 carry a model probability
  * `KXATPEXACTMATCH-26NOV01DJOVAC-DJO20` Will Novak Djokovic win the Novak Djokovic vs Valentin Vacherot match by a set score of 2-0?: 0.01/0.47 mid 24.0%, model 44.1% (projection_v2.0 (prediction ledger)) -- gap +20.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01DJOVAC-DJO21` Will Novak Djokovic win the Novak Djokovic vs Valentin Vacherot match by a set score of 2-1?: 0.01/0.32 mid 16.5%, model 29.6% (projection_v2.0 (prediction ledger)) -- gap +13.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01DJOVAC-1-DJO` Will Novak Djokovic win set 1 in the Novak Djokovic vs Valentin Vacherot match: 0.12/0.98 mid 55.0%, model 66.4% (projection_v2.0 (prediction ledger)) -- gap +11.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01DJOVAC-2-DJO` Will Novak Djokovic win set 2 in the Novak Djokovic vs Valentin Vacherot match: 0.12/0.98 mid 55.0%, model 66.4% (projection_v2.0 (prediction ledger)) -- gap +11.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01DJOVAC-2-VAC` Will Valentin Vacherot win set 2 in the Novak Djokovic vs Valentin Vacherot match: 0.02/0.80 mid 41.0%, model 33.6% (projection_v2.0 (prediction ledger)) -- gap -7.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01DJOVAC-1-VAC` Will Valentin Vacherot win set 1 in the Novak Djokovic vs Valentin Vacherot match: 0.01/0.80 mid 40.5%, model 33.6% (projection_v2.0 (prediction ledger)) -- gap -6.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01DJOVAC-VAC21` Will Valentin Vacherot win the Novak Djokovic vs Valentin Vacherot match by a set score of 2-1?: 0.01/0.23 mid 12.0%, model 15.0% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01DJOVAC-VAC20` Will Valentin Vacherot win the Novak Djokovic vs Valentin Vacherot match by a set score of 2-0?: 0.01/0.23 mid 12.0%, model 11.3% (projection_v2.0 (prediction ledger)) -- gap -0.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Alexander Erler / Daniil Medvedev (`KXATPDOUBLES-26NOV01ERLMEDKRAPUT-ERLMED`) | 0.06 / 0.93 (2) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kevin Krawietz / Tim Putz (`KXATPDOUBLES-26NOV01ERLMEDKRAPUT-KRAPUT`) | 0.06 / 0.93 (2) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Quentin Halys vs Arthur Fery -- ATP Paris R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111460:209259:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arthur Fery (`KXATPMATCH-26NOV01HALFER-FER`) | 0.42 / 0.43 (18780) | 42.5% | 48.6% | 52.4% | 51.9% [50.5%-52.4%] | -- | -- | -- | -- | PASS | +6.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Quentin Halys (`KXATPMATCH-26NOV01HALFER-HAL`) | 0.57 / 0.58 (2065) | 57.5% | 51.4% | 47.6% | 48.1% [47.6%-49.5%] | -- | -- | -- | -- | PASS | -6.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6422.0, B 4544.0; serve-point win A 66.4%, B 33.9%; Elo A 1834.0, B 1831.9; model uncertainty 0.0097
* Form inputs: days since last match A 5, B 1; matches on record A 840, B 267; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV01HALFER-18` Over 17.5 games: 0.64/0.96 mid 80.0%, model 95.7% (projection_v2.0 (prediction ledger)) -- gap +15.7 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01HALFER-HAL6` Will Quentin Halys win at least 5.5 more games than Arthur Fery?: 0.01/0.39 mid 20.0%, model 6.7% (projection_v2.0 (prediction ledger)) -- gap -13.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01HALFER-FER21` Will Arthur Fery win the Quentin Halys vs Arthur Fery match by a set score of 2-1?: 0.01/0.25 mid 13.0%, model 24.5% (projection_v2.0 (prediction ledger)) -- gap +11.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01HALFER-HAL21` Will Quentin Halys win the Quentin Halys vs Arthur Fery match by a set score of 2-1?: 0.01/0.29 mid 15.0%, model 25.4% (projection_v2.0 (prediction ledger)) -- gap +10.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01HALFER-HAL3` Will Quentin Halys win at least 2.5 more games than Arthur Fery?: 0.44/0.46 mid 45.0%, model 35.2% (projection_v2.0 (prediction ledger)) -- gap -9.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01HALFER-FER20` Will Arthur Fery win the Quentin Halys vs Arthur Fery match by a set score of 2-0?: 0.01/0.30 mid 15.5%, model 24.1% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01HALFER-23` Over 22.5 games: 0.57/0.59 mid 58.0%, model 64.4% (projection_v2.0 (prediction ledger)) -- gap +6.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01HALFER-1-FER` Will Arthur Fery win set 1 in the Quentin Halys vs Arthur Fery match: 0.42/0.45 mid 43.5%, model 49.1% (projection_v2.0 (prediction ledger)) -- gap +5.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01HALFER-1-HAL` Will Quentin Halys win set 1 in the Quentin Halys vs Arthur Fery match: 0.55/0.58 mid 56.5%, model 50.9% (projection_v2.0 (prediction ledger)) -- gap -5.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV01HALFER-FER2` Will Arthur Fery win at least 1.5 more games than Quentin Halys?: 0.27/0.64 mid 45.5%, model 40.6% (projection_v2.0 (prediction ledger)) -- gap -4.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01HALFER-HAL20` Will Quentin Halys win the Quentin Halys vs Arthur Fery match by a set score of 2-0?: 0.01/0.41 mid 21.0%, model 25.9% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01HALFER-28` Over 27.5 games: 0.18/0.60 mid 39.0%, model 43.6% (projection_v2.0 (prediction ledger)) -- gap +4.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01HALFER-2-HAL` Will Quentin Halys win set 2 in the Quentin Halys vs Arthur Fery match: 0.13/0.80 mid 46.5%, model 50.9% (projection_v2.0 (prediction ledger)) -- gap +4.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01HALFER-2-FER` Will Arthur Fery win set 2 in the Quentin Halys vs Arthur Fery match: 0.13/0.80 mid 46.5%, model 49.1% (projection_v2.0 (prediction ledger)) -- gap +2.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ugo Humbert vs Botic Van de Zandschulp -- ATP Paris R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:122298:200005:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ugo Humbert (`KXATPMATCH-26NOV01HUMVAN-HUM`) | 0.59 / 0.60 (175) | 59.5% | 56.1% | 54.9% | 55.9% [54.9%-56.4%] | -- | -- | -- | -- | PASS | -3.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Botic Van de Zandschulp (`KXATPMATCH-26NOV01HUMVAN-VAN`) | 0.41 / 0.42 (21180) | 41.5% | 43.9% | 45.1% | 44.1% [43.6%-45.1%] | -- | -- | -- | -- | PASS | +2.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4892.0, B 5999.0; serve-point win A 65.9%, B 35.4%; Elo A 1938.3, B 1883.9; model uncertainty 0.0072
* Form inputs: days since last match A 3, B 4; matches on record A 625, B 651; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.005, surface_dev_loose -0.000, surface_dev_tight +0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26NOV01HUMVAN-HUM6` Will Ugo Humbert win at least 5.5 more games than Botic Van de Zandschulp?: 0.09/0.37 mid 23.0%, model 9.1% (projection_v2.0 (prediction ledger)) -- gap -13.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01HUMVAN-19` Over 18.5 games: 0.59/0.94 mid 76.5%, model 90.2% (projection_v2.0 (prediction ledger)) -- gap +13.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01HUMVAN-HUM21` Will Ugo Humbert win the Ugo Humbert vs Botic Van de Zandschulp match by a set score of 2-1?: 0.01/0.29 mid 15.0%, model 26.9% (projection_v2.0 (prediction ledger)) -- gap +11.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01HUMVAN-24` Over 23.5 games: 0.43/0.46 mid 44.5%, model 55.5% (projection_v2.0 (prediction ledger)) -- gap +11.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01HUMVAN-VAN21` Will Botic Van de Zandschulp win the Ugo Humbert vs Botic Van de Zandschulp match by a set score of 2-1?: 0.01/0.24 mid 12.5%, model 22.8% (projection_v2.0 (prediction ledger)) -- gap +10.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01HUMVAN-HUM3` Will Ugo Humbert win at least 2.5 more games than Botic Van de Zandschulp?: 0.47/0.50 mid 48.5%, model 40.3% (projection_v2.0 (prediction ledger)) -- gap -8.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01HUMVAN-2-HUM` Will Ugo Humbert win set 2 in the Ugo Humbert vs Botic Van de Zandschulp match: 0.13/0.80 mid 46.5%, model 54.1% (projection_v2.0 (prediction ledger)) -- gap +7.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01HUMVAN-HUM20` Will Ugo Humbert win the Ugo Humbert vs Botic Van de Zandschulp match by a set score of 2-0?: 0.01/0.43 mid 22.0%, model 29.3% (projection_v2.0 (prediction ledger)) -- gap +7.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01HUMVAN-VAN20` Will Botic Van de Zandschulp win the Ugo Humbert vs Botic Van de Zandschulp match by a set score of 2-0?: 0.01/0.28 mid 14.5%, model 21.1% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01HUMVAN-29` Over 28.5 games: 0.06/0.60 mid 33.0%, model 38.0% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01HUMVAN-1-HUM` Will Ugo Humbert win set 1 in the Ugo Humbert vs Botic Van de Zandschulp match: 0.57/0.60 mid 58.5%, model 54.1% (projection_v2.0 (prediction ledger)) -- gap -4.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01HUMVAN-1-VAN` Will Botic Van de Zandschulp win set 1 in the Ugo Humbert vs Botic Van de Zandschulp match: 0.40/0.43 mid 41.5%, model 45.9% (projection_v2.0 (prediction ledger)) -- gap +4.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01HUMVAN-2-VAN` Will Botic Van de Zandschulp win set 2 in the Ugo Humbert vs Botic Van de Zandschulp match: 0.13/0.80 mid 46.5%, model 45.9% (projection_v2.0 (prediction ledger)) -- gap -0.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV01HUMVAN-VAN2` Will Botic Van de Zandschulp win at least 1.5 more games than Ugo Humbert?: 0.15/0.57 mid 36.0%, model 36.2% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Austin Krajicek / Nikola Mektic vs Quentin Halys / Pierre-Hugues Herbert -- ATP Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-01T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01KRAMEKHALHER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Quentin Halys / Pierre-Hugues Herbert (`KXATPDOUBLES-26NOV01KRAMEKHALHER-HALHER`) | 0.13 / 0.91 (1) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Austin Krajicek / Nikola Mektic (`KXATPDOUBLES-26NOV01KRAMEKHALHER-KRAMEK`) | 0.07 / 0.79 (2) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Orlando Luz / Rafael Matos vs Matteo Berrettini / Flavio Cobolli -- ATP Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-01T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01LUZMATBERCOB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Berrettini / Flavio Cobolli (`KXATPDOUBLES-26NOV01LUZMATBERCOB-BERCOB`) | 0.07 / 0.93 (30) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Orlando Luz / Rafael Matos (`KXATPDOUBLES-26NOV01LUZMATBERCOB-LUZMAT`) | 0.07 / 0.93 (30) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Daniel Merida vs Alexander Blockx -- ATP Paris R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:210017:210696:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Blockx (`KXATPMATCH-26NOV01MERBLO-BLO`) | 0.58 / 0.59 (2812) | 58.5% | 63.1% | 74.2% | 71.8% [67.8%-73.9%] | -- | -- | -- | -- | PASS | +4.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Daniel Merida (`KXATPMATCH-26NOV01MERBLO-MER`) | 0.40 / 0.41 (35) | 40.5% | 36.9% | 25.8% | 28.2% [26.2%-32.1%] | -- | -- | -- | -- | PASS | -3.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 5577.0, B 5354.0; serve-point win A 62.3%, B 35.1%; Elo A 1772.9, B 1873.8; model uncertainty 0.03
* Form inputs: days since last match A 3, B 22; matches on record A 356, B 247; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.008, surface_dev_loose -0.004, surface_dev_tight +0.008
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV01MERBLO-20` Over 19.5 games: 0.44/0.72 mid 58.0%, model 79.8% (projection_v2.0 (prediction ledger)) -- gap +21.8 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV01MERBLO-MER2` Will Daniel Merida win at least 1.5 more games than Alexander Blockx?: 0.29/0.63 mid 46.0%, model 30.0% (projection_v2.0 (prediction ledger)) -- gap -16.0 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01MERBLO-2-BLO` Will Alexander Blockx win set 2 in the Daniel Merida vs Alexander Blockx match: 0.13/0.80 mid 46.5%, model 58.8% (projection_v2.0 (prediction ledger)) -- gap +12.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV01MERBLO-BLO5` Will Alexander Blockx win at least 4.5 more games than Daniel Merida?: 0.21/0.49 mid 35.0%, model 24.5% (projection_v2.0 (prediction ledger)) -- gap -10.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01MERBLO-MER20` Will Daniel Merida win the Daniel Merida vs Alexander Blockx match by a set score of 2-0?: 0.01/0.52 mid 26.5%, model 17.0% (projection_v2.0 (prediction ledger)) -- gap -9.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV01MERBLO-30` Over 29.5 games: 0.11/0.31 mid 21.0%, model 29.9% (projection_v2.0 (prediction ledger)) -- gap +8.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV01MERBLO-25` Over 24.5 games: 0.43/0.46 mid 44.5%, model 51.9% (projection_v2.0 (prediction ledger)) -- gap +7.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01MERBLO-BLO21` Will Alexander Blockx win the Daniel Merida vs Alexander Blockx match by a set score of 2-1?: 0.01/0.69 mid 35.0%, model 28.5% (projection_v2.0 (prediction ledger)) -- gap -6.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01MERBLO-2-MER` Will Daniel Merida win set 2 in the Daniel Merida vs Alexander Blockx match: 0.13/0.80 mid 46.5%, model 41.2% (projection_v2.0 (prediction ledger)) -- gap -5.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01MERBLO-MER21` Will Daniel Merida win the Daniel Merida vs Alexander Blockx match by a set score of 2-1?: 0.01/0.32 mid 16.5%, model 20.0% (projection_v2.0 (prediction ledger)) -- gap +3.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV01MERBLO-BLO2` Will Alexander Blockx win at least 1.5 more games than Daniel Merida?: 0.53/0.56 mid 54.5%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap +1.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01MERBLO-1-BLO` Will Alexander Blockx win set 1 in the Daniel Merida vs Alexander Blockx match: 0.56/0.59 mid 57.5%, model 58.8% (projection_v2.0 (prediction ledger)) -- gap +1.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01MERBLO-1-MER` Will Daniel Merida win set 1 in the Daniel Merida vs Alexander Blockx match: 0.41/0.44 mid 42.5%, model 41.2% (projection_v2.0 (prediction ledger)) -- gap -1.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01MERBLO-BLO20` Will Alexander Blockx win the Daniel Merida vs Alexander Blockx match by a set score of 2-0?: 0.01/0.68 mid 34.5%, model 34.6% (projection_v2.0 (prediction ledger)) -- gap +0.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alex Michelsen vs Jiri Lehecka -- ATP Paris R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208103:210506:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jiri Lehecka (`KXATPMATCH-26NOV01MICLEH-LEH`) | 0.60 / 0.62 (18) | 61.0% | 54.4% | 55.3% | 55.3% [52.9%-59.2%] | -- | -- | -- | -- | PASS | -6.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alex Michelsen (`KXATPMATCH-26NOV01MICLEH-MIC`) | 0.37 / 0.38 (1482) | 37.5% | 45.6% | 44.7% | 44.7% [40.8%-47.1%] | -- | -- | -- | -- | SHADOW_BET | +8.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5733.0, B 5638.0; serve-point win A 65.8%, B 33.3%; Elo A 1959.7, B 1984.9; model uncertainty 0.0313
* Form inputs: days since last match A 2, B 1; matches on record A 318, B 462; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.024, surface_pool_high +0.024, surface_dev_loose +0.000, surface_dev_tight -0.000
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26NOV01MICLEH-LEH21` Will Jiri Lehecka win the Alex Michelsen vs Jiri Lehecka match by a set score of 2-1?: 0.01/0.72 mid 36.5%, model 26.4% (projection_v2.0 (prediction ledger)) -- gap -10.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01MICLEH-LEH20` Will Jiri Lehecka win the Alex Michelsen vs Jiri Lehecka match by a set score of 2-0?: 0.01/0.72 mid 36.5%, model 28.0% (projection_v2.0 (prediction ledger)) -- gap -8.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01MICLEH-1-LEH` Will Jiri Lehecka win set 1 in the Alex Michelsen vs Jiri Lehecka match: 0.13/0.80 mid 46.5%, model 52.9% (projection_v2.0 (prediction ledger)) -- gap +6.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01MICLEH-2-LEH` Will Jiri Lehecka win set 2 in the Alex Michelsen vs Jiri Lehecka match: 0.13/0.80 mid 46.5%, model 52.9% (projection_v2.0 (prediction ledger)) -- gap +6.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01MICLEH-MIC20` Will Alex Michelsen win the Alex Michelsen vs Jiri Lehecka match by a set score of 2-0?: 0.01/0.47 mid 24.0%, model 22.2% (projection_v2.0 (prediction ledger)) -- gap -1.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01MICLEH-1-MIC` Will Alex Michelsen win set 1 in the Alex Michelsen vs Jiri Lehecka match: 0.13/0.80 mid 46.5%, model 47.1% (projection_v2.0 (prediction ledger)) -- gap +0.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01MICLEH-2-MIC` Will Alex Michelsen win set 2 in the Alex Michelsen vs Jiri Lehecka match: 0.13/0.80 mid 46.5%, model 47.1% (projection_v2.0 (prediction ledger)) -- gap +0.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01MICLEH-MIC21` Will Alex Michelsen win the Alex Michelsen vs Jiri Lehecka match by a set score of 2-1?: 0.01/0.47 mid 24.0%, model 23.5% (projection_v2.0 (prediction ledger)) -- gap -0.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lucas Miedler / Neil Oberleitner vs Marcelo Melo / Alexander Zverev -- ATP Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-01T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01MIEOBEMELZVE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcelo Melo / Alexander Zverev (`KXATPDOUBLES-26NOV01MIEOBEMELZVE-MELZVE`) | 0.06 / 0.68 (1) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lucas Miedler / Neil Oberleitner (`KXATPDOUBLES-26NOV01MIEOBEMELZVE-MIEOBE`) | 0.27 / 0.94 (4) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lorenzo Musetti vs Hubert Hurkacz -- ATP Paris R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:128034:207518:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hubert Hurkacz (`KXATPMATCH-26NOV01MUSHUR-HUR`) | 0.51 / 0.52 (1174) | 51.5% | 50.0% | 49.0% | 51.0% [48.5%-52.4%] | -- | -- | -- | -- | PASS | -1.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lorenzo Musetti (`KXATPMATCH-26NOV01MUSHUR-MUS`) | 0.49 / 0.50 (18979) | 49.5% | 50.0% | 51.0% | 49.0% [47.6%-51.4%] | -- | -- | -- | -- | PASS | +0.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5110.0, B 5432.0; serve-point win A 67.1%, B 32.9%; Elo A 1949.1, B 1990.4; model uncertainty 0.0193
* Form inputs: days since last match A 2, B 3; matches on record A 490, B 691; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.014, surface_dev_loose +0.005, surface_dev_tight -0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV01MUSHUR-20` Over 19.5 games: 0.56/0.77 mid 66.5%, model 86.0% (projection_v2.0 (prediction ledger)) -- gap +19.5 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01MUSHUR-30` Over 29.5 games: 0.06/0.34 mid 20.0%, model 36.6% (projection_v2.0 (prediction ledger)) -- gap +16.6 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01MUSHUR-HUR5` Will Hubert Hurkacz win at least 4.5 more games than Lorenzo Musetti?: 0.13/0.37 mid 25.0%, model 12.6% (projection_v2.0 (prediction ledger)) -- gap -12.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01MUSHUR-HUR21` Will Hubert Hurkacz win the Lorenzo Musetti vs Hubert Hurkacz match by a set score of 2-1?: 0.01/0.27 mid 14.0%, model 25.0% (projection_v2.0 (prediction ledger)) -- gap +11.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01MUSHUR-MUS20` Will Lorenzo Musetti win the Lorenzo Musetti vs Hubert Hurkacz match by a set score of 2-0?: 0.01/0.34 mid 17.5%, model 25.0% (projection_v2.0 (prediction ledger)) -- gap +7.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01MUSHUR-HUR20` Will Hubert Hurkacz win the Lorenzo Musetti vs Hubert Hurkacz match by a set score of 2-0?: 0.01/0.36 mid 18.5%, model 25.0% (projection_v2.0 (prediction ledger)) -- gap +6.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01MUSHUR-25` Over 24.5 games: 0.49/0.52 mid 50.5%, model 56.7% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01MUSHUR-MUS2` Will Lorenzo Musetti win at least 1.5 more games than Hubert Hurkacz?: 0.26/0.46 mid 36.0%, model 41.7% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01MUSHUR-HUR2` Will Hubert Hurkacz win at least 1.5 more games than Lorenzo Musetti?: 0.44/0.47 mid 45.5%, model 41.7% (projection_v2.0 (prediction ledger)) -- gap -3.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01MUSHUR-2-HUR` Will Hubert Hurkacz win set 2 in the Lorenzo Musetti vs Hubert Hurkacz match: 0.13/0.80 mid 46.5%, model 50.0% (projection_v2.0 (prediction ledger)) -- gap +3.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01MUSHUR-2-MUS` Will Lorenzo Musetti win set 2 in the Lorenzo Musetti vs Hubert Hurkacz match: 0.13/0.80 mid 46.5%, model 50.0% (projection_v2.0 (prediction ledger)) -- gap +3.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01MUSHUR-1-HUR` Will Hubert Hurkacz win set 1 in the Lorenzo Musetti vs Hubert Hurkacz match: 0.50/0.53 mid 51.5%, model 50.0% (projection_v2.0 (prediction ledger)) -- gap -1.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01MUSHUR-1-MUS` Will Lorenzo Musetti win set 1 in the Lorenzo Musetti vs Hubert Hurkacz match: 0.47/0.50 mid 48.5%, model 50.0% (projection_v2.0 (prediction ledger)) -- gap +1.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01MUSHUR-MUS21` Will Lorenzo Musetti win the Lorenzo Musetti vs Hubert Hurkacz match by a set score of 2-1?: 0.13/0.39 mid 26.0%, model 25.0% (projection_v2.0 (prediction ledger)) -- gap -1.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Brandon Nakashima vs Matteo Berrettini -- ATP Paris R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126610:206909:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Berrettini (`KXATPMATCH-26NOV01NAKBER-BER`) | 0.41 / 0.43 (19612) | 42.0% | 40.9% | 44.0% | 44.5% [39.1%-51.9%] | -- | -- | -- | -- | PASS | -1.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Brandon Nakashima (`KXATPMATCH-26NOV01NAKBER-NAK`) | 0.57 / 0.59 (15052) | 58.0% | 59.1% | 56.0% | 55.5% [48.1%-60.9%] | -- | -- | -- | -- | PASS | +1.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6149.0, B 4151.0; serve-point win A 71.9%, B 30.1%; Elo A 1944.6, B 1907.9; model uncertainty 0.0638
* Form inputs: days since last match A 3, B 1; matches on record A 472, B 565; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.046, surface_pool_high +0.054, surface_dev_loose +0.009, surface_dev_tight +0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV01NAKBER-21` Over 20.5 games: 0.55/0.94 mid 74.5%, model 85.3% (projection_v2.0 (prediction ledger)) -- gap +10.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01NAKBER-NAK20` Will Brandon Nakashima win the Brandon Nakashima vs Matteo Berrettini match by a set score of 2-0?: 0.01/0.41 mid 21.0%, model 31.5% (projection_v2.0 (prediction ledger)) -- gap +10.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01NAKBER-2-NAK` Will Brandon Nakashima win set 2 in the Brandon Nakashima vs Matteo Berrettini match: 0.13/0.80 mid 46.5%, model 56.1% (projection_v2.0 (prediction ledger)) -- gap +9.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01NAKBER-BER21` Will Matteo Berrettini win the Brandon Nakashima vs Matteo Berrettini match by a set score of 2-1?: 0.01/0.25 mid 13.0%, model 21.6% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01NAKBER-26` Over 25.5 games: 0.48/0.51 mid 49.5%, model 57.2% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01NAKBER-31` Over 30.5 games: 0.09/0.56 mid 32.5%, model 39.2% (projection_v2.0 (prediction ledger)) -- gap +6.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01NAKBER-NAK3` Will Brandon Nakashima win at least 2.5 more games than Matteo Berrettini?: 0.41/0.44 mid 42.5%, model 37.4% (projection_v2.0 (prediction ledger)) -- gap -5.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01NAKBER-BER20` Will Matteo Berrettini win the Brandon Nakashima vs Matteo Berrettini match by a set score of 2-0?: 0.01/0.29 mid 15.0%, model 19.3% (projection_v2.0 (prediction ledger)) -- gap +4.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01NAKBER-2-BER` Will Matteo Berrettini win set 2 in the Brandon Nakashima vs Matteo Berrettini match: 0.13/0.80 mid 46.5%, model 43.9% (projection_v2.0 (prediction ledger)) -- gap -2.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01NAKBER-1-NAK` Will Brandon Nakashima win set 1 in the Brandon Nakashima vs Matteo Berrettini match: 0.56/0.59 mid 57.5%, model 56.1% (projection_v2.0 (prediction ledger)) -- gap -1.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV01NAKBER-BER2` Will Matteo Berrettini win at least 1.5 more games than Brandon Nakashima?: 0.06/0.60 mid 33.0%, model 31.7% (projection_v2.0 (prediction ledger)) -- gap -1.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01NAKBER-1-BER` Will Matteo Berrettini win set 1 in the Brandon Nakashima vs Matteo Berrettini match: 0.42/0.44 mid 43.0%, model 43.9% (projection_v2.0 (prediction ledger)) -- gap +0.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01NAKBER-NAK21` Will Brandon Nakashima win the Brandon Nakashima vs Matteo Berrettini match by a set score of 2-1?: 0.17/0.39 mid 28.0%, model 27.6% (projection_v2.0 (prediction ledger)) -- gap -0.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Cameron Norrie vs Matteo Arnaldi -- ATP Paris R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111815:208286:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Arnaldi (`KXATPMATCH-26NOV01NORARN-ARN`) | 0.32 / 0.33 (2705) | 32.5% | 37.3% | 38.0% | 38.0% [37.1%-39.5%] | -- | -- | -- | -- | PASS | +4.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Cameron Norrie (`KXATPMATCH-26NOV01NORARN-NOR`) | 0.67 / 0.68 (1503) | 67.5% | 62.7% | 62.0% | 62.0% [60.5%-62.9%] | -- | -- | -- | -- | PASS | -4.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5400.0, B 4906.0; serve-point win A 63.7%, B 38.9%; Elo A 1888.0, B 1790.2; model uncertainty 0.0121
* Form inputs: days since last match A 2, B 5; matches on record A 679, B 400; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight +0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26NOV01NORARN-NOR21` Will Cameron Norrie win the Cameron Norrie vs Matteo Arnaldi match by a set score of 2-1?: 0.01/0.29 mid 15.0%, model 28.4% (projection_v2.0 (prediction ledger)) -- gap +13.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01NORARN-19` Over 18.5 games: 0.53/0.93 mid 73.0%, model 85.8% (projection_v2.0 (prediction ledger)) -- gap +12.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01NORARN-2-NOR` Will Cameron Norrie win set 2 in the Cameron Norrie vs Matteo Arnaldi match: 0.13/0.80 mid 46.5%, model 58.6% (projection_v2.0 (prediction ledger)) -- gap +12.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01NORARN-ARN21` Will Matteo Arnaldi win the Cameron Norrie vs Matteo Arnaldi match by a set score of 2-1?: 0.01/0.21 mid 11.0%, model 20.1% (projection_v2.0 (prediction ledger)) -- gap +9.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01NORARN-24` Over 23.5 games: 0.42/0.45 mid 43.5%, model 52.6% (projection_v2.0 (prediction ledger)) -- gap +9.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01NORARN-NOR20` Will Cameron Norrie win the Cameron Norrie vs Matteo Arnaldi match by a set score of 2-0?: 0.01/0.50 mid 25.5%, model 34.3% (projection_v2.0 (prediction ledger)) -- gap +8.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01NORARN-NOR2` Will Cameron Norrie win at least 1.5 more games than Matteo Arnaldi?: 0.49/0.76 mid 62.5%, model 55.7% (projection_v2.0 (prediction ledger)) -- gap -6.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01NORARN-NOR5` Will Cameron Norrie win at least 4.5 more games than Matteo Arnaldi?: 0.31/0.34 mid 32.5%, model 25.8% (projection_v2.0 (prediction ledger)) -- gap -6.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01NORARN-2-ARN` Will Matteo Arnaldi win set 2 in the Cameron Norrie vs Matteo Arnaldi match: 0.13/0.80 mid 46.5%, model 41.4% (projection_v2.0 (prediction ledger)) -- gap -5.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV01NORARN-29` Over 28.5 games: 0.02/0.55 mid 28.5%, model 33.5% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01NORARN-1-ARN` Will Matteo Arnaldi win set 1 in the Cameron Norrie vs Matteo Arnaldi match: 0.35/0.38 mid 36.5%, model 41.4% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01NORARN-1-NOR` Will Cameron Norrie win set 1 in the Cameron Norrie vs Matteo Arnaldi match: 0.62/0.65 mid 63.5%, model 58.6% (projection_v2.0 (prediction ledger)) -- gap -4.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01NORARN-ARN20` Will Matteo Arnaldi win the Cameron Norrie vs Matteo Arnaldi match by a set score of 2-0?: 0.01/0.24 mid 12.5%, model 17.2% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01NORARN-ARN2` Will Matteo Arnaldi win at least 1.5 more games than Cameron Norrie?: 0.16/0.54 mid 35.0%, model 30.5% (projection_v2.0 (prediction ledger)) -- gap -4.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Francisco Cabral / James Tracy (`KXATPDOUBLES-26NOV01NOUVENCABTRA-CABTRA`) | 0.06 / 0.93 (10) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Petr Nouza / Michael Venus (`KXATPDOUBLES-26NOV01NOUVENCABTRA-NOUVEN`) | 0.06 / 0.93 (10) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Hugo Nys / Edouard Roger-Vasselin vs Sadio Doumbia / David Pel -- ATP Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-01T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01NYSROGDOUPEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sadio Doumbia / David Pel (`KXATPDOUBLES-26NOV01NYSROGDOUPEL-DOUPEL`) | 0.05 / 0.78 (2) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hugo Nys / Edouard Roger-Vasselin (`KXATPDOUBLES-26NOV01NYSROGDOUPEL-NYSROG`) | 0.16 / 0.94 (2) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tommy Paul vs Holger Rune -- ATP Paris R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126205:208029:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tommy Paul (`KXATPMATCH-26NOV01PAURUN-PAU`) | 0.65 / 0.66 (16980) | 65.5% | 65.6% | 64.5% | 63.6% [61.7%-64.6%] | -- | -- | -- | -- | PASS | +0.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Holger Rune (`KXATPMATCH-26NOV01PAURUN-RUN`) | 0.33 / 0.35 (1363) | 34.0% | 34.4% | 35.5% | 36.4% [35.4%-38.3%] | -- | -- | -- | -- | PASS | +0.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6095.0, B 3079.0; serve-point win A 66.1%, B 37.1%; Elo A 2033.3, B 1965.0; model uncertainty 0.0143
* Form inputs: days since last match A 1, B 1; matches on record A 732, B 448; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.019, surface_dev_loose -0.009, surface_dev_tight +0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV01PAURUN-18` Over 17.5 games: 0.62/0.96 mid 79.0%, model 93.2% (projection_v2.0 (prediction ledger)) -- gap +14.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01PAURUN-2-PAU` Will Tommy Paul win set 2 in the Tommy Paul vs Holger Rune match: 0.13/0.80 mid 46.5%, model 60.5% (projection_v2.0 (prediction ledger)) -- gap +14.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01PAURUN-PAU21` Will Tommy Paul win the Tommy Paul vs Holger Rune match by a set score of 2-1?: 0.01/0.29 mid 15.0%, model 28.9% (projection_v2.0 (prediction ledger)) -- gap +13.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01PAURUN-PAU7` Will Tommy Paul win at least 6.5 more games than Holger Rune?: 0.01/0.39 mid 20.0%, model 6.8% (projection_v2.0 (prediction ledger)) -- gap -13.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01PAURUN-PAU20` Will Tommy Paul win the Tommy Paul vs Holger Rune match by a set score of 2-0?: 0.01/0.48 mid 24.5%, model 36.6% (projection_v2.0 (prediction ledger)) -- gap +12.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01PAURUN-23` Over 22.5 games: 0.49/0.51 mid 50.0%, model 59.7% (projection_v2.0 (prediction ledger)) -- gap +9.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01PAURUN-RUN21` Will Holger Rune win the Tommy Paul vs Holger Rune match by a set score of 2-1?: 0.01/0.22 mid 11.5%, model 18.9% (projection_v2.0 (prediction ledger)) -- gap +7.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01PAURUN-2-RUN` Will Holger Rune win set 2 in the Tommy Paul vs Holger Rune match: 0.13/0.80 mid 46.5%, model 39.5% (projection_v2.0 (prediction ledger)) -- gap -7.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV01PAURUN-28` Over 27.5 games: 0.08/0.61 mid 34.5%, model 39.6% (projection_v2.0 (prediction ledger)) -- gap +5.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01PAURUN-PAU4` Will Tommy Paul win at least 3.5 more games than Holger Rune?: 0.42/0.45 mid 43.5%, model 38.6% (projection_v2.0 (prediction ledger)) -- gap -4.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01PAURUN-RUN20` Will Holger Rune win the Tommy Paul vs Holger Rune match by a set score of 2-0?: 0.01/0.25 mid 13.0%, model 15.6% (projection_v2.0 (prediction ledger)) -- gap +2.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01PAURUN-RUN2` Will Holger Rune win at least 1.5 more games than Tommy Paul?: 0.01/0.50 mid 25.5%, model 27.6% (projection_v2.0 (prediction ledger)) -- gap +2.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01PAURUN-1-RUN` Will Holger Rune win set 1 in the Tommy Paul vs Holger Rune match: 0.36/0.39 mid 37.5%, model 39.5% (projection_v2.0 (prediction ledger)) -- gap +2.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01PAURUN-1-PAU` Will Tommy Paul win set 1 in the Tommy Paul vs Holger Rune match: 0.61/0.63 mid 62.0%, model 60.5% (projection_v2.0 (prediction ledger)) -- gap -1.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Arthur Rinderknech vs Francisco Cerundolo -- ATP Paris R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126239:202103:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francisco Cerundolo (`KXATPMATCH-26NOV01RINCER-CER`) | 0.67 / 0.68 (3129) | 67.5% | 63.9% | 62.5% | 61.1% [59.2%-63.5%] | -- | -- | -- | -- | PASS | -3.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Arthur Rinderknech (`KXATPMATCH-26NOV01RINCER-RIN`) | 0.32 / 0.33 (24643) | 32.5% | 36.1% | 37.5% | 38.9% [36.5%-40.8%] | -- | -- | -- | -- | PASS | +3.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5909.0, B 5818.0; serve-point win A 64.2%, B 32.9%; Elo A 1826.0, B 1868.6; model uncertainty 0.0213
* Form inputs: days since last match A 4, B 4; matches on record A 569, B 564; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.019, surface_dev_loose -0.004, surface_dev_tight -0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV01RINCER-18` Over 17.5 games: 0.66/0.96 mid 81.0%, model 94.5% (projection_v2.0 (prediction ledger)) -- gap +13.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01RINCER-CER21` Will Francisco Cerundolo win the Arthur Rinderknech vs Francisco Cerundolo match by a set score of 2-1?: 0.01/0.30 mid 15.5%, model 28.6% (projection_v2.0 (prediction ledger)) -- gap +13.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01RINCER-2-CER` Will Francisco Cerundolo win set 2 in the Arthur Rinderknech vs Francisco Cerundolo match: 0.13/0.80 mid 46.5%, model 59.4% (projection_v2.0 (prediction ledger)) -- gap +12.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV01RINCER-28` Over 27.5 games: 0.12/0.48 mid 30.0%, model 41.3% (projection_v2.0 (prediction ledger)) -- gap +11.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01RINCER-CER20` Will Francisco Cerundolo win the Arthur Rinderknech vs Francisco Cerundolo match by a set score of 2-0?: 0.01/0.48 mid 24.5%, model 35.3% (projection_v2.0 (prediction ledger)) -- gap +10.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01RINCER-23` Over 22.5 games: 0.51/0.54 mid 52.5%, model 61.7% (projection_v2.0 (prediction ledger)) -- gap +9.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01RINCER-CER4` Will Francisco Cerundolo win at least 3.5 more games than Arthur Rinderknech?: 0.43/0.46 mid 44.5%, model 35.6% (projection_v2.0 (prediction ledger)) -- gap -8.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01RINCER-RIN21` Will Arthur Rinderknech win the Arthur Rinderknech vs Francisco Cerundolo match by a set score of 2-1?: 0.09/0.42 mid 25.5%, model 19.6% (projection_v2.0 (prediction ledger)) -- gap -5.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01RINCER-2-RIN` Will Arthur Rinderknech win set 2 in the Arthur Rinderknech vs Francisco Cerundolo match: 0.13/0.80 mid 46.5%, model 40.6% (projection_v2.0 (prediction ledger)) -- gap -5.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01RINCER-1-CER` Will Francisco Cerundolo win set 1 in the Arthur Rinderknech vs Francisco Cerundolo match: 0.62/0.65 mid 63.5%, model 59.4% (projection_v2.0 (prediction ledger)) -- gap -4.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01RINCER-1-RIN` Will Arthur Rinderknech win set 1 in the Arthur Rinderknech vs Francisco Cerundolo match: 0.35/0.38 mid 36.5%, model 40.6% (projection_v2.0 (prediction ledger)) -- gap +4.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV01RINCER-RIN2` Will Arthur Rinderknech win at least 1.5 more games than Francisco Cerundolo?: 0.01/0.49 mid 25.0%, model 28.9% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01RINCER-RIN20` Will Arthur Rinderknech win the Arthur Rinderknech vs Francisco Cerundolo match by a set score of 2-0?: 0.01/0.27 mid 14.0%, model 16.5% (projection_v2.0 (prediction ledger)) -- gap +2.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Andrey Rublev vs Tomas Martin Etcheverry -- ATP Paris R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126094:144869:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tomas Martin Etcheverry (`KXATPMATCH-26NOV01RUBETC-ETC`) | 0.30 / 0.32 (18030) | 31.0% | 31.0% | 35.9% | 33.7% [31.4%-34.6%] | -- | -- | -- | -- | PASS | -0.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Andrey Rublev (`KXATPMATCH-26NOV01RUBETC-RUB`) | 0.68 / 0.69 (248) | 68.5% | 69.0% | 64.1% | 66.3% [65.4%-68.5%] | -- | -- | -- | -- | PASS | +0.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5940.0, B 5595.0; serve-point win A 69.4%, B 34.8%; Elo A 1947.6, B 1768.9; model uncertainty 0.0157
* Form inputs: days since last match A 4, B 5; matches on record A 836, B 649; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.004, surface_dev_loose -0.001, surface_dev_tight +0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPSETWINNER-26NOV01RUBETC-2-RUB` Will Andrey Rublev win set 2 in the Andrey Rublev vs Tomas Martin Etcheverry match: 0.13/0.80 mid 46.5%, model 63.0% (projection_v2.0 (prediction ledger)) -- gap +16.5 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV01RUBETC-18` Over 17.5 games: 0.64/0.96 mid 80.0%, model 95.2% (projection_v2.0 (prediction ledger)) -- gap +15.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01RUBETC-RUB21` Will Andrey Rublev win the Andrey Rublev vs Tomas Martin Etcheverry match by a set score of 2-1?: 0.01/0.30 mid 15.5%, model 29.4% (projection_v2.0 (prediction ledger)) -- gap +13.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01RUBETC-RUB7` Will Andrey Rublev win at least 6.5 more games than Tomas Martin Etcheverry?: 0.01/0.37 mid 19.0%, model 5.1% (projection_v2.0 (prediction ledger)) -- gap -13.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01RUBETC-RUB20` Will Andrey Rublev win the Andrey Rublev vs Tomas Martin Etcheverry match by a set score of 2-0?: 0.01/0.51 mid 26.0%, model 39.6% (projection_v2.0 (prediction ledger)) -- gap +13.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01RUBETC-ETC20` Will Tomas Martin Etcheverry win the Andrey Rublev vs Tomas Martin Etcheverry match by a set score of 2-0?: 0.12/0.38 mid 25.0%, model 13.7% (projection_v2.0 (prediction ledger)) -- gap -11.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01RUBETC-23` Over 22.5 games: 0.51/0.54 mid 52.5%, model 62.2% (projection_v2.0 (prediction ledger)) -- gap +9.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01RUBETC-2-ETC` Will Tomas Martin Etcheverry win set 2 in the Andrey Rublev vs Tomas Martin Etcheverry match: 0.13/0.80 mid 46.5%, model 37.0% (projection_v2.0 (prediction ledger)) -- gap -9.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV01RUBETC-RUB4` Will Andrey Rublev win at least 3.5 more games than Tomas Martin Etcheverry?: 0.43/0.46 mid 44.5%, model 37.9% (projection_v2.0 (prediction ledger)) -- gap -6.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01RUBETC-1-ETC` Will Tomas Martin Etcheverry win set 1 in the Andrey Rublev vs Tomas Martin Etcheverry match: 0.33/0.36 mid 34.5%, model 37.0% (projection_v2.0 (prediction ledger)) -- gap +2.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01RUBETC-1-RUB` Will Andrey Rublev win set 1 in the Andrey Rublev vs Tomas Martin Etcheverry match: 0.64/0.67 mid 65.5%, model 63.0% (projection_v2.0 (prediction ledger)) -- gap -2.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01RUBETC-ETC21` Will Tomas Martin Etcheverry win the Andrey Rublev vs Tomas Martin Etcheverry match by a set score of 2-1?: 0.01/0.38 mid 19.5%, model 17.3% (projection_v2.0 (prediction ledger)) -- gap -2.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01RUBETC-28` Over 27.5 games: 0.23/0.64 mid 43.5%, model 41.3% (projection_v2.0 (prediction ledger)) -- gap -2.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01RUBETC-ETC2` Will Tomas Martin Etcheverry win at least 1.5 more games than Andrey Rublev?: 0.01/0.50 mid 25.5%, model 23.9% (projection_v2.0 (prediction ledger)) -- gap -1.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Denis Shapovalov vs Karen Khachanov -- ATP Paris R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111575:133430:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karen Khachanov (`KXATPMATCH-26NOV01SHAKHA-KHA`) | 0.60 / 0.61 (4519) | 60.5% | 59.6% | 61.2% | 58.8% [56.9%-59.7%] | -- | -- | -- | -- | PASS | -0.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Denis Shapovalov (`KXATPMATCH-26NOV01SHAKHA-SHA`) | 0.38 / 0.39 (263) | 38.5% | 40.4% | 38.8% | 41.2% [40.3%-43.1%] | -- | -- | -- | -- | PASS | +1.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4653.0, B 5835.0; serve-point win A 64.1%, B 33.9%; Elo A 1932.3, B 1936.1; model uncertainty 0.0144
* Form inputs: days since last match A 2, B 4; matches on record A 582, B 765; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.014, surface_dev_loose +0.005, surface_dev_tight -0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV01SHAKHA-18` Over 17.5 games: 0.66/0.96 mid 81.0%, model 94.5% (projection_v2.0 (prediction ledger)) -- gap +13.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01SHAKHA-KHA21` Will Karen Khachanov win the Denis Shapovalov vs Karen Khachanov match by a set score of 2-1?: 0.01/0.29 mid 15.0%, model 27.8% (projection_v2.0 (prediction ledger)) -- gap +12.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01SHAKHA-KHA6` Will Karen Khachanov win at least 5.5 more games than Denis Shapovalov?: 0.01/0.40 mid 20.5%, model 10.5% (projection_v2.0 (prediction ledger)) -- gap -10.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01SHAKHA-2-KHA` Will Karen Khachanov win set 2 in the Denis Shapovalov vs Karen Khachanov match: 0.13/0.80 mid 46.5%, model 56.4% (projection_v2.0 (prediction ledger)) -- gap +9.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01SHAKHA-SHA21` Will Denis Shapovalov win the Denis Shapovalov vs Karen Khachanov match by a set score of 2-1?: 0.01/0.23 mid 12.0%, model 21.4% (projection_v2.0 (prediction ledger)) -- gap +9.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01SHAKHA-KHA20` Will Karen Khachanov win the Denis Shapovalov vs Karen Khachanov match by a set score of 2-0?: 0.01/0.44 mid 22.5%, model 31.9% (projection_v2.0 (prediction ledger)) -- gap +9.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01SHAKHA-23` Over 22.5 games: 0.55/0.57 mid 56.0%, model 62.0% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01SHAKHA-SHA20` Will Denis Shapovalov win the Denis Shapovalov vs Karen Khachanov match by a set score of 2-0?: 0.01/0.27 mid 14.0%, model 19.0% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01SHAKHA-28` Over 27.5 games: 0.26/0.48 mid 37.0%, model 41.6% (projection_v2.0 (prediction ledger)) -- gap +4.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01SHAKHA-2-SHA` Will Denis Shapovalov win set 2 in the Denis Shapovalov vs Karen Khachanov match: 0.13/0.80 mid 46.5%, model 43.6% (projection_v2.0 (prediction ledger)) -- gap -2.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV01SHAKHA-KHA3` Will Karen Khachanov win at least 2.5 more games than Denis Shapovalov?: 0.45/0.47 mid 46.0%, model 43.7% (projection_v2.0 (prediction ledger)) -- gap -2.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01SHAKHA-SHA2` Will Denis Shapovalov win at least 1.5 more games than Karen Khachanov?: 0.08/0.62 mid 35.0%, model 33.0% (projection_v2.0 (prediction ledger)) -- gap -2.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01SHAKHA-1-KHA` Will Karen Khachanov win set 1 in the Denis Shapovalov vs Karen Khachanov match: 0.56/0.59 mid 57.5%, model 56.4% (projection_v2.0 (prediction ledger)) -- gap -1.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01SHAKHA-1-SHA` Will Denis Shapovalov win set 1 in the Denis Shapovalov vs Karen Khachanov match: 0.41/0.44 mid 42.5%, model 43.6% (projection_v2.0 (prediction ledger)) -- gap +1.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jan-Lennard Struff vs Arthur Gea -- ATP Paris R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105526:210338:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arthur Gea (`KXATPMATCH-26NOV01STRGEA-GEA`) | 0.42 / 0.56 (1) | 49.0% | 68.6% | 69.1% | 66.8% [58.4%-69.9%] | -- | -- | -- | -- | PASS | +19.6 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jan-Lennard Struff (`KXATPMATCH-26NOV01STRGEA-STR`) | 0.38 / 0.65 (12) | 51.5% | 31.4% | 30.9% | 33.2% [30.1%-41.6%] | -- | -- | -- | -- | PASS | -20.1 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5412.0, B 5382.0; serve-point win A 62.4%, B 33.7%; Elo A 1827.8, B 1875.7; model uncertainty 0.0576
* Form inputs: days since last match A 1, B 16; matches on record A 1074, B 269; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26NOV01STRGEA-GEA  (YES = Arthur Gea)
Model: 69%
Kalshi: 49%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.037, surface_pool_high -0.031, surface_dev_loose -0.026, surface_dev_tight +0.036
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26NOV01STRGEA-1-GEA` Will Arthur Gea win set 1 in the Jan-Lennard Struff vs Arthur Gea match: 0.13/0.80 mid 46.5%, model 62.7% (projection_v2.0 (prediction ledger)) -- gap +16.2 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01STRGEA-2-GEA` Will Arthur Gea win set 2 in the Jan-Lennard Struff vs Arthur Gea match: 0.13/0.80 mid 46.5%, model 62.7% (projection_v2.0 (prediction ledger)) -- gap +16.2 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01STRGEA-1-STR` Will Jan-Lennard Struff win set 1 in the Jan-Lennard Struff vs Arthur Gea match: 0.13/0.80 mid 46.5%, model 37.3% (projection_v2.0 (prediction ledger)) -- gap -9.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01STRGEA-2-STR` Will Jan-Lennard Struff win set 2 in the Jan-Lennard Struff vs Arthur Gea match: 0.13/0.80 mid 46.5%, model 37.3% (projection_v2.0 (prediction ledger)) -- gap -9.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alejandro Tabilo vs Rafael Jodar -- ATP Paris R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126214:212588:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rafael Jodar (`KXATPMATCH-26NOV01TABJOD-JOD`) | 0.78 / 0.79 (1125) | 78.5% | 73.4% | 70.9% | 71.8% [70.1%-72.2%] | -- | -- | -- | -- | PASS | -5.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alejandro Tabilo (`KXATPMATCH-26NOV01TABJOD-TAB`) | 0.20 / 0.22 (1839) | 21.0% | 26.6% | 29.1% | 28.2% [27.8%-29.9%] | -- | -- | -- | -- | SHADOW_BET | +5.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6132.0, B 5268.0; serve-point win A 61.2%, B 33.8%; Elo A 1836.1, B 2015.9; model uncertainty 0.0105
* Form inputs: days since last match A 4, B 2; matches on record A 655, B 142; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.004, surface_dev_loose -0.004, surface_dev_tight +0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPSETWINNER-26NOV01TABJOD-2-JOD` Will Rafael Jodar win set 2 in the Alejandro Tabilo vs Rafael Jodar match: 0.13/0.80 mid 46.5%, model 66.1% (projection_v2.0 (prediction ledger)) -- gap +19.6 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01TABJOD-JOD21` Will Rafael Jodar win the Alejandro Tabilo vs Rafael Jodar match by a set score of 2-1?: 0.01/0.29 mid 15.0%, model 29.6% (projection_v2.0 (prediction ledger)) -- gap +14.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01TABJOD-JOD8` Will Rafael Jodar win at least 7.5 more games than Alejandro Tabilo?: 0.01/0.35 mid 18.0%, model 4.2% (projection_v2.0 (prediction ledger)) -- gap -13.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01TABJOD-22` Over 21.5 games: 0.49/0.52 mid 50.5%, model 63.6% (projection_v2.0 (prediction ledger)) -- gap +13.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01TABJOD-JOD5` Will Rafael Jodar win at least 4.5 more games than Alejandro Tabilo?: 0.44/0.47 mid 45.5%, model 32.7% (projection_v2.0 (prediction ledger)) -- gap -12.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01TABJOD-2-TAB` Will Alejandro Tabilo win set 2 in the Alejandro Tabilo vs Rafael Jodar match: 0.13/0.80 mid 46.5%, model 33.9% (projection_v2.0 (prediction ledger)) -- gap -12.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01TABJOD-JOD20` Will Rafael Jodar win the Alejandro Tabilo vs Rafael Jodar match by a set score of 2-0?: 0.01/0.63 mid 32.0%, model 43.8% (projection_v2.0 (prediction ledger)) -- gap +11.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01TABJOD-27` Over 26.5 games: 0.26/0.40 mid 33.0%, model 39.5% (projection_v2.0 (prediction ledger)) -- gap +6.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01TABJOD-JOD2` Will Rafael Jodar win at least 1.5 more games than Alejandro Tabilo?: 0.67/0.77 mid 72.0%, model 67.0% (projection_v2.0 (prediction ledger)) -- gap -5.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01TABJOD-1-JOD` Will Rafael Jodar win set 1 in the Alejandro Tabilo vs Rafael Jodar match: 0.70/0.72 mid 71.0%, model 66.1% (projection_v2.0 (prediction ledger)) -- gap -4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01TABJOD-1-TAB` Will Alejandro Tabilo win set 1 in the Alejandro Tabilo vs Rafael Jodar match: 0.28/0.31 mid 29.5%, model 33.9% (projection_v2.0 (prediction ledger)) -- gap +4.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV01TABJOD-17` Over 16.5 games: 0.86/0.98 mid 92.0%, model 96.0% (projection_v2.0 (prediction ledger)) -- gap +4.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01TABJOD-TAB21` Will Alejandro Tabilo win the Alejandro Tabilo vs Rafael Jodar match by a set score of 2-1?: 0.04/0.32 mid 18.0%, model 15.2% (projection_v2.0 (prediction ledger)) -- gap -2.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01TABJOD-TAB20` Will Alejandro Tabilo win the Alejandro Tabilo vs Rafael Jodar match by a set score of 2-0?: 0.01/0.22 mid 11.5%, model 11.5% (projection_v2.0 (prediction ledger)) -- gap -0.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Stefanos Tsitsipas vs Learner Tien -- ATP Paris R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126774:210530:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Learner Tien (`KXATPMATCH-26NOV01TSITIE-TIE`) | 0.54 / 0.56 (18785) | 55.0% | 48.7% | 50.5% | 52.0% [45.6%-55.9%] | -- | -- | -- | -- | PASS | -6.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Stefanos Tsitsipas (`KXATPMATCH-26NOV01TSITIE-TSI`) | 0.44 / 0.46 (17038) | 45.0% | 51.3% | 49.5% | 48.0% [44.1%-54.4%] | -- | -- | -- | -- | WATCH | +6.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5658.0, B 5484.0; serve-point win A 65.7%, B 34.6%; Elo A 1938.2, B 1985.8; model uncertainty 0.0513
* Form inputs: days since last match A 7, B 3; matches on record A 812, B 251; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.044, surface_pool_high -0.039, surface_dev_loose -0.010, surface_dev_tight +0.010
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26NOV01TSITIE-TIE5` Will Learner Tien win at least 4.5 more games than Stefanos Tsitsipas?: 0.19/0.43 mid 31.0%, model 13.8% (projection_v2.0 (prediction ledger)) -- gap -17.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01TSITIE-19` Over 18.5 games: 0.59/0.94 mid 76.5%, model 90.7% (projection_v2.0 (prediction ledger)) -- gap +14.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01TSITIE-TSI21` Will Stefanos Tsitsipas win the Stefanos Tsitsipas vs Learner Tien match by a set score of 2-1?: 0.01/0.25 mid 13.0%, model 25.4% (projection_v2.0 (prediction ledger)) -- gap +12.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01TSITIE-TIE21` Will Learner Tien win the Stefanos Tsitsipas vs Learner Tien match by a set score of 2-1?: 0.01/0.28 mid 14.5%, model 24.6% (projection_v2.0 (prediction ledger)) -- gap +10.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01TSITIE-TSI20` Will Stefanos Tsitsipas win the Stefanos Tsitsipas vs Learner Tien match by a set score of 2-0?: 0.01/0.31 mid 16.0%, model 25.9% (projection_v2.0 (prediction ledger)) -- gap +9.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01TSITIE-24` Over 23.5 games: 0.46/0.50 mid 48.0%, model 56.1% (projection_v2.0 (prediction ledger)) -- gap +8.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01TSITIE-TIE2` Will Learner Tien win at least 1.5 more games than Stefanos Tsitsipas?: 0.47/0.50 mid 48.5%, model 40.8% (projection_v2.0 (prediction ledger)) -- gap -7.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01TSITIE-TSI2` Will Stefanos Tsitsipas win at least 1.5 more games than Learner Tien?: 0.29/0.48 mid 38.5%, model 43.4% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01TSITIE-1-TIE` Will Learner Tien win set 1 in the Stefanos Tsitsipas vs Learner Tien match: 0.52/0.55 mid 53.5%, model 49.1% (projection_v2.0 (prediction ledger)) -- gap -4.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01TSITIE-1-TSI` Will Stefanos Tsitsipas win set 1 in the Stefanos Tsitsipas vs Learner Tien match: 0.45/0.48 mid 46.5%, model 50.8% (projection_v2.0 (prediction ledger)) -- gap +4.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01TSITIE-2-TSI` Will Stefanos Tsitsipas win set 2 in the Stefanos Tsitsipas vs Learner Tien match: 0.13/0.80 mid 46.5%, model 50.8% (projection_v2.0 (prediction ledger)) -- gap +4.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01TSITIE-TIE20` Will Learner Tien win the Stefanos Tsitsipas vs Learner Tien match by a set score of 2-0?: 0.01/0.39 mid 20.0%, model 24.2% (projection_v2.0 (prediction ledger)) -- gap +4.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01TSITIE-2-TIE` Will Learner Tien win set 2 in the Stefanos Tsitsipas vs Learner Tien match: 0.13/0.80 mid 46.5%, model 49.1% (projection_v2.0 (prediction ledger)) -- gap +2.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV01TSITIE-29` Over 28.5 games: 0.24/0.53 mid 38.5%, model 38.6% (projection_v2.0 (prediction ledger)) -- gap +0.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Luca Van Assche vs Mariano Navone -- ATP Paris R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208363:209414:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mariano Navone (`KXATPMATCH-26NOV01VANNAV-NAV`) | 0.40 / 0.41 (5468) | 40.5% | 44.3% | 46.9% | 45.4% [43.3%-47.4%] | -- | -- | -- | -- | PASS | +3.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luca Van Assche (`KXATPMATCH-26NOV01VANNAV-VAN`) | 0.58 / 0.59 (15) | 58.5% | 55.7% | 53.1% | 54.6% [52.6%-56.7%] | -- | -- | -- | -- | PASS | -2.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6040.0, B 5714.0; serve-point win A 60.0%, B 41.1%; Elo A 1801.5, B 1721.0; model uncertainty 0.0204
* Form inputs: days since last match A 5, B 5; matches on record A 394, B 433; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose +0.020, surface_dev_tight -0.021
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26NOV01VANNAV-VAN21` Will Luca Van Assche win the Luca Van Assche vs Mariano Navone match by a set score of 2-1?: 0.01/0.29 mid 15.0%, model 26.7% (projection_v2.0 (prediction ledger)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01VANNAV-19` Over 18.5 games: 0.52/0.93 mid 72.5%, model 83.7% (projection_v2.0 (prediction ledger)) -- gap +11.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01VANNAV-NAV21` Will Mariano Navone win the Luca Van Assche vs Mariano Navone match by a set score of 2-1?: 0.01/0.24 mid 12.5%, model 23.0% (projection_v2.0 (prediction ledger)) -- gap +10.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01VANNAV-VAN5` Will Luca Van Assche win at least 4.5 more games than Mariano Navone?: 0.19/0.46 mid 32.5%, model 23.7% (projection_v2.0 (prediction ledger)) -- gap -8.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01VANNAV-2-VAN` Will Luca Van Assche win set 2 in the Luca Van Assche vs Mariano Navone match: 0.13/0.80 mid 46.5%, model 53.8% (projection_v2.0 (prediction ledger)) -- gap +7.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01VANNAV-NAV20` Will Mariano Navone win the Luca Van Assche vs Mariano Navone match by a set score of 2-0?: 0.01/0.28 mid 14.5%, model 21.4% (projection_v2.0 (prediction ledger)) -- gap +6.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01VANNAV-VAN2` Will Luca Van Assche win at least 1.5 more games than Mariano Navone?: 0.54/0.57 mid 55.5%, model 48.8% (projection_v2.0 (prediction ledger)) -- gap -6.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01VANNAV-24` Over 23.5 games: 0.45/0.47 mid 46.0%, model 52.6% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01VANNAV-29` Over 28.5 games: 0.02/0.54 mid 28.0%, model 31.4% (projection_v2.0 (prediction ledger)) -- gap +3.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01VANNAV-1-NAV` Will Mariano Navone win set 1 in the Luca Van Assche vs Mariano Navone match: 0.43/0.46 mid 44.5%, model 46.2% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01VANNAV-1-VAN` Will Luca Van Assche win set 1 in the Luca Van Assche vs Mariano Navone match: 0.54/0.57 mid 55.5%, model 53.8% (projection_v2.0 (prediction ledger)) -- gap -1.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01VANNAV-VAN20` Will Luca Van Assche win the Luca Van Assche vs Mariano Navone match by a set score of 2-0?: 0.12/0.43 mid 27.5%, model 28.9% (projection_v2.0 (prediction ledger)) -- gap +1.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01VANNAV-NAV2` Will Mariano Navone win at least 1.5 more games than Luca Van Assche?: 0.10/0.64 mid 37.0%, model 37.6% (projection_v2.0 (prediction ledger)) -- gap +0.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01VANNAV-2-NAV` Will Mariano Navone win set 2 in the Luca Van Assche vs Mariano Navone match: 0.13/0.80 mid 46.5%, model 46.2% (projection_v2.0 (prediction ledger)) -- gap -0.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ilinca Dalina Amariei vs Angelica Sara -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221168:267408:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ilinca Dalina Amariei (`KXITFWMATCH-26NOV01AMASAR-AMA`) | 0.87 / 0.90 (14) | 88.5% | 82.5% | 81.9% | 77.3% [74.8%-80.4%] | -- | -- | -- | -- | PASS | -6.0 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Angelica Sara (`KXITFWMATCH-26NOV01AMASAR-SAR`) | 0.11 / 0.12 (23) | 11.5% | 17.5% | 18.1% | 22.7% [19.6%-25.2%] | -- | -- | -- | -- | PASS | +6.0 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2360.0, B 641.0; serve-point win A 56.4%, B 50.5%; Elo A 1534.4, B 1339.7; model uncertainty 0.028
* Form inputs: days since last match A 327, B 355; matches on record A 325, B 26; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.031, surface_pool_high -0.025, surface_dev_loose +0.004, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Felitsata Dorofeeva-Rybas vs Georgina Groth -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:265020:267022:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felitsata Dorofeeva-Rybas (`KXITFWMATCH-26NOV01DORGRO-DOR`) | 0.90 / 0.92 (2) | 91.0% | 91.9% | 85.8% | 83.3% [81.2%-86.7%] | -- | -- | -- | -- | PASS | +0.9 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Georgina Groth (`KXITFWMATCH-26NOV01DORGRO-GRO`) | 0.06 / 0.09 (5) | 7.5% | 8.1% | 14.2% | 16.7% [13.3%-18.9%] | -- | -- | -- | -- | PASS | +0.6 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 923.0, B 413.0; serve-point win A 57.8%, B 52.6%; Elo A 1447.6, B 1177.0; model uncertainty 0.0277
* Form inputs: days since last match A 334, B 201; matches on record A 19, B 25; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.003, surface_dev_loose +0.003, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Helena Muzinic vs Valeriia Artemeva -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:263887:267841:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valeriia Artemeva (`KXITFWMATCH-26NOV01MUZART-ART`) | 0.90 / 0.94 (116) | 92.0% | 98.1% | 43.1% | 86.9% [86.3%-88.0%] | -- | -- | -- | -- | PASS | +6.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Helena Muzinic (`KXITFWMATCH-26NOV01MUZART-MUZ`) | 0.05 / 0.08 (8) | 6.5% | 1.9% | 56.9% | 13.1% [12.0%-13.7%] | -- | -- | -- | -- | PASS | -4.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 1430.0; serve-point win A 45.1%, B 39.3%; Elo A 1027.7, B 1357.5; model uncertainty 0.0085
* Form inputs: days since last match A 789, B 201; matches on record A 19, B 41; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.006, surface_pool_high -0.011, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Summer Yardley vs Angelica Raggi -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216051:216405:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Angelica Raggi (`KXITFWMATCH-26NOV01YARRAG-RAG`) | 0.92 / 0.95 (112) | 93.5% | 95.3% | 90.7% | 90.7% [89.1%-92.4%] | -- | -- | -- | -- | PASS | +1.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Summer Yardley (`KXITFWMATCH-26NOV01YARRAG-YAR`) | 0.05 / 0.06 (3) | 5.5% | 4.7% | 9.3% | 9.3% [7.6%-10.9%] | -- | -- | -- | -- | PASS | -0.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 504.0, B 2349.0; serve-point win A 46.0%, B 41.5%; Elo A 1106.5, B 1503.9; model uncertainty 0.0165
* Form inputs: days since last match A 383, B 194; matches on record A 80, B 320; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.007, surface_dev_loose -0.004, surface_dev_tight +0.002
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marco Bavaro vs Peter Makk -- ATP Challenger Taranto Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01BAVMAK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marco Bavaro (`KXATPCHALLENGERMATCH-26NOV01BAVMAK-BAV`) | 0.06 / 0.08 (7) | 7.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Peter Makk (`KXATPCHALLENGERMATCH-26NOV01BAVMAK-MAK`) | 0.89 / 0.94 (6) | 91.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Andrea Colombo vs Adrian Andreev -- ATP Challenger Taranto Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01COLAND:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Andreev (`KXATPCHALLENGERMATCH-26NOV01COLAND-AND`) | 0.62 / 0.65 (7) | 63.5% | 89.5% | -- | -- [-----] | -- | 63.3% | -- | INSUFFICIENT_INPUTS | -- | +26.0 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Andrea Colombo (`KXATPCHALLENGERMATCH-26NOV01COLAND-COL`) | 0.32 / 0.37 (1) | 34.5% | 10.5% | -- | -- [-----] | -- | 36.7% | -- | INSUFFICIENT_INPUTS | -- | -24.0 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 56.5%, B 33.7%; Elo A 1196.5, B 1645.1; model uncertainty None
* Form inputs: days since last match A 187, B 40; matches on record A 31, B 361; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV01COLAND-AND  (YES = Adrian Andreev)
Model: 89%
Kalshi: 64%
Gap: +26 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE

## Massimo Giunta vs Nikita Belozertsev -- ATP Challenger Taranto Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01GIUBEL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikita Belozertsev (`KXATPCHALLENGERMATCH-26NOV01GIUBEL-BEL`) | 0.14 / 0.22 (21) | 18.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Massimo Giunta (`KXATPCHALLENGERMATCH-26NOV01GIUBEL-GIU`) | 0.74 / 0.81 (1) | 77.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Max Houkes vs Dominik Macej -- ATP Challenger Bratislava II Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01HOUMAC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Max Houkes (`KXATPCHALLENGERMATCH-26NOV01HOUMAC-HOU`) | 0.95 / 0.96 (20) | 95.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dominik Macej (`KXATPCHALLENGERMATCH-26NOV01HOUMAC-MAC`) | 0.04 / 0.05 (100) | 4.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Tiago Pereira vs Filiberto Fumagalli -- ATP Challenger Taranto Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01PERFUM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Filiberto Fumagalli (`KXATPCHALLENGERMATCH-26NOV01PERFUM-FUM`) | 0.15 / 0.19 (12) | 17.0% | 8.2% | -- | -- [-----] | -- | 18.2% | -- | INSUFFICIENT_INPUTS | -- | -8.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Tiago Pereira (`KXATPCHALLENGERMATCH-26NOV01PERFUM-PER`) | 0.80 / 0.84 (200) | 82.0% | 91.8% | -- | -- [-----] | -- | 81.7% | -- | INSUFFICIENT_INPUTS | -- | +9.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 66.4%, B 44.4%; Elo A 1550.4, B 1090.3; model uncertainty None
* Form inputs: days since last match A 102, B 327; matches on record A 266, B 25; data quality D
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER

## Oleg Prihodko vs Yannik Kelm -- ATP Challenger Bratislava II Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-01T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01PRIKEL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yannik Kelm (`KXATPCHALLENGERMATCH-26NOV01PRIKEL-KEL`) | 0.47 / 0.50 (16) | 48.5% | 25.7% | -- | -- [-----] | -- | 50.0% | -- | INSUFFICIENT_INPUTS | -- | -22.8 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Oleg Prihodko (`KXATPCHALLENGERMATCH-26NOV01PRIKEL-PRI`) | 0.48 / 0.51 (26) | 49.5% | 74.3% | -- | -- [-----] | -- | 50.0% | -- | INSUFFICIENT_INPUTS | -- | +24.8 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 63.2%, B 41.9%; Elo A 1544.0, B 1239.4; model uncertainty None
* Form inputs: days since last match A 40, B 187; matches on record A 483, B 83; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV01PRIKEL-PRI  (YES = Oleg Prihodko)
Model: 74%
Kalshi: 50%
Gap: +25 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: EVENT_MAPPING_RISK, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER

## Nuno Borges vs Alex Molcan -- ATP Paris Q3

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-01 16:30Z
* Current expected start: 2026-11-01 13:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: 2026-11-01 12:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T16:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:132686:144684:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nuno Borges (`KXATPMATCH-26NOV01BORMOL-BOR`) | 0.57 / 0.59 (17754) | 58.0% | 62.8% | 58.4% | 60.8% [58.9%-62.1%] | -- | 58.0% | 58.0% | MODEL_LONE_OUTLIER | PASS | +4.8 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Alex Molcan (`KXATPMATCH-26NOV01BORMOL-MOL`) | 0.41 / 0.43 (6572) | 42.0% | 37.1% | 41.6% | 39.2% [37.9%-41.1%] | -- | 42.2% | 42.2% | MODEL_LONE_OUTLIER | PASS | -4.8 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5889.0, B 4355.0; serve-point win A 65.8%, B 36.8%; Elo A 1865.6, B 1749.1; model uncertainty 0.0161
* Form inputs: days since last match A 1, B 6; matches on record A 553, B 554; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.009, surface_dev_loose +0.014, surface_dev_tight -0.019
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26NOV01BORMOL-BOR21` Will Nuno Borges win the Nuno Borges vs Alex Molcan match by a set score of 2-1?: 0.01/0.28 mid 14.5%, model 28.4% (projection_v2.0 (prediction ledger)) -- gap +13.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01BORMOL-BOR20` Will Nuno Borges win the Nuno Borges vs Alex Molcan match by a set score of 2-0?: 0.01/0.42 mid 21.5%, model 34.4% (projection_v2.0 (prediction ledger)) -- gap +12.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01BORMOL-2-BOR` Will Nuno Borges win set 2 in the Nuno Borges vs Alex Molcan match: 0.02/0.98 mid 50.0%, model 58.7% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01BORMOL-2-MOL` Will Alex Molcan win set 2 in the Nuno Borges vs Alex Molcan match: 0.01/0.98 mid 49.5%, model 41.3% (projection_v2.0 (prediction ledger)) -- gap -8.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01BORMOL-MOL21` Will Alex Molcan win the Nuno Borges vs Alex Molcan match by a set score of 2-1?: 0.01/0.24 mid 12.5%, model 20.1% (projection_v2.0 (prediction ledger)) -- gap +7.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01BORMOL-1-BOR` Will Nuno Borges win set 1 in the Nuno Borges vs Alex Molcan match: 0.53/0.55 mid 54.0%, model 58.7% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01BORMOL-1-MOL` Will Alex Molcan win set 1 in the Nuno Borges vs Alex Molcan match: 0.45/0.46 mid 45.5%, model 41.3% (projection_v2.0 (prediction ledger)) -- gap -4.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01BORMOL-MOL20` Will Alex Molcan win the Nuno Borges vs Alex Molcan match by a set score of 2-0?: 0.01/0.30 mid 15.5%, model 17.1% (projection_v2.0 (prediction ledger)) -- gap +1.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Noma Noha Akugue vs Alina Charaeva -- WTA 125K Courmayeur F

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-01 17:00Z
* Current expected start: 2026-11-01 14:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: 2026-11-01 13:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · surface ? · scheduled 2026-11-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26NOV01NOHCHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alina Charaeva (`KXWTACHALLENGERMATCH-26NOV01NOHCHA-CHA`) | 0.64 / 0.66 (1281) | 65.0% | -- | -- | -- [-----] | -- | 64.7% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Noma Noha Akugue (`KXWTACHALLENGERMATCH-26NOV01NOHCHA-NOH`) | 0.34 / 0.36 (791) | 35.0% | -- | -- | -- [-----] | -- | 35.4% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Alice Tubello vs Julia Grabher -- WTA 125K Curitiba F

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-01 17:00Z
* Current expected start: 2026-11-01 14:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: 2026-11-01 13:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · surface ? · scheduled 2026-11-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26NOV01TUBGRA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julia Grabher (`KXWTACHALLENGERMATCH-26NOV01TUBGRA-GRA`) | 0.54 / 0.56 (1382) | 55.0% | -- | -- | -- [-----] | -- | 56.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alice Tubello (`KXWTACHALLENGERMATCH-26NOV01TUBGRA-TUB`) | 0.44 / 0.46 (15) | 45.0% | -- | -- | -- [-----] | -- | 43.4% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Yurii Dzhavakian vs Gijs Brouwer -- M15 Sharm ElSheikh F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:122113:133835:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gijs Brouwer (`KXITFMATCH-26NOV01DZHBRO-BRO`) | 0.80 / 0.83 (247) | 81.5% | 80.4% | 62.5% | 69.8% [66.9%-75.8%] | -- | -- | -- | -- | PASS | -1.1 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yurii Dzhavakian (`KXITFMATCH-26NOV01DZHBRO-DZH`) | 0.12 / 0.21 (15) | 16.5% | 19.6% | 37.5% | 30.2% [24.2%-33.1%] | -- | -- | -- | -- | PASS | +3.1 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5142.0, B 1950.0; serve-point win A 52.6%, B 40.9%; Elo A 1383.3, B 1610.4; model uncertainty 0.0444
* Form inputs: days since last match A 187, B 54; matches on record A 436, B 513; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.023, surface_pool_high +0.019, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sara Cakarevic vs Stamatia Tsoutsi -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214319:270377:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Cakarevic (`KXITFWMATCH-26NOV01CAKTSO-CAK`) | 0.96 / 0.97 (427) | 96.5% | 88.9% | 56.3% | 73.8% [66.5%-79.5%] | -- | -- | -- | -- | PASS | -7.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Stamatia Tsoutsi (`KXITFWMATCH-26NOV01CAKTSO-TSO`) | 0.03 / 0.04 (3751) | 3.5% | 11.1% | 43.7% | 26.2% [20.5%-33.5%] | -- | -- | -- | -- | PASS | +7.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1791.0, B 30.0; serve-point win A 60.0%, B 49.2%; Elo A 1460.0, B 1283.9; model uncertainty 0.0653
* Form inputs: days since last match A 19, B 341; matches on record A 475, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.057, surface_pool_high -0.073, surface_dev_loose -0.001, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aya El Sayed vs Rikke De Koning -- W15 Sharm ElSheikh F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221083:252584:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rikke De Koning (`KXITFWMATCH-26NOV01ELSDEK-DEK`) | 0.50 / 0.56 (126) | 53.0% | 64.2% | 62.6% | 60.0% [57.4%-62.1%] | -- | -- | -- | -- | PASS | +11.2 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aya El Sayed (`KXITFWMATCH-26NOV01ELSDEK-ELS`) | 0.44 / 0.45 (55) | 44.5% | 35.8% | 37.4% | 40.0% [37.9%-42.6%] | -- | -- | -- | -- | PASS | -8.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 698.0, B 1253.0; serve-point win A 52.3%, B 45.0%; Elo A 1200.5, B 1256.5; model uncertainty 0.0233
* Form inputs: days since last match A 327, B 187; matches on record A 81, B 139; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Despoina Koskina vs Teodora Miron -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:269946:270171:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Despoina Koskina (`KXITFWMATCH-26NOV01KOSMIR-KOS`) | 0.05 / 0.10 (9) | 7.5% | 24.8% | 53.7% | 37.4% [37.4%-37.4%] | -- | -- | -- | -- | PASS | +17.3 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Teodora Miron (`KXITFWMATCH-26NOV01KOSMIR-MIR`) | 0.88 / 0.92 (8) | 90.0% | 75.2% | 46.3% | 62.6% [62.6%-62.6%] | -- | -- | -- | -- | PASS | -14.8 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 136.0; serve-point win A 50.9%, B 44.0%; Elo A 1229.4, B 1320.1; model uncertainty 0.0002
* Form inputs: days since last match A 712, B 467; matches on record A 2, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV01KOSMIR-KOS  (YES = Despoina Koskina)
Model: 25%
Kalshi: 8%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Krystyna Pochtovyk vs Jessica Bertoldo -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216075:239449:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jessica Bertoldo (`KXITFWMATCH-26NOV01POCBER-BER`) | 0.84 / 0.88 (108) | 86.0% | 78.7% | 80.9% | 77.0% [74.0%-80.9%] | -- | -- | -- | -- | PASS | -7.3 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Krystyna Pochtovyk (`KXITFWMATCH-26NOV01POCBER-POC`) | 0.15 / 0.16 (36) | 15.5% | 21.3% | 19.1% | 23.0% [19.1%-26.0%] | -- | -- | -- | -- | PASS | +5.8 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 999.0, B 1651.0; serve-point win A 46.5%, B 47.6%; Elo A 1252.8, B 1439.6; model uncertainty 0.0341
* Form inputs: days since last match A 208, B 201; matches on record A 168, B 169; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.004, surface_dev_loose +0.000, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cristiana Nicoleta Todoni vs Vicky Van de Peer -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220614:261104:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cristiana Nicoleta Todoni (`KXITFWMATCH-26NOV01TODVAN-TOD`) | 0.80 / 0.83 (5) | 81.5% | 41.0% | 40.0% | 37.9% [35.4%-39.4%] | -- | -- | -- | -- | PASS | -40.5 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Vicky Van de Peer (`KXITFWMATCH-26NOV01TODVAN-VAN`) | 0.15 / 0.20 (12) | 17.5% | 59.0% | 60.1% | 62.1% [60.6%-64.6%] | -- | -- | -- | -- | PASS | +41.5 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 865.0, B 1898.0; serve-point win A 52.1%, B 46.2%; Elo A 1304.5, B 1398.5; model uncertainty 0.0202
* Form inputs: days since last match A 111, B 418; matches on record A 57, B 239; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV01TODVAN-VAN  (YES = Vicky Van de Peer)
Model: 59%
Kalshi: 18%
Gap: +41 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.010, surface_dev_loose +0.015, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sebastian Gima vs Ryan Peniston -- ATP Challenger Taranto Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 14:20Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T14:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01GIMPEN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sebastian Gima (`KXATPCHALLENGERMATCH-26NOV01GIMPEN-GIM`) | 0.30 / 0.35 (139) | 32.5% | -- | -- | -- [-----] | -- | 32.2% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ryan Peniston (`KXATPCHALLENGERMATCH-26NOV01GIMPEN-PEN`) | 0.61 / 0.69 (34) | 65.0% | -- | -- | -- [-----] | -- | 67.7% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; WIDE_SPREAD

## Lucas Poullain vs Tomas Lanik -- ATP Challenger Bratislava II Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 14:20Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T14:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01POULAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tomas Lanik (`KXATPCHALLENGERMATCH-26NOV01POULAN-LAN`) | 0.13 / 0.16 (9) | 14.5% | -- | -- | -- [-----] | -- | 10.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lucas Poullain (`KXATPCHALLENGERMATCH-26NOV01POULAN-POU`) | 0.83 / 0.86 (350) | 84.5% | -- | -- | -- [-----] | -- | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Matteo Sciahbasi vs Arvid Nordquist -- ATP Challenger Taranto Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 14:20Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T14:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01SCINOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arvid Nordquist (`KXATPCHALLENGERMATCH-26NOV01SCINOR-NOR`) | 0.56 / 0.61 (128) | 58.5% | -- | -- | -- [-----] | -- | 59.3% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matteo Sciahbasi (`KXATPCHALLENGERMATCH-26NOV01SCINOR-SCI`) | 0.37 / 0.43 (85) | 40.0% | -- | -- | -- [-----] | -- | 40.7% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER

## Jacopo Vasami vs Kenny De Schepper -- ATP Challenger Taranto Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 14:20Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T14:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01VASDES:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kenny De Schepper (`KXATPCHALLENGERMATCH-26NOV01VASDES-DES`) | 0.23 / 0.27 (27) | 25.0% | -- | -- | -- [-----] | -- | 26.3% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jacopo Vasami (`KXATPCHALLENGERMATCH-26NOV01VASDES-VAS`) | 0.71 / 0.76 (301) | 73.5% | -- | -- | -- [-----] | -- | 73.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER

## Michael Vrbensky vs Marek Gengel -- ATP Challenger Bratislava II Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 14:20Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T14:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01VRBGEN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marek Gengel (`KXATPCHALLENGERMATCH-26NOV01VRBGEN-GEN`) | 0.51 / 0.56 (15) | 53.5% | -- | -- | -- [-----] | -- | 54.1% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Michael Vrbensky (`KXATPCHALLENGERMATCH-26NOV01VRBGEN-VRB`) | 0.45 / 0.47 (51) | 46.0% | -- | -- | -- [-----] | -- | 46.0% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER

## Marcus Walters vs Radu Albot -- ATP Challenger Taranto Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 14:20Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T14:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01WALALB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Radu Albot (`KXATPCHALLENGERMATCH-26NOV01WALALB-ALB`) | 0.63 / 0.69 (5) | 66.0% | -- | -- | -- [-----] | -- | 69.9% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marcus Walters (`KXATPCHALLENGERMATCH-26NOV01WALALB-WAL`) | 0.30 / 0.31 (6) | 30.5% | -- | -- | -- [-----] | -- | 29.8% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE

## Jiri Lehecka vs Valentin Vacherot -- ATP Basel F

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-01 17:30Z
* Current expected start: 2026-11-01 14:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: 2026-11-01 13:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-11-01T17:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200473:208103:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jiri Lehecka (`KXATPMATCH-26NOV01LEHVAC-LEH`) | 0.64 / 0.65 (73892) | 64.5% | 63.0% | 64.6% | 63.8% [62.9%-65.2%] | -- | 63.5% | 63.5% | MARKETS_AGREE | PASS | -1.5 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Valentin Vacherot (`KXATPMATCH-26NOV01LEHVAC-VAC`) | 0.35 / 0.36 (3905) | 35.5% | 37.0% | 35.4% | 36.2% [34.8%-37.1%] | -- | 36.8% | 36.8% | MARKETS_AGREE | PASS | +1.5 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5638.0, B 4676.0; serve-point win A 70.8%, B 32.0%; Elo A 1984.9, B 1896.6; model uncertainty 0.0114
* Form inputs: days since last match A 1, B 1; matches on record A 462, B 425; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.009, surface_dev_loose +0.004, surface_dev_tight -0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV01LEHVAC-25` Over 24.5 games: 0.48/0.49 mid 48.5%, model 57.7% (projection_v2.0 (prediction ledger)) -- gap +9.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01LEHVAC-LEH6` Will Jiri Lehecka win at least 5.5 more games than Valentin Vacherot?: 0.09/0.17 mid 13.0%, model 6.5% (projection_v2.0 (prediction ledger)) -- gap -6.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01LEHVAC-20` Over 19.5 games: 0.75/0.89 mid 82.0%, model 88.3% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01LEHVAC-LEH20` Will Jiri Lehecka win the Jiri Lehecka vs Valentin Vacherot match by a set score of 2-0?: 0.38/0.42 mid 40.0%, model 34.5% (projection_v2.0 (prediction ledger)) -- gap -5.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01LEHVAC-LEH21` Will Jiri Lehecka win the Jiri Lehecka vs Valentin Vacherot match by a set score of 2-1?: 0.22/0.25 mid 23.5%, model 28.5% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01LEHVAC-VAC21` Will Valentin Vacherot win the Jiri Lehecka vs Valentin Vacherot match by a set score of 2-1?: 0.14/0.17 mid 15.5%, model 20.0% (projection_v2.0 (prediction ledger)) -- gap +4.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01LEHVAC-30` Over 29.5 games: 0.29/0.41 mid 35.0%, model 38.9% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01LEHVAC-LEH3` Will Jiri Lehecka win at least 2.5 more games than Valentin Vacherot?: 0.46/0.48 mid 47.0%, model 43.1% (projection_v2.0 (prediction ledger)) -- gap -3.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01LEHVAC-VAC2` Will Valentin Vacherot win at least 1.5 more games than Jiri Lehecka?: 0.24/0.38 mid 31.0%, model 28.7% (projection_v2.0 (prediction ledger)) -- gap -2.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01LEHVAC-1-LEH` Will Jiri Lehecka win set 1 in the Jiri Lehecka vs Valentin Vacherot match: 0.59/0.62 mid 60.5%, model 58.8% (projection_v2.0 (prediction ledger)) -- gap -1.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01LEHVAC-1-VAC` Will Valentin Vacherot win set 1 in the Jiri Lehecka vs Valentin Vacherot match: 0.38/0.41 mid 39.5%, model 41.2% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01LEHVAC-2-VAC` Will Valentin Vacherot win set 2 in the Jiri Lehecka vs Valentin Vacherot match: 0.38/0.41 mid 39.5%, model 41.2% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01LEHVAC-2-LEH` Will Jiri Lehecka win set 2 in the Jiri Lehecka vs Valentin Vacherot match: 0.58/0.62 mid 60.0%, model 58.8% (projection_v2.0 (prediction ledger)) -- gap -1.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01LEHVAC-VAC20` Will Valentin Vacherot win the Jiri Lehecka vs Valentin Vacherot match by a set score of 2-0?: 0.17/0.19 mid 18.0%, model 17.0% (projection_v2.0 (prediction ledger)) -- gap -1.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Martina Lo Pumo vs Clervie Ngounoue -- W75 Petange R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214403:238064:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martina Lo Pumo (`KXITFWMATCH-26NOV01LOPNGO-LOP`) | 0.04 / 0.08 (7) | 6.0% | 0.7% | 13.3% | 2.9% [2.2%-3.6%] | -- | -- | -- | -- | PASS | -5.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Clervie Ngounoue (`KXITFWMATCH-26NOV01LOPNGO-NGO`) | 0.89 / 0.94 (10) | 91.5% | 99.3% | 86.7% | 97.1% [96.4%-97.8%] | -- | -- | -- | -- | PASS | +7.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 41.0, B 2509.0; serve-point win A 46.1%, B 35.3%; Elo A 1084.9, B 1704.5; model uncertainty 0.007
* Form inputs: days since last match A 446, B 68; matches on record A 23, B 153; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.007, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stephanie Judith Visscher vs Katarina Kujovic -- W75 Petange R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220613:268778:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katarina Kujovic (`KXITFWMATCH-26NOV01VISKUJ-KUJ`) | 0.17 / 0.20 (13) | 18.5% | 7.5% | 8.2% | 14.0% [11.6%-17.3%] | -- | -- | -- | -- | PASS | -11.0 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Stephanie Judith Visscher (`KXITFWMATCH-26NOV01VISKUJ-VIS`) | 0.78 / 0.82 (88) | 80.0% | 92.5% | 91.8% | 86.0% [82.7%-88.4%] | -- | -- | -- | -- | PASS | +12.5 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3377.0, B 711.0; serve-point win A 64.3%, B 46.8%; Elo A 1566.0, B 1299.8; model uncertainty 0.0285
* Form inputs: days since last match A 48, B 299; matches on record A 453, B 15; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high -0.009, surface_dev_loose +0.003, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aziz Ouakaa vs Lilian Marmousez -- M15 Monastir F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200297:208421:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lilian Marmousez (`KXITFMATCH-26NOV01OUAMAR-MAR`) | 0.78 / 0.82 (435) | 80.0% | 80.4% | 85.5% | 82.3% [79.5%-84.0%] | 80.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.4 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aziz Ouakaa (`KXITFMATCH-26NOV01OUAMAR-OUA`) | 0.18 / 0.20 (256) | 19.0% | 19.6% | 14.5% | 17.7% [16.0%-20.5%] | 19.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.6 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3444.0, B 2574.0; serve-point win A 55.1%, B 38.4%; Elo A 1357.4, B 1554.5; model uncertainty 0.0226
* Form inputs: days since last match A 82, B 159; matches on record A 439, B 272; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.017, surface_pool_high +0.025, surface_dev_loose +0.004, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Benjamin Pietri vs Miles Jones -- M15 Heraklion F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202125:207404:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miles Jones (`KXITFMATCH-26NOV01PIEJON-JON`) | 0.38 / 0.40 (249) | 39.0% | 73.1% | 81.2% | 73.3% [67.7%-77.5%] | 38.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +34.1 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Benjamin Pietri (`KXITFMATCH-26NOV01PIEJON-PIE`) | 0.58 / 0.59 (60) | 58.5% | 26.9% | 18.8% | 26.7% [22.6%-32.3%] | 61.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -31.6 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1540.0, B 2182.0; serve-point win A 54.3%, B 41.0%; Elo A 1291.0, B 1391.3; model uncertainty 0.0486
* Form inputs: days since last match A 54, B 194; matches on record A 233, B 132; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV01PIEJON-JON  (YES = Miles Jones)
Model: 73%
Kalshi: 39%
Gap: +34 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.017, surface_pool_high +0.009, surface_dev_loose -0.009, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Veronika Podrez vs Oceane Dodin -- W75 Poitiers F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206219:247669:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oceane Dodin (`KXITFWMATCH-26NOV01PODDOD-DOD`) | 0.36 / 0.38 (32) | 37.0% | 35.3% | 12.3% | 27.0% [20.3%-42.7%] | 37.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Veronika Podrez (`KXITFWMATCH-26NOV01PODDOD-POD`) | 0.60 / 0.64 (130) | 62.0% | 64.7% | 87.7% | 73.0% [57.3%-79.7%] | 62.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3466.0, B 1969.0; serve-point win A 60.2%, B 42.7%; Elo A 1719.9, B 1748.1; model uncertainty 0.112
* Form inputs: days since last match A 37, B 38; matches on record A 227, B 714; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose +0.004, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marie Vogt vs Kayo Nishimura -- W15 Monastir F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223100:260613:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kayo Nishimura (`KXITFWMATCH-26NOV01VOGNIS-NIS`) | 0.63 / 0.64 (242) | 63.5% | 62.5% | 44.1% | 53.2% [50.0%-58.0%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.0 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marie Vogt (`KXITFWMATCH-26NOV01VOGNIS-VOG`) | 0.37 / 0.39 (18) | 38.0% | 37.5% | 55.9% | 46.8% [42.0%-50.0%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -0.5 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2280.0, B 2288.0; serve-point win A 51.7%, B 46.0%; Elo A 1415.5, B 1542.8; model uncertainty 0.0398
* Form inputs: days since last match A 20, B 187; matches on record A 164, B 161; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.032, surface_pool_high -0.032, surface_dev_loose -0.016, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matyas Cerny vs Sebastian Sorger -- ATP Challenger Bratislava II Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01CERSOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matyas Cerny (`KXATPCHALLENGERMATCH-26NOV01CERSOR-CER`) | 0.23 / 0.27 (10) | 25.0% | -- | -- | -- [-----] | -- | 25.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sebastian Sorger (`KXATPCHALLENGERMATCH-26NOV01CERSOR-SOR`) | 0.69 / 0.77 (160) | 73.0% | -- | -- | -- [-----] | -- | 74.2% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; WIDE_SPREAD

## Giovanni Mpetshi Perricard vs Yanis Ghazouani Durand -- ATP Challenger Bratislava II Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01MPEGHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yanis Ghazouani Durand (`KXATPCHALLENGERMATCH-26NOV01MPEGHA-GHA`) | 0.09 / 0.10 (22) | 9.5% | -- | -- | -- [-----] | -- | 11.0% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Giovanni Mpetshi Perricard (`KXATPCHALLENGERMATCH-26NOV01MPEGHA-MPE`) | 0.88 / 0.92 (134) | 90.0% | -- | -- | -- [-----] | -- | 89.2% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Anna Burchak vs Georgina Garcia-Perez -- W75 Petange R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:202916:270253:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Burchak (`KXITFWMATCH-26NOV01BURGAR-BUR`) | 0.24 / 0.29 (50) | 26.5% | 5.1% | 41.3% | 13.4% [9.3%-16.3%] | -- | -- | -- | -- | PASS | -21.4 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Georgina Garcia-Perez (`KXITFWMATCH-26NOV01BURGAR-GAR`) | 0.67 / 0.75 (6) | 71.0% | 94.9% | 58.7% | 86.6% [83.7%-90.7%] | -- | -- | -- | -- | PASS | +23.9 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 191.0, B 507.0; serve-point win A 53.4%, B 33.9%; Elo A 1222.9, B 1586.6; model uncertainty 0.0353
* Form inputs: days since last match A 376, B 48; matches on record A 3, B 484; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV01BURGAR-GAR  (YES = Georgina Garcia-Perez)
Model: 95%
Kalshi: 71%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.023, surface_pool_high +0.023, surface_dev_loose -0.001, surface_dev_tight -0.002
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kira Pavlova vs Julie Myatovic -- W75 Petange R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223302:260204:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julie Myatovic (`KXITFWMATCH-26NOV01PAVMYA-MYA`) | 0.06 / 0.08 (7) | 7.0% | 6.7% | 16.1% | 10.4% [9.0%-11.2%] | -- | -- | -- | -- | PASS | -0.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kira Pavlova (`KXITFWMATCH-26NOV01PAVMYA-PAV`) | 0.90 / 0.94 (116) | 92.0% | 93.3% | 83.9% | 89.6% [88.8%-91.0%] | -- | -- | -- | -- | PASS | +1.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2405.0, B 350.0; serve-point win A 57.8%, B 53.4%; Elo A 1588.9, B 1189.9; model uncertainty 0.0106
* Form inputs: days since last match A 208, B 201; matches on record A 230, B 65; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.011, surface_dev_loose +0.002, surface_dev_tight -0.002
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tomas Farjat vs Valentin Basel -- ATP Challenger Villa Maria Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01FARBAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valentin Basel (`KXATPCHALLENGERMATCH-26NOV01FARBAS-BAS`) | 0.52 / 0.58 (56) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tomas Farjat (`KXATPCHALLENGERMATCH-26NOV01FARBAS-FAR`) | 0.39 / 0.48 (4) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Thiago Agustin Pernas vs Federico Aguilar Cardozo -- ATP Challenger Villa Maria Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01PERAGU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Federico Aguilar Cardozo (`KXATPCHALLENGERMATCH-26NOV01PERAGU-AGU`) | 0.52 / 0.71 (6) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Thiago Agustin Pernas (`KXATPCHALLENGERMATCH-26NOV01PERAGU-PER`) | 0.31 / 0.50 (39) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Rocco Valente vs Ryo Tabata -- ATP Challenger Villa Maria Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01VALTAB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ryo Tabata (`KXATPCHALLENGERMATCH-26NOV01VALTAB-TAB`) | 0.62 / 0.81 (13) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rocco Valente (`KXATPCHALLENGERMATCH-26NOV01VALTAB-VAL`) | 0.23 / 0.42 (14) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Polina Maneshina vs Beatris Spasova -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-01T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV01MANSPA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Maneshina (`KXITFWMATCH-26NOV01MANSPA-MAN`) | 0.07 / 0.18 (5) | 12.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Beatris Spasova (`KXITFWMATCH-26NOV01MANSPA-SPA`) | 0.79 / 0.92 (4) | 85.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Juliette Mazzoni vs Cristina Diaz Adrover -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220934:232881:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cristina Diaz Adrover (`KXITFWMATCH-26NOV01MAZDIA-DIA`) | 0.90 / 0.92 (118) | 91.0% | 98.0% | 91.6% | 94.1% [93.1%-95.0%] | -- | -- | -- | -- | PASS | +7.0 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Juliette Mazzoni (`KXITFWMATCH-26NOV01MAZDIA-MAZ`) | 0.06 / 0.08 (25) | 7.0% | 2.0% | 8.4% | 5.9% [5.0%-6.9%] | -- | -- | -- | -- | PASS | -5.0 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 206.0, B 3491.0; serve-point win A 47.2%, B 37.2%; Elo A 972.3, B 1462.3; model uncertainty 0.0093
* Form inputs: days since last match A 306, B 19; matches on record A 127, B 204; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.010, surface_dev_loose -0.002, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Antonia Stoyanov vs Nina Andronicou -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:263903:267422:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nina Andronicou (`KXITFWMATCH-26NOV01STOAND-AND`) | 0.06 / 0.09 (8) | 7.5% | 6.8% | 32.0% | 26.0% [25.2%-26.5%] | -- | -- | -- | -- | PASS | -0.7 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Antonia Stoyanov (`KXITFWMATCH-26NOV01STOAND-STO`) | 0.86 / 0.94 (167) | 90.0% | 93.2% | 68.0% | 74.0% [73.5%-74.8%] | -- | -- | -- | -- | PASS | +3.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 608.0, B 185.0; serve-point win A 58.7%, B 52.5%; Elo A 1451.4, B 1261.9; model uncertainty 0.0065
* Form inputs: days since last match A 201, B 362; matches on record A 24, B 4; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eliska Tichackova vs Natalia Fehr -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223064:254748:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Natalia Fehr (`KXITFWMATCH-26NOV01TICFEH-FEH`) | 0.03 / 0.04 (5162) | 3.5% | 0.4% | 1.5% | 2.8% [2.4%-3.2%] | -- | -- | -- | -- | PASS | -3.1 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Eliska Tichackova (`KXITFWMATCH-26NOV01TICFEH-TIC`) | 0.96 / 0.97 (353) | 96.5% | 99.6% | 98.5% | 97.2% [96.8%-97.6%] | -- | -- | -- | -- | PASS | +3.1 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1647.0, B 203.0; serve-point win A 60.7%, B 59.5%; Elo A 1623.6, B 1022.0; model uncertainty 0.0042
* Form inputs: days since last match A 250, B 341; matches on record A 46, B 110; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.004, surface_dev_loose +0.003, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tessa Johanna Brockmann vs Olivia Gram -- W75 Petange R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221376:260598:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tessa Johanna Brockmann (`KXITFWMATCH-26NOV01BROGRA-BRO`) | 0.93 / 0.95 (57) | 94.0% | 96.8% | 82.5% | 89.9% [86.8%-92.8%] | -- | -- | -- | -- | PASS | +2.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Olivia Gram (`KXITFWMATCH-26NOV01BROGRA-GRA`) | 0.04 / 0.06 (358) | 5.0% | 3.2% | 17.5% | 10.1% [7.2%-13.2%] | -- | -- | -- | -- | PASS | -1.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3426.0, B 194.0; serve-point win A 61.4%, B 52.6%; Elo A 1598.4, B 1204.2; model uncertainty 0.0299
* Form inputs: days since last match A 18, B 488; matches on record A 169, B 182; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.023, surface_pool_high -0.031, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Annemarie Lazar vs Tilwith Di Girolami -- W75 Petange R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:228910:241728:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tilwith Di Girolami (`KXITFWMATCH-26NOV01LAZDIG-DIG`) | 0.81 / 0.93 (40) | 87.0% | 90.5% | 69.8% | 78.3% [75.9%-81.0%] | -- | -- | -- | -- | PASS | +3.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Annemarie Lazar (`KXITFWMATCH-26NOV01LAZDIG-LAZ`) | 0.04 / 0.14 (30) | 9.0% | 9.5% | 30.2% | 21.7% [19.0%-24.1%] | -- | -- | -- | -- | PASS | +0.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 404.0, B 1533.0; serve-point win A 50.3%, B 39.8%; Elo A 1200.5, B 1440.2; model uncertainty 0.0256
* Form inputs: days since last match A 250, B 187; matches on record A 57, B 202; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.024, surface_dev_loose +0.009, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marko Bekeni vs Matthew William Donald -- ATP Challenger Bratislava II Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 16:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T16:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01BEKDON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marko Bekeni (`KXATPCHALLENGERMATCH-26NOV01BEKDON-BEK`) | 0.06 / 0.09 (6) | 7.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matthew William Donald (`KXATPCHALLENGERMATCH-26NOV01BEKDON-DON`) | 0.90 / 0.94 (105) | 92.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Radovan Michalik vs Vadym Ursu -- ATP Challenger Bratislava II Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 16:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T16:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01MICURS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Radovan Michalik (`KXATPCHALLENGERMATCH-26NOV01MICURS-MIC`) | 0.07 / 0.12 (135) | 9.5% | -- | -- | -- [-----] | -- | 11.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vadym Ursu (`KXATPCHALLENGERMATCH-26NOV01MICURS-URS`) | 0.87 / 0.92 (65) | 89.5% | -- | -- | -- [-----] | -- | 92.6% | 92.6% | EXTERNAL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Moise Kouame vs Martin Damm Jr -- ATP Challenger Brest F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01KOUDAM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martin Damm Jr (`KXATPCHALLENGERMATCH-26NOV01KOUDAM-DAM`) | 0.48 / 0.49 (4409) | 48.5% | -- | -- | -- [-----] | 53.1% | -- | 53.1% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Moise Kouame (`KXATPCHALLENGERMATCH-26NOV01KOUDAM-KOU`) | 0.51 / 0.52 (14) | 51.5% | -- | -- | -- [-----] | 46.9% | -- | 46.9% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Janika Kusy vs Laura Svatikova -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215505:259886:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Janika Kusy (`KXITFWMATCH-26NOV01KUSSVA-KUS`) | 0.05 / 0.07 (6) | 6.0% | 6.5% | 47.9% | 21.2% [17.5%-24.4%] | -- | -- | -- | -- | PASS | +0.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Laura Svatikova (`KXITFWMATCH-26NOV01KUSSVA-SVA`) | 0.90 / 0.95 (5) | 92.5% | 93.5% | 52.1% | 78.8% [75.5%-82.5%] | -- | -- | -- | -- | PASS | +1.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 70.0, B 1657.0; serve-point win A 48.9%, B 39.7%; Elo A 1064.6, B 1303.4; model uncertainty 0.0347
* Form inputs: days since last match A 425, B 348; matches on record A 54, B 244; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.022, surface_pool_high +0.024, surface_dev_loose -0.000, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Astrid Lew Yan Foon vs Karyna Fiadosik -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:235159:269703:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karyna Fiadosik (`KXITFWMATCH-26NOV01LEWFIA-FIA`) | 0.03 / 0.04 (5310) | 3.5% | 1.3% | 34.5% | 11.1% [8.8%-13.3%] | -- | -- | -- | -- | PASS | -2.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Astrid Lew Yan Foon (`KXITFWMATCH-26NOV01LEWFIA-LEW`) | 0.96 / 0.97 (303) | 96.5% | 98.7% | 65.5% | 88.9% [86.7%-91.2%] | -- | -- | -- | -- | PASS | +2.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1722.0, B 44.0; serve-point win A 64.1%, B 52.8%; Elo A 1525.8, B 1154.8; model uncertainty 0.0229
* Form inputs: days since last match A 117, B 600; matches on record A 180, B 7; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.021, surface_dev_loose -0.001, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Emma Mazzoni vs Mirjana Jovanovic -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220790:260993:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mirjana Jovanovic (`KXITFWMATCH-26NOV01MAZJOV-JOV`) | 0.81 / 0.84 (43) | 82.5% | 80.9% | 40.5% | 73.0% [70.3%-78.0%] | -- | -- | -- | -- | PASS | -1.6 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Emma Mazzoni (`KXITFWMATCH-26NOV01MAZJOV-MAZ`) | 0.14 / 0.19 (10) | 16.5% | 19.1% | 59.5% | 27.0% [22.0%-29.7%] | -- | -- | -- | -- | PASS | +2.6 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 168.0, B 871.0; serve-point win A 51.5%, B 41.9%; Elo A 1070.3, B 1277.7; model uncertainty 0.0387
* Form inputs: days since last match A 187, B 208; matches on record A 135, B 117; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.026, surface_pool_high +0.013, surface_dev_loose -0.004, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lucie Petruzelova vs Maria Eleni Poulka -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221219:266767:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucie Petruzelova (`KXITFWMATCH-26NOV01PETPOU-PET`) | 0.96 / 0.97 (427) | 96.5% | 95.0% | 27.4% | 78.0% [75.6%-79.6%] | -- | -- | -- | -- | PASS | -1.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Eleni Poulka (`KXITFWMATCH-26NOV01PETPOU-POU`) | 0.03 / 0.04 (4508) | 3.5% | 5.0% | 72.6% | 22.0% [20.4%-24.4%] | -- | -- | -- | -- | PASS | +1.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1518.0, B 0.0; serve-point win A 60.8%, B 51.6%; Elo A 1281.7, B 1065.0; model uncertainty 0.0199
* Form inputs: days since last match A 201, B 719; matches on record A 141, B 18; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.024, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nastasja Schunk vs Daria Egorova -- W50 Istanbul F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221768:266864:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daria Egorova (`KXITFWMATCH-26NOV01SCHEGO-EGO`) | 0.57 / 0.59 (154) | 58.0% | 66.3% | 87.4% | 80.3% [59.5%-86.6%] | -- | -- | -- | -- | PASS | +8.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nastasja Schunk (`KXITFWMATCH-26NOV01SCHEGO-SCH`) | 0.41 / 0.42 (133) | 41.5% | 33.7% | 12.6% | 19.7% [13.4%-40.5%] | -- | -- | -- | -- | PASS | -7.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2120.0, B 2142.0; serve-point win A 52.6%, B 44.2%; Elo A 1548.5, B 1672.8; model uncertainty 0.1353
* Form inputs: days since last match A 44, B 32; matches on record A 249, B 86; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.043, surface_pool_high -0.035, surface_dev_loose -0.018, surface_dev_tight +0.019
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Klara Veldman vs Iva Marinkovic -- W15 Taby F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223418:267845:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iva Marinkovic (`KXITFWMATCH-26NOV01VELMAR-MAR`) | 0.39 / 0.47 (47) | 43.0% | 49.7% | 59.5% | 52.1% [50.0%-53.2%] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Klara Veldman (`KXITFWMATCH-26NOV01VELMAR-VEL`) | 0.53 / 0.58 (53) | 55.5% | 50.3% | 40.5% | 47.9% [46.8%-50.0%] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.2 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1299.0, B 542.0; serve-point win A 54.5%, B 45.6%; Elo A 1331.3, B 1321.3; model uncertainty 0.016
* Form inputs: days since last match A 187, B 187; matches on record A 141, B 17; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.011, surface_dev_loose +0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Santiago De la Fuente vs Faustino Boffelli -- ATP Challenger Villa Maria Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 17:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T17:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01DLFBOF:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Faustino Boffelli (`KXATPCHALLENGERMATCH-26NOV01DLFBOF-BOF`) | 0.06 / 0.23 (21) | 14.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Santiago De la Fuente (`KXATPCHALLENGERMATCH-26NOV01DLFBOF-DLF`) | 0.78 / 0.95 (109) | 86.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Lorenzo Gagliardo vs Tadeo Meneo -- ATP Challenger Villa Maria Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 17:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T17:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01GAGMEN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Gagliardo (`KXATPCHALLENGERMATCH-26NOV01GAGMEN-GAG`) | 0.78 / 0.95 (109) | 86.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tadeo Meneo (`KXATPCHALLENGERMATCH-26NOV01GAGMEN-MEN`) | 0.06 / 0.26 (21) | 16.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Ian Luca Vertberger vs Denys Klok -- ATP Challenger Villa Maria Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 17:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T17:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01VERKLO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Denys Klok (`KXATPCHALLENGERMATCH-26NOV01VERKLO-KLO`) | 0.59 / 0.80 (6) | 69.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ian Luca Vertberger (`KXATPCHALLENGERMATCH-26NOV01VERKLO-VER`) | 0.25 / 0.46 (19) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nahia Berecoechea vs Justine Bretnacher -- W75 Petange R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222171:267401:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nahia Berecoechea (`KXITFWMATCH-26NOV01BERBRE-BER`) | 0.90 / 0.97 (303) | 93.5% | 98.1% | 87.3% | 87.6% [86.4%-88.6%] | -- | -- | -- | -- | PASS | +4.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Justine Bretnacher (`KXITFWMATCH-26NOV01BERBRE-BRE`) | 0.03 / 0.07 (8) | 5.0% | 1.9% | 12.7% | 12.4% [11.4%-13.6%] | -- | -- | -- | -- | PASS | -3.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1894.0, B 222.0; serve-point win A 59.4%, B 56.1%; Elo A 1547.8, B 1207.4; model uncertainty 0.011
* Form inputs: days since last match A 201, B 341; matches on record A 250, B 22; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Leila Fabbri vs Anastasiya Kuparev -- W75 Petange R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223032:223398:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leila Fabbri (`KXITFWMATCH-26NOV01FABKUP-FAB`) | 0.25 / 0.34 (29) | 29.5% | 47.0% | 77.2% | 59.5% [57.4%-62.6%] | -- | -- | -- | -- | PASS | +17.5 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anastasiya Kuparev (`KXITFWMATCH-26NOV01FABKUP-KUP`) | 0.62 / 0.71 (37) | 66.5% | 53.0% | 22.8% | 40.5% [37.4%-42.6%] | -- | -- | -- | -- | PASS | -13.5 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 723.0; serve-point win A 54.4%, B 45.0%; Elo A 1247.6, B 1178.2; model uncertainty 0.0257
* Form inputs: days since last match A 726, B 215; matches on record A 3, B 121; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV01FABKUP-FAB  (YES = Leila Fabbri)
Model: 47%
Kalshi: 30%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.031, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jonas Forejtek vs Ryan Seggerman -- ATP Challenger Bratislava II Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 17:50Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T17:50:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01FORSEG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jonas Forejtek (`KXATPCHALLENGERMATCH-26NOV01FORSEG-FOR`) | 0.54 / 0.58 (5) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ryan Seggerman (`KXATPCHALLENGERMATCH-26NOV01FORSEG-SEG`) | 0.37 / 0.45 (3) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Andrej Martin vs Eero Vasa -- ATP Challenger Bratislava II Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 17:50Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T17:50:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01MARVAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrej Martin (`KXATPCHALLENGERMATCH-26NOV01MARVAS-MAR`) | 0.48 / 0.53 (35) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eero Vasa (`KXATPCHALLENGERMATCH-26NOV01MARVAS-VAS`) | 0.43 / 0.49 (11) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Fiona Crawley vs Suzan Lamens -- W75 Glasgow F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215480:220680:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fiona Crawley (`KXITFWMATCH-26NOV01CRALAM-CRA`) | 0.40 / 0.43 (12) | 41.5% | 54.7% | 65.1% | 61.1% [50.5%-65.1%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.2 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Suzan Lamens (`KXITFWMATCH-26NOV01CRALAM-LAM`) | 0.56 / 0.58 (53) | 57.0% | 45.3% | 34.9% | 38.9% [34.9%-49.5%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.7 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2695.0, B 3938.0; serve-point win A 53.0%, B 47.9%; Elo A 1754.6, B 1724.8; model uncertainty 0.073
* Form inputs: days since last match A 22, B 26; matches on record A 131, B 545; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.025, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Christina Bednarczyk vs Gina Marie Dittmann -- W75 Petange R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222273:266695:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Christina Bednarczyk (`KXITFWMATCH-26NOV01BEDDIT-BED`) | 0.06 / 0.14 (14) | 10.0% | 8.0% | 46.3% | 20.4% [18.2%-22.3%] | -- | -- | -- | -- | PASS | -2.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gina Marie Dittmann (`KXITFWMATCH-26NOV01BEDDIT-DIT`) | 0.83 / 0.90 (42) | 86.5% | 92.0% | 53.7% | 79.6% [77.7%-81.8%] | -- | -- | -- | -- | PASS | +5.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 162.0, B 1885.0; serve-point win A 48.7%, B 40.8%; Elo A 1156.2, B 1412.4; model uncertainty 0.0206
* Form inputs: days since last match A 257, B 208; matches on record A 10, B 115; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.015, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gaia Maduzzi vs Hanna Bougouffa -- W75 Petange R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:230121:266431:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hanna Bougouffa (`KXITFWMATCH-26NOV01MADBOU-BOU`) | 0.10 / 0.20 (33) | 15.0% | 8.4% | 27.7% | 22.2% [21.0%-23.0%] | -- | -- | -- | -- | PASS | -6.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gaia Maduzzi (`KXITFWMATCH-26NOV01MADBOU-MAD`) | 0.76 / 0.85 (44) | 80.5% | 91.6% | 72.3% | 77.8% [77.0%-79.0%] | -- | -- | -- | -- | PASS | +11.1 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1969.0, B 245.0; serve-point win A 57.0%, B 53.3%; Elo A 1508.7, B 1280.0; model uncertainty 0.0101
* Form inputs: days since last match A 4, B 460; matches on record A 62, B 134; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.004, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Blaise Bicknell vs Kacper Szymkowiak -- M15 Pembroke F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-01T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209080:212852:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Blaise Bicknell (`KXITFMATCH-26NOV01BICSZY-BIC`) | 0.68 / 0.71 (28) | 69.5% | 60.0% | 46.4% | 58.2% [53.6%-65.0%] | 68.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.5 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kacper Szymkowiak (`KXITFMATCH-26NOV01BICSZY-SZY`) | 0.29 / 0.31 (30) | 30.0% | 40.0% | 53.6% | 41.8% [35.0%-46.4%] | 31.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +10.0 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3719.0, B 1216.0; serve-point win A 60.7%, B 41.2%; Elo A 1497.2, B 1370.4; model uncertainty 0.0571
* Form inputs: days since last match A 33, B 236; matches on record A 233, B 41; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chopra / Kuhar vs Marshall / Slocombe -- M15 Pembroke SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-01T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01CHOKUHMARSLO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chopra / Kuhar (`KXITFDOUBLES-26NOV01CHOKUHMARSLO-CHOKUH`) | 0.07 / 0.89 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marshall / Slocombe (`KXITFDOUBLES-26NOV01CHOKUHMARSLO-MARSLO`) | 0.07 / 0.89 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Cox / Fradkin vs Schachter / Voelzke -- M15 Pembroke SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-01T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01COXFRASCHVOE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cox / Fradkin (`KXITFDOUBLES-26NOV01COXFRASCHVOE-COXFRA`) | 0.07 / 0.89 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Schachter / Voelzke (`KXITFDOUBLES-26NOV01COXFRASCHVOE-SCHVOE`) | 0.07 / 0.89 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Valentini Grammatikopoulou vs Weronika Ewald -- W35 Malta F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:204394:260541:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Weronika Ewald (`KXITFWMATCH-26NOV01GRAEWA-EWA`) | 0.50 / 0.53 (17) | 51.5% | 67.9% | 51.1% | 55.3% [51.1%-60.0%] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +16.4 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valentini Grammatikopoulou (`KXITFWMATCH-26NOV01GRAEWA-GRA`) | 0.45 / 0.48 (8) | 46.5% | 32.1% | 48.9% | 44.7% [40.0%-48.9%] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -14.4 pp | REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2942.0, B 2476.0; serve-point win A 51.7%, B 44.8%; Elo A 1508.1, B 1594.6; model uncertainty 0.0448
* Form inputs: days since last match A 110, B 187; matches on record A 724, B 129; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV01GRAEWA-EWA  (YES = Weronika Ewald)
Model: 68%
Kalshi: 52%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.043, surface_pool_high -0.042, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tomas Martinez vs Oscar Jose Gutierrez -- M15 João Pessoa F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-01T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:121264:211658:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oscar Jose Gutierrez (`KXITFMATCH-26NOV01MARGUT-GUT`) | 0.62 / 0.66 (54) | 64.0% | 53.5% | 47.4% | 53.7% [51.6%-56.2%] | 62.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -10.5 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tomas Martinez (`KXITFMATCH-26NOV01MARGUT-MAR`) | 0.32 / 0.34 (38) | 33.0% | 46.5% | 52.6% | 46.3% [43.8%-48.4%] | 37.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.5 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1526.0, B 2766.0; serve-point win A 56.8%, B 42.5%; Elo A 1246.6, B 1315.8; model uncertainty 0.0234
* Form inputs: days since last match A 40, B 201; matches on record A 59, B 606; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Leonie Schuknecht vs Selina Dal -- W75 Petange R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223399:269943:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Selina Dal (`KXITFWMATCH-26NOV01SCHDAL-DAL`) | 0.81 / 0.90 (42) | 85.5% | 91.1% | 81.7% | 83.5% [81.8%-84.5%] | -- | -- | -- | -- | PASS | +5.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Leonie Schuknecht (`KXITFWMATCH-26NOV01SCHDAL-SCH`) | 0.06 / 0.14 (7) | 10.0% | 8.9% | 18.3% | 16.6% [15.5%-18.2%] | -- | -- | -- | -- | PASS | -1.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 382.0, B 867.0; serve-point win A 49.6%, B 40.3%; Elo A 1290.6, B 1571.0; model uncertainty 0.0136
* Form inputs: days since last match A 271, B 187; matches on record A 9, B 186; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.017, surface_dev_loose -0.006, surface_dev_tight +0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Isabella Maria Serban vs Tina Manescu -- W75 Petange R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:265197:270181:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tina Manescu (`KXITFWMATCH-26NOV01SERMAN-MAN`) | 0.17 / 0.29 (5) | 23.0% | 17.2% | 26.0% | 29.6% [27.3%-31.9%] | -- | -- | -- | -- | PASS | -5.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Isabella Maria Serban (`KXITFWMATCH-26NOV01SERMAN-SER`) | 0.67 / 0.79 (119) | 73.0% | 82.8% | 74.0% | 70.4% [68.0%-72.7%] | -- | -- | -- | -- | PASS | +9.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2134.0, B 446.0; serve-point win A 56.4%, B 50.7%; Elo A 1448.9, B 1307.0; model uncertainty 0.0231
* Form inputs: days since last match A 4, B 187; matches on record A 116, B 11; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.023, surface_pool_high -0.024, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniel Masur vs Georgii Kravchenko -- M25 Malta F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01MASKRA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Georgii Kravchenko (`KXITFMATCH-26NOV01MASKRA-KRA`) | 0.43 / 0.46 (38) | 44.5% | 39.1% | -- | -- [-----] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | -- | -5.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Daniel Masur (`KXITFMATCH-26NOV01MASKRA-MAS`) | 0.53 / 0.56 (30) | 54.5% | 60.9% | -- | -- [-----] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | -- | +6.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 64.2%, B 38.0%; Elo A 1563.3, B 1444.6; model uncertainty None
* Form inputs: days since last match A 40, B 19; matches on record A 772, B 390; data quality A
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luciana Moyano vs Josefina Estevez -- W15 Neuquén F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-01T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV01MOYEST:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Josefina Estevez (`KXITFWMATCH-26NOV01MOYEST-EST`) | 0.38 / 0.39 (40) | 38.5% | 22.0% | -- | -- [-----] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | -- | -16.5 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Luciana Moyano (`KXITFWMATCH-26NOV01MOYEST-MOY`) | 0.55 / 0.58 (97) | 56.5% | 78.0% | -- | -- [-----] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | -- | +21.5 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 50.5%, B 55.3%; Elo A 1454.4, B 1294.6; model uncertainty None
* Form inputs: days since last match A 187, B 292; matches on record A 106, B 55; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV01MOYEST-MOY  (YES = Luciana Moyano)
Model: 78%
Kalshi: 56%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: EVENT_MAPPING_RISK, LOW_DATA_QUALITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Emery Combs vs Malwina Rowinska -- W15 Sumter SC F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-01T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV01COMROW:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emery Combs (`KXITFWMATCH-26NOV01COMROW-COM`) | 0.55 / 0.59 (35) | 57.0% | -- | -- | -- [-----] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Malwina Rowinska (`KXITFWMATCH-26NOV01COMROW-ROW`) | 0.35 / 0.43 (35) | 39.0% | -- | -- | -- [-----] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alina Shcherbinina vs Dana Guzman -- W35 Norman OK F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-01T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV01SHCGUZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dana Guzman (`KXITFWMATCH-26NOV01SHCGUZ-GUZ`) | 0.53 / 0.62 (43) | 57.5% | -- | -- | -- [-----] | 59.9% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alina Shcherbinina (`KXITFWMATCH-26NOV01SHCGUZ-SHC`) | 0.34 / 0.40 (13) | 37.0% | -- | -- | -- [-----] | 40.1% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amandine Hesse vs Carolin Raschdorf -- W75 Petange R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-01T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV01HESRAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amandine Hesse (`KXITFWMATCH-26NOV01HESRAS-HES`) | 0.79 / 0.94 (416) | 86.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Carolin Raschdorf (`KXITFWMATCH-26NOV01HESRAS-RAS`) | 0.03 / 0.17 (23) | 10.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ximena Senties vs Judith Hernandez Miranda -- W50 Huamantla R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-01T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV01SENHER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Judith Hernandez Miranda (`KXITFWMATCH-26NOV01SENHER-HER`) | 0.13 / 0.95 (2) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ximena Senties (`KXITFWMATCH-26NOV01SENHER-SEN`) | 0.04 / 0.89 (57) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Isis Louise Van den Broek vs Onalee Wagner -- W75 Petange R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-01T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV01VANWAG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isis Louise Van den Broek (`KXITFWMATCH-26NOV01VANWAG-VAN`) | 0.06 / 0.95 (2) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Onalee Wagner (`KXITFWMATCH-26NOV01VANWAG-WAG`) | 0.06 / 0.96 (19) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ana Carmen Zamburek vs Prisha Vyas -- W50 Huamantla R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-01T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV01ZAMVYA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Prisha Vyas (`KXITFWMATCH-26NOV01ZAMVYA-VYA`) | 0.05 / 0.85 (100) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ana Carmen Zamburek (`KXITFWMATCH-26NOV01ZAMVYA-ZAM`) | 0.09 / 0.96 (2) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sarai Gabrielle Clarke vs Ashleigh Harvey -- W50 Huamantla R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-01T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV01CLAHAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sarai Gabrielle Clarke (`KXITFWMATCH-26NOV01CLAHAR-CLA`) | 0.05 / 0.95 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ashleigh Harvey (`KXITFWMATCH-26NOV01CLAHAR-HAR`) | 0.04 / 0.96 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Julieta Pareja vs Caroline Dolehide -- W100 New Braunfels TX F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-01T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV01PARDOL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Caroline Dolehide (`KXITFWMATCH-26NOV01PARDOL-DOL`) | 0.04 / 0.45 (45) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Julieta Pareja (`KXITFWMATCH-26NOV01PARDOL-PAR`) | 0.55 / 0.97 (1186) | 76.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Fanny Pire vs Tamila Gadamauri -- W75 Petange R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-01T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV01PIRGAD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tamila Gadamauri (`KXITFWMATCH-26NOV01PIRGAD-GAD`) | 0.81 / 0.94 (416) | 87.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fanny Pire (`KXITFWMATCH-26NOV01PIRGAD-PIR`) | 0.03 / 0.14 (17) | 8.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maria Jose Portillo Ramirez vs Zoe Hitt -- W50 Huamantla R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-01T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV01PORHIT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zoe Hitt (`KXITFWMATCH-26NOV01PORHIT-HIT`) | 0.05 / 0.89 (100) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maria Jose Portillo Ramirez (`KXITFWMATCH-26NOV01PORHIT-POR`) | 0.05 / 0.96 (2) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Leticia Romanova vs Jana Otzipka -- W75 Petange R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-01T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV01ROMOTZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jana Otzipka (`KXITFWMATCH-26NOV01ROMOTZ-OTZ`) | 0.40 / 0.87 (59) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Leticia Romanova (`KXITFWMATCH-26NOV01ROMOTZ-ROM`) | 0.09 / 0.54 (38) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sorana Cirstea vs Maria Timofeeva -- WTA Hong Kong R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · surface ? · scheduled 2026-11-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26NOV01CIRTIM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sorana Cirstea (`KXWTAMATCH-26NOV01CIRTIM-CIR`) | 0.69 / 0.72 (201) | 70.5% | -- | -- | -- [-----] | -- | 71.0% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maria Timofeeva (`KXWTAMATCH-26NOV01CIRTIM-TIM`) | 0.27 / 0.31 (6) | 29.0% | -- | -- | -- [-----] | -- | 29.3% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Leylah Fernandez vs Sofia Kenin -- WTA Hong Kong R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · surface ? · scheduled 2026-11-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26NOV01FERKEN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leylah Fernandez (`KXWTAMATCH-26NOV01FERKEN-FER`) | 0.72 / 0.73 (6) | 72.5% | -- | -- | -- [-----] | -- | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sofia Kenin (`KXWTAMATCH-26NOV01FERKEN-KEN`) | 0.25 / 0.28 (4) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Talia Gibson vs Oleksandra Oliynykova -- WTA Hong Kong R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · surface ? · scheduled 2026-11-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26NOV01GIBOLI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Talia Gibson (`KXWTAMATCH-26NOV01GIBOLI-GIB`) | 0.81 / 0.83 (97) | 82.0% | -- | -- | -- [-----] | -- | 82.3% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Oleksandra Oliynykova (`KXWTAMATCH-26NOV01GIBOLI-OLI`) | 0.16 / 0.19 (6) | 17.5% | -- | -- | -- [-----] | -- | 17.8% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Viktorija Golubic vs Katie Boulter -- WTA Hong Kong R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · surface ? · scheduled 2026-11-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26NOV01GOLBOU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katie Boulter (`KXWTAMATCH-26NOV01GOLBOU-BOU`) | 0.58 / 0.61 (39) | 59.5% | -- | -- | -- [-----] | -- | 60.7% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Viktorija Golubic (`KXWTAMATCH-26NOV01GOLBOU-GOL`) | 0.38 / 0.42 (87) | 40.0% | -- | -- | -- [-----] | -- | 39.0% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Maddison Inglis vs Maya Joint -- WTA Hong Kong R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · surface ? · scheduled 2026-11-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26NOV01INGJOI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maddison Inglis (`KXWTAMATCH-26NOV01INGJOI-ING`) | 0.21 / 0.24 (6) | 22.5% | -- | -- | -- [-----] | -- | 23.2% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maya Joint (`KXWTAMATCH-26NOV01INGJOI-JOI`) | 0.76 / 0.78 (165) | 77.0% | -- | -- | -- [-----] | -- | 76.7% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alycia Parks vs Alexandra Eala -- WTA Hong Kong R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · surface ? · scheduled 2026-11-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26NOV01PAREAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandra Eala (`KXWTAMATCH-26NOV01PAREAL-EAL`) | 0.79 / 0.81 (6) | 80.0% | -- | -- | -- [-----] | -- | 80.0% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alycia Parks (`KXWTAMATCH-26NOV01PAREAL-PAR`) | 0.19 / 0.22 (2236) | 20.5% | -- | -- | -- [-----] | -- | 20.1% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kaitlin Quevedo vs Paula Badosa -- WTA Hong Kong R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · surface ? · scheduled 2026-11-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26NOV01QUEBAD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Paula Badosa (`KXWTAMATCH-26NOV01QUEBAD-BAD`) | 0.67 / 0.68 (135) | 67.5% | -- | -- | -- [-----] | -- | 41.0% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kaitlin Quevedo (`KXWTAMATCH-26NOV01QUEBAD-QUE`) | 0.31 / 0.36 (79) | 33.5% | -- | -- | -- [-----] | -- | 28.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Antonia Ruzic vs Alina Charaeva -- WTA Hong Kong R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · surface ? · scheduled 2026-11-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26NOV01RUZCHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alina Charaeva (`KXWTAMATCH-26NOV01RUZCHA-CHA`) | 0.54 / 0.58 (154) | 56.0% | -- | -- | -- [-----] | -- | 55.4% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Antonia Ruzic (`KXWTAMATCH-26NOV01RUZCHA-RUZ`) | 0.42 / 0.46 (80) | 44.0% | -- | -- | -- [-----] | -- | 44.8% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE

## Xinran Sun vs Tereza Valentova -- WTA Hong Kong R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · surface ? · scheduled 2026-11-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26NOV01SUNVAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xinran Sun (`KXWTAMATCH-26NOV01SUNVAL-SUN`) | 0.26 / 0.28 (10) | 27.0% | -- | -- | -- [-----] | -- | 28.9% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tereza Valentova (`KXWTAMATCH-26NOV01SUNVAL-VAL`) | 0.72 / 0.73 (6) | 72.5% | -- | -- | -- [-----] | -- | 72.3% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Xinyu Wang vs Adithya Karunaratne -- WTA Hong Kong R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · surface ? · scheduled 2026-11-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26NOV01WANKAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adithya Karunaratne (`KXWTAMATCH-26NOV01WANKAR-KAR`) | 0.08 / 0.10 (53) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xinyu Wang (`KXWTAMATCH-26NOV01WANKAR-WAN`) | 0.90 / 0.91 (1) | 90.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Venus Williams vs Mary Stoiana -- WTA Hong Kong R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · surface ? · scheduled 2026-11-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26NOV01WILSTO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mary Stoiana (`KXWTAMATCH-26NOV01WILSTO-STO`) | 0.84 / 0.86 (209) | 85.0% | -- | -- | -- [-----] | -- | 86.4% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Venus Williams (`KXWTAMATCH-26NOV01WILSTO-WIL`) | 0.13 / 0.16 (4) | 14.5% | -- | -- | -- [-----] | -- | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dayana Yastremska vs Zeynep Sonmez -- WTA Hong Kong R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 02:34Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · surface ? · scheduled 2026-11-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26NOV01YASSON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zeynep Sonmez (`KXWTAMATCH-26NOV01YASSON-SON`) | 0.46 / 0.50 (196) | 48.0% | -- | -- | -- [-----] | -- | 47.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dayana Yastremska (`KXWTAMATCH-26NOV01YASSON-YAS`) | 0.50 / 0.54 (6) | 52.0% | -- | -- | -- [-----] | -- | 50.8% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
