# ASSISTED SLATE -- 2026-11-13T23:45Z (`SL-20261113T234538Z-274dce2d`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

95 open matches not seen started, 227 markets. Skipped: {}. Sources: shadow board 2026-11-13T20:39:15.921258+00:00, Model 4 2026-11-13T20:39:36.653835+00:00, Gen-1 ledger 2026-11-13T20:39:12.831621+00:00, external 2026-11-13T23:22:02.749082+00:00, capture 20261113T232030Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-11-14 12:00Z**
* Recommended RUN TENNIS time: **2026-11-14 11:15Z**
* Final price/status check time: **2026-11-14 11:50Z**
* Number of matches in window: 1 (Taylor Fritz vs Thiago Agustin Tirante)

Slate built 2026-11-13T23:45Z. Refresh due by: 2026-11-14 11:15Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 9, "HIGH_REVIEW": 23, "NORMAL": 78, "REVIEW": 20, "UNPRICED": 97}; match winners: {"EXTREME": 9, "HIGH_REVIEW": 21, "NORMAL": 48, "REVIEW": 18, "UNPRICED": 94}; quote freshness at build: {"FRESH": 130}.

## Genaro Alberto Olivieri vs Joao Lucas Reis Da Silva -- ATP Challenger Lima QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-13T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144821:206307:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Genaro Alberto Olivieri (`KXATPCHALLENGERMATCH-26NOV13OLIREI-OLI`) | 0.37 / 0.38 (7918) | 37.5% | 33.6% | 29.7% | 31.5% [30.1%-33.9%] | -- | 36.9% | 36.9% | MARKETS_AGREE | PASS | -3.9 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Joao Lucas Reis Da Silva (`KXATPCHALLENGERMATCH-26NOV13OLIREI-REI`) | 0.62 / 0.63 (7520) | 62.5% | 66.4% | 70.3% | 68.5% [66.1%-69.9%] | -- | 62.9% | 62.9% | MARKETS_AGREE | SHADOW_BET | +3.9 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5176.0, B 5010.0; serve-point win A 57.3%, B 39.4%; Elo A 1588.2, B 1671.7; model uncertainty 0.0188
* Form inputs: days since last match A 11, B 11; matches on record A 613, B 485; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.009, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED

## Daniel Jade vs Tyler Zink -- M25 Vale do Lobo QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208342:212711:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Jade (`KXITFMATCH-26NOV13JADZIN-JAD`) | 0.89 / 0.90 (4655) | 89.5% | 9.9% | 5.3% | 10.8% [8.5%-12.5%] | -- | -- | -- | -- | PASS | -79.6 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tyler Zink (`KXITFMATCH-26NOV13JADZIN-ZIN`) | 0.10 / 0.11 (5606) | 10.5% | 90.1% | 94.7% | 89.2% [87.5%-91.5%] | -- | -- | -- | -- | PASS | +79.6 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 691.0, B 4139.0; serve-point win A 57.4%, B 32.4%; Elo A 1212.1, B 1524.2; model uncertainty 0.0202
* Form inputs: days since last match A 32, B 181; matches on record A 23, B 197; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV13JADZIN-ZIN  (YES = Tyler Zink)
Model: 90%
Kalshi: 10%
Gap: +80 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.015, surface_dev_loose -0.009, surface_dev_tight +0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carles Cordoba vs Matias Ponce de leon gomila -- M15 Las Palmas de Gran Canaria QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 20:02Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-13T20:02:20Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210038:213059:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carles Cordoba (`KXITFMATCH-26NOV13CORPON-COR`) | 0.34 / 0.37 (3) | 35.5% | 48.6% | 20.4% | 45.3% [39.1%-53.1%] | -- | -- | -- | -- | PASS | +13.1 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matias Ponce de leon gomila (`KXITFMATCH-26NOV13CORPON-PON`) | 0.63 / 0.66 (5) | 64.5% | 51.4% | 79.6% | 54.7% [46.9%-60.9%] | -- | -- | -- | -- | PASS | -13.1 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1490.0, B 397.0; serve-point win A 57.5%, B 42.2%; Elo A 1289.8, B 1265.0; model uncertainty 0.0701
* Form inputs: days since last match A 207, B 417; matches on record A 42, B 13; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.010, surface_dev_loose -0.005, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Branchetti / Mouilleron Salvo vs Bruna / Dellien -- M15 Roldan SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13BRAMOUBRUDEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Branchetti / Mouilleron Salvo (`KXITFDOUBLES-26NOV13BRAMOUBRUDEL-BRAMOU`) | 0.28 / 0.36 (227) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bruna / Dellien (`KXITFDOUBLES-26NOV13BRAMOUBRUDEL-BRUDEL`) | 0.60 / 0.67 (6) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Estevez / Zeitune vs Basel / Martinez -- M15 Roldan SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13ESTZEIBASMAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Basel / Martinez (`KXITFDOUBLES-26NOV13ESTZEIBASMAR-BASMAR`) | 0.15 / 0.80 (100) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Estevez / Zeitune (`KXITFDOUBLES-26NOV13ESTZEIBASMAR-ESTZEI`) | 0.01 / 0.46 (28) | 23.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Ivan Ivanov vs Pavel Lagutin -- M25 Vale do Lobo QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 21:45Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T21:45:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:129814:213760:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ivan Ivanov (`KXITFMATCH-26NOV13IVALAG-IVA`) | 0.25 / 0.26 (902) | 25.5% | 49.2% | 26.2% | 40.6% [33.5%-48.9%] | -- | -- | -- | -- | WATCH | +23.7 pp | HIGH_REVIEW | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pavel Lagutin (`KXITFMATCH-26NOV13IVALAG-LAG`) | 0.74 / 0.75 (2252) | 74.5% | 50.8% | 73.8% | 59.4% [51.0%-66.5%] | -- | -- | -- | -- | PASS | -23.7 pp | HIGH_REVIEW | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2387.0, B 1727.0; serve-point win A 55.9%, B 43.9%; Elo A 1453.2, B 1398.8; model uncertainty 0.0771
* Form inputs: days since last match A 25, B 32; matches on record A 75, B 43; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV13IVALAG-IVA  (YES = Ivan Ivanov)
Model: 49%
Kalshi: 26%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.015, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Johns / Rodenas vs Leote Prata / Morais -- M25 Vale do Lobo QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13JOHRODLEOMOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Johns / Rodenas (`KXITFDOUBLES-26NOV13JOHRODLEOMOR-JOHROD`) | 0.11 / 0.69 (31) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Leote Prata / Morais (`KXITFDOUBLES-26NOV13JOHRODLEOMOR-LEOMOR`) | 0.26 / 0.50 (8) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Gabriela Dabrowski / Luisa Stefani vs Su-Wei Hsieh / Jelena Ostapenko -- WTA Finals Women Doubles Group

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-11-14 01:20Z
* Current expected start: 2026-11-13 23:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-13 23:25Z
* Recommended handicap-by time: 2026-11-13 22:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

