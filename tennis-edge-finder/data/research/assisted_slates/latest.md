# ASSISTED SLATE -- 2026-10-13T15:10Z (`SL-20261013T151020Z-6000ac3a`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

274 open matches not seen started, 689 markets. Skipped: {"no_match_winner_listed": 1, "first_ball_already_observed": 8, "scheduled_start_over_24h_past": 2}. Sources: shadow board 2026-10-13T14:40:14.970603+00:00, Model 4 2026-10-13T14:40:52.142743+00:00, Gen-1 ledger 2026-10-13T14:40:11.462969+00:00, external 2026-10-13T14:49:13.691501+00:00, capture 20261013T145715Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-10-14 03:00Z**
* Recommended RUN TENNIS time: **2026-10-14 02:15Z**
* Final price/status check time: **2026-10-14 02:50Z**
* Number of matches in window: 9 (Sonay Kartal vs Belinda Bencic, Marie Bouzkova vs Maja Chwalinska, Magdalena Frech vs Iga Swiatek, Elina Svitolina vs Liudmila Samsonova, Botic Van de Zandschulp vs Rafael Jodar, Iva Jovic vs Dayana Yastremska ...)

* **1 main-tour match(es) have NO verified start status** (START_UNKNOWN): BET blocked until a live status check.

Slate built 2026-10-13T15:10Z. Refresh due by: 2026-10-14 02:15Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 50, "HIGH_REVIEW": 52, "NORMAL": 259, "REVIEW": 66, "UNPRICED": 262}; match winners: {"EXTREME": 50, "HIGH_REVIEW": 43, "NORMAL": 148, "REVIEW": 48, "UNPRICED": 259}; quote freshness at build: {"FRESH": 427}.

## Sabastiani Leon vs Florentine Dekkers -- W15 Islamabad R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214800:223334:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Florentine Dekkers (`KXITFWMATCH-26OCT13LEODEK-DEK`) | 0.74 / 0.82 (40) | 78.0% | 50.2% | 84.9% | 53.2% [53.2%-53.2%] | 55.2% | -- | 55.2% | KALSHI_LONE_OUTLIER | PASS | -27.8 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | AGREES_WITH_MODEL | AMBIGUOUS |
| Sabastiani Leon (`KXITFWMATCH-26OCT13LEODEK-LEO`) | 0.17 / 0.23 (5) | 20.0% | 49.8% | 15.1% | 46.8% [46.8%-46.8%] | 44.8% | -- | 44.8% | KALSHI_LONE_OUTLIER | PASS | +29.8 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | AGREES_WITH_MODEL | AMBIGUOUS |

