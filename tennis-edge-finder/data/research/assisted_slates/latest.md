# ASSISTED SLATE -- 2026-11-12T17:23Z (`SL-20261112T172319Z-f87098ac`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

210 open matches not seen started, 448 markets. Skipped: {"scheduled_start_over_24h_past": 5, "first_ball_already_observed": 1}. Sources: shadow board 2026-11-12T13:07:51.743569+00:00, Model 4 2026-11-12T13:08:20.863781+00:00, Gen-1 ledger 2026-11-12T13:07:48.547858+00:00, external 2026-11-12T17:01:11.440593+00:00, capture 20261112T165922Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-11-12 19:00Z**
* Recommended RUN TENNIS time: **2026-11-12 18:15Z**
* Final price/status check time: **2026-11-12 18:50Z**
* Number of matches in window: 2 (Lorenzo Musetti vs Ugo Humbert, Marta Kostyuk vs Coco Gauff)

Slate built 2026-11-12T17:23Z. Refresh due by: 2026-11-12 18:15Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 19, "HIGH_REVIEW": 31, "NORMAL": 119, "REVIEW": 37, "UNPRICED": 242}; match winners: {"EXTREME": 19, "HIGH_REVIEW": 29, "NORMAL": 97, "REVIEW": 33, "UNPRICED": 242}; quote freshness at build: {"FRESH": 206}.

## De Armas / Garay vs Basel / Martinez -- M15 Roldan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11DEAGARBASMAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Basel / Martinez (`KXITFDOUBLES-26NOV11DEAGARBASMAR-BASMAR`) | 0.65 / 0.71 (217) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| De Armas / Garay (`KXITFDOUBLES-26NOV11DEAGARBASMAR-DEAGAR`) | 0.27 / 0.33 (242) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Mario Arce Fernandez vs Manuel Mazza -- M15 Las Palmas de Gran Canaria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207601:213535:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mario Arce Fernandez (`KXITFMATCH-26NOV12ARCMAZ-ARC`) | 0.12 / 0.14 (736) | 13.0% | 11.3% | 13.2% | 18.9% [16.8%-20.1%] | 15.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.7 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Manuel Mazza (`KXITFMATCH-26NOV12ARCMAZ-MAZ`) | 0.84 / 0.88 (711) | 86.0% | 88.7% | 86.8% | 81.1% [79.9%-83.2%] | 84.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.7 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 239.0, B 2013.0; serve-point win A 52.6%, B 38.1%; Elo A 1183.7, B 1427.0; model uncertainty 0.0167
* Form inputs: days since last match A 213, B 198; matches on record A 7, B 151; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.004, surface_dev_loose -0.007, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alberto Barroso Campos vs David Aguiar Johansson -- M15 Las Palmas de Gran Canaria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132744:214253:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| David Aguiar Johansson (`KXITFMATCH-26NOV12BARAGU-AGU`) | 0.06 / 0.09 (1814) | 7.5% | 31.5% | 37.6% | 38.6% [32.0%-46.3%] | -- | -- | -- | -- | PASS | +24.0 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alberto Barroso Campos (`KXITFMATCH-26NOV12BARAGU-BAR`) | 0.90 / 0.92 (250) | 91.0% | 68.5% | 62.4% | 61.4% [53.7%-68.0%] | -- | -- | -- | -- | PASS | -22.5 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2471.0, B 85.0; serve-point win A 59.7%, B 44.0%; Elo A 1325.2, B 1248.1; model uncertainty 0.0716
* Form inputs: days since last match A 45, B 367; matches on record A 365, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV12BARAGU-AGU  (YES = David Aguiar Johansson)
Model: 31%
Kalshi: 8%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.063, surface_pool_high -0.077, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carles Cordoba vs Xavi Palomar -- M15 Las Palmas de Gran Canaria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213059:214015:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carles Cordoba (`KXITFMATCH-26NOV12CORPAL-COR`) | 0.56 / 0.62 (48) | 59.0% | 78.0% | 71.5% | 68.8% [66.8%-72.0%] | 65.2% | -- | 65.2% | MODEL_LONE_OUTLIER | PASS | +19.0 pp | HIGH_REVIEW | FRESH | D / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Xavi Palomar (`KXITFMATCH-26NOV12CORPAL-PAL`) | 0.36 / 0.42 (51) | 39.0% | 22.0% | 28.5% | 31.2% [28.0%-33.2%] | 34.8% | -- | 34.8% | EXTERNAL_LONE_OUTLIER | PASS | -17.0 pp | HIGH_REVIEW | FRESH | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1490.0, B 617.0; serve-point win A 59.3%, B 46.6%; Elo A 1289.8, B 1161.1; model uncertainty 0.0263
* Form inputs: days since last match A 206, B 206; matches on record A 42, B 12; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV12CORPAL-COR  (YES = Carles Cordoba)
Model: 78%
Kalshi: 59%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: SUPPORTS_MODEL_DIRECTION
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.009, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ivan Gakhov vs Sergi Fita Juan -- M15 Las Palmas de Gran Canaria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:123809:211390:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sergi Fita Juan (`KXITFMATCH-26NOV12GAKFIT-FIT`) | 0.13 / 0.16 (634) | 14.5% | 16.5% | 30.5% | 17.7% [13.2%-21.3%] | -- | -- | -- | -- | PASS | +2.0 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ivan Gakhov (`KXITFMATCH-26NOV12GAKFIT-GAK`) | 0.83 / 0.86 (610) | 84.5% | 83.5% | 69.5% | 82.3% [78.7%-86.8%] | -- | -- | -- | -- | PASS | -1.0 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4154.0, B 1247.0; serve-point win A 62.3%, B 45.2%; Elo A 1590.5, B 1215.2; model uncertainty 0.0406
* Form inputs: days since last match A 38, B 199; matches on record A 857, B 41; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.003, surface_dev_loose +0.000, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bruno Pujol Navarro vs Matias Ponce de leon gomila -- M15 Las Palmas de Gran Canaria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207547:210038:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matias Ponce de leon gomila (`KXITFMATCH-26NOV12PUJPON-PON`) | 0.59 / 0.65 (19) | 62.0% | 63.1% | 80.6% | 63.3% [58.2%-71.0%] | 60.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Bruno Pujol Navarro (`KXITFMATCH-26NOV12PUJPON-PUJ`) | 0.31 / 0.37 (2) | 34.0% | 36.9% | 19.4% | 36.7% [29.0%-41.8%] | 39.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 250.0, B 397.0; serve-point win A 56.9%, B 40.6%; Elo A 1189.8, B 1265.0; model uncertainty 0.0639
* Form inputs: days since last match A 276, B 416; matches on record A 126, B 13; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.029, surface_dev_loose -0.010, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bianca Andreescu vs Marina Bassols Ribera -- WTA Challenger Sopo QF

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-11-12 19:10Z
* Current expected start: 2026-11-12 17:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-12 16:57Z
* Recommended handicap-by time: 2026-11-12 16:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA125 (CHALLENGER) · surface ? · scheduled 2026-11-12T19:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26NOV12ANDBAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bianca Andreescu (`KXWTACHALLENGERMATCH-26NOV12ANDBAS-AND`) | 0.78 / 0.79 (7859) | 78.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marina Bassols Ribera (`KXWTACHALLENGERMATCH-26NOV12ANDBAS-BAS`) | 0.21 / 0.22 (14537) | 21.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; STATUS_AMBIGUOUS; NO_EXTERNAL_PRICE

## Karim Al-Amin vs Marcel Zielinski -- M15 Las Palmas de Gran Canaria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210505:213100:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karim Al-Amin (`KXITFMATCH-26NOV12ALAZIE-ALA`) | 0.24 / 0.29 (381) | 26.5% | 23.8% | 35.7% | 32.8% [31.0%-34.8%] | 28.0% | -- | 28.0% | KALSHI_LONE_OUTLIER | PASS | -2.7 pp | NORMAL | FRESH | F / POOR | ALL_AGREE | VERIFIED |
| Marcel Zielinski (`KXITFMATCH-26NOV12ALAZIE-ZIE`) | 0.70 / 0.74 (489) | 72.0% | 76.2% | 64.3% | 67.2% [65.2%-69.0%] | 72.0% | -- | 72.0% | MODEL_LONE_OUTLIER | PASS | +4.2 pp | NORMAL | FRESH | F / POOR | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 74.0, B 2564.0; serve-point win A 55.8%, B 38.7%; Elo A 1268.1, B 1392.0; model uncertainty 0.0189
* Form inputs: days since last match A 486, B 227; matches on record A 3, B 151; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.019, surface_dev_loose +0.001, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rudolf Molleker vs Tomas Curras Abasolo -- M25 Vale do Lobo R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200330:200484:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tomas Curras Abasolo (`KXITFMATCH-26NOV12MOLCUR-CUR`) | -- / 0.01 (136040) | -- | 38.8% | 49.0% | 44.9% [36.9%-47.9%] | 29.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -- | UNPRICED | FRESH | B / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |
| Rudolf Molleker (`KXITFMATCH-26NOV12MOLCUR-MOL`) | 0.99 / -- (0) | -- | 61.2% | 51.0% | 55.1% [52.1%-63.1%] | 70.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | FRESH | B / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 4211.0, B 2492.0; serve-point win A 61.4%, B 40.8%; Elo A 1440.6, B 1366.3; model uncertainty 0.0553
* Form inputs: days since last match A 87, B 206; matches on record A 526, B 131; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.031, surface_dev_loose -0.026, surface_dev_tight +0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ignacio Parisca vs Maximilian Figl -- M15 Las Palmas de Gran Canaria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211904:212306:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maximilian Figl (`KXITFMATCH-26NOV12PARFIG-FIG`) | 0.11 / 0.13 (250) | 12.0% | 23.9% | 21.5% | 24.3% [21.5%-27.1%] | 14.4% | -- | 14.4% | KALSHI_LONE_OUTLIER | WATCH | +11.9 pp | REVIEW | FRESH | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Ignacio Parisca (`KXITFMATCH-26NOV12PARFIG-PAR`) | 0.85 / 0.88 (284) | 86.5% | 76.1% | 78.5% | 75.7% [72.9%-78.5%] | 85.6% | -- | 85.6% | MODEL_LONE_OUTLIER | PASS | -10.4 pp | REVIEW | FRESH | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1927.0, B 1358.0; serve-point win A 62.8%, B 42.7%; Elo A 1383.1, B 1204.8; model uncertainty 0.0278
* Form inputs: days since last match A 73, B 199; matches on record A 98, B 60; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.004, surface_dev_loose +0.011, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Roberto Perez socas vs Niklas Guttau -- M15 Las Palmas de Gran Canaria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207408:214254:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Niklas Guttau (`KXITFMATCH-26NOV12PERGUT-GUT`) | 0.80 / 0.83 (285) | 81.5% | 51.8% | 58.3% | 46.9% [44.8%-50.5%] | 80.5% | -- | 80.5% | MODEL_LONE_OUTLIER | PASS | -29.7 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Roberto Perez socas (`KXITFMATCH-26NOV12PERGUT-PER`) | 0.15 / 0.19 (528) | 17.0% | 48.2% | 41.7% | 53.1% [49.5%-55.2%] | 19.5% | -- | 19.5% | KALSHI_LONE_OUTLIER | PASS | +31.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 169.0, B 830.0; serve-point win A 57.3%, B 42.3%; Elo A 1299.8, B 1270.8; model uncertainty 0.0285
* Form inputs: days since last match A 367, B 234; matches on record A 2, B 61; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV12PERGUT-PER  (YES = Roberto Perez socas)
Model: 48%
Kalshi: 17%
Gap: +31 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Samuele Pieri vs Jacopo Berrettini -- M25 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 17:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T17:10:05Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202235:210129:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jacopo Berrettini (`KXITFMATCH-26NOV12PIEBER-BER`) | -- / 0.01 (158262) | -- | 52.5% | 51.0% | 52.6% [51.0%-53.1%] | -- | -- | -- | -- | PASS | -- | UNPRICED | FRESH | B / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |
| Samuele Pieri (`KXITFMATCH-26NOV12PIEBER-PIE`) | 0.99 / -- (0) | -- | 47.5% | 49.0% | 47.4% [46.9%-49.0%] | -- | -- | -- | -- | PASS | -- | UNPRICED | FRESH | B / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 3983.0, B 3742.0; serve-point win A 58.1%, B 41.4%; Elo A 1534.6, B 1571.4; model uncertainty 0.0104
* Form inputs: days since last match A 24, B 227; matches on record A 208, B 386; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.005, surface_dev_loose -0.005, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Benjamin Lock / Courtney John Lock vs Brian Bozemoj / Stijn Pel -- ATP Challenger Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 17:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-12T17:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12LOCLOCBOZPEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brian Bozemoj / Stijn Pel (`KXATPCHALLENGERDOUBLES-26NOV12LOCLOCBOZPEL-BOZPEL`) | 0.30 / 0.48 (61) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Benjamin Lock / Courtney John Lock (`KXATPCHALLENGERDOUBLES-26NOV12LOCLOCBOZPEL-LOCLOC`) | 0.40 / 0.59 (1) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lorenzo Musetti vs Ugo Humbert -- ATP Stockholm QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-12 21:40Z
* Current expected start: 2026-11-12 19:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-12 16:57Z
* Recommended handicap-by time: 2026-11-12 18:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-11-12T21:40:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200005:207518:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ugo Humbert (`KXATPMATCH-26NOV12MUSHUM-HUM`) | 0.35 / 0.36 (82) | 35.5% | 40.9% | 38.7% | 40.5% [36.4%-43.8%] | -- | 35.9% | 35.9% | MARKETS_AGREE | WATCH | +5.4 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Lorenzo Musetti (`KXATPMATCH-26NOV12MUSHUM-MUS`) | 0.64 / 0.65 (164637) | 64.5% | 59.1% | 61.3% | 59.5% [56.2%-63.6%] | -- | 64.5% | 64.5% | MARKETS_AGREE | PASS | -5.4 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5369.0, B 4987.0; serve-point win A 68.6%, B 33.3%; Elo A 1960.9, B 1937.2; model uncertainty 0.0372
* Form inputs: days since last match A 2, B 3; matches on record A 494, B 628; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.037, surface_pool_high -0.033, surface_dev_loose -0.000, surface_dev_tight +0.001
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV12MUSHUM-23` Over 22.5 games: 0.50/0.51 mid 50.5%, model 65.6% (projection_v2.0 (prediction ledger)) -- gap +15.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV12MUSHUM-MUS4` Will Lorenzo Musetti win at least 3.5 more games than Ugo Humbert?: 0.40/0.41 mid 40.5%, model 28.8% (projection_v2.0 (prediction ledger)) -- gap -11.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV12MUSHUM-28` Over 27.5 games: 0.32/0.34 mid 33.0%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap +11.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV12MUSHUM-MUS20` Will Lorenzo Musetti win the Lorenzo Musetti vs Ugo Humbert match by a set score of 2-0?: 0.40/0.42 mid 41.0%, model 31.4% (projection_v2.0 (prediction ledger)) -- gap -9.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV12MUSHUM-18` Over 17.5 games: 0.86/0.89 mid 87.5%, model 96.4% (projection_v2.0 (prediction ledger)) -- gap +8.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV12MUSHUM-MUS7` Will Lorenzo Musetti win at least 6.5 more games than Ugo Humbert?: 0.08/0.13 mid 10.5%, model 3.2% (projection_v2.0 (prediction ledger)) -- gap -7.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV12MUSHUM-HUM21` Will Ugo Humbert win the Lorenzo Musetti vs Ugo Humbert match by a set score of 2-1?: 0.15/0.16 mid 15.5%, model 21.6% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV12MUSHUM-2-HUM` Will Ugo Humbert win set 2 in the Lorenzo Musetti vs Ugo Humbert match: 0.38/0.40 mid 39.0%, model 43.9% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV12MUSHUM-MUS21` Will Lorenzo Musetti win the Lorenzo Musetti vs Ugo Humbert match by a set score of 2-1?: 0.22/0.24 mid 23.0%, model 27.6% (projection_v2.0 (prediction ledger)) -- gap +4.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV12MUSHUM-1-HUM` Will Ugo Humbert win set 1 in the Lorenzo Musetti vs Ugo Humbert match: 0.39/0.41 mid 40.0%, model 43.9% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV12MUSHUM-2-MUS` Will Lorenzo Musetti win set 2 in the Lorenzo Musetti vs Ugo Humbert match: 0.59/0.61 mid 60.0%, model 56.1% (projection_v2.0 (prediction ledger)) -- gap -3.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV12MUSHUM-1-MUS` Will Lorenzo Musetti win set 1 in the Lorenzo Musetti vs Ugo Humbert match: 0.58/0.60 mid 59.0%, model 56.1% (projection_v2.0 (prediction ledger)) -- gap -2.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV12MUSHUM-HUM2` Will Ugo Humbert win at least 1.5 more games than Lorenzo Musetti?: 0.30/0.32 mid 31.0%, model 32.9% (projection_v2.0 (prediction ledger)) -- gap +1.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV12MUSHUM-HUM20` Will Ugo Humbert win the Lorenzo Musetti vs Ugo Humbert match by a set score of 2-0?: 0.18/0.20 mid 19.0%, model 19.3% (projection_v2.0 (prediction ledger)) -- gap +0.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE

## Nicolas Barrientos / Juan Sebastian Gomez vs Boris Arias / Ignacio Carou -- ATP Challenger Lima QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-12T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12BARGOMARICAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Boris Arias / Ignacio Carou (`KXATPCHALLENGERDOUBLES-26NOV12BARGOMARICAR-ARICAR`) | 0.35 / 0.36 (4725) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nicolas Barrientos / Juan Sebastian Gomez (`KXATPCHALLENGERDOUBLES-26NOV12BARGOMARICAR-BARGOM`) | 0.64 / 0.65 (708) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Ozan Baris vs Michael Zheng -- ATP Challenger Knoxville R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-12T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210028:210116:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ozan Baris (`KXATPCHALLENGERMATCH-26NOV12BARZHE-BAR`) | 0.07 / 0.08 (85817) | 7.5% | 12.4% | 14.3% | 12.7% [11.6%-14.0%] | -- | 27.4% | 27.4% | MODEL_LONE_OUTLIER | PASS | +4.9 pp | NORMAL | FRESH | B / ADEQUATE | EXTERNAL_OUTLIER | VERIFIED |
| Michael Zheng (`KXATPCHALLENGERMATCH-26NOV12BARZHE-ZHE`) | 0.92 / 0.93 (96532) | 92.5% | 87.6% | 85.7% | 87.4% [86.0%-88.4%] | -- | 73.0% | 73.0% | MODEL_LONE_OUTLIER | SHADOW_BET | -4.9 pp | NORMAL | FRESH | B / ADEQUATE | EXTERNAL_OUTLIER | VERIFIED |