DOUBLES (TOUR_FINALS) · surface ? · scheduled 2026-11-14T01:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV13DABSTEHSIOST:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriela Dabrowski / Luisa Stefani (`KXWTADOUBLES-26NOV13DABSTEHSIOST-DABSTE`) | 0.60 / 0.61 (51) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Su-Wei Hsieh / Jelena Ostapenko (`KXWTADOUBLES-26NOV13DABSTEHSIOST-HSIOST`) | 0.39 / 0.40 (5985) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; STATUS_AMBIGUOUS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Nikolas Sanchez Izquierdo vs Miguel Tobon -- ATP Challenger Lima QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-14T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:101495:207663:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikolas Sanchez Izquierdo (`KXATPCHALLENGERMATCH-26NOV13SAITOB-SAI`) | 0.25 / 0.26 (38285) | 25.5% | 71.8% | 67.5% | 70.7% [69.3%-75.7%] | -- | -- | -- | -- | SHADOW_BET | +46.3 pp | EXTREME (DATA_WARNING) | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Miguel Tobon (`KXATPCHALLENGERMATCH-26NOV13SAITOB-TOB`) | 0.74 / 0.75 (123263) | 74.5% | 28.2% | 32.5% | 29.3% [24.3%-30.7%] | -- | -- | -- | -- | PASS | -46.3 pp | EXTREME (DATA_WARNING) | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5051.0, B 3281.0; serve-point win A 61.9%, B 42.5%; Elo A 1661.4, B 1454.2; model uncertainty 0.032
* Form inputs: days since last match A 11, B 110; matches on record A 583, B 423; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV13SAITOB-SAI  (YES = Nikolas Sanchez Izquierdo)
Model: 72%
Kalshi: 26%
Gap: +46 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.004, surface_dev_loose -0.009, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Hanyu Guo / Kristina Mladenovic vs Elise Mertens / Shuai Zhang -- WTA Finals Women Doubles Group

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-14 02:30Z
* Current expected start: 2026-11-14 00:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-13 23:25Z
* Recommended handicap-by time: 2026-11-13 23:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_FINALS) · surface ? · scheduled 2026-11-14T02:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV13GUOMLAMERZHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hanyu Guo / Kristina Mladenovic (`KXWTADOUBLES-26NOV13GUOMLAMERZHA-GUOMLA`) | 0.55 / 0.56 (48) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Elise Mertens / Shuai Zhang (`KXWTADOUBLES-26NOV13GUOMLAMERZHA-MERZHA`) | 0.43 / 0.45 (6123) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Stefan Kozlov vs Michael Zheng -- ATP Challenger Knoxville QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-14T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111578:210116:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefan Kozlov (`KXATPCHALLENGERMATCH-26NOV13KOZZHE-KOZ`) | 0.35 / 0.36 (77710) | 35.5% | 35.9% | 40.7% | 37.7% [35.8%-38.7%] | -- | -- | -- | -- | PASS | +0.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Michael Zheng (`KXATPCHALLENGERMATCH-26NOV13KOZZHE-ZHE`) | 0.64 / 0.65 (64964) | 64.5% | 64.1% | 59.3% | 62.3% [61.3%-64.2%] | -- | -- | -- | -- | PASS | -0.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3794.0, B 3352.0; serve-point win A 57.6%, B 39.6%; Elo A 1616.3, B 1755.6; model uncertainty 0.0148
* Form inputs: days since last match A 11, B 11; matches on record A 624, B 142; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Kayla Cross vs Jessica Hinojosa Gomez -- W50 Chihuahua SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 03:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-14T03:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213739:239436:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kayla Cross (`KXITFWMATCH-26NOV13CROHIN-CRO`) | 0.99 / -- (0) | -- | 82.8% | 67.1% | 70.0% [66.1%-76.9%] | -- | -- | -- | -- | PASS | -- | UNPRICED | FRESH | A / ADEQUATE | INSUFFICIENT_INPUTS | VERIFIED |
| Jessica Hinojosa Gomez (`KXITFWMATCH-26NOV13CROHIN-HIN`) | -- / 0.01 (172159) | -- | 17.2% | 32.9% | 30.0% [23.1%-33.9%] | -- | -- | -- | -- | WATCH | -- | UNPRICED | FRESH | A / ADEQUATE | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 2619.0, B 1620.0; serve-point win A 56.2%, B 50.9%; Elo A 1541.9, B 1369.3; model uncertainty 0.0539
* Form inputs: days since last match A 60, B 18; matches on record A 237, B 177; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.041, surface_pool_high -0.038, surface_dev_loose +0.009, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carlos Alvarez Valdes / Urrea vs De Alba / Sau Franco -- M15 Zamora SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-14T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13CARURRDEASAU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlos Alvarez Valdes / Urrea (`KXITFDOUBLES-26NOV13CARURRDEASAU-CARURR`) | 0.80 / 0.81 (2) | 80.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| De Alba / Sau Franco (`KXITFDOUBLES-26NOV13CARURRDEASAU-DEASAU`) | 0.14 / 0.19 (172) | 16.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Lucca Cervantes Tomas / Alejandro Reyes Tirado vs Flores / Matta -- M15 Zamora SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-14T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13LUCALEFLOMAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Flores / Matta (`KXITFDOUBLES-26NOV13LUCALEFLOMAT-FLOMAT`) | 0.17 / 0.34 (1) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lucca Cervantes Tomas / Alejandro Reyes Tirado (`KXITFDOUBLES-26NOV13LUCALEFLOMAT-LUCALE`) | 0.55 / 0.69 (21) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Rio Noguchi vs Yu Hsiou Hsu -- ATP Challenger Matsuyama SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-14T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200318:200677:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yu Hsiou Hsu (`KXATPCHALLENGERMATCH-26NOV13NOGHSU-HSU`) | 0.50 / 0.51 (1255) | 50.5% | 49.3% | 47.4% | 48.4% [46.9%-50.5%] | -- | 49.9% | 49.9% | MODEL_LONE_OUTLIER | PASS | -1.2 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Rio Noguchi (`KXATPCHALLENGERMATCH-26NOV13NOGHSU-NOG`) | 0.49 / 0.50 (18745) | 49.5% | 50.7% | 52.6% | 51.6% [49.5%-53.1%] | -- | 49.8% | 49.8% | MARKETS_AGREE | PASS | +1.2 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4350.0, B 4515.0; serve-point win A 58.7%, B 41.5%; Elo A 1603.5, B 1618.8; model uncertainty 0.0182
* Form inputs: days since last match A 18, B 11; matches on record A 575, B 532; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.021, surface_dev_loose +0.005, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Rei Sakamoto vs Billy Harris -- ATP Challenger Matsuyama SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-14T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126129:210536:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Billy Harris (`KXATPCHALLENGERMATCH-26NOV13SAKHAR-HAR`) | 0.25 / 0.26 (17529) | 25.5% | 27.5% | 33.9% | 31.7% [30.4%-33.8%] | -- | 25.4% | 25.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +2.0 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Rei Sakamoto (`KXATPCHALLENGERMATCH-26NOV13SAKHAR-SAK`) | 0.74 / 0.75 (1017) | 74.5% | 72.5% | 66.1% | 68.3% [66.2%-69.6%] | -- | 75.0% | 75.0% | MODEL_LONE_OUTLIER | PASS | -2.0 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4519.0, B 5763.0; serve-point win A 68.6%, B 36.3%; Elo A 1784.3, B 1608.9; model uncertainty 0.0171
* Form inputs: days since last match A 18, B 11; matches on record A 190, B 640; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.018, surface_pool_high +0.013, surface_dev_loose +0.008, surface_dev_tight -0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Vivian Wolff vs Miriam Bianca Bulgaru -- W50 Chihuahua SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-14T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214480:215386:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miriam Bianca Bulgaru (`KXITFWMATCH-26NOV13WOLBUL-BUL`) | 0.42 / 0.45 (15) | 43.5% | 44.8% | 27.3% | 37.9% [33.8%-46.2%] | -- | -- | -- | -- | PASS | +1.3 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Vivian Wolff (`KXITFWMATCH-26NOV13WOLBUL-WOL`) | 0.53 / 0.56 (39) | 54.5% | 55.2% | 72.7% | 62.1% [53.8%-66.2%] | -- | -- | -- | -- | WATCH | +0.7 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2229.0, B 3417.0; serve-point win A 51.4%, B 49.5%; Elo A 1638.5, B 1669.5; model uncertainty 0.0621
* Form inputs: days since last match A 45, B 200; matches on record A 284, B 517; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.035, surface_pool_high -0.036, surface_dev_loose +0.020, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sebastian Gorzny vs August Holmgren -- ATP Challenger Brisbane SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-14T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200416:210478:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sebastian Gorzny (`KXATPCHALLENGERMATCH-26NOV13GORHOL-GOR`) | 0.48 / 0.50 (11869) | 49.0% | 32.2% | 35.3% | 35.3% [29.5%-39.5%] | -- | 48.3% | -- | INSUFFICIENT_INPUTS | PASS | -16.8 pp | HIGH_REVIEW | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| August Holmgren (`KXATPCHALLENGERMATCH-26NOV13GORHOL-HOL`) | 0.51 / 0.52 (11861) | 51.5% | 67.8% | 64.7% | 64.7% [60.5%-70.5%] | -- | 51.6% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +16.3 pp | HIGH_REVIEW | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1167.0, B 4476.0; serve-point win A 64.6%, B 31.6%; Elo A 1502.6, B 1609.9; model uncertainty 0.0496
* Form inputs: days since last match A 18, B 11; matches on record A 41, B 320; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV13GORHOL-HOL  (YES = August Holmgren)
Model: 68%
Kalshi: 52%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: LOW_DISPLAYED_LIQUIDITY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.040, surface_pool_high +0.042, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Finn Reynolds / James Watt vs Pruchya Isaro / Yuta Shimizu -- ATP Challenger Matsuyama F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 06:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-14T06:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13REYWATISASHI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pruchya Isaro / Yuta Shimizu (`KXATPCHALLENGERDOUBLES-26NOV13REYWATISASHI-ISASHI`) | 0.27 / 0.74 (1127) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Finn Reynolds / James Watt (`KXATPCHALLENGERDOUBLES-26NOV13REYWATISASHI-REYWAT`) | 0.64 / 0.74 (90) | 69.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Blake Ellis / Li Tu vs Alafia Ayeni / Kokoro Isomura -- ATP Challenger Brisbane F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-14T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13ELLTULAVEISO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alafia Ayeni / Kokoro Isomura (`KXATPCHALLENGERDOUBLES-26NOV13ELLTULAVEISO-AVEISO`) | 0.30 / 0.76 (1002) | 53.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Blake Ellis / Li Tu (`KXATPCHALLENGERDOUBLES-26NOV13ELLTULAVEISO-ELLTUL`) | 0.60 / 0.72 (2) | 66.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Gadecki / Wen Wan vs Stevens / Thompson -- W75 Brisbane F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-14T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV13GADWENSTETHO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gadecki / Wen Wan (`KXITFWDOUBLES-26NOV13GADWENSTETHO-GADWEN`) | 0.13 / 0.68 (2) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stevens / Thompson (`KXITFWDOUBLES-26NOV13GADWENSTETHO-STETHO`) | 0.30 / 0.86 (1) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Joanna Garland vs Emerson Jones -- W75 Brisbane SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-14T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220466:263644:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joanna Garland (`KXITFWMATCH-26NOV13GARJON-GAR`) | 0.52 / 0.53 (119) | 52.5% | 44.3% | 37.2% | 41.2% [39.2%-47.4%] | 52.9% | -- | 52.9% | MARKETS_AGREE | PASS | -8.2 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Emerson Jones (`KXITFWMATCH-26NOV13GARJON-JON`) | 0.46 / 0.48 (485) | 47.0% | 55.7% | 62.8% | 58.8% [52.6%-60.8%] | 47.1% | -- | 47.1% | MODEL_LONE_OUTLIER | WATCH | +8.7 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2480.0, B 3547.0; serve-point win A 58.1%, B 40.8%; Elo A 1772.3, B 1788.5; model uncertainty 0.0407
* Form inputs: days since last match A 9, B 10; matches on record A 397, B 156; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.020, surface_dev_tight +0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Juncheng Shang vs Christian Langmo -- ATP Challenger Brisbane SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 07:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-14T07:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132052:209992:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Christian Langmo (`KXATPCHALLENGERMATCH-26NOV13SHALAN-LAN`) | 0.14 / 0.15 (11580) | 14.5% | 16.1% | 35.2% | 25.8% [20.8%-29.5%] | -- | 15.0% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +1.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Juncheng Shang (`KXATPCHALLENGERMATCH-26NOV13SHALAN-SHA`) | 0.85 / 0.86 (1510) | 85.5% | 83.9% | 64.8% | 74.2% [70.5%-79.2%] | -- | 86.4% | -- | INSUFFICIENT_INPUTS | PASS | -1.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2480.0, B 3910.0; serve-point win A 69.8%, B 38.3%; Elo A 1805.1, B 1486.3; model uncertainty 0.0438
* Form inputs: days since last match A 18, B 18; matches on record A 239, B 445; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.016, surface_dev_loose -0.001, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Strakhova / Tikhonova vs Cross / Papamichail -- W50 Chihuahua F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 07:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-14T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV13STRTIKCROPAP:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cross / Papamichail (`KXITFWDOUBLES-26NOV13STRTIKCROPAP-CROPAP`) | 0.31 / 0.38 (243) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Strakhova / Tikhonova (`KXITFWDOUBLES-26NOV13STRTIKCROPAP-STRTIK`) | 0.60 / 0.66 (200) | 63.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Edoardo Cherie Ligniere vs Azuma Visaya -- M15 Kuala Lumpur SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-14T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210405:212122:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Edoardo Cherie Ligniere (`KXITFMATCH-26NOV13CHEVIS-CHE`) | 0.62 / 0.63 (374) | 62.5% | 46.4% | 37.6% | 44.2% [42.1%-44.8%] | -- | -- | -- | -- | PASS | -16.1 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Azuma Visaya (`KXITFMATCH-26NOV13CHEVIS-VIS`) | 0.37 / 0.38 (125) | 37.5% | 53.6% | 62.4% | 55.8% [55.2%-57.9%] | -- | -- | -- | -- | PASS | +16.1 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 266.0, B 253.0; serve-point win A 56.5%, B 42.9%; Elo A 1191.9, B 1230.0; model uncertainty 0.0135
* Form inputs: days since last match A 200, B 354; matches on record A 17, B 11; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV13CHEVIS-VIS  (YES = Azuma Visaya)
Model: 54%
Kalshi: 38%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniil Sarksian vs Dev Javia -- M15 Kuala Lumpur SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-14T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209956:212022:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dev Javia (`KXITFMATCH-26NOV13SARJAV-JAV`) | 0.67 / 0.68 (355) | 67.5% | 55.7% | 61.3% | 58.8% [56.8%-60.3%] | -- | -- | -- | -- | PASS | -11.8 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daniil Sarksian (`KXITFMATCH-26NOV13SARJAV-SAR`) | 0.32 / 0.33 (802) | 32.5% | 44.3% | 38.7% | 41.2% [39.7%-43.2%] | -- | -- | -- | -- | WATCH | +11.8 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2188.0, B 1847.0; serve-point win A 57.9%, B 41.0%; Elo A 1227.8, B 1268.6; model uncertainty 0.0178
* Form inputs: days since last match A 214, B 186; matches on record A 62, B 144; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.021, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zhuoxuan Bai vs Carol Young Suh Lee -- W75 Brisbane SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-14T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221803:222296:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zhuoxuan Bai (`KXITFWMATCH-26NOV13BAILEE-BAI`) | 0.38 / 0.40 (67) | 39.0% | 49.5% | 42.1% | 45.2% [43.7%-46.8%] | 39.4% | -- | 39.4% | MARKETS_AGREE | WATCH | +10.5 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Carol Young Suh Lee (`KXITFWMATCH-26NOV13BAILEE-LEE`) | 0.60 / 0.61 (97) | 60.5% | 50.5% | 57.9% | 54.8% [53.2%-56.3%] | 60.6% | -- | 60.6% | MARKETS_AGREE | PASS | -10.0 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1601.0, B 4047.0; serve-point win A 55.8%, B 44.1%; Elo A 1765.4, B 1774.5; model uncertainty 0.0158
* Form inputs: days since last match A 35, B 11; matches on record A 213, B 160; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.016, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xi Luo vs Valeria Savinykh -- W15 Maanshan SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-14T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:202443:264069:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xi Luo (`KXITFWMATCH-26NOV13LUOSAV-LUO`) | 0.32 / 0.34 (384) | 33.0% | 39.0% | 63.1% | 36.9% [27.8%-44.2%] | 34.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.0 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valeria Savinykh (`KXITFWMATCH-26NOV13LUOSAV-SAV`) | 0.66 / 0.67 (379) | 66.5% | 61.0% | 36.9% | 63.1% [55.8%-72.2%] | 65.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.5 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 827.0, B 1181.0; serve-point win A 53.1%, B 44.8%; Elo A 1415.7, B 1611.5; model uncertainty 0.0816
* Form inputs: days since last match A 200, B 45; matches on record A 43, B 735; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kanon Sawashiro vs Heather Watson -- W50 Yokohama SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-14T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV13SAWWAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanon Sawashiro (`KXITFWMATCH-26NOV13SAWWAT-SAW`) | 0.19 / 0.20 (207) | 19.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Heather Watson (`KXITFWMATCH-26NOV13SAWWAT-WAT`) | 0.78 / 0.81 (26) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alina Tikhonova vs Thasaporn Naklo -- W15 Maanshan SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-14T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220597:270431:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thasaporn Naklo (`KXITFWMATCH-26NOV13TIKNAK-NAK`) | 0.31 / 0.32 (873) | 31.5% | 44.6% | 26.0% | 45.2% [38.4%-52.1%] | 31.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.1 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alina Tikhonova (`KXITFWMATCH-26NOV13TIKNAK-TIK`) | 0.68 / 0.70 (318) | 69.0% | 55.4% | 74.0% | 54.8% [47.9%-61.6%] | 68.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.6 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 349.0, B 2173.0; serve-point win A 53.9%, B 47.1%; Elo A 1453.2, B 1456.9; model uncertainty 0.0686
* Form inputs: days since last match A 284, B 200; matches on record A 5, B 166; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.011, surface_dev_loose +0.011, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Denis Yevseyev vs Tsz Fu Wong -- M15 Hua Hin SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-14T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106187:212971:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tsz Fu Wong (`KXITFMATCH-26NOV13YEVWON-WON`) | 0.09 / 0.11 (155) | 10.0% | 6.5% | 8.8% | 7.3% [6.5%-8.2%] | -- | -- | -- | -- | PASS | -3.5 pp | NORMAL | FRESH | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Denis Yevseyev (`KXITFMATCH-26NOV13YEVWON-YEV`) | 0.88 / 0.91 (358) | 89.5% | 93.5% | 91.2% | 92.7% [91.8%-93.5%] | -- | -- | -- | -- | PASS | +4.0 pp | NORMAL | FRESH | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5377.0, B 498.0; serve-point win A 64.6%, B 47.0%; Elo A 1524.8, B 1070.2; model uncertainty 0.0089
* Form inputs: days since last match A 67, B 56; matches on record A 911, B 20; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.009, surface_dev_loose +0.007, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chia Yi Tsao vs Kyoka Okamura -- W50 Yokohama SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-14T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV13TSAOKA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kyoka Okamura (`KXITFWMATCH-26NOV13TSAOKA-OKA`) | 0.73 / 0.77 (181) | 75.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Chia Yi Tsao (`KXITFWMATCH-26NOV13TSAOKA-TSA`) | 0.22 / 0.25 (125) | 23.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rigele Te vs Noritaka Koizumi -- M15 Maanshan SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-14T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144751:212476:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Noritaka Koizumi (`KXITFMATCH-26NOV13TEXKOI-KOI`) | 0.09 / 0.11 (3923) | 10.0% | 23.0% | 51.5% | 34.4% [32.4%-35.8%] | 11.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.0 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rigele Te (`KXITFMATCH-26NOV13TEXKOI-TEX`) | 0.88 / 0.90 (250) | 89.0% | 77.0% | 48.5% | 65.6% [64.2%-67.6%] | 89.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.0 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1492.0, B 190.0; serve-point win A 66.7%, B 39.2%; Elo A 1414.4, B 1285.6; model uncertainty 0.0169
* Form inputs: days since last match A 18, B 228; matches on record A 319, B 8; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high +0.000, surface_dev_loose +0.003, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zhao Zhao vs Sheng Tang -- M15 Maanshan SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-14T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206888:207463:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sheng Tang (`KXITFMATCH-26NOV13ZHATAN-TAN`) | 0.37 / 0.39 (202) | 38.0% | 54.3% | 36.6% | 49.0% [47.5%-50.0%] | 40.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +16.3 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zhao Zhao (`KXITFMATCH-26NOV13ZHATAN-ZHA`) | 0.60 / 0.62 (51) | 61.0% | 45.7% | 63.4% | 51.0% [50.0%-52.5%] | 59.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.3 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 155.0, B 714.0; serve-point win A 61.7%, B 37.5%; Elo A 1177.3, B 1177.1; model uncertainty 0.0126
* Form inputs: days since last match A 221, B 207; matches on record A 25, B 92; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV13ZHATAN-TAN  (YES = Sheng Tang)
Model: 54%
Kalshi: 38%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oki / Taka vs Eichenseher / Mueller -- M15 Kuala Lumpur F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-14T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13OKITAKEICMUE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eichenseher / Mueller (`KXITFDOUBLES-26NOV13OKITAKEICMUE-EICMUE`) | 0.36 / 0.90 (0) | 63.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Oki / Taka (`KXITFDOUBLES-26NOV13OKITAKEICMUE-OKITAK`) | 0.06 / 0.63 (1) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sanhui Shin vs Ergi Kirkin -- M15 Hua Hin SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-14T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13SHIKIR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ergi Kirkin (`KXITFMATCH-26NOV13SHIKIR-KIR`) | 0.60 / 0.62 (406) | 61.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sanhui Shin (`KXITFMATCH-26NOV13SHIKIR-SHI`) | 0.37 / 0.40 (955) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jeong / Yang vs Jin / Sun -- M15 Maanshan F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-14T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV14JEOYANJINSUN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jeong / Yang (`KXITFDOUBLES-26NOV14JEOYANJINSUN-JEOYAN`) | 0.38 / 0.88 (4) | 63.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jin / Sun (`KXITFDOUBLES-26NOV14JEOYANJINSUN-JINSUN`) | 0.05 / 0.66 (3) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Michele Ribecai vs Henry Searle -- ATP Challenger Hersonissos SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-14T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV14RIBSEA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michele Ribecai (`KXATPCHALLENGERMATCH-26NOV14RIBSEA-RIB`) | 0.37 / 0.38 (124) | 37.5% | 45.8% | -- | -- [-----] | -- | 38.4% | 38.4% | MODEL_LONE_OUTLIER | -- | +8.3 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | AMBIGUOUS |
| Henry Searle (`KXATPCHALLENGERMATCH-26NOV14RIBSEA-SEA`) | 0.61 / 0.62 (145) | 61.5% | 54.2% | -- | -- [-----] | -- | 62.2% | 62.2% | MODEL_LONE_OUTLIER | -- | -7.3 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 62.5%, B 36.7%; Elo A 1536.3, B 1604.0; model uncertainty None
* Form inputs: days since last match A 25, B 25; matches on record A 191, B 197; data quality A
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Hou / Plipuech vs Im / Shin -- W15 Maanshan F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-14T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV14HOUPLIIMXSHI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hou / Plipuech (`KXITFWDOUBLES-26NOV14HOUPLIIMXSHI-HOUPLI`) | 0.35 / 0.84 (1) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Im / Shin (`KXITFWDOUBLES-26NOV14HOUPLIIMXSHI-IMXSHI`) | 0.05 / 0.71 (1006) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kim / Morisaki vs Li / Saito -- W50 Yokohama F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-14T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV14KIMMORLIXSAI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kim / Morisaki (`KXITFWDOUBLES-26NOV14KIMMORLIXSAI-KIMMOR`) | 0.11 / 0.84 (4) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Li / Saito (`KXITFWDOUBLES-26NOV14KIMMORLIXSAI-LIXSAI`) | 0.12 / 0.84 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Taylor Fritz vs Thiago Agustin Tirante -- ATP Stockholm F

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-14 15:00Z
* Current expected start: 2026-11-14 12:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-13 23:25Z
* Recommended handicap-by time: 2026-11-14 11:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-11-14T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126203:202058:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Taylor Fritz (`KXATPMATCH-26NOV14FRITIR-FRI`) | 0.83 / 0.84 (1009) | 83.5% | 83.2% | 78.4% | 80.4% [79.8%-81.7%] | -- | 83.7% | 83.7% | MODEL_LONE_OUTLIER | PASS | -0.3 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Thiago Agustin Tirante (`KXATPMATCH-26NOV14FRITIR-TIR`) | 0.16 / 0.17 (86701) | 16.5% | 16.8% | 21.6% | 19.6% [18.3%-20.2%] | -- | 16.3% | 16.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +0.3 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 7020.0, B 5643.0; serve-point win A 73.6%, B 34.6%; Elo A 2063.3, B 1739.0; model uncertainty 0.0096
* Form inputs: days since last match A 2, B 5; matches on record A 773, B 494; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.004, surface_dev_tight +0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPSETWINNER-26NOV14FRITIR-2-FRI` Will Taylor Fritz win set 2 in the Taylor Fritz vs Thiago Agustin Tirante match: 0.04/0.95 mid 49.5%, model 74.0% (projection_v2.0 (prediction ledger)) -- gap +24.5 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV14FRITIR-2-TIR` Will Thiago Agustin Tirante win set 2 in the Taylor Fritz vs Thiago Agustin Tirante match: 0.02/0.97 mid 49.5%, model 26.0% (projection_v2.0 (prediction ledger)) -- gap -23.5 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV14FRITIR-FRI7` Will Taylor Fritz win at least 6.5 more games than Thiago Agustin Tirante?: 0.12/0.19 mid 15.5%, model 6.8% (projection_v2.0 (prediction ledger)) -- gap -8.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV14FRITIR-20` Over 19.5 games: 0.68/0.78 mid 73.0%, model 81.1% (projection_v2.0 (prediction ledger)) -- gap +8.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV14FRITIR-25` Over 24.5 games: 0.35/0.43 mid 39.0%, model 46.6% (projection_v2.0 (prediction ledger)) -- gap +7.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV14FRITIR-30` Over 29.5 games: 0.17/0.28 mid 22.5%, model 29.9% (projection_v2.0 (prediction ledger)) -- gap +7.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV14FRITIR-FRI20` Will Taylor Fritz win the Taylor Fritz vs Thiago Agustin Tirante match by a set score of 2-0?: 0.60/0.63 mid 61.5%, model 54.7% (projection_v2.0 (prediction ledger)) -- gap -6.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV14FRITIR-FRI4` Will Taylor Fritz win at least 3.5 more games than Thiago Agustin Tirante?: 0.55/0.56 mid 55.5%, model 49.3% (projection_v2.0 (prediction ledger)) -- gap -6.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV14FRITIR-TIR21` Will Thiago Agustin Tirante win the Taylor Fritz vs Thiago Agustin Tirante match by a set score of 2-1?: 0.07/0.23 mid 15.0%, model 10.0% (projection_v2.0 (prediction ledger)) -- gap -5.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV14FRITIR-FRI21` Will Taylor Fritz win the Taylor Fritz vs Thiago Agustin Tirante match by a set score of 2-1?: 0.22/0.29 mid 25.5%, model 28.5% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV14FRITIR-1-TIR` Will Thiago Agustin Tirante win set 1 in the Taylor Fritz vs Thiago Agustin Tirante match: 0.23/0.24 mid 23.5%, model 26.0% (projection_v2.0 (prediction ledger)) -- gap +2.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV14FRITIR-1-FRI` Will Taylor Fritz win set 1 in the Taylor Fritz vs Thiago Agustin Tirante match: 0.74/0.76 mid 75.0%, model 74.0% (projection_v2.0 (prediction ledger)) -- gap -1.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV14FRITIR-TIR20` Will Thiago Agustin Tirante win the Taylor Fritz vs Thiago Agustin Tirante match by a set score of 2-0?: 0.06/0.09 mid 7.5%, model 6.8% (projection_v2.0 (prediction ledger)) -- gap -0.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV14FRITIR-TIR2` Will Thiago Agustin Tirante win at least 1.5 more games than Taylor Fritz?: 0.05/0.18 mid 11.5%, model 11.7% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Francesco Maestrelli vs Philip Henning -- ATP Challenger Hersonissos SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 12:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-14T12:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV14MAEHEN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Philip Henning (`KXATPCHALLENGERMATCH-26NOV14MAEHEN-HEN`) | 0.46 / 0.47 (11) | 46.5% | -- | -- | -- [-----] | -- | 46.6% | 46.6% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Francesco Maestrelli (`KXATPCHALLENGERMATCH-26NOV14MAEHEN-MAE`) | 0.52 / 0.54 (5081) | 53.0% | -- | -- | -- [-----] | -- | 54.2% | 54.2% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Dmitry Popko vs Dragos Nicolae Madaras -- M15 Antalya SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-14T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:122078:200096:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dragos Nicolae Madaras (`KXITFMATCH-26NOV14POPMAD-MAD`) | 0.44 / 0.57 (1) | 50.5% | 71.8% | 94.9% | 82.7% [57.2%-91.1%] | -- | -- | -- | -- | PASS | +21.3 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dmitry Popko (`KXITFMATCH-26NOV14POPMAD-POP`) | 0.42 / 0.50 (1) | 46.0% | 28.2% | 5.1% | 17.3% [8.9%-42.8%] | -- | -- | -- | -- | PASS | -17.8 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3275.0, B 1412.0; serve-point win A 55.8%, B 39.9%; Elo A 1567.7, B 1644.1; model uncertainty 0.1695
* Form inputs: days since last match A 130, B 228; matches on record A 828, B 453; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV14POPMAD-MAD  (YES = Dragos Nicolae Madaras)
Model: 72%
Kalshi: 50%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.028, surface_pool_high -0.022, surface_dev_loose -0.026, surface_dev_tight +0.028
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alan Wazny vs Stefan Adrian Andreescu -- M15 Antalya SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-14T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210650:213048:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefan Adrian Andreescu (`KXITFMATCH-26NOV14WAZAND-AND`) | 0.41 / 0.45 (1) | 43.0% | 65.6% | 77.2% | 74.7% [69.2%-76.8%] | -- | -- | -- | -- | PASS | +22.6 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alan Wazny (`KXITFMATCH-26NOV14WAZAND-WAZ`) | 0.53 / 0.58 (156) | 55.5% | 34.4% | 22.8% | 25.3% [23.2%-30.8%] | -- | -- | -- | -- | PASS | -21.1 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1502.0, B 3228.0; serve-point win A 53.2%, B 43.8%; Elo A 1283.8, B 1441.5; model uncertainty 0.038
* Form inputs: days since last match A 60, B 263; matches on record A 36, B 144; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV14WAZAND-AND  (YES = Stefan Adrian Andreescu)
Model: 66%
Kalshi: 43%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight +0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nikola Mektic / Edouard Roger-Vasselin vs Erik Grevelius / Adam Heinonen -- ATP Stockholm F

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-14 16:30Z
* Current expected start: 2026-11-14 13:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-13 23:25Z
* Recommended handicap-by time: 2026-11-14 12:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-14T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV14MEKROGGREHEI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Erik Grevelius / Adam Heinonen (`KXATPDOUBLES-26NOV14MEKROGGREHEI-GREHEI`) | 0.31 / 0.39 (42) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nikola Mektic / Edouard Roger-Vasselin (`KXATPDOUBLES-26NOV14MEKROGGREHEI-MEKROG`) | 0.55 / 0.64 (108) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Filip Duda / Tiago Pereira vs James Mackinlay / Jeevan Nedunchezhiyan -- ATP Challenger Monastir F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-14T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV14DUDPERMACNED:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Filip Duda / Tiago Pereira (`KXATPCHALLENGERDOUBLES-26NOV14DUDPERMACNED-DUDPER`) | 0.47 / 0.69 (3) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| James Mackinlay / Jeevan Nedunchezhiyan (`KXATPCHALLENGERDOUBLES-26NOV14DUDPERMACNED-MACNED`) | 0.24 / 0.45 (3) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jonas Forejtek vs Marvin Moeller -- ATP Challenger Monastir SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-14T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV14FORMOE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jonas Forejtek (`KXATPCHALLENGERMATCH-26NOV14FORMOE-FOR`) | 0.65 / 0.67 (61) | 66.0% | -- | -- | -- [-----] | -- | 64.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marvin Moeller (`KXATPCHALLENGERMATCH-26NOV14FORMOE-MOE`) | 0.33 / 0.35 (4917) | 34.0% | -- | -- | -- [-----] | -- | 35.2% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Marek Gengel vs Yurii Dzhavakian -- M15 Sharm ElSheikh SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-14T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:122113:200309:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yurii Dzhavakian (`KXITFMATCH-26NOV14GENDZH-DZH`) | 0.14 / 0.21 (5) | 17.5% | 19.5% | 19.1% | 20.9% [18.4%-26.6%] | -- | -- | -- | -- | PASS | +2.0 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marek Gengel (`KXITFMATCH-26NOV14GENDZH-GEN`) | 0.79 / 0.85 (1) | 82.0% | 80.5% | 80.9% | 79.1% [73.4%-81.6%] | -- | -- | -- | -- | PASS | -1.5 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3291.0, B 5142.0; serve-point win A 61.8%, B 44.8%; Elo A 1578.0, B 1383.3; model uncertainty 0.0411
* Form inputs: days since last match A 60, B 200; matches on record A 628, B 436; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.015, surface_dev_loose +0.015, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Robert Guna vs Imanol Lopez Morillo -- M15 Heraklion SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-14T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202209:211491:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Robert Guna (`KXITFMATCH-26NOV14GUNLOP-GUN`) | 0.43 / 0.44 (115) | 43.5% | 37.6% | 52.1% | 40.3% [28.4%-45.4%] | -- | -- | -- | -- | PASS | -5.9 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Imanol Lopez Morillo (`KXITFMATCH-26NOV14GUNLOP-LOP`) | 0.54 / 0.56 (118) | 55.0% | 62.4% | 47.9% | 59.7% [54.6%-71.6%] | -- | -- | -- | -- | PASS | +7.4 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1036.0, B 2512.0; serve-point win A 58.4%, B 39.2%; Elo A 1235.7, B 1365.3; model uncertainty 0.0847
* Form inputs: days since last match A 284, B 46; matches on record A 27, B 357; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.040, surface_pool_high +0.035, surface_dev_loose +0.025, surface_dev_tight -0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Artur Kukasian vs Filiberto Fumagalli -- M15 Sharm ElSheikh SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-14T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210092:210477:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Filiberto Fumagalli (`KXITFMATCH-26NOV14KUKFUM-FUM`) | 0.53 / 0.57 (250) | 55.0% | 21.4% | 25.7% | 24.4% [22.5%-25.7%] | -- | -- | -- | -- | PASS | -33.6 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Artur Kukasian (`KXITFMATCH-26NOV14KUKFUM-KUK`) | 0.40 / 0.43 (5) | 41.5% | 78.6% | 74.3% | 75.6% [74.4%-77.5%] | -- | -- | -- | -- | PASS | +37.1 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2159.0, B 526.0; serve-point win A 64.1%, B 42.0%; Elo A 1300.0, B 1102.5; model uncertainty 0.0158
* Form inputs: days since last match A 242, B 340; matches on record A 99, B 25; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV14KUKFUM-KUK  (YES = Artur Kukasian)
Model: 79%
Kalshi: 42%
Gap: +37 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.000, surface_dev_loose +0.007, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Flynn Thomas vs Josip Simundza -- M15 Heraklion SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-14T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210537:213151:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Josip Simundza (`KXITFMATCH-26NOV14THOSIM-SIM`) | 0.49 / 0.51 (269) | 50.0% | 59.6% | 71.5% | 58.7% [54.1%-62.6%] | -- | -- | -- | -- | PASS | +9.6 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Flynn Thomas (`KXITFMATCH-26NOV14THOSIM-THO`) | 0.48 / 0.50 (271) | 49.0% | 40.4% | 28.5% | 41.3% [37.4%-45.9%] | -- | -- | -- | -- | PASS | -8.6 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 723.0, B 2596.0; serve-point win A 59.5%, B 38.6%; Elo A 1283.7, B 1298.8; model uncertainty 0.0426
* Form inputs: days since last match A 221, B 186; matches on record A 16, B 111; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.025, surface_pool_high +0.020, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yekaterina Dmitrichenko vs Lamis Alhussein Abdel Aziz -- W15 Sharm ElSheikh SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-14T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213974:216243:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lamis Alhussein Abdel Aziz (`KXITFWMATCH-26NOV14DMIALH-ALH`) | 0.47 / 0.52 (5) | 49.5% | 88.9% | 91.9% | 86.3% [84.4%-87.7%] | -- | -- | -- | -- | PASS | +39.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yekaterina Dmitrichenko (`KXITFWMATCH-26NOV14DMIALH-DMI`) | 0.47 / 0.51 (5) | 49.0% | 11.1% | 8.1% | 13.7% [12.3%-15.6%] | -- | -- | -- | -- | PASS | -37.9 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 301.0, B 4747.0; serve-point win A 51.7%, B 39.1%; Elo A 1295.6, B 1596.1; model uncertainty 0.0161
* Form inputs: days since last match A 459, B 10; matches on record A 134, B 519; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV14DMIALH-ALH  (YES = Lamis Alhussein Abdel Aziz)
Model: 89%
Kalshi: 50%
Gap: +39 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.006, surface_pool_high +0.000, surface_dev_loose -0.003, surface_dev_tight +0.002
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valeriia Iushchenko vs Anais Gabriel -- W15 Antalya SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-14T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV14IUSGAB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anais Gabriel (`KXITFWMATCH-26NOV14IUSGAB-GAB`) | 0.12 / 0.22 (8) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Valeriia Iushchenko (`KXITFWMATCH-26NOV14IUSGAB-IUS`) | 0.80 / 0.83 (5) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ane Mintegi Del Olmo vs Lucia Cortez Llorca -- W35 Heraklion SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-14T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215398:221213:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucia Cortez Llorca (`KXITFWMATCH-26NOV14MINCOR-COR`) | 0.12 / 0.14 (116) | 13.0% | 14.1% | 15.1% | 18.1% [15.4%-24.7%] | -- | -- | -- | -- | PASS | +1.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ane Mintegi Del Olmo (`KXITFWMATCH-26NOV14MINCOR-MIN`) | 0.84 / 0.87 (250) | 85.5% | 85.9% | 84.9% | 81.9% [75.3%-84.6%] | -- | -- | -- | -- | PASS | +0.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2133.0, B 2415.0; serve-point win A 55.6%, B 52.4%; Elo A 1614.1, B 1399.7; model uncertainty 0.0465
* Form inputs: days since last match A 28, B 30; matches on record A 167, B 426; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.007, surface_dev_loose +0.024, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alisa Oktiabreva vs Sapfo Sakellaridi -- W35 Heraklion SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-14T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220364:260765:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alisa Oktiabreva (`KXITFWMATCH-26NOV14OKTSAK-OKT`) | 0.91 / 0.95 (442) | 93.0% | 87.5% | 63.5% | 70.7% [67.9%-73.0%] | -- | -- | -- | -- | PASS | -5.5 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sapfo Sakellaridi (`KXITFWMATCH-26NOV14OKTSAK-SAK`) | 0.05 / 0.07 (425) | 6.0% | 12.5% | 36.5% | 29.3% [27.0%-32.1%] | -- | -- | -- | -- | WATCH | +6.5 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1999.0, B 4165.0; serve-point win A 59.4%, B 49.3%; Elo A 1652.3, B 1427.4; model uncertainty 0.0253
* Form inputs: days since last match A 116, B 18; matches on record A 67, B 705; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ilay Yoruk vs Diana-Ioana Simionescu -- W15 Antalya SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-14T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215879:264978:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diana-Ioana Simionescu (`KXITFWMATCH-26NOV14YORSIM-SIM`) | 0.68 / 0.73 (67) | 70.5% | 66.3% | 81.5% | 66.6% [51.6%-74.0%] | -- | -- | -- | -- | PASS | -4.2 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ilay Yoruk (`KXITFWMATCH-26NOV14YORSIM-YOR`) | 0.26 / 0.29 (325) | 27.5% | 33.7% | 18.5% | 33.4% [26.0%-48.4%] | -- | -- | -- | -- | WATCH | +6.2 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1694.0, B 1418.0; serve-point win A 50.9%, B 46.0%; Elo A 1423.6, B 1427.4; model uncertainty 0.1121
* Form inputs: days since last match A 40, B 270; matches on record A 466, B 46; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.010, surface_dev_loose -0.024, surface_dev_tight +0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nikita Belozertsev vs Wissam Abderrahman -- M15 Monastir SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-14T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV14BELABD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wissam Abderrahman (`KXITFMATCH-26NOV14BELABD-ABD`) | 0.46 / 0.49 (250) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nikita Belozertsev (`KXITFMATCH-26NOV14BELABD-BEL`) | 0.52 / 0.53 (377) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Liam Gavrielides vs Julien Penzlin -- M15 Monastir SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-14T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209887:210114:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liam Gavrielides (`KXITFMATCH-26NOV14GAVPEN-GAV`) | 0.64 / 0.66 (250) | 65.0% | 82.2% | 81.8% | 74.7% [72.2%-76.3%] | -- | -- | -- | -- | PASS | +17.2 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Julien Penzlin (`KXITFMATCH-26NOV14GAVPEN-PEN`) | 0.31 / 0.35 (20) | 33.0% | 17.8% | 18.2% | 25.3% [23.7%-27.8%] | -- | -- | -- | -- | PASS | -15.2 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1215.0, B 317.0; serve-point win A 65.0%, B 42.2%; Elo A 1347.7, B 1176.4; model uncertainty 0.0201
* Form inputs: days since last match A 200, B 354; matches on record A 143, B 10; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV14GAVPEN-GAV  (YES = Liam Gavrielides)
Model: 82%
Kalshi: 65%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.021, surface_dev_loose +0.012, surface_dev_tight -0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Huang / Lu vs Chanta / Sornlaksup -- M15 Hua Hin F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-14T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV14HUALUXCHASOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chanta / Sornlaksup (`KXITFDOUBLES-26NOV14HUALUXCHASOR-CHASOR`) | 0.07 / 0.89 (4) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Huang / Lu (`KXITFDOUBLES-26NOV14HUALUXCHASOR-HUALUX`) | 0.06 / 0.89 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Aurora Corvi vs Maria Toma -- W15 Nules SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-14T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215966:264998:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aurora Corvi (`KXITFWMATCH-26NOV14CORTOM-COR`) | 0.34 / 0.36 (5) | 35.0% | 22.2% | 26.9% | 31.0% [27.8%-33.4%] | -- | -- | -- | -- | PASS | -12.8 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Toma (`KXITFWMATCH-26NOV14CORTOM-TOM`) | 0.62 / 0.64 (18) | 63.0% | 77.8% | 73.1% | 69.0% [66.6%-72.2%] | -- | -- | -- | -- | PASS | +14.8 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 531.0, B 1852.0; serve-point win A 50.7%, B 43.6%; Elo A 1227.9, B 1355.3; model uncertainty 0.0281
* Form inputs: days since last match A 221, B 54; matches on record A 24, B 252; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.014, surface_dev_loose -0.009, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daria Kuczer vs Lavinia Luciano -- W15 Monastir SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-14T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214784:266758:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daria Kuczer (`KXITFWMATCH-26NOV14KUCLUC-KUC`) | 0.82 / 0.83 (162) | 82.5% | 72.5% | 63.7% | 63.7% [58.5%-70.4%] | -- | -- | -- | -- | PASS | -10.1 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lavinia Luciano (`KXITFWMATCH-26NOV14KUCLUC-LUC`) | 0.16 / 0.18 (325) | 17.0% | 27.6% | 36.3% | 36.3% [29.6%-41.5%] | -- | -- | -- | -- | PASS | +10.6 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 816.0, B 1465.0; serve-point win A 53.2%, B 51.2%; Elo A 1451.2, B 1353.9; model uncertainty 0.0593
* Form inputs: days since last match A 466, B 207; matches on record A 172, B 83; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.049, surface_pool_high -0.051, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anastasia Lizunova vs Matilde Mariani -- W15 Monastir SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-14T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220343:261073:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasia Lizunova (`KXITFWMATCH-26NOV14LIZMAR-LIZ`) | 0.62 / 0.64 (258) | 63.0% | 50.7% | 63.6% | 58.0% [52.1%-62.6%] | -- | -- | -- | -- | PASS | -12.3 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matilde Mariani (`KXITFWMATCH-26NOV14LIZMAR-MAR`) | 0.34 / 0.37 (73) | 35.5% | 49.3% | 36.4% | 42.0% [37.4%-47.9%] | -- | -- | -- | -- | PASS | +13.8 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 647.0, B 616.0; serve-point win A 52.4%, B 47.8%; Elo A 1408.9, B 1368.6; model uncertainty 0.0525
* Form inputs: days since last match A 228, B 214; matches on record A 21, B 146; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.031, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stanke / Van Herck vs Kaan Oktay / Schlossmann -- M15 Sharm ElSheikh F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-14T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV14STAVANKAASCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kaan Oktay / Schlossmann (`KXITFDOUBLES-26NOV14STAVANKAASCH-KAASCH`) | 0.14 / 0.33 (1) | 23.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stanke / Van Herck (`KXITFDOUBLES-26NOV14STAVANKAASCH-STAVAN`) | 0.60 / 0.79 (3) | 69.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sandra Samir vs Anna Snigireva -- W15 Sharm ElSheikh SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-14T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211529:263980:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sandra Samir (`KXITFWMATCH-26NOV14SAMSNI-SAM`) | 0.61 / 0.62 (188) | 61.5% | 61.7% | 70.5% | 69.1% [67.1%-69.1%] | -- | -- | -- | -- | WATCH | +0.2 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anna Snigireva (`KXITFWMATCH-26NOV14SAMSNI-SNI`) | 0.35 / 0.39 (9) | 37.0% | 38.3% | 29.5% | 30.9% [30.9%-32.9%] | -- | -- | -- | -- | PASS | +1.3 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4604.0, B 1889.0; serve-point win A 51.0%, B 51.2%; Elo A 1556.7, B 1441.4; model uncertainty 0.0097
* Form inputs: days since last match A 11, B 200; matches on record A 807, B 86; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.009, surface_dev_loose -0.000, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jaeger / Masiianskaia vs Husar / Lizunova -- W15 Monastir F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-14T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV14JAEMASHUSLIZ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Husar / Lizunova (`KXITFWDOUBLES-26NOV14JAEMASHUSLIZ-HUSLIZ`) | 0.56 / 0.77 (1) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jaeger / Masiianskaia (`KXITFWDOUBLES-26NOV14JAEMASHUSLIZ-JAEMAS`) | 0.16 / 0.37 (1) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Iva Primorac Pavicic vs Beatrise Zeltina -- W15 Paris SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-14T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206248:260339:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iva Primorac Pavicic (`KXITFWMATCH-26NOV14PRIZEL-PRI`) | 0.31 / 0.35 (36) | 33.0% | 42.9% | 22.8% | 40.0% [33.0%-52.7%] | -- | -- | -- | -- | PASS | +9.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Beatrise Zeltina (`KXITFWMATCH-26NOV14PRIZEL-ZEL`) | 0.61 / 0.66 (661) | 63.5% | 57.1% | 77.2% | 60.0% [47.3%-67.0%] | -- | -- | -- | -- | PASS | -6.4 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1407.0, B 1940.0; serve-point win A 54.2%, B 44.4%; Elo A 1581.9, B 1523.4; model uncertainty 0.0982
* Form inputs: days since last match A 32, B 214; matches on record A 415, B 64; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.015, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alberto Barroso Campos vs Marcel Zielinski -- M15 Las Palmas de Gran Canaria QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-14T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132744:210505:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alberto Barroso Campos (`KXITFMATCH-26NOV14BARZIE-BAR`) | 0.47 / 0.49 (250) | 48.0% | 39.3% | 47.9% | 45.3% [41.6%-50.0%] | -- | -- | -- | -- | PASS | -8.7 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marcel Zielinski (`KXITFMATCH-26NOV14BARZIE-ZIE`) | 0.49 / 0.51 (196) | 50.0% | 60.7% | 52.1% | 54.7% [50.0%-58.4%] | -- | -- | -- | -- | PASS | +10.7 pp | REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2471.0, B 2564.0; serve-point win A 55.8%, B 42.1%; Elo A 1325.2, B 1392.0; model uncertainty 0.0418
* Form inputs: days since last match A 46, B 228; matches on record A 365, B 151; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.037, surface_pool_high -0.036, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Baum / Cerny vs Popko / Tiurnev -- M15 Antalya F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-14T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV14BAUCERPOPTIU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Baum / Cerny (`KXITFDOUBLES-26NOV14BAUCERPOPTIU-BAUCER`) | 0.36 / 0.55 (1) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Popko / Tiurnev (`KXITFDOUBLES-26NOV14BAUCERPOPTIU-POPTIU`) | 0.38 / 0.57 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sergi Fita Juan vs Manuel Mazza -- M15 Las Palmas de Gran Canaria QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-14T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207601:211390:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sergi Fita Juan (`KXITFMATCH-26NOV14FITMAZ-FIT`) | 0.18 / 0.23 (1) | 20.5% | 24.9% | 26.0% | 23.9% [23.1%-25.6%] | -- | -- | -- | -- | PASS | +4.3 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Manuel Mazza (`KXITFMATCH-26NOV14FITMAZ-MAZ`) | 0.75 / 0.79 (304) | 77.0% | 75.1% | 74.0% | 76.1% [74.4%-76.9%] | -- | -- | -- | -- | PASS | -1.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1247.0, B 2013.0; serve-point win A 55.1%, B 39.7%; Elo A 1215.2, B 1427.0; model uncertainty 0.0126
* Form inputs: days since last match A 200, B 199; matches on record A 41, B 151; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.008, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ignacio Parisca vs Roberto Perez socas -- M15 Las Palmas de Gran Canaria QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-14T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212306:214254:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ignacio Parisca (`KXITFMATCH-26NOV14PARPER-PAR`) | 0.85 / 0.88 (1) | 86.5% | 76.1% | 79.2% | 64.4% [61.3%-66.8%] | -- | -- | -- | -- | PASS | -10.4 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Roberto Perez socas (`KXITFMATCH-26NOV14PARPER-PER`) | 0.09 / 0.12 (140) | 10.5% | 23.9% | 20.8% | 35.6% [33.2%-38.7%] | -- | -- | -- | -- | PASS | +13.4 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1927.0, B 169.0; serve-point win A 60.1%, B 45.3%; Elo A 1383.1, B 1299.8; model uncertainty 0.0276
* Form inputs: days since last match A 74, B 368; matches on record A 98, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luca Potenza vs Giuseppe La Vela -- M25 San Gregorio di Catania SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-14T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206553:208153:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giuseppe La Vela (`KXITFMATCH-26NOV14POTLAV-LAV`) | 0.31 / 0.36 (469) | 33.5% | 53.7% | 50.0% | 53.6% [51.6%-55.7%] | -- | -- | -- | -- | PASS | +20.2 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luca Potenza (`KXITFMATCH-26NOV14POTLAV-POT`) | 0.62 / 0.65 (251) | 63.5% | 46.3% | 50.0% | 46.4% [44.3%-48.4%] | -- | -- | -- | -- | PASS | -17.2 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3341.0, B 2431.0; serve-point win A 58.9%, B 40.4%; Elo A 1371.6, B 1436.7; model uncertainty 0.0207
* Form inputs: days since last match A 32, B 53; matches on record A 346, B 183; data quality A

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV14POTLAV-LAV  (YES = Giuseppe La Vela)
Model: 54%
Kalshi: 34%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.021, surface_dev_loose -0.015, surface_dev_tight +0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arystanbekova / Yesypchuk vs Bojica / Safta -- W15 Antalya F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-14T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV14ARYYESBOJSAF:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arystanbekova / Yesypchuk (`KXITFWDOUBLES-26NOV14ARYYESBOJSAF-ARYYES`) | 0.47 / 0.66 (1) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bojica / Safta (`KXITFWDOUBLES-26NOV14ARYYESBOJSAF-BOJSAF`) | 0.23 / 0.46 (1) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Katerina Tsygourova vs Neus Torner Sensano -- W15 Nules SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-14T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216173:269717:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Neus Torner Sensano (`KXITFWMATCH-26NOV14TSYTOR-TOR`) | 0.41 / 0.44 (11) | 42.5% | 68.3% | 77.0% | 64.7% [54.3%-71.4%] | -- | -- | -- | -- | PASS | +25.8 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Katerina Tsygourova (`KXITFWMATCH-26NOV14TSYTOR-TSY`) | 0.53 / 0.57 (148) | 55.0% | 31.7% | 23.0% | 35.3% [28.6%-45.7%] | -- | -- | -- | -- | PASS | -23.3 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2323.0, B 1512.0; serve-point win A 46.9%, B 49.6%; Elo A 1482.8, B 1493.6; model uncertainty 0.0854
* Form inputs: days since last match A 33, B 61; matches on record A 284, B 40; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV14TSYTOR-TOR  (YES = Neus Torner Sensano)
Model: 68%
Kalshi: 42%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Galphin Cossu / David Martinez vs Batsabaken / Denitto -- M15 Monastir F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-14T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV14GALDAVBATDEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Batsabaken / Denitto (`KXITFDOUBLES-26NOV14GALDAVBATDEN-BATDEN`) | 0.14 / 0.46 (1) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Galphin Cossu / David Martinez (`KXITFDOUBLES-26NOV14GALDAVBATDEN-GALDAV`) | 0.48 / 0.81 (1) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Isis Louise Van den Broek vs Chelsea Fontenel -- W15 Paris SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-14T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:239454:264227:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chelsea Fontenel (`KXITFWMATCH-26NOV14VANFON-FON`) | 0.23 / 0.27 (9) | 25.0% | 21.4% | 33.0% | 27.4% [25.2%-29.2%] | -- | -- | -- | -- | PASS | -3.6 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Isis Louise Van den Broek (`KXITFWMATCH-26NOV14VANFON-VAN`) | 0.72 / 0.75 (453) | 73.5% | 78.6% | 67.0% | 72.6% [70.8%-74.8%] | -- | -- | -- | -- | PASS | +5.1 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1856.0, B 2027.0; serve-point win A 57.1%, B 48.8%; Elo A 1548.9, B 1321.2; model uncertainty 0.0199
* Form inputs: days since last match A 200, B 207; matches on record A 103, B 114; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.004, surface_dev_loose +0.013, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jones / Jones vs Brand / Thomas -- M15 Heraklion F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-14T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV14JONJONBRATHO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brand / Thomas (`KXITFDOUBLES-26NOV14JONJONBRATHO-BRATHO`) | 0.22 / 0.40 (100) | 31.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jones / Jones (`KXITFDOUBLES-26NOV14JONJONBRATHO-JONJON`) | 0.53 / 0.73 (3) | 63.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alex Marti Pujolras vs Raffaele Ciurnelli -- M25 San Gregorio di Catania SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-14T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207704:214125:2026-11-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raffaele Ciurnelli (`KXITFMATCH-26NOV14MARCIU-CIU`) | 0.26 / 0.29 (250) | 27.5% | 10.8% | 15.4% | 18.4% [16.9%-18.7%] | -- | -- | -- | -- | PASS | -16.6 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alex Marti Pujolras (`KXITFMATCH-26NOV14MARCIU-MAR`) | 0.67 / 0.71 (28) | 69.0% | 89.1% | 84.6% | 81.6% [81.3%-83.1%] | -- | -- | -- | -- | PASS | +20.1 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2643.0, B 44.0; serve-point win A 60.8%, B 48.5%; Elo A 1529.9, B 1267.2; model uncertainty 0.0087
* Form inputs: days since last match A 25, B 438; matches on record A 415, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV14MARCIU-MAR  (YES = Alex Marti Pujolras)
Model: 89%
Kalshi: 69%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.007, surface_dev_loose +0.001, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rojas / Vega Hernandez vs Aunion Duran / Palomar -- M15 Las Palmas de Gran Canaria SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-14T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV14ROJVEGAUNPAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aunion Duran / Palomar (`KXITFDOUBLES-26NOV14ROJVEGAUNPAL-AUNPAL`) | 0.33 / 0.53 (1) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rojas / Vega Hernandez (`KXITFDOUBLES-26NOV14ROJVEGAUNPAL-ROJVEG`) | 0.40 / 0.60 (1) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Gavrila / Sakellaridi vs Argyrokastriti / Cortez Llorca -- W35 Heraklion F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-14T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV14GAVSAKARGCOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Argyrokastriti / Cortez Llorca (`KXITFWDOUBLES-26NOV14GAVSAKARGCOR-ARGCOR`) | 0.27 / 0.46 (3) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gavrila / Sakellaridi (`KXITFWDOUBLES-26NOV14GAVSAKARGCOR-GAVSAK`) | 0.49 / 0.67 (1) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Juan Estevez vs Murkel Dellien -- M15 Roldan SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-14T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV14ESTDEL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Murkel Dellien (`KXITFMATCH-26NOV14ESTDEL-DEL`) | 0.40 / 0.44 (5) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Juan Estevez (`KXITFMATCH-26NOV14ESTDEL-EST`) | 0.55 / 0.59 (250) | 57.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Potenza / Tabacco vs Iannaccone / Ovcharenko -- M25 San Gregorio di Catania F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-14T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV14POTTABIANOVC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iannaccone / Ovcharenko (`KXITFDOUBLES-26NOV14POTTABIANOVC-IANOVC`) | 0.32 / 0.50 (1) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Potenza / Tabacco (`KXITFDOUBLES-26NOV14POTTABIANOVC-POTTAB`) | 0.44 / 0.63 (3) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Victoria Bosio vs Marie Mettraux -- W15 São Carlos SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-14T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV14BOSMET:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Victoria Bosio (`KXITFWMATCH-26NOV14BOSMET-BOS`) | 0.64 / 0.68 (15) | 66.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marie Mettraux (`KXITFWMATCH-26NOV14BOSMET-MET`) | 0.31 / 0.35 (7) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marjorie Souza vs Barbara Gatica -- W15 São Carlos SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-14T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV14SOUGAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barbara Gatica (`KXITFWMATCH-26NOV14SOUGAT-GAT`) | 0.86 / 0.89 (222) | 87.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marjorie Souza (`KXITFWMATCH-26NOV14SOUGAT-SOU`) | 0.11 / 0.14 (200) | 12.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Forcano / Izquierdo Luque vs Perez Ramos / Wright -- M25 Vale do Lobo SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-14T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV14FORIZQPERWRI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Forcano / Izquierdo Luque (`KXITFDOUBLES-26NOV14FORIZQPERWRI-FORIZQ`) | 0.31 / 0.51 (1) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Perez Ramos / Wright (`KXITFDOUBLES-26NOV14FORIZQPERWRI-PERWRI`) | 0.42 / 0.62 (1) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hernan Casanova vs Rocco Valente -- M15 Roldan SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-14T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV14CASVAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hernan Casanova (`KXITFMATCH-26NOV14CASVAL-CAS`) | 0.81 / 0.91 (4) | 86.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rocco Valente (`KXITFMATCH-26NOV14CASVAL-VAL`) | 0.06 / 0.13 (22) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Da Rosa Castro / Monteiro vs Almazan Valiente / Lagutin -- M25 Vale do Lobo QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-14T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV14DARMONALMLAG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Almazan Valiente / Lagutin (`KXITFDOUBLES-26NOV14DARMONALMLAG-ALMLAG`) | 0.07 / 0.89 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Da Rosa Castro / Monteiro (`KXITFDOUBLES-26NOV14DARMONALMLAG-DARMON`) | 0.06 / 0.89 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dias / Garcia Vidal vs Gatica / Pereira -- W15 São Carlos F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-14T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV14DIAGARGATPER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dias / Garcia Vidal (`KXITFWDOUBLES-26NOV14DIAGARGATPER-DIAGAR`) | 0.11 / 0.84 (4) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gatica / Pereira (`KXITFWDOUBLES-26NOV14DIAGARGATPER-GATPER`) | 0.11 / 0.84 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Valerio Aboian vs Juan Bautista Torres -- M25 Santa Cruz do Sul SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-14T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV14ABOTOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valerio Aboian (`KXITFMATCH-26NOV14ABOTOR-ABO`) | 0.45 / 0.79 (3) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Juan Bautista Torres (`KXITFMATCH-26NOV14ABOTOR-TOR`) | 0.23 / 0.55 (5) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cannon Kingsley vs Oskar Brostrom Poulsen -- M25 Montreal SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-14T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV14KINPOU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cannon Kingsley (`KXITFMATCH-26NOV14KINPOU-KIN`) | 0.64 / 0.71 (385) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Oskar Brostrom Poulsen (`KXITFMATCH-26NOV14KINPOU-POU`) | 0.26 / 0.32 (79) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maximilian Marterer vs Theodore Dean -- M25 Montreal SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-14 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-14T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV14MARDEA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theodore Dean (`KXITFMATCH-26NOV14MARDEA-DEA`) | 0.10 / 0.18 (24) | 14.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maximilian Marterer (`KXITFMATCH-26NOV14MARDEA-MAR`) | 0.77 / 0.87 (70) | 82.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jessica Pegula vs Mirra Andreeva -- WTA Finals Women Singles SF

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-14 23:00Z
* Current expected start: 2026-11-14 23:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-13 23:25Z
* Recommended handicap-by time: 2026-11-14 22:15Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-14T05:00:00+00:00 as not a valid time

