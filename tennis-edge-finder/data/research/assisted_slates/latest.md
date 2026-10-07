# ASSISTED SLATE -- 2026-10-07T14:26Z (`SL-20261007T142640Z-80ee5bbf`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

216 open matches not seen started, 534 markets. Skipped: {"scheduled_start_over_24h_past": 17, "first_ball_already_observed": 2}. Sources: shadow board 2026-10-07T13:52:31.625652+00:00, Model 4 2026-10-07T13:53:53.376634+00:00, Gen-1 ledger 2026-10-07T13:52:27.416231+00:00, external 2026-10-07T14:16:26.037767+00:00, capture 20261007T141400Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-10-08 04:00Z**
* Recommended RUN TENNIS time: **2026-10-08 03:15Z**
* Final price/status check time: **2026-10-08 03:50Z**
* Number of matches in window: 4 (Kimmer Coppejans vs Stefanos Tsitsipas, Pavel Kotov vs Tallon Griekspoor, Camilo Ugo Carabelli vs Ilia Simakin, Bernard Tomic vs Matteo Arnaldi)

Slate built 2026-10-07T14:26Z. Refresh due by: 2026-10-08 03:15Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 28, "HIGH_REVIEW": 37, "NORMAL": 206, "REVIEW": 47, "UNPRICED": 216}; match winners: {"EXTREME": 28, "HIGH_REVIEW": 32, "NORMAL": 129, "REVIEW": 28, "UNPRICED": 215}; quote freshness at build: {"FRESH": 318}.

## Florian Broska vs Lukas Neumayer -- ATP Challenger Braga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-06T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202239:209903:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Florian Broska (`KXATPCHALLENGERMATCH-26OCT06BRONEU-BRO`) | 0.24 / 0.25 (528) | 24.5% | 25.7% | 45.0% | 36.1% [32.0%-40.0%] | -- | -- | -- | -- | SHADOW_BET | +1.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lukas Neumayer (`KXATPCHALLENGERMATCH-26OCT06BRONEU-NEU`) | 0.75 / 0.76 (10825) | 75.5% | 74.3% | 55.0% | 63.8% [60.0%-68.0%] | -- | -- | -- | -- | PASS | -1.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3459.0, B 5238.0; serve-point win A 59.9%, B 34.9%; Elo A 1485.5, B 1727.2; model uncertainty 0.0402
* Form inputs: days since last match A 15, B 15; matches on record A 218, B 402; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.009, surface_dev_loose +0.000, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE

## Tiago Cacao / Francisco Rocha vs Finn Bass / Scott Duncan -- ATP Challenger Braga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-06T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06CACROCBASDUN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Finn Bass / Scott Duncan (`KXATPCHALLENGERDOUBLES-26OCT06CACROCBASDUN-BASDUN`) | 0.57 / 0.67 (66) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tiago Cacao / Francisco Rocha (`KXATPCHALLENGERDOUBLES-26OCT06CACROCBASDUN-CACROC`) | 0.33 / 0.42 (5) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Marvin Moeller vs Tiago Torres -- ATP Challenger Braga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 16:05Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-06T16:05:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202359:208426:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marvin Moeller (`KXATPCHALLENGERMATCH-26OCT06MOETOR-MOE`) | 0.67 / 0.68 (5655) | 67.5% | 66.7% | 74.1% | 70.6% [68.2%-72.0%] | -- | -- | -- | -- | SHADOW_BET | -0.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tiago Torres (`KXATPCHALLENGERMATCH-26OCT06MOETOR-TOR`) | 0.32 / 0.33 (38246) | 32.5% | 33.3% | 25.9% | 29.4% [28.0%-31.8%] | -- | -- | -- | -- | PASS | +0.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5499.0, B 3105.0; serve-point win A 58.4%, B 44.9%; Elo A 1636.5, B 1558.8; model uncertainty 0.0187
* Form inputs: days since last match A 15, B 8; matches on record A 407, B 91; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.009, surface_dev_loose -0.009, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE

## Edas Butvilas vs Max Hans Rehberg -- ATP Challenger Villena R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 16:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-06T16:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208819:210220:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Edas Butvilas (`KXATPCHALLENGERMATCH-26OCT06BUTREH-BUT`) | 0.58 / 0.59 (50435) | 58.5% | 55.6% | 51.5% | 53.5% [52.0%-56.4%] | -- | -- | -- | -- | PASS | -2.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Max Hans Rehberg (`KXATPCHALLENGERMATCH-26OCT06BUTREH-REH`) | 0.41 / 0.42 (24335) | 41.5% | 44.4% | 48.5% | 46.5% [43.6%-48.0%] | -- | -- | -- | -- | WATCH | +2.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5096.0, B 3983.0; serve-point win A 65.3%, B 35.9%; Elo A 1670.1, B 1609.9; model uncertainty 0.0223
* Form inputs: days since last match A 8, B 29; matches on record A 267, B 254; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.010, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE

## Stefan Latinovic / Mili Poljicak vs Enrique Carrascosa Diaz / Maxi Carrascosa Diaz -- ATP Challenger Villena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 16:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-06T16:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06LATPOLCARCAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Enrique Carrascosa Diaz / Maxi Carrascosa Diaz (`KXATPCHALLENGERDOUBLES-26OCT06LATPOLCARCAR-CARCAR`) | 0.09 / 0.10 (5) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stefan Latinovic / Mili Poljicak (`KXATPCHALLENGERDOUBLES-26OCT06LATPOLCARCAR-LATPOL`) | 0.52 / 0.92 (160) | 72.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Eichenseher / Thurner vs Galea / Munoz Fuster -- M15 Pontevedra R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06EICTHUGALMUN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eichenseher / Thurner (`KXITFDOUBLES-26OCT06EICTHUGALMUN-EICTHU`) | 0.49 / 0.98 (14) | 73.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Galea / Munoz Fuster (`KXITFDOUBLES-26OCT06EICTHUGALMUN-GALMUN`) | 0.04 / 0.17 (30) | 10.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Zoe Doldan vs Maria Florencia Urrutia -- W15 Cipolletti R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220447:269847:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zoe Doldan (`KXITFWMATCH-26OCT06DOLURR-DOL`) | 0.06 / 0.07 (677) | 6.5% | 5.5% | 30.0% | 18.8% [18.8%-18.8%] | -- | -- | -- | -- | PASS | -1.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Florencia Urrutia (`KXITFWMATCH-26OCT06DOLURR-URR`) | 0.93 / 0.94 (182) | 93.5% | 94.5% | 70.0% | 81.2% [81.2%-81.2%] | -- | -- | -- | -- | PASS | +1.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 2454.0; serve-point win A 46.2%, B 41.8%; Elo A 1244.4, B 1501.0; model uncertainty 0.0001
* Form inputs: days since last match A 715, B 162; matches on record A 1, B 106; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ana Sofia Sanchez vs Milagros Cristobal -- W15 Cipolletti R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:204419:264197:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Milagros Cristobal (`KXITFWMATCH-26OCT06SANCRI-CRI`) | 0.01 / 0.02 (43792) | 1.5% | 0.7% | 14.1% | 6.0% [5.7%-6.3%] | -- | -- | -- | -- | PASS | -0.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ana Sofia Sanchez (`KXITFWMATCH-26OCT06SANCRI-SAN`) | 0.99 / -- (0) | -- | 99.3% | 85.9% | 94.0% [93.7%-94.3%] | -- | -- | -- | -- | PASS | -- | UNPRICED | FRESH | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 3191.0, B 71.0; serve-point win A 58.7%, B 59.9%; Elo A 1620.5, B 1133.4; model uncertainty 0.0031
* Form inputs: days since last match A 24, B 197; matches on record A 854, B 8; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carola Celina Sosa vs Sofia Meabe -- W15 Cipolletti R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260707:266446:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Meabe (`KXITFWMATCH-26OCT06SOSMEA-MEA`) | 0.91 / 0.93 (3) | 92.0% | 87.1% | 64.1% | 80.1% [78.5%-81.8%] | -- | -- | -- | -- | PASS | -4.9 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carola Celina Sosa (`KXITFWMATCH-26OCT06SOSMEA-SOS`) | 0.06 / 0.07 (22) | 6.5% | 12.9% | 35.9% | 19.9% [18.2%-21.4%] | -- | -- | -- | -- | PASS | +6.4 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 230.0, B 235.0; serve-point win A 48.4%, B 43.1%; Elo A 1073.9, B 1335.6; model uncertainty 0.0164
* Form inputs: days since last match A 260, B 260; matches on record A 35, B 18; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Leyla Fiorella Britez Risso vs Maria Sofia Madrid Rocca -- W15 Cipolletti R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222513:237458:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leyla Fiorella Britez Risso (`KXITFWMATCH-26OCT06BRIMAD-BRI`) | 0.92 / 0.94 (26) | 93.0% | 89.0% | 28.2% | 76.5% [76.5%-76.5%] | -- | -- | -- | -- | PASS | -4.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Maria Sofia Madrid Rocca (`KXITFWMATCH-26OCT06BRIMAD-MAD`) | 0.06 / 0.10 (18) | 8.0% | 11.0% | 71.8% | 23.5% [23.5%-23.5%] | -- | -- | -- | -- | PASS | +3.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 257.0, B 0.0; serve-point win A 57.7%, B 51.5%; Elo A 1409.9, B 1206.8; model uncertainty 0.0003
* Form inputs: days since last match A 848, B 1205; matches on record A 44, B 25; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Florencia Belen Moron vs Justina Maria Gonzalez Daniele -- W15 Cipolletti R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260357:260708:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Justina Maria Gonzalez Daniele (`KXITFWMATCH-26OCT06MORGON-GON`) | 0.95 / 0.97 (293) | 96.0% | 95.5% | 83.3% | 85.2% [84.6%-86.4%] | -- | -- | -- | -- | PASS | -0.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Florencia Belen Moron (`KXITFWMATCH-26OCT06MORGON-MOR`) | 0.03 / 0.06 (460) | 4.5% | 4.5% | 16.7% | 14.8% [13.6%-15.4%] | -- | -- | -- | -- | PASS | -0.0 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 144.0, B 2911.0; serve-point win A 45.2%, B 42.1%; Elo A 1107.5, B 1409.6; model uncertainty 0.0093
* Form inputs: days since last match A 260, B 162; matches on record A 77, B 154; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luciana Moyano vs Sofia Nahiara Nappi -- W15 Cipolletti R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06MOYNAP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luciana Moyano (`KXITFWMATCH-26OCT06MOYNAP-MOY`) | 0.94 / 0.96 (10) | 95.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sofia Nahiara Nappi (`KXITFWMATCH-26OCT06MOYNAP-NAP`) | 0.04 / 0.07 (3) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## BASEL / DELFINA VEGA GUDINO vs Luisana Mondati / Tejada -- W15 Cipolletti R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06BASDELLUITEJ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BASEL / DELFINA VEGA GUDINO (`KXITFWDOUBLES-26OCT06BASDELLUITEJ-BASDEL`) | 0.05 / 0.62 (1) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luisana Mondati / Tejada (`KXITFWDOUBLES-26OCT06BASDELLUITEJ-LUITEJ`) | 0.05 / 0.80 (1) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Daniela Duarte / Lassaga vs Victoria Gobbi Monllau / Zornada -- W15 Cipolletti R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06DANLASVICZOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniela Duarte / Lassaga (`KXITFWDOUBLES-26OCT06DANLASVICZOR-DANLAS`) | 0.06 / 0.53 (11) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Victoria Gobbi Monllau / Zornada (`KXITFWDOUBLES-26OCT06DANLASVICZOR-VICZOR`) | 0.54 / 0.67 (5) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nahiara Nappi / Rondinoni vs Cristobal / Pajello -- W15 Cipolletti R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06NAHRONCRIPAJ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cristobal / Pajello (`KXITFWDOUBLES-26OCT06NAHRONCRIPAJ-CRIPAJ`) | 0.16 / 0.89 (0) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nahiara Nappi / Rondinoni (`KXITFWDOUBLES-26OCT06NAHRONCRIPAJ-NAHRON`) | 0.05 / 0.89 (5) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sofia Sanchez / Florencia Urrutia vs Maria Maruca / Soto Neira -- W15 Cipolletti R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06SOFFLOMARSOT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Maruca / Soto Neira (`KXITFWDOUBLES-26OCT06SOFFLOMARSOT-MARSOT`) | 0.06 / 0.45 (10) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sofia Sanchez / Florencia Urrutia (`KXITFWDOUBLES-26OCT06SOFFLOMARSOT-SOFFLO`) | 0.58 / 0.90 (5) | 74.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Baier / Corvalan Mitilli vs Doldan / Celina Sosa -- W15 Cipolletti R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06BAICORDOLCEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Baier / Corvalan Mitilli (`KXITFWDOUBLES-26OCT06BAICORDOLCEL-BAICOR`) | 0.05 / 0.86 (0) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Doldan / Celina Sosa (`KXITFWDOUBLES-26OCT06BAICORDOLCEL-DOLCEL`) | 0.06 / 0.88 (3) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Bhatia / Belen Moron vs Ailin Larraya Guidi / Meabe -- W15 Cipolletti R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06BHABELAILMEA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ailin Larraya Guidi / Meabe (`KXITFWDOUBLES-26OCT06BHABELAILMEA-AILMEA`) | 0.22 / 0.91 (10) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bhatia / Belen Moron (`KXITFWDOUBLES-26OCT06BHABELAILMEA-BHABEL`) | 0.09 / 0.18 (5) | 13.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Fiorella Britez Risso / Kawano Cho vs Bulbarella / Rain -- W15 Cipolletti R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06FIOKAWBULRAI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bulbarella / Rain (`KXITFWDOUBLES-26OCT06FIOKAWBULRAI-BULRAI`) | 0.26 / 0.33 (66) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fiorella Britez Risso / Kawano Cho (`KXITFWDOUBLES-26OCT06FIOKAWBULRAI-FIOKAW`) | 0.60 / 0.71 (1) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jurado / Sofia Madrid Rocca vs Mai / Markus -- W15 Cipolletti R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06JURSOFMAIMAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jurado / Sofia Madrid Rocca (`KXITFWDOUBLES-26OCT06JURSOFMAIMAR-JURSOF`) | 0.05 / 0.90 (50) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mai / Markus (`KXITFWDOUBLES-26OCT06JURSOFMAIMAR-MAIMAR`) | 0.05 / 0.90 (51) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Trey Hilderbrand / Bogdan Pavel vs Victor Vlad Cornea / David Poljak -- ATP Challenger Villena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:50Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-07T13:50:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07HILPAVCORPOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Victor Vlad Cornea / David Poljak (`KXATPCHALLENGERDOUBLES-26OCT07HILPAVCORPOL-CORPOL`) | 0.19 / 0.23 (1) | 21.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Trey Hilderbrand / Bogdan Pavel (`KXATPCHALLENGERDOUBLES-26OCT07HILPAVCORPOL-HILPAV`) | 0.77 / 0.81 (380) | 79.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Viktoria Hruncakova vs Himeno Sakatsume -- WTA 125K Samsun R16

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-07 16:30Z
* Current expected start: 2026-10-07 14:20Z
* Source: COURT_PROGRESSION: preceding match on Center Court - Can Uner finished; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-07 14:15Z
* Recommended handicap-by time: 2026-10-07 13:35Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA125 (WTA_125) · Hard · scheduled 2026-10-07T16:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:214149:221124:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Viktoria Hruncakova (`KXWTACHALLENGERMATCH-26OCT07HRUSAK-HRU`) | 0.27 / 0.29 (7065) | 28.0% | 34.3% | 32.6% | 33.5% [32.6%-38.2%] | 29.4% | -- | 29.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.3 pp | NORMAL | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Himeno Sakatsume (`KXWTACHALLENGERMATCH-26OCT07HRUSAK-SAK`) | 0.71 / 0.73 (3198) | 72.0% | 65.7% | 67.5% | 66.5% [61.8%-67.4%] | 70.6% | -- | 70.6% | MODEL_LONE_OUTLIER | PASS | -6.3 pp | NORMAL | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3899.0, B 3693.0; serve-point win A 58.5%, B 38.4%; Elo A 1671.6, B 1759.1; model uncertainty 0.0281
* Form inputs: days since last match A 1, B 2; matches on record A 720, B 413; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight +0.009
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; STATUS_AMBIGUOUS