* Serve evidence (points): A 1236.0, B 3352.0; serve-point win A 56.1%, B 34.8%; Elo A 1405.9, B 1755.6; model uncertainty 0.0121
* Form inputs: days since last match A 17, B 10; matches on record A 93, B 142; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.014, surface_dev_loose -0.005, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Giles Hussey / Harry Wendelken vs Trey Hilderbrand / Bogdan Pavel -- ATP Challenger Knoxville QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-12T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12HUSWENHILPAV:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Trey Hilderbrand / Bogdan Pavel (`KXATPCHALLENGERDOUBLES-26NOV12HUSWENHILPAV-HILPAV`) | 0.43 / 0.51 (84) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Giles Hussey / Harry Wendelken (`KXATPCHALLENGERDOUBLES-26NOV12HUSWENHILPAV-HUSWEN`) | 0.48 / 0.54 (43) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Alan Magadan vs Alex Barrena -- ATP Challenger Lima R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-12T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209246:209875:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex Barrena (`KXATPCHALLENGERMATCH-26NOV12MAGBAR-BAR`) | 0.89 / 0.90 (301) | 89.5% | 77.6% | 72.2% | 76.4% [74.4%-78.0%] | -- | 76.7% | 76.7% | MODEL_LONE_OUTLIER | PASS | -11.9 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Alan Magadan (`KXATPCHALLENGERMATCH-26NOV12MAGBAR-MAG`) | 0.10 / 0.11 (496) | 10.5% | 22.4% | 27.8% | 23.6% [22.0%-25.6%] | -- | 23.9% | 23.9% | MODEL_LONE_OUTLIER | PASS | +11.9 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 2107.0, B 4752.0; serve-point win A 55.2%, B 39.0%; Elo A 1361.6, B 1618.4; model uncertainty 0.0182
* Form inputs: days since last match A 10, B 17; matches on record A 86, B 339; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.016, surface_dev_loose -0.001, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Aunion Duran / Palomar vs Garcia Longo / Miletich -- M15 Las Palmas de Gran Canaria QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 19:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12AUNPALGARMIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aunion Duran / Palomar (`KXITFDOUBLES-26NOV12AUNPALGARMIL-AUNPAL`) | 0.16 / 0.90 (0) | 53.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Garcia Longo / Miletich (`KXITFDOUBLES-26NOV12AUNPALGARMIL-GARMIL`) | 0.06 / 0.79 (2) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Cordoba / Fita Juan vs Naharro / Pujol Navarro -- M15 Las Palmas de Gran Canaria QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 19:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12CORFITNAHPUJ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cordoba / Fita Juan (`KXITFDOUBLES-26NOV12CORFITNAHPUJ-CORFIT`) | 0.06 / 0.64 (1) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Naharro / Pujol Navarro (`KXITFDOUBLES-26NOV12CORFITNAHPUJ-NAHPUJ`) | 0.30 / 0.92 (2) | 61.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Gonzalez-Galino / Ponce de leon gomila vs Barroso Campos / Schiavone -- M15 Las Palmas de Gran Canaria QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 19:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12GONPONBARSCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barroso Campos / Schiavone (`KXITFDOUBLES-26NOV12GONPONBARSCH-BARSCH`) | 0.04 / 0.64 (1) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gonzalez-Galino / Ponce de leon gomila (`KXITFDOUBLES-26NOV12GONPONBARSCH-GONPON`) | 0.29 / 0.94 (1) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Rojas / Vega Hernandez vs Arce Fernandez / Belda -- M15 Las Palmas de Gran Canaria QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 19:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12ROJVEGARCBEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arce Fernandez / Belda (`KXITFDOUBLES-26NOV12ROJVEGARCBEL-ARCBEL`) | 0.04 / 0.79 (2) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rojas / Vega Hernandez (`KXITFDOUBLES-26NOV12ROJVEGARCBEL-ROJVEG`) | 0.15 / 0.90 (0) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Fontenel / Vogt vs Nesmianovych / Gabriela Vasilescu -- W15 Paris SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12FONVOGNESGAB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fontenel / Vogt (`KXITFWDOUBLES-26NOV12FONVOGNESGAB-FONVOG`) | 0.26 / 0.87 (1) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nesmianovych / Gabriela Vasilescu (`KXITFWDOUBLES-26NOV12FONVOGNESGAB-NESGAB`) | 0.09 / 0.69 (1) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Marta Kostyuk vs Coco Gauff -- WTA Finals Women Singles Group A

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-12 23:00Z
* Current expected start: 2026-11-12 20:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-12 16:57Z
* Recommended handicap-by time: 2026-11-12 19:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

WTA (TOUR_FINALS) · Hard · scheduled 2026-11-12T23:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:216146:221103:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Coco Gauff (`KXWTAMATCH-26NOV12KOSGAU-GAU`) | 0.74 / 0.75 (3113) | 74.5% | 65.4% | 55.3% | 59.0% [57.4%-64.0%] | -- | 74.7% | 74.7% | MODEL_LONE_OUTLIER | PASS | -9.1 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Marta Kostyuk (`KXWTAMATCH-26NOV12KOSGAU-KOS`) | 0.25 / 0.26 (180247) | 25.5% | 34.6% | 44.7% | 41.0% [36.0%-42.6%] | -- | 25.2% | 25.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +9.1 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4067.0, B 5157.0; serve-point win A 53.3%, B 43.7%; Elo A 2056.8, B 2195.6; model uncertainty 0.0332
* Form inputs: days since last match A 2, B 2; matches on record A 434, B 448; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.005, surface_dev_loose +0.010, surface_dev_tight -0.016
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV12KOSGAU-20` Over 19.5 games: 0.55/0.56 mid 55.5%, model 71.4% (projection_v2.0 (prediction ledger)) -- gap +15.9 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV12KOSGAU-25` Over 24.5 games: 0.32/0.34 mid 33.0%, model 46.5% (projection_v2.0 (prediction ledger)) -- gap +13.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV12KOSGAU-2-KOS` Will Marta Kostyuk win set 2 in the Marta Kostyuk vs Coco Gauff match: 0.27/0.30 mid 28.5%, model 39.6% (projection_v2.0 (prediction ledger)) -- gap +11.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV12KOSGAU-1-KOS` Will Marta Kostyuk win set 1 in the Marta Kostyuk vs Coco Gauff match: 0.29/0.31 mid 30.0%, model 39.6% (projection_v2.0 (prediction ledger)) -- gap +9.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV12KOSGAU-1-GAU` Will Coco Gauff win set 1 in the Marta Kostyuk vs Coco Gauff match: 0.69/0.70 mid 69.5%, model 60.4% (projection_v2.0 (prediction ledger)) -- gap -9.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV12KOSGAU-2-GAU` Will Coco Gauff win set 2 in the Marta Kostyuk vs Coco Gauff match: 0.68/0.69 mid 68.5%, model 60.4% (projection_v2.0 (prediction ledger)) -- gap -8.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26NOV12KOSGAU-15` Over 14.5 games: 0.91/0.95 mid 93.0%, model 98.7% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE

## Sofia Meabe vs Luisa Meyer auf der Heide -- W15 São Carlos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220053:266446:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Meabe (`KXITFWMATCH-26NOV12MEAMEY-MEA`) | 0.49 / 0.50 (212) | 49.5% | 22.4% | 15.2% | 28.3% [24.8%-30.6%] | 27.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -27.1 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luisa Meyer auf der Heide (`KXITFWMATCH-26NOV12MEAMEY-MEY`) | 0.49 / 0.50 (5305) | 49.5% | 77.6% | 84.8% | 71.7% [69.4%-75.2%] | 72.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +28.1 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 235.0, B 1401.0; serve-point win A 51.0%, B 43.3%; Elo A 1346.8, B 1491.4; model uncertainty 0.0293
* Form inputs: days since last match A 297, B 241; matches on record A 18, B 252; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV12MEAMEY-MEY  (YES = Luisa Meyer auf der Heide)
Model: 78%
Kalshi: 50%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.018, surface_pool_high +0.005, surface_dev_loose -0.009, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stefan Kozlov vs Braden Shick -- ATP Challenger Knoxville R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 20:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-12T20:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111578:211711:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefan Kozlov (`KXATPCHALLENGERMATCH-26NOV12KOZSHI-KOZ`) | 0.68 / 0.69 (25082) | 68.5% | 60.5% | 55.2% | 56.7% [55.2%-59.7%] | -- | 67.4% | 67.4% | MODEL_LONE_OUTLIER | PASS | -8.0 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Braden Shick (`KXATPCHALLENGERMATCH-26NOV12KOZSHI-SHI`) | 0.31 / 0.32 (1000) | 31.5% | 39.5% | 44.8% | 43.3% [40.3%-44.8%] | -- | 31.7% | 31.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +8.0 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3794.0, B 3074.0; serve-point win A 60.7%, B 41.3%; Elo A 1616.3, B 1547.1; model uncertainty 0.0227
* Form inputs: days since last match A 10, B 10; matches on record A 624, B 102; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.015, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Johan Nikles / Carlos Sanchez Jover vs Facundo Bagnis / Facundo Mena -- ATP Challenger Lima QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 20:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-12T20:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12NIKSANBAGMEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Facundo Bagnis / Facundo Mena (`KXATPCHALLENGERDOUBLES-26NOV12NIKSANBAGMEN-BAGMEN`) | 0.60 / 0.67 (200) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Johan Nikles / Carlos Sanchez Jover (`KXATPCHALLENGERDOUBLES-26NOV12NIKSANBAGMEN-NIKSAN`) | 0.30 / 0.36 (43) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Franco Roncadelli vs Francisco Comesana -- ATP Challenger Lima R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 20:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-12T20:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207681:208364:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francisco Comesana (`KXATPCHALLENGERMATCH-26NOV12RONCOM-COM`) | 0.78 / 0.79 (12492) | 78.5% | 74.4% | 59.8% | 64.3% [62.3%-69.0%] | -- | 78.5% | 78.5% | MODEL_LONE_OUTLIER | PASS | -4.1 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Franco Roncadelli (`KXATPCHALLENGERMATCH-26NOV12RONCOM-RON`) | 0.21 / 0.22 (10) | 21.5% | 25.6% | 40.2% | 35.7% [31.0%-37.7%] | -- | 21.9% | 21.9% | MODEL_LONE_OUTLIER | SHADOW_BET | +4.1 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4282.0, B 5187.0; serve-point win A 55.9%, B 39.1%; Elo A 1578.4, B 1795.1; model uncertainty 0.0335
* Form inputs: days since last match A 10, B 10; matches on record A 326, B 466; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Andres Andrade / Johannes Ingildsen vs Oscar Lacides / Shunsuke Mitsui -- ATP Challenger Knoxville QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-12T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12ANDINGLACMIT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andres Andrade / Johannes Ingildsen (`KXATPCHALLENGERDOUBLES-26NOV12ANDINGLACMIT-ANDING`) | 0.51 / 0.54 (29) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Oscar Lacides / Shunsuke Mitsui (`KXATPCHALLENGERDOUBLES-26NOV12ANDINGLACMIT-LACMIT`) | 0.40 / 0.47 (44) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Joaquim Almeida vs Felix Corwin -- M15 Naples FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200228:212760:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joaquim Almeida (`KXITFMATCH-26NOV12ALMCOR-ALM`) | 0.51 / 0.52 (511) | 51.5% | 20.3% | 17.1% | 25.4% [23.8%-27.2%] | -- | -- | -- | -- | PASS | -31.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Felix Corwin (`KXITFMATCH-26NOV12ALMCOR-COR`) | 0.48 / 0.49 (463) | 48.5% | 79.7% | 82.9% | 74.6% [72.8%-76.2%] | -- | -- | -- | -- | PASS | +31.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 86.0, B 3058.0; serve-point win A 53.5%, B 40.2%; Elo A 1204.8, B 1386.5; model uncertainty 0.0169
* Form inputs: days since last match A 759, B 213; matches on record A 15, B 371; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV12ALMCOR-COR  (YES = Felix Corwin)
Model: 80%
Kalshi: 48%
Gap: +31 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.017, surface_pool_high +0.017, surface_dev_loose -0.001, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Justin Riley Anson vs Ryan Colby -- M15 Naples FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12ANSCOL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Justin Riley Anson (`KXITFMATCH-26NOV12ANSCOL-ANS`) | 0.21 / 0.22 (2190) | 21.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ryan Colby (`KXITFMATCH-26NOV12ANSCOL-COL`) | 0.78 / 0.79 (2218) | 78.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sebastian Baez vs Calvin Hemery -- ATP Challenger Orleans R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-12T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:123921:202104:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sebastian Baez (`KXATPCHALLENGERMATCH-26NOV12BAEHEM-BAE`) | 0.73 / 0.75 (3233) | 74.0% | 73.1% | 56.0% | 60.0% [58.0%-63.9%] | -- | 73.8% | 73.8% | MODEL_LONE_OUTLIER | PASS | -0.9 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Calvin Hemery (`KXATPCHALLENGERMATCH-26NOV12BAEHEM-HEM`) | 0.25 / 0.26 (866) | 25.5% | 26.9% | 44.0% | 40.0% [36.1%-42.0%] | -- | 26.4% | 26.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +1.4 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5268.0, B 4976.0; serve-point win A 65.0%, B 39.9%; Elo A 1709.8, B 1549.6; model uncertainty 0.0292
* Form inputs: days since last match A 10, B 24; matches on record A 509, B 754; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Tobia Grandinetti vs Hernan Casanova -- M15 Roldan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106292:211634:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hernan Casanova (`KXITFMATCH-26NOV12GRACAS-CAS`) | 0.98 / 0.99 (10334) | 98.5% | 86.8% | 64.9% | 82.8% [81.6%-84.6%] | 94.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.7 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tobia Grandinetti (`KXITFMATCH-26NOV12GRACAS-GRA`) | 0.01 / 0.02 (5836) | 1.5% | 13.2% | 35.1% | 17.2% [15.4%-18.4%] | 5.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +11.7 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 160.0, B 3175.0; serve-point win A 52.7%, B 38.8%; Elo A 1265.5, B 1558.3; model uncertainty 0.0152
* Form inputs: days since last match A 360, B 10; matches on record A 5, B 814; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Emilio Sanchez Bronzetti vs Evan Bynoe -- M15 Naples FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208466:212056:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Evan Bynoe (`KXITFMATCH-26NOV12SANBYN-BYN`) | 0.86 / 0.87 (317) | 86.5% | 66.8% | 59.9% | 56.3% [55.2%-57.4%] | 78.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -19.7 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Emilio Sanchez Bronzetti (`KXITFMATCH-26NOV12SANBYN-SAN`) | 0.11 / 0.15 (46) | 13.0% | 33.2% | 40.1% | 43.7% [42.6%-44.8%] | 21.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +20.2 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 72.0, B 1821.0; serve-point win A 55.5%, B 41.2%; Elo A 1211.7, B 1255.3; model uncertainty 0.0105
* Form inputs: days since last match A 479, B 199; matches on record A 4, B 100; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV12SANBYN-SAN  (YES = Emilio Sanchez Bronzetti)
Model: 33%
Kalshi: 13%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jack Secord vs Santiago Giamichelle -- M15 Naples FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213761:213839:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Santiago Giamichelle (`KXITFMATCH-26NOV12SECGIA-GIA`) | 0.32 / 0.34 (929) | 33.0% | 24.6% | 42.7% | 32.2% [31.7%-33.1%] | 36.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jack Secord (`KXITFMATCH-26NOV12SECGIA-SEC`) | 0.66 / 0.67 (151) | 66.5% | 75.4% | 57.3% | 67.8% [66.9%-68.3%] | 63.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +8.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 173.0, B 263.0; serve-point win A 59.4%, B 45.9%; Elo A 1345.4, B 1209.3; model uncertainty 0.0071
* Form inputs: days since last match A 79, B 353; matches on record A 5, B 5; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.000, surface_dev_loose -0.004, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rocco Valente vs Lucio Ratti -- M15 Roldan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211636:212260:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucio Ratti (`KXITFMATCH-26NOV12VALRAT-RAT`) | 0.83 / 0.84 (17645) | 83.5% | 92.0% | 87.4% | 87.7% [86.0%-89.7%] | 89.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +8.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rocco Valente (`KXITFMATCH-26NOV12VALRAT-VAL`) | 0.16 / 0.17 (11847) | 16.5% | 8.0% | 12.6% | 12.3% [10.3%-14.0%] | 11.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 719.0, B 2663.0; serve-point win A 53.2%, B 36.0%; Elo A 1108.1, B 1449.8; model uncertainty 0.0186
* Form inputs: days since last match A 241, B 10; matches on record A 38, B 115; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Louis Wessels vs Theodore Dean -- M25 Montreal R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144923:213932:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theodore Dean (`KXITFMATCH-26NOV12WESDEA-DEA`) | 0.72 / 0.73 (22159) | 72.5% | 53.3% | 44.2% | 51.6% [48.4%-55.8%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -19.2 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Louis Wessels (`KXITFMATCH-26NOV12WESDEA-WES`) | 0.27 / 0.28 (26473) | 27.5% | 46.7% | 55.8% | 48.4% [44.2%-51.6%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +19.2 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2563.0, B 1263.0; serve-point win A 56.8%, B 42.5%; Elo A 1365.5, B 1424.3; model uncertainty 0.0367
* Form inputs: days since last match A 38, B 311; matches on record A 543, B 21; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV12WESDEA-WES  (YES = Louis Wessels)
Model: 47%
Kalshi: 28%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.032, surface_pool_high -0.042, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Filip Jeff Planinsek vs Alastair Gray -- ATP Challenger Knoxville R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 21:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-12T21:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202400:210731:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alastair Gray (`KXATPCHALLENGERMATCH-26NOV12PLAGRA-GRA`) | 0.72 / 0.73 (11537) | 72.5% | 75.5% | 75.5% | 75.9% [74.1%-76.6%] | -- | 71.5% | 71.5% | MARKETS_AGREE | SHADOW_BET | +3.0 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Filip Jeff Planinsek (`KXATPCHALLENGERMATCH-26NOV12PLAGRA-PLA`) | 0.27 / 0.28 (1121) | 27.5% | 24.5% | 24.5% | 24.1% [23.4%-25.9%] | -- | 28.8% | 28.8% | MARKETS_AGREE | PASS | -3.0 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 1932.0, B 3404.0; serve-point win A 62.4%, B 32.0%; Elo A 1383.3, B 1582.8; model uncertainty 0.0125
* Form inputs: days since last match A 55, B 10; matches on record A 102, B 328; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.004, surface_dev_loose -0.004, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Jessica Pegula vs Linda Noskova -- WTA Finals Women Singles Group A

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-13 00:10Z
* Current expected start: 2026-11-12 21:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-12 16:57Z
* Recommended handicap-by time: 2026-11-12 20:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN

WTA (TOUR_FINALS) · Hard · scheduled 2026-11-13T00:10:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202468:222328:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Linda Noskova (`KXWTAMATCH-26NOV12PEGNOS-NOS`) | 0.53 / 0.54 (4842) | 53.5% | 45.8% | 25.4% | 28.8% [27.1%-33.1%] | -- | -- | -- | -- | PASS | -7.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jessica Pegula (`KXWTAMATCH-26NOV12PEGNOS-PEG`) | 0.46 / 0.47 (93007) | 46.5% | 54.2% | 74.6% | 71.2% [66.9%-72.9%] | -- | -- | -- | -- | WATCH | +7.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5824.0, B 4568.0; serve-point win A 62.5%, B 38.3%; Elo A 2197.1, B 2113.0; model uncertainty 0.0298
* Form inputs: days since last match A 2, B 2; matches on record A 769, B 337; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high +0.000, surface_dev_loose +0.004, surface_dev_tight +0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV12PEGNOS-24` Over 23.5 games: 0.44/0.45 mid 44.5%, model 53.9% (projection_v2.0 (prediction ledger)) -- gap +9.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV12PEGNOS-29` Over 28.5 games: 0.25/0.26 mid 25.5%, model 34.2% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV12PEGNOS-19` Over 18.5 games: 0.77/0.80 mid 78.5%, model 86.5% (projection_v2.0 (prediction ledger)) -- gap +8.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV12PEGNOS-1-PEG` Will Jessica Pegula win set 1 in the Jessica Pegula vs Linda Noskova match: 0.45/0.46 mid 45.5%, model 52.8% (projection_v2.0 (prediction ledger)) -- gap +7.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV12PEGNOS-1-NOS` Will Linda Noskova win set 1 in the Jessica Pegula vs Linda Noskova match: 0.53/0.55 mid 54.0%, model 47.2% (projection_v2.0 (prediction ledger)) -- gap -6.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV12PEGNOS-2-PEG` Will Jessica Pegula win set 2 in the Jessica Pegula vs Linda Noskova match: 0.43/0.49 mid 46.0%, model 52.8% (projection_v2.0 (prediction ledger)) -- gap +6.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV12PEGNOS-2-NOS` Will Linda Noskova win set 2 in the Jessica Pegula vs Linda Noskova match: 0.50/0.54 mid 52.0%, model 47.2% (projection_v2.0 (prediction ledger)) -- gap -4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NO_EXTERNAL_PRICE