WTA (TOUR_FINALS) · Hard · scheduled 2026-11-14T23:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26NOV14PEGAND:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mirra Andreeva (`KXWTAMATCH-26NOV14PEGAND-AND`) | 0.69 / 0.70 (3217) | 69.5% | 52.3% | -- | -- [-----] | -- | 66.7% | 66.7% | MODEL_LONE_OUTLIER | -- | -17.2 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | AMBIGUOUS |
| Jessica Pegula (`KXWTAMATCH-26NOV14PEGAND-PEG`) | 0.32 / 0.33 (5367) | 32.5% | 47.7% | -- | -- [-----] | -- | 32.0% | 32.0% | MODEL_LONE_OUTLIER | -- | +15.2 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 58.2%, B 41.3%; Elo A 2201.9, B 2104.8; model uncertainty None
* Form inputs: days since last match A 1, B 2; matches on record A 770, B 267; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26NOV14PEGAND-PEG  (YES = Jessica Pegula)
Model: 48%
Kalshi: 32%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: EVENT_MAPPING_RISK, EXTERNAL_MARKET_REJECTION
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 4 carry a model probability
  * `KXWTASETWINNER-26NOV14PEGAND-1-AND` Will Mirra Andreeva win set 1 in the Jessica Pegula vs Mirra Andreeva match: 0.01/0.98 mid 49.5%, model 51.5% (projection_v2.0 (prediction ledger)) -- gap +2.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV14PEGAND-1-PEG` Will Jessica Pegula win set 1 in the Jessica Pegula vs Mirra Andreeva match: 0.03/0.98 mid 50.5%, model 48.5% (projection_v2.0 (prediction ledger)) -- gap -2.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV14PEGAND-2-AND` Will Mirra Andreeva win set 2 in the Jessica Pegula vs Mirra Andreeva match: 0.01/0.98 mid 49.5%, model 51.5% (projection_v2.0 (prediction ledger)) -- gap +2.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV14PEGAND-2-PEG` Will Jessica Pegula win set 2 in the Jessica Pegula vs Mirra Andreeva match: 0.01/0.98 mid 49.5%, model 48.5% (projection_v2.0 (prediction ledger)) -- gap -1.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Harri Heliovaara / Henry Patten vs Orlando Luz / Rafael Matos -- ATP World Tour Finals Men Doubles Group

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-15 13:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_FINALS) · surface ? · scheduled 2026-11-15T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV15HELPATLUZMAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Harri Heliovaara / Henry Patten (`KXATPDOUBLES-26NOV15HELPATLUZMAT-HELPAT`) | 0.73 / 0.76 (150) | 74.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Orlando Luz / Rafael Matos (`KXATPDOUBLES-26NOV15HELPATLUZMAT-LUZMAT`) | 0.24 / 0.27 (808) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Alexander Zverev vs Rafael Jodar -- ATP World Tour Finals Men Singles Group A

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-15 16:00Z
* Current expected start: 2026-11-15 16:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: 2026-11-15 15:15Z

* Status notes: NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source)

ATP (TOUR_FINALS) · Hard · scheduled 2026-11-15T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:100644:212588:2026-11-15`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rafael Jodar (`KXATPMATCH-26NOV15ZVEJOD-JOD`) | 0.30 / 0.32 (363) | 31.0% | 38.3% | 34.4% | 34.0% [31.3%-35.3%] | -- | 32.2% | 32.2% | MODEL_LONE_OUTLIER | PASS | +7.3 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Alexander Zverev (`KXATPMATCH-26NOV15ZVEJOD-ZVE`) | 0.67 / 0.68 (85) | 67.5% | 61.7% | 65.6% | 66.0% [64.7%-68.7%] | -- | 67.8% | 67.8% | MODEL_LONE_OUTLIER | PASS | -5.8 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 8098.0, B 5364.0; serve-point win A 67.8%, B 34.7%; Elo A 2133.6, B 2001.8; model uncertainty 0.02
* Form inputs: days since last match A 9, B 10; matches on record A 941, B 144; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.013, surface_dev_loose -0.005, surface_dev_tight +0.005
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26NOV15ZVEJOD-ZVE20` Will Alexander Zverev win the Alexander Zverev vs Rafael Jodar match by a set score of 2-0?: 0.41/0.44 mid 42.5%, model 33.5% (projection_v2.0 (prediction ledger)) -- gap -9.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV15ZVEJOD-2-ZVE` Will Alexander Zverev win set 2 in the Alexander Zverev vs Rafael Jodar match: 0.02/0.97 mid 49.5%, model 57.8% (projection_v2.0 (prediction ledger)) -- gap +8.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV15ZVEJOD-2-JOD` Will Rafael Jodar win set 2 in the Alexander Zverev vs Rafael Jodar match: 0.02/0.97 mid 49.5%, model 42.2% (projection_v2.0 (prediction ledger)) -- gap -7.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV15ZVEJOD-JOD21` Will Rafael Jodar win the Alexander Zverev vs Rafael Jodar match by a set score of 2-1?: 0.10/0.20 mid 15.0%, model 20.6% (projection_v2.0 (prediction ledger)) -- gap +5.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV15ZVEJOD-1-JOD` Will Rafael Jodar win set 1 in the Alexander Zverev vs Rafael Jodar match: 0.36/0.40 mid 38.0%, model 42.2% (projection_v2.0 (prediction ledger)) -- gap +4.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV15ZVEJOD-ZVE21` Will Alexander Zverev win the Alexander Zverev vs Rafael Jodar match by a set score of 2-1?: 0.21/0.29 mid 25.0%, model 28.2% (projection_v2.0 (prediction ledger)) -- gap +3.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV15ZVEJOD-1-ZVE` Will Alexander Zverev win set 1 in the Alexander Zverev vs Rafael Jodar match: 0.60/0.62 mid 61.0%, model 57.8% (projection_v2.0 (prediction ledger)) -- gap -3.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV15ZVEJOD-JOD20` Will Rafael Jodar win the Alexander Zverev vs Rafael Jodar match by a set score of 2-0?: 0.15/0.18 mid 16.5%, model 17.8% (projection_v2.0 (prediction ledger)) -- gap +1.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Marcelo Arevalo / Mate Pavic vs Theo Arribage / Albano Olivetti -- ATP World Tour Finals Men Doubles Group

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-15 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_FINALS) · surface ? · scheduled 2026-11-15T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV15AREPAVARROLI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcelo Arevalo / Mate Pavic (`KXATPDOUBLES-26NOV15AREPAVARROLI-AREPAV`) | 0.52 / 0.57 (150) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Theo Arribage / Albano Olivetti (`KXATPDOUBLES-26NOV15AREPAVARROLI-ARROLI`) | 0.40 / 0.46 (150) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Ben Shelton vs Arthur Fils -- ATP World Tour Finals Men Singles Group A

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-15 22:30Z
* Current expected start: 2026-11-15 22:30Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: 2026-11-15 21:45Z

