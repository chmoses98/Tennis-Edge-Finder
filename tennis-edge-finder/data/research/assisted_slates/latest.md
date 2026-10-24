# ASSISTED SLATE -- 2026-10-24T00:31Z (`SL-20261024T003118Z-9856ec47`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

144 open matches not seen started, 612 markets. Skipped: {"no_play_confirmed": 1, "scheduled_start_over_24h_past": 2, "no_match_winner_listed": 1}. Sources: shadow board 2026-10-23T21:53:47.814172+00:00, Model 4 2026-10-23T21:54:36.049296+00:00, Gen-1 ledger 2026-10-23T21:53:42.981313+00:00, external 2026-10-24T00:09:03.216937+00:00, capture 20261024T000710Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-10-24 01:30Z**
* Recommended RUN TENNIS time: **2026-10-24 00:45Z**
* Final price/status check time: **2026-10-24 01:20Z**
* Number of matches in window: 9 (Liudmila Samsonova vs Heather Watson, Yuliia Starodubtseva vs Aliaksandra Sasnovich, Shiho Tsujioka vs Kamilla Rakhimova, Ann Li vs Ashlyn Krueger, Polina Iatcenko vs Alexandra Shubladze, Maya Joint vs Viktorija Golubic ...)

Slate built 2026-10-24T00:31Z. Refresh due by: 2026-10-24 00:45Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 31, "HIGH_REVIEW": 52, "NORMAL": 300, "REVIEW": 62, "UNPRICED": 167}; match winners: {"EXTREME": 18, "HIGH_REVIEW": 28, "NORMAL": 116, "REVIEW": 20, "UNPRICED": 106}; quote freshness at build: {"FRESH": 445}.

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
| Francesco Forti (`KXATPCHALLENGERMATCH-26OCT23FORROC-FOR`) | 0.22 / 0.23 (552) | 22.5% | 55.4% | 56.5% | 53.0% [47.5%-55.5%] | -- | -- | -- | -- | WATCH | +32.9 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oriol Roca Batalla (`KXATPCHALLENGERMATCH-26OCT23FORROC-ROC`) | 0.76 / 0.77 (2907) | 76.5% | 44.6% | 43.5% | 47.0% [44.5%-52.5%] | -- | -- | -- | -- | PASS | -31.9 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1932.0, B 2870.0; serve-point win A 63.2%, B 37.9%; Elo A 1495.2, B 1504.8; model uncertainty 0.0404
* Form inputs: days since last match A 11, B 11; matches on record A 373, B 981; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT23FORROC-FOR  (YES = Francesco Forti)
Model: 55%
Kalshi: 22%
Gap: +33 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose +0.020, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE

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
| Juan Jose Bianchi / Jakub Vrba (`KXATPCHALLENGERDOUBLES-26OCT23HERHOUBIAVRB-BIAVRB`) | 0.10 / 0.72 (1) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mats Hermans / Max Houkes (`KXATPCHALLENGERDOUBLES-26OCT23HERHOUBIAVRB-HERHOU`) | 0.06 / 0.86 (1) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Diego Hidalgo / Mariano Kestelboim vs Alan Magadan / Rodrigo Pacheco Mendez -- ATP Challenger Cali SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-24T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT23HIDKESMAGPAC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diego Hidalgo / Mariano Kestelboim (`KXATPCHALLENGERDOUBLES-26OCT23HIDKESMAGPAC-HIDKES`) | 0.34 / 0.50 (69) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alan Magadan / Rodrigo Pacheco Mendez (`KXATPCHALLENGERDOUBLES-26OCT23HIDKESMAGPAC-MAGPAC`) | 0.58 / 0.63 (50) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Liudmila Samsonova vs Heather Watson -- WTA Tokyo Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 04:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 01:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 00:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T04:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:201586:214643:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liudmila Samsonova (`KXWTAMATCH-26OCT23SAMWAT-SAM`) | 0.86 / 0.87 (1) | 86.5% | 76.8% | 73.0% | 73.4% [71.7%-75.6%] | 85.3% | 87.8% | 86.6% | MODEL_LONE_OUTLIER | PASS | -9.7 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Heather Watson (`KXWTAMATCH-26OCT23SAMWAT-WAT`) | 0.12 / 0.14 (10025) | 13.0% | 23.2% | 27.0% | 26.6% [24.4%-28.3%] | 14.7% | 12.8% | 13.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +10.2 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3968.0, B 2194.0; serve-point win A 61.7%, B 44.0%; Elo A 1909.6, B 1734.1; model uncertainty 0.0198
* Form inputs: days since last match A 4, B 6; matches on record A 540, B 821; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.017, surface_pool_high -0.017, surface_dev_loose -0.009, surface_dev_tight +0.004
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT23SAMWAT-2-WAT` Will Heather Watson win set 2 in the Liudmila Samsonova vs Heather Watson match: 0.15/0.20 mid 17.5%, model 31.2% (projection_v2.0 (prediction ledger)) -- gap +13.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23SAMWAT-1-SAM` Will Liudmila Samsonova win set 1 in the Liudmila Samsonova vs Heather Watson match: 0.80/0.83 mid 81.5%, model 68.8% (projection_v2.0 (prediction ledger)) -- gap -12.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23SAMWAT-1-WAT` Will Heather Watson win set 1 in the Liudmila Samsonova vs Heather Watson match: 0.17/0.20 mid 18.5%, model 31.2% (projection_v2.0 (prediction ledger)) -- gap +12.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23SAMWAT-2-SAM` Will Liudmila Samsonova win set 2 in the Liudmila Samsonova vs Heather Watson match: 0.79/0.83 mid 81.0%, model 68.8% (projection_v2.0 (prediction ledger)) -- gap -12.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE

## Yuliia Starodubtseva vs Aliaksandra Sasnovich -- WTA Tokyo Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 04:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 01:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 00:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T04:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:205925:263857:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aliaksandra Sasnovich (`KXWTAMATCH-26OCT23STASAS-SAS`) | 0.57 / 0.59 (5947) | 58.0% | 49.2% | 50.5% | 51.1% [51.1%-54.8%] | -- | 57.7% | 57.7% | MODEL_LONE_OUTLIER | PASS | -8.8 pp | NORMAL | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Yuliia Starodubtseva (`KXWTAMATCH-26OCT23STASAS-STA`) | 0.43 / 0.44 (12159) | 43.5% | 50.8% | 49.5% | 48.9% [45.2%-48.9%] | -- | 42.2% | 42.2% | MARKETS_AGREE | WATCH | +7.3 pp | NORMAL | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4584.0, B 4822.0; serve-point win A 55.7%, B 44.4%; Elo A 1802.8, B 1842.1; model uncertainty 0.0185
* Form inputs: days since last match A 6, B 2; matches on record A 262, B 792; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.011
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT23STASAS-2-STA` Will Yuliia Starodubtseva win set 2 in the Yuliia Starodubtseva vs Aliaksandra Sasnovich match: 0.41/0.44 mid 42.5%, model 50.5% (projection_v2.0 (prediction ledger)) -- gap +8.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT23STASAS-1-STA` Will Yuliia Starodubtseva win set 1 in the Yuliia Starodubtseva vs Aliaksandra Sasnovich match: 0.42/0.45 mid 43.5%, model 50.5% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT23STASAS-1-SAS` Will Aliaksandra Sasnovich win set 1 in the Yuliia Starodubtseva vs Aliaksandra Sasnovich match: 0.54/0.58 mid 56.0%, model 49.5% (projection_v2.0 (prediction ledger)) -- gap -6.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT23STASAS-2-SAS` Will Aliaksandra Sasnovich win set 2 in the Yuliia Starodubtseva vs Aliaksandra Sasnovich match: 0.54/0.58 mid 56.0%, model 49.5% (projection_v2.0 (prediction ledger)) -- gap -6.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER

## Shiho Tsujioka vs Kamilla Rakhimova -- WTA Tokyo Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 04:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 01:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 00:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T04:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215872:263801:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kamilla Rakhimova (`KXWTAMATCH-26OCT23TSURAK-RAK`) | 0.94 / 0.95 (800) | 94.5% | 92.9% | 74.9% | 87.5% [82.6%-93.5%] | 94.0% | 95.8% | 94.9% | MODEL_LONE_OUTLIER | PASS | -1.6 pp | NORMAL | FRESH | C / LIMITED | ALL_AGREE | VERIFIED |
| Shiho Tsujioka (`KXWTAMATCH-26OCT23TSURAK-TSU`) | 0.06 / 0.07 (14502) | 6.5% | 7.1% | 25.1% | 12.5% [6.5%-17.4%] | 6.0% | 4.8% | 5.4% | MODEL_LONE_OUTLIER | WATCH | +0.6 pp | NORMAL | FRESH | C / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 1131.0, B 5718.0; serve-point win A 47.5%, B 41.5%; Elo A 1384.6, B 1844.5; model uncertainty 0.0548
* Form inputs: days since last match A 186, B 4; matches on record A 42, B 478; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.023, surface_dev_loose -0.000, surface_dev_tight +0.003
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT23TSURAK-1-RAK` Will Kamilla Rakhimova win set 1 in the Shiho Tsujioka vs Kamilla Rakhimova match: 0.90/0.92 mid 91.0%, model 83.8% (projection_v2.0 (prediction ledger)) -- gap -7.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT23TSURAK-1-TSU` Will Shiho Tsujioka win set 1 in the Shiho Tsujioka vs Kamilla Rakhimova match: 0.08/0.10 mid 9.0%, model 16.2% (projection_v2.0 (prediction ledger)) -- gap +7.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT23TSURAK-2-TSU` Will Shiho Tsujioka win set 2 in the Shiho Tsujioka vs Kamilla Rakhimova match: 0.08/0.10 mid 9.0%, model 16.2% (projection_v2.0 (prediction ledger)) -- gap +7.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT23TSURAK-2-RAK` Will Kamilla Rakhimova win set 2 in the Shiho Tsujioka vs Kamilla Rakhimova match: 0.81/0.93 mid 87.0%, model 83.8% (projection_v2.0 (prediction ledger)) -- gap -3.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Bruno (2002) Oliveira / Natan Rodrigues vs Federico Zeballos / Marcelo Zormann -- ATP Challenger Cali SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-24T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT23OLIRODZEBZOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bruno (2002) Oliveira / Natan Rodrigues (`KXATPCHALLENGERDOUBLES-26OCT23OLIRODZEBZOR-OLIROD`) | 0.41 / 0.58 (6) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Federico Zeballos / Marcelo Zormann (`KXATPCHALLENGERDOUBLES-26OCT23OLIRODZEBZOR-ZEBZOR`) | 0.42 / 0.59 (5) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ann Li vs Ashlyn Krueger -- WTA Osaka SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 03:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 02:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215983:221909:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ann Li (`KXWTAMATCH-26OCT23ANNKRU-ANN`) | 0.59 / 0.60 (1933) | 59.5% | 56.2% | 63.7% | 60.7% [57.3%-62.2%] | 59.4% | 59.9% | 59.7% | MARKETS_AGREE | PASS | -3.3 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Ashlyn Krueger (`KXWTAMATCH-26OCT23ANNKRU-KRU`) | 0.39 / 0.41 (54298) | 40.0% | 43.8% | 36.3% | 39.3% [37.8%-42.7%] | 40.6% | 40.2% | 40.4% | MARKETS_AGREE | PASS | +3.8 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4567.0, B 4211.0; serve-point win A 60.4%, B 40.8%; Elo A 1921.8, B 1900.5; model uncertainty 0.0247
* Form inputs: days since last match A 0, B 0; matches on record A 474, B 344; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.000, surface_dev_loose +0.010, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT23ANNKRU-28` Over 27.5 games: 0.26/0.27 mid 26.5%, model 36.9% (projection_v2.0 (prediction ledger)) -- gap +10.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT23ANNKRU-23` Over 22.5 games: 0.48/0.49 mid 48.5%, model 57.8% (projection_v2.0 (prediction ledger)) -- gap +9.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT23ANNKRU-18` Over 17.5 games: 0.80/0.83 mid 81.5%, model 90.3% (projection_v2.0 (prediction ledger)) -- gap +8.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT23ANNKRU-2-KRU` Will Ashlyn Krueger win set 2 in the Ann Li vs Ashlyn Krueger match: 0.40/0.44 mid 42.0%, model 45.8% (projection_v2.0 (prediction ledger)) -- gap +3.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23ANNKRU-1-KRU` Will Ashlyn Krueger win set 1 in the Ann Li vs Ashlyn Krueger match: 0.43/0.44 mid 43.5%, model 45.8% (projection_v2.0 (prediction ledger)) -- gap +2.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23ANNKRU-2-ANN` Will Ann Li win set 2 in the Ann Li vs Ashlyn Krueger match: 0.55/0.58 mid 56.5%, model 54.2% (projection_v2.0 (prediction ledger)) -- gap -2.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23ANNKRU-1-ANN` Will Ann Li win set 1 in the Ann Li vs Ashlyn Krueger match: 0.55/0.56 mid 55.5%, model 54.2% (projection_v2.0 (prediction ledger)) -- gap -1.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE

## Polina Iatcenko vs Alexandra Shubladze -- WTA Guangzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 03:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 02:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:223325:260168:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Iatcenko (`KXWTAMATCH-26OCT23IATSHU-IAT`) | 0.31 / 0.33 (5094) | 32.0% | 38.9% | 26.6% | 34.0% [30.6%-39.5%] | -- | -- | -- | -- | PASS | +6.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexandra Shubladze (`KXWTAMATCH-26OCT23IATSHU-SHU`) | 0.67 / 0.69 (4580) | 68.0% | 61.1% | 73.5% | 66.0% [60.5%-69.4%] | -- | -- | -- | -- | PASS | -6.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2951.0, B 3247.0; serve-point win A 53.5%, B 44.3%; Elo A 1761.4, B 1759.9; model uncertainty 0.0443
* Form inputs: days since last match A 11, B 19; matches on record A 299, B 206; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.024, surface_pool_high +0.025, surface_dev_loose -0.010, surface_dev_tight +0.010
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT23IATSHU-2-IAT` Will Polina Iatcenko win set 2 in the Polina Iatcenko vs Alexandra Shubladze match: 0.33/0.38 mid 35.5%, model 42.5% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23IATSHU-2-SHU` Will Alexandra Shubladze win set 2 in the Polina Iatcenko vs Alexandra Shubladze match: 0.62/0.67 mid 64.5%, model 57.5% (projection_v2.0 (prediction ledger)) -- gap -7.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23IATSHU-1-IAT` Will Polina Iatcenko win set 1 in the Polina Iatcenko vs Alexandra Shubladze match: 0.34/0.38 mid 36.0%, model 42.5% (projection_v2.0 (prediction ledger)) -- gap +6.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23IATSHU-1-SHU` Will Alexandra Shubladze win set 1 in the Polina Iatcenko vs Alexandra Shubladze match: 0.62/0.64 mid 63.0%, model 57.5% (projection_v2.0 (prediction ledger)) -- gap -5.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Maya Joint vs Viktorija Golubic -- WTA Tokyo Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 04:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 03:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 02:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T04:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:203530:233741:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Viktorija Golubic (`KXWTAMATCH-26OCT23JOIGOL-GOL`) | 0.46 / 0.48 (6164) | 47.0% | 50.3% | 52.7% | 53.7% [52.7%-54.8%] | 46.8% | 46.6% | 46.7% | MARKETS_AGREE | SHADOW_BET | +3.3 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Maya Joint (`KXWTAMATCH-26OCT23JOIGOL-JOI`) | 0.52 / 0.54 (4815) | 53.0% | 49.7% | 47.3% | 46.3% [45.2%-47.3%] | 53.2% | 53.1% | 53.2% | MARKETS_AGREE | PASS | -3.3 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3855.0, B 4714.0; serve-point win A 53.7%, B 46.2%; Elo A 1825.3, B 1859.2; model uncertainty 0.0106
* Form inputs: days since last match A 3, B 2; matches on record A 239, B 833; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.005, surface_dev_loose -0.005, surface_dev_tight +0.011
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT23JOIGOL-1-GOL` Will Viktorija Golubic win set 1 in the Maya Joint vs Viktorija Golubic match: 0.45/0.47 mid 46.0%, model 50.2% (projection_v2.0 (prediction ledger)) -- gap +4.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23JOIGOL-1-JOI` Will Maya Joint win set 1 in the Maya Joint vs Viktorija Golubic match: 0.52/0.54 mid 53.0%, model 49.8% (projection_v2.0 (prediction ledger)) -- gap -3.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23JOIGOL-2-GOL` Will Viktorija Golubic win set 2 in the Maya Joint vs Viktorija Golubic match: 0.45/0.49 mid 47.0%, model 50.2% (projection_v2.0 (prediction ledger)) -- gap +3.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23JOIGOL-2-JOI` Will Maya Joint win set 2 in the Maya Joint vs Viktorija Golubic match: 0.50/0.54 mid 52.0%, model 49.8% (projection_v2.0 (prediction ledger)) -- gap -2.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE

## Polina Kudermetova vs Alevtina Ibragimova -- WTA Guangzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 03:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 02:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:221236:260581:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alevtina Ibragimova (`KXWTAMATCH-26OCT23KUDIBR-IBR`) | 0.29 / 0.30 (1139) | 29.5% | 31.1% | 40.6% | 37.6% [34.1%-39.1%] | 29.9% | 30.6% | 30.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +1.6 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Polina Kudermetova (`KXWTAMATCH-26OCT23KUDIBR-KUD`) | 0.70 / 0.71 (5853) | 70.5% | 68.9% | 59.4% | 62.4% [60.9%-65.9%] | 70.1% | 70.0% | 70.0% | MODEL_LONE_OUTLIER | PASS | -1.6 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4285.0, B 2867.0; serve-point win A 59.2%, B 44.6%; Elo A 1814.3, B 1688.5; model uncertainty 0.0251
* Form inputs: days since last match A 1, B 18; matches on record A 391, B 201; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight +0.005
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT23KUDIBR-2-IBR` Will Alevtina Ibragimova win set 2 in the Polina Kudermetova vs Alevtina Ibragimova match: 0.30/0.37 mid 33.5%, model 37.1% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23KUDIBR-2-KUD` Will Polina Kudermetova win set 2 in the Polina Kudermetova vs Alevtina Ibragimova match: 0.63/0.70 mid 66.5%, model 62.9% (projection_v2.0 (prediction ledger)) -- gap -3.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23KUDIBR-1-IBR` Will Alevtina Ibragimova win set 1 in the Polina Kudermetova vs Alevtina Ibragimova match: 0.35/0.36 mid 35.5%, model 37.1% (projection_v2.0 (prediction ledger)) -- gap +1.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23KUDIBR-1-KUD` Will Polina Kudermetova win set 1 in the Polina Kudermetova vs Alevtina Ibragimova match: 0.63/0.65 mid 64.0%, model 62.9% (projection_v2.0 (prediction ledger)) -- gap -1.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Oleksandra Oliynykova vs Mai Hontama -- WTA Tokyo Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 04:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 03:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 02:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T04:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215988:220716:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mai Hontama (`KXWTAMATCH-26OCT23OLIHON-HON`) | 0.47 / 0.49 (4295) | 48.0% | 45.1% | 27.4% | 33.5% [30.6%-38.5%] | 48.9% | 47.7% | 48.3% | MODEL_LONE_OUTLIER | PASS | -2.9 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Oleksandra Oliynykova (`KXWTAMATCH-26OCT23OLIHON-OLI`) | 0.51 / 0.52 (1851) | 51.5% | 54.9% | 72.6% | 66.5% [61.6%-69.4%] | 51.1% | 52.4% | 51.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +3.4 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4041.0, B 4001.0; serve-point win A 54.6%, B 46.4%; Elo A 1653.4, B 1671.5; model uncertainty 0.0393
* Form inputs: days since last match A 3, B 4; matches on record A 439, B 490; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.030, surface_dev_loose -0.015, surface_dev_tight +0.010
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT23OLIHON-1-OLI` Will Oleksandra Oliynykova win set 1 in the Oleksandra Oliynykova vs Mai Hontama match: 0.49/0.52 mid 50.5%, model 53.3% (projection_v2.0 (prediction ledger)) -- gap +2.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23OLIHON-2-OLI` Will Oleksandra Oliynykova win set 2 in the Oleksandra Oliynykova vs Mai Hontama match: 0.49/0.52 mid 50.5%, model 53.3% (projection_v2.0 (prediction ledger)) -- gap +2.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23OLIHON-1-HON` Will Mai Hontama win set 1 in the Oleksandra Oliynykova vs Mai Hontama match: 0.48/0.50 mid 49.0%, model 46.7% (projection_v2.0 (prediction ledger)) -- gap -2.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23OLIHON-2-HON` Will Mai Hontama win set 2 in the Oleksandra Oliynykova vs Mai Hontama match: 0.45/0.50 mid 47.5%, model 46.7% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER

## Ena Shibahara vs Alycia Parks -- WTA Tokyo Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 04:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 03:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 02:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T04:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214262:219917:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alycia Parks (`KXWTAMATCH-26OCT23SHIPAR-PAR`) | 0.55 / 0.56 (2264) | 55.5% | 66.3% | 67.6% | 66.7% [64.1%-67.1%] | 54.3% | 55.7% | 55.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +10.8 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Ena Shibahara (`KXWTAMATCH-26OCT23SHIPAR-SHI`) | 0.44 / 0.45 (29240) | 44.5% | 33.7% | 32.4% | 33.3% [32.9%-35.9%] | 45.7% | 44.5% | 45.1% | MODEL_LONE_OUTLIER | PASS | -10.8 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3247.0, B 5263.0; serve-point win A 60.4%, B 36.3%; Elo A 1672.6, B 1769.5; model uncertainty 0.0152
* Form inputs: days since last match A 3, B 3; matches on record A 250, B 439; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.004, surface_dev_tight +0.013
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER

## Jenna DeFalco vs Jana Hossam Salah -- W35 Bakersfield CA QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 03:45Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T03:45:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221914:266764:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jenna DeFalco (`KXITFWMATCH-26OCT23DEFHOS-DEF`) | 0.38 / 0.41 (107) | 39.5% | -- | 40.5% | 57.9% [53.7%-61.6%] | -- | -- | -- | -- | PASS | +18.4 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jana Hossam Salah (`KXITFWMATCH-26OCT23DEFHOS-HOS`) | 0.59 / 0.62 (275) | 60.5% | -- | 59.5% | 42.1% [38.4%-46.3%] | -- | -- | -- | -- | PASS | -18.4 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1687.0, B 378.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0393
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT23DEFHOS-DEF  (YES = Jenna DeFalco)
Model: 58%
Kalshi: 40%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kimberly Birrell vs Aoi Ito -- WTA Tokyo Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 04:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 04:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 03:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T04:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214040:256684:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kimberly Birrell (`KXWTAMATCH-26OCT23BIRITO-BIR`) | 0.70 / 0.71 (2250) | 70.5% | 71.9% | 76.3% | 72.5% [69.8%-73.8%] | 70.1% | 71.2% | 70.7% | MARKETS_AGREE | PASS | +1.4 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Aoi Ito (`KXWTAMATCH-26OCT23BIRITO-ITO`) | 0.30 / 0.31 (11099) | 30.5% | 28.1% | 23.7% | 27.5% [26.2%-30.2%] | 29.9% | 29.3% | 29.6% | MARKETS_AGREE | PASS | -2.4 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5020.0, B 2722.0; serve-point win A 57.6%, B 46.8%; Elo A 1875.3, B 1762.1; model uncertainty 0.0202
* Form inputs: days since last match A 10, B 5; matches on record A 476, B 303; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.013, surface_dev_loose +0.009, surface_dev_tight -0.004
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT23BIRITO-2-BIR` Will Kimberly Birrell win set 2 in the Kimberly Birrell vs Aoi Ito match: 0.26/0.90 mid 58.0%, model 65.0% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23BIRITO-2-ITO` Will Aoi Ito win set 2 in the Kimberly Birrell vs Aoi Ito match: 0.14/0.59 mid 36.5%, model 35.0% (projection_v2.0 (prediction ledger)) -- gap -1.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23BIRITO-1-BIR` Will Kimberly Birrell win set 1 in the Kimberly Birrell vs Aoi Ito match: 0.64/0.68 mid 66.0%, model 65.0% (projection_v2.0 (prediction ledger)) -- gap -1.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23BIRITO-1-ITO` Will Aoi Ito win set 1 in the Kimberly Birrell vs Aoi Ito match: 0.34/0.35 mid 34.5%, model 35.0% (projection_v2.0 (prediction ledger)) -- gap +0.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Katie Boulter vs Katerina Siniakova -- WTA Osaka SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 04:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 03:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211107:211701:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katie Boulter (`KXWTAMATCH-26OCT23BOUSIN-BOU`) | 0.38 / 0.39 (3772) | 38.5% | 46.3% | 46.3% | 46.3% [45.8%-46.8%] | 39.1% | 38.3% | 38.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +7.8 pp | NORMAL | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Katerina Siniakova (`KXWTAMATCH-26OCT23BOUSIN-SIN`) | 0.60 / 0.61 (2008) | 60.5% | 53.7% | 53.7% | 53.7% [53.2%-54.2%] | 60.9% | 61.6% | 61.2% | MODEL_LONE_OUTLIER | PASS | -6.8 pp | NORMAL | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3928.0, B 4278.0; serve-point win A 55.7%, B 43.6%; Elo A 1894.6, B 1921.3; model uncertainty 0.0053
* Form inputs: days since last match A 0, B 0; matches on record A 593, B 723; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT23BOUSIN-23` Over 22.5 games: 0.45/0.46 mid 45.5%, model 56.2% (projection_v2.0 (prediction ledger)) -- gap +10.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT23BOUSIN-18` Over 17.5 games: 0.78/0.79 mid 78.5%, model 87.9% (projection_v2.0 (prediction ledger)) -- gap +9.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT23BOUSIN-28` Over 27.5 games: 0.26/0.27 mid 26.5%, model 34.4% (projection_v2.0 (prediction ledger)) -- gap +7.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT23BOUSIN-2-BOU` Will Katie Boulter win set 2 in the Katie Boulter vs Katerina Siniakova match: 0.38/0.42 mid 40.0%, model 47.5% (projection_v2.0 (prediction ledger)) -- gap +7.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT23BOUSIN-1-BOU` Will Katie Boulter win set 1 in the Katie Boulter vs Katerina Siniakova match: 0.39/0.43 mid 41.0%, model 47.5% (projection_v2.0 (prediction ledger)) -- gap +6.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT23BOUSIN-2-SIN` Will Katerina Siniakova win set 2 in the Katie Boulter vs Katerina Siniakova match: 0.57/0.60 mid 58.5%, model 52.5% (projection_v2.0 (prediction ledger)) -- gap -6.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT23BOUSIN-1-SIN` Will Katerina Siniakova win set 1 in the Katie Boulter vs Katerina Siniakova match: 0.57/0.59 mid 58.0%, model 52.5% (projection_v2.0 (prediction ledger)) -- gap -5.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE

## Kayla Day vs Shuai Zhang -- WTA Tokyo Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 04:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 04:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 03:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T04:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:201533:215037:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kayla Day (`KXWTAMATCH-26OCT23DAYZHA-DAY`) | 0.47 / 0.48 (22) | 47.5% | 52.7% | 60.8% | 53.6% [45.3%-56.7%] | -- | -- | -- | -- | WATCH | +5.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Shuai Zhang (`KXWTAMATCH-26OCT23DAYZHA-ZHA`) | 0.52 / 0.53 (1750) | 52.5% | 47.3% | 39.2% | 46.4% [43.3%-54.7%] | -- | -- | -- | -- | PASS | -5.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3639.0, B 3846.0; serve-point win A 58.9%, B 41.6%; Elo A 1748.9, B 1845.2; model uncertainty 0.0572
* Form inputs: days since last match A 1, B 3; matches on record A 481, B 1068; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.010, surface_dev_tight -0.010
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT23DAYZHA-2-ZHA` Will Shuai Zhang win set 2 in the Kayla Day vs Shuai Zhang match: 0.26/0.84 mid 55.0%, model 48.2% (projection_v2.0 (prediction ledger)) -- gap -6.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23DAYZHA-1-DAY` Will Kayla Day win set 1 in the Kayla Day vs Shuai Zhang match: 0.48/0.50 mid 49.0%, model 51.8% (projection_v2.0 (prediction ledger)) -- gap +2.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23DAYZHA-1-ZHA` Will Shuai Zhang win set 1 in the Kayla Day vs Shuai Zhang match: 0.50/0.52 mid 51.0%, model 48.2% (projection_v2.0 (prediction ledger)) -- gap -2.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23DAYZHA-2-DAY` Will Kayla Day win set 2 in the Kayla Day vs Shuai Zhang match: 0.16/0.84 mid 50.0%, model 51.8% (projection_v2.0 (prediction ledger)) -- gap +1.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Elena Pridankina vs Tyra Caterina Grant -- WTA Guangzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 04:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 03:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:239389:261972:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tyra Caterina Grant (`KXWTAMATCH-26OCT23PRIGRA-GRA`) | 0.44 / 0.46 (11393) | 45.0% | 52.7% | 51.0% | 51.0% [47.9%-52.1%] | -- | -- | -- | -- | WATCH | +7.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elena Pridankina (`KXWTAMATCH-26OCT23PRIGRA-PRI`) | 0.54 / 0.55 (5) | 54.5% | 47.3% | 48.9% | 48.9% [47.9%-52.1%] | -- | -- | -- | -- | PASS | -7.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3685.0, B 2460.0; serve-point win A 57.8%, B 41.7%; Elo A 1722.6, B 1729.8; model uncertainty 0.021
* Form inputs: days since last match A 16, B 6; matches on record A 287, B 116; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose +0.000, surface_dev_tight -0.005
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT23PRIGRA-2-PRI` Will Elena Pridankina win set 2 in the Elena Pridankina vs Tyra Caterina Grant match: 0.26/0.84 mid 55.0%, model 48.2% (projection_v2.0 (prediction ledger)) -- gap -6.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23PRIGRA-1-GRA` Will Tyra Caterina Grant win set 1 in the Elena Pridankina vs Tyra Caterina Grant match: 0.44/0.47 mid 45.5%, model 51.8% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23PRIGRA-1-PRI` Will Elena Pridankina win set 1 in the Elena Pridankina vs Tyra Caterina Grant match: 0.53/0.54 mid 53.5%, model 48.2% (projection_v2.0 (prediction ledger)) -- gap -5.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23PRIGRA-2-GRA` Will Tyra Caterina Grant win set 2 in the Elena Pridankina vs Tyra Caterina Grant match: 0.20/0.84 mid 52.0%, model 51.8% (projection_v2.0 (prediction ledger)) -- gap -0.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jeline Vandromme vs Carol Young Suh Lee -- WTA Guangzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 04:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 03:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:221803:259871:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carol Young Suh Lee (`KXWTAMATCH-26OCT23VANLEE-LEE`) | 0.42 / 0.44 (2154) | 43.0% | 34.8% | 32.5% | 36.3% [34.4%-41.2%] | -- | -- | -- | -- | PASS | -8.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jeline Vandromme (`KXWTAMATCH-26OCT23VANLEE-VAN`) | 0.55 / 0.57 (20023) | 56.0% | 65.2% | 67.5% | 63.7% [58.8%-65.6%] | -- | -- | -- | -- | WATCH | +9.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3468.0, B 4047.0; serve-point win A 60.9%, B 42.2%; Elo A 1796.2, B 1765.0; model uncertainty 0.0341
* Form inputs: days since last match A 6, B 31; matches on record A 130, B 154; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.010, surface_dev_tight -0.015
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT23VANLEE-1-VAN` Will Jeline Vandromme win set 1 in the Jeline Vandromme vs Carol Young Suh Lee match: 0.53/0.57 mid 55.0%, model 60.3% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23VANLEE-2-VAN` Will Jeline Vandromme win set 2 in the Jeline Vandromme vs Carol Young Suh Lee match: 0.26/0.84 mid 55.0%, model 60.3% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23VANLEE-1-LEE` Will Carol Young Suh Lee win set 1 in the Jeline Vandromme vs Carol Young Suh Lee match: 0.44/0.45 mid 44.5%, model 39.7% (projection_v2.0 (prediction ledger)) -- gap -4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23VANLEE-2-LEE` Will Carol Young Suh Lee win set 2 in the Jeline Vandromme vs Carol Young Suh Lee match: 0.26/0.55 mid 40.5%, model 39.7% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Yexin Ma vs Daria Kasatkina -- WTA Tokyo Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 04:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 04:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 03:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-24T04:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT23YEXKAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daria Kasatkina (`KXWTAMATCH-26OCT23YEXKAS-KAS`) | 0.81 / 0.82 (2734) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yexin Ma (`KXWTAMATCH-26OCT23YEXKAS-YEX`) | 0.19 / 0.20 (5273) | 19.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sara Saito vs Ariana Arseneault -- W75 Saguenay QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 04:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T04:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220502:260170:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ariana Arseneault (`KXITFWMATCH-26OCT23SAIARS-ARS`) | 0.80 / 0.81 (6071) | 80.5% | 32.4% | 54.3% | 42.0% [32.9%-46.8%] | -- | -- | -- | -- | PASS | -48.1 pp | EXTREME (DATA_WARNING) | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sara Saito (`KXITFWMATCH-26OCT23SAIARS-SAI`) | 0.19 / 0.21 (6) | 20.0% | 67.6% | 45.7% | 58.0% [53.2%-67.1%] | -- | -- | -- | -- | WATCH | +47.6 pp | EXTREME (DATA_WARNING) | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3341.0, B 2049.0; serve-point win A 54.9%, B 48.5%; Elo A 1658.8, B 1491.0; model uncertainty 0.0693
* Form inputs: days since last match A 25, B 32; matches on record A 198, B 129; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT23SAIARS-SAI  (YES = Sara Saito)
Model: 68%
Kalshi: 20%
Gap: +48 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LEVEL_TRANSFER_RISK, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Burgic / Szabo vs Mi / Mushika -- W35 Bakersfield CA SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 04:45Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-24T04:45:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT23BURSZAMIXMUS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Burgic / Szabo (`KXITFWDOUBLES-26OCT23BURSZAMIXMUS-BURSZA`) | 0.05 / 0.72 (1) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mi / Mushika (`KXITFWDOUBLES-26OCT23BURSZAMIXMUS-MIXMUS`) | 0.06 / 0.94 (100) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Desirae Krawczyk / Fanny Stollar vs Ulrikke Eikeri / Quinn Gleason -- WTA Ningbo SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 08:00Z
* Current expected start: 2026-10-24 05:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 04:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-24T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24KRASTOEIKGLE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ulrikke Eikeri / Quinn Gleason (`KXWTADOUBLES-26OCT24KRASTOEIKGLE-EIKGLE`) | 0.49 / 0.51 (40) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Desirae Krawczyk / Fanny Stollar (`KXWTADOUBLES-26OCT24KRASTOEIKGLE-KRASTO`) | 0.49 / 0.51 (452) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Matthew Dellavedova vs Stefan Vujic -- M25 Tamworth QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200166:202354:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthew Dellavedova (`KXITFMATCH-26OCT23DELVUJ-DEL`) | 0.37 / 0.38 (17078) | 37.5% | 88.8% | 43.4% | 88.9% [87.9%-89.9%] | -- | -- | -- | -- | PASS | +51.3 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Stefan Vujic (`KXITFMATCH-26OCT23DELVUJ-VUJ`) | 0.62 / 0.63 (40439) | 62.5% | 11.2% | 56.6% | 11.1% [10.1%-12.0%] | -- | -- | -- | -- | PASS | -51.3 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1203.0, B 65.0; serve-point win A 66.3%, B 43.3%; Elo A 1490.7, B 1104.0; model uncertainty 0.0096
* Form inputs: days since last match A 31, B 151; matches on record A 356, B 63; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT23DELVUJ-DEL  (YES = Matthew Dellavedova)
Model: 89%
Kalshi: 38%
Gap: +51 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Blake Ellis vs Herman Hoeyeraal -- M25 Tamworth QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:134329:208382:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Blake Ellis (`KXITFMATCH-26OCT23ELLHOE-ELL`) | 0.99 / -- (0) | -- | 92.0% | 54.4% | 88.2% [87.2%-88.9%] | -- | -- | -- | -- | PASS | -- | UNPRICED | FRESH | D / POOR | INSUFFICIENT_INPUTS | VERIFIED |
| Herman Hoeyeraal (`KXITFMATCH-26OCT23ELLHOE-HOE`) | -- / 0.01 (164335) | -- | 8.0% | 45.6% | 11.8% [11.1%-12.8%] | -- | -- | -- | -- | PASS | -- | UNPRICED | FRESH | D / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 1850.0, B 74.0; serve-point win A 70.5%, B 40.9%; Elo A 1579.5, B 1211.8; model uncertainty 0.0086
* Form inputs: days since last match A 39, B 109; matches on record A 366, B 8; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vaidehee Chaudhari vs I Wen Wan -- W35 Sydney SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT23CHAWAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vaidehee Chaudhari (`KXITFWMATCH-26OCT23CHAWAN-CHA`) | -- / 0.01 (185628) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| I Wen Wan (`KXITFWMATCH-26OCT23CHAWAN-WAN`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hikaru Sato vs Mio Mushika -- W35 Sydney SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221141:222986:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mio Mushika (`KXITFWMATCH-26OCT23SATMUS-MUS`) | 0.09 / 0.10 (6643) | 9.5% | 67.3% | 84.4% | 73.6% [61.5%-79.6%] | -- | -- | -- | -- | PASS | +57.8 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hikaru Sato (`KXITFWMATCH-26OCT23SATMUS-SAT`) | 0.90 / 0.91 (13927) | 90.5% | 32.7% | 15.6% | 26.4% [20.4%-38.5%] | -- | -- | -- | -- | PASS | -57.8 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1807.0, B 2224.0; serve-point win A 55.7%, B 40.8%; Elo A 1465.8, B 1520.7; model uncertainty 0.0906
* Form inputs: days since last match A 186, B 186; matches on record A 175, B 201; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT23SATMUS-MUS  (YES = Mio Mushika)
Model: 67%
Kalshi: 10%
Gap: +58 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.004, surface_dev_loose -0.016, surface_dev_tight +0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hugo Hashimoto vs Chun-Chien Hou -- M15 Tanagura SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 05:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T05:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213074:213114:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Hashimoto (`KXITFMATCH-26OCT23HASHOU-HAS`) | 0.90 / 0.91 (55) | 90.5% | 67.5% | 63.4% | 61.9% [61.9%-62.0%] | -- | -- | -- | -- | PASS | -23.0 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Chun-Chien Hou (`KXITFMATCH-26OCT23HASHOU-HOU`) | 0.09 / 0.10 (8307) | 9.5% | 32.5% | 36.6% | 38.1% [38.0%-38.1%] | -- | -- | -- | -- | PASS | +23.0 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 50.0; serve-point win A 64.2%, B 39.4%; Elo A 1315.4, B 1233.2; model uncertainty 0.0005
* Form inputs: days since last match A 830, B 732; matches on record A 2, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT23HASHOU-HOU  (YES = Chun-Chien Hou)
Model: 32%
Kalshi: 10%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuto Oki vs Takuya Kumasaka -- M15 Tanagura SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 05:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T05:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207998:212639:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Takuya Kumasaka (`KXITFMATCH-26OCT23OKIKUM-KUM`) | 0.54 / 0.62 (29) | 58.0% | 61.5% | 34.0% | 51.0% [49.0%-52.0%] | -- | -- | -- | -- | PASS | +3.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuto Oki (`KXITFMATCH-26OCT23OKIKUM-OKI`) | 0.30 / 0.38 (55) | 34.0% | 38.5% | 66.0% | 49.0% [48.0%-51.0%] | -- | -- | -- | -- | PASS | +4.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 113.0, B 862.0; serve-point win A 59.4%, B 38.3%; Elo A 1327.6, B 1338.1; model uncertainty 0.0153
* Form inputs: days since last match A 207, B 74; matches on record A 6, B 151; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Akli / Sieg vs Bayerlova / Gimbrere -- W75 Saguenay SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 05:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-24T05:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT23AKLSIEBAYGIM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Akli / Sieg (`KXITFWDOUBLES-26OCT23AKLSIEBAYGIM-AKLSIE`) | 0.56 / 0.78 (10) | 67.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bayerlova / Gimbrere (`KXITFWDOUBLES-26OCT23AKLSIEBAYGIM-BAYGIM`) | 0.37 / 0.44 (17) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Storm Hunter / Janice Tjen vs Jesika Maleckova / Miriam Skoch -- WTA Osaka F

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 06:00Z
* Current expected start: 2026-10-24 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 05:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-24T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT23HUNTJEMALSKO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Storm Hunter / Janice Tjen (`KXWTADOUBLES-26OCT23HUNTJEMALSKO-HUNTJE`) | 0.71 / 0.72 (3339) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jesika Maleckova / Miriam Skoch (`KXWTADOUBLES-26OCT23HUNTJEMALSKO-MALSKO`) | 0.26 / 0.29 (1877) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Hayu Kinoshita vs Yulia Putintseva -- WTA Tokyo Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 04:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T04:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:201709:260171:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hayu Kinoshita (`KXWTAMATCH-26OCT23KINPUT-KIN`) | 0.11 / 0.12 (8520) | 11.5% | 28.1% | 58.4% | 44.2% [29.0%-50.5%] | 12.7% | 11.1% | 11.9% | MODEL_LONE_OUTLIER | PASS | +16.6 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Yulia Putintseva (`KXWTAMATCH-26OCT23KINPUT-PUT`) | 0.88 / 0.90 (3835) | 89.0% | 71.9% | 41.6% | 55.8% [49.5%-71.0%] | 87.3% | 88.0% | 87.3% | MODEL_LONE_OUTLIER | PASS | -17.1 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3494.0, B 4366.0; serve-point win A 55.0%, B 40.6%; Elo A 1619.5, B 1893.8; model uncertainty 0.1077
* Form inputs: days since last match A 25, B 3; matches on record A 175, B 859; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT23KINPUT-KIN  (YES = Hayu Kinoshita)
Model: 28%
Kalshi: 12%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.010
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT23KINPUT-1-KIN` Will Hayu Kinoshita win set 1 in the Hayu Kinoshita vs Yulia Putintseva match: 0.17/0.20 mid 18.5%, model 34.9% (projection_v2.0 (prediction ledger)) -- gap +16.4 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23KINPUT-1-PUT` Will Yulia Putintseva win set 1 in the Hayu Kinoshita vs Yulia Putintseva match: 0.80/0.83 mid 81.5%, model 65.1% (projection_v2.0 (prediction ledger)) -- gap -16.4 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23KINPUT-2-KIN` Will Hayu Kinoshita win set 2 in the Hayu Kinoshita vs Yulia Putintseva match: 0.14/0.41 mid 27.5%, model 34.9% (projection_v2.0 (prediction ledger)) -- gap +7.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23KINPUT-2-PUT` Will Yulia Putintseva win set 2 in the Hayu Kinoshita vs Yulia Putintseva match: 0.41/0.86 mid 63.5%, model 65.1% (projection_v2.0 (prediction ledger)) -- gap +1.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tatiana Prozorova vs Ekaterine Gorgodze -- WTA Guangzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202493:236955:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterine Gorgodze (`KXWTAMATCH-26OCT23PROGOR-GOR`) | 0.18 / 0.20 (3671) | 19.0% | 14.6% | 13.3% | 15.7% [13.6%-22.6%] | 20.2% | 19.5% | 19.8% | MODEL_LONE_OUTLIER | PASS | -4.4 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Tatiana Prozorova (`KXWTAMATCH-26OCT23PROGOR-PRO`) | 0.80 / 0.81 (268) | 80.5% | 85.4% | 86.7% | 84.3% [77.4%-86.4%] | 79.8% | 80.7% | 80.3% | MODEL_LONE_OUTLIER | WATCH | +4.9 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3551.0, B 4075.0; serve-point win A 62.1%, B 46.0%; Elo A 1800.3, B 1577.7; model uncertainty 0.0452
* Form inputs: days since last match A 5, B 10; matches on record A 292, B 949; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.003, surface_dev_loose +0.017, surface_dev_tight -0.019
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT23PROGOR-2-PRO` Will Tatiana Prozorova win set 2 in the Tatiana Prozorova vs Ekaterine Gorgodze match: 0.27/0.86 mid 56.5%, model 75.9% (projection_v2.0 (prediction ledger)) -- gap +19.4 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23PROGOR-2-GOR` Will Ekaterine Gorgodze win set 2 in the Tatiana Prozorova vs Ekaterine Gorgodze match: 0.15/0.58 mid 36.5%, model 24.1% (projection_v2.0 (prediction ledger)) -- gap -12.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23PROGOR-1-PRO` Will Tatiana Prozorova win set 1 in the Tatiana Prozorova vs Ekaterine Gorgodze match: 0.73/0.76 mid 74.5%, model 75.9% (projection_v2.0 (prediction ledger)) -- gap +1.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23PROGOR-1-GOR` Will Ekaterine Gorgodze win set 1 in the Tatiana Prozorova vs Ekaterine Gorgodze match: 0.23/0.26 mid 24.5%, model 24.1% (projection_v2.0 (prediction ledger)) -- gap -0.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Xinyu Wang vs Tereza Valentova -- WTA Tokyo Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 04:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-24T04:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT23WANVAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tereza Valentova (`KXWTAMATCH-26OCT23WANVAL-VAL`) | 0.58 / 0.59 (3539) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xinyu Wang (`KXWTAMATCH-26OCT23WANVAL-WAN`) | 0.41 / 0.42 (4400) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hong Yi Cody Wong vs Emerson Jones -- WTA Guangzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:216587:263644:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emerson Jones (`KXWTAMATCH-26OCT23WONJON-JON`) | 0.90 / 0.91 (1937) | 90.5% | 84.3% | 86.6% | 84.5% [82.0%-86.0%] | 88.1% | 91.8% | 89.9% | MODEL_LONE_OUTLIER | PASS | -6.2 pp | NORMAL | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Hong Yi Cody Wong (`KXWTAMATCH-26OCT23WONJON-WON`) | 0.09 / 0.10 (6008) | 9.5% | 15.7% | 13.4% | 15.5% [14.0%-18.0%] | 11.9% | 9.2% | 10.6% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.2 pp | NORMAL | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1599.0, B 3547.0; serve-point win A 54.8%, B 37.5%; Elo A 1531.8, B 1792.6; model uncertainty 0.0197
* Form inputs: days since last match A 61, B 3; matches on record A 280, B 151; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.003, surface_pool_high +0.006, surface_dev_loose -0.003, surface_dev_tight +0.006
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT23WONJON-2-JON` Will Emerson Jones win set 2 in the Hong Yi Cody Wong vs Emerson Jones match: 0.37/0.90 mid 63.5%, model 74.9% (projection_v2.0 (prediction ledger)) -- gap +11.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT23WONJON-1-WON` Will Hong Yi Cody Wong win set 1 in the Hong Yi Cody Wong vs Emerson Jones match: 0.13/0.16 mid 14.5%, model 25.1% (projection_v2.0 (prediction ledger)) -- gap +10.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT23WONJON-1-JON` Will Emerson Jones win set 1 in the Hong Yi Cody Wong vs Emerson Jones match: 0.84/0.85 mid 84.5%, model 74.9% (projection_v2.0 (prediction ledger)) -- gap -9.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT23WONJON-2-WON` Will Hong Yi Cody Wong win set 2 in the Hong Yi Cody Wong vs Emerson Jones match: 0.14/0.41 mid 27.5%, model 25.1% (projection_v2.0 (prediction ledger)) -- gap -2.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Isaac Becroft vs Casey Hoole -- M25 Tamworth SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208653:211315:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isaac Becroft (`KXITFMATCH-26OCT23BECHOO-BEC`) | 0.46 / 0.48 (74) | 47.0% | 38.7% | 37.1% | 49.5% [48.0%-50.0%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Casey Hoole (`KXITFMATCH-26OCT23BECHOO-HOO`) | 0.52 / 0.56 (90) | 54.0% | 61.3% | 62.9% | 50.5% [50.0%-52.0%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 69.0, B 175.0; serve-point win A 61.1%, B 36.6%; Elo A 1375.8, B 1374.7; model uncertainty 0.0101
* Form inputs: days since last match A 655, B 676; matches on record A 70, B 16; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Coleman Wong vs Yi Zhou -- ATP Challenger Guangzhou Nansha SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-24T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209409:212044:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Coleman Wong (`KXATPCHALLENGERMATCH-26OCT23WONZHO-WON`) | 0.65 / 0.66 (12184) | 65.5% | 64.0% | 61.3% | 62.3% [61.8%-63.2%] | -- | -- | -- | -- | PASS | -1.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yi Zhou (`KXATPCHALLENGERMATCH-26OCT23WONZHO-ZHO`) | 0.35 / 0.36 (1131) | 35.5% | 36.0% | 38.7% | 37.8% [36.8%-38.2%] | -- | -- | -- | -- | PASS | +0.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4502.0, B 2882.0; serve-point win A 69.2%, B 33.8%; Elo A 1716.5, B 1611.4; model uncertainty 0.0072
* Form inputs: days since last match A 16, B 12; matches on record A 290, B 150; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.004, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Katie Boulter vs Sayaka Ishii -- WTA Tokyo Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 04:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 06:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 05:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T04:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211107:259967:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katie Boulter (`KXWTAMATCH-26OCT23BOUISH-BOU`) | 0.50 / 0.55 (117) | 52.5% | 84.4% | 88.5% | 85.5% [81.7%-88.3%] | -- | -- | -- | -- | WATCH | +31.9 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sayaka Ishii (`KXWTAMATCH-26OCT23BOUISH-ISH`) | 0.43 / 0.48 (133) | 45.5% | 15.6% | 11.5% | 14.5% [11.7%-18.3%] | -- | -- | -- | -- | PASS | -29.9 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3928.0, B 1713.0; serve-point win A 62.0%, B 45.8%; Elo A 1894.6, B 1638.7; model uncertainty 0.0331
* Form inputs: days since last match A 0, B 5; matches on record A 593, B 191; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT23BOUISH-BOU  (YES = Katie Boulter)
Model: 84%
Kalshi: 52%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, UNKNOWN
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.028, surface_pool_high -0.039, surface_dev_loose +0.008, surface_dev_tight -0.009
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT23BOUISH-1-BOU` Will Katie Boulter win set 1 in the Katie Boulter vs Sayaka Ishii match: 0.05/0.87 mid 46.0%, model 75.0% (projection_v2.0 (prediction ledger)) -- gap +29.0 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23BOUISH-2-BOU` Will Katie Boulter win set 2 in the Katie Boulter vs Sayaka Ishii match: 0.14/0.90 mid 52.0%, model 75.0% (projection_v2.0 (prediction ledger)) -- gap +23.0 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23BOUISH-2-ISH` Will Sayaka Ishii win set 2 in the Katie Boulter vs Sayaka Ishii match: 0.14/0.80 mid 47.0%, model 25.0% (projection_v2.0 (prediction ledger)) -- gap -22.0 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23BOUISH-1-ISH` Will Sayaka Ishii win set 1 in the Katie Boulter vs Sayaka Ishii match: 0.06/0.83 mid 44.5%, model 25.0% (projection_v2.0 (prediction ledger)) -- gap -19.5 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lucas Miedler / Neil Oberleitner vs N. Sriram Balaji / Evan King -- ATP Almaty SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 09:30Z
* Current expected start: 2026-10-24 07:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 06:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-24T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24MIEOBEBALKIN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N. Sriram Balaji / Evan King (`KXATPDOUBLES-26OCT24MIEOBEBALKIN-BALKIN`) | 0.33 / 0.36 (27) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lucas Miedler / Neil Oberleitner (`KXATPDOUBLES-26OCT24MIEOBEBALKIN-MIEOBE`) | 0.63 / 0.66 (188) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Leylah Fernandez vs Marie Bouzkova -- WTA Ningbo SF

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-24 08:00Z
* Current expected start: 2026-10-24 07:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-23 10:00Z
* Recommended handicap-by time: 2026-10-24 06:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-60_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213631:220367:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marie Bouzkova (`KXWTAMATCH-26OCT24FERBOU-BOU`) | 0.51 / 0.52 (2102) | 51.5% | 46.6% | 45.3% | 46.3% [45.3%-50.5%] | -- | -- | -- | -- | PASS | -4.9 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Leylah Fernandez (`KXWTAMATCH-26OCT24FERBOU-FER`) | 0.49 / 0.50 (62451) | 49.5% | 53.4% | 54.7% | 53.7% [49.5%-54.7%] | -- | -- | -- | -- | WATCH | +3.9 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4828.0, B 4089.0; serve-point win A 57.6%, B 43.1%; Elo A 1973.1, B 1967.0; model uncertainty 0.0262
* Form inputs: days since last match A 0, B 0; matches on record A 403, B 647; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.011, surface_dev_loose -0.000, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT24FERBOU-22` Over 21.5 games: 0.53/0.54 mid 53.5%, model 63.4% (projection_v2.0 (prediction ledger)) -- gap +9.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT24FERBOU-27` Over 26.5 games: 0.30/0.32 mid 31.0%, model 40.0% (projection_v2.0 (prediction ledger)) -- gap +9.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT24FERBOU-17` Over 16.5 games: 0.85/0.90 mid 87.5%, model 94.1% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT24FERBOU-1-FER` Will Leylah Annie Fernandez win set 1 in the Leylah Annie Fernandez vs Marie Bouzkova match: 0.47/0.50 mid 48.5%, model 52.2% (projection_v2.0 (prediction ledger)) -- gap +3.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT24FERBOU-2-FER` Will Leylah Annie Fernandez win set 2 in the Leylah Annie Fernandez vs Marie Bouzkova match: 0.47/0.50 mid 48.5%, model 52.2% (projection_v2.0 (prediction ledger)) -- gap +3.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT24FERBOU-1-BOU` Will Marie Bouzkova win set 1 in the Leylah Annie Fernandez vs Marie Bouzkova match: 0.50/0.52 mid 51.0%, model 47.8% (projection_v2.0 (prediction ledger)) -- gap -3.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT24FERBOU-2-BOU` Will Marie Bouzkova win set 2 in the Leylah Annie Fernandez vs Marie Bouzkova match: 0.48/0.52 mid 50.0%, model 47.8% (projection_v2.0 (prediction ledger)) -- gap -2.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; NO_EXTERNAL_PRICE

## Barry / Sato vs Stevens / Thompson -- W35 Sydney F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-24T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT23BARSATSTETHO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barry / Sato (`KXITFWDOUBLES-26OCT23BARSATSTETHO-BARSAT`) | 0.05 / 0.46 (46) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stevens / Thompson (`KXITFWDOUBLES-26OCT23BARSATSTETHO-STETHO`) | 0.06 / 0.65 (100) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Tristan Schoolkate vs Jie Cui -- ATP Challenger Guangzhou Nansha SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 07:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-24T07:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200666:209262:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jie Cui (`KXATPCHALLENGERMATCH-26OCT24SCHCUI-CUI`) | 0.34 / 0.35 (5152) | 34.5% | 32.4% | 24.9% | 27.3% [25.7%-28.9%] | 34.3% | 33.6% | 33.6% | MODEL_LONE_OUTLIER | PASS | -2.1 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Tristan Schoolkate (`KXATPCHALLENGERMATCH-26OCT24SCHCUI-SCH`) | 0.65 / 0.66 (4718) | 65.5% | 67.7% | 75.1% | 72.7% [71.1%-74.3%] | 65.7% | 65.8% | 65.8% | MODEL_LONE_OUTLIER | SHADOW_BET | +2.1 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4674.0, B 2205.0; serve-point win A 68.7%, B 35.1%; Elo A 1664.0, B 1527.2; model uncertainty 0.016
* Form inputs: days since last match A 18, B 11; matches on record A 377, B 279; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.016, surface_dev_loose +0.004, surface_dev_tight -0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Harriet Dart vs Cheuk Ying Shek -- WTA Guangzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 07:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 06:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211279:263941:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Harriet Dart (`KXWTAMATCH-26OCT23DARSHE-DAR`) | 0.89 / 0.91 (45) | 90.0% | 85.7% | 70.9% | 79.7% [74.9%-86.0%] | -- | -- | -- | -- | PASS | -4.3 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Cheuk Ying Shek (`KXWTAMATCH-26OCT23DARSHE-SHE`) | 0.08 / 0.11 (2452) | 9.5% | 14.3% | 29.1% | 20.3% [14.0%-25.1%] | -- | -- | -- | -- | WATCH | +4.8 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4244.0, B 1558.0; serve-point win A 57.1%, B 50.9%; Elo A 1787.6, B 1461.7; model uncertainty 0.0558
* Form inputs: days since last match A 4, B 193; matches on record A 676, B 47; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.019, surface_dev_loose +0.004, surface_dev_tight -0.008
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT23DARSHE-1-DAR` Will Harriet Dart win set 1 in the Harriet Dart vs Cheuk Ying Shek match: 0.42/0.91 mid 66.5%, model 76.2% (projection_v2.0 (prediction ledger)) -- gap +9.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT23DARSHE-2-DAR` Will Harriet Dart win set 2 in the Harriet Dart vs Cheuk Ying Shek match: 0.47/0.86 mid 66.5%, model 76.2% (projection_v2.0 (prediction ledger)) -- gap +9.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT23DARSHE-1-SHE` Will Cheuk Ying Shek win set 1 in the Harriet Dart vs Cheuk Ying Shek match: 0.04/0.58 mid 31.0%, model 23.8% (projection_v2.0 (prediction ledger)) -- gap -7.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT23DARSHE-2-SHE` Will Cheuk Ying Shek win set 2 in the Harriet Dart vs Cheuk Ying Shek match: 0.14/0.41 mid 27.5%, model 23.8% (projection_v2.0 (prediction ledger)) -- gap -3.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Joanna Garland vs Maddison Inglis -- WTA Guangzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 07:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 06:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213666:220466:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joanna Garland (`KXWTAMATCH-26OCT23GARING-GAR`) | 0.43 / 0.45 (2145) | 44.0% | 54.4% | 56.0% | 53.5% [52.0%-55.5%] | 44.4% | 44.5% | -- | INSUFFICIENT_INPUTS | PASS | +10.4 pp | REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maddison Inglis (`KXWTAMATCH-26OCT23GARING-ING`) | 0.55 / 0.56 (156) | 55.5% | 45.6% | 44.0% | 46.5% [44.5%-48.0%] | 55.6% | 55.6% | -- | INSUFFICIENT_INPUTS | PASS | -9.9 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2480.0, B 3027.0; serve-point win A 63.0%, B 37.9%; Elo A 1771.2, B 1768.4; model uncertainty 0.0173
* Form inputs: days since last match A 29, B 5; matches on record A 393, B 483; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.005, surface_dev_loose -0.010, surface_dev_tight +0.015
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT23GARING-2-ING` Will Maddison Inglis win set 2 in the Joanna Garland vs Maddison Inglis match: 0.26/0.84 mid 55.0%, model 47.0% (projection_v2.0 (prediction ledger)) -- gap -8.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT23GARING-1-GAR` Will Joanna Garland win set 1 in the Joanna Garland vs Maddison Inglis match: 0.45/0.46 mid 45.5%, model 53.0% (projection_v2.0 (prediction ledger)) -- gap +7.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT23GARING-1-ING` Will Maddison Inglis win set 1 in the Joanna Garland vs Maddison Inglis match: 0.52/0.54 mid 53.0%, model 47.0% (projection_v2.0 (prediction ledger)) -- gap -6.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT23GARING-2-GAR` Will Joanna Garland win set 2 in the Joanna Garland vs Maddison Inglis match: 0.26/0.82 mid 54.0%, model 53.0% (projection_v2.0 (prediction ledger)) -- gap -1.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Beale / Vujic vs Talic / Vickery -- M25 Tamworth QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-24T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT23BEAVUJTALVIC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Beale / Vujic (`KXITFDOUBLES-26OCT23BEAVUJTALVIC-BEAVUJ`) | 0.68 / 0.86 (178) | 77.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Talic / Vickery (`KXITFDOUBLES-26OCT23BEAVUJTALVIC-TALVIC`) | 0.09 / 0.24 (1) | 16.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Becroft / Shepp vs Bruce-Smith / Storch -- M25 Tamworth QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-24T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT23BECSHEBRUSTO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Becroft / Shepp (`KXITFDOUBLES-26OCT23BECSHEBRUSTO-BECSHE`) | 0.78 / 0.95 (38) | 86.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bruce-Smith / Storch (`KXITFDOUBLES-26OCT23BECSHEBRUSTO-BRUSTO`) | 0.06 / 0.16 (29) | 11.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Mikalai Haliak vs Filip Peliwo -- M15 Shenzhen SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106290:144915:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mikalai Haliak (`KXITFMATCH-26OCT23HALPEL-HAL`) | 0.48 / 0.49 (1) | 48.5% | 51.4% | 39.3% | 43.3% [39.3%-51.0%] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Filip Peliwo (`KXITFMATCH-26OCT23HALPEL-PEL`) | 0.49 / 0.52 (238) | 50.5% | 48.6% | 60.7% | 56.7% [49.0%-60.7%] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2107.0, B 952.0; serve-point win A 60.3%, B 40.0%; Elo A 1351.0, B 1382.6; model uncertainty 0.0586
* Form inputs: days since last match A 704, B 39; matches on record A 302, B 732; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.031, surface_pool_high -0.040, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sarksian / Shin vs Dao Chen / Dong -- M15 Shenzhen F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-24T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT23SARSHIDAODON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dao Chen / Dong (`KXITFDOUBLES-26OCT23SARSHIDAODON-DAODON`) | 0.14 / 0.26 (1) | 20.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sarksian / Shin (`KXITFDOUBLES-26OCT23SARSHIDAODON-SARSHI`) | 0.66 / 0.84 (156) | 75.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Luca Staeheli vs Boris Butulija -- M15 Shenzhen SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200197:207664:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Boris Butulija (`KXITFMATCH-26OCT23STABUT-BUT`) | 0.07 / 0.08 (4098) | 7.5% | 27.1% | 49.0% | 37.8% [35.9%-38.3%] | 7.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +19.6 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luca Staeheli (`KXITFMATCH-26OCT23STABUT-STA`) | 0.91 / 0.93 (13) | 92.0% | 72.9% | 51.0% | 62.2% [61.7%-64.1%] | 92.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -19.1 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 545.0, B 77.0; serve-point win A 62.5%, B 42.3%; Elo A 1265.3, B 1172.5; model uncertainty 0.012
* Form inputs: days since last match A 25, B 718; matches on record A 65, B 214; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT23STABUT-BUT  (YES = Boris Butulija)
Model: 27%
Kalshi: 8%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Violet Apisah vs Aruzhan Sagandykova -- W15 Singapore SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221802:270061:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Violet Apisah (`KXITFWMATCH-26OCT23APISAG-API`) | 0.58 / 0.59 (60) | 58.5% | 31.4% | 31.6% | 45.8% [43.7%-46.8%] | -- | -- | -- | -- | PASS | -27.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Aruzhan Sagandykova (`KXITFWMATCH-26OCT23APISAG-SAG`) | 0.40 / 0.43 (59) | 41.5% | 68.6% | 68.4% | 54.2% [53.2%-56.3%] | -- | -- | -- | -- | PASS | +27.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 122.0, B 1744.0; serve-point win A 53.7%, B 42.7%; Elo A 1379.7, B 1403.7; model uncertainty 0.0157
* Form inputs: days since last match A 2815, B 27; matches on record A 2, B 45; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT23APISAG-SAG  (YES = Aruzhan Sagandykova)
Model: 69%
Kalshi: 42%
Gap: +27 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jing-Jing Lu vs Alexandra Malova -- W15 Singapore SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT23LUXMAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jing-Jing Lu (`KXITFWMATCH-26OCT23LUXMAL-LUX`) | 0.54 / 0.58 (116) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexandra Malova (`KXITFWMATCH-26OCT23LUXMAL-MAL`) | 0.43 / 0.44 (100) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yu Hsiou Hsu / Fajing Sun vs Thijmen Loof / Kaito Uesugi -- ATP Challenger Guangzhou Nansha F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 08:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-24T08:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24HSUSUNLOOUES:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yu Hsiou Hsu / Fajing Sun (`KXATPCHALLENGERDOUBLES-26OCT24HSUSUNLOOUES-HSUSUN`) | 0.05 / 0.55 (1) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Thijmen Loof / Kaito Uesugi (`KXATPCHALLENGERDOUBLES-26OCT24HSUSUNLOOUES-LOOUES`) | 0.05 / 0.88 (1) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jacob Fearnley vs Pablo Carreno Busta -- ATP Vienna Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 12:00Z
* Current expected start: 2026-10-24 09:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 08:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105807:207985:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pablo Carreno Busta (`KXATPMATCH-26OCT24FEACAR-CAR`) | 0.38 / 0.41 (34) | 39.5% | 40.1% | 38.4% | 44.4% [39.9%-51.0%] | 40.6% | 39.3% | -- | INSUFFICIENT_INPUTS | PASS | +0.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jacob Fearnley (`KXATPMATCH-26OCT24FEACAR-FEA`) | 0.56 / 0.60 (76) | 58.0% | 59.9% | 61.6% | 55.6% [49.0%-60.1%] | 59.4% | 60.4% | -- | INSUFFICIENT_INPUTS | PASS | +1.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4197.0, B 3944.0; serve-point win A 62.4%, B 39.5%; Elo A 1781.1, B 1841.3; model uncertainty 0.0555
* Form inputs: days since last match A 2, B 11; matches on record A 185, B 959; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.030, surface_dev_loose +0.020, surface_dev_tight -0.015
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT24FEACAR-CAR20` Will Pablo Carreno Busta win the Jacob Fearnley vs Pablo Carreno Busta match by a set score of 2-0?: 0.01/0.87 mid 44.0%, model 18.8% (projection_v2.0 (prediction ledger)) -- gap -25.2 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24FEACAR-CAR21` Will Pablo Carreno Busta win the Jacob Fearnley vs Pablo Carreno Busta match by a set score of 2-1?: 0.01/0.62 mid 31.5%, model 21.3% (projection_v2.0 (prediction ledger)) -- gap -10.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24FEACAR-1-FEA` Will Jacob Fearnley win set 1 in the Jacob Fearnley vs Pablo Carreno Busta match: 0.01/0.98 mid 49.5%, model 56.6% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24FEACAR-2-CAR` Will Pablo Carreno Busta win set 2 in the Jacob Fearnley vs Pablo Carreno Busta match: 0.03/0.97 mid 50.0%, model 43.4% (projection_v2.0 (prediction ledger)) -- gap -6.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24FEACAR-2-FEA` Will Jacob Fearnley win set 2 in the Jacob Fearnley vs Pablo Carreno Busta match: 0.03/0.97 mid 50.0%, model 56.6% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24FEACAR-1-CAR` Will Pablo Carreno Busta win set 1 in the Jacob Fearnley vs Pablo Carreno Busta match: 0.01/0.98 mid 49.5%, model 43.4% (projection_v2.0 (prediction ledger)) -- gap -6.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24FEACAR-FEA21` Will Jacob Fearnley win the Jacob Fearnley vs Pablo Carreno Busta match by a set score of 2-1?: 0.02/0.59 mid 30.5%, model 27.8% (projection_v2.0 (prediction ledger)) -- gap -2.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24FEACAR-FEA20` Will Jacob Fearnley win the Jacob Fearnley vs Pablo Carreno Busta match by a set score of 2-0?: 0.01/0.65 mid 33.0%, model 32.1% (projection_v2.0 (prediction ledger)) -- gap -0.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; WIDE_SPREAD

## Marcos Giron vs Yannick Hanfmann -- ATP Basel Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 11:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 09:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 08:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105870:106218:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcos Giron (`KXATPMATCH-26OCT24GIRHAN-GIR`) | 0.35 / 0.37 (15) | 36.0% | 56.8% | 43.2% | 47.6% [45.2%-50.5%] | -- | -- | -- | -- | PASS | +20.8 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yannick Hanfmann (`KXATPMATCH-26OCT24GIRHAN-HAN`) | 0.62 / 0.64 (8) | 63.0% | 43.2% | 56.8% | 52.4% [49.5%-54.8%] | -- | -- | -- | -- | PASS | -19.8 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4256.0, B 4359.0; serve-point win A 67.3%, B 34.1%; Elo A 1805.2, B 1728.0; model uncertainty 0.0266
* Form inputs: days since last match A 3, B 14; matches on record A 708, B 656; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT24GIRHAN-GIR  (YES = Marcos Giron)
Model: 57%
Kalshi: 36%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, UNKNOWN
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.024, surface_pool_high +0.024, surface_dev_loose +0.000, surface_dev_tight +0.005
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT24GIRHAN-1-GIR` Will Marcos Giron win set 1 in the Marcos Giron vs Yannick Hanfmann match: 0.02/0.97 mid 49.5%, model 54.5% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24GIRHAN-2-GIR` Will Marcos Giron win set 2 in the Marcos Giron vs Yannick Hanfmann match: 0.02/0.98 mid 50.0%, model 54.5% (projection_v2.0 (prediction ledger)) -- gap +4.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24GIRHAN-2-HAN` Will Yannick Hanfmann win set 2 in the Marcos Giron vs Yannick Hanfmann match: 0.02/0.98 mid 50.0%, model 45.5% (projection_v2.0 (prediction ledger)) -- gap -4.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24GIRHAN-1-HAN` Will Yannick Hanfmann win set 1 in the Marcos Giron vs Yannick Hanfmann match: 0.02/0.97 mid 49.5%, model 45.5% (projection_v2.0 (prediction ledger)) -- gap -4.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Miomir Kecmanovic vs Rinky Hijikata -- ATP Basel Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 11:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 09:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 08:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200175:208014:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rinky Hijikata (`KXATPMATCH-26OCT24KECHIJ-HIJ`) | 0.38 / 0.42 (57) | 40.0% | 46.6% | 38.1% | 41.0% [39.6%-43.5%] | 41.7% | 42.6% | 41.7% | MARKETS_AGREE | PASS | +6.6 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Miomir Kecmanovic (`KXATPMATCH-26OCT24KECHIJ-KEC`) | 0.57 / 0.60 (110) | 58.5% | 53.4% | 61.9% | 59.0% [56.5%-60.4%] | 58.3% | 58.7% | 58.3% | MODEL_LONE_OUTLIER | PASS | -5.1 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5277.0, B 5199.0; serve-point win A 63.4%, B 37.3%; Elo A 1776.8, B 1789.2; model uncertainty 0.0196
* Form inputs: days since last match A 4, B 3; matches on record A 608, B 435; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.005
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT24KECHIJ-1-HIJ` Will Rinky Hijikata win set 1 in the Miomir Kecmanovic vs Rinky Hijikata match: 0.02/0.51 mid 26.5%, model 47.7% (projection_v2.0 (prediction ledger)) -- gap +21.2 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24KECHIJ-1-KEC` Will Miomir Kecmanovic win set 1 in the Miomir Kecmanovic vs Rinky Hijikata match: 0.33/0.96 mid 64.5%, model 52.3% (projection_v2.0 (prediction ledger)) -- gap -12.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24KECHIJ-2-HIJ` Will Rinky Hijikata win set 2 in the Miomir Kecmanovic vs Rinky Hijikata match: 0.03/0.97 mid 50.0%, model 47.7% (projection_v2.0 (prediction ledger)) -- gap -2.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24KECHIJ-2-KEC` Will Miomir Kecmanovic win set 2 in the Miomir Kecmanovic vs Rinky Hijikata match: 0.03/0.97 mid 50.0%, model 52.3% (projection_v2.0 (prediction ledger)) -- gap +2.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Bulte / Falck vs Atkinson / Bouzige -- M25 Tamworth SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-24T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT23BULFALATKBOU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Atkinson / Bouzige (`KXITFDOUBLES-26OCT23BULFALATKBOU-ATKBOU`) | 0.01 / 0.98 (22) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bulte / Falck (`KXITFDOUBLES-26OCT23BULFALATKBOU-BULFAL`) | 0.01 / 0.99 (1132) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Taisei Ichikawa vs Ergi Kirkin -- M15 Singapore SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144985:207383:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Taisei Ichikawa (`KXITFMATCH-26OCT23ICHKIR-ICH`) | 0.31 / 0.33 (137) | 32.0% | 41.0% | 68.6% | 46.4% [28.8%-57.6%] | -- | -- | -- | -- | PASS | +9.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ergi Kirkin (`KXITFMATCH-26OCT23ICHKIR-KIR`) | 0.66 / 0.68 (110) | 67.0% | 59.0% | 31.4% | 53.6% [42.4%-71.2%] | -- | -- | -- | -- | PASS | -8.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 708.0, B 1449.0; serve-point win A 60.9%, B 37.4%; Elo A 1329.6, B 1428.3; model uncertainty 0.144
* Form inputs: days since last match A 697, B 74; matches on record A 170, B 432; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.060, surface_pool_high +0.066, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maxime Janvier vs Kosuke Ogura -- M15 Singapore SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126125:202124:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maxime Janvier (`KXITFMATCH-26OCT23JANOGU-JAN`) | 0.76 / 0.79 (200) | 77.5% | 80.7% | 71.4% | 74.7% [70.5%-79.0%] | -- | -- | -- | -- | PASS | +3.2 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kosuke Ogura (`KXITFMATCH-26OCT23JANOGU-OGU`) | 0.21 / 0.23 (199) | 22.0% | 19.3% | 28.6% | 25.3% [21.0%-29.5%] | -- | -- | -- | -- | PASS | -2.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2255.0, B 358.0; serve-point win A 66.8%, B 40.1%; Elo A 1485.1, B 1291.8; model uncertainty 0.0423
* Form inputs: days since last match A 46, B 291; matches on record A 719, B 178; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.035, surface_pool_high -0.042, surface_dev_loose +0.004, surface_dev_tight -0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Varvara Panshina vs Daria KHOMUTSIANSKAYA -- W35 Qian Daohu SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222944:267420:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daria KHOMUTSIANSKAYA (`KXITFWMATCH-26OCT23PANKHO-KHO`) | 0.57 / 0.62 (18) | 59.5% | 68.5% | 92.8% | 86.0% [72.6%-89.4%] | -- | -- | -- | -- | WATCH | +9.1 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Varvara Panshina (`KXITFWMATCH-26OCT23PANKHO-PAN`) | 0.38 / 0.40 (18) | 39.0% | 31.4% | 7.2% | 14.1% [10.6%-27.4%] | -- | -- | -- | -- | PASS | -7.5 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2447.0, B 3178.0; serve-point win A 52.9%, B 43.5%; Elo A 1546.4, B 1665.8; model uncertainty 0.0843
* Form inputs: days since last match A 102, B 277; matches on record A 102, B 171; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.006, surface_pool_high +0.009, surface_dev_loose -0.011, surface_dev_tight +0.022
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xinxin Yao vs Rada Zolotareva -- W35 Qian Daohu SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:252587:260951:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xinxin Yao (`KXITFWMATCH-26OCT23YAOZOL-YAO`) | 0.52 / 0.56 (106) | 54.0% | 43.1% | 31.9% | 40.0% [36.4%-43.1%] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -10.9 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rada Zolotareva (`KXITFWMATCH-26OCT23YAOZOL-ZOL`) | 0.47 / 0.49 (169) | 48.0% | 56.9% | 68.0% | 60.1% [56.9%-63.6%] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +8.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2972.0, B 1811.0; serve-point win A 52.3%, B 46.4%; Elo A 1573.7, B 1579.7; model uncertainty 0.0336
* Form inputs: days since last match A 18, B 46; matches on record A 320, B 96; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.031, surface_pool_high +0.026, surface_dev_loose +0.016, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matisse Bobichon / Kilian Feldbausch vs Theo Arribage / Albano Olivetti -- ATP Lyon SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-23 13:00Z
* Current expected start: 2026-10-24 09:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 08:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-23T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT23BOBFELARROLI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theo Arribage / Albano Olivetti (`KXATPDOUBLES-26OCT23BOBFELARROLI-ARROLI`) | 0.83 / 0.85 (760) | 84.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matisse Bobichon / Kilian Feldbausch (`KXATPDOUBLES-26OCT23BOBFELARROLI-BOBFEL`) | 0.14 / 0.17 (555) | 15.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Vit Kopriva vs Lukas Neumayer -- ATP Vienna Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 12:30Z
* Current expected start: 2026-10-24 09:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 08:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200240:209903:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vit Kopriva (`KXATPMATCH-26OCT24KOPNEU-KOP`) | 0.54 / 0.55 (121) | 54.5% | 56.9% | 51.0% | 54.6% [53.1%-57.1%] | 54.3% | 53.8% | 54.3% | MODEL_LONE_OUTLIER | PASS | +2.4 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Lukas Neumayer (`KXATPMATCH-26OCT24KOPNEU-NEU`) | 0.41 / 0.46 (93) | 43.5% | 43.1% | 49.0% | 45.4% [42.9%-46.9%] | 45.7% | 46.2% | 45.7% | KALSHI_LONE_OUTLIER | PASS | -0.4 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4886.0, B 4653.0; serve-point win A 61.9%, B 39.4%; Elo A 1682.3, B 1568.4; model uncertainty 0.0203
* Form inputs: days since last match A 11, B 11; matches on record A 698, B 376; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.005, surface_dev_loose -0.005, surface_dev_tight +0.005
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT24KOPNEU-KOP21` Will Vit Kopriva win the Vit Kopriva vs Lukas Neumayer match by a set score of 2-1?: 0.01/0.29 mid 15.0%, model 27.1% (projection_v2.0 (prediction ledger)) -- gap +12.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24KOPNEU-KOP20` Will Vit Kopriva win the Vit Kopriva vs Lukas Neumayer match by a set score of 2-0?: 0.01/0.37 mid 19.0%, model 29.8% (projection_v2.0 (prediction ledger)) -- gap +10.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24KOPNEU-NEU21` Will Lukas Neumayer win the Vit Kopriva vs Lukas Neumayer match by a set score of 2-1?: 0.01/0.27 mid 14.0%, model 22.5% (projection_v2.0 (prediction ledger)) -- gap +8.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24KOPNEU-1-KOP` Will Vit Kopriva win set 1 in the Vit Kopriva vs Lukas Neumayer match: 0.02/0.97 mid 49.5%, model 54.6% (projection_v2.0 (prediction ledger)) -- gap +5.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24KOPNEU-NEU20` Will Lukas Neumayer win the Vit Kopriva vs Lukas Neumayer match by a set score of 2-0?: 0.01/0.31 mid 16.0%, model 20.6% (projection_v2.0 (prediction ledger)) -- gap +4.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24KOPNEU-2-KOP` Will Vit Kopriva win set 2 in the Vit Kopriva vs Lukas Neumayer match: 0.02/0.98 mid 50.0%, model 54.6% (projection_v2.0 (prediction ledger)) -- gap +4.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24KOPNEU-2-NEU` Will Lukas Neumayer win set 2 in the Vit Kopriva vs Lukas Neumayer match: 0.02/0.98 mid 50.0%, model 45.4% (projection_v2.0 (prediction ledger)) -- gap -4.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24KOPNEU-1-NEU` Will Lukas Neumayer win set 1 in the Vit Kopriva vs Lukas Neumayer match: 0.02/0.97 mid 49.5%, model 45.4% (projection_v2.0 (prediction ledger)) -- gap -4.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dayana Yastremska vs Xiaodi You -- WTA Guangzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 09:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 08:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214646:215035:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dayana Yastremska (`KXWTAMATCH-26OCT23YASYOU-YAS`) | 0.83 / 0.84 (115) | 83.5% | 66.5% | 37.5% | 48.9% [42.1%-68.9%] | -- | -- | -- | -- | PASS | -17.0 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Xiaodi You (`KXWTAMATCH-26OCT23YASYOU-YOU`) | 0.16 / 0.18 (1921) | 17.0% | 33.5% | 62.5% | 51.1% [31.1%-57.9%] | -- | -- | -- | -- | WATCH | +16.5 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4632.0, B 3618.0; serve-point win A 56.5%, B 46.7%; Elo A 1842.7, B 1651.6; model uncertainty 0.134
* Form inputs: days since last match A 6, B 24; matches on record A 480, B 579; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT23YASYOU-YOU  (YES = Xiaodi You)
Model: 34%
Kalshi: 17%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.027, surface_pool_high -0.032, surface_dev_loose -0.021, surface_dev_tight +0.016
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT23YASYOU-1-YAS` Will Dayana Yastremska win set 1 in the Dayana Yastremska vs Xiaodi You match: 0.73/0.77 mid 75.0%, model 61.2% (projection_v2.0 (prediction ledger)) -- gap -13.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23YASYOU-1-YOU` Will Xiaodi You win set 1 in the Dayana Yastremska vs Xiaodi You match: 0.24/0.26 mid 25.0%, model 38.8% (projection_v2.0 (prediction ledger)) -- gap +13.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23YASYOU-2-YAS` Will Dayana Yastremska win set 2 in the Dayana Yastremska vs Xiaodi You match: 0.27/0.87 mid 57.0%, model 61.2% (projection_v2.0 (prediction ledger)) -- gap +4.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23YASYOU-2-YOU` Will Xiaodi You win set 2 in the Dayana Yastremska vs Xiaodi You match: 0.16/0.58 mid 37.0%, model 38.8% (projection_v2.0 (prediction ledger)) -- gap +1.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Elena Rybakina vs Diana Shnaider -- WTA Ningbo SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 12:30Z
* Current expected start: 2026-10-24 09:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 08:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214981:223670:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elena Rybakina (`KXWTAMATCH-26OCT24RYBSHN-RYB`) | 0.64 / 0.65 (25314) | 64.5% | -- | 86.0% | 85.1% [82.3%-85.9%] | 63.9% | 63.5% | 63.5% | MODEL_LONE_OUTLIER | WATCH | +20.6 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Diana Shnaider (`KXWTAMATCH-26OCT24RYBSHN-SHN`) | 0.36 / 0.37 (11785) | 36.5% | -- | 14.0% | 14.9% [14.1%-17.7%] | 36.1% | 36.9% | 36.9% | MODEL_LONE_OUTLIER | PASS | -21.6 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 6087.0, B 4846.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0184
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT24RYBSHN-RYB  (YES = Elena Rybakina)
Model: 85%
Kalshi: 64%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: EXTERNAL_STALE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, UNKNOWN
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.003, surface_pool_high -0.000, surface_dev_loose +0.006, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT24RYBSHN-22` Over 21.5 games: 0.51/0.52 mid 51.5%, model 65.4% (market_conditioned_v1 (model4_board_v1)) -- gap +13.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT24RYBSHN-27` Over 26.5 games: 0.30/0.32 mid 31.0%, model 41.6% (market_conditioned_v1 (model4_board_v1)) -- gap +10.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT24RYBSHN-17` Over 16.5 games: 0.85/0.89 mid 87.0%, model 96.1% (market_conditioned_v1 (model4_board_v1)) -- gap +9.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nikoloz Basilashvili vs Stefanos Tsitsipas -- ATP Almaty SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 13:00Z
* Current expected start: 2026-10-24 10:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 09:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105932:126774:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikoloz Basilashvili (`KXATPMATCH-26OCT24BASTSI-BAS`) | 0.30 / 0.31 (35769) | 30.5% | 18.9% | 27.5% | 24.0% [20.4%-26.3%] | 30.9% | 30.3% | 30.3% | MODEL_LONE_OUTLIER | PASS | -11.6 pp | REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Stefanos Tsitsipas (`KXATPMATCH-26OCT24BASTSI-TSI`) | 0.70 / 0.71 (35656) | 70.5% | 81.1% | 72.5% | 76.0% [73.7%-79.6%] | 69.1% | 70.5% | 70.5% | MODEL_LONE_OUTLIER | SHADOW_BET | +10.6 pp | REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3254.0, B 5234.0; serve-point win A 64.1%, B 28.5%; Elo A 1696.5, B 1953.8; model uncertainty 0.0298
* Form inputs: days since last match A 0, B 0; matches on record A 915, B 804; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.023, surface_dev_loose +0.016, surface_dev_tight -0.009
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPSETWINNER-26OCT24BASTSI-1-TSI` Will Stefanos Tsitsipas win set 1 in the Nikoloz Basilashvili vs Stefanos Tsitsipas match: 0.61/0.65 mid 63.0%, model 72.2% (projection_v2.0 (prediction ledger)) -- gap +9.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24BASTSI-BAS20` Will Nikoloz Basilashvili win the Nikoloz Basilashvili vs Stefanos Tsitsipas match by a set score of 2-0?: 0.14/0.19 mid 16.5%, model 7.7% (projection_v2.0 (prediction ledger)) -- gap -8.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24BASTSI-TSI4` Will Stefanos Tsitsipas win at least 3.5 more games than Nikoloz Basilashvili?: 0.41/0.42 mid 41.5%, model 50.2% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BASTSI-1-BAS` Will Nikoloz Basilashvili win set 1 in the Nikoloz Basilashvili vs Stefanos Tsitsipas match: 0.34/0.38 mid 36.0%, model 27.8% (projection_v2.0 (prediction ledger)) -- gap -8.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BASTSI-2-TSI` Will Stefanos Tsitsipas win set 2 in the Nikoloz Basilashvili vs Stefanos Tsitsipas match: 0.62/0.68 mid 65.0%, model 72.2% (projection_v2.0 (prediction ledger)) -- gap +7.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24BASTSI-TSI20` Will Stefanos Tsitsipas win the Nikoloz Basilashvili vs Stefanos Tsitsipas match by a set score of 2-0?: 0.43/0.47 mid 45.0%, model 52.1% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24BASTSI-BAS2` Will Nikoloz Basilashvili win at least 1.5 more games than Stefanos Tsitsipas?: 0.16/0.25 mid 20.5%, model 13.6% (projection_v2.0 (prediction ledger)) -- gap -6.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BASTSI-2-BAS` Will Nikoloz Basilashvili win set 2 in the Nikoloz Basilashvili vs Stefanos Tsitsipas match: 0.32/0.36 mid 34.0%, model 27.8% (projection_v2.0 (prediction ledger)) -- gap -6.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24BASTSI-TSI21` Will Stefanos Tsitsipas win the Nikoloz Basilashvili vs Stefanos Tsitsipas match by a set score of 2-1?: 0.22/0.26 mid 24.0%, model 29.0% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24BASTSI-BAS21` Will Nikoloz Basilashvili win the Nikoloz Basilashvili vs Stefanos Tsitsipas match by a set score of 2-1?: 0.12/0.17 mid 14.5%, model 11.2% (projection_v2.0 (prediction ledger)) -- gap -3.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24BASTSI-18` Over 17.5 games: 0.90/0.94 mid 92.0%, model 93.1% (projection_v2.0 (prediction ledger)) -- gap +1.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24BASTSI-28` Over 27.5 games: 0.34/0.35 mid 34.5%, model 35.4% (projection_v2.0 (prediction ledger)) -- gap +0.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24BASTSI-23` Over 22.5 games: 0.55/0.57 mid 56.0%, model 55.5% (projection_v2.0 (prediction ledger)) -- gap -0.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Linda Fruhvirtova vs Katarzyna Kawa -- WTA Guangzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 10:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 09:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:203514:222258:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Linda Fruhvirtova (`KXWTAMATCH-26OCT23FRUKAW-FRU`) | 0.46 / 0.48 (15) | 47.0% | 66.6% | 74.8% | 73.5% [60.0%-76.9%] | -- | -- | -- | -- | WATCH | +19.6 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Katarzyna Kawa (`KXWTAMATCH-26OCT23FRUKAW-KAW`) | 0.52 / 0.54 (1450) | 53.0% | 33.4% | 25.2% | 26.5% [23.1%-40.0%] | -- | -- | -- | -- | PASS | -19.6 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4353.0, B 4311.0; serve-point win A 55.4%, B 47.8%; Elo A 1765.2, B 1620.4; model uncertainty 0.0843
* Form inputs: days since last match A 16, B 1; matches on record A 298, B 705; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT23FRUKAW-FRU  (YES = Linda Fruhvirtova)
Model: 67%
Kalshi: 47%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.027, surface_pool_high +0.034, surface_dev_loose +0.034, surface_dev_tight -0.036
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT23FRUKAW-2-KAW` Will Katarzyna Kawa win set 2 in the Linda Fruhvirtova vs Katarzyna Kawa match: 0.26/0.83 mid 54.5%, model 38.7% (projection_v2.0 (prediction ledger)) -- gap -15.8 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23FRUKAW-1-FRU` Will Linda Fruhvirtova win set 1 in the Linda Fruhvirtova vs Katarzyna Kawa match: 0.46/0.49 mid 47.5%, model 61.3% (projection_v2.0 (prediction ledger)) -- gap +13.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23FRUKAW-1-KAW` Will Katarzyna Kawa win set 1 in the Linda Fruhvirtova vs Katarzyna Kawa match: 0.51/0.54 mid 52.5%, model 38.7% (projection_v2.0 (prediction ledger)) -- gap -13.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23FRUKAW-2-FRU` Will Linda Fruhvirtova win set 2 in the Linda Fruhvirtova vs Katarzyna Kawa match: 0.26/0.84 mid 55.0%, model 61.3% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Yihan Qu vs Teodora Kostovic -- WTA Guangzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 10:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 09:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:264086:267439:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Teodora Kostovic (`KXWTAMATCH-26OCT23YIHKOS-KOS`) | 0.87 / 0.88 (10472) | 87.5% | 97.0% | 92.0% | 94.6% [93.9%-95.4%] | -- | -- | -- | -- | PASS | +9.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yihan Qu (`KXWTAMATCH-26OCT23YIHKOS-YIH`) | 0.13 / 0.14 (363) | 13.5% | 3.0% | 8.0% | 5.4% [4.6%-6.1%] | -- | -- | -- | -- | PASS | -10.5 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 377.0, B 3286.0; serve-point win A 50.3%, B 35.3%; Elo A 1192.8, B 1710.9; model uncertainty 0.0075
* Form inputs: days since last match A 6, B 8; matches on record A 16, B 114; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.007, surface_dev_loose -0.003, surface_dev_tight +0.001
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT23YIHKOS-2-KOS` Will Teodora Kostovic win set 2 in the Yihan Qu vs Teodora Kostovic match: 0.35/0.85 mid 60.0%, model 89.6% (projection_v2.0 (prediction ledger)) -- gap +29.6 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXWTASETWINNER-26OCT23YIHKOS-2-YIH` Will Yihan Qu win set 2 in the Yihan Qu vs Teodora Kostovic match: 0.18/0.38 mid 28.0%, model 10.4% (projection_v2.0 (prediction ledger)) -- gap -17.6 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXWTASETWINNER-26OCT23YIHKOS-1-KOS` Will Teodora Kostovic win set 1 in the Yihan Qu vs Teodora Kostovic match: 0.75/0.78 mid 76.5%, model 89.6% (projection_v2.0 (prediction ledger)) -- gap +13.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXWTASETWINNER-26OCT23YIHKOS-1-YIH` Will Yihan Qu win set 1 in the Yihan Qu vs Teodora Kostovic match: 0.21/0.22 mid 21.5%, model 10.4% (projection_v2.0 (prediction ledger)) -- gap -11.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data POOR
* Warnings: LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Chirag Duhan vs Karan Singh -- M25 Mumbai SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210000:210003:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chirag Duhan (`KXITFMATCH-26OCT24DUHSIN-DUH`) | 0.12 / 0.14 (258) | 13.0% | 28.4% | 69.5% | 33.7% [31.7%-35.5%] | 12.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +15.4 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Karan Singh (`KXITFMATCH-26OCT24DUHSIN-SIN`) | 0.86 / 0.88 (78) | 87.0% | 71.6% | 30.6% | 66.3% [64.5%-68.3%] | 87.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.4 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 54.0, B 1167.0; serve-point win A 62.3%, B 33.1%; Elo A 1204.9, B 1330.3; model uncertainty 0.0193
* Form inputs: days since last match A 697, B 88; matches on record A 56, B 179; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT24DUHSIN-DUH  (YES = Chirag Duhan)
Model: 28%
Kalshi: 13%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose +0.001, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Digvijay Pratap Singh vs Garrett Johns -- M25 Mumbai SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24SINJOH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Garrett Johns (`KXITFMATCH-26OCT24SINJOH-JOH`) | 0.56 / 0.58 (108) | 57.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Digvijay Pratap Singh (`KXITFMATCH-26OCT24SINJOH-SIN`) | 0.40 / 0.44 (144) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Juan Manuel Cerundolo vs Zachary Svajda -- ATP Basel Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 11:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 10:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 09:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207678:208260:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Manuel Cerundolo (`KXATPMATCH-26OCT24CERSVA-CER`) | 0.37 / 0.41 (39) | 39.0% | 51.8% | 48.0% | 48.5% [46.6%-51.0%] | 38.4% | 38.3% | 38.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +12.8 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Zachary Svajda (`KXATPMATCH-26OCT24CERSVA-SVA`) | 0.55 / 0.61 (92) | 58.0% | 48.1% | 52.0% | 51.5% [49.0%-53.4%] | 61.6% | 61.6% | 61.6% | ALL_THREE_DISAGREE | PASS | -9.8 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5318.0, B 3677.0; serve-point win A 65.0%, B 35.4%; Elo A 1750.6, B 1764.3; model uncertainty 0.0222
* Form inputs: days since last match A 3, B 13; matches on record A 507, B 321; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.020, surface_dev_loose -0.015, surface_dev_tight +0.010
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT24CERSVA-1-CER` Will Juan Manuel Cerundolo win set 1 in the Juan Manuel Cerundolo vs Zachary Svajda match: 0.01/0.98 mid 49.5%, model 51.2% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24CERSVA-2-CER` Will Juan Manuel Cerundolo win set 2 in the Juan Manuel Cerundolo vs Zachary Svajda match: 0.01/0.98 mid 49.5%, model 51.2% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24CERSVA-2-SVA` Will Zachary Svajda win set 2 in the Juan Manuel Cerundolo vs Zachary Svajda match: 0.02/0.98 mid 50.0%, model 48.8% (projection_v2.0 (prediction ledger)) -- gap -1.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24CERSVA-1-SVA` Will Zachary Svajda win set 1 in the Juan Manuel Cerundolo vs Zachary Svajda match: 0.01/0.98 mid 49.5%, model 48.8% (projection_v2.0 (prediction ledger)) -- gap -0.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Jaime Faria vs Mika Brunold -- ATP Basel Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 11:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 10:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 09:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:209983:210262:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mika Brunold (`KXATPMATCH-26OCT24FARBRU-BRU`) | 0.40 / 0.43 (53) | 41.5% | 29.1% | 44.5% | 29.8% [17.4%-34.8%] | 42.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.4 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jaime Faria (`KXATPMATCH-26OCT24FARBRU-FAR`) | 0.55 / 0.59 (65) | 57.0% | 70.9% | 55.5% | 70.2% [65.2%-82.6%] | 57.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.9 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4786.0, B 1536.0; serve-point win A 65.1%, B 39.2%; Elo A 1778.3, B 1510.5; model uncertainty 0.0871
* Form inputs: days since last match A 4, B 683; matches on record A 313, B 128; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.004, surface_dev_loose -0.018, surface_dev_tight +0.018
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT24FARBRU-1-FAR` Will Jaime Faria win set 1 in the Jaime Faria vs Mika Brunold match: 0.02/0.97 mid 49.5%, model 64.4% (projection_v2.0 (prediction ledger)) -- gap +14.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT24FARBRU-2-BRU` Will Mika Brunold win set 2 in the Jaime Faria vs Mika Brunold match: 0.02/0.98 mid 50.0%, model 35.6% (projection_v2.0 (prediction ledger)) -- gap -14.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT24FARBRU-2-FAR` Will Jaime Faria win set 2 in the Jaime Faria vs Mika Brunold match: 0.02/0.98 mid 50.0%, model 64.4% (projection_v2.0 (prediction ledger)) -- gap +14.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT24FARBRU-1-BRU` Will Mika Brunold win set 1 in the Jaime Faria vs Mika Brunold match: 0.02/0.97 mid 49.5%, model 35.6% (projection_v2.0 (prediction ledger)) -- gap -13.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data POOR
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Adolfo Daniel Vallejo vs Lorenzo Sonego -- ATP Vienna Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 13:10Z
* Current expected start: 2026-10-24 10:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 09:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T13:10:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:132283:209226:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Sonego (`KXATPMATCH-26OCT24VALSON-SON`) | 0.42 / 0.45 (47) | 43.5% | 46.1% | 60.4% | 60.4% [58.4%-61.8%] | 46.8% | 46.8% | -- | INSUFFICIENT_INPUTS | PASS | +2.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Adolfo Daniel Vallejo (`KXATPMATCH-26OCT24VALSON-VAL`) | 0.54 / 0.57 (126) | 55.5% | 53.9% | 39.6% | 39.6% [38.2%-41.6%] | 53.2% | 53.5% | -- | INSUFFICIENT_INPUTS | PASS | -1.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5092.0, B 4551.0; serve-point win A 64.0%, B 36.8%; Elo A 1707.5, B 1781.5; model uncertainty 0.0168
* Form inputs: days since last match A 13, B 4; matches on record A 211, B 690; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high +0.000, surface_dev_loose -0.014, surface_dev_tight +0.019
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT24VALSON-VAL21` Will Adolfo Daniel Vallejo win the Adolfo Daniel Vallejo vs Lorenzo Sonego match by a set score of 2-1?: 0.02/0.28 mid 15.0%, model 26.2% (projection_v2.0 (prediction ledger)) -- gap +11.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24VALSON-SON21` Will Lorenzo Sonego win the Adolfo Daniel Vallejo vs Lorenzo Sonego match by a set score of 2-1?: 0.01/0.27 mid 14.0%, model 23.6% (projection_v2.0 (prediction ledger)) -- gap +9.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24VALSON-VAL20` Will Adolfo Daniel Vallejo win the Adolfo Daniel Vallejo vs Lorenzo Sonego match by a set score of 2-0?: 0.01/0.37 mid 19.0%, model 27.7% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24VALSON-SON20` Will Lorenzo Sonego win the Adolfo Daniel Vallejo vs Lorenzo Sonego match by a set score of 2-0?: 0.01/0.31 mid 16.0%, model 22.4% (projection_v2.0 (prediction ledger)) -- gap +6.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24VALSON-1-VAL` Will Adolfo Daniel Vallejo win set 1 in the Adolfo Daniel Vallejo vs Lorenzo Sonego match: 0.02/0.97 mid 49.5%, model 52.6% (projection_v2.0 (prediction ledger)) -- gap +3.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24VALSON-2-SON` Will Lorenzo Sonego win set 2 in the Adolfo Daniel Vallejo vs Lorenzo Sonego match: 0.02/0.98 mid 50.0%, model 47.4% (projection_v2.0 (prediction ledger)) -- gap -2.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24VALSON-2-VAL` Will Adolfo Daniel Vallejo win set 2 in the Adolfo Daniel Vallejo vs Lorenzo Sonego match: 0.02/0.98 mid 50.0%, model 52.6% (projection_v2.0 (prediction ledger)) -- gap +2.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24VALSON-1-SON` Will Lorenzo Sonego win set 1 in the Adolfo Daniel Vallejo vs Lorenzo Sonego match: 0.02/0.97 mid 49.5%, model 47.4% (projection_v2.0 (prediction ledger)) -- gap -2.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## An Lin / Lu vs Chanta / Naklo -- W15 Singapore F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 10:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-24T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24ANLLUXCHANAK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| An Lin / Lu (`KXITFWDOUBLES-26OCT24ANLLUXCHANAK-ANLLUX`) | 0.16 / 0.60 (62) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Chanta / Naklo (`KXITFWDOUBLES-26OCT24ANLLUXCHANAK-CHANAK`) | 0.16 / 0.54 (54) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Joel Schwaerzler vs Titouan Droguet -- ATP Vienna Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 13:40Z
* Current expected start: 2026-10-24 11:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 10:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T13:40:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208169:212082:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Titouan Droguet (`KXATPMATCH-26OCT24SCHDRO-DRO`) | 0.68 / 0.72 (974) | 70.0% | 73.8% | 74.0% | 74.0% [73.2%-75.5%] | -- | 70.9% | -- | INSUFFICIENT_INPUTS | PASS | +3.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Joel Schwaerzler (`KXATPMATCH-26OCT24SCHDRO-SCH`) | 0.25 / 0.30 (11) | 27.5% | 26.2% | 26.0% | 26.0% [24.5%-26.8%] | -- | 25.0% | -- | INSUFFICIENT_INPUTS | PASS | -1.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3799.0, B 5236.0; serve-point win A 64.0%, B 30.8%; Elo A 1607.9, B 1798.5; model uncertainty 0.0117
* Form inputs: days since last match A 18, B 3; matches on record A 147, B 394; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.008, surface_dev_loose -0.007, surface_dev_tight -0.001
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT24SCHDRO-SCH21` Will Joel Schwaerzler win the Joel Schwaerzler vs Titouan Droguet match by a set score of 2-1?: 0.02/0.89 mid 45.5%, model 14.9% (projection_v2.0 (prediction ledger)) -- gap -30.6 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24SCHDRO-1-DRO` Will Titouan Droguet win set 1 in the Joel Schwaerzler vs Titouan Droguet match: 0.01/0.98 mid 49.5%, model 66.5% (projection_v2.0 (prediction ledger)) -- gap +17.0 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24SCHDRO-2-DRO` Will Titouan Droguet win set 2 in the Joel Schwaerzler vs Titouan Droguet match: 0.02/0.98 mid 50.0%, model 66.5% (projection_v2.0 (prediction ledger)) -- gap +16.5 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24SCHDRO-1-SCH` Will Joel Schwaerzler win set 1 in the Joel Schwaerzler vs Titouan Droguet match: 0.01/0.98 mid 49.5%, model 33.5% (projection_v2.0 (prediction ledger)) -- gap -16.0 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24SCHDRO-2-SCH` Will Joel Schwaerzler win set 2 in the Joel Schwaerzler vs Titouan Droguet match: 0.01/0.98 mid 49.5%, model 33.5% (projection_v2.0 (prediction ledger)) -- gap -16.0 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24SCHDRO-DRO21` Will Titouan Droguet win the Joel Schwaerzler vs Titouan Droguet match by a set score of 2-1?: 0.01/0.85 mid 43.0%, model 29.6% (projection_v2.0 (prediction ledger)) -- gap -13.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24SCHDRO-SCH20` Will Joel Schwaerzler win the Joel Schwaerzler vs Titouan Droguet match by a set score of 2-0?: 0.02/0.43 mid 22.5%, model 11.2% (projection_v2.0 (prediction ledger)) -- gap -11.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24SCHDRO-DRO20` Will Titouan Droguet win the Joel Schwaerzler vs Titouan Droguet match by a set score of 2-0?: 0.01/0.77 mid 39.0%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Anastasia Zakharova vs Ruien Zhang -- WTA Guangzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 11:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 10:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:220435:263869:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasia Zakharova (`KXWTAMATCH-26OCT23ZAKZHA-ZAK`) | 0.90 / 0.91 (43) | 90.5% | 87.7% | 89.9% | 89.4% [87.7%-90.1%] | -- | -- | -- | -- | PASS | -2.8 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ruien Zhang (`KXWTAMATCH-26OCT23ZAKZHA-ZHA`) | 0.08 / 0.09 (2006) | 8.5% | 12.3% | 10.1% | 10.6% [9.9%-12.3%] | -- | -- | -- | -- | PASS | +3.8 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4628.0, B 1375.0; serve-point win A 61.5%, B 47.4%; Elo A 1813.0, B 1448.5; model uncertainty 0.012
* Form inputs: days since last match A 2, B 18; matches on record A 481, B 107; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.007, surface_dev_loose +0.007, surface_dev_tight -0.010
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT23ZAKZHA-2-ZAK` Will Anastasia Zakharova win set 2 in the Anastasia Zakharova vs Ruien Zhang match: 0.41/0.85 mid 63.0%, model 78.1% (projection_v2.0 (prediction ledger)) -- gap +15.1 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23ZAKZHA-1-ZAK` Will Anastasia Zakharova win set 1 in the Anastasia Zakharova vs Ruien Zhang match: 0.85/0.88 mid 86.5%, model 78.1% (projection_v2.0 (prediction ledger)) -- gap -8.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23ZAKZHA-1-ZHA` Will Ruien Zhang win set 1 in the Anastasia Zakharova vs Ruien Zhang match: 0.12/0.16 mid 14.0%, model 21.9% (projection_v2.0 (prediction ledger)) -- gap +7.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23ZAKZHA-2-ZHA` Will Ruien Zhang win set 2 in the Anastasia Zakharova vs Ruien Zhang match: 0.14/0.17 mid 15.5%, model 21.9% (projection_v2.0 (prediction ledger)) -- gap +6.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nicolas Barrientos / David Pel vs Sadio Doumbia / Bart Stevens -- ATP Brussels SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 15:00Z
* Current expected start: 2026-10-24 11:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 10:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-24T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24BARPELDOUSTE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Barrientos / David Pel (`KXATPDOUBLES-26OCT24BARPELDOUSTE-BARPEL`) | 0.43 / 0.45 (478) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sadio Doumbia / Bart Stevens (`KXATPDOUBLES-26OCT24BARPELDOUSTE-DOUSTE`) | 0.54 / 0.57 (581) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## D Prajwal Dev / Kumar Sinha vs Kalyanpur / Mukund -- M25 Mumbai F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-24T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24DPRKUMKALMUK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D Prajwal Dev / Kumar Sinha (`KXITFDOUBLES-26OCT24DPRKUMKALMUK-DPRKUM`) | 0.05 / 0.95 (38) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kalyanpur / Mukund (`KXITFDOUBLES-26OCT24DPRKUMKALMUK-KALMUK`) | 0.06 / 0.90 (5) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Masabayashi / Suksumrarn vs Kawachi / Ogura -- M15 Singapore F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-24T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24MASSUKKAWOGU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kawachi / Ogura (`KXITFDOUBLES-26OCT24MASSUKKAWOGU-KAWOGU`) | 0.06 / 0.50 (3) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Masabayashi / Suksumrarn (`KXITFDOUBLES-26OCT24MASSUKKAWOGU-MASSUK`) | 0.35 / 0.64 (69) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sebastian Baez vs Giovanni Mpetshi Perricard -- ATP Basel Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 11:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 12:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 11:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:202104:208659:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sebastian Baez (`KXATPMATCH-26OCT24BAEMPE-BAE`) | 0.52 / 0.53 (87) | 52.5% | 54.9% | 59.3% | 57.5% [56.1%-58.4%] | 50.0% | 50.0% | -- | INSUFFICIENT_INPUTS | PASS | +2.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Giovanni Mpetshi Perricard (`KXATPMATCH-26OCT24BAEMPE-MPE`) | 0.45 / 0.50 (109) | 47.5% | 45.1% | 40.7% | 42.5% [41.6%-43.9%] | 50.0% | 50.0% | -- | INSUFFICIENT_INPUTS | PASS | -2.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4992.0, B 3847.0; serve-point win A 69.5%, B 31.5%; Elo A 1715.5, B 1698.8; model uncertainty 0.0116
* Form inputs: days since last match A 3, B 6; matches on record A 494, B 309; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose -0.005, surface_dev_tight +0.000
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT24BAEMPE-1-BAE` Will Sebastian Baez win set 1 in the Sebastian Baez vs Giovanni Mpetshi Perricard match: 0.01/0.98 mid 49.5%, model 53.3% (projection_v2.0 (prediction ledger)) -- gap +3.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BAEMPE-2-BAE` Will Sebastian Baez win set 2 in the Sebastian Baez vs Giovanni Mpetshi Perricard match: 0.02/0.98 mid 50.0%, model 53.3% (projection_v2.0 (prediction ledger)) -- gap +3.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BAEMPE-2-MPE` Will Giovanni Mpetshi Perricard win set 2 in the Sebastian Baez vs Giovanni Mpetshi Perricard match: 0.02/0.98 mid 50.0%, model 46.7% (projection_v2.0 (prediction ledger)) -- gap -3.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BAEMPE-1-MPE` Will Giovanni Mpetshi Perricard win set 1 in the Sebastian Baez vs Giovanni Mpetshi Perricard match: 0.01/0.98 mid 49.5%, model 46.7% (projection_v2.0 (prediction ledger)) -- gap -2.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Alex Molcan vs Hamad Medjedovic -- ATP Vienna Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 14:20Z
* Current expected start: 2026-10-24 12:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 11:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-140_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T14:20:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144684:209098:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hamad Medjedovic (`KXATPMATCH-26OCT24MOLMED-MED`) | 0.58 / 0.59 (139) | 58.5% | 46.4% | 40.8% | 43.6% [41.7%-45.6%] | 56.6% | 56.6% | 56.6% | MODEL_LONE_OUTLIER | PASS | -12.2 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Alex Molcan (`KXATPMATCH-26OCT24MOLMED-MOL`) | 0.41 / 0.44 (138) | 42.5% | 53.6% | 59.2% | 56.4% [54.4%-58.3%] | 43.4% | 41.2% | 43.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +11.2 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3131.0, B 3309.0; serve-point win A 65.6%, B 35.1%; Elo A 1748.0, B 1741.5; model uncertainty 0.0193
* Form inputs: days since last match A 16, B 3; matches on record A 508, B 285; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.010, surface_dev_loose +0.014, surface_dev_tight -0.009
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT24MOLMED-MOL21` Will Alex Molcan win the Alex Molcan vs Hamad Medjedovic match by a set score of 2-1?: 0.01/0.25 mid 13.0%, model 26.2% (projection_v2.0 (prediction ledger)) -- gap +13.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MOLMED-MOL20` Will Alex Molcan win the Alex Molcan vs Hamad Medjedovic match by a set score of 2-0?: 0.01/0.30 mid 15.5%, model 27.5% (projection_v2.0 (prediction ledger)) -- gap +12.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MOLMED-MED21` Will Hamad Medjedovic win the Alex Molcan vs Hamad Medjedovic match by a set score of 2-1?: 0.01/0.29 mid 15.0%, model 23.7% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MOLMED-1-MOL` Will Alex Molcan win set 1 in the Alex Molcan vs Hamad Medjedovic match: 0.01/0.98 mid 49.5%, model 52.4% (projection_v2.0 (prediction ledger)) -- gap +2.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MOLMED-2-MED` Will Hamad Medjedovic win set 2 in the Alex Molcan vs Hamad Medjedovic match: 0.02/0.98 mid 50.0%, model 47.6% (projection_v2.0 (prediction ledger)) -- gap -2.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MOLMED-2-MOL` Will Alex Molcan win set 2 in the Alex Molcan vs Hamad Medjedovic match: 0.02/0.98 mid 50.0%, model 52.4% (projection_v2.0 (prediction ledger)) -- gap +2.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MOLMED-MED20` Will Hamad Medjedovic win the Alex Molcan vs Hamad Medjedovic match by a set score of 2-0?: 0.01/0.40 mid 20.5%, model 22.6% (projection_v2.0 (prediction ledger)) -- gap +2.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MOLMED-1-MED` Will Hamad Medjedovic win set 1 in the Alex Molcan vs Hamad Medjedovic match: 0.01/0.98 mid 49.5%, model 47.6% (projection_v2.0 (prediction ledger)) -- gap -1.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tommy Paul vs Taylor Fritz -- ATP Lyon SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 13:00Z
* Current expected start: 2026-10-24 12:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 11:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-60_MIN

ATP (TOUR_500_250) · Clay · scheduled 2026-10-24T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126203:126205:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Taylor Fritz (`KXATPMATCH-26OCT24PAUFRI-FRI`) | 0.63 / 0.65 (25532) | 64.0% | 41.4% | 52.9% | 49.0% [46.6%-51.4%] | -- | -- | -- | -- | PASS | -22.6 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tommy Paul (`KXATPMATCH-26OCT24PAUFRI-PAU`) | 0.36 / 0.37 (55582) | 36.5% | 58.6% | 47.1% | 51.0% [48.5%-53.4%] | -- | -- | -- | -- | SHADOW_BET | +22.1 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5709.0, B 6022.0; serve-point win A 67.5%, B 34.3%; Elo A 1995.2, B 1884.4; model uncertainty 0.0242
* Form inputs: days since last match A 2, B 1; matches on record A 721, B 740; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT24PAUFRI-PAU  (YES = Tommy Paul)
Model: 59%
Kalshi: 36%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, UNKNOWN
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.015, surface_dev_loose +0.024, surface_dev_tight -0.024
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT24PAUFRI-FRI3` Will Taylor Fritz win at least 2.5 more games than Tommy Paul?: 0.48/0.50 mid 49.0%, model 26.5% (projection_v2.0 (prediction ledger)) -- gap -22.5 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24PAUFRI-PAU2` Will Tommy Paul win at least 1.5 more games than Taylor Fritz?: 0.27/0.30 mid 28.5%, model 50.5% (projection_v2.0 (prediction ledger)) -- gap +22.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24PAUFRI-FRI20` Will Taylor Fritz win the Tommy Paul vs Taylor Fritz match by a set score of 2-0?: 0.38/0.42 mid 40.0%, model 19.6% (projection_v2.0 (prediction ledger)) -- gap -20.4 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24PAUFRI-FRI6` Will Taylor Fritz win at least 5.5 more games than Tommy Paul?: 0.09/0.37 mid 23.0%, model 4.2% (projection_v2.0 (prediction ledger)) -- gap -18.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24PAUFRI-2-FRI` Will Taylor Fritz win set 2 in the Tommy Paul vs Taylor Fritz match: 0.58/0.64 mid 61.0%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap -16.8 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24PAUFRI-2-PAU` Will Tommy Paul win set 2 in the Tommy Paul vs Taylor Fritz match: 0.36/0.42 mid 39.0%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap +16.8 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24PAUFRI-1-PAU` Will Tommy Paul win set 1 in the Tommy Paul vs Taylor Fritz match: 0.40/0.41 mid 40.5%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap +15.3 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24PAUFRI-1-FRI` Will Taylor Fritz win set 1 in the Tommy Paul vs Taylor Fritz match: 0.57/0.61 mid 59.0%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap -14.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24PAUFRI-PAU20` Will Tommy Paul win the Tommy Paul vs Taylor Fritz match by a set score of 2-0?: 0.17/0.20 mid 18.5%, model 31.1% (projection_v2.0 (prediction ledger)) -- gap +12.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24PAUFRI-PAU21` Will Tommy Paul win the Tommy Paul vs Taylor Fritz match by a set score of 2-1?: 0.14/0.19 mid 16.5%, model 27.5% (projection_v2.0 (prediction ledger)) -- gap +11.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24PAUFRI-24` Over 23.5 games: 0.47/0.49 mid 48.0%, model 56.2% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24PAUFRI-29` Over 28.5 games: 0.31/0.34 mid 32.5%, model 39.4% (projection_v2.0 (prediction ledger)) -- gap +6.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24PAUFRI-19` Over 18.5 games: 0.83/0.87 mid 85.0%, model 91.6% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24PAUFRI-FRI21` Will Taylor Fritz win the Tommy Paul vs Taylor Fritz match by a set score of 2-1?: 0.22/0.25 mid 23.5%, model 21.8% (projection_v2.0 (prediction ledger)) -- gap -1.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: NO_EXTERNAL_PRICE; WIDE_SPREAD

## Madelyn Nugroho / Zheng vs Panshina / Zolotareva -- W35 Qian Daohu F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-24T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24MADZHEPANZOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Madelyn Nugroho / Zheng (`KXITFWDOUBLES-26OCT24MADZHEPANZOL-MADZHE`) | 0.16 / 0.40 (41) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Panshina / Zolotareva (`KXITFWDOUBLES-26OCT24MADZHEPANZOL-PANZOL`) | 0.05 / 0.75 (100) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Henry Bernet vs Daniel Altmaier -- ATP Basel Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 11:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 12:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 11:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:127157:148679:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Altmaier (`KXATPMATCH-26OCT24BERALT-ALT`) | 0.60 / 0.63 (200) | 61.5% | 63.4% | 48.5% | 63.8% [53.9%-76.5%] | 61.6% | 62.7% | -- | INSUFFICIENT_INPUTS | PASS | +1.9 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Henry Bernet (`KXATPMATCH-26OCT24BERALT-BER`) | 0.34 / 0.38 (68) | 36.0% | 36.6% | 51.5% | 36.2% [23.5%-46.1%] | 38.4% | 38.7% | -- | INSUFFICIENT_INPUTS | PASS | +0.6 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1360.0, B 5258.0; serve-point win A 64.8%, B 32.4%; Elo A 1515.4, B 1714.1; model uncertainty 0.1134
* Form inputs: days since last match A 11, B 1; matches on record A 34, B 707; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.066, surface_pool_high +0.080, surface_dev_loose +0.019, surface_dev_tight -0.023
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT24BERALT-1-ALT` Will Daniel Altmaier win set 1 in the Henry Bernet vs Daniel Altmaier match: 0.02/0.97 mid 49.5%, model 59.0% (projection_v2.0 (prediction ledger)) -- gap +9.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BERALT-2-ALT` Will Daniel Altmaier win set 2 in the Henry Bernet vs Daniel Altmaier match: 0.02/0.98 mid 50.0%, model 59.0% (projection_v2.0 (prediction ledger)) -- gap +9.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BERALT-2-BER` Will Henry Bernet win set 2 in the Henry Bernet vs Daniel Altmaier match: 0.02/0.98 mid 50.0%, model 41.0% (projection_v2.0 (prediction ledger)) -- gap -9.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BERALT-1-BER` Will Henry Bernet win set 1 in the Henry Bernet vs Daniel Altmaier match: 0.02/0.97 mid 49.5%, model 41.0% (projection_v2.0 (prediction ledger)) -- gap -8.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Fabian Marozsan vs Sebastian Sorger -- ATP Vienna Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 14:50Z
* Current expected start: 2026-10-24 12:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 11:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-140_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T14:50:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:206681:210285:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fabian Marozsan (`KXATPMATCH-26OCT24MARSOR-MAR`) | 0.85 / 0.88 (98) | 86.5% | 86.7% | 75.9% | 88.1% [84.0%-91.7%] | -- | -- | -- | -- | PASS | +0.2 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sebastian Sorger (`KXATPMATCH-26OCT24MARSOR-SOR`) | 0.11 / 0.15 (232) | 13.0% | 13.3% | 24.1% | 11.9% [8.3%-16.0%] | -- | -- | -- | -- | PASS | +0.3 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4525.0, B 572.0; serve-point win A 67.5%, B 41.3%; Elo A 1780.4, B 1368.9; model uncertainty 0.0387
* Form inputs: days since last match A 3, B 46; matches on record A 440, B 154; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.024, surface_dev_loose -0.000, surface_dev_tight -0.000
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT24MARSOR-SOR20` Will Sebastian Sorger win the Fabian Marozsan vs Sebastian Sorger match by a set score of 2-0?: 0.01/0.91 mid 46.0%, model 5.2% (projection_v2.0 (prediction ledger)) -- gap -40.8 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPEXACTMATCH-26OCT24MARSOR-SOR21` Will Sebastian Sorger win the Fabian Marozsan vs Sebastian Sorger match by a set score of 2-1?: 0.01/0.87 mid 44.0%, model 8.1% (projection_v2.0 (prediction ledger)) -- gap -35.9 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPSETWINNER-26OCT24MARSOR-1-MAR` Will Fabian Marozsan win set 1 in the Fabian Marozsan vs Sebastian Sorger match: 0.01/0.98 mid 49.5%, model 77.1% (projection_v2.0 (prediction ledger)) -- gap +27.6 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT24MARSOR-2-MAR` Will Fabian Marozsan win set 2 in the Fabian Marozsan vs Sebastian Sorger match: 0.02/0.98 mid 50.0%, model 77.1% (projection_v2.0 (prediction ledger)) -- gap +27.1 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT24MARSOR-2-SOR` Will Sebastian Sorger win set 2 in the Fabian Marozsan vs Sebastian Sorger match: 0.02/0.98 mid 50.0%, model 22.9% (projection_v2.0 (prediction ledger)) -- gap -27.1 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT24MARSOR-1-SOR` Will Sebastian Sorger win set 1 in the Fabian Marozsan vs Sebastian Sorger match: 0.01/0.98 mid 49.5%, model 22.9% (projection_v2.0 (prediction ledger)) -- gap -26.6 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPEXACTMATCH-26OCT24MARSOR-MAR20` Will Fabian Marozsan win the Fabian Marozsan vs Sebastian Sorger match by a set score of 2-0?: 0.01/0.85 mid 43.0%, model 59.5% (projection_v2.0 (prediction ledger)) -- gap +16.5 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPEXACTMATCH-26OCT24MARSOR-MAR21` Will Fabian Marozsan win the Fabian Marozsan vs Sebastian Sorger match by a set score of 2-1?: 0.01/0.25 mid 13.0%, model 27.2% (projection_v2.0 (prediction ledger)) -- gap +14.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
* Warnings: NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sandro Kopp vs Filippo Romano -- ATP Challenger Florence SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-24T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24KOPROM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sandro Kopp (`KXATPCHALLENGERMATCH-26OCT24KOPROM-KOP`) | 0.53 / 0.54 (2328) | 53.5% | -- | -- | -- [-----] | 53.1% | 52.7% | 52.7% | MARKETS_AGREE | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Filippo Romano (`KXATPCHALLENGERMATCH-26OCT24KOPROM-ROM`) | 0.46 / 0.47 (3249) | 46.5% | -- | -- | -- [-----] | 46.9% | 47.9% | 47.9% | MARKETS_AGREE | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Daniil Medvedev vs Alexander Bublik -- ATP Almaty SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 16:00Z
* Current expected start: 2026-10-24 13:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 12:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:106421:122330:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Bublik (`KXATPMATCH-26OCT24MEDBUB-BUB`) | 0.35 / 0.36 (2164) | 35.5% | 32.6% | 30.5% | 30.5% [29.6%-32.1%] | -- | -- | -- | -- | PASS | -3.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daniil Medvedev (`KXATPMATCH-26OCT24MEDBUB-MED`) | 0.65 / 0.66 (47350) | 65.5% | 67.5% | 69.5% | 69.5% [67.8%-70.4%] | -- | -- | -- | -- | WATCH | +1.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5908.0, B 5279.0; serve-point win A 68.3%, B 35.4%; Elo A 2100.7, B 1950.5; model uncertainty 0.0126
* Form inputs: days since last match A 1, B 10; matches on record A 859, B 705; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose -0.000, surface_dev_tight +0.001
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT24MEDBUB-MED6` Will Daniil Medvedev win at least 5.5 more games than Alexander Bublik?: 0.06/0.54 mid 30.0%, model 12.0% (projection_v2.0 (prediction ledger)) -- gap -18.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MEDBUB-2-BUB` Will Alexander Bublik win set 2 in the Daniil Medvedev vs Alexander Bublik match: 0.02/0.98 mid 50.0%, model 38.1% (projection_v2.0 (prediction ledger)) -- gap -11.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MEDBUB-2-MED` Will Daniil Medvedev win set 2 in the Daniil Medvedev vs Alexander Bublik match: 0.02/0.98 mid 50.0%, model 61.9% (projection_v2.0 (prediction ledger)) -- gap +11.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MEDBUB-MED21` Will Daniil Medvedev win the Daniil Medvedev vs Alexander Bublik match by a set score of 2-1?: 0.13/0.28 mid 20.5%, model 29.2% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24MEDBUB-24` Over 23.5 games: 0.47/0.48 mid 47.5%, model 53.7% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MEDBUB-MED20` Will Daniil Medvedev win the Daniil Medvedev vs Alexander Bublik match by a set score of 2-0?: 0.25/0.41 mid 33.0%, model 38.3% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24MEDBUB-BUB2` Will Alexander Bublik win at least 1.5 more games than Daniil Medvedev?: 0.28/0.32 mid 30.0%, model 25.5% (projection_v2.0 (prediction ledger)) -- gap -4.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24MEDBUB-29` Over 28.5 games: 0.30/0.36 mid 33.0%, model 37.2% (projection_v2.0 (prediction ledger)) -- gap +4.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MEDBUB-BUB20` Will Alexander Bublik win the Daniil Medvedev vs Alexander Bublik match by a set score of 2-0?: 0.03/0.19 mid 11.0%, model 14.5% (projection_v2.0 (prediction ledger)) -- gap +3.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MEDBUB-BUB21` Will Alexander Bublik win the Daniil Medvedev vs Alexander Bublik match by a set score of 2-1?: 0.09/0.21 mid 15.0%, model 18.0% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24MEDBUB-MED3` Will Daniil Medvedev win at least 2.5 more games than Alexander Bublik?: 0.48/0.49 mid 48.5%, model 50.7% (projection_v2.0 (prediction ledger)) -- gap +2.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MEDBUB-1-BUB` Will Alexander Bublik win set 1 in the Daniil Medvedev vs Alexander Bublik match: 0.37/0.39 mid 38.0%, model 38.1% (projection_v2.0 (prediction ledger)) -- gap +0.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MEDBUB-1-MED` Will Daniil Medvedev win set 1 in the Daniil Medvedev vs Alexander Bublik match: 0.60/0.64 mid 62.0%, model 61.9% (projection_v2.0 (prediction ledger)) -- gap -0.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT24MEDBUB-19` Over 18.5 games: 0.88/0.92 mid 90.0%, model 90.0% (projection_v2.0 (prediction ledger)) -- gap +0.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Viacheslav Bielinskyi vs Alessio Basile -- M15 Bol QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209907:211450:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alessio Basile (`KXITFMATCH-26OCT24BIEBAS-BAS`) | 0.30 / 0.43 (6) | 36.5% | 13.7% | 52.6% | 19.8% [17.4%-22.8%] | -- | -- | -- | -- | PASS | -22.8 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Viacheslav Bielinskyi (`KXITFMATCH-26OCT24BIEBAS-BIE`) | 0.49 / 0.71 (86) | 60.0% | 86.3% | 47.4% | 80.2% [77.2%-82.6%] | -- | -- | -- | -- | PASS | +26.3 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 154.0, B 0.0; serve-point win A 64.9%, B 43.6%; Elo A 1478.6, B 1236.3; model uncertainty 0.027
* Form inputs: days since last match A 406, B 795; matches on record A 153, B 23; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT24BIEBAS-BIE  (YES = Viacheslav Bielinskyi)
Model: 86%
Kalshi: 60%
Gap: +26 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.030, surface_dev_loose +0.000, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marek Gengel vs Arda Azkara -- M15 Sharm ElSheikh SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200309:207907:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arda Azkara (`KXITFMATCH-26OCT24GENAZK-AZK`) | 0.36 / 0.40 (100) | 38.0% | 27.1% | 58.0% | 32.6% [25.6%-38.2%] | -- | -- | -- | -- | PASS | -10.9 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marek Gengel (`KXITFMATCH-26OCT24GENAZK-GEN`) | 0.50 / 0.63 (123) | 56.5% | 72.9% | 42.0% | 67.4% [61.8%-74.4%] | -- | -- | -- | -- | PASS | +16.4 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1422.0, B 548.0; serve-point win A 65.9%, B 39.0%; Elo A 1610.4, B 1418.2; model uncertainty 0.0627
* Form inputs: days since last match A 683, B 88; matches on record A 535, B 51; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT24GENAZK-GEN  (YES = Marek Gengel)
Model: 73%
Kalshi: 56%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.023, surface_pool_high +0.018, surface_dev_loose -0.005, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nico Hipfl vs Ivan Biletic -- M15 Bol QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211503:212919:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ivan Biletic (`KXITFMATCH-26OCT24HIPBIL-BIL`) | 0.16 / 0.22 (136) | 19.0% | 31.5% | 42.0% | 46.0% [46.0%-46.0%] | -- | -- | -- | -- | PASS | +12.5 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Nico Hipfl (`KXITFMATCH-26OCT24HIPBIL-HIP`) | 0.62 / 0.79 (119) | 70.5% | 68.5% | 58.0% | 54.0% [54.0%-54.0%] | -- | -- | -- | -- | PASS | -2.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 101.0, B 0.0; serve-point win A 64.3%, B 39.5%; Elo A 1285.0, B 1254.8; model uncertainty 0.0001
* Form inputs: days since last match A 97, B 879; matches on record A 16, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Imanol Lopez Morillo vs Alan Wazny -- M15 Bol QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202209:213048:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Imanol Lopez Morillo (`KXITFMATCH-26OCT24LOPWAZ-LOP`) | 0.40 / 0.58 (12) | 49.0% | 79.9% | 47.9% | 70.9% [64.0%-78.1%] | -- | -- | -- | -- | PASS | +30.9 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alan Wazny (`KXITFMATCH-26OCT24LOPWAZ-WAZ`) | 0.32 / 0.50 (150) | 41.0% | 20.1% | 52.1% | 29.1% [21.9%-36.0%] | -- | -- | -- | -- | PASS | -20.9 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 173.0, B 252.0; serve-point win A 61.1%, B 45.3%; Elo A 1396.8, B 1217.0; model uncertainty 0.0705
* Form inputs: days since last match A 25, B 39; matches on record A 282, B 7; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT24LOPWAZ-LOP  (YES = Imanol Lopez Morillo)
Model: 80%
Kalshi: 49%
Gap: +31 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.056, surface_pool_high -0.056, surface_dev_loose -0.000, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oskari Paldanius vs Sergey Petrov -- M15 Sharm ElSheikh SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24PALPET:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oskari Paldanius (`KXITFMATCH-26OCT24PALPET-PAL`) | 0.59 / 0.72 (197) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sergey Petrov (`KXITFMATCH-26OCT24PALPET-PET`) | 0.27 / 0.33 (142) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marco Trungelliti vs Alexander Ritschard -- ATP Challenger Lisbon SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-24T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24TRURIT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Ritschard (`KXATPCHALLENGERMATCH-26OCT24TRURIT-RIT`) | 0.46 / 0.47 (2837) | 46.5% | -- | -- | -- [-----] | 46.9% | 47.0% | 47.0% | MARKETS_AGREE | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marco Trungelliti (`KXATPCHALLENGERMATCH-26OCT24TRURIT-TRU`) | 0.53 / 0.54 (1952) | 53.5% | -- | -- | -- [-----] | 53.1% | 53.5% | 53.5% | MARKETS_AGREE | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Kamilla Bartone vs Lamis Alhussein Abdel Aziz -- W15 Sharm ElSheikh SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213974:221886:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lamis Alhussein Abdel Aziz (`KXITFWMATCH-26OCT24BARALH-ALH`) | 0.51 / 0.63 (20) | 57.0% | -- | 88.5% | 76.3% [67.0%-80.9%] | -- | -- | -- | -- | PASS | +19.3 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kamilla Bartone (`KXITFWMATCH-26OCT24BARALH-BAR`) | 0.33 / 0.41 (45) | 37.0% | -- | 11.5% | 23.7% [19.1%-33.0%] | -- | -- | -- | -- | PASS | -13.3 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1376.0, B 4747.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0695
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT24BARALH-ALH  (YES = Lamis Alhussein Abdel Aziz)
Model: 76%
Kalshi: 57%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose +0.000, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daria Gorska vs Mia Horvit -- W15 Bol QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213551:239484:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daria Gorska (`KXITFWMATCH-26OCT24GORHOR-GOR`) | 0.23 / 0.24 (554) | 23.5% | -- | 43.7% | 37.0% [30.2%-40.1%] | 28.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.5 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mia Horvit (`KXITFWMATCH-26OCT24GORHOR-HOR`) | 0.72 / 0.76 (30) | 74.0% | -- | 56.3% | 63.0% [60.0%-69.8%] | 71.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.0 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 685.0, B 1568.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0494
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.039, surface_pool_high +0.030, surface_dev_loose +0.000, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andrea Obradovic vs Sapfo Sakellaridi -- W15 Bol QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220364:239474:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrea Obradovic (`KXITFWMATCH-26OCT24OBRSAK-OBR`) | 0.35 / 0.40 (45) | 37.5% | -- | 22.7% | 36.6% [30.9%-43.7%] | -- | -- | -- | -- | PASS | -0.9 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sapfo Sakellaridi (`KXITFWMATCH-26OCT24OBRSAK-SAK`) | 0.59 / 0.63 (67) | 61.0% | -- | 77.3% | 63.4% [56.3%-69.1%] | -- | -- | -- | -- | PASS | +2.4 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 929.0, B 4165.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0643
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.058, surface_pool_high +0.061, surface_dev_loose -0.015, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Karla Popovic vs Sandra Samir -- W15 Sharm ElSheikh SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:210500:211529:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karla Popovic (`KXITFWMATCH-26OCT24POPSAM-POP`) | 0.49 / 0.52 (2) | 50.5% | -- | 51.6% | 42.5% [32.9%-48.9%] | -- | -- | -- | -- | PASS | -8.0 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sandra Samir (`KXITFWMATCH-26OCT24POPSAM-SAM`) | 0.46 / 0.51 (0) | 48.5% | -- | 48.4% | 57.5% [51.1%-67.1%] | -- | -- | -- | -- | WATCH | +9.0 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1204.0, B 4604.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0802
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.031, surface_pool_high +0.021, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tara Wuerth vs Viktoria Varga -- W15 Bol QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24WUEVAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Viktoria Varga (`KXITFWMATCH-26OCT24WUEVAR-VAR`) | 0.03 / 0.06 (13) | 4.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tara Wuerth (`KXITFWMATCH-26OCT24WUEVAR-WUE`) | 0.94 / 0.97 (202) | 95.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sonja Zhenikhova vs Maja Radenkovic -- W15 Bol QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222041:264961:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maja Radenkovic (`KXITFWMATCH-26OCT24ZHERAD-RAD`) | 0.16 / 0.20 (25) | 18.0% | -- | 61.6% | 35.4% [34.4%-36.4%] | -- | -- | -- | -- | PASS | +17.4 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Sonja Zhenikhova (`KXITFWMATCH-26OCT24ZHERAD-ZHE`) | 0.78 / 0.82 (608) | 80.0% | -- | 38.4% | 64.6% [63.6%-65.6%] | -- | -- | -- | -- | PASS | -15.4 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1212.0, B 0.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.01
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT24ZHERAD-RAD  (YES = Maja Radenkovic)
Model: 35%
Kalshi: 18%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Jacopo Bilardo / Giorgio Ricca (`KXATPCHALLENGERDOUBLES-26OCT24NANROSBILRIC-BILRIC`) | 0.05 / 0.95 (223) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mattia Nannelli / Leonardo Rossi (`KXATPCHALLENGERDOUBLES-26OCT24NANROSBILRIC-NANROS`) | 0.05 / 0.95 (223) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 12:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105902:206499:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| James Duckworth (`KXATPMATCH-26OCT24KOVDUC-DUC`) | 0.35 / 0.36 (88) | 35.5% | 44.8% | 56.5% | 54.6% [51.9%-57.9%] | 37.7% | 41.3% | 37.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +9.3 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Aleksandar Kovacevic (`KXATPMATCH-26OCT24KOVDUC-KOV`) | 0.62 / 0.68 (198) | 65.0% | 55.2% | 43.5% | 45.4% [42.1%-48.1%] | 62.3% | 66.6% | 62.3% | MODEL_LONE_OUTLIER | PASS | -9.8 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4778.0, B 5151.0; serve-point win A 70.5%, B 30.6%; Elo A 1756.5, B 1745.6; model uncertainty 0.0303
* Form inputs: days since last match A 3, B 0; matches on record A 400, B 900; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.032, surface_pool_high +0.028, surface_dev_loose +0.005, surface_dev_tight -0.005
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT24KOVDUC-1-DUC` Will James Duckworth win set 1 in the Aleksandar Kovacevic vs James Duckworth match: 0.02/0.46 mid 24.0%, model 46.5% (projection_v2.0 (prediction ledger)) -- gap +22.5 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24KOVDUC-1-KOV` Will Aleksandar Kovacevic win set 1 in the Aleksandar Kovacevic vs James Duckworth match: 0.25/0.91 mid 58.0%, model 53.5% (projection_v2.0 (prediction ledger)) -- gap -4.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24KOVDUC-2-DUC` Will James Duckworth win set 2 in the Aleksandar Kovacevic vs James Duckworth match: 0.02/0.98 mid 50.0%, model 46.5% (projection_v2.0 (prediction ledger)) -- gap -3.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24KOVDUC-2-KOV` Will Aleksandar Kovacevic win set 2 in the Aleksandar Kovacevic vs James Duckworth match: 0.02/0.98 mid 50.0%, model 53.5% (projection_v2.0 (prediction ledger)) -- gap +3.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Geoffrey Blancaneaux vs Giannicola Misasi -- M15 Bol QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 13:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144972:208401:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Geoffrey Blancaneaux (`KXITFMATCH-26OCT24BLAMIS-BLA`) | 0.69 / 0.84 (100) | 76.5% | 91.3% | 44.9% | 87.9% [86.9%-89.4%] | -- | -- | -- | -- | PASS | +14.8 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Giannicola Misasi (`KXITFMATCH-26OCT24BLAMIS-MIS`) | 0.15 / 0.20 (163) | 17.5% | 8.6% | 55.1% | 12.0% [10.6%-13.1%] | -- | -- | -- | -- | PASS | -8.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3141.0, B 0.0; serve-point win A 66.9%, B 43.8%; Elo A 1522.5, B 1172.9; model uncertainty 0.0125
* Form inputs: days since last match A 25, B 690; matches on record A 630, B 71; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.011, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Francisco Cerundolo vs Tallon Griekspoor -- ATP Brussels SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 17:00Z
* Current expected start: 2026-10-24 14:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 13:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:134868:202103:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francisco Cerundolo (`KXATPMATCH-26OCT24CERGRI-CER`) | 0.61 / 0.63 (31398) | 62.0% | 58.7% | 64.7% | 61.5% [58.7%-62.9%] | -- | 62.7% | 62.7% | MARKETS_AGREE | WATCH | -3.3 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Tallon Griekspoor (`KXATPMATCH-26OCT24CERGRI-GRI`) | 0.37 / 0.38 (75) | 37.5% | 41.3% | 35.3% | 38.5% [37.1%-41.3%] | -- | 37.5% | 37.5% | MARKETS_AGREE | PASS | +3.8 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5642.0, B 4445.0; serve-point win A 67.1%, B 34.7%; Elo A 1873.6, B 1873.8; model uncertainty 0.021
* Form inputs: days since last match A 14, B 2; matches on record A 553, B 679; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.019, surface_dev_loose -0.005, surface_dev_tight -0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT24CERGRI-30` Over 29.5 games: 0.20/0.27 mid 23.5%, model 34.4% (projection_v2.0 (prediction ledger)) -- gap +10.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24CERGRI-25` Over 24.5 games: 0.44/0.46 mid 45.0%, model 55.0% (projection_v2.0 (prediction ledger)) -- gap +10.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24CERGRI-20` Over 19.5 games: 0.74/0.77 mid 75.5%, model 84.1% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24CERGRI-CER5` Will Francisco Cerundolo win at least 4.5 more games than Tallon Griekspoor?: 0.23/0.28 mid 25.5%, model 18.1% (projection_v2.0 (prediction ledger)) -- gap -7.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24CERGRI-CER20` Will Francisco Cerundolo win the Francisco Cerundolo vs Tallon Griekspoor match by a set score of 2-0?: 0.36/0.39 mid 37.5%, model 31.2% (projection_v2.0 (prediction ledger)) -- gap -6.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24CERGRI-CER2` Will Francisco Cerundolo win at least 1.5 more games than Tallon Griekspoor?: 0.55/0.57 mid 56.0%, model 50.7% (projection_v2.0 (prediction ledger)) -- gap -5.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24CERGRI-CER21` Will Francisco Cerundolo win the Francisco Cerundolo vs Tallon Griekspoor match by a set score of 2-1?: 0.21/0.25 mid 23.0%, model 27.5% (projection_v2.0 (prediction ledger)) -- gap +4.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24CERGRI-GRI21` Will Tallon Griekspoor win the Francisco Cerundolo vs Tallon Griekspoor match by a set score of 2-1?: 0.16/0.19 mid 17.5%, model 21.8% (projection_v2.0 (prediction ledger)) -- gap +4.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24CERGRI-1-CER` Will Francisco Cerundolo win set 1 in the Francisco Cerundolo vs Tallon Griekspoor match: 0.57/0.61 mid 59.0%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap -3.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24CERGRI-1-GRI` Will Tallon Griekspoor win set 1 in the Francisco Cerundolo vs Tallon Griekspoor match: 0.39/0.43 mid 41.0%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap +3.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24CERGRI-2-CER` Will Francisco Cerundolo win set 2 in the Francisco Cerundolo vs Tallon Griekspoor match: 0.56/0.61 mid 58.5%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap -2.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24CERGRI-2-GRI` Will Tallon Griekspoor win set 2 in the Francisco Cerundolo vs Tallon Griekspoor match: 0.39/0.44 mid 41.5%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap +2.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24CERGRI-GRI20` Will Tallon Griekspoor win the Francisco Cerundolo vs Tallon Griekspoor match by a set score of 2-0?: 0.19/0.24 mid 21.5%, model 19.5% (projection_v2.0 (prediction ledger)) -- gap -2.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24CERGRI-GRI2` Will Tallon Griekspoor win at least 1.5 more games than Francisco Cerundolo?: 0.29/0.42 mid 35.5%, model 33.6% (projection_v2.0 (prediction ledger)) -- gap -1.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Flavio Cobolli vs Lorenzo Musetti -- ATP Lyon SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 16:10Z
* Current expected start: 2026-10-24 14:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 13:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-130_MIN

ATP (TOUR_500_250) · surface ? · scheduled 2026-10-24T16:10:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT24COBMUS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Flavio Cobolli (`KXATPMATCH-26OCT24COBMUS-COB`) | 0.50 / 0.51 (1128) | 50.5% | -- | -- | -- [-----] | -- | 46.0% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lorenzo Musetti (`KXATPMATCH-26OCT24COBMUS-MUS`) | 0.53 / 0.54 (113) | 53.5% | -- | -- | -- [-----] | -- | 53.8% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Corentin Moutet vs Tomas Machac -- ATP Vienna Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 17:00Z
* Current expected start: 2026-10-24 14:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 13:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144895:207830:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tomas Machac (`KXATPMATCH-26OCT24MOUMAC-MAC`) | 0.55 / 0.58 (47) | 56.5% | 56.1% | 45.4% | 50.0% [48.0%-55.1%] | -- | -- | -- | -- | PASS | -0.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Corentin Moutet (`KXATPMATCH-26OCT24MOUMAC-MOU`) | 0.39 / 0.44 (200) | 41.5% | 43.9% | 54.6% | 50.0% [44.9%-52.0%] | -- | -- | -- | -- | PASS | +2.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4376.0, B 3720.0; serve-point win A 60.5%, B 38.3%; Elo A 1823.8, B 1918.6; model uncertainty 0.0357
* Form inputs: days since last match A 2, B 1; matches on record A 586, B 445; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight -0.015
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT24MOUMAC-MAC21` Will Tomas Machac win the Corentin Moutet vs Tomas Machac match by a set score of 2-1?: 0.01/0.30 mid 15.5%, model 26.9% (projection_v2.0 (prediction ledger)) -- gap +11.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MOUMAC-MOU21` Will Corentin Moutet win the Corentin Moutet vs Tomas Machac match by a set score of 2-1?: 0.01/0.25 mid 13.0%, model 22.8% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MOUMAC-MAC20` Will Tomas Machac win the Corentin Moutet vs Tomas Machac match by a set score of 2-0?: 0.01/0.40 mid 20.5%, model 29.2% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MOUMAC-MOU20` Will Corentin Moutet win the Corentin Moutet vs Tomas Machac match by a set score of 2-0?: 0.01/0.29 mid 15.0%, model 21.1% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MOUMAC-1-MAC` Will Tomas Machac win set 1 in the Corentin Moutet vs Tomas Machac match: 0.02/0.97 mid 49.5%, model 54.1% (projection_v2.0 (prediction ledger)) -- gap +4.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MOUMAC-2-MAC` Will Tomas Machac win set 2 in the Corentin Moutet vs Tomas Machac match: 0.02/0.98 mid 50.0%, model 54.1% (projection_v2.0 (prediction ledger)) -- gap +4.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MOUMAC-2-MOU` Will Corentin Moutet win set 2 in the Corentin Moutet vs Tomas Machac match: 0.02/0.98 mid 50.0%, model 45.9% (projection_v2.0 (prediction ledger)) -- gap -4.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MOUMAC-1-MOU` Will Corentin Moutet win set 1 in the Corentin Moutet vs Tomas Machac match: 0.02/0.97 mid 49.5%, model 45.9% (projection_v2.0 (prediction ledger)) -- gap -3.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Cezar Cretu vs Fons Van Sambeek -- M15 Heraklion SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-24T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206470:209913:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cezar Cretu (`KXITFMATCH-26OCT24CREVAN-CRE`) | 0.83 / 0.87 (69) | 85.0% | 94.4% | 85.1% | 91.4% [90.3%-93.1%] | -- | -- | -- | -- | PASS | +9.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Fons Van Sambeek (`KXITFMATCH-26OCT24CREVAN-VAN`) | 0.12 / 0.15 (101) | 13.5% | 5.6% | 14.9% | 8.6% [6.9%-9.7%] | -- | -- | -- | -- | PASS | -7.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1940.0, B 244.0; serve-point win A 65.0%, B 47.3%; Elo A 1593.6, B 1165.2; model uncertainty 0.0141
* Form inputs: days since last match A 11, B 711; matches on record A 338, B 36; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.010, surface_dev_loose +0.003, surface_dev_tight -0.002
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gretskiy / Kunitsyn vs Anavatan / Mert Ozdemir -- M15 Sharm ElSheikh F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-24T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24GREKUNANAMER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anavatan / Mert Ozdemir (`KXITFDOUBLES-26OCT24GREKUNANAMER-ANAMER`) | 0.08 / 0.78 (113) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gretskiy / Kunitsyn (`KXITFDOUBLES-26OCT24GREKUNANAMER-GREKUN`) | 0.08 / 0.38 (40) | 23.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Matteo Gribaldo vs Adrian Oetzbach -- M25 Santa Margherita di Pula F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24GRIOET:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Gribaldo (`KXITFMATCH-26OCT24GRIOET-GRI`) | 0.39 / 0.43 (100) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Adrian Oetzbach (`KXITFMATCH-26OCT24GRIOET-OET`) | 0.58 / 0.59 (107) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

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
| Amit Vales (`KXITFMATCH-26OCT24VALXIL-VAL`) | 0.45 / 0.46 (213) | 45.5% | -- | 59.9% | 48.9% [42.8%-53.7%] | -- | -- | -- | -- | PASS | +3.5 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ioannis Xilas (`KXITFMATCH-26OCT24VALXIL-XIL`) | 0.51 / 0.55 (56) | 53.0% | -- | 40.2% | 51.0% [46.3%-57.2%] | -- | -- | -- | -- | PASS | -1.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 397.0, B 992.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0545
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.036, surface_pool_high +0.031, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alessandra Mazzola vs Jennifer Ruggeri -- W35 Santa Margherita di Pula SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-24T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220306:221411:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alessandra Mazzola (`KXITFWMATCH-26OCT24MAZRUG-MAZ`) | 0.33 / 0.35 (38) | 34.0% | -- | 38.4% | 37.9% [37.9%-39.9%] | -- | -- | -- | -- | PASS | +3.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jennifer Ruggeri (`KXITFWMATCH-26OCT24MAZRUG-RUG`) | 0.61 / 0.66 (29) | 63.5% | -- | 61.6% | 62.2% [60.1%-62.2%] | -- | -- | -- | -- | PASS | -1.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2354.0, B 3454.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0104
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
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
| Alhussein Abdel Aziz / Samir (`KXITFWDOUBLES-26OCT24POPSHIALHSAM-ALHSAM`) | 0.08 / 0.58 (59) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Popovic / Shinikova (`KXITFWDOUBLES-26OCT24POPSHIALHSAM-POPSHI`) | 0.08 / 0.60 (62) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Nina Radovanovic vs Ane Mintegi Del Olmo -- W35 Santa Margherita di Pula SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-24T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221213:222602:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ane Mintegi Del Olmo (`KXITFWMATCH-26OCT24RADMIN-MIN`) | 0.79 / 0.83 (401) | 81.0% | -- | 76.6% | 83.3% [79.7%-85.8%] | 81.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.3 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nina Radovanovic (`KXITFWMATCH-26OCT24RADMIN-RAD`) | 0.15 / 0.19 (24) | 17.0% | -- | 23.4% | 16.7% [14.2%-20.3%] | 18.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.3 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 976.0, B 2133.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0305
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.036, surface_pool_high -0.025, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Svyatoslav Gulin vs Elmer Moller -- ATP Challenger Lisbon SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 14:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-24T14:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24GULMOL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Svyatoslav Gulin (`KXATPCHALLENGERMATCH-26OCT24GULMOL-GUL`) | 0.31 / 0.33 (3503) | 32.0% | -- | -- | -- [-----] | 33.6% | 32.5% | 32.5% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Elmer Moller (`KXATPCHALLENGERMATCH-26OCT24GULMOL-MOL`) | 0.67 / 0.69 (3620) | 68.0% | -- | -- | -- [-----] | 66.4% | 71.4% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Charo Esquiva Banuls vs Neus Torner Sensano -- W15 Villena F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 14:45Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T14:45:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264962:269717:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charo Esquiva Banuls (`KXITFWMATCH-26OCT24ESQTOR-ESQ`) | 0.76 / 0.80 (20) | 78.0% | -- | 6.9% | 25.9% [17.7%-41.5%] | -- | -- | -- | -- | PASS | -52.1 pp | EXTREME (DATA_WARNING) | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Neus Torner Sensano (`KXITFWMATCH-26OCT24ESQTOR-TOR`) | 0.19 / 0.22 (26) | 20.5% | -- | 93.2% | 74.1% [58.5%-82.3%] | -- | -- | -- | -- | WATCH | +53.6 pp | EXTREME (DATA_WARNING) | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1005.0, B 1512.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.119
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT24ESQTOR-TOR  (YES = Neus Torner Sensano)
Model: 74%
Kalshi: 20%
Gap: +54 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.018, surface_dev_loose -0.038, surface_dev_tight +0.036
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

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
| Robin Bertrand (`KXITFMATCH-26OCT24BERGAV-BER`) | 0.68 / 0.70 (10) | 69.0% | 65.0% | 49.5% | 61.1% [54.1%-70.8%] | -- | -- | -- | -- | PASS | -4.0 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Liam Gavrielides (`KXITFMATCH-26OCT24BERGAV-GAV`) | 0.28 / 0.31 (50) | 29.5% | 35.0% | 50.5% | 38.9% [29.2%-45.9%] | -- | -- | -- | -- | PASS | +5.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2130.0, B 402.0; serve-point win A 62.6%, B 40.4%; Elo A 1543.6, B 1443.8; model uncertainty 0.0834
* Form inputs: days since last match A 158, B 263; matches on record A 313, B 127; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.058, surface_pool_high -0.070, surface_dev_loose -0.020, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
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
| Eliakim Coulibaly (`KXITFMATCH-26OCT24COUFAU-COU`) | 0.53 / 0.55 (114) | 54.0% | 50.4% | 48.5% | 54.6% [52.6%-60.1%] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Thomas Faurel (`KXITFMATCH-26OCT24COUFAU-FAU`) | 0.39 / 0.47 (75) | 43.0% | 49.6% | 51.5% | 45.4% [39.9%-47.4%] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1477.0, B 1707.0; serve-point win A 61.0%, B 39.1%; Elo A 1572.6, B 1495.9; model uncertainty 0.0376
* Form inputs: days since last match A 697, B 25; matches on record A 248, B 54; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ianin / Sharma vs John Lock / Nortey -- M25 Luanda F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-24T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24IANSHAJOHNOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ianin / Sharma (`KXITFDOUBLES-26OCT24IANSHAJOHNOR-IANSHA`) | 0.08 / 0.57 (58) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| John Lock / Nortey (`KXITFDOUBLES-26OCT24IANSHAJOHNOR-JOHNOR`) | 0.08 / 0.62 (65) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

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
| Ferdinand Livet Novkirichka (`KXITFMATCH-26OCT24LIVRAH-LIV`) | 0.21 / 0.25 (27) | 23.0% | 30.0% | 50.0% | 47.0% [47.0%-47.0%] | -- | -- | -- | -- | PASS | +7.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Kasra Rahmani (`KXITFMATCH-26OCT24LIVRAH-RAH`) | 0.72 / 0.78 (96) | 75.0% | 70.0% | 50.0% | 53.0% [53.0%-53.0%] | -- | -- | -- | -- | PASS | -5.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 59.9%, B 35.9%; Elo A 1253.1, B 1273.4; model uncertainty 0.0
* Form inputs: days since last match A 879, B 704; matches on record A 1, B 9; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Tiphanie Lemaitre (`KXITFWMATCH-26OCT24LEMMIL-LEM`) | 0.49 / 0.51 (320) | 50.0% | -- | 40.5% | 55.3% [47.9%-62.6%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elena Milovanovic (`KXITFWMATCH-26OCT24LEMMIL-MIL`) | 0.47 / 0.51 (110) | 49.0% | -- | 59.5% | 44.7% [37.4%-52.1%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 2475.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0736
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
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
| Kayo Nishimura (`KXITFWMATCH-26OCT24NISVOG-NIS`) | 0.50 / 0.53 (2234) | 51.5% | -- | 25.1% | 34.8% [30.5%-46.8%] | -- | -- | -- | -- | PASS | -16.6 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marie Vogt (`KXITFWMATCH-26OCT24NISVOG-VOG`) | 0.44 / 0.47 (63) | 45.5% | -- | 74.9% | 65.1% [53.2%-69.5%] | -- | -- | -- | -- | WATCH | +19.6 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2288.0, B 2280.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0815
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT24NISVOG-VOG  (YES = Marie Vogt)
Model: 65%
Kalshi: 46%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.020, surface_dev_tight +0.025
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
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
| Daria Lopatetska (`KXITFWMATCH-26OCT24ZAJLOP-LOP`) | 0.60 / 0.63 (33) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Katerina Zajickova (`KXITFWMATCH-26OCT24ZAJLOP-ZAJ`) | 0.37 / 0.38 (209) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Dominik Recek / Daniel Siniakov (`KXATPCHALLENGERDOUBLES-26OCT24RIBVOLRECSIN-RECSIN`) | 0.05 / 0.95 (223) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Michele Ribecai / Gabriele Volpi (`KXATPCHALLENGERDOUBLES-26OCT24RIBVOLRECSIN-RIBVOL`) | 0.05 / 0.95 (223) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Paul Jubb (`KXITFMATCH-26OCT24JUBTAR-JUB`) | 0.20 / 0.22 (132) | 21.0% | 30.1% | 33.7% | 36.0% [33.2%-38.0%] | -- | -- | -- | -- | WATCH | +9.1 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oliver Tarvet (`KXITFMATCH-26OCT24JUBTAR-TAR`) | 0.75 / 0.79 (34) | 77.0% | 69.9% | 66.3% | 64.0% [62.0%-66.8%] | -- | -- | -- | -- | PASS | -7.1 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2131.0, B 1422.0; serve-point win A 59.5%, B 36.4%; Elo A 1604.2, B 1687.5; model uncertainty 0.0238
* Form inputs: days since last match A 60, B 18; matches on record A 326, B 69; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Thiago Agustin Tirante vs Adrian Mannarino -- ATP Vienna Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 19:00Z
* Current expected start: 2026-10-24 16:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 15:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T19:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105173:202058:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Mannarino (`KXATPMATCH-26OCT24TIRMAN-MAN`) | 0.42 / 0.46 (161) | 44.0% | 41.3% | 35.7% | 40.8% [38.9%-43.7%] | 47.8% | 48.7% | 47.8% | ALL_THREE_DISAGREE | PASS | -2.7 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_OUTLIER | VERIFIED |
| Thiago Agustin Tirante (`KXATPMATCH-26OCT24TIRMAN-TIR`) | 0.54 / 0.58 (126) | 56.0% | 58.7% | 64.3% | 59.2% [56.3%-61.1%] | 52.2% | 50.3% | 52.2% | ALL_THREE_DISAGREE | SHADOW_BET | +2.7 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_OUTLIER | VERIFIED |

* Serve evidence (points): A 4804.0, B 4318.0; serve-point win A 67.0%, B 34.8%; Elo A 1735.0, B 1776.7; model uncertainty 0.0238
* Form inputs: days since last match A 4, B 0; matches on record A 450, B 1276; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.019, surface_dev_loose +0.009, surface_dev_tight -0.009
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT24TIRMAN-1-MAN` Will Adrian Mannarino win set 1 in the Thiago Agustin Tirante vs Adrian Mannarino match: 0.02/0.59 mid 30.5%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap +13.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24TIRMAN-TIR20` Will Thiago Agustin Tirante win the Thiago Agustin Tirante vs Adrian Mannarino match by a set score of 2-0?: 0.02/0.34 mid 18.0%, model 31.2% (projection_v2.0 (prediction ledger)) -- gap +13.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24TIRMAN-1-TIR` Will Thiago Agustin Tirante win set 1 in the Thiago Agustin Tirante vs Adrian Mannarino match: 0.41/0.97 mid 69.0%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap -13.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24TIRMAN-TIR21` Will Thiago Agustin Tirante win the Thiago Agustin Tirante vs Adrian Mannarino match by a set score of 2-1?: 0.01/0.28 mid 14.5%, model 27.5% (projection_v2.0 (prediction ledger)) -- gap +13.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24TIRMAN-MAN21` Will Adrian Mannarino win the Thiago Agustin Tirante vs Adrian Mannarino match by a set score of 2-1?: 0.01/0.27 mid 14.0%, model 21.8% (projection_v2.0 (prediction ledger)) -- gap +7.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24TIRMAN-2-MAN` Will Adrian Mannarino win set 2 in the Thiago Agustin Tirante vs Adrian Mannarino match: 0.02/0.98 mid 50.0%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap -5.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24TIRMAN-2-TIR` Will Thiago Agustin Tirante win set 2 in the Thiago Agustin Tirante vs Adrian Mannarino match: 0.02/0.98 mid 50.0%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24TIRMAN-MAN20` Will Adrian Mannarino win the Thiago Agustin Tirante vs Adrian Mannarino match by a set score of 2-0?: 0.01/0.33 mid 17.0%, model 19.5% (projection_v2.0 (prediction ledger)) -- gap +2.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
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
| Bertrand / van Wyk (`KXITFDOUBLES-26OCT24ISIMASBERVAN-BERVAN`) | 0.22 / 0.72 (5) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Isik Kosaner / Massellani (`KXITFDOUBLES-26OCT24ISIMASBERVAN-ISIMAS`) | 0.08 / 0.45 (45) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Daniel Domingos (`KXITFMATCH-26OCT24LOGDOM-DOM`) | 0.10 / 0.12 (193) | 11.0% | 18.6% | 47.9% | 31.1% [31.0%-31.2%] | -- | -- | -- | -- | PASS | +7.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jack Loge (`KXITFMATCH-26OCT24LOGDOM-LOG`) | 0.88 / 0.90 (79) | 89.0% | 81.4% | 52.1% | 68.9% [68.8%-69.0%] | -- | -- | -- | -- | PASS | -7.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 467.0, B 0.0; serve-point win A 63.0%, B 43.9%; Elo A 1378.5, B 1237.8; model uncertainty 0.0013
* Form inputs: days since last match A 81, B 697; matches on record A 89, B 5; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
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
| De Zeeuw / Louise Van den Broek (`KXITFWDOUBLES-26OCT24DEZLOULIUMOC-DEZLOU`) | 0.05 / 0.95 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Liu / Moccia (`KXITFWDOUBLES-26OCT24DEZLOULIUMOC-LIUMOC`) | 0.05 / 0.95 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Kumru / Paszun (`KXITFWDOUBLES-26OCT24KUMPASVOGYAS-KUMPAS`) | 0.11 / 0.63 (67) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vogt / Yashina (`KXITFWDOUBLES-26OCT24KUMPASVOGYAS-VOGYAS`) | 0.08 / 0.57 (58) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Arthur Fils vs Jan-Lennard Struff -- ATP Brussels SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 19:30Z
* Current expected start: 2026-10-24 16:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 00:05Z
* Recommended handicap-by time: 2026-10-24 15:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T19:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105526:209950:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arthur Fils (`KXATPMATCH-26OCT24FILSTR-FIL`) | 0.81 / 0.82 (6004) | 81.5% | 85.3% | 81.7% | 81.7% [78.5%-83.0%] | 79.8% | 81.0% | 79.8% | MODEL_LONE_OUTLIER | PASS | +3.8 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Jan-Lennard Struff (`KXATPMATCH-26OCT24FILSTR-STR`) | 0.18 / 0.19 (1283) | 18.5% | 14.7% | 18.3% | 18.3% [17.0%-21.5%] | 20.2% | 18.4% | 19.3% | MODEL_LONE_OUTLIER | PASS | -3.8 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4268.0, B 4793.0; serve-point win A 71.3%, B 37.4%; Elo A 2036.2, B 1782.6; model uncertainty 0.0224
* Form inputs: days since last match A 11, B 2; matches on record A 331, B 1056; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.006, surface_dev_loose +0.012, surface_dev_tight -0.019
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT24FILSTR-FIL20` Will Arthur Fils win the Arthur Fils vs Jan-Lennard Struff match by a set score of 2-0?: 0.02/0.61 mid 31.5%, model 57.5% (projection_v2.0 (prediction ledger)) -- gap +26.0 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24FILSTR-2-FIL` Will Arthur Fils win set 2 in the Arthur Fils vs Jan-Lennard Struff match: 0.02/0.98 mid 50.0%, model 75.9% (projection_v2.0 (prediction ledger)) -- gap +25.9 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24FILSTR-2-STR` Will Jan-Lennard Struff win set 2 in the Arthur Fils vs Jan-Lennard Struff match: 0.02/0.98 mid 50.0%, model 24.1% (projection_v2.0 (prediction ledger)) -- gap -25.9 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24FILSTR-FIL21` Will Arthur Fils win the Arthur Fils vs Jan-Lennard Struff match by a set score of 2-1?: 0.17/0.27 mid 22.0%, model 27.8% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24FILSTR-STR20` Will Jan-Lennard Struff win the Arthur Fils vs Jan-Lennard Struff match by a set score of 2-0?: 0.05/0.10 mid 7.5%, model 5.8% (projection_v2.0 (prediction ledger)) -- gap -1.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24FILSTR-1-FIL` Will Arthur Fils win set 1 in the Arthur Fils vs Jan-Lennard Struff match: 0.72/0.77 mid 74.5%, model 75.9% (projection_v2.0 (prediction ledger)) -- gap +1.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24FILSTR-1-STR` Will Jan-Lennard Struff win set 1 in the Arthur Fils vs Jan-Lennard Struff match: 0.24/0.27 mid 25.5%, model 24.1% (projection_v2.0 (prediction ledger)) -- gap -1.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24FILSTR-STR21` Will Jan-Lennard Struff win the Arthur Fils vs Jan-Lennard Struff match by a set score of 2-1?: 0.05/0.11 mid 8.0%, model 8.8% (projection_v2.0 (prediction ledger)) -- gap +0.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Jodie Anna Burrage (`KXITFWMATCH-26OCT24BURKLU-BUR`) | 0.46 / 0.50 (77) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hannah Klugman (`KXITFWMATCH-26OCT24BURKLU-KLU`) | 0.49 / 0.54 (96) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
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
| Laura Mair (`KXITFWMATCH-26OCT24MAITEI-MAI`) | 0.39 / 0.40 (1) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aran Teixido Garcia (`KXITFWMATCH-26OCT24MAITEI-TEI`) | 0.56 / 0.57 (58) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Maximilian Marterer (`KXITFMATCH-26OCT24NAGMAR-MAR`) | 0.68 / 0.72 (33) | 70.0% | 95.3% | 65.6% | 95.8% [95.3%-96.1%] | -- | -- | -- | -- | PASS | +25.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Arthur Nagel (`KXITFMATCH-26OCT24NAGMAR-NAG`) | 0.30 / 0.31 (137) | 30.5% | 4.7% | 34.4% | 4.2% [3.9%-4.7%] | -- | -- | -- | -- | PASS | -25.9 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 69.0, B 3762.0; serve-point win A 57.0%, B 29.5%; Elo A 1268.9, B 1833.6; model uncertainty 0.0041
* Form inputs: days since last match A 39, B 515; matches on record A 44, B 672; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT24NAGMAR-MAR  (YES = Maximilian Marterer)
Model: 95%
Kalshi: 70%
Gap: +25 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
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
| Weronika Falkowska (`KXITFWMATCH-26OCT24FALURG-FAL`) | 0.48 / 0.52 (70) | 50.0% | -- | 58.4% | 54.2% [47.3%-57.4%] | -- | -- | -- | -- | PASS | +4.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Federica Urgesi (`KXITFWMATCH-26OCT24FALURG-URG`) | 0.44 / 0.52 (95) | 48.0% | -- | 41.6% | 45.8% [42.6%-52.7%] | -- | -- | -- | -- | PASS | -2.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2031.0, B 2635.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0501
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.011, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Elsa Jacquemot (`KXITFWMATCH-26OCT24LAMJAC-JAC`) | 0.46 / 0.49 (15) | 47.5% | -- | 48.9% | 46.8% [44.1%-47.9%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Suzan Lamens (`KXITFWMATCH-26OCT24LAMJAC-LAM`) | 0.49 / 0.52 (18) | 50.5% | -- | 51.1% | 53.2% [52.1%-55.9%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

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
| Adrien Gobat (`KXITFMATCH-26OCT24HENGOB-GOB`) | 0.27 / 0.34 (29) | 30.5% | 32.6% | 40.4% | 36.0% [35.1%-37.0%] | -- | -- | -- | -- | PASS | +2.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Philip Henning (`KXITFMATCH-26OCT24HENGOB-HEN`) | 0.64 / 0.69 (90) | 66.5% | 67.4% | 59.6% | 64.0% [63.0%-64.9%] | -- | -- | -- | -- | PASS | +0.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1821.0, B 307.0; serve-point win A 63.3%, B 40.2%; Elo A 1522.4, B 1417.5; model uncertainty 0.0092
* Form inputs: days since last match A 11, B 592; matches on record A 143, B 109; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Mariam Bolkvadze (`KXITFWMATCH-26OCT24BOLTAN-BOL`) | 0.38 / 0.49 (57) | 43.5% | -- | 27.8% | 38.4% [34.4%-45.2%] | -- | -- | -- | -- | PASS | -5.1 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Harmony Tan (`KXITFWMATCH-26OCT24BOLTAN-TAN`) | 0.45 / 0.56 (62) | 50.5% | -- | 72.2% | 61.6% [54.8%-65.6%] | -- | -- | -- | -- | PASS | +11.1 pp | REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1814.0, B 3731.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.054
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.021, surface_dev_loose -0.000, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

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
| Britton / Klugman (`KXITFWDOUBLES-26OCT24CHRSILBRIKLU-BRIKLU`) | 0.30 / 0.70 (0) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Christie / Silva (`KXITFWDOUBLES-26OCT24CHRSILBRIKLU-CHRSIL`) | 0.30 / 0.61 (2) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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

ITF (ITF) · surface ? · scheduled 2026-10-24T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24SANGAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barbara Gatica (`KXITFWMATCH-26OCT24SANGAT-GAT`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ana Sofia Sanchez (`KXITFWMATCH-26OCT24SANGAT-SAN`) | 0.03 / 0.97 (206) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
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

ITF (ITF) · surface ? · scheduled 2026-10-24T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24ZAVLEO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Manon Leonard (`KXITFWMATCH-26OCT24ZAVLEO-LEO`) | 0.43 / 0.60 (28) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Katarina Zavatska (`KXITFWMATCH-26OCT24ZAVLEO-ZAV`) | 0.34 / 0.51 (62) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
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

ITF (ITF) · surface ? · scheduled 2026-10-24T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24URRGON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Justina Maria Gonzalez Daniele (`KXITFWMATCH-26OCT24URRGON-GON`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maria Florencia Urrutia (`KXITFWMATCH-26OCT24URRGON-URR`) | 0.03 / 0.97 (206) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oliver Ojakaar vs Rodrigo Fernandes -- M15 Ithaca SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24OJAFER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rodrigo Fernandes (`KXITFMATCH-26OCT24OJAFER-FER`) | 0.10 / 0.45 (2) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Oliver Ojakaar (`KXITFMATCH-26OCT24OJAFER-OJA`) | 0.56 / 0.76 (6) | 66.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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

ITF (ITF) · surface ? · scheduled 2026-10-24T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24ANTYME:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jack Anthrop (`KXITFMATCH-26OCT24ANTYME-ANT`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rafael Ymer (`KXITFMATCH-26OCT24ANTYME-YME`) | 0.03 / 0.97 (280) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Reese Brantmeier vs Hiromi Abe -- W75 Saguenay SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24BRAABE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hiromi Abe (`KXITFWMATCH-26OCT24BRAABE-ABE`) | 0.05 / 0.95 (6) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Reese Brantmeier (`KXITFWMATCH-26OCT24BRAABE-BRA`) | 0.04 / 0.94 (6) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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

ITF (ITF) · surface ? · scheduled 2026-10-24T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24BREMCD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Madison Brengle (`KXITFWMATCH-26OCT24BREMCD-BRE`) | 0.50 / 0.94 (438) | 72.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ella McDonald (`KXITFWMATCH-26OCT24BREMCD-MCD`) | 0.04 / 0.49 (6) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