## Jarno Jans / Joran Vliegen vs Arda Azkara / Clement Chidekh -- ATP Challenger Knoxville QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 21:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-12T21:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12JANVLIAZKCHI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arda Azkara / Clement Chidekh (`KXATPCHALLENGERDOUBLES-26NOV12JANVLIAZKCHI-AZKCHI`) | 0.22 / 0.28 (28) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jarno Jans / Joran Vliegen (`KXATPCHALLENGERDOUBLES-26NOV12JANVLIAZKCHI-JANVLI`) | 0.68 / 0.75 (219) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Bruna / Dellien vs De Dios / Dreycopp -- M15 Roldan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12BRUDELDEDDRE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bruna / Dellien (`KXITFDOUBLES-26NOV12BRUDELDEDDRE-BRUDEL`) | 0.70 / 0.79 (230) | 74.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| De Dios / Dreycopp (`KXITFDOUBLES-26NOV12BRUDELDEDDRE-DEDDRE`) | 0.16 / 0.25 (225) | 20.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Dragos Cazacu vs Jerrid Gaines Jr -- M15 Naples FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12CAZGAI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dragos Cazacu (`KXITFMATCH-26NOV12CAZGAI-CAZ`) | 0.72 / 0.74 (250) | 73.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jerrid Gaines Jr (`KXITFMATCH-26NOV12CAZGAI-GAI`) | 0.25 / 0.27 (198) | 26.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Thomas Gerbaud vs Mikael Arseneault -- M25 Montreal R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212530:212840:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mikael Arseneault (`KXITFMATCH-26NOV12GERARS-ARS`) | 0.75 / 0.76 (4121) | 75.5% | 63.5% | 62.8% | 56.0% [54.1%-59.3%] | 80.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.0 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Thomas Gerbaud (`KXITFMATCH-26NOV12GERARS-GER`) | 0.24 / 0.25 (4617) | 24.5% | 36.5% | 37.2% | 44.0% [40.7%-45.9%] | 19.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +12.0 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 568.0, B 759.0; serve-point win A 62.1%, B 35.1%; Elo A 1226.2, B 1251.9; model uncertainty 0.0263
* Form inputs: days since last match A 248, B 115; matches on record A 19, B 33; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.009, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gavin Goode vs Youcef Rihane -- M15 Naples FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209065:213836:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gavin Goode (`KXITFMATCH-26NOV12GOORIH-GOO`) | 0.45 / 0.47 (67) | 46.0% | 71.9% | 35.9% | 67.9% [67.0%-67.9%] | 52.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +25.9 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Youcef Rihane (`KXITFMATCH-26NOV12GOORIH-RIH`) | 0.52 / 0.55 (351) | 53.5% | 28.1% | 64.1% | 32.1% [32.1%-33.0%] | 47.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -25.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 444.0, B 0.0; serve-point win A 62.2%, B 42.3%; Elo A 1320.1, B 1191.5; model uncertainty 0.0047
* Form inputs: days since last match A 199, B 1116; matches on record A 10, B 17; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV12GOORIH-GOO  (YES = Gavin Goode)
Model: 72%
Kalshi: 46%
Gap: +26 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.009, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cannon Kingsley vs Axel Nefve -- M25 Montreal R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207992:208051:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cannon Kingsley (`KXITFMATCH-26NOV12KINNEF-KIN`) | 0.72 / 0.73 (3004) | 72.5% | 80.8% | 84.3% | 82.7% [77.7%-84.3%] | 82.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +8.2 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Axel Nefve (`KXITFMATCH-26NOV12KINNEF-NEF`) | 0.27 / 0.28 (13020) | 27.5% | 19.2% | 15.7% | 17.3% [15.7%-22.3%] | 17.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.2 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3872.0, B 2734.0; serve-point win A 63.5%, B 43.3%; Elo A 1530.7, B 1297.1; model uncertainty 0.0329
* Form inputs: days since last match A 213, B 227; matches on record A 253, B 148; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high -0.000, surface_dev_loose +0.003, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Victor Lilov vs Nikita Filin -- M25 Columbus OH R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210098:212570:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikita Filin (`KXITFMATCH-26NOV12LILFIL-FIL`) | 0.73 / 0.76 (95) | 74.5% | 28.6% | 58.7% | 34.4% [30.3%-39.3%] | -- | -- | -- | -- | PASS | -45.9 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Victor Lilov (`KXITFMATCH-26NOV12LILFIL-LIL`) | 0.23 / 0.27 (93) | 25.0% | 71.4% | 41.3% | 65.6% [60.7%-69.7%] | -- | -- | -- | -- | PASS | +46.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2261.0, B 201.0; serve-point win A 62.3%, B 42.0%; Elo A 1341.9, B 1207.6; model uncertainty 0.0452
* Form inputs: days since last match A 339, B 367; matches on record A 196, B 12; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV12LILFIL-LIL  (YES = Victor Lilov)
Model: 71%
Kalshi: 25%
Gap: +46 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.014, surface_dev_loose -0.001, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lucca Liu vs Fadi Bidan -- M15 Naples FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:149266:213175:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fadi Bidan (`KXITFMATCH-26NOV12LIUBID-BID`) | 0.28 / 0.29 (107) | 28.5% | 40.7% | 20.5% | 38.6% [32.7%-45.3%] | 31.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +12.2 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lucca Liu (`KXITFMATCH-26NOV12LIUBID-LIU`) | 0.69 / 0.72 (504) | 70.5% | 59.3% | 79.5% | 61.4% [54.7%-67.3%] | 68.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.2 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 620.0, B 919.0; serve-point win A 58.9%, B 42.9%; Elo A 1280.2, B 1258.8; model uncertainty 0.063
* Form inputs: days since last match A 241, B 346; matches on record A 16, B 50; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vladislav Melnic vs Nicolas Arseneault -- M25 Montreal R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207331:212531:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Arseneault (`KXITFMATCH-26NOV12MELARS-ARS`) | 0.86 / 0.88 (1513) | 87.0% | 75.5% | 65.8% | 71.1% [69.4%-73.4%] | 86.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.5 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Vladislav Melnic (`KXITFMATCH-26NOV12MELARS-MEL`) | 0.12 / 0.14 (919) | 13.0% | 24.5% | 34.2% | 28.9% [26.6%-30.6%] | 13.3% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +11.5 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1486.0, B 1460.0; serve-point win A 59.6%, B 34.9%; Elo A 1225.1, B 1424.6; model uncertainty 0.0202
* Form inputs: days since last match A 213, B 115; matches on record A 80, B 59; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.004, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexander Okonkwo vs Theo Papamalamis -- M25 Columbus OH R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12OKOPAP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Okonkwo (`KXITFMATCH-26NOV12OKOPAP-OKO`) | 0.42 / 0.43 (1189) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Theo Papamalamis (`KXITFMATCH-26NOV12OKOPAP-PAP`) | 0.57 / 0.58 (4768) | 57.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bruno (2002) Oliveira / Natan Rodrigues vs Karol Drzewiecki / Piotr Matuszewski -- ATP Challenger Lima QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-12T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12OLIRODDRZMAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karol Drzewiecki / Piotr Matuszewski (`KXATPCHALLENGERDOUBLES-26NOV12OLIRODDRZMAT-DRZMAT`) | 0.62 / 0.71 (228) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bruno (2002) Oliveira / Natan Rodrigues (`KXATPCHALLENGERDOUBLES-26NOV12OLIRODDRZMAT-OLIROD`) | 0.26 / 0.31 (29) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Denis Petak vs Matthew Forbes -- M25 Columbus OH R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212084:212733:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthew Forbes (`KXITFMATCH-26NOV12PETFOR-FOR`) | 0.87 / 0.88 (1343) | 87.5% | 81.5% | 78.9% | 73.5% [70.3%-75.7%] | 68.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.0 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Denis Petak (`KXITFMATCH-26NOV12PETFOR-PET`) | 0.12 / 0.13 (12466) | 12.5% | 18.4% | 21.1% | 26.6% [24.3%-29.7%] | 31.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.0 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1339.0, B 594.0; serve-point win A 59.9%, B 32.9%; Elo A 1204.0, B 1361.1; model uncertainty 0.027
* Form inputs: days since last match A 262, B 80; matches on record A 42, B 18; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.011, surface_dev_tight +0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zsombor Velcz vs Tomas Jirousek -- M15 Naples FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207844:209852:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tomas Jirousek (`KXITFMATCH-26NOV12VELJIR-JIR`) | 0.40 / 0.43 (337) | 41.5% | 36.8% | 50.0% | 40.8% [39.8%-42.8%] | 40.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.7 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Zsombor Velcz (`KXITFMATCH-26NOV12VELJIR-VEL`) | 0.56 / 0.60 (469) | 58.0% | 63.2% | 50.0% | 59.2% [57.2%-60.2%] | 59.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 419.0, B 0.0; serve-point win A 61.2%, B 41.4%; Elo A 1321.3, B 1259.6; model uncertainty 0.0151
* Form inputs: days since last match A 381, B 1179; matches on record A 67, B 95; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.020, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Max Wiskandt vs Joshua Peck -- M25 Montreal R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200234:208328:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joshua Peck (`KXITFMATCH-26NOV12WISPEC-PEC`) | 0.02 / 0.03 (12859) | 2.5% | 13.9% | 20.3% | 17.2% [15.9%-18.9%] | 13.3% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +11.4 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Max Wiskandt (`KXITFMATCH-26NOV12WISPEC-WIS`) | 0.97 / 0.98 (2423) | 97.5% | 86.1% | 79.7% | 82.8% [81.2%-84.1%] | 86.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.4 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3286.0, B 1103.0; serve-point win A 65.4%, B 43.1%; Elo A 1451.5, B 1149.6; model uncertainty 0.0147
* Form inputs: days since last match A 31, B 199; matches on record A 237, B 78; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high +0.000, surface_dev_loose +0.006, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nishesh Basavareddy vs Kyrian Jacquet -- ATP Challenger Orleans R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 22:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-12T22:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208021:210460:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nishesh Basavareddy (`KXATPCHALLENGERMATCH-26NOV12BASJAC-BAS`) | 0.54 / 0.55 (2308) | 54.5% | 56.0% | 57.4% | 57.0% [53.0%-58.4%] | -- | 53.8% | 53.8% | MARKETS_AGREE | PASS | +1.5 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Kyrian Jacquet (`KXATPCHALLENGERMATCH-26NOV12BASJAC-JAC`) | 0.45 / 0.46 (6967) | 45.5% | 44.0% | 42.6% | 43.0% [41.6%-47.0%] | -- | 45.7% | 45.7% | MARKETS_AGREE | PASS | -1.5 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4072.0, B 4370.0; serve-point win A 64.4%, B 36.8%; Elo A 1806.7, B 1774.4; model uncertainty 0.0271
* Form inputs: days since last match A 10, B 10; matches on record A 189, B 416; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.015, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Pedro Albuquerque Dietrich vs Eduardo Ribeiro -- M25 Santa Cruz do Sul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200495:214226:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pedro Albuquerque Dietrich (`KXITFMATCH-26NOV12ALBRIB-ALB`) | 0.01 / 0.02 (7234) | 1.5% | 13.6% | 18.9% | 19.5% [18.7%-20.4%] | -- | -- | -- | -- | PASS | +12.1 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Eduardo Ribeiro (`KXITFMATCH-26NOV12ALBRIB-RIB`) | 0.98 / 0.99 (5654) | 98.5% | 86.4% | 81.2% | 80.5% [79.6%-81.3%] | -- | -- | -- | -- | PASS | -12.1 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 53.0, B 3426.0; serve-point win A 55.0%, B 36.5%; Elo A 1284.9, B 1528.0; model uncertainty 0.0084
* Form inputs: days since last match A 381, B 10; matches on record A 1, B 307; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.007, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Juan Pablo Ficovich vs Kaue Noatto -- M25 Santa Cruz do Sul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126663:213613:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Pablo Ficovich (`KXITFMATCH-26NOV12FICNOA-FIC`) | 0.88 / 0.91 (308) | 89.5% | 96.2% | 86.0% | 89.9% [89.7%-90.7%] | -- | -- | -- | -- | PASS | +6.7 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kaue Noatto (`KXITFMATCH-26NOV12FICNOA-NOA`) | 0.09 / 0.11 (65) | 10.0% | 3.8% | 14.0% | 10.1% [9.3%-10.3%] | -- | -- | -- | -- | PASS | -6.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4225.0, B 89.0; serve-point win A 67.1%, B 46.7%; Elo A 1582.5, B 1194.2; model uncertainty 0.0049
* Form inputs: days since last match A 10, B 297; matches on record A 726, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.000, surface_dev_loose +0.002, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Victoria Bosio vs Giulia Gomes Ferreira -- W15 São Carlos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206345:267384:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Victoria Bosio (`KXITFWMATCH-26NOV12BOSGOM-BOS`) | 0.98 / 0.99 (567) | 98.5% | 96.4% | 91.3% | 87.4% [87.4%-87.4%] | -- | -- | -- | -- | PASS | -2.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Giulia Gomes Ferreira (`KXITFWMATCH-26NOV12BOSGOM-GOM`) | 0.01 / 0.02 (11198) | 1.5% | 3.6% | 8.7% | 12.6% [12.6%-12.6%] | -- | -- | -- | -- | PASS | +2.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 3098.0, B 0.0; serve-point win A 60.6%, B 52.9%; Elo A 1566.7, B 1230.0; model uncertainty 0.0
* Form inputs: days since last match A 17, B 892; matches on record A 565, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luna Maria Cinalli vs Lan Mi -- W15 São Carlos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260141:260711:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luna Maria Cinalli (`KXITFWMATCH-26NOV12CINMIX-CIN`) | 0.60 / 0.68 (46) | 64.0% | 43.8% | 39.9% | 45.2% [43.6%-46.8%] | 65.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -20.2 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lan Mi (`KXITFWMATCH-26NOV12CINMIX-MIX`) | 0.30 / 0.38 (4) | 34.0% | 56.2% | 60.1% | 54.8% [53.2%-56.4%] | 34.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +22.2 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 795.0, B 2699.0; serve-point win A 50.3%, B 48.5%; Elo A 1401.9, B 1413.1; model uncertainty 0.016
* Form inputs: days since last match A 15, B 16; matches on record A 36, B 90; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV12CINMIX-MIX  (YES = Lan Mi)
Model: 56%
Kalshi: 34%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.005, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dias / Garcia Vidal vs Gomes / Melleiro -- W15 São Carlos QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12DIAGARGOMMEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dias / Garcia Vidal (`KXITFWDOUBLES-26NOV12DIAGARGOMMEL-DIAGAR`) | 0.84 / 0.89 (512) | 86.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gomes / Melleiro (`KXITFWDOUBLES-26NOV12DIAGARGOMMEL-GOMMEL`) | 0.10 / 0.16 (633) | 13.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Dasha Ivanova vs Ava Catanzarite -- W35 Weston FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214007:260303:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ava Catanzarite (`KXITFWMATCH-26NOV12IVACAT-CAT`) | 0.19 / 0.20 (8087) | 19.5% | 25.8% | 50.0% | 36.5% [32.5%-40.6%] | 44.8% | -- | 44.8% | MODEL_LONE_OUTLIER | PASS | +6.3 pp | NORMAL | FRESH | F / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Dasha Ivanova (`KXITFWMATCH-26NOV12IVACAT-IVA`) | 0.80 / 0.81 (411) | 80.5% | 74.2% | 50.0% | 63.5% [59.5%-67.5%] | 55.2% | -- | 55.2% | MODEL_LONE_OUTLIER | PASS | -6.3 pp | NORMAL | FRESH | F / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 2204.0, B 106.0; serve-point win A 57.5%, B 47.3%; Elo A 1377.3, B 1276.9; model uncertainty 0.0402
* Form inputs: days since last match A 199, B 241; matches on record A 503, B 12; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.030, surface_pool_high -0.041, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Michaela Laki vs Julia Adams -- W35 Weston FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223129:266450:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julia Adams (`KXITFWMATCH-26NOV12LAKADA-ADA`) | 0.36 / 0.37 (11297) | 36.5% | 39.4% | 56.4% | 36.4% [32.5%-42.6%] | 59.9% | -- | 59.9% | MODEL_LONE_OUTLIER | PASS | +2.9 pp | NORMAL | FRESH | F / POOR | EXTERNAL_OUTLIER | VERIFIED |
| Michaela Laki (`KXITFWMATCH-26NOV12LAKADA-LAK`) | 0.63 / 0.64 (3841) | 63.5% | 60.6% | 43.6% | 63.6% [57.4%-67.5%] | 40.1% | -- | 40.1% | MODEL_LONE_OUTLIER | PASS | -2.9 pp | NORMAL | FRESH | F / POOR | EXTERNAL_OUTLIER | VERIFIED |

