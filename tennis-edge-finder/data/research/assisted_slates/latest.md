# ASSISTED SLATE -- 2026-10-17T21:14Z (`SL-20261017T211445Z-7704a31b`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

211 open matches not seen started, 966 markets. Skipped: {}. Sources: shadow board 2026-10-17T21:08:02.451189+00:00, Model 4 2026-10-17T21:08:28.382356+00:00, Gen-1 ledger 2026-10-17T21:07:59.395984+00:00, external 2026-10-17T20:52:19.469963+00:00, capture 20261017T205051Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-10-18 02:30Z**
* Recommended RUN TENNIS time: **2026-10-18 01:45Z**
* Final price/status check time: **2026-10-18 02:20Z**
* Number of matches in window: 8 (Maya Joint vs Kayla Day, Taylah Preston vs Emerson Jones, Mary Stoiana vs Sayaka Ishii, Daria Snigur vs Katarzyna Kawa, Anastasia Zakharova vs Polina Kudermetova, Harriet Dart vs Aoi Ito ...)

* **32 main-tour match(es) have NO verified start status** (START_UNKNOWN): BET blocked until a live status check.

Slate built 2026-10-17T21:14Z. Refresh due by: 2026-10-18 01:45Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 81, "HIGH_REVIEW": 99, "NORMAL": 410, "REVIEW": 145, "UNPRICED": 231}; match winners: {"EXTREME": 66, "HIGH_REVIEW": 51, "NORMAL": 110, "REVIEW": 41, "UNPRICED": 154}; quote freshness at build: {"FRESH": 735}.

## Ioannis Xilas vs Luka Talan Lopatic -- M15 Heraklion SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 20:34Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-17T20:34:40Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209354:212589:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luka Talan Lopatic (`KXITFMATCH-26OCT17XILTAL-TAL`) | 0.26 / 0.36 (28) | 31.0% | 27.1% | 62.8% | 41.7% [37.7%-45.8%] | -- | -- | -- | -- | PASS | -3.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Ioannis Xilas (`KXITFMATCH-26OCT17XILTAL-XIL`) | 0.57 / 0.70 (10) | 63.5% | 72.9% | 37.2% | 58.3% [54.2%-62.3%] | -- | -- | -- | -- | PASS | +9.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 992.0, B 0.0; serve-point win A 61.1%, B 43.6%; Elo A 1344.3, B 1286.5; model uncertainty 0.0407
* Form inputs: days since last match A 96, B 1055; matches on record A 90, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.040, surface_pool_high -0.041, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gatica / Pereira vs Ayala / Romero -- W15 Maceio F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-17T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17GATPERAYAROM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ayala / Romero (`KXITFWDOUBLES-26OCT17GATPERAYAROM-AYAROM`) | 0.17 / 0.21 (93) | 19.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gatica / Pereira (`KXITFWDOUBLES-26OCT17GATPERAYAROM-GATPER`) | 0.78 / 0.79 (0) | 78.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Francisco Comesana vs Thiago Seyboth Wild -- ATP Challenger Santa Cruz 2 SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 23:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-17T23:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:205734:207681:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francisco Comesana (`KXATPCHALLENGERMATCH-26OCT17COMSEY-COM`) | 0.45 / 0.46 (7144) | 45.5% | 45.6% | 31.0% | 37.3% [34.1%-41.6%] | 40.1% | 39.7% | 39.9% | MODEL_LONE_OUTLIER | PASS | +0.1 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_OUTLIER | VERIFIED |
| Thiago Seyboth Wild (`KXATPCHALLENGERMATCH-26OCT17COMSEY-SEY`) | 0.54 / 0.55 (31045) | 54.5% | 54.4% | 69.0% | 62.7% [58.4%-65.9%] | 59.9% | 60.5% | 60.2% | MODEL_LONE_OUTLIER | PASS | -0.1 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_OUTLIER | VERIFIED |

* Serve evidence (points): A 4413.0, B 3996.0; serve-point win A 64.0%, B 35.1%; Elo A 1777.7, B 1742.2; model uncertainty 0.0375
* Form inputs: days since last match A 12, B 12; matches on record A 441, B 485; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.014, surface_dev_tight +0.024
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Lui Maxted vs Cosme Rolland de Ravel -- M25 Austin TX SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 00:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210747:tml:R0KE:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lui Maxted (`KXITFMATCH-26OCT17MAXROL-MAX`) | 0.40 / 0.41 (27041) | 40.5% | 37.2% | 47.5% | 35.2% [34.2%-35.2%] | -- | -- | -- | -- | PASS | -3.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Cosme Rolland de Ravel (`KXITFMATCH-26OCT17MAXROL-ROL`) | 0.59 / 0.60 (21787) | 59.5% | 62.8% | 52.5% | 64.8% [64.8%-65.8%] | -- | -- | -- | -- | PASS | +3.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 473.0; serve-point win A 61.1%, B 36.3%; Elo A 1353.4, B 1459.5; model uncertainty 0.005
* Form inputs: days since last match A 726, B 110; matches on record A 16, B 7; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Diego Hidalgo / Mariano Kestelboim vs Luis Guto Miguel / Eduardo Ribeiro -- ATP Challenger Santa Cruz 2 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-18T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT17HIDKESMIGRIB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diego Hidalgo / Mariano Kestelboim (`KXATPCHALLENGERDOUBLES-26OCT17HIDKESMIGRIB-HIDKES`) | 0.48 / 0.53 (2) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luis Guto Miguel / Eduardo Ribeiro (`KXATPCHALLENGERDOUBLES-26OCT17HIDKESMIGRIB-MIGRIB`) | 0.40 / 0.49 (131) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sebastian Gomez / Urrea vs Alvarado / Mbithi -- M15 Quito F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-18T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT17SEBURRALVMBI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alvarado / Mbithi (`KXITFDOUBLES-26OCT17SEBURRALVMBI-ALVMBI`) | 0.90 / 0.92 (61) | 91.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sebastian Gomez / Urrea (`KXITFDOUBLES-26OCT17SEBURRALVMBI-SEBURR`) | 0.09 / 0.11 (3033) | 10.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Lepchenko / Liutova vs Herrero Linana / Zamarripa -- W100 Edmond OK QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-18T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17LEPLIUHERZAM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Herrero Linana / Zamarripa (`KXITFWDOUBLES-26OCT17LEPLIUHERZAM-HERZAM`) | 0.69 / 0.79 (25) | 74.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lepchenko / Liutova (`KXITFWDOUBLES-26OCT17LEPLIUHERZAM-LEPLIU`) | 0.14 / 0.24 (32) | 19.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Alastair Gray vs Dominick Mosejczuk -- M25 Austin TX SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT17GRAMOS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alastair Gray (`KXITFMATCH-26OCT17GRAMOS-GRA`) | 0.65 / 0.67 (170) | 66.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dominick Mosejczuk (`KXITFMATCH-26OCT17GRAMOS-MOS`) | 0.33 / 0.37 (7) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sloane Stephens vs Julieta Pareja -- W100 Edmond OK SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:201585:264075:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julieta Pareja (`KXITFWMATCH-26OCT17STEPAR-PAR`) | 0.37 / 0.38 (18882) | 37.5% | 42.9% | 62.0% | 46.3% [31.1%-54.8%] | -- | -- | -- | -- | PASS | +5.4 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sloane Stephens (`KXITFWMATCH-26OCT17STEPAR-STE`) | 0.62 / 0.63 (22566) | 62.5% | 57.1% | 38.0% | 53.7% [45.2%-68.9%] | -- | -- | -- | -- | WATCH | -5.4 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2061.0, B 1273.0; serve-point win A 56.0%, B 45.3%; Elo A 1813.0, B 1696.0; model uncertainty 0.1182
* Form inputs: days since last match A 29, B 38; matches on record A 685, B 63; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.042, surface_pool_high -0.048, surface_dev_loose -0.016, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maya Joint vs Kayla Day -- WTA Osaka Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 04:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-18 02:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: 2026-10-18 01:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T04:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215037:233741:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kayla Day (`KXWTAMATCH-26OCT17JOIDAY-DAY`) | 0.43 / 0.45 (2353) | 44.0% | 47.9% | 74.1% | 64.4% [50.0%-68.7%] | 44.4% | 34.6% | -- | INSUFFICIENT_INPUTS | WATCH | +4.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maya Joint (`KXWTAMATCH-26OCT17JOIDAY-JOI`) | 0.55 / 0.57 (14231) | 56.0% | 52.0% | 25.9% | 35.6% [31.3%-50.0%] | 55.6% | 57.5% | -- | INSUFFICIENT_INPUTS | PASS | -4.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3855.0, B 3639.0; serve-point win A 57.0%, B 43.4%; Elo A 1824.8, B 1748.9; model uncertainty 0.0937
* Form inputs: days since last match A 0, B 0; matches on record A 237, B 478; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.024, surface_dev_tight +0.025
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT17JOIDAY-16` Over 15.5 games: 0.55/0.99 mid 77.0%, model 97.4% (projection_v2.0 (prediction ledger)) -- gap +20.4 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17JOIDAY-21` Over 20.5 games: 0.56/0.58 mid 57.0%, model 68.2% (projection_v2.0 (prediction ledger)) -- gap +11.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17JOIDAY-26` Over 25.5 games: 0.27/0.41 mid 34.0%, model 45.0% (projection_v2.0 (prediction ledger)) -- gap +11.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT17JOIDAY-1-DAY` Will Kayla Day win set 1 in the Maya Joint vs Kayla Day match: 0.43/0.45 mid 44.0%, model 48.6% (projection_v2.0 (prediction ledger)) -- gap +4.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17JOIDAY-1-JOI` Will Maya Joint win set 1 in the Maya Joint vs Kayla Day match: 0.54/0.57 mid 55.5%, model 51.4% (projection_v2.0 (prediction ledger)) -- gap -4.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17JOIDAY-2-DAY` Will Kayla Day win set 2 in the Maya Joint vs Kayla Day match: 0.43/0.47 mid 45.0%, model 48.6% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17JOIDAY-2-JOI` Will Maya Joint win set 2 in the Maya Joint vs Kayla Day match: 0.52/0.55 mid 53.5%, model 51.4% (projection_v2.0 (prediction ledger)) -- gap -2.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; WIDE_SPREAD

## Taylah Preston vs Emerson Jones -- WTA Osaka Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 04:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-18 02:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: 2026-10-18 01:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T04:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:223194:263644:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emerson Jones (`KXWTAMATCH-26OCT17PREJON-JON`) | 0.49 / 0.50 (492) | 49.5% | 44.3% | 35.0% | 38.5% [37.0%-43.2%] | 51.1% | 49.8% | 49.8% | MARKETS_AGREE | PASS | -5.2 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Taylah Preston (`KXWTAMATCH-26OCT17PREJON-PRE`) | 0.49 / 0.51 (13353) | 50.0% | 55.7% | 65.0% | 61.5% [56.8%-63.0%] | 48.9% | 50.3% | 50.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +5.7 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5098.0, B 3547.0; serve-point win A 56.5%, B 44.6%; Elo A 1818.4, B 1792.5; model uncertainty 0.0307
* Form inputs: days since last match A 0, B 0; matches on record A 265, B 149; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.010, surface_dev_tight -0.015
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT17PREJON-17` Over 16.5 games: 0.26/0.99 mid 62.5%, model 93.5% (projection_v2.0 (prediction ledger)) -- gap +31.0 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17PREJON-22` Over 21.5 games: 0.49/0.51 mid 50.0%, model 62.5% (projection_v2.0 (prediction ledger)) -- gap +12.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17PREJON-27` Over 26.5 games: 0.03/0.59 mid 31.0%, model 39.2% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT17PREJON-1-PRE` Will Taylah Preston win set 1 in the Taylah Preston vs Emerson Jones match: 0.47/0.50 mid 48.5%, model 53.8% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17PREJON-2-PRE` Will Taylah Preston win set 2 in the Taylah Preston vs Emerson Jones match: 0.47/0.50 mid 48.5%, model 53.8% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17PREJON-1-JON` Will Emerson Jones win set 1 in the Taylah Preston vs Emerson Jones match: 0.48/0.52 mid 50.0%, model 46.2% (projection_v2.0 (prediction ledger)) -- gap -3.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17PREJON-2-JON` Will Emerson Jones win set 2 in the Taylah Preston vs Emerson Jones match: 0.48/0.52 mid 50.0%, model 46.2% (projection_v2.0 (prediction ledger)) -- gap -3.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mary Stoiana vs Sayaka Ishii -- WTA Osaka Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 04:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-18 02:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: 2026-10-18 01:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T04:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:223168:259967:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sayaka Ishii (`KXWTAMATCH-26OCT17STOISH-ISH`) | 0.13 / 0.14 (3784) | 13.5% | 21.9% | 19.9% | 23.6% [22.1%-27.3%] | 14.7% | 12.6% | 14.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +8.4 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Mary Stoiana (`KXWTAMATCH-26OCT17STOISH-STO`) | 0.86 / 0.87 (1778) | 86.5% | 78.1% | 80.2% | 76.3% [72.7%-77.9%] | 85.3% | 87.0% | 86.2% | MODEL_LONE_OUTLIER | PASS | -8.4 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2840.0, B 1713.0; serve-point win A 61.7%, B 44.2%; Elo A 1802.0, B 1641.6; model uncertainty 0.0263
* Form inputs: days since last match A 0, B 0; matches on record A 141, B 190; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.012, surface_pool_high -0.012, surface_dev_loose +0.007, surface_dev_tight -0.012
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 6 carry a model probability
  * `KXWTAGTOTAL-26OCT17STOISH-19` Over 18.5 games: 0.50/0.52 mid 51.0%, model 76.0% (projection_v2.0 (prediction ledger)) -- gap +25.0 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT17STOISH-2-ISH` Will Sayaka Ishii win set 2 in the Mary Stoiana vs Sayaka Ishii match: 0.13/0.19 mid 16.0%, model 30.2% (projection_v2.0 (prediction ledger)) -- gap +14.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17STOISH-1-ISH` Will Sayaka Ishii win set 1 in the Mary Stoiana vs Sayaka Ishii match: 0.15/0.20 mid 17.5%, model 30.2% (projection_v2.0 (prediction ledger)) -- gap +12.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17STOISH-1-STO` Will Mary Stoiana win set 1 in the Mary Stoiana vs Sayaka Ishii match: 0.82/0.83 mid 82.5%, model 69.8% (projection_v2.0 (prediction ledger)) -- gap -12.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17STOISH-2-STO` Will Mary Stoiana win set 2 in the Mary Stoiana vs Sayaka Ishii match: 0.81/0.84 mid 82.5%, model 69.8% (projection_v2.0 (prediction ledger)) -- gap -12.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17STOISH-24` Over 23.5 games: 0.11/0.59 mid 35.0%, model 44.3% (projection_v2.0 (prediction ledger)) -- gap +9.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Brostrom Poulsen / Slavic vs Arutiunian / Pieczkowski -- M15 Lexington KY F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 02:55Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-18T02:55:40Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT17BROSLAARUPIE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arutiunian / Pieczkowski (`KXITFDOUBLES-26OCT17BROSLAARUPIE-ARUPIE`) | 0.01 / 0.99 (601) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Brostrom Poulsen / Slavic (`KXITFDOUBLES-26OCT17BROSLAARUPIE-BROSLA`) | 0.01 / 0.99 (1451) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Daria Snigur vs Katarzyna Kawa -- WTA Ningbo Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 05:00Z
* Current expected start: 2026-10-18 03:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: 2026-10-18 02:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-120_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:203514:220750:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katarzyna Kawa (`KXWTAMATCH-26OCT17SNIKAW-KAW`) | 0.16 / 0.17 (503) | 16.5% | 12.4% | 3.6% | 5.6% [3.9%-15.8%] | 19.1% | 17.0% | 17.0% | MODEL_LONE_OUTLIER | PASS | -4.1 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Daria Snigur (`KXWTAMATCH-26OCT17SNIKAW-SNI`) | 0.82 / 0.84 (14970) | 83.0% | 87.6% | 96.4% | 94.4% [84.2%-96.1%] | 80.9% | 82.7% | 82.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +4.6 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4190.0, B 4311.0; serve-point win A 57.7%, B 50.9%; Elo A 1893.2, B 1606.2; model uncertainty 0.0596
* Form inputs: days since last match A 0, B 0; matches on record A 442, B 702; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.007, surface_dev_loose +0.015, surface_dev_tight -0.020
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT17SNIKAW-16` Over 15.5 games: 0.54/0.95 mid 74.5%, model 90.5% (projection_v2.0 (prediction ledger)) -- gap +16.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17SNIKAW-21` Over 20.5 games: 0.41/0.42 mid 41.5%, model 48.7% (projection_v2.0 (prediction ledger)) -- gap +7.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17SNIKAW-26` Over 25.5 games: 0.05/0.41 mid 23.0%, model 28.2% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT17SNIKAW-2-KAW` Will Katarzyna Kawa win set 2 in the Daria Snigur vs Katarzyna Kawa match: 0.18/0.23 mid 20.5%, model 22.0% (projection_v2.0 (prediction ledger)) -- gap +1.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17SNIKAW-1-SNI` Will Daria Snigur win set 1 in the Daria Snigur vs Katarzyna Kawa match: 0.76/0.78 mid 77.0%, model 78.0% (projection_v2.0 (prediction ledger)) -- gap +1.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17SNIKAW-1-KAW` Will Katarzyna Kawa win set 1 in the Daria Snigur vs Katarzyna Kawa match: 0.19/0.23 mid 21.0%, model 22.0% (projection_v2.0 (prediction ledger)) -- gap +1.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17SNIKAW-2-SNI` Will Daria Snigur win set 2 in the Daria Snigur vs Katarzyna Kawa match: 0.77/0.79 mid 78.0%, model 78.0% (projection_v2.0 (prediction ledger)) -- gap +0.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Anastasia Zakharova vs Polina Kudermetova -- WTA Ningbo Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 05:00Z
* Current expected start: 2026-10-18 03:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: 2026-10-18 02:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-120_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:220435:221236:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Kudermetova (`KXWTAMATCH-26OCT17ZAKKUD-KUD`) | 0.45 / 0.46 (9957) | 45.5% | 52.8% | 47.4% | 47.9% [46.8%-48.4%] | 44.4% | 43.9% | -- | INSUFFICIENT_INPUTS | WATCH | +7.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anastasia Zakharova (`KXWTAMATCH-26OCT17ZAKKUD-ZAK`) | 0.55 / 0.56 (12018) | 55.5% | 47.2% | 52.6% | 52.1% [51.6%-53.2%] | 55.6% | 53.8% | -- | INSUFFICIENT_INPUTS | PASS | -8.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4628.0, B 4285.0; serve-point win A 55.9%, B 43.6%; Elo A 1819.2, B 1806.1; model uncertainty 0.0079
* Form inputs: days since last match A 0, B 0; matches on record A 479, B 388; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.011, surface_dev_loose +0.005, surface_dev_tight +0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT17ZAKKUD-17` Over 16.5 games: 0.47/0.98 mid 72.5%, model 93.7% (projection_v2.0 (prediction ledger)) -- gap +21.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17ZAKKUD-22` Over 21.5 games: 0.48/0.49 mid 48.5%, model 62.8% (projection_v2.0 (prediction ledger)) -- gap +14.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT17ZAKKUD-1-KUD` Will Polina Kudermetova win set 1 in the Anastasia Zakharova vs Polina Kudermetova match: 0.29/0.47 mid 38.0%, model 51.9% (projection_v2.0 (prediction ledger)) -- gap +13.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17ZAKKUD-27` Over 26.5 games: 0.03/0.55 mid 29.0%, model 39.5% (projection_v2.0 (prediction ledger)) -- gap +10.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT17ZAKKUD-1-ZAK` Will Anastasia Zakharova win set 1 in the Anastasia Zakharova vs Polina Kudermetova match: 0.53/0.55 mid 54.0%, model 48.1% (projection_v2.0 (prediction ledger)) -- gap -5.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17ZAKKUD-2-KUD` Will Polina Kudermetova win set 2 in the Anastasia Zakharova vs Polina Kudermetova match: 0.33/0.59 mid 46.0%, model 51.9% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17ZAKKUD-2-ZAK` Will Anastasia Zakharova win set 2 in the Anastasia Zakharova vs Polina Kudermetova match: 0.41/0.67 mid 54.0%, model 48.1% (projection_v2.0 (prediction ledger)) -- gap -5.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Harriet Dart vs Aoi Ito -- WTA Osaka Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 04:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-18 04:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: 2026-10-18 03:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T04:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211279:256684:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Harriet Dart (`KXWTAMATCH-26OCT17DARITO-DAR`) | 0.58 / 0.60 (752) | 59.0% | 62.4% | 79.2% | 71.3% [64.6%-74.4%] | 58.3% | 58.9% | 58.6% | MODEL_LONE_OUTLIER | SHADOW_BET | +3.4 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Aoi Ito (`KXWTAMATCH-26OCT17DARITO-ITO`) | 0.40 / 0.41 (8) | 40.5% | 37.6% | 20.8% | 28.7% [25.6%-35.4%] | 41.7% | 41.5% | 41.6% | MODEL_LONE_OUTLIER | PASS | -2.9 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4244.0, B 2722.0; serve-point win A 55.0%, B 47.3%; Elo A 1789.0, B 1765.2; model uncertainty 0.0489
* Form inputs: days since last match A 0, B 0; matches on record A 674, B 302; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.027, surface_pool_high -0.028, surface_dev_loose +0.009, surface_dev_tight -0.018
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT17DARITO-23` Over 22.5 games: 0.42/0.44 mid 43.0%, model 54.1% (projection_v2.0 (prediction ledger)) -- gap +11.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17DARITO-28` Over 27.5 games: 0.03/0.51 mid 27.0%, model 32.3% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT17DARITO-1-DAR` Will Harriet Dart win set 1 in the Harriet Dart vs Aoi Ito match: 0.55/0.57 mid 56.0%, model 58.3% (projection_v2.0 (prediction ledger)) -- gap +2.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17DARITO-2-DAR` Will Harriet Dart win set 2 in the Harriet Dart vs Aoi Ito match: 0.55/0.58 mid 56.5%, model 58.3% (projection_v2.0 (prediction ledger)) -- gap +1.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17DARITO-1-ITO` Will Aoi Ito win set 1 in the Harriet Dart vs Aoi Ito match: 0.40/0.45 mid 42.5%, model 41.7% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17DARITO-18` Over 17.5 games: 0.75/0.98 mid 86.5%, model 86.0% (projection_v2.0 (prediction ledger)) -- gap -0.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT17DARITO-2-ITO` Will Aoi Ito win set 2 in the Harriet Dart vs Aoi Ito match: 0.40/0.44 mid 42.0%, model 41.7% (projection_v2.0 (prediction ledger)) -- gap -0.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sinja Kraus vs Sofia Kenin -- WTA Osaka Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 04:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-18 04:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: 2026-10-18 03:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T04:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213550:221257:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Kenin (`KXWTAMATCH-26OCT17KRAKEN-KEN`) | 0.53 / 0.54 (6209) | 53.5% | 50.5% | 29.6% | 38.2% [34.8%-47.4%] | 52.2% | 53.3% | 53.3% | MODEL_LONE_OUTLIER | PASS | -3.0 pp | NORMAL | FRESH | A / LIMITED | EXTERNAL_STALE | VERIFIED |
| Sinja Kraus (`KXWTAMATCH-26OCT17KRAKEN-KRA`) | 0.47 / 0.48 (22299) | 47.5% | 49.5% | 70.4% | 61.8% [52.6%-65.2%] | 47.8% | 47.0% | 47.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +2.0 pp | NORMAL | FRESH | A / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5054.0, B 3897.0; serve-point win A 58.4%, B 41.5%; Elo A 1722.8, B 1812.1; model uncertainty 0.0631
* Form inputs: days since last match A 0, B 0; matches on record A 493, B 525; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.020, surface_dev_loose +0.015, surface_dev_tight -0.020
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT17KRAKEN-16` Over 15.5 games: 0.26/0.99 mid 62.5%, model 97.8% (projection_v2.0 (prediction ledger)) -- gap +35.3 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT17KRAKEN-21` Over 20.5 games: 0.53/0.54 mid 53.5%, model 69.3% (projection_v2.0 (prediction ledger)) -- gap +15.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT17KRAKEN-26` Over 25.5 games: 0.27/0.41 mid 34.0%, model 45.9% (projection_v2.0 (prediction ledger)) -- gap +11.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT17KRAKEN-1-KRA` Will Sinja Kraus win set 1 in the Sinja Kraus vs Sofia Kenin match: 0.45/0.47 mid 46.0%, model 49.6% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT17KRAKEN-1-KEN` Will Sofia Kenin win set 1 in the Sinja Kraus vs Sofia Kenin match: 0.52/0.54 mid 53.0%, model 50.3% (projection_v2.0 (prediction ledger)) -- gap -2.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT17KRAKEN-2-KRA` Will Sinja Kraus win set 2 in the Sinja Kraus vs Sofia Kenin match: 0.45/0.49 mid 47.0%, model 49.6% (projection_v2.0 (prediction ledger)) -- gap +2.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT17KRAKEN-2-KEN` Will Sofia Kenin win set 2 in the Sinja Kraus vs Sofia Kenin match: 0.50/0.54 mid 52.0%, model 50.3% (projection_v2.0 (prediction ledger)) -- gap -1.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; WIDE_SPREAD

## Claire Liu vs Maddison Inglis -- WTA Osaka Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 06:40Z
* Current expected start: 2026-10-18 04:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: 2026-10-18 03:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T06:40:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213666:214906:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maddison Inglis (`KXWTAMATCH-26OCT17LIUING-ING`) | 0.35 / 0.37 (8103) | 36.0% | 45.7% | 46.4% | 47.9% [42.2%-51.0%] | 36.8% | 54.8% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +9.7 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Claire Liu (`KXWTAMATCH-26OCT17LIUING-LIU`) | 0.63 / 0.65 (2543) | 64.0% | 54.3% | 53.6% | 52.1% [49.0%-57.8%] | 63.2% | 63.2% | 63.2% | MODEL_LONE_OUTLIER | PASS | -9.7 pp | NORMAL | FRESH | A / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3837.0, B 3027.0; serve-point win A 58.9%, B 41.9%; Elo A 1770.0, B 1770.9; model uncertainty 0.0443
* Form inputs: days since last match A 0, B 0; matches on record A 455, B 482; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.042, surface_pool_high -0.031, surface_dev_loose +0.005, surface_dev_tight +0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT17LIUING-18` Over 17.5 games: 0.26/0.97 mid 61.5%, model 89.4% (projection_v2.0 (prediction ledger)) -- gap +27.9 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT17LIUING-23` Over 22.5 games: 0.42/0.44 mid 43.0%, model 57.2% (projection_v2.0 (prediction ledger)) -- gap +14.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT17LIUING-2-ING` Will Maddison Inglis win set 2 in the Claire Liu vs Maddison Inglis match: 0.36/0.40 mid 38.0%, model 47.1% (projection_v2.0 (prediction ledger)) -- gap +9.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT17LIUING-1-ING` Will Maddison Inglis win set 1 in the Claire Liu vs Maddison Inglis match: 0.37/0.40 mid 38.5%, model 47.1% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT17LIUING-2-LIU` Will Claire Liu win set 2 in the Claire Liu vs Maddison Inglis match: 0.59/0.64 mid 61.5%, model 52.9% (projection_v2.0 (prediction ledger)) -- gap -8.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT17LIUING-1-LIU` Will Claire Liu win set 1 in the Claire Liu vs Maddison Inglis match: 0.60/0.62 mid 61.0%, model 52.9% (projection_v2.0 (prediction ledger)) -- gap -8.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26OCT17LIUING-28` Over 27.5 games: 0.03/0.59 mid 31.0%, model 36.0% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
* Warnings: EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Connie Ma vs Lea Ma -- W35 Redding CA SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221143:221220:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Connie Ma (`KXITFWMATCH-26OCT17MAXMAX2-MAX`) | 0.64 / 0.66 (1428) | 65.0% | 29.5% | 26.1% | 31.0% [29.0%-32.9%] | -- | -- | -- | -- | PASS | -35.5 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Lea Ma (`KXITFWMATCH-26OCT17MAXMAX2-MAX2`) | 0.36 / 0.38 (520) | 37.0% | 70.5% | 73.9% | 69.0% [67.1%-71.0%] | -- | -- | -- | -- | PASS | +33.5 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 2727.0; serve-point win A 56.5%, B 39.4%; Elo A 1475.0, B 1614.7; model uncertainty 0.0195
* Form inputs: days since last match A 1839, B 34; matches on record A 21, B 168; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT17MAXMAX2-MAX2  (YES = Lea Ma)
Model: 71%
Kalshi: 37%
Gap: +34 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.018, surface_pool_high +0.019, surface_dev_loose +0.001, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alycia Parks vs Yulia Putintseva -- WTA Ningbo Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 05:00Z
* Current expected start: 2026-10-18 04:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: 2026-10-18 03:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-30_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:201709:219917:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alycia Parks (`KXWTAMATCH-26OCT17PARPUT-PAR`) | 0.27 / 0.28 (13) | 27.5% | 38.4% | 41.2% | 39.1% [37.1%-40.7%] | 28.2% | 26.4% | 27.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +10.9 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Yulia Putintseva (`KXWTAMATCH-26OCT17PARPUT-PUT`) | 0.72 / 0.73 (6942) | 72.5% | 61.6% | 58.8% | 60.9% [59.3%-62.9%] | 71.8% | 74.0% | 71.8% | MODEL_LONE_OUTLIER | PASS | -10.9 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5263.0, B 4366.0; serve-point win A 56.9%, B 40.8%; Elo A 1775.0, B 1893.3; model uncertainty 0.0177
* Form inputs: days since last match A 0, B 0; matches on record A 437, B 857; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.010, surface_dev_loose +0.010, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT17PARPUT-22` Over 21.5 games: 0.47/0.49 mid 48.0%, model 62.6% (projection_v2.0 (prediction ledger)) -- gap +14.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17PARPUT-17` Over 16.5 games: 0.68/0.98 mid 83.0%, model 94.0% (projection_v2.0 (prediction ledger)) -- gap +11.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17PARPUT-27` Over 26.5 games: 0.03/0.56 mid 29.5%, model 39.4% (projection_v2.0 (prediction ledger)) -- gap +9.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT17PARPUT-1-PAR` Will Alycia Parks win set 1 in the Alycia Parks vs Yulia Putintseva match: 0.30/0.35 mid 32.5%, model 42.2% (projection_v2.0 (prediction ledger)) -- gap +9.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17PARPUT-1-PUT` Will Yulia Putintseva win set 1 in the Alycia Parks vs Yulia Putintseva match: 0.66/0.67 mid 66.5%, model 57.8% (projection_v2.0 (prediction ledger)) -- gap -8.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17PARPUT-2-PUT` Will Yulia Putintseva win set 2 in the Alycia Parks vs Yulia Putintseva match: 0.59/0.71 mid 65.0%, model 57.8% (projection_v2.0 (prediction ledger)) -- gap -7.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17PARPUT-2-PAR` Will Alycia Parks win set 2 in the Alycia Parks vs Yulia Putintseva match: 0.28/0.43 mid 35.5%, model 42.2% (projection_v2.0 (prediction ledger)) -- gap +6.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Anhelina Kalinina vs Aliaksandra Sasnovich -- WTA Ningbo Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 07:10Z
* Current expected start: 2026-10-18 04:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: 2026-10-18 03:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T07:10:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:205925:211843:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anhelina Kalinina (`KXWTAMATCH-26OCT18KALSAS-KAL`) | 0.41 / 0.42 (2585) | 41.5% | 51.5% | 56.8% | 54.8% [51.6%-55.3%] | 42.5% | 40.5% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +10.0 pp | REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aliaksandra Sasnovich (`KXWTAMATCH-26OCT18KALSAS-SAS`) | 0.57 / 0.59 (2493) | 58.0% | 48.5% | 43.2% | 45.2% [44.7%-48.4%] | 57.5% | 56.9% | -- | INSUFFICIENT_INPUTS | PASS | -9.5 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4204.0, B 4822.0; serve-point win A 56.1%, B 44.2%; Elo A 1824.8, B 1839.7; model uncertainty 0.0184
* Form inputs: days since last match A 5, B 0; matches on record A 611, B 789; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.011, surface_dev_loose -0.005, surface_dev_tight +0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT18KALSAS-17` Over 16.5 games: 0.27/0.99 mid 63.0%, model 93.6% (projection_v2.0 (prediction ledger)) -- gap +30.6 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT18KALSAS-22` Over 21.5 games: 0.48/0.50 mid 49.0%, model 62.8% (projection_v2.0 (prediction ledger)) -- gap +13.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT18KALSAS-1-KAL` Will Anhelina Kalinina win set 1 in the Anhelina Kalinina vs Aliaksandra Sasnovich match: 0.41/0.45 mid 43.0%, model 51.0% (projection_v2.0 (prediction ledger)) -- gap +8.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT18KALSAS-2-KAL` Will Anhelina Kalinina win set 2 in the Anhelina Kalinina vs Aliaksandra Sasnovich match: 0.41/0.46 mid 43.5%, model 51.0% (projection_v2.0 (prediction ledger)) -- gap +7.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT18KALSAS-2-SAS` Will Aliaksandra Sasnovich win set 2 in the Anhelina Kalinina vs Aliaksandra Sasnovich match: 0.54/0.59 mid 56.5%, model 49.0% (projection_v2.0 (prediction ledger)) -- gap -7.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT18KALSAS-1-SAS` Will Aliaksandra Sasnovich win set 1 in the Anhelina Kalinina vs Aliaksandra Sasnovich match: 0.54/0.57 mid 55.5%, model 49.0% (projection_v2.0 (prediction ledger)) -- gap -6.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26OCT18KALSAS-27` Over 26.5 games: 0.03/0.72 mid 37.5%, model 39.4% (projection_v2.0 (prediction ledger)) -- gap +1.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
* Warnings: EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Gabriel Diallo vs Rei Sakamoto -- ATP Almaty Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-18 06:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: 2026-10-18 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:209113:210536:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriel Diallo (`KXATPMATCH-26OCT18DIASAK-DIA`) | 0.51 / 0.52 (2463) | 51.5% | 55.4% | 52.8% | 55.7% [54.7%-57.1%] | 51.1% | 51.3% | 51.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +3.9 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Rei Sakamoto (`KXATPMATCH-26OCT18DIASAK-SAK`) | 0.48 / 0.49 (7082) | 48.5% | 44.6% | 47.2% | 44.3% [42.9%-45.3%] | 48.9% | 48.8% | 48.8% | MODEL_LONE_OUTLIER | PASS | -3.9 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4598.0, B 3076.0; serve-point win A 69.0%, B 32.2%; Elo A 1825.8, B 1744.4; model uncertainty 0.0119
* Form inputs: days since last match A 0, B 0; matches on record A 277, B 145; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.009, surface_dev_tight +0.014
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT18DIASAK-DIA21` Will Gabriel Diallo win the Gabriel Diallo vs Rei Sakamoto match by a set score of 2-1?: 0.06/0.24 mid 15.0%, model 26.7% (projection_v2.0 (prediction ledger)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18DIASAK-19` Over 18.5 games: 0.69/0.99 mid 84.0%, model 94.0% (projection_v2.0 (prediction ledger)) -- gap +9.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18DIASAK-24` Over 23.5 games: 0.48/0.49 mid 48.5%, model 58.4% (projection_v2.0 (prediction ledger)) -- gap +9.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18DIASAK-SAK5` Will Rei Sakamoto win at least 4.5 more games than Gabriel Diallo?: 0.13/0.23 mid 18.0%, model 9.1% (projection_v2.0 (prediction ledger)) -- gap -8.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18DIASAK-SAK21` Will Rei Sakamoto win the Gabriel Diallo vs Rei Sakamoto match by a set score of 2-1?: 0.09/0.23 mid 16.0%, model 23.1% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18DIASAK-SAK2` Will Rei Sakamoto win at least 1.5 more games than Gabriel Diallo?: 0.42/0.44 mid 43.0%, model 36.1% (projection_v2.0 (prediction ledger)) -- gap -6.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18DIASAK-29` Over 28.5 games: 0.33/0.38 mid 35.5%, model 42.1% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18DIASAK-SAK20` Will Rei Sakamoto win the Gabriel Diallo vs Rei Sakamoto match by a set score of 2-0?: 0.24/0.30 mid 27.0%, model 21.5% (projection_v2.0 (prediction ledger)) -- gap -5.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18DIASAK-1-DIA` Will Gabriel Diallo win set 1 in the Gabriel Diallo vs Rei Sakamoto match: 0.48/0.52 mid 50.0%, model 53.6% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18DIASAK-2-DIA` Will Gabriel Diallo win set 2 in the Gabriel Diallo vs Rei Sakamoto match: 0.49/0.52 mid 50.5%, model 53.6% (projection_v2.0 (prediction ledger)) -- gap +3.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18DIASAK-1-SAK` Will Rei Sakamoto win set 1 in the Gabriel Diallo vs Rei Sakamoto match: 0.47/0.50 mid 48.5%, model 46.4% (projection_v2.0 (prediction ledger)) -- gap -2.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18DIASAK-2-SAK` Will Rei Sakamoto win set 2 in the Gabriel Diallo vs Rei Sakamoto match: 0.47/0.50 mid 48.5%, model 46.4% (projection_v2.0 (prediction ledger)) -- gap -2.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT18DIASAK-DIA2` Will Gabriel Diallo win at least 1.5 more games than Rei Sakamoto?: 0.45/0.46 mid 45.5%, model 46.6% (projection_v2.0 (prediction ledger)) -- gap +1.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18DIASAK-DIA20` Will Gabriel Diallo win the Gabriel Diallo vs Rei Sakamoto match by a set score of 2-0?: 0.28/0.30 mid 29.0%, model 28.7% (projection_v2.0 (prediction ledger)) -- gap -0.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; WIDE_SPREAD