* Serve evidence (points): A 1097.0, B 0.0; serve-point win A 51.5%, B 48.4%; Elo A 1212.7, B 1233.7; model uncertainty 0.0
* Form inputs: days since last match A 79, B 791; matches on record A 227, B 21; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT13LEODEK-LEO  (YES = Sabastiani Leon)
Model: 50%
Kalshi: 20%
Gap: +30 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_MODEL
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, SCHEDULED_START_PASSED, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sara Victoria Balan vs Anastasiia Nikolaieva -- W15 Chisinau R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13BALNIK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Victoria Balan (`KXITFWMATCH-26OCT13BALNIK-BAL`) | 0.48 / 0.54 (5) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anastasiia Nikolaieva (`KXITFWMATCH-26OCT13BALNIK-NIK`) | 0.41 / 0.48 (5) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Melinda Biro vs Maria Pankratova -- W15 Chisinau R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13BIRPAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Melinda Biro (`KXITFWMATCH-26OCT13BIRPAN-BIR`) | 0.47 / 0.84 (1) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maria Pankratova (`KXITFWMATCH-26OCT13BIRPAN-PAN`) | 0.05 / 0.55 (10) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anastasiya Kuparev vs Sabrina Olimjanova -- W15 Islamabad R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223398:263850:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasiya Kuparev (`KXITFWMATCH-26OCT13KUPOLI-KUP`) | 0.22 / 0.24 (0) | 23.0% | 46.6% | 55.8% | 44.7% [40.5%-47.3%] | 33.0% | -- | 33.0% | MODEL_LONE_OUTLIER | PASS | +23.6 pp | HIGH_REVIEW | FRESH | D / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Sabrina Olimjanova (`KXITFWMATCH-26OCT13KUPOLI-OLI`) | 0.71 / 0.75 (5) | 73.0% | 53.4% | 44.2% | 55.3% [52.7%-59.5%] | 67.0% | -- | 67.0% | MODEL_LONE_OUTLIER | PASS | -19.6 pp | HIGH_REVIEW | FRESH | D / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 723.0, B 500.0; serve-point win A 54.2%, B 45.1%; Elo A 1178.2, B 1242.2; model uncertainty 0.0342
* Form inputs: days since last match A 196, B 357; matches on record A 121, B 39; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT13KUPOLI-KUP  (YES = Anastasiya Kuparev)
Model: 47%
Kalshi: 23%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: SUPPORTS_MODEL_DIRECTION
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.021, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sophie Luescher vs Maria Mikhailova -- W15 Chisinau R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221153:223153:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sophie Luescher (`KXITFWMATCH-26OCT13LUEMIK-LUE`) | 0.93 / 0.96 (1) | 94.5% | 64.4% | 55.3% | 65.6% [61.6%-68.5%] | 88.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -30.1 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Mikhailova (`KXITFWMATCH-26OCT13LUEMIK-MIK`) | 0.03 / 0.06 (8) | 4.5% | 35.6% | 44.7% | 34.4% [31.5%-38.4%] | 11.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +31.1 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 175.0, B 1234.0; serve-point win A 53.8%, B 49.0%; Elo A 1282.5, B 1162.7; model uncertainty 0.0347
* Form inputs: days since last match A 168, B 168; matches on record A 77, B 163; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT13LUEMIK-MIK  (YES = Maria Mikhailova)
Model: 36%
Kalshi: 4%
Gap: +31 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.040, surface_pool_high +0.029, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aliesia Reva vs Defne Cirpanli -- W15 Chisinau R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222856:241018:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Defne Cirpanli (`KXITFWMATCH-26OCT13REVCIR-CIR`) | 0.32 / 0.47 (65) | 39.5% | 69.9% | 62.5% | 65.0% [60.5%-68.8%] | 40.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +30.4 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aliesia Reva (`KXITFWMATCH-26OCT13REVCIR-REV`) | 0.57 / 0.61 (1) | 59.0% | 30.1% | 37.5% | 35.0% [31.2%-39.5%] | 59.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -28.9 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 654.0, B 1730.0; serve-point win A 53.4%, B 42.7%; Elo A 1179.4, B 1291.8; model uncertainty 0.0416
* Form inputs: days since last match A 329, B 163; matches on record A 36, B 224; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT13REVCIR-CIR  (YES = Defne Cirpanli)
Model: 70%
Kalshi: 40%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.030, surface_pool_high -0.019, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Emma Van Poppel vs Nissa Finnigan -- W15 Islamabad R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222748:259890:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nissa Finnigan (`KXITFWMATCH-26OCT13VANFIN-FIN`) | 0.05 / 0.34 (1) | 19.5% | 59.7% | 96.0% | 74.7% [74.6%-74.8%] | -- | -- | -- | -- | PASS | +40.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Emma Van Poppel (`KXITFWMATCH-26OCT13VANFIN-VAN`) | 0.70 / 0.92 (1) | 81.0% | 40.3% | 4.0% | 25.3% [25.2%-25.4%] | -- | -- | -- | -- | PASS | -40.7 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 983.0, B 0.0; serve-point win A 54.5%, B 43.6%; Elo A 1072.5, B 1259.3; model uncertainty 0.0007
* Form inputs: days since last match A 168, B 1652; matches on record A 167, B 3; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT13VANFIN-FIN  (YES = Nissa Finnigan)
Model: 60%
Kalshi: 20%
Gap: +40 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jan Kumstat vs Edas Butvilas -- ATP Challenger Olbia R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 13:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-13T13:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210220:211618:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Edas Butvilas (`KXATPCHALLENGERMATCH-26OCT13KUMBUT-BUT`) | 0.58 / 0.59 (33303) | 58.5% | 28.8% | 16.9% | 25.4% [18.9%-36.9%] | 59.2% | 58.9% | 59.0% | MODEL_LONE_OUTLIER | PASS | -29.7 pp | EXTREME (DATA_WARNING) | FRESH | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Jan Kumstat (`KXATPCHALLENGERMATCH-26OCT13KUMBUT-KUM`) | 0.41 / 0.42 (23041) | 41.5% | 71.2% | 83.1% | 74.6% [63.1%-81.1%] | 40.8% | 41.0% | 40.9% | MODEL_LONE_OUTLIER | WATCH | +29.7 pp | EXTREME (DATA_WARNING) | FRESH | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1433.0, B 3824.0; serve-point win A 67.7%, B 36.9%; Elo A 1680.5, B 1575.0; model uncertainty 0.0903
* Form inputs: days since last match A 43, B 8; matches on record A 35, B 231; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT13KUMBUT-KUM  (YES = Jan Kumstat)
Model: 71%
Kalshi: 42%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: B (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.036, surface_pool_high +0.027, surface_dev_loose +0.029, surface_dev_tight -0.031
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED

## Ekaterina Agureeva vs Andreea Prisacariu -- W15 Chisinau R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214653:266852:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Agureeva (`KXITFWMATCH-26OCT13AGUPRI-AGU`) | 0.09 / 0.15 (31) | 12.0% | -- | 38.4% | 36.4% [28.7%-45.2%] | -- | -- | -- | -- | PASS | +24.4 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Andreea Prisacariu (`KXITFWMATCH-26OCT13AGUPRI-PRI`) | 0.87 / 0.91 (4) | 89.0% | -- | 61.6% | 63.6% [54.8%-71.3%] | -- | -- | -- | -- | PASS | -25.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 144.0, B 2406.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0826
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT13AGUPRI-AGU  (YES = Ekaterina Agureeva)
Model: 36%
Kalshi: 12%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.068, surface_pool_high +0.088, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kei Yau Cheung vs Wozuko Mdlulwa -- W15 Islamabad R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259965:267638:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kei Yau Cheung (`KXITFWMATCH-26OCT13CHEMDL-CHE`) | -- / 0.01 (218) | -- | -- | 52.1% | 40.5% [39.5%-41.5%] | 8.5% | -- | 8.5% | KALSHI_LONE_OUTLIER | PASS | -- | UNPRICED | FRESH | D / POOR | INSUFFICIENT_INPUTS | VERIFIED |
| Wozuko Mdlulwa (`KXITFWMATCH-26OCT13CHEMDL-MDL`) | 0.98 / 0.99 (66) | 98.5% | -- | 47.9% | 59.5% [58.5%-60.6%] | 91.5% | -- | 91.5% | KALSHI_LONE_OUTLIER | PASS | -39.0 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 139.0, B 1106.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0103
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jovanovic / Kroitor vs Marinescu / Williams -- W15 Chisinau R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13JOVKROMARWIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jovanovic / Kroitor (`KXITFWDOUBLES-26OCT13JOVKROMARWIL-JOVKRO`) | 0.05 / 0.86 (1) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marinescu / Williams (`KXITFWDOUBLES-26OCT13JOVKROMARWIL-MARWIL`) | 0.05 / 0.58 (1) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nesmianovych / Pire vs Iurina / Semichina -- W15 Chisinau R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13NESPIRIURSEM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iurina / Semichina (`KXITFWDOUBLES-26OCT13NESPIRIURSEM-IURSEM`) | 0.05 / 0.95 (213) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nesmianovych / Pire (`KXITFWDOUBLES-26OCT13NESPIRIURSEM-NESPIR`) | 0.05 / 0.95 (211) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Giulia Safina Popa vs Daniela Ciobanu -- W15 Chisinau R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211267:267428:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniela Ciobanu (`KXITFWMATCH-26OCT13POPCIO-CIO`) | 0.05 / 0.08 (14) | 6.5% | -- | 13.9% | 16.7% [14.4%-17.4%] | -- | -- | -- | -- | PASS | +10.2 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Giulia Safina Popa (`KXITFWMATCH-26OCT13POPCIO-POP`) | 0.92 / 0.95 (210) | 93.5% | -- | 86.1% | 83.3% [82.6%-85.5%] | -- | -- | -- | -- | PASS | -10.2 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1013.0, B 157.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0149
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Romisa Romisa Malik vs Elena Jamshidi -- W15 Islamabad R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13ROMJAM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elena Jamshidi (`KXITFWMATCH-26OCT13ROMJAM-JAM`) | 0.70 / 0.84 (51) | 77.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Romisa Romisa Malik (`KXITFWMATCH-26OCT13ROMJAM-ROM`) | 0.18 / 0.19 (1) | 18.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hynek Barton vs Maxim Mrva -- ATP Challenger Olbia R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-13T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210558:211617:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hynek Barton (`KXATPCHALLENGERMATCH-26OCT13BARMRV-BAR`) | 0.60 / 0.62 (58) | 61.0% | 46.5% | 64.3% | 59.3% [44.8%-62.8%] | 57.2% | 60.5% | 58.8% | KALSHI_LONE_OUTLIER | PASS | -14.5 pp | REVIEW | FRESH | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Maxim Mrva (`KXATPCHALLENGERMATCH-26OCT13BARMRV-MRV`) | 0.38 / 0.39 (411) | 38.5% | 53.5% | 35.7% | 40.7% [37.2%-55.2%] | 42.8% | 39.3% | 41.0% | KALSHI_LONE_OUTLIER | PASS | +15.0 pp | REVIEW | FRESH | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2459.0, B 3391.0; serve-point win A 58.3%, B 41.0%; Elo A 1579.0, B 1580.7; model uncertainty 0.0901
* Form inputs: days since last match A 198, B 22; matches on record A 131, B 101; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.010, surface_dev_loose +0.010, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED

## Max Wiskandt vs Miguel Damas -- ATP Challenger Catania R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-13T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207732:208328:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miguel Damas (`KXATPCHALLENGERMATCH-26OCT13WISDAM-DAM`) | 0.88 / 0.89 (17168) | 88.5% | 55.7% | 30.6% | 47.4% [40.2%-64.7%] | -- | 60.7% | 60.7% | MODEL_LONE_OUTLIER | PASS | -32.8 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | AGREES_WITH_MODEL | VERIFIED |
| Max Wiskandt (`KXATPCHALLENGERMATCH-26OCT13WISDAM-WIS`) | 0.11 / 0.12 (24141) | 11.5% | 44.3% | 69.5% | 52.6% [35.3%-59.8%] | -- | 38.9% | 38.9% | MODEL_LONE_OUTLIER | PASS | +32.8 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 1551.0, B 2818.0; serve-point win A 58.2%, B 40.7%; Elo A 1434.4, B 1543.7; model uncertainty 0.1226
* Form inputs: days since last match A 701, B 8; matches on record A 146, B 293; data quality F

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT13WISDAM-WIS  (YES = Max Wiskandt)
Model: 44%
Kalshi: 12%
Gap: +33 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: SUPPORTS_MODEL_DIRECTION
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, SCHEDULED_START_PASSED, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED

## Marco Cecchinato vs Pedro Vives Marcos -- ATP Challenger Catania R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-13T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106065:206325:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marco Cecchinato (`KXATPCHALLENGERMATCH-26OCT13CECVIV-CEC`) | 0.29 / 0.30 (34158) | 29.5% | 61.3% | 70.2% | 68.0% [66.6%-68.8%] | -- | 65.0% | 65.0% | MODEL_LONE_OUTLIER | PASS | +31.8 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | AGREES_WITH_MODEL | VERIFIED |
| Pedro Vives Marcos (`KXATPCHALLENGERMATCH-26OCT13CECVIV-VIV`) | 0.71 / 0.72 (30133) | 71.5% | 38.7% | 29.8% | 32.0% [31.1%-33.4%] | -- | 34.4% | 34.4% | MODEL_LONE_OUTLIER | PASS | -32.8 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 4793.0, B 588.0; serve-point win A 63.9%, B 38.3%; Elo A 1631.2, B 1513.7; model uncertainty 0.011
* Form inputs: days since last match A 8, B 8; matches on record A 953, B 172; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT13CECVIV-CEC  (YES = Marco Cecchinato)
Model: 61%
Kalshi: 30%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_MODEL
Data quality: B (LIMITED)
Reasons: THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, LEVEL_TRANSFER_RISK, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED

## Elsa Jacquemot vs Teodora Kostovic -- WTA 125K Rovereto R32

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-13 16:50Z
* Current expected start: 2026-10-13 15:06Z
* Source: COURT_PROGRESSION: preceding match on Court 1 in progress (set 3 of best-of-3); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-13 14:56Z
* Recommended handicap-by time: 2026-10-13 14:21Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA125 (WTA_125) · Hard · scheduled 2026-10-13T16:50:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221039:267439:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elsa Jacquemot (`KXWTACHALLENGERMATCH-26OCT13JACKOS-JAC`) | 0.36 / 0.38 (10887) | 37.0% | 35.8% | 39.6% | 42.2% [40.7%-48.4%] | -- | 37.0% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | -1.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Teodora Kostovic (`KXWTACHALLENGERMATCH-26OCT13JACKOS-KOS`) | 0.62 / 0.64 (23) | 63.0% | 64.2% | 60.4% | 57.8% [51.6%-59.3%] | -- | 62.8% | -- | INSUFFICIENT_INPUTS | PASS | +1.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4592.0, B 3286.0; serve-point win A 56.4%, B 40.8%; Elo A 1708.0, B 1712.2; model uncertainty 0.0388
* Form inputs: days since last match A 1, B 11; matches on record A 401, B 112; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight +0.005
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; STATUS_AMBIGUOUS

## Tristan Boyer vs Alejandro Moro Canas -- ATP Challenger Maia R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 15:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-13T15:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207729:208279:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tristan Boyer (`KXATPCHALLENGERMATCH-26OCT13BOYMOR-BOY`) | 0.64 / 0.65 (889) | 64.5% | 50.3% | 43.4% | 46.9% [45.4%-48.5%] | -- | 47.7% | 47.7% | MARKETS_AGREE | WATCH | -14.2 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Alejandro Moro Canas (`KXATPCHALLENGERMATCH-26OCT13BOYMOR-MOR`) | 0.35 / 0.36 (34554) | 35.5% | 49.7% | 56.6% | 53.1% [51.5%-54.6%] | -- | 52.2% | 52.2% | MARKETS_AGREE | PASS | +14.2 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 2991.0, B 4809.0; serve-point win A 61.1%, B 39.0%; Elo A 1659.4, B 1627.1; model uncertainty 0.0153
* Form inputs: days since last match A 8, B 8; matches on record A 220, B 324; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Michael Vrbensky vs Raul Brancaccio -- ATP Challenger Maia R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 15:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-13T15:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:134840:202398:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raul Brancaccio (`KXATPCHALLENGERMATCH-26OCT13VRBBRA-BRA`) | 0.18 / 0.19 (24308) | 18.5% | 52.6% | 57.6% | 52.6% [51.0%-54.1%] | -- | 69.5% | 69.5% | MODEL_LONE_OUTLIER | PASS | +34.1 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Michael Vrbensky (`KXATPCHALLENGERMATCH-26OCT13VRBBRA-VRB`) | 0.81 / 0.82 (28243) | 81.5% | 47.4% | 42.4% | 47.4% [45.9%-49.0%] | -- | 30.6% | 30.6% | MODEL_LONE_OUTLIER | SHADOW_BET | -34.1 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 1127.0, B 3454.0; serve-point win A 60.7%, B 38.8%; Elo A 1604.8, B 1596.5; model uncertainty 0.0153
* Form inputs: days since last match A 78, B 8; matches on record A 450, B 574; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT13VRBBRA-BRA  (YES = Raul Brancaccio)
Model: 53%
Kalshi: 18%
Gap: +34 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: SUPPORTS_MODEL_DIRECTION
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Jessica Bouzas Maneiro vs Milana Ivantsiv -- WTA 125K Lisbon R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-13 16:30Z
* Current expected start: 2026-10-13 15:36Z
* Source: COURT_PROGRESSION: preceding match on Estadio CIF in progress (set 1 of best-of-3); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-13 14:56Z
* Recommended handicap-by time: 2026-10-13 14:51Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Clay · scheduled 2026-10-13T16:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:222601:270481:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jessica Bouzas Maneiro (`KXWTACHALLENGERMATCH-26OCT13BOUIVA-BOU`) | 0.98 / 0.99 (100) | 98.5% | 98.5% | -- | -- [-----] | 96.7% | 95.5% | 96.7% | MARKETS_AGREE | -- | +0.0 pp | NORMAL | FRESH | F / POOR | ALL_AGREE | VERIFIED |
| Milana Ivantsiv (`KXWTACHALLENGERMATCH-26OCT13BOUIVA-IVA`) | -- / 0.02 (5646) | -- | 1.5% | 3.9% | 7.0% [4.9%-9.7%] | 3.3% | 9.6% | 6.4% | KALSHI_LONE_OUTLIER | PASS | -- | UNPRICED | FRESH | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 3457.0, B 64.0; serve-point win A 59.3%, B 57.0%; Elo A 1826.8, B 1378.4; model uncertainty 0.0241
* Form inputs: days since last match A 9, B 176; matches on record A 438, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.022, surface_pool_high -0.026, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; ONE_SIDED_OR_NO_QUOTE

## Dominika Salkova vs Elisa Visentin -- WTA 125K Rovereto R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-13 19:00Z
* Current expected start: 2026-10-13 15:36Z
* Source: COURT_PROGRESSION: preceding match on Centre Court in progress (set 1 of best-of-3); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-13 14:56Z
* Recommended handicap-by time: 2026-10-13 14:51Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Hard · scheduled 2026-10-13T19:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:216085:222966:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dominika Salkova (`KXWTACHALLENGERMATCH-26OCT13SALVIS-SAL`) | 0.98 / 0.99 (30117) | 98.5% | 99.5% | 86.5% | 96.0% [94.7%-97.0%] | -- | -- | -- | -- | PASS | +0.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elisa Visentin (`KXWTACHALLENGERMATCH-26OCT13SALVIS-VIS`) | 0.02 / 0.03 (411) | 2.5% | 0.5% | 13.5% | 4.0% [3.0%-5.3%] | -- | -- | -- | -- | PASS | -1.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3665.0, B 54.0; serve-point win A 64.8%, B 54.5%; Elo A 1720.4, B 1160.0; model uncertainty 0.0114
* Form inputs: days since last match A 8, B 358; matches on record A 294, B 12; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.013, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Jarno Jans / Joran Vliegen vs Arthur Reymond / Luca Sanchez -- ATP Challenger Olbia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 15:40Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-13T15:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13JANVLIREYSAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jarno Jans / Joran Vliegen (`KXATPCHALLENGERDOUBLES-26OCT13JANVLIREYSAN-JANVLI`) | 0.52 / 0.59 (5729) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arthur Reymond / Luca Sanchez (`KXATPCHALLENGERDOUBLES-26OCT13JANVLIREYSAN-REYSAN`) | 0.43 / 0.48 (1120) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Nathaniel Lammons / Jackson Withrow vs Alexander Donski / Filip Pieczonka -- ATP Challenger Olbia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 15:40Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-13T15:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13LAMWITDONPIE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Donski / Filip Pieczonka (`KXATPCHALLENGERDOUBLES-26OCT13LAMWITDONPIE-DONPIE`) | 0.42 / 0.50 (122) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nathaniel Lammons / Jackson Withrow (`KXATPCHALLENGERDOUBLES-26OCT13LAMWITDONPIE-LAMWIT`) | 0.50 / 0.55 (56) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jeevan Nedunchezhiyan / Billy Suarez vs Marko Maric / Tadija Radovanovic -- ATP Challenger Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 15:40Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-13T15:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13NEDSUAMARRAD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marko Maric / Tadija Radovanovic (`KXATPCHALLENGERDOUBLES-26OCT13NEDSUAMARRAD-MARRAD`) | 0.25 / 0.36 (40) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jeevan Nedunchezhiyan / Billy Suarez (`KXATPCHALLENGERDOUBLES-26OCT13NEDSUAMARRAD-NEDSUA`) | 0.57 / 0.69 (40) | 63.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Radoslav Shandarov / Vasil Shandarov vs Juan Jose Bianchi / Kody Pearson -- ATP Challenger Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 15:40Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-13T15:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13SHASHABIAPEA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Jose Bianchi / Kody Pearson (`KXATPCHALLENGERDOUBLES-26OCT13SHASHABIAPEA-BIAPEA`) | 0.17 / 0.95 (100) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Radoslav Shandarov / Vasil Shandarov (`KXATPCHALLENGERDOUBLES-26OCT13SHASHABIAPEA-SHASHA`) | 0.05 / 0.71 (1) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Luca Nardi vs August Holmgren -- ATP Challenger Olbia R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 15:50Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-13T15:50:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200416:208134:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| August Holmgren (`KXATPCHALLENGERMATCH-26OCT13NARHOL-HOL`) | 0.48 / 0.51 (183) | 49.5% | 42.5% | 44.5% | 42.5% [41.0%-43.5%] | -- | 49.9% | 49.9% | MODEL_LONE_OUTLIER | PASS | -7.0 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Luca Nardi (`KXATPCHALLENGERMATCH-26OCT13NARHOL-NAR`) | 0.49 / 0.50 (1) | 49.5% | 57.5% | 55.5% | 57.5% [56.5%-59.0%] | -- | 49.6% | 49.6% | MODEL_LONE_OUTLIER | SHADOW_BET | +8.0 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3056.0, B 3616.0; serve-point win A 64.0%, B 37.5%; Elo A 1659.3, B 1572.4; model uncertainty 0.0128
* Form inputs: days since last match A 8, B 8; matches on record A 346, B 286; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.015, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; THIN_DISPLAYED_SIZE

## Gabriele Bosio vs Giovanni Oradini -- M25 Santa Margherita di Pula R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-13T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132831:208152:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriele Bosio (`KXITFMATCH-26OCT13BOSORA-BOS`) | 0.38 / 0.39 (126) | 38.5% | 26.7% | 42.4% | 27.8% [23.9%-30.4%] | 21.9% | -- | 21.9% | KALSHI_LONE_OUTLIER | PASS | -11.8 pp | REVIEW | FRESH | F / POOR | AGREES_WITH_MODEL | AMBIGUOUS |
| Giovanni Oradini (`KXITFMATCH-26OCT13BOSORA-ORA`) | 0.60 / 0.62 (3245) | 61.0% | 73.3% | 57.6% | 72.2% [69.6%-76.1%] | 78.1% | -- | 78.1% | MODEL_LONE_OUTLIER | PASS | +12.3 pp | REVIEW | FRESH | F / POOR | AGREES_WITH_MODEL | AMBIGUOUS |

* Serve evidence (points): A 128.0, B 598.0; serve-point win A 58.6%, B 36.5%; Elo A 1260.5, B 1438.4; model uncertainty 0.0323
* Form inputs: days since last match A 757, B 22; matches on record A 131, B 260; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.025, surface_pool_high +0.026, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Odysseas Geladaris vs Finn Murgett -- M15 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13GELMUR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Odysseas Geladaris (`KXITFMATCH-26OCT13GELMUR-GEL`) | 0.05 / 0.07 (3) | 6.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Finn Murgett (`KXITFMATCH-26OCT13GELMUR-MUR`) | 0.91 / 0.94 (57) | 92.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Petros Tsitsipas vs Rodrigo Alujas -- M15 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-13T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202065:212286:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rodrigo Alujas (`KXITFMATCH-26OCT13TSIALU-ALU`) | 0.04 / 0.08 (119) | 6.0% | 65.2% | 82.2% | 55.1% [50.0%-60.2%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +59.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Petros Tsitsipas (`KXITFMATCH-26OCT13TSIALU-TSI`) | 0.91 / 0.95 (94) | 93.0% | 34.8% | 17.8% | 44.9% [39.8%-50.0%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -58.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 427.0, B 229.0; serve-point win A 59.4%, B 37.6%; Elo A 1189.9, B 1188.3; model uncertainty 0.0508
* Form inputs: days since last match A 365, B 673; matches on record A 120, B 33; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT13TSIALU-ALU  (YES = Rodrigo Alujas)
Model: 65%
Kalshi: 6%
Gap: +59 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.020, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elena Barbulescu / Simionescu vs Garnevska / Simeonova -- W50 Stara Zagora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13ELESIMGARSIM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elena Barbulescu / Simionescu (`KXITFWDOUBLES-26OCT13ELESIMGARSIM-ELESIM`) | 0.05 / 0.95 (213) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Garnevska / Simeonova (`KXITFWDOUBLES-26OCT13ELESIMGARSIM-GARSIM`) | 0.05 / 0.92 (1) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Iancu / Maria Marioara vs Kostova / Krastenova -- W50 Stara Zagora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13IANMARKOSKRA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iancu / Maria Marioara (`KXITFWDOUBLES-26OCT13IANMARKOSKRA-IANMAR`) | 0.05 / 0.95 (213) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kostova / Krastenova (`KXITFWDOUBLES-26OCT13IANMARKOSKRA-KOSKRA`) | 0.05 / 0.93 (1) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Karatancheva / Velikova vs Markova / Simeonova -- W50 Stara Zagora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13KARVELMARSIM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karatancheva / Velikova (`KXITFWDOUBLES-26OCT13KARVELMARSIM-KARVEL`) | 0.92 / 0.95 (153) | 93.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Markova / Simeonova (`KXITFWDOUBLES-26OCT13KARVELMARSIM-MARSIM`) | 0.06 / 0.10 (1) | 8.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Florian Broska vs Milos Karol -- ATP Challenger Maia R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-13T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202239:209984:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Florian Broska (`KXATPCHALLENGERMATCH-26OCT13BROKAR-BRO`) | 0.54 / 0.55 (20541) | 54.5% | 51.3% | 56.2% | 53.3% [52.0%-54.3%] | 53.1% | 53.5% | 53.3% | MODEL_LONE_OUTLIER | PASS | -3.2 pp | NORMAL | FRESH | F / POOR | ALL_AGREE | VERIFIED |
| Milos Karol (`KXATPCHALLENGERMATCH-26OCT13BROKAR-KAR`) | 0.46 / 0.47 (11741) | 46.5% | 48.7% | 43.8% | 46.7% [45.7%-48.0%] | 46.9% | 46.3% | 46.6% | MODEL_LONE_OUTLIER | PASS | +2.2 pp | NORMAL | FRESH | F / POOR | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 1151.0, B 1164.0; serve-point win A 68.3%, B 32.0%; Elo A 1460.2, B 1450.8; model uncertainty 0.0116
* Form inputs: days since last match A 8, B 694; matches on record A 141, B 165; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.000, surface_dev_loose +0.009, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Andrej Martin vs Nikolas Sanchez Izquierdo -- ATP Challenger Maia R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-13T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105413:207663:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrej Martin (`KXATPCHALLENGERMATCH-26OCT13MARSAI-MAR`) | 0.31 / 0.32 (5249) | 31.5% | 24.7% | 14.7% | 28.4% [21.5%-36.8%] | 32.3% | 31.6% | 31.9% | MODEL_LONE_OUTLIER | PASS | -6.8 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Nikolas Sanchez Izquierdo (`KXATPCHALLENGERMATCH-26OCT13MARSAI-SAI`) | 0.69 / 0.70 (26366) | 69.5% | 75.3% | 85.3% | 71.6% [63.2%-78.5%] | 67.7% | 68.8% | 68.2% | MODEL_LONE_OUTLIER | PASS | +5.8 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1496.0, B 3746.0; serve-point win A 57.1%, B 37.6%; Elo A 1593.4, B 1617.1; model uncertainty 0.0769
* Form inputs: days since last match A 8, B 8; matches on record A 985, B 525; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose -0.017, surface_dev_tight +0.022
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Charl / Vlajic vs Mozgaleva / Terentyeva -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13CHAVLAMOZTER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charl / Vlajic (`KXITFWDOUBLES-26OCT13CHAVLAMOZTER-CHAVLA`) | 0.15 / 0.17 (15) | 16.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mozgaleva / Terentyeva (`KXITFWDOUBLES-26OCT13CHAVLAMOZTER-MOZTER`) | 0.78 / 0.85 (31) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Carles Hernandez vs Kylian Collignon -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-13T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208264:212262:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kylian Collignon (`KXITFMATCH-26OCT13HERCOL-COL`) | 0.12 / 0.18 (197) | 15.0% | 17.2% | 54.0% | 39.0% [38.0%-40.0%] | 11.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carles Hernandez (`KXITFMATCH-26OCT13HERCOL-HER`) | 0.79 / 0.86 (50) | 82.5% | 82.8% | 46.0% | 61.0% [60.0%-62.0%] | 88.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 84.0, B 0.0; serve-point win A 65.8%, B 41.6%; Elo A 1237.0, B 1154.8; model uncertainty 0.0098
* Form inputs: days since last match A 8, B 687; matches on record A 41, B 17; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Giles Hussey vs Amar Tahirovic -- M15 Offenbach R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13HUSTAH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giles Hussey (`KXITFMATCH-26OCT13HUSTAH-HUS`) | 0.75 / 0.78 (5) | 76.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Amar Tahirovic (`KXITFMATCH-26OCT13HUSTAH-TAH`) | 0.22 / 0.25 (334) | 23.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tiago Pereira vs Luka Mikrut -- ATP Challenger Maia R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-13T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210053:211500:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luka Mikrut (`KXATPCHALLENGERMATCH-26OCT13PERMIK-MIK`) | 0.99 / -- (0) | -- | 89.9% | 95.9% | 92.1% [86.1%-95.2%] | -- | 76.4% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | -- | UNPRICED | FRESH | B / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |
| Tiago Pereira (`KXATPCHALLENGERMATCH-26OCT13PERMIK-PER`) | 0.01 / 0.02 (21205) | 1.5% | 10.1% | 4.1% | 7.9% [4.8%-13.9%] | -- | 23.5% | -- | INSUFFICIENT_INPUTS | PASS | +8.6 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 926.0, B 2504.0; serve-point win A 55.8%, B 34.3%; Elo A 1367.6, B 1721.7; model uncertainty 0.0455
* Form inputs: days since last match A 84, B 8; matches on record A 152, B 188; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.012, surface_pool_high -0.009, surface_dev_loose -0.006, surface_dev_tight +0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; ONE_SIDED_OR_NO_QUOTE

## Belibova / Gamretkaia vs Mikhailova / Pankratova -- W15 Chisinau R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13BELGAMMIKPAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Belibova / Gamretkaia (`KXITFWDOUBLES-26OCT13BELGAMMIKPAN-BELGAM`) | 0.07 / 0.91 (327) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mikhailova / Pankratova (`KXITFWDOUBLES-26OCT13BELGAMMIKPAN-MIKPAN`) | 0.07 / 0.58 (1) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Biro / Wanja Brune Olsen vs Maria Ciuhrii / Hincu -- W15 Chisinau R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13BIRWANMARHIN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Biro / Wanja Brune Olsen (`KXITFWDOUBLES-26OCT13BIRWANMARHIN-BIRWAN`) | 0.05 / 0.95 (211) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maria Ciuhrii / Hincu (`KXITFWDOUBLES-26OCT13BIRWANMARHIN-MARHIN`) | 0.05 / 0.95 (213) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Maria Buculei / Nikolaieva vs Boyden / Safta -- W15 Chisinau R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13MARNIKBOYSAF:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Boyden / Safta (`KXITFWDOUBLES-26OCT13MARNIKBOYSAF-BOYSAF`) | 0.20 / 0.95 (213) | 57.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maria Buculei / Nikolaieva (`KXITFWDOUBLES-26OCT13MARNIKBOYSAF-MARNIK`) | 0.05 / 0.95 (213) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Teodora Miron vs Adelina Lacinova -- W35 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-13T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:270171:espn:espn:16130:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adelina Lacinova (`KXITFWMATCH-26OCT13MIRLAC-LAC`) | 0.97 / 0.98 (272) | 97.5% | 78.7% | 55.3% | 70.4% [70.3%-71.3%] | -- | -- | -- | -- | PASS | -18.8 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Teodora Miron (`KXITFWMATCH-26OCT13MIRLAC-MIR`) | 0.02 / 0.03 (8) | 2.5% | 21.3% | 44.7% | 29.6% [28.7%-29.6%] | -- | -- | -- | -- | PASS | +18.8 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 136.0, B 0.0; serve-point win A 50.3%, B 43.7%; Elo A 1322.2, B 1475.8; model uncertainty 0.0047
* Form inputs: days since last match A 449, B 9; matches on record A 2, B 5; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT13MIRLAC-MIR  (YES = Teodora Miron)
Model: 21%
Kalshi: 2%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Reva / Reva vs Drobca / Helbet -- W15 Chisinau R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13REVREVDROHEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Drobca / Helbet (`KXITFWDOUBLES-26OCT13REVREVDROHEL-DROHEL`) | 0.05 / 0.95 (213) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Reva / Reva (`KXITFWDOUBLES-26OCT13REVREVDROHEL-REVREV`) | 0.05 / 0.95 (213) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Bianca Andreescu vs Mia Ristic -- WTA 125K Rovereto R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-13 20:30Z
* Current expected start: 2026-10-13 17:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-13 14:56Z
* Recommended handicap-by time: 2026-10-13 16:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Hard · scheduled 2026-10-13T20:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:215370:239392:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bianca Andreescu (`KXWTACHALLENGERMATCH-26OCT13ANDRIS-AND`) | 0.80 / 0.81 (4626) | 80.5% | 74.1% | 62.2% | 68.8% [66.0%-72.0%] | 78.0% | 80.0% | 80.0% | MODEL_LONE_OUTLIER | PASS | -6.4 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Mia Ristic (`KXWTACHALLENGERMATCH-26OCT13ANDRIS-RIS`) | 0.19 / 0.20 (7555) | 19.5% | 25.9% | 37.8% | 31.2% [28.1%-34.0%] | 22.0% | 19.9% | 19.9% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.4 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 2877.0, B 3260.0; serve-point win A 62.5%, B 42.5%; Elo A 1880.4, B 1634.7; model uncertainty 0.0295
* Form inputs: days since last match A 4, B 18; matches on record A 366, B 238; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.018, surface_pool_high +0.018, surface_dev_loose +0.021, surface_dev_tight -0.017
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Alfano / Aleksandar Amarandei vs Spadola / Vavassori -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13ALFALESPAVAV:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alfano / Aleksandar Amarandei (`KXITFDOUBLES-26OCT13ALFALESPAVAV-ALFALE`) | 0.04 / 0.07 (328) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Spadola / Vavassori (`KXITFDOUBLES-26OCT13ALFALESPAVAV-SPAVAV`) | 0.92 / 0.95 (303) | 93.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Romain Arneodo / Hendrik Jebens vs Henry Bernet / Dominic Stricker -- ATP Challenger Roanne R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-13T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13ARNJEBBERSTR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Romain Arneodo / Hendrik Jebens (`KXATPCHALLENGERDOUBLES-26OCT13ARNJEBBERSTR-ARNJEB`) | 0.45 / 0.75 (1) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Henry Bernet / Dominic Stricker (`KXATPCHALLENGERDOUBLES-26OCT13ARNJEBBERSTR-BERSTR`) | 0.06 / 0.58 (100) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Pierre-Hugues Herbert vs Norbert Gombos -- ATP Challenger Roanne R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-13T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105613:105732:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Norbert Gombos (`KXATPCHALLENGERMATCH-26OCT13HERGOM-GOM`) | 0.42 / 0.43 (5316) | 42.5% | 40.4% | 42.1% | 40.6% [39.6%-42.6%] | 44.6% | 44.1% | 44.3% | MODEL_LONE_OUTLIER | PASS | -2.1 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Pierre-Hugues Herbert (`KXATPCHALLENGERMATCH-26OCT13HERGOM-HER`) | 0.57 / 0.58 (10162) | 57.5% | 59.6% | 57.9% | 59.4% [57.4%-60.4%] | 55.4% | 55.6% | 55.5% | MODEL_LONE_OUTLIER | WATCH | +2.1 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 2989.0, B 3555.0; serve-point win A 65.0%, B 36.9%; Elo A 1683.9, B 1609.5; model uncertainty 0.0148
* Form inputs: days since last match A 49, B 23; matches on record A 846, B 992; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.019, surface_dev_loose +0.005, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Blomqvist / Roots vs Sacco / Vaissaud -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13BLOROOSACVAI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Blomqvist / Roots (`KXITFWDOUBLES-26OCT13BLOROOSACVAI-BLOROO`) | 0.02 / 0.04 (1) | 3.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sacco / Vaissaud (`KXITFWDOUBLES-26OCT13BLOROOSACVAI-SACVAI`) | 0.94 / 0.96 (363) | 95.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Chastang Cooper / Toma vs ANDREA Molaro / Paola Marina Pieragostini -- W35 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13CHATOMANDPAO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ANDREA Molaro / Paola Marina Pieragostini (`KXITFWDOUBLES-26OCT13CHATOMANDPAO-ANDPAO`) | 0.52 / 0.60 (300) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Chastang Cooper / Toma (`KXITFWDOUBLES-26OCT13CHATOMANDPAO-CHATOM`) | 0.39 / 0.47 (406) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Dessolis / Odorizzi vs Luciano / Mariani -- W35 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13DESODOLUCMAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dessolis / Odorizzi (`KXITFWDOUBLES-26OCT13DESODOLUCMAR-DESODO`) | 0.18 / 0.19 (300) | 18.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luciano / Mariani (`KXITFWDOUBLES-26OCT13DESODOLUCMAR-LUCMAR`) | 0.82 / 0.83 (328) | 82.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Marta Lombardini vs Nina Radovanovic -- W35 Santa Margherita di Pula R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-13T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222602:267409:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marta Lombardini (`KXITFWMATCH-26OCT13LOMRAD-LOM`) | 0.49 / 0.51 (6303) | 50.0% | 60.9% | 47.3% | 53.8% [48.4%-60.1%] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +10.9 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nina Radovanovic (`KXITFWMATCH-26OCT13LOMRAD-RAD`) | 0.49 / 0.51 (6076) | 50.0% | 39.1% | 52.7% | 46.2% [39.9%-51.6%] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -10.9 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 984.0, B 976.0; serve-point win A 52.1%, B 49.9%; Elo A 1448.4, B 1386.2; model uncertainty 0.0585
* Form inputs: days since last match A 20, B 169; matches on record A 25, B 247; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.054, surface_pool_high +0.063, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pistola / Ye vs Bohrer Martins / Ezzat -- W35 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13PISYEXBOHEZZ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bohrer Martins / Ezzat (`KXITFWDOUBLES-26OCT13PISYEXBOHEZZ-BOHEZZ`) | 0.79 / 0.84 (1) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pistola / Ye (`KXITFWDOUBLES-26OCT13PISYEXBOHEZZ-PISYEX`) | 0.17 / 0.19 (414) | 18.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Carlo Alberto Caniato vs Daniel Siniakov -- ATP Challenger Catania R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-13T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209338:212241:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlo Alberto Caniato (`KXATPCHALLENGERMATCH-26OCT13CANSIN-CAN`) | 0.79 / 0.80 (486) | 79.5% | 81.1% | 74.4% | 77.9% [76.7%-78.7%] | 79.2% | 80.7% | 80.7% | MODEL_LONE_OUTLIER | PASS | +1.6 pp | NORMAL | FRESH | C / LIMITED | EXTERNAL_STALE | VERIFIED |
| Daniel Siniakov (`KXATPCHALLENGERMATCH-26OCT13CANSIN-SIN`) | 0.19 / 0.20 (17270) | 19.5% | 18.9% | 25.6% | 22.1% [21.3%-23.3%] | 20.8% | 19.1% | 19.1% | MODEL_LONE_OUTLIER | WATCH | -0.6 pp | NORMAL | FRESH | C / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 1491.0, B 334.0; serve-point win A 66.4%, B 40.6%; Elo A 1440.0, B 1212.8; model uncertainty 0.0099
* Form inputs: days since last match A 8, B 36; matches on record A 88, B 81; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE

## Yannik Kelm vs Pierre Yves Bailly -- M15 Offenbach R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210048:212025:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pierre Yves Bailly (`KXITFMATCH-26OCT13KELBAI-BAI`) | 0.47 / 0.79 (1) | 63.0% | 89.9% | 70.1% | 82.9% [82.6%-83.1%] | 66.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +26.9 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yannik Kelm (`KXITFMATCH-26OCT13KELBAI-KEL`) | 0.07 / 0.45 (1) | 26.0% | 10.1% | 29.9% | 17.1% [16.9%-17.4%] | 33.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.9 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 193.0, B 0.0; serve-point win A 55.5%, B 34.6%; Elo A 1174.7, B 1445.6; model uncertainty 0.0025
* Form inputs: days since last match A 687, B 694; matches on record A 35, B 30; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT13KELBAI-BAI  (YES = Pierre Yves Bailly)
Model: 90%
Kalshi: 63%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nolan / Perego vs Chatziavraam / Kountourakis -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13NOLPERCHAKOU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chatziavraam / Kountourakis (`KXITFDOUBLES-26OCT13NOLPERCHAKOU-CHAKOU`) | 0.16 / 0.21 (300) | 18.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nolan / Perego (`KXITFDOUBLES-26OCT13NOLPERCHAKOU-NOLPER`) | 0.78 / 0.84 (330) | 81.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Mili Poljicak vs Francesco Maestrelli -- ATP Challenger Olbia R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-13T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208353:209890:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesco Maestrelli (`KXATPCHALLENGERMATCH-26OCT13POLMAE-MAE`) | 0.58 / 0.60 (8967) | 59.0% | 51.8% | 51.0% | 48.5% [47.5%-50.5%] | 58.4% | 59.4% | 58.9% | MODEL_LONE_OUTLIER | PASS | -7.2 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Mili Poljicak (`KXATPCHALLENGERMATCH-26OCT13POLMAE-POL`) | 0.41 / 0.42 (10999) | 41.5% | 48.2% | 49.0% | 51.5% [49.5%-52.5%] | 41.6% | 40.9% | 41.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.7 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2223.0, B 3939.0; serve-point win A 62.4%, B 37.2%; Elo A 1628.2, B 1601.8; model uncertainty 0.0151
* Form inputs: days since last match A 15, B 8; matches on record A 231, B 329; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Uzhylovskyi / Ho Yap vs Kypriotis / Nouchakis -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13UZHHOYKYPNOU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kypriotis / Nouchakis (`KXITFDOUBLES-26OCT13UZHHOYKYPNOU-KYPNOU`) | 0.74 / 0.80 (305) | 77.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Uzhylovskyi / Ho Yap (`KXITFDOUBLES-26OCT13UZHHOYKYPNOU-UZHHOY`) | 0.18 / 0.24 (73) | 21.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Marco Trungelliti vs Thiago Monteiro -- ATP Challenger Maia R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 18:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-13T18:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105477:106329:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thiago Monteiro (`KXATPCHALLENGERMATCH-26OCT13TRUMON-MON`) | 0.43 / 0.44 (11119) | 43.5% | 49.1% | 39.6% | 40.1% [39.6%-41.6%] | -- | 43.3% | 43.3% | MODEL_LONE_OUTLIER | PASS | +5.6 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Marco Trungelliti (`KXATPCHALLENGERMATCH-26OCT13TRUMON-TRU`) | 0.56 / 0.57 (2242) | 56.5% | 50.9% | 60.4% | 59.9% [58.4%-60.4%] | -- | 56.2% | 56.2% | MODEL_LONE_OUTLIER | WATCH | -5.6 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4986.0, B 4338.0; serve-point win A 63.6%, B 36.6%; Elo A 1774.7, B 1716.1; model uncertainty 0.0098
* Form inputs: days since last match A 6, B 8; matches on record A 985, B 920; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.005, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Nagoudi / Piatti vs Deflandre / Picard -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13NAGPIADEFPIC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Deflandre / Picard (`KXITFDOUBLES-26OCT13NAGPIADEFPIC-DEFPIC`) | 0.02 / 0.68 (1) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nagoudi / Piatti (`KXITFDOUBLES-26OCT13NAGPIADEFPIC-NAGPIA`) | 0.03 / 0.82 (1) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Valentin Basel vs Enzo Lima -- M15 Maringa R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211478:211761:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valentin Basel (`KXITFMATCH-26OCT13BASLIM-BAS`) | 0.91 / 0.92 (2) | 91.5% | 84.1% | 38.3% | 70.6% [68.0%-72.5%] | 66.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Enzo Lima (`KXITFMATCH-26OCT13BASLIM-LIM`) | 0.07 / 0.08 (5413) | 7.5% | 15.9% | 61.7% | 29.4% [27.5%-32.0%] | 33.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +8.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 178.0, B 107.0; serve-point win A 64.2%, B 43.6%; Elo A 1230.4, B 1059.7; model uncertainty 0.0223
* Form inputs: days since last match A 113, B 701; matches on record A 36, B 19; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bertimon / Bertimon vs Kuperstein / Tumbas Kajgo -- M15 Bol R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13BERBERKUPTUM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bertimon / Bertimon (`KXITFDOUBLES-26OCT13BERBERKUPTUM-BERBER`) | 0.02 / 0.06 (107) | 4.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kuperstein / Tumbas Kajgo (`KXITFDOUBLES-26OCT13BERBERKUPTUM-KUPTUM`) | 0.93 / 0.98 (29) | 95.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Bertrand / Makhlouf vs chetouane / Sandor Takacs -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13BERMAKCHESAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bertrand / Makhlouf (`KXITFDOUBLES-26OCT13BERMAKCHESAN-BERMAK`) | 0.54 / 0.58 (791) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| chetouane / Sandor Takacs (`KXITFDOUBLES-26OCT13BERMAKCHESAN-CHESAN`) | 0.42 / 0.45 (741) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Carrascosa Diaz / Carrascosa Diaz vs Agustin Pernas / Vasilev -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13CARCARAGUVAS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Agustin Pernas / Vasilev (`KXITFDOUBLES-26OCT13CARCARAGUVAS-AGUVAS`) | 0.26 / 0.95 (55) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Carrascosa Diaz / Carrascosa Diaz (`KXITFDOUBLES-26OCT13CARCARAGUVAS-CARCAR`) | 0.02 / 0.90 (10) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Mondazzi / Ravasio vs Freire Da Silva / Rivet -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13MONRAVFRERIV:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Freire Da Silva / Rivet (`KXITFDOUBLES-26OCT13MONRAVFRERIV-FRERIV`) | 0.08 / 0.82 (39) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mondazzi / Ravasio (`KXITFDOUBLES-26OCT13MONRAVFRERIV-MONRAV`) | 0.04 / 0.68 (1) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dante Pagani vs Joao Eduardo Schiessl -- M15 Maringa R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210214:213677:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dante Pagani (`KXITFMATCH-26OCT13PAGSCH-PAG`) | 0.19 / 0.22 (55) | 20.5% | 18.2% | 62.6% | 32.1% [31.2%-33.1%] | 24.0% | -- | 24.0% | MODEL_LONE_OUTLIER | PASS | -2.3 pp | NORMAL | FRESH | F / POOR | EXTERNAL_OUTLIER | VERIFIED |
| Joao Eduardo Schiessl (`KXITFMATCH-26OCT13PAGSCH-SCH`) | 0.76 / 0.80 (1) | 78.0% | 81.8% | 37.4% | 67.8% [66.9%-68.8%] | 76.0% | -- | 76.0% | KALSHI_LONE_OUTLIER | PASS | +3.8 pp | NORMAL | FRESH | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 56.0, B 1048.0; serve-point win A 57.0%, B 35.9%; Elo A 1257.5, B 1397.9; model uncertainty 0.0092
* Form inputs: days since last match A 274, B 8; matches on record A 4, B 131; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sabanov / Sabanov vs Baybars / Bueno Gil -- M15 Bol R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13SABSABBAYBUE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Baybars / Bueno Gil (`KXITFDOUBLES-26OCT13SABSABBAYBUE-BAYBUE`) | 0.32 / 0.34 (99) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sabanov / Sabanov (`KXITFDOUBLES-26OCT13SABSABBAYBUE-SABSAB`) | 0.63 / 0.67 (2) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Sophie Bekker vs Mika Stojsavljevic -- W35 Birmingham R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Grass · scheduled 2026-10-13T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:261963:264392:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sophie Bekker (`KXITFWMATCH-26OCT13BEKSTO-BEK`) | 0.07 / 0.08 (1834) | 7.5% | 1.9% | 38.6% | 10.3% [8.9%-12.4%] | 7.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mika Stojsavljevic (`KXITFWMATCH-26OCT13BEKSTO-STO`) | 0.92 / 0.93 (7919) | 92.5% | 98.1% | 61.4% | 89.7% [87.6%-91.1%] | 92.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 19.0, B 2019.0; serve-point win A 49.3%, B 34.9%; Elo A 1238.0, B 1613.4; model uncertainty 0.0176
* Form inputs: days since last match A 428, B 106; matches on record A 10, B 75; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.020, surface_dev_loose +0.001, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Iankovskaia / Shkutova vs Fontenel / Nishimura -- W35 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13IANSHKFONNIS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fontenel / Nishimura (`KXITFWDOUBLES-26OCT13IANSHKFONNIS-FONNIS`) | 0.72 / 0.83 (147) | 77.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Iankovskaia / Shkutova (`KXITFWDOUBLES-26OCT13IANSHKFONNIS-IANSHK`) | 0.11 / 0.28 (34) | 19.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Elena Malygina vs Victoria Allen -- W35 Birmingham R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Grass · scheduled 2026-10-13T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216116:216253:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Victoria Allen (`KXITFWMATCH-26OCT13MALALL-ALL`) | 0.25 / 0.28 (339) | 26.5% | 25.3% | 36.6% | 30.4% [26.7%-32.3%] | 21.9% | -- | 21.9% | KALSHI_LONE_OUTLIER | WATCH | -1.2 pp | NORMAL | FRESH | B / LIMITED | ALL_AGREE | VERIFIED |
| Elena Malygina (`KXITFWMATCH-26OCT13MALALL-MAL`) | 0.73 / 0.75 (85) | 74.0% | 74.7% | 63.4% | 69.6% [67.7%-73.3%] | 78.1% | -- | 78.1% | MODEL_LONE_OUTLIER | PASS | +0.7 pp | NORMAL | FRESH | B / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 2298.0, B 1893.0; serve-point win A 60.1%, B 44.9%; Elo A 1689.5, B 1481.1; model uncertainty 0.028
* Form inputs: days since last match A 18, B 136; matches on record A 440, B 83; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eliz Maloney vs Jodie Anna Burrage -- W35 Birmingham R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13MALBUR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jodie Anna Burrage (`KXITFWMATCH-26OCT13MALBUR-BUR`) | 0.88 / 0.92 (204) | 90.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eliz Maloney (`KXITFWMATCH-26OCT13MALBUR-MAL`) | 0.08 / 0.11 (129) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lara Savic vs Esther Adeshina -- W35 Birmingham R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13SAVADE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Esther Adeshina (`KXITFWMATCH-26OCT13SAVADE-ADE`) | 0.93 / 0.94 (3518) | 93.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lara Savic (`KXITFWMATCH-26OCT13SAVADE-SAV`) | 0.06 / 0.08 (1294) | 7.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Belkovics / Sallay vs Lewandowski / Cristian Lucaciu -- M15 Szabolcsveresmart R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13BELSALLEWCRI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Belkovics / Sallay (`KXITFDOUBLES-26OCT13BELSALLEWCRI-BELSAL`) | 0.36 / 0.38 (1) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lewandowski / Cristian Lucaciu (`KXITFDOUBLES-26OCT13BELSALLEWCRI-LEWCRI`) | 0.62 / 0.63 (1018) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Czyrek / Martinovic vs Orlando Fellin / Manukyan -- M15 Szabolcsveresmart R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13CZYMARORLMAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Czyrek / Martinovic (`KXITFDOUBLES-26OCT13CZYMARORLMAN-CZYMAR`) | 0.02 / 0.03 (1155) | 2.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Orlando Fellin / Manukyan (`KXITFDOUBLES-26OCT13CZYMARORLMAN-ORLMAN`) | 0.98 / 0.99 (83) | 98.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Moise Kouame vs Diego Dedura -- ATP Challenger Roanne R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-13T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212309:213608:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diego Dedura (`KXATPCHALLENGERMATCH-26OCT13KOUDED-DED`) | 0.25 / 0.26 (181) | 25.5% | 41.4% | 31.9% | 38.7% [33.8%-45.3%] | 30.3% | 26.0% | 28.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +15.9 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | B / ADEQUATE | AGREES_WITH_KALSHI | AMBIGUOUS |
| Moise Kouame (`KXATPCHALLENGERMATCH-26OCT13KOUDED-KOU`) | 0.73 / 0.74 (6616) | 73.5% | 58.6% | 68.1% | 61.3% [54.7%-66.2%] | 69.7% | 74.4% | 72.0% | MODEL_LONE_OUTLIER | PASS | -14.9 pp | REVIEW | FRESH | B / ADEQUATE | AGREES_WITH_KALSHI | AMBIGUOUS |

* Serve evidence (points): A 1583.0, B 2769.0; serve-point win A 59.4%, B 42.3%; Elo A 1546.6, B 1515.5; model uncertainty 0.0579
* Form inputs: days since last match A 14, B 8; matches on record A 33, B 115; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT13KOUDED-DED  (YES = Diego Dedura)
Model: 41%
Kalshi: 26%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: B (ADEQUATE)
Reasons: PLAYER_IDENTITY_RISK, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.025, surface_dev_loose +0.030, surface_dev_tight -0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Ewald / Kotliar vs Adkar / Tran -- W35 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13EWAKOTADKTRA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adkar / Tran (`KXITFWDOUBLES-26OCT13EWAKOTADKTRA-ADKTRA`) | 0.02 / 0.03 (28) | 2.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ewald / Kotliar (`KXITFWDOUBLES-26OCT13EWAKOTADKTRA-EWAKOT`) | 0.95 / 0.97 (8) | 96.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Kumru / Tahiri vs Barrera Aguirre / Zhu -- W35 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13KUMTAHBARZHU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barrera Aguirre / Zhu (`KXITFWDOUBLES-26OCT13KUMTAHBARZHU-BARZHU`) | 0.10 / 0.68 (1) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kumru / Tahiri (`KXITFWDOUBLES-26OCT13KUMTAHBARZHU-KUMTAH`) | 0.02 / 0.92 (61) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Matthew Rankin vs Tyler Bowers -- M15 Lexington KY R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211677:212668:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tyler Bowers (`KXITFMATCH-26OCT13RANBOW-BOW`) | 0.21 / 0.28 (20) | 24.5% | 71.9% | 50.0% | 69.5% [69.5%-69.6%] | -- | -- | -- | -- | PASS | +47.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Matthew Rankin (`KXITFMATCH-26OCT13RANBOW-RAN`) | 0.75 / 0.78 (16) | 76.5% | 28.1% | 50.0% | 30.5% [30.4%-30.6%] | -- | -- | -- | -- | PASS | -48.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 185.0; serve-point win A 59.1%, B 36.4%; Elo A 1264.9, B 1407.4; model uncertainty 0.0008
* Form inputs: days since last match A 1443, B 701; matches on record A 3, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT13RANBOW-BOW  (YES = Tyler Bowers)
Model: 72%
Kalshi: 24%
Gap: +47 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.001, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Youcef Rihane vs Jack Loutit -- M15 Lexington KY R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209065:211638:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jack Loutit (`KXITFMATCH-26OCT13RIHLOU-LOU`) | 0.04 / 0.05 (3755) | 4.5% | 86.2% | 49.5% | 79.1% [78.2%-79.9%] | -- | -- | -- | -- | PASS | +81.7 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Youcef Rihane (`KXITFMATCH-26OCT13RIHLOU-RIH`) | 0.95 / 0.97 (4690) | 96.0% | 13.8% | 50.5% | 20.9% [20.1%-21.8%] | -- | -- | -- | -- | PASS | -82.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 152.0; serve-point win A 58.2%, B 33.1%; Elo A 1201.9, B 1431.3; model uncertainty 0.0083
* Form inputs: days since last match A 1086, B 395; matches on record A 17, B 58; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT13RIHLOU-LOU  (YES = Jack Loutit)
Model: 86%
Kalshi: 4%
Gap: +82 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.007, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gabriel Schenekenberg vs Tomas Martinez -- M15 Maringa R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211658:211662:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tomas Martinez (`KXITFMATCH-26OCT13SCHMAR-MAR`) | 0.69 / 0.77 (300) | 73.0% | 63.8% | 42.8% | 58.2% [56.7%-59.2%] | 72.0% | -- | 72.0% | MODEL_LONE_OUTLIER | PASS | -9.2 pp | NORMAL | FRESH | F / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Gabriel Schenekenberg (`KXITFMATCH-26OCT13SCHMAR-SCH`) | 0.23 / 0.24 (32) | 23.5% | 36.2% | 57.2% | 41.8% [40.8%-43.3%] | 28.0% | -- | 28.0% | KALSHI_LONE_OUTLIER | PASS | +12.7 pp | REVIEW | FRESH | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 103.0, B 185.0; serve-point win A 58.9%, B 38.3%; Elo A 1146.0, B 1205.2; model uncertainty 0.0123
* Form inputs: days since last match A 722, B 22; matches on record A 8, B 15; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tom Sickenberger vs Raul Garcia -- M15 Lexington KY R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207881:212289:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raul Garcia (`KXITFMATCH-26OCT13SICGAR-GAR`) | 0.82 / 0.84 (5287) | 83.0% | 48.6% | 42.4% | 40.9% [40.8%-40.9%] | -- | -- | -- | -- | PASS | -34.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Tom Sickenberger (`KXITFMATCH-26OCT13SICGAR-SIC`) | 0.16 / 0.18 (4985) | 17.0% | 51.4% | 57.6% | 59.1% [59.1%-59.2%] | -- | -- | -- | -- | PASS | +34.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 90.0; serve-point win A 61.2%, B 39.1%; Elo A 1246.5, B 1181.3; model uncertainty 0.0006
* Form inputs: days since last match A 785, B 619; matches on record A 2, B 14; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT13SICGAR-SIC  (YES = Tom Sickenberger)
Model: 51%
Kalshi: 17%
Gap: +34 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eli Stephenson vs Bjorn Swenson -- M15 Lexington KY R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13STESWE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eli Stephenson (`KXITFMATCH-26OCT13STESWE-STE`) | 0.79 / 0.80 (4123) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bjorn Swenson (`KXITFMATCH-26OCT13STESWE-SWE`) | 0.20 / 0.21 (88) | 20.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rafael Tosetto vs Ignacio Monzon -- M15 Maringa R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:133820:208006:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ignacio Monzon (`KXITFMATCH-26OCT13TOSMON-MON`) | 0.65 / 0.70 (10) | 67.5% | 62.0% | 55.2% | 65.1% [64.2%-66.9%] | 67.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.5 pp | NORMAL | FRESH | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rafael Tosetto (`KXITFMATCH-26OCT13TOSMON-TOS`) | 0.30 / 0.32 (37) | 31.0% | 38.0% | 44.8% | 34.8% [33.1%-35.8%] | 32.5% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +7.0 pp | NORMAL | FRESH | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 251.0, B 727.0; serve-point win A 58.4%, B 39.3%; Elo A 1206.5, B 1331.9; model uncertainty 0.0137
* Form inputs: days since last match A 162, B 99; matches on record A 66, B 356; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amiraghyan / Nikcevic vs Kozak / Seric -- W15 Bol R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13AMINIKKOZSER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amiraghyan / Nikcevic (`KXITFWDOUBLES-26OCT13AMINIKKOZSER-AMINIK`) | 0.94 / 0.97 (302) | 95.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kozak / Seric (`KXITFWDOUBLES-26OCT13AMINIKKOZSER-KOZSER`) | 0.02 / 0.06 (419) | 4.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Brooks / Gardiner vs Maquet / Ozerova -- W35 Birmingham R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13BROGARMAQOZE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brooks / Gardiner (`KXITFWDOUBLES-26OCT13BROGARMAQOZE-BROGAR`) | 0.02 / 0.76 (1) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maquet / Ozerova (`KXITFWDOUBLES-26OCT13BROGARMAQOZE-MAQOZE`) | 0.10 / 0.93 (100) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jennifer Rosa Dourado vs Luna Maria Cinalli -- W15 Maceio R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215854:260711:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luna Maria Cinalli (`KXITFWMATCH-26OCT13DOUCIN-CIN`) | 0.97 / 0.98 (402) | 97.5% | 81.5% | 72.6% | 76.1% [74.4%-77.7%] | 92.8% | -- | 92.8% | MODEL_LONE_OUTLIER | PASS | -16.0 pp | HIGH_REVIEW | FRESH | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Jennifer Rosa Dourado (`KXITFWMATCH-26OCT13DOUCIN-DOU`) | 0.01 / 0.02 (31) | 1.5% | 18.5% | 27.4% | 23.9% [22.3%-25.6%] | 7.2% | -- | 7.2% | MODEL_LONE_OUTLIER | WATCH | +17.0 pp | HIGH_REVIEW | FRESH | C / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 723.0, B 795.0; serve-point win A 50.3%, B 43.0%; Elo A 1156.8, B 1377.8; model uncertainty 0.0166
* Form inputs: days since last match A 204, B 169; matches on record A 134, B 34; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT13DOUCIN-DOU  (YES = Jennifer Rosa Dourado)
Model: 19%
Kalshi: 2%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: SUPPORTS_MODEL_DIRECTION
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ana Clara Furlan Britzki vs Paola Lopez -- W15 Maceio R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13FURLOP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ana Clara Furlan Britzki (`KXITFWMATCH-26OCT13FURLOP-FUR`) | 0.02 / 0.03 (10829) | 2.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Paola Lopez (`KXITFWMATCH-26OCT13FURLOP-LOP`) | 0.97 / 0.98 (5513) | 97.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Griffiths / Smart vs Burguete Beltran / Jankowska -- W35 Birmingham R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13GRISMABURJAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Burguete Beltran / Jankowska (`KXITFWDOUBLES-26OCT13GRISMABURJAN-BURJAN`) | 0.01 / 0.95 (52) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Griffiths / Smart (`KXITFWDOUBLES-26OCT13GRISMABURJAN-GRISMA`) | 0.02 / 0.95 (52) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Mititelu / Williams vs Cleaver / Wainwright -- W35 Birmingham R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13MITWILCLEWAI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cleaver / Wainwright (`KXITFWDOUBLES-26OCT13MITWILCLEWAI-CLEWAI`) | 0.03 / 0.94 (100) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mititelu / Williams (`KXITFWDOUBLES-26OCT13MITWILCLEWAI-MITWIL`) | 0.03 / 0.93 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Giovana Schincariol Delatorre Barbosa vs Lais Mika Shibata -- W15 Maceio R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:263985:266781:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giovana Schincariol Delatorre Barbosa (`KXITFWMATCH-26OCT13SCHSHI-SCH`) | 0.97 / 0.98 (6127) | 97.5% | 89.3% | 33.0% | 66.6% [64.6%-68.5%] | 95.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lais Mika Shibata (`KXITFWMATCH-26OCT13SCHSHI-SHI`) | 0.02 / 0.03 (899) | 2.5% | 10.7% | 67.0% | 33.4% [31.5%-35.4%] | 4.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +8.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 533.0, B 97.0; serve-point win A 58.3%, B 51.0%; Elo A 1262.6, B 1132.3; model uncertainty 0.0196
* Form inputs: days since last match A 204, B 330; matches on record A 20, B 7; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Giovanni Mpetshi Perricard vs Etienne Donnet -- ATP Challenger Roanne R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 20:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-13T20:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208044:208659:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Etienne Donnet (`KXATPCHALLENGERMATCH-26OCT13MPEDON-DON`) | 0.22 / 0.23 (497) | 22.5% | 12.3% | 33.9% | 16.1% [9.4%-23.3%] | 24.7% | 22.5% | 22.5% | MODEL_LONE_OUTLIER | PASS | -10.2 pp | REVIEW | FRESH | D / POOR | EXTERNAL_STALE | VERIFIED |
| Giovanni Mpetshi Perricard (`KXATPCHALLENGERMATCH-26OCT13MPEDON-MPE`) | 0.76 / 0.78 (2675) | 77.0% | 87.7% | 66.1% | 83.9% [76.7%-90.6%] | 75.3% | 78.2% | 78.2% | MODEL_LONE_OUTLIER | PASS | +10.7 pp | REVIEW | FRESH | D / POOR | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4159.0, B 237.0; serve-point win A 76.2%, B 33.9%; Elo A 1720.5, B 1407.9; model uncertainty 0.0699
* Form inputs: days since last match A 43, B 393; matches on record A 307, B 55; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.048, surface_pool_high -0.062, surface_dev_loose +0.001, surface_dev_tight -0.002
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE

## Valerio Aboian vs Franco Roncadelli -- ATP Challenger Santa Cruz 2 R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-13T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208364:209254:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valerio Aboian (`KXATPCHALLENGERMATCH-26OCT13ABORON-ABO`) | 0.34 / 0.35 (1602) | 34.5% | 45.6% | 37.5% | 41.6% [39.5%-43.7%] | 34.8% | 34.8% | 34.8% | MODEL_LONE_OUTLIER | SHADOW_BET | +11.1 pp | REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Franco Roncadelli (`KXATPCHALLENGERMATCH-26OCT13ABORON-RON`) | 0.64 / 0.66 (2950) | 65.0% | 54.4% | 62.5% | 58.4% [56.3%-60.5%] | 65.1% | 65.0% | 65.0% | MODEL_LONE_OUTLIER | PASS | -10.6 pp | REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 2545.0, B 2986.0; serve-point win A 55.3%, B 43.9%; Elo A 1523.9, B 1540.9; model uncertainty 0.0209
* Form inputs: days since last match A 8, B 8; matches on record A 297, B 277; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Pedro Albuquerque Dietrich vs Joao Cunha Cunha -- M15 Maringa R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13ALBCUN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pedro Albuquerque Dietrich (`KXITFMATCH-26OCT13ALBCUN-ALB`) | 0.70 / 0.74 (96) | 72.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Joao Cunha Cunha (`KXITFMATCH-26OCT13ALBCUN-CUN`) | 0.22 / 0.27 (27) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andre De Almeida Santos / Wendler Filho vs Barreiros Reyes / Lorenzo Santos Gava -- M15 Maringa R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13ANDWENBARLOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andre De Almeida Santos / Wendler Filho (`KXITFDOUBLES-26OCT13ANDWENBARLOR-ANDWEN`) | 0.02 / 0.95 (50) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Barreiros Reyes / Lorenzo Santos Gava (`KXITFDOUBLES-26OCT13ANDWENBARLOR-BARLOR`) | 0.02 / 0.95 (50) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jonah Braswell vs Iker Urribarrens Ramirez -- M25 Austin TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211738:212098:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jonah Braswell (`KXITFMATCH-26OCT13BRAURR-BRA`) | 0.48 / 0.79 (65) | 63.5% | 52.3% | 45.5% | 53.0% [52.0%-54.0%] | -- | -- | -- | -- | PASS | -11.2 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Iker Urribarrens Ramirez (`KXITFMATCH-26OCT13BRAURR-URR`) | 0.09 / 0.31 (1) | 20.0% | 47.7% | 54.5% | 47.0% [46.0%-48.0%] | -- | -- | -- | -- | PASS | +27.7 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 111.0, B 0.0; serve-point win A 62.4%, B 38.0%; Elo A 1328.5, B 1308.8; model uncertainty 0.0101
* Form inputs: days since last match A 827, B 729; matches on record A 12, B 20; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT13BRAURR-URR  (YES = Iker Urribarrens Ramirez)
Model: 48%
Kalshi: 20%
Gap: +28 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gonzalo Bueno vs Maximo Zeitune -- ATP Challenger Santa Cruz 2 R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-13T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208293:212784:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gonzalo Bueno (`KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE`) | 0.58 / 0.59 (2071) | 58.5% | 88.3% | 65.2% | 85.8% [82.0%-89.0%] | 57.2% | 59.6% | -- | INSUFFICIENT_INPUTS | WATCH | +29.8 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maximo Zeitune (`KXATPCHALLENGERMATCH-26OCT13BUEZEI-ZEI`) | 0.40 / 0.42 (7948) | 41.0% | 11.7% | 34.8% | 14.2% [11.0%-18.0%] | 42.8% | 40.3% | -- | INSUFFICIENT_INPUTS | PASS | -29.3 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4183.0, B 747.0; serve-point win A 63.1%, B 46.1%; Elo A 1630.8, B 1205.0; model uncertainty 0.0351
* Form inputs: days since last match A 43, B 8; matches on record A 287, B 26; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE  (YES = Gonzalo Bueno)
Model: 88%
Kalshi: 58%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE

## Pedro Henrique Chabalgoity vs Rodrigo Kenichi Abe Hirai -- M15 Maringa R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13CHAABE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rodrigo Kenichi Abe Hirai (`KXITFMATCH-26OCT13CHAABE-ABE`) | 0.06 / 0.10 (2) | 8.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pedro Henrique Chabalgoity (`KXITFMATCH-26OCT13CHAABE-CHA`) | 0.91 / 0.93 (234) | 92.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lorenzo Claverie vs Mauricio Echazu -- M15 Quito R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-13T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105273:209936:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Claverie (`KXITFMATCH-26OCT13CLAECH-CLA`) | 0.68 / 0.70 (157) | 69.0% | 68.3% | 78.0% | 62.2% [54.9%-68.0%] | 72.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.7 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Mauricio Echazu (`KXITFMATCH-26OCT13CLAECH-ECH`) | 0.30 / 0.32 (324) | 31.0% | 31.7% | 22.1% | 37.8% [31.9%-45.1%] | 27.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.7 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 473.0, B 457.0; serve-point win A 66.2%, B 37.6%; Elo A 1431.4, B 1387.2; model uncertainty 0.0656
* Form inputs: days since last match A 79, B 2150; matches on record A 97, B 683; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high -0.000, surface_dev_loose +0.009, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Miles Clark vs Juan Sebastian Gomez -- M15 Quito R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-13T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105944:212473:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miles Clark (`KXITFMATCH-26OCT13CLAGOM-CLA`) | 0.18 / 0.20 (1614) | 19.0% | 25.1% | 68.0% | 25.8% [24.9%-25.8%] | 20.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Juan Sebastian Gomez (`KXITFMATCH-26OCT13CLAGOM-GOM`) | 0.80 / 0.82 (942) | 81.0% | 74.9% | 31.9% | 74.2% [74.2%-75.1%] | 79.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 933.0; serve-point win A 56.3%, B 38.5%; Elo A 1205.1, B 1391.0; model uncertainty 0.0045
* Form inputs: days since last match A 708, B 99; matches on record A 5, B 466; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high -0.000, surface_dev_loose -0.001, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Crevelaro / Felipe Silva vs Noatto / Storck Franca -- M15 Maringa R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13CREFELNOASTO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Crevelaro / Felipe Silva (`KXITFDOUBLES-26OCT13CREFELNOASTO-CREFEL`) | 0.03 / 0.92 (400) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Noatto / Storck Franca (`KXITFDOUBLES-26OCT13CREFELNOASTO-NOASTO`) | 0.13 / 0.94 (100) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Gabriel Debru vs Micah Braswell -- M25 Austin TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209334:210120:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Micah Braswell (`KXITFMATCH-26OCT13DEBBRA-BRA`) | 0.08 / 0.20 (1) | 14.0% | 47.0% | 50.0% | 51.0% [44.9%-55.1%] | -- | -- | -- | -- | PASS | +33.0 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gabriel Debru (`KXITFMATCH-26OCT13DEBBRA-DEB`) | 0.79 / 0.85 (1) | 82.0% | 53.0% | 50.0% | 49.0% [44.9%-55.1%] | -- | -- | -- | -- | PASS | -29.0 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1388.0, B 1799.0; serve-point win A 61.8%, B 38.8%; Elo A 1578.0, B 1593.0; model uncertainty 0.0508
* Form inputs: days since last match A 78, B 701; matches on record A 184, B 62; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT13DEBBRA-BRA  (YES = Micah Braswell)
Model: 47%
Kalshi: 14%
Gap: +33 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.031, surface_pool_high -0.041, surface_dev_loose -0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ryan Fishback vs Facundo Perlov -- M15 Quito R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13FISPER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ryan Fishback (`KXITFMATCH-26OCT13FISPER-FIS`) | 0.75 / 0.86 (1) | 80.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Facundo Perlov (`KXITFMATCH-26OCT13FISPER-PER`) | 0.06 / 0.21 (48) | 13.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Abel Forger vs James Quattro -- M25 Austin TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211524:213606:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Abel Forger (`KXITFMATCH-26OCT13FORQUA-FOR`) | 0.49 / 0.87 (0) | 68.0% | 69.3% | 48.0% | 53.0% [53.0%-54.0%] | -- | -- | -- | -- | PASS | +1.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| James Quattro (`KXITFMATCH-26OCT13FORQUA-QUA`) | 0.16 / 0.25 (1) | 20.5% | 30.7% | 52.0% | 47.0% [46.0%-47.0%] | -- | -- | -- | -- | PASS | +10.2 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 127.0, B 0.0; serve-point win A 64.1%, B 39.9%; Elo A 1275.6, B 1250.9; model uncertainty 0.0051
* Form inputs: days since last match A 92, B 729; matches on record A 45, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Darian King vs Charlelie Cosnet -- M15 Lexington KY R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105985:210444:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charlelie Cosnet (`KXITFMATCH-26OCT13KINCOS-COS`) | 0.12 / 0.22 (62) | 17.0% | 12.2% | 58.7% | 12.4% [10.9%-14.0%] | -- | -- | -- | -- | PASS | -4.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Darian King (`KXITFMATCH-26OCT13KINCOS-KIN`) | 0.66 / 0.81 (31) | 73.5% | 87.8% | 41.3% | 87.6% [86.0%-89.1%] | -- | -- | -- | -- | PASS | +14.3 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 571.0, B 0.0; serve-point win A 65.0%, B 44.1%; Elo A 1583.4, B 1242.1; model uncertainty 0.0157
* Form inputs: days since last match A 372, B 736; matches on record A 626, B 12; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.016, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Niko Klyachkin vs Pepijn Bastiaansen -- M15 Lexington KY R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13KLYBAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pepijn Bastiaansen (`KXITFMATCH-26OCT13KLYBAS-BAS`) | 0.90 / 0.91 (2) | 90.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Niko Klyachkin (`KXITFMATCH-26OCT13KLYBAS-KLY`) | 0.09 / 0.11 (14) | 10.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Henry Lieberman vs Jaden Weekes -- M15 Lexington KY R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211647:212545:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Henry Lieberman (`KXITFMATCH-26OCT13LIEWEE-LIE`) | 0.46 / 0.55 (54) | 50.5% | 17.8% | 46.4% | 33.1% [32.3%-33.2%] | -- | -- | -- | -- | PASS | -32.7 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jaden Weekes (`KXITFMATCH-26OCT13LIEWEE-WEE`) | 0.41 / 0.48 (1) | 44.5% | 82.2% | 53.6% | 66.9% [66.8%-67.7%] | -- | -- | -- | -- | PASS | +37.7 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 58.0, B 204.0; serve-point win A 57.5%, B 35.3%; Elo A 1189.9, B 1317.6; model uncertainty 0.0046
* Form inputs: days since last match A 701, B 701; matches on record A 5, B 25; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT13LIEWEE-WEE  (YES = Jaden Weekes)
Model: 82%
Kalshi: 44%
Gap: +38 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marko Mesarovic vs Alejandro Moreno -- M15 Lexington KY R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:204737:211670:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marko Mesarovic (`KXITFMATCH-26OCT13MESMOR-MES`) | 0.72 / 0.80 (46) | 76.0% | 51.7% | 50.0% | 46.0% [46.0%-46.0%] | -- | -- | -- | -- | PASS | -24.2 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Alejandro Moreno (`KXITFMATCH-26OCT13MESMOR-MOR`) | 0.17 / 0.25 (27) | 21.0% | 48.2% | 50.0% | 54.0% [54.0%-54.0%] | -- | -- | -- | -- | PASS | +27.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 62.2%, B 38.2%; Elo A 1200.3, B 1230.5; model uncertainty 0.0
* Form inputs: days since last match A 694, B 1177; matches on record A 8, B 5; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT13MESMOR-MOR  (YES = Alejandro Moreno)
Model: 48%
Kalshi: 21%
Gap: +27 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Manuel Mouilleron Salvo vs Nicolas Hollender -- M15 Quito R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-13T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210598:211389:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Hollender (`KXITFMATCH-26OCT13MOUHOL-HOL`) | 0.11 / 0.12 (1599) | 11.5% | 51.2% | 37.3% | 51.0% [50.0%-52.1%] | 15.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +39.7 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Manuel Mouilleron Salvo (`KXITFMATCH-26OCT13MOUHOL-MOU`) | 0.88 / 0.89 (1097) | 88.5% | 48.8% | 62.7% | 49.0% [47.9%-50.0%] | 84.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -39.7 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 107.0, B 70.0; serve-point win A 60.0%, B 39.8%; Elo A 1063.6, B 1078.1; model uncertainty 0.0103
* Form inputs: days since last match A 680, B 687; matches on record A 35, B 11; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT13MOUHOL-HOL  (YES = Nicolas Hollender)
Model: 51%
Kalshi: 12%
Gap: +40 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Genaro Alberto Olivieri vs Lucio Ratti -- ATP Challenger Santa Cruz 2 R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-13T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144821:211636:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Genaro Alberto Olivieri (`KXATPCHALLENGERMATCH-26OCT13OLIRAT-OLI`) | 0.63 / 0.64 (8819) | 63.5% | 79.2% | 51.6% | 74.0% [68.6%-78.4%] | 63.8% | 62.5% | 63.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +15.7 pp | HIGH_REVIEW | FRESH | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Lucio Ratti (`KXATPCHALLENGERMATCH-26OCT13OLIRAT-RAT`) | 0.36 / 0.37 (1643) | 36.5% | 20.8% | 48.4% | 26.0% [21.6%-31.4%] | 36.2% | 37.4% | 36.8% | MODEL_LONE_OUTLIER | PASS | -15.7 pp | HIGH_REVIEW | FRESH | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4381.0, B 904.0; serve-point win A 61.1%, B 45.1%; Elo A 1576.9, B 1285.7; model uncertainty 0.0489
* Form inputs: days since last match A 8, B 22; matches on record A 583, B 54; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT13OLIRAT-OLI  (YES = Genaro Alberto Olivieri)
Model: 79%
Kalshi: 64%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: B (LIMITED)
Reasons: THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.004, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Zsombor Velcz vs Blu Baker -- M25 Austin TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209124:209852:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Blu Baker (`KXITFMATCH-26OCT13VELBAK-BAK`) | 0.52 / 0.55 (1) | 53.5% | 55.0% | 28.5% | 52.1% [46.9%-56.2%] | -- | -- | -- | -- | PASS | +1.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Zsombor Velcz (`KXITFMATCH-26OCT13VELBAK-VEL`) | 0.45 / 0.47 (451) | 46.0% | 45.0% | 71.5% | 47.9% [43.8%-53.1%] | -- | -- | -- | -- | PASS | -1.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 469.0; serve-point win A 59.5%, B 39.5%; Elo A 1314.7, B 1326.6; model uncertainty 0.0464
* Form inputs: days since last match A 848, B 1170; matches on record A 60, B 78; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.041, surface_pool_high +0.052, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ayana Akli vs Annabelle Xu -- W50 Quebec City R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222376:264149:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ayana Akli (`KXITFWMATCH-26OCT13AKLXUX-AKL`) | 0.84 / 0.85 (520) | 84.5% | 87.3% | 62.6% | 76.9% [73.1%-81.1%] | -- | -- | -- | -- | PASS | +2.8 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Annabelle Xu (`KXITFWMATCH-26OCT13AKLXUX-XUX`) | 0.15 / 0.16 (3) | 15.5% | 12.7% | 37.4% | 23.1% [18.9%-26.9%] | -- | -- | -- | -- | WATCH | -2.8 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2838.0, B 722.0; serve-point win A 57.5%, B 51.1%; Elo A 1612.6, B 1347.8; model uncertainty 0.0399
* Form inputs: days since last match A 22, B 76; matches on record A 123, B 43; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.008, surface_dev_loose -0.004, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofia Johnson vs Anne Christine Lutkemeyer -- W100 Edmond OK R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13JOHLUT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Johnson (`KXITFWMATCH-26OCT13JOHLUT-JOH`) | 0.81 / 0.82 (138) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anne Christine Lutkemeyer (`KXITFWMATCH-26OCT13JOHLUT-LUT`) | 0.13 / 0.18 (2) | 15.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anastasia Kulikova vs Alana Smith -- W100 Edmond OK R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214741:220673:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasia Kulikova (`KXITFWMATCH-26OCT13KULSMI-KUL`) | 0.42 / 0.54 (97) | 48.0% | 48.1% | 55.2% | 53.1% [51.0%-55.2%] | -- | -- | -- | -- | PASS | +0.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alana Smith (`KXITFWMATCH-26OCT13KULSMI-SMI`) | 0.41 / 0.49 (1) | 45.0% | 51.9% | 44.8% | 46.9% [44.8%-49.0%] | -- | -- | -- | -- | PASS | +6.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1819.0, B 1759.0; serve-point win A 58.3%, B 41.3%; Elo A 1539.8, B 1531.3; model uncertainty 0.0208
* Form inputs: days since last match A 15, B 7; matches on record A 416, B 193; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.021, surface_dev_loose -0.005, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Raphaelle Lacasse vs Jamilah Snells -- W50 Quebec City R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221165:222262:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raphaelle Lacasse (`KXITFWMATCH-26OCT13LACSNE-LAC`) | 0.88 / 0.90 (623) | 89.0% | 62.9% | 53.7% | 57.8% [56.3%-59.5%] | -- | -- | -- | -- | PASS | -26.1 pp | EXTREME (DATA_WARNING) | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jamilah Snells (`KXITFWMATCH-26OCT13LACSNE-SNE`) | 0.09 / 0.12 (2) | 10.5% | 37.1% | 46.3% | 42.2% [40.5%-43.7%] | -- | -- | -- | -- | WATCH | +26.6 pp | EXTREME (DATA_WARNING) | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1172.0, B 1270.0; serve-point win A 58.3%, B 44.1%; Elo A 1401.0, B 1330.4; model uncertainty 0.0159
* Form inputs: days since last match A 23, B 23; matches on record A 115, B 112; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT13LACSNE-SNE  (YES = Jamilah Snells)
Model: 37%
Kalshi: 10%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: LOW_DISPLAYED_LIQUIDITY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high -0.000, surface_dev_loose -0.011, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Edda Mamedova vs Valeriya Strakhova -- W100 Edmond OK R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211063:239422:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Edda Mamedova (`KXITFWMATCH-26OCT13MAMSTR-MAM`) | 0.63 / 0.81 (24) | 72.0% | 74.9% | 90.5% | 75.7% [59.0%-85.8%] | -- | -- | -- | -- | PASS | +2.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valeriya Strakhova (`KXITFWMATCH-26OCT13MAMSTR-STR`) | 0.14 / 0.24 (2) | 19.0% | 25.1% | 9.5% | 24.3% [14.2%-41.0%] | -- | -- | -- | -- | PASS | +6.1 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 879.0, B 2323.0; serve-point win A 54.5%, B 50.5%; Elo A 1519.2, B 1419.4; model uncertainty 0.1341
* Form inputs: days since last match A 239, B 86; matches on record A 91, B 766; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.030, surface_pool_high +0.036, surface_dev_loose +0.012, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Martina Okalova vs Chukwumelije Clarke -- W100 Edmond OK R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214862:269864:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chukwumelije Clarke (`KXITFWMATCH-26OCT13OKACLA-CLA`) | 0.63 / 0.73 (48) | 68.0% | 44.3% | 74.0% | 53.2% [43.6%-61.6%] | -- | -- | -- | -- | PASS | -23.7 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Martina Okalova (`KXITFWMATCH-26OCT13OKACLA-OKA`) | 0.23 / 0.30 (17) | 26.5% | 55.7% | 26.0% | 46.8% [38.4%-56.4%] | -- | -- | -- | -- | PASS | +29.2 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1467.0, B 633.0; serve-point win A 53.0%, B 48.0%; Elo A 1465.3, B 1421.4; model uncertainty 0.09
* Form inputs: days since last match A 80, B 183; matches on record A 201, B 15; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT13OKACLA-OKA  (YES = Martina Okalova)
Model: 56%
Kalshi: 26%
Gap: +29 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.021, surface_dev_loose -0.016, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kajsa Rinaldo Persson vs Isabella Marton -- W50 Quebec City R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211643:260400:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isabella Marton (`KXITFWMATCH-26OCT13RINMAR-MAR`) | 0.06 / 0.12 (37) | 9.0% | 7.5% | 8.4% | 10.6% [8.2%-13.6%] | -- | -- | -- | -- | PASS | -1.5 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kajsa Rinaldo Persson (`KXITFWMATCH-26OCT13RINMAR-RIN`) | 0.85 / 0.92 (3) | 88.5% | 92.5% | 91.6% | 89.4% [86.5%-91.8%] | -- | -- | -- | -- | PASS | +4.0 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3104.0, B 1055.0; serve-point win A 60.9%, B 50.0%; Elo A 1566.1, B 1223.0; model uncertainty 0.0267
* Form inputs: days since last match A 20, B 73; matches on record A 430, B 32; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.024, surface_pool_high -0.029, surface_dev_loose +0.012, surface_dev_tight -0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bojicic Ono / Braga vs Tosetto / Zanellato -- M15 Maringa R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13BOJBRATOSZAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bojicic Ono / Braga (`KXITFDOUBLES-26OCT13BOJBRATOSZAN-BOJBRA`) | 0.05 / 0.95 (174) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tosetto / Zanellato (`KXITFDOUBLES-26OCT13BOJBRATOSZAN-TOSZAN`) | 0.06 / 0.94 (100) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Braga / Schenekenberg vs Henrique Ferreira Gomes / Junqueira de Andrade -- M15 Maringa R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13BRASCHHENJUN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Braga / Schenekenberg (`KXITFDOUBLES-26OCT13BRASCHHENJUN-BRASCH`) | 0.05 / 0.95 (74) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Henrique Ferreira Gomes / Junqueira de Andrade (`KXITFDOUBLES-26OCT13BRASCHHENJUN-HENJUN`) | 0.06 / 0.95 (74) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Shu Matsuoka vs Dominick Mosejczuk -- M25 Austin TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13MATMOS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shu Matsuoka (`KXITFMATCH-26OCT13MATMOS-MAT`) | 0.16 / 0.18 (13) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dominick Mosejczuk (`KXITFMATCH-26OCT13MATMOS-MOS`) | 0.77 / 0.84 (83) | 80.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Theo Papamalamis vs Matei Cristian Onofrei -- M15 Lexington KY R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210494:212245:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matei Cristian Onofrei (`KXITFMATCH-26OCT13PAPONO-ONO`) | 0.04 / 0.05 (961) | 4.5% | 17.6% | 58.7% | 19.7% [18.0%-20.8%] | 5.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.1 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Theo Papamalamis (`KXITFMATCH-26OCT13PAPONO-PAP`) | 0.95 / 0.96 (73) | 95.5% | 82.4% | 41.3% | 80.3% [79.2%-82.0%] | 94.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.1 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 354.0, B 70.0; serve-point win A 63.8%, B 43.4%; Elo A 1365.1, B 1105.5; model uncertainty 0.0139
* Form inputs: days since last match A 428, B 687; matches on record A 55, B 25; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oskar Brostrom Poulsen vs Nikola Slavic -- M15 Lexington KY R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208302:211355:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oskar Brostrom Poulsen (`KXITFMATCH-26OCT13POUSLA-POU`) | 0.57 / 0.59 (51) | 58.0% | 39.0% | 59.2% | 42.7% [42.0%-43.3%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -19.0 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nikola Slavic (`KXITFMATCH-26OCT13POUSLA-SLA`) | 0.41 / 0.43 (1) | 42.0% | 61.0% | 40.8% | 57.3% [56.7%-58.0%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +19.0 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 62.0, B 99.0; serve-point win A 64.2%, B 33.5%; Elo A 1197.6, B 1251.3; model uncertainty 0.0067
* Form inputs: days since last match A 176, B 93; matches on record A 6, B 17; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT13POUSLA-SLA  (YES = Nikola Slavic)
Model: 61%
Kalshi: 42%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.001, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Johan Alexander Rodriguez vs Carel Aubriel Ngounoue -- M25 Austin TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13RODNGO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carel Aubriel Ngounoue (`KXITFMATCH-26OCT13RODNGO-NGO`) | 0.20 / 0.22 (6244) | 21.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Johan Alexander Rodriguez (`KXITFMATCH-26OCT13RODNGO-ROD`) | 0.75 / 0.80 (7) | 77.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jerry Roddick vs Aryan Shah -- M25 Austin TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211325:212542:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jerry Roddick (`KXITFMATCH-26OCT13RODSHA-ROD`) | 0.35 / 0.40 (47) | 37.5% | 17.7% | 50.0% | 23.8% [23.8%-23.8%] | -- | -- | -- | -- | PASS | -19.8 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aryan Shah (`KXITFMATCH-26OCT13RODSHA-SHA`) | 0.58 / 0.63 (170) | 60.5% | 82.3% | 50.0% | 76.2% [76.2%-76.2%] | -- | -- | -- | -- | PASS | +21.8 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 58.3%, B 34.4%; Elo A 1211.4, B 1412.1; model uncertainty 0.0
* Form inputs: days since last match A 729, B 80; matches on record A 4, B 61; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT13RODSHA-SHA  (YES = Aryan Shah)
Model: 82%
Kalshi: 60%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cosme Rolland de Ravel vs Hiroki Sakagawa -- M25 Austin TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212243:tml:R0KE:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cosme Rolland de Ravel (`KXITFMATCH-26OCT13ROLSAK-ROL`) | 0.82 / 0.85 (75) | 83.5% | 84.3% | 52.5% | 80.5% [80.5%-81.2%] | -- | -- | -- | -- | PASS | +0.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hiroki Sakagawa (`KXITFMATCH-26OCT13ROLSAK-SAK`) | 0.14 / 0.17 (6210) | 15.5% | 15.7% | 47.5% | 19.5% [18.8%-19.5%] | -- | -- | -- | -- | PASS | +0.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 473.0, B 0.0; serve-point win A 66.3%, B 41.6%; Elo A 1459.5, B 1211.3; model uncertainty 0.0034
* Form inputs: days since last match A 106, B 687; matches on record A 7, B 8; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.007, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Victor Couto Loureiro / Pagotto vs Jose Gutierrez / Klok -- M15 Maringa R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13VICPAGJOSKLO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jose Gutierrez / Klok (`KXITFDOUBLES-26OCT13VICPAGJOSKLO-JOSKLO`) | 0.36 / 0.52 (2) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Victor Couto Loureiro / Pagotto (`KXITFDOUBLES-26OCT13VICPAGJOSKLO-VICPAG`) | 0.48 / 0.77 (8) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Julia Adams vs Dana Guzman -- W100 Edmond OK R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221834:266450:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julia Adams (`KXITFWMATCH-26OCT13ADAGUZ-ADA`) | 0.16 / 0.18 (9) | 17.0% | 30.9% | 45.7% | 41.0% [36.4%-44.7%] | -- | -- | -- | -- | PASS | +13.8 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dana Guzman (`KXITFWMATCH-26OCT13ADAGUZ-GUZ`) | 0.79 / 0.80 (321) | 79.5% | 69.2% | 54.3% | 59.0% [55.3%-63.6%] | -- | -- | -- | -- | PASS | -10.3 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2996.0, B 812.0; serve-point win A 52.1%, B 44.2%; Elo A 1473.4, B 1552.1; model uncertainty 0.0414
* Form inputs: days since last match A 169, B 239; matches on record A 163, B 42; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.026, surface_pool_high +0.037, surface_dev_loose +0.016, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Avery Alexander vs Victoria Hu -- W50 Quebec City R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221023:270186:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Avery Alexander (`KXITFWMATCH-26OCT13ALEHUX-ALE`) | 0.31 / 0.37 (72) | 34.0% | 10.4% | 19.5% | 19.8% [18.8%-20.9%] | -- | -- | -- | -- | PASS | -23.6 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Victoria Hu (`KXITFWMATCH-26OCT13ALEHUX-HUX`) | 0.60 / 0.68 (6186) | 64.0% | 89.6% | 80.5% | 80.2% [79.0%-81.2%] | -- | -- | -- | -- | PASS | +25.6 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 315.0, B 2960.0; serve-point win A 51.2%, B 39.3%; Elo A 1229.4, B 1469.9; model uncertainty 0.0107
* Form inputs: days since last match A 73, B 169; matches on record A 9, B 293; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT13ALEHUX-HUX  (YES = Victoria Hu)
Model: 90%
Kalshi: 64%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.011, surface_dev_loose -0.007, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Michaela Bayerlova vs Mimi Xu -- W50 Quebec City R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215693:259685:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michaela Bayerlova (`KXITFWMATCH-26OCT13BAYXUX-BAY`) | 0.12 / 0.13 (6160) | 12.5% | 10.7% | 19.3% | 19.3% [16.5%-21.5%] | -- | -- | -- | -- | WATCH | -1.8 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Mimi Xu (`KXITFWMATCH-26OCT13BAYXUX-XUX`) | 0.87 / 0.88 (83) | 87.5% | 89.3% | 80.7% | 80.7% [78.5%-83.5%] | -- | -- | -- | -- | PASS | +1.8 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1530.0, B 1841.0; serve-point win A 49.2%, B 41.5%; Elo A 1338.0, B 1592.8; model uncertainty 0.0249
* Form inputs: days since last match A 100, B 253; matches on record A 350, B 98; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.004, surface_dev_loose -0.027, surface_dev_tight +0.018
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofia Elena Cabezas Dominguez vs Thea Frodin -- W100 Edmond OK R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221982:264140:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Elena Cabezas Dominguez (`KXITFWMATCH-26OCT13CABFRO-CAB`) | 0.30 / 0.34 (6125) | 32.0% | 57.6% | 49.5% | 58.4% [55.8%-61.5%] | -- | -- | -- | -- | WATCH | +25.6 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Thea Frodin (`KXITFWMATCH-26OCT13CABFRO-FRO`) | 0.61 / 0.67 (1) | 64.0% | 42.4% | 50.5% | 41.6% [38.5%-44.2%] | -- | -- | -- | -- | PASS | -21.6 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1826.0, B 1232.0; serve-point win A 56.8%, B 44.6%; Elo A 1484.8, B 1374.0; model uncertainty 0.0286
* Form inputs: days since last match A 176, B 42; matches on record A 71, B 36; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT13CABFRO-CAB  (YES = Sofia Elena Cabezas Dominguez)
Model: 58%
Kalshi: 32%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.006, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kennedy Drenser-Hagmann vs Zoie Epps -- W100 Edmond OK R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13DREEPP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kennedy Drenser-Hagmann (`KXITFWMATCH-26OCT13DREEPP-DRE`) | 0.58 / 0.59 (35) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Zoie Epps (`KXITFWMATCH-26OCT13DREEPP-EPP`) | 0.39 / 0.43 (26) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ana Grubor vs Hina Inoue -- W50 Quebec City R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222080:258191:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ana Grubor (`KXITFWMATCH-26OCT13GRUINO-GRU`) | 0.12 / 0.13 (37) | 12.5% | 12.6% | 47.3% | 28.7% [17.9%-35.4%] | -- | -- | -- | -- | WATCH | +0.1 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hina Inoue (`KXITFWMATCH-26OCT13GRUINO-INO`) | 0.87 / 0.89 (51) | 88.0% | 87.5% | 52.7% | 71.3% [64.6%-82.1%] | -- | -- | -- | -- | PASS | -0.6 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1727.0, B 2804.0; serve-point win A 49.9%, B 41.5%; Elo A 1314.9, B 1638.6; model uncertainty 0.0876
* Form inputs: days since last match A 73, B 176; matches on record A 193, B 325; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.009, surface_dev_loose +0.019, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carmen Andreea Herea vs Alina Shcherbinina -- W100 Edmond OK R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221278:260142:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carmen Andreea Herea (`KXITFWMATCH-26OCT13HERSHC-HER`) | 0.34 / 0.40 (33) | 37.0% | 81.0% | 56.4% | 70.4% [66.2%-74.4%] | -- | -- | -- | -- | PASS | +44.0 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alina Shcherbinina (`KXITFWMATCH-26OCT13HERSHC-SHC`) | 0.56 / 0.62 (2) | 59.0% | 19.0% | 43.6% | 29.6% [25.6%-33.8%] | -- | -- | -- | -- | PASS | -40.0 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 799.0, B 127.0; serve-point win A 55.2%, B 51.4%; Elo A 1506.7, B 1349.9; model uncertainty 0.0412
* Form inputs: days since last match A 93, B 239; matches on record A 105, B 55; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT13HERSHC-HER  (YES = Carmen Andreea Herea)
Model: 81%
Kalshi: 37%
Gap: +44 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.027, surface_pool_high -0.038, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hernan Casanova vs Juan Manuel La Serna -- ATP Challenger Santa Cruz 2 R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 22:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-13T22:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106292:210412:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hernan Casanova (`KXATPCHALLENGERMATCH-26OCT13CASLA-CAS`) | 0.43 / 0.44 (15386) | 43.5% | 47.1% | 49.5% | 51.6% [50.5%-52.1%] | 48.0% | 45.3% | 46.7% | KALSHI_LONE_OUTLIER | SHADOW_BET | +3.6 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Juan Manuel La Serna (`KXATPCHALLENGERMATCH-26OCT13CASLA-LA`) | 0.57 / 0.58 (11066) | 57.5% | 52.9% | 50.5% | 48.4% [47.9%-49.5%] | 52.0% | 55.8% | 53.9% | MODEL_LONE_OUTLIER | PASS | -4.6 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 2171.0, B 2310.0; serve-point win A 54.9%, B 44.5%; Elo A 1556.1, B 1525.0; model uncertainty 0.008
* Form inputs: days since last match A 15, B 36; matches on record A 770, B 138; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Guido Ivan Justo vs Arklon Huertas Del Pino Cordova -- ATP Challenger Santa Cruz 2 R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 22:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-13T22:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207736:207815:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arklon Huertas Del Pino Cordova (`KXATPCHALLENGERMATCH-26OCT13JUSHUE-HUE`) | 0.10 / 0.13 (860) | 11.5% | 14.9% | 11.3% | 16.8% [14.5%-18.5%] | -- | -- | -- | -- | SHADOW_BET | +3.4 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Guido Ivan Justo (`KXATPCHALLENGERMATCH-26OCT13JUSHUE-JUS`) | 0.87 / 0.90 (1615) | 88.5% | 85.1% | 88.7% | 83.2% [81.5%-85.5%] | -- | -- | -- | -- | PASS | -3.4 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 3391.0, B 981.0; serve-point win A 62.9%, B 45.1%; Elo A 1631.8, B 1403.8; model uncertainty 0.0196
* Form inputs: days since last match A 8, B 127; matches on record A 292, B 267; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.010, surface_dev_loose +0.009, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Luis Guto Miguel vs Murkel Dellien -- ATP Challenger Santa Cruz 2 R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 22:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-13T22:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:123961:213036:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Murkel Dellien (`KXATPCHALLENGERMATCH-26OCT13MIGDEV-DEV`) | 0.33 / 0.34 (2251) | 33.5% | 50.1% | 35.6% | 53.7% [48.4%-57.9%] | 37.5% | 35.9% | -- | INSUFFICIENT_INPUTS | WATCH | +16.6 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Luis Guto Miguel (`KXATPCHALLENGERMATCH-26OCT13MIGDEV-MIG`) | 0.65 / 0.66 (5814) | 65.5% | 49.9% | 64.4% | 46.3% [42.1%-51.6%] | 62.5% | 64.1% | -- | INSUFFICIENT_INPUTS | PASS | -15.6 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 921.0, B 3269.0; serve-point win A 56.9%, B 43.1%; Elo A 1434.4, B 1536.8; model uncertainty 0.0471
* Form inputs: days since last match A 15, B 8; matches on record A 24, B 367; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT13MIGDEV-DEV  (YES = Murkel Dellien)
Model: 50%
Kalshi: 34%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.032, surface_pool_high -0.021, surface_dev_loose +0.011, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE

## MARTIN SEBASTIAN ALMEIDA VELEZ vs Felipe De Dios -- M15 Quito R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13ALMDED:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MARTIN SEBASTIAN ALMEIDA VELEZ (`KXITFMATCH-26OCT13ALMDED-ALM`) | 0.07 / 0.13 (99) | 10.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Felipe De Dios (`KXITFMATCH-26OCT13ALMDED-DED`) | 0.75 / 0.93 (17) | 84.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alex Hernandez vs Gray Voelzke -- M15 Quito R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13HERVOE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex Hernandez (`KXITFMATCH-26OCT13HERVOE-HER`) | 0.93 / 0.94 (417) | 93.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gray Voelzke (`KXITFMATCH-26OCT13HERVOE-VOE`) | 0.05 / 0.06 (26) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mwendwa Mbithi vs Darwin Andres Macias Elizalde -- M15 Quito R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13MBIMAC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Darwin Andres Macias Elizalde (`KXITFMATCH-26OCT13MBIMAC-MAC`) | 0.05 / 0.07 (380) | 6.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mwendwa Mbithi (`KXITFMATCH-26OCT13MBIMAC-MBI`) | 0.91 / 0.95 (53) | 93.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Juan Sebastian Osorio vs Mateo Del Pino -- M15 Quito R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-13T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126581:210182:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mateo Del Pino (`KXITFMATCH-26OCT13OSODEL-DEL`) | 0.23 / 0.25 (136) | 24.0% | 43.1% | 52.6% | 47.9% [43.8%-50.0%] | 27.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +19.1 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Juan Sebastian Osorio (`KXITFMATCH-26OCT13OSODEL-OSO`) | 0.74 / 0.78 (6505) | 76.0% | 56.9% | 47.4% | 52.1% [50.0%-56.2%] | 72.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -19.1 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 319.0, B 190.0; serve-point win A 60.2%, B 41.1%; Elo A 1202.2, B 1176.9; model uncertainty 0.0309
* Form inputs: days since last match A 106, B 687; matches on record A 91, B 64; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT13OSODEL-DEL  (YES = Mateo Del Pino)
Model: 43%
Kalshi: 24%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.041, surface_dev_loose +0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mediorreal Arias / Sofia Sanchez vs Bernardes / Kawano Cho -- W15 Maceio R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13MEDSOFBERKAW:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bernardes / Kawano Cho (`KXITFWDOUBLES-26OCT13MEDSOFBERKAW-BERKAW`) | 0.06 / 0.67 (1) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mediorreal Arias / Sofia Sanchez (`KXITFWDOUBLES-26OCT13MEDSOFBERKAW-MEDSOF`) | 0.05 / 0.92 (0) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Melleiro / Jose Sanchez Uribe vs Konishi Camargo Silva / Labrana -- W15 Maceio R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13MELJOSKONLAB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Konishi Camargo Silva / Labrana (`KXITFWDOUBLES-26OCT13MELJOSKONLAB-KONLAB`) | 0.58 / 0.85 (0) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Melleiro / Jose Sanchez Uribe (`KXITFWDOUBLES-26OCT13MELJOSKONLAB-MELJOS`) | 0.07 / 0.39 (63) | 23.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Paula Manrique / Sigrist vs Gontijo / Zuccon -- W15 Maceio R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13PAUSIGGONZUC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gontijo / Zuccon (`KXITFWDOUBLES-26OCT13PAUSIGGONZUC-GONZUC`) | 0.10 / 0.89 (100) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Paula Manrique / Sigrist (`KXITFWDOUBLES-26OCT13PAUSIGGONZUC-PAUSIG`) | 0.05 / 0.92 (160) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Anthrop / Jansen vs Bassem Sobhy / Kohlmann de Freitas -- M15 Lexington KY R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13ANTJANBASKOH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anthrop / Jansen (`KXITFDOUBLES-26OCT13ANTJANBASKOH-ANTJAN`) | 0.08 / 0.58 (59) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bassem Sobhy / Kohlmann de Freitas (`KXITFDOUBLES-26OCT13ANTJANBASKOH-BASKOH`) | 0.06 / 0.53 (100) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Arutiunian / Pieczkowski vs Oscar Lien / Ymer -- M15 Lexington KY R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13ARUPIEOSCYME:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arutiunian / Pieczkowski (`KXITFDOUBLES-26OCT13ARUPIEOSCYME-ARUPIE`) | 0.05 / 0.95 (174) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Oscar Lien / Ymer (`KXITFDOUBLES-26OCT13ARUPIEOSCYME-OSCYME`) | 0.06 / 0.94 (100) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Abe / Yoshioka vs Akli / Sieg -- W50 Quebec City R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-13T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13ABEYOSAKLSIE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Abe / Yoshioka (`KXITFWDOUBLES-26OCT13ABEYOSAKLSIE-ABEYOS`) | 0.28 / 0.66 (104) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Akli / Sieg (`KXITFWDOUBLES-26OCT13ABEYOSAKLSIE-AKLSIE`) | 0.36 / 0.65 (100) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Martina Capurro Taborda vs Kristina Penickova -- W100 Edmond OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211920:266381:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martina Capurro Taborda (`KXITFWMATCH-26OCT13CAPPEN-CAP`) | 0.25 / 0.26 (7354) | 25.5% | 58.4% | 72.9% | 61.5% [55.8%-65.5%] | 25.7% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +32.9 pp | EXTREME (DATA_WARNING) | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kristina Penickova (`KXITFWMATCH-26OCT13CAPPEN-PEN`) | 0.74 / 0.76 (234) | 75.0% | 41.6% | 27.1% | 38.5% [34.5%-44.2%] | 74.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -33.4 pp | EXTREME (DATA_WARNING) | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3440.0, B 1178.0; serve-point win A 56.3%, B 45.3%; Elo A 1509.9, B 1497.9; model uncertainty 0.0483
* Form inputs: days since last match A 31, B 48; matches on record A 383, B 39; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT13CAPPEN-CAP  (YES = Martina Capurro Taborda)
Model: 58%
Kalshi: 26%
Gap: +33 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.040, surface_pool_high -0.041, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maria Lourdes Carle vs Kristina Liutova -- W100 Edmond OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214604:269714:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Lourdes Carle (`KXITFWMATCH-26OCT13CARLIU-CAR`) | 0.16 / 0.19 (6899) | 17.5% | 32.4% | 30.9% | 37.9% [31.9%-45.7%] | 19.5% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +14.9 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kristina Liutova (`KXITFWMATCH-26OCT13CARLIU-LIU`) | 0.81 / 0.83 (2) | 82.0% | 67.6% | 69.1% | 62.2% [54.3%-68.1%] | 80.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -14.4 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4567.0, B 754.0; serve-point win A 48.0%, B 48.6%; Elo A 1639.9, B 1701.6; model uncertainty 0.0691
* Form inputs: days since last match A 21, B 43; matches on record A 524, B 37; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.026, surface_pool_high -0.025, surface_dev_loose -0.030, surface_dev_tight +0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hanna Chang vs Madison Brengle -- W100 Edmond OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:201483:213949:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Madison Brengle (`KXITFWMATCH-26OCT13CHABRE-BRE`) | 0.68 / 0.69 (80) | 68.5% | 61.0% | 42.0% | 52.7% [48.4%-63.6%] | 71.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.5 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hanna Chang (`KXITFWMATCH-26OCT13CHABRE-CHA`) | 0.30 / 0.32 (6302) | 31.0% | 39.0% | 58.0% | 47.3% [36.4%-51.6%] | 28.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +8.0 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3084.0, B 2464.0; serve-point win A 51.4%, B 46.6%; Elo A 1608.7, B 1752.5; model uncertainty 0.0762
* Form inputs: days since last match A 176, B 48; matches on record A 519, B 1012; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.011, surface_dev_loose +0.027, surface_dev_tight -0.032
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ruby Cooling vs Natalie Kha -- W35 Redding CA R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13COOKHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ruby Cooling (`KXITFWMATCH-26OCT13COOKHA-COO`) | 0.66 / 0.68 (88) | 67.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Natalie Kha (`KXITFWMATCH-26OCT13COOKHA-KHA`) | 0.28 / 0.33 (76) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Salma Drugdova vs Mathilde Ngijol Carre -- W35 Redding CA R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:235160:264248:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Salma Drugdova (`KXITFWMATCH-26OCT13DRUNGI-DRU`) | 0.53 / 0.60 (40) | 56.5% | 68.8% | 72.3% | 65.6% [62.6%-69.0%] | -- | -- | -- | -- | PASS | +12.3 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mathilde Ngijol Carre (`KXITFWMATCH-26OCT13DRUNGI-NGI`) | 0.38 / 0.42 (33) | 40.0% | 31.2% | 27.7% | 34.4% [31.0%-37.4%] | -- | -- | -- | -- | PASS | -8.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1429.0, B 227.0; serve-point win A 53.7%, B 49.9%; Elo A 1474.7, B 1369.4; model uncertainty 0.0322
* Form inputs: days since last match A 435, B 239; matches on record A 158, B 35; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.019, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Shihomi Li Xuan Leong vs Nao Nishino -- W35 Redding CA R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:263622:265628:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shihomi Li Xuan Leong (`KXITFWMATCH-26OCT13LEONIS-LEO`) | 0.32 / 0.37 (39) | 34.5% | 51.6% | 75.5% | 53.7% [48.9%-58.9%] | -- | -- | -- | -- | PASS | +17.1 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nao Nishino (`KXITFWMATCH-26OCT13LEONIS-NIS`) | 0.59 / 0.64 (42) | 61.5% | 48.4% | 24.5% | 46.3% [41.1%-51.1%] | -- | -- | -- | -- | PASS | -13.1 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 969.0, B 295.0; serve-point win A 55.4%, B 44.9%; Elo A 1363.2, B 1367.9; model uncertainty 0.05
* Form inputs: days since last match A 330, B 442; matches on record A 52, B 12; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT13LEONIS-LEO  (YES = Shihomi Li Xuan Leong)
Model: 52%
Kalshi: 34%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Clemence Mercier vs Sara Saito -- W50 Quebec City R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260170:260855:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Clemence Mercier (`KXITFWMATCH-26OCT13MERSAI-MER`) | 0.12 / 0.13 (289) | 12.5% | 12.8% | 44.2% | 22.8% [16.8%-27.5%] | -- | -- | -- | -- | PASS | +0.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sara Saito (`KXITFWMATCH-26OCT13MERSAI-SAI`) | 0.87 / 0.88 (452) | 87.5% | 87.2% | 55.8% | 77.2% [72.5%-83.2%] | -- | -- | -- | -- | PASS | -0.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 263.0, B 3341.0; serve-point win A 50.4%, B 41.1%; Elo A 1329.2, B 1574.9; model uncertainty 0.0535
* Form inputs: days since last match A 365, B 15; matches on record A 26, B 198; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.031, surface_pool_high +0.029, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Abigail Rencheli vs Juliana Nicole Singeorzan -- W35 Redding CA R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221741:270414:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Abigail Rencheli (`KXITFWMATCH-26OCT13RENSIN-REN`) | 0.59 / 0.66 (400) | 62.5% | 77.3% | 54.3% | 63.6% [63.1%-64.6%] | -- | -- | -- | -- | PASS | +14.8 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Juliana Nicole Singeorzan (`KXITFWMATCH-26OCT13RENSIN-SIN`) | 0.31 / 0.36 (37) | 33.5% | 22.7% | 45.7% | 36.4% [35.4%-36.9%] | -- | -- | -- | -- | PASS | -10.8 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 739.0, B 123.0; serve-point win A 55.8%, B 49.8%; Elo A 1350.2, B 1242.3; model uncertainty 0.0075
* Form inputs: days since last match A 316, B 239; matches on record A 45, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Akasha Urhobo vs Xinyu Gao -- W100 Edmond OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-13T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214386:259857:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xinyu Gao (`KXITFWMATCH-26OCT13URHGAO-GAO`) | 0.55 / 0.57 (387) | 56.0% | 54.4% | 36.5% | 45.2% [41.1%-52.7%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Akasha Urhobo (`KXITFWMATCH-26OCT13URHGAO-URH`) | 0.42 / 0.45 (44) | 43.5% | 45.6% | 63.5% | 54.8% [47.3%-58.9%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +2.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3335.0, B 3203.0; serve-point win A 54.9%, B 44.3%; Elo A 1625.7, B 1711.8; model uncertainty 0.058
* Form inputs: days since last match A 50, B 10; matches on record A 174, B 419; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.005, surface_dev_loose +0.005, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pedro Boscardin Dias vs Facundo Mena -- ATP Challenger Santa Cruz 2 R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-14T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106057:208046:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pedro Boscardin Dias (`KXATPCHALLENGERMATCH-26OCT13BOSMEN-BOS`) | 0.51 / 0.52 (2408) | 51.5% | 41.8% | 30.0% | 32.2% [31.3%-33.6%] | -- | -- | -- | -- | PASS | -9.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Facundo Mena (`KXATPCHALLENGERMATCH-26OCT13BOSMEN-MEN`) | 0.48 / 0.49 (11424) | 48.5% | 58.2% | 70.0% | 67.8% [66.4%-68.7%] | -- | -- | -- | -- | WATCH | +9.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3520.0, B 3770.0; serve-point win A 60.4%, B 38.0%; Elo A 1548.9, B 1631.9; model uncertainty 0.0115
* Form inputs: days since last match A 8, B 15; matches on record A 293, B 905; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.009, surface_dev_loose -0.005, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Thiago Cigarran vs Nicolas Kicker -- ATP Challenger Santa Cruz 2 R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-14T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106044:208532:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thiago Cigarran (`KXATPCHALLENGERMATCH-26OCT13CIGKIC-CIG`) | 0.21 / 0.22 (14) | 21.5% | 14.3% | 13.4% | 11.0% [9.8%-12.2%] | -- | -- | -- | -- | PASS | -7.2 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nicolas Kicker (`KXATPCHALLENGERMATCH-26OCT13CIGKIC-KIC`) | 0.78 / 0.79 (16160) | 78.5% | 85.7% | 86.6% | 89.0% [87.8%-90.2%] | -- | -- | -- | -- | SHADOW_BET | +7.2 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 552.0, B 3106.0; serve-point win A 52.6%, B 39.3%; Elo A 1243.7, B 1624.0; model uncertainty 0.012
* Form inputs: days since last match A 57, B 22; matches on record A 111, B 676; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight +0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Cruz Alcon / Enrique Menzel Piccioli vs Matta / Rengifo -- M15 Quito R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13CRUENRMATREN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cruz Alcon / Enrique Menzel Piccioli (`KXITFDOUBLES-26OCT13CRUENRMATREN-CRUENR`) | 0.05 / 0.92 (1) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matta / Rengifo (`KXITFDOUBLES-26OCT13CRUENRMATREN-MATREN`) | 0.07 / 0.94 (100) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Esteban Rico Arias / Salazar vs Camacho / Carlos Fuentes Vasquez -- M15 Quito R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13ESTSALCAMCAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Camacho / Carlos Fuentes Vasquez (`KXITFDOUBLES-26OCT13ESTSALCAMCAR-CAMCAR`) | 0.07 / 0.93 (100) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Esteban Rico Arias / Salazar (`KXITFDOUBLES-26OCT13ESTSALCAMCAR-ESTSAL`) | 0.05 / 0.95 (174) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Sebastian Gorzny vs Edward Winter -- M25 Austin TX R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210399:210478:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sebastian Gorzny (`KXITFMATCH-26OCT13GORWIN-GOR`) | 0.61 / 0.66 (52) | 63.5% | 66.3% | 89.3% | 67.2% [58.1%-75.8%] | -- | -- | -- | -- | PASS | +2.8 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Edward Winter (`KXITFMATCH-26OCT13GORWIN-WIN`) | 0.33 / 0.35 (32) | 34.0% | 33.7% | 10.7% | 32.8% [24.2%-41.9%] | -- | -- | -- | -- | PASS | -0.3 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 993.0, B 459.0; serve-point win A 63.5%, B 39.8%; Elo A 1495.2, B 1440.1; model uncertainty 0.0884
* Form inputs: days since last match A 29, B 75; matches on record A 37, B 112; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.018, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alastair Gray vs Spencer Johnson -- M25 Austin TX R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202400:212958:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alastair Gray (`KXITFMATCH-26OCT13GRAJOH-GRA`) | 0.40 / 0.42 (186) | 41.0% | 55.7% | 51.5% | 57.3% [54.8%-60.2%] | -- | -- | -- | -- | WATCH | +14.7 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Spencer Johnson (`KXITFMATCH-26OCT13GRAJOH-JOH`) | 0.57 / 0.61 (6187) | 59.0% | 44.3% | 48.5% | 42.7% [39.8%-45.2%] | -- | -- | -- | -- | PASS | -14.7 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2063.0, B 393.0; serve-point win A 66.7%, B 34.4%; Elo A 1531.8, B 1467.3; model uncertainty 0.0271
* Form inputs: days since last match A 50, B 50; matches on record A 259, B 17; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.014, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Diego Hidalgo / Mariano Kestelboim vs Nicolas Ciancaglini / Agustin Eduardo Cuellar Lorberg -- ATP Challenger Santa Cruz 2 R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-14T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13HIDKESCIACUE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Ciancaglini / Agustin Eduardo Cuellar Lorberg (`KXATPCHALLENGERDOUBLES-26OCT13HIDKESCIACUE-CIACUE`) | 0.05 / 0.11 (49) | 8.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Diego Hidalgo / Mariano Kestelboim (`KXATPCHALLENGERDOUBLES-26OCT13HIDKESCIACUE-HIDKES`) | 0.87 / 0.95 (440) | 91.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Aidan Mchugh vs Karl Poling -- M25 Austin TX R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202420:207202:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aidan Mchugh (`KXITFMATCH-26OCT13MCHPOL-MCH`) | 0.53 / 0.57 (1624) | 55.0% | 62.5% | 50.0% | 56.5% [52.0%-62.8%] | -- | -- | -- | -- | PASS | +7.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Karl Poling (`KXITFMATCH-26OCT13MCHPOL-POL`) | 0.42 / 0.44 (6) | 43.0% | 37.5% | 50.0% | 43.5% [37.2%-48.0%] | -- | -- | -- | -- | PASS | -5.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2336.0, B 890.0; serve-point win A 64.2%, B 38.4%; Elo A 1481.7, B 1413.1; model uncertainty 0.0541
* Form inputs: days since last match A 701, B 22; matches on record A 414, B 74; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.035, surface_dev_loose -0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sebastian Dominguez Collado / Echazu vs Hollender / Meneo -- M15 Quito R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13SEBECHHOLMEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hollender / Meneo (`KXITFDOUBLES-26OCT13SEBECHHOLMEN-HOLMEN`) | 0.60 / 0.70 (100) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sebastian Dominguez Collado / Echazu (`KXITFDOUBLES-26OCT13SEBECHHOLMEN-SEBECH`) | 0.08 / 0.33 (37) | 20.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Li Tu vs Kaylan Bigun -- M25 Austin TX R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111454:210744:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kaylan Bigun (`KXITFMATCH-26OCT13TUXBIG-BIG`) | 0.38 / 0.39 (7074) | 38.5% | 15.3% | 19.4% | 14.9% [12.4%-16.1%] | -- | -- | -- | -- | PASS | -23.2 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Li Tu (`KXITFMATCH-26OCT13TUXBIG-TUX`) | 0.60 / 0.62 (22) | 61.0% | 84.7% | 80.6% | 85.1% [83.9%-87.6%] | -- | -- | -- | -- | PASS | +23.7 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2962.0, B 734.0; serve-point win A 66.0%, B 42.0%; Elo A 1597.7, B 1267.4; model uncertainty 0.0186
* Form inputs: days since last match A 52, B 708; matches on record A 309, B 41; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT13TUXBIG-TUX  (YES = Li Tu)
Model: 85%
Kalshi: 61%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.006, surface_pool_high -0.006, surface_dev_loose +0.009, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alicea / Snells vs Kupres / Xu -- W50 Quebec City R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13ALISNEKUPXUX:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alicea / Snells (`KXITFWDOUBLES-26OCT13ALISNEKUPXUX-ALISNE`) | 0.40 / 0.59 (40) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kupres / Xu (`KXITFWDOUBLES-26OCT13ALISNEKUPXUX-KUPXUX`) | 0.34 / 0.56 (100) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Arseneault / Lacasse vs Demers / Thibault -- W50 Quebec City R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13ARSLACDEMTHI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arseneault / Lacasse (`KXITFWDOUBLES-26OCT13ARSLACDEMTHI-ARSLAC`) | 0.20 / 0.95 (111) | 57.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Demers / Thibault (`KXITFWDOUBLES-26OCT13ARSLACDEMTHI-DEMTHI`) | 0.05 / 0.73 (100) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Azambuja Werner / DE MATTOS SILVA vs Krajmer / Souza -- W15 Maceio R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13AZADEMKRASOU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Azambuja Werner / DE MATTOS SILVA (`KXITFWDOUBLES-26OCT13AZADEMKRASOU-AZADEM`) | 0.05 / 0.95 (213) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Krajmer / Souza (`KXITFWDOUBLES-26OCT13AZADEMKRASOU-KRASOU`) | 0.07 / 0.95 (111) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Berlanga Bandera / Okalova vs Johnson / Rapolu -- W100 Edmond OK R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13BEROKAJOHRAP:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Berlanga Bandera / Okalova (`KXITFWDOUBLES-26OCT13BEROKAJOHRAP-BEROKA`) | 0.31 / 0.56 (49) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Johnson / Rapolu (`KXITFWDOUBLES-26OCT13BEROKAJOHRAP-JOHRAP`) | 0.44 / 0.67 (168) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Patsy Daughters vs Sydney Jara -- W35 Redding CA R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260851:269801:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Patsy Daughters (`KXITFWMATCH-26OCT13DAUJAR-DAU`) | 0.07 / 0.10 (100) | 8.5% | 25.0% | 56.9% | 32.4% [31.5%-33.4%] | -- | -- | -- | -- | PASS | +16.5 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sydney Jara (`KXITFWMATCH-26OCT13DAUJAR-JAR`) | 0.87 / 0.93 (6174) | 90.0% | 75.0% | 43.1% | 67.6% [66.6%-68.5%] | -- | -- | -- | -- | PASS | -15.0 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 49.0, B 635.0; serve-point win A 50.7%, B 44.3%; Elo A 1148.2, B 1282.9; model uncertainty 0.0096
* Form inputs: days since last match A 463, B 239; matches on record A 50, B 21; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT13DAUJAR-DAU  (YES = Patsy Daughters)
Model: 25%
Kalshi: 8%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Estevez / Florencia Urrutia vs Lopez / Plaza -- W15 Maceio R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13ESTFLOLOPPLA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Estevez / Florencia Urrutia (`KXITFWDOUBLES-26OCT13ESTFLOLOPPLA-ESTFLO`) | 0.71 / 0.88 (0) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lopez / Plaza (`KXITFWDOUBLES-26OCT13ESTFLOLOPPLA-LOPPLA`) | 0.10 / 0.21 (0) | 15.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Fernanda Lopes / Schincariol Delatorre Barbosa vs Ayala / Romero -- W15 Maceio R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13FERSCHAYAROM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ayala / Romero (`KXITFWDOUBLES-26OCT13FERSCHAYAROM-AYAROM`) | 0.81 / 0.95 (113) | 88.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fernanda Lopes / Schincariol Delatorre Barbosa (`KXITFWDOUBLES-26OCT13FERSCHAYAROM-FERSCH`) | 0.06 / 0.13 (28) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Imogen Haddad vs Virginia Crocker -- W35 Redding CA R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260559:270059:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Virginia Crocker (`KXITFWMATCH-26OCT13HADCRO-CRO`) | 0.17 / 0.22 (6111) | 19.5% | 31.2% | 27.6% | 38.6% [37.5%-39.6%] | -- | -- | -- | -- | PASS | +11.7 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Imogen Haddad (`KXITFWMATCH-26OCT13HADCRO-HAD`) | 0.76 / 0.80 (44) | 78.0% | 68.8% | 72.4% | 61.5% [60.4%-62.5%] | -- | -- | -- | -- | PASS | -9.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 441.0; serve-point win A 58.4%, B 45.3%; Elo A 1303.0, B 1223.0; model uncertainty 0.0101
* Form inputs: days since last match A 701, B 288; matches on record A 35, B 7; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Heuser / Sharabura vs Herrero Linana / Zamarripa -- W100 Edmond OK R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13HEUSHAHERZAM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Herrero Linana / Zamarripa (`KXITFWDOUBLES-26OCT13HEUSHAHERZAM-HERZAM`) | 0.81 / 0.95 (111) | 88.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Heuser / Sharabura (`KXITFWDOUBLES-26OCT13HEUSHAHERZAM-HEUSHA`) | 0.08 / 0.14 (29) | 11.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Yoana Konstantinova vs Delaney Letzel -- W35 Redding CA R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-14T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13KONLET:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yoana Konstantinova (`KXITFWMATCH-26OCT13KONLET-KON`) | 0.35 / 0.40 (13) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Delaney Letzel (`KXITFWMATCH-26OCT13KONLET-LET`) | 0.58 / 0.61 (54) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lahey / Vagramov vs Elena Cabezas Dominguez / Rogers -- W100 Edmond OK R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13LAHVAGELEROG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elena Cabezas Dominguez / Rogers (`KXITFWDOUBLES-26OCT13LAHVAGELEROG-ELEROG`) | 0.56 / 0.73 (5) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lahey / Vagramov (`KXITFWDOUBLES-26OCT13LAHVAGELEROG-LAHVAG`) | 0.08 / 0.38 (40) | 23.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## McAdoo / Strakhova vs Mandlik / Zarazua -- W100 Edmond OK R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13MCASTRMANZAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mandlik / Zarazua (`KXITFWDOUBLES-26OCT13MCASTRMANZAR-MANZAR`) | 0.34 / 0.50 (6) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| McAdoo / Strakhova (`KXITFWDOUBLES-26OCT13MCASTRMANZAR-MCASTR`) | 0.22 / 0.60 (62) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mao Mushika vs Tia Messerli -- W35 Redding CA R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:239446:270475:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tia Messerli (`KXITFWMATCH-26OCT13MUSMES-MES`) | 0.08 / 0.11 (40) | 9.5% | 8.1% | 27.7% | 19.5% [17.4%-21.0%] | -- | -- | -- | -- | PASS | -1.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mao Mushika (`KXITFWMATCH-26OCT13MUSMES-MUS`) | 0.88 / 0.92 (6104) | 90.0% | 91.9% | 72.3% | 80.5% [79.0%-82.6%] | -- | -- | -- | -- | PASS | +1.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 793.0, B 287.0; serve-point win A 56.3%, B 54.1%; Elo A 1518.2, B 1255.6; model uncertainty 0.0179
* Form inputs: days since last match A 372, B 169; matches on record A 125, B 5; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.015, surface_dev_loose +0.000, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arseneault / Mesarovic vs Cosnet / Klyachkin -- M15 Lexington KY R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13ARSMESCOSKLY:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arseneault / Mesarovic (`KXITFDOUBLES-26OCT13ARSMESCOSKLY-ARSMES`) | 0.05 / 0.95 (174) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cosnet / Klyachkin (`KXITFDOUBLES-26OCT13ARSMESCOSKLY-COSKLY`) | 0.06 / 0.94 (100) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Barrett / Corwin vs Kapasi / Sheldon -- M15 Lexington KY R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13BARCORKAPSHE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barrett / Corwin (`KXITFDOUBLES-26OCT13BARCORKAPSHE-BARCOR`) | 0.22 / 0.90 (0) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kapasi / Sheldon (`KXITFDOUBLES-26OCT13BARCORKAPSHE-KAPSHE`) | 0.07 / 0.71 (46) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Blando / Overmyer vs Baker / Benson -- M25 Austin TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13BLAOVEBAKBEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Baker / Benson (`KXITFDOUBLES-26OCT13BLAOVEBAKBEN-BAKBEN`) | 0.08 / 0.78 (100) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Blando / Overmyer (`KXITFDOUBLES-26OCT13BLAOVEBAKBEN-BLAOVE`) | 0.20 / 0.93 (1) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Blando / Vasser vs EMANUEL AMBROGI / Alexander Rodriguez -- M25 Austin TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13BLAVASEMAALE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Blando / Vasser (`KXITFDOUBLES-26OCT13BLAVASEMAALE-BLAVAS`) | 0.33 / 0.64 (46) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| EMANUEL AMBROGI / Alexander Rodriguez (`KXITFDOUBLES-26OCT13BLAVASEMAALE-EMAALE`) | 0.35 / 0.61 (0) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Debru / Marionneau vs Bynoe / Vance -- M25 Austin TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13DEBMARBYNVAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bynoe / Vance (`KXITFDOUBLES-26OCT13DEBMARBYNVAN-BYNVAN`) | 0.27 / 0.51 (100) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Debru / Marionneau (`KXITFDOUBLES-26OCT13DEBMARBYNVAN-DEBMAR`) | 0.42 / 0.75 (138) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Exsted / Goode vs Gogineni / Young -- M15 Lexington KY R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13EXSGOOGOGYOU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Exsted / Goode (`KXITFDOUBLES-26OCT13EXSGOOGOGYOU-EXSGOO`) | 0.05 / 0.42 (43) | 23.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gogineni / Young (`KXITFDOUBLES-26OCT13EXSGOOGOGYOU-GOGYOU`) | 0.51 / 0.62 (20) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Forde / Sickenberger vs Loutit / Stephenson -- M15 Lexington KY R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13FORSICLOUSTE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Forde / Sickenberger (`KXITFDOUBLES-26OCT13FORSICLOUSTE-FORSIC`) | 0.05 / 0.84 (400) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Loutit / Stephenson (`KXITFDOUBLES-26OCT13FORSICLOUSTE-LOUSTE`) | 0.22 / 0.94 (44) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Roddick / Tokac vs Braswell / Braswell -- M25 Austin TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13RODTOKBRABRA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Braswell / Braswell (`KXITFDOUBLES-26OCT13RODTOKBRABRA-BRABRA`) | 0.05 / 0.95 (74) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Roddick / Tokac (`KXITFDOUBLES-26OCT13RODTOKBRABRA-RODTOK`) | 0.05 / 0.95 (74) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Grubor / Kuhl vs Bayerlova / Gimbrere -- W50 Quebec City R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13GRUKUHBAYGIM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bayerlova / Gimbrere (`KXITFWDOUBLES-26OCT13GRUKUHBAYGIM-BAYGIM`) | 0.80 / 0.94 (100) | 87.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Grubor / Kuhl (`KXITFWDOUBLES-26OCT13GRUKUHBAYGIM-GRUKUH`) | 0.05 / 0.15 (29) | 10.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Eduardo Ribeiro vs Juan Carlos Prado Angelo -- ATP Challenger Santa Cruz 2 R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 01:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-14T01:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200495:210178:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Carlos Prado Angelo (`KXATPCHALLENGERMATCH-26OCT13RIBPRA-PRA`) | 0.75 / 0.76 (381) | 75.5% | 70.3% | 58.2% | 62.6% [61.7%-65.0%] | -- | -- | -- | -- | PASS | -5.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Eduardo Ribeiro (`KXATPCHALLENGERMATCH-26OCT13RIBPRA-RIB`) | 0.24 / 0.25 (600) | 24.5% | 29.6% | 41.8% | 37.4% [35.0%-38.4%] | -- | -- | -- | -- | SHADOW_BET | +5.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2300.0, B 3817.0; serve-point win A 58.4%, B 37.5%; Elo A 1512.2, B 1660.0; model uncertainty 0.0169
* Form inputs: days since last match A 8, B 8; matches on record A 267, B 217; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Thiago Seyboth Wild vs Mateus Alves -- ATP Challenger Santa Cruz 2 R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 01:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-14T01:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:127123:205734:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mateus Alves (`KXATPCHALLENGERMATCH-26OCT13SEYALV-ALV`) | 0.15 / 0.16 (743) | 15.5% | 16.0% | 9.8% | 13.9% [10.8%-18.9%] | -- | -- | -- | -- | PASS | +0.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Thiago Seyboth Wild (`KXATPCHALLENGERMATCH-26OCT13SEYALV-SEY`) | 0.84 / 0.85 (103) | 84.5% | 84.0% | 90.2% | 86.1% [81.0%-89.2%] | -- | -- | -- | -- | WATCH | -0.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3996.0, B 1772.0; serve-point win A 69.2%, B 38.9%; Elo A 1742.2, B 1502.8; model uncertainty 0.0408
* Form inputs: days since last match A 8, B 15; matches on record A 485, B 332; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.016, surface_dev_loose +0.011, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Gonzalo Villanueva vs Carlos Maria Zarate -- ATP Challenger Santa Cruz 2 R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 01:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-14T01:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106380:212785:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gonzalo Villanueva (`KXATPCHALLENGERMATCH-26OCT13VILZAR-VIL`) | 0.70 / 0.72 (3032) | 71.0% | 88.6% | 81.2% | 85.7% [84.4%-86.8%] | -- | -- | -- | -- | WATCH | +17.6 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carlos Maria Zarate (`KXATPCHALLENGERMATCH-26OCT13VILZAR-ZAR`) | 0.28 / 0.30 (745) | 29.0% | 11.4% | 18.8% | 14.3% [13.2%-15.6%] | -- | -- | -- | -- | PASS | -17.6 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3636.0, B 812.0; serve-point win A 63.8%, B 45.5%; Elo A 1519.9, B 1175.5; model uncertainty 0.0122
* Form inputs: days since last match A 8, B 15; matches on record A 730, B 24; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT13VILZAR-VIL  (YES = Gonzalo Villanueva)
Model: 89%
Kalshi: 71%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.003, surface_pool_high +0.009, surface_dev_loose +0.006, surface_dev_tight -0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE

## Alvarado / Mbithi vs De Dios / Grippo -- M15 Quito R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13ALVMBIDEDGRI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alvarado / Mbithi (`KXITFDOUBLES-26OCT13ALVMBIDEDGRI-ALVMBI`) | 0.14 / 0.82 (0) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| De Dios / Grippo (`KXITFDOUBLES-26OCT13ALVMBIDEDGRI-DEDGRI`) | 0.10 / 0.57 (0) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Casares / Andre Galarraga vs Covato / Voelzke -- M15 Quito R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13CASANDCOVVOE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Casares / Andre Galarraga (`KXITFDOUBLES-26OCT13CASANDCOVVOE-CASAND`) | 0.05 / 0.92 (160) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Covato / Voelzke (`KXITFDOUBLES-26OCT13CASANDCOVVOE-COVVOE`) | 0.10 / 0.93 (63) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jo-Yee Chan vs Mell Elizabeth Reasco Gonzalez -- W35 Redding CA R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 02:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221242:270125:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jo-Yee Chan (`KXITFWMATCH-26OCT13CHAREA-CHA`) | 0.45 / 0.46 (46) | 45.5% | 34.0% | 29.1% | 32.9% [31.9%-34.9%] | -- | -- | -- | -- | PASS | -11.5 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mell Elizabeth Reasco Gonzalez (`KXITFWMATCH-26OCT13CHAREA-REA`) | 0.53 / 0.54 (182) | 53.5% | 66.0% | 70.9% | 67.1% [65.1%-68.1%] | -- | -- | -- | -- | PASS | +12.5 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 531.0, B 2361.0; serve-point win A 51.2%, B 45.8%; Elo A 1410.0, B 1519.0; model uncertainty 0.0146
* Form inputs: days since last match A 435, B 169; matches on record A 8, B 178; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.020, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amelie Justine Hejtmanek vs Annika Penickova -- W35 Redding CA R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 02:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260323:266379:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amelie Justine Hejtmanek (`KXITFWMATCH-26OCT13HEJPEN-HEJ`) | 0.06 / 0.09 (2494) | 7.5% | 19.0% | 25.7% | 30.2% [24.9%-35.4%] | -- | -- | -- | -- | WATCH | +11.5 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Annika Penickova (`KXITFWMATCH-26OCT13HEJPEN-PEN`) | 0.91 / 0.93 (2) | 92.0% | 81.0% | 74.3% | 69.8% [64.6%-75.1%] | -- | -- | -- | -- | PASS | -11.0 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1296.0, B 702.0; serve-point win A 52.0%, B 41.4%; Elo A 1348.8, B 1478.8; model uncertainty 0.0527
* Form inputs: days since last match A 176, B 49; matches on record A 54, B 38; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.023, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Krisha Mahendran vs Jenna DeFalco -- W35 Redding CA R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 02:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221914:266645:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jenna DeFalco (`KXITFWMATCH-26OCT13MAHDEF-DEF`) | 0.45 / 0.47 (11) | 46.0% | 32.7% | 17.8% | 40.5% [32.5%-50.0%] | -- | -- | -- | -- | PASS | -13.3 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Krisha Mahendran (`KXITFWMATCH-26OCT13MAHDEF-MAH`) | 0.51 / 0.54 (24) | 52.5% | 67.3% | 82.2% | 59.5% [50.0%-67.5%] | -- | -- | -- | -- | PASS | +14.8 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 456.0, B 1687.0; serve-point win A 55.2%, B 48.1%; Elo A 1450.9, B 1442.5; model uncertainty 0.0877
* Form inputs: days since last match A 372, B 169; matches on record A 13, B 247; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.005, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Connie Ma vs Victoria Rodriguez -- W35 Redding CA R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 02:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211874:221143:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Connie Ma (`KXITFWMATCH-26OCT13MAXROD-MAX`) | 0.77 / 0.80 (7657) | 78.5% | 46.5% | 53.2% | 39.4% [38.4%-41.5%] | -- | -- | -- | -- | PASS | -32.0 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Victoria Rodriguez (`KXITFWMATCH-26OCT13MAXROD-ROD`) | 0.21 / 0.23 (417) | 22.0% | 53.5% | 46.8% | 60.6% [58.5%-61.6%] | -- | -- | -- | -- | PASS | +31.5 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 2050.0; serve-point win A 49.5%, B 49.9%; Elo A 1475.0, B 1548.3; model uncertainty 0.0156
* Form inputs: days since last match A 1835, B 31; matches on record A 21, B 574; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT13MAXROD-ROD  (YES = Victoria Rodriguez)
Model: 53%
Kalshi: 22%
Gap: +31 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.010, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sonay Kartal vs Belinda Bencic -- WTA Wuhan R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-13 06:00Z
* Current expected start: 2026-10-14 03:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-13 14:56Z
* Recommended handicap-by time: 2026-10-14 02:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1260_MIN

WTA (MASTERS_1000) · Hard · scheduled 2026-10-13T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202505:222661:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Belinda Bencic (`KXWTAMATCH-26OCT12KARBEN-BEN`) | 0.68 / 0.69 (47928) | 68.5% | 66.3% | 57.7% | 61.8% [58.7%-72.7%] | -- | -- | -- | -- | PASS | -2.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sonay Kartal (`KXWTAMATCH-26OCT12KARBEN-KAR`) | 0.32 / 0.33 (29737) | 32.5% | 33.7% | 42.3% | 38.2% [27.3%-41.3%] | -- | -- | -- | -- | WATCH | +1.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3052.0, B 3571.0; serve-point win A 57.6%, B 39.1%; Elo A 1936.6, B 2085.1; model uncertainty 0.0697
* Form inputs: days since last match A 1, B 8; matches on record A 253, B 673; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.029, surface_pool_high +0.030, surface_dev_loose +0.000, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT12KARBEN-22` Over 21.5 games: 0.43/0.44 mid 43.5%, model 62.1% (projection_v2.0 (prediction ledger)) -- gap +18.6 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT12KARBEN-27` Over 26.5 games: 0.21/0.33 mid 27.0%, model 39.0% (projection_v2.0 (prediction ledger)) -- gap +12.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT12KARBEN-17` Over 16.5 games: 0.79/0.91 mid 85.0%, model 94.1% (projection_v2.0 (prediction ledger)) -- gap +9.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT12KARBEN-1-KAR` Will Sonay Kartal win set 1 in the Sonay Kartal vs Belinda Bencic match: 0.35/0.37 mid 36.0%, model 38.9% (projection_v2.0 (prediction ledger)) -- gap +2.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT12KARBEN-2-KAR` Will Sonay Kartal win set 2 in the Sonay Kartal vs Belinda Bencic match: 0.34/0.38 mid 36.0%, model 38.9% (projection_v2.0 (prediction ledger)) -- gap +2.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT12KARBEN-2-BEN` Will Belinda Bencic win set 2 in the Sonay Kartal vs Belinda Bencic match: 0.61/0.66 mid 63.5%, model 61.1% (projection_v2.0 (prediction ledger)) -- gap -2.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT12KARBEN-1-BEN` Will Belinda Bencic win set 1 in the Sonay Kartal vs Belinda Bencic match: 0.62/0.64 mid 63.0%, model 61.1% (projection_v2.0 (prediction ledger)) -- gap -1.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Marie Bouzkova vs Maja Chwalinska -- WTA Wuhan R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-14 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-14 03:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-13 14:56Z
* Recommended handicap-by time: 2026-10-14 02:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-14T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213631:216081:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marie Bouzkova (`KXWTAMATCH-26OCT13BOUCHW-BOU`) | 0.65 / 0.66 (1870) | 65.5% | 59.6% | 33.9% | 45.7% [40.5%-59.5%] | -- | 66.9% | -- | INSUFFICIENT_INPUTS | PASS | -5.9 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maja Chwalinska (`KXWTAMATCH-26OCT13BOUCHW-CHW`) | 0.33 / 0.35 (27618) | 34.0% | 40.4% | 66.1% | 54.3% [40.5%-59.5%] | -- | 34.2% | -- | INSUFFICIENT_INPUTS | WATCH | +6.4 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4089.0, B 3543.0; serve-point win A 53.9%, B 47.9%; Elo A 1969.4, B 1800.8; model uncertainty 0.0952
* Form inputs: days since last match A 1, B 0; matches on record A 643, B 392; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.011, surface_dev_loose -0.026, surface_dev_tight +0.021
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT13BOUCHW-21` Over 20.5 games: 0.49/0.50 mid 49.5%, model 65.8% (projection_v2.0 (prediction ledger)) -- gap +16.4 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT13BOUCHW-26` Over 25.5 games: 0.26/0.32 mid 29.0%, model 42.7% (projection_v2.0 (prediction ledger)) -- gap +13.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT13BOUCHW-2-CHW` Will Maja Chwalinska win set 2 in the Marie Bouzkova vs Maja Chwalinska match: 0.34/0.38 mid 36.0%, model 43.6% (projection_v2.0 (prediction ledger)) -- gap +7.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT13BOUCHW-1-CHW` Will Maja Chwalinska win set 1 in the Marie Bouzkova vs Maja Chwalinska match: 0.36/0.38 mid 37.0%, model 43.6% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT13BOUCHW-2-BOU` Will Marie Bouzkova win set 2 in the Marie Bouzkova vs Maja Chwalinska match: 0.61/0.64 mid 62.5%, model 56.4% (projection_v2.0 (prediction ledger)) -- gap -6.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT13BOUCHW-1-BOU` Will Marie Bouzkova win set 1 in the Marie Bouzkova vs Maja Chwalinska match: 0.61/0.63 mid 62.0%, model 56.4% (projection_v2.0 (prediction ledger)) -- gap -5.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26OCT13BOUCHW-16` Over 15.5 games: 0.90/0.97 mid 93.5%, model 96.4% (projection_v2.0 (prediction ledger)) -- gap +2.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Magdalena Frech vs Iga Swiatek -- WTA Wuhan R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-14 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-14 03:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-13 14:56Z
* Recommended handicap-by time: 2026-10-14 02:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-14T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211684:216347:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Magdalena Frech (`KXWTAMATCH-26OCT13FRESWI-FRE`) | 0.08 / 0.09 (20042) | 8.5% | 12.2% | 7.1% | 8.4% [6.9%-12.3%] | 10.1% | 7.9% | 7.9% | MARKETS_AGREE | PASS | +3.6 pp | NORMAL | FRESH | A / LIMITED | EXTERNAL_STALE | VERIFIED |
| Iga Swiatek (`KXWTAMATCH-26OCT13FRESWI-SWI`) | 0.91 / 0.92 (6536) | 91.5% | 87.8% | 92.9% | 91.6% [87.7%-93.1%] | 89.9% | 92.2% | 92.2% | MARKETS_AGREE | PASS | -3.6 pp | NORMAL | FRESH | A / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4552.0, B 4863.0; serve-point win A 52.6%, B 38.5%; Elo A 1837.2, B 2175.8; model uncertainty 0.027
* Form inputs: days since last match A 1, B 4; matches on record A 701, B 544; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.002, surface_pool_high -0.000, surface_dev_loose +0.002, surface_dev_tight -0.004
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 6 carry a model probability
  * `KXWTAGTOTAL-26OCT13FRESWI-19` Over 18.5 games: 0.44/0.45 mid 44.5%, model 65.8% (projection_v2.0 (prediction ledger)) -- gap +21.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT13FRESWI-24` Over 23.5 games: 0.02/0.51 mid 26.5%, model 35.0% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT13FRESWI-1-FRE` Will Magdalena Frech win set 1 in the Magdalena Frech vs Iga Swiatek match: 0.12/0.16 mid 14.0%, model 21.8% (projection_v2.0 (prediction ledger)) -- gap +7.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT13FRESWI-1-SWI` Will Iga Swiatek win set 1 in the Magdalena Frech vs Iga Swiatek match: 0.85/0.86 mid 85.5%, model 78.2% (projection_v2.0 (prediction ledger)) -- gap -7.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT13FRESWI-2-FRE` Will Magdalena Frech win set 2 in the Magdalena Frech vs Iga Swiatek match: 0.13/0.16 mid 14.5%, model 21.8% (projection_v2.0 (prediction ledger)) -- gap +7.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT13FRESWI-2-SWI` Will Iga Swiatek win set 2 in the Magdalena Frech vs Iga Swiatek match: 0.85/0.86 mid 85.5%, model 78.2% (projection_v2.0 (prediction ledger)) -- gap -7.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Elina Svitolina vs Liudmila Samsonova -- WTA Wuhan R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-14 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-14 03:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-13 14:56Z
* Recommended handicap-by time: 2026-10-14 02:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-14T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202494:214643:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liudmila Samsonova (`KXWTAMATCH-26OCT13SVISAM-SAM`) | 0.28 / 0.29 (4733) | 28.5% | 30.8% | 21.3% | 22.1% [20.9%-24.8%] | -- | 28.8% | 28.8% | MARKETS_AGREE | PASS | +2.3 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Elina Svitolina (`KXWTAMATCH-26OCT13SVISAM-SVI`) | 0.71 / 0.72 (24506) | 71.5% | 69.2% | 78.7% | 77.9% [75.2%-79.1%] | -- | 72.0% | 72.0% | MARKETS_AGREE | SHADOW_BET | -2.3 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4144.0, B 3968.0; serve-point win A 60.5%, B 43.4%; Elo A 2110.7, B 1919.2; model uncertainty 0.0193
* Form inputs: days since last match A 4, B 0; matches on record A 856, B 538; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high +0.000, surface_dev_loose +0.011, surface_dev_tight -0.020
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT13SVISAM-21` Over 20.5 games: 0.53/0.54 mid 53.5%, model 65.6% (projection_v2.0 (prediction ledger)) -- gap +12.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT13SVISAM-26` Over 25.5 games: 0.28/0.33 mid 30.5%, model 42.4% (projection_v2.0 (prediction ledger)) -- gap +11.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT13SVISAM-2-SAM` Will Liudmila Samsonova win set 2 in the Elina Svitolina vs Liudmila Samsonova match: 0.30/0.34 mid 32.0%, model 36.9% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT13SVISAM-2-SVI` Will Elina Svitolina win set 2 in the Elina Svitolina vs Liudmila Samsonova match: 0.65/0.70 mid 67.5%, model 63.1% (projection_v2.0 (prediction ledger)) -- gap -4.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT13SVISAM-1-SAM` Will Liudmila Samsonova win set 1 in the Elina Svitolina vs Liudmila Samsonova match: 0.32/0.34 mid 33.0%, model 36.9% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT13SVISAM-16` Over 15.5 games: 0.91/0.96 mid 93.5%, model 97.0% (projection_v2.0 (prediction ledger)) -- gap +3.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT13SVISAM-1-SVI` Will Elina Svitolina win set 1 in the Elina Svitolina vs Liudmila Samsonova match: 0.65/0.66 mid 65.5%, model 63.1% (projection_v2.0 (prediction ledger)) -- gap -2.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE

## Chang / Rowley vs Li Xuan Leong / Soke -- W35 Redding CA R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 03:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T03:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13CHAROWLIXSOK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chang / Rowley (`KXITFWDOUBLES-26OCT13CHAROWLIXSOK-CHAROW`) | 0.05 / 0.95 (111) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Li Xuan Leong / Soke (`KXITFWDOUBLES-26OCT13CHAROWLIXSOK-LIXSOK`) | 0.05 / 0.95 (111) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Drugdova / Zucchini vs Cooling / Reed -- W35 Redding CA R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 03:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T03:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13DRUZUCCOOREE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cooling / Reed (`KXITFWDOUBLES-26OCT13DRUZUCCOOREE-COOREE`) | 0.05 / 0.95 (111) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Drugdova / Zucchini (`KXITFWDOUBLES-26OCT13DRUZUCCOOREE-DRUZUC`) | 0.05 / 0.95 (111) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Olmos / Nicole Singeorzan vs Rose / Taskovic -- W35 Redding CA R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 03:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T03:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13OLMNICROSTAS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Olmos / Nicole Singeorzan (`KXITFWDOUBLES-26OCT13OLMNICROSTAS-OLMNIC`) | 0.05 / 0.95 (111) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rose / Taskovic (`KXITFWDOUBLES-26OCT13OLMNICROSTAS-ROSTAS`) | 0.05 / 0.95 (111) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Botic Van de Zandschulp vs Rafael Jodar -- ATP Shanghai R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-14 07:00Z
* Current expected start: 2026-10-14 04:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-13 14:56Z
* Recommended handicap-by time: 2026-10-14 03:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (MASTERS_1000) · Hard · scheduled 2026-10-14T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:122298:212588:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rafael Jodar (`KXATPMATCH-26OCT14VANJOD-JOD`) | 0.63 / 0.64 (149) | 63.5% | 64.1% | 69.7% | 67.5% [65.5%-68.4%] | 63.9% | 62.9% | 63.4% | MODEL_LONE_OUTLIER | WATCH | +0.6 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Botic Van de Zandschulp (`KXATPMATCH-26OCT14VANJOD-VAN`) | 0.37 / 0.38 (119890) | 37.5% | 35.9% | 30.3% | 32.6% [31.6%-34.5%] | 36.1% | 36.1% | 36.1% | MODEL_LONE_OUTLIER | PASS | -1.6 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5134.0, B 4261.0; serve-point win A 58.7%, B 38.5%; Elo A 1908.1, B 1970.8; model uncertainty 0.0143
* Form inputs: days since last match A 1, B 1; matches on record A 617, B 114; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose +0.000, surface_dev_tight +0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT14VANJOD-28` Over 27.5 games: 0.24/0.32 mid 28.0%, model 35.8% (projection_v2.0 (prediction ledger)) -- gap +7.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT14VANJOD-23` Over 22.5 games: 0.48/0.50 mid 49.0%, model 56.3% (projection_v2.0 (prediction ledger)) -- gap +7.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT14VANJOD-JOD21` Will Rafael Jodar win the Botic Van de Zandschulp vs Rafael Jodar match by a set score of 2-1?: 0.21/0.24 mid 22.5%, model 28.7% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT14VANJOD-JOD20` Will Rafael Jodar win the Botic Van de Zandschulp vs Rafael Jodar match by a set score of 2-0?: 0.39/0.41 mid 40.0%, model 35.4% (projection_v2.0 (prediction ledger)) -- gap -4.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT14VANJOD-VAN20` Will Botic Van de Zandschulp win the Botic Van de Zandschulp vs Rafael Jodar match by a set score of 2-0?: 0.19/0.21 mid 20.0%, model 16.4% (projection_v2.0 (prediction ledger)) -- gap -3.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT14VANJOD-VAN21` Will Botic Van de Zandschulp win the Botic Van de Zandschulp vs Rafael Jodar match by a set score of 2-1?: 0.15/0.18 mid 16.5%, model 19.5% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT14VANJOD-18` Over 17.5 games: 0.85/0.88 mid 86.5%, model 89.5% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT14VANJOD-JOD6` Will Rafael Jodar win at least 5.5 more games than Botic Van de Zandschulp?: 0.20/0.23 mid 21.5%, model 18.6% (projection_v2.0 (prediction ledger)) -- gap -2.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT14VANJOD-JOD3` Will Rafael Jodar win at least 2.5 more games than Botic Van de Zandschulp?: 0.52/0.55 mid 53.5%, model 50.9% (projection_v2.0 (prediction ledger)) -- gap -2.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT14VANJOD-VAN2` Will Botic Van de Zandschulp win at least 1.5 more games than Rafael Jodar?: 0.29/0.32 mid 30.5%, model 29.5% (projection_v2.0 (prediction ledger)) -- gap -1.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT14VANJOD-1-VAN` Will Botic Van de Zandschulp win set 1 in the Botic Van de Zandschulp vs Rafael Jodar match: 0.38/0.41 mid 39.5%, model 40.5% (projection_v2.0 (prediction ledger)) -- gap +1.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT14VANJOD-2-VAN` Will Botic Van de Zandschulp win set 2 in the Botic Van de Zandschulp vs Rafael Jodar match: 0.38/0.41 mid 39.5%, model 40.5% (projection_v2.0 (prediction ledger)) -- gap +1.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT14VANJOD-1-JOD` Will Rafael Jodar win set 1 in the Botic Van de Zandschulp vs Rafael Jodar match: 0.59/0.61 mid 60.0%, model 59.5% (projection_v2.0 (prediction ledger)) -- gap -0.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT14VANJOD-2-JOD` Will Rafael Jodar win set 2 in the Botic Van de Zandschulp vs Rafael Jodar match: 0.58/0.62 mid 60.0%, model 59.5% (projection_v2.0 (prediction ledger)) -- gap -0.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Iva Jovic vs Dayana Yastremska -- WTA Wuhan R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-14 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-14 04:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-13 14:56Z
* Recommended handicap-by time: 2026-10-14 03:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-14T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215035:260300:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iva Jovic (`KXWTAMATCH-26OCT13JOVYAS-JOV`) | 0.80 / 0.81 (1014) | 80.5% | 78.8% | 80.4% | 78.1% [70.6%-80.3%] | -- | 77.4% | -- | INSUFFICIENT_INPUTS | PASS | -1.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dayana Yastremska (`KXWTAMATCH-26OCT13JOVYAS-YAS`) | 0.19 / 0.20 (1423) | 19.5% | 21.2% | 19.6% | 21.9% [19.7%-29.4%] | -- | 26.3% | -- | INSUFFICIENT_INPUTS | PASS | +1.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3602.0, B 4632.0; serve-point win A 60.4%, B 45.7%; Elo A 2009.6, B 1851.8; model uncertainty 0.0489
* Form inputs: days since last match A 6, B 0; matches on record A 168, B 478; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose +0.011, surface_dev_tight -0.020
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT13JOVYAS-1-YAS` Will Dayana Yastremska win set 1 in the Iva Jovic vs Dayana Yastremska match: 0.23/0.25 mid 24.0%, model 29.7% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT13JOVYAS-2-JOV` Will Iva Jovic win set 2 in the Iva Jovic vs Dayana Yastremska match: 0.74/0.78 mid 76.0%, model 70.3% (projection_v2.0 (prediction ledger)) -- gap -5.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT13JOVYAS-1-JOV` Will Iva Jovic win set 1 in the Iva Jovic vs Dayana Yastremska match: 0.74/0.77 mid 75.5%, model 70.3% (projection_v2.0 (prediction ledger)) -- gap -5.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT13JOVYAS-2-YAS` Will Dayana Yastremska win set 2 in the Iva Jovic vs Dayana Yastremska match: 0.22/0.27 mid 24.5%, model 29.7% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE

## Karolina Muchova vs Caty McNally -- WTA Wuhan R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-14 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-14 04:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-13 14:56Z
* Recommended handicap-by time: 2026-10-14 03:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-14T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214096:216083:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Caty McNally (`KXWTAMATCH-26OCT13MUCMCC-MCC`) | 0.19 / 0.21 (4028) | 20.0% | 24.0% | 19.9% | 19.2% [18.2%-21.3%] | -- | 20.4% | 20.4% | MODEL_LONE_OUTLIER | PASS | +4.0 pp | NORMAL | FRESH | B / LIMITED | ALL_AGREE | VERIFIED |
| Karolina Muchova (`KXWTAMATCH-26OCT13MUCMCC-MUC`) | 0.79 / 0.81 (32757) | 80.0% | 76.0% | 80.1% | 80.8% [78.7%-81.8%] | -- | 80.0% | 80.0% | MODEL_LONE_OUTLIER | PASS | -4.0 pp | NORMAL | FRESH | B / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3972.0, B 3757.0; serve-point win A 61.8%, B 43.7%; Elo A 2136.0, B 1869.3; model uncertainty 0.0154
* Form inputs: days since last match A 5, B 175; matches on record A 481, B 313; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.007, surface_dev_loose +0.010, surface_dev_tight -0.018
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT13MUCMCC-20` Over 19.5 games: 0.52/0.54 mid 53.0%, model 69.7% (projection_v2.0 (prediction ledger)) -- gap +16.7 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT13MUCMCC-25` Over 24.5 games: 0.22/0.33 mid 27.5%, model 43.7% (projection_v2.0 (prediction ledger)) -- gap +16.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT13MUCMCC-15` Over 14.5 games: 0.75/0.99 mid 87.0%, model 98.8% (projection_v2.0 (prediction ledger)) -- gap +11.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT13MUCMCC-2-MUC` Will Karolina Muchova win set 2 in the Karolina Muchova vs Catherine McNally match: 0.73/0.77 mid 75.0%, model 68.1% (projection_v2.0 (prediction ledger)) -- gap -6.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT13MUCMCC-1-MUC` Will Karolina Muchova win set 1 in the Karolina Muchova vs Catherine McNally match: 0.73/0.76 mid 74.5%, model 68.1% (projection_v2.0 (prediction ledger)) -- gap -6.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT13MUCMCC-2-MCC` Will Catherine McNally win set 2 in the Karolina Muchova vs Catherine McNally match: 0.23/0.28 mid 25.5%, model 31.9% (projection_v2.0 (prediction ledger)) -- gap +6.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT13MUCMCC-1-MCC` Will Catherine McNally win set 1 in the Karolina Muchova vs Catherine McNally match: 0.25/0.28 mid 26.5%, model 31.9% (projection_v2.0 (prediction ledger)) -- gap +5.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jasmine Paolini vs Nikola Bartunkova -- WTA Wuhan R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-14 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-14 04:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-13 14:56Z
* Recommended handicap-by time: 2026-10-14 03:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-14T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211148:223360:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikola Bartunkova (`KXWTAMATCH-26OCT13PAOBAR-BAR`) | 0.58 / 0.59 (6123) | 58.5% | 49.8% | 45.8% | 42.1% [36.5%-44.8%] | -- | 59.7% | 59.7% | MODEL_LONE_OUTLIER | PASS | -8.7 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Jasmine Paolini (`KXWTAMATCH-26OCT13PAOBAR-PAO`) | 0.40 / 0.41 (150) | 40.5% | 50.2% | 54.2% | 57.9% [55.2%-63.5%] | -- | 40.7% | 40.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +9.7 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4852.0, B 3248.0; serve-point win A 56.7%, B 43.3%; Elo A 2008.5, B 1905.3; model uncertainty 0.041
* Form inputs: days since last match A 1, B 0; matches on record A 709, B 250; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.010
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT13PAOBAR-21` Over 20.5 games: 0.55/0.57 mid 56.0%, model 68.2% (projection_v2.0 (prediction ledger)) -- gap +12.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT13PAOBAR-26` Over 25.5 games: 0.29/0.38 mid 33.5%, model 44.9% (projection_v2.0 (prediction ledger)) -- gap +11.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT13PAOBAR-1-PAO` Will Jasmine Paolini win set 1 in the Jasmine Paolini vs Nikola Bartunkova match: 0.41/0.45 mid 43.0%, model 50.1% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT13PAOBAR-2-BAR` Will Nikola Bartunkova win set 2 in the Jasmine Paolini vs Nikola Bartunkova match: 0.55/0.59 mid 57.0%, model 49.9% (projection_v2.0 (prediction ledger)) -- gap -7.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT13PAOBAR-2-PAO` Will Jasmine Paolini win set 2 in the Jasmine Paolini vs Nikola Bartunkova match: 0.41/0.45 mid 43.0%, model 50.1% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT13PAOBAR-1-BAR` Will Nikola Bartunkova win set 1 in the Jasmine Paolini vs Nikola Bartunkova match: 0.55/0.58 mid 56.5%, model 49.9% (projection_v2.0 (prediction ledger)) -- gap -6.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT13PAOBAR-16` Over 15.5 games: 0.90/0.97 mid 93.5%, model 97.4% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Yulia Putintseva vs Diana Shnaider -- WTA Wuhan R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-14 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-14 04:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-13 14:56Z
* Recommended handicap-by time: 2026-10-14 03:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-14T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:201709:223670:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yulia Putintseva (`KXWTAMATCH-26OCT13PUTSHN-PUT`) | 0.25 / 0.27 (23905) | 26.0% | 33.9% | 43.2% | 43.2% [38.0%-45.3%] | -- | 26.4% | 26.4% | MODEL_LONE_OUTLIER | WATCH | +7.9 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Diana Shnaider (`KXWTAMATCH-26OCT13PUTSHN-SHN`) | 0.74 / 0.75 (18369) | 74.5% | 66.1% | 56.8% | 56.8% [54.7%-62.0%] | -- | 73.6% | 73.6% | MODEL_LONE_OUTLIER | PASS | -8.4 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4366.0, B 4846.0; serve-point win A 55.0%, B 41.9%; Elo A 1898.2, B 1960.2; model uncertainty 0.0361
* Form inputs: days since last match A 0, B 0; matches on record A 855, B 317; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.021, surface_dev_loose -0.000, surface_dev_tight -0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT13PUTSHN-20` Over 19.5 games: 0.54/0.55 mid 54.5%, model 72.2% (projection_v2.0 (prediction ledger)) -- gap +17.6 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT13PUTSHN-25` Over 24.5 games: 0.26/0.34 mid 30.0%, model 46.9% (projection_v2.0 (prediction ledger)) -- gap +16.9 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT13PUTSHN-15` Over 14.5 games: 0.75/0.99 mid 87.0%, model 98.9% (projection_v2.0 (prediction ledger)) -- gap +11.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT13PUTSHN-1-PUT` Will Yulia Putintseva win set 1 in the Yulia Putintseva vs Diana Shnaider match: 0.28/0.31 mid 29.5%, model 39.1% (projection_v2.0 (prediction ledger)) -- gap +9.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT13PUTSHN-2-PUT` Will Yulia Putintseva win set 2 in the Yulia Putintseva vs Diana Shnaider match: 0.28/0.31 mid 29.5%, model 39.1% (projection_v2.0 (prediction ledger)) -- gap +9.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT13PUTSHN-2-SHN` Will Diana Shnaider win set 2 in the Yulia Putintseva vs Diana Shnaider match: 0.68/0.72 mid 70.0%, model 60.9% (projection_v2.0 (prediction ledger)) -- gap -9.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT13PUTSHN-1-SHN` Will Diana Shnaider win set 1 in the Yulia Putintseva vs Diana Shnaider match: 0.68/0.70 mid 69.0%, model 60.9% (projection_v2.0 (prediction ledger)) -- gap -8.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Maria Kozyreva / Peyton Stearns vs Shuko Aoyama / En-Shuo Liang -- WTA Wuhan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-14T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13KOZSTEAOYLIA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shuko Aoyama / En-Shuo Liang (`KXWTADOUBLES-26OCT13KOZSTEAOYLIA-AOYLIA`) | 0.73 / 0.74 (27) | 73.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maria Kozyreva / Peyton Stearns (`KXWTADOUBLES-26OCT13KOZSTEAOYLIA-KOZSTE`) | 0.26 / 0.27 (25) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Lilian Poling vs Cadence Brace -- W50 Quebec City R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221585:223335:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cadence Brace (`KXITFWMATCH-26OCT13POLBRA-BRA`) | 0.88 / 0.94 (94) | 91.0% | 96.0% | 95.3% | 92.2% [88.6%-94.6%] | -- | -- | -- | -- | PASS | +5.0 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lilian Poling (`KXITFWMATCH-26OCT13POLBRA-POL`) | 0.05 / 0.07 (3) | 6.0% | 4.0% | 4.7% | 7.8% [5.4%-11.4%] | -- | -- | -- | -- | PASS | -2.0 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1063.0, B 2165.0; serve-point win A 45.4%, B 41.5%; Elo A 1276.4, B 1646.4; model uncertainty 0.0301
* Form inputs: days since last match A 169, B 27; matches on record A 93, B 222; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.009, surface_dev_tight +0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Casper Ruud vs Felix Auger-Aliassime -- ATP Shanghai R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-14 07:00Z
* Current expected start: 2026-10-14 05:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-13 14:56Z
* Recommended handicap-by time: 2026-10-14 04:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-90_MIN

ATP (MASTERS_1000) · Hard · scheduled 2026-10-14T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:134770:200000:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felix Auger-Aliassime (`KXATPMATCH-26OCT14RUUAUG-AUG`) | 0.58 / 0.59 (71579) | 58.5% | 53.2% | 59.0% | 58.5% [53.3%-61.7%] | 58.3% | 57.7% | 58.0% | MODEL_LONE_OUTLIER | PASS | -5.3 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Casper Ruud (`KXATPMATCH-26OCT14RUUAUG-RUU`) | 0.41 / 0.42 (13442) | 41.5% | 46.8% | 41.0% | 41.5% [38.3%-46.7%] | 41.7% | 42.4% | 42.0% | MODEL_LONE_OUTLIER | PASS | +5.3 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4688.0, B 5694.0; serve-point win A 67.9%, B 31.4%; Elo A 1953.9, B 2005.6; model uncertainty 0.0419
* Form inputs: days since last match A 1, B 1; matches on record A 704, B 646; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.033, surface_pool_high -0.032, surface_dev_loose -0.013, surface_dev_tight +0.014
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT14RUUAUG-30` Over 29.5 games: 0.22/0.29 mid 25.5%, model 38.4% (projection_v2.0 (prediction ledger)) -- gap +12.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT14RUUAUG-20` Over 19.5 games: 0.72/0.78 mid 75.0%, model 87.5% (projection_v2.0 (prediction ledger)) -- gap +12.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT14RUUAUG-25` Over 24.5 games: 0.45/0.47 mid 46.0%, model 57.8% (projection_v2.0 (prediction ledger)) -- gap +11.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT14RUUAUG-AUG5` Will Felix Auger-Aliassime win at least 4.5 more games than Casper Ruud?: 0.20/0.21 mid 20.5%, model 12.6% (projection_v2.0 (prediction ledger)) -- gap -7.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT14RUUAUG-AUG20` Will Felix Auger-Aliassime win the Casper Ruud vs Felix Auger-Aliassime match by a set score of 2-0?: 0.34/0.36 mid 35.0%, model 27.2% (projection_v2.0 (prediction ledger)) -- gap -7.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT14RUUAUG-AUG2` Will Felix Auger-Aliassime win at least 1.5 more games than Casper Ruud?: 0.51/0.52 mid 51.5%, model 44.5% (projection_v2.0 (prediction ledger)) -- gap -7.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT14RUUAUG-RUU21` Will Casper Ruud win the Casper Ruud vs Felix Auger-Aliassime match by a set score of 2-1?: 0.16/0.20 mid 18.0%, model 23.9% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT14RUUAUG-2-RUU` Will Casper Ruud win set 2 in the Casper Ruud vs Felix Auger-Aliassime match: 0.41/0.45 mid 43.0%, model 47.9% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT14RUUAUG-2-AUG` Will Felix Auger-Aliassime win set 2 in the Casper Ruud vs Felix Auger-Aliassime match: 0.55/0.58 mid 56.5%, model 52.1% (projection_v2.0 (prediction ledger)) -- gap -4.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT14RUUAUG-RUU2` Will Casper Ruud win at least 1.5 more games than Felix Auger-Aliassime?: 0.33/0.36 mid 34.5%, model 38.3% (projection_v2.0 (prediction ledger)) -- gap +3.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT14RUUAUG-AUG21` Will Felix Auger-Aliassime win the Casper Ruud vs Felix Auger-Aliassime match by a set score of 2-1?: 0.20/0.25 mid 22.5%, model 26.0% (projection_v2.0 (prediction ledger)) -- gap +3.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT14RUUAUG-1-AUG` Will Felix Auger-Aliassime win set 1 in the Casper Ruud vs Felix Auger-Aliassime match: 0.54/0.57 mid 55.5%, model 52.1% (projection_v2.0 (prediction ledger)) -- gap -3.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT14RUUAUG-1-RUU` Will Casper Ruud win set 1 in the Casper Ruud vs Felix Auger-Aliassime match: 0.43/0.46 mid 44.5%, model 47.9% (projection_v2.0 (prediction ledger)) -- gap +3.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT14RUUAUG-RUU20` Will Casper Ruud win the Casper Ruud vs Felix Auger-Aliassime match by a set score of 2-0?: 0.22/0.24 mid 23.0%, model 22.9% (projection_v2.0 (prediction ledger)) -- gap -0.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jelena Ostapenko vs Jessica Pegula -- WTA Wuhan R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-14 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-14 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-13 14:56Z
* Recommended handicap-by time: 2026-10-14 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-14T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202468:211533:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jelena Ostapenko (`KXWTAMATCH-26OCT13OSTPEG-OST`) | 0.30 / 0.31 (150) | 30.5% | 18.2% | 8.6% | 10.1% [8.8%-16.1%] | -- | 30.9% | 30.9% | MODEL_LONE_OUTLIER | PASS | -12.3 pp | REVIEW | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Jessica Pegula (`KXWTAMATCH-26OCT13OSTPEG-PEG`) | 0.69 / 0.70 (20012) | 69.5% | 81.8% | 91.4% | 89.9% [83.9%-91.2%] | -- | 73.8% | -- | INSUFFICIENT_INPUTS | WATCH | +12.3 pp | REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3919.0, B 5824.0; serve-point win A 53.4%, B 39.7%; Elo A 1912.6, B 2210.1; model uncertainty 0.0367
* Form inputs: days since last match A 0, B 33; matches on record A 677, B 766; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.007, surface_dev_loose -0.007, surface_dev_tight +0.012
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTASETWINNER-26OCT13OSTPEG-1-PEG` Will Jessica Pegula win set 1 in the Jelena Ostapenko vs Jessica Pegula match: 0.63/0.64 mid 63.5%, model 72.8% (projection_v2.0 (prediction ledger)) -- gap +9.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT13OSTPEG-1-OST` Will Jelena Ostapenko win set 1 in the Jelena Ostapenko vs Jessica Pegula match: 0.34/0.38 mid 36.0%, model 27.3% (projection_v2.0 (prediction ledger)) -- gap -8.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT13OSTPEG-2-OST` Will Jelena Ostapenko win set 2 in the Jelena Ostapenko vs Jessica Pegula match: 0.32/0.35 mid 33.5%, model 27.3% (projection_v2.0 (prediction ledger)) -- gap -6.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT13OSTPEG-2-PEG` Will Jessica Pegula win set 2 in the Jelena Ostapenko vs Jessica Pegula match: 0.65/0.68 mid 66.5%, model 72.8% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26OCT13OSTPEG-26` Over 25.5 games: 0.26/0.31 mid 28.5%, model 34.6% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT13OSTPEG-21` Over 20.5 games: 0.52/0.54 mid 53.0%, model 56.6% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT13OSTPEG-16` Over 15.5 games: 0.89/0.96 mid 92.5%, model 94.2% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Janice Tjen vs Daria Snigur -- WTA Wuhan R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-14 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-14 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-13 14:56Z
* Recommended handicap-by time: 2026-10-14 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-14T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:220750:222145:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daria Snigur (`KXWTAMATCH-26OCT13TJESNI-SNI`) | 0.60 / 0.62 (7998) | 61.0% | 67.4% | 67.6% | 62.3% [58.3%-64.7%] | -- | -- | -- | -- | WATCH | +6.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Janice Tjen (`KXWTAMATCH-26OCT13TJESNI-TJE`) | 0.38 / 0.39 (363) | 38.5% | 32.6% | 32.4% | 37.7% [35.3%-41.7%] | -- | -- | -- | -- | PASS | -5.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3631.0, B 4190.0; serve-point win A 57.1%, B 39.4%; Elo A 1893.0, B 1901.0; model uncertainty 0.0322
* Form inputs: days since last match A 1, B 0; matches on record A 181, B 440; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.024, surface_dev_tight +0.025
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT13TJESNI-22` Over 21.5 games: 0.48/0.50 mid 49.0%, model 61.4% (projection_v2.0 (prediction ledger)) -- gap +12.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT13TJESNI-27` Over 26.5 games: 0.23/0.34 mid 28.5%, model 38.4% (projection_v2.0 (prediction ledger)) -- gap +9.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT13TJESNI-17` Over 16.5 games: 0.86/0.89 mid 87.5%, model 93.7% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT13TJESNI-1-SNI` Will Daria Snigur win set 1 in the Janice Tjen vs Daria Snigur match: 0.56/0.59 mid 57.5%, model 61.9% (projection_v2.0 (prediction ledger)) -- gap +4.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT13TJESNI-2-SNI` Will Daria Snigur win set 2 in the Janice Tjen vs Daria Snigur match: 0.56/0.60 mid 58.0%, model 61.9% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT13TJESNI-2-TJE` Will Janice Tjen win set 2 in the Janice Tjen vs Daria Snigur match: 0.40/0.44 mid 42.0%, model 38.1% (projection_v2.0 (prediction ledger)) -- gap -3.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT13TJESNI-1-TJE` Will Janice Tjen win set 1 in the Janice Tjen vs Daria Snigur match: 0.39/0.43 mid 41.0%, model 38.1% (projection_v2.0 (prediction ledger)) -- gap -2.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Katie Volynets vs Hanyu Guo -- WTA Wuhan R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-14 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-14 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-13 14:56Z
* Recommended handicap-by time: 2026-10-14 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-14T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215250:220465:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hanyu Guo (`KXWTAMATCH-26OCT13VOLGUO-GUO`) | 0.18 / 0.20 (30453) | 19.0% | 30.1% | 51.6% | 44.1% [30.1%-49.5%] | -- | 20.1% | 20.1% | MODEL_LONE_OUTLIER | WATCH | +11.1 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Katie Volynets (`KXWTAMATCH-26OCT13VOLGUO-VOL`) | 0.80 / 0.81 (2955) | 80.5% | 69.9% | 48.4% | 55.9% [50.5%-69.9%] | -- | 80.3% | 80.3% | MODEL_LONE_OUTLIER | PASS | -10.6 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5386.0, B 3015.0; serve-point win A 55.5%, B 48.4%; Elo A 1893.7, B 1749.5; model uncertainty 0.0968
* Form inputs: days since last match A 0, B 0; matches on record A 451, B 327; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.032, surface_pool_high -0.026, surface_dev_loose -0.011, surface_dev_tight +0.011
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 6 carry a model probability
  * `KXWTAGTOTAL-26OCT13VOLGUO-19` Over 18.5 games: 0.57/0.58 mid 57.5%, model 76.6% (projection_v2.0 (prediction ledger)) -- gap +19.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT13VOLGUO-24` Over 23.5 games: 0.24/0.34 mid 29.0%, model 47.3% (projection_v2.0 (prediction ledger)) -- gap +18.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT13VOLGUO-2-VOL` Will Katie Volynets win set 2 in the Katie Volynets vs Hanyu Guo match: 0.74/0.78 mid 76.0%, model 63.6% (projection_v2.0 (prediction ledger)) -- gap -12.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT13VOLGUO-2-GUO` Will Hanyu Guo win set 2 in the Katie Volynets vs Hanyu Guo match: 0.22/0.27 mid 24.5%, model 36.4% (projection_v2.0 (prediction ledger)) -- gap +11.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT13VOLGUO-1-GUO` Will Hanyu Guo win set 1 in the Katie Volynets vs Hanyu Guo match: 0.25/0.26 mid 25.5%, model 36.4% (projection_v2.0 (prediction ledger)) -- gap +10.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT13VOLGUO-1-VOL` Will Katie Volynets win set 1 in the Katie Volynets vs Hanyu Guo match: 0.74/0.75 mid 74.5%, model 63.6% (projection_v2.0 (prediction ledger)) -- gap -10.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Su-Wei Hsieh / Jelena Ostapenko vs Sofia Kenin / Irina Khromacheva -- WTA Wuhan R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-14 14:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-14 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-13 14:56Z
* Recommended handicap-by time: 2026-10-14 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-14T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT14HSIOSTKENKHR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Su-Wei Hsieh / Jelena Ostapenko (`KXWTADOUBLES-26OCT14HSIOSTKENKHR-HSIOST`) | 0.74 / 0.78 (6) | 76.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sofia Kenin / Irina Khromacheva (`KXWTADOUBLES-26OCT14HSIOSTKENKHR-KENKHR`) | 0.21 / 0.24 (54) | 22.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Han Shi vs Leylah Fernandez -- WTA Wuhan R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-14 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

WTA (MASTERS_1000) · Hard · scheduled 2026-10-14T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:220367:222559:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leylah Fernandez (`KXWTAMATCH-26OCT13SHIFER-FER`) | 0.76 / 0.77 (25653) | 76.5% | 85.7% | 64.4% | 74.1% [70.1%-82.9%] | 74.5% | -- | 74.5% | ALL_THREE_DISAGREE | PASS | +9.2 pp | NORMAL | FRESH | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Han Shi (`KXWTAMATCH-26OCT13SHIFER-SHI`) | 0.23 / 0.25 (42230) | 24.0% | 14.3% | 35.6% | 25.9% [17.1%-29.9%] | 25.5% | -- | 25.5% | ALL_THREE_DISAGREE | PASS | -9.7 pp | NORMAL | FRESH | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3226.0, B 4828.0; serve-point win A 52.8%, B 39.2%; Elo A 1600.6, B 1966.3; model uncertainty 0.064
* Form inputs: days since last match A 169, B 1; matches on record A 228, B 399; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.009, surface_dev_loose +0.013, surface_dev_tight -0.009
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT13SHIFER-15` Over 14.5 games: 0.75/0.99 mid 87.0%, model 97.2% (projection_v2.0 (prediction ledger)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT13SHIFER-20` Over 19.5 games: 0.53/0.54 mid 53.5%, model 59.8% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT13SHIFER-1-FER` Will Leylah Annie Fernandez win set 1 in the Han Shi vs Leylah Annie Fernandez match: 0.69/0.72 mid 70.5%, model 76.1% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT13SHIFER-2-FER` Will Leylah Annie Fernandez win set 2 in the Han Shi vs Leylah Annie Fernandez match: 0.69/0.72 mid 70.5%, model 76.1% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT13SHIFER-2-SHI` Will Han Shi win set 2 in the Han Shi vs Leylah Annie Fernandez match: 0.28/0.31 mid 29.5%, model 23.8% (projection_v2.0 (prediction ledger)) -- gap -5.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT13SHIFER-1-SHI` Will Han Shi win set 1 in the Han Shi vs Leylah Annie Fernandez match: 0.28/0.29 mid 28.5%, model 23.8% (projection_v2.0 (prediction ledger)) -- gap -4.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26OCT13SHIFER-25` Over 24.5 games: 0.26/0.37 mid 31.5%, model 35.1% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sara Errani / Jasmine Paolini vs Tereza Mihalikova / Olivia Nicholls -- WTA Wuhan R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-14 14:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-14 07:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-13 14:56Z
* Recommended handicap-by time: 2026-10-14 06:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-14T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT14ERRPAOMIHNIC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Errani / Jasmine Paolini (`KXWTADOUBLES-26OCT14ERRPAOMIHNIC-ERRPAO`) | 0.72 / 0.76 (2749) | 74.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tereza Mihalikova / Olivia Nicholls (`KXWTADOUBLES-26OCT14ERRPAOMIHNIC-MIHNIC`) | 0.24 / 0.28 (56) | 26.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Theo Arribage / Albano Olivetti vs Kevin Krawietz / Tim Putz -- ATP Shanghai QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-14T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT14ARROLIKRAPUT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theo Arribage / Albano Olivetti (`KXATPDOUBLES-26OCT14ARROLIKRAPUT-ARROLI`) | 0.38 / 0.44 (2325) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kevin Krawietz / Tim Putz (`KXATPDOUBLES-26OCT14ARROLIKRAPUT-KRAPUT`) | 0.56 / 0.61 (83) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Francisco Cabral / James Tracy vs Robert Galloway / Andre Goransson -- ATP Shanghai QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-14T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT14CABTRAGALGOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francisco Cabral / James Tracy (`KXATPDOUBLES-26OCT14CABTRAGALGOR-CABTRA`) | 0.49 / 0.53 (323) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Robert Galloway / Andre Goransson (`KXATPDOUBLES-26OCT14CABTRAGALGOR-GALGOR`) | 0.47 / 0.49 (201) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Christian Harrison / Neal Skupski vs Jakob Schnaitter / Mark Wallner -- ATP Shanghai QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-13 14:56Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-15T04:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-14T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT14HARSKUSCHWAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Christian Harrison / Neal Skupski (`KXATPDOUBLES-26OCT14HARSKUSCHWAL-HARSKU`) | 0.72 / 0.77 (407) | 74.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jakob Schnaitter / Mark Wallner (`KXATPDOUBLES-26OCT14HARSKUSCHWAL-SCHWAL`) | 0.23 / 0.26 (150) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Yanan Hou vs Ekaterina Kuznetsova -- W15 Shenzhen R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206708:261066:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yanan Hou (`KXITFWMATCH-26OCT13HOUKUZ-HOU`) | 0.64 / 0.76 (5433) | 70.0% | 80.3% | 69.5% | 65.6% [63.1%-69.5%] | -- | -- | -- | -- | PASS | +10.3 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ekaterina Kuznetsova (`KXITFWMATCH-26OCT13HOUKUZ-KUZ`) | 0.24 / 0.29 (63) | 26.5% | 19.7% | 30.5% | 34.4% [30.5%-36.9%] | -- | -- | -- | -- | WATCH | -6.8 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 995.0, B 494.0; serve-point win A 55.1%, B 51.3%; Elo A 1360.3, B 1255.4; model uncertainty 0.032
* Form inputs: days since last match A 169, B 169; matches on record A 120, B 114; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Junlu Sun vs Jiangxue HAN -- W15 Shenzhen R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220497:264970:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jiangxue HAN (`KXITFWMATCH-26OCT13SUNHAN-HAN`) | 0.70 / 0.81 (106) | 75.5% | 85.0% | 42.5% | 71.4% [71.4%-71.4%] | -- | -- | -- | -- | PASS | +9.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Junlu Sun (`KXITFWMATCH-26OCT13SUNHAN-SUN`) | 0.15 / 0.21 (3) | 18.0% | 15.0% | 57.5% | 28.6% [28.6%-28.6%] | -- | -- | -- | -- | PASS | -3.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 1410.0; serve-point win A 46.8%, B 45.5%; Elo A 1304.4, B 1458.9; model uncertainty 0.0002
* Form inputs: days since last match A 757, B 169; matches on record A 15, B 174; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arina Varaksina vs Shiho Tsujioka -- W15 Shenzhen R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:255662:263801:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shiho Tsujioka (`KXITFWMATCH-26OCT13VARTSU-TSU`) | 0.50 / 0.65 (6319) | 57.5% | 73.5% | 79.4% | 69.0% [64.6%-74.1%] | -- | -- | -- | -- | PASS | +16.0 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Arina Varaksina (`KXITFWMATCH-26OCT13VARTSU-VAR`) | 0.35 / 0.46 (46) | 40.5% | 26.5% | 20.6% | 30.9% [25.9%-35.4%] | -- | -- | -- | -- | PASS | -14.0 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 586.0, B 1131.0; serve-point win A 48.7%, B 46.7%; Elo A 1277.4, B 1384.6; model uncertainty 0.0471
* Form inputs: days since last match A 176, B 176; matches on record A 27, B 42; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT13VARTSU-TSU  (YES = Shiho Tsujioka)
Model: 73%
Kalshi: 57%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.009, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ziyan Zhang vs Xiran Lan -- W15 Shenzhen R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-14T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13ZHALAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xiran Lan (`KXITFWMATCH-26OCT13ZHALAN-LAN`) | 0.77 / 0.86 (5366) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ziyan Zhang (`KXITFWMATCH-26OCT13ZHALAN-ZHA`) | 0.14 / 0.18 (5134) | 16.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ashlyn Krueger vs Lanlana Tararudee -- WTA Wuhan R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-14 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-14 07:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-13 14:56Z
* Recommended handicap-by time: 2026-10-14 06:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-14T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:221909:222290:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ashlyn Krueger (`KXWTAMATCH-26OCT13KRUTAR-KRU`) | 0.52 / 0.54 (7331) | 53.0% | 45.2% | 20.6% | 27.5% [23.3%-41.7%] | -- | 52.8% | -- | INSUFFICIENT_INPUTS | PASS | -7.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lanlana Tararudee (`KXWTAMATCH-26OCT13KRUTAR-TAR`) | 0.46 / 0.48 (8759) | 47.0% | 54.8% | 79.4% | 72.5% [58.3%-76.7%] | -- | 47.0% | -- | INSUFFICIENT_INPUTS | WATCH | +7.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4211.0, B 4262.0; serve-point win A 58.4%, B 40.7%; Elo A 1883.7, B 1873.1; model uncertainty 0.0919
* Form inputs: days since last match A 0, B 1; matches on record A 339, B 294; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose -0.013, surface_dev_tight +0.017
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 4 carry a model probability
  * `KXWTASETWINNER-26OCT13KRUTAR-2-KRU` Will Ashlyn Krueger win set 2 in the Ashlyn Krueger vs Lanlana Tararudee match: 0.51/0.55 mid 53.0%, model 46.8% (projection_v2.0 (prediction ledger)) -- gap -6.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT13KRUTAR-1-TAR` Will Lanlana Tararudee win set 1 in the Ashlyn Krueger vs Lanlana Tararudee match: 0.45/0.50 mid 47.5%, model 53.2% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT13KRUTAR-2-TAR` Will Lanlana Tararudee win set 2 in the Ashlyn Krueger vs Lanlana Tararudee match: 0.45/0.50 mid 47.5%, model 53.2% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT13KRUTAR-1-KRU` Will Ashlyn Krueger win set 1 in the Ashlyn Krueger vs Lanlana Tararudee match: 0.51/0.53 mid 52.0%, model 46.8% (projection_v2.0 (prediction ledger)) -- gap -5.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sergey Fomin vs Dominik Palan -- M25 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200672:208158:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sergey Fomin (`KXITFMATCH-26OCT13FOMPAL-FOM`) | 0.63 / 0.65 (21) | 64.0% | 63.0% | 55.5% | 57.9% [54.0%-63.2%] | 63.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.0 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dominik Palan (`KXITFMATCH-26OCT13FOMPAL-PAL`) | 0.34 / 0.36 (6346) | 35.0% | 37.0% | 44.5% | 42.1% [36.8%-46.0%] | 36.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +2.0 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1667.0, B 1229.0; serve-point win A 65.5%, B 37.2%; Elo A 1412.1, B 1342.5; model uncertainty 0.0464
* Form inputs: days since last match A 29, B 29; matches on record A 322, B 283; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.038, surface_pool_high -0.039, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zichen Shao vs Anton Shepp -- M25 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-14T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13SHASHE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zichen Shao (`KXITFMATCH-26OCT13SHASHE-SHA`) | 0.08 / 0.09 (27) | 8.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anton Shepp (`KXITFMATCH-26OCT13SHASHE-SHE`) | 0.90 / 0.91 (6364) | 90.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kristjan Tamm vs Xing Dao Chen -- M25 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144932:212263:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xing Dao Chen (`KXITFMATCH-26OCT13TAMCHE-CHE`) | 0.23 / 0.27 (19) | 25.0% | 25.4% | 39.1% | 32.6% [32.1%-33.4%] | 28.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kristjan Tamm (`KXITFMATCH-26OCT13TAMCHE-TAM`) | 0.74 / 0.75 (337) | 74.5% | 74.6% | 60.9% | 67.4% [66.6%-67.8%] | 72.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 541.0, B 90.0; serve-point win A 66.0%, B 39.3%; Elo A 1326.9, B 1199.6; model uncertainty 0.0064
* Form inputs: days since last match A 25, B 666; matches on record A 229, B 21; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tiana Tian Deng vs Adithya Karunaratne -- W15 Shenzhen R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220453:260528:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tiana Tian Deng (`KXITFWMATCH-26OCT13DENKAR-DEN`) | 0.25 / 0.39 (42) | 32.0% | 13.8% | 6.6% | 13.6% [10.4%-17.3%] | -- | -- | -- | -- | PASS | -18.2 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Adithya Karunaratne (`KXITFWMATCH-26OCT13DENKAR-KAR`) | 0.57 / 0.69 (114) | 63.0% | 86.2% | 93.4% | 86.5% [82.7%-89.6%] | -- | -- | -- | -- | PASS | +23.2 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 853.0, B 1765.0; serve-point win A 51.3%, B 40.4%; Elo A 1288.7, B 1537.1; model uncertainty 0.0343
* Form inputs: days since last match A 99, B 176; matches on record A 41, B 300; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT13DENKAR-KAR  (YES = Adithya Karunaratne)
Model: 86%
Kalshi: 63%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.015, surface_dev_loose -0.011, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hong Yi Cody Wong vs Yuyao Li -- W15 Shenzhen R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216587:264986:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuyao Li (`KXITFWMATCH-26OCT13WONLIX-LIX`) | 0.08 / 0.12 (14) | 10.0% | 10.2% | 23.5% | 18.6% [17.6%-20.0%] | -- | -- | -- | -- | PASS | +0.2 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hong Yi Cody Wong (`KXITFWMATCH-26OCT13WONLIX-WON`) | 0.82 / 0.92 (6675) | 87.0% | 89.8% | 76.5% | 81.4% [80.0%-82.4%] | -- | -- | -- | -- | PASS | +2.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1599.0, B 606.0; serve-point win A 62.4%, B 47.3%; Elo A 1531.8, B 1258.4; model uncertainty 0.0119
* Form inputs: days since last match A 51, B 169; matches on record A 280, B 19; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.007, surface_dev_loose +0.006, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sarah Ye vs Ke Ren -- W15 Shenzhen R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260621:270205:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ke Ren (`KXITFWMATCH-26OCT13YEXREN-REN`) | 0.45 / 0.56 (5305) | 50.5% | 45.8% | 35.9% | 45.2% [43.1%-47.9%] | -- | -- | -- | -- | PASS | -4.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sarah Ye (`KXITFWMATCH-26OCT13YEXREN-YEX`) | 0.38 / 0.49 (49) | 43.5% | 54.2% | 64.1% | 54.8% [52.1%-56.9%] | -- | -- | -- | -- | PASS | +10.7 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 443.0, B 366.0; serve-point win A 54.5%, B 46.2%; Elo A 1269.8, B 1253.1; model uncertainty 0.0238
* Form inputs: days since last match A 169, B 169; matches on record A 7, B 72; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.011, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## jiale Zhang vs Honori Koyama -- W15 Shenzhen R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260742:260795:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Honori Koyama (`KXITFWMATCH-26OCT13ZHAKOY-KOY`) | 0.85 / 0.94 (446) | 89.5% | 73.7% | 26.5% | 66.6% [65.6%-66.6%] | -- | -- | -- | -- | PASS | -15.8 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| jiale Zhang (`KXITFWMATCH-26OCT13ZHAKOY-ZHA`) | 0.06 / 0.10 (13) | 8.0% | 26.3% | 73.6% | 33.4% [33.4%-34.4%] | -- | -- | -- | -- | PASS | +18.3 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 626.0; serve-point win A 50.6%, B 44.6%; Elo A 1157.5, B 1273.9; model uncertainty 0.005
* Form inputs: days since last match A 729, B 225; matches on record A 68, B 66; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT13ZHAKOY-ZHA  (YES = jiale Zhang)
Model: 26%
Kalshi: 8%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anhelina Kalinina / Dayana Yastremska vs Anna Danilina / Shuai Zhang -- WTA Wuhan R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-14 14:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-14 09:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-13 14:56Z
* Recommended handicap-by time: 2026-10-14 08:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-14T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT14KALYASDANZHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Danilina / Shuai Zhang (`KXWTADOUBLES-26OCT14KALYASDANZHA-DANZHA`) | 0.65 / 0.81 (1) | 73.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anhelina Kalinina / Dayana Yastremska (`KXWTADOUBLES-26OCT14KALYASDANZHA-KALYAS`) | 0.18 / 0.36 (195) | 27.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Weiyi Kong vs Matthew Shearer -- M25 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-14T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13KONSHE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Weiyi Kong (`KXITFMATCH-26OCT13KONSHE-KON`) | 0.39 / 0.42 (29) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matthew Shearer (`KXITFMATCH-26OCT13KONSHE-SHE`) | 0.57 / 0.60 (39) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jamie Mackenzie vs Corban Crowther -- M25 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-14T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13MACCRO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Corban Crowther (`KXITFMATCH-26OCT13MACCRO-CRO`) | 0.07 / 0.15 (16) | 11.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jamie Mackenzie (`KXITFMATCH-26OCT13MACCRO-MAC`) | 0.69 / 0.88 (0) | 78.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anthony Susanto vs Kuan-Yi Lee -- M25 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:134120:200045:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kuan-Yi Lee (`KXITFMATCH-26OCT13SUSLEE-LEE`) | 0.88 / 0.91 (116) | 89.5% | 90.6% | 82.7% | 87.4% [86.9%-88.2%] | 86.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anthony Susanto (`KXITFMATCH-26OCT13SUSLEE-SUS`) | 0.10 / 0.14 (32) | 12.0% | 9.3% | 17.3% | 12.6% [11.8%-13.1%] | 13.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 102.0, B 312.0; serve-point win A 56.4%, B 33.2%; Elo A 1048.5, B 1386.5; model uncertainty 0.0066
* Form inputs: days since last match A 666, B 715; matches on record A 49, B 264; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Evan Zhu vs Egor Pleshivtsev -- M25 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200632:212574:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Egor Pleshivtsev (`KXITFMATCH-26OCT13ZHUPLE-PLE`) | 0.17 / 0.20 (200) | 18.5% | 24.1% | 73.1% | 28.6% [26.1%-30.4%] | 20.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Evan Zhu (`KXITFMATCH-26OCT13ZHUPLE-ZHU`) | 0.80 / 0.82 (49) | 81.0% | 75.9% | 26.9% | 71.4% [69.6%-73.9%] | 79.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1210.0, B 0.0; serve-point win A 63.9%, B 41.6%; Elo A 1355.9, B 1197.0; model uncertainty 0.0216
* Form inputs: days since last match A 14, B 666; matches on record A 347, B 4; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.026, surface_pool_high -0.018, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anchisa Chanta vs aoyi li -- W15 Shenzhen R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-14T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13CHALIX:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anchisa Chanta (`KXITFWMATCH-26OCT13CHALIX-CHA`) | 0.83 / 0.94 (5541) | 88.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| aoyi li (`KXITFWMATCH-26OCT13CHALIX-LIX`) | 0.03 / 0.11 (28) | 7.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Meng Yi Chen vs Sijia Wei -- W15 Shenzhen R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221096:221903:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Meng Yi Chen (`KXITFWMATCH-26OCT13CHEWEI-CHE`) | 0.05 / 0.12 (28) | 8.5% | 9.1% | 25.2% | 18.2% [16.2%-20.4%] | -- | -- | -- | -- | PASS | +0.6 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sijia Wei (`KXITFWMATCH-26OCT13CHEWEI-WEI`) | 0.82 / 0.90 (31) | 86.0% | 90.9% | 74.8% | 81.8% [79.6%-83.8%] | -- | -- | -- | -- | PASS | +4.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1394.0, B 2150.0; serve-point win A 49.0%, B 41.0%; Elo A 1382.4, B 1716.7; model uncertainty 0.0211
* Form inputs: days since last match A 218, B 8; matches on record A 162, B 308; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.007, surface_dev_loose -0.004, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yiming Dang vs Chengyiyi Yuan -- W15 Shenzhen R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215134:222330:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yiming Dang (`KXITFWMATCH-26OCT13DANYUA-DAN`) | 0.27 / 0.32 (6139) | 29.5% | 24.5% | 25.2% | 25.2% [24.3%-26.9%] | -- | -- | -- | -- | PASS | -5.0 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Chengyiyi Yuan (`KXITFWMATCH-26OCT13DANYUA-YUA`) | 0.67 / 0.72 (119) | 69.5% | 75.5% | 74.8% | 74.8% [73.1%-75.7%] | -- | -- | -- | -- | WATCH | +6.0 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1108.0, B 2947.0; serve-point win A 50.7%, B 44.1%; Elo A 1291.9, B 1478.6; model uncertainty 0.013
* Form inputs: days since last match A 15, B 16; matches on record A 90, B 239; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.013, surface_dev_loose -0.004, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexandra Malova vs Junhan Zhang -- W15 Shenzhen R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-14T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT13MALZHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandra Malova (`KXITFWMATCH-26OCT13MALZHA-MAL`) | 0.18 / 0.23 (90) | 20.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Junhan Zhang (`KXITFWMATCH-26OCT13MALZHA-ZHA`) | 0.72 / 0.81 (5208) | 76.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chirag Duhan vs Arnav Paparkar -- M25 Solapur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-14T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13DUHPAP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chirag Duhan (`KXITFMATCH-26OCT13DUHPAP-DUH`) | 0.32 / 0.46 (0) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arnav Paparkar (`KXITFMATCH-26OCT13DUHPAP-PAP`) | 0.41 / 0.58 (41) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Madhwin Kamath vs Udit Kamboj -- M25 Solapur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209979:213648:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Madhwin Kamath (`KXITFMATCH-26OCT13KAMKAM2-KAM`) | 0.20 / 0.66 (0) | 43.0% | 42.2% | 50.0% | 40.0% [38.0%-40.9%] | -- | -- | -- | -- | PASS | -0.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Udit Kamboj (`KXITFMATCH-26OCT13KAMKAM2-KAM2`) | 0.15 / 0.53 (0) | 34.0% | 57.8% | 50.0% | 60.0% [59.1%-62.0%] | -- | -- | -- | -- | PASS | +23.8 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 61.2%, B 37.2%; Elo A 1202.3, B 1275.1; model uncertainty 0.0147
* Form inputs: days since last match A 876, B 701; matches on record A 32, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT13KAMKAM2-KAM2  (YES = Udit Kamboj)
Model: 58%
Kalshi: 34%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aziz Ouakaa vs Adhithya Ganesan -- M25 Solapur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200297:212258:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adhithya Ganesan (`KXITFMATCH-26OCT13OUAGAN-GAN`) | 0.42 / 0.47 (16) | 44.5% | 68.4% | 80.7% | 64.1% [62.1%-68.0%] | -- | -- | -- | -- | PASS | +23.9 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aziz Ouakaa (`KXITFMATCH-26OCT13OUAGAN-OUA`) | 0.49 / 0.53 (0) | 51.0% | 31.6% | 19.3% | 35.9% [32.0%-37.9%] | -- | -- | -- | -- | PASS | -19.4 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 655.0, B 50.0; serve-point win A 58.1%, B 38.2%; Elo A 1286.5, B 1387.2; model uncertainty 0.0294
* Form inputs: days since last match A 64, B 673; matches on record A 356, B 46; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT13OUAGAN-GAN  (YES = Adhithya Ganesan)
Model: 68%
Kalshi: 44%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.029, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniil Medvedev vs Stefanos Tsitsipas -- ATP Shanghai R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-14 07:00Z
* Current expected start: 2026-10-14 10:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-13 14:56Z
* Recommended handicap-by time: 2026-10-14 09:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+180_MIN

ATP (MASTERS_1000) · Hard · scheduled 2026-10-14T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:106421:126774:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniil Medvedev (`KXATPMATCH-26OCT14MEDTSI-MED`) | 0.68 / 0.69 (2099) | 68.5% | 69.9% | 74.3% | 73.1% [69.0%-75.1%] | 66.9% | -- | 66.9% | MODEL_LONE_OUTLIER | WATCH | +1.4 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Stefanos Tsitsipas (`KXATPMATCH-26OCT14MEDTSI-TSI`) | 0.30 / 0.32 (20753) | 31.0% | 30.1% | 25.7% | 26.9% [24.9%-31.1%] | 33.1% | -- | 33.1% | MODEL_LONE_OUTLIER | PASS | -0.9 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5727.0, B 5084.0; serve-point win A 67.3%, B 37.0%; Elo A 2099.7, B 1955.9; model uncertainty 0.0308
* Form inputs: days since last match A 1, B 1; matches on record A 855, B 800; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.017, surface_pool_high +0.020, surface_dev_loose +0.012, surface_dev_tight -0.008
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT14MEDTSI-24` Over 23.5 games: 0.44/0.45 mid 44.5%, model 51.8% (projection_v2.0 (prediction ledger)) -- gap +7.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT14MEDTSI-29` Over 28.5 games: 0.24/0.31 mid 27.5%, model 34.7% (projection_v2.0 (prediction ledger)) -- gap +7.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT14MEDTSI-MED21` Will Daniil Medvedev win the Daniil Medvedev vs Stefanos Tsitsipas match by a set score of 2-1?: 0.22/0.26 mid 24.0%, model 29.4% (projection_v2.0 (prediction ledger)) -- gap +5.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT14MEDTSI-MED6` Will Daniil Medvedev win at least 5.5 more games than Stefanos Tsitsipas?: 0.17/0.20 mid 18.5%, model 15.1% (projection_v2.0 (prediction ledger)) -- gap -3.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT14MEDTSI-TSI20` Will Stefanos Tsitsipas win the Daniil Medvedev vs Stefanos Tsitsipas match by a set score of 2-0?: 0.16/0.17 mid 16.5%, model 13.2% (projection_v2.0 (prediction ledger)) -- gap -3.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT14MEDTSI-MED20` Will Daniil Medvedev win the Daniil Medvedev vs Stefanos Tsitsipas match by a set score of 2-0?: 0.42/0.45 mid 43.5%, model 40.5% (projection_v2.0 (prediction ledger)) -- gap -3.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT14MEDTSI-TSI2` Will Stefanos Tsitsipas win at least 1.5 more games than Daniil Medvedev?: 0.25/0.28 mid 26.5%, model 23.6% (projection_v2.0 (prediction ledger)) -- gap -2.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT14MEDTSI-19` Over 18.5 games: 0.84/0.87 mid 85.5%, model 87.6% (projection_v2.0 (prediction ledger)) -- gap +2.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT14MEDTSI-TSI21` Will Stefanos Tsitsipas win the Daniil Medvedev vs Stefanos Tsitsipas match by a set score of 2-1?: 0.13/0.17 mid 15.0%, model 16.9% (projection_v2.0 (prediction ledger)) -- gap +1.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT14MEDTSI-1-MED` Will Daniil Medvedev win set 1 in the Daniil Medvedev vs Stefanos Tsitsipas match: 0.62/0.64 mid 63.0%, model 63.6% (projection_v2.0 (prediction ledger)) -- gap +0.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT14MEDTSI-MED3` Will Daniil Medvedev win at least 2.5 more games than Stefanos Tsitsipas?: 0.53/0.55 mid 54.0%, model 54.4% (projection_v2.0 (prediction ledger)) -- gap +0.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT14MEDTSI-2-MED` Will Daniil Medvedev win set 2 in the Daniil Medvedev vs Stefanos Tsitsipas match: 0.62/0.66 mid 64.0%, model 63.6% (projection_v2.0 (prediction ledger)) -- gap -0.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT14MEDTSI-2-TSI` Will Stefanos Tsitsipas win set 2 in the Daniil Medvedev vs Stefanos Tsitsipas match: 0.34/0.38 mid 36.0%, model 36.4% (projection_v2.0 (prediction ledger)) -- gap +0.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT14MEDTSI-1-TSI` Will Stefanos Tsitsipas win set 1 in the Daniil Medvedev vs Stefanos Tsitsipas match: 0.35/0.38 mid 36.5%, model 36.4% (projection_v2.0 (prediction ledger)) -- gap -0.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## S D Prajwal Dev vs Noah Schachter -- M25 Solapur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 10:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:133794:208132:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S D Prajwal Dev (`KXITFMATCH-26OCT14DEVSCH-DEV`) | 0.53 / 0.67 (0) | 60.0% | 51.9% | 29.4% | 51.5% [44.9%-57.1%] | -- | -- | -- | -- | PASS | -8.1 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Noah Schachter (`KXITFMATCH-26OCT14DEVSCH-SCH`) | 0.24 / 0.36 (40) | 30.0% | 48.0% | 70.6% | 48.5% [42.9%-55.1%] | -- | -- | -- | -- | PASS | +18.1 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 360.0, B 489.0; serve-point win A 60.6%, B 39.8%; Elo A 1330.7, B 1279.2; model uncertainty 0.0612
* Form inputs: days since last match A 99, B 246; matches on record A 252, B 123; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT14DEVSCH-SCH  (YES = Noah Schachter)
Model: 48%
Kalshi: 30%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Grigoriy Lomakin vs Sidharth Rawat -- M25 Solapur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 10:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106168:200441:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Grigoriy Lomakin (`KXITFMATCH-26OCT14LOMRAW-LOM`) | 0.08 / 0.19 (2) | 13.5% | 34.0% | 52.1% | 32.1% [28.5%-35.3%] | -- | -- | -- | -- | PASS | +20.5 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sidharth Rawat (`KXITFMATCH-26OCT14LOMRAW-RAW`) | 0.69 / 0.81 (0) | 75.0% | 66.0% | 47.9% | 67.9% [64.7%-71.5%] | -- | -- | -- | -- | PASS | -9.0 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 328.0, B 530.0; serve-point win A 58.4%, B 38.4%; Elo A 1175.6, B 1340.0; model uncertainty 0.0339
* Form inputs: days since last match A 29, B 36; matches on record A 268, B 523; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT14LOMRAW-LOM  (YES = Grigoriy Lomakin)
Model: 34%
Kalshi: 14%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.018, surface_pool_high +0.014, surface_dev_loose -0.001, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Caheer Warik vs Pawit Sornlaksup -- M25 Solapur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 10:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210687:212890:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pawit Sornlaksup (`KXITFMATCH-26OCT14WARSOR-SOR`) | 0.84 / 0.90 (0) | 87.0% | 68.7% | 32.3% | 64.9% [63.9%-65.0%] | -- | -- | -- | -- | PASS | -18.3 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Caheer Warik (`KXITFMATCH-26OCT14WARSOR-WAR`) | 0.07 / 0.12 (54) | 9.5% | 31.3% | 67.7% | 35.1% [35.0%-36.1%] | -- | -- | -- | -- | PASS | +21.8 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 52.0; serve-point win A 59.5%, B 36.7%; Elo A 1247.1, B 1351.8; model uncertainty 0.0054
* Form inputs: days since last match A 785, B 281; matches on record A 3, B 39; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT14WARSOR-WAR  (YES = Caheer Warik)
Model: 31%
Kalshi: 10%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aryna Sabalenka vs Ann Li -- WTA Wuhan R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-14 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-14 11:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-13 14:56Z
* Recommended handicap-by time: 2026-10-14 10:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-14T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214544:215983:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ann Li (`KXWTAMATCH-26OCT13SABANN-ANN`) | 0.15 / 0.16 (383) | 15.5% | 10.7% | 8.3% | 8.5% [8.0%-9.4%] | -- | -- | -- | -- | PASS | -4.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aryna Sabalenka (`KXWTAMATCH-26OCT13SABANN-SAB`) | 0.84 / 0.85 (24852) | 84.5% | 89.3% | 91.7% | 91.5% [90.6%-92.0%] | -- | -- | -- | -- | SHADOW_BET | +4.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5768.0, B 4567.0; serve-point win A 65.5%, B 44.1%; Elo A 2296.4, B 1894.5; model uncertainty 0.0073
* Form inputs: days since last match A 9, B 0; matches on record A 718, B 468; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.004, surface_dev_loose +0.001, surface_dev_tight -0.002
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT13SABANN-15` Over 14.5 games: 0.75/0.99 mid 87.0%, model 97.8% (projection_v2.0 (prediction ledger)) -- gap +10.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT13SABANN-20` Over 19.5 games: 0.50/0.52 mid 51.0%, model 59.0% (projection_v2.0 (prediction ledger)) -- gap +8.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT13SABANN-25` Over 24.5 games: 0.24/0.33 mid 28.5%, model 32.7% (projection_v2.0 (prediction ledger)) -- gap +4.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT13SABANN-1-ANN` Will Ann Li win set 1 in the Aryna Sabalenka vs Ann Li match: 0.20/0.24 mid 22.0%, model 20.3% (projection_v2.0 (prediction ledger)) -- gap -1.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT13SABANN-1-SAB` Will Aryna Sabalenka win set 1 in the Aryna Sabalenka vs Ann Li match: 0.76/0.80 mid 78.0%, model 79.7% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT13SABANN-2-ANN` Will Ann Li win set 2 in the Aryna Sabalenka vs Ann Li match: 0.20/0.24 mid 22.0%, model 20.3% (projection_v2.0 (prediction ledger)) -- gap -1.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT13SABANN-2-SAB` Will Aryna Sabalenka win set 2 in the Aryna Sabalenka vs Ann Li match: 0.76/0.80 mid 78.0%, model 79.7% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jordan Chiu vs Cruz Hewitt -- M25 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207780:213178:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jordan Chiu (`KXITFMATCH-26OCT14CHIHEW-CHI`) | 0.07 / 0.12 (22) | 9.5% | 3.6% | 46.9% | 6.8% [6.8%-7.0%] | 12.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Cruz Hewitt (`KXITFMATCH-26OCT14CHIHEW-HEW`) | 0.85 / 0.92 (0) | 88.5% | 96.4% | 53.0% | 93.2% [93.0%-93.2%] | 87.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 999.0; serve-point win A 54.7%, B 31.1%; Elo A 1011.4, B 1466.0; model uncertainty 0.0012
* Form inputs: days since last match A 673, B 8; matches on record A 22, B 30; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.003, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Timofei Derepasko vs Isaac Becroft -- M25 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208653:212157:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isaac Becroft (`KXITFMATCH-26OCT14DERBEC-BEC`) | 0.56 / 0.60 (42) | 58.0% | 65.1% | 54.5% | 64.9% [63.9%-67.6%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Timofei Derepasko (`KXITFMATCH-26OCT14DERBEC-DER`) | 0.40 / 0.43 (0) | 41.5% | 34.9% | 45.5% | 35.1% [32.4%-36.1%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 262.0, B 69.0; serve-point win A 60.5%, B 36.4%; Elo A 1241.9, B 1357.0; model uncertainty 0.0187
* Form inputs: days since last match A 29, B 645; matches on record A 12, B 70; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.009, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arthur Weber vs Yuta Kikuchi -- M25 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207186:209043:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuta Kikuchi (`KXITFMATCH-26OCT14WEBKIK-KIK`) | 0.18 / 0.22 (0) | 20.0% | 41.7% | 27.1% | 35.8% [32.0%-37.9%] | 24.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +21.7 pp | HIGH_REVIEW | FRESH | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Arthur Weber (`KXITFMATCH-26OCT14WEBKIK-WEB`) | 0.77 / 0.81 (283) | 79.0% | 58.3% | 72.9% | 64.2% [62.1%-68.0%] | 75.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -20.7 pp | HIGH_REVIEW | FRESH | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1097.0, B 130.0; serve-point win A 60.4%, B 41.2%; Elo A 1438.7, B 1341.5; model uncertainty 0.0295
* Form inputs: days since last match A 14, B 29; matches on record A 169, B 78; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT14WEBKIK-KIK  (YES = Yuta Kikuchi)
Model: 42%
Kalshi: 20%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.019, surface_dev_loose +0.010, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yaojie ZENG vs Xirui Han -- M25 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210483:212472:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xirui Han (`KXITFMATCH-26OCT14ZENHAN-HAN`) | 0.17 / 0.20 (4) | 18.5% | 44.6% | 69.6% | 54.0% [54.0%-55.0%] | 21.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +26.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Yaojie ZENG (`KXITFMATCH-26OCT14ZENHAN-ZEN`) | 0.79 / 0.83 (5983) | 81.0% | 55.4% | 30.4% | 46.0% [45.0%-46.0%] | 78.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -25.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 290.0, B 0.0; serve-point win A 64.3%, B 36.8%; Elo A 1228.3, B 1259.6; model uncertainty 0.005
* Form inputs: days since last match A 14, B 757; matches on record A 32, B 5; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT14ZENHAN-HAN  (YES = Xirui Han)
Model: 45%
Kalshi: 18%
Gap: +26 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tommy Paul vs Zizou Bergs -- ATP Shanghai R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-13 05:00Z
* Current expected start: 2026-10-14 11:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-13 14:56Z
* Recommended handicap-by time: 2026-10-14 10:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1830_MIN

ATP (MASTERS_1000) · Hard · scheduled 2026-10-13T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126205:200267:2026-10-13`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zizou Bergs (`KXATPMATCH-26OCT12PAUBER-BER`) | 0.34 / 0.35 (24114) | 34.5% | 29.3% | 26.2% | 25.4% [24.6%-25.8%] | -- | -- | -- | -- | PASS | -5.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tommy Paul (`KXATPMATCH-26OCT12PAUBER-PAU`) | 0.66 / 0.67 (69989) | 66.5% | 70.7% | 73.8% | 74.6% [74.2%-75.4%] | -- | -- | -- | -- | SHADOW_BET | +4.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5633.0, B 5362.0; serve-point win A 66.1%, B 38.2%; Elo A 2026.5, B 1814.0; model uncertainty 0.0059
* Form inputs: days since last match A 3, B 1; matches on record A 717, B 551; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high +0.000, surface_dev_loose +0.007, surface_dev_tight +0.001
* Derivatives listed: 6 (GAME_SPREAD, MATCH_WINNER, TOTAL_GAMES); 6 carry a model probability
  * `KXATPGTOTAL-26OCT12PAUBER-28` Over 27.5 games: 0.29/0.33 mid 31.0%, model 37.1% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT12PAUBER-23` Over 22.5 games: 0.50/0.52 mid 51.0%, model 56.8% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT12PAUBER-PAU6` Will Tommy Paul win at least 5.5 more games than Zizou Bergs?: 0.21/0.25 mid 23.0%, model 17.8% (projection_v2.0 (prediction ledger)) -- gap -5.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT12PAUBER-BER2` Will Zizou Bergs win at least 1.5 more games than Tommy Paul?: 0.26/0.28 mid 27.0%, model 22.6% (projection_v2.0 (prediction ledger)) -- gap -4.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT12PAUBER-18` Over 17.5 games: 0.86/0.89 mid 87.5%, model 91.7% (projection_v2.0 (prediction ledger)) -- gap +4.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT12PAUBER-PAU3` Will Tommy Paul win at least 2.5 more games than Zizou Bergs?: 0.55/0.56 mid 55.5%, model 56.7% (projection_v2.0 (prediction ledger)) -- gap +1.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Astrid Cirotte vs Julia Khramtsova -- W15 Islamabad R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:236980:263706:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Astrid Cirotte (`KXITFWMATCH-26OCT14CIRKHR-CIR`) | 0.78 / 0.97 (104) | 87.5% | 76.4% | 60.5% | 65.5% [64.5%-66.0%] | -- | -- | -- | -- | PASS | -11.1 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Julia Khramtsova (`KXITFWMATCH-26OCT14CIRKHR-KHR`) | 0.03 / 0.16 (29) | 9.5% | 23.6% | 39.5% | 34.5% [34.0%-35.5%] | -- | -- | -- | -- | PASS | +14.1 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2379.0, B 401.0; serve-point win A 57.7%, B 47.7%; Elo A 1366.7, B 1250.4; model uncertainty 0.0074
* Form inputs: days since last match A 183, B 351; matches on record A 227, B 31; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Manish Sureshkumar vs Samir Banerjee -- M25 Solapur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200176:209079:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Samir Banerjee (`KXITFMATCH-26OCT14SURBAN-BAN`) | 0.57 / 0.90 (0) | 73.5% | 77.3% | 72.9% | 70.7% [69.7%-72.6%] | -- | -- | -- | -- | PASS | +3.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Manish Sureshkumar (`KXITFMATCH-26OCT14SURBAN-SUR`) | 0.05 / 0.22 (33) | 13.5% | 22.7% | 27.1% | 29.3% [27.4%-30.3%] | -- | -- | -- | -- | PASS | +9.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 275.0, B 167.0; serve-point win A 56.6%, B 37.7%; Elo A 1309.1, B 1460.8; model uncertainty 0.0143
* Form inputs: days since last match A 148, B 701; matches on record A 291, B 74; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.004, surface_dev_loose -0.001, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dhakshineswar Suresh vs Dev Javia -- M25 Solapur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-14T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202290:209956:2026-10-14`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dev Javia (`KXITFMATCH-26OCT14SURJAV-JAV`) | 0.13 / 0.26 (34) | 19.5% | 14.9% | 32.4% | 17.5% [14.6%-22.1%] | -- | -- | -- | -- | PASS | -4.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dhakshineswar Suresh (`KXITFMATCH-26OCT14SURJAV-SUR`) | 0.64 / 0.87 (0) | 75.5% | 85.0% | 67.6% | 82.5% [77.9%-85.4%] | -- | -- | -- | -- | PASS | +9.6 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1239.0, B 110.0; serve-point win A 71.8%, B 36.8%; Elo A 1593.4, B 1317.3; model uncertainty 0.0378
* Form inputs: days since last match A 48, B 155; matches on record A 62, B 96; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.046, surface_pool_high +0.029, surface_dev_loose -0.001, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Noemi La Cagnina vs Cristiana Nicoleta Todoni -- W35 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-14T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT14LACTOD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Noemi La Cagnina (`KXITFWMATCH-26OCT14LACTOD-LAC`) | 0.03 / 0.97 (104) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cristiana Nicoleta Todoni (`KXITFWMATCH-26OCT14LACTOD-TOD`) | 0.03 / 0.95 (30) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Juliette Mazzoni vs Miriam Bianca Bulgaru -- W35 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-14T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT14MAZBUL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miriam Bianca Bulgaru (`KXITFWMATCH-26OCT14MAZBUL-BUL`) | 0.03 / 0.97 (104) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Juliette Mazzoni (`KXITFWMATCH-26OCT14MAZBUL-MAZ`) | 0.03 / 0.97 (82) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Emma Mazzoni vs Dunja Maric -- W35 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-14T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT14MAZMAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dunja Maric (`KXITFWMATCH-26OCT14MAZMAR-MAR`) | 0.03 / 0.97 (104) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Emma Mazzoni (`KXITFWMATCH-26OCT14MAZMAR-MAZ`) | 0.03 / 0.97 (82) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alisa Oktiabreva vs ofir manhard -- W35 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-14T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT14OKTMAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ofir manhard (`KXITFWMATCH-26OCT14OKTMAN-MAN`) | 0.03 / 0.97 (104) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alisa Oktiabreva (`KXITFWMATCH-26OCT14OKTMAN-OKT`) | 0.03 / 0.97 (82) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## An / Tian vs Sun / Sun -- W15 Shenzhen R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT14ANXTIASUNSUN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| An / Tian (`KXITFWDOUBLES-26OCT14ANXTIASUNSUN-ANXTIA`) | 0.06 / 0.95 (111) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sun / Sun (`KXITFWDOUBLES-26OCT14ANXTIASUNSUN-SUNSUN`) | 0.05 / 0.95 (111) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Zuzanna Bednarz vs Melissa Boyden -- W15 Chisinau R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-14T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT14BEDBOY:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zuzanna Bednarz (`KXITFWMATCH-26OCT14BEDBOY-BED`) | 0.72 / 0.97 (117) | 84.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Melissa Boyden (`KXITFWMATCH-26OCT14BEDBOY-BOY`) | 0.03 / 0.21 (31) | 12.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maria Charl vs Lamis Alhussein Abdel Aziz -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-14T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT14CHAALH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lamis Alhussein Abdel Aziz (`KXITFWMATCH-26OCT14CHAALH-ALH`) | 0.03 / 0.97 (104) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maria Charl (`KXITFWMATCH-26OCT14CHAALH-CHA`) | 0.03 / 0.95 (30) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ellie Daniels vs Karla Popovic -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-14T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT14DANPOP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ellie Daniels (`KXITFWMATCH-26OCT14DANPOP-DAN`) | 0.03 / 0.97 (104) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Karla Popovic (`KXITFWMATCH-26OCT14DANPOP-POP`) | 0.03 / 0.97 (82) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arina Gamretkaia vs Iana Semichina -- W15 Chisinau R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-14T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT14GAMSEM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arina Gamretkaia (`KXITFWMATCH-26OCT14GAMSEM-GAM`) | 0.49 / 0.78 (113) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Iana Semichina (`KXITFWMATCH-26OCT14GAMSEM-SEM`) | 0.06 / 0.44 (44) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mirjana Jovanovic vs Felitsata Dorofeeva-Rybas -- W15 Chisinau R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-14T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT14JOVDOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felitsata Dorofeeva-Rybas (`KXITFWMATCH-26OCT14JOVDOR-DOR`) | 0.03 / 0.95 (30) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mirjana Jovanovic (`KXITFWMATCH-26OCT14JOVDOR-JOV`) | 0.03 / 0.97 (82) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kalimullina / Varaksina vs Laam Lai / Ren -- W15 Shenzhen R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT14KALVARLAAREN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kalimullina / Varaksina (`KXITFWDOUBLES-26OCT14KALVARLAAREN-KALVAR`) | 0.08 / 0.51 (51) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Laam Lai / Ren (`KXITFWDOUBLES-26OCT14KALVARLAAREN-LAAREN`) | 0.42 / 0.74 (96) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Kuznetsova / Suvirdjonkova vs Nie / Zheng -- W15 Shenzhen R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT14KUZSUVNIEZHE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kuznetsova / Suvirdjonkova (`KXITFWDOUBLES-26OCT14KUZSUVNIEZHE-KUZSUV`) | 0.05 / 0.95 (111) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nie / Zheng (`KXITFWDOUBLES-26OCT14KUZSUVNIEZHE-NIEZHE`) | 0.05 / 0.95 (111) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Teodora Vlajic vs Yuliya Perapekhina -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-14T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT14VLAPER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuliya Perapekhina (`KXITFWMATCH-26OCT14VLAPER-PER`) | 0.03 / 0.97 (104) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Teodora Vlajic (`KXITFWMATCH-26OCT14VLAPER-VLA`) | 0.03 / 0.97 (82) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Radka Zelnickova vs Alisa Vasileva -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-14T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT14ZELVAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alisa Vasileva (`KXITFWMATCH-26OCT14ZELVAS-VAS`) | 0.03 / 0.97 (104) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Radka Zelnickova (`KXITFWMATCH-26OCT14ZELVAS-ZEL`) | 0.03 / 0.97 (82) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zhang / Zheng vs Yang / Zhou -- W15 Shenzhen R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-14T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT14ZHAZHEYANZHO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yang / Zhou (`KXITFWDOUBLES-26OCT14ZHAZHEYANZHO-YANZHO`) | 0.05 / 0.94 (100) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Zhang / Zheng (`KXITFWDOUBLES-26OCT14ZHAZHEYANZHO-ZHAZHE`) | 0.05 / 0.95 (111) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Gabriela Dabrowski / Luisa Stefani vs Ulrikke Eikeri / Quinn Gleason -- WTA Wuhan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-13 14:56Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-15T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-14T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT14DABSTEEIKGLE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriela Dabrowski / Luisa Stefani (`KXWTADOUBLES-26OCT14DABSTEEIKGLE-DABSTE`) | 0.83 / 0.87 (525) | 85.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ulrikke Eikeri / Quinn Gleason (`KXWTADOUBLES-26OCT14DABSTEEIKGLE-EIKGLE`) | 0.12 / 0.17 (525) | 14.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Hanyu Guo / Kristina Mladenovic vs Marie Bouzkova / Sara Sorribes Tormo -- WTA Wuhan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-14 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-13 14:56Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-15T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-14T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT14GUOMLABOUSOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marie Bouzkova / Sara Sorribes Tormo (`KXWTADOUBLES-26OCT14GUOMLABOUSOR-BOUSOR`) | 0.33 / 0.37 (350) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hanyu Guo / Kristina Mladenovic (`KXWTADOUBLES-26OCT14GUOMLABOUSOR-GUOMLA`) | 0.62 / 0.67 (225) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