* Serve evidence (points): A 97.0, B 2996.0; serve-point win A 55.0%, B 47.0%; Elo A 1491.6, B 1390.9; model uncertainty 0.0505
* Form inputs: days since last match A 612, B 199; matches on record A 205, B 163; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.062, surface_pool_high +0.039, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dasha Plekhanova vs Salma Djoubri -- W35 Weston FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220305:223203:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Salma Djoubri (`KXITFWMATCH-26NOV12PLEDJO-DJO`) | 0.83 / 0.85 (108) | 84.0% | 33.9% | 21.9% | 38.4% [33.9%-42.6%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -50.1 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dasha Plekhanova (`KXITFWMATCH-26NOV12PLEDJO-PLE`) | 0.15 / 0.17 (36) | 16.0% | 66.1% | 78.1% | 61.6% [57.4%-66.1%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +50.1 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 907.0, B 169.0; serve-point win A 55.0%, B 48.0%; Elo A 1522.2, B 1456.4; model uncertainty 0.0433
* Form inputs: days since last match A 17, B 360; matches on record A 87, B 168; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV12PLEDJO-PLE  (YES = Dasha Plekhanova)
Model: 66%
Kalshi: 16%
Gap: +50 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.020, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anita Sahdiieva vs Capucine Jauffret -- W35 Weston FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221370:263981:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Capucine Jauffret (`KXITFWMATCH-26NOV12SAHJAU-JAU`) | 0.30 / 0.31 (12616) | 30.5% | 48.4% | 63.1% | 52.7% [46.8%-56.9%] | 64.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +17.9 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anita Sahdiieva (`KXITFWMATCH-26NOV12SAHJAU-SAH`) | 0.69 / 0.70 (8261) | 69.5% | 51.6% | 36.9% | 47.3% [43.1%-53.2%] | 35.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -17.9 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1325.0, B 767.0; serve-point win A 53.0%, B 47.3%; Elo A 1381.5, B 1362.5; model uncertainty 0.0506
* Form inputs: days since last match A 199, B 78; matches on record A 111, B 24; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV12SAHJAU-JAU  (YES = Capucine Jauffret)
Model: 48%
Kalshi: 30%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose -0.016, surface_dev_tight +0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Katerina Siniakova / Taylor Townsend vs Cristina Bucsa / Nicole Melichar-Martinez -- WTA Finals Women Doubles Group

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-13 01:20Z
* Current expected start: 2026-11-12 23:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-12 16:57Z
* Recommended handicap-by time: 2026-11-12 22:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_FINALS) · surface ? · scheduled 2026-11-13T01:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12SINTOWBUCMEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cristina Bucsa / Nicole Melichar-Martinez (`KXWTADOUBLES-26NOV12SINTOWBUCMEL-BUCMEL`) | 0.21 / 0.24 (401) | 22.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Katerina Siniakova / Taylor Townsend (`KXWTADOUBLES-26NOV12SINTOWBUCMEL-SINTOW`) | 0.76 / 0.77 (631) | 76.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Bor Artnak vs Emanuel Ivanisevic -- M25 Columbus OH R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210107:212924:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bor Artnak (`KXITFMATCH-26NOV12ARTIVA-ART`) | 0.78 / 0.80 (18) | 79.0% | 86.2% | 89.6% | 83.8% [80.5%-87.1%] | 78.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.2 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Emanuel Ivanisevic (`KXITFMATCH-26NOV12ARTIVA-IVA`) | 0.20 / 0.21 (650) | 20.5% | 13.8% | 10.4% | 16.2% [13.0%-19.4%] | 21.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3186.0, B 679.0; serve-point win A 61.8%, B 46.5%; Elo A 1469.8, B 1224.5; model uncertainty 0.0325
* Form inputs: days since last match A 55, B 185; matches on record A 251, B 19; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.006, surface_pool_high -0.006, surface_dev_loose +0.013, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Brostrom Poulsen / Slavic vs Thomas George / Nicholas Tudorica -- M25 Montreal QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12BROSLATHONIC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brostrom Poulsen / Slavic (`KXITFDOUBLES-26NOV12BROSLATHONIC-BROSLA`) | 0.84 / 0.90 (17) | 87.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Thomas George / Nicholas Tudorica (`KXITFDOUBLES-26NOV12BROSLATHONIC-THONIC`) | 0.06 / 0.11 (14) | 8.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Alec Deckers vs William Manning -- M25 Columbus OH R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207793:213152:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alec Deckers (`KXITFMATCH-26NOV12DECMAN-DEC`) | 0.60 / 0.63 (1) | 61.5% | 72.2% | 59.3% | 71.4% [69.8%-72.6%] | 62.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +10.7 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| William Manning (`KXITFMATCH-26NOV12DECMAN-MAN`) | 0.36 / 0.38 (2) | 37.0% | 27.8% | 40.7% | 28.6% [27.4%-30.2%] | 37.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.2 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2380.0, B 296.0; serve-point win A 71.4%, B 33.6%; Elo A 1451.9, B 1273.1; model uncertainty 0.0138
* Form inputs: days since last match A 80, B 136; matches on record A 184, B 9; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose +0.003, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Estevez / Zeitune vs Correa Beguerie / Valente -- M15 Roldan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12ESTZEICORVAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Correa Beguerie / Valente (`KXITFDOUBLES-26NOV12ESTZEICORVAL-CORVAL`) | 0.13 / 0.19 (24) | 16.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Estevez / Zeitune (`KXITFDOUBLES-26NOV12ESTZEICORVAL-ESTZEI`) | 0.76 / 0.85 (200) | 80.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Diego Hidalgo / Andres Molteni vs Daniel Rincon / Oriol Roca Batalla -- ATP Challenger Lima QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-12T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12HIDMOLRINROC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diego Hidalgo / Andres Molteni (`KXATPCHALLENGERDOUBLES-26NOV12HIDMOLRINROC-HIDMOL`) | 0.59 / 0.68 (150) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daniel Rincon / Oriol Roca Batalla (`KXATPCHALLENGERDOUBLES-26NOV12HIDMOLRINROC-RINROC`) | 0.34 / 0.35 (133) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Aidan Kim vs Jack Anthrop -- M25 Columbus OH R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210077:210294:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jack Anthrop (`KXITFMATCH-26NOV12KIMANT-ANT`) | 0.38 / 0.41 (4) | 39.5% | 47.9% | 68.2% | 56.1% [46.4%-61.6%] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +8.4 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aidan Kim (`KXITFMATCH-26NOV12KIMANT-KIM`) | 0.58 / 0.61 (1) | 59.5% | 52.1% | 31.8% | 43.9% [38.4%-53.6%] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.4 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 913.0, B 1030.0; serve-point win A 61.5%, B 38.9%; Elo A 1455.8, B 1442.4; model uncertainty 0.0757
* Form inputs: days since last match A 80, B 367; matches on record A 101, B 77; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rishvanth Krishna vs Ofek Shimanov -- M25 Columbus OH R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210645:213945:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rishvanth Krishna (`KXITFMATCH-26NOV12KRISHI-KRI`) | 0.39 / 0.41 (250) | 40.0% | 41.2% | 58.8% | 51.0% [50.0%-52.6%] | 37.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ofek Shimanov (`KXITFMATCH-26NOV12KRISHI-SHI`) | 0.58 / 0.60 (310) | 59.0% | 58.8% | 41.2% | 49.0% [47.4%-50.0%] | 62.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 69.0, B 305.0; serve-point win A 58.2%, B 40.1%; Elo A 1267.9, B 1258.9; model uncertainty 0.013
* Form inputs: days since last match A 507, B 247; matches on record A 1, B 58; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kuhar / Roh vs Dean / Tripathi -- M25 Montreal QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12KUHROHDEATRI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dean / Tripathi (`KXITFDOUBLES-26NOV12KUHROHDEATRI-DEATRI`) | 0.64 / 0.74 (200) | 69.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kuhar / Roh (`KXITFDOUBLES-26NOV12KUHROHDEATRI-KUHROH`) | 0.22 / 0.30 (37) | 26.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Nefve / Peck vs De Jonge / Opitz -- M25 Montreal QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12NEFPECDEJOPI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| De Jonge / Opitz (`KXITFDOUBLES-26NOV12NEFPECDEJOPI-DEJOPI`) | 0.64 / 0.75 (200) | 69.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nefve / Peck (`KXITFDOUBLES-26NOV12NEFPECDEJOPI-NEFPEC`) | 0.19 / 0.28 (200) | 23.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Raphael Perot vs Michael Antonius -- M25 Columbus OH R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212222:214004:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michael Antonius (`KXITFMATCH-26NOV12PERANT-ANT`) | 0.52 / 0.55 (594) | 53.5% | 42.2% | 32.8% | 35.1% [33.2%-38.1%] | 52.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.3 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Raphael Perot (`KXITFMATCH-26NOV12PERANT-PER`) | 0.43 / 0.47 (6) | 45.0% | 57.8% | 67.2% | 64.8% [61.9%-66.8%] | 47.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +12.8 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2367.0, B 903.0; serve-point win A 58.4%, B 43.1%; Elo A 1518.3, B 1423.2; model uncertainty 0.0247
* Form inputs: days since last match A 45, B 10; matches on record A 86, B 22; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.015, surface_dev_loose +0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rozin / Silva vs Visker / Wessels -- M25 Montreal QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12ROZSILVISWES:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rozin / Silva (`KXITFDOUBLES-26NOV12ROZSILVISWES-ROZSIL`) | 0.21 / 0.28 (3) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Visker / Wessels (`KXITFDOUBLES-26NOV12ROZSILVISWES-VISWES`) | 0.67 / 0.75 (200) | 71.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Apostolou / Syed vs Almeida / Vega -- M15 Naples FL QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 23:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12APOSYEALMVEG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Almeida / Vega (`KXITFDOUBLES-26NOV12APOSYEALMVEG-ALMVEG`) | 0.86 / 0.89 (1) | 87.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Apostolou / Syed (`KXITFDOUBLES-26NOV12APOSYEALMVEG-APOSYE`) | 0.07 / 0.11 (22) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Azam / Reddy vs Sheldon / Sheldon -- M15 Naples FL QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 23:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12AZAREDSHESHE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Azam / Reddy (`KXITFDOUBLES-26NOV12AZAREDSHESHE-AZARED`) | 0.26 / 0.33 (37) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sheldon / Sheldon (`KXITFDOUBLES-26NOV12AZAREDSHESHE-SHESHE`) | 0.62 / 0.69 (1) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kapasi / Zapp vs Nittmann / Watzka -- M15 Naples FL QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 23:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12KAPZAPNITWAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kapasi / Zapp (`KXITFDOUBLES-26NOV12KAPZAPNITWAT-KAPZAP`) | 0.69 / 0.78 (237) | 73.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nittmann / Watzka (`KXITFDOUBLES-26NOV12KAPZAPNITWAT-NITWAT`) | 0.18 / 0.27 (226) | 22.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## McCormick / Witten vs Giamichelle / Sanchez Bronzetti -- M15 Naples FL QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 23:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12MCCWITGIASAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giamichelle / Sanchez Bronzetti (`KXITFDOUBLES-26NOV12MCCWITGIASAN-GIASAN`) | 0.28 / 0.36 (81) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| McCormick / Witten (`KXITFDOUBLES-26NOV12MCCWITGIASAN-MCCWIT`) | 0.66 / 0.67 (257) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Guilherme Barbieri Renner vs Pedro Boscardin Dias -- M25 Santa Cruz do Sul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-13T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208046:214225:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pedro Boscardin Dias (`KXITFMATCH-26NOV12RENBOS-BOS`) | 0.92 / 0.93 (250) | 92.5% | 90.6% | 68.6% | 85.8% [84.6%-86.3%] | -- | -- | -- | -- | PASS | -1.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Guilherme Barbieri Renner (`KXITFMATCH-26NOV12RENBOS-REN`) | 0.07 / 0.08 (753) | 7.5% | 9.4% | 31.4% | 14.2% [13.7%-15.4%] | -- | -- | -- | -- | PASS | +1.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 50.0, B 4677.0; serve-point win A 53.3%, B 36.6%; Elo A 1248.8, B 1562.4; model uncertainty 0.0089
* Form inputs: days since last match A 381, B 10; matches on record A 1, B 349; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.012, surface_pool_high -0.006, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Juan Bautista Torres vs Lorenzo Joaquin Rodriguez -- M25 Santa Cruz do Sul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-13T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202271:208913:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Joaquin Rodriguez (`KXITFMATCH-26NOV12TORROD-ROD`) | 0.29 / 0.31 (14) | 30.0% | 27.3% | 34.0% | 32.5% [31.6%-34.5%] | -- | -- | -- | -- | PASS | -2.7 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Juan Bautista Torres (`KXITFMATCH-26NOV12TORROD-TOR`) | 0.68 / 0.69 (250) | 68.5% | 72.7% | 66.0% | 67.5% [65.5%-68.4%] | -- | -- | -- | -- | PASS | +4.2 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5064.0, B 3239.0; serve-point win A 57.1%, B 47.4%; Elo A 1604.3, B 1451.1; model uncertainty 0.0146
* Form inputs: days since last match A 199, B 10; matches on record A 360, B 264; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Karla Bartel vs Maria Kononova -- W15 Lincoln NE R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215236:264107:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karla Bartel (`KXITFWMATCH-26NOV12BARKON-BAR`) | 0.42 / 0.43 (337) | 42.5% | 59.2% | 80.5% | 53.7% [46.8%-60.9%] | -- | -- | -- | -- | PASS | +16.7 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Kononova (`KXITFWMATCH-26NOV12BARKON-KON`) | 0.54 / 0.57 (54) | 55.5% | 40.8% | 19.5% | 46.3% [39.1%-53.2%] | -- | -- | -- | -- | PASS | -14.7 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 966.0, B 370.0; serve-point win A 57.2%, B 44.5%; Elo A 1316.3, B 1343.3; model uncertainty 0.0706
* Form inputs: days since last match A 360, B 269; matches on record A 22, B 139; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV12BARKON-BAR  (YES = Karla Bartel)
Model: 59%
Kalshi: 42%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.011, surface_dev_loose +0.016, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cadence Brace vs Rachel Gailis -- W35 Weston FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-13T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222037:223335:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cadence Brace (`KXITFWMATCH-26NOV12BRAGAI-BRA`) | 0.64 / 0.65 (880) | 64.5% | 70.7% | 71.8% | 64.6% [61.6%-67.1%] | -- | -- | -- | -- | PASS | +6.2 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rachel Gailis (`KXITFWMATCH-26NOV12BRAGAI-GAI`) | 0.35 / 0.36 (325) | 35.5% | 29.3% | 28.2% | 35.4% [32.9%-38.4%] | -- | -- | -- | -- | PASS | -6.2 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2165.0, B 857.0; serve-point win A 54.6%, B 49.5%; Elo A 1550.2, B 1473.4; model uncertainty 0.0275
* Form inputs: days since last match A 57, B 107; matches on record A 222, B 113; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.000, surface_dev_loose +0.015, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jana Hossam Salah vs Allegra Korpanec Davies -- W35 Weston FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-13T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260914:266764:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jana Hossam Salah (`KXITFWMATCH-26NOV12HOSKOR-HOS`) | 0.58 / 0.60 (47) | 59.0% | 59.8% | 68.8% | 58.4% [55.3%-62.0%] | -- | -- | -- | -- | PASS | +0.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Allegra Korpanec Davies (`KXITFWMATCH-26NOV12HOSKOR-KOR`) | 0.39 / 0.41 (93) | 40.0% | 40.2% | 31.2% | 41.6% [38.0%-44.7%] | -- | -- | -- | -- | PASS | +0.2 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 378.0, B 1796.0; serve-point win A 57.1%, B 44.8%; Elo A 1371.0, B 1335.9; model uncertainty 0.0333
* Form inputs: days since last match A 325, B 199; matches on record A 19, B 48; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ashley Lahey vs Ilinca Dalina Amariei -- W35 Weston FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-13T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216076:221168:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ilinca Dalina Amariei (`KXITFWMATCH-26NOV12LAHAMA-AMA`) | 0.40 / 0.42 (283) | 41.0% | 48.3% | 49.5% | 51.6% [49.5%-53.7%] | -- | -- | -- | -- | PASS | +7.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ashley Lahey (`KXITFWMATCH-26NOV12LAHAMA-LAH`) | 0.57 / 0.60 (484) | 58.5% | 51.7% | 50.5% | 48.4% [46.3%-50.5%] | -- | -- | -- | -- | PASS | -6.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1883.0, B 2360.0; serve-point win A 55.8%, B 44.5%; Elo A 1569.5, B 1601.5; model uncertainty 0.0213
* Form inputs: days since last match A 423, B 339; matches on record A 239, B 325; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.016, surface_dev_loose +0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kristina Paskauskas vs Katie Spencer -- W15 Lincoln NE R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:258195:270382:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kristina Paskauskas (`KXITFWMATCH-26NOV12PASSPE-PAS`) | 0.83 / 0.84 (957) | 83.5% | 78.9% | 51.6% | 66.1% [65.1%-67.0%] | -- | -- | -- | -- | PASS | -4.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Katie Spencer (`KXITFWMATCH-26NOV12PASSPE-SPE`) | 0.15 / 0.16 (44) | 15.5% | 21.1% | 48.4% | 33.9% [33.0%-34.9%] | -- | -- | -- | -- | PASS | +5.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 382.0, B 128.0; serve-point win A 57.2%, B 48.8%; Elo A 1443.3, B 1318.6; model uncertainty 0.0098
* Form inputs: days since last match A 346, B 346; matches on record A 101, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Karlin Schock vs Eva Maria Ionescu -- W15 Lincoln NE R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260490:270127:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eva Maria Ionescu (`KXITFWMATCH-26NOV12SCHION-ION`) | 0.73 / 0.74 (197) | 73.5% | 92.3% | 65.5% | 78.7% [77.9%-80.3%] | -- | -- | -- | -- | PASS | +18.8 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Karlin Schock (`KXITFWMATCH-26NOV12SCHION-SCH`) | 0.25 / 0.26 (115) | 25.5% | 7.7% | 34.5% | 21.3% [19.7%-22.1%] | -- | -- | -- | -- | PASS | -17.8 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 117.0, B 1868.0; serve-point win A 49.9%, B 39.4%; Elo A 1241.8, B 1477.2; model uncertainty 0.0121
* Form inputs: days since last match A 374, B 123; matches on record A 2, B 92; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV12SCHION-ION  (YES = Eva Maria Ionescu)
Model: 92%
Kalshi: 74%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.008, surface_dev_loose +0.000, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maria Taranova vs Aishi Das -- W15 Lincoln NE R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:261133:269912:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aishi Das (`KXITFWMATCH-26NOV12TARDAS-DAS`) | 0.66 / 0.67 (333) | 66.5% | 77.8% | 70.0% | 58.5% [58.5%-59.5%] | -- | -- | -- | -- | PASS | +11.3 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Maria Taranova (`KXITFWMATCH-26NOV12TARDAS-TAR`) | 0.32 / 0.33 (7) | 32.5% | 22.1% | 30.0% | 41.5% [40.5%-41.5%] | -- | -- | -- | -- | PASS | -10.3 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 979.0; serve-point win A 49.7%, B 44.6%; Elo A 1283.0, B 1345.8; model uncertainty 0.0053
* Form inputs: days since last match A 738, B 199; matches on record A 1, B 30; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aran Teixido Garcia vs Carolina Kuhl -- W35 Weston FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12TEIKUH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carolina Kuhl (`KXITFWMATCH-26NOV12TEIKUH-KUH`) | 0.45 / 0.46 (329) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aran Teixido Garcia (`KXITFWMATCH-26NOV12TEIKUH-TEI`) | 0.54 / 0.55 (623) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ellen Perez / Demi Schuurs vs Sara Errani / Jasmine Paolini -- WTA Finals Women Doubles Group

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-13 02:30Z
* Current expected start: 2026-11-13 00:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-12 16:57Z
* Recommended handicap-by time: 2026-11-12 23:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_FINALS) · surface ? · scheduled 2026-11-13T02:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12PERSCHERRPAO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Errani / Jasmine Paolini (`KXWTADOUBLES-26NOV12PERSCHERRPAO-ERRPAO`) | 0.66 / 0.69 (898) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ellen Perez / Demi Schuurs (`KXWTADOUBLES-26NOV12PERSCHERRPAO-PERSCH`) | 0.31 / 0.33 (82) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Blu Baker vs Jesse Flores -- M15 Zamora QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132374:209124:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Blu Baker (`KXITFMATCH-26NOV12BAKFLO-BAK`) | 0.70 / 0.72 (375) | 71.0% | 56.9% | 51.5% | 57.0% [55.0%-60.1%] | -- | -- | -- | -- | PASS | -14.1 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jesse Flores (`KXITFMATCH-26NOV12BAKFLO-FLO`) | 0.28 / 0.29 (1733) | 28.5% | 43.1% | 48.5% | 43.0% [39.9%-45.0%] | -- | -- | -- | -- | WATCH | +14.6 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1707.0, B 2047.0; serve-point win A 63.2%, B 38.2%; Elo A 1402.1, B 1309.5; model uncertainty 0.0252
* Form inputs: days since last match A 213, B 199; matches on record A 119, B 190; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marcos Giron vs Abdullah Shelbayh -- ATP Challenger Knoxville R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-13T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12GIRSHE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcos Giron (`KXATPCHALLENGERMATCH-26NOV12GIRSHE-GIR`) | 0.73 / 0.74 (1051) | 73.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Abdullah Shelbayh (`KXATPCHALLENGERMATCH-26NOV12GIRSHE-SHE`) | 0.26 / 0.27 (4358) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Matias Soto vs Luis Carlos Alvarez Valdes -- M15 Zamora QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207130:211468:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luis Carlos Alvarez Valdes (`KXITFMATCH-26NOV12SOTALV-ALV`) | 0.52 / 0.55 (125) | 53.5% | 38.0% | 55.7% | 38.2% [29.3%-44.3%] | -- | -- | -- | -- | PASS | -15.4 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matias Soto (`KXITFMATCH-26NOV12SOTALV-SOT`) | 0.44 / 0.46 (1) | 45.0% | 62.0% | 44.3% | 61.8% [55.7%-70.7%] | -- | -- | -- | -- | PASS | +16.9 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4186.0, B 923.0; serve-point win A 59.5%, B 42.9%; Elo A 1586.6, B 1424.0; model uncertainty 0.0749
* Form inputs: days since last match A 24, B 381; matches on record A 288, B 45; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV12SOTALV-SOT  (YES = Matias Soto)
Model: 62%
Kalshi: 45%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bernardes / Rosa Dourado vs Boyden / Hrda -- W15 São Carlos QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12BERROSBOYHRD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bernardes / Rosa Dourado (`KXITFWDOUBLES-26NOV12BERROSBOYHRD-BERROS`) | 0.23 / 0.28 (3) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Boyden / Hrda (`KXITFWDOUBLES-26NOV12BERROSBOYHRD-BOYHRD`) | 0.67 / 0.73 (92) | 70.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Ana Grubor vs Ava Esposito Cogan -- W15 Lincoln NE R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12GRUESP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ava Esposito Cogan (`KXITFWMATCH-26NOV12GRUESP-ESP`) | 0.53 / 0.54 (760) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ana Grubor (`KXITFWMATCH-26NOV12GRUESP-GRU`) | 0.43 / 0.44 (5) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kelly Keller vs Merna Refaat -- W15 Lincoln NE R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221473:260103:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kelly Keller (`KXITFWMATCH-26NOV12KELREF-KEL`) | 0.12 / 0.13 (2271) | 12.5% | 32.6% | 44.1% | 41.5% [40.5%-42.0%] | -- | -- | -- | -- | PASS | +20.1 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Merna Refaat (`KXITFWMATCH-26NOV12KELREF-REF`) | 0.86 / 0.89 (346) | 87.5% | 67.3% | 55.9% | 58.5% [58.0%-59.5%] | -- | -- | -- | -- | PASS | -20.1 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 436.0, B 556.0; serve-point win A 48.9%, B 47.8%; Elo A 1334.0, B 1402.3; model uncertainty 0.0077
* Form inputs: days since last match A 269, B 395; matches on record A 54, B 201; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV12KELREF-KEL  (YES = Kelly Keller)
Model: 33%
Kalshi: 12%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Konishi Camargo Silva / Souza vs Kawano Cho / Meabe -- W15 São Carlos QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12KONSOUKAWMEA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kawano Cho / Meabe (`KXITFWDOUBLES-26NOV12KONSOUKAWMEA-KAWMEA`) | 0.36 / 0.43 (124) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Konishi Camargo Silva / Souza (`KXITFWDOUBLES-26NOV12KONSOUKAWMEA-KONSOU`) | 0.55 / 0.60 (246) | 57.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Isabella Kruger vs Mia Kupres -- W15 Lincoln NE R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221996:222377:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isabella Kruger (`KXITFWMATCH-26NOV12KRUKUP-KRU`) | 0.49 / 0.53 (407) | 51.0% | 72.5% | 57.4% | 71.2% [70.2%-72.0%] | -- | -- | -- | -- | PASS | +21.5 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Mia Kupres (`KXITFWMATCH-26NOV12KRUKUP-KUP`) | 0.46 / 0.48 (255) | 47.0% | 27.5% | 42.6% | 28.8% [28.0%-29.8%] | -- | -- | -- | -- | PASS | -19.5 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 144.0; serve-point win A 57.9%, B 46.6%; Elo A 1578.7, B 1420.3; model uncertainty 0.0091
* Form inputs: days since last match A 752, B 109; matches on record A 148, B 64; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV12KRUKUP-KRU  (YES = Isabella Kruger)
Model: 73%
Kalshi: 51%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kaya Moe vs Arina Malygina -- W15 Lincoln NE R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12MOEMAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arina Malygina (`KXITFWMATCH-26NOV12MOEMAL-MAL`) | 0.67 / 0.69 (5) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kaya Moe (`KXITFWMATCH-26NOV12MOEMAL-MOE`) | 0.31 / 0.32 (323) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Joao Lucas Reis Da Silva vs Gonzalo Bueno -- ATP Challenger Lima R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-13T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206307:208293:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gonzalo Bueno (`KXATPCHALLENGERMATCH-26NOV12REIBUE-BUE`) | 0.39 / 0.40 (421) | 39.5% | 41.7% | 32.8% | 36.7% [34.2%-40.7%] | -- | -- | -- | -- | PASS | +2.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Joao Lucas Reis Da Silva (`KXATPCHALLENGERMATCH-26NOV12REIBUE-REI`) | 0.59 / 0.60 (63) | 59.5% | 58.3% | 67.2% | 63.3% [59.3%-65.8%] | -- | -- | -- | -- | WATCH | -1.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5010.0, B 4995.0; serve-point win A 59.3%, B 42.3%; Elo A 1671.7, B 1668.7; model uncertainty 0.0323
* Form inputs: days since last match A 10, B 10; matches on record A 485, B 324; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Adams / Sahdiieva vs Burgic / Podhajecka -- W35 Weston FL QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12ADASAHBURPOD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adams / Sahdiieva (`KXITFWDOUBLES-26NOV12ADASAHBURPOD-ADASAH`) | 0.68 / 0.84 (1) | 76.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Burgic / Podhajecka (`KXITFWDOUBLES-26NOV12ADASAHBURPOD-BURPOD`) | 0.10 / 0.26 (3) | 18.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Miriam Bianca Bulgaru vs Despina Papamichail -- W50 Chihuahua QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-13T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:202604:214480:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miriam Bianca Bulgaru (`KXITFWMATCH-26NOV12BULPAP-BUL`) | 0.44 / 0.46 (46) | 45.0% | 55.8% | 30.9% | 37.9% [34.8%-43.1%] | -- | -- | -- | -- | PASS | +10.8 pp | REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Despina Papamichail (`KXITFWMATCH-26NOV12BULPAP-PAP`) | 0.52 / 0.54 (374) | 53.0% | 44.2% | 69.1% | 62.2% [56.9%-65.2%] | -- | -- | -- | -- | WATCH | -8.8 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3417.0, B 4365.0; serve-point win A 51.1%, B 50.0%; Elo A 1669.5, B 1641.6; model uncertainty 0.0412
* Form inputs: days since last match A 199, B 8; matches on record A 517, B 993; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.026, surface_dev_loose -0.000, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kayla Cross vs Ipek Oz -- W50 Chihuahua QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-13T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213998:239436:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kayla Cross (`KXITFWMATCH-26NOV12CROOZX-CRO`) | 0.37 / 0.38 (250) | 37.5% | 48.9% | 66.0% | 57.4% [51.6%-60.5%] | -- | -- | -- | -- | WATCH | +11.3 pp | REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ipek Oz (`KXITFWMATCH-26NOV12CROOZX-OZX`) | 0.61 / 0.62 (198) | 61.5% | 51.1% | 34.0% | 42.6% [39.5%-48.4%] | -- | -- | -- | -- | PASS | -10.3 pp | REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2619.0, B 2398.0; serve-point win A 54.4%, B 45.4%; Elo A 1541.9, B 1597.1; model uncertainty 0.0446
* Form inputs: days since last match A 59, B 65; matches on record A 237, B 487; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.026, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bassem Sobhy / Kelly vs Komolpisut / Suttisomboon -- M25 Columbus OH QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12BASKELKOMSUT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bassem Sobhy / Kelly (`KXITFDOUBLES-26NOV12BASKELKOMSUT-BASKEL`) | 0.06 / 0.89 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Komolpisut / Suttisomboon (`KXITFDOUBLES-26NOV12BASKELKOMSUT-KOMSUT`) | 0.07 / 0.89 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Rafael De Alba vs Kai Thompson -- M15 Zamora QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208908:214142:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rafael De Alba (`KXITFMATCH-26NOV12DEATHO-DEA`) | 0.43 / 0.46 (15) | 44.5% | 49.4% | 31.8% | 41.1% [40.1%-41.7%] | -- | -- | -- | -- | PASS | +4.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kai Thompson (`KXITFMATCH-26NOV12DEATHO-THO`) | 0.53 / 0.56 (389) | 54.5% | 50.6% | 68.2% | 58.9% [58.3%-59.9%] | -- | -- | -- | -- | PASS | -3.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1439.0, B 164.0; serve-point win A 57.4%, B 42.5%; Elo A 1198.5, B 1255.5; model uncertainty 0.0081
* Form inputs: days since last match A 199, B 311; matches on record A 35, B 4; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lucca Cervantes Tomas / Alejandro Reyes Tirado vs Alujas / Benson -- M15 Zamora QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12LUCALEALUBEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alujas / Benson (`KXITFDOUBLES-26NOV12LUCALEALUBEN-ALUBEN`) | 0.47 / 0.57 (150) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lucca Cervantes Tomas / Alejandro Reyes Tirado (`KXITFDOUBLES-26NOV12LUCALEALUBEN-LUCALE`) | 0.37 / 0.47 (197) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Black / Jauffret vs Hu / Lahey -- W35 Weston FL QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12BLAJAUHUXLAH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Black / Jauffret (`KXITFWDOUBLES-26NOV12BLAJAUHUXLAH-BLAJAU`) | 0.40 / 0.46 (196) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hu / Lahey (`KXITFWDOUBLES-26NOV12BLAJAUHUXLAH-HUXLAH`) | 0.52 / 0.58 (150) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Hossam Salah / Korpanec Davies vs Evtimova / Harding -- W35 Weston FL QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12HOSKOREVTHAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Evtimova / Harding (`KXITFWDOUBLES-26NOV12HOSKOREVTHAR-EVTHAR`) | 0.31 / 0.39 (192) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hossam Salah / Korpanec Davies (`KXITFWDOUBLES-26NOV12HOSKOREVTHAR-HOSKOR`) | 0.60 / 0.65 (150) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Martinez / Reed vs Bulatova / Kuhl -- W35 Weston FL QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12MARREEBULKUH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bulatova / Kuhl (`KXITFWDOUBLES-26NOV12MARREEBULKUH-BULKUH`) | 0.55 / 0.65 (5) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Martinez / Reed (`KXITFWDOUBLES-26NOV12MARREEBULKUH-MARREE`) | 0.30 / 0.41 (43) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Carpico / Filin vs Anthrop / Stearns -- M25 Columbus OH QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 02:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T02:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12CARFILANTSTE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anthrop / Stearns (`KXITFDOUBLES-26NOV12CARFILANTSTE-ANTSTE`) | 0.15 / 0.34 (1) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Carpico / Filin (`KXITFDOUBLES-26NOV12CARFILANTSTE-CARFIL`) | 0.55 / 0.80 (3) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kim / Nakashima vs Heck / Young -- M25 Columbus OH QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 02:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T02:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12KIMNAKHECYOU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Heck / Young (`KXITFDOUBLES-26NOV12KIMNAKHECYOU-HECYOU`) | 0.07 / 0.89 (43) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kim / Nakashima (`KXITFDOUBLES-26NOV12KIMNAKHECYOU-KIMNAK`) | 0.07 / 0.89 (41) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Nathaniel Lammons / John-Patrick Smith vs Hynek Barton / Maks Kasnikowski -- ATP Challenger Knoxville QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 02:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-13T02:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12LAMSMIBARKAS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hynek Barton / Maks Kasnikowski (`KXATPCHALLENGERDOUBLES-26NOV12LAMSMIBARKAS-BARKAS`) | 0.08 / 0.32 (2) | 20.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nathaniel Lammons / John-Patrick Smith (`KXATPCHALLENGERDOUBLES-26NOV12LAMSMIBARKAS-LAMSMI`) | 0.71 / 0.94 (56) | 82.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Genaro Alberto Olivieri vs Juan Pablo Varillas -- ATP Challenger Lima R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 02:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-13T02:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:122669:144821:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Genaro Alberto Olivieri (`KXATPCHALLENGERMATCH-26NOV12OLIVAR-OLI`) | 0.39 / 0.40 (6113) | 39.5% | 44.2% | 36.3% | 36.3% [35.8%-37.3%] | -- | -- | -- | -- | PASS | +4.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Juan Pablo Varillas (`KXATPCHALLENGERMATCH-26NOV12OLIVAR-VAR`) | 0.60 / 0.61 (5173) | 60.5% | 55.8% | 63.7% | 63.7% [62.7%-64.2%] | -- | -- | -- | -- | WATCH | -4.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5176.0, B 5090.0; serve-point win A 58.7%, B 40.1%; Elo A 1588.2, B 1678.1; model uncertainty 0.0075
* Form inputs: days since last match A 10, B 10; matches on record A 613, B 797; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.005, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Leite / Sakamoto vs Alves / Fa Rodriguez Taverna -- M25 Santa Cruz do Sul QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 03:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12LEISAKALVFAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alves / Fa Rodriguez Taverna (`KXITFDOUBLES-26NOV12LEISAKALVFAR-ALVFAR`) | 0.68 / 0.89 (1) | 78.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Leite / Sakamoto (`KXITFDOUBLES-26NOV12LEISAKALVFAR-LEISAK`) | 0.07 / 0.26 (1) | 16.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tosetto / Zanellato vs Noatto / Pinheiro da Cruz Junior -- M25 Santa Cruz do Sul QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 03:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12TOSZANNOAPIN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Noatto / Pinheiro da Cruz Junior (`KXITFDOUBLES-26NOV12TOSZANNOAPIN-NOAPIN`) | 0.12 / 0.30 (1) | 21.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tosetto / Zanellato (`KXITFDOUBLES-26NOV12TOSZANNOAPIN-TOSZAN`) | 0.64 / 0.82 (1) | 73.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mettraux / Meyer auf der Heide vs Gatica / Pereira -- W15 São Carlos QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 03:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12METMEYGATPER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gatica / Pereira (`KXITFWDOUBLES-26NOV12METMEYGATPER-GATPER`) | 0.46 / 0.65 (56) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mettraux / Meyer auf der Heide (`KXITFWDOUBLES-26NOV12METMEYGATPER-METMEY`) | 0.31 / 0.48 (1) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Malaika Rapolu vs Jessica Hinojosa Gomez -- W50 Chihuahua QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 03:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-13T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213739:222837:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jessica Hinojosa Gomez (`KXITFWMATCH-26NOV12RAPHIN-HIN`) | 0.07 / 0.09 (124) | 8.0% | 12.9% | 25.9% | 24.2% [21.8%-26.4%] | -- | -- | -- | -- | WATCH | +4.9 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Malaika Rapolu (`KXITFWMATCH-26NOV12RAPHIN-RAP`) | 0.89 / 0.91 (2) | 90.0% | 87.1% | 74.1% | 75.8% [73.6%-78.2%] | -- | -- | -- | -- | PASS | -2.9 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1761.0, B 1620.0; serve-point win A 55.0%, B 53.4%; Elo A 1586.8, B 1369.3; model uncertainty 0.0227
* Form inputs: days since last match A 56, B 17; matches on record A 134, B 177; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.017, surface_dev_loose -0.017, surface_dev_tight +0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carlos Alvarez Valdes / Urrea vs Alvarez / Cozad -- M15 Zamora QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 03:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T03:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12CARURRALVCOZ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alvarez / Cozad (`KXITFDOUBLES-26NOV12CARURRALVCOZ-ALVCOZ`) | 0.16 / 0.79 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Carlos Alvarez Valdes / Urrea (`KXITFDOUBLES-26NOV12CARURRALVCOZ-CARURR`) | 0.16 / 0.79 (3) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Flores / Matta vs Covato / Voelzke -- M15 Zamora QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 03:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T03:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12FLOMATCOVVOE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Covato / Voelzke (`KXITFDOUBLES-26NOV12FLOMATCOVVOE-COVVOE`) | 0.34 / 0.58 (8) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Flores / Matta (`KXITFDOUBLES-26NOV12FLOMATCOVVOE-FLOMAT`) | 0.37 / 0.55 (56) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Albuquerque Dietrich / Dummer Macedo vs Braga / Braga -- M25 Santa Cruz do Sul QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12ALBDUMBRABRA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Albuquerque Dietrich / Dummer Macedo (`KXITFDOUBLES-26NOV12ALBDUMBRABRA-ALBDUM`) | 0.07 / 0.68 (1) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Braga / Braga (`KXITFDOUBLES-26NOV12ALBDUMBRABRA-BRABRA`) | 0.27 / 0.88 (1) | 57.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sebastian Gorzny vs Alex Bolt -- ATP Challenger Brisbane QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-13T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12GORBOL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex Bolt (`KXATPCHALLENGERMATCH-26NOV12GORBOL-BOL`) | 0.48 / 0.49 (5532) | 48.5% | -- | -- | -- [-----] | -- | 48.5% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sebastian Gorzny (`KXATPCHALLENGERMATCH-26NOV12GORBOL-GOR`) | 0.51 / 0.52 (33) | 51.5% | -- | -- | -- [-----] | -- | 51.9% | 51.9% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Victor Couto Loureiro / Ribeiro vs Barranco Cosano / Dutra da Silva -- M25 Santa Cruz do Sul QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12VICRIBBARDUT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barranco Cosano / Dutra da Silva (`KXITFDOUBLES-26NOV12VICRIBBARDUT-BARDUT`) | 0.07 / 0.63 (56) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Victor Couto Loureiro / Ribeiro (`KXITFDOUBLES-26NOV12VICRIBBARDUT-VICRIB`) | 0.31 / 0.89 (26) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Coe / Taranova vs Das / Maria Ionescu -- W15 Lincoln NE QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12COETARDASMAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Coe / Taranova (`KXITFWDOUBLES-26NOV12COETARDASMAR-COETAR`) | 0.11 / 0.84 (56) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Das / Maria Ionescu (`KXITFWDOUBLES-26NOV12COETARDASMAR-DASMAR`) | 0.11 / 0.84 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Rahimkhani / Rizzetto vs Dean / Kononova -- W15 Lincoln NE QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12RAHRIZDEAKON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dean / Kononova (`KXITFWDOUBLES-26NOV12RAHRIZDEAKON-DEAKON`) | 0.53 / 0.75 (4) | 64.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rahimkhani / Rizzetto (`KXITFWDOUBLES-26NOV12RAHRIZDEAKON-RAHRIZ`) | 0.13 / 0.40 (2) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mauricio Echazu vs Dante Carlos Teramo -- M15 Zamora QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105273:213929:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mauricio Echazu (`KXITFMATCH-26NOV12ECHTER-ECH`) | 0.56 / 0.60 (41) | 58.0% | 67.0% | 66.3% | 68.1% [67.6%-69.3%] | -- | -- | -- | -- | PASS | +9.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dante Carlos Teramo (`KXITFMATCH-26NOV12ECHTER-TER`) | 0.37 / 0.42 (120) | 39.5% | 33.0% | 33.7% | 31.9% [30.7%-32.4%] | -- | -- | -- | -- | PASS | -6.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 170.0, B 114.0; serve-point win A 63.7%, B 39.8%; Elo A 1368.9, B 1236.4; model uncertainty 0.0082
* Form inputs: days since last match A 199, B 388; matches on record A 685, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yu Hsiou Hsu vs Jay Friend -- ATP Challenger Matsuyama QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-13T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12HSUHAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jay Friend (`KXATPCHALLENGERMATCH-26NOV12HSUHAR-HAR`) | 0.57 / 0.59 (1839) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yu Hsiou Hsu (`KXATPCHALLENGERMATCH-26NOV12HSUHAR-HSU`) | 0.41 / 0.43 (2848) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Rio Noguchi vs Taro Daniel -- ATP Challenger Matsuyama QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-13T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12NOGDAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Taro Daniel (`KXATPCHALLENGERMATCH-26NOV12NOGDAN-DAN`) | 0.67 / 0.70 (6) | 68.5% | -- | -- | -- [-----] | -- | 68.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rio Noguchi (`KXATPCHALLENGERMATCH-26NOV12NOGDAN-NOG`) | 0.28 / 0.31 (30) | 29.5% | -- | -- | -- [-----] | -- | 28.2% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; THIN_DISPLAYED_SIZE