## Jarno Jans / Joran Vliegen vs Hynek Barton / Filip Duda -- ATP Challenger Villena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 14:50Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-07T14:50:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07JANVLIBARDUD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hynek Barton / Filip Duda (`KXATPCHALLENGERDOUBLES-26OCT07JANVLIBARDUD-BARDUD`) | 0.16 / 0.38 (5) | 27.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jarno Jans / Joran Vliegen (`KXATPCHALLENGERDOUBLES-26OCT07JANVLIBARDUD-JANVLI`) | 0.25 / 0.66 (15) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Finn Reynolds / James Watt vs Maks Kasnikowski / Francesco Maestrelli -- ATP Challenger Villena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-07T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07REYWATKASMAE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maks Kasnikowski / Francesco Maestrelli (`KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE`) | 0.11 / 0.14 (22) | 12.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Finn Reynolds / James Watt (`KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-REYWAT`) | 0.84 / 0.89 (50) | 86.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Atharva Sharma / Volodoymyr Uzhylovskyi vs Buvaysar Gadamauri / Dimitris Sakellaridis -- ATP Challenger Palermo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 15:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-07T15:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07SHAUZVGADSAK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Buvaysar Gadamauri / Dimitris Sakellaridis (`KXATPCHALLENGERDOUBLES-26OCT07SHAUZVGADSAK-GADSAK`) | 0.50 / 0.74 (1) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Atharva Sharma / Volodoymyr Uzhylovskyi (`KXATPCHALLENGERDOUBLES-26OCT07SHAUZVGADSAK-SHAUZV`) | 0.05 / 0.50 (1) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Matej Dodig / Andrej Nedic vs Younes Lalami Laaroussi / Mario Mansilla Diez -- ATP Challenger Braga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-07T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07DODNEDLALMAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matej Dodig / Andrej Nedic (`KXATPCHALLENGERDOUBLES-26OCT07DODNEDLALMAN-DODNED`) | 0.45 / 0.52 (1) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Younes Lalami Laaroussi / Mario Mansilla Diez (`KXATPCHALLENGERDOUBLES-26OCT07DODNEDLALMAN-LALMAN`) | 0.45 / 0.53 (54) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Evangelos Kypriotis vs Leyton Rivera -- M15 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208864:212595:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Evangelos Kypriotis (`KXITFMATCH-26OCT07KYPRIV-KYP`) | 0.18 / 0.19 (39) | 18.5% | 32.8% | 42.2% | 42.2% [38.6%-44.8%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +14.3 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Leyton Rivera (`KXITFMATCH-26OCT07KYPRIV-RIV`) | 0.80 / 0.81 (2) | 80.5% | 67.2% | 57.8% | 57.8% [55.2%-61.4%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.3 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 586.0, B 1995.0; serve-point win A 56.5%, B 40.0%; Elo A 1114.2, B 1169.3; model uncertainty 0.031
* Form inputs: days since last match A 142, B 128; matches on record A 16, B 86; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oriol Roca Batalla / Carlos Sanchez Jover vs Oleksandr Ovcharenko / Kai Wehnelt -- ATP Challenger Palermo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-07T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07ROCSANOVCWEH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oleksandr Ovcharenko / Kai Wehnelt (`KXATPCHALLENGERDOUBLES-26OCT07ROCSANOVCWEH-OVCWEH`) | 0.41 / 0.51 (862) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Oriol Roca Batalla / Carlos Sanchez Jover (`KXATPCHALLENGERDOUBLES-26OCT07ROCSANOVCWEH-ROCSAN`) | 0.49 / 0.63 (15) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Andrej Martin vs Alejandro Moro Canas -- ATP Challenger Palermo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 15:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-07T15:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105413:208279:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrej Martin (`KXATPCHALLENGERMATCH-26OCT07MARMOR-MAR`) | 0.01 / 0.02 (34198) | 1.5% | 28.3% | 27.7% | 33.6% [30.8%-36.9%] | 22.3% | 19.9% | 21.1% | MODEL_LONE_OUTLIER | WATCH | +26.8 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Alejandro Moro Canas (`KXATPCHALLENGERMATCH-26OCT07MARMOR-MOR`) | 0.98 / 0.99 (44803) | 98.5% | 71.7% | 72.3% | 66.4% [63.1%-69.2%] | 77.7% | 80.0% | 78.9% | MODEL_LONE_OUTLIER | PASS | -26.8 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 2470.0, B 5786.0; serve-point win A 58.5%, B 37.0%; Elo A 1591.4, B 1628.6; model uncertainty 0.0305
* Form inputs: days since last match A 9, B 23; matches on record A 1019, B 357; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT07MARMOR-MAR  (YES = Andrej Martin)
Model: 28%
Kalshi: 2%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: SUPPORTS_MODEL_DIRECTION
Data quality: A (ADEQUATE)
Reasons: EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.028, surface_pool_high +0.029, surface_dev_loose -0.009, surface_dev_tight +0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Michel Hopp vs Francesco Ferrari -- M15 Burgas R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:133224:210424:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesco Ferrari (`KXITFMATCH-26OCT07HOPFER-FER`) | 0.30 / 0.31 (6543) | 30.5% | 49.5% | 41.1% | 43.7% [42.1%-45.8%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +19.1 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Michel Hopp (`KXITFMATCH-26OCT07HOPFER-HOP`) | 0.69 / 0.70 (479) | 69.5% | 50.4% | 58.9% | 56.3% [54.2%-57.9%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -19.1 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2440.0, B 1192.0; serve-point win A 56.1%, B 44.0%; Elo A 1319.2, B 1291.6; model uncertainty 0.0185
* Form inputs: days since last match A 128, B 128; matches on record A 88, B 191; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT07HOPFER-FER  (YES = Francesco Ferrari)
Model: 50%
Kalshi: 30%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Benjamin Kittay / Takeru Yuzuki vs Anthony Genov / Mark Whitehouse -- ATP Challenger Villena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-07T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07KITYUZGENWHI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anthony Genov / Mark Whitehouse (`KXATPCHALLENGERDOUBLES-26OCT07KITYUZGENWHI-GENWHI`) | 0.40 / 0.50 (50) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Benjamin Kittay / Takeru Yuzuki (`KXATPCHALLENGERDOUBLES-26OCT07KITYUZGENWHI-KITYUZ`) | 0.50 / 0.60 (50) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Francesca Gandolfi vs Matilde Paoletti -- W35 Santa Margherita di Pula R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-07T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222396:260984:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesca Gandolfi (`KXITFWMATCH-26OCT07GANPAO-GAN`) | 0.11 / 0.12 (1) | 11.5% | 13.5% | 48.4% | 21.8% [18.8%-25.9%] | 24.0% | -- | 24.0% | MARKETS_AGREE | PASS | +2.0 pp | NORMAL | FRESH | D / POOR | EXTERNAL_OUTLIER | VERIFIED |
| Matilde Paoletti (`KXITFWMATCH-26OCT07GANPAO-PAO`) | 0.88 / 0.89 (595) | 88.5% | 86.5% | 51.6% | 78.2% [74.1%-81.2%] | 76.0% | -- | 76.0% | KALSHI_LONE_OUTLIER | PASS | -2.0 pp | NORMAL | FRESH | D / POOR | EXTERNAL_OUTLIER | VERIFIED |

* Serve evidence (points): A 1436.0, B 466.0; serve-point win A 46.0%, B 45.8%; Elo A 1370.0, B 1663.3; model uncertainty 0.0359
* Form inputs: days since last match A 87, B 184; matches on record A 41, B 103; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.015, surface_dev_loose -0.004, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kiara Nina Kucikova vs Sofia Avataneo -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:242450:266562:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Avataneo (`KXITFWMATCH-26OCT07KUCAVA-AVA`) | 0.66 / 0.71 (99) | 68.5% | 41.9% | 19.9% | 40.4% [36.8%-45.2%] | -- | -- | -- | -- | PASS | -26.6 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kiara Nina Kucikova (`KXITFWMATCH-26OCT07KUCAVA-KUC`) | 0.28 / 0.32 (1) | 30.0% | 58.1% | 80.1% | 59.6% [54.8%-63.2%] | -- | -- | -- | -- | PASS | +28.1 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 269.0, B 821.0; serve-point win A 51.0%, B 50.5%; Elo A 1212.4, B 1178.7; model uncertainty 0.0418
* Form inputs: days since last match A 177, B 163; matches on record A 8, B 143; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT07KUCAVA-KUC  (YES = Kiara Nina Kucikova)
Model: 58%
Kalshi: 30%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arjun Kadhe / Jody Maginley vs Hendrik Jebens / Michael Vrbensky -- ATP Challenger Villena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 16:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-07T16:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07KADMAGJEBVRB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hendrik Jebens / Michael Vrbensky (`KXATPCHALLENGERDOUBLES-26OCT07KADMAGJEBVRB-JEBVRB`) | 0.58 / 0.67 (57) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arjun Kadhe / Jody Maginley (`KXATPCHALLENGERDOUBLES-26OCT07KADMAGJEBVRB-KADMAG`) | 0.33 / 0.36 (13) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Tudor Batin vs Nicola Senn -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:149272:213173:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tudor Batin (`KXITFMATCH-26OCT07BATSEN-BAT`) | 0.40 / 0.43 (45) | 41.5% | 64.3% | 60.8% | 62.3% [60.8%-64.7%] | -- | -- | -- | -- | PASS | +22.8 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nicola Senn (`KXITFMATCH-26OCT07BATSEN-SEN`) | 0.56 / 0.58 (1) | 57.0% | 35.7% | 39.2% | 37.7% [35.3%-39.2%] | -- | -- | -- | -- | PASS | -21.3 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 819.0, B 491.0; serve-point win A 60.3%, B 42.5%; Elo A 1265.6, B 1173.4; model uncertainty 0.0197
* Form inputs: days since last match A 170, B 128; matches on record A 18, B 10; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT07BATSEN-BAT  (YES = Tudor Batin)
Model: 64%
Kalshi: 42%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mathys Domenc vs Petros Tsitsipas -- M15 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202065:212912:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mathys Domenc (`KXITFMATCH-26OCT07DOMTSI-DOM`) | 0.56 / 0.57 (24) | 56.5% | 55.4% | 72.4% | 56.0% [52.0%-60.4%] | 56.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.1 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Petros Tsitsipas (`KXITFMATCH-26OCT07DOMTSI-TSI`) | 0.39 / 0.43 (6) | 41.0% | 44.6% | 27.6% | 44.0% [39.6%-48.0%] | 43.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.6 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 606.0, B 2289.0; serve-point win A 63.2%, B 37.9%; Elo A 1259.3, B 1264.6; model uncertainty 0.042
* Form inputs: days since last match A 135, B 128; matches on record A 12, B 167; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jose Dominguez Alonso vs Jip Van Assendelft -- M15 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210206:213537:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jose Dominguez Alonso (`KXITFMATCH-26OCT07DOMVAN-DOM`) | 0.99 / -- (0) | -- | 32.3% | 18.9% | 33.7% [31.7%-35.7%] | 49.0% | -- | 49.0% | ALL_THREE_DISAGREE | PASS | -- | UNPRICED | FRESH | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |
| Jip Van Assendelft (`KXITFMATCH-26OCT07DOMVAN-VAN`) | -- / 0.01 (220418) | -- | 67.7% | 81.2% | 66.3% [64.3%-68.3%] | 50.9% | -- | 50.9% | MODEL_LONE_OUTLIER | PASS | -- | UNPRICED | FRESH | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 662.0, B 202.0; serve-point win A 55.1%, B 41.4%; Elo A 1135.9, B 1236.1; model uncertainty 0.0201
* Form inputs: days since last match A 149, B 429; matches on record A 15, B 10; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Adan Freire Da Silva vs Kris van Wyk -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144748:207676:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adan Freire Da Silva (`KXITFMATCH-26OCT07FREVAN-FRE`) | 0.05 / 0.06 (955) | 5.5% | 56.8% | 65.4% | 54.7% [50.0%-58.4%] | 50.0% | -- | 50.0% | KALSHI_LONE_OUTLIER | WATCH | +51.3 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Kris van Wyk (`KXITFMATCH-26OCT07FREVAN-VAN`) | 0.94 / 0.95 (4791) | 94.5% | 43.2% | 34.6% | 45.3% [41.6%-50.0%] | 50.0% | -- | 50.0% | MODEL_LONE_OUTLIER | PASS | -51.3 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 1879.0, B 2770.0; serve-point win A 57.2%, B 44.1%; Elo A 1243.4, B 1309.9; model uncertainty 0.0419
* Form inputs: days since last match A 135, B 128; matches on record A 95, B 327; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT07FREVAN-FRE  (YES = Adan Freire Da Silva)
Model: 57%
Kalshi: 6%
Gap: +51 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: SUPPORTS_MODEL_DIRECTION
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.016, surface_dev_loose +0.011, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alessandro Mondazzi vs Kaan Isik Kosaner -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07MONKOS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kaan Isik Kosaner (`KXITFMATCH-26OCT07MONKOS-KOS`) | 0.51 / 0.63 (11) | 57.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alessandro Mondazzi (`KXITFMATCH-26OCT07MONKOS-MON`) | 0.34 / 0.42 (2) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Riccardo Perin / Luca Potenza vs Jonas Forejtek / Max Wiskandt -- ATP Challenger Palermo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-07T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07PERPOTFORWIS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jonas Forejtek / Max Wiskandt (`KXATPCHALLENGERDOUBLES-26OCT07PERPOTFORWIS-FORWIS`) | 0.12 / 0.53 (54) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Riccardo Perin / Luca Potenza (`KXATPCHALLENGERDOUBLES-26OCT07PERPOTFORWIS-PERPOT`) | 0.08 / 0.53 (54) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Hugo Pierre vs Aaron Funk -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:145008:212630:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aaron Funk (`KXITFMATCH-26OCT07PIEFUN-FUN`) | 0.74 / 0.75 (3254) | 74.5% | 67.4% | 67.0% | 65.1% [61.2%-67.0%] | -- | -- | -- | -- | PASS | -7.1 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hugo Pierre (`KXITFMATCH-26OCT07PIEFUN-PIE`) | 0.24 / 0.25 (21) | 24.5% | 32.6% | 33.0% | 34.9% [33.0%-38.8%] | -- | -- | -- | -- | PASS | +8.1 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1289.0, B 1561.0; serve-point win A 57.9%, B 38.6%; Elo A 1177.2, B 1265.9; model uncertainty 0.0292
* Form inputs: days since last match A 177, B 135; matches on record A 72, B 46; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose -0.010, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Michalis Sakellaridis vs Peter Makk -- M15 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207407:207541:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Peter Makk (`KXITFMATCH-26OCT07SAKMAK-MAK`) | 0.53 / 0.95 (16) | 74.0% | 94.8% | 98.3% | 94.2% [92.3%-96.3%] | 94.4% | -- | 94.4% | MARKETS_AGREE | PASS | +20.9 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | C / LIMITED | AGREES_WITH_MODEL | AMBIGUOUS |
| Michalis Sakellaridis (`KXITFMATCH-26OCT07SAKMAK-SAK`) | 0.03 / 0.15 (16) | 9.0% | 5.1% | 1.7% | 5.8% [3.7%-7.6%] | 5.6% | -- | 5.6% | MARKETS_AGREE | PASS | -3.9 pp | NORMAL | FRESH | C / LIMITED | ALL_AGREE | AMBIGUOUS |

* Serve evidence (points): A 555.0, B 2464.0; serve-point win A 49.5%, B 38.2%; Elo A 1085.1, B 1495.3; model uncertainty 0.0199
* Form inputs: days since last match A 123, B 18; matches on record A 48, B 92; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT07SAKMAK-MAK  (YES = Peter Makk)
Model: 95%
Kalshi: 74%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_MODEL
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_CALIBRATION_OUTLIER, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.006, surface_pool_high +0.006, surface_dev_loose -0.006, surface_dev_tight +0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bercel Sandor Takacs vs Isaac Nortey -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07TAKNOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isaac Nortey (`KXITFMATCH-26OCT07TAKNOR-NOR`) | 0.85 / 0.86 (2) | 85.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bercel Sandor Takacs (`KXITFMATCH-26OCT07TAKNOR-TAK`) | 0.12 / 0.13 (168) | 12.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matylda Burylo vs Viola Turini -- W35 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222845:230876:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matylda Burylo (`KXITFWMATCH-26OCT07BURTUR-BUR`) | 0.26 / 0.27 (5634) | 26.5% | 11.5% | 22.1% | 22.5% [21.0%-24.1%] | 15.5% | -- | 15.5% | KALSHI_LONE_OUTLIER | PASS | -15.1 pp | HIGH_REVIEW | FRESH | D / POOR | AGREES_WITH_MODEL | VERIFIED |
| Viola Turini (`KXITFWMATCH-26OCT07BURTUR-TUR`) | 0.73 / 0.74 (2024) | 73.5% | 88.5% | 77.9% | 77.5% [75.9%-79.0%] | 84.5% | -- | 84.5% | KALSHI_LONE_OUTLIER | PASS | +15.1 pp | HIGH_REVIEW | FRESH | D / POOR | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 498.0, B 1075.0; serve-point win A 51.2%, B 39.7%; Elo A 1246.2, B 1456.2; model uncertainty 0.0154
* Form inputs: days since last match A 219, B 87; matches on record A 42, B 111; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT07BURTUR-TUR  (YES = Viola Turini)
Model: 89%
Kalshi: 74%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_MODEL
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.016, surface_dev_loose -0.015, surface_dev_tight +0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zuzanna Pawlikowska vs Oriana Gniewkowska -- W35 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264187:264215:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oriana Gniewkowska (`KXITFWMATCH-26OCT07PAWGNI-GNI`) | -- / 0.01 (14203) | -- | 13.1% | 25.9% | 25.5% [24.2%-27.3%] | 13.3% | -- | 13.3% | KALSHI_LONE_OUTLIER | PASS | -- | UNPRICED | FRESH | D / POOR | INSUFFICIENT_INPUTS | VERIFIED |
| Zuzanna Pawlikowska (`KXITFWMATCH-26OCT07PAWGNI-PAW`) | 0.99 / -- (0) | -- | 87.0% | 74.1% | 74.5% [72.7%-75.8%] | 86.7% | -- | 86.7% | KALSHI_LONE_OUTLIER | PASS | -- | UNPRICED | FRESH | D / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 2671.0, B 810.0; serve-point win A 53.6%, B 54.8%; Elo A 1490.0, B 1305.8; model uncertainty 0.0151
* Form inputs: days since last match A 63, B 359; matches on record A 145, B 34; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.018, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Isis Louise Van den Broek vs Kristina Novak -- W35 Lagos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216038:264227:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kristina Novak (`KXITFWMATCH-26OCT07VANNOV-NOV`) | -- / 0.01 (169982) | -- | 20.0% | 20.3% | 21.4% [18.8%-23.9%] | 23.2% | -- | 23.2% | KALSHI_LONE_OUTLIER | PASS | -- | UNPRICED | FRESH | C / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |
| Isis Louise Van den Broek (`KXITFWMATCH-26OCT07VANNOV-VAN`) | 0.99 / -- (0) | -- | 80.0% | 79.7% | 78.5% [76.1%-81.2%] | 76.8% | -- | 76.8% | KALSHI_LONE_OUTLIER | WATCH | -- | UNPRICED | FRESH | C / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 1856.0, B 994.0; serve-point win A 55.8%, B 50.5%; Elo A 1572.7, B 1354.5; model uncertainty 0.0253
* Form inputs: days since last match A 163, B 22; matches on record A 103, B 140; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chenting Zhu vs Ekaterina Tupitsyna -- W35 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264064:270065:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Tupitsyna (`KXITFWMATCH-26OCT07ZHUTUP-TUP`) | 0.89 / 0.90 (1) | 89.5% | 64.4% | 89.6% | 75.1% [62.6%-83.1%] | -- | -- | -- | -- | PASS | -25.1 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Chenting Zhu (`KXITFWMATCH-26OCT07ZHUTUP-ZHU`) | 0.07 / 0.10 (45) | 8.5% | 35.6% | 10.4% | 24.9% [16.9%-37.4%] | -- | -- | -- | -- | WATCH | +27.1 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2166.0, B 1295.0; serve-point win A 53.7%, B 43.5%; Elo A 1492.8, B 1548.5; model uncertainty 0.1026
* Form inputs: days since last match A 7, B 163; matches on record A 99, B 27; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT07ZHUTUP-ZHU  (YES = Chenting Zhu)
Model: 36%
Kalshi: 8%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.000, surface_dev_loose -0.029, surface_dev_tight +0.026
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nicolas Barrientos / Matej Vocel vs Sergio Martos Gornes / Szymon Walkow -- ATP Challenger Braga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 16:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-07T16:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07BARVOCMARWAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Barrientos / Matej Vocel (`KXATPCHALLENGERDOUBLES-26OCT07BARVOCMARWAL-BARVOC`) | 0.66 / 0.70 (50) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sergio Martos Gornes / Szymon Walkow (`KXATPCHALLENGERDOUBLES-26OCT07BARVOCMARWAL-MARWAL`) | 0.29 / 0.34 (2) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Tiago Pereira / Benjamin Winter Lopez vs Ignasi Forcano Aparicio / Rafael Izquierdo Luque -- ATP Challenger Braga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 16:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-07T16:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07PERWINFORIZQ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ignasi Forcano Aparicio / Rafael Izquierdo Luque (`KXATPCHALLENGERDOUBLES-26OCT07PERWINFORIZQ-FORIZQ`) | 0.30 / 0.35 (28) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tiago Pereira / Benjamin Winter Lopez (`KXATPCHALLENGERDOUBLES-26OCT07PERWINFORIZQ-PERWIN`) | 0.63 / 0.72 (5) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mateus Alves / Luis Britto vs Alan Magadan / Alexander Merino -- ATP Challenger Antofagasta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-07T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07ALVBRIMAGMER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mateus Alves / Luis Britto (`KXATPCHALLENGERDOUBLES-26OCT07ALVBRIMAGMER-ALVBRI`) | 0.38 / 0.53 (10) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alan Magadan / Alexander Merino (`KXATPCHALLENGERDOUBLES-26OCT07ALVBRIMAGMER-MAGMER`) | 0.45 / 0.61 (396) | 53.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Andrea Bacaloni vs Javier Munoz Fuster -- M15 Pontevedra R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211407:214499:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrea Bacaloni (`KXITFMATCH-26OCT07BACMUN-BAC`) | 0.87 / 0.88 (396) | 87.5% | 43.2% | 62.3% | 36.7% [35.7%-39.7%] | 90.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -44.3 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Javier Munoz Fuster (`KXITFMATCH-26OCT07BACMUN-MUN`) | 0.12 / 0.13 (3296) | 12.5% | 56.8% | 37.7% | 63.3% [60.3%-64.3%] | 9.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +44.3 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 787.0, B 43.0; serve-point win A 57.4%, B 41.3%; Elo A 1164.9, B 1266.4; model uncertainty 0.0199
* Form inputs: days since last match A 128, B 198; matches on record A 104, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT07BACMUN-MUN  (YES = Javier Munoz Fuster)
Model: 57%
Kalshi: 12%
Gap: +44 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eduardo Ribeiro / Marcelo Zormann vs Anders Matta / Lorenzo Joaquin Rodriguez -- ATP Challenger Antofagasta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-07T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07RIBZORMATROD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anders Matta / Lorenzo Joaquin Rodriguez (`KXATPCHALLENGERDOUBLES-26OCT07RIBZORMATROD-MATROD`) | 0.17 / 0.19 (1) | 18.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eduardo Ribeiro / Marcelo Zormann (`KXATPCHALLENGERDOUBLES-26OCT07RIBZORMATROD-RIBZOR`) | 0.75 / 0.83 (1) | 79.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Thiago Seyboth Wild vs Murkel Dellien -- ATP Challenger Antofagasta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-07T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:123961:205734:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Murkel Dellien (`KXATPCHALLENGERMATCH-26OCT07SEYDEV-DEV`) | 0.14 / 0.15 (3165) | 14.5% | 15.5% | 16.4% | 17.7% [16.7%-19.4%] | 16.4% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +1.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Thiago Seyboth Wild (`KXATPCHALLENGERMATCH-26OCT07SEYDEV-SEY`) | 0.85 / 0.86 (951) | 85.5% | 84.5% | 83.6% | 82.3% [80.6%-83.3%] | 83.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 4758.0, B 4428.0; serve-point win A 64.3%, B 43.5%; Elo A 1735.7, B 1516.2; model uncertainty 0.0136
* Form inputs: days since last match A 30, B 9; matches on record A 501, B 400; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.007, surface_dev_loose +0.007, surface_dev_tight -0.017
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Julie Myatovic vs Stephanie Judith Visscher -- W35 Villeneuve d'Ascq R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220613:260204:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julie Myatovic (`KXITFWMATCH-26OCT07MYAVIS-MYA`) | -- / 0.01 (25968) | -- | 6.3% | 6.4% | 9.4% [7.8%-10.5%] | 11.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -- | UNPRICED | FRESH | C / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |
| Stephanie Judith Visscher (`KXITFWMATCH-26OCT07MYAVIS-VIS`) | 0.99 / -- (0) | -- | 93.7% | 93.6% | 90.6% [89.5%-92.2%] | 89.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | FRESH | C / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 350.0, B 3377.0; serve-point win A 52.4%, B 35.8%; Elo A 1189.9, B 1566.0; model uncertainty 0.0134
* Form inputs: days since last match A 177, B 24; matches on record A 65, B 453; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.006, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jeevan Nedunchezhiyan / Billy Suarez vs Martin Krumich / Andrej Martin -- ATP Challenger Palermo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 17:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-07T17:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07NEDSUAKRUMAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martin Krumich / Andrej Martin (`KXATPCHALLENGERDOUBLES-26OCT07NEDSUAKRUMAR-KRUMAR`) | 0.05 / 0.75 (100) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jeevan Nedunchezhiyan / Billy Suarez (`KXATPCHALLENGERDOUBLES-26OCT07NEDSUAKRUMAR-NEDSUA`) | 0.05 / 0.75 (100) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Alfano / Sciahbasi vs Ifi / Stanke -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07ALFSCIIFISTA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alfano / Sciahbasi (`KXITFDOUBLES-26OCT07ALFSCIIFISTA-ALFSCI`) | 0.09 / 0.66 (1) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ifi / Stanke (`KXITFDOUBLES-26OCT07ALFSCIIFISTA-IFISTA`) | 0.35 / 0.37 (15) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tabacco / Tabacco vs Crivellaro / Oradini -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07TABTABCRIORA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Crivellaro / Oradini (`KXITFDOUBLES-26OCT07TABTABCRIORA-CRIORA`) | 0.04 / 0.51 (1) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tabacco / Tabacco (`KXITFDOUBLES-26OCT07TABTABCRIORA-TABTAB`) | 0.48 / 0.58 (1) | 53.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Maria Andrienko vs NICOLE ANDREA Molaro -- W35 Santa Margherita di Pula R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-07T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221515:270211:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Andrienko (`KXITFWMATCH-26OCT07ANDMOL-AND`) | 0.88 / 0.89 (1) | 88.5% | 80.3% | 59.6% | 59.6% [57.5%-61.6%] | 82.2% | -- | 82.2% | ALL_THREE_DISAGREE | PASS | -8.2 pp | NORMAL | FRESH | F / POOR | AGREES_WITH_MODEL | VERIFIED |
| NICOLE ANDREA Molaro (`KXITFWMATCH-26OCT07ANDMOL-MOL`) | 0.10 / 0.12 (2467) | 11.0% | 19.7% | 40.4% | 40.4% [38.4%-42.5%] | 17.8% | -- | 17.8% | KALSHI_LONE_OUTLIER | PASS | +8.7 pp | NORMAL | FRESH | F / POOR | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 611.0, B 106.0; serve-point win A 52.0%, B 54.3%; Elo A 1378.5, B 1312.0; model uncertainty 0.0208
* Form inputs: days since last match A 415, B 401; matches on record A 149, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.021, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Josy Daems vs Miriam Bianca Bulgaru -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214480:260539:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miriam Bianca Bulgaru (`KXITFWMATCH-26OCT07DAEBUL-BUL`) | 0.75 / 0.81 (75) | 78.0% | 57.7% | 34.4% | 41.0% [36.9%-51.6%] | 66.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -20.3 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Josy Daems (`KXITFWMATCH-26OCT07DAEBUL-DAE`) | 0.19 / 0.24 (1) | 21.5% | 42.3% | 65.5% | 59.0% [48.4%-63.1%] | 33.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +20.8 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2580.0, B 3417.0; serve-point win A 53.8%, B 44.8%; Elo A 1484.9, B 1497.5; model uncertainty 0.0733
* Form inputs: days since last match A 205, B 163; matches on record A 103, B 517; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT07DAEBUL-DAE  (YES = Josy Daems)
Model: 42%
Kalshi: 22%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.015, surface_dev_loose +0.021, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Iveta Dapkute vs Angelina Voloshchuk -- W35 Lagos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:210158:259794:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iveta Dapkute (`KXITFWMATCH-26OCT07DAPVOL-DAP`) | 0.09 / 0.11 (311) | 10.0% | 12.7% | 36.3% | 28.6% [26.9%-30.5%] | 11.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +2.7 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Angelina Voloshchuk (`KXITFWMATCH-26OCT07DAPVOL-VOL`) | 0.89 / 0.91 (2) | 90.0% | 87.3% | 63.7% | 71.4% [69.5%-73.1%] | 89.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.7 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 792.0, B 1797.0; serve-point win A 47.1%, B 44.4%; Elo A 1371.0, B 1567.9; model uncertainty 0.0181
* Form inputs: days since last match A 163, B 12; matches on record A 203, B 117; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anna Petkovic vs Marta Lombardini -- W35 Santa Margherita di Pula R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-07T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:252571:267409:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marta Lombardini (`KXITFWMATCH-26OCT07PETLOM-LOM`) | 0.80 / 0.81 (3624) | 80.5% | 60.0% | 56.9% | 56.4% [54.3%-57.5%] | 75.3% | -- | 75.3% | KALSHI_LONE_OUTLIER | PASS | -20.5 pp | HIGH_REVIEW | FRESH | C / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Anna Petkovic (`KXITFWMATCH-26OCT07PETLOM-PET`) | 0.19 / 0.20 (6113) | 19.5% | 40.0% | 43.1% | 43.6% [42.5%-45.7%] | 24.7% | -- | 24.7% | KALSHI_LONE_OUTLIER | PASS | +20.5 pp | HIGH_REVIEW | FRESH | C / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 1778.0, B 984.0; serve-point win A 50.0%, B 48.1%; Elo A 1405.7, B 1448.1; model uncertainty 0.016
* Form inputs: days since last match A 80, B 14; matches on record A 78, B 25; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT07PETLOM-PET  (YES = Anna Petkovic)
Model: 40%
Kalshi: 20%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: SUPPORTS_MODEL_DIRECTION
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.005, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Laia Petretic vs Maria Martinez Vaquero -- W35 Lagos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222346:222891:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Martinez Vaquero (`KXITFWMATCH-26OCT07PETMAR-MAR`) | 0.89 / 0.91 (184) | 90.0% | 49.9% | 31.0% | 38.9% [34.4%-45.7%] | 73.6% | -- | 73.6% | MODEL_LONE_OUTLIER | PASS | -40.1 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Laia Petretic (`KXITFWMATCH-26OCT07PETMAR-PET`) | 0.09 / 0.12 (160) | 10.5% | 50.1% | 69.0% | 61.1% [54.3%-65.6%] | 26.4% | -- | 26.4% | MODEL_LONE_OUTLIER | WATCH | +39.6 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 1964.0, B 1593.0; serve-point win A 52.0%, B 48.0%; Elo A 1455.0, B 1439.4; model uncertainty 0.0569
* Form inputs: days since last match A 163, B 17; matches on record A 203, B 112; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT07PETMAR-PET  (YES = Laia Petretic)
Model: 50%
Kalshi: 10%
Gap: +40 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: SUPPORTS_MODEL_DIRECTION
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valeria Savinykh vs Lizette Cabrera -- W35 Lagos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:202443:211878:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lizette Cabrera (`KXITFWMATCH-26OCT07SAVCAB-CAB`) | 0.48 / 0.68 (3) | 58.0% | 74.8% | 71.2% | 67.0% [63.6%-68.9%] | 66.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +16.8 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valeria Savinykh (`KXITFWMATCH-26OCT07SAVCAB-SAV`) | 0.24 / 0.38 (20) | 31.0% | 25.2% | 28.8% | 33.0% [31.1%-36.4%] | 33.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.8 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1181.0, B 3443.0; serve-point win A 52.1%, B 42.9%; Elo A 1590.4, B 1688.1; model uncertainty 0.0267
* Form inputs: days since last match A 8, B 16; matches on record A 735, B 524; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT07SAVCAB-CAB  (YES = Lizette Cabrera)
Model: 75%
Kalshi: 58%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Fabre / Maute vs Garcia Longo / Miletich -- M15 Burgas R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07FABMAUGARMIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fabre / Maute (`KXITFDOUBLES-26OCT07FABMAUGARMIL-FABMAU`) | 0.23 / 0.27 (1) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Garcia Longo / Miletich (`KXITFDOUBLES-26OCT07FABMAUGARMIL-GARMIL`) | 0.73 / 0.76 (884) | 74.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Axel Garcian vs Luc Fomba -- M15+H Rodez R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200187:209247:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luc Fomba (`KXITFMATCH-26OCT07GARFOM-FOM`) | 0.11 / 0.12 (2022) | 11.5% | 27.0% | 34.4% | 28.0% [27.2%-29.3%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +15.5 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Axel Garcian (`KXITFMATCH-26OCT07GARFOM-GAR`) | 0.88 / 0.89 (442) | 88.5% | 73.0% | 65.6% | 72.0% [70.7%-72.8%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.5 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2369.0, B 568.0; serve-point win A 62.1%, B 42.6%; Elo A 1411.7, B 1227.4; model uncertainty 0.0109
* Form inputs: days since last match A 380, B 212; matches on record A 174, B 70; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT07GARFOM-FOM  (YES = Luc Fomba)
Model: 27%
Kalshi: 12%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nannelli / Paolini vs Milushev / Naydenov -- M15 Burgas R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07NANPAOMILNAY:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Milushev / Naydenov (`KXITFDOUBLES-26OCT07NANPAOMILNAY-MILNAY`) | 0.20 / 0.27 (932) | 23.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nannelli / Paolini (`KXITFDOUBLES-26OCT07NANPAOMILNAY-NANPAO`) | 0.73 / 0.74 (38) | 73.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Alexandre Reco vs Romain Andres -- M15+H Rodez R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209258:213410:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Romain Andres (`KXITFMATCH-26OCT07RECAND-AND`) | 0.56 / 0.57 (5911) | 56.5% | 19.5% | 36.9% | 31.2% [29.4%-32.1%] | 13.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -37.0 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexandre Reco (`KXITFMATCH-26OCT07RECAND-REC`) | 0.43 / 0.44 (5223) | 43.5% | 80.5% | 63.1% | 68.8% [67.9%-70.6%] | 86.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +37.0 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1230.0, B 248.0; serve-point win A 63.5%, B 43.2%; Elo A 1319.2, B 1170.7; model uncertainty 0.0136
* Form inputs: days since last match A 9, B 128; matches on record A 118, B 5; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT07RECAND-REC  (YES = Alexandre Reco)
Model: 80%
Kalshi: 44%
Gap: +37 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maxence Rivet vs Emile Hudd -- M15+H Rodez R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209163:212134:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emile Hudd (`KXITFMATCH-26OCT07RIVHUD-HUD`) | 0.80 / 0.81 (4645) | 80.5% | 85.3% | 84.2% | 82.3% [79.8%-84.9%] | 73.6% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +4.8 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maxence Rivet (`KXITFMATCH-26OCT07RIVHUD-RIV`) | 0.19 / 0.20 (1040) | 19.5% | 14.7% | 15.8% | 17.7% [15.1%-20.2%] | 26.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.8 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1107.0, B 3414.0; serve-point win A 56.2%, B 35.6%; Elo A 1235.3, B 1485.2; model uncertainty 0.0253
* Form inputs: days since last match A 156, B 44; matches on record A 114, B 175; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ustiniya Lekomtseva vs Andrea Lola Popovic -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:261098:270222:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ustiniya Lekomtseva (`KXITFWMATCH-26OCT07LEKPOP-LEK`) | 0.42 / 0.50 (1) | 46.0% | 53.4% | 37.3% | 48.9% [46.2%-51.1%] | -- | -- | -- | -- | PASS | +7.4 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Andrea Lola Popovic (`KXITFWMATCH-26OCT07LEKPOP-POP`) | 0.48 / 0.54 (1) | 51.0% | 46.6% | 62.7% | 51.1% [48.9%-53.8%] | -- | -- | -- | -- | PASS | -4.4 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1512.0, B 406.0; serve-point win A 50.0%, B 50.6%; Elo A 1349.2, B 1333.4; model uncertainty 0.0241
* Form inputs: days since last match A 163, B 163; matches on record A 98, B 7; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Diana Martynov vs Selina Dal -- W35 Villeneuve d'Ascq R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221157:223399:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Selina Dal (`KXITFWMATCH-26OCT07MARDAL-DAL`) | 0.35 / 0.38 (55) | 36.5% | 69.9% | 84.5% | 73.1% [65.6%-79.3%] | 39.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +33.4 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Diana Martynov (`KXITFWMATCH-26OCT07MARDAL-MAR`) | 0.59 / 0.65 (37) | 62.0% | 30.1% | 15.5% | 26.9% [20.7%-34.4%] | 60.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -31.9 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1861.0, B 867.0; serve-point win A 51.0%, B 45.1%; Elo A 1465.8, B 1571.0; model uncertainty 0.0686
* Form inputs: days since last match A 31, B 163; matches on record A 329, B 186; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT07MARDAL-DAL  (YES = Selina Dal)
Model: 70%
Kalshi: 36%
Gap: +33 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.013, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofia Martianova vs Yuliya Perapekhina -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:266528:267932:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Martianova (`KXITFWMATCH-26OCT07MARPER-MAR`) | -- / 0.01 (10854) | -- | 38.5% | 38.4% | 42.6% [41.5%-42.6%] | -- | -- | -- | -- | PASS | -- | UNPRICED | FRESH | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |
| Yuliya Perapekhina (`KXITFWMATCH-26OCT07MARPER-PER`) | 0.99 / -- (0) | -- | 61.5% | 61.6% | 57.4% [57.4%-58.5%] | -- | -- | -- | -- | PASS | -- | UNPRICED | FRESH | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 1528.0, B 77.0; serve-point win A 53.1%, B 44.7%; Elo A 1262.9, B 1316.3; model uncertainty 0.0053
* Form inputs: days since last match A 163, B 506; matches on record A 53, B 10; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.011, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andrea Roots vs Iva Marinkovic -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222918:267845:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iva Marinkovic (`KXITFWMATCH-26OCT07ROOMAR-MAR`) | 0.99 / -- (0) | -- | 89.0% | 78.1% | 81.1% [80.4%-82.2%] | -- | -- | -- | -- | PASS | -- | UNPRICED | FRESH | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |
| Andrea Roots (`KXITFWMATCH-26OCT07ROOMAR-ROO`) | -- / 0.01 (41816) | -- | 11.0% | 21.9% | 18.9% [17.8%-19.6%] | -- | -- | -- | -- | PASS | -- | UNPRICED | FRESH | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 163.0, B 542.0; serve-point win A 48.8%, B 42.1%; Elo A 1063.9, B 1321.3; model uncertainty 0.0091
* Form inputs: days since last match A 366, B 163; matches on record A 54, B 17; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.007, surface_dev_loose -0.007, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Viktoria Varga vs Alesia Breaz -- W15 Székesfehérvár R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-07T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:249669:270165:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alesia Breaz (`KXITFWMATCH-26OCT07VARBRE-BRE`) | 0.97 / 0.98 (907) | 97.5% | 82.7% | 73.2% | 71.4% [70.5%-74.1%] | 86.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -14.8 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Viktoria Varga (`KXITFWMATCH-26OCT07VARBRE-VAR`) | 0.02 / 0.03 (7754) | 2.5% | 17.3% | 26.8% | 28.6% [25.9%-29.5%] | 13.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +14.8 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 139.0, B 933.0; serve-point win A 47.0%, B 46.0%; Elo A 1262.0, B 1423.6; model uncertainty 0.018
* Form inputs: days since last match A 338, B 71; matches on record A 14, B 21; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.009, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marie Vogt vs Lidia Encheva -- W50 Burgas R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223100:260565:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lidia Encheva (`KXITFWMATCH-26OCT07VOGENC-ENC`) | 0.73 / 0.75 (4098) | 74.0% | 61.1% | 41.0% | 48.4% [44.1%-54.8%] | 62.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.9 pp | REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marie Vogt (`KXITFWMATCH-26OCT07VOGENC-VOG`) | 0.25 / 0.27 (7232) | 26.0% | 38.9% | 59.0% | 51.6% [45.2%-55.9%] | 37.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +12.9 pp | REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2280.0, B 2702.0; serve-point win A 50.2%, B 47.7%; Elo A 1537.7, B 1601.8; model uncertainty 0.0534
* Form inputs: days since last match A 15, B 191; matches on record A 163, B 148; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valerio Aboian / Arklon Huertas Del Pino Cordova vs Hernan Casanova / Gonzalo Villanueva -- ATP Challenger Antofagasta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 18:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-07T18:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07ABOHUECASVIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valerio Aboian / Arklon Huertas Del Pino Cordova (`KXATPCHALLENGERDOUBLES-26OCT07ABOHUECASVIL-ABOHUE`) | 0.05 / 0.77 (1) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hernan Casanova / Gonzalo Villanueva (`KXATPCHALLENGERDOUBLES-26OCT07ABOHUECASVIL-CASVIL`) | 0.08 / 0.80 (15) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Thiago Cigarran / Santiago De la Fuente vs Boris Arias / Ignacio Carou -- ATP Challenger Antofagasta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 18:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-07T18:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07CIGDLFARICAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Boris Arias / Ignacio Carou (`KXATPCHALLENGERDOUBLES-26OCT07CIGDLFARICAR-ARICAR`) | 0.05 / 0.80 (15) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Thiago Cigarran / Santiago De la Fuente (`KXATPCHALLENGERDOUBLES-26OCT07CIGDLFARICAR-CIGDLF`) | 0.05 / 0.80 (15) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Matheus Pucinelli de Almeida vs Genaro Alberto Olivieri -- ATP Challenger Antofagasta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 18:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-07T18:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144821:207799:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Genaro Alberto Olivieri (`KXATPCHALLENGERMATCH-26OCT07PDAOLI-OLI`) | 0.30 / 0.31 (1449) | 30.5% | 34.1% | 17.4% | 22.1% [19.1%-27.2%] | 32.3% | 30.4% | 31.3% | MARKETS_AGREE | PASS | +3.6 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Matheus Pucinelli de Almeida (`KXATPCHALLENGERMATCH-26OCT07PDAOLI-PDA`) | 0.68 / 0.69 (464) | 68.5% | 65.9% | 82.6% | 77.9% [72.8%-80.9%] | 67.7% | 69.2% | 68.5% | MODEL_LONE_OUTLIER | SHADOW_BET | -2.6 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4881.0, B 4898.0; serve-point win A 57.8%, B 45.3%; Elo A 1635.3, B 1583.9; model uncertainty 0.0403
* Form inputs: days since last match A 9, B 9; matches on record A 410, B 603; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.008, surface_dev_tight -0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Buchwald / Heinrich vs Nagoudi / Piatti -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07BUCHEINAGPIA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Buchwald / Heinrich (`KXITFDOUBLES-26OCT07BUCHEINAGPIA-BUCHEI`) | 0.02 / 0.93 (9) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nagoudi / Piatti (`KXITFDOUBLES-26OCT07BUCHEINAGPIA-NAGPIA`) | 0.30 / 0.94 (41) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Collignon / Rahmani vs Lavazza / Bautista Otegui -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07COLRAHLAVBAU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Collignon / Rahmani (`KXITFDOUBLES-26OCT07COLRAHLAVBAU-COLRAH`) | 0.02 / 0.95 (50) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lavazza / Bautista Otegui (`KXITFDOUBLES-26OCT07COLRAHLAVBAU-LAVBAU`) | 0.02 / 0.95 (50) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Mansouri / Ouakaa vs Colombo / Ravasio -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07MANOUACOLRAV:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Colombo / Ravasio (`KXITFDOUBLES-26OCT07MANOUACOLRAV-COLRAV`) | 0.02 / 0.69 (1) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mansouri / Ouakaa (`KXITFDOUBLES-26OCT07MANOUACOLRAV-MANOUA`) | 0.02 / 0.85 (62) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Agra Amorim / Ivantsiv vs Liu / Moccia -- W35 Lagos QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07AGRIVALIUMOC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Agra Amorim / Ivantsiv (`KXITFWDOUBLES-26OCT07AGRIVALIUMOC-AGRIVA`) | 0.02 / 0.70 (1) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Liu / Moccia (`KXITFWDOUBLES-26OCT07AGRIVALIUMOC-LIUMOC`) | -- / 0.88 (11) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ahti / Haavisto vs Bosman / Zoldakova -- W35 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07AHTHAABOSZOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ahti / Haavisto (`KXITFWDOUBLES-26OCT07AHTHAABOSZOL-AHTHAA`) | 0.04 / 0.17 (30) | 10.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bosman / Zoldakova (`KXITFWDOUBLES-26OCT07AHTHAABOSZOL-BOSZOL`) | 0.35 / 0.87 (5) | 61.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Bennemann / Mazzola vs Antici / Giambelli -- W35 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07BENMAZANTGIA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Antici / Giambelli (`KXITFWDOUBLES-26OCT07BENMAZANTGIA-ANTGIA`) | -- / 0.74 (1) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bennemann / Mazzola (`KXITFWDOUBLES-26OCT07BENMAZANTGIA-BENMAZ`) | 0.02 / 0.90 (50) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Castro / Garakani vs Filipa Santos / Shinde -- W35 Lagos QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07CASGARFILSHI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Castro / Garakani (`KXITFWDOUBLES-26OCT07CASGARFILSHI-CASGAR`) | 0.02 / 0.16 (29) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Filipa Santos / Shinde (`KXITFWDOUBLES-26OCT07CASGARFILSHI-FILSHI`) | -- / 0.90 (50) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Kmiecik / Skliar vs Gharbi / Rebai -- W35 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07KMISKLGHAREB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gharbi / Rebai (`KXITFWDOUBLES-26OCT07KMISKLGHAREB-GHAREB`) | -- / 0.11 (1) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kmiecik / Skliar (`KXITFWDOUBLES-26OCT07KMISKLGHAREB-KMISKL`) | 0.88 / 0.91 (150) | 89.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE

## Krejcova / Paszun vs Biolay / Lim -- W35 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07KREPASBIOLIM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Biolay / Lim (`KXITFWDOUBLES-26OCT07KREPASBIOLIM-BIOLIM`) | 0.02 / 0.78 (113) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Krejcova / Paszun (`KXITFWDOUBLES-26OCT07KREPASBIOLIM-KREPAS`) | 0.01 / 0.76 (1) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Radovanovic / Senic vs Taraba Wallberg / Zeltina -- W35 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07RADSENTARZEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Radovanovic / Senic (`KXITFWDOUBLES-26OCT07RADSENTARZEL-RADSEN`) | 0.49 / 0.51 (15) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Taraba Wallberg / Zeltina (`KXITFWDOUBLES-26OCT07RADSENTARZEL-TARZEL`) | 0.45 / 0.51 (742) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Max Alcala Gurri / Nikolas Sanchez Izquierdo vs Joao Domingues / Tiago Torres -- ATP Challenger Braga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 18:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-07T18:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07ALCSAIDOMTOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Max Alcala Gurri / Nikolas Sanchez Izquierdo (`KXATPCHALLENGERDOUBLES-26OCT07ALCSAIDOMTOR-ALCSAI`) | 0.42 / 0.51 (10) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Joao Domingues / Tiago Torres (`KXATPCHALLENGERDOUBLES-26OCT07ALCSAIDOMTOR-DOMTOR`) | 0.49 / 0.57 (58) | 53.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Aleksandr Braynin vs Hugo Cardinaud -- M15+H Rodez R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202089:213220:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aleksandr Braynin (`KXITFMATCH-26OCT07BRACAR-BRA`) | 0.81 / 0.83 (10) | 82.0% | 70.4% | 73.0% | 63.8% [61.7%-67.7%] | 83.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.6 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hugo Cardinaud (`KXITFMATCH-26OCT07BRACAR-CAR`) | 0.15 / 0.22 (5) | 18.5% | 29.6% | 27.0% | 36.2% [32.3%-38.3%] | 16.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +11.1 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3451.0, B 296.0; serve-point win A 60.5%, B 43.6%; Elo A 1304.6, B 1218.6; model uncertainty 0.0297
* Form inputs: days since last match A 128, B 142; matches on record A 236, B 9; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dominguez Alvarez / Rodriguez Figueiredo vs Castelnuovo / Genier -- M15 Pontevedra R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07DOMRODCASGEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Castelnuovo / Genier (`KXITFDOUBLES-26OCT07DOMRODCASGEN-CASGEN`) | 0.02 / 0.95 (50) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dominguez Alvarez / Rodriguez Figueiredo (`KXITFDOUBLES-26OCT07DOMRODCASGEN-DOMROD`) | 0.02 / 0.95 (50) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Gonzalez-Galino / Cesar Porras vs Garcia Carbajal / Palomar -- M15 Pontevedra R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07GONCESGARPAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Garcia Carbajal / Palomar (`KXITFDOUBLES-26OCT07GONCESGARPAL-GARPAL`) | 0.54 / 0.56 (66) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gonzalez-Galino / Cesar Porras (`KXITFDOUBLES-26OCT07GONCESGARPAL-GONCES`) | 0.41 / 0.46 (1) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Lucca Cervantes Tomas / Alejandro Reyes Tirado vs Cicma / Curras Abasolo -- M15 Pontevedra R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07LUCALECICCUR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cicma / Curras Abasolo (`KXITFDOUBLES-26OCT07LUCALECICCUR-CICCUR`) | -- / 0.01 (99) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lucca Cervantes Tomas / Alejandro Reyes Tirado (`KXITFDOUBLES-26OCT07LUCALECICCUR-LUCALE`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE

## Andres Molteni / David Vega Hernandez vs Alejandro Manzanera Pertusa / Thomas Miranda -- ATP Challenger Villena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-07T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07MOLVEGMANMIR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alejandro Manzanera Pertusa / Thomas Miranda (`KXATPCHALLENGERDOUBLES-26OCT07MOLVEGMANMIR-MANMIR`) | 0.09 / 0.13 (104) | 11.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Andres Molteni / David Vega Hernandez (`KXATPCHALLENGERDOUBLES-26OCT07MOLVEGMANMIR-MOLVEG`) | 0.87 / 0.91 (2) | 89.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Julien Penzlin vs Valentin Lapalu -- M15+H Rodez R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209516:210114:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valentin Lapalu (`KXITFMATCH-26OCT07PENLAP-LAP`) | 0.32 / 0.37 (201) | 34.5% | 51.3% | 46.9% | 51.5% [50.5%-52.6%] | 34.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +16.8 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Julien Penzlin (`KXITFMATCH-26OCT07PENLAP-PEN`) | 0.52 / 0.73 (6) | 62.5% | 48.7% | 53.1% | 48.5% [47.4%-49.5%] | 65.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.8 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 494.0, B 790.0; serve-point win A 60.8%, B 39.0%; Elo A 1210.0, B 1230.0; model uncertainty 0.0103
* Form inputs: days since last match A 128, B 184; matches on record A 14, B 63; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT07PENLAP-LAP  (YES = Valentin Lapalu)
Model: 51%
Kalshi: 34%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Michele Ribecai / Gabriele Volpi vs Carlo Alberto Caniato / Francesco Forti -- ATP Challenger Palermo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-07T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07RIBVOLCANFOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlo Alberto Caniato / Francesco Forti (`KXATPCHALLENGERDOUBLES-26OCT07RIBVOLCANFOR-CANFOR`) | 0.71 / 0.80 (15) | 75.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Michele Ribecai / Gabriele Volpi (`KXATPCHALLENGERDOUBLES-26OCT07RIBVOLCANFOR-RIBVOL`) | 0.06 / 0.29 (200) | 17.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Morderger / Morderger vs Monnot / Villet -- W35 Villeneuve d'Ascq QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07MORMORMONVIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Monnot / Villet (`KXITFWDOUBLES-26OCT07MORMORMONVIL-MONVIL`) | -- / 0.90 (50) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Morderger / Morderger (`KXITFWDOUBLES-26OCT07MORMORMONVIL-MORMOR`) | 0.02 / 0.90 (50) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Boutleux / Grandvincent vs Caillat / Renard -- M15+H Rodez R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07BOUGRACAIREN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Boutleux / Grandvincent (`KXITFDOUBLES-26OCT07BOUGRACAIREN-BOUGRA`) | 0.02 / 0.95 (50) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Caillat / Renard (`KXITFDOUBLES-26OCT07BOUGRACAIREN-CAIREN`) | 0.02 / 0.95 (50) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Murkel Dellien / Franco Roncadelli vs Juan Estevez / Lucio Ratti -- ATP Challenger Antofagasta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-07T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07DEVRONESTRAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Murkel Dellien / Franco Roncadelli (`KXATPCHALLENGERDOUBLES-26OCT07DEVRONESTRAT-DEVRON`) | 0.64 / 0.69 (36) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Juan Estevez / Lucio Ratti (`KXATPCHALLENGERDOUBLES-26OCT07DEVRONESTRAT-ESTRAT`) | 0.31 / 0.36 (10) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Bruno (2002) Oliveira / Natan Rodrigues vs Joaquin Aguilar Cardozo / Alex Barrena -- ATP Challenger Antofagasta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-07T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07OLIRODAGUBAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joaquin Aguilar Cardozo / Alex Barrena (`KXATPCHALLENGERDOUBLES-26OCT07OLIRODAGUBAR-AGUBAR`) | 0.62 / 0.72 (50) | 67.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bruno (2002) Oliveira / Natan Rodrigues (`KXATPCHALLENGERDOUBLES-26OCT07OLIRODAGUBAR-OLIROD`) | 0.28 / 0.38 (52) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Bella Bergqvist Larsson vs Victoria Hu -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07BERHUX:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bella Bergqvist Larsson (`KXITFWMATCH-26OCT07BERHUX-BER`) | 0.58 / 0.61 (376) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Victoria Hu (`KXITFWMATCH-26OCT07BERHUX-HUX`) | 0.39 / 0.42 (138) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Biot / Claeys vs Pohle / Schaedel -- W15 Székesfehérvár QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07BIOCLAPOHSCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Biot / Claeys (`KXITFWDOUBLES-26OCT07BIOCLAPOHSCH-BIOCLA`) | 0.25 / 0.35 (15) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pohle / Schaedel (`KXITFWDOUBLES-26OCT07BIOCLAPOHSCH-POHSCH`) | 0.59 / 0.73 (15) | 66.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Biro / Breaz vs Chytilova / Poborilova -- W15 Székesfehérvár QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07BIRBRECHYPOB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Biro / Breaz (`KXITFWDOUBLES-26OCT07BIRBRECHYPOB-BIRBRE`) | 0.09 / 0.80 (120) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Chytilova / Poborilova (`KXITFWDOUBLES-26OCT07BIRBRECHYPOB-CHYPOB`) | -- / 0.74 (1) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Helena Buchwald vs Kaitlyn Carnicella -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259887:264014:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Helena Buchwald (`KXITFWMATCH-26OCT07BUCCAR-BUC`) | 0.42 / 0.43 (3809) | 42.5% | 56.7% | 37.4% | 53.2% [48.4%-58.5%] | 43.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +14.2 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kaitlyn Carnicella (`KXITFWMATCH-26OCT07BUCCAR-CAR`) | 0.57 / 0.58 (3990) | 57.5% | 43.3% | 62.6% | 46.8% [41.5%-51.6%] | 56.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -14.2 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 320.0, B 242.0; serve-point win A 53.5%, B 47.7%; Elo A 1362.3, B 1322.3; model uncertainty 0.0504
* Form inputs: days since last match A 436, B 436; matches on record A 101, B 16; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.021, surface_dev_loose -0.011, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniel / Nahimana vs Desai / Weckerle -- W35 Villeneuve d'Ascq QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07DANNAHDESWEC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel / Nahimana (`KXITFWDOUBLES-26OCT07DANNAHDESWEC-DANNAH`) | 0.02 / 0.90 (50) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Desai / Weckerle (`KXITFWDOUBLES-26OCT07DANNAHDESWEC-DESWEC`) | -- / 0.90 (50) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Jane Dunyon vs Martina Capurro Taborda -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211920:266672:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martina Capurro Taborda (`KXITFWMATCH-26OCT07DUNCAP-CAP`) | 0.97 / 0.98 (2290) | 97.5% | 94.0% | 93.3% | 84.5% [81.2%-87.5%] | 90.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jane Dunyon (`KXITFWMATCH-26OCT07DUNCAP-DUN`) | 0.02 / 0.03 (4478) | 2.5% | 6.0% | 6.7% | 15.5% [12.5%-18.9%] | 9.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 200.0, B 3440.0; serve-point win A 47.2%, B 41.2%; Elo A 1231.1, B 1509.9; model uncertainty 0.0317
* Form inputs: days since last match A 457, B 25; matches on record A 21, B 383; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.029, surface_pool_high +0.034, surface_dev_loose -0.003, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Fenyves / Nemcsek vs Kovacs / Teker -- W15 Székesfehérvár QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07FENNEMKOVTEK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fenyves / Nemcsek (`KXITFWDOUBLES-26OCT07FENNEMKOVTEK-FENNEM`) | 0.02 / 0.90 (50) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kovacs / Teker (`KXITFWDOUBLES-26OCT07FENNEMKOVTEK-KOVTEK`) | -- / 0.90 (50) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Georgiana Goina / Molnar vs Kalman / Mihalka -- W15 Székesfehérvár QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07GEOMOLKALMIH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Georgiana Goina / Molnar (`KXITFWDOUBLES-26OCT07GEOMOLKALMIH-GEOMOL`) | 0.15 / 0.65 (1) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kalman / Mihalka (`KXITFWDOUBLES-26OCT07GEOMOLKALMIH-KALMIH`) | 0.35 / 0.68 (10) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Valeriya Strakhova vs Maria Lourdes Carle -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211063:214604:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Lourdes Carle (`KXITFWMATCH-26OCT07STRCAR-CAR`) | 0.84 / 0.85 (4923) | 84.5% | 80.6% | 68.6% | 72.7% [70.9%-74.9%] | 83.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.9 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valeriya Strakhova (`KXITFWMATCH-26OCT07STRCAR-STR`) | 0.15 / 0.16 (1269) | 15.5% | 19.4% | 31.4% | 27.3% [25.1%-29.1%] | 17.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +3.9 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2323.0, B 4567.0; serve-point win A 46.4%, B 47.2%; Elo A 1419.4, B 1640.0; model uncertainty 0.02
* Form inputs: days since last match A 80, B 15; matches on record A 766, B 524; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.009, surface_dev_loose +0.013, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tyler Mercier vs Tristan McCormick -- M15 Quito R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07MERMCC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tristan McCormick (`KXITFMATCH-26OCT07MERMCC-MCC`) | 0.95 / 0.96 (2044) | 95.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tyler Mercier (`KXITFMATCH-26OCT07MERMCC-MER`) | 0.04 / 0.05 (723) | 4.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nicolas Esteban Rico Arias vs Ryan Fishback -- M15 Quito R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-07T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208381:212160:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ryan Fishback (`KXITFMATCH-26OCT07RICFIS-FIS`) | 0.92 / 0.94 (3033) | 93.0% | 85.2% | 86.0% | 78.8% [75.5%-82.9%] | -- | -- | -- | -- | PASS | -7.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nicolas Esteban Rico Arias (`KXITFMATCH-26OCT07RICFIS-RIC`) | 0.06 / 0.08 (4526) | 7.0% | 14.8% | 14.0% | 21.2% [17.1%-24.5%] | -- | -- | -- | -- | PASS | +7.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 684.0, B 2621.0; serve-point win A 50.4%, B 41.8%; Elo A 1077.7, B 1271.8; model uncertainty 0.037
* Form inputs: days since last match A 163, B 205; matches on record A 20, B 92; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.004, surface_dev_loose -0.016, surface_dev_tight +0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andres Urrea vs Mauricio Echazu -- M15 Quito R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-07T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105273:127443:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mauricio Echazu (`KXITFMATCH-26OCT07URRECH-ECH`) | 0.69 / 0.71 (7) | 70.0% | 80.2% | 76.9% | 77.7% [76.2%-79.4%] | 68.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +10.2 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Andres Urrea (`KXITFMATCH-26OCT07URRECH-URR`) | 0.29 / 0.31 (6) | 30.0% | 19.8% | 23.1% | 22.3% [20.6%-23.8%] | 31.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -10.2 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 417.0, B 170.0; serve-point win A 58.7%, B 34.7%; Elo A 1165.4, B 1384.1; model uncertainty 0.0161
* Form inputs: days since last match A 163, B 163; matches on record A 51, B 685; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose -0.006, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gianluca Cadenasso vs Massimo Giunta -- ATP Challenger Palermo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-07T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210668:211533:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gianluca Cadenasso (`KXATPCHALLENGERMATCH-26OCT07CADGIU-CAD`) | 0.62 / 0.64 (11480) | 63.0% | 65.2% | 63.4% | 66.3% [65.3%-68.1%] | 61.6% | 63.1% | 63.1% | MARKETS_AGREE | WATCH | +2.2 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Massimo Giunta (`KXATPCHALLENGERMATCH-26OCT07CADGIU-GIU`) | 0.36 / 0.37 (408) | 36.5% | 34.8% | 36.6% | 33.7% [31.9%-34.7%] | 38.4% | 37.5% | 37.5% | MARKETS_AGREE | PASS | -1.7 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 2844.0, B 3590.0; serve-point win A 63.5%, B 39.6%; Elo A 1634.0, B 1462.7; model uncertainty 0.0139
* Form inputs: days since last match A 9, B 9; matches on record A 170, B 181; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.009, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Joao Lucas Reis Da Silva vs Guido Ivan Justo -- ATP Challenger Antofagasta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-07T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206307:207815:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Guido Ivan Justo (`KXATPCHALLENGERMATCH-26OCT07REIJUS-JUS`) | 0.47 / 0.48 (475) | 47.5% | 55.9% | 64.6% | 62.2% [59.7%-63.2%] | 45.9% | 47.0% | 47.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +8.3 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Joao Lucas Reis Da Silva (`KXATPCHALLENGERMATCH-26OCT07REIJUS-REI`) | 0.52 / 0.53 (6947) | 52.5% | 44.1% | 35.4% | 37.8% [36.8%-40.3%] | 54.1% | 53.4% | 53.4% | MODEL_LONE_OUTLIER | PASS | -8.3 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4857.0, B 5127.0; serve-point win A 59.2%, B 39.7%; Elo A 1630.6, B 1647.0; model uncertainty 0.0174
* Form inputs: days since last match A 9, B 9; matches on record A 476, B 354; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.005, surface_dev_loose +0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Anna Burchak vs Valentina Steiner -- W35 Villeneuve d'Ascq R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260296:270253:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Burchak (`KXITFWMATCH-26OCT07BURSTE-BUR`) | 0.05 / 0.06 (129) | 5.5% | 5.7% | 13.3% | 15.7% [14.2%-17.0%] | 9.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valentina Steiner (`KXITFWMATCH-26OCT07BURSTE-STE`) | 0.92 / 0.94 (452) | 93.0% | 94.3% | 86.7% | 84.3% [83.0%-85.8%] | 90.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 191.0, B 1525.0; serve-point win A 49.9%, B 38.1%; Elo A 1222.9, B 1511.3; model uncertainty 0.0142
* Form inputs: days since last match A 352, B 13; matches on record A 3, B 78; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.013, surface_dev_loose +0.001, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuki Naito vs Alexis Nguyen -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216044:260787:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuki Naito (`KXITFWMATCH-26OCT07NAINGU-NAI`) | 0.65 / 0.66 (3092) | 65.5% | 69.0% | 68.0% | 63.6% [58.0%-68.0%] | 63.8% | -- | 63.8% | MODEL_LONE_OUTLIER | PASS | +3.5 pp | NORMAL | FRESH | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Alexis Nguyen (`KXITFWMATCH-26OCT07NAINGU-NGU`) | 0.35 / 0.36 (3165) | 35.5% | 31.0% | 32.0% | 36.4% [32.0%-42.0%] | 36.2% | -- | 36.2% | MODEL_LONE_OUTLIER | PASS | -4.5 pp | NORMAL | FRESH | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2186.0, B 1010.0; serve-point win A 55.8%, B 47.9%; Elo A 1477.3, B 1406.5; model uncertainty 0.0503
* Form inputs: days since last match A 16, B 163; matches on record A 359, B 69; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.044, surface_pool_high -0.056, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lucciana Perez Alarcon vs Mia Slama -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:252495:260693:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucciana Perez Alarcon (`KXITFWMATCH-26OCT07PERSLA-PER`) | 0.77 / 0.78 (3238) | 77.5% | 86.9% | 83.6% | 82.3% [80.8%-83.6%] | 75.3% | -- | 75.3% | ALL_THREE_DISAGREE | PASS | +9.4 pp | NORMAL | FRESH | F / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Mia Slama (`KXITFWMATCH-26OCT07PERSLA-SLA`) | 0.22 / 0.23 (957) | 22.5% | 13.1% | 16.4% | 17.7% [16.4%-19.2%] | 24.7% | -- | 24.7% | ALL_THREE_DISAGREE | PASS | -9.4 pp | NORMAL | FRESH | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1408.0, B 435.0; serve-point win A 56.4%, B 51.9%; Elo A 1638.9, B 1374.9; model uncertainty 0.0139
* Form inputs: days since last match A 44, B 422; matches on record A 97, B 34; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.014, surface_dev_loose -0.000, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kajsa Rinaldo Persson vs Ema Burgic -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:202619:211643:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ema Burgic (`KXITFWMATCH-26OCT07RINBUR-BUR`) | 0.20 / 0.21 (204) | 20.5% | 23.2% | 37.9% | 36.9% [26.5%-44.1%] | 23.2% | -- | 23.2% | KALSHI_LONE_OUTLIER | WATCH | +2.7 pp | NORMAL | FRESH | C / LIMITED | ALL_AGREE | VERIFIED |
| Kajsa Rinaldo Persson (`KXITFWMATCH-26OCT07RINBUR-RIN`) | 0.79 / 0.80 (40) | 79.5% | 76.8% | 62.1% | 63.1% [55.9%-73.5%] | 76.8% | -- | 76.8% | MODEL_LONE_OUTLIER | PASS | -2.7 pp | NORMAL | FRESH | C / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3104.0, B 1373.0; serve-point win A 56.3%, B 49.2%; Elo A 1566.2, B 1468.1; model uncertainty 0.0882
* Form inputs: days since last match A 14, B 226; matches on record A 430, B 225; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.063, surface_pool_high -0.072, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Astra Sharma vs Madison Sieg -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206292:221020:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Astra Sharma (`KXITFWMATCH-26OCT07SHASIE-SHA`) | 0.72 / 0.73 (33) | 72.5% | 66.4% | 37.6% | 48.9% [44.2%-60.5%] | 71.1% | -- | 71.1% | MODEL_LONE_OUTLIER | PASS | -6.1 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Madison Sieg (`KXITFWMATCH-26OCT07SHASIE-SIE`) | 0.27 / 0.29 (5515) | 28.0% | 33.6% | 62.4% | 51.0% [39.5%-55.8%] | 28.9% | -- | 28.9% | MODEL_LONE_OUTLIER | WATCH | +5.6 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2800.0, B 2163.0; serve-point win A 58.7%, B 44.5%; Elo A 1638.0, B 1525.1; model uncertainty 0.0812
* Form inputs: days since last match A 21, B 22; matches on record A 423, B 228; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose -0.026, surface_dev_tight +0.032
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mateo Del Pino vs Manuel Mouilleron Salvo -- M15 Quito R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-07T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210182:211389:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mateo Del Pino (`KXITFMATCH-26OCT07DELMOU-DEL`) | 0.55 / 0.57 (645) | 56.0% | 74.0% | 63.6% | 68.0% [67.0%-69.7%] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +18.0 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Manuel Mouilleron Salvo (`KXITFMATCH-26OCT07DELMOU-MOU`) | 0.43 / 0.45 (3456) | 44.0% | 26.0% | 36.4% | 32.0% [30.3%-33.0%] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -18.0 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1717.0, B 790.0; serve-point win A 56.3%, B 48.5%; Elo A 1203.2, B 1050.3; model uncertainty 0.0136
* Form inputs: days since last match A 142, B 142; matches on record A 99, B 49; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT07DELMOU-DEL  (YES = Mateo Del Pino)
Model: 74%
Kalshi: 56%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.005, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valentino Grippo vs Daniel Salazar -- M15 Quito R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-07T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202369:213201:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valentino Grippo (`KXITFMATCH-26OCT07GRISAL-GRI`) | 0.20 / 0.23 (1664) | 21.5% | 18.1% | 25.7% | 25.3% [23.2%-27.1%] | -- | -- | -- | -- | PASS | -3.4 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Daniel Salazar (`KXITFMATCH-26OCT07GRISAL-SAL`) | 0.78 / 0.80 (277) | 79.0% | 81.8% | 74.3% | 74.7% [72.9%-76.8%] | -- | -- | -- | -- | PASS | +2.9 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 759.0, B 2125.0; serve-point win A 51.6%, B 41.5%; Elo A 1076.2, B 1265.8; model uncertainty 0.0197
* Form inputs: days since last match A 149, B 128; matches on record A 15, B 85; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.013, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gray Voelzke vs Sergio Luis Hernandez Ramirez -- M15 Quito R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-07T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144848:213882:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sergio Luis Hernandez Ramirez (`KXITFMATCH-26OCT07VOEHER-HER`) | 0.76 / 0.77 (2198) | 76.5% | 72.0% | 85.2% | 65.9% [63.6%-69.5%] | 72.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gray Voelzke (`KXITFMATCH-26OCT07VOEHER-VOE`) | 0.23 / 0.24 (958) | 23.5% | 28.0% | 14.8% | 34.1% [30.5%-36.4%] | 27.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1205.0, B 354.0; serve-point win A 62.0%, B 33.4%; Elo A 1112.5, B 1186.0; model uncertainty 0.0294
* Form inputs: days since last match A 128, B 93; matches on record A 22, B 50; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.022, surface_pool_high +0.023, surface_dev_loose -0.004, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Victor Barreira Bonzom vs Yannick Baluska -- M15+H Rodez R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07BARBAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yannick Baluska (`KXITFMATCH-26OCT07BARBAL-BAL`) | 0.45 / 0.47 (1906) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Victor Barreira Bonzom (`KXITFMATCH-26OCT07BARBAL-BAR`) | 0.53 / 0.55 (1483) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ninon Carpentier vs Oceane Dodin -- W35 Villeneuve d'Ascq R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206219:270156:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ninon Carpentier (`KXITFWMATCH-26OCT07CARDOD-CAR`) | 0.02 / 0.03 (73) | 2.5% | 0.8% | 17.7% | 4.5% [3.9%-5.3%] | 5.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.7 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oceane Dodin (`KXITFWMATCH-26OCT07CARDOD-DOD`) | 0.97 / 0.98 (16080) | 97.5% | 99.2% | 82.3% | 95.5% [94.7%-96.1%] | 94.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.7 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 188.0, B 1969.0; serve-point win A 49.3%, B 32.2%; Elo A 1186.7, B 1748.1; model uncertainty 0.007
* Form inputs: days since last match A 275, B 14; matches on record A 4, B 714; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.001, surface_pool_high -0.000, surface_dev_loose -0.002, surface_dev_tight +0.002
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nick Hardt vs Felipe Meligeni Alves -- ATP Challenger Antofagasta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 22:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-07T22:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200335:200572:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nick Hardt (`KXATPCHALLENGERMATCH-26OCT07HARMEL-HAR`) | 0.32 / 0.33 (4547) | 32.5% | 48.6% | 64.7% | 57.2% [53.1%-60.2%] | -- | 33.0% | 33.0% | MODEL_LONE_OUTLIER | WATCH | +16.1 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Felipe Meligeni Alves (`KXATPCHALLENGERMATCH-26OCT07HARMEL-MEL`) | 0.68 / 0.69 (16737) | 68.5% | 51.4% | 35.3% | 42.8% [39.8%-46.9%] | -- | 67.6% | 67.6% | MODEL_LONE_OUTLIER | PASS | -17.1 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4276.0, B 3001.0; serve-point win A 59.3%, B 40.4%; Elo A 1613.5, B 1670.3; model uncertainty 0.0357
* Form inputs: days since last match A 18, B 9; matches on record A 443, B 524; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT07HARMEL-HAR  (YES = Nick Hardt)
Model: 49%
Kalshi: 32%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Felipe Jose Rivadeneira Gallegos vs Tomas Jordi Leston -- M15 Quito R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07RIVLES:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tomas Jordi Leston (`KXITFMATCH-26OCT07RIVLES-LES`) | 0.78 / 0.80 (23) | 79.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Felipe Jose Rivadeneira Gallegos (`KXITFMATCH-26OCT07RIVLES-RIV`) | 0.20 / 0.22 (38) | 21.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cadence Brace vs Chukwumelije Clarke -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223335:269864:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cadence Brace (`KXITFWMATCH-26OCT07BRACLA-BRA`) | 0.65 / 0.66 (839) | 65.5% | 87.0% | 65.1% | 75.3% [73.1%-77.0%] | 63.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +21.4 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Chukwumelije Clarke (`KXITFWMATCH-26OCT07BRACLA-CLA`) | 0.32 / 0.35 (5309) | 33.5% | 13.1% | 34.9% | 24.7% [23.1%-26.9%] | 36.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -20.4 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2165.0, B 633.0; serve-point win A 56.5%, B 51.8%; Elo A 1646.4, B 1421.4; model uncertainty 0.0191
* Form inputs: days since last match A 21, B 177; matches on record A 222, B 15; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT07BRACLA-BRA  (YES = Cadence Brace)
Model: 87%
Kalshi: 66%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.017, surface_pool_high +0.008, surface_dev_loose -0.008, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Madison Brengle vs McKenna Schaefbauer -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:201483:239103:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Madison Brengle (`KXITFWMATCH-26OCT07BRESCH-BRE`) | 0.92 / 0.93 (21) | 92.5% | 96.8% | 91.2% | 93.0% [91.4%-93.9%] | 90.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| McKenna Schaefbauer (`KXITFWMATCH-26OCT07BRESCH-SCH`) | 0.07 / 0.08 (1366) | 7.5% | 3.2% | 8.8% | 7.0% [6.1%-8.6%] | 9.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2464.0, B 204.0; serve-point win A 57.8%, B 56.0%; Elo A 1752.5, B 1303.1; model uncertainty 0.0126
* Form inputs: days since last match A 42, B 422; matches on record A 1012, B 53; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.015, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mimi Xu vs Aspen Schuman -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259685:260767:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aspen Schuman (`KXITFWMATCH-26OCT07XUXSCH-SCH`) | 0.26 / 0.28 (30) | 27.0% | 29.5% | 59.4% | 40.6% [34.5%-46.3%] | 28.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Mimi Xu (`KXITFWMATCH-26OCT07XUXSCH-XUX`) | 0.71 / 0.75 (917) | 73.0% | 70.5% | 40.6% | 59.4% [53.7%-65.5%] | 71.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1841.0, B 437.0; serve-point win A 58.1%, B 45.9%; Elo A 1592.8, B 1486.6; model uncertainty 0.0592
* Form inputs: days since last match A 247, B 331; matches on record A 98, B 46; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sahaja Yamalapalli vs Whitney Osuigwe -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215992:246481:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Whitney Osuigwe (`KXITFWMATCH-26OCT07YAMOSU-OSU`) | 0.78 / 0.79 (139) | 78.5% | 66.1% | 54.3% | 55.4% [54.8%-58.0%] | 78.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.3 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sahaja Yamalapalli (`KXITFWMATCH-26OCT07YAMOSU-YAM`) | 0.21 / 0.22 (4645) | 21.5% | 33.9% | 45.7% | 44.6% [42.0%-45.2%] | 21.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +12.3 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2258.0, B 3327.0; serve-point win A 49.1%, B 47.8%; Elo A 1570.3, B 1628.7; model uncertainty 0.0159
* Form inputs: days since last match A 15, B 24; matches on record A 233, B 400; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kate Fakih vs Allegra Korpanec Davies -- W35 Las Vegas NV R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260914:261278:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kate Fakih (`KXITFWMATCH-26OCT07FAKKOR-FAK`) | 0.74 / 0.75 (446) | 74.5% | 72.8% | 41.6% | 61.5% [58.4%-64.5%] | 73.6% | -- | 73.6% | MODEL_LONE_OUTLIER | PASS | -1.7 pp | NORMAL | FRESH | D / POOR | ALL_AGREE | VERIFIED |
| Allegra Korpanec Davies (`KXITFWMATCH-26OCT07FAKKOR-KOR`) | 0.24 / 0.25 (28) | 24.5% | 27.2% | 58.4% | 38.6% [35.5%-41.6%] | 26.4% | -- | 26.4% | MODEL_LONE_OUTLIER | PASS | +2.7 pp | NORMAL | FRESH | D / POOR | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 215.0, B 1796.0; serve-point win A 58.8%, B 45.8%; Elo A 1427.6, B 1320.3; model uncertainty 0.0309
* Form inputs: days since last match A 366, B 163; matches on record A 46, B 48; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Thea Frodin vs Yekaterina Dmitrichenko -- W35 Las Vegas NV R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216243:264140:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yekaterina Dmitrichenko (`KXITFWMATCH-26OCT07FRODMI-DMI`) | 0.40 / 0.42 (55) | 41.0% | 28.7% | 41.2% | 38.6% [36.6%-42.7%] | 40.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.3 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Thea Frodin (`KXITFWMATCH-26OCT07FRODMI-FRO`) | 0.57 / 0.60 (109) | 58.5% | 71.3% | 58.8% | 61.4% [57.3%-63.4%] | 59.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +12.8 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1232.0, B 301.0; serve-point win A 59.7%, B 44.6%; Elo A 1374.0, B 1295.6; model uncertainty 0.0304
* Form inputs: days since last match A 36, B 422; matches on record A 36, B 134; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.041, surface_pool_high +0.020, surface_dev_loose -0.001, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Emma Kamper vs Anne Christine Lutkemeyer -- W35 Las Vegas NV R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07KAMLUT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emma Kamper (`KXITFWMATCH-26OCT07KAMLUT-KAM`) | 0.52 / 0.54 (3320) | 53.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anne Christine Lutkemeyer (`KXITFWMATCH-26OCT07KAMLUT-LUT`) | 0.43 / 0.46 (46) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anastasia Kulikova vs Anastasia Abbagnato -- W35 Las Vegas NV R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214741:221031:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasia Abbagnato (`KXITFWMATCH-26OCT07KULABB-ABB`) | 0.16 / 0.17 (2) | 16.5% | 42.0% | 49.5% | 46.3% [45.3%-47.4%] | 17.8% | -- | 17.8% | MODEL_LONE_OUTLIER | WATCH | +25.5 pp | EXTREME (DATA_WARNING) | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Anastasia Kulikova (`KXITFWMATCH-26OCT07KULABB-KUL`) | 0.82 / 0.83 (50) | 82.5% | 58.0% | 50.5% | 53.7% [52.6%-54.7%] | 82.2% | -- | 82.2% | MODEL_LONE_OUTLIER | PASS | -24.5 pp | HIGH_REVIEW | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1819.0, B 1964.0; serve-point win A 58.5%, B 43.0%; Elo A 1539.8, B 1490.9; model uncertainty 0.0106
* Form inputs: days since last match A 9, B 78; matches on record A 416, B 220; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT07KULABB-ABB  (YES = Anastasia Abbagnato)
Model: 42%
Kalshi: 16%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: A (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lucas Andrade Da Silva vs Alberto Odiseo Alvarado Berrospi -- M15 Quito R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 23:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-07T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208726:212455:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alberto Odiseo Alvarado Berrospi (`KXITFMATCH-26OCT07ANDALV-ALV`) | 0.04 / 0.05 (1386) | 4.5% | 8.2% | 10.5% | 9.6% [8.0%-11.1%] | 7.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.6 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lucas Andrade Da Silva (`KXITFMATCH-26OCT07ANDALV-AND`) | 0.95 / 0.96 (3183) | 95.5% | 91.8% | 89.5% | 90.4% [88.9%-92.0%] | 92.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.6 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 803.0, B 570.0; serve-point win A 67.8%, B 43.3%; Elo A 1482.8, B 1094.1; model uncertainty 0.0155
* Form inputs: days since last match A 9, B 310; matches on record A 24, B 63; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.000, surface_dev_loose +0.008, surface_dev_tight -0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bobo / McCormick vs Bini / Fishback -- M15 Quito R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 23:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07BOBMCCBINFIS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bini / Fishback (`KXITFDOUBLES-26OCT07BOBMCCBINFIS-BINFIS`) | 0.05 / 0.79 (1) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bobo / McCormick (`KXITFDOUBLES-26OCT07BOBMCCBINFIS-BOBMCC`) | 0.05 / 0.84 (162) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hollender / Meneo vs Sebastian Dominguez Collado / Echazu -- M15 Quito R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 23:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07HOLMENSEBECH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hollender / Meneo (`KXITFDOUBLES-26OCT07HOLMENSEBECH-HOLMEN`) | 0.05 / 0.74 (96) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sebastian Dominguez Collado / Echazu (`KXITFDOUBLES-26OCT07HOLMENSEBECH-SEBECH`) | 0.05 / 0.69 (1) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Joao Victor Couto Loureiro / Franco Ribero vs Pedro Boscardin Dias / Joao Lucas Reis Da Silva -- ATP Challenger Antofagasta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-08T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07COURIBBOSREI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pedro Boscardin Dias / Joao Lucas Reis Da Silva (`KXATPCHALLENGERDOUBLES-26OCT07COURIBBOSREI-BOSREI`) | 0.54 / 0.63 (200) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Joao Victor Couto Loureiro / Franco Ribero (`KXATPCHALLENGERDOUBLES-26OCT07COURIBBOSREI-COURIB`) | 0.37 / 0.46 (50) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Emma Ottavia Ghirardato vs Francesca Pace -- W35 Las Vegas NV R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:256673:264270:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emma Ottavia Ghirardato (`KXITFWMATCH-26OCT07GHIPAC-GHI`) | 0.22 / 0.24 (114) | 23.0% | 18.3% | 25.2% | 27.3% [24.0%-31.9%] | -- | -- | -- | -- | PASS | -4.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Francesca Pace (`KXITFWMATCH-26OCT07GHIPAC-PAC`) | 0.75 / 0.78 (6347) | 76.5% | 81.7% | 74.8% | 72.7% [68.2%-76.0%] | -- | -- | -- | -- | PASS | +5.2 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 465.0, B 2585.0; serve-point win A 54.5%, B 38.6%; Elo A 1274.5, B 1437.3; model uncertainty 0.0394
* Form inputs: days since last match A 345, B 85; matches on record A 36, B 129; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.034, surface_pool_high +0.045, surface_dev_loose +0.001, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Natalie Kha vs Diletta Cherubini -- W35 Las Vegas NV R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-08T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07KHACHE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diletta Cherubini (`KXITFWMATCH-26OCT07KHACHE-CHE`) | 0.73 / 0.75 (28) | 74.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Natalie Kha (`KXITFWMATCH-26OCT07KHACHE-KHA`) | 0.25 / 0.29 (75) | 27.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Francesca Mattioli vs Duru Soke -- W35 Las Vegas NV R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:224488:260150:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesca Mattioli (`KXITFWMATCH-26OCT07MATSOK-MAT`) | 0.26 / 0.28 (84) | 27.0% | 53.0% | 43.6% | 59.0% [56.4%-62.1%] | -- | -- | -- | -- | PASS | +26.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Duru Soke (`KXITFWMATCH-26OCT07MATSOK-SOK`) | 0.72 / 0.73 (214) | 72.5% | 46.9% | 56.4% | 41.0% [37.9%-43.6%] | -- | -- | -- | -- | PASS | -25.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 492.0, B 316.0; serve-point win A 52.0%, B 48.6%; Elo A 1476.0, B 1387.9; model uncertainty 0.0284
* Form inputs: days since last match A 429, B 289; matches on record A 28, B 71; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT07MATSOK-MAT  (YES = Francesca Mattioli)
Model: 53%
Kalshi: 27%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mell Elizabeth Reasco Gonzalez vs Maria Sholokhova -- W35 Las Vegas NV R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221242:233718:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mell Elizabeth Reasco Gonzalez (`KXITFWMATCH-26OCT07REASHO-REA`) | 0.29 / 0.31 (3) | 30.0% | 32.5% | 6.2% | 24.7% [13.3%-52.1%] | -- | -- | -- | -- | PASS | +2.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Sholokhova (`KXITFWMATCH-26OCT07REASHO-SHO`) | 0.69 / 0.70 (1681) | 69.5% | 67.5% | 93.8% | 75.3% [47.9%-86.7%] | -- | -- | -- | -- | PASS | -2.0 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2361.0, B 1181.0; serve-point win A 49.9%, B 46.7%; Elo A 1519.0, B 1517.5; model uncertainty 0.1943
* Form inputs: days since last match A 163, B 436; matches on record A 178, B 85; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.017, surface_pool_high -0.013, surface_dev_loose -0.029, surface_dev_tight +0.031
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bajraliu / Rus vs Dunyon / Pate -- W50 Lexington SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 00:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-08T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07BAJRUSDUNPAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bajraliu / Rus (`KXITFWDOUBLES-26OCT07BAJRUSDUNPAT-BAJRUS`) | 0.05 / 0.90 (50) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dunyon / Pate (`KXITFWDOUBLES-26OCT07BAJRUSDUNPAT-DUNPAT`) | 0.05 / 0.90 (50) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Hewitt / Strakhova vs Buchwald / Carnicella -- W50 Lexington SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 00:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-08T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07HEWSTRBUCCAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Buchwald / Carnicella (`KXITFWDOUBLES-26OCT07HEWSTRBUCCAR-BUCCAR`) | 0.05 / 0.73 (1) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hewitt / Strakhova (`KXITFWDOUBLES-26OCT07HEWSTRBUCCAR-HEWSTR`) | 0.35 / 0.90 (50) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Inoue / Naito vs Burgic / Maria Ilie -- W50 Lexington SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 00:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-08T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07INONAIBURMAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Burgic / Maria Ilie (`KXITFWDOUBLES-26OCT07INONAIBURMAR-BURMAR`) | 0.14 / 0.73 (2) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Inoue / Naito (`KXITFWDOUBLES-26OCT07INONAIBURMAR-INONAI`) | 0.05 / 0.84 (53) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Rapolu / Sieg vs Bergqvist Larsson / Stojanova -- W50 Lexington SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 00:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-08T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07RAPSIEBERSTO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bergqvist Larsson / Stojanova (`KXITFWDOUBLES-26OCT07RAPSIEBERSTO-BERSTO`) | 0.06 / 0.73 (1) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rapolu / Sieg (`KXITFWDOUBLES-26OCT07RAPSIEBERSTO-RAPSIE`) | 0.05 / 0.89 (5) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Del Pino / Mouilleron Salvo vs Andres Macias Elizalde / Jose Rivadeneira Gallegos -- M15 Quito R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-08T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07DELMOUANDJOS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andres Macias Elizalde / Jose Rivadeneira Gallegos (`KXITFDOUBLES-26OCT07DELMOUANDJOS-ANDJOS`) | 0.05 / 0.95 (124) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Del Pino / Mouilleron Salvo (`KXITFDOUBLES-26OCT07DELMOUANDJOS-DELMOU`) | 0.05 / 0.95 (124) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Bernales / Fakih vs Chang / Shymanovich -- W35 Las Vegas NV R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-08T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07BERFAKCHASHY:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bernales / Fakih (`KXITFWDOUBLES-26OCT07BERFAKCHASHY-BERFAK`) | 0.05 / 0.90 (50) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Chang / Shymanovich (`KXITFWDOUBLES-26OCT07BERFAKCHASHY-CHASHY`) | 0.05 / 0.90 (50) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Fairclough / Christine Lutkemeyer vs Alicea / Snells -- W35 Las Vegas NV R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-08T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07FAICHRALISNE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alicea / Snells (`KXITFWDOUBLES-26OCT07FAICHRALISNE-ALISNE`) | 0.05 / 0.76 (1) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fairclough / Christine Lutkemeyer (`KXITFWDOUBLES-26OCT07FAICHRALISNE-FAICHR`) | 0.05 / 0.80 (125) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Janae Preston vs Ana Grubor -- W35 Las Vegas NV R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:258191:270320:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ana Grubor (`KXITFWMATCH-26OCT07PREGRU-GRU`) | 0.06 / 0.07 (12) | 6.5% | 23.1% | 39.9% | 35.8% [34.3%-38.4%] | -- | -- | -- | -- | WATCH | +16.6 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Janae Preston (`KXITFWMATCH-26OCT07PREGRU-PRE`) | 0.92 / 0.94 (104) | 93.0% | 77.0% | 60.1% | 64.2% [61.6%-65.7%] | -- | -- | -- | -- | PASS | -16.1 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 739.0, B 1727.0; serve-point win A 52.4%, B 53.1%; Elo A 1423.8, B 1314.9; model uncertainty 0.0201
* Form inputs: days since last match A 43, B 67; matches on record A 14, B 193; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT07PREGRU-GRU  (YES = Ana Grubor)
Model: 23%
Kalshi: 6%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.020, surface_dev_loose -0.020, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Katrina Scott vs Lexington Reed -- W35 Las Vegas NV R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221512:239186:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lexington Reed (`KXITFWMATCH-26OCT07SCOREE-REE`) | 0.26 / 0.28 (29) | 27.0% | 10.0% | 23.2% | 20.1% [17.5%-22.8%] | -- | -- | -- | -- | PASS | -17.0 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Katrina Scott (`KXITFWMATCH-26OCT07SCOREE-SCO`) | 0.70 / 0.74 (17) | 72.0% | 90.0% | 76.8% | 79.9% [77.2%-82.5%] | -- | -- | -- | -- | PASS | +18.0 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2201.0, B 144.0; serve-point win A 60.1%, B 49.6%; Elo A 1616.3, B 1375.5; model uncertainty 0.0263
* Form inputs: days since last match A 24, B 310; matches on record A 250, B 98; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT07SCOREE-SCO  (YES = Katrina Scott)
Model: 90%
Kalshi: 72%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.022, surface_pool_high -0.027, surface_dev_loose +0.003, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Battistone / Hu vs Abbagnato / Gomez Pezuela Cano -- W35 Las Vegas NV R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-08T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07BATHUXABBGOM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Abbagnato / Gomez Pezuela Cano (`KXITFWDOUBLES-26OCT07BATHUXABBGOM-ABBGOM`) | 0.05 / 0.90 (50) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Battistone / Hu (`KXITFWDOUBLES-26OCT07BATHUXABBGOM-BATHUX`) | 0.05 / 0.90 (50) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Cheong / Kha vs Rencheli / Sholokhova -- W35 Las Vegas NV R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-08T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07CHEKHARENSHO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cheong / Kha (`KXITFWDOUBLES-26OCT07CHEKHARENSHO-CHEKHA`) | 0.05 / 0.90 (50) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rencheli / Sholokhova (`KXITFWDOUBLES-26OCT07CHEKHARENSHO-RENSHO`) | 0.05 / 0.90 (50) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Justine Hejtmanek / Rodriguez vs Chan / Ottavia Ghirardato -- W35 Las Vegas NV R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-08T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07JUSRODCHAOTT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chan / Ottavia Ghirardato (`KXITFWDOUBLES-26OCT07JUSRODCHAOTT-CHAOTT`) | 0.05 / 0.90 (50) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Justine Hejtmanek / Rodriguez (`KXITFWDOUBLES-26OCT07JUSRODCHAOTT-JUSROD`) | 0.05 / 0.72 (89) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Maklakova / Mamedova vs Falkner / Soke -- W35 Las Vegas NV R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-08T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07MAKMAMFALSOK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Falkner / Soke (`KXITFWDOUBLES-26OCT07MAKMAMFALSOK-FALSOK`) | 0.05 / 0.79 (1) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maklakova / Mamedova (`KXITFWDOUBLES-26OCT07MAKMAMFALSOK-MAKMAM`) | 0.05 / 0.63 (67) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kimmer Coppejans vs Stefanos Tsitsipas -- ATP Shanghai R128

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-07 07:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-08 04:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-07 14:15Z
* Recommended handicap-by time: 2026-10-08 03:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · Hard · scheduled 2026-10-07T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:106293:126774:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kimmer Coppejans (`KXATPMATCH-26OCT07COPTSI-COP`) | 0.10 / 0.11 (15810) | 10.5% | 22.1% | 33.3% | 28.4% [24.2%-30.6%] | -- | -- | -- | -- | WATCH | +11.6 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Stefanos Tsitsipas (`KXATPMATCH-26OCT07COPTSI-TSI`) | 0.89 / 0.91 (34363) | 90.0% | 77.9% | 66.7% | 71.6% [69.4%-75.8%] | -- | -- | -- | -- | PASS | -12.1 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5117.0, B 5347.0; serve-point win A 59.1%, B 34.9%; Elo A 1638.2, B 1928.8; model uncertainty 0.0317
* Form inputs: days since last match A 1, B 5; matches on record A 892, B 803; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.017, surface_dev_loose +0.004, surface_dev_tight -0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT07COPTSI-TSI20` Will Stefanos Tsitsipas win the Kimmer Coppejans vs Stefanos Tsitsipas match by a set score of 2-0?: 0.69/0.71 mid 70.0%, model 48.4% (projection_v2.0 (prediction ledger)) -- gap -21.6 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT07COPTSI-20` Over 19.5 games: 0.52/0.53 mid 52.5%, model 71.9% (projection_v2.0 (prediction ledger)) -- gap +19.4 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT07COPTSI-TSI3` Will Stefanos Tsitsipas win at least 2.5 more games than Kimmer Coppejans?: 0.82/0.85 mid 83.5%, model 65.5% (projection_v2.0 (prediction ledger)) -- gap -18.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT07COPTSI-25` Over 24.5 games: 0.26/0.28 mid 27.0%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap +17.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT07COPTSI-TSI6` Will Stefanos Tsitsipas win at least 5.5 more games than Kimmer Coppejans?: 0.41/0.42 mid 41.5%, model 25.7% (projection_v2.0 (prediction ledger)) -- gap -15.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT07COPTSI-2-COP` Will Kimmer Coppejans win set 2 in the Kimmer Coppejans vs Stefanos Tsitsipas match: 0.15/0.16 mid 15.5%, model 30.4% (projection_v2.0 (prediction ledger)) -- gap +14.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT07COPTSI-1-COP` Will Kimmer Coppejans win set 1 in the Kimmer Coppejans vs Stefanos Tsitsipas match: 0.16/0.17 mid 16.5%, model 30.4% (projection_v2.0 (prediction ledger)) -- gap +13.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT07COPTSI-2-TSI` Will Stefanos Tsitsipas win set 2 in the Kimmer Coppejans vs Stefanos Tsitsipas match: 0.82/0.85 mid 83.5%, model 69.6% (projection_v2.0 (prediction ledger)) -- gap -13.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT07COPTSI-1-TSI` Will Stefanos Tsitsipas win set 1 in the Kimmer Coppejans vs Stefanos Tsitsipas match: 0.82/0.84 mid 83.0%, model 69.6% (projection_v2.0 (prediction ledger)) -- gap -13.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT07COPTSI-15` Over 14.5 games: 0.79/0.95 mid 87.0%, model 99.2% (projection_v2.0 (prediction ledger)) -- gap +12.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT07COPTSI-TSI21` Will Stefanos Tsitsipas win the Kimmer Coppejans vs Stefanos Tsitsipas match by a set score of 2-1?: 0.17/0.20 mid 18.5%, model 29.4% (projection_v2.0 (prediction ledger)) -- gap +10.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT07COPTSI-COP21` Will Kimmer Coppejans win the Kimmer Coppejans vs Stefanos Tsitsipas match by a set score of 2-1?: 0.04/0.06 mid 5.0%, model 12.9% (projection_v2.0 (prediction ledger)) -- gap +7.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT07COPTSI-COP20` Will Kimmer Coppejans win the Kimmer Coppejans vs Stefanos Tsitsipas match by a set score of 2-0?: 0.03/0.06 mid 4.5%, model 9.2% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Pavel Kotov vs Tallon Griekspoor -- ATP Shanghai R128

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-07 07:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-08 04:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-07 14:15Z
* Recommended handicap-by time: 2026-10-08 03:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · Hard · scheduled 2026-10-07T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:134868:200303:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tallon Griekspoor (`KXATPMATCH-26OCT07KOTGRI-GRI`) | 0.66 / 0.67 (2774) | 66.5% | 63.2% | 54.7% | 58.0% [56.1%-63.5%] | -- | -- | -- | -- | PASS | -3.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pavel Kotov (`KXATPMATCH-26OCT07KOTGRI-KOT`) | 0.33 / 0.35 (39019) | 34.0% | 36.8% | 45.3% | 42.0% [36.5%-43.9%] | -- | -- | -- | -- | WATCH | +2.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4116.0, B 4725.0; serve-point win A 67.3%, B 29.9%; Elo A 1738.3, B 1868.3; model uncertainty 0.0372
* Form inputs: days since last match A 1, B 6; matches on record A 534, B 685; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.018, surface_pool_high +0.014, surface_dev_loose +0.000, surface_dev_tight -0.010
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT07KOTGRI-GRI7` Will Tallon Griekspoor win at least 6.5 more games than Pavel Kotov?: 0.02/0.29 mid 15.5%, model 3.1% (projection_v2.0 (prediction ledger)) -- gap -12.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT07KOTGRI-23` Over 22.5 games: 0.54/0.55 mid 54.5%, model 66.5% (projection_v2.0 (prediction ledger)) -- gap +12.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT07KOTGRI-28` Over 27.5 games: 0.29/0.36 mid 32.5%, model 44.3% (projection_v2.0 (prediction ledger)) -- gap +11.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT07KOTGRI-GRI4` Will Tallon Griekspoor win at least 3.5 more games than Pavel Kotov?: 0.40/0.41 mid 40.5%, model 30.4% (projection_v2.0 (prediction ledger)) -- gap -10.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT07KOTGRI-GRI20` Will Tallon Griekspoor win the Pavel Kotov vs Tallon Griekspoor match by a set score of 2-0?: 0.41/0.43 mid 42.0%, model 34.7% (projection_v2.0 (prediction ledger)) -- gap -7.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT07KOTGRI-18` Over 17.5 games: 0.87/0.94 mid 90.5%, model 96.9% (projection_v2.0 (prediction ledger)) -- gap +6.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT07KOTGRI-GRI21` Will Tallon Griekspoor win the Pavel Kotov vs Tallon Griekspoor match by a set score of 2-1?: 0.22/0.26 mid 24.0%, model 28.5% (projection_v2.0 (prediction ledger)) -- gap +4.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT07KOTGRI-KOT21` Will Pavel Kotov win the Pavel Kotov vs Tallon Griekspoor match by a set score of 2-1?: 0.14/0.17 mid 15.5%, model 19.9% (projection_v2.0 (prediction ledger)) -- gap +4.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT07KOTGRI-1-GRI` Will Tallon Griekspoor win set 1 in the Pavel Kotov vs Tallon Griekspoor match: 0.62/0.64 mid 63.0%, model 58.9% (projection_v2.0 (prediction ledger)) -- gap -4.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT07KOTGRI-1-KOT` Will Pavel Kotov win set 1 in the Pavel Kotov vs Tallon Griekspoor match: 0.35/0.39 mid 37.0%, model 41.1% (projection_v2.0 (prediction ledger)) -- gap +4.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT07KOTGRI-2-GRI` Will Tallon Griekspoor win set 2 in the Pavel Kotov vs Tallon Griekspoor match: 0.61/0.65 mid 63.0%, model 58.9% (projection_v2.0 (prediction ledger)) -- gap -4.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT07KOTGRI-2-KOT` Will Pavel Kotov win set 2 in the Pavel Kotov vs Tallon Griekspoor match: 0.35/0.39 mid 37.0%, model 41.1% (projection_v2.0 (prediction ledger)) -- gap +4.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT07KOTGRI-KOT2` Will Pavel Kotov win at least 1.5 more games than Tallon Griekspoor?: 0.26/0.30 mid 28.0%, model 28.8% (projection_v2.0 (prediction ledger)) -- gap +0.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT07KOTGRI-KOT20` Will Pavel Kotov win the Pavel Kotov vs Tallon Griekspoor match by a set score of 2-0?: 0.15/0.19 mid 17.0%, model 16.9% (projection_v2.0 (prediction ledger)) -- gap -0.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Camilo Ugo Carabelli vs Ilia Simakin -- ATP Shanghai R128

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-07 07:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-08 04:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-07 14:15Z
* Recommended handicap-by time: 2026-10-08 03:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · Hard · scheduled 2026-10-07T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200116:209899:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ilia Simakin (`KXATPMATCH-26OCT07UGOSIM-SIM`) | 0.67 / 0.68 (41304) | 67.5% | 72.1% | 87.3% | 83.0% [73.5%-86.5%] | -- | -- | -- | -- | SHADOW_BET | +4.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Camilo Ugo Carabelli (`KXATPMATCH-26OCT07UGOSIM-UGO`) | 0.32 / 0.33 (486) | 32.5% | 27.9% | 12.7% | 17.0% [13.5%-26.5%] | -- | -- | -- | -- | PASS | -4.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5218.0, B 5039.0; serve-point win A 60.9%, B 34.4%; Elo A 1643.9, B 1738.7; model uncertainty 0.065
* Form inputs: days since last match A 9, B 1; matches on record A 650, B 285; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.027, surface_pool_high -0.021, surface_dev_loose -0.029, surface_dev_tight +0.036
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT07UGOSIM-23` Over 22.5 games: 0.45/0.48 mid 46.5%, model 55.6% (projection_v2.0 (prediction ledger)) -- gap +9.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT07UGOSIM-28` Over 27.5 games: 0.24/0.30 mid 27.0%, model 36.1% (projection_v2.0 (prediction ledger)) -- gap +9.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT07UGOSIM-18` Over 17.5 games: 0.82/0.85 mid 83.5%, model 90.7% (projection_v2.0 (prediction ledger)) -- gap +7.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT07UGOSIM-SIM21` Will Ilia Simakin win the Camilo Ugo Carabelli vs Ilia Simakin match by a set score of 2-1?: 0.21/0.25 mid 23.0%, model 29.6% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT07UGOSIM-UGO2` Will Camilo Ugo Carabelli win at least 1.5 more games than Ilia Simakin?: 0.26/0.28 mid 27.0%, model 21.9% (projection_v2.0 (prediction ledger)) -- gap -5.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT07UGOSIM-UGO20` Will Camilo Ugo Carabelli win the Camilo Ugo Carabelli vs Ilia Simakin match by a set score of 2-0?: 0.15/0.19 mid 17.0%, model 12.1% (projection_v2.0 (prediction ledger)) -- gap -4.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT07UGOSIM-SIM7` Will Ilia Simakin win at least 6.5 more games than Camilo Ugo Carabelli?: 0.13/0.17 mid 15.0%, model 10.3% (projection_v2.0 (prediction ledger)) -- gap -4.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT07UGOSIM-SIM20` Will Ilia Simakin win the Camilo Ugo Carabelli vs Ilia Simakin match by a set score of 2-0?: 0.43/0.46 mid 44.5%, model 42.5% (projection_v2.0 (prediction ledger)) -- gap -2.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT07UGOSIM-1-SIM` Will Ilia Simakin win set 1 in the Camilo Ugo Carabelli vs Ilia Simakin match: 0.62/0.65 mid 63.5%, model 65.2% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT07UGOSIM-1-UGO` Will Camilo Ugo Carabelli win set 1 in the Camilo Ugo Carabelli vs Ilia Simakin match: 0.35/0.38 mid 36.5%, model 34.8% (projection_v2.0 (prediction ledger)) -- gap -1.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT07UGOSIM-2-SIM` Will Ilia Simakin win set 2 in the Camilo Ugo Carabelli vs Ilia Simakin match: 0.62/0.65 mid 63.5%, model 65.2% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT07UGOSIM-2-UGO` Will Camilo Ugo Carabelli win set 2 in the Camilo Ugo Carabelli vs Ilia Simakin match: 0.35/0.38 mid 36.5%, model 34.8% (projection_v2.0 (prediction ledger)) -- gap -1.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT07UGOSIM-UGO21` Will Camilo Ugo Carabelli win the Camilo Ugo Carabelli vs Ilia Simakin match by a set score of 2-1?: 0.13/0.16 mid 14.5%, model 15.8% (projection_v2.0 (prediction ledger)) -- gap +1.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT07UGOSIM-SIM4` Will Ilia Simakin win at least 3.5 more games than Camilo Ugo Carabelli?: 0.46/0.47 mid 46.5%, model 46.7% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Elise Mertens / Diana Shnaider vs Ellen Perez / Demi Schuurs -- WTA Beijing QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-08 08:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-08 05:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-07 14:15Z
* Recommended handicap-by time: 2026-10-08 04:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-08T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT08MERSHNPERSCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elise Mertens / Diana Shnaider (`KXWTADOUBLES-26OCT08MERSHNPERSCH-MERSHN`) | 0.62 / 0.67 (353) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ellen Perez / Demi Schuurs (`KXWTADOUBLES-26OCT08MERSHNPERSCH-PERSCH`) | 0.33 / 0.36 (190) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Haruna Arakawa vs Tori Russell -- W35 Wagga Wagga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214505:270302:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Haruna Arakawa (`KXITFWMATCH-26OCT07ARARUS-ARA`) | 0.50 / 0.64 (3366) | 57.0% | 89.2% | 85.5% | 83.6% [81.9%-85.5%] | -- | -- | -- | -- | PASS | +32.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tori Russell (`KXITFWMATCH-26OCT07ARARUS-RUS`) | 0.36 / 0.40 (42) | 38.0% | 10.8% | 14.5% | 16.4% [14.5%-18.1%] | -- | -- | -- | -- | PASS | -27.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2195.0, B 327.0; serve-point win A 56.9%, B 52.4%; Elo A 1502.0, B 1226.4; model uncertainty 0.0183
* Form inputs: days since last match A 338, B 240; matches on record A 411, B 7; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT07ARARUS-ARA  (YES = Haruna Arakawa)
Model: 89%
Kalshi: 57%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zhuoxuan Bai vs Emerson Jones -- WTA 125K Suzhou R16

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-08 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

WTA125 (WTA_125) · surface ? · scheduled 2026-10-08T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT07BAIJON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zhuoxuan Bai (`KXWTACHALLENGERMATCH-26OCT07BAIJON-BAI`) | 0.36 / 0.40 (1) | 38.0% | -- | -- | -- [-----] | -- | 38.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Emerson Jones (`KXWTACHALLENGERMATCH-26OCT07BAIJON-JON`) | 0.56 / 0.63 (46) | 59.5% | -- | -- | -- [-----] | -- | 59.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Haruka Kaji vs Jasmine Adams -- W35 Wagga Wagga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211844:221863:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jasmine Adams (`KXITFWMATCH-26OCT07KAJADA-ADA`) | 0.04 / 0.08 (42) | 6.0% | 5.4% | 27.2% | 14.5% [13.2%-16.1%] | -- | -- | -- | -- | PASS | -0.6 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Haruka Kaji (`KXITFWMATCH-26OCT07KAJADA-KAJ`) | 0.91 / 0.96 (3577) | 93.5% | 94.6% | 72.8% | 85.5% [83.9%-86.8%] | -- | -- | -- | -- | PASS | +1.1 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3255.0, B 296.0; serve-point win A 62.7%, B 49.5%; Elo A 1605.3, B 1274.0; model uncertainty 0.0145
* Form inputs: days since last match A 9, B 198; matches on record A 515, B 12; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.006, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elvina Kalieva vs Tamara Korpatsch -- WTA 125K Suzhou R16

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-08 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

WTA125 (WTA_125) · surface ? · scheduled 2026-10-08T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT07KALKOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elvina Kalieva (`KXWTACHALLENGERMATCH-26OCT07KALKOR-KAL`) | 0.50 / 0.51 (27) | 50.5% | -- | -- | -- [-----] | -- | 48.5% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tamara Korpatsch (`KXWTACHALLENGERMATCH-26OCT07KALKOR-KOR`) | 0.47 / 0.52 (501) | 49.5% | -- | -- | -- [-----] | -- | 51.3% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Ena Shibahara vs Monique Barry -- W35 Wagga Wagga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214262:222667:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Monique Barry (`KXITFWMATCH-26OCT07SHIBAR-BAR`) | 0.07 / 0.10 (1603) | 8.5% | 7.4% | 16.0% | 14.2% [13.4%-15.3%] | -- | -- | -- | -- | WATCH | -1.1 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ena Shibahara (`KXITFWMATCH-26OCT07SHIBAR-SHI`) | 0.90 / 0.93 (3500) | 91.5% | 92.6% | 84.0% | 85.8% [84.7%-86.6%] | -- | -- | -- | -- | PASS | +1.1 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3247.0, B 1840.0; serve-point win A 63.7%, B 47.3%; Elo A 1676.2, B 1331.5; model uncertainty 0.0099
* Form inputs: days since last match A 191, B 198; matches on record A 249, B 209; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high +0.000, surface_dev_loose +0.008, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mutsumi Uemura vs Hikaru Sato -- W35 Wagga Wagga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221141:260828:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hikaru Sato (`KXITFWMATCH-26OCT07UEMSAT-SAT`) | 0.67 / 0.69 (22) | 68.0% | 70.9% | 54.2% | 64.9% [62.5%-67.4%] | -- | -- | -- | -- | PASS | +2.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mutsumi Uemura (`KXITFWMATCH-26OCT07UEMSAT-UEM`) | 0.31 / 0.33 (898) | 32.0% | 29.1% | 45.8% | 35.1% [32.6%-37.5%] | -- | -- | -- | -- | PASS | -2.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 824.0, B 1807.0; serve-point win A 54.6%, B 41.2%; Elo A 1314.4, B 1465.8; model uncertainty 0.0249
* Form inputs: days since last match A 170, B 170; matches on record A 22, B 175; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.005, surface_dev_loose -0.004, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bernard Tomic vs Matteo Arnaldi -- ATP Shanghai R128

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-07 07:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-08 05:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-07 14:15Z
* Recommended handicap-by time: 2026-10-08 04:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · Hard · scheduled 2026-10-07T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:106071:208286:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Arnaldi (`KXATPMATCH-26OCT07TOMARN-ARN`) | 0.66 / 0.67 (7513) | 66.5% | 62.1% | 47.0% | 51.5% [49.0%-58.9%] | -- | -- | -- | -- | PASS | -4.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Bernard Tomic (`KXATPMATCH-26OCT07TOMARN-TOM`) | 0.33 / 0.34 (1352) | 33.5% | 37.9% | 53.0% | 48.5% [41.1%-51.0%] | -- | -- | -- | -- | SHADOW_BET | +4.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5299.0, B 5134.0; serve-point win A 62.4%, B 35.2%; Elo A 1672.1, B 1794.0; model uncertainty 0.0496
* Form inputs: days since last match A 1, B 4; matches on record A 884, B 396; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.030, surface_pool_high +0.020, surface_dev_loose +0.010, surface_dev_tight -0.020
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT07TOMARN-28` Over 27.5 games: 0.27/0.32 mid 29.5%, model 39.5% (projection_v2.0 (prediction ledger)) -- gap +10.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT07TOMARN-23` Over 22.5 games: 0.49/0.51 mid 50.0%, model 59.7% (projection_v2.0 (prediction ledger)) -- gap +9.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT07TOMARN-ARN3` Will Matteo Arnaldi win at least 2.5 more games than Bernard Tomic?: 0.56/0.57 mid 56.5%, model 47.2% (projection_v2.0 (prediction ledger)) -- gap -9.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT07TOMARN-ARN20` Will Matteo Arnaldi win the Bernard Tomic vs Matteo Arnaldi match by a set score of 2-0?: 0.41/0.45 mid 43.0%, model 33.8% (projection_v2.0 (prediction ledger)) -- gap -9.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT07TOMARN-ARN6` Will Matteo Arnaldi win at least 5.5 more games than Bernard Tomic?: 0.19/0.23 mid 21.0%, model 13.5% (projection_v2.0 (prediction ledger)) -- gap -7.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT07TOMARN-18` Over 17.5 games: 0.84/0.89 mid 86.5%, model 92.9% (projection_v2.0 (prediction ledger)) -- gap +6.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT07TOMARN-2-ARN` Will Matteo Arnaldi win set 2 in the Bernard Tomic vs Matteo Arnaldi match: 0.62/0.65 mid 63.5%, model 58.2% (projection_v2.0 (prediction ledger)) -- gap -5.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT07TOMARN-TOM21` Will Bernard Tomic win the Bernard Tomic vs Matteo Arnaldi match by a set score of 2-1?: 0.14/0.17 mid 15.5%, model 20.4% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT07TOMARN-1-ARN` Will Matteo Arnaldi win set 1 in the Bernard Tomic vs Matteo Arnaldi match: 0.61/0.65 mid 63.0%, model 58.2% (projection_v2.0 (prediction ledger)) -- gap -4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT07TOMARN-1-TOM` Will Bernard Tomic win set 1 in the Bernard Tomic vs Matteo Arnaldi match: 0.36/0.38 mid 37.0%, model 41.8% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT07TOMARN-2-TOM` Will Bernard Tomic win set 2 in the Bernard Tomic vs Matteo Arnaldi match: 0.35/0.39 mid 37.0%, model 41.8% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT07TOMARN-ARN21` Will Matteo Arnaldi win the Bernard Tomic vs Matteo Arnaldi match by a set score of 2-1?: 0.22/0.25 mid 23.5%, model 28.3% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT07TOMARN-TOM2` Will Bernard Tomic win at least 1.5 more games than Matteo Arnaldi?: 0.27/0.31 mid 29.0%, model 30.9% (projection_v2.0 (prediction ledger)) -- gap +1.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT07TOMARN-TOM20` Will Bernard Tomic win the Bernard Tomic vs Matteo Arnaldi match by a set score of 2-0?: 0.16/0.19 mid 17.5%, model 17.5% (projection_v2.0 (prediction ledger)) -- gap +0.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Elise Mertens vs Iga Swiatek -- WTA Beijing QF

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-10-08 06:00Z
* Current expected start: 2026-10-08 06:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-07 14:15Z
* Recommended handicap-by time: 2026-10-08 05:15Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-09T04:00:00+00:00 as not a valid time

WTA (MASTERS_1000) · Hard · scheduled 2026-10-08T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:210722:216347:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elise Mertens (`KXWTAMATCH-26OCT07MERSWI-MER`) | 0.20 / 0.21 (19636) | 20.5% | 28.9% | 25.2% | 25.1% [23.9%-26.5%] | 18.2% | -- | 18.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +8.4 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Iga Swiatek (`KXWTAMATCH-26OCT07MERSWI-SWI`) | 0.80 / 0.81 (26890) | 80.5% | 71.1% | 74.8% | 74.9% [73.6%-76.1%] | 81.8% | -- | 81.8% | MODEL_LONE_OUTLIER | PASS | -9.4 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3838.0, B 4863.0; serve-point win A 55.6%, B 40.1%; Elo A 1988.1, B 2178.1; model uncertainty 0.0127
* Form inputs: days since last match A 0, B 0; matches on record A 802, B 542; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.004, surface_dev_loose +0.013, surface_dev_tight -0.012
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT07MERSWI-2-MER` Will Elise Mertens win set 2 in the Elise Mertens vs Iga Swiatek match: 0.23/0.27 mid 25.0%, model 35.6% (projection_v2.0 (prediction ledger)) -- gap +10.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT07MERSWI-2-SWI` Will Iga Swiatek win set 2 in the Elise Mertens vs Iga Swiatek match: 0.73/0.77 mid 75.0%, model 64.4% (projection_v2.0 (prediction ledger)) -- gap -10.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT07MERSWI-1-MER` Will Elise Mertens win set 1 in the Elise Mertens vs Iga Swiatek match: 0.26/0.27 mid 26.5%, model 35.6% (projection_v2.0 (prediction ledger)) -- gap +9.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT07MERSWI-1-SWI` Will Iga Swiatek win set 1 in the Elise Mertens vs Iga Swiatek match: 0.72/0.74 mid 73.0%, model 64.4% (projection_v2.0 (prediction ledger)) -- gap -8.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE

## Olga Danilova vs Naho Sato -- W35 Wagga Wagga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220997:266541:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Olga Danilova (`KXITFWMATCH-26OCT07DANSAT-DAN`) | 0.03 / 0.21 (82) | 12.0% | 18.2% | 47.3% | 31.4% [23.4%-36.9%] | -- | -- | -- | -- | PASS | +6.2 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Naho Sato (`KXITFWMATCH-26OCT07DANSAT-SAT`) | 0.50 / 0.95 (50) | 72.5% | 81.8% | 52.7% | 68.6% [63.1%-76.5%] | -- | -- | -- | -- | PASS | +9.3 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1340.0, B 1522.0; serve-point win A 48.7%, B 44.6%; Elo A 1235.7, B 1476.0; model uncertainty 0.067
* Form inputs: days since last match A 198, B 170; matches on record A 51, B 304; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mio Mushika vs Himari Sato -- W35 Wagga Wagga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216156:222986:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mio Mushika (`KXITFWMATCH-26OCT07MUSSAT-MUS`) | 0.68 / 0.86 (52) | 77.0% | 93.1% | 98.9% | 89.3% [80.4%-95.1%] | -- | -- | -- | -- | PASS | +16.1 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Himari Sato (`KXITFWMATCH-26OCT07MUSSAT-SAT`) | 0.11 / 0.28 (35) | 19.5% | 6.9% | 1.1% | 10.7% [4.9%-19.6%] | -- | -- | -- | -- | PASS | -12.6 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2224.0, B 578.0; serve-point win A 58.4%, B 52.7%; Elo A 1520.7, B 1280.3; model uncertainty 0.0736
* Form inputs: days since last match A 170, B 177; matches on record A 201, B 200; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT07MUSSAT-MUS  (YES = Mio Mushika)
Model: 93%
Kalshi: 77%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.005, surface_dev_loose +0.014, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ashleigh Simes vs Yuno Kitahara -- W35 Wagga Wagga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221929:263881:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuno Kitahara (`KXITFWMATCH-26OCT07SIMKIT-KIT`) | 0.58 / 0.61 (1669) | 59.5% | 49.9% | 53.2% | 48.9% [45.2%-51.1%] | -- | -- | -- | -- | PASS | -9.7 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ashleigh Simes (`KXITFWMATCH-26OCT07SIMKIT-SIM`) | 0.39 / 0.42 (3189) | 40.5% | 50.1% | 46.8% | 51.1% [48.9%-54.8%] | -- | -- | -- | -- | WATCH | +9.7 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 942.0, B 2068.0; serve-point win A 55.0%, B 45.0%; Elo A 1452.9, B 1428.6; model uncertainty 0.0292
* Form inputs: days since last match A 198, B 170; matches on record A 33, B 119; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.021, surface_dev_loose -0.021, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## I Wen Wan vs Tahlia Kokkinis -- W35 Wagga Wagga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260667:267449:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tahlia Kokkinis (`KXITFWMATCH-26OCT07WANKOK-KOK`) | 0.81 / 0.82 (138) | 81.5% | 91.1% | 84.9% | 81.2% [79.1%-82.9%] | -- | -- | -- | -- | PASS | +9.6 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| I Wen Wan (`KXITFWMATCH-26OCT07WANKOK-WAN`) | 0.14 / 0.17 (36) | 15.5% | 8.9% | 15.1% | 18.8% [17.1%-20.9%] | -- | -- | -- | -- | PASS | -6.6 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 553.0, B 1935.0; serve-point win A 51.2%, B 38.6%; Elo A 1276.4, B 1514.8; model uncertainty 0.0192
* Form inputs: days since last match A 219, B 141; matches on record A 26, B 101; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.007, surface_dev_loose -0.004, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Juan Manuel Cerundolo vs Nicolas Mejia -- ATP Shanghai R128

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-07 07:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-08 07:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-07 14:15Z
* Recommended handicap-by time: 2026-10-08 06:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · Hard · scheduled 2026-10-07T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200711:207678:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Manuel Cerundolo (`KXATPMATCH-26OCT07CERMEJ-CER`) | 0.66 / 0.67 (20327) | 66.5% | 69.2% | 66.6% | 66.2% [65.7%-67.1%] | -- | -- | -- | -- | PASS | +2.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nicolas Mejia (`KXATPMATCH-26OCT07CERMEJ-MEJ`) | 0.33 / 0.34 (4336) | 33.5% | 30.8% | 33.4% | 33.8% [32.9%-34.3%] | -- | -- | -- | -- | PASS | -2.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6271.0, B 5242.0; serve-point win A 64.6%, B 39.4%; Elo A 1744.6, B 1635.7; model uncertainty 0.007
* Form inputs: days since last match A 7, B 1; matches on record A 541, B 509; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.004, surface_dev_loose -0.001, surface_dev_tight +0.001
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT07CERMEJ-23` Over 22.5 games: 0.48/0.49 mid 48.5%, model 56.4% (projection_v2.0 (prediction ledger)) -- gap +7.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT07CERMEJ-28` Over 27.5 games: 0.26/0.32 mid 29.0%, model 36.5% (projection_v2.0 (prediction ledger)) -- gap +7.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT07CERMEJ-CER21` Will Juan Manuel Cerundolo win the Juan Manuel Cerundolo vs Nicolas Mejia match by a set score of 2-1?: 0.22/0.25 mid 23.5%, model 29.4% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT07CERMEJ-18` Over 17.5 games: 0.83/0.89 mid 86.0%, model 90.8% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT07CERMEJ-MEJ20` Will Nicolas Mejia win the Juan Manuel Cerundolo vs Nicolas Mejia match by a set score of 2-0?: 0.16/0.19 mid 17.5%, model 13.6% (projection_v2.0 (prediction ledger)) -- gap -3.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT07CERMEJ-MEJ2` Will Nicolas Mejia win at least 1.5 more games than Juan Manuel Cerundolo?: 0.27/0.29 mid 28.0%, model 24.5% (projection_v2.0 (prediction ledger)) -- gap -3.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT07CERMEJ-CER20` Will Juan Manuel Cerundolo win the Juan Manuel Cerundolo vs Nicolas Mejia match by a set score of 2-0?: 0.41/0.45 mid 43.0%, model 39.9% (projection_v2.0 (prediction ledger)) -- gap -3.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT07CERMEJ-CER6` Will Juan Manuel Cerundolo win at least 5.5 more games than Nicolas Mejia?: 0.20/0.23 mid 21.5%, model 18.6% (projection_v2.0 (prediction ledger)) -- gap -2.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT07CERMEJ-CER3` Will Juan Manuel Cerundolo win at least 2.5 more games than Nicolas Mejia?: 0.52/0.53 mid 52.5%, model 55.3% (projection_v2.0 (prediction ledger)) -- gap +2.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT07CERMEJ-MEJ21` Will Nicolas Mejia win the Juan Manuel Cerundolo vs Nicolas Mejia match by a set score of 2-1?: 0.14/0.17 mid 15.5%, model 17.2% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT07CERMEJ-1-CER` Will Juan Manuel Cerundolo win set 1 in the Juan Manuel Cerundolo vs Nicolas Mejia match: 0.61/0.63 mid 62.0%, model 63.1% (projection_v2.0 (prediction ledger)) -- gap +1.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT07CERMEJ-1-MEJ` Will Nicolas Mejia win set 1 in the Juan Manuel Cerundolo vs Nicolas Mejia match: 0.37/0.39 mid 38.0%, model 36.9% (projection_v2.0 (prediction ledger)) -- gap -1.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT07CERMEJ-2-CER` Will Juan Manuel Cerundolo win set 2 in the Juan Manuel Cerundolo vs Nicolas Mejia match: 0.61/0.65 mid 63.0%, model 63.1% (projection_v2.0 (prediction ledger)) -- gap +0.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT07CERMEJ-2-MEJ` Will Nicolas Mejia win set 2 in the Juan Manuel Cerundolo vs Nicolas Mejia match: 0.35/0.39 mid 37.0%, model 36.9% (projection_v2.0 (prediction ledger)) -- gap -0.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Karolina Muchova vs Nikola Bartunkova -- WTA Beijing QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-08 06:00Z
* Current expected start: 2026-10-08 07:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-07 14:15Z
* Recommended handicap-by time: 2026-10-08 06:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+60_MIN

WTA (MASTERS_1000) · Hard · scheduled 2026-10-08T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214096:223360:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikola Bartunkova (`KXWTAMATCH-26OCT07MUCBAR-BAR`) | 0.30 / 0.32 (54879) | 31.0% | 28.0% | 22.2% | 21.5% [20.5%-22.2%] | 30.9% | 31.1% | 31.0% | MODEL_LONE_OUTLIER | PASS | -3.0 pp | NORMAL | FRESH | A / LIMITED | ALL_AGREE | VERIFIED |
| Karolina Muchova (`KXWTAMATCH-26OCT07MUCBAR-MUC`) | 0.68 / 0.70 (31030) | 69.0% | 72.0% | 77.8% | 78.5% [77.8%-79.5%] | 69.1% | 70.0% | 69.6% | MODEL_LONE_OUTLIER | SHADOW_BET | +3.0 pp | NORMAL | FRESH | A / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3972.0, B 3248.0; serve-point win A 62.0%, B 42.5%; Elo A 2141.6, B 1891.4; model uncertainty 0.0085
* Form inputs: days since last match A 1, B 1; matches on record A 479, B 247; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.008, surface_dev_loose +0.007, surface_dev_tight -0.004
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT07MUCBAR-22` Over 21.5 games: 0.49/0.51 mid 50.0%, model 60.0% (projection_v2.0 (prediction ledger)) -- gap +10.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT07MUCBAR-27` Over 26.5 games: 0.26/0.29 mid 27.5%, model 37.3% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT07MUCBAR-17` Over 16.5 games: 0.83/0.89 mid 86.0%, model 93.5% (projection_v2.0 (prediction ledger)) -- gap +7.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT07MUCBAR-2-MUC` Will Karolina Muchova win set 2 in the Karolina Muchova vs Nikola Bartunkova match: 0.66/0.67 mid 66.5%, model 65.1% (projection_v2.0 (prediction ledger)) -- gap -1.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT07MUCBAR-1-MUC` Will Karolina Muchova win set 1 in the Karolina Muchova vs Nikola Bartunkova match: 0.63/0.65 mid 64.0%, model 65.1% (projection_v2.0 (prediction ledger)) -- gap +1.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT07MUCBAR-1-BAR` Will Nikola Bartunkova win set 1 in the Karolina Muchova vs Nikola Bartunkova match: 0.34/0.35 mid 34.5%, model 34.9% (projection_v2.0 (prediction ledger)) -- gap +0.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT07MUCBAR-2-BAR` Will Nikola Bartunkova win set 2 in the Karolina Muchova vs Nikola Bartunkova match: 0.33/0.36 mid 34.5%, model 34.9% (projection_v2.0 (prediction ledger)) -- gap +0.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Matthew Dellavedova vs Jordan Chiu -- M25 Luan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202354:207780:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jordan Chiu (`KXITFMATCH-26OCT07DELCHI-CHI`) | 0.06 / 0.15 (30) | 10.5% | 4.1% | 7.3% | 6.1% [5.5%-6.9%] | -- | -- | -- | -- | PASS | -6.4 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matthew Dellavedova (`KXITFMATCH-26OCT07DELCHI-DEL`) | 0.75 / 0.90 (5) | 82.5% | 95.9% | 92.7% | 93.9% [93.1%-94.5%] | -- | -- | -- | -- | PASS | +13.4 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4623.0, B 402.0; serve-point win A 66.8%, B 46.7%; Elo A 1490.7, B 1004.9; model uncertainty 0.0071
* Form inputs: days since last match A 15, B 163; matches on record A 470, B 30; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.003, surface_dev_loose +0.003, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nino Ehrenschneider vs Sasikumar Mukund -- M25 Luan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-08T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07EHRMUK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nino Ehrenschneider (`KXITFMATCH-26OCT07EHRMUK-EHR`) | 0.50 / 0.71 (0) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sasikumar Mukund (`KXITFMATCH-26OCT07EHRMUK-MUK`) | 0.28 / 0.44 (45) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuta Tomida vs Petr Bar Biryukov -- M25 Luan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209951:212616:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Petr Bar Biryukov (`KXITFMATCH-26OCT07TOMBAR-BAR`) | 0.20 / 0.81 (0) | 50.5% | 72.6% | 56.9% | 69.1% [64.6%-74.6%] | -- | -- | -- | -- | PASS | +22.1 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Yuta Tomida (`KXITFMATCH-26OCT07TOMBAR-TOM`) | 0.04 / 0.22 (0) | 13.0% | 27.4% | 43.1% | 30.9% [25.4%-35.4%] | -- | -- | -- | -- | PASS | +14.4 pp | REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 2056.0, B 4649.0; serve-point win A 61.6%, B 33.6%; Elo A 1281.3, B 1553.4; model uncertainty 0.0498
* Form inputs: days since last match A 135, B 8; matches on record A 55, B 248; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT07TOMBAR-BAR  (YES = Petr Bar Biryukov)
Model: 73%
Kalshi: 50%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, EVENT_MAPPING_RISK, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose +0.009, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Taiyo Yamanaka vs Anton Shepp -- M25 Luan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208277:209394:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anton Shepp (`KXITFMATCH-26OCT07YAMSHE-SHE`) | 0.72 / 0.77 (9) | 74.5% | 73.9% | 83.3% | 79.3% [73.8%-82.3%] | -- | -- | -- | -- | PASS | -0.6 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Taiyo Yamanaka (`KXITFMATCH-26OCT07YAMSHE-YAM`) | 0.21 / 0.25 (0) | 23.0% | 26.1% | 16.7% | 20.6% [17.7%-26.2%] | -- | -- | -- | -- | PASS | +3.1 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2717.0, B 2301.0; serve-point win A 61.9%, B 32.9%; Elo A 1310.2, B 1470.9; model uncertainty 0.0426
* Form inputs: days since last match A 142, B 17; matches on record A 191, B 75; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high +0.000, surface_dev_loose -0.013, surface_dev_tight +0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arakawa / Nishimoto vs Barry / Sawashiro -- W35 Wagga Wagga QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-08T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07ARANISBARSAW:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arakawa / Nishimoto (`KXITFWDOUBLES-26OCT07ARANISBARSAW-ARANIS`) | 0.05 / 0.64 (69) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Barry / Sawashiro (`KXITFWDOUBLES-26OCT07ARANISBARSAW-BARSAW`) | 0.05 / 0.90 (50) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Arakawa / Uemura vs Adams / Dodaj -- W35 Wagga Wagga QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-08T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07ARAUEMADADOD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adams / Dodaj (`KXITFWDOUBLES-26OCT07ARAUEMADADOD-ADADOD`) | 0.05 / 0.90 (50) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arakawa / Uemura (`KXITFWDOUBLES-26OCT07ARAUEMADADOD-ARAUEM`) | 0.05 / 0.90 (50) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Carbis / Swarbrick vs Hosoki / Sato -- W35 Wagga Wagga QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-08T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07CARSWAHOSSAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carbis / Swarbrick (`KXITFWDOUBLES-26OCT07CARSWAHOSSAT-CARSWA`) | 0.05 / 0.90 (50) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hosoki / Sato (`KXITFWDOUBLES-26OCT07CARSWAHOSSAT-HOSSAT`) | 0.05 / 0.90 (50) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Yiru Chen vs Anna Yang -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264242:266372:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yiru Chen (`KXITFWMATCH-26OCT07CHEYAN-CHE`) | 0.31 / 0.50 (50) | 40.5% | 47.6% | 33.4% | 40.5% [38.9%-41.5%] | -- | -- | -- | -- | PASS | +7.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anna Yang (`KXITFWMATCH-26OCT07CHEYAN-YAN`) | 0.47 / 0.63 (46) | 55.0% | 52.4% | 66.6% | 59.5% [58.5%-61.1%] | -- | -- | -- | -- | PASS | -2.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 625.0, B 270.0; serve-point win A 53.2%, B 46.4%; Elo A 1245.2, B 1302.6; model uncertainty 0.0129
* Form inputs: days since last match A 163, B 345; matches on record A 28, B 21; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Francesca Franchi vs Yuhan Wang -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260596:264205:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesca Franchi (`KXITFWMATCH-26OCT07FRAWAN-FRA`) | 0.03 / 0.20 (31) | 11.5% | 4.0% | 46.3% | 17.5% [17.5%-18.2%] | -- | -- | -- | -- | PASS | -7.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuhan Wang (`KXITFWMATCH-26OCT07FRAWAN-WAN`) | 0.74 / 0.95 (50) | 84.5% | 96.0% | 53.7% | 82.5% [81.8%-82.5%] | -- | -- | -- | -- | PASS | +11.5 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 1724.0; serve-point win A 47.0%, B 39.9%; Elo A 1163.5, B 1428.1; model uncertainty 0.0035
* Form inputs: days since last match A 709, B 6; matches on record A 8, B 44; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.007, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Varvara Panshina vs Soo Ha Jang -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260122:267420:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Soo Ha Jang (`KXITFWMATCH-26OCT07PANJAN-JAN`) | 0.09 / 0.22 (83) | 15.5% | 12.7% | 19.2% | 21.4% [19.2%-23.5%] | -- | -- | -- | -- | PASS | -2.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Varvara Panshina (`KXITFWMATCH-26OCT07PANJAN-PAN`) | 0.70 / 0.92 (3549) | 81.0% | 87.4% | 80.8% | 78.5% [76.5%-80.8%] | -- | -- | -- | -- | PASS | +6.3 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2447.0, B 726.0; serve-point win A 56.9%, B 51.6%; Elo A 1546.4, B 1328.4; model uncertainty 0.0215
* Form inputs: days since last match A 86, B 163; matches on record A 102, B 42; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.004, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stevens / Thompson vs Khan / McKenzie -- W35 Wagga Wagga QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-08T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07STETHOKHAMCK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Khan / McKenzie (`KXITFWDOUBLES-26OCT07STETHOKHAMCK-KHAMCK`) | 0.05 / 0.90 (50) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stevens / Thompson (`KXITFWDOUBLES-26OCT07STETHOKHAMCK-STETHO`) | 0.05 / 0.90 (50) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Xiao Tang vs Jiaqi Wang -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221181:267516:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xiao Tang (`KXITFWMATCH-26OCT07TANWAN-TAN`) | 0.15 / 0.30 (36) | 22.5% | 6.5% | 8.4% | 14.8% [13.3%-15.5%] | -- | -- | -- | -- | PASS | -16.0 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jiaqi Wang (`KXITFWMATCH-26OCT07TANWAN-WAN`) | 0.63 / 0.85 (3539) | 74.0% | 93.5% | 91.6% | 85.2% [84.5%-86.7%] | -- | -- | -- | -- | PASS | +19.5 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 206.0, B 2849.0; serve-point win A 47.2%, B 41.5%; Elo A 1253.5, B 1543.7; model uncertainty 0.0109
* Form inputs: days since last match A 163, B 163; matches on record A 6, B 250; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT07TANWAN-WAN  (YES = Jiaqi Wang)
Model: 94%
Kalshi: 74%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.003, surface_dev_loose -0.006, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Su-Wei Hsieh / Jelena Ostapenko vs Erin Routliffe / Aldila Sutjiadi -- WTA Beijing QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-07 14:15Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-09T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-08T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT08HSIOSTROUSUT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Su-Wei Hsieh / Jelena Ostapenko (`KXWTADOUBLES-26OCT08HSIOSTROUSUT-HSIOST`) | 0.59 / 0.64 (301) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Erin Routliffe / Aldila Sutjiadi (`KXWTADOUBLES-26OCT08HSIOSTROUSUT-ROUSUT`) | 0.36 / 0.40 (192) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Katerina Siniakova / Shuai Zhang vs Storm Hunter / Kristina Mladenovic -- WTA Beijing QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-07 14:15Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-09T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-08T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT08SINZHAHUNMLA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Storm Hunter / Kristina Mladenovic (`KXWTADOUBLES-26OCT08SINZHAHUNMLA-HUNMLA`) | 0.22 / 0.28 (35) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Katerina Siniakova / Shuai Zhang (`KXWTADOUBLES-26OCT08SINZHAHUNMLA-SINZHA`) | 0.70 / 0.76 (23) | 73.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Yanki Erel vs Egor Pleshivtsev -- M25 Luan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207129:212574:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yanki Erel (`KXITFMATCH-26OCT07EREPLE-ERE`) | 0.69 / 0.89 (0) | 79.0% | 86.5% | 87.8% | 87.3% [86.0%-88.0%] | -- | -- | -- | -- | PASS | +7.5 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Egor Pleshivtsev (`KXITFMATCH-26OCT07EREPLE-PLE`) | 0.06 / 0.21 (32) | 13.5% | 13.5% | 12.2% | 12.7% [12.0%-14.0%] | -- | -- | -- | -- | PASS | +0.0 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4125.0, B 2112.0; serve-point win A 66.5%, B 42.2%; Elo A 1607.3, B 1289.3; model uncertainty 0.0102
* Form inputs: days since last match A 8, B 128; matches on record A 405, B 47; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.005, surface_dev_loose -0.001, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xirui Han vs Yaojie ZENG -- M25 Luan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210483:212472:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xirui Han (`KXITFMATCH-26OCT07HANZEN-HAN`) | 0.18 / 0.20 (24) | 19.0% | 28.2% | 38.9% | 33.6% [32.6%-34.5%] | -- | -- | -- | -- | PASS | +9.2 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yaojie ZENG (`KXITFMATCH-26OCT07HANZEN-ZEN`) | 0.69 / 0.81 (0) | 75.0% | 71.8% | 61.2% | 66.5% [65.5%-67.4%] | -- | -- | -- | -- | PASS | -3.2 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 578.0, B 2095.0; serve-point win A 58.4%, B 37.2%; Elo A 1158.3, B 1292.5; model uncertainty 0.0094
* Form inputs: days since last match A 128, B 8; matches on record A 18, B 84; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.009, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dong Ju Kim vs Yan Cheng CHEN -- M25 Luan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207456:212460:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yan Cheng CHEN (`KXITFMATCH-26OCT07KIMCHE-CHE`) | 0.24 / 0.26 (19) | 25.0% | 30.9% | 30.3% | 33.2% [31.2%-34.7%] | -- | -- | -- | -- | WATCH | +5.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dong Ju Kim (`KXITFMATCH-26OCT07KIMCHE-KIM`) | 0.63 / 0.74 (0) | 68.5% | 69.1% | 69.7% | 66.8% [65.3%-68.8%] | -- | -- | -- | -- | PASS | +0.6 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1970.0, B 1203.0; serve-point win A 58.9%, B 44.9%; Elo A 1358.9, B 1253.4; model uncertainty 0.0173
* Form inputs: days since last match A 135, B 128; matches on record A 64, B 28; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ko Suzuki vs Mert Alkaya -- M25 Luan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:120545:207368:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mert Alkaya (`KXITFMATCH-26OCT07SUZALK-ALK`) | 0.73 / 0.90 (5) | 81.5% | 95.2% | 94.6% | 91.8% [89.7%-93.9%] | -- | -- | -- | -- | PASS | +13.7 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ko Suzuki (`KXITFMATCH-26OCT07SUZALK-SUZ`) | 0.05 / 0.27 (35) | 16.0% | 4.8% | 5.4% | 8.2% [6.1%-10.3%] | -- | -- | -- | -- | PASS | -11.2 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 513.0, B 4252.0; serve-point win A 53.5%, B 33.6%; Elo A 1156.2, B 1551.0; model uncertainty 0.021
* Form inputs: days since last match A 128, B 17; matches on record A 140, B 200; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.002, surface_dev_loose -0.006, surface_dev_tight +0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Meiqi Guo vs Daria Egorova -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216162:266864:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daria Egorova (`KXITFWMATCH-26OCT07GUOEGO-EGO`) | 0.58 / 0.79 (31) | 68.5% | 71.8% | 73.8% | 71.6% [66.0%-74.7%] | -- | -- | -- | -- | PASS | +3.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Meiqi Guo (`KXITFWMATCH-26OCT07GUOEGO-GUO`) | 0.15 / 0.33 (37) | 24.0% | 28.2% | 26.2% | 28.4% [25.3%-34.0%] | -- | -- | -- | -- | PASS | +4.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2729.0, B 2142.0; serve-point win A 52.9%, B 42.7%; Elo A 1542.5, B 1672.8; model uncertainty 0.0433
* Form inputs: days since last match A 10, B 8; matches on record A 272, B 86; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.004, surface_dev_loose -0.009, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yanan Hou vs Alina Yuneva -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:261066:269753:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yanan Hou (`KXITFWMATCH-26OCT07HOUYUN-HOU`) | 0.77 / 0.85 (0) | 81.0% | 84.4% | 89.8% | 75.7% [69.5%-83.9%] | -- | -- | -- | -- | PASS | +3.4 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alina Yuneva (`KXITFWMATCH-26OCT07HOUYUN-YUN`) | 0.13 / 0.21 (0) | 17.0% | 15.6% | 10.2% | 24.3% [16.1%-30.5%] | -- | -- | -- | -- | PASS | -1.4 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 995.0, B 449.0; serve-point win A 56.3%, B 51.3%; Elo A 1360.3, B 1208.9; model uncertainty 0.0724
* Form inputs: days since last match A 163, B 163; matches on record A 120, B 15; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.016, surface_dev_loose +0.016, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gaeul Jang vs Fang An Lin -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:252586:260638:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gaeul Jang (`KXITFWMATCH-26OCT07JANLIN-JAN`) | 0.49 / 0.69 (3254) | 59.0% | 63.0% | 42.6% | 53.2% [49.5%-59.0%] | -- | -- | -- | -- | PASS | +4.0 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Fang An Lin (`KXITFWMATCH-26OCT07JANLIN-LIN`) | 0.27 / 0.49 (99) | 38.0% | 37.0% | 57.4% | 46.8% [41.0%-50.5%] | -- | -- | -- | -- | PASS | -1.1 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1146.0, B 762.0; serve-point win A 55.8%, B 46.7%; Elo A 1400.2, B 1341.7; model uncertainty 0.0475
* Form inputs: days since last match A 18, B 170; matches on record A 81, B 114; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.016, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marianna Shikhanova vs Junhan Zhang -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260694:269845:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marianna Shikhanova (`KXITFWMATCH-26OCT07SHIZHA-SHI`) | 0.16 / 0.32 (87) | 24.0% | 10.4% | 45.8% | 27.2% [26.2%-28.1%] | -- | -- | -- | -- | PASS | -13.6 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Junhan Zhang (`KXITFWMATCH-26OCT07SHIZHA-ZHA`) | 0.62 / 0.85 (3256) | 73.5% | 89.6% | 54.2% | 72.8% [71.9%-73.8%] | -- | -- | -- | -- | PASS | +16.1 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 49.0, B 2226.0; serve-point win A 52.3%, B 38.1%; Elo A 1210.1, B 1384.4; model uncertainty 0.0093
* Form inputs: days since last match A 345, B 9; matches on record A 6, B 95; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT07SHIZHA-ZHA  (YES = Junhan Zhang)
Model: 90%
Kalshi: 74%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high -0.000, surface_dev_loose +0.001, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ekaterina Alexandrova vs Mirra Andreeva -- WTA Beijing QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-08 06:00Z
* Current expected start: 2026-10-08 11:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-07 14:15Z
* Recommended handicap-by time: 2026-10-08 10:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+300_MIN

WTA (MASTERS_1000) · Hard · scheduled 2026-10-08T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:206420:259799:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Alexandrova (`KXWTAMATCH-26OCT07ALEAND-ALE`) | 0.25 / 0.26 (62648) | 25.5% | 25.8% | 23.1% | 25.1% [23.1%-32.7%] | 25.5% | 24.6% | 25.1% | MODEL_LONE_OUTLIER | PASS | +0.3 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Mirra Andreeva (`KXWTAMATCH-26OCT07ALEAND-AND`) | 0.75 / 0.76 (38119) | 75.5% | 74.2% | 76.9% | 74.9% [67.3%-76.9%] | 74.5% | 75.5% | 75.0% | MODEL_LONE_OUTLIER | PASS | -1.3 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4877.0, B 4895.0; serve-point win A 55.0%, B 40.1%; Elo A 1948.0, B 2079.9; model uncertainty 0.048
* Form inputs: days since last match A 1, B 1; matches on record A 741, B 262; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.008, surface_dev_loose -0.016, surface_dev_tight +0.013
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT07ALEAND-22` Over 21.5 games: 0.44/0.46 mid 45.0%, model 57.2% (projection_v2.0 (prediction ledger)) -- gap +12.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT07ALEAND-27` Over 26.5 games: 0.21/0.28 mid 24.5%, model 34.9% (projection_v2.0 (prediction ledger)) -- gap +10.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT07ALEAND-17` Over 16.5 games: 0.80/0.84 mid 82.0%, model 91.4% (projection_v2.0 (prediction ledger)) -- gap +9.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT07ALEAND-2-ALE` Will Ekaterina Alexandrova win set 2 in the Ekaterina Alexandrova vs Mirra Andreeva match: 0.29/0.31 mid 30.0%, model 33.3% (projection_v2.0 (prediction ledger)) -- gap +3.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT07ALEAND-1-ALE` Will Ekaterina Alexandrova win set 1 in the Ekaterina Alexandrova vs Mirra Andreeva match: 0.29/0.32 mid 30.5%, model 33.3% (projection_v2.0 (prediction ledger)) -- gap +2.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT07ALEAND-1-AND` Will Mirra Andreeva win set 1 in the Ekaterina Alexandrova vs Mirra Andreeva match: 0.68/0.71 mid 69.5%, model 66.7% (projection_v2.0 (prediction ledger)) -- gap -2.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT07ALEAND-2-AND` Will Mirra Andreeva win set 2 in the Ekaterina Alexandrova vs Mirra Andreeva match: 0.68/0.71 mid 69.5%, model 66.7% (projection_v2.0 (prediction ledger)) -- gap -2.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: WIDE_SPREAD

## Barsukov / Ehrenschneider vs Tang / Zhao -- M25 Luan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-08T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT08BAREHRTANZHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barsukov / Ehrenschneider (`KXITFDOUBLES-26OCT08BAREHRTANZHA-BAREHR`) | 0.05 / 0.71 (86) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tang / Zhao (`KXITFDOUBLES-26OCT08BAREHRTANZHA-TANZHA`) | 0.05 / 0.53 (53) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Becroft / Shepp vs Masabayashi / Yamanaka -- M25 Luan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-08T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT08BECSHEMASYAM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Becroft / Shepp (`KXITFDOUBLES-26OCT08BECSHEMASYAM-BECSHE`) | 0.05 / 0.81 (131) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Masabayashi / Yamanaka (`KXITFDOUBLES-26OCT08BECSHEMASYAM-MASYAM`) | 0.05 / 0.95 (124) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Dong / LIU vs Inui / Yang -- M25 Luan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-08T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT08DONLIUINUYAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dong / LIU (`KXITFDOUBLES-26OCT08DONLIUINUYAN-DONLIU`) | 0.05 / 0.95 (124) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Inui / Yang (`KXITFDOUBLES-26OCT08DONLIUINUYAN-INUYAN`) | 0.05 / 0.95 (124) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Huang / Jeong vs Bar Biryukov / Hongyu -- M25 Luan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-08T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT08HUAJEOBARHON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bar Biryukov / Hongyu (`KXITFDOUBLES-26OCT08HUAJEOBARHON-BARHON`) | 0.05 / 0.95 (124) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Huang / Jeong (`KXITFDOUBLES-26OCT08HUAJEOBARHON-HUAJEO`) | 0.05 / 0.77 (108) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Abhilasha Bista vs Julia Khramtsova -- W15 Islamabad R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260238:263706:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Abhilasha Bista (`KXITFWMATCH-26OCT08BISKHR-BIS`) | 0.03 / 0.95 (50) | 49.0% | 9.5% | 12.2% | 22.2% [17.4%-24.3%] | -- | -- | -- | -- | PASS | -39.5 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Julia Khramtsova (`KXITFWMATCH-26OCT08BISKHR-KHR`) | 0.03 / 0.95 (50) | 49.0% | 90.5% | 87.8% | 77.8% [75.7%-82.6%] | -- | -- | -- | -- | PASS | +41.5 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 183.0, B 401.0; serve-point win A 47.4%, B 42.8%; Elo A 1046.6, B 1250.4; model uncertainty 0.0348
* Form inputs: days since last match A 177, B 345; matches on record A 43, B 31; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT08BISKHR-KHR  (YES = Julia Khramtsova)
Model: 91%
Kalshi: 49%
Gap: +42 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Astrid Cirotte vs Gloria Levinsky -- W15 Islamabad R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:236980:270182:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Astrid Cirotte (`KXITFWMATCH-26OCT08CIRLEV-CIR`) | 0.05 / 0.94 (25) | 49.5% | 81.9% | 61.5% | 64.6% [62.6%-65.6%] | -- | -- | -- | -- | PASS | +32.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gloria Levinsky (`KXITFWMATCH-26OCT08CIRLEV-LEV`) | 0.04 / 0.94 (25) | 49.0% | 18.1% | 38.5% | 35.4% [34.4%-37.4%] | -- | -- | -- | -- | PASS | -30.9 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2379.0, B 45.0; serve-point win A 57.9%, B 48.9%; Elo A 1366.7, B 1264.2; model uncertainty 0.0151
* Form inputs: days since last match A 177, B 429; matches on record A 227, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT08CIRLEV-CIR  (YES = Astrid Cirotte)
Model: 82%
Kalshi: 50%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Florentine Dekkers vs Kamonwan Yodpetch -- W15 Islamabad R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223334:259907:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Florentine Dekkers (`KXITFWMATCH-26OCT08DEKYOD-DEK`) | 0.05 / 0.94 (30) | 49.5% | 14.9% | 60.0% | 37.4% [36.4%-37.4%] | -- | -- | -- | -- | PASS | -34.5 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Kamonwan Yodpetch (`KXITFWMATCH-26OCT08DEKYOD-YOD`) | 0.04 / 0.94 (25) | 49.0% | 85.0% | 40.0% | 62.6% [62.6%-63.6%] | -- | -- | -- | -- | PASS | +36.0 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 1037.0; serve-point win A 50.5%, B 41.7%; Elo A 1233.7, B 1326.6; model uncertainty 0.0051
* Form inputs: days since last match A 786, B 163; matches on record A 21, B 72; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT08DEKYOD-YOD  (YES = Kamonwan Yodpetch)
Model: 85%
Kalshi: 49%
Gap: +36 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Egorova / Yuneva vs Kakenova / Toregen -- W15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-08T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT08EGOYUNKAKTOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Egorova / Yuneva (`KXITFWDOUBLES-26OCT08EGOYUNKAKTOR-EGOYUN`) | 0.05 / 0.90 (50) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kakenova / Toregen (`KXITFWDOUBLES-26OCT08EGOYUNKAKTOR-KAKTOR`) | 0.05 / 0.90 (50) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Ksenia Laskutova vs Sofiia Suslova -- W15 Islamabad R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215372:252582:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ksenia Laskutova (`KXITFWMATCH-26OCT08LASSUS-LAS`) | 0.03 / 0.83 (147) | 43.0% | 73.0% | 78.9% | 72.6% [69.4%-76.1%] | -- | -- | -- | -- | PASS | +30.0 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sofiia Suslova (`KXITFWMATCH-26OCT08LASSUS-SUS`) | 0.03 / 0.95 (50) | 49.0% | 27.0% | 21.1% | 27.4% [23.9%-30.6%] | -- | -- | -- | -- | PASS | -22.0 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1449.0, B 719.0; serve-point win A 56.0%, B 48.6%; Elo A 1432.2, B 1288.2; model uncertainty 0.0333
* Form inputs: days since last match A 163, B 219; matches on record A 372, B 38; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT08LASSUS-LAS  (YES = Ksenia Laskutova)
Model: 73%
Kalshi: 43%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.000, surface_dev_loose +0.009, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lu / Wang vs Han / Yang -- W15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-08T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT08LUXWANHANYAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Han / Yang (`KXITFWDOUBLES-26OCT08LUXWANHANYAN-HANYAN`) | 0.05 / 0.90 (50) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lu / Wang (`KXITFWDOUBLES-26OCT08LUXWANHANYAN-LUXWAN`) | 0.05 / 0.90 (50) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Panshina / Suvirdjonkova vs Ren / Tang -- W15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-08T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT08PANSUVRENTAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Panshina / Suvirdjonkova (`KXITFWDOUBLES-26OCT08PANSUVRENTAN-PANSUV`) | 0.05 / 0.90 (50) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ren / Tang (`KXITFWDOUBLES-26OCT08PANSUVRENTAN-RENTAN`) | 0.05 / 0.90 (50) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Cameron Norrie vs Dalibor Svrcina -- ATP Shanghai R128

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-08 07:00Z
* Current expected start: 2026-10-08 11:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-07 14:15Z
* Recommended handicap-by time: 2026-10-08 10:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+270_MIN

ATP (MASTERS_1000) · Hard · scheduled 2026-10-08T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111815:207494:2026-10-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cameron Norrie (`KXATPMATCH-26OCT08NORSVR-NOR`) | 0.64 / 0.65 (29772) | 64.5% | 58.4% | 52.6% | 56.8% [54.7%-59.9%] | 63.9% | 63.5% | 63.7% | MODEL_LONE_OUTLIER | PASS | -6.1 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Dalibor Svrcina (`KXATPMATCH-26OCT08NORSVR-SVR`) | 0.35 / 0.36 (6537) | 35.5% | 41.6% | 47.4% | 43.2% [40.2%-45.3%] | 36.1% | 36.5% | 36.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.1 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5827.0, B 5222.0; serve-point win A 58.6%, B 43.0%; Elo A 1904.7, B 1746.9; model uncertainty 0.0257
* Form inputs: days since last match A 6, B 1; matches on record A 675, B 423; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose -0.010, surface_dev_tight +0.010
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT08NORSVR-NOR3` Will Cameron Norrie win at least 2.5 more games than Dalibor Svrcina?: 0.57/0.58 mid 57.5%, model 45.7% (projection_v2.0 (prediction ledger)) -- gap -11.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT08NORSVR-NOR20` Will Cameron Norrie win the Cameron Norrie vs Dalibor Svrcina match by a set score of 2-0?: 0.41/0.43 mid 42.0%, model 30.9% (projection_v2.0 (prediction ledger)) -- gap -11.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT08NORSVR-23` Over 22.5 games: 0.45/0.47 mid 46.0%, model 56.4% (projection_v2.0 (prediction ledger)) -- gap +10.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT08NORSVR-28` Over 27.5 games: 0.22/0.29 mid 25.5%, model 35.0% (projection_v2.0 (prediction ledger)) -- gap +9.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT08NORSVR-NOR6` Will Cameron Norrie win at least 5.5 more games than Dalibor Svrcina?: 0.23/0.29 mid 26.0%, model 17.4% (projection_v2.0 (prediction ledger)) -- gap -8.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT08NORSVR-18` Over 17.5 games: 0.77/0.83 mid 80.0%, model 88.6% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT08NORSVR-SVR21` Will Dalibor Svrcina win the Cameron Norrie vs Dalibor Svrcina match by a set score of 2-1?: 0.14/0.18 mid 16.0%, model 21.9% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT08NORSVR-1-NOR` Will Cameron Norrie win set 1 in the Cameron Norrie vs Dalibor Svrcina match: 0.60/0.63 mid 61.5%, model 55.6% (projection_v2.0 (prediction ledger)) -- gap -5.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT08NORSVR-1-SVR` Will Dalibor Svrcina win set 1 in the Cameron Norrie vs Dalibor Svrcina match: 0.37/0.40 mid 38.5%, model 44.4% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT08NORSVR-2-SVR` Will Dalibor Svrcina win set 2 in the Cameron Norrie vs Dalibor Svrcina match: 0.37/0.40 mid 38.5%, model 44.4% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT08NORSVR-SVR2` Will Dalibor Svrcina win at least 1.5 more games than Cameron Norrie?: 0.28/0.31 mid 29.5%, model 35.1% (projection_v2.0 (prediction ledger)) -- gap +5.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT08NORSVR-2-NOR` Will Cameron Norrie win set 2 in the Cameron Norrie vs Dalibor Svrcina match: 0.59/0.63 mid 61.0%, model 55.6% (projection_v2.0 (prediction ledger)) -- gap -5.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT08NORSVR-NOR21` Will Cameron Norrie win the Cameron Norrie vs Dalibor Svrcina match by a set score of 2-1?: 0.21/0.24 mid 22.5%, model 27.5% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT08NORSVR-SVR20` Will Dalibor Svrcina win the Cameron Norrie vs Dalibor Svrcina match by a set score of 2-0?: 0.17/0.20 mid 18.5%, model 19.7% (projection_v2.0 (prediction ledger)) -- gap +1.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Joshua Charlton vs Sam Ryan Ziegann -- M25 Darwin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT08CHARYA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joshua Charlton (`KXITFMATCH-26OCT08CHARYA-CHA`) | 0.64 / 0.68 (0) | 66.0% | 67.7% | -- | -- [-----] | -- | -- | -- | -- | -- | +1.7 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Sam Ryan Ziegann (`KXITFMATCH-26OCT08CHARYA-RYA`) | 0.30 / 0.36 (40) | 33.0% | 32.3% | -- | -- [-----] | -- | -- | -- | -- | -- | -0.7 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 68.0%, B 35.8%; Elo A 1296.7, B 1199.2; model uncertainty None
* Form inputs: days since last match A 142, B 30; matches on record A 114, B 93; data quality B
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ethan Cook vs Philip Sekulic -- M25 Darwin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT08COOSEK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ethan Cook (`KXITFMATCH-26OCT08COOSEK-COO`) | 0.11 / 0.13 (103) | 12.0% | 13.1% | -- | -- [-----] | 13.8% | -- | -- | INSUFFICIENT_INPUTS | -- | +1.1 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Philip Sekulic (`KXITFMATCH-26OCT08COOSEK-SEK`) | 0.85 / 0.90 (1885) | 87.5% | 86.9% | -- | -- [-----] | 86.2% | -- | -- | INSUFFICIENT_INPUTS | -- | -0.6 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 58.0%, B 33.1%; Elo A 1214.6, B 1556.4; model uncertainty None
* Form inputs: days since last match A 135, B 15; matches on record A 69, B 274; data quality B
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chen Dong vs Stefan Vujic -- M25 Darwin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT08DONVUJ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chen Dong (`KXITFMATCH-26OCT08DONVUJ-DON`) | 0.50 / 0.54 (25) | 52.0% | 62.0% | -- | -- [-----] | -- | -- | -- | -- | -- | +10.0 pp | REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Stefan Vujic (`KXITFMATCH-26OCT08DONVUJ-VUJ`) | 0.44 / 0.49 (0) | 46.5% | 38.0% | -- | -- [-----] | -- | -- | -- | -- | -- | -8.5 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 67.5%, B 35.0%; Elo A 1305.5, B 1177.4; model uncertainty None
* Form inputs: days since last match A 177, B 128; matches on record A 42, B 105; data quality B
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Casey Hoole vs Tai Leonard Sach -- M25 Darwin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-08T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT08HOOSAC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Casey Hoole (`KXITFMATCH-26OCT08HOOSAC-HOO`) | 0.55 / 0.59 (0) | 57.0% | 47.6% | -- | -- [-----] | -- | -- | -- | -- | -- | -9.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Tai Leonard Sach (`KXITFMATCH-26OCT08HOOSAC-SAC`) | 0.38 / 0.44 (45) | 41.0% | 52.4% | -- | -- [-----] | -- | -- | -- | -- | -- | +11.4 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 62.1%, B 37.4%; Elo A 1380.2, B 1417.8; model uncertainty None
* Form inputs: days since last match A 646, B 128; matches on record A 17, B 86; data quality F
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elena Jamshidi vs Sabrina Olimjanova -- W15 Islamabad R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-08T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT08JAMOLI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elena Jamshidi (`KXITFWMATCH-26OCT08JAMOLI-JAM`) | 0.03 / 0.95 (50) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sabrina Olimjanova (`KXITFWMATCH-26OCT08JAMOLI-OLI`) | 0.03 / 0.95 (50) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## suzuna oigawa vs Wozuko Mdlulwa -- W15 Islamabad R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-08T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT08OIGMDL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wozuko Mdlulwa (`KXITFWMATCH-26OCT08OIGMDL-MDL`) | 0.03 / 0.95 (50) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| suzuna oigawa (`KXITFWMATCH-26OCT08OIGMDL-OIG`) | 0.03 / 0.95 (50) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Varvara Rubtsova vs Anastasiya Kuparev -- W15 Islamabad R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-08T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT08RUBKUP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasiya Kuparev (`KXITFWMATCH-26OCT08RUBKUP-KUP`) | 0.03 / 0.95 (50) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Varvara Rubtsova (`KXITFWMATCH-26OCT08RUBKUP-RUB`) | 0.03 / 0.95 (50) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Emma Van Poppel vs Sevil Yuldasheva -- W15 Islamabad R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-08 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-08T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT08VANYUL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emma Van Poppel (`KXITFWMATCH-26OCT08VANYUL-VAN`) | 0.05 / 0.94 (40) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sevil Yuldasheva (`KXITFWMATCH-26OCT08VANYUL-YUL`) | 0.04 / 0.94 (25) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sara Errani / Jasmine Paolini vs Gabriela Dabrowski / Luisa Stefani -- WTA Beijing QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-08 08:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-08 12:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-07 14:15Z
* Recommended handicap-by time: 2026-10-08 11:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-08T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT08ERRPAODABSTE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriela Dabrowski / Luisa Stefani (`KXWTADOUBLES-26OCT08ERRPAODABSTE-DABSTE`) | 0.50 / 0.56 (377) | 53.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sara Errani / Jasmine Paolini (`KXWTADOUBLES-26OCT08ERRPAODABSTE-ERRPAO`) | 0.44 / 0.48 (48) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