## Adam Walton vs Nikoloz Basilashvili -- ATP Almaty Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-18 06:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: 2026-10-18 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105932:200443:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikoloz Basilashvili (`KXATPMATCH-26OCT18WALBAS-BAS`) | 0.56 / 0.57 (1688) | 56.5% | 35.8% | 39.3% | 40.2% [36.9%-45.1%] | 55.6% | 56.0% | 55.9% | MODEL_LONE_OUTLIER | PASS | -20.7 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Adam Walton (`KXATPMATCH-26OCT18WALBAS-WAL`) | 0.42 / 0.43 (3670) | 42.5% | 64.2% | 60.7% | 59.8% [54.9%-63.1%] | 44.4% | 43.9% | 44.1% | MODEL_LONE_OUTLIER | SHADOW_BET | +21.7 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5302.0, B 3285.0; serve-point win A 66.3%, B 36.6%; Elo A 1742.6, B 1683.6; model uncertainty 0.0407
* Form inputs: days since last match A 0, B 0; matches on record A 348, B 911; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT18WALBAS-WAL  (YES = Adam Walton)
Model: 64%
Kalshi: 42%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.024, surface_pool_high +0.033, surface_dev_loose -0.015, surface_dev_tight +0.015
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT18WALBAS-WAL2` Will Adam Walton win at least 1.5 more games than Nikoloz Basilashvili?: 0.32/0.40 mid 36.0%, model 56.8% (projection_v2.0 (prediction ledger)) -- gap +20.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18WALBAS-BAS2` Will Nikoloz Basilashvili win at least 1.5 more games than Adam Walton?: 0.49/0.50 mid 49.5%, model 28.7% (projection_v2.0 (prediction ledger)) -- gap -20.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18WALBAS-WAL20` Will Adam Walton win the Adam Walton vs Nikoloz Basilashvili match by a set score of 2-0?: 0.07/0.26 mid 16.5%, model 35.5% (projection_v2.0 (prediction ledger)) -- gap +19.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18WALBAS-2-WAL` Will Adam Walton win set 2 in the Adam Walton vs Nikoloz Basilashvili match: 0.43/0.47 mid 45.0%, model 59.6% (projection_v2.0 (prediction ledger)) -- gap +14.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18WALBAS-1-WAL` Will Adam Walton win set 1 in the Adam Walton vs Nikoloz Basilashvili match: 0.43/0.48 mid 45.5%, model 59.6% (projection_v2.0 (prediction ledger)) -- gap +14.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18WALBAS-BAS20` Will Nikoloz Basilashvili win the Adam Walton vs Nikoloz Basilashvili match by a set score of 2-0?: 0.25/0.34 mid 29.5%, model 16.3% (projection_v2.0 (prediction ledger)) -- gap -13.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18WALBAS-2-BAS` Will Nikoloz Basilashvili win set 2 in the Adam Walton vs Nikoloz Basilashvili match: 0.52/0.55 mid 53.5%, model 40.4% (projection_v2.0 (prediction ledger)) -- gap -13.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18WALBAS-1-BAS` Will Nikoloz Basilashvili win set 1 in the Adam Walton vs Nikoloz Basilashvili match: 0.52/0.54 mid 53.0%, model 40.4% (projection_v2.0 (prediction ledger)) -- gap -12.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18WALBAS-WAL21` Will Adam Walton win the Adam Walton vs Nikoloz Basilashvili match by a set score of 2-1?: 0.10/0.23 mid 16.5%, model 28.7% (projection_v2.0 (prediction ledger)) -- gap +12.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18WALBAS-BAS5` Will Nikoloz Basilashvili win at least 4.5 more games than Adam Walton?: 0.09/0.24 mid 16.5%, model 9.0% (projection_v2.0 (prediction ledger)) -- gap -7.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18WALBAS-21` Over 20.5 games: 0.50/0.88 mid 69.0%, model 73.9% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18WALBAS-BAS21` Will Nikoloz Basilashvili win the Adam Walton vs Nikoloz Basilashvili match by a set score of 2-1?: 0.04/0.26 mid 15.0%, model 19.4% (projection_v2.0 (prediction ledger)) -- gap +4.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18WALBAS-26` Over 25.5 games: 0.40/0.49 mid 44.5%, model 48.9% (projection_v2.0 (prediction ledger)) -- gap +4.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18WALBAS-31` Over 30.5 games: 0.03/0.43 mid 23.0%, model 26.6% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; WIDE_SPREAD

## Tatiana Prozorova vs Kamilla Rakhimova -- WTA Ningbo Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 08:20Z
* Current expected start: 2026-10-18 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: 2026-10-18 05:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-140_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T08:20:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215872:236955:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tatiana Prozorova (`KXWTAMATCH-26OCT18PRORAK-PRO`) | 0.42 / 0.43 (8) | 42.5% | 49.3% | 72.2% | 64.8% [49.5%-69.0%] | 40.6% | 43.7% | 43.7% | MODEL_LONE_OUTLIER | WATCH | +6.8 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Kamilla Rakhimova (`KXWTAMATCH-26OCT18PRORAK-RAK`) | 0.56 / 0.58 (1950) | 57.0% | 50.7% | 27.8% | 35.2% [31.0%-50.5%] | 59.4% | 56.2% | 56.2% | MODEL_LONE_OUTLIER | PASS | -6.3 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3551.0, B 5718.0; serve-point win A 58.5%, B 41.4%; Elo A 1799.1, B 1839.4; model uncertainty 0.0977
* Form inputs: days since last match A 10, B 7; matches on record A 290, B 475; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose +0.009, surface_dev_tight -0.019
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT18PRORAK-16` Over 15.5 games: 0.46/0.97 mid 71.5%, model 97.8% (projection_v2.0 (prediction ledger)) -- gap +26.3 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT18PRORAK-21` Over 20.5 games: 0.53/0.55 mid 54.0%, model 69.3% (projection_v2.0 (prediction ledger)) -- gap +15.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT18PRORAK-26` Over 25.5 games: 0.03/0.63 mid 33.0%, model 46.0% (projection_v2.0 (prediction ledger)) -- gap +13.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT18PRORAK-2-PRO` Will Tatiana Prozorova win set 2 in the Tatiana Prozorova vs Kamilla Rakhimova match: 0.41/0.44 mid 42.5%, model 49.5% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT18PRORAK-1-PRO` Will Tatiana Prozorova win set 1 in the Tatiana Prozorova vs Kamilla Rakhimova match: 0.41/0.45 mid 43.0%, model 49.5% (projection_v2.0 (prediction ledger)) -- gap +6.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT18PRORAK-2-RAK` Will Kamilla Rakhimova win set 2 in the Tatiana Prozorova vs Kamilla Rakhimova match: 0.54/0.58 mid 56.0%, model 50.5% (projection_v2.0 (prediction ledger)) -- gap -5.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT18PRORAK-1-RAK` Will Kamilla Rakhimova win set 1 in the Tatiana Prozorova vs Kamilla Rakhimova match: 0.54/0.57 mid 55.5%, model 50.5% (projection_v2.0 (prediction ledger)) -- gap -5.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Han Shi vs Alina Korneeva -- WTA Ningbo Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 08:20Z
* Current expected start: 2026-10-18 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: 2026-10-18 05:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-140_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T08:20:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:222559:252499:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alina Korneeva (`KXWTAMATCH-26OCT18SHIKOR-KOR`) | 0.74 / 0.75 (2755) | 74.5% | 85.2% | 76.0% | 79.6% [78.0%-82.8%] | 73.4% | 73.9% | 73.6% | MODEL_LONE_OUTLIER | SHADOW_BET | +10.7 pp | REVIEW | FRESH | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Han Shi (`KXWTAMATCH-26OCT18SHIKOR-SHI`) | 0.25 / 0.27 (9030) | 26.0% | 14.8% | 24.0% | 20.4% [17.2%-22.0%] | 26.7% | 26.4% | 26.5% | MODEL_LONE_OUTLIER | PASS | -11.2 pp | REVIEW | FRESH | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3226.0, B 3297.0; serve-point win A 50.3%, B 41.8%; Elo A 1600.6, B 1915.0; model uncertainty 0.0237
* Form inputs: days since last match A 173, B 21; matches on record A 228, B 191; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.011, surface_dev_loose +0.004, surface_dev_tight -0.004
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT18SHIKOR-15` Over 14.5 games: 0.50/0.99 mid 74.5%, model 96.6% (projection_v2.0 (prediction ledger)) -- gap +22.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT18SHIKOR-2-SHI` Will Han Shi win set 2 in the Han Shi vs Alina Korneeva match: 0.26/0.38 mid 32.0%, model 24.2% (projection_v2.0 (prediction ledger)) -- gap -7.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT18SHIKOR-1-KOR` Will Alina Korneeva win set 1 in the Han Shi vs Alina Korneeva match: 0.68/0.70 mid 69.0%, model 75.8% (projection_v2.0 (prediction ledger)) -- gap +6.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT18SHIKOR-1-SHI` Will Han Shi win set 1 in the Han Shi vs Alina Korneeva match: 0.27/0.32 mid 29.5%, model 24.2% (projection_v2.0 (prediction ledger)) -- gap -5.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT18SHIKOR-2-KOR` Will Alina Korneeva win set 2 in the Han Shi vs Alina Korneeva match: 0.68/0.73 mid 70.5%, model 75.8% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26OCT18SHIKOR-20` Over 19.5 games: 0.56/0.57 mid 56.5%, model 58.8% (projection_v2.0 (prediction ledger)) -- gap +2.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT18SHIKOR-25` Over 24.5 games: 0.03/0.63 mid 33.0%, model 34.8% (projection_v2.0 (prediction ledger)) -- gap +1.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Xi Cheng Huang vs Semen Pankin -- ATP Challenger Guangzhou Nansha Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-18T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT17HUAPAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xi Cheng Huang (`KXATPCHALLENGERMATCH-26OCT17HUAPAN-HUA`) | 0.08 / 0.10 (6591) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Semen Pankin (`KXATPCHALLENGERMATCH-26OCT17HUAPAN-PAN`) | 0.91 / 0.93 (8977) | 92.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Arthur Weber vs Dominik Palan -- ATP Challenger Guangzhou Nansha Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-18T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207186:208158:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dominik Palan (`KXATPCHALLENGERMATCH-26OCT17WEBPAL-PAL`) | 0.20 / 0.21 (8) | 20.5% | 38.5% | 28.5% | 32.5% [29.8%-36.6%] | -- | 20.8% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +18.0 pp | HIGH_REVIEW | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Arthur Weber (`KXATPCHALLENGERMATCH-26OCT17WEBPAL-WEB`) | 0.78 / 0.80 (521) | 79.0% | 61.5% | 71.5% | 67.5% [63.4%-70.2%] | -- | 78.8% | -- | INSUFFICIENT_INPUTS | PASS | -17.5 pp | HIGH_REVIEW | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1097.0, B 1229.0; serve-point win A 63.9%, B 38.4%; Elo A 1438.7, B 1342.5; model uncertainty 0.034
* Form inputs: days since last match A 18, B 33; matches on record A 169, B 283; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT17WEBPAL-PAL  (YES = Dominik Palan)
Model: 39%
Kalshi: 20%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: LOW_DISPLAYED_LIQUIDITY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.018, surface_pool_high +0.000, surface_dev_loose +0.009, surface_dev_tight -0.019
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; THIN_DISPLAYED_SIZE

## Xiaoyin Yang vs Khumoyun Sultanov -- ATP Challenger Guangzhou Nansha Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-18T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT17YANSUL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Khumoyun Sultanov (`KXATPCHALLENGERMATCH-26OCT17YANSUL-SUL`) | 0.89 / 0.92 (105) | 90.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xiaoyin Yang (`KXATPCHALLENGERMATCH-26OCT17YANSUL-YAN`) | 0.07 / 0.11 (666) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Millen Hurrion vs Koki Matsuda -- ATP Challenger Guangzhou Nansha Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 07:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-18T07:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209140:211628:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Millen Hurrion (`KXATPCHALLENGERMATCH-26OCT18HURMAT-HUR`) | 0.63 / 0.66 (78) | 64.5% | 70.5% | 49.0% | 65.1% [59.4%-70.6%] | -- | 67.5% | -- | INSUFFICIENT_INPUTS | PASS | +6.0 pp | NORMAL | FRESH | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Koki Matsuda (`KXATPCHALLENGERMATCH-26OCT18HURMAT-MAT`) | 0.33 / 0.34 (350) | 33.5% | 29.5% | 51.0% | 34.9% [29.4%-40.6%] | -- | 32.3% | -- | INSUFFICIENT_INPUTS | PASS | -4.0 pp | NORMAL | FRESH | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 300.0, B 1097.0; serve-point win A 65.9%, B 38.4%; Elo A 1429.0, B 1296.1; model uncertainty 0.0561
* Form inputs: days since last match A 75, B 33; matches on record A 101, B 83; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.032, surface_pool_high -0.028, surface_dev_loose +0.004, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY

## Masamichi Imamura vs Saba Purtseladze -- ATP Challenger Guangzhou Nansha Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 07:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-18T07:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:201987:208182:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Masamichi Imamura (`KXATPCHALLENGERMATCH-26OCT18IMAPUR-IMA`) | 0.59 / 0.62 (447) | 60.5% | 67.2% | 75.9% | 69.7% [64.7%-72.7%] | -- | 59.6% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +6.7 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Saba Purtseladze (`KXATPCHALLENGERMATCH-26OCT18IMAPUR-PUR`) | 0.37 / 0.40 (46) | 38.5% | 32.8% | 24.1% | 30.3% [27.4%-35.3%] | -- | 40.3% | -- | INSUFFICIENT_INPUTS | PASS | -5.7 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1040.0, B 1480.0; serve-point win A 65.0%, B 38.6%; Elo A 1522.0, B 1418.9; model uncertainty 0.0396
* Form inputs: days since last match A 25, B 68; matches on record A 149, B 279; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.013, surface_dev_loose +0.008, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Omar Jasika vs Hiroki Moriya -- ATP Challenger Guangzhou Nansha Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 07:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-18T07:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105655:117357:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Omar Jasika (`KXATPCHALLENGERMATCH-26OCT18JASMOR-JAS`) | 0.63 / 0.65 (107) | 64.0% | 58.1% | 37.8% | 44.3% [41.8%-47.4%] | -- | 65.3% | -- | INSUFFICIENT_INPUTS | PASS | -5.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hiroki Moriya (`KXATPCHALLENGERMATCH-26OCT18JASMOR-MOR`) | 0.32 / 0.36 (250) | 34.0% | 41.9% | 62.2% | 55.7% [52.6%-58.2%] | -- | 34.5% | -- | INSUFFICIENT_INPUTS | WATCH | +7.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2343.0, B 2232.0; serve-point win A 60.2%, B 41.4%; Elo A 1509.5, B 1481.1; model uncertainty 0.0282
* Form inputs: days since last match A 18, B 33; matches on record A 462, B 1021; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.025, surface_pool_high +0.026, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Nao Nishino vs Annika Penickova -- W35 Redding CA SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 07:15Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T07:15:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:265628:266379:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nao Nishino (`KXITFWMATCH-26OCT17NISPEN-NIS`) | 0.29 / 0.32 (333) | 30.5% | 26.4% | 23.2% | 32.6% [28.8%-36.4%] | 29.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Annika Penickova (`KXITFWMATCH-26OCT17NISPEN-PEN`) | 0.68 / 0.69 (2211) | 68.5% | 73.6% | 76.8% | 67.4% [63.6%-71.2%] | 70.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 295.0, B 702.0; serve-point win A 52.9%, B 42.4%; Elo A 1367.9, B 1478.8; model uncertainty 0.0378
* Form inputs: days since last match A 446, B 53; matches on record A 12, B 38; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.005, surface_dev_loose -0.009, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Roman Safiullin vs Ilia Simakin -- ATP Almaty Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 08:00Z
* Current expected start: 2026-10-18 07:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: 2026-10-18 06:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-30_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126128:209899:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Roman Safiullin (`KXATPMATCH-26OCT18SAFSIM-SAF`) | 0.78 / 0.79 (17) | 78.5% | 67.3% | 52.4% | 57.8% [54.9%-65.4%] | 77.5% | 77.6% | 77.5% | MODEL_LONE_OUTLIER | PASS | -11.2 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Ilia Simakin (`KXATPMATCH-26OCT18SAFSIM-SIM`) | 0.20 / 0.22 (15144) | 21.0% | 32.7% | 47.5% | 42.2% [34.6%-45.1%] | 22.5% | 22.1% | 22.3% | MODEL_LONE_OUTLIER | WATCH | +11.7 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4418.0, B 3713.0; serve-point win A 67.2%, B 36.5%; Elo A 1876.8, B 1720.5; model uncertainty 0.0524
* Form inputs: days since last match A 8, B 9; matches on record A 675, B 239; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.024, surface_pool_high -0.019, surface_dev_loose -0.005, surface_dev_tight +0.015
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT18SAFSIM-17` Over 16.5 games: 0.01/0.99 mid 50.0%, model 97.6% (projection_v2.0 (prediction ledger)) -- gap +47.6 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18SAFSIM-SAF5` Will Roman Safiullin win at least 4.5 more games than Ilia Simakin?: 0.42/0.43 mid 42.5%, model 24.9% (projection_v2.0 (prediction ledger)) -- gap -17.6 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18SAFSIM-22` Over 21.5 games: 0.52/0.53 mid 52.5%, model 68.8% (projection_v2.0 (prediction ledger)) -- gap +16.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18SAFSIM-SAF2` Will Roman Safiullin win at least 1.5 more games than Ilia Simakin?: 0.73/0.78 mid 75.5%, model 60.0% (projection_v2.0 (prediction ledger)) -- gap -15.5 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18SAFSIM-27` Over 26.5 games: 0.24/0.33 mid 28.5%, model 43.1% (projection_v2.0 (prediction ledger)) -- gap +14.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18SAFSIM-SAF21` Will Roman Safiullin win the Roman Safiullin vs Ilia Simakin match by a set score of 2-1?: 0.07/0.25 mid 16.0%, model 29.2% (projection_v2.0 (prediction ledger)) -- gap +13.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18SAFSIM-1-SIM` Will Ilia Simakin win set 1 in the Roman Safiullin vs Ilia Simakin match: 0.25/0.28 mid 26.5%, model 38.2% (projection_v2.0 (prediction ledger)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18SAFSIM-1-SAF` Will Roman Safiullin win set 1 in the Roman Safiullin vs Ilia Simakin match: 0.71/0.75 mid 73.0%, model 61.8% (projection_v2.0 (prediction ledger)) -- gap -11.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18SAFSIM-2-SAF` Will Roman Safiullin win set 2 in the Roman Safiullin vs Ilia Simakin match: 0.71/0.75 mid 73.0%, model 61.8% (projection_v2.0 (prediction ledger)) -- gap -11.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18SAFSIM-2-SIM` Will Ilia Simakin win set 2 in the Roman Safiullin vs Ilia Simakin match: 0.25/0.29 mid 27.0%, model 38.2% (projection_v2.0 (prediction ledger)) -- gap +11.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18SAFSIM-SAF20` Will Roman Safiullin win the Roman Safiullin vs Ilia Simakin match by a set score of 2-0?: 0.36/0.59 mid 47.5%, model 38.2% (projection_v2.0 (prediction ledger)) -- gap -9.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18SAFSIM-SIM21` Will Ilia Simakin win the Roman Safiullin vs Ilia Simakin match by a set score of 2-1?: 0.07/0.11 mid 9.0%, model 18.1% (projection_v2.0 (prediction ledger)) -- gap +9.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18SAFSIM-SIM20` Will Ilia Simakin win the Roman Safiullin vs Ilia Simakin match by a set score of 2-0?: 0.01/0.11 mid 6.0%, model 14.6% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Martin Borisiouk vs Matthew Dellavedova -- M25 Qian Daohu F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 07:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200456:202354:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martin Borisiouk (`KXITFMATCH-26OCT17BORDEL-BOR`) | 0.36 / 0.39 (306) | 37.5% | 42.1% | 65.5% | 39.2% [33.5%-45.6%] | 38.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.7 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matthew Dellavedova (`KXITFMATCH-26OCT17BORDEL-DEL`) | 0.61 / 0.64 (74) | 62.5% | 57.9% | 34.5% | 60.8% [54.4%-66.5%] | 61.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.7 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 345.0, B 1203.0; serve-point win A 63.4%, B 35.0%; Elo A 1337.8, B 1461.1; model uncertainty 0.0604
* Form inputs: days since last match A 33, B 25; matches on record A 80, B 356; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.024, surface_pool_high +0.015, surface_dev_loose +0.001, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ekaterina Khodzhaeva vs Natalie CHEN -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17KHOCHE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Natalie CHEN (`KXITFWMATCH-26OCT17KHOCHE-CHE`) | 0.07 / 0.90 (100) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ekaterina Khodzhaeva (`KXITFWMATCH-26OCT17KHOCHE-KHO`) | 0.03 / 0.96 (39) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuka Matsumoto vs Faith Perera -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17MATPER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuka Matsumoto (`KXITFWMATCH-26OCT17MATPER-MAT`) | 0.03 / 0.95 (27) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Faith Perera (`KXITFWMATCH-26OCT17MATPER-PER`) | 0.03 / 0.95 (100) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofya Nabokova vs Jannat Chiripal -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17NABCHI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jannat Chiripal (`KXITFWMATCH-26OCT17NABCHI-CHI`) | 0.04 / 0.97 (285) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sofya Nabokova (`KXITFWMATCH-26OCT17NABCHI-NAB`) | 0.03 / 0.97 (363) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sarah Pang vs Xiaochuan Nie -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215091:222181:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xiaochuan Nie (`KXITFWMATCH-26OCT17PANNIE-NIE`) | 0.03 / 0.97 (285) | 50.0% | 76.2% | 61.6% | 68.5% [67.6%-69.4%] | -- | -- | -- | -- | PASS | +26.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Sarah Pang (`KXITFWMATCH-26OCT17PANNIE-PAN`) | 0.05 / 0.91 (100) | 48.0% | 23.8% | 38.4% | 31.5% [30.6%-32.4%] | -- | -- | -- | -- | PASS | -24.2 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 146.0, B 63.0; serve-point win A 50.3%, B 44.4%; Elo A 962.5, B 1099.8; model uncertainty 0.0093
* Form inputs: days since last match A 957, B 334; matches on record A 73, B 9; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT17PANNIE-NIE  (YES = Xiaochuan Nie)
Model: 76%
Kalshi: 50%
Gap: +26 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lidia Podgorichani vs Harini Parthiban -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17PODPAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Harini Parthiban (`KXITFWMATCH-26OCT17PODPAR-PAR`) | 0.03 / 0.96 (100) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lidia Podgorichani (`KXITFWMATCH-26OCT17PODPAR-POD`) | 0.03 / 0.95 (27) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gabriela Dabrowski / Luisa Stefani vs Storm Hunter / Katerina Siniakova -- WTA Wuhan F

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 11:00Z
* Current expected start: 2026-10-18 08:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: 2026-10-18 07:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-18T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18DABSTEHUNSIN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriela Dabrowski / Luisa Stefani (`KXWTADOUBLES-26OCT18DABSTEHUNSIN-DABSTE`) | 0.53 / 0.56 (284) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Storm Hunter / Katerina Siniakova (`KXWTADOUBLES-26OCT18DABSTEHUNSIN-HUNSIN`) | 0.44 / 0.46 (394) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Ariana Geerlings Martinez vs Laura Samson -- WTA 125K Mallorca F

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 11:00Z
* Current expected start: 2026-10-18 08:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: 2026-10-18 07:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Grass · scheduled 2026-10-18T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:231639:266671:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ariana Geerlings Martinez (`KXWTACHALLENGERMATCH-26OCT18GEESAM-GEE`) | 0.37 / 0.39 (253) | 38.0% | 37.2% | 38.9% | 38.4% [35.9%-38.9%] | 39.1% | 37.4% | 39.1% | MARKETS_AGREE | PASS | -0.8 pp | NORMAL | FRESH | A / LIMITED | ALL_AGREE | AMBIGUOUS |
| Laura Samson (`KXWTACHALLENGERMATCH-26OCT18GEESAM-SAM`) | 0.61 / 0.62 (11) | 61.5% | 62.8% | 61.1% | 61.6% [61.1%-64.1%] | 60.9% | 62.7% | 60.9% | MARKETS_AGREE | PASS | +1.3 pp | NORMAL | FRESH | A / LIMITED | ALL_AGREE | AMBIGUOUS |

* Serve evidence (points): A 2773.0, B 2910.0; serve-point win A 50.4%, B 47.1%; Elo A 1701.0, B 1793.2; model uncertainty 0.0151
* Form inputs: days since last match A 0, B 1; matches on record A 159, B 134; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Daria KHOMUTSIANSKAYA vs Sijia Wei -- W15 Shenzhen F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221096:222944:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daria KHOMUTSIANSKAYA (`KXITFWMATCH-26OCT17KHOWEI-KHO`) | 0.47 / 0.51 (7440) | 49.0% | 52.3% | 92.9% | 78.6% [60.0%-85.5%] | 50.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +3.3 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sijia Wei (`KXITFWMATCH-26OCT17KHOWEI-WEI`) | 0.49 / 0.51 (5) | 50.0% | 47.7% | 7.1% | 21.3% [14.5%-40.0%] | 50.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.3 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3178.0, B 2150.0; serve-point win A 56.4%, B 44.1%; Elo A 1665.8, B 1716.7; model uncertainty 0.1275
* Form inputs: days since last match A 271, B 12; matches on record A 171, B 308; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.022, surface_pool_high -0.020, surface_dev_loose +0.007, surface_dev_tight -0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yu Shan vs Anna Yang -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220031:264242:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yu Shan (`KXITFWMATCH-26OCT17SHAYAN-SHA`) | 0.08 / 0.13 (185) | 10.5% | 35.8% | 10.4% | 28.8% [24.2%-32.5%] | -- | -- | -- | -- | PASS | +25.3 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anna Yang (`KXITFWMATCH-26OCT17SHAYAN-YAN`) | 0.86 / 0.89 (92) | 87.5% | 64.2% | 89.6% | 71.2% [67.5%-75.8%] | -- | -- | -- | -- | PASS | -23.3 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 408.0, B 270.0; serve-point win A 54.3%, B 42.9%; Elo A 1186.3, B 1302.6; model uncertainty 0.0417
* Form inputs: days since last match A 173, B 355; matches on record A 153, B 21; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT17SHAYAN-SHA  (YES = Yu Shan)
Model: 36%
Kalshi: 10%
Gap: +25 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.018, surface_dev_loose -0.009, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Junjie Sun vs Chihiro Muramatsu -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17SUNMUR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chihiro Muramatsu (`KXITFWMATCH-26OCT17SUNMUR-MUR`) | 0.09 / 0.96 (59) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Junjie Sun (`KXITFWMATCH-26OCT17SUNMUR-SUN`) | 0.03 / 0.69 (81) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jiayu Xu vs Kanna Soeda -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222606:267412:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanna Soeda (`KXITFWMATCH-26OCT17XUXSOE-SOE`) | 0.04 / 0.12 (135) | 8.0% | 29.2% | 79.7% | 40.5% [35.4%-46.3%] | -- | -- | -- | -- | PASS | +21.2 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jiayu Xu (`KXITFWMATCH-26OCT17XUXSOE-XUX`) | 0.87 / 0.93 (6248) | 90.0% | 70.8% | 20.3% | 59.5% [53.7%-64.6%] | -- | -- | -- | -- | PASS | -19.2 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 444.0, B 117.0; serve-point win A 55.2%, B 48.9%; Elo A 1324.1, B 1233.8; model uncertainty 0.0543
* Form inputs: days since last match A 173, B 488; matches on record A 86, B 28; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT17XUXSOE-SOE  (YES = Kanna Soeda)
Model: 29%
Kalshi: 8%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.021, surface_dev_loose -0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ma / Passola vs Rencheli / Sholokhova -- W35 Redding CA F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 08:15Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-18T08:15:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17MAXPASRENSHO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ma / Passola (`KXITFWDOUBLES-26OCT17MAXPASRENSHO-MAXPAS`) | 0.08 / 0.49 (49) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rencheli / Sholokhova (`KXITFWDOUBLES-26OCT17MAXPASRENSHO-RENSHO`) | 0.13 / 0.66 (73) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Kasidit Samrej vs Naoya Honda -- ATP Challenger Guangzhou Nansha Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 08:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-18T08:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208937:211897:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naoya Honda (`KXATPCHALLENGERMATCH-26OCT18SAMHON-HON`) | 0.30 / 0.32 (353) | 31.0% | 36.4% | 64.6% | 37.8% [31.8%-43.6%] | -- | 29.8% | -- | INSUFFICIENT_INPUTS | WATCH | +5.4 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kasidit Samrej (`KXATPCHALLENGERMATCH-26OCT18SAMHON-SAM`) | 0.67 / 0.70 (249) | 68.5% | 63.6% | 35.4% | 62.2% [56.4%-68.2%] | -- | 69.9% | -- | INSUFFICIENT_INPUTS | PASS | -4.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1583.0, B 491.0; serve-point win A 65.6%, B 37.2%; Elo A 1468.5, B 1315.2; model uncertainty 0.0591
* Form inputs: days since last match A 28, B 33; matches on record A 208, B 27; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high +0.000, surface_dev_loose +0.004, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY

## Yuta Shimizu vs Alibek Kachmazov -- ATP Challenger Guangzhou Nansha Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 08:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-18T08:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202122:208230:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alibek Kachmazov (`KXATPCHALLENGERMATCH-26OCT18SHIKAC-KAC`) | 0.64 / 0.68 (851) | 66.0% | 50.3% | 58.1% | 59.6% [57.1%-60.6%] | -- | 67.3% | -- | INSUFFICIENT_INPUTS | PASS | -15.7 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuta Shimizu (`KXATPCHALLENGERMATCH-26OCT18SHIKAC-SHI`) | 0.32 / 0.34 (380) | 33.0% | 49.6% | 41.9% | 40.4% [39.4%-42.9%] | -- | 32.8% | -- | INSUFFICIENT_INPUTS | PASS | +16.6 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3350.0, B 4061.0; serve-point win A 61.3%, B 38.7%; Elo A 1578.0, B 1664.9; model uncertainty 0.0175
* Form inputs: days since last match A 18, B 446; matches on record A 442, B 327; data quality D

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT18SHIKAC-SHI  (YES = Yuta Shimizu)
Model: 50%
Kalshi: 33%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY

## Yaojie Zeng vs Evan Zhu -- ATP Challenger Guangzhou Nansha Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 08:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-18T08:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200632:210483:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yaojie Zeng (`KXATPCHALLENGERMATCH-26OCT18ZENZHU-ZEN`) | 0.21 / 0.22 (140) | 21.5% | 37.9% | 53.0% | 35.7% [32.4%-38.2%] | -- | 21.9% | -- | INSUFFICIENT_INPUTS | WATCH | +16.4 pp | HIGH_REVIEW | FRESH | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Evan Zhu (`KXATPCHALLENGERMATCH-26OCT18ZENZHU-ZHU`) | 0.76 / 0.79 (414) | 77.5% | 62.1% | 47.0% | 64.3% [61.8%-67.6%] | -- | 77.9% | -- | INSUFFICIENT_INPUTS | PASS | -15.4 pp | HIGH_REVIEW | FRESH | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 290.0, B 1210.0; serve-point win A 61.7%, B 35.8%; Elo A 1228.3, B 1355.9; model uncertainty 0.0287
* Form inputs: days since last match A 18, B 18; matches on record A 32, B 347; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT18ZENZHU-ZEN  (YES = Yaojie Zeng)
Model: 38%
Kalshi: 22%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.014, surface_dev_loose -0.004, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY

## Alejandro Davidovich Fokina vs Rafael Jodar -- ATP Shanghai F

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 11:30Z
* Current expected start: 2026-10-18 08:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: 2026-10-18 07:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (MASTERS_1000) · Hard · scheduled 2026-10-18T11:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200221:212588:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alejandro Davidovich Fokina (`KXATPMATCH-26OCT18DAVJOD-DAV`) | 0.43 / 0.45 (13277) | 44.0% | 42.8% | 39.5% | 41.5% [40.0%-44.0%] | 44.4% | 44.3% | 44.3% | MARKETS_AGREE | PASS | -1.2 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Rafael Jodar (`KXATPMATCH-26OCT18DAVJOD-JOD`) | 0.56 / 0.57 (99812) | 56.5% | 57.2% | 60.5% | 58.5% [56.0%-60.0%] | 55.6% | 55.8% | 55.7% | MARKETS_AGREE | PASS | +0.7 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4905.0, B 4261.0; serve-point win A 61.6%, B 37.0%; Elo A 1965.1, B 1993.3; model uncertainty 0.0198
* Form inputs: days since last match A 2, B 1; matches on record A 555, B 116; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose -0.010, surface_dev_tight +0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT18DAVJOD-24` Over 23.5 games: 0.46/0.47 mid 46.5%, model 53.6% (projection_v2.0 (prediction ledger)) -- gap +7.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18DAVJOD-29` Over 28.5 games: 0.27/0.29 mid 28.0%, model 34.2% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18DAVJOD-19` Over 18.5 games: 0.79/0.83 mid 81.0%, model 86.5% (projection_v2.0 (prediction ledger)) -- gap +5.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18DAVJOD-JOD21` Will Rafael Jodar win the Alejandro Davidovich Fokina vs Rafael Jodar match by a set score of 2-1?: 0.22/0.24 mid 23.0%, model 27.1% (projection_v2.0 (prediction ledger)) -- gap +4.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18DAVJOD-JOD5` Will Rafael Jodar win at least 4.5 more games than Alejandro Davidovich Fokina?: 0.25/0.27 mid 26.0%, model 22.1% (projection_v2.0 (prediction ledger)) -- gap -3.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18DAVJOD-DAV2` Will Alejandro Davidovich Fokina win at least 1.5 more games than Rafael Jodar?: 0.37/0.41 mid 39.0%, model 35.8% (projection_v2.0 (prediction ledger)) -- gap -3.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18DAVJOD-JOD20` Will Rafael Jodar win the Alejandro Davidovich Fokina vs Rafael Jodar match by a set score of 2-0?: 0.30/0.36 mid 33.0%, model 30.0% (projection_v2.0 (prediction ledger)) -- gap -3.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18DAVJOD-DAV21` Will Alejandro Davidovich Fokina win the Alejandro Davidovich Fokina vs Rafael Jodar match by a set score of 2-1?: 0.18/0.21 mid 19.5%, model 22.4% (projection_v2.0 (prediction ledger)) -- gap +2.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18DAVJOD-DAV20` Will Alejandro Davidovich Fokina win the Alejandro Davidovich Fokina vs Rafael Jodar match by a set score of 2-0?: 0.20/0.26 mid 23.0%, model 20.4% (projection_v2.0 (prediction ledger)) -- gap -2.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18DAVJOD-1-JOD` Will Rafael Jodar win set 1 in the Alejandro Davidovich Fokina vs Rafael Jodar match: 0.52/0.54 mid 53.0%, model 54.8% (projection_v2.0 (prediction ledger)) -- gap +1.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18DAVJOD-2-JOD` Will Rafael Jodar win set 2 in the Alejandro Davidovich Fokina vs Rafael Jodar match: 0.52/0.55 mid 53.5%, model 54.8% (projection_v2.0 (prediction ledger)) -- gap +1.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18DAVJOD-1-DAV` Will Alejandro Davidovich Fokina win set 1 in the Alejandro Davidovich Fokina vs Rafael Jodar match: 0.44/0.47 mid 45.5%, model 45.2% (projection_v2.0 (prediction ledger)) -- gap -0.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18DAVJOD-2-DAV` Will Alejandro Davidovich Fokina win set 2 in the Alejandro Davidovich Fokina vs Rafael Jodar match: 0.43/0.47 mid 45.0%, model 45.2% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT18DAVJOD-JOD2` Will Rafael Jodar win at least 1.5 more games than Alejandro Davidovich Fokina?: 0.49/0.51 mid 50.0%, model 49.9% (projection_v2.0 (prediction ledger)) -- gap -0.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE

## Nancy Lee vs Saily Prashantkumar Thakkar -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:263658:270052:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nancy Lee (`KXITFWMATCH-26OCT17LEETHA-LEE`) | 0.04 / 0.95 (4) | 49.5% | 77.6% | 77.4% | 65.1% [64.6%-66.6%] | -- | -- | -- | -- | PASS | +28.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Saily Prashantkumar Thakkar (`KXITFWMATCH-26OCT17LEETHA-THA`) | 0.03 / 0.97 (263) | 50.0% | 22.4% | 22.6% | 34.9% [33.4%-35.4%] | -- | -- | -- | -- | PASS | -27.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 73.0, B 301.0; serve-point win A 55.2%, B 50.4%; Elo A 1286.3, B 1183.5; model uncertainty 0.0101
* Form inputs: days since last match A 341, B 173; matches on record A 1, B 11; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT17LEETHA-LEE  (YES = Nancy Lee)
Model: 78%
Kalshi: 50%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Moeka Miyata vs Niyati Hiranandani Bhandari -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17MIYBHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Niyati Hiranandani Bhandari (`KXITFWMATCH-26OCT17MIYBHA-BHA`) | 0.03 / 0.94 (100) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Moeka Miyata (`KXITFWMATCH-26OCT17MIYBHA-MIY`) | 0.03 / 0.97 (263) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Saina Jayesh Vaidya vs Saumrita Jagatdeo Verma -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17VAIVER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Saina Jayesh Vaidya (`KXITFWMATCH-26OCT17VAIVER-VAI`) | 0.03 / 0.97 (385) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Saumrita Jagatdeo Verma (`KXITFWMATCH-26OCT17VAIVER-VER`) | 0.04 / 0.94 (100) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Caitlin Diane Woo vs Violet Apisah -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17WOOAPI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Violet Apisah (`KXITFWMATCH-26OCT17WOOAPI-API`) | 0.03 / 0.97 (285) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Caitlin Diane Woo (`KXITFWMATCH-26OCT17WOOAPI-WOO`) | 0.03 / 0.93 (6) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zi Xuan Yang vs Amodini Naik -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17YANNAI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amodini Naik (`KXITFWMATCH-26OCT17YANNAI-NAI`) | 0.03 / 0.97 (285) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Zi Xuan Yang (`KXITFWMATCH-26OCT17YANNAI-YAN`) | 0.03 / 0.97 (263) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Terence Atmane vs Rinky Hijikata -- ATP Almaty R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208014:209279:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Terence Atmane (`KXATPMATCH-26OCT18ATMHIJ-ATM`) | 0.47 / 0.49 (1697) | 48.0% | 47.1% | 54.9% | 52.9% [48.5%-54.4%] | -- | -- | -- | -- | WATCH | -0.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rinky Hijikata (`KXATPMATCH-26OCT18ATMHIJ-HIJ`) | 0.52 / 0.53 (6164) | 52.5% | 52.8% | 45.1% | 47.1% [45.6%-51.5%] | -- | -- | -- | -- | PASS | +0.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4446.0, B 5282.0; serve-point win A 65.7%, B 33.7%; Elo A 1764.1, B 1794.6; model uncertainty 0.0292
* Form inputs: days since last match A 12, B 10; matches on record A 397, B 434; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.010
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT18ATMHIJ-HIJ21` Will Rinky Hijikata win the Terence Atmane vs Rinky Hijikata match by a set score of 2-1?: 0.02/0.27 mid 14.5%, model 25.9% (projection_v2.0 (prediction ledger)) -- gap +11.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18ATMHIJ-ATM21` Will Terence Atmane win the Terence Atmane vs Rinky Hijikata match by a set score of 2-1?: 0.02/0.26 mid 14.0%, model 24.0% (projection_v2.0 (prediction ledger)) -- gap +10.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18ATMHIJ-19` Over 18.5 games: 0.64/0.99 mid 81.5%, model 91.3% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18ATMHIJ-HIJ20` Will Rinky Hijikata win the Terence Atmane vs Rinky Hijikata match by a set score of 2-0?: 0.02/0.34 mid 18.0%, model 26.9% (projection_v2.0 (prediction ledger)) -- gap +8.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18ATMHIJ-24` Over 23.5 games: 0.45/0.53 mid 49.0%, model 56.4% (projection_v2.0 (prediction ledger)) -- gap +7.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18ATMHIJ-29` Over 28.5 games: 0.13/0.54 mid 33.5%, model 39.2% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18ATMHIJ-ATM20` Will Terence Atmane win the Terence Atmane vs Rinky Hijikata match by a set score of 2-0?: 0.02/0.34 mid 18.0%, model 23.1% (projection_v2.0 (prediction ledger)) -- gap +5.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18ATMHIJ-ATM3` Will Terence Atmane win at least 2.5 more games than Rinky Hijikata?: 0.34/0.39 mid 36.5%, model 31.7% (projection_v2.0 (prediction ledger)) -- gap -4.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ATMHIJ-1-HIJ` Will Rinky Hijikata win set 1 in the Terence Atmane vs Rinky Hijikata match: 0.03/0.94 mid 48.5%, model 51.9% (projection_v2.0 (prediction ledger)) -- gap +3.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ATMHIJ-2-HIJ` Will Rinky Hijikata win set 2 in the Terence Atmane vs Rinky Hijikata match: 0.06/0.95 mid 50.5%, model 51.9% (projection_v2.0 (prediction ledger)) -- gap +1.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ATMHIJ-2-ATM` Will Terence Atmane win set 2 in the Terence Atmane vs Rinky Hijikata match: 0.02/0.92 mid 47.0%, model 48.1% (projection_v2.0 (prediction ledger)) -- gap +1.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT18ATMHIJ-HIJ2` Will Rinky Hijikata win at least 1.5 more games than Terence Atmane?: 0.42/0.46 mid 44.0%, model 44.8% (projection_v2.0 (prediction ledger)) -- gap +0.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ATMHIJ-1-ATM` Will Terence Atmane win set 1 in the Terence Atmane vs Rinky Hijikata match: 0.03/0.94 mid 48.5%, model 48.1% (projection_v2.0 (prediction ledger)) -- gap -0.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## N. Sriram Balaji / Evan King vs Anirudh Chandrasekar / Ray Ho -- ATP Almaty R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18BALKINCHARAY:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N. Sriram Balaji / Evan King (`KXATPDOUBLES-26OCT18BALKINCHARAY-BALKIN`) | 0.06 / 0.90 (10) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anirudh Chandrasekar / Ray Ho (`KXATPDOUBLES-26OCT18BALKINCHARAY-CHARAY`) | 0.06 / 0.90 (10) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Mattia Bellucci vs Tomas Martin Etcheverry -- ATP Almaty R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144869:208233:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mattia Bellucci (`KXATPMATCH-26OCT18BELETC-BEL`) | 0.50 / 0.52 (6397) | 51.0% | 57.8% | 48.5% | 50.0% [49.5%-51.5%] | -- | -- | -- | -- | PASS | +6.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tomas Martin Etcheverry (`KXATPMATCH-26OCT18BELETC-ETC`) | 0.48 / 0.50 (502) | 49.0% | 42.2% | 51.4% | 50.0% [48.5%-50.5%] | -- | -- | -- | -- | PASS | -6.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4439.0, B 5437.0; serve-point win A 67.4%, B 34.3%; Elo A 1795.9, B 1757.3; model uncertainty 0.0097
* Form inputs: days since last match A 10, B 7; matches on record A 394, B 635; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.000, surface_dev_loose +0.010, surface_dev_tight -0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT18BELETC-20` Over 19.5 games: 0.53/0.94 mid 73.5%, model 84.8% (projection_v2.0 (prediction ledger)) -- gap +11.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18BELETC-25` Over 24.5 games: 0.43/0.49 mid 46.0%, model 55.5% (projection_v2.0 (prediction ledger)) -- gap +9.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18BELETC-BEL21` Will Mattia Bellucci win the Mattia Bellucci vs Tomas Martin Etcheverry match by a set score of 2-1?: 0.08/0.29 mid 18.5%, model 27.3% (projection_v2.0 (prediction ledger)) -- gap +8.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18BELETC-ETC21` Will Tomas Martin Etcheverry win the Mattia Bellucci vs Tomas Martin Etcheverry match by a set score of 2-1?: 0.01/0.26 mid 13.5%, model 22.1% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18BELETC-BEL2` Will Mattia Bellucci win at least 1.5 more games than Tomas Martin Etcheverry?: 0.37/0.46 mid 41.5%, model 49.7% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BELETC-1-BEL` Will Mattia Bellucci win set 1 in the Mattia Bellucci vs Tomas Martin Etcheverry match: 0.03/0.92 mid 47.5%, model 55.2% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT18BELETC-ETC2` Will Tomas Martin Etcheverry win at least 1.5 more games than Mattia Bellucci?: 0.37/0.46 mid 41.5%, model 34.3% (projection_v2.0 (prediction ledger)) -- gap -7.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BELETC-2-BEL` Will Mattia Bellucci win set 2 in the Mattia Bellucci vs Tomas Martin Etcheverry match: 0.01/0.96 mid 48.5%, model 55.2% (projection_v2.0 (prediction ledger)) -- gap +6.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18BELETC-30` Over 29.5 games: 0.12/0.46 mid 29.0%, model 35.2% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BELETC-1-ETC` Will Tomas Martin Etcheverry win set 1 in the Mattia Bellucci vs Tomas Martin Etcheverry match: 0.06/0.94 mid 50.0%, model 44.8% (projection_v2.0 (prediction ledger)) -- gap -5.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BELETC-2-ETC` Will Tomas Martin Etcheverry win set 2 in the Mattia Bellucci vs Tomas Martin Etcheverry match: 0.02/0.96 mid 49.0%, model 44.8% (projection_v2.0 (prediction ledger)) -- gap -4.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18BELETC-BEL20` Will Mattia Bellucci win the Mattia Bellucci vs Tomas Martin Etcheverry match by a set score of 2-0?: 0.21/0.44 mid 32.5%, model 30.5% (projection_v2.0 (prediction ledger)) -- gap -2.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18BELETC-ETC20` Will Tomas Martin Etcheverry win the Mattia Bellucci vs Tomas Martin Etcheverry match by a set score of 2-0?: 0.01/0.36 mid 18.5%, model 20.1% (projection_v2.0 (prediction ledger)) -- gap +1.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Luciano Darderi / Tomas Martin Etcheverry vs Jason Kubler / John Peers -- ATP Almaty R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18DARETCKUBPEE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luciano Darderi / Tomas Martin Etcheverry (`KXATPDOUBLES-26OCT18DARETCKUBPEE-DARETC`) | 0.20 / 0.76 (4) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jason Kubler / John Peers (`KXATPDOUBLES-26OCT18DARETCKUBPEE-KUBPEE`) | 0.18 / 0.82 (11) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alexander Donski / Filip Pieczonka vs Arthur Reymond / Luca Sanchez -- ATP Almaty R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18DONPIEREYSAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Donski / Filip Pieczonka (`KXATPDOUBLES-26OCT18DONPIEREYSAN-DONPIE`) | 0.06 / 0.89 (5) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arthur Reymond / Luca Sanchez (`KXATPDOUBLES-26OCT18DONPIEREYSAN-REYSAN`) | 0.07 / 0.89 (5) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sander Gille / Sem Verbeek vs Yuki Bhambri / Ryan Seggerman -- ATP Almaty R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18GILVERBHASEG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuki Bhambri / Ryan Seggerman (`KXATPDOUBLES-26OCT18GILVERBHASEG-BHASEG`) | 0.06 / 0.90 (10) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sander Gille / Sem Verbeek (`KXATPDOUBLES-26OCT18GILVERBHASEG-GILVER`) | 0.06 / 0.90 (10) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Rinky Hijikata / Adam Walton vs Alexander Bublik / Zangar Nurlanuly -- ATP Almaty R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18HIJWALBUBNUR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Bublik / Zangar Nurlanuly (`KXATPDOUBLES-26OCT18HIJWALBUBNUR-BUBNUR`) | 0.07 / 0.89 (5) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rinky Hijikata / Adam Walton (`KXATPDOUBLES-26OCT18HIJWALBUBNUR-HIJWAL`) | 0.07 / 0.89 (5) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Miomir Kecmanovic vs James Duckworth -- ATP Almaty R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105902:200175:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| James Duckworth (`KXATPMATCH-26OCT18KECDUC-DUC`) | 0.39 / 0.40 (70) | 39.5% | 37.7% | 45.6% | 45.1% [45.1%-45.6%] | -- | -- | -- | -- | SHADOW_BET | -1.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Miomir Kecmanovic (`KXATPMATCH-26OCT18KECDUC-KEC`) | 0.57 / 0.60 (100) | 58.5% | 62.3% | 54.4% | 54.9% [54.4%-54.9%] | -- | -- | -- | -- | PASS | +3.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5396.0, B 5242.0; serve-point win A 67.4%, B 35.1%; Elo A 1788.4, B 1745.5; model uncertainty 0.0025
* Form inputs: days since last match A 10, B 9; matches on record A 606, B 896; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT18KECDUC-20` Over 19.5 games: 0.01/0.99 mid 50.0%, model 83.5% (projection_v2.0 (prediction ledger)) -- gap +33.5 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18KECDUC-KEC21` Will Miomir Kecmanovic win the Miomir Kecmanovic vs James Duckworth match by a set score of 2-1?: 0.02/0.29 mid 15.5%, model 28.3% (projection_v2.0 (prediction ledger)) -- gap +12.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18KECDUC-KEC20` Will Miomir Kecmanovic win the Miomir Kecmanovic vs James Duckworth match by a set score of 2-0?: 0.01/0.43 mid 22.0%, model 34.0% (projection_v2.0 (prediction ledger)) -- gap +12.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18KECDUC-2-KEC` Will Miomir Kecmanovic win set 2 in the Miomir Kecmanovic vs James Duckworth match: 0.02/0.95 mid 48.5%, model 58.3% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18KECDUC-1-KEC` Will Miomir Kecmanovic win set 1 in the Miomir Kecmanovic vs James Duckworth match: 0.06/0.92 mid 49.0%, model 58.3% (projection_v2.0 (prediction ledger)) -- gap +9.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18KECDUC-DUC21` Will James Duckworth win the Miomir Kecmanovic vs James Duckworth match by a set score of 2-1?: 0.02/0.23 mid 12.5%, model 20.3% (projection_v2.0 (prediction ledger)) -- gap +7.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18KECDUC-1-DUC` Will James Duckworth win set 1 in the Miomir Kecmanovic vs James Duckworth match: 0.06/0.92 mid 49.0%, model 41.7% (projection_v2.0 (prediction ledger)) -- gap -7.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18KECDUC-2-DUC` Will James Duckworth win set 2 in the Miomir Kecmanovic vs James Duckworth match: 0.02/0.95 mid 48.5%, model 41.7% (projection_v2.0 (prediction ledger)) -- gap -6.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18KECDUC-25` Over 24.5 games: 0.45/0.51 mid 48.0%, model 54.2% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18KECDUC-DUC20` Will James Duckworth win the Miomir Kecmanovic vs James Duckworth match by a set score of 2-0?: 0.02/0.26 mid 14.0%, model 17.4% (projection_v2.0 (prediction ledger)) -- gap +3.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18KECDUC-30` Over 29.5 games: 0.10/0.51 mid 30.5%, model 33.8% (projection_v2.0 (prediction ledger)) -- gap +3.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18KECDUC-DUC2` Will James Duckworth win at least 1.5 more games than Miomir Kecmanovic?: 0.30/0.36 mid 33.0%, model 30.2% (projection_v2.0 (prediction ledger)) -- gap -2.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18KECDUC-KEC2` Will Miomir Kecmanovic win at least 1.5 more games than James Duckworth?: 0.51/0.54 mid 52.5%, model 54.4% (projection_v2.0 (prediction ledger)) -- gap +1.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18KECDUC-KEC5` Will Miomir Kecmanovic win at least 4.5 more games than James Duckworth?: 0.15/0.22 mid 18.5%, model 20.3% (projection_v2.0 (prediction ledger)) -- gap +1.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nathaniel Lammons / Jackson Withrow vs Jakob Schnaitter / Mark Wallner -- ATP Almaty R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18LAMWITSCHWAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nathaniel Lammons / Jackson Withrow (`KXATPDOUBLES-26OCT18LAMWITSCHWAL-LAMWIT`) | 0.47 / 0.51 (150) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jakob Schnaitter / Mark Wallner (`KXATPDOUBLES-26OCT18LAMWITSCHWAL-SCHWAL`) | 0.48 / 0.52 (350) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Adrian Mannarino vs Aleksandar Vukic -- ATP Almaty R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105173:126846:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Mannarino (`KXATPMATCH-26OCT18MANVUK-MAN`) | 0.63 / 0.64 (149) | 63.5% | 48.8% | 57.3% | 56.3% [55.9%-57.3%] | -- | -- | -- | -- | PASS | -14.7 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aleksandar Vukic (`KXATPMATCH-26OCT18MANVUK-VUK`) | 0.35 / 0.37 (1213) | 36.0% | 51.2% | 42.7% | 43.7% [42.7%-44.1%] | -- | -- | -- | -- | SHADOW_BET | +15.2 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4276.0, B 4441.0; serve-point win A 65.8%, B 33.9%; Elo A 1772.8, B 1736.9; model uncertainty 0.0071
* Form inputs: days since last match A 6, B 11; matches on record A 1273, B 591; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT18MANVUK-VUK  (YES = Aleksandar Vukic)
Model: 51%
Kalshi: 36%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, UNKNOWN
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight +0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT18MANVUK-19` Over 18.5 games: 0.01/0.99 mid 50.0%, model 91.2% (projection_v2.0 (prediction ledger)) -- gap +41.2 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18MANVUK-MAN2` Will Adrian Mannarino win at least 1.5 more games than Aleksandar Vukic?: 0.53/0.59 mid 56.0%, model 40.9% (projection_v2.0 (prediction ledger)) -- gap -15.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18MANVUK-VUK21` Will Aleksandar Vukic win the Adrian Mannarino vs Aleksandar Vukic match by a set score of 2-1?: 0.02/0.22 mid 12.0%, model 25.4% (projection_v2.0 (prediction ledger)) -- gap +13.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18MANVUK-VUK20` Will Aleksandar Vukic win the Adrian Mannarino vs Aleksandar Vukic match by a set score of 2-0?: 0.02/0.24 mid 13.0%, model 25.8% (projection_v2.0 (prediction ledger)) -- gap +12.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18MANVUK-MAN5` Will Adrian Mannarino win at least 4.5 more games than Aleksandar Vukic?: 0.23/0.28 mid 25.5%, model 13.4% (projection_v2.0 (prediction ledger)) -- gap -12.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18MANVUK-VUK2` Will Aleksandar Vukic win at least 1.5 more games than Adrian Mannarino?: 0.28/0.36 mid 32.0%, model 43.1% (projection_v2.0 (prediction ledger)) -- gap +11.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18MANVUK-29` Over 28.5 games: 0.01/0.99 mid 50.0%, model 39.1% (projection_v2.0 (prediction ledger)) -- gap -10.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18MANVUK-MAN21` Will Adrian Mannarino win the Adrian Mannarino vs Aleksandar Vukic match by a set score of 2-1?: 0.02/0.29 mid 15.5%, model 24.6% (projection_v2.0 (prediction ledger)) -- gap +9.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18MANVUK-24` Over 23.5 games: 0.45/0.51 mid 48.0%, model 56.4% (projection_v2.0 (prediction ledger)) -- gap +8.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MANVUK-1-VUK` Will Aleksandar Vukic win set 1 in the Adrian Mannarino vs Aleksandar Vukic match: 0.03/0.83 mid 43.0%, model 50.8% (projection_v2.0 (prediction ledger)) -- gap +7.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MANVUK-2-VUK` Will Aleksandar Vukic win set 2 in the Adrian Mannarino vs Aleksandar Vukic match: 0.03/0.94 mid 48.5%, model 50.8% (projection_v2.0 (prediction ledger)) -- gap +2.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18MANVUK-MAN20` Will Adrian Mannarino win the Adrian Mannarino vs Aleksandar Vukic match by a set score of 2-0?: 0.01/0.46 mid 23.5%, model 24.2% (projection_v2.0 (prediction ledger)) -- gap +0.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MANVUK-1-MAN` Will Adrian Mannarino win set 1 in the Adrian Mannarino vs Aleksandar Vukic match: 0.03/0.94 mid 48.5%, model 49.2% (projection_v2.0 (prediction ledger)) -- gap +0.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MANVUK-2-MAN` Will Adrian Mannarino win set 2 in the Adrian Mannarino vs Aleksandar Vukic match: 0.03/0.95 mid 49.0%, model 49.2% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Fabian Marozsan vs Timofey Skatov -- ATP Almaty R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:206681:207608:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fabian Marozsan (`KXATPMATCH-26OCT18MARSKA-MAR`) | 0.76 / 0.79 (6211) | 77.5% | 73.8% | 70.9% | 72.6% [71.7%-73.8%] | -- | -- | -- | -- | PASS | -3.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Timofey Skatov (`KXATPMATCH-26OCT18MARSKA-SKA`) | 0.21 / 0.22 (8) | 21.5% | 26.2% | 29.1% | 27.4% [26.2%-28.3%] | -- | -- | -- | -- | PASS | +4.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4574.0, B 4414.0; serve-point win A 66.3%, B 38.8%; Elo A 1778.2, B 1562.5; model uncertainty 0.0103
* Form inputs: days since last match A 9, B 11; matches on record A 439, B 455; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.004, surface_dev_loose +0.012, surface_dev_tight -0.008
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18MARSKA-2-MAR` Will Fabian Marozsan win set 2 in the Fabian Marozsan vs Timofey Skatov match: 0.01/0.96 mid 48.5%, model 66.5% (projection_v2.0 (prediction ledger)) -- gap +18.0 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MARSKA-1-MAR` Will Fabian Marozsan win set 1 in the Fabian Marozsan vs Timofey Skatov match: 0.04/0.94 mid 49.0%, model 66.5% (projection_v2.0 (prediction ledger)) -- gap +17.5 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MARSKA-2-SKA` Will Timofey Skatov win set 2 in the Fabian Marozsan vs Timofey Skatov match: 0.01/0.96 mid 48.5%, model 33.5% (projection_v2.0 (prediction ledger)) -- gap -15.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18MARSKA-MAR21` Will Fabian Marozsan win the Fabian Marozsan vs Timofey Skatov match by a set score of 2-1?: 0.01/0.29 mid 15.0%, model 29.6% (projection_v2.0 (prediction ledger)) -- gap +14.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18MARSKA-MAR20` Will Fabian Marozsan win the Fabian Marozsan vs Timofey Skatov match by a set score of 2-0?: 0.01/0.64 mid 32.5%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18MARSKA-SKA20` Will Timofey Skatov win the Fabian Marozsan vs Timofey Skatov match by a set score of 2-0?: 0.01/0.44 mid 22.5%, model 11.2% (projection_v2.0 (prediction ledger)) -- gap -11.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18MARSKA-SKA21` Will Timofey Skatov win the Fabian Marozsan vs Timofey Skatov match by a set score of 2-1?: 0.01/0.44 mid 22.5%, model 14.9% (projection_v2.0 (prediction ledger)) -- gap -7.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MARSKA-1-SKA` Will Timofey Skatov win set 1 in the Fabian Marozsan vs Timofey Skatov match: 0.03/0.75 mid 39.0%, model 33.5% (projection_v2.0 (prediction ledger)) -- gap -5.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lucas Miedler / Neil Oberleitner vs Francisco Cabral / James Tracy -- ATP Shanghai F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18MIEOBECABTRA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francisco Cabral / James Tracy (`KXATPDOUBLES-26OCT18MIEOBECABTRA-CABTRA`) | 0.47 / 0.51 (1001) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lucas Miedler / Neil Oberleitner (`KXATPDOUBLES-26OCT18MIEOBECABTRA-MIEOBE`) | 0.49 / 0.51 (24) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Lucas Miedler / Neil Oberleitner vs Amir Omarkhanov / Beibit Zhukayev -- ATP Almaty R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18MIEOBEOMAZHU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucas Miedler / Neil Oberleitner (`KXATPDOUBLES-26OCT18MIEOBEOMAZHU-MIEOBE`) | 0.07 / 0.90 (10) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Amir Omarkhanov / Beibit Zhukayev (`KXATPDOUBLES-26OCT18MIEOBEOMAZHU-OMAZHU`) | 0.06 / 0.89 (5) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Zangar Nurlanuly vs Tomas Machac -- ATP Almaty R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207830:tml:N0GN:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tomas Machac (`KXATPMATCH-26OCT18NURMAC-MAC`) | 0.95 / 0.96 (1796) | 95.5% | 98.2% | 88.3% | 96.2% [94.8%-97.6%] | -- | -- | -- | -- | PASS | +2.6 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zangar Nurlanuly (`KXATPMATCH-26OCT18NURMAC-NUR`) | 0.05 / 0.06 (6724) | 5.5% | 1.8% | 11.7% | 3.8% [2.4%-5.2%] | -- | -- | -- | -- | PASS | -3.6 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 195.0, B 3439.0; serve-point win A 54.0%, B 29.4%; Elo A 1329.8, B 1926.2; model uncertainty 0.014
* Form inputs: days since last match A 68, B 8; matches on record A 4, B 440; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.014, surface_dev_loose +0.000, surface_dev_tight -0.001
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18NURMAC-1-MAC` Will Tomas Machac win set 1 in the Zangar Nurlanuly vs Tomas Machac match: 0.03/0.92 mid 47.5%, model 91.9% (projection_v2.0 (prediction ledger)) -- gap +44.4 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT18NURMAC-2-MAC` Will Tomas Machac win set 2 in the Zangar Nurlanuly vs Tomas Machac match: 0.01/0.96 mid 48.5%, model 91.9% (projection_v2.0 (prediction ledger)) -- gap +43.4 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT18NURMAC-2-NUR` Will Zangar Nurlanuly win set 2 in the Zangar Nurlanuly vs Tomas Machac match: 0.02/0.96 mid 49.0%, model 8.1% (projection_v2.0 (prediction ledger)) -- gap -40.9 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPEXACTMATCH-26OCT18NURMAC-MAC20` Will Tomas Machac win the Zangar Nurlanuly vs Tomas Machac match by a set score of 2-0?: 0.01/0.91 mid 46.0%, model 84.5% (projection_v2.0 (prediction ledger)) -- gap +38.5 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data POOR
  * `KXATPSETWINNER-26OCT18NURMAC-1-NUR` Will Zangar Nurlanuly win set 1 in the Zangar Nurlanuly vs Tomas Machac match: 0.04/0.85 mid 44.5%, model 8.1% (projection_v2.0 (prediction ledger)) -- gap -36.4 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPEXACTMATCH-26OCT18NURMAC-MAC21` Will Tomas Machac win the Zangar Nurlanuly vs Tomas Machac match by a set score of 2-1?: 0.01/0.44 mid 22.5%, model 13.6% (projection_v2.0 (prediction ledger)) -- gap -8.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