## Bartel / Kupres vs Kruger / Refaat -- W15 Lincoln NE QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12BARKUPKRUREF:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bartel / Kupres (`KXITFWDOUBLES-26NOV12BARKUPKRUREF-BARKUP`) | 0.36 / 0.55 (1) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kruger / Refaat (`KXITFWDOUBLES-26NOV12BARKUPKRUREF-KRUREF`) | 0.39 / 0.58 (27) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Raidt / Spencer vs Esposito Cogan / Moe -- W15 Lincoln NE QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12RAISPEESPMOE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Esposito Cogan / Moe (`KXITFWDOUBLES-26NOV12RAISPEESPMOE-ESPMOE`) | 0.12 / 0.84 (4) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Raidt / Spencer (`KXITFWDOUBLES-26NOV12RAISPEESPMOE-RAISPE`) | 0.10 / 0.84 (1) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dane Sweeny vs Juncheng Shang -- ATP Challenger Brisbane QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 05:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-13T05:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12SWESHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juncheng Shang (`KXATPCHALLENGERMATCH-26NOV12SWESHA-SHA`) | 0.60 / 0.63 (6) | 61.5% | -- | -- | -- [-----] | -- | 66.8% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dane Sweeny (`KXATPCHALLENGERMATCH-26NOV12SWESHA-SWE`) | 0.35 / 0.38 (26) | 36.5% | -- | -- | -- [-----] | -- | 38.8% | 38.8% | KALSHI_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; THIN_DISPLAYED_SIZE