* Status notes: NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source)

ATP (TOUR_FINALS) · Hard · scheduled 2026-11-15T22:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:209950:210097:2026-11-15`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arthur Fils (`KXATPMATCH-26NOV15SHEFIL-FIL`) | 0.37 / 0.41 (8829) | 39.0% | 48.1% | 49.1% | 48.1% [45.9%-50.0%] | -- | 38.9% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +9.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ben Shelton (`KXATPMATCH-26NOV15SHEFIL-SHE`) | 0.60 / 0.61 (124) | 60.5% | 51.9% | 50.9% | 51.8% [50.0%-54.1%] | -- | 61.8% | 61.8% | MODEL_LONE_OUTLIER | PASS | -8.6 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 6706.0, B 4613.0; serve-point win A 70.8%, B 29.7%; Elo A 2081.5, B 2040.7; model uncertainty 0.0208
* Form inputs: days since last match A 5, B 8; matches on record A 322, B 340; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.018, surface_pool_high +0.023, surface_dev_loose -0.000, surface_dev_tight +0.000
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26NOV15SHEFIL-FIL21` Will Arthur Fils win the Ben Shelton vs Arthur Fils match by a set score of 2-1?: 0.01/0.24 mid 12.5%, model 24.3% (projection_v2.0 (prediction ledger)) -- gap +11.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV15SHEFIL-SHE21` Will Ben Shelton win the Ben Shelton vs Arthur Fils match by a set score of 2-1?: 0.01/0.30 mid 15.5%, model 25.6% (projection_v2.0 (prediction ledger)) -- gap +10.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV15SHEFIL-SHE20` Will Ben Shelton win the Ben Shelton vs Arthur Fils match by a set score of 2-0?: 0.34/0.37 mid 35.5%, model 26.3% (projection_v2.0 (prediction ledger)) -- gap -9.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV15SHEFIL-1-FIL` Will Arthur Fils win set 1 in the Ben Shelton vs Arthur Fils match: 0.41/0.44 mid 42.5%, model 48.7% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV15SHEFIL-1-SHE` Will Ben Shelton win set 1 in the Ben Shelton vs Arthur Fils match: 0.55/0.56 mid 55.5%, model 51.3% (projection_v2.0 (prediction ledger)) -- gap -4.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV15SHEFIL-FIL20` Will Arthur Fils win the Ben Shelton vs Arthur Fils match by a set score of 2-0?: 0.18/0.22 mid 20.0%, model 23.7% (projection_v2.0 (prediction ledger)) -- gap +3.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV15SHEFIL-2-SHE` Will Ben Shelton win set 2 in the Ben Shelton vs Arthur Fils match: 0.02/0.97 mid 49.5%, model 51.3% (projection_v2.0 (prediction ledger)) -- gap +1.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV15SHEFIL-2-FIL` Will Arthur Fils win set 2 in the Ben Shelton vs Arthur Fils match: 0.02/0.97 mid 49.5%, model 48.7% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