* Warnings: BET_BLOCKED_START_STATUS; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jean-Julien Rojer / Theodore Winegar vs Facundo Diaz Acosta / Thiago Agustin Tirante -- ATP Almaty R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18ROJWINDIATIR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Facundo Diaz Acosta / Thiago Agustin Tirante (`KXATPDOUBLES-26OCT18ROJWINDIATIR-DIATIR`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jean-Julien Rojer / Theodore Winegar (`KXATPDOUBLES-26OCT18ROJWINDIATIR-ROJWIN`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Thiago Agustin Tirante vs Facundo Diaz Acosta -- ATP Almaty R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:202058:207680:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Facundo Diaz Acosta (`KXATPMATCH-26OCT18TIRDIA-DIA`) | 0.26 / 0.28 (887) | 27.0% | 39.5% | 46.5% | 43.6% [39.2%-45.5%] | -- | -- | -- | -- | SHADOW_BET | +12.5 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Thiago Agustin Tirante (`KXATPMATCH-26OCT18TIRDIA-TIR`) | 0.72 / 0.74 (1049) | 73.0% | 60.5% | 53.5% | 56.4% [54.5%-60.8%] | -- | -- | -- | -- | PASS | -12.5 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4745.0, B 5003.0; serve-point win A 65.1%, B 37.0%; Elo A 1741.7, B 1628.9; model uncertainty 0.0317
* Form inputs: days since last match A 7, B 9; matches on record A 449, B 449; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.010, surface_dev_loose +0.029, surface_dev_tight -0.020
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT18TIRDIA-TIR4` Will Thiago Agustin Tirante win at least 3.5 more games than Facundo Diaz Acosta?: 0.48/0.53 mid 50.5%, model 34.6% (projection_v2.0 (prediction ledger)) -- gap -15.9 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18TIRDIA-DIA2` Will Facundo Diaz Acosta win at least 1.5 more games than Thiago Agustin Tirante?: 0.15/0.24 mid 19.5%, model 32.3% (projection_v2.0 (prediction ledger)) -- gap +12.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18TIRDIA-TIR21` Will Thiago Agustin Tirante win the Thiago Agustin Tirante vs Facundo Diaz Acosta match by a set score of 2-1?: 0.02/0.29 mid 15.5%, model 28.0% (projection_v2.0 (prediction ledger)) -- gap +12.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18TIRDIA-23` Over 22.5 games: 0.46/0.51 mid 48.5%, model 60.6% (projection_v2.0 (prediction ledger)) -- gap +12.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18TIRDIA-DIA21` Will Facundo Diaz Acosta win the Thiago Agustin Tirante vs Facundo Diaz Acosta match by a set score of 2-1?: 0.02/0.19 mid 10.5%, model 21.0% (projection_v2.0 (prediction ledger)) -- gap +10.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18TIRDIA-18` Over 17.5 games: 0.67/0.99 mid 83.0%, model 93.5% (projection_v2.0 (prediction ledger)) -- gap +10.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18TIRDIA-28` Over 27.5 games: 0.11/0.52 mid 31.5%, model 40.3% (projection_v2.0 (prediction ledger)) -- gap +8.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18TIRDIA-1-TIR` Will Thiago Agustin Tirante win set 1 in the Thiago Agustin Tirante vs Facundo Diaz Acosta match: 0.03/0.94 mid 48.5%, model 57.1% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18TIRDIA-2-TIR` Will Thiago Agustin Tirante win set 2 in the Thiago Agustin Tirante vs Facundo Diaz Acosta match: 0.01/0.96 mid 48.5%, model 57.1% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18TIRDIA-1-DIA` Will Facundo Diaz Acosta win set 1 in the Thiago Agustin Tirante vs Facundo Diaz Acosta match: 0.03/0.94 mid 48.5%, model 42.9% (projection_v2.0 (prediction ledger)) -- gap -5.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18TIRDIA-2-DIA` Will Facundo Diaz Acosta win set 2 in the Thiago Agustin Tirante vs Facundo Diaz Acosta match: 0.01/0.96 mid 48.5%, model 42.9% (projection_v2.0 (prediction ledger)) -- gap -5.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18TIRDIA-TIR20` Will Thiago Agustin Tirante win the Thiago Agustin Tirante vs Facundo Diaz Acosta match by a set score of 2-0?: 0.02/0.53 mid 27.5%, model 32.6% (projection_v2.0 (prediction ledger)) -- gap +5.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18TIRDIA-DIA20` Will Facundo Diaz Acosta win the Thiago Agustin Tirante vs Facundo Diaz Acosta match by a set score of 2-0?: 0.02/0.30 mid 16.0%, model 18.4% (projection_v2.0 (prediction ledger)) -- gap +2.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Stefanos Tsitsipas vs Aleksandar Kovacevic -- ATP Almaty R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126774:206499:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aleksandar Kovacevic (`KXATPMATCH-26OCT18TSIKOV-KOV`) | 0.22 / 0.25 (7135) | 23.5% | 27.0% | 32.6% | 30.5% [23.5%-35.1%] | -- | -- | -- | -- | WATCH | +3.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Stefanos Tsitsipas (`KXATPMATCH-26OCT18TSIKOV-TSI`) | 0.73 / 0.77 (132) | 75.0% | 73.0% | 67.4% | 69.5% [64.9%-76.5%] | -- | -- | -- | -- | PASS | -2.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5084.0, B 4809.0; serve-point win A 73.1%, B 32.2%; Elo A 1952.1, B 1756.9; model uncertainty 0.0581
* Form inputs: days since last match A 3, B 10; matches on record A 801, B 399; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.039, surface_pool_high -0.046, surface_dev_loose -0.008, surface_dev_tight +0.013
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT18TSIKOV-18` Over 17.5 games: 0.01/0.99 mid 50.0%, model 97.1% (projection_v2.0 (prediction ledger)) -- gap +47.1 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18TSIKOV-1-TSI` Will Stefanos Tsitsipas win set 1 in the Stefanos Tsitsipas vs Aleksandar Kovacevic match: 0.03/0.94 mid 48.5%, model 65.9% (projection_v2.0 (prediction ledger)) -- gap +17.4 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18TSIKOV-2-TSI` Will Stefanos Tsitsipas win set 2 in the Stefanos Tsitsipas vs Aleksandar Kovacevic match: 0.03/0.95 mid 49.0%, model 65.9% (projection_v2.0 (prediction ledger)) -- gap +16.9 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18TSIKOV-2-KOV` Will Aleksandar Kovacevic win set 2 in the Stefanos Tsitsipas vs Aleksandar Kovacevic match: 0.03/0.95 mid 49.0%, model 34.1% (projection_v2.0 (prediction ledger)) -- gap -14.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18TSIKOV-TSI20` Will Stefanos Tsitsipas win the Stefanos Tsitsipas vs Aleksandar Kovacevic match by a set score of 2-0?: 0.01/0.57 mid 29.0%, model 43.4% (projection_v2.0 (prediction ledger)) -- gap +14.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18TSIKOV-23` Over 22.5 games: 0.49/0.55 mid 52.0%, model 66.1% (projection_v2.0 (prediction ledger)) -- gap +14.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18TSIKOV-TSI21` Will Stefanos Tsitsipas win the Stefanos Tsitsipas vs Aleksandar Kovacevic match by a set score of 2-1?: 0.01/0.31 mid 16.0%, model 29.6% (projection_v2.0 (prediction ledger)) -- gap +13.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18TSIKOV-TSI4` Will Stefanos Tsitsipas win at least 3.5 more games than Aleksandar Kovacevic?: 0.46/0.52 mid 49.0%, model 35.5% (projection_v2.0 (prediction ledger)) -- gap -13.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18TSIKOV-KOV20` Will Aleksandar Kovacevic win the Stefanos Tsitsipas vs Aleksandar Kovacevic match by a set score of 2-0?: 0.01/0.44 mid 22.5%, model 11.7% (projection_v2.0 (prediction ledger)) -- gap -10.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18TSIKOV-28` Over 27.5 games: 0.26/0.39 mid 32.5%, model 42.2% (projection_v2.0 (prediction ledger)) -- gap +9.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18TSIKOV-1-KOV` Will Aleksandar Kovacevic win set 1 in the Stefanos Tsitsipas vs Aleksandar Kovacevic match: 0.03/0.83 mid 43.0%, model 34.1% (projection_v2.0 (prediction ledger)) -- gap -8.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18TSIKOV-KOV21` Will Aleksandar Kovacevic win the Stefanos Tsitsipas vs Aleksandar Kovacevic match by a set score of 2-1?: 0.01/0.44 mid 22.5%, model 15.3% (projection_v2.0 (prediction ledger)) -- gap -7.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18TSIKOV-KOV2` Will Aleksandar Kovacevic win at least 1.5 more games than Stefanos Tsitsipas?: 0.09/0.18 mid 13.5%, model 19.7% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Yanan Hou vs chengwei Han -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:261066:264152:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| chengwei Han (`KXITFWMATCH-26OCT17HOUHAN-HAN`) | 0.04 / 0.26 (6110) | 15.0% | 6.5% | 43.1% | 22.7% [21.1%-23.5%] | -- | -- | -- | -- | PASS | -8.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yanan Hou (`KXITFWMATCH-26OCT17HOUHAN-HOU`) | 0.74 / 0.95 (66) | 84.5% | 93.5% | 56.9% | 77.3% [76.5%-78.9%] | -- | -- | -- | -- | PASS | +9.0 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 995.0, B 40.0; serve-point win A 58.8%, B 52.6%; Elo A 1360.3, B 1141.0; model uncertainty 0.0119
* Form inputs: days since last match A 173, B 194; matches on record A 120, B 15; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.016, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zijun Jiang vs Zihan Yang -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17JIAYAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zijun Jiang (`KXITFWMATCH-26OCT17JIAYAN-JIA`) | 0.23 / 0.94 (74) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Zihan Yang (`KXITFWMATCH-26OCT17JIAYAN-YAN`) | 0.03 / 0.28 (22) | 15.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xichen Zhao vs WENFEI YU -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:252494:264184:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| WENFEI YU (`KXITFWMATCH-26OCT17ZHAYUX-YUX`) | 0.04 / 0.97 (285) | 50.5% | 65.6% | 64.7% | 59.6% [56.4%-61.1%] | -- | -- | -- | -- | PASS | +15.1 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Xichen Zhao (`KXITFWMATCH-26OCT17ZHAYUX-ZHA`) | 0.03 / 0.87 (39) | 45.0% | 34.4% | 35.3% | 40.4% [38.9%-43.6%] | -- | -- | -- | -- | PASS | -10.6 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 896.0, B 238.0; serve-point win A 49.6%, B 47.4%; Elo A 1293.3, B 1351.8; model uncertainty 0.0236
* Form inputs: days since last match A 173, B 173; matches on record A 133, B 35; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT17ZHAYUX-YUX  (YES = WENFEI YU)
Model: 66%
Kalshi: 50%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.015, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Samir Banerjee vs Karan Singh -- M25 Solapur F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209079:210000:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Samir Banerjee (`KXITFMATCH-26OCT17BANSIN-BAN`) | 0.64 / 0.65 (71) | 64.5% | 72.2% | 78.4% | 68.5% [66.5%-70.0%] | 65.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.7 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Karan Singh (`KXITFMATCH-26OCT17BANSIN-SIN`) | 0.31 / 0.34 (43) | 32.5% | 27.8% | 21.6% | 31.4% [30.0%-33.5%] | 34.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.7 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 167.0, B 1139.0; serve-point win A 64.4%, B 40.2%; Elo A 1460.8, B 1336.3; model uncertainty 0.0173
* Form inputs: days since last match A 705, B 82; matches on record A 74, B 178; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yaroslav Demin vs Alexander Binda -- ATP Challenger Guangzhou Nansha Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-18T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18DEMBIN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Binda (`KXATPCHALLENGERMATCH-26OCT18DEMBIN-BIN`) | 0.47 / 0.51 (250) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yaroslav Demin (`KXATPCHALLENGERMATCH-26OCT18DEMBIN-DEM`) | 0.48 / 0.50 (69) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Mitsuki Wei Kang Leong vs Fumin Jiang -- ATP Challenger Guangzhou Nansha Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-18T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18LEOJIA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fumin Jiang (`KXATPCHALLENGERMATCH-26OCT18LEOJIA-JIA`) | 0.05 / 0.08 (490) | 6.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mitsuki Wei Kang Leong (`KXATPCHALLENGERMATCH-26OCT18LEOJIA-LEO`) | 0.91 / 0.93 (40) | 92.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Egor Pleshivtsev vs Luca Castelnuovo -- ATP Challenger Guangzhou Nansha Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-18T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132573:212574:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luca Castelnuovo (`KXATPCHALLENGERMATCH-26OCT18PLECAS-CAS`) | 0.66 / 0.70 (322) | 68.0% | 83.7% | 50.0% | 75.5% [74.9%-75.5%] | -- | 67.7% | -- | INSUFFICIENT_INPUTS | PASS | +15.7 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Egor Pleshivtsev (`KXATPCHALLENGERMATCH-26OCT18PLECAS-PLE`) | 0.30 / 0.33 (15) | 31.5% | 16.3% | 50.0% | 24.5% [24.5%-25.1%] | -- | 32.3% | -- | INSUFFICIENT_INPUTS | PASS | -15.2 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 1351.0; serve-point win A 61.2%, B 30.8%; Elo A 1197.0, B 1392.7; model uncertainty 0.0034
* Form inputs: days since last match A 670, B 25; matches on record A 4, B 297; data quality F

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT18PLECAS-CAS  (YES = Luca Castelnuovo)
Model: 84%
Kalshi: 68%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.001, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Aleksandr Shevchenko vs Stefanos Sakellaridis -- ATP Almaty Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 13:00Z
* Current expected start: 2026-10-18 10:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: 2026-10-18 09:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207686:208852:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefanos Sakellaridis (`KXATPMATCH-26OCT18SHESAK-SAK`) | 0.35 / 0.36 (100) | 35.5% | 42.4% | 54.9% | 48.5% [44.1%-51.5%] | 37.7% | 35.2% | 37.7% | KALSHI_LONE_OUTLIER | PASS | +6.9 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | AMBIGUOUS |
| Aleksandr Shevchenko (`KXATPMATCH-26OCT18SHESAK-SHE`) | 0.64 / 0.65 (1988) | 64.5% | 57.6% | 45.1% | 51.5% [48.5%-55.9%] | 62.3% | 64.9% | 62.3% | KALSHI_LONE_OUTLIER | PASS | -6.9 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | AMBIGUOUS |

* Serve evidence (points): A 4772.0, B 3408.0; serve-point win A 66.6%, B 34.9%; Elo A 1712.4, B 1606.8; model uncertainty 0.0366
* Form inputs: days since last match A 23, B 12; matches on record A 477, B 321; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.005, surface_dev_loose -0.015, surface_dev_tight +0.015
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT18SHESAK-19` Over 18.5 games: 0.38/0.98 mid 68.0%, model 90.7% (projection_v2.0 (prediction ledger)) -- gap +22.7 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT18SHESAK-SHE6` Will Alexander Shevchenko win at least 5.5 more games than Stefanos Sakellaridis?: 0.05/0.55 mid 30.0%, model 9.0% (projection_v2.0 (prediction ledger)) -- gap -21.0 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18SHESAK-24` Over 23.5 games: 0.43/0.45 mid 44.0%, model 55.7% (projection_v2.0 (prediction ledger)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18SHESAK-29` Over 28.5 games: 0.06/0.49 mid 27.5%, model 38.5% (projection_v2.0 (prediction ledger)) -- gap +11.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18SHESAK-SAK21` Will Stefanos Sakellaridis win the Alexander Shevchenko vs Stefanos Sakellaridis match by a set score of 2-1?: 0.02/0.21 mid 11.5%, model 22.2% (projection_v2.0 (prediction ledger)) -- gap +10.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18SHESAK-SHE21` Will Alexander Shevchenko win the Alexander Shevchenko vs Stefanos Sakellaridis match by a set score of 2-1?: 0.07/0.29 mid 18.0%, model 27.3% (projection_v2.0 (prediction ledger)) -- gap +9.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18SHESAK-2-SAK` Will Stefanos Sakellaridis win set 2 in the Alexander Shevchenko vs Stefanos Sakellaridis match: 0.31/0.41 mid 36.0%, model 44.9% (projection_v2.0 (prediction ledger)) -- gap +8.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT18SHESAK-SHE3` Will Alexander Shevchenko win at least 2.5 more games than Stefanos Sakellaridis?: 0.49/0.51 mid 50.0%, model 41.3% (projection_v2.0 (prediction ledger)) -- gap -8.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18SHESAK-SAK20` Will Stefanos Sakellaridis win the Alexander Shevchenko vs Stefanos Sakellaridis match by a set score of 2-0?: 0.02/0.23 mid 12.5%, model 20.2% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18SHESAK-1-SAK` Will Stefanos Sakellaridis win set 1 in the Alexander Shevchenko vs Stefanos Sakellaridis match: 0.36/0.41 mid 38.5%, model 44.9% (projection_v2.0 (prediction ledger)) -- gap +6.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18SHESAK-2-SHE` Will Alexander Shevchenko win set 2 in the Alexander Shevchenko vs Stefanos Sakellaridis match: 0.59/0.63 mid 61.0%, model 55.1% (projection_v2.0 (prediction ledger)) -- gap -5.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT18SHESAK-SAK2` Will Stefanos Sakellaridis win at least 1.5 more games than Alexander Shevchenko?: 0.22/0.37 mid 29.5%, model 34.7% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18SHESAK-SHE20` Will Alexander Shevchenko win the Alexander Shevchenko vs Stefanos Sakellaridis match by a set score of 2-0?: 0.22/0.44 mid 33.0%, model 30.3% (projection_v2.0 (prediction ledger)) -- gap -2.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18SHESAK-1-SHE` Will Alexander Shevchenko win set 1 in the Alexander Shevchenko vs Stefanos Sakellaridis match: 0.42/0.63 mid 52.5%, model 55.1% (projection_v2.0 (prediction ledger)) -- gap +2.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Na Hyun Kang vs Mirudhula Palanivel -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260245:267418:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Na Hyun Kang (`KXITFWMATCH-26OCT18KANPAL-KAN`) | 0.03 / 0.95 (27) | 49.0% | 84.1% | 56.9% | 64.6% [64.6%-65.6%] | -- | -- | -- | -- | PASS | +35.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mirudhula Palanivel (`KXITFWMATCH-26OCT18KANPAL-PAL`) | 0.03 / 0.91 (53) | 47.0% | 15.9% | 43.1% | 35.4% [34.4%-35.4%] | -- | -- | -- | -- | PASS | -31.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 462.0, B 73.0; serve-point win A 56.3%, B 51.2%; Elo A 1286.1, B 1176.6; model uncertainty 0.0051
* Form inputs: days since last match A 173, B 397; matches on record A 31, B 12; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18KANPAL-KAN  (YES = Na Hyun Kang)
Model: 84%
Kalshi: 49%
Gap: +35 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aditi Rawat vs Kelly Yi Xian CHEN -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18RAWCHE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kelly Yi Xian CHEN (`KXITFWMATCH-26OCT18RAWCHE-CHE`) | 0.03 / 0.97 (285) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aditi Rawat (`KXITFWMATCH-26OCT18RAWCHE-RAW`) | 0.03 / 0.97 (263) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jiho Shin vs Lulwa Naswardhani -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18SHINAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lulwa Naswardhani (`KXITFWMATCH-26OCT18SHINAS-NAS`) | 0.03 / 0.97 (285) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jiho Shin (`KXITFWMATCH-26OCT18SHINAS-SHI`) | 0.03 / 0.97 (263) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nirelle Yasin vs Bela Tamhankar -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18YASTAM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bela Tamhankar (`KXITFWMATCH-26OCT18YASTAM-TAM`) | 0.03 / 0.95 (27) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nirelle Yasin (`KXITFWMATCH-26OCT18YASTAM-YAS`) | 0.03 / 0.95 (27) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Minxu Zhou vs Nalu Himeno -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222527:269971:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nalu Himeno (`KXITFWMATCH-26OCT18ZHOHIM-HIM`) | 0.03 / 0.97 (285) | 50.0% | 22.1% | 26.9% | 25.2% [25.1%-26.1%] | -- | -- | -- | -- | PASS | -27.9 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Minxu Zhou (`KXITFWMATCH-26OCT18ZHOHIM-ZHO`) | 0.03 / 0.97 (263) | 50.0% | 77.9% | 73.1% | 74.8% [73.9%-74.9%] | -- | -- | -- | -- | PASS | +27.9 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 38.0; serve-point win A 56.4%, B 49.4%; Elo A 1278.5, B 1094.5; model uncertainty 0.0046
* Form inputs: days since last match A 698, B 222; matches on record A 3, B 20; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18ZHOHIM-ZHO  (YES = Minxu Zhou)
Model: 78%
Kalshi: 50%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Remy Bertola vs Federico Cina -- ATP Brussels Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-18 10:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: 2026-10-18 09:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200329:210748:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Remy Bertola (`KXATPMATCH-26OCT18BERCIN-BER`) | 0.38 / 0.40 (692) | 39.0% | 35.8% | 39.7% | 38.3% [38.3%-39.7%] | 36.1% | 37.2% | -- | INSUFFICIENT_INPUTS | PASS | -3.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Federico Cina (`KXATPMATCH-26OCT18BERCIN-CIN`) | 0.60 / 0.62 (410) | 61.0% | 64.2% | 60.3% | 61.7% [60.3%-61.7%] | 63.9% | 62.9% | -- | INSUFFICIENT_INPUTS | PASS | +3.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3382.0, B 3338.0; serve-point win A 63.2%, B 33.9%; Elo A 1574.7, B 1670.7; model uncertainty 0.0071
* Form inputs: days since last match A 19, B 10; matches on record A 405, B 152; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight +0.009
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT18BERCIN-CIN20` Will Federico Cina win the Remy Bertola vs Federico Cina match by a set score of 2-0?: 0.02/0.45 mid 23.5%, model 35.5% (projection_v2.0 (prediction ledger)) -- gap +12.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18BERCIN-17` Over 16.5 games: 0.80/0.98 mid 89.0%, model 97.5% (projection_v2.0 (prediction ledger)) -- gap +8.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18BERCIN-22` Over 21.5 games: 0.61/0.62 mid 61.5%, model 68.8% (projection_v2.0 (prediction ledger)) -- gap +7.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18BERCIN-CIN21` Will Federico Cina win the Remy Bertola vs Federico Cina match by a set score of 2-1?: 0.16/0.27 mid 21.5%, model 28.7% (projection_v2.0 (prediction ledger)) -- gap +7.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18BERCIN-27` Over 26.5 games: 0.33/0.43 mid 38.0%, model 43.6% (projection_v2.0 (prediction ledger)) -- gap +5.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18BERCIN-BER21` Will Remy Bertola win the Remy Bertola vs Federico Cina match by a set score of 2-1?: 0.09/0.19 mid 14.0%, model 19.5% (projection_v2.0 (prediction ledger)) -- gap +5.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BERCIN-2-CIN` Will Federico Cina win set 2 in the Remy Bertola vs Federico Cina match: 0.51/0.60 mid 55.5%, model 59.6% (projection_v2.0 (prediction ledger)) -- gap +4.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT18BERCIN-BER2` Will Remy Bertola win at least 1.5 more games than Federico Cina?: 0.26/0.38 mid 32.0%, model 28.8% (projection_v2.0 (prediction ledger)) -- gap -3.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18BERCIN-CIN4` Will Federico Cina win at least 3.5 more games than Remy Bertola?: 0.38/0.41 mid 39.5%, model 37.1% (projection_v2.0 (prediction ledger)) -- gap -2.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BERCIN-1-CIN` Will Federico Cina win set 1 in the Remy Bertola vs Federico Cina match: 0.57/0.61 mid 59.0%, model 59.6% (projection_v2.0 (prediction ledger)) -- gap +0.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18BERCIN-BER20` Will Remy Bertola win the Remy Bertola vs Federico Cina match by a set score of 2-0?: 0.08/0.25 mid 16.5%, model 16.4% (projection_v2.0 (prediction ledger)) -- gap -0.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BERCIN-1-BER` Will Remy Bertola win set 1 in the Remy Bertola vs Federico Cina match: 0.38/0.43 mid 40.5%, model 40.4% (projection_v2.0 (prediction ledger)) -- gap -0.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BERCIN-2-BER` Will Remy Bertola win set 2 in the Remy Bertola vs Federico Cina match: 0.38/0.43 mid 40.5%, model 40.4% (projection_v2.0 (prediction ledger)) -- gap -0.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Maja Chwalinska vs Sonay Kartal -- WTA Wuhan F

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 13:30Z
* Current expected start: 2026-10-18 10:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: 2026-10-18 09:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

WTA (MASTERS_1000) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:216081:222661:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maja Chwalinska (`KXWTAMATCH-26OCT18CHWKAR-CHW`) | 0.48 / 0.49 (9605) | 48.5% | 39.2% | 50.0% | 43.2% [40.1%-46.3%] | 47.8% | 47.6% | 47.7% | MARKETS_AGREE | PASS | -9.3 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Sonay Kartal (`KXWTAMATCH-26OCT18CHWKAR-KAR`) | 0.50 / 0.51 (287) | 50.5% | 60.8% | 50.0% | 56.8% [53.7%-60.0%] | 52.2% | 52.4% | 52.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +10.3 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3543.0, B 3052.0; serve-point win A 55.1%, B 42.8%; Elo A 1835.8, B 1975.4; model uncertainty 0.0313
* Form inputs: days since last match A 1, B 1; matches on record A 395, B 256; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.016, surface_dev_loose +0.011, surface_dev_tight -0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT18CHWKAR-22` Over 21.5 games: 0.50/0.52 mid 51.0%, model 61.7% (projection_v2.0 (prediction ledger)) -- gap +10.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT18CHWKAR-27` Over 26.5 games: 0.26/0.33 mid 29.5%, model 38.6% (projection_v2.0 (prediction ledger)) -- gap +9.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT18CHWKAR-2-KAR` Will Sonay Kartal win set 2 in the Maja Chwalinska vs Sonay Kartal match: 0.40/0.61 mid 50.5%, model 57.3% (projection_v2.0 (prediction ledger)) -- gap +6.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT18CHWKAR-1-KAR` Will Sonay Kartal win set 1 in the Maja Chwalinska vs Sonay Kartal match: 0.49/0.54 mid 51.5%, model 57.3% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT18CHWKAR-2-CHW` Will Maja Chwalinska win set 2 in the Maja Chwalinska vs Sonay Kartal match: 0.46/0.51 mid 48.5%, model 42.7% (projection_v2.0 (prediction ledger)) -- gap -5.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT18CHWKAR-1-CHW` Will Maja Chwalinska win set 1 in the Maja Chwalinska vs Sonay Kartal match: 0.46/0.49 mid 47.5%, model 42.7% (projection_v2.0 (prediction ledger)) -- gap -4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT18CHWKAR-17` Over 16.5 games: 0.81/0.96 mid 88.5%, model 93.2% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Daniel Altmaier vs Titouan Droguet -- ATP Lyon R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-18T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:127157:208169:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Altmaier (`KXATPMATCH-26OCT18ALTDRO-ALT`) | 0.06 / 0.94 (222) | 50.0% | 36.1% | 33.4% | 34.8% [33.8%-37.6%] | -- | -- | -- | -- | PASS | -13.9 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Titouan Droguet (`KXATPMATCH-26OCT18ALTDRO-DRO`) | 0.06 / 0.94 (200) | 50.0% | 63.9% | 66.6% | 65.2% [62.4%-66.2%] | -- | -- | -- | -- | PASS | +13.9 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5348.0, B 5236.0; serve-point win A 61.2%, B 36.0%; Elo A 1805.7, B 1873.4; model uncertainty 0.0191
* Form inputs: days since last match A 8, B 26; matches on record A 705, B 393; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.010, surface_dev_tight +0.015
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18ALTDRO-1-DRO` Will Titouan Droguet win set 1 in the Daniel Altmaier vs Titouan Droguet match: 0.01/0.98 mid 49.5%, model 59.4% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ALTDRO-2-DRO` Will Titouan Droguet win set 2 in the Daniel Altmaier vs Titouan Droguet match: 0.01/0.98 mid 49.5%, model 59.4% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ALTDRO-1-ALT` Will Daniel Altmaier win set 1 in the Daniel Altmaier vs Titouan Droguet match: 0.01/0.98 mid 49.5%, model 40.6% (projection_v2.0 (prediction ledger)) -- gap -8.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ALTDRO-2-ALT` Will Daniel Altmaier win set 2 in the Daniel Altmaier vs Titouan Droguet match: 0.01/0.98 mid 49.5%, model 40.6% (projection_v2.0 (prediction ledger)) -- gap -8.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Matteo Arnaldi vs Lorenzo Musetti -- ATP Lyon R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-18T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207518:208286:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Arnaldi (`KXATPMATCH-26OCT18ARNMUS-ARN`) | 0.08 / 0.94 (200) | 51.0% | 30.2% | 31.7% | 29.9% [29.0%-30.8%] | -- | -- | -- | -- | PASS | -20.8 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lorenzo Musetti (`KXATPMATCH-26OCT18ARNMUS-MUS`) | 0.06 / 0.94 (200) | 50.0% | 69.8% | 68.3% | 70.1% [69.2%-71.0%] | -- | -- | -- | -- | PASS | +19.8 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4135.0, B 4676.0; serve-point win A 58.5%, B 37.5%; Elo A 1915.4, B 2101.7; model uncertainty 0.0091
* Form inputs: days since last match A 7, B 8; matches on record A 385, B 466; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT18ARNMUS-MUS  (YES = Lorenzo Musetti)
Model: 70%
Kalshi: 50%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: WIDE_SPREAD, NO_EXTERNAL_REFERENCE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high -0.000, surface_dev_loose +0.004, surface_dev_tight -0.004
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18ARNMUS-1-MUS` Will Lorenzo Musetti win set 1 in the Matteo Arnaldi vs Lorenzo Musetti match: 0.01/0.98 mid 49.5%, model 63.5% (projection_v2.0 (prediction ledger)) -- gap +14.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ARNMUS-2-MUS` Will Lorenzo Musetti win set 2 in the Matteo Arnaldi vs Lorenzo Musetti match: 0.01/0.98 mid 49.5%, model 63.5% (projection_v2.0 (prediction ledger)) -- gap +14.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ARNMUS-1-ARN` Will Matteo Arnaldi win set 1 in the Matteo Arnaldi vs Lorenzo Musetti match: 0.01/0.98 mid 49.5%, model 36.5% (projection_v2.0 (prediction ledger)) -- gap -13.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ARNMUS-2-ARN` Will Matteo Arnaldi win set 2 in the Matteo Arnaldi vs Lorenzo Musetti match: 0.01/0.98 mid 49.5%, model 36.5% (projection_v2.0 (prediction ledger)) -- gap -13.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Mattia Bellucci vs Martin Landaluce -- ATP Challenger Jinan F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-18T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208233:212021:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mattia Bellucci (`KXATPCHALLENGERMATCH-26OCT18BELLAN-BEL`) | 0.59 / 0.60 (250) | 59.5% | 55.5% | 52.5% | 56.0% [54.0%-67.5%] | 59.2% | 59.3% | -- | INSUFFICIENT_INPUTS | PASS | -4.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Martin Landaluce (`KXATPCHALLENGERMATCH-26OCT18BELLAN-LAN`) | 0.39 / 0.40 (815) | 39.5% | 44.5% | 47.5% | 44.0% [32.5%-46.0%] | 40.8% | 40.7% | -- | INSUFFICIENT_INPUTS | PASS | +5.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4439.0, B 3597.0; serve-point win A 63.9%, B 37.2%; Elo A 1795.9, B 1706.0; model uncertainty 0.0675
* Form inputs: days since last match A 10, B 698; matches on record A 394, B 115; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.015, surface_dev_loose -0.015, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE

## Ugo Blanchet vs Nicolai Budkov Kjaer -- ATP Lyon R16

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-18T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:149282:200259:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ugo Blanchet (`KXATPMATCH-26OCT18BLABUD-BLA`) | 0.06 / 0.94 (222) | 50.0% | 37.7% | 34.3% | 36.6% [34.2%-41.0%] | -- | -- | -- | -- | PASS | -12.3 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nicolai Budkov Kjaer (`KXATPMATCH-26OCT18BLABUD-BUD`) | 0.06 / 0.94 (200) | 50.0% | 62.3% | 65.7% | 63.4% [59.0%-65.8%] | -- | -- | -- | -- | PASS | +12.3 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3260.0, B 3085.0; serve-point win A 61.2%, B 36.3%; Elo A 1585.3, B 1649.3; model uncertainty 0.0342
* Form inputs: days since last match A 19, B 19; matches on record A 356, B 143; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.009, surface_dev_loose -0.025, surface_dev_tight +0.020
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18BLABUD-1-BUD` Will Nicolai Budkov Kjaer win set 1 in the Ugo Blanchet vs Nicolai Budkov Kjaer match: 0.01/0.98 mid 49.5%, model 58.3% (projection_v2.0 (prediction ledger)) -- gap +8.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BLABUD-2-BUD` Will Nicolai Budkov Kjaer win set 2 in the Ugo Blanchet vs Nicolai Budkov Kjaer match: 0.01/0.98 mid 49.5%, model 58.3% (projection_v2.0 (prediction ledger)) -- gap +8.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BLABUD-1-BLA` Will Ugo Blanchet win set 1 in the Ugo Blanchet vs Nicolai Budkov Kjaer match: 0.01/0.98 mid 49.5%, model 41.7% (projection_v2.0 (prediction ledger)) -- gap -7.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BLABUD-2-BLA` Will Ugo Blanchet win set 2 in the Ugo Blanchet vs Nicolai Budkov Kjaer match: 0.01/0.98 mid 49.5%, model 41.7% (projection_v2.0 (prediction ledger)) -- gap -7.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Benjamin Bonzi vs Cameron Norrie -- ATP Lyon R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-18T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111815:126127:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Benjamin Bonzi (`KXATPMATCH-26OCT18BONNOR-BON`) | 0.06 / 0.94 (222) | 50.0% | 38.6% | 47.5% | 42.5% [39.6%-44.5%] | -- | -- | -- | -- | PASS | -11.4 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Cameron Norrie (`KXATPMATCH-26OCT18BONNOR-NOR`) | 0.06 / 0.94 (200) | 50.0% | 61.4% | 52.5% | 57.5% [55.5%-60.4%] | -- | -- | -- | -- | PASS | +11.4 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4477.0, B 5008.0; serve-point win A 62.4%, B 35.3%; Elo A 1728.7, B 1884.8; model uncertainty 0.0245
* Form inputs: days since last match A 19, B 9; matches on record A 770, B 657; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight +0.000
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18BONNOR-1-NOR` Will Cameron Norrie win set 1 in the Benjamin Bonzi vs Cameron Norrie match: 0.01/0.98 mid 49.5%, model 57.7% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BONNOR-2-NOR` Will Cameron Norrie win set 2 in the Benjamin Bonzi vs Cameron Norrie match: 0.01/0.98 mid 49.5%, model 57.7% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BONNOR-1-BON` Will Benjamin Bonzi win set 1 in the Benjamin Bonzi vs Cameron Norrie match: 0.01/0.98 mid 49.5%, model 42.3% (projection_v2.0 (prediction ledger)) -- gap -7.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BONNOR-2-BON` Will Benjamin Bonzi win set 2 in the Benjamin Bonzi vs Cameron Norrie match: 0.01/0.98 mid 49.5%, model 42.3% (projection_v2.0 (prediction ledger)) -- gap -7.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Jaime Faria vs Felix Balshaw -- ATP Lyon R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-18T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:210262:213149:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felix Balshaw (`KXATPMATCH-26OCT18FARBAL-BAL`) | 0.06 / 0.92 (50) | 49.0% | 30.9% | 42.0% | 31.7% [24.1%-37.2%] | -- | -- | -- | -- | PASS | -18.1 pp | HIGH_REVIEW | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jaime Faria (`KXATPMATCH-26OCT18FARBAL-FAR`) | 0.06 / 0.94 (200) | 50.0% | 69.1% | 58.0% | 68.3% [62.8%-75.9%] | -- | -- | -- | -- | PASS | +19.1 pp | HIGH_REVIEW | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4745.0, B 1807.0; serve-point win A 65.4%, B 38.6%; Elo A 1800.9, B 1569.3; model uncertainty 0.0658
* Form inputs: days since last match A 10, B 12; matches on record A 312, B 44; data quality B

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT18FARBAL-FAR  (YES = Jaime Faria)
Model: 69%
Kalshi: 50%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: WIDE_SPREAD, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.022, surface_pool_high -0.023, surface_dev_loose -0.005, surface_dev_tight -0.005
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18FARBAL-2-BAL` Will Felix Balshaw win set 2 in the Jaime Faria vs Felix Balshaw match: 0.05/0.98 mid 51.5%, model 37.0% (projection_v2.0 (prediction ledger)) -- gap -14.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18FARBAL-2-FAR` Will Jaime Faria win set 2 in the Jaime Faria vs Felix Balshaw match: 0.01/0.97 mid 49.0%, model 63.0% (projection_v2.0 (prediction ledger)) -- gap +14.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18FARBAL-1-FAR` Will Jaime Faria win set 1 in the Jaime Faria vs Felix Balshaw match: 0.01/0.98 mid 49.5%, model 63.0% (projection_v2.0 (prediction ledger)) -- gap +13.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18FARBAL-1-BAL` Will Felix Balshaw win set 1 in the Jaime Faria vs Felix Balshaw match: 0.01/0.98 mid 49.5%, model 37.0% (projection_v2.0 (prediction ledger)) -- gap -12.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Ugo Humbert vs Corentin Moutet -- ATP Lyon R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-18T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144895:200005:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ugo Humbert (`KXATPMATCH-26OCT18HUMMOU-HUM`) | 0.10 / 0.94 (222) | 52.0% | 45.0% | 46.5% | 43.5% [40.0%-50.5%] | -- | -- | -- | -- | PASS | -7.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Corentin Moutet (`KXATPMATCH-26OCT18HUMMOU-MOU`) | 0.08 / 0.92 (20) | 50.0% | 55.0% | 53.5% | 56.5% [49.5%-60.0%] | -- | -- | -- | -- | PASS | +5.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4602.0, B 4547.0; serve-point win A 61.8%, B 37.2%; Elo A 1731.6, B 1830.1; model uncertainty 0.0525
* Form inputs: days since last match A 8, B 46; matches on record A 613, B 584; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.040, surface_pool_high -0.035, surface_dev_loose -0.030, surface_dev_tight +0.040
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18HUMMOU-1-MOU` Will Corentin Moutet win set 1 in the Ugo Humbert vs Corentin Moutet match: 0.01/0.98 mid 49.5%, model 53.4% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18HUMMOU-2-MOU` Will Corentin Moutet win set 2 in the Ugo Humbert vs Corentin Moutet match: 0.01/0.98 mid 49.5%, model 53.4% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18HUMMOU-1-HUM` Will Ugo Humbert win set 1 in the Ugo Humbert vs Corentin Moutet match: 0.01/0.98 mid 49.5%, model 46.6% (projection_v2.0 (prediction ledger)) -- gap -2.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18HUMMOU-2-HUM` Will Ugo Humbert win set 2 in the Ugo Humbert vs Corentin Moutet match: 0.01/0.98 mid 49.5%, model 46.6% (projection_v2.0 (prediction ledger)) -- gap -2.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Kyrian Jacquet vs Sascha Gueymard Wayenburg -- ATP Lyon R16

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-18T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208021:209849:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sascha Gueymard Wayenburg (`KXATPMATCH-26OCT18JACGUE-GUE`) | 0.06 / 0.94 (222) | 50.0% | 21.0% | 38.6% | 27.2% [16.1%-31.6%] | -- | -- | -- | -- | PASS | -29.0 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kyrian Jacquet (`KXATPMATCH-26OCT18JACGUE-JAC`) | 0.08 / 0.94 (200) | 51.0% | 79.0% | 61.4% | 72.8% [68.4%-83.9%] | -- | -- | -- | -- | PASS | +28.0 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3771.0, B 1404.0; serve-point win A 65.9%, B 40.5%; Elo A 1691.6, B 1428.9; model uncertainty 0.0775
* Form inputs: days since last match A 11, B 151; matches on record A 388, B 220; data quality B

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT18JACGUE-JAC  (YES = Kyrian Jacquet)
Model: 79%
Kalshi: 51%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: WIDE_SPREAD, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.017, surface_pool_high -0.013, surface_dev_loose -0.008, surface_dev_tight +0.007
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18JACGUE-1-JAC` Will Kyrian Jacquet win set 1 in the Kyrian Jacquet vs Sascha Gueymard Wayenburg match: 0.01/0.98 mid 49.5%, model 70.5% (projection_v2.0 (prediction ledger)) -- gap +21.0 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT18JACGUE-2-JAC` Will Kyrian Jacquet win set 2 in the Kyrian Jacquet vs Sascha Gueymard Wayenburg match: 0.01/0.98 mid 49.5%, model 70.5% (projection_v2.0 (prediction ledger)) -- gap +21.0 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT18JACGUE-1-GUE` Will Sascha Gueymard Wayenburg win set 1 in the Kyrian Jacquet vs Sascha Gueymard Wayenburg match: 0.01/0.98 mid 49.5%, model 29.5% (projection_v2.0 (prediction ledger)) -- gap -20.0 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT18JACGUE-2-GUE` Will Sascha Gueymard Wayenburg win set 2 in the Kyrian Jacquet vs Sascha Gueymard Wayenburg match: 0.01/0.98 mid 49.5%, model 29.5% (projection_v2.0 (prediction ledger)) -- gap -20.0 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Yeongseok Jeong vs Henry De Keulenaer -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18JEODEK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Henry De Keulenaer (`KXITFMATCH-26OCT18JEODEK-DEK`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yeongseok Jeong (`KXITFMATCH-26OCT18JEODEK-JEO`) | 0.03 / 0.97 (363) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Szymon Kielan vs Benjamin Hassan -- ATP Challenger Lisbon Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-18T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:133975:209910:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Benjamin Hassan (`KXATPCHALLENGERMATCH-26OCT18KIEHAS-HAS`) | 0.05 / 0.95 (100) | 50.0% | 90.9% | 65.7% | 86.4% [84.1%-90.3%] | -- | -- | -- | -- | PASS | +40.9 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Szymon Kielan (`KXATPCHALLENGERMATCH-26OCT18KIEHAS-KIE`) | 0.05 / 0.95 (100) | 50.0% | 9.1% | 34.3% | 13.6% [9.7%-15.9%] | -- | -- | -- | -- | PASS | -40.9 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 225.0, B 3395.0; serve-point win A 57.5%, B 31.9%; Elo A 1270.7, B 1630.9; model uncertainty 0.0311
* Form inputs: days since last match A 726, B 19; matches on record A 118, B 508; data quality F

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT18KIEHAS-HAS  (YES = Benjamin Hassan)
Model: 91%
Kalshi: 50%
Gap: +41 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.011, surface_dev_loose -0.002, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jan Kumstat vs Michael Mmoh -- ATP Lyon R16

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-18T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111581:211618:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jan Kumstat (`KXATPMATCH-26OCT18KUMMMO-KUM`) | 0.06 / 0.94 (222) | 50.0% | 76.4% | 82.0% | 76.8% [65.0%-82.9%] | -- | -- | -- | -- | PASS | +26.4 pp | EXTREME (DATA_WARNING) | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Michael Mmoh (`KXATPMATCH-26OCT18KUMMMO-MMO`) | 0.06 / 0.94 (200) | 50.0% | 23.6% | 18.0% | 23.2% [17.1%-35.0%] | -- | -- | -- | -- | PASS | -26.4 pp | EXTREME (DATA_WARNING) | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1433.0, B 2931.0; serve-point win A 67.6%, B 38.2%; Elo A 1680.5, B 1529.5; model uncertainty 0.0895
* Form inputs: days since last match A 47, B 19; matches on record A 35, B 552; data quality B

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT18KUMMMO-KUM  (YES = Jan Kumstat)
Model: 76%
Kalshi: 50%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: WIDE_SPREAD, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.044, surface_pool_high +0.039, surface_dev_loose +0.025, surface_dev_tight -0.023
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18KUMMMO-1-KUM` Will Jan Kumstat win set 1 in the Jan Kumstat vs Michael Mmoh match: 0.01/0.98 mid 49.5%, model 68.4% (projection_v2.0 (prediction ledger)) -- gap +18.9 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18KUMMMO-2-KUM` Will Jan Kumstat win set 2 in the Jan Kumstat vs Michael Mmoh match: 0.01/0.98 mid 49.5%, model 68.4% (projection_v2.0 (prediction ledger)) -- gap +18.9 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18KUMMMO-1-MMO` Will Michael Mmoh win set 1 in the Jan Kumstat vs Michael Mmoh match: 0.01/0.98 mid 49.5%, model 31.6% (projection_v2.0 (prediction ledger)) -- gap -17.9 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18KUMMMO-2-MMO` Will Michael Mmoh win set 2 in the Jan Kumstat vs Michael Mmoh match: 0.01/0.98 mid 49.5%, model 31.6% (projection_v2.0 (prediction ledger)) -- gap -17.9 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Francesco Maestrelli vs Borna Gojo -- ATP Lyon R16

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-18T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:127339:208353:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Borna Gojo (`KXATPMATCH-26OCT18MAEGOJ-GOJ`) | 0.06 / 0.94 (222) | 50.0% | 58.0% | 64.3% | 60.1% [57.7%-62.5%] | -- | -- | -- | -- | PASS | +8.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Francesco Maestrelli (`KXATPMATCH-26OCT18MAEGOJ-MAE`) | 0.06 / 0.94 (200) | 50.0% | 42.0% | 35.7% | 39.9% [37.5%-42.3%] | -- | -- | -- | -- | PASS | -8.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3939.0, B 2738.0; serve-point win A 65.3%, B 33.1%; Elo A 1601.8, B 1619.2; model uncertainty 0.0235
* Form inputs: days since last match A 12, B 12; matches on record A 329, B 441; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.023, surface_pool_high +0.024, surface_dev_loose +0.000, surface_dev_tight -0.005
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18MAEGOJ-1-GOJ` Will Borna Gojo win set 1 in the Francesco Maestrelli vs Borna Gojo match: 0.01/0.98 mid 49.5%, model 55.3% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MAEGOJ-2-GOJ` Will Borna Gojo win set 2 in the Francesco Maestrelli vs Borna Gojo match: 0.01/0.98 mid 49.5%, model 55.3% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MAEGOJ-1-MAE` Will Francesco Maestrelli win set 1 in the Francesco Maestrelli vs Borna Gojo match: 0.01/0.98 mid 49.5%, model 44.7% (projection_v2.0 (prediction ledger)) -- gap -4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MAEGOJ-2-MAE` Will Francesco Maestrelli win set 2 in the Francesco Maestrelli vs Borna Gojo match: 0.01/0.98 mid 49.5%, model 44.7% (projection_v2.0 (prediction ledger)) -- gap -4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Hamad Medjedovic vs Brandon Nakashima -- ATP Lyon R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-18T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:206909:209098:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hamad Medjedovic (`KXATPMATCH-26OCT18MEDNAK-MED`) | 0.08 / 0.94 (222) | 51.0% | 47.4% | 39.9% | 46.1% [43.7%-49.5%] | -- | -- | -- | -- | PASS | -3.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Brandon Nakashima (`KXATPMATCH-26OCT18MEDNAK-NAK`) | 0.06 / 0.94 (200) | 50.0% | 52.6% | 60.1% | 53.9% [50.5%-56.3%] | -- | -- | -- | -- | PASS | +2.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3408.0, B 5558.0; serve-point win A 66.0%, B 33.5%; Elo A 1922.3, B 1847.6; model uncertainty 0.0291
* Form inputs: days since last match A 9, B 6; matches on record A 284, B 456; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose +0.019, surface_dev_tight -0.019
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18MEDNAK-1-NAK` Will Brandon Nakashima win set 1 in the Hamad Medjedovic vs Brandon Nakashima match: 0.01/0.98 mid 49.5%, model 51.7% (projection_v2.0 (prediction ledger)) -- gap +2.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MEDNAK-2-NAK` Will Brandon Nakashima win set 2 in the Hamad Medjedovic vs Brandon Nakashima match: 0.01/0.98 mid 49.5%, model 51.7% (projection_v2.0 (prediction ledger)) -- gap +2.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MEDNAK-1-MED` Will Hamad Medjedovic win set 1 in the Hamad Medjedovic vs Brandon Nakashima match: 0.01/0.98 mid 49.5%, model 48.3% (projection_v2.0 (prediction ledger)) -- gap -1.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MEDNAK-2-MED` Will Hamad Medjedovic win set 2 in the Hamad Medjedovic vs Brandon Nakashima match: 0.01/0.98 mid 49.5%, model 48.3% (projection_v2.0 (prediction ledger)) -- gap -1.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Maxim Mrva vs Dusan Lajovic -- ATP Lyon R16

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-18T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105583:211617:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dusan Lajovic (`KXATPMATCH-26OCT18MRVLAJ-LAJ`) | 0.06 / 0.94 (222) | 50.0% | 57.0% | 67.6% | 69.9% [69.0%-71.3%] | -- | -- | -- | -- | PASS | +7.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maxim Mrva (`KXATPMATCH-26OCT18MRVLAJ-MRV`) | 0.06 / 0.94 (200) | 50.0% | 43.0% | 32.4% | 30.1% [28.7%-31.0%] | -- | -- | -- | -- | PASS | -7.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3391.0, B 3735.0; serve-point win A 57.9%, B 40.8%; Elo A 1580.7, B 1771.0; model uncertainty 0.0116
* Form inputs: days since last match A 26, B 33; matches on record A 101, B 1042; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.004, surface_dev_loose +0.000, surface_dev_tight +0.000
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18MRVLAJ-1-MRV` Will Maxim Mrva win set 1 in the Maxim Mrva vs Dusan Lajovic match: 0.05/0.98 mid 51.5%, model 45.3% (projection_v2.0 (prediction ledger)) -- gap -6.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MRVLAJ-2-LAJ` Will Dusan Lajovic win set 2 in the Maxim Mrva vs Dusan Lajovic match: 0.01/0.96 mid 48.5%, model 54.7% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MRVLAJ-1-LAJ` Will Dusan Lajovic win set 1 in the Maxim Mrva vs Dusan Lajovic match: 0.01/0.97 mid 49.0%, model 54.7% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MRVLAJ-2-MRV` Will Maxim Mrva win set 2 in the Maxim Mrva vs Dusan Lajovic match: 0.01/0.96 mid 48.5%, model 45.3% (projection_v2.0 (prediction ledger)) -- gap -3.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ren Nakamura vs Julien Tremolieres -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18NAKTRE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ren Nakamura (`KXITFMATCH-26OCT18NAKTRE-NAK`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Julien Tremolieres (`KXITFMATCH-26OCT18NAKTRE-TRE`) | 0.03 / 0.97 (363) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mattia Nannelli vs Dimitris Sakellaridis -- ATP Challenger Florence Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-18T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212029:213617:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mattia Nannelli (`KXATPCHALLENGERMATCH-26OCT18NANSAK-NAN`) | 0.19 / 0.29 (68) | 24.0% | 47.8% | 61.1% | 61.1% [60.1%-62.0%] | -- | 27.2% | -- | INSUFFICIENT_INPUTS | PASS | +23.8 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dimitris Sakellaridis (`KXATPCHALLENGERMATCH-26OCT18NANSAK-SAK`) | 0.61 / 0.75 (256) | 68.0% | 52.2% | 38.9% | 38.9% [38.0%-39.9%] | -- | 72.9% | -- | INSUFFICIENT_INPUTS | PASS | -15.8 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 114.0; serve-point win A 61.3%, B 38.2%; Elo A 1272.5, B 1196.0; model uncertainty 0.0098
* Form inputs: days since last match A 719, B 12; matches on record A 1, B 39; data quality F

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT18NANSAK-NAN  (YES = Mattia Nannelli)
Model: 48%
Kalshi: 24%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; WIDE_SPREAD

## Guillermo Olaso vs Charles Josshua Kinaadman -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18OLAKIN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charles Josshua Kinaadman (`KXITFMATCH-26OCT18OLAKIN-KIN`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Guillermo Olaso (`KXITFMATCH-26OCT18OLAKIN-OLA`) | 0.03 / 0.97 (363) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sergi Perez Contri vs Sebastian Gima -- ATP Challenger Florence Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-18T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:133997:209142:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sebastian Gima (`KXATPCHALLENGERMATCH-26OCT18PERGIM-GIM`) | 0.44 / 0.49 (369) | 46.5% | 34.5% | 30.2% | 41.8% [38.8%-44.8%] | -- | 46.6% | -- | INSUFFICIENT_INPUTS | PASS | -12.0 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sergi Perez Contri (`KXATPCHALLENGERMATCH-26OCT18PERGIM-PER`) | 0.41 / 0.55 (125) | 48.0% | 65.5% | 69.8% | 58.2% [55.2%-61.2%] | -- | 53.3% | -- | INSUFFICIENT_INPUTS | PASS | +17.5 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 459.0, B 833.0; serve-point win A 61.1%, B 42.0%; Elo A 1388.8, B 1359.6; model uncertainty 0.0304
* Form inputs: days since last match A 194, B 26; matches on record A 280, B 297; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT18PERGIM-PER  (YES = Sergi Perez Contri)
Model: 66%
Kalshi: 48%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.030, surface_pool_high -0.031, surface_dev_loose -0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; WIDE_SPREAD

## Marko Retelj vs Roy Hobbs -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18RETHOB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Roy Hobbs (`KXITFMATCH-26OCT18RETHOB-HOB`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marko Retelj (`KXITFMATCH-26OCT18RETHOB-RET`) | 0.03 / 0.97 (363) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jurij Rodionov vs Pierre-Hugues Herbert -- ATP Lyon R16

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-18T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105732:200514:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pierre-Hugues Herbert (`KXATPMATCH-26OCT18RODHER-HER`) | 0.06 / 0.93 (26) | 49.5% | 28.5% | 39.6% | 39.1% [38.1%-41.0%] | -- | -- | -- | -- | PASS | -21.0 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jurij Rodionov (`KXATPMATCH-26OCT18RODHER-ROD`) | 0.06 / 0.94 (200) | 50.0% | 71.5% | 60.5% | 60.9% [59.0%-61.9%] | -- | -- | -- | -- | PASS | +21.5 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4821.0, B 2989.0; serve-point win A 65.1%, B 39.4%; Elo A 1690.8, B 1607.2; model uncertainty 0.0148
* Form inputs: days since last match A 28, B 53; matches on record A 584, B 846; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT18RODHER-ROD  (YES = Jurij Rodionov)
Model: 71%
Kalshi: 50%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: WIDE_SPREAD, NO_EXTERNAL_REFERENCE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.010, surface_dev_tight -0.005
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18RODHER-1-ROD` Will Jurij Rodionov win set 1 in the Jurij Rodionov vs Pierre-Hugues Herbert match: 0.01/0.96 mid 48.5%, model 64.8% (projection_v2.0 (prediction ledger)) -- gap +16.2 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18RODHER-2-ROD` Will Jurij Rodionov win set 2 in the Jurij Rodionov vs Pierre-Hugues Herbert match: 0.01/0.96 mid 48.5%, model 64.8% (projection_v2.0 (prediction ledger)) -- gap +16.2 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18RODHER-1-HER` Will Pierre-Hugues Herbert win set 1 in the Jurij Rodionov vs Pierre-Hugues Herbert match: 0.01/0.96 mid 48.5%, model 35.2% (projection_v2.0 (prediction ledger)) -- gap -13.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18RODHER-2-HER` Will Pierre-Hugues Herbert win set 2 in the Jurij Rodionov vs Pierre-Hugues Herbert match: 0.01/0.96 mid 48.5%, model 35.2% (projection_v2.0 (prediction ledger)) -- gap -13.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Valentin Royer vs Clement Tabur -- ATP Lyon R16

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-18T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:202127:208316:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valentin Royer (`KXATPMATCH-26OCT18ROYTAB-ROY`) | 0.06 / 0.94 (222) | 50.0% | 63.0% | 52.0% | 57.5% [55.0%-60.5%] | -- | -- | -- | -- | PASS | +13.0 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Clement Tabur (`KXATPMATCH-26OCT18ROYTAB-TAB`) | 0.06 / 0.94 (200) | 50.0% | 37.0% | 48.0% | 42.5% [39.5%-45.0%] | -- | -- | -- | -- | PASS | -13.0 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4813.0, B 3384.0; serve-point win A 63.8%, B 38.8%; Elo A 1728.4, B 1582.1; model uncertainty 0.0272
* Form inputs: days since last match A 9, B 19; matches on record A 401, B 442; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose +0.000, surface_dev_tight -0.000
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18ROYTAB-1-ROY` Will Valentin Royer win set 1 in the Valentin Royer vs Clement Tabur match: 0.01/0.96 mid 48.5%, model 58.7% (projection_v2.0 (prediction ledger)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ROYTAB-2-ROY` Will Valentin Royer win set 2 in the Valentin Royer vs Clement Tabur match: 0.01/0.96 mid 48.5%, model 58.7% (projection_v2.0 (prediction ledger)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ROYTAB-1-TAB` Will Clement Tabur win set 1 in the Valentin Royer vs Clement Tabur match: 0.01/0.96 mid 48.5%, model 41.3% (projection_v2.0 (prediction ledger)) -- gap -7.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ROYTAB-2-TAB` Will Clement Tabur win set 2 in the Valentin Royer vs Clement Tabur match: 0.01/0.96 mid 48.5%, model 41.3% (projection_v2.0 (prediction ledger)) -- gap -7.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Matteo Sciahbasi vs Daniel Siniakov -- ATP Challenger Florence Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-18T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209338:tml:S1AZ:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Sciahbasi (`KXATPCHALLENGERMATCH-26OCT18SCISIN-SCI`) | 0.18 / 0.29 (36) | 23.5% | 56.7% | 52.6% | 66.9% [64.2%-67.8%] | -- | 27.0% | -- | INSUFFICIENT_INPUTS | PASS | +33.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daniel Siniakov (`KXATPCHALLENGERMATCH-26OCT18SCISIN-SIN`) | 0.62 / 0.74 (64) | 68.0% | 43.3% | 47.4% | 33.1% [32.1%-35.8%] | -- | 73.2% | -- | INSUFFICIENT_INPUTS | PASS | -24.7 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 78.0, B 334.0; serve-point win A 61.0%, B 40.3%; Elo A 1355.6, B 1231.7; model uncertainty 0.0183
* Form inputs: days since last match A 19, B 40; matches on record A 1, B 81; data quality F

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT18SCISIN-SCI  (YES = Matteo Sciahbasi)
Model: 57%
Kalshi: 24%
Gap: +33 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.019, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; WIDE_SPREAD

## Joao Silva vs Alexander Ritschard -- ATP Challenger Lisbon Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-18T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106310:133197:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Ritschard (`KXATPCHALLENGERMATCH-26OCT18SILRIT-RIT`) | 0.05 / 0.95 (100) | 50.0% | 94.4% | 86.5% | 91.9% [90.7%-93.1%] | -- | -- | -- | -- | PASS | +44.4 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Joao Silva (`KXATPCHALLENGERMATCH-26OCT18SILRIT-SIL`) | 0.05 / 0.95 (100) | 50.0% | 5.6% | 13.5% | 8.1% [6.9%-9.3%] | -- | -- | -- | -- | PASS | -44.4 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 103.0, B 1877.0; serve-point win A 54.5%, B 33.0%; Elo A 1308.3, B 1736.4; model uncertainty 0.012
* Form inputs: days since last match A 91, B 40; matches on record A 4, B 519; data quality D

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT18SILRIT-RIT  (YES = Alexander Ritschard)
Model: 94%
Kalshi: 50%
Gap: +44 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.012, surface_dev_loose -0.002, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Lorenzo Sonego vs Moise Kouame -- ATP Lyon R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-18T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:132283:213608:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Moise Kouame (`KXATPMATCH-26OCT18SONKOU-KOU`) | 0.06 / 0.94 (222) | 50.0% | 29.6% | 43.0% | 28.2% [20.4%-35.4%] | -- | -- | -- | -- | PASS | -20.4 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lorenzo Sonego (`KXATPMATCH-26OCT18SONKOU-SON`) | 0.06 / 0.94 (200) | 50.0% | 70.4% | 57.0% | 71.8% [64.6%-79.6%] | -- | -- | -- | -- | PASS | +20.4 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4551.0, B 1583.0; serve-point win A 65.9%, B 38.4%; Elo A 1802.2, B 1519.3; model uncertainty 0.0746
* Form inputs: days since last match A 12, B 18; matches on record A 689, B 33; data quality B

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT18SONKOU-SON  (YES = Lorenzo Sonego)
Model: 70%
Kalshi: 50%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: WIDE_SPREAD, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.026, surface_dev_loose -0.021, surface_dev_tight +0.012
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18SONKOU-1-SON` Will Lorenzo Sonego win set 1 in the Lorenzo Sonego vs Moise Kouame match: 0.05/0.96 mid 50.5%, model 64.0% (projection_v2.0 (prediction ledger)) -- gap +13.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT18SONKOU-2-SON` Will Lorenzo Sonego win set 2 in the Lorenzo Sonego vs Moise Kouame match: 0.05/0.96 mid 50.5%, model 64.0% (projection_v2.0 (prediction ledger)) -- gap +13.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT18SONKOU-1-KOU` Will Moise Kouame win set 1 in the Lorenzo Sonego vs Moise Kouame match: 0.01/0.93 mid 47.0%, model 36.0% (projection_v2.0 (prediction ledger)) -- gap -11.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT18SONKOU-2-KOU` Will Moise Kouame win set 2 in the Lorenzo Sonego vs Moise Kouame match: 0.01/0.93 mid 47.0%, model 36.0% (projection_v2.0 (prediction ledger)) -- gap -11.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Otto Virtanen vs Vitaliy Sachko -- ATP Lyon R16

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-18T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126964:202261:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vitaliy Sachko (`KXATPMATCH-26OCT18VIRSAC-SAC`) | 0.06 / 0.94 (222) | 50.0% | 52.8% | 50.5% | 52.5% [48.5%-56.5%] | -- | -- | -- | -- | PASS | +2.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Otto Virtanen (`KXATPMATCH-26OCT18VIRSAC-VIR`) | 0.06 / 0.94 (200) | 50.0% | 47.2% | 49.5% | 47.5% [43.5%-51.5%] | -- | -- | -- | -- | PASS | -2.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4578.0, B 3730.0; serve-point win A 62.2%, B 37.3%; Elo A 1596.5, B 1653.4; model uncertainty 0.0403
* Form inputs: days since last match A 28, B 19; matches on record A 414, B 517; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.030, surface_pool_high -0.040, surface_dev_loose -0.020, surface_dev_tight +0.010
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18VIRSAC-2-SAC` Will Vitaliy Sachko win set 2 in the Otto Virtanen vs Vitaliy Sachko match: 0.01/0.96 mid 48.5%, model 51.8% (projection_v2.0 (prediction ledger)) -- gap +3.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18VIRSAC-1-SAC` Will Vitaliy Sachko win set 1 in the Otto Virtanen vs Vitaliy Sachko match: 0.05/0.93 mid 49.0%, model 51.8% (projection_v2.0 (prediction ledger)) -- gap +2.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18VIRSAC-1-VIR` Will Otto Virtanen win set 1 in the Otto Virtanen vs Vitaliy Sachko match: 0.05/0.93 mid 49.0%, model 48.2% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18VIRSAC-2-VIR` Will Otto Virtanen win set 2 in the Otto Virtanen vs Vitaliy Sachko match: 0.01/0.96 mid 48.5%, model 48.2% (projection_v2.0 (prediction ledger)) -- gap -0.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Stan Wawrinka vs Martin Landaluce -- ATP Lyon R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-18T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:104527:212021:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martin Landaluce (`KXATPMATCH-26OCT18WAWLAN-LAN`) | 0.06 / 0.94 (222) | 50.0% | 60.9% | 60.4% | 53.5% [36.5%-56.5%] | -- | -- | -- | -- | PASS | +10.9 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Stan Wawrinka (`KXATPMATCH-26OCT18WAWLAN-WAW`) | 0.06 / 0.94 (200) | 50.0% | 39.1% | 39.6% | 46.5% [43.5%-63.5%] | -- | -- | -- | -- | PASS | -10.9 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3775.0, B 3597.0; serve-point win A 62.7%, B 35.1%; Elo A 1798.5, B 1699.1; model uncertainty 0.0998
* Form inputs: days since last match A 29, B 698; matches on record A 1173, B 115; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.020, surface_dev_tight +0.025
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18WAWLAN-1-LAN` Will Martin Landaluce win set 1 in the Stan Wawrinka vs Martin Landaluce match: 0.01/0.93 mid 47.0%, model 57.3% (projection_v2.0 (prediction ledger)) -- gap +10.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT18WAWLAN-1-WAW` Will Stan Wawrinka win set 1 in the Stan Wawrinka vs Martin Landaluce match: 0.05/0.96 mid 50.5%, model 42.7% (projection_v2.0 (prediction ledger)) -- gap -7.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT18WAWLAN-2-LAN` Will Martin Landaluce win set 2 in the Stan Wawrinka vs Martin Landaluce match: 0.05/0.96 mid 50.5%, model 57.3% (projection_v2.0 (prediction ledger)) -- gap +6.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT18WAWLAN-2-WAW` Will Stan Wawrinka win set 2 in the Stan Wawrinka vs Martin Landaluce match: 0.01/0.93 mid 47.0%, model 42.7% (projection_v2.0 (prediction ledger)) -- gap -4.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data POOR
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Meng Yi Chen vs Junlu Sun -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221903:264970:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Meng Yi Chen (`KXITFWMATCH-26OCT18CHESUN-CHE`) | 0.37 / 0.61 (64) | 49.0% | 75.4% | 42.0% | 61.6% [59.5%-62.6%] | -- | -- | -- | -- | PASS | +26.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Junlu Sun (`KXITFWMATCH-26OCT18CHESUN-SUN`) | 0.19 / 0.55 (56) | 37.0% | 24.6% | 58.0% | 38.4% [37.4%-40.5%] | -- | -- | -- | -- | PASS | -12.4 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1394.0, B 0.0; serve-point win A 56.0%, B 49.1%; Elo A 1382.4, B 1304.4; model uncertainty 0.0154
* Form inputs: days since last match A 222, B 761; matches on record A 162, B 15; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18CHESUN-CHE  (YES = Meng Yi Chen)
Model: 75%
Kalshi: 49%
Gap: +26 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yui Chikaraishi vs Jasmin Jebawy -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211965:220469:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yui Chikaraishi (`KXITFWMATCH-26OCT18CHIJEB-CHI`) | 0.04 / 0.97 (285) | 50.5% | 63.5% | 13.3% | 61.6% [56.4%-65.6%] | -- | -- | -- | -- | PASS | +13.0 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jasmin Jebawy (`KXITFWMATCH-26OCT18CHIJEB-JEB`) | 0.03 / 0.97 (263) | 50.0% | 36.5% | 86.7% | 38.4% [34.4%-43.6%] | -- | -- | -- | -- | PASS | -13.5 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 532.0, B 50.0; serve-point win A 53.5%, B 49.0%; Elo A 1310.3, B 1217.2; model uncertainty 0.0462
* Form inputs: days since last match A 215, B 285; matches on record A 185, B 285; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.052, surface_pool_high +0.040, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jasmine Lin vs Liuyan An -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:265015:270288:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liuyan An (`KXITFWMATCH-26OCT18LINANX-ANX`) | 0.91 / 0.96 (6768) | 93.5% | 47.1% | 46.3% | 43.6% [43.6%-44.7%] | -- | -- | -- | -- | PASS | -46.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jasmine Lin (`KXITFWMATCH-26OCT18LINANX-LIN`) | 0.03 / 0.11 (163) | 7.0% | 52.9% | 53.7% | 56.4% [55.3%-56.4%] | -- | -- | -- | -- | PASS | +45.9 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 31.0, B 425.0; serve-point win A 53.4%, B 47.1%; Elo A 1275.7, B 1230.4; model uncertainty 0.0053
* Form inputs: days since last match A 369, B 173; matches on record A 1, B 13; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18LINANX-LIN  (YES = Jasmine Lin)
Model: 53%
Kalshi: 7%
Gap: +46 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jiumeng Liu vs Xiaowei Li -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264090:264157:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jiumeng Liu (`KXITFWMATCH-26OCT18LIULIX-LIU`) | 0.04 / 0.41 (43) | 22.5% | 45.5% | 75.6% | 47.9% [46.8%-50.0%] | -- | -- | -- | -- | PASS | +23.0 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Xiaowei Li (`KXITFWMATCH-26OCT18LIULIX-LIX`) | 0.58 / 0.92 (6371) | 75.0% | 54.5% | 24.4% | 52.1% [50.0%-53.2%] | -- | -- | -- | -- | PASS | -20.5 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 80.0; serve-point win A 53.7%, B 45.5%; Elo A 1175.5, B 1188.0; model uncertainty 0.016
* Form inputs: days since last match A 670, B 173; matches on record A 30, B 28; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18LIULIX-LIU  (YES = Jiumeng Liu)
Model: 45%
Kalshi: 22%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.021, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Darja Suvirdjonkova vs Guyu Xu -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222294:265644:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Darja Suvirdjonkova (`KXITFWMATCH-26OCT18SUVXUX-SUV`) | 0.04 / 0.97 (285) | 50.5% | 93.7% | 83.5% | 81.8% [80.3%-84.2%] | -- | -- | -- | -- | PASS | +43.1 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Guyu Xu (`KXITFWMATCH-26OCT18SUVXUX-XUX`) | 0.03 / 0.95 (33) | 49.0% | 6.3% | 16.5% | 18.2% [15.8%-19.7%] | -- | -- | -- | -- | PASS | -42.6 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1431.0, B 115.0; serve-point win A 59.2%, B 52.2%; Elo A 1298.2, B 1037.9; model uncertainty 0.0193
* Form inputs: days since last match A 173, B 173; matches on record A 130, B 29; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18SUVXUX-SUV  (YES = Darja Suvirdjonkova)
Model: 94%
Kalshi: 50%
Gap: +43 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.007, surface_dev_loose +0.007, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Clement Chidekh vs Gauthier Onclin -- ATP Brussels Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-18 12:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: 2026-10-18 11:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:206889:206904:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Clement Chidekh (`KXATPMATCH-26OCT18CHIONC-CHI`) | 0.72 / 0.74 (363) | 73.0% | 68.6% | 76.1% | 71.5% [63.6%-75.3%] | 73.4% | 68.8% | -- | INSUFFICIENT_INPUTS | PASS | -4.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gauthier Onclin (`KXATPMATCH-26OCT18CHIONC-ONC`) | 0.25 / 0.26 (947) | 25.5% | 31.4% | 23.9% | 28.5% [24.6%-36.4%] | 26.7% | 26.4% | 26.4% | MODEL_LONE_OUTLIER | WATCH | +5.9 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3878.0, B 3092.0; serve-point win A 61.9%, B 41.8%; Elo A 1687.3, B 1608.1; model uncertainty 0.0587
* Form inputs: days since last match A 19, B 12; matches on record A 279, B 406; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.027, surface_pool_high +0.021, surface_dev_loose +0.008, surface_dev_tight -0.013
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT18CHIONC-23` Over 22.5 games: 0.42/0.43 mid 42.5%, model 54.7% (projection_v2.0 (prediction ledger)) -- gap +12.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18CHIONC-2-CHI` Will Clement Chidekh win set 2 in the Clement Chidekh vs Gauthier Onclin match: 0.31/0.72 mid 51.5%, model 62.7% (projection_v2.0 (prediction ledger)) -- gap +11.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT18CHIONC-CHI4` Will Clement Chidekh win at least 3.5 more games than Gauthier Onclin?: 0.56/0.57 mid 56.5%, model 46.0% (projection_v2.0 (prediction ledger)) -- gap -10.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18CHIONC-CHI21` Will Clement Chidekh win the Clement Chidekh vs Gauthier Onclin match by a set score of 2-1?: 0.13/0.27 mid 20.0%, model 29.3% (projection_v2.0 (prediction ledger)) -- gap +9.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18CHIONC-CHI20` Will Clement Chidekh win the Clement Chidekh vs Gauthier Onclin match by a set score of 2-0?: 0.02/0.58 mid 30.0%, model 39.3% (projection_v2.0 (prediction ledger)) -- gap +9.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18CHIONC-18` Over 17.5 games: 0.60/0.99 mid 79.5%, model 88.5% (projection_v2.0 (prediction ledger)) -- gap +9.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18CHIONC-1-ONC` Will Gauthier Onclin win set 1 in the Clement Chidekh vs Gauthier Onclin match: 0.27/0.32 mid 29.5%, model 37.3% (projection_v2.0 (prediction ledger)) -- gap +7.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18CHIONC-1-CHI` Will Clement Chidekh win set 1 in the Clement Chidekh vs Gauthier Onclin match: 0.68/0.72 mid 70.0%, model 62.7% (projection_v2.0 (prediction ledger)) -- gap -7.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18CHIONC-28` Over 27.5 games: 0.08/0.47 mid 27.5%, model 34.5% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18CHIONC-CHI7` Will Clement Chidekh win at least 6.5 more games than Gauthier Onclin?: 0.14/0.24 mid 19.0%, model 12.1% (projection_v2.0 (prediction ledger)) -- gap -6.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18CHIONC-ONC21` Will Gauthier Onclin win the Clement Chidekh vs Gauthier Onclin match by a set score of 2-1?: 0.05/0.43 mid 24.0%, model 17.4% (projection_v2.0 (prediction ledger)) -- gap -6.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18CHIONC-ONC2` Will Gauthier Onclin win at least 1.5 more games than Clement Chidekh?: 0.14/0.27 mid 20.5%, model 25.3% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18CHIONC-ONC20` Will Gauthier Onclin win the Clement Chidekh vs Gauthier Onclin match by a set score of 2-0?: 0.01/0.23 mid 12.0%, model 13.9% (projection_v2.0 (prediction ledger)) -- gap +1.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18CHIONC-2-ONC` Will Gauthier Onclin win set 2 in the Clement Chidekh vs Gauthier Onclin match: 0.27/0.45 mid 36.0%, model 37.3% (projection_v2.0 (prediction ledger)) -- gap +1.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jialan Cai vs Ke Ren -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260621:267498:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jialan Cai (`KXITFWMATCH-26OCT18CAIREN-CAI`) | 0.04 / 0.42 (47) | 23.0% | 45.3% | 78.9% | 48.9% [45.7%-53.7%] | -- | -- | -- | -- | PASS | +22.3 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ke Ren (`KXITFWMATCH-26OCT18CAIREN-REN`) | 0.50 / 0.82 (6235) | 66.0% | 54.7% | 21.1% | 51.1% [46.3%-54.3%] | -- | -- | -- | -- | PASS | -11.3 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 204.0, B 366.0; serve-point win A 53.4%, B 45.8%; Elo A 1218.7, B 1253.1; model uncertainty 0.04
* Form inputs: days since last match A 187, B 173; matches on record A 11, B 72; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18CAIREN-CAI  (YES = Jialan Cai)
Model: 45%
Kalshi: 23%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.005, surface_dev_loose +0.011, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marika Jones vs Yiru Chen -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222913:266372:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yiru Chen (`KXITFWMATCH-26OCT18JONCHE-CHE`) | 0.75 / 0.96 (6691) | 85.5% | 77.6% | 61.6% | 66.6% [64.6%-69.0%] | -- | -- | -- | -- | PASS | -7.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marika Jones (`KXITFWMATCH-26OCT18JONCHE-JON`) | 0.03 / 0.27 (35) | 15.0% | 22.4% | 38.4% | 33.4% [31.0%-35.4%] | -- | -- | -- | -- | PASS | +7.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 76.0, B 625.0; serve-point win A 46.6%, B 47.8%; Elo A 1127.1, B 1245.2; model uncertainty 0.0218
* Form inputs: days since last match A 348, B 173; matches on record A 78, B 28; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.015, surface_dev_loose +0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xi Luo vs Sitong Chen -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264069:268784:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sitong Chen (`KXITFWMATCH-26OCT18LUOCHE-CHE`) | 0.04 / 0.81 (132) | 42.5% | 9.0% | 21.1% | 26.0% [23.9%-26.0%] | -- | -- | -- | -- | PASS | -33.5 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Xi Luo (`KXITFWMATCH-26OCT18LUOCHE-LUO`) | 0.03 / 0.96 (625) | 49.5% | 91.0% | 78.9% | 74.0% [74.0%-76.1%] | -- | -- | -- | -- | PASS | +41.5 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 827.0, B 85.0; serve-point win A 58.4%, B 51.6%; Elo A 1415.7, B 1232.7; model uncertainty 0.0107
* Form inputs: days since last match A 173, B 180; matches on record A 43, B 3; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18LUOCHE-LUO  (YES = Xi Luo)
Model: 91%
Kalshi: 50%
Gap: +41 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.009, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zi Ye Zhang vs Ekaterina Kuznetsova -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206708:264143:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Kuznetsova (`KXITFWMATCH-26OCT18ZHAKUZ-KUZ`) | 0.23 / 0.68 (79) | 45.5% | 57.8% | 86.2% | 54.8% [43.1%-64.7%] | -- | -- | -- | -- | PASS | +12.3 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Zi Ye Zhang (`KXITFWMATCH-26OCT18ZHAKUZ-ZHA`) | 0.15 / 0.49 (49) | 32.0% | 42.2% | 13.8% | 45.2% [35.3%-56.9%] | -- | -- | -- | -- | PASS | +10.2 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 603.0, B 494.0; serve-point win A 49.1%, B 49.4%; Elo A 1306.1, B 1255.4; model uncertainty 0.108
* Form inputs: days since last match A 411, B 173; matches on record A 44, B 114; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.021, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eric Ahren Moonga vs Tobias Albig -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18AHRALB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eric Ahren Moonga (`KXITFMATCH-26OCT18AHRALB-AHR`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tobias Albig (`KXITFMATCH-26OCT18AHRALB-ALB`) | 0.03 / 0.97 (363) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hong-Lin Fu vs Taentawan Taddeo Majoli Maggioli -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18FUXMAJ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hong-Lin Fu (`KXITFMATCH-26OCT18FUXMAJ-FUX`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Taentawan Taddeo Majoli Maggioli (`KXITFMATCH-26OCT18FUXMAJ-MAJ`) | 0.03 / 0.97 (363) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luke Jie Xi Ho vs Yoan Naydenov -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18HOXNAY:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luke Jie Xi Ho (`KXITFMATCH-26OCT18HOXNAY-HOX`) | 0.05 / 0.95 (30) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yoan Naydenov (`KXITFMATCH-26OCT18HOXNAY-NAY`) | 0.03 / 0.97 (363) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luke Koh vs Aditya Kothari -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18KOHKOT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luke Koh (`KXITFMATCH-26OCT18KOHKOT-KOH`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aditya Kothari (`KXITFMATCH-26OCT18KOHKOT-KOT`) | 0.05 / 0.95 (30) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Michael Ng vs Hendrik Thada Grohbruegge -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18NGXGRO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hendrik Thada Grohbruegge (`KXITFMATCH-26OCT18NGXGRO-GRO`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Michael Ng (`KXITFMATCH-26OCT18NGXGRO-NGX`) | 0.03 / 0.97 (363) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nishesh Basavareddy vs Aziz Dougaz -- ATP Brussels Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 16:00Z
* Current expected start: 2026-10-18 13:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: 2026-10-18 12:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144826:210460:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nishesh Basavareddy (`KXATPMATCH-26OCT18BASDOU-BAS`) | 0.80 / 0.81 (67) | 80.5% | 61.8% | 52.9% | 60.1% [57.2%-62.9%] | -- | 80.8% | -- | INSUFFICIENT_INPUTS | PASS | -18.7 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aziz Dougaz (`KXATPMATCH-26OCT18BASDOU-DOU`) | 0.18 / 0.20 (6550) | 19.0% | 38.2% | 47.1% | 39.9% [37.1%-42.8%] | -- | 19.2% | -- | INSUFFICIENT_INPUTS | WATCH | +19.2 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2705.0, B 2266.0; serve-point win A 67.6%, B 34.9%; Elo A 1737.5, B 1590.1; model uncertainty 0.0281
* Form inputs: days since last match A 12, B 11; matches on record A 142, B 623; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT18BASDOU-DOU  (YES = Aziz Dougaz)
Model: 38%
Kalshi: 19%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, UNKNOWN
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.024, surface_pool_high +0.019, surface_dev_loose -0.010, surface_dev_tight +0.005
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18BASDOU-2-DOU` Will Aziz Dougaz win set 2 in the Nishesh Basavareddy vs Aziz Dougaz match: 0.21/0.26 mid 23.5%, model 42.0% (projection_v2.0 (prediction ledger)) -- gap +18.6 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BASDOU-1-DOU` Will Aziz Dougaz win set 1 in the Nishesh Basavareddy vs Aziz Dougaz match: 0.22/0.26 mid 24.0%, model 42.0% (projection_v2.0 (prediction ledger)) -- gap +18.1 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18BASDOU-BAS20` Will Nishesh Basavareddy win the Nishesh Basavareddy vs Aziz Dougaz match by a set score of 2-0?: 0.39/0.61 mid 50.0%, model 33.6% (projection_v2.0 (prediction ledger)) -- gap -16.4 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BASDOU-1-BAS` Will Nishesh Basavareddy win set 1 in the Nishesh Basavareddy vs Aziz Dougaz match: 0.67/0.78 mid 72.5%, model 58.0% (projection_v2.0 (prediction ledger)) -- gap -14.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BASDOU-2-BAS` Will Nishesh Basavareddy win set 2 in the Nishesh Basavareddy vs Aziz Dougaz match: 0.64/0.78 mid 71.0%, model 58.0% (projection_v2.0 (prediction ledger)) -- gap -13.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18BASDOU-DOU21` Will Aziz Dougaz win the Nishesh Basavareddy vs Aziz Dougaz match by a set score of 2-1?: 0.02/0.22 mid 12.0%, model 20.5% (projection_v2.0 (prediction ledger)) -- gap +8.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18BASDOU-BAS21` Will Nishesh Basavareddy win the Nishesh Basavareddy vs Aziz Dougaz match by a set score of 2-1?: 0.06/0.37 mid 21.5%, model 28.2% (projection_v2.0 (prediction ledger)) -- gap +6.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18BASDOU-DOU20` Will Aziz Dougaz win the Nishesh Basavareddy vs Aziz Dougaz match by a set score of 2-0?: 0.02/0.21 mid 11.5%, model 17.7% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Finn Murgett vs Amit Vales -- M15 Heraklion SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-18T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208818:211707:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Finn Murgett (`KXITFMATCH-26OCT18MURVAL-MUR`) | 0.38 / 0.52 (26) | 45.0% | 34.9% | 53.1% | 36.9% [36.9%-37.0%] | -- | -- | -- | -- | PASS | -10.1 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Amit Vales (`KXITFMATCH-26OCT18MURVAL-VAL`) | 0.40 / 0.53 (96) | 46.5% | 65.1% | 46.9% | 63.1% [63.0%-63.1%] | -- | -- | -- | -- | PASS | +18.6 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 397.0; serve-point win A 59.6%, B 37.4%; Elo A 1222.1, B 1315.0; model uncertainty 0.0005
* Form inputs: days since last match A 1069, B 29; matches on record A 15, B 61; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT18MURVAL-VAL  (YES = Amit Vales)
Model: 65%
Kalshi: 46%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oskari Paldanius vs Romain Faucon -- M15 Sharm ElSheikh F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209940:213619:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Romain Faucon (`KXITFMATCH-26OCT18PALFAU-FAU`) | 0.42 / 0.48 (96) | 45.0% | 35.3% | 62.5% | 39.9% [39.9%-39.9%] | -- | -- | -- | -- | PASS | -9.7 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oskari Paldanius (`KXITFMATCH-26OCT18PALFAU-PAL`) | 0.49 / 0.58 (103) | 53.5% | 64.7% | 37.5% | 60.1% [60.1%-60.1%] | -- | -- | -- | -- | PASS | +11.2 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 177.0, B 0.0; serve-point win A 62.9%, B 40.0%; Elo A 1264.6, B 1193.3; model uncertainty 0.0002
* Form inputs: days since last match A 89, B 726; matches on record A 7, B 75; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carolina Alves vs Alena Kovackova -- W50 Stara Zagora SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206430:266800:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carolina Alves (`KXITFWMATCH-26OCT18ALVKOV-ALV`) | 0.16 / 0.20 (32) | 18.0% | 31.2% | 47.3% | 42.6% [38.9%-44.1%] | -- | -- | -- | -- | WATCH | +13.2 pp | REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alena Kovackova (`KXITFWMATCH-26OCT18ALVKOV-KOV`) | 0.69 / 0.84 (6344) | 76.5% | 68.8% | 52.7% | 57.4% [55.9%-61.1%] | -- | -- | -- | -- | PASS | -7.7 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3024.0, B 2074.0; serve-point win A 51.9%, B 44.4%; Elo A 1548.8, B 1650.5; model uncertainty 0.0261
* Form inputs: days since last match A 31, B 194; matches on record A 699, B 72; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Felitsata Dorofeeva-Rybas vs Giulia Safina Popa -- W15 Chisinau F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:267022:267428:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felitsata Dorofeeva-Rybas (`KXITFWMATCH-26OCT18DORPOP-DOR`) | 0.56 / 0.61 (986) | 58.5% | 39.5% | 52.7% | 44.1% [39.4%-46.2%] | -- | -- | -- | -- | PASS | -19.0 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Giulia Safina Popa (`KXITFWMATCH-26OCT18DORPOP-POP`) | 0.38 / 0.43 (44) | 40.5% | 60.5% | 47.3% | 55.9% [53.8%-60.6%] | -- | -- | -- | -- | PASS | +20.0 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 923.0, B 1013.0; serve-point win A 50.8%, B 47.2%; Elo A 1447.6, B 1526.2; model uncertainty 0.0341
* Form inputs: days since last match A 320, B 383; matches on record A 19, B 38; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18DORPOP-POP  (YES = Giulia Safina Popa)
Model: 60%
Kalshi: 40%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.016, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alisa Oktiabreva vs Tilwith Di Girolami -- W35 Heraklion F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-18T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:228910:260765:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tilwith Di Girolami (`KXITFWMATCH-26OCT18OKTDIG-DIG`) | 0.05 / 0.06 (51) | 5.5% | 10.8% | 26.4% | 20.2% [18.4%-22.2%] | -- | -- | -- | -- | WATCH | +5.3 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alisa Oktiabreva (`KXITFWMATCH-26OCT18OKTDIG-OKT`) | 0.76 / 0.94 (6265) | 85.0% | 89.1% | 73.6% | 79.8% [77.8%-81.6%] | -- | -- | -- | -- | PASS | +4.2 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1999.0, B 1533.0; serve-point win A 54.0%, B 55.2%; Elo A 1777.6, B 1473.7; model uncertainty 0.0189
* Form inputs: days since last match A 89, B 173; matches on record A 67, B 202; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.004, surface_dev_loose -0.004, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ipek Oz vs Lucie Petruzelova -- W50 Stara Zagora SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213998:221219:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ipek Oz (`KXITFWMATCH-26OCT18OZXPET-OZX`) | 0.63 / 0.81 (6503) | 72.0% | 88.4% | 63.0% | 76.4% [72.5%-82.5%] | -- | -- | -- | -- | PASS | +16.4 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lucie Petruzelova (`KXITFWMATCH-26OCT18OZXPET-PET`) | 0.19 / 0.23 (33) | 21.0% | 11.6% | 37.0% | 23.6% [17.5%-27.5%] | -- | -- | -- | -- | PASS | -9.4 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2398.0, B 1518.0; serve-point win A 59.3%, B 49.7%; Elo A 1642.6, B 1321.0; model uncertainty 0.0495
* Form inputs: days since last match A 39, B 187; matches on record A 487, B 141; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18OZXPET-OZX  (YES = Ipek Oz)
Model: 88%
Kalshi: 72%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: WIDE_SPREAD, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuliya Perapekhina vs Lamis Alhussein Abdel Aziz -- W15 Sharm ElSheikh F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213974:266528:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lamis Alhussein Abdel Aziz (`KXITFWMATCH-26OCT18PERALH-ALH`) | 0.20 / 0.27 (68) | 23.5% | 87.7% | 94.5% | 84.5% [81.8%-86.9%] | -- | -- | -- | -- | PASS | +64.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuliya Perapekhina (`KXITFWMATCH-26OCT18PERALH-PER`) | 0.50 / 0.77 (83) | 63.5% | 12.3% | 5.5% | 15.5% [13.1%-18.2%] | -- | -- | -- | -- | PASS | -51.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 77.0, B 4747.0; serve-point win A 49.8%, B 41.5%; Elo A 1316.3, B 1601.9; model uncertainty 0.0254
* Form inputs: days since last match A 516, B 180; matches on record A 10, B 518; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18PERALH-ALH  (YES = Lamis Alhussein Abdel Aziz)
Model: 88%
Kalshi: 24%
Gap: +64 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.024, surface_pool_high +0.027, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Guido Andreozzi / Manuel Guinard vs Michael Geerts / Joran Vliegen -- ATP Brussels R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18ANDGUIGEEVLI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Guido Andreozzi / Manuel Guinard (`KXATPDOUBLES-26OCT18ANDGUIGEEVLI-ANDGUI`) | 0.06 / 0.90 (10) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Michael Geerts / Joran Vliegen (`KXATPDOUBLES-26OCT18ANDGUIGEEVLI-GEEVLI`) | 0.06 / 0.90 (10) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Sander Arends / Luke Johnson vs Orlando Luz / Rafael Matos -- ATP Brussels R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18AREJOHLUZMAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sander Arends / Luke Johnson (`KXATPDOUBLES-26OCT18AREJOHLUZMAT-AREJOH`) | 0.06 / 0.89 (5) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Orlando Luz / Rafael Matos (`KXATPDOUBLES-26OCT18AREJOHLUZMAT-LUZMAT`) | 0.06 / 0.89 (5) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nicolas Barrientos / David Pel vs Marcelo Melo / John-Patrick Smith -- ATP Brussels R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18BARPELMELSMI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Barrientos / David Pel (`KXATPDOUBLES-26OCT18BARPELMELSMI-BARPEL`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marcelo Melo / John-Patrick Smith (`KXATPDOUBLES-26OCT18BARPELMELSMI-MELSMI`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Finnian Bult vs Sam Kydd Baumgartner -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18BULBAU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sam Kydd Baumgartner (`KXITFMATCH-26OCT18BULBAU-BAU`) | 0.07 / 0.96 (22) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Finnian Bult (`KXITFMATCH-26OCT18BULBAU-BUL`) | 0.05 / 0.95 (30) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Francisco Cerundolo / Alex Michelsen vs Zizou Bergs / Alexander Blockx -- ATP Brussels R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18CERMICBERBLO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zizou Bergs / Alexander Blockx (`KXATPDOUBLES-26OCT18CERMICBERBLO-BERBLO`) | 0.18 / 0.90 (10) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Francisco Cerundolo / Alex Michelsen (`KXATPDOUBLES-26OCT18CERMICBERBLO-CERMIC`) | 0.05 / 0.89 (3) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Raphael Collignon / David Goffin vs Marc Polmans / Jan Zielinski -- ATP Brussels R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18COLGOFPOLZIE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raphael Collignon / David Goffin (`KXATPDOUBLES-26OCT18COLGOFPOLZIE-COLGOF`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marc Polmans / Jan Zielinski (`KXATPDOUBLES-26OCT18COLGOFPOLZIE-POLZIE`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Congsup Congcar vs Natthayut Nithithananont -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:133667:209396:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Congsup Congcar (`KXITFMATCH-26OCT18CONNIT-CON`) | 0.06 / 0.96 (22) | 51.0% | 62.7% | 45.9% | 50.0% [49.0%-51.0%] | -- | -- | -- | -- | PASS | +11.7 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Natthayut Nithithananont (`KXITFMATCH-26OCT18CONNIT-NIT`) | 0.03 / 0.96 (28) | 49.5% | 37.3% | 54.1% | 50.0% [49.0%-51.0%] | -- | -- | -- | -- | PASS | -12.2 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 54.0, B 43.0; serve-point win A 62.8%, B 39.8%; Elo A 1124.6, B 1124.8; model uncertainty 0.0102
* Form inputs: days since last match A 978, B 719; matches on record A 113, B 13; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sadio Doumbia / Bart Stevens vs Maximo Gonzalez / Andres Molteni -- ATP Brussels R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18DOUSTEGONMOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sadio Doumbia / Bart Stevens (`KXATPDOUBLES-26OCT18DOUSTEGONMOL-DOUSTE`) | 0.06 / 0.90 (10) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maximo Gonzalez / Andres Molteni (`KXATPDOUBLES-26OCT18DOUSTEGONMOL-GONMOL`) | 0.06 / 0.90 (10) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jacob Fearnley vs Hugo Gaston -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200384:207985:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jacob Fearnley (`KXATPMATCH-26OCT18FEAGAS-FEA`) | 0.66 / 0.67 (363) | 66.5% | 58.6% | 55.6% | 55.6% [53.6%-57.2%] | -- | 69.9% | -- | INSUFFICIENT_INPUTS | PASS | -7.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hugo Gaston (`KXATPMATCH-26OCT18FEAGAS-GAS`) | 0.32 / 0.34 (8409) | 33.0% | 41.4% | 44.4% | 44.4% [42.8%-46.4%] | -- | 30.6% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +8.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4058.0, B 4582.0; serve-point win A 61.0%, B 40.6%; Elo A 1773.0, B 1728.8; model uncertainty 0.0179
* Form inputs: days since last match A 19, B 12; matches on record A 178, B 502; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose -0.005, surface_dev_tight +0.010
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT18FEAGAS-GAS21` Will Hugo Gaston win the Jacob Fearnley vs Hugo Gaston match by a set score of 2-1?: 0.01/0.17 mid 9.0%, model 21.8% (projection_v2.0 (prediction ledger)) -- gap +12.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18FEAGAS-GAS2` Will Hugo Gaston win at least 1.5 more games than Jacob Fearnley?: 0.18/0.27 mid 22.5%, model 34.7% (projection_v2.0 (prediction ledger)) -- gap +12.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18FEAGAS-2-GAS` Will Hugo Gaston win set 2 in the Jacob Fearnley vs Hugo Gaston match: 0.26/0.39 mid 32.5%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT18FEAGAS-FEA4` Will Jacob Fearnley win at least 3.5 more games than Hugo Gaston?: 0.45/0.50 mid 47.5%, model 36.2% (projection_v2.0 (prediction ledger)) -- gap -11.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18FEAGAS-FEA21` Will Jacob Fearnley win the Jacob Fearnley vs Hugo Gaston match by a set score of 2-1?: 0.06/0.27 mid 16.5%, model 27.5% (projection_v2.0 (prediction ledger)) -- gap +11.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18FEAGAS-GAS20` Will Hugo Gaston win the Jacob Fearnley vs Hugo Gaston match by a set score of 2-0?: 0.01/0.19 mid 10.0%, model 19.6% (projection_v2.0 (prediction ledger)) -- gap +9.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18FEAGAS-18` Over 17.5 games: 0.66/0.99 mid 82.5%, model 90.3% (projection_v2.0 (prediction ledger)) -- gap +7.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18FEAGAS-1-GAS` Will Hugo Gaston win set 1 in the Jacob Fearnley vs Hugo Gaston match: 0.34/0.39 mid 36.5%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18FEAGAS-23` Over 22.5 games: 0.48/0.52 mid 50.0%, model 57.7% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18FEAGAS-2-FEA` Will Jacob Fearnley win set 2 in the Jacob Fearnley vs Hugo Gaston match: 0.60/0.66 mid 63.0%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap -7.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18FEAGAS-1-FEA` Will Jacob Fearnley win set 1 in the Jacob Fearnley vs Hugo Gaston match: 0.55/0.66 mid 60.5%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap -4.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18FEAGAS-FEA20` Will Jacob Fearnley win the Jacob Fearnley vs Hugo Gaston match by a set score of 2-0?: 0.25/0.46 mid 35.5%, model 31.1% (projection_v2.0 (prediction ledger)) -- gap -4.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18FEAGAS-28` Over 27.5 games: 0.12/0.53 mid 32.5%, model 36.9% (projection_v2.0 (prediction ledger)) -- gap +4.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tallon Griekspoor vs Max Schoenhaus -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:134868:212268:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tallon Griekspoor (`KXATPMATCH-26OCT18GRISCH-GRI`) | 0.78 / 0.79 (99) | 78.5% | 80.0% | 72.1% | 83.3% [77.7%-89.4%] | -- | 78.8% | -- | INSUFFICIENT_INPUTS | WATCH | +1.5 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Max Schoenhaus (`KXATPMATCH-26OCT18GRISCH-SCH`) | 0.20 / 0.21 (84) | 20.5% | 20.0% | 27.9% | 16.7% [10.6%-22.3%] | -- | 21.0% | -- | INSUFFICIENT_INPUTS | PASS | -0.5 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4445.0, B 1578.0; serve-point win A 71.4%, B 35.6%; Elo A 1871.5, B 1465.9; model uncertainty 0.0584
* Form inputs: days since last match A 9, B 33; matches on record A 677, B 52; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.023, surface_pool_high -0.028, surface_dev_loose +0.002, surface_dev_tight -0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT18GRISCH-GRI21` Will Tallon Griekspoor win the Tallon Griekspoor vs Max Schoenhaus match by a set score of 2-1?: 0.06/0.26 mid 16.0%, model 29.2% (projection_v2.0 (prediction ledger)) -- gap +13.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18GRISCH-18` Over 17.5 games: 0.68/0.99 mid 83.5%, model 93.6% (projection_v2.0 (prediction ledger)) -- gap +10.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18GRISCH-23` Over 22.5 games: 0.47/0.52 mid 49.5%, model 56.6% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18GRISCH-GRI4` Will Tallon Griekspoor win at least 3.5 more games than Max Schoenhaus?: 0.53/0.55 mid 54.0%, model 48.6% (projection_v2.0 (prediction ledger)) -- gap -5.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18GRISCH-GRI20` Will Tallon Griekspoor win the Tallon Griekspoor vs Max Schoenhaus match by a set score of 2-0?: 0.35/0.57 mid 46.0%, model 50.8% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18GRISCH-SCH21` Will Max Schoenhaus win the Tallon Griekspoor vs Max Schoenhaus match by a set score of 2-1?: 0.01/0.13 mid 7.0%, model 11.8% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18GRISCH-28` Over 27.5 games: 0.11/0.52 mid 31.5%, model 36.2% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18GRISCH-GRI7` Will Tallon Griekspoor win at least 6.5 more games than Max Schoenhaus?: 0.05/0.15 mid 10.0%, model 7.6% (projection_v2.0 (prediction ledger)) -- gap -2.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18GRISCH-1-SCH` Will Max Schoenhaus win set 1 in the Tallon Griekspoor vs Max Schoenhaus match: 0.09/0.44 mid 26.5%, model 28.7% (projection_v2.0 (prediction ledger)) -- gap +2.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18GRISCH-2-SCH` Will Max Schoenhaus win set 2 in the Tallon Griekspoor vs Max Schoenhaus match: 0.08/0.45 mid 26.5%, model 28.7% (projection_v2.0 (prediction ledger)) -- gap +2.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18GRISCH-SCH20` Will Max Schoenhaus win the Tallon Griekspoor vs Max Schoenhaus match by a set score of 2-0?: 0.01/0.12 mid 6.5%, model 8.2% (projection_v2.0 (prediction ledger)) -- gap +1.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18GRISCH-SCH2` Will Max Schoenhaus win at least 1.5 more games than Tallon Griekspoor?: 0.14/0.18 mid 16.0%, model 14.5% (projection_v2.0 (prediction ledger)) -- gap -1.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18GRISCH-1-GRI` Will Tallon Griekspoor win set 1 in the Tallon Griekspoor vs Max Schoenhaus match: 0.54/0.86 mid 70.0%, model 71.3% (projection_v2.0 (prediction ledger)) -- gap +1.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18GRISCH-2-GRI` Will Tallon Griekspoor win set 2 in the Tallon Griekspoor vs Max Schoenhaus match: 0.53/0.90 mid 71.5%, model 71.3% (projection_v2.0 (prediction ledger)) -- gap -0.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tallon Griekspoor / Botic Van de Zandschulp vs Juan Manuel Cerundolo / Benjamin Kittay -- ATP Brussels R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18GRIVANCERKIT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Manuel Cerundolo / Benjamin Kittay (`KXATPDOUBLES-26OCT18GRIVANCERKIT-CERKIT`) | 0.06 / 0.90 (10) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tallon Griekspoor / Botic Van de Zandschulp (`KXATPDOUBLES-26OCT18GRIVANCERKIT-GRIVAN`) | 0.06 / 0.90 (10) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Mariano Navone vs Juan Manuel Cerundolo -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207678:208363:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Manuel Cerundolo (`KXATPMATCH-26OCT18NAVCER-CER`) | 0.38 / 0.39 (363) | 38.5% | 46.6% | 36.5% | 40.4% [38.9%-42.9%] | -- | 40.9% | -- | INSUFFICIENT_INPUTS | PASS | +8.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mariano Navone (`KXATPMATCH-26OCT18NAVCER-NAV`) | 0.59 / 0.60 (5) | 59.5% | 53.4% | 63.5% | 59.6% [57.1%-61.1%] | -- | 59.1% | -- | INSUFFICIENT_INPUTS | PASS | -6.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5176.0, B 5332.0; serve-point win A 61.9%, B 38.8%; Elo A 1725.4, B 1754.7; model uncertainty 0.0199
* Form inputs: days since last match A 9, B 7; matches on record A 410, B 506; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.015, surface_dev_loose -0.001, surface_dev_tight -0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT18NAVCER-CER21` Will Juan Manuel Cerundolo win the Mariano Navone vs Juan Manuel Cerundolo match by a set score of 2-1?: 0.01/0.20 mid 10.5%, model 23.8% (projection_v2.0 (prediction ledger)) -- gap +13.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18NAVCER-NAV6` Will Mariano Navone win at least 5.5 more games than Juan Manuel Cerundolo?: 0.05/0.42 mid 23.5%, model 11.8% (projection_v2.0 (prediction ledger)) -- gap -11.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18NAVCER-NAV21` Will Mariano Navone win the Mariano Navone vs Juan Manuel Cerundolo match by a set score of 2-1?: 0.04/0.26 mid 15.0%, model 26.1% (projection_v2.0 (prediction ledger)) -- gap +11.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18NAVCER-18` Over 17.5 games: 0.64/0.99 mid 81.5%, model 91.8% (projection_v2.0 (prediction ledger)) -- gap +10.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18NAVCER-23` Over 22.5 games: 0.47/0.52 mid 49.5%, model 59.3% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18NAVCER-NAV3` Will Mariano Navone win at least 2.5 more games than Juan Manuel Cerundolo?: 0.46/0.52 mid 49.0%, model 39.7% (projection_v2.0 (prediction ledger)) -- gap -9.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18NAVCER-CER20` Will Juan Manuel Cerundolo win the Mariano Navone vs Juan Manuel Cerundolo match by a set score of 2-0?: 0.03/0.25 mid 14.0%, model 22.8% (projection_v2.0 (prediction ledger)) -- gap +8.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18NAVCER-28` Over 27.5 games: 0.11/0.52 mid 31.5%, model 38.7% (projection_v2.0 (prediction ledger)) -- gap +7.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18NAVCER-CER2` Will Juan Manuel Cerundolo win at least 1.5 more games than Mariano Navone?: 0.30/0.38 mid 34.0%, model 39.5% (projection_v2.0 (prediction ledger)) -- gap +5.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18NAVCER-1-CER` Will Juan Manuel Cerundolo win set 1 in the Mariano Navone vs Juan Manuel Cerundolo match: 0.25/0.60 mid 42.5%, model 47.7% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18NAVCER-2-CER` Will Juan Manuel Cerundolo win set 2 in the Mariano Navone vs Juan Manuel Cerundolo match: 0.39/0.46 mid 42.5%, model 47.7% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18NAVCER-2-NAV` Will Mariano Navone win set 2 in the Mariano Navone vs Juan Manuel Cerundolo match: 0.53/0.60 mid 56.5%, model 52.3% (projection_v2.0 (prediction ledger)) -- gap -4.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18NAVCER-1-NAV` Will Mariano Navone win set 1 in the Mariano Navone vs Juan Manuel Cerundolo match: 0.37/0.73 mid 55.0%, model 52.3% (projection_v2.0 (prediction ledger)) -- gap -2.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18NAVCER-NAV20` Will Mariano Navone win the Mariano Navone vs Juan Manuel Cerundolo match by a set score of 2-0?: 0.18/0.38 mid 28.0%, model 27.3% (projection_v2.0 (prediction ledger)) -- gap -0.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Petr Nouza / Michael Venus vs Constantin Frantzen / Robert Galloway -- ATP Brussels R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18NOUVENFRAGAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Constantin Frantzen / Robert Galloway (`KXATPDOUBLES-26OCT18NOUVENFRAGAL-FRAGAL`) | 0.18 / 0.90 (10) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Petr Nouza / Michael Venus (`KXATPDOUBLES-26OCT18NOUVENFRAGAL-NOUVEN`) | 0.06 / 0.89 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dino Prizmic vs Damir Dzumhur -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:106000:209976:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Damir Dzumhur (`KXATPMATCH-26OCT18PRIDZU-DZU`) | 0.29 / 0.31 (471) | 30.0% | 23.2% | 30.3% | 29.4% [28.5%-31.2%] | -- | 30.3% | -- | INSUFFICIENT_INPUTS | PASS | -6.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dino Prizmic (`KXATPMATCH-26OCT18PRIDZU-PRI`) | 0.67 / 0.68 (116) | 67.5% | 76.8% | 69.7% | 70.6% [68.8%-71.5%] | -- | 69.9% | -- | INSUFFICIENT_INPUTS | WATCH | +9.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3904.0, B 4752.0; serve-point win A 63.0%, B 42.6%; Elo A 1827.6, B 1664.3; model uncertainty 0.0138
* Form inputs: days since last match A 26, B 12; matches on record A 223, B 1058; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight -0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT18PRIDZU-PRI21` Will Dino Prizmic win the Dino Prizmic vs Damir Dzumhur match by a set score of 2-1?: 0.06/0.27 mid 16.5%, model 29.5% (projection_v2.0 (prediction ledger)) -- gap +13.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18PRIDZU-PRI20` Will Dino Prizmic win the Dino Prizmic vs Damir Dzumhur match by a set score of 2-0?: 0.25/0.47 mid 36.0%, model 47.3% (projection_v2.0 (prediction ledger)) -- gap +11.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18PRIDZU-PRI4` Will Dino Prizmic win at least 3.5 more games than Damir Dzumhur?: 0.45/0.52 mid 48.5%, model 55.0% (projection_v2.0 (prediction ledger)) -- gap +6.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18PRIDZU-18` Over 17.5 games: 0.61/0.99 mid 80.0%, model 86.0% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18PRIDZU-2-PRI` Will Dino Prizmic win set 2 in the Dino Prizmic vs Damir Dzumhur match: 0.47/0.80 mid 63.5%, model 68.8% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18PRIDZU-DZU21` Will Damir Dzumhur win the Dino Prizmic vs Damir Dzumhur match by a set score of 2-1?: 0.01/0.16 mid 8.5%, model 13.4% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18PRIDZU-DZU2` Will Damir Dzumhur win at least 1.5 more games than Dino Prizmic?: 0.18/0.27 mid 22.5%, model 18.1% (projection_v2.0 (prediction ledger)) -- gap -4.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18PRIDZU-1-PRI` Will Dino Prizmic win set 1 in the Dino Prizmic vs Damir Dzumhur match: 0.47/0.82 mid 64.5%, model 68.8% (projection_v2.0 (prediction ledger)) -- gap +4.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18PRIDZU-23` Over 22.5 games: 0.44/0.50 mid 47.0%, model 50.5% (projection_v2.0 (prediction ledger)) -- gap +3.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18PRIDZU-2-DZU` Will Damir Dzumhur win set 2 in the Dino Prizmic vs Damir Dzumhur match: 0.18/0.51 mid 34.5%, model 31.2% (projection_v2.0 (prediction ledger)) -- gap -3.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18PRIDZU-1-DZU` Will Damir Dzumhur win set 1 in the Dino Prizmic vs Damir Dzumhur match: 0.16/0.51 mid 33.5%, model 31.2% (projection_v2.0 (prediction ledger)) -- gap -2.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18PRIDZU-28` Over 27.5 games: 0.09/0.50 mid 29.5%, model 31.2% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18PRIDZU-DZU20` Will Damir Dzumhur win the Dino Prizmic vs Damir Dzumhur match by a set score of 2-0?: 0.01/0.17 mid 9.0%, model 9.8% (projection_v2.0 (prediction ledger)) -- gap +0.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Holger Rune vs Raphael Collignon -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208029:209920:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raphael Collignon (`KXATPMATCH-26OCT18RUNCOL-COL`) | 0.42 / 0.44 (556) | 43.0% | 38.0% | 42.7% | 38.0% [35.6%-39.8%] | -- | 45.3% | -- | INSUFFICIENT_INPUTS | PASS | -5.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Holger Rune (`KXATPMATCH-26OCT18RUNCOL-RUN`) | 0.56 / 0.58 (8160) | 57.0% | 62.0% | 57.3% | 62.0% [60.2%-64.4%] | -- | 54.3% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +5.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2551.0, B 5214.0; serve-point win A 67.0%, B 35.5%; Elo A 1972.9, B 1825.6; model uncertainty 0.021
* Form inputs: days since last match A 10, B 47; matches on record A 430, B 351; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.009, surface_dev_loose +0.004, surface_dev_tight -0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT18RUNCOL-RUN21` Will Holger Rune win the Holger Rune vs Raphael Collignon match by a set score of 2-1?: 0.04/0.24 mid 14.0%, model 28.3% (projection_v2.0 (prediction ledger)) -- gap +14.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18RUNCOL-RUN20` Will Holger Rune win the Holger Rune vs Raphael Collignon match by a set score of 2-0?: 0.12/0.34 mid 23.0%, model 33.7% (projection_v2.0 (prediction ledger)) -- gap +10.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18RUNCOL-RUN2` Will Holger Rune win at least 1.5 more games than Raphael Collignon?: 0.39/0.50 mid 44.5%, model 54.2% (projection_v2.0 (prediction ledger)) -- gap +9.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18RUNCOL-COL2` Will Raphael Collignon win at least 1.5 more games than Holger Rune?: 0.38/0.42 mid 40.0%, model 30.6% (projection_v2.0 (prediction ledger)) -- gap -9.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18RUNCOL-COL21` Will Raphael Collignon win the Holger Rune vs Raphael Collignon match by a set score of 2-1?: 0.02/0.22 mid 12.0%, model 20.4% (projection_v2.0 (prediction ledger)) -- gap +8.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18RUNCOL-20` Over 19.5 games: 0.57/0.98 mid 77.5%, model 82.9% (projection_v2.0 (prediction ledger)) -- gap +5.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18RUNCOL-25` Over 24.5 games: 0.45/0.52 mid 48.5%, model 53.9% (projection_v2.0 (prediction ledger)) -- gap +5.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18RUNCOL-2-COL` Will Raphael Collignon win set 2 in the Holger Rune vs Raphael Collignon match: 0.44/0.48 mid 46.0%, model 41.9% (projection_v2.0 (prediction ledger)) -- gap -4.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18RUNCOL-2-RUN` Will Holger Rune win set 2 in the Holger Rune vs Raphael Collignon match: 0.52/0.56 mid 54.0%, model 58.1% (projection_v2.0 (prediction ledger)) -- gap +4.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18RUNCOL-30` Over 29.5 games: 0.09/0.50 mid 29.5%, model 33.2% (projection_v2.0 (prediction ledger)) -- gap +3.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18RUNCOL-RUN5` Will Holger Rune win at least 4.5 more games than Raphael Collignon?: 0.11/0.24 mid 17.5%, model 20.7% (projection_v2.0 (prediction ledger)) -- gap +3.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18RUNCOL-1-COL` Will Raphael Collignon win set 1 in the Holger Rune vs Raphael Collignon match: 0.27/0.51 mid 39.0%, model 41.9% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18RUNCOL-COL20` Will Raphael Collignon win the Holger Rune vs Raphael Collignon match by a set score of 2-0?: 0.05/0.27 mid 16.0%, model 17.6% (projection_v2.0 (prediction ledger)) -- gap +1.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18RUNCOL-1-RUN` Will Holger Rune win set 1 in the Holger Rune vs Raphael Collignon match: 0.47/0.70 mid 58.5%, model 58.1% (projection_v2.0 (prediction ledger)) -- gap -0.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Rahul Sachdev vs Ethan David Zapp -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18SACZAP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rahul Sachdev (`KXITFMATCH-26OCT18SACZAP-SAC`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ethan David Zapp (`KXITFMATCH-26OCT18SACZAP-ZAP`) | 0.03 / 0.97 (363) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Omaansh Choudhary Saharia vs Alexander Watanabe Eriksson -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18SAHWAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Omaansh Choudhary Saharia (`KXITFMATCH-26OCT18SAHWAT-SAH`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexander Watanabe Eriksson (`KXITFMATCH-26OCT18SAHWAT-WAT`) | 0.03 / 0.97 (363) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Toby Samuel vs Zizou Bergs -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200267:210389:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zizou Bergs (`KXATPMATCH-26OCT18SAMBER-BER`) | 0.65 / 0.67 (6373) | 66.0% | 46.0% | 28.0% | 36.1% [30.6%-44.0%] | -- | 68.8% | 68.8% | ALL_THREE_DISAGREE | PASS | -20.0 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Toby Samuel (`KXATPMATCH-26OCT18SAMBER-SAM`) | 0.33 / 0.34 (59) | 33.5% | 54.0% | 72.0% | 63.8% [56.0%-69.4%] | -- | -- | -- | INSUFFICIENT_INPUTS | WATCH | +20.5 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2684.0, B 5362.0; serve-point win A 62.9%, B 37.9%; Elo A 1804.6, B 1810.8; model uncertainty 0.0666
* Form inputs: days since last match A 19, B 3; matches on record A 136, B 552; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT18SAMBER-SAM  (YES = Toby Samuel)
Model: 54%
Kalshi: 34%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.019, surface_dev_loose +0.042, surface_dev_tight -0.029
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT18SAMBER-SAM2` Will Toby Samuel win at least 1.5 more games than Zizou Bergs?: 0.24/0.32 mid 28.0%, model 46.7% (projection_v2.0 (prediction ledger)) -- gap +18.7 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18SAMBER-SAM20` Will Toby Samuel win the Toby Samuel vs Zizou Bergs match by a set score of 2-0?: 0.01/0.19 mid 10.0%, model 27.7% (projection_v2.0 (prediction ledger)) -- gap +17.7 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18SAMBER-SAM21` Will Toby Samuel win the Toby Samuel vs Zizou Bergs match by a set score of 2-1?: 0.01/0.19 mid 10.0%, model 26.2% (projection_v2.0 (prediction ledger)) -- gap +16.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18SAMBER-BER2` Will Zizou Bergs win at least 1.5 more games than Toby Samuel?: 0.49/0.59 mid 54.0%, model 38.8% (projection_v2.0 (prediction ledger)) -- gap -15.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18SAMBER-2-SAM` Will Toby Samuel win set 2 in the Toby Samuel vs Zizou Bergs match: 0.19/0.56 mid 37.5%, model 52.6% (projection_v2.0 (prediction ledger)) -- gap +15.2 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18SAMBER-1-SAM` Will Toby Samuel win set 1 in the Toby Samuel vs Zizou Bergs match: 0.21/0.56 mid 38.5%, model 52.6% (projection_v2.0 (prediction ledger)) -- gap +14.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18SAMBER-2-BER` Will Zizou Bergs win set 2 in the Toby Samuel vs Zizou Bergs match: 0.42/0.79 mid 60.5%, model 47.3% (projection_v2.0 (prediction ledger)) -- gap -13.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18SAMBER-1-BER` Will Zizou Bergs win set 1 in the Toby Samuel vs Zizou Bergs match: 0.42/0.77 mid 59.5%, model 47.3% (projection_v2.0 (prediction ledger)) -- gap -12.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18SAMBER-BER20` Will Zizou Bergs win the Toby Samuel vs Zizou Bergs match by a set score of 2-0?: 0.19/0.43 mid 31.0%, model 22.4% (projection_v2.0 (prediction ledger)) -- gap -8.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18SAMBER-BER21` Will Zizou Bergs win the Toby Samuel vs Zizou Bergs match by a set score of 2-1?: 0.06/0.27 mid 16.5%, model 23.6% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18SAMBER-31` Over 30.5 games: 0.09/0.50 mid 29.5%, model 24.2% (projection_v2.0 (prediction ledger)) -- gap -5.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18SAMBER-21` Over 20.5 games: 0.55/0.96 mid 75.5%, model 72.8% (projection_v2.0 (prediction ledger)) -- gap -2.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18SAMBER-26` Over 25.5 games: 0.45/0.50 mid 47.5%, model 48.7% (projection_v2.0 (prediction ledger)) -- gap +1.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18SAMBER-BER5` Will Zizou Bergs win at least 4.5 more games than Toby Samuel?: 0.12/0.21 mid 16.5%, model 15.4% (projection_v2.0 (prediction ledger)) -- gap -1.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jan-Lennard Struff vs Marcos Giron -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105526:106218:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcos Giron (`KXATPMATCH-26OCT18STRGIR-GIR`) | 0.36 / 0.38 (326) | 37.0% | 52.3% | 49.0% | 49.5% [44.2%-53.4%] | -- | 38.0% | -- | INSUFFICIENT_INPUTS | PASS | +15.3 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jan-Lennard Struff (`KXATPMATCH-26OCT18STRGIR-STR`) | 0.61 / 0.63 (544) | 62.0% | 47.7% | 51.0% | 50.5% [46.6%-55.8%] | -- | 61.8% | -- | INSUFFICIENT_INPUTS | PASS | -14.3 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4788.0, B 4538.0; serve-point win A 66.0%, B 33.6%; Elo A 1780.4, B 1807.1; model uncertainty 0.0462
* Form inputs: days since last match A 7, B 9; matches on record A 1054, B 707; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT18STRGIR-GIR  (YES = Marcos Giron)
Model: 52%
Kalshi: 37%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.029, surface_pool_high -0.039, surface_dev_loose -0.010, surface_dev_tight +0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPSETWINNER-26OCT18STRGIR-2-GIR` Will Marcos Giron win set 2 in the Jan-Lennard Struff vs Marcos Giron match: 0.21/0.43 mid 32.0%, model 51.5% (projection_v2.0 (prediction ledger)) -- gap +19.5 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18STRGIR-2-STR` Will Jan-Lennard Struff win set 2 in the Jan-Lennard Struff vs Marcos Giron match: 0.55/0.77 mid 66.0%, model 48.5% (projection_v2.0 (prediction ledger)) -- gap -17.5 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18STRGIR-GIR21` Will Marcos Giron win the Jan-Lennard Struff vs Marcos Giron match by a set score of 2-1?: 0.01/0.18 mid 9.5%, model 25.7% (projection_v2.0 (prediction ledger)) -- gap +16.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18STRGIR-STR3` Will Jan-Lennard Struff win at least 2.5 more games than Marcos Giron?: 0.46/0.50 mid 48.0%, model 32.0% (projection_v2.0 (prediction ledger)) -- gap -16.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18STRGIR-GIR20` Will Marcos Giron win the Jan-Lennard Struff vs Marcos Giron match by a set score of 2-0?: 0.01/0.22 mid 11.5%, model 26.6% (projection_v2.0 (prediction ledger)) -- gap +15.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18STRGIR-GIR2` Will Marcos Giron win at least 1.5 more games than Jan-Lennard Struff?: 0.29/0.33 mid 31.0%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap +13.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18STRGIR-1-GIR` Will Marcos Giron win set 1 in the Jan-Lennard Struff vs Marcos Giron match: 0.20/0.58 mid 39.0%, model 51.5% (projection_v2.0 (prediction ledger)) -- gap +12.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18STRGIR-1-STR` Will Jan-Lennard Struff win set 1 in the Jan-Lennard Struff vs Marcos Giron match: 0.40/0.77 mid 58.5%, model 48.5% (projection_v2.0 (prediction ledger)) -- gap -10.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18STRGIR-19` Over 18.5 games: 0.65/0.99 mid 82.0%, model 91.5% (projection_v2.0 (prediction ledger)) -- gap +9.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18STRGIR-STR21` Will Jan-Lennard Struff win the Jan-Lennard Struff vs Marcos Giron match by a set score of 2-1?: 0.07/0.26 mid 16.5%, model 24.2% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18STRGIR-24` Over 23.5 games: 0.47/0.52 mid 49.5%, model 56.5% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18STRGIR-29` Over 28.5 games: 0.13/0.54 mid 33.5%, model 39.5% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18STRGIR-STR20` Will Jan-Lennard Struff win the Jan-Lennard Struff vs Marcos Giron match by a set score of 2-0?: 0.18/0.40 mid 29.0%, model 23.5% (projection_v2.0 (prediction ledger)) -- gap -5.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Botic Van de Zandschulp vs Kamil Majchrzak -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111794:122298:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kamil Majchrzak (`KXATPMATCH-26OCT18VANMAJ-MAJ`) | 0.37 / 0.39 (363) | 38.0% | 38.0% | 41.0% | 40.0% [39.0%-41.5%] | -- | 40.3% | -- | INSUFFICIENT_INPUTS | PASS | +0.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Botic Van de Zandschulp (`KXATPMATCH-26OCT18VANMAJ-VAN`) | 0.61 / 0.62 (128) | 61.5% | 62.0% | 59.0% | 60.0% [58.5%-61.0%] | -- | 59.8% | -- | INSUFFICIENT_INPUTS | PASS | +0.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5172.0, B 4319.0; serve-point win A 63.7%, B 38.7%; Elo A 1902.6, B 1803.8; model uncertainty 0.0123
* Form inputs: days since last match A 3, B 10; matches on record A 618, B 674; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose +0.010, surface_dev_tight -0.015
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT18VANMAJ-VAN21` Will Botic Van de Zandschulp win the Botic Van de Zandschulp vs Kamil Majchrzak match by a set score of 2-1?: 0.06/0.26 mid 16.0%, model 28.3% (projection_v2.0 (prediction ledger)) -- gap +12.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18VANMAJ-MAJ21` Will Kamil Majchrzak win the Botic Van de Zandschulp vs Kamil Majchrzak match by a set score of 2-1?: 0.02/0.20 mid 11.0%, model 20.4% (projection_v2.0 (prediction ledger)) -- gap +9.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18VANMAJ-VAN2` Will Botic Van de Zandschulp win at least 1.5 more games than Kamil Majchrzak?: 0.34/0.57 mid 45.5%, model 54.8% (projection_v2.0 (prediction ledger)) -- gap +9.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18VANMAJ-31` Over 30.5 games: 0.10/0.51 mid 30.5%, model 23.4% (projection_v2.0 (prediction ledger)) -- gap -7.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18VANMAJ-2-MAJ` Will Kamil Majchrzak win set 2 in the Botic Van de Zandschulp vs Kamil Majchrzak match: 0.25/0.45 mid 35.0%, model 42.0% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18VANMAJ-VAN20` Will Botic Van de Zandschulp win the Botic Van de Zandschulp vs Kamil Majchrzak match by a set score of 2-0?: 0.17/0.39 mid 28.0%, model 33.7% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18VANMAJ-MAJ20` Will Kamil Majchrzak win the Botic Van de Zandschulp vs Kamil Majchrzak match by a set score of 2-0?: 0.03/0.24 mid 13.5%, model 17.6% (projection_v2.0 (prediction ledger)) -- gap +4.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18VANMAJ-21` Over 20.5 games: 0.55/0.96 mid 75.5%, model 71.6% (projection_v2.0 (prediction ledger)) -- gap -3.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18VANMAJ-1-VAN` Will Botic Van de Zandschulp win set 1 in the Botic Van de Zandschulp vs Kamil Majchrzak match: 0.39/0.74 mid 56.5%, model 58.0% (projection_v2.0 (prediction ledger)) -- gap +1.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT18VANMAJ-MAJ2` Will Kamil Majchrzak win at least 1.5 more games than Botic Van de Zandschulp?: 0.13/0.51 mid 32.0%, model 31.2% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18VANMAJ-2-VAN` Will Botic Van de Zandschulp win set 2 in the Botic Van de Zandschulp vs Kamil Majchrzak match: 0.54/0.61 mid 57.5%, model 58.0% (projection_v2.0 (prediction ledger)) -- gap +0.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18VANMAJ-26` Over 25.5 games: 0.45/0.51 mid 48.0%, model 47.5% (projection_v2.0 (prediction ledger)) -- gap -0.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18VANMAJ-1-MAJ` Will Kamil Majchrzak win set 1 in the Botic Van de Zandschulp vs Kamil Majchrzak match: 0.24/0.59 mid 41.5%, model 42.0% (projection_v2.0 (prediction ledger)) -- gap +0.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Azuma Visaya vs Clemens Cserni -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18VISCSE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Clemens Cserni (`KXITFMATCH-26OCT18VISCSE-CSE`) | 0.04 / 0.95 (69) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Azuma Visaya (`KXITFMATCH-26OCT18VISCSE-VIS`) | 0.03 / 0.97 (363) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Martin Damm Jr vs Andrea Guerrieri -- ATP Brussels Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 17:00Z
* Current expected start: 2026-10-18 14:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 20:46Z
* Recommended handicap-by time: 2026-10-18 13:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:102093:200462:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martin Damm Jr (`KXATPMATCH-26OCT18DAMGUE-DAM`) | 0.69 / 0.72 (14121) | 70.5% | 44.9% | 38.4% | 44.6% [41.8%-52.0%] | -- | 69.7% | -- | INSUFFICIENT_INPUTS | PASS | -25.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Andrea Guerrieri (`KXATPMATCH-26OCT18DAMGUE-GUE`) | 0.28 / 0.31 (6106) | 29.5% | 55.1% | 61.6% | 55.4% [48.0%-58.2%] | -- | 30.3% | -- | INSUFFICIENT_INPUTS | PASS | +25.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3075.0, B 2272.0; serve-point win A 65.3%, B 33.7%; Elo A 1594.2, B 1563.8; model uncertainty 0.0513
* Form inputs: days since last match A 726, B 19; matches on record A 252, B 345; data quality F

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT18DAMGUE-GUE  (YES = Andrea Guerrieri)
Model: 55%
Kalshi: 30%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.024, surface_pool_high +0.024, surface_dev_loose -0.019, surface_dev_tight +0.009
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT18DAMGUE-DAM20` Will Martin Damm Jr win the Martin Damm Jr vs Andrea Guerrieri match by a set score of 2-0?: 0.24/0.65 mid 44.5%, model 21.7% (projection_v2.0 (prediction ledger)) -- gap -22.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data POOR
  * `KXATPSETWINNER-26OCT18DAMGUE-1-GUE` Will Andrea Guerrieri win set 1 in the Martin Damm Jr vs Andrea Guerrieri match: 0.32/0.35 mid 33.5%, model 53.4% (projection_v2.0 (prediction ledger)) -- gap +19.9 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT18DAMGUE-2-GUE` Will Andrea Guerrieri win set 2 in the Martin Damm Jr vs Andrea Guerrieri match: 0.32/0.36 mid 34.0%, model 53.4% (projection_v2.0 (prediction ledger)) -- gap +19.4 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT18DAMGUE-1-DAM` Will Martin Damm Jr win set 1 in the Martin Damm Jr vs Andrea Guerrieri match: 0.63/0.68 mid 65.5%, model 46.6% (projection_v2.0 (prediction ledger)) -- gap -18.9 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT18DAMGUE-2-DAM` Will Martin Damm Jr win set 2 in the Martin Damm Jr vs Andrea Guerrieri match: 0.63/0.68 mid 65.5%, model 46.6% (projection_v2.0 (prediction ledger)) -- gap -18.9 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPEXACTMATCH-26OCT18DAMGUE-GUE21` Will Andrea Guerrieri win the Martin Damm Jr vs Andrea Guerrieri match by a set score of 2-1?: 0.07/0.34 mid 20.5%, model 26.6% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
  * `KXATPEXACTMATCH-26OCT18DAMGUE-DAM21` Will Martin Damm Jr win the Martin Damm Jr vs Andrea Guerrieri match by a set score of 2-1?: 0.07/0.46 mid 26.5%, model 23.2% (projection_v2.0 (prediction ledger)) -- gap -3.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
* Warnings: ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nolan / Perego vs Walters / Wright -- M15 Heraklion F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-18T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18NOLPERWALWRI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nolan / Perego (`KXITFDOUBLES-26OCT18NOLPERWALWRI-NOLPER`) | 0.05 / 0.95 (105) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Walters / Wright (`KXITFDOUBLES-26OCT18NOLPERWALWRI-WALWRI`) | 0.05 / 0.95 (105) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Lukas Pokorny vs Pietro Orlando Fellin -- M15 Szabolcsveresmart F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209165:209931:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pietro Orlando Fellin (`KXITFMATCH-26OCT18POKFEL-FEL`) | 0.35 / 0.46 (46) | 40.5% | 27.3% | 60.5% | 24.7% [23.1%-26.4%] | -- | -- | -- | -- | PASS | -13.2 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Lukas Pokorny (`KXITFMATCH-26OCT18POKFEL-POK`) | 0.23 / 0.56 (43) | 39.5% | 72.7% | 39.5% | 75.3% [73.7%-76.9%] | -- | -- | -- | -- | PASS | +33.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 740.0, B 0.0; serve-point win A 64.8%, B 39.9%; Elo A 1457.0, B 1264.7; model uncertainty 0.0165
* Form inputs: days since last match A 40, B 691; matches on record A 210, B 45; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT18POKFEL-POK  (YES = Lukas Pokorny)
Model: 73%
Kalshi: 40%
Gap: +33 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.016, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Martin Riu vs Leonardo Borrelli -- M25 Sarreguemines R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18RIUBOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leonardo Borrelli (`KXITFMATCH-26OCT18RIUBOR-BOR`) | 0.04 / 0.87 (192) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Martin Riu (`KXITFMATCH-26OCT18RIUBOR-RIU`) | 0.03 / 0.96 (675) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elijah Sanogo vs Andre Megrabian -- M25 Sarreguemines R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18SANMEG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andre Megrabian (`KXITFMATCH-26OCT18SANMEG-MEG`) | 0.04 / 0.93 (407) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Elijah Sanogo (`KXITFMATCH-26OCT18SANMEG-SAN`) | 0.03 / 0.96 (675) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Antoine Walch vs James Beaven -- M25 Sarreguemines R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126505:212536:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| James Beaven (`KXITFMATCH-26OCT18WALBEA-BEA`) | 0.04 / 0.93 (407) | 48.5% | 36.6% | 50.0% | 43.9% [43.9%-43.9%] | -- | -- | -- | -- | PASS | -11.9 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Antoine Walch (`KXITFMATCH-26OCT18WALBEA-WAL`) | 0.03 / 0.96 (675) | 49.5% | 63.4% | 50.0% | 56.1% [56.1%-56.1%] | -- | -- | -- | -- | PASS | +13.9 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 63.3%, B 39.4%; Elo A 1201.8, B 1161.8; model uncertainty 0.0
* Form inputs: days since last match A 817, B 677; matches on record A 65, B 7; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jiangxue HAN vs jiale Zhang -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220497:260795:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jiangxue HAN (`KXITFWMATCH-26OCT18HANZHA-HAN`) | 0.04 / 0.96 (22) | 50.0% | 92.6% | 42.5% | 85.2% [84.0%-85.9%] | -- | -- | -- | -- | PASS | +42.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| jiale Zhang (`KXITFWMATCH-26OCT18HANZHA-ZHA`) | 0.03 / 0.95 (27) | 49.0% | 7.4% | 57.5% | 14.8% [14.1%-16.0%] | -- | -- | -- | -- | PASS | -41.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1410.0, B 0.0; serve-point win A 56.0%, B 54.8%; Elo A 1458.9, B 1157.5; model uncertainty 0.0094
* Form inputs: days since last match A 173, B 733; matches on record A 174, B 68; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18HANZHA-HAN  (YES = Jiangxue HAN)
Model: 93%
Kalshi: 50%
Gap: +43 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.006, surface_pool_high -0.013, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jessica Pieri vs Nina Radovanovic -- W35 Santa Margherita di Pula F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-18T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213620:222602:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jessica Pieri (`KXITFWMATCH-26OCT18PIERAD-PIE`) | 0.33 / 0.52 (27) | 42.5% | 81.3% | 45.2% | 66.6% [60.6%-72.3%] | -- | -- | -- | -- | PASS | +38.8 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nina Radovanovic (`KXITFWMATCH-26OCT18PIERAD-RAD`) | 0.39 / 0.53 (184) | 46.0% | 18.7% | 54.8% | 33.4% [27.7%-39.4%] | -- | -- | -- | -- | PASS | -27.3 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2683.0, B 976.0; serve-point win A 54.9%, B 51.7%; Elo A 1618.6, B 1386.2; model uncertainty 0.0583
* Form inputs: days since last match A 21, B 173; matches on record A 508, B 247; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18PIERAD-PIE  (YES = Jessica Pieri)
Model: 81%
Kalshi: 42%
Gap: +39 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.029, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuhan Wang vs Jiayue Pan -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18WANPAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jiayue Pan (`KXITFWMATCH-26OCT18WANPAN-PAN`) | 0.04 / 0.53 (54) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yuhan Wang (`KXITFWMATCH-26OCT18WANPAN-WAN`) | 0.23 / 0.97 (213) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carolann Delaunay vs Liv Boulard -- W50 Cherbourg-en-Cotentin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:246480:260185:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liv Boulard (`KXITFWMATCH-26OCT18DELBOU-BOU`) | 0.04 / 0.86 (53) | 45.0% | 65.1% | 66.5% | 54.8% [52.7%-57.9%] | -- | -- | -- | -- | PASS | +20.1 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carolann Delaunay (`KXITFWMATCH-26OCT18DELBOU-DEL`) | 0.03 / 0.96 (675) | 49.5% | 34.8% | 33.5% | 45.2% [42.1%-47.3%] | -- | -- | -- | -- | PASS | -14.7 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 628.0, B 476.0; serve-point win A 52.9%, B 44.2%; Elo A 1235.3, B 1244.6; model uncertainty 0.0263
* Form inputs: days since last match A 180, B 103; matches on record A 85, B 50; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18DELBOU-BOU  (YES = Liv Boulard)
Model: 65%
Kalshi: 45%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.005, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gina Marie Dittmann vs Evita Ramirez -- W50 Cherbourg-en-Cotentin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221522:222273:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gina Marie Dittmann (`KXITFWMATCH-26OCT18DITRAM-DIT`) | 0.04 / 0.89 (36) | 46.5% | 87.2% | 55.9% | 71.7% [68.5%-77.3%] | -- | -- | -- | -- | PASS | +40.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Evita Ramirez (`KXITFWMATCH-26OCT18DITRAM-RAM`) | 0.03 / 0.96 (675) | 49.5% | 12.8% | 44.1% | 28.3% [22.7%-31.5%] | -- | -- | -- | -- | PASS | -36.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1885.0, B 116.0; serve-point win A 58.0%, B 50.5%; Elo A 1412.4, B 1236.8; model uncertainty 0.044
* Form inputs: days since last match A 194, B 726; matches on record A 115, B 133; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18DITRAM-DIT  (YES = Gina Marie Dittmann)
Model: 87%
Kalshi: 46%
Gap: +41 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.039, surface_pool_high -0.032, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Clara Vlasselaer vs Hanna Bougouffa -- W50 Cherbourg-en-Cotentin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221003:230121:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hanna Bougouffa (`KXITFWMATCH-26OCT18VLABOU-BOU`) | 0.04 / 0.87 (192) | 45.5% | 13.5% | 30.9% | 24.8% [22.0%-27.3%] | -- | -- | -- | -- | PASS | -32.0 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Clara Vlasselaer (`KXITFWMATCH-26OCT18VLABOU-VLA`) | 0.03 / 0.96 (675) | 49.5% | 86.5% | 69.1% | 75.2% [72.7%-78.0%] | -- | -- | -- | -- | PASS | +37.0 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1490.0, B 245.0; serve-point win A 62.2%, B 46.2%; Elo A 1481.5, B 1280.0; model uncertainty 0.0267
* Form inputs: days since last match A 173, B 446; matches on record A 332, B 134; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18VLABOU-VLA  (YES = Clara Vlasselaer)
Model: 86%
Kalshi: 50%
Gap: +37 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.025, surface_pool_high +0.024, surface_dev_loose +0.004, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Robin Bertrand vs Luca Wiedenmann -- M15 Monastir F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18BERWIE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Robin Bertrand (`KXITFMATCH-26OCT18BERWIE-BER`) | 0.29 / 0.55 (21) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luca Wiedenmann (`KXITFMATCH-26OCT18BERWIE-WIE`) | 0.35 / 0.49 (49) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Robert Dolya vs Rishabhdev Rajshekar Raman -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18DOLRAJ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Robert Dolya (`KXITFMATCH-26OCT18DOLRAJ-DOL`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rishabhdev Rajshekar Raman (`KXITFMATCH-26OCT18DOLRAJ-RAJ`) | 0.03 / 0.97 (363) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Adrien Gobat vs Romain Andres -- M25 Sarreguemines R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18GOBAND:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Romain Andres (`KXITFMATCH-26OCT18GOBAND-AND`) | 0.05 / 0.94 (488) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Adrien Gobat (`KXITFMATCH-26OCT18GOBAND-GOB`) | 0.03 / 0.96 (675) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## LUCAS GONCALVES FRANCA vs Miguel Simao -- M25 Luanda R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18GONSIM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LUCAS GONCALVES FRANCA (`KXITFMATCH-26OCT18GONSIM-GON`) | 0.05 / 0.95 (30) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Miguel Simao (`KXITFMATCH-26OCT18GONSIM-SIM`) | 0.03 / 0.97 (363) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## AARYA JADHAV vs Sparsh Rathi Rathi -- M25 Luanda R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18JADRAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AARYA JADHAV (`KXITFMATCH-26OCT18JADRAT-JAD`) | 0.70 / 0.90 (15) | 80.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sparsh Rathi Rathi (`KXITFMATCH-26OCT18JADRAT-RAT`) | 0.03 / 0.15 (15) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kazuma Kawachi vs Muthu Aadhitiya Senthilkumar -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:124074:208573:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kazuma Kawachi (`KXITFMATCH-26OCT18KAWSEN-KAW`) | 0.66 / 0.95 (30) | 80.5% | 74.3% | 34.2% | 68.5% [66.7%-70.3%] | -- | -- | -- | -- | PASS | -6.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Muthu Aadhitiya Senthilkumar (`KXITFMATCH-26OCT18KAWSEN-SEN`) | 0.03 / 0.34 (6069) | 18.5% | 25.7% | 65.8% | 31.4% [29.7%-33.3%] | -- | -- | -- | -- | PASS | +7.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 121.0, B 0.0; serve-point win A 64.4%, B 40.8%; Elo A 1178.2, B 1046.1; model uncertainty 0.018
* Form inputs: days since last match A 719, B 1552; matches on record A 220, B 23; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.018, surface_dev_loose +0.001, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alberto Morolli vs Hugo Pierre -- M25 Sarreguemines R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:145008:210272:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alberto Morolli (`KXITFMATCH-26OCT18MORPIE-MOR`) | 0.04 / 0.96 (22) | 50.0% | 31.5% | 42.4% | 49.0% [49.0%-49.0%] | -- | -- | -- | -- | PASS | -18.5 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hugo Pierre (`KXITFMATCH-26OCT18MORPIE-PIE`) | 0.03 / 0.97 (363) | 50.0% | 68.5% | 57.6% | 51.0% [51.0%-51.0%] | -- | -- | -- | -- | PASS | +18.5 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 60.0, B 0.0; serve-point win A 60.4%, B 35.8%; Elo A 1152.0, B 1159.2; model uncertainty 0.0
* Form inputs: days since last match A 698, B 677; matches on record A 15, B 43; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT18MORPIE-PIE  (YES = Hugo Pierre)
Model: 69%
Kalshi: 50%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Afonso Oliveira vs Joao Rasgado -- M25 Luanda R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18OLIRAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Afonso Oliveira (`KXITFMATCH-26OCT18OLIRAS-OLI`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Joao Rasgado (`KXITFMATCH-26OCT18OLIRAS-RAS`) | 0.03 / 0.97 (363) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amaury Raynel vs Thomas Gerbaud -- M25 Sarreguemines R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209985:212840:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thomas Gerbaud (`KXITFMATCH-26OCT18RAYGER-GER`) | 0.04 / 0.93 (407) | 48.5% | 23.2% | 52.1% | 30.1% [29.6%-30.3%] | -- | -- | -- | -- | PASS | -25.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Amaury Raynel (`KXITFMATCH-26OCT18RAYGER-RAY`) | 0.03 / 0.94 (466) | 48.5% | 76.8% | 47.9% | 69.9% [69.7%-70.4%] | -- | -- | -- | -- | PASS | +28.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 149.0, B 0.0; serve-point win A 62.1%, B 43.6%; Elo A 1387.8, B 1236.9; model uncertainty 0.0037
* Form inputs: days since last match A 397, B 782; matches on record A 158, B 9; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT18RAYGER-RAY  (YES = Amaury Raynel)
Model: 77%
Kalshi: 48%
Gap: +28 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rosie Cho vs Mayuka Aikawa -- W100 Wrexham R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18CHOAIK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mayuka Aikawa (`KXITFWMATCH-26OCT18CHOAIK-AIK`) | 0.04 / 0.93 (68) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rosie Cho (`KXITFWMATCH-26OCT18CHOAIK-CHO`) | 0.03 / 0.96 (675) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anna-Lena Friedsam vs Sophie Bekker -- W100 Wrexham R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:204431:264392:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sophie Bekker (`KXITFWMATCH-26OCT18FRIBEK-BEK`) | 0.04 / 0.91 (328) | 47.5% | 1.3% | 36.0% | 4.6% [4.3%-4.8%] | -- | -- | -- | -- | PASS | -46.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anna-Lena Friedsam (`KXITFWMATCH-26OCT18FRIBEK-FRI`) | 0.03 / 0.96 (603) | 49.5% | 98.7% | 64.0% | 95.4% [95.2%-95.7%] | -- | -- | -- | -- | PASS | +49.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3834.0, B 19.0; serve-point win A 64.6%, B 52.2%; Elo A 1767.1, B 1238.0; model uncertainty 0.0025
* Form inputs: days since last match A 5, B 432; matches on record A 669, B 10; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18FRIBEK-FRI  (YES = Anna-Lena Friedsam)
Model: 99%
Kalshi: 50%
Gap: +49 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elena Milovanovic vs Vaishnavi Adkar -- W35 Monastir F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-18T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220429:261038:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vaishnavi Adkar (`KXITFWMATCH-26OCT18MILADK-ADK`) | 0.41 / 0.69 (34) | 55.0% | 65.1% | 52.7% | 56.4% [53.2%-59.0%] | -- | -- | -- | -- | PASS | +10.1 pp | REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elena Milovanovic (`KXITFWMATCH-26OCT18MILADK-MIL`) | 0.23 / 0.50 (100) | 36.5% | 34.9% | 47.3% | 43.6% [41.0%-46.8%] | -- | -- | -- | -- | PASS | -1.6 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2475.0, B 2186.0; serve-point win A 51.6%, B 45.5%; Elo A 1435.0, B 1514.8; model uncertainty 0.0291
* Form inputs: days since last match A 180, B 173; matches on record A 299, B 143; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.026, surface_pool_high -0.021, surface_dev_loose -0.026, surface_dev_tight +0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anna Petkovic vs Tara Wuerth -- W15 Bol F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18PETWUE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Petkovic (`KXITFWMATCH-26OCT18PETWUE-PET`) | 0.13 / 0.17 (6026) | 15.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tara Wuerth (`KXITFWMATCH-26OCT18PETWUE-WUE`) | 0.72 / 0.87 (354) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Leticia Romanova vs Victoria Allen -- W100 Wrexham R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216253:266701:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Victoria Allen (`KXITFWMATCH-26OCT18ROMALL-ALL`) | 0.04 / 0.94 (488) | 49.0% | 93.6% | 67.3% | 76.9% [76.8%-77.1%] | -- | -- | -- | -- | PASS | +44.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Leticia Romanova (`KXITFWMATCH-26OCT18ROMALL-ROM`) | 0.03 / 0.96 (675) | 49.5% | 6.4% | 32.7% | 23.1% [22.9%-23.2%] | -- | -- | -- | -- | PASS | -43.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 1893.0; serve-point win A 51.7%, B 36.7%; Elo A 1276.8, B 1488.4; model uncertainty 0.0012
* Form inputs: days since last match A 978, B 140; matches on record A 1, B 83; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18ROMALL-ALL  (YES = Victoria Allen)
Model: 94%
Kalshi: 49%
Gap: +45 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amahee Charrier vs Lian Tran -- W50 Cherbourg-en-Cotentin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18CHATRA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amahee Charrier (`KXITFWMATCH-26OCT18CHATRA-CHA`) | 0.04 / 0.93 (407) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lian Tran (`KXITFWMATCH-26OCT18CHATRA-TRA`) | 0.03 / 0.84 (31) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sarah Iliev vs Severine Deppner -- W50 Cherbourg-en-Cotentin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:225858:266649:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Severine Deppner (`KXITFWMATCH-26OCT18ILIDEP-DEP`) | 0.04 / 0.93 (407) | 48.5% | 8.0% | 20.6% | 21.0% [19.9%-23.4%] | -- | -- | -- | -- | PASS | -40.5 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sarah Iliev (`KXITFWMATCH-26OCT18ILIDEP-ILI`) | 0.03 / 0.96 (603) | 49.5% | 92.0% | 79.4% | 79.0% [76.6%-80.1%] | -- | -- | -- | -- | PASS | +42.5 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1783.0, B 295.0; serve-point win A 56.6%, B 53.9%; Elo A 1486.6, B 1260.1; model uncertainty 0.0177
* Form inputs: days since last match A 187, B 285; matches on record A 157, B 45; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18ILIDEP-ILI  (YES = Sarah Iliev)
Model: 92%
Kalshi: 50%
Gap: +43 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.024, surface_dev_loose +0.008, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Helena Stevic vs Maia Ilinca Burcescu -- W50 Cherbourg-en-Cotentin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221740:267176:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maia Ilinca Burcescu (`KXITFWMATCH-26OCT18STEBUR-BUR`) | 0.04 / 0.93 (407) | 48.5% | 82.8% | 81.2% | 74.5% [71.4%-78.6%] | -- | -- | -- | -- | PASS | +34.3 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Helena Stevic (`KXITFWMATCH-26OCT18STEBUR-STE`) | 0.03 / 0.96 (675) | 49.5% | 17.2% | 18.8% | 25.5% [21.4%-28.6%] | -- | -- | -- | -- | PASS | -32.3 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1185.0, B 877.0; serve-point win A 47.4%, B 45.6%; Elo A 1282.6, B 1435.0; model uncertainty 0.0362
* Form inputs: days since last match A 173, B 81; matches on record A 178, B 30; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18STEBUR-BUR  (YES = Maia Ilinca Burcescu)
Model: 83%
Kalshi: 48%
Gap: +34 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.004, surface_dev_loose -0.000, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Baptiste BELLINELLI vs Mudiwa Munyimani -- M25 Luanda R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18BELMUN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Baptiste BELLINELLI (`KXITFMATCH-26OCT18BELMUN-BEL`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mudiwa Munyimani (`KXITFMATCH-26OCT18BELMUN-MUN`) | 0.03 / 0.97 (363) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jack Loge vs Thomas Faurel -- M25 Luanda F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211504:212225:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thomas Faurel (`KXITFMATCH-26OCT18LOGFAU-FAU`) | 0.31 / 0.62 (122) | 46.5% | 70.7% | 51.0% | 63.3% [60.8%-65.0%] | -- | -- | -- | -- | PASS | +24.2 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jack Loge (`KXITFMATCH-26OCT18LOGFAU-LOG`) | 0.27 / 0.60 (63) | 43.5% | 29.3% | 49.0% | 36.7% [35.0%-39.2%] | -- | -- | -- | -- | PASS | -14.2 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 467.0, B 1707.0; serve-point win A 56.9%, B 38.9%; Elo A 1378.5, B 1495.8; model uncertainty 0.0213
* Form inputs: days since last match A 75, B 19; matches on record A 89, B 54; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT18LOGFAU-FAU  (YES = Thomas Faurel)
Model: 71%
Kalshi: 46%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jolino Makiesse Miguel Feijo Simao vs Maita Munyimani -- M25 Luanda R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18SIMMUN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maita Munyimani (`KXITFMATCH-26OCT18SIMMUN-MUN`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jolino Makiesse Miguel Feijo Simao (`KXITFMATCH-26OCT18SIMMUN-SIM`) | 0.03 / 0.97 (363) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lizette Cabrera vs Megan Davies -- W100 Wrexham R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211878:216251:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lizette Cabrera (`KXITFWMATCH-26OCT18CABDAV-CAB`) | 0.23 / 0.94 (58) | 58.5% | 97.9% | 76.8% | 92.0% [91.6%-92.5%] | -- | -- | -- | -- | PASS | +39.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Megan Davies (`KXITFWMATCH-26OCT18CABDAV-DAV`) | 0.03 / 0.51 (51) | 27.0% | 2.1% | 23.2% | 8.0% [7.5%-8.4%] | -- | -- | -- | -- | PASS | -24.9 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3443.0, B 70.0; serve-point win A 62.6%, B 52.7%; Elo A 1687.9, B 1251.7; model uncertainty 0.0043
* Form inputs: days since last match A 26, B 369; matches on record A 524, B 11; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18CABDAV-CAB  (YES = Lizette Cabrera)
Model: 98%
Kalshi: 58%
Gap: +39 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofya Lansere vs Daniela Vismane -- W100 Wrexham R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215144:216139:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofya Lansere (`KXITFWMATCH-26OCT18LANVIS-LAN`) | 0.04 / 0.93 (407) | 48.5% | 78.4% | 89.5% | 66.1% [60.6%-74.4%] | -- | -- | -- | -- | PASS | +29.9 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daniela Vismane (`KXITFWMATCH-26OCT18LANVIS-VIS`) | 0.03 / 0.96 (675) | 49.5% | 21.6% | 10.5% | 33.9% [25.6%-39.4%] | -- | -- | -- | -- | PASS | -27.9 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3253.0, B 336.0; serve-point win A 56.1%, B 49.8%; Elo A 1594.9, B 1525.7; model uncertainty 0.0691
* Form inputs: days since last match A 15, B 173; matches on record A 351, B 354; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18LANVIS-LAN  (YES = Sofya Lansere)
Model: 78%
Kalshi: 48%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Annabel Wong vs Petra Sedlackova -- W100 Wrexham R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18WONSED:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Petra Sedlackova (`KXITFWMATCH-26OCT18WONSED-SED`) | 0.04 / 0.93 (68) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Annabel Wong (`KXITFWMATCH-26OCT18WONSED-WON`) | 0.03 / 0.96 (675) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Octave Caillat vs Timeo Trufelli -- M25 Sarreguemines R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18CAITRU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Octave Caillat (`KXITFMATCH-26OCT18CAITRU-CAI`) | 0.04 / 0.95 (550) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Timeo Trufelli (`KXITFMATCH-26OCT18CAITRU-TRU`) | 0.04 / 0.96 (675) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kenny De Schepper vs Nicolas GRY -- M25 Sarreguemines R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18DESGRY:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kenny De Schepper (`KXITFMATCH-26OCT18DESGRY-DES`) | 0.04 / 0.96 (89) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nicolas GRY (`KXITFMATCH-26OCT18DESGRY-GRY`) | 0.03 / 0.96 (625) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kristijan Juhas vs Alan Wazny -- M15 Bol F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209099:213048:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kristijan Juhas (`KXITFMATCH-26OCT18JUHWAZ-JUH`) | 0.28 / 0.65 (54) | 46.5% | 64.0% | 54.7% | 62.3% [61.4%-62.3%] | -- | -- | -- | -- | PASS | +17.5 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Alan Wazny (`KXITFMATCH-26OCT18JUHWAZ-WAZ`) | 0.31 / 0.50 (50) | 40.5% | 36.0% | 45.3% | 37.7% [37.7%-38.6%] | -- | -- | -- | -- | PASS | -4.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 252.0; serve-point win A 60.2%, B 42.6%; Elo A 1298.8, B 1217.0; model uncertainty 0.0043
* Form inputs: days since last match A 852, B 33; matches on record A 56, B 7; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT18JUHWAZ-JUH  (YES = Kristijan Juhas)
Model: 64%
Kalshi: 46%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Martin SIMON vs Florent Lagarrigue -- M25 Sarreguemines R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18SIMLAG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Florent Lagarrigue (`KXITFMATCH-26OCT18SIMLAG-LAG`) | 0.05 / 0.94 (466) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Martin SIMON (`KXITFMATCH-26OCT18SIMLAG-SIM`) | 0.03 / 0.96 (675) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Delia Gaillard vs Marine Szostak -- W50 Cherbourg-en-Cotentin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222347:238084:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Delia Gaillard (`KXITFWMATCH-26OCT18GAISZO-GAI`) | 0.04 / 0.94 (488) | 49.0% | 13.1% | 10.1% | 22.3% [15.5%-28.7%] | -- | -- | -- | -- | PASS | -35.9 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marine Szostak (`KXITFWMATCH-26OCT18GAISZO-SZO`) | 0.04 / 0.94 (421) | 49.0% | 86.9% | 90.0% | 77.7% [71.3%-84.5%] | -- | -- | -- | -- | PASS | +37.9 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 500.0, B 1767.0; serve-point win A 49.9%, B 41.7%; Elo A 1281.9, B 1449.7; model uncertainty 0.066
* Form inputs: days since last match A 173, B 173; matches on record A 77, B 238; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18GAISZO-SZO  (YES = Marine Szostak)
Model: 87%
Kalshi: 49%
Gap: +38 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.004, surface_dev_loose -0.008, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mina Hodzic vs Carolin Raschdorf -- W100 Wrexham R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216095:234481:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mina Hodzic (`KXITFWMATCH-26OCT18HODRAS-HOD`) | 0.23 / 0.93 (317) | 58.0% | 82.6% | 77.0% | 79.4% [77.1%-80.8%] | -- | -- | -- | -- | PASS | +24.6 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Carolin Raschdorf (`KXITFWMATCH-26OCT18HODRAS-RAS`) | 0.03 / 0.37 (40) | 20.0% | 17.4% | 23.0% | 20.6% [19.2%-22.9%] | -- | -- | -- | -- | PASS | -2.6 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 2700.0, B 843.0; serve-point win A 60.1%, B 47.1%; Elo A 1565.7, B 1328.0; model uncertainty 0.0185
* Form inputs: days since last match A 4, B 236; matches on record A 288, B 85; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18HODRAS-HOD  (YES = Mina Hodzic)
Model: 83%
Kalshi: 58%
Gap: +25 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eliz Maloney vs Indianna Spink -- W100 Wrexham R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216340:222421:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eliz Maloney (`KXITFWMATCH-26OCT18MALSPI-MAL`) | 0.23 / 0.65 (72) | 44.0% | 43.8% | 47.3% | 47.3% [46.8%-47.3%] | -- | -- | -- | -- | PASS | -0.2 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Indianna Spink (`KXITFWMATCH-26OCT18MALSPI-SPI`) | 0.16 / 0.58 (118) | 37.0% | 56.2% | 52.7% | 52.7% [52.7%-53.2%] | -- | -- | -- | -- | PASS | +19.2 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 886.0, B 1392.0; serve-point win A 54.0%, B 44.8%; Elo A 1376.2, B 1396.0; model uncertainty 0.0027
* Form inputs: days since last match A 194, B 119; matches on record A 211, B 45; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18MALSPI-SPI  (YES = Indianna Spink)
Model: 56%
Kalshi: 37%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Julie Myatovic vs Arina Arifullina -- W50 Cherbourg-en-Cotentin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:239160:260204:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arina Arifullina (`KXITFWMATCH-26OCT18MYAARI-ARI`) | 0.09 / 0.81 (57) | 45.0% | 60.9% | 63.2% | 66.1% [62.6%-68.6%] | -- | -- | -- | -- | PASS | +15.9 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Julie Myatovic (`KXITFWMATCH-26OCT18MYAARI-MYA`) | 0.03 / 0.94 (466) | 48.5% | 39.1% | 36.8% | 33.9% [31.4%-37.4%] | -- | -- | -- | -- | PASS | -9.4 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 350.0, B 1518.0; serve-point win A 50.3%, B 47.6%; Elo A 1189.9, B 1305.4; model uncertainty 0.0298
* Form inputs: days since last match A 187, B 97; matches on record A 65, B 118; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18MYAARI-ARI  (YES = Arina Arifullina)
Model: 61%
Kalshi: 45%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.015, surface_dev_loose +0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lois Newberry vs Dalayna Hewitt -- W100 Wrexham R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220550:259964:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dalayna Hewitt (`KXITFWMATCH-26OCT18NEWHEW-HEW`) | 0.05 / 0.93 (407) | 49.0% | 83.4% | 82.1% | 79.2% [76.6%-82.6%] | -- | -- | -- | -- | PASS | +34.4 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lois Newberry (`KXITFWMATCH-26OCT18NEWHEW-NEW`) | 0.03 / 0.91 (328) | 47.0% | 16.6% | 17.9% | 20.8% [17.4%-23.4%] | -- | -- | -- | -- | PASS | -30.4 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 666.0, B 918.0; serve-point win A 54.0%, B 38.6%; Elo A 1263.7, B 1482.7; model uncertainty 0.0303
* Form inputs: days since last match A 208, B 187; matches on record A 37, B 233; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18NEWHEW-HEW  (YES = Dalayna Hewitt)
Model: 83%
Kalshi: 49%
Gap: +34 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jana Otzipka vs Megan Mae Root -- W50 Cherbourg-en-Cotentin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260445:269759:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jana Otzipka (`KXITFWMATCH-26OCT18OTZROO-OTZ`) | 0.23 / 0.96 (22) | 59.5% | 93.2% | 78.5% | 78.2% [76.5%-79.7%] | -- | -- | -- | -- | PASS | +33.7 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Megan Mae Root (`KXITFWMATCH-26OCT18OTZROO-ROO`) | 0.03 / 0.48 (48) | 25.5% | 6.8% | 21.5% | 21.8% [20.3%-23.4%] | -- | -- | -- | -- | PASS | -18.7 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 908.0, B 70.0; serve-point win A 58.3%, B 52.8%; Elo A 1434.0, B 1213.5; model uncertainty 0.0158
* Form inputs: days since last match A 173, B 173; matches on record A 98, B 8; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18OTZROO-OTZ  (YES = Jana Otzipka)
Model: 93%
Kalshi: 60%
Gap: +34 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.016, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Christian Djonov vs Moritz Hoffmann -- M25 Sarreguemines R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206709:211645:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Christian Djonov (`KXITFMATCH-26OCT18DJOHOF-DJO`) | 0.04 / 0.96 (22) | 50.0% | 44.0% | 50.0% | 52.0% [52.0%-52.0%] | -- | -- | -- | -- | PASS | -6.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Moritz Hoffmann (`KXITFMATCH-26OCT18DJOHOF-HOF`) | 0.03 / 0.97 (313) | 50.0% | 56.0% | 50.0% | 48.0% [48.0%-48.0%] | -- | -- | -- | -- | PASS | +6.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 61.4%, B 37.4%; Elo A 1215.0, B 1200.0; model uncertainty 0.0
* Form inputs: days since last match A 817, B 698; matches on record A 2, B 10; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vincent Dullinger vs Arian Barbic -- M25 Sarreguemines R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18DULBAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arian Barbic (`KXITFMATCH-26OCT18DULBAR-BAR`) | 0.04 / 0.95 (500) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vincent Dullinger (`KXITFMATCH-26OCT18DULBAR-DUL`) | 0.03 / 0.96 (625) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matteo Waring vs Nicola Senn -- M25 Sarreguemines R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18WARSEN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicola Senn (`KXITFMATCH-26OCT18WARSEN-SEN`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matteo Waring (`KXITFMATCH-26OCT18WARSEN-WAR`) | 0.03 / 0.97 (313) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tessa Johanna Brockmann vs Mia Wainwright -- W100 Wrexham R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260598:261968:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tessa Johanna Brockmann (`KXITFWMATCH-26OCT18BROWAI-BRO`) | 0.04 / 0.94 (80) | 49.0% | 97.0% | 88.0% | 92.7% [91.7%-93.4%] | -- | -- | -- | -- | PASS | +48.0 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mia Wainwright (`KXITFWMATCH-26OCT18BROWAI-WAI`) | 0.03 / 0.97 (1046) | 50.0% | 3.0% | 12.0% | 7.3% [6.6%-8.3%] | -- | -- | -- | -- | PASS | -47.0 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3426.0, B 547.0; serve-point win A 61.0%, B 53.2%; Elo A 1727.2, B 1256.7; model uncertainty 0.0085
* Form inputs: days since last match A 4, B 299; matches on record A 169, B 18; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18BROWAI-BRO  (YES = Tessa Johanna Brockmann)
Model: 97%
Kalshi: 49%
Gap: +48 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## HAJAR CRINEBOUCH vs Diana Marcinkevica -- W50 Cherbourg-en-Cotentin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:203509:263728:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| HAJAR CRINEBOUCH (`KXITFWMATCH-26OCT18CRIMAR-CRI`) | 0.07 / 0.95 (500) | 51.0% | 27.4% | 45.2% | 26.5% [19.7%-30.5%] | -- | -- | -- | -- | PASS | -23.6 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Diana Marcinkevica (`KXITFWMATCH-26OCT18CRIMAR-MAR`) | 0.03 / 0.74 (96) | 38.5% | 72.6% | 54.8% | 73.5% [69.5%-80.3%] | -- | -- | -- | -- | PASS | +34.1 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 479.0, B 1101.0; serve-point win A 51.4%, B 44.1%; Elo A 1211.1, B 1441.4; model uncertainty 0.0545
* Form inputs: days since last match A 159, B 208; matches on record A 17, B 942; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18CRIMAR-MAR  (YES = Diana Marcinkevica)
Model: 73%
Kalshi: 38%
Gap: +34 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.026, surface_pool_high +0.018, surface_dev_loose -0.008, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anastasiia Firman vs Milena Maria Ciocan -- W50 Cherbourg-en-Cotentin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260582:270134:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Milena Maria Ciocan (`KXITFWMATCH-26OCT18FIRCIO-CIO`) | 0.04 / 0.95 (500) | 49.5% | 15.0% | 18.9% | 30.6% [27.4%-32.5%] | -- | -- | -- | -- | PASS | -34.5 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anastasiia Firman (`KXITFWMATCH-26OCT18FIRCIO-FIR`) | 0.03 / 0.84 (157) | 43.5% | 85.0% | 81.1% | 69.4% [67.5%-72.6%] | -- | -- | -- | -- | PASS | +41.5 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1700.0, B 217.0; serve-point win A 58.0%, B 49.8%; Elo A 1363.6, B 1236.2; model uncertainty 0.0253
* Form inputs: days since last match A 215, B 229; matches on record A 91, B 6; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18FIRCIO-FIR  (YES = Anastasiia Firman)
Model: 85%
Kalshi: 44%
Gap: +42 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose -0.000, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kate Gardiner vs Salma Djoubri -- W50 Cherbourg-en-Cotentin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220305:222440:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Salma Djoubri (`KXITFWMATCH-26OCT18GARDJO-DJO`) | 0.04 / 0.95 (500) | 49.5% | 90.8% | 53.7% | 74.8% [70.8%-79.6%] | -- | -- | -- | -- | PASS | +41.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kate Gardiner (`KXITFWMATCH-26OCT18GARDJO-GAR`) | 0.03 / 0.96 (625) | 49.5% | 9.2% | 46.3% | 25.2% [20.4%-29.2%] | -- | -- | -- | -- | PASS | -40.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 135.0, B 169.0; serve-point win A 49.2%, B 40.9%; Elo A 1261.3, B 1467.4; model uncertainty 0.044
* Form inputs: days since last match A 446, B 334; matches on record A 3, B 168; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18GARDJO-DJO  (YES = Salma Djoubri)
Model: 91%
Kalshi: 50%
Gap: +41 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.029, surface_pool_high +0.035, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Caroline Werner vs Amelie Brooks -- W100 Wrexham R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259608:espn:espn:4384:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amelie Brooks (`KXITFWMATCH-26OCT18WERBRO-BRO`) | 0.04 / 0.95 (500) | 49.5% | 2.9% | 48.4% | 9.1% [9.1%-9.1%] | -- | -- | -- | -- | PASS | -46.6 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Caroline Werner (`KXITFWMATCH-26OCT18WERBRO-WER`) | 0.03 / 0.95 (66) | 49.0% | 97.1% | 51.6% | 90.9% [90.9%-90.9%] | -- | -- | -- | -- | PASS | +48.1 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 164.0; serve-point win A 60.4%, B 53.9%; Elo A 1618.5, B 1211.6; model uncertainty 0.0001
* Form inputs: days since last match A 5, B 173; matches on record A 24, B 19; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18WERBRO-WER  (YES = Caroline Werner)
Model: 97%
Kalshi: 49%
Gap: +48 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Liv Zingg vs Ankita Raina -- W100 Wrexham R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18ZINRAI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ankita Raina (`KXITFWMATCH-26OCT18ZINRAI-RAI`) | 0.23 / 0.72 (90) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Liv Zingg (`KXITFWMATCH-26OCT18ZINRAI-ZIN`) | 0.09 / 0.51 (51) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