## Colmegna / Zolotareva vs Cross / Papamichail -- W50 Chihuahua SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 05:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T05:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12COLZOLCROPAP:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Colmegna / Zolotareva (`KXITFWDOUBLES-26NOV12COLZOLCROPAP-COLZOL`) | 0.24 / 0.43 (1) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cross / Papamichail (`KXITFWDOUBLES-26NOV12COLZOLCROPAP-CROPAP`) | 0.51 / 0.70 (1) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## De Alba / Sau Franco vs Odiseo Alvarado Berrospi / Betancourt -- M15 Zamora QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12DEASAUODIBET:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| De Alba / Sau Franco (`KXITFDOUBLES-26NOV12DEASAUODIBET-DEASAU`) | 0.63 / 0.82 (1) | 72.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Odiseo Alvarado Berrospi / Betancourt (`KXITFDOUBLES-26NOV12DEASAUODIBET-ODIBET`) | 0.13 / 0.31 (56) | 22.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Bernard Tomic vs August Holmgren -- ATP Challenger Brisbane QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-13T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12TOMHOL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| August Holmgren (`KXATPCHALLENGERMATCH-26NOV12TOMHOL-HOL`) | 0.58 / 0.60 (6582) | 59.0% | -- | -- | -- [-----] | -- | 58.9% | 58.9% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bernard Tomic (`KXATPCHALLENGERMATCH-26NOV12TOMHOL-TOM`) | 0.40 / 0.41 (217) | 40.5% | -- | -- | -- [-----] | -- | 41.8% | 41.8% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Rei Sakamoto vs Ognjen Milic -- ATP Challenger Matsuyama QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 06:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-13T06:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12SAKMIL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ognjen Milic (`KXATPCHALLENGERMATCH-26NOV12SAKMIL-MIL`) | 0.10 / 0.14 (44) | 12.0% | -- | -- | -- [-----] | -- | 14.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rei Sakamoto (`KXATPCHALLENGERMATCH-26NOV12SAKMIL-SAK`) | 0.84 / 0.88 (15) | 86.0% | -- | -- | -- [-----] | -- | 85.9% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Kaichi Uchida vs Billy Harris -- ATP Challenger Matsuyama QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 06:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-13T06:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12UCHHAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Billy Harris (`KXATPCHALLENGERMATCH-26NOV12UCHHAR-HAR`) | 0.78 / 0.80 (7365) | 79.0% | -- | -- | -- [-----] | -- | 79.1% | 79.1% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kaichi Uchida (`KXATPCHALLENGERMATCH-26NOV12UCHHAR-UCH`) | 0.20 / 0.22 (4794) | 21.0% | -- | -- | -- [-----] | -- | 21.3% | 21.3% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Blake Bayldon / Thomas Fancutt vs Blake Ellis / Li Tu -- ATP Challenger Brisbane SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 06:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-13T06:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12BAYFANELLTUL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Blake Bayldon / Thomas Fancutt (`KXATPCHALLENGERDOUBLES-26NOV12BAYFANELLTUL-BAYFAN`) | 0.44 / 0.92 (114) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Blake Ellis / Li Tu (`KXATPCHALLENGERDOUBLES-26NOV12BAYFANELLTUL-ELLTUL`) | 0.39 / 0.63 (56) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Joanna Garland vs Olivia Gadecki -- W75 Brisbane QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216265:220466:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Olivia Gadecki (`KXITFWMATCH-26NOV12GARGAD-GAD`) | 0.32 / 0.35 (28) | 33.5% | 37.3% | 43.8% | 44.3% [42.2%-45.4%] | 35.6% | -- | 35.6% | MODEL_LONE_OUTLIER | WATCH | +3.8 pp | NORMAL | FRESH | B / LIMITED | ALL_AGREE | VERIFIED |
| Joanna Garland (`KXITFWMATCH-26NOV12GARGAD-GAR`) | 0.62 / 0.66 (14) | 64.0% | 62.7% | 56.2% | 55.7% [54.6%-57.8%] | 64.4% | -- | 64.4% | MODEL_LONE_OUTLIER | PASS | -1.3 pp | NORMAL | FRESH | B / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 2480.0, B 3148.0; serve-point win A 60.6%, B 41.9%; Elo A 1772.3, B 1735.5; model uncertainty 0.0156
* Form inputs: days since last match A 8, B 199; matches on record A 397, B 342; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yeonwoo Ku vs Kanon Sawashiro -- W50 Yokohama QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12KUXSAW:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yeonwoo Ku (`KXITFWMATCH-26NOV12KUXSAW-KUX`) | 0.82 / 0.85 (25) | 83.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kanon Sawashiro (`KXITFWMATCH-26NOV12KUXSAW-SAW`) | 0.14 / 0.15 (90) | 14.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Himeno Sakatsume vs Zhuoxuan Bai -- W75 Brisbane QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221124:222296:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zhuoxuan Bai (`KXITFWMATCH-26NOV12SAKBAI-BAI`) | 0.43 / 0.44 (1) | 43.5% | 51.6% | 45.7% | 47.9% [46.3%-49.5%] | 46.2% | -- | 46.2% | EXTERNAL_LONE_OUTLIER | WATCH | +8.1 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Himeno Sakatsume (`KXITFWMATCH-26NOV12SAKBAI-SAK`) | 0.54 / 0.56 (5) | 55.0% | 48.4% | 54.3% | 52.1% [50.5%-53.7%] | 53.8% | -- | 53.8% | KALSHI_LONE_OUTLIER | PASS | -6.6 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3693.0, B 1601.0; serve-point win A 54.1%, B 45.6%; Elo A 1764.5, B 1765.4; model uncertainty 0.016
* Form inputs: days since last match A 9, B 34; matches on record A 421, B 213; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose -0.016, surface_dev_tight +0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Strakhova / Tikhonova vs Hinojosa Gomez / Tran -- W50 Chihuahua SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12STRTIKHINTRA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hinojosa Gomez / Tran (`KXITFWDOUBLES-26NOV12STRTIKHINTRA-HINTRA`) | 0.10 / 0.19 (3) | 14.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Strakhova / Tikhonova (`KXITFWDOUBLES-26NOV12STRTIKHINTRA-STRTIK`) | 0.76 / 0.84 (14) | 80.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Miriana Tona vs Vivian Wolff -- W50 Chihuahua QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-13T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:210847:215386:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miriana Tona (`KXITFWMATCH-26NOV12TONWOL-TON`) | 0.27 / 0.30 (336) | 28.5% | 20.5% | 25.5% | 27.7% [25.5%-32.9%] | 30.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.0 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Vivian Wolff (`KXITFWMATCH-26NOV12TONWOL-WOL`) | 0.70 / 0.71 (3) | 70.5% | 79.5% | 74.5% | 72.3% [67.1%-74.5%] | 69.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +9.0 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2556.0, B 2229.0; serve-point win A 48.8%, B 45.1%; Elo A 1511.0, B 1638.5; model uncertainty 0.037
* Form inputs: days since last match A 66, B 44; matches on record A 410, B 284; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.009, surface_dev_loose -0.022, surface_dev_tight +0.023
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chia Yi Tsao vs Sara Saito -- W50 Yokohama QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259623:260170:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Saito (`KXITFWMATCH-26NOV12TSASAI-SAI`) | 0.76 / 0.81 (70) | 78.5% | 66.2% | 46.8% | 56.9% [51.6%-66.5%] | 78.1% | -- | 78.1% | MODEL_LONE_OUTLIER | PASS | -12.3 pp | REVIEW | FRESH | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Chia Yi Tsao (`KXITFWMATCH-26NOV12TSASAI-TSA`) | 0.18 / 0.21 (34) | 19.5% | 33.8% | 53.2% | 43.1% [33.5%-48.4%] | 21.9% | -- | 21.9% | MODEL_LONE_OUTLIER | WATCH | +14.3 pp | REVIEW | FRESH | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 824.0, B 3341.0; serve-point win A 54.0%, B 42.9%; Elo A 1482.7, B 1574.9; model uncertainty 0.0747
* Form inputs: days since last match A 206, B 45; matches on record A 145, B 198; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.041, surface_pool_high +0.032, surface_dev_loose +0.005, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Akira Santillan vs Christian Langmo -- ATP Challenger Brisbane QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 07:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-13T07:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12SANLAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Christian Langmo (`KXATPCHALLENGERMATCH-26NOV12SANLAN-LAN`) | 0.39 / 0.43 (8) | 41.0% | -- | -- | -- [-----] | -- | 42.4% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Akira Santillan (`KXATPCHALLENGERMATCH-26NOV12SANLAN-SAN`) | 0.55 / 0.59 (53) | 57.0% | -- | -- | -- [-----] | -- | 57.8% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; THIN_DISPLAYED_SIZE

## Pruchya Isaro / Yuta Shimizu vs Arjun Kadhe / Aoran Wang -- ATP Challenger Matsuyama SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 07:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-13T07:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12ISASHIKADWAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pruchya Isaro / Yuta Shimizu (`KXATPCHALLENGERDOUBLES-26NOV12ISASHIKADWAN-ISASHI`) | 0.26 / 0.94 (56) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arjun Kadhe / Aoran Wang (`KXATPCHALLENGERDOUBLES-26NOV12ISASHIKADWAN-KADWAN`) | 0.06 / 0.78 (56) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Finn Reynolds / James Watt vs Yusuke Kusuhara / Shunsuke Nakagawa -- ATP Challenger Matsuyama SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 07:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-13T07:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12REYWATKUSNAK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yusuke Kusuhara / Shunsuke Nakagawa (`KXATPCHALLENGERDOUBLES-26NOV12REYWATKUSNAK-KUSNAK`) | 0.11 / 0.28 (3) | 19.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Finn Reynolds / James Watt (`KXATPCHALLENGERDOUBLES-26NOV12REYWATKUSNAK-REYWAT`) | 0.67 / 0.85 (56) | 76.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Reece Falck / Billy Suarez vs Alafia Ayeni / Kokoro Isomura -- ATP Challenger Brisbane SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 07:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-13T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12FALSUAAVEISO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alafia Ayeni / Kokoro Isomura (`KXATPCHALLENGERDOUBLES-26NOV12FALSUAAVEISO-AVEISO`) | 0.06 / 0.78 (56) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Reece Falck / Billy Suarez (`KXATPCHALLENGERDOUBLES-26NOV12FALSUAAVEISO-FALSUA`) | 0.29 / 0.94 (56) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## M Rifqi Fitriadi vs Edoardo Cherie Ligniere -- M15 Kuala Lumpur QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12FITCHE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Edoardo Cherie Ligniere (`KXITFMATCH-26NOV12FITCHE-CHE`) | 0.34 / 0.36 (406) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| M Rifqi Fitriadi (`KXITFMATCH-26NOV12FITCHE-FIT`) | 0.63 / 0.65 (20) | 64.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuto Oki vs Dev Javia -- M15 Kuala Lumpur QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209956:212639:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dev Javia (`KXITFMATCH-26NOV12OKIJAV-JAV`) | 0.46 / 0.52 (145) | 49.0% | 48.3% | 47.4% | 47.4% [46.4%-51.5%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.7 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuto Oki (`KXITFMATCH-26NOV12OKIJAV-OKI`) | 0.47 / 0.49 (276) | 48.0% | 51.7% | 52.6% | 52.6% [48.5%-53.6%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.7 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1766.0, B 1847.0; serve-point win A 60.5%, B 39.8%; Elo A 1280.4, B 1268.6; model uncertainty 0.0257
* Form inputs: days since last match A 227, B 185; matches on record A 42, B 144; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.010, surface_dev_loose +0.010, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniil Sarksian vs Ammar Faleh Alhogbani -- M15 Kuala Lumpur QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212022:212249:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ammar Faleh Alhogbani (`KXITFMATCH-26NOV12SARALH-ALH`) | 0.25 / 0.29 (423) | 27.0% | 39.9% | 36.1% | 38.6% [37.1%-41.7%] | -- | -- | -- | -- | PASS | +12.9 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daniil Sarksian (`KXITFMATCH-26NOV12SARALH-SAR`) | 0.68 / 0.72 (250) | 70.0% | 60.1% | 63.9% | 61.4% [58.3%-62.9%] | -- | -- | -- | -- | PASS | -9.9 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2188.0, B 1359.0; serve-point win A 58.0%, B 43.9%; Elo A 1227.8, B 1160.7; model uncertainty 0.0231
* Form inputs: days since last match A 213, B 318; matches on record A 62, B 37; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.005, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rigele Te vs James Connel -- M15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144751:212250:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| James Connel (`KXITFMATCH-26NOV12TEXCON-CON`) | 0.22 / 0.27 (68) | 24.5% | 52.3% | 81.2% | 59.5% [48.0%-68.9%] | -- | -- | -- | -- | PASS | +27.9 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rigele Te (`KXITFMATCH-26NOV12TEXCON-TEX`) | 0.71 / 0.74 (9) | 72.5% | 47.6% | 18.8% | 40.5% [31.1%-52.0%] | -- | -- | -- | -- | PASS | -24.9 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1492.0, B 844.0; serve-point win A 62.1%, B 37.4%; Elo A 1414.4, B 1378.7; model uncertainty 0.1047
* Form inputs: days since last match A 17, B 199; matches on record A 319, B 26; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV12TEXCON-CON  (YES = James Connel)
Model: 52%
Kalshi: 24%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yue Xia vs Noritaka Koizumi -- M15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212476:213883:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Noritaka Koizumi (`KXITFMATCH-26NOV12XIAKOI-KOI`) | 0.61 / 0.64 (1) | 62.5% | 69.2% | 74.8% | 62.6% [61.2%-66.9%] | -- | -- | -- | -- | PASS | +6.7 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yue Xia (`KXITFMATCH-26NOV12XIAKOI-XIA`) | 0.35 / 0.37 (339) | 36.0% | 30.8% | 25.2% | 37.4% [33.1%-38.8%] | -- | -- | -- | -- | PASS | -5.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 202.0, B 190.0; serve-point win A 58.9%, B 37.1%; Elo A 1205.9, B 1285.6; model uncertainty 0.0285
* Form inputs: days since last match A 430, B 227; matches on record A 4, B 8; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zhao Zhao vs Jordan Chiu -- M15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206888:207780:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jordan Chiu (`KXITFMATCH-26NOV12ZHACHI-CHI`) | 0.40 / 0.43 (7) | 41.5% | 24.1% | 31.1% | 27.5% [27.2%-28.0%] | -- | -- | -- | -- | PASS | -17.4 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zhao Zhao (`KXITFMATCH-26NOV12ZHACHI-ZHA`) | 0.56 / 0.57 (168) | 56.5% | 75.9% | 68.9% | 72.5% [72.0%-72.8%] | -- | -- | -- | -- | PASS | +19.4 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 155.0, B 402.0; serve-point win A 62.5%, B 43.0%; Elo A 1177.3, B 1004.9; model uncertainty 0.004
* Form inputs: days since last match A 220, B 199; matches on record A 25, B 30; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV12ZHACHI-ZHA  (YES = Zhao Zhao)
Model: 76%
Kalshi: 56%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Berfu Cengiz vs Heather Watson -- W50 Yokohama QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:201586:214507:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Berfu Cengiz (`KXITFWMATCH-26NOV12CENWAT-CEN`) | 0.50 / 0.54 (304) | 52.0% | 33.0% | 48.9% | 38.0% [32.1%-42.1%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -19.0 pp | HIGH_REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Heather Watson (`KXITFWMATCH-26NOV12CENWAT-WAT`) | 0.45 / 0.48 (356) | 46.5% | 67.0% | 51.1% | 62.0% [57.9%-67.9%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +20.5 pp | HIGH_REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1612.0, B 2194.0; serve-point win A 53.9%, B 42.8%; Elo A 1571.0, B 1732.8; model uncertainty 0.0502
* Form inputs: days since last match A 44, B 12; matches on record A 455, B 824; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV12CENWAT-WAT  (YES = Heather Watson)
Model: 67%
Kalshi: 46%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.000, surface_dev_loose +0.025, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carol Young Suh Lee vs Hayu Kinoshita -- W75 Brisbane QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221803:260171:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hayu Kinoshita (`KXITFWMATCH-26NOV12LEEKIN-KIN`) | 0.25 / 0.27 (449) | 26.0% | 32.9% | 52.1% | 44.3% [38.6%-47.4%] | 26.4% | -- | 26.4% | MODEL_LONE_OUTLIER | WATCH | +6.9 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Carol Young Suh Lee (`KXITFWMATCH-26NOV12LEEKIN-LEE`) | 0.73 / 0.75 (299) | 74.0% | 67.1% | 47.9% | 55.7% [52.6%-61.4%] | 73.6% | -- | 73.6% | MODEL_LONE_OUTLIER | PASS | -6.9 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4047.0, B 3494.0; serve-point win A 60.3%, B 43.1%; Elo A 1774.5, B 1614.1; model uncertainty 0.0439
* Form inputs: days since last match A 10, B 12; matches on record A 160, B 177; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.010, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kyoka Okamura vs Rinko Matsuda -- W50 Yokohama QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211846:259690:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rinko Matsuda (`KXITFWMATCH-26NOV12OKAMAT-MAT`) | 0.27 / 0.30 (5) | 28.5% | 33.5% | 69.7% | 55.8% [37.5%-62.9%] | 30.3% | -- | 30.3% | MODEL_LONE_OUTLIER | WATCH | +5.0 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Kyoka Okamura (`KXITFWMATCH-26NOV12OKAMAT-OKA`) | 0.67 / 0.71 (61) | 69.0% | 66.5% | 30.3% | 44.2% [37.0%-62.5%] | 69.7% | -- | 69.7% | MODEL_LONE_OUTLIER | PASS | -2.5 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 2971.0, B 2804.0; serve-point win A 58.0%, B 45.2%; Elo A 1649.2, B 1494.2; model uncertainty 0.1273
* Form inputs: days since last match A 9, B 12; matches on record A 631, B 204; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jiaqi Wang vs Alina Tikhonova -- W15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221181:270431:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alina Tikhonova (`KXITFWMATCH-26NOV12WANTIK-TIK`) | 0.66 / 0.71 (19) | 68.5% | 34.9% | 43.6% | 38.9% [36.4%-42.0%] | -- | -- | -- | -- | PASS | -33.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jiaqi Wang (`KXITFWMATCH-26NOV12WANTIK-WAN`) | 0.30 / 0.33 (29) | 31.5% | 65.1% | 56.4% | 61.1% [58.0%-63.6%] | -- | -- | -- | -- | PASS | +33.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2849.0, B 349.0; serve-point win A 54.2%, B 48.7%; Elo A 1543.7, B 1453.2; model uncertainty 0.0282
* Form inputs: days since last match A 199, B 283; matches on record A 250, B 5; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV12WANTIK-WAN  (YES = Jiaqi Wang)
Model: 65%
Kalshi: 32%
Gap: +34 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xinxin Yao vs Emerson Jones -- W75 Brisbane QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:252587:263644:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emerson Jones (`KXITFWMATCH-26NOV12YAOJON-JON`) | 0.74 / 0.77 (742) | 75.5% | 82.6% | 82.1% | 80.7% [77.6%-82.5%] | 74.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Xinxin Yao (`KXITFWMATCH-26NOV12YAOJON-YAO`) | 0.22 / 0.25 (299) | 23.5% | 17.4% | 17.9% | 19.3% [17.5%-22.4%] | 25.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2972.0, B 3547.0; serve-point win A 50.9%, B 42.0%; Elo A 1573.7, B 1788.5; model uncertainty 0.0241
* Form inputs: days since last match A 38, B 9; matches on record A 320, B 156; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.004, surface_dev_loose +0.000, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Thanapet Chanta vs Tsz Fu Wong -- M15 Hua Hin QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207788:212971:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thanapet Chanta (`KXITFMATCH-26NOV12CHAWON-CHA`) | 0.90 / 0.94 (128) | 92.0% | 86.7% | 91.3% | 84.1% [81.1%-88.6%] | -- | -- | -- | -- | PASS | -5.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tsz Fu Wong (`KXITFMATCH-26NOV12CHAWON-WON`) | 0.05 / 0.07 (28) | 6.0% | 13.3% | 8.7% | 15.9% [11.4%-18.9%] | -- | -- | -- | -- | PASS | +7.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2163.0, B 498.0; serve-point win A 63.7%, B 44.9%; Elo A 1328.2, B 1070.2; model uncertainty 0.0374
* Form inputs: days since last match A 178, B 55; matches on record A 160, B 20; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.006, surface_pool_high -0.000, surface_dev_loose +0.012, surface_dev_tight -0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hao Sheng Koay vs Azuma Visaya -- M15 Kuala Lumpur QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144896:210405:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hao Sheng Koay (`KXITFMATCH-26NOV12KOAVIS-KOA`) | 0.45 / 0.49 (293) | 47.0% | 49.5% | 47.9% | 54.7% [54.1%-56.2%] | -- | -- | -- | -- | PASS | +2.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Azuma Visaya (`KXITFMATCH-26NOV12KOAVIS-VIS`) | 0.50 / 0.53 (3) | 51.5% | 50.5% | 52.1% | 45.3% [43.8%-45.9%] | -- | -- | -- | -- | PASS | -1.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 241.0, B 253.0; serve-point win A 58.8%, B 41.1%; Elo A 1273.3, B 1230.0; model uncertainty 0.0102
* Form inputs: days since last match A 367, B 353; matches on record A 10, B 11; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Denis Yevseyev vs Fons Van Sambeek -- M15 Hua Hin QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106187:209913:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fons Van Sambeek (`KXITFMATCH-26NOV12YEVVAN-VAN`) | 0.38 / 0.42 (250) | 40.0% | 26.7% | 39.2% | 25.3% [16.1%-30.9%] | -- | -- | -- | -- | PASS | -13.3 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Denis Yevseyev (`KXITFMATCH-26NOV12YEVVAN-YEV`) | 0.52 / 0.58 (5) | 55.0% | 73.3% | 60.8% | 74.7% [69.1%-83.9%] | -- | -- | -- | -- | PASS | +18.3 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5377.0, B 1119.0; serve-point win A 60.8%, B 44.0%; Elo A 1524.8, B 1248.8; model uncertainty 0.0743
* Form inputs: days since last match A 66, B 199; matches on record A 911, B 58; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV12YEVVAN-YEV  (YES = Denis Yevseyev)
Model: 73%
Kalshi: 55%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.028, surface_pool_high -0.035, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Barry / Kawaguchi vs Stevens / Thompson -- W75 Brisbane SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12BARKAWSTETHO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barry / Kawaguchi (`KXITFWDOUBLES-26NOV12BARKAWSTETHO-BARKAW`) | 0.55 / 0.74 (5) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stevens / Thompson (`KXITFWDOUBLES-26NOV12BARKAWSTETHO-STETHO`) | 0.21 / 0.38 (1) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sheng Tang vs Dong Ju Kim -- M15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207456:207463:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dong Ju Kim (`KXITFMATCH-26NOV12TANKIM-KIM`) | 0.71 / 0.76 (73) | 73.5% | 70.3% | 67.8% | 67.3% [65.5%-68.7%] | -- | -- | -- | -- | PASS | -3.2 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sheng Tang (`KXITFMATCH-26NOV12TANKIM-TAN`) | 0.23 / 0.25 (286) | 24.0% | 29.7% | 32.2% | 32.7% [31.3%-34.5%] | -- | -- | -- | -- | PASS | +5.7 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 714.0, B 1454.0; serve-point win A 58.8%, B 37.0%; Elo A 1177.1, B 1293.7; model uncertainty 0.016
* Form inputs: days since last match A 206, B 213; matches on record A 92, B 54; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.009, surface_dev_loose +0.000, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Huang / Zhang vs Gadecki / Wen Wan -- W75 Brisbane SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12HUAZHAGADWEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gadecki / Wen Wan (`KXITFWDOUBLES-26NOV12HUAZHAGADWEN-GADWEN`) | 0.11 / 0.83 (1) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Huang / Zhang (`KXITFWDOUBLES-26NOV12HUAZHAGADWEN-HUAZHA`) | 0.10 / 0.84 (24) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Thasaporn Naklo vs Ikumi Yamazaki -- W15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220597:221265:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thasaporn Naklo (`KXITFWMATCH-26NOV12NAKYAM-NAK`) | 0.70 / 0.74 (250) | 72.0% | 45.9% | 48.9% | 47.9% [42.6%-51.1%] | -- | -- | -- | -- | PASS | -26.1 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ikumi Yamazaki (`KXITFWMATCH-26NOV12NAKYAM-YAM`) | 0.28 / 0.29 (330) | 28.5% | 54.1% | 51.1% | 52.1% [48.9%-57.4%] | -- | -- | -- | -- | PASS | +25.6 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2173.0, B 1933.0; serve-point win A 54.6%, B 44.6%; Elo A 1456.9, B 1477.0; model uncertainty 0.0424
* Form inputs: days since last match A 199, B 199; matches on record A 166, B 215; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV12NAKYAM-YAM  (YES = Ikumi Yamazaki)
Model: 54%
Kalshi: 28%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.026, surface_pool_high +0.032, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yushan Shao vs Valeria Savinykh -- W15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:202443:269253:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valeria Savinykh (`KXITFWMATCH-26NOV12SHASAV-SAV`) | 0.41 / 0.45 (13) | 43.0% | 62.4% | 33.9% | 59.5% [51.1%-71.7%] | -- | -- | -- | -- | PASS | +19.4 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yushan Shao (`KXITFWMATCH-26NOV12SHASAV-SHA`) | 0.55 / 0.56 (58) | 55.5% | 37.6% | 66.1% | 40.5% [28.3%-48.9%] | -- | -- | -- | -- | PASS | -17.9 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1123.0, B 1181.0; serve-point win A 52.6%, B 45.1%; Elo A 1398.2, B 1611.5; model uncertainty 0.1033
* Form inputs: days since last match A 37, B 44; matches on record A 29, B 735; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV12SHASAV-SAV  (YES = Valeria Savinykh)
Model: 62%
Kalshi: 43%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.010, surface_dev_loose +0.011, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arina Varaksina vs Xi Luo -- W15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:255662:264069:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xi Luo (`KXITFWMATCH-26NOV12VARLUO-LUO`) | 0.67 / 0.70 (45) | 68.5% | 79.6% | 85.2% | 74.4% [69.4%-79.3%] | -- | -- | -- | -- | PASS | +11.1 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Arina Varaksina (`KXITFWMATCH-26NOV12VARLUO-VAR`) | 0.29 / 0.32 (12) | 30.5% | 20.4% | 14.8% | 25.6% [20.7%-30.6%] | -- | -- | -- | -- | PASS | -10.1 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 586.0, B 827.0; serve-point win A 50.0%, B 43.8%; Elo A 1277.4, B 1415.7; model uncertainty 0.0493
* Form inputs: days since last match A 206, B 199; matches on record A 27, B 43; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.017, surface_dev_tight +0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oscar Brown vs Sanhui Shin -- M15 Hua Hin QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12BROSHI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oscar Brown (`KXITFMATCH-26NOV12BROSHI-BRO`) | 0.35 / 0.39 (52) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sanhui Shin (`KXITFMATCH-26NOV12BROSHI-SHI`) | 0.58 / 0.64 (313) | 61.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kuan-Shou Chen vs Ergi Kirkin -- M15 Hua Hin QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-13T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144985:213769:2026-11-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kuan-Shou Chen (`KXITFMATCH-26NOV12CHEKIR-CHE`) | 0.45 / 0.49 (54) | 47.0% | 13.7% | 18.6% | 16.9% [13.0%-21.9%] | -- | -- | -- | -- | PASS | -33.3 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ergi Kirkin (`KXITFMATCH-26NOV12CHEKIR-KIR`) | 0.49 / 0.51 (250) | 50.0% | 86.3% | 81.4% | 83.1% [78.1%-87.1%] | -- | -- | -- | -- | PASS | +36.3 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 224.0, B 3401.0; serve-point win A 53.5%, B 38.1%; Elo A 1173.8, B 1451.9; model uncertainty 0.0448
* Form inputs: days since last match A 10, B 94; matches on record A 6, B 492; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV12CHEKIR-KIR  (YES = Ergi Kirkin)
Model: 86%
Kalshi: 50%
Gap: +36 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.039, surface_pool_high +0.050, surface_dev_loose -0.003, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hosoki / Katsumi vs Li / Saito -- W50 Yokohama SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12HOSKATLIXSAI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hosoki / Katsumi (`KXITFWDOUBLES-26NOV12HOSKATLIXSAI-HOSKAT`) | 0.10 / 0.84 (2) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Li / Saito (`KXITFWDOUBLES-26NOV12HOSKATLIXSAI-LIXSAI`) | 0.11 / 0.84 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kim / Morisaki vs Kuwata / Shimizu -- W50 Yokohama SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12KIMMORKUWSHI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kim / Morisaki (`KXITFWDOUBLES-26NOV12KIMMORKUWSHI-KIMMOR`) | 0.08 / 0.83 (100) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kuwata / Shimizu (`KXITFWDOUBLES-26NOV12KIMMORKUWSHI-KUWSHI`) | 0.11 / 0.83 (100) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Nikola Mektic / Edouard Roger-Vasselin vs Adam Pavlasek / Patrik Rikl -- ATP Stockholm SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-13 15:00Z
* Current expected start: 2026-11-13 10:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-12 16:57Z
* Recommended handicap-by time: 2026-11-13 09:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-13T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13MEKROGPAVRIK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikola Mektic / Edouard Roger-Vasselin (`KXATPDOUBLES-26NOV13MEKROGPAVRIK-MEKROG`) | 0.29 / 0.92 (27) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Adam Pavlasek / Patrik Rikl (`KXATPDOUBLES-26NOV13MEKROGPAVRIK-PAVRIK`) | 0.06 / 0.75 (7) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Faleh Alhogbani / Cherie Ligniere vs Eichenseher / Mueller -- M15 Kuala Lumpur SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13FALCHEEICMUE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eichenseher / Mueller (`KXITFDOUBLES-26NOV13FALCHEEICMUE-EICMUE`) | 0.62 / 0.81 (25) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Faleh Alhogbani / Cherie Ligniere (`KXITFDOUBLES-26NOV13FALCHEEICMUE-FALCHE`) | 0.16 / 0.32 (128) | 24.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jeong / Yang vs Aleshchev / Storch -- M15 Maanshan SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13JEOYANALESTO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aleshchev / Storch (`KXITFDOUBLES-26NOV13JEOYANALESTO-ALESTO`) | 0.05 / 0.24 (56) | 14.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jeong / Yang (`KXITFDOUBLES-26NOV13JEOYANALESTO-JEOYAN`) | 0.70 / 0.89 (26) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Liu / Xiao vs Jin / Sun -- M15 Maanshan SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13LIUXIAJINSUN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jin / Sun (`KXITFDOUBLES-26NOV13LIUXIAJINSUN-JINSUN`) | 0.09 / 0.89 (56) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Liu / Xiao (`KXITFDOUBLES-26NOV13LIUXIAJINSUN-LIUXIA`) | 0.05 / 0.89 (56) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Oki / Taka vs Rifqi Fitriadi / Sarksian -- M15 Kuala Lumpur SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13OKITAKRIFSAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oki / Taka (`KXITFDOUBLES-26NOV13OKITAKRIFSAR-OKITAK`) | 0.06 / 0.89 (56) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rifqi Fitriadi / Sarksian (`KXITFDOUBLES-26NOV13OKITAKRIFSAR-RIFSAR`) | 0.05 / 0.89 (56) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Hou / Plipuech vs Cao / Tikhonova -- W15 Maanshan SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV13HOUPLICAOTIK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cao / Tikhonova (`KXITFWDOUBLES-26NOV13HOUPLICAOTIK-CAOTIK`) | 0.12 / 0.79 (100) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hou / Plipuech (`KXITFWDOUBLES-26NOV13HOUPLICAOTIK-HOUPLI`) | 0.15 / 0.84 (23) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Im / Shin vs Guo / An Lin -- W15 Maanshan SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV13IMXSHIGUOANL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Guo / An Lin (`KXITFWDOUBLES-26NOV13IMXSHIGUOANL-GUOANL`) | 0.11 / 0.84 (3) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Im / Shin (`KXITFWDOUBLES-26NOV13IMXSHIGUOANL-IMXSHI`) | 0.10 / 0.84 (3) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Chanta / Sornlaksup vs Sumizawa / Vithoontien -- M15 Hua Hin SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13CHASORSUMVIT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chanta / Sornlaksup (`KXITFDOUBLES-26NOV13CHASORSUMVIT-CHASOR`) | 0.51 / 0.69 (76) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sumizawa / Vithoontien (`KXITFDOUBLES-26NOV13CHASORSUMVIT-SUMVIT`) | 0.27 / 0.43 (1) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Koaykul / Navasirisomboon vs Huang / Lu -- M15 Hua Hin SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13KOANAVHUALUX:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Huang / Lu (`KXITFDOUBLES-26NOV13KOANAVHUALUX-HUALUX`) | 0.08 / 0.89 (1) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Koaykul / Navasirisomboon (`KXITFDOUBLES-26NOV13KOANAVHUALUX-KOANAV`) | 0.06 / 0.89 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Evgenii Tiurnev vs Dmitry Popko -- M15 Antalya QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13TIUPOP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dmitry Popko (`KXITFMATCH-26NOV13TIUPOP-POP`) | 0.60 / 0.78 (1) | 69.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Evgenii Tiurnev (`KXITFMATCH-26NOV13TIUPOP-TIU`) | 0.17 / 0.34 (1) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ali Yazdani vs Stefan Adrian Andreescu -- M15 Antalya QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13YAZAND:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefan Adrian Andreescu (`KXITFMATCH-26NOV13YAZAND-AND`) | 0.72 / 0.81 (435) | 76.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ali Yazdani (`KXITFMATCH-26NOV13YAZAND-YAZ`) | 0.17 / 0.24 (343) | 20.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anais Gabriel vs Asylzhan Arystanbekova -- W15 Antalya QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV13GABARY:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Asylzhan Arystanbekova (`KXITFWMATCH-26NOV13GABARY-ARY`) | 0.75 / 0.80 (36) | 77.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anais Gabriel (`KXITFWMATCH-26NOV13GABARY-GAB`) | 0.16 / 0.25 (35) | 20.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Diana-Ioana Simionescu vs Andreea Prisacariu -- W15 Antalya QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV13SIMPRI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andreea Prisacariu (`KXITFWMATCH-26NOV13SIMPRI-PRI`) | 0.39 / 0.45 (320) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Diana-Ioana Simionescu (`KXITFWMATCH-26NOV13SIMPRI-SIM`) | 0.52 / 0.59 (1) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daria Yesypchuk vs Valeriia Iushchenko -- W15 Antalya QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV13YESIUS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valeriia Iushchenko (`KXITFWMATCH-26NOV13YESIUS-IUS`) | 0.51 / 0.61 (4) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daria Yesypchuk (`KXITFWMATCH-26NOV13YESIUS-YES`) | 0.37 / 0.43 (44) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pierre Yves Bailly vs Filiberto Fumagalli -- M15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13BAIFUM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pierre Yves Bailly (`KXITFMATCH-26NOV13BAIFUM-BAI`) | 0.77 / 0.86 (138) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Filiberto Fumagalli (`KXITFMATCH-26NOV13BAIFUM-FUM`) | 0.10 / 0.18 (5) | 14.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lorenzo Bocchi vs Yurii Dzhavakian -- M15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13BOCDZH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Bocchi (`KXITFMATCH-26NOV13BOCDZH-BOC`) | 0.45 / 0.67 (1) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yurii Dzhavakian (`KXITFMATCH-26NOV13BOCDZH-DZH`) | 0.28 / 0.47 (3) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Antoni Fabre vs Alan Wazny -- M15 Antalya QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13FABWAZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Antoni Fabre (`KXITFMATCH-26NOV13FABWAZ-FAB`) | 0.20 / 0.25 (34) | 22.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alan Wazny (`KXITFMATCH-26NOV13FABWAZ-WAZ`) | 0.71 / 0.79 (250) | 75.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marek Gengel vs Hazem Naw -- M15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13GENNAW:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marek Gengel (`KXITFMATCH-26NOV13GENNAW-GEN`) | 0.65 / 0.68 (305) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hazem Naw (`KXITFMATCH-26NOV13GENNAW-NAW`) | 0.29 / 0.35 (5) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Robert Guna vs Mac Visser -- M15 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13GUNVIS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Robert Guna (`KXITFMATCH-26NOV13GUNVIS-GUN`) | 0.65 / 0.71 (291) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mac Visser (`KXITFMATCH-26NOV13GUNVIS-VIS`) | 0.28 / 0.34 (29) | 31.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Michel Hopp vs Imanol Lopez Morillo -- M15 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13HOPLOP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michel Hopp (`KXITFMATCH-26NOV13HOPLOP-HOP`) | 0.38 / 0.43 (4) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Imanol Lopez Morillo (`KXITFMATCH-26NOV13HOPLOP-LOP`) | 0.50 / 0.61 (294) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Miles Jones vs Josip Simundza -- M15 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13JONSIM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miles Jones (`KXITFMATCH-26NOV13JONSIM-JON`) | 0.63 / 0.67 (4) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Josip Simundza (`KXITFMATCH-26NOV13JONSIM-SIM`) | 0.30 / 0.34 (2) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jannik Maute vs Dragos Nicolae Madaras -- M15 Antalya QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13MAUMAD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dragos Nicolae Madaras (`KXITFMATCH-26NOV13MAUMAD-MAD`) | 0.72 / 0.83 (2) | 77.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jannik Maute (`KXITFMATCH-26NOV13MAUMAD-MAU`) | 0.11 / 0.23 (3) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arthur Weber vs Flynn Thomas -- M15 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13WEBTHO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Flynn Thomas (`KXITFMATCH-26NOV13WEBTHO-THO`) | 0.29 / 0.30 (19) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arthur Weber (`KXITFMATCH-26NOV13WEBTHO-WEB`) | 0.68 / 0.74 (401) | 71.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jan Wygona vs Artur Kukasian -- M15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13WYGKUK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Artur Kukasian (`KXITFMATCH-26NOV13WYGKUK-KUK`) | 0.66 / 0.74 (1) | 70.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jan Wygona (`KXITFMATCH-26NOV13WYGKUK-WYG`) | 0.21 / 0.29 (3) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anastasija Cvetkovic vs Alisa Oktiabreva -- W35 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV13CVEOKT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasija Cvetkovic (`KXITFWMATCH-26NOV13CVEOKT-CVE`) | 0.10 / 0.13 (41) | 11.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alisa Oktiabreva (`KXITFWMATCH-26NOV13CVEOKT-OKT`) | 0.87 / 0.90 (23) | 88.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yekaterina Dmitrichenko vs Mu Jie Tzeng -- W15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV13DMITZE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yekaterina Dmitrichenko (`KXITFWMATCH-26NOV13DMITZE-DMI`) | 0.55 / 0.72 (3) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mu Jie Tzeng (`KXITFWMATCH-26NOV13DMITZE-TZE`) | 0.19 / 0.39 (5) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anastasia Efremova vs Lamis Alhussein Abdel Aziz -- W15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV13EFRALH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lamis Alhussein Abdel Aziz (`KXITFWMATCH-26NOV13EFRALH-ALH`) | 0.66 / 0.85 (6) | 75.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anastasia Efremova (`KXITFWMATCH-26NOV13EFRALH-EFR`) | 0.07 / 0.27 (56) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yasmin Ezzat vs Anna Snigireva -- W15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV13EZZSNI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yasmin Ezzat (`KXITFWMATCH-26NOV13EZZSNI-EZZ`) | 0.56 / 0.75 (5) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anna Snigireva (`KXITFWMATCH-26NOV13EZZSNI-SNI`) | 0.19 / 0.37 (3) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sapfo Sakellaridi vs Matilde Paoletti -- W35 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV13SAKPAO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matilde Paoletti (`KXITFWMATCH-26NOV13SAKPAO-PAO`) | 0.79 / 0.84 (3) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sapfo Sakellaridi (`KXITFWMATCH-26NOV13SAKPAO-SAK`) | 0.15 / 0.19 (7) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ilay Yoruk vs Marija Lauva -- W15 Antalya QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV13YORLAU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marija Lauva (`KXITFWMATCH-26NOV13YORLAU-LAU`) | 0.32 / 0.39 (10) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ilay Yoruk (`KXITFWMATCH-26NOV13YORLAU-YOR`) | 0.61 / 0.65 (350) | 63.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aurora Zantedeschi vs Lucia Cortez Llorca -- W35 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV13ZANCOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucia Cortez Llorca (`KXITFWMATCH-26NOV13ZANCOR-COR`) | 0.37 / 0.40 (42) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aurora Zantedeschi (`KXITFWMATCH-26NOV13ZANCOR-ZAN`) | 0.59 / 0.64 (9) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andrea Colombo vs Wissam Abderrahman -- M15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13COLABD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wissam Abderrahman (`KXITFMATCH-26NOV13COLABD-ABD`) | 0.54 / 0.66 (1) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Andrea Colombo (`KXITFMATCH-26NOV13COLABD-COL`) | 0.31 / 0.43 (4) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tuncay Duran vs Nikita Belozertsev -- M15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13DURBEL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikita Belozertsev (`KXITFMATCH-26NOV13DURBEL-BEL`) | 0.32 / 0.78 (40) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tuncay Duran (`KXITFMATCH-26NOV13DURBEL-DUR`) | 0.57 / 0.68 (7) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Julien Penzlin vs Amaury Raynel -- M15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13PENRAY:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julien Penzlin (`KXITFMATCH-26NOV13PENRAY-PEN`) | 0.59 / 0.74 (31) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Amaury Raynel (`KXITFMATCH-26NOV13PENRAY-RAY`) | 0.29 / 0.44 (28) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anastasia Bertacchi vs Lavinia Luciano -- W15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV13BERLUC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasia Bertacchi (`KXITFWMATCH-26NOV13BERLUC-BER`) | 0.67 / 0.79 (3) | 73.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lavinia Luciano (`KXITFWMATCH-26NOV13BERLUC-LUC`) | 0.17 / 0.74 (10) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anastasia Lizunova vs Louanne Djafari -- W15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV13LIZDJA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Louanne Djafari (`KXITFWMATCH-26NOV13LIZDJA-DJA`) | 0.04 / 0.15 (7) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anastasia Lizunova (`KXITFWMATCH-26NOV13LIZDJA-LIZ`) | 0.85 / 0.94 (7) | 89.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matilde Mariani vs Mia Horvit -- W15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV13MARHOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mia Horvit (`KXITFWMATCH-26NOV13MARHOR-HOR`) | 0.61 / 0.67 (3) | 64.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matilde Mariani (`KXITFWMATCH-26NOV13MARHOR-MAR`) | 0.25 / 0.35 (4) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bothma / Gabet vs Kaan Oktay / Schlossmann -- M15 Sharm ElSheikh SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13BOTGABKAASCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bothma / Gabet (`KXITFDOUBLES-26NOV13BOTGABKAASCH-BOTGAB`) | 0.01 / 0.90 (2) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kaan Oktay / Schlossmann (`KXITFDOUBLES-26NOV13BOTGABKAASCH-KAASCH`) | 0.01 / 0.90 (2) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Stanke / Van Herck vs Blazka / Gengel -- M15 Sharm ElSheikh SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-13T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV13STAVANBLAGEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Blazka / Gengel (`KXITFDOUBLES-26NOV13STAVANBLAGEN-BLAGEN`) | 0.01 / 0.90 (2) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stanke / Van Herck (`KXITFDOUBLES-26NOV13STAVANBLAGEN-STAVAN`) | 0.01 / 0.90 (2) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sandra Samir vs Alyssa Reguer -- W15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-13 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-13T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV13SAMREG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alyssa Reguer (`KXITFWMATCH-26NOV13SAMREG-REG`) | 0.19 / 0.38 (56) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sandra Samir (`KXITFWMATCH-26NOV13SAMREG-SAM`) | 0.55 / 0.73 (4) | 64.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
