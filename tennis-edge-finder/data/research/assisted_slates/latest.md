# ASSISTED SLATE -- 2026-10-16T09:07Z (`SL-20261016T090724Z-33cf831c`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

187 open matches not seen started, 464 markets. Skipped: {"scheduled_start_over_24h_past": 15, "first_ball_already_observed": 4}. Sources: shadow board 2026-10-16T05:03:16.849492+00:00, Model 4 2026-10-16T05:03:35.739621+00:00, Gen-1 ledger 2026-10-16T05:03:13.374223+00:00, external 2026-10-16T08:47:58.369503+00:00, capture 20261016T084615Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-10-16 09:07Z**
* Recommended RUN TENNIS time: **2026-10-16 08:22Z**  (**OVERDUE -- run now**)
* Final price/status check time: **2026-10-16 08:57Z**
* Number of matches in window: 2 (Daniil Medvedev vs Tommy Paul, Ann Li vs Iga Swiatek)

Slate built 2026-10-16T09:07Z. Refresh due by: 2026-10-16 08:22Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 32, "HIGH_REVIEW": 33, "NORMAL": 119, "REVIEW": 27, "UNPRICED": 253}; match winners: {"EXTREME": 32, "HIGH_REVIEW": 32, "NORMAL": 101, "REVIEW": 25, "UNPRICED": 184}; quote freshness at build: {"FRESH": 211}.

## Benjamin Pietri vs Finn Murgett -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-15 13:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-15T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202125:208818:2026-10-15`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Finn Murgett (`KXITFMATCH-26OCT15PIEMUR-MUR`) | 0.13 / 0.17 (131) | 15.0% | -- | 52.5% | 50.0% [48.0%-52.0%] | -- | -- | -- | -- | PASS | +35.0 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Benjamin Pietri (`KXITFMATCH-26OCT15PIEMUR-PIE`) | 0.83 / 0.85 (1) | 84.0% | -- | 47.5% | 50.0% [48.0%-52.0%] | -- | -- | -- | -- | PASS | -34.0 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 51.0, B 0.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0202
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT15PIEMUR-MUR  (YES = Finn Murgett)
Model: 50%
Kalshi: 15%
Gap: +35 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anastasija Cvetkovic vs Elena Korokozidi -- W35 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-15 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-15T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222481:264167:2026-10-15`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasija Cvetkovic (`KXITFWMATCH-26OCT15CVEKOR-CVE`) | 0.81 / 0.87 (46) | 84.0% | -- | 62.1% | 57.5% [55.3%-60.1%] | -- | -- | -- | -- | PASS | -26.5 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elena Korokozidi (`KXITFWMATCH-26OCT15CVEKOR-KOR`) | 0.14 / 0.19 (14) | 16.5% | -- | 37.9% | 42.5% [39.9%-44.7%] | -- | -- | -- | -- | WATCH | +26.0 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1234.0, B 2005.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0237
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT15CVEKOR-KOR  (YES = Elena Korokozidi)
Model: 43%
Kalshi: 16%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Madison Brengle vs Sloane Stephens -- W100 Edmond OK R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-15 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-15T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:201483:201585:2026-10-15`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Madison Brengle (`KXITFWMATCH-26OCT15BRESTE-BRE`) | 0.34 / 0.36 (127) | 35.0% | -- | 67.1% | 56.9% [41.5%-63.6%] | -- | -- | -- | -- | WATCH | +21.9 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sloane Stephens (`KXITFWMATCH-26OCT15BRESTE-STE`) | 0.63 / 0.66 (50) | 64.5% | -- | 32.9% | 43.1% [36.4%-58.5%] | -- | -- | -- | -- | PASS | -21.4 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2464.0, B 2061.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.1107
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT15BRESTE-BRE  (YES = Madison Brengle)
Model: 57%
Kalshi: 35%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.032, surface_pool_high +0.031, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yeonwoo Ku vs Arantxa Rus -- W100 Edmond OK R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-15 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-15T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT15KUXRUS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yeonwoo Ku (`KXITFWMATCH-26OCT15KUXRUS-KUX`) | 0.58 / 0.61 (178) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arantxa Rus (`KXITFWMATCH-26OCT15KUXRUS-RUS`) | 0.40 / 0.42 (660) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arseneault / Mesarovic vs Kapasi / Sheldon -- M15 Lexington KY QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT15ARSMESKAPSHE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arseneault / Mesarovic (`KXITFDOUBLES-26OCT15ARSMESKAPSHE-ARSMES`) | 0.16 / 0.84 (1) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kapasi / Sheldon (`KXITFDOUBLES-26OCT15ARSMESKAPSHE-KAPSHE`) | 0.11 / 0.79 (1) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Arutiunian / Pieczkowski vs Gogineni / Young -- M15 Lexington KY QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT15ARUPIEGOGYOU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arutiunian / Pieczkowski (`KXITFDOUBLES-26OCT15ARUPIEGOGYOU-ARUPIE`) | 0.11 / 0.79 (1) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gogineni / Young (`KXITFDOUBLES-26OCT15ARUPIEGOGYOU-GOGYOU`) | 0.11 / 0.77 (1) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## McAdoo / Strakhova vs Johnson / Rapolu -- W100 Edmond OK QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT15MCASTRJOHRAP:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Johnson / Rapolu (`KXITFWDOUBLES-26OCT15MCASTRJOHRAP-JOHRAP`) | 0.01 / 0.59 (64) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| McAdoo / Strakhova (`KXITFWDOUBLES-26OCT15MCASTRJOHRAP-MCASTR`) | 0.01 / 0.92 (1) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Brostrom Poulsen / Slavic vs Mercer / Weekes -- M15 Lexington KY QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 02:05Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T02:05:43Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT15BROSLAMERWEE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brostrom Poulsen / Slavic (`KXITFDOUBLES-26OCT15BROSLAMERWEE-BROSLA`) | 0.05 / 0.93 (40) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mercer / Weekes (`KXITFDOUBLES-26OCT15BROSLAMERWEE-MERWEE`) | 0.07 / 0.73 (1) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hanyu Guo / Kristina Mladenovic vs Storm Hunter / Katerina Siniakova -- WTA Wuhan QF

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-16 14:00Z
* Current expected start: 2026-10-16 09:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: 2026-10-16 08:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-16T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16GUOMLAHUNSIN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hanyu Guo / Kristina Mladenovic (`KXWTADOUBLES-26OCT16GUOMLAHUNSIN-GUOMLA`) | 0.31 / 0.35 (35) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Storm Hunter / Katerina Siniakova (`KXWTADOUBLES-26OCT16GUOMLAHUNSIN-HUNSIN`) | 0.65 / 0.68 (3) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; STATUS_AMBIGUOUS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Sergey Fomin vs Yusuke Takahashi -- M25 Qian Daohu QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-16T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126208:200672:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sergey Fomin (`KXITFMATCH-26OCT15FOMTAK-FOM`) | 0.41 / 0.44 (90) | 42.5% | 46.6% | 46.4% | 47.4% [42.9%-53.6%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.1 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yusuke Takahashi (`KXITFMATCH-26OCT15FOMTAK-TAK`) | 0.56 / 0.58 (1) | 57.0% | 53.4% | 53.6% | 52.5% [46.4%-57.1%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -3.6 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1667.0, B 1554.0; serve-point win A 61.0%, B 38.3%; Elo A 1412.1, B 1428.7; model uncertainty 0.0533
* Form inputs: days since last match A 32, B 137; matches on record A 322, B 479; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.036, surface_pool_high -0.046, surface_dev_loose -0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Egor Pleshivtsev vs Cruz Hewitt -- M25 Qian Daohu QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-16T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212574:213178:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cruz Hewitt (`KXITFMATCH-26OCT15PLEHEW-HEW`) | 0.43 / 0.45 (2737) | 44.0% | 90.6% | 53.0% | 82.6% [82.1%-82.6%] | 76.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +46.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Egor Pleshivtsev (`KXITFMATCH-26OCT15PLEHEW-PLE`) | 0.55 / 0.57 (2900) | 56.0% | 9.4% | 46.9% | 17.4% [17.4%-17.9%] | 23.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -46.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 999.0; serve-point win A 56.6%, B 33.1%; Elo A 1197.0, B 1466.0; model uncertainty 0.0028
* Form inputs: days since last match A 669, B 11; matches on record A 4, B 30; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT15PLEHEW-HEW  (YES = Cruz Hewitt)
Model: 91%
Kalshi: 44%
Gap: +47 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniil Medvedev vs Tommy Paul -- ATP Shanghai QF

**START STATUS: START_IMMINENT**
* Nominal schedule: 2026-10-16 07:00Z
* Current expected start: 2026-10-16 09:07Z
* Source: COURT_PROGRESSION: preceding match on Stadium Court in progress (set 3 of best-of-5); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: 2026-10-16 08:22Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+127_MIN

ATP (MASTERS_1000) · Hard · scheduled 2026-10-16T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:106421:126205:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniil Medvedev (`KXATPMATCH-26OCT16MEDPAU-MED`) | 0.67 / 0.68 (277682) | 67.5% | 61.4% | 58.5% | 59.0% [57.5%-60.0%] | 66.4% | 66.5% | 66.4% | MODEL_LONE_OUTLIER | PASS | -6.1 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Tommy Paul (`KXATPMATCH-26OCT16MEDPAU-PAU`) | 0.32 / 0.33 (29872) | 32.5% | 38.6% | 41.5% | 41.0% [40.1%-42.5%] | 33.6% | 32.8% | 33.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.1 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5727.0, B 5633.0; serve-point win A 64.2%, B 38.1%; Elo A 2103.4, B 2032.8; model uncertainty 0.0122
* Form inputs: days since last match A 2, B 2; matches on record A 856, B 719; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight +0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT16MEDPAU-MED20` Will Daniil Medvedev win the Daniil Medvedev vs Tommy Paul match by a set score of 2-0?: 0.42/0.43 mid 42.5%, model 33.3% (projection_v2.0 (prediction ledger)) -- gap -9.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT16MEDPAU-23` Over 22.5 games: 0.51/0.52 mid 51.5%, model 59.4% (projection_v2.0 (prediction ledger)) -- gap +7.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT16MEDPAU-MED3` Will Daniil Medvedev win at least 2.5 more games than Tommy Paul?: 0.54/0.55 mid 54.5%, model 46.8% (projection_v2.0 (prediction ledger)) -- gap -7.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT16MEDPAU-28` Over 27.5 games: 0.28/0.35 mid 31.5%, model 39.1% (projection_v2.0 (prediction ledger)) -- gap +7.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT16MEDPAU-MED6` Will Daniil Medvedev win at least 5.5 more games than Tommy Paul?: 0.20/0.22 mid 21.0%, model 13.8% (projection_v2.0 (prediction ledger)) -- gap -7.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT16MEDPAU-2-MED` Will Daniil Medvedev win set 2 in the Daniil Medvedev vs Tommy Paul match: 0.63/0.65 mid 64.0%, model 57.7% (projection_v2.0 (prediction ledger)) -- gap -6.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT16MEDPAU-2-PAU` Will Tommy Paul win set 2 in the Daniil Medvedev vs Tommy Paul match: 0.35/0.37 mid 36.0%, model 42.3% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT16MEDPAU-1-MED` Will Daniil Medvedev win set 1 in the Daniil Medvedev vs Tommy Paul match: 0.63/0.64 mid 63.5%, model 57.7% (projection_v2.0 (prediction ledger)) -- gap -5.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT16MEDPAU-PAU21` Will Tommy Paul win the Daniil Medvedev vs Tommy Paul match by a set score of 2-1?: 0.14/0.16 mid 15.0%, model 20.7% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT16MEDPAU-1-PAU` Will Tommy Paul win set 1 in the Daniil Medvedev vs Tommy Paul match: 0.37/0.38 mid 37.5%, model 42.3% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT16MEDPAU-MED21` Will Daniil Medvedev win the Daniil Medvedev vs Tommy Paul match by a set score of 2-1?: 0.24/0.26 mid 25.0%, model 28.2% (projection_v2.0 (prediction ledger)) -- gap +3.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT16MEDPAU-PAU2` Will Tommy Paul win at least 1.5 more games than Daniil Medvedev?: 0.27/0.30 mid 28.5%, model 31.6% (projection_v2.0 (prediction ledger)) -- gap +3.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT16MEDPAU-18` Over 17.5 games: 0.89/0.92 mid 90.5%, model 92.5% (projection_v2.0 (prediction ledger)) -- gap +2.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT16MEDPAU-PAU20` Will Tommy Paul win the Daniil Medvedev vs Tommy Paul match by a set score of 2-0?: 0.15/0.17 mid 16.0%, model 17.9% (projection_v2.0 (prediction ledger)) -- gap +1.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; WIDE_SPREAD

## Ann Li vs Iga Swiatek -- WTA Wuhan QF

**START STATUS: START_IMMINENT**
* Nominal schedule: 2026-10-16 14:00Z
* Current expected start: 2026-10-16 09:07Z
* Source: COURT_PROGRESSION: preceding match on Dongfeng Voyah Center Court in progress (set 2 of best-of-3); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: 2026-10-16 08:22Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-293_MIN

WTA (MASTERS_1000) · Hard · scheduled 2026-10-16T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215983:216347:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ann Li (`KXWTAMATCH-26OCT16ANNSWI-ANN`) | 0.21 / 0.22 (163642) | 21.5% | -- | 11.0% | 12.3% [11.0%-15.0%] | 21.4% | 20.4% | 20.9% | MODEL_LONE_OUTLIER | PASS | -9.2 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Iga Swiatek (`KXWTAMATCH-26OCT16ANNSWI-SWI`) | 0.78 / 0.79 (13790) | 78.5% | -- | 89.0% | 87.7% [85.0%-89.0%] | 78.6% | 80.7% | 79.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +9.2 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4567.0, B 4863.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0199
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.008, surface_dev_loose +0.005, surface_dev_tight -0.003
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT16ANNSWI-15` Over 14.5 games: 0.72/0.99 mid 85.5%, model 98.2% (projection_v2.0 (prediction ledger)) -- gap +12.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT16ANNSWI-20` Over 19.5 games: 0.54/0.56 mid 55.0%, model 65.2% (projection_v2.0 (prediction ledger)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT16ANNSWI-25` Over 24.5 games: 0.27/0.33 mid 30.0%, model 39.6% (projection_v2.0 (prediction ledger)) -- gap +9.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Evan King / Ryan Seggerman vs Jay Friend / Ray Ho -- ATP Challenger Jinan SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 09:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-16T09:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16KINSEGHARRAY:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jay Friend / Ray Ho (`KXATPCHALLENGERDOUBLES-26OCT16KINSEGHARRAY-HARRAY`) | 0.63 / 0.66 (129) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Evan King / Ryan Seggerman (`KXATPCHALLENGERDOUBLES-26OCT16KINSEGHARRAY-KINSEG`) | 0.35 / 0.39 (690) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Thijmen Loof / Kaito Uesugi vs Jean-Julien Rojer / Theodore Winegar -- ATP Challenger Jinan SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 09:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-16T09:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16LOOUESROJWIN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thijmen Loof / Kaito Uesugi (`KXATPCHALLENGERDOUBLES-26OCT16LOOUESROJWIN-LOOUES`) | 0.08 / 0.43 (52) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jean-Julien Rojer / Theodore Winegar (`KXATPCHALLENGERDOUBLES-26OCT16LOOUESROJWIN-ROJWIN`) | 0.46 / 0.60 (3) | 53.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dalma Galfi vs Francesca Jones -- WTA 125K Lisbon QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-16 13:00Z
* Current expected start: 2026-10-16 10:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: 2026-10-16 09:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Clay · scheduled 2026-10-16T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:213646:215936:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dalma Galfi (`KXWTACHALLENGERMATCH-26OCT16GALJON-GAL`) | 0.41 / 0.42 (13160) | 41.5% | 38.7% | 55.3% | 48.9% [45.2%-51.6%] | 41.6% | 41.2% | 41.4% | MODEL_LONE_OUTLIER | SHADOW_BET | -2.8 pp | NORMAL | FRESH | A / LIMITED | ALL_AGREE | VERIFIED |
| Francesca Jones (`KXWTACHALLENGERMATCH-26OCT16GALJON-JON`) | 0.58 / 0.59 (5989) | 58.5% | 61.3% | 44.7% | 51.1% [48.4%-54.8%] | 58.4% | 58.9% | 58.6% | MODEL_LONE_OUTLIER | PASS | +2.8 pp | NORMAL | FRESH | A / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4440.0, B 3546.0; serve-point win A 55.4%, B 42.5%; Elo A 1770.9, B 1884.7; model uncertainty 0.0317
* Form inputs: days since last match A 3, B 3; matches on record A 627, B 409; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.016, surface_dev_loose +0.011, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Leyre Romero Gormaz vs Fiona Ferro -- WTA 125K Lisbon QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-16 13:00Z
* Current expected start: 2026-10-16 10:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: 2026-10-16 09:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Clay · scheduled 2026-10-16T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:211539:220742:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fiona Ferro (`KXWTACHALLENGERMATCH-26OCT16ROMFER-FER`) | 0.67 / 0.68 (23971) | 67.5% | 58.8% | 50.0% | 53.2% [51.6%-56.4%] | 66.4% | 67.6% | 67.6% | MODEL_LONE_OUTLIER | PASS | -8.7 pp | NORMAL | FRESH | A / LIMITED | EXTERNAL_STALE | VERIFIED |
| Leyre Romero Gormaz (`KXWTACHALLENGERMATCH-26OCT16ROMFER-ROM`) | 0.33 / 0.34 (21460) | 33.5% | 41.2% | 50.0% | 46.8% [43.6%-48.4%] | 33.6% | 32.0% | 32.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +7.7 pp | NORMAL | FRESH | A / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4018.0, B 2631.0; serve-point win A 52.2%, B 46.2%; Elo A 1725.4, B 1781.2; model uncertainty 0.0239
* Form inputs: days since last match A 4, B 2; matches on record A 422, B 571; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.011, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Gabriela Knutson vs Martyna Kubka -- WTA 125K Rovereto QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-16 13:30Z
* Current expected start: 2026-10-16 10:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: 2026-10-16 09:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-16T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT16KNUKUB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriela Knutson (`KXWTACHALLENGERMATCH-26OCT16KNUKUB-KNU`) | 0.52 / 0.53 (9835) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Martyna Kubka (`KXWTACHALLENGERMATCH-26OCT16KNUKUB-KUB`) | 0.47 / 0.48 (31395) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Francesca Curmi vs Elizara Yaneva -- WTA 125K Mallorca QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-16 13:05Z
* Current expected start: 2026-10-16 11:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: 2026-10-16 10:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Grass · scheduled 2026-10-16T13:05:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221014:260664:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesca Curmi (`KXWTACHALLENGERMATCH-26OCT16CURYAN-CUR`) | 0.46 / 0.47 (47) | 46.5% | 36.4% | 33.5% | 37.4% [34.9%-42.1%] | 48.0% | 45.5% | 48.0% | MODEL_LONE_OUTLIER | PASS | -10.1 pp | REVIEW | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Elizara Yaneva (`KXWTACHALLENGERMATCH-26OCT16CURYAN-YAN`) | 0.52 / 0.53 (174) | 52.5% | 63.6% | 66.5% | 62.6% [57.9%-65.1%] | 52.0% | 54.6% | 52.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +11.1 pp | REVIEW | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2628.0, B 2860.0; serve-point win A 52.7%, B 44.7%; Elo A 1742.9, B 1788.3; model uncertainty 0.0358
* Form inputs: days since last match A 2, B 2; matches on record A 322, B 109; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Jessica Bouzas Maneiro vs Polona Hercog -- WTA 125K Lisbon QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-16 14:10Z
* Current expected start: 2026-10-16 11:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: 2026-10-16 10:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Clay · scheduled 2026-10-16T14:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:201555:222601:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jessica Bouzas Maneiro (`KXWTACHALLENGERMATCH-26OCT16BOUHER-BOU`) | 0.77 / 0.78 (21711) | 77.5% | 63.1% | 26.1% | 36.9% [29.2%-57.4%] | 75.0% | 76.4% | 75.7% | MODEL_LONE_OUTLIER | PASS | -14.3 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Polona Hercog (`KXWTACHALLENGERMATCH-26OCT16BOUHER-HER`) | 0.22 / 0.24 (1166) | 23.0% | 36.9% | 73.9% | 63.1% [42.6%-70.8%] | 25.0% | 23.4% | 24.2% | MODEL_LONE_OUTLIER | WATCH | +13.8 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3457.0, B 2590.0; serve-point win A 55.9%, B 46.7%; Elo A 1828.9, B 1776.6; model uncertainty 0.1409
* Form inputs: days since last match A 2, B 2; matches on record A 440, B 867; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.041, surface_pool_high -0.035, surface_dev_loose -0.015, surface_dev_tight +0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Clara Burel vs Guiomar Maristany Zuleta de Reales -- WTA 125K Lisbon QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-16 14:10Z
* Current expected start: 2026-10-16 11:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: 2026-10-16 10:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Clay · scheduled 2026-10-16T14:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:215571:216262:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Clara Burel (`KXWTACHALLENGERMATCH-26OCT16BURMAR-BUR`) | 0.69 / 0.70 (1158) | 69.5% | 47.3% | 36.8% | 43.6% [40.4%-52.1%] | -- | 70.0% | 70.0% | MODEL_LONE_OUTLIER | PASS | -22.2 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Guiomar Maristany Zuleta de Reales (`KXWTACHALLENGERMATCH-26OCT16BURMAR-MAR`) | 0.29 / 0.31 (1180) | 30.0% | 52.7% | 63.2% | 56.4% [47.9%-59.6%] | -- | 30.6% | 30.6% | MODEL_LONE_OUTLIER | WATCH | +22.7 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1472.0, B 3618.0; serve-point win A 51.1%, B 48.4%; Elo A 1778.9, B 1769.1; model uncertainty 0.0585
* Form inputs: days since last match A 4, B 2; matches on record A 304, B 477; data quality A

```
DISCREPANCY SANITY CHECK  KXWTACHALLENGERMATCH-26OCT16BURMAR-MAR  (YES = Guiomar Maristany Zuleta de Reales)
Model: 53%
Kalshi: 30%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.011, surface_dev_loose -0.005, surface_dev_tight +0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Dominika Salkova vs Lea Boskovic -- WTA 125K Rovereto QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-16 14:40Z
* Current expected start: 2026-10-16 12:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: 2026-10-16 11:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Hard · scheduled 2026-10-16T14:40:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:214521:222966:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lea Boskovic (`KXWTACHALLENGERMATCH-26OCT16SALBOS-BOS`) | 0.39 / 0.40 (1541) | 39.5% | 34.9% | 30.7% | 33.5% [32.6%-36.0%] | 40.1% | 39.4% | 39.7% | MODEL_LONE_OUTLIER | PASS | -4.6 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Dominika Salkova (`KXWTACHALLENGERMATCH-26OCT16SALBOS-SAL`) | 0.60 / 0.62 (17962) | 61.0% | 65.1% | 69.3% | 66.5% [64.0%-67.4%] | 59.9% | 60.5% | 60.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +4.1 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3665.0, B 2773.0; serve-point win A 57.0%, B 46.0%; Elo A 1720.7, B 1642.4; model uncertainty 0.0169
* Form inputs: days since last match A 3, B 3; matches on record A 295, B 438; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Tom Gentzsch vs Damir Dzumhur -- ATP Challenger Olbia QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-16T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106000:210167:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Damir Dzumhur (`KXATPCHALLENGERMATCH-26OCT16GENDZU-DZU`) | 0.50 / 0.51 (6480) | 50.5% | 50.0% | 41.8% | 50.5% [46.4%-55.7%] | 51.0% | 50.8% | 50.8% | MODEL_LONE_OUTLIER | PASS | -0.5 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Tom Gentzsch (`KXATPCHALLENGERMATCH-26OCT16GENDZU-GEN`) | 0.49 / 0.50 (11618) | 49.5% | 50.0% | 58.2% | 49.5% [44.3%-53.6%] | 49.0% | 49.3% | 49.3% | MODEL_LONE_OUTLIER | PASS | +0.5 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3256.0, B 4752.0; serve-point win A 59.3%, B 40.7%; Elo A 1613.7, B 1744.2; model uncertainty 0.0465
* Form inputs: days since last match A 25, B 11; matches on record A 260, B 1058; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.016, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Sara Errani / Jasmine Paolini vs Anna Danilina / Shuai Zhang -- WTA Wuhan QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-16 14:00Z
* Current expected start: 2026-10-16 12:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: 2026-10-16 11:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-16T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16ERRPAODANZHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Danilina / Shuai Zhang (`KXWTADOUBLES-26OCT16ERRPAODANZHA-DANZHA`) | 0.35 / 0.37 (578) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sara Errani / Jasmine Paolini (`KXWTADOUBLES-26OCT16ERRPAODANZHA-ERRPAO`) | 0.61 / 0.64 (361) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Andrea Lazaro Garcia vs Laura Samson -- WTA 125K Mallorca QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-16 15:30Z
* Current expected start: 2026-10-16 12:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: 2026-10-16 11:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Grass · scheduled 2026-10-16T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:210622:266671:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrea Lazaro Garcia (`KXWTACHALLENGERMATCH-26OCT16LAZSAM-LAZ`) | 0.40 / 0.42 (10807) | 41.0% | 50.4% | 43.1% | 47.3% [45.2%-53.2%] | 40.8% | 41.2% | 41.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +9.4 pp | NORMAL | FRESH | A / LIMITED | EXTERNAL_STALE | VERIFIED |
| Laura Samson (`KXWTACHALLENGERMATCH-26OCT16LAZSAM-SAM`) | 0.58 / 0.59 (757) | 58.5% | 49.6% | 56.9% | 52.7% [46.8%-54.8%] | 59.2% | 58.7% | 58.7% | MODEL_LONE_OUTLIER | PASS | -8.9 pp | NORMAL | FRESH | A / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3043.0, B 2910.0; serve-point win A 53.2%, B 46.9%; Elo A 1816.8, B 1780.7; model uncertainty 0.04
* Form inputs: days since last match A 4, B 25; matches on record A 509, B 132; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose -0.016, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Ariel Behar / Joshua Paris vs Romain Arneodo / Hendrik Jebens -- ATP Challenger Roanne SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-16T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16BEHPARARNJEB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Romain Arneodo / Hendrik Jebens (`KXATPCHALLENGERDOUBLES-26OCT16BEHPARARNJEB-ARNJEB`) | 0.55 / 0.58 (34) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ariel Behar / Joshua Paris (`KXATPCHALLENGERDOUBLES-26OCT16BEHPARARNJEB-BEHPAR`) | 0.38 / 0.44 (264) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Amr Elsayed vs Anton Arzhankin -- M15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16ELSARZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anton Arzhankin (`KXITFMATCH-26OCT16ELSARZ-ARZ`) | 0.26 / 0.27 (2801) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Amr Elsayed (`KXITFMATCH-26OCT16ELSARZ-ELS`) | 0.73 / 0.74 (2774) | 73.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lorenzo Giustino vs Zsombor Piros -- ATP Challenger Maia QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-16T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105841:200436:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Giustino (`KXATPCHALLENGERMATCH-26OCT16GIUPIR-GIU`) | 0.22 / 0.23 (20787) | 22.5% | 19.6% | 21.7% | 22.9% [21.7%-24.1%] | 23.1% | 21.6% | 21.6% | MODEL_LONE_OUTLIER | PASS | -2.9 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Zsombor Piros (`KXATPCHALLENGERMATCH-26OCT16GIUPIR-PIR`) | 0.78 / 0.79 (2627) | 78.5% | 80.4% | 78.3% | 77.1% [75.9%-78.3%] | 76.9% | 78.5% | 78.5% | MODEL_LONE_OUTLIER | PASS | +1.9 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4191.0, B 4115.0; serve-point win A 57.7%, B 35.6%; Elo A 1593.7, B 1778.6; model uncertainty 0.0118
* Form inputs: days since last match A 11, B 11; matches on record A 1034, B 526; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.004, surface_dev_loose -0.007, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Saveliy Ivanov vs Romain Faucon -- M15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-16T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209940:211676:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Romain Faucon (`KXITFMATCH-26OCT16IVAFAU-FAU`) | 0.91 / 0.94 (5) | 92.5% | 47.0% | 46.5% | 48.0% [47.0%-49.0%] | -- | -- | -- | -- | PASS | -45.5 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Saveliy Ivanov (`KXITFMATCH-26OCT16IVAFAU-IVA`) | 0.05 / 0.09 (369) | 7.0% | 53.0% | 53.5% | 52.0% [51.0%-53.0%] | -- | -- | -- | -- | PASS | +46.0 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 204.0, B 0.0; serve-point win A 63.8%, B 36.8%; Elo A 1207.6, B 1193.3; model uncertainty 0.01
* Form inputs: days since last match A 718, B 725; matches on record A 65, B 75; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT16IVAFAU-IVA  (YES = Saveliy Ivanov)
Model: 53%
Kalshi: 7%
Gap: +46 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jarno Jans / Joran Vliegen vs Nathaniel Lammons / Jackson Withrow -- ATP Challenger Olbia SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-16T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16JANVLILAMWIT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jarno Jans / Joran Vliegen (`KXATPCHALLENGERDOUBLES-26OCT16JANVLILAMWIT-JANVLI`) | 0.18 / 0.53 (43) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nathaniel Lammons / Jackson Withrow (`KXATPCHALLENGERDOUBLES-26OCT16JANVLILAMWIT-LAMWIT`) | 0.33 / 0.62 (53) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Alejo Sanchez Quilez vs Luka Mikrut -- ATP Challenger Maia QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-16T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210053:211639:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luka Mikrut (`KXATPCHALLENGERMATCH-26OCT16SANMIK-MIK`) | 0.78 / 0.79 (648) | 78.5% | 84.9% | 91.0% | 87.5% [83.4%-90.6%] | 78.0% | 80.0% | 80.0% | MARKETS_AGREE | SHADOW_BET | +6.4 pp | NORMAL | FRESH | B / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Alejo Sanchez Quilez (`KXATPCHALLENGERMATCH-26OCT16SANMIK-SAN`) | 0.20 / 0.21 (15951) | 20.5% | 15.1% | 9.0% | 12.5% [9.4%-16.6%] | 22.0% | 20.3% | 20.3% | MARKETS_AGREE | PASS | -5.4 pp | NORMAL | FRESH | B / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 1220.0, B 2504.0; serve-point win A 57.2%, B 34.7%; Elo A 1435.5, B 1721.7; model uncertainty 0.0361
* Form inputs: days since last match A 11, B 11; matches on record A 113, B 188; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.013, surface_dev_loose -0.013, surface_dev_tight +0.017
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Gala Ivanovic vs Carolina Alves -- W50 Stara Zagora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206430:270115:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carolina Alves (`KXITFWMATCH-26OCT16IVAALV-ALV`) | 0.93 / 0.94 (4927) | 93.5% | -- | 70.9% | 73.1% [72.2%-74.0%] | 80.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -20.4 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gala Ivanovic (`KXITFWMATCH-26OCT16IVAALV-IVA`) | 0.06 / 0.07 (7778) | 6.5% | -- | 29.1% | 26.9% [26.0%-27.8%] | 19.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +20.4 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 844.0, B 3024.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0088
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT16IVAALV-IVA  (YES = Gala Ivanovic)
Model: 27%
Kalshi: 6%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Iva Ivanova vs Federica Urgesi -- W50 Stara Zagora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223415:252509:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iva Ivanova (`KXITFWMATCH-26OCT16IVAURG-IVA`) | 0.60 / 0.61 (3124) | 60.5% | -- | 47.9% | 42.0% [36.9%-44.6%] | 28.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -18.5 pp | HIGH_REVIEW | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Federica Urgesi (`KXITFWMATCH-26OCT16IVAURG-URG`) | 0.39 / 0.40 (3763) | 39.5% | -- | 52.1% | 58.0% [55.4%-63.1%] | 71.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +18.5 pp | HIGH_REVIEW | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2920.0, B 2635.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.039
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT16IVAURG-URG  (YES = Federica Urgesi)
Model: 58%
Kalshi: 40%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Iva Marinkovic vs Ustiniya Lekomtseva -- W15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-16T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:261098:267845:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ustiniya Lekomtseva (`KXITFWMATCH-26OCT16MARLEK-LEK`) | 0.96 / 0.98 (121) | 97.0% | -- | 39.4% | 50.5% [46.8%-53.2%] | -- | -- | -- | -- | PASS | -46.5 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Iva Marinkovic (`KXITFWMATCH-26OCT16MARLEK-MAR`) | 0.01 / 0.04 (3158) | 2.5% | -- | 60.6% | 49.5% [46.8%-53.2%] | -- | -- | -- | -- | PASS | +47.0 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 542.0, B 1512.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0321
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT16MARLEK-MAR  (YES = Iva Marinkovic)
Model: 49%
Kalshi: 2%
Gap: +47 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.011, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ipek Oz vs Anja Stankovic -- W50 Stara Zagora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213998:244087:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ipek Oz (`KXITFWMATCH-26OCT16OZXSTA-OZX`) | 0.89 / 0.90 (3820) | 89.5% | -- | 44.7% | 54.7% [50.0%-64.0%] | 79.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -34.8 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anja Stankovic (`KXITFWMATCH-26OCT16OZXSTA-STA`) | 0.11 / 0.12 (20638) | 11.5% | -- | 55.3% | 45.3% [36.0%-50.0%] | 20.6% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +33.8 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2398.0, B 2297.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0701
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT16OZXSTA-STA  (YES = Anja Stankovic)
Model: 45%
Kalshi: 12%
Gap: +34 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Federica Sacco vs Lamis Alhussein Abdel Aziz -- W15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-16T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213974:221864:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lamis Alhussein Abdel Aziz (`KXITFWMATCH-26OCT16SACALH-ALH`) | 0.65 / 0.71 (56) | 68.0% | -- | 80.2% | 76.7% [73.9%-78.3%] | -- | -- | -- | -- | WATCH | +8.7 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Federica Sacco (`KXITFWMATCH-26OCT16SACALH-SAC`) | 0.28 / 0.35 (6) | 31.5% | -- | 19.8% | 23.3% [21.7%-26.2%] | -- | -- | -- | -- | PASS | -8.2 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1826.0, B 4747.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0223
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Beatris Spasova vs Luisina Giovannini -- W50 Stara Zagora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221315:236972:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luisina Giovannini (`KXITFWMATCH-26OCT16SPAGIO-GIO`) | 0.99 / -- (0) | -- | -- | 99.0% | 97.2% [96.0%-98.5%] | 94.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -- | UNPRICED | FRESH | C / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |
| Beatris Spasova (`KXITFWMATCH-26OCT16SPAGIO-SPA`) | -- / 0.01 (99820) | -- | -- | 1.1% | 2.8% [1.5%-4.0%] | 5.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | FRESH | C / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 520.0, B 3057.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0125
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dune Vaissaud vs Karla Popovic -- W15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-16T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:210500:266642:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karla Popovic (`KXITFWMATCH-26OCT16VAIPOP-POP`) | 0.15 / 0.20 (13) | 17.5% | -- | 64.7% | 59.0% [52.7%-63.2%] | -- | -- | -- | -- | WATCH | +41.5 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dune Vaissaud (`KXITFWMATCH-26OCT16VAIPOP-VAI`) | 0.78 / 0.84 (52) | 81.0% | -- | 35.3% | 41.0% [36.8%-47.3%] | -- | -- | -- | -- | PASS | -40.0 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2429.0, B 1204.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0524
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT16VAIPOP-POP  (YES = Karla Popovic)
Model: 59%
Kalshi: 18%
Gap: +42 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.005, surface_dev_loose -0.005, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maks Kasnikowski vs Stefano Travaglia -- ATP Challenger Olbia QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 13:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-16T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105882:209874:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maks Kasnikowski (`KXATPCHALLENGERMATCH-26OCT16KASTRA-KAS`) | 0.58 / 0.59 (3984) | 58.5% | 47.0% | 43.3% | 41.8% [37.4%-43.9%] | 58.4% | 59.4% | 59.4% | MODEL_LONE_OUTLIER | PASS | -11.5 pp | REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Stefano Travaglia (`KXATPCHALLENGERMATCH-26OCT16KASTRA-TRA`) | 0.41 / 0.42 (2617) | 41.5% | 53.0% | 56.7% | 58.2% [56.1%-62.6%] | 41.6% | 41.5% | 41.5% | MODEL_LONE_OUTLIER | SHADOW_BET | +11.5 pp | REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3242.0, B 3948.0; serve-point win A 60.1%, B 39.4%; Elo A 1592.6, B 1678.9; model uncertainty 0.0324
* Form inputs: days since last match A 11, B 25; matches on record A 273, B 967; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.020, surface_dev_loose +0.005, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Geoffrey Blancaneaux vs Kristijan Juhas -- M15 Bol QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 13:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-16T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144972:209099:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Geoffrey Blancaneaux (`KXITFMATCH-26OCT16BLAJUH-BLA`) | 0.09 / 0.12 (4717) | 10.5% | 83.2% | 44.9% | 78.6% [76.3%-80.7%] | 59.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +72.7 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Kristijan Juhas (`KXITFMATCH-26OCT16BLAJUH-JUH`) | 0.88 / 0.91 (2624) | 89.5% | 16.8% | 55.1% | 21.4% [19.3%-23.7%] | 40.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -72.7 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 3141.0, B 0.0; serve-point win A 65.3%, B 42.3%; Elo A 1522.4, B 1298.8; model uncertainty 0.0223
* Form inputs: days since last match A 18, B 851; matches on record A 630, B 56; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT16BLAJUH-BLA  (YES = Geoffrey Blancaneaux)
Model: 83%
Kalshi: 10%
Gap: +73 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.022, surface_pool_high -0.023, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nikita Mashtakov vs Noah Lopez -- M15 Bol QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 13:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-16T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210055:tml:MW62:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Noah Lopez (`KXITFMATCH-26OCT16MASLOP-LOP`) | 0.01 / 0.02 (268) | 1.5% | 25.2% | 29.3% | 19.0% [17.8%-20.1%] | 25.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +23.7 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Nikita Mashtakov (`KXITFMATCH-26OCT16MASLOP-MAS`) | 0.98 / 0.99 (3221) | 98.5% | 74.8% | 70.7% | 81.0% [80.0%-82.2%] | 74.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -23.7 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 306.0, B 172.0; serve-point win A 62.5%, B 42.7%; Elo A 1408.9, B 1146.1; model uncertainty 0.0112
* Form inputs: days since last match A 25, B 732; matches on record A 5, B 98; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT16MASLOP-LOP  (YES = Noah Lopez)
Model: 25%
Kalshi: 2%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Suresh / Sureshkumar vs Ganesan / Lomakin -- M25 Solapur SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 13:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16SURSURGANLOM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ganesan / Lomakin (`KXITFDOUBLES-26OCT16SURSURGANLOM-GANLOM`) | 0.19 / 0.69 (1) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Suresh / Sureshkumar (`KXITFDOUBLES-26OCT16SURSURGANLOM-SURSUR`) | 0.11 / 0.80 (10) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Didi Bredberg Canizares vs Alesia Breaz -- W15 Bol QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 13:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-16T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223375:270165:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Didi Bredberg Canizares (`KXITFWMATCH-26OCT16BREBRE2-BRE`) | 0.53 / 0.54 (1) | 53.5% | -- | 73.6% | 59.0% [52.1%-64.1%] | 30.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +5.5 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alesia Breaz (`KXITFWMATCH-26OCT16BREBRE2-BRE2`) | 0.44 / 0.47 (2533) | 45.5% | -- | 26.4% | 41.0% [35.9%-47.9%] | 69.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.5 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1191.0, B 933.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.06
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.016, surface_dev_loose +0.015, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Buvaysar Gadamauri vs Felix Gill -- ATP Challenger Catania QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-16T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207527:208269:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Buvaysar Gadamauri (`KXATPCHALLENGERMATCH-26OCT16GADGIL-GAD`) | 0.35 / 0.36 (1) | 35.5% | 48.3% | 50.5% | 47.0% [45.0%-48.5%] | 36.9% | 36.3% | 36.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +12.8 pp | REVIEW | FRESH | A / LIMITED | EXTERNAL_STALE | VERIFIED |
| Felix Gill (`KXATPCHALLENGERMATCH-26OCT16GADGIL-GIL`) | 0.63 / 0.64 (4532) | 63.5% | 51.7% | 49.5% | 53.0% [51.5%-55.0%] | 63.1% | 63.5% | 63.5% | MODEL_LONE_OUTLIER | PASS | -11.8 pp | REVIEW | FRESH | A / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 2063.0, B 2694.0; serve-point win A 62.7%, B 37.0%; Elo A 1585.6, B 1649.8; model uncertainty 0.0176
* Form inputs: days since last match A 11, B 25; matches on record A 234, B 281; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE

## Jonas GUNDACKER vs Pietro Orlando Fellin -- M15 Szabolcsveresmart QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-16T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209165:212981:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pietro Orlando Fellin (`KXITFMATCH-26OCT16GUNFEL-FEL`) | 0.87 / 0.88 (2541) | 87.5% | 79.5% | 50.0% | 65.8% [64.9%-66.7%] | 65.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Jonas GUNDACKER (`KXITFMATCH-26OCT16GUNFEL-GUN`) | 0.12 / 0.13 (1966) | 12.5% | 20.5% | 50.0% | 34.2% [33.3%-35.1%] | 34.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +8.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 58.8%, B 34.8%; Elo A 1153.4, B 1264.7; model uncertainty 0.0093
* Form inputs: days since last match A 760, B 690; matches on record A 7, B 45; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Radu Mihai Papoe vs Zdenek Kolar -- ATP Challenger Catania QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-16T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144645:208457:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zdenek Kolar (`KXATPCHALLENGERMATCH-26OCT16PAPKOL-KOL`) | 0.43 / 0.44 (267) | 43.5% | 47.7% | 59.4% | 47.4% [43.8%-50.5%] | 43.7% | 43.5% | 43.5% | MODEL_LONE_OUTLIER | WATCH | +4.2 pp | NORMAL | FRESH | B / LIMITED | EXTERNAL_STALE | VERIFIED |
| Radu Mihai Papoe (`KXATPCHALLENGERMATCH-26OCT16PAPKOL-PAP`) | 0.56 / 0.57 (3235) | 56.5% | 52.3% | 40.6% | 52.6% [49.5%-56.2%] | 56.3% | 56.5% | 56.5% | MODEL_LONE_OUTLIER | PASS | -4.2 pp | NORMAL | FRESH | B / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 833.0, B 3944.0; serve-point win A 56.8%, B 43.6%; Elo A 1652.1, B 1582.1; model uncertainty 0.0339
* Form inputs: days since last match A 28, B 11; matches on record A 124, B 769; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Plans / Verbeek vs Faleh Alhogbani / Mabrouk -- M15 Sharm ElSheikh SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16PLAVERFALMAB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Faleh Alhogbani / Mabrouk (`KXITFDOUBLES-26OCT16PLAVERFALMAB-FALMAB`) | 0.28 / 0.35 (21) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Plans / Verbeek (`KXITFDOUBLES-26OCT16PLAVERFALMAB-PLAVER`) | 0.65 / 0.71 (487) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Stefan Seifert vs Wojciech Marek -- M15 Szabolcsveresmart QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-16T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:104510:207457:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wojciech Marek (`KXITFMATCH-26OCT16SEIMAR-MAR`) | 0.20 / 0.22 (333) | 21.0% | 33.3% | 34.1% | 28.6% [24.6%-32.7%] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +12.3 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Stefan Seifert (`KXITFMATCH-26OCT16SEIMAR-SEI`) | 0.78 / 0.80 (313) | 79.0% | 66.7% | 65.9% | 71.4% [67.3%-75.4%] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.3 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 188.0, B 160.0; serve-point win A 62.6%, B 40.7%; Elo A 1485.5, B 1325.9; model uncertainty 0.0402
* Form inputs: days since last match A 2433, B 1537; matches on record A 371, B 84; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.030, surface_pool_high -0.040, surface_dev_loose +0.001, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Giorgio Tabacco vs Branko Djuric -- M25 Santa Margherita di Pula SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-16T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209937:210025:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Branko Djuric (`KXITFMATCH-26OCT16TABDJU-DJU`) | 0.22 / 0.23 (3334) | 22.5% | 61.8% | 67.2% | 59.1% [57.1%-62.0%] | 56.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +39.3 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Giorgio Tabacco (`KXITFMATCH-26OCT16TABDJU-TAB`) | 0.77 / 0.78 (3374) | 77.5% | 38.2% | 32.8% | 40.9% [38.0%-42.9%] | 43.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -39.3 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 144.0, B 387.0; serve-point win A 60.6%, B 37.0%; Elo A 1360.5, B 1416.1; model uncertainty 0.0247
* Form inputs: days since last match A 46, B 399; matches on record A 124, B 69; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT16TABDJU-DJU  (YES = Branko Djuric)
Model: 62%
Kalshi: 22%
Gap: +39 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexander Weis vs Matthew William Donald -- M25 Santa Margherita di Pula SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-16T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200255:210054:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthew William Donald (`KXITFMATCH-26OCT16WEIDON-DON`) | 0.58 / 0.63 (1) | 60.5% | 35.8% | 56.2% | 36.2% [33.3%-40.7%] | 61.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -24.7 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexander Weis (`KXITFMATCH-26OCT16WEIDON-WEI`) | 0.38 / 0.42 (92) | 40.0% | 64.2% | 43.8% | 63.8% [59.3%-66.7%] | 38.5% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +24.2 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 883.0, B 667.0; serve-point win A 59.7%, B 43.1%; Elo A 1501.0, B 1341.7; model uncertainty 0.0369
* Form inputs: days since last match A 67, B 18; matches on record A 467, B 128; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT16WEIDON-WEI  (YES = Alexander Weis)
Model: 64%
Kalshi: 40%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.030, surface_pool_high +0.019, surface_dev_loose -0.004, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sara Victoria Balan vs Sophie Luescher -- W15 Chisinau QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-16T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221153:267431:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Victoria Balan (`KXITFWMATCH-26OCT16BALLUE-BAL`) | 0.45 / 0.49 (5) | 47.0% | -- | 69.0% | 60.6% [58.5%-64.6%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.6 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sophie Luescher (`KXITFWMATCH-26OCT16BALLUE-LUE`) | 0.50 / 0.54 (1) | 52.0% | -- | 31.0% | 39.4% [35.4%-41.5%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.6 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1045.0, B 175.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0309
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rositsa Dencheva vs Valeriia Artemeva -- W50 Stara Zagora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259913:267841:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valeriia Artemeva (`KXITFWMATCH-26OCT16DENART-ART`) | 0.05 / 0.06 (515) | 5.5% | -- | 19.9% | 12.2% [9.7%-14.8%] | 7.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +6.7 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rositsa Dencheva (`KXITFWMATCH-26OCT16DENART-DEN`) | 0.93 / 0.95 (216) | 94.0% | -- | 80.1% | 87.8% [85.2%-90.3%] | 92.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.2 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2446.0, B 1430.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0253
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Angela Fita Boluda vs Ilinca Dalina Amariei -- W50 Stara Zagora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214236:221168:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ilinca Dalina Amariei (`KXITFWMATCH-26OCT16FITAMA-AMA`) | 0.40 / 0.43 (273) | 41.5% | -- | 39.5% | 37.5% [34.9%-38.5%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.0 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Angela Fita Boluda (`KXITFWMATCH-26OCT16FITAMA-FIT`) | 0.57 / 0.60 (5115) | 58.5% | -- | 60.5% | 62.5% [61.5%-65.1%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +4.0 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4603.0, B 2360.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0176
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arina Gamretkaia vs Felitsata Dorofeeva-Rybas -- W15 Chisinau QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-16T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:267022:267440:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felitsata Dorofeeva-Rybas (`KXITFWMATCH-26OCT16GAMDOR-DOR`) | 0.99 / -- (0) | -- | -- | 58.5% | 73.1% [73.1%-73.2%] | 90.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | FRESH | F / POOR | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arina Gamretkaia (`KXITFWMATCH-26OCT16GAMDOR-GAM`) | -- / 0.02 (622) | -- | -- | 41.5% | 26.9% [26.9%-26.9%] | 9.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | FRESH | F / POOR | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 923.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0003
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valentini Grammatikopoulou vs Angelica Raggi -- W35 Santa Margherita di Pula QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-16T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:204394:216051:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valentini Grammatikopoulou (`KXITFWMATCH-26OCT16GRARAG-GRA`) | 0.50 / 0.51 (3763) | 50.5% | -- | 69.1% | 66.6% [61.6%-67.6%] | 67.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +16.1 pp | HIGH_REVIEW | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Angelica Raggi (`KXITFWMATCH-26OCT16GRARAG-RAG`) | 0.49 / 0.50 (1552) | 49.5% | -- | 30.9% | 33.4% [32.4%-38.4%] | 33.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -16.1 pp | HIGH_REVIEW | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2942.0, B 2349.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.03
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT16GRARAG-GRA  (YES = Valentini Grammatikopoulou)
Model: 67%
Kalshi: 50%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.020, surface_dev_loose +0.005, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kristina Kroitor vs Justine Bretnacher -- W15 Chisinau QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-16T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:267401:269755:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Justine Bretnacher (`KXITFWMATCH-26OCT16KROBRE-BRE`) | 0.08 / 0.09 (1684) | 8.5% | -- | 2.1% | 8.0% [6.2%-9.2%] | 9.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kristina Kroitor (`KXITFWMATCH-26OCT16KROBRE-KRO`) | 0.91 / 0.92 (3007) | 91.5% | -- | 97.9% | 92.0% [90.8%-93.8%] | 90.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2484.0, B 222.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0151
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.002, surface_dev_loose +0.004, surface_dev_tight -0.002
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lucie Petruzelova vs Denislava Glushkova -- W50 Stara Zagora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221219:221364:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Denislava Glushkova (`KXITFWMATCH-26OCT16PETGLU-GLU`) | 0.38 / 0.39 (350) | 38.5% | -- | 77.8% | 82.6% [80.8%-84.0%] | 37.8% | -- | 37.8% | MODEL_LONE_OUTLIER | WATCH | +44.1 pp | EXTREME (DATA_WARNING) | FRESH | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Lucie Petruzelova (`KXITFWMATCH-26OCT16PETGLU-PET`) | 0.60 / 0.62 (66) | 61.0% | -- | 22.2% | 17.4% [16.0%-19.1%] | 62.2% | -- | 62.2% | MODEL_LONE_OUTLIER | PASS | -43.6 pp | EXTREME (DATA_WARNING) | FRESH | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1518.0, B 2333.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0156
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT16PETGLU-GLU  (YES = Denislava Glushkova)
Model: 83%
Kalshi: 38%
Gap: +44 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: B (ADEQUATE)
Reasons: EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jessica Pieri vs Matilde Paoletti -- W35 Santa Margherita di Pula QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-16T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213620:222396:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matilde Paoletti (`KXITFWMATCH-26OCT16PIEPAO-PAO`) | 0.81 / 0.83 (1) | 82.0% | -- | 41.0% | 52.7% [48.9%-56.4%] | 56.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -29.3 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jessica Pieri (`KXITFWMATCH-26OCT16PIEPAO-PIE`) | 0.16 / 0.18 (1126) | 17.0% | -- | 59.0% | 47.3% [43.6%-51.1%] | 43.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +30.3 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2683.0, B 466.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0374
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT16PIEPAO-PIE  (YES = Jessica Pieri)
Model: 47%
Kalshi: 17%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.037, surface_pool_high -0.037, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Giulia Safina Popa vs Andreea Prisacariu -- W15 Chisinau QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-16T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214653:267428:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giulia Safina Popa (`KXITFWMATCH-26OCT16POPPRI-POP`) | 0.96 / 0.97 (23) | 96.5% | -- | 51.1% | 54.8% [47.9%-59.6%] | 67.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -41.7 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Andreea Prisacariu (`KXITFWMATCH-26OCT16POPPRI-PRI`) | 0.02 / 0.03 (7800) | 2.5% | -- | 48.9% | 45.2% [40.5%-52.1%] | 32.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +42.7 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1013.0, B 2406.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0585
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT16POPPRI-PRI  (YES = Andreea Prisacariu)
Model: 45%
Kalshi: 2%
Gap: +43 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.059, surface_pool_high +0.047, surface_dev_loose -0.021, surface_dev_tight +0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nina Radovanovic vs Natalija Senic -- W35 Santa Margherita di Pula QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-16T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222602:239476:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nina Radovanovic (`KXITFWMATCH-26OCT16RADSEN-RAD`) | 0.91 / 0.92 (4312) | 91.5% | -- | 18.1% | 18.4% [15.1%-26.9%] | 65.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -73.1 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Natalija Senic (`KXITFWMATCH-26OCT16RADSEN-SEN`) | 0.08 / 0.09 (5790) | 8.5% | -- | 81.9% | 81.6% [73.1%-84.9%] | 34.3% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +73.1 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 976.0, B 2163.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0589
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT16RADSEN-SEN  (YES = Natalija Senic)
Model: 82%
Kalshi: 8%
Gap: +73 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.046, surface_pool_high -0.034, surface_dev_loose +0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Beatrise Zeltina vs Nellie Taraba Wallberg -- W35 Santa Margherita di Pula QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-16T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:254765:260339:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nellie Taraba Wallberg (`KXITFWMATCH-26OCT16ZELTAR-TAR`) | 0.54 / 0.57 (1913) | 55.5% | -- | 32.9% | 40.4% [36.8%-47.9%] | 40.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.1 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Beatrise Zeltina (`KXITFWMATCH-26OCT16ZELTAR-ZEL`) | 0.42 / 0.43 (1) | 42.5% | -- | 67.1% | 59.6% [52.1%-63.2%] | 59.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +17.1 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1940.0, B 1634.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0551
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT16ZELTAR-ZEL  (YES = Beatrise Zeltina)
Model: 60%
Kalshi: 42%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.026, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sonja Zhenikhova vs Alena Kovackova -- W50 Stara Zagora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264961:266800:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alena Kovackova (`KXITFWMATCH-26OCT16ZHEKOV-KOV`) | 0.85 / 0.86 (66) | 85.5% | -- | 79.6% | 80.4% [78.5%-82.2%] | 83.0% | -- | 83.0% | KALSHI_LONE_OUTLIER | PASS | -5.1 pp | NORMAL | FRESH | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Sonja Zhenikhova (`KXITFWMATCH-26OCT16ZHEKOV-ZHE`) | 0.13 / 0.14 (29) | 13.5% | -- | 20.4% | 19.6% [17.8%-21.5%] | 17.0% | -- | 17.0% | KALSHI_LONE_OUTLIER | WATCH | +6.1 pp | NORMAL | FRESH | C / LIMITED | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 1212.0, B 2074.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0185
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Adam Heinonen / Michael Vrbensky vs Tiago Pereira / Benjamin Winter Lopez -- ATP Challenger Maia SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-16T14:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16HEIVRBPERWIN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adam Heinonen / Michael Vrbensky (`KXATPCHALLENGERDOUBLES-26OCT16HEIVRBPERWIN-HEIVRB`) | 0.08 / 0.61 (25) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tiago Pereira / Benjamin Winter Lopez (`KXATPCHALLENGERDOUBLES-26OCT16HEIVRBPERWIN-PERWIN`) | 0.39 / 0.85 (100) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Daniel Masur / Tim Ruehl vs Daniel Cukierman / Fernando Romboli -- ATP Challenger Olbia SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-16T14:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16MASRUECUKROM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Cukierman / Fernando Romboli (`KXATPCHALLENGERDOUBLES-26OCT16MASRUECUKROM-CUKROM`) | 0.53 / 0.68 (77) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daniel Masur / Tim Ruehl (`KXATPCHALLENGERDOUBLES-26OCT16MASRUECUKROM-MASRUE`) | 0.28 / 0.47 (10) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Carles Cordoba vs Iannis Miletich -- M15 Bol QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-16T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211391:213059:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carles Cordoba (`KXITFMATCH-26OCT16CORMIL-COR`) | 0.19 / 0.20 (1) | 19.5% | 23.1% | 60.3% | 30.1% [29.4%-30.2%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Iannis Miletich (`KXITFMATCH-26OCT16CORMIL-MIL`) | 0.79 / 0.80 (2117) | 79.5% | 77.0% | 39.7% | 69.9% [69.8%-70.5%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 110.0; serve-point win A 61.4%, B 32.7%; Elo A 1205.4, B 1351.2; model uncertainty 0.0038
* Form inputs: days since last match A 683, B 683; matches on record A 9, B 37; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.001, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Milos Karol / Andrew Paulson vs Alexandru Jecan / Szymon Kielan -- ATP Challenger Maia SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-16T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16KARPAUJECKIE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandru Jecan / Szymon Kielan (`KXATPCHALLENGERDOUBLES-26OCT16KARPAUJECKIE-JECKIE`) | 0.28 / 0.37 (10) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Milos Karol / Andrew Paulson (`KXATPCHALLENGERDOUBLES-26OCT16KARPAUJECKIE-KARPAU`) | 0.63 / 0.72 (92) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Gorska / Pawelska vs Bizjak / Yemshanova -- W15 Bol SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16GORPAWBIZYEM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bizjak / Yemshanova (`KXITFWDOUBLES-26OCT16GORPAWBIZYEM-BIZYEM`) | 0.53 / 0.55 (135) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gorska / Pawelska (`KXITFWDOUBLES-26OCT16GORPAWBIZYEM-GORPAW`) | 0.45 / 0.46 (1) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Alisa Oktiabreva vs Cristiana Nicoleta Todoni -- W35 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-16T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260765:261104:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alisa Oktiabreva (`KXITFWMATCH-26OCT16OKTTOD-OKT`) | 0.95 / 0.97 (1634) | 96.0% | -- | 92.2% | 93.7% [92.4%-94.6%] | 84.5% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -2.3 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Cristiana Nicoleta Todoni (`KXITFWMATCH-26OCT16OKTTOD-TOD`) | 0.03 / 0.05 (1787) | 4.0% | -- | 7.8% | 6.3% [5.4%-7.6%] | 15.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.3 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1999.0, B 865.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0109
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.003, surface_dev_loose +0.002, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anna Petkovic vs Ani Amiraghyan -- W15 Bol QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-16T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206060:252571:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ani Amiraghyan (`KXITFWMATCH-26OCT16PETAMI-AMI`) | 0.20 / 0.21 (330) | 20.5% | -- | 60.6% | 54.3% [49.5%-58.5%] | 50.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +33.8 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anna Petkovic (`KXITFWMATCH-26OCT16PETAMI-PET`) | 0.78 / 0.80 (174) | 79.0% | -- | 39.4% | 45.7% [41.5%-50.5%] | 50.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -33.3 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1778.0, B 808.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0452
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT16PETAMI-AMI  (YES = Ani Amiraghyan)
Model: 54%
Kalshi: 20%
Gap: +34 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.042, surface_pool_high +0.048, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maria Sara Popa vs Dunja Maric -- W35 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-16T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222859:260017:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dunja Maric (`KXITFWMATCH-26OCT16POPMAR-MAR`) | 0.36 / 0.38 (1) | 37.0% | -- | 42.6% | 46.8% [45.7%-50.5%] | 37.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +9.8 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Sara Popa (`KXITFWMATCH-26OCT16POPMAR-POP`) | 0.59 / 0.65 (152) | 62.0% | -- | 57.4% | 53.2% [49.5%-54.3%] | 62.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.8 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2326.0, B 1430.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.024
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Veronika Sekerkova vs Eliska Tichackova -- W15 Bol QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-16T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:254748:267542:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Veronika Sekerkova (`KXITFWMATCH-26OCT16SEKTIC-SEK`) | 0.05 / 0.06 (3774) | 5.5% | -- | 6.9% | 10.5% [9.1%-12.0%] | 20.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Eliska Tichackova (`KXITFWMATCH-26OCT16SEKTIC-TIC`) | 0.94 / 0.95 (253) | 94.5% | -- | 93.1% | 89.5% [88.0%-90.9%] | 79.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 56.0, B 1647.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0145
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.015, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alice Tubello vs Stella Jurina -- W35 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-16T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220554:223062:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stella Jurina (`KXITFWMATCH-26OCT16TUBJUR-JUR`) | 0.03 / 0.04 (55) | 3.5% | -- | 9.3% | 5.5% [4.6%-6.4%] | 4.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Alice Tubello (`KXITFWMATCH-26OCT16TUBJUR-TUB`) | 0.96 / 0.97 (1) | 96.5% | -- | 90.7% | 94.5% [93.6%-95.4%] | 95.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 2580.0, B 0.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0088
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.009, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Florent Bax vs Allan Gatoto -- M25 Luanda QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202147:212753:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Florent Bax (`KXITFMATCH-26OCT16BAXGAT-BAX`) | 0.95 / 0.96 (4114) | 95.5% | 92.7% | 51.0% | 85.7% [85.7%-85.8%] | 92.8% | -- | 92.8% | MODEL_LONE_OUTLIER | PASS | -2.8 pp | NORMAL | FRESH | F / POOR | ALL_AGREE | AMBIGUOUS |
| Allan Gatoto (`KXITFMATCH-26OCT16BAXGAT-GAT`) | 0.04 / 0.05 (1576) | 4.5% | 7.3% | 49.0% | 14.3% [14.2%-14.3%] | 7.2% | -- | 7.2% | MODEL_LONE_OUTLIER | PASS | +2.8 pp | NORMAL | FRESH | F / POOR | ALL_AGREE | AMBIGUOUS |

* Serve evidence (points): A 2193.0, B 0.0; serve-point win A 70.3%, B 41.5%; Elo A 1538.2, B 1222.5; model uncertainty 0.0006
* Form inputs: days since last match A 32, B 928; matches on record A 261, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Robin Bertrand vs Felix Roussel -- M15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16BERROU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Robin Bertrand (`KXITFMATCH-26OCT16BERROU-BER`) | 0.81 / 0.82 (1947) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Felix Roussel (`KXITFMATCH-26OCT16BERROU-ROU`) | 0.18 / 0.19 (2537) | 18.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jerome Kym vs Dominic Stricker -- ATP Challenger Roanne QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-16T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208502:208843:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jerome Kym (`KXATPCHALLENGERMATCH-26OCT16KYMSTR-KYM`) | 0.55 / 0.56 (9680) | 55.5% | 61.0% | 69.1% | 61.5% [58.2%-64.8%] | -- | 54.5% | 54.5% | MODEL_LONE_OUTLIER | SHADOW_BET | +5.5 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Dominic Stricker (`KXATPCHALLENGERMATCH-26OCT16KYMSTR-STR`) | 0.44 / 0.46 (15630) | 45.0% | 39.0% | 30.9% | 38.5% [35.2%-41.8%] | -- | 45.1% | 45.1% | MODEL_LONE_OUTLIER | PASS | -6.0 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2885.0, B 2363.0; serve-point win A 67.3%, B 35.0%; Elo A 1683.6, B 1688.1; model uncertainty 0.0326
* Form inputs: days since last match A 18, B 11; matches on record A 249, B 250; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.005, surface_dev_loose +0.009, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Mathys Picard vs Leo Borg -- M15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16PICBOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leo Borg (`KXITFMATCH-26OCT16PICBOR-BOR`) | 0.74 / 0.76 (388) | 75.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mathys Picard (`KXITFMATCH-26OCT16PICBOR-PIC`) | 0.24 / 0.26 (614) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Flynn Thomas vs Calvin Mueller -- M15 Offenbach SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209166:213151:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Calvin Mueller (`KXITFMATCH-26OCT16THOMUE-MUE`) | 0.61 / 0.62 (65) | 61.5% | 41.2% | 50.0% | 48.0% [48.0%-48.0%] | 62.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -20.3 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Flynn Thomas (`KXITFMATCH-26OCT16THOMUE-THO`) | 0.37 / 0.38 (1) | 37.5% | 58.8% | 50.0% | 52.0% [52.0%-52.0%] | 37.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +21.3 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 62.9%, B 38.9%; Elo A 1289.2, B 1277.6; model uncertainty 0.0
* Form inputs: days since last match A 697, B 2629; matches on record A 3, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT16THOMUE-THO  (YES = Flynn Thomas)
Model: 59%
Kalshi: 38%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dorian Tremblay vs Emilien Demanet -- M25 Luanda QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209847:212598:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emilien Demanet (`KXITFMATCH-26OCT16TREDEM-DEM`) | 0.91 / 0.93 (3157) | 92.0% | 91.5% | 62.0% | 80.0% [79.9%-80.0%] | 89.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Dorian Tremblay (`KXITFMATCH-26OCT16TREDEM-TRE`) | 0.07 / 0.09 (1417) | 8.0% | 8.5% | 38.0% | 20.0% [20.0%-20.1%] | 10.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 243.0; serve-point win A 56.3%, B 32.9%; Elo A 1185.7, B 1431.2; model uncertainty 0.0005
* Form inputs: days since last match A 760, B 74; matches on record A 8, B 69; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vaishnavi Adkar vs Sofia Camila Rojas -- W35 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-16T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:261038:266630:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vaishnavi Adkar (`KXITFWMATCH-26OCT16ADKROJ-ADK`) | 0.64 / 0.65 (1325) | 64.5% | -- | 39.5% | 47.9% [42.6%-52.1%] | 64.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -16.6 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sofia Camila Rojas (`KXITFWMATCH-26OCT16ADKROJ-ROJ`) | 0.35 / 0.36 (1494) | 35.5% | -- | 60.5% | 52.1% [47.9%-57.4%] | 35.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +16.6 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2186.0, B 553.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0476
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT16ADKROJ-ROJ  (YES = Sofia Camila Rojas)
Model: 52%
Kalshi: 36%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.016, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anna Burrage / Cabrera vs Allen / Judith Visscher -- W35 Birmingham F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16ANNCABALLJUD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Allen / Judith Visscher (`KXITFWDOUBLES-26OCT16ANNCABALLJUD-ALLJUD`) | 0.28 / 0.50 (25) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anna Burrage / Cabrera (`KXITFWDOUBLES-26OCT16ANNCABALLJUD-ANNCAB`) | 0.26 / 0.61 (64) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Anna Kubareva vs Elena Milovanovic -- W35 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-16T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215707:220429:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Kubareva (`KXITFWMATCH-26OCT16KUBMIL-KUB`) | 0.41 / 0.52 (10) | 46.5% | -- | 68.1% | 59.0% [47.9%-63.6%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +12.5 pp | REVIEW | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elena Milovanovic (`KXITFWMATCH-26OCT16KUBMIL-MIL`) | 0.44 / 0.53 (5) | 48.5% | -- | 31.9% | 41.0% [36.4%-52.1%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.5 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2121.0, B 2475.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0789
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.010, surface_dev_loose +0.041, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tiphanie Lemaitre vs Ekaterina Tupitsyna -- W35 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-16T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:270065:espn:espn:13746:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tiphanie Lemaitre (`KXITFWMATCH-26OCT16LEMTUP-LEM`) | 0.47 / 0.48 (355) | 47.5% | -- | 15.9% | 41.5% [40.5%-41.5%] | 47.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ekaterina Tupitsyna (`KXITFWMATCH-26OCT16LEMTUP-TUP`) | 0.51 / 0.53 (476) | 52.0% | -- | 84.1% | 58.5% [58.5%-59.5%] | 52.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 1295.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0053
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kayo Nishimura vs Chenting Zhu -- W35 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-16T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260613:264064:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kayo Nishimura (`KXITFWMATCH-26OCT16NISZHU-NIS`) | 0.38 / 0.46 (412) | 42.0% | -- | 53.2% | 56.4% [54.8%-58.5%] | -- | -- | -- | -- | WATCH | +14.4 pp | REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Chenting Zhu (`KXITFWMATCH-26OCT16NISZHU-ZHU`) | 0.54 / 0.58 (64) | 56.0% | -- | 46.8% | 43.6% [41.5%-45.2%] | -- | -- | -- | -- | PASS | -12.4 pp | REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2288.0, B 2166.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0184
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anita Tu vs Tara Wuerth -- W15 Bol QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16TUXWUE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anita Tu (`KXITFWMATCH-26OCT16TUXWUE-TUX`) | 0.06 / 0.11 (12) | 8.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tara Wuerth (`KXITFWMATCH-26OCT16TUXWUE-WUE`) | 0.85 / 0.92 (91) | 88.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oleksandr Ovcharenko / Kai Wehnelt vs Juan Jose Bianchi / Kody Pearson -- ATP Challenger Catania SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 15:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-16T15:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16OVCWEHBIAPEA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Jose Bianchi / Kody Pearson (`KXATPCHALLENGERDOUBLES-26OCT16OVCWEHBIAPEA-BIAPEA`) | 0.22 / 0.35 (12) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Oleksandr Ovcharenko / Kai Wehnelt (`KXATPCHALLENGERDOUBLES-26OCT16OVCWEHBIAPEA-OVCWEH`) | 0.65 / 0.81 (27) | 73.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Max Wiskandt vs Massimo Giunta -- ATP Challenger Catania QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 15:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-16T15:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208328:210668:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Massimo Giunta (`KXATPCHALLENGERMATCH-26OCT16WISGIU-GIU`) | 0.65 / 0.66 (2803) | 65.5% | 38.8% | 33.8% | 36.1% [33.9%-38.4%] | 64.6% | 66.0% | 65.3% | MODEL_LONE_OUTLIER | PASS | -26.7 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Max Wiskandt (`KXATPCHALLENGERMATCH-26OCT16WISGIU-WIS`) | 0.34 / 0.35 (3181) | 34.5% | 61.2% | 66.2% | 63.9% [61.6%-66.1%] | 35.4% | 33.8% | 34.6% | MODEL_LONE_OUTLIER | PASS | +26.7 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1551.0, B 1067.0; serve-point win A 66.5%, B 35.8%; Elo A 1434.4, B 1350.5; model uncertainty 0.0226
* Form inputs: days since last match A 704, B 11; matches on record A 146, B 99; data quality F

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT16WISGIU-WIS  (YES = Max Wiskandt)
Model: 61%
Kalshi: 34%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Carlos Alvarez Valdes / Massucco vs Ifi / Stanke -- M25 Santa Margherita di Pula SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16CARMASIFISTA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlos Alvarez Valdes / Massucco (`KXITFDOUBLES-26OCT16CARMASIFISTA-CARMAS`) | 0.45 / 0.64 (2) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ifi / Stanke (`KXITFDOUBLES-26OCT16CARMASIFISTA-IFISTA`) | 0.22 / 0.50 (3) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Andrea Fiorentini vs Peter Makk -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16FIOMAK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrea Fiorentini (`KXITFMATCH-26OCT16FIOMAK-FIO`) | 0.19 / 0.74 (3) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Peter Makk (`KXITFMATCH-26OCT16FIOMAK-MAK`) | 0.34 / 0.89 (1) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valentin Gonzalez-Galino vs Giulio Perego -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16GONPER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valentin Gonzalez-Galino (`KXITFMATCH-26OCT16GONPER-GON`) | 0.08 / 0.60 (70) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Giulio Perego (`KXITFMATCH-26OCT16GONPER-PER`) | 0.72 / 0.74 (1) | 73.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lagerbohm / Vasa vs Chang / Wright -- M25 Santa Margherita di Pula SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16LAGVASCHAWRI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chang / Wright (`KXITFDOUBLES-26OCT16LAGVASCHAWRI-CHAWRI`) | 0.24 / 0.33 (42) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lagerbohm / Vasa (`KXITFDOUBLES-26OCT16LAGVASCHAWRI-LAGVAS`) | 0.42 / 0.76 (0) | 59.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Amit Vales vs Benjamin Gusic Wan -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16VALGUS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Benjamin Gusic Wan (`KXITFMATCH-26OCT16VALGUS-GUS`) | 0.16 / 0.70 (16) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Amit Vales (`KXITFMATCH-26OCT16VALGUS-VAL`) | 0.40 / 0.89 (26) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jip Van Assendelft vs Petros Tsitsipas -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16VANTSI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Petros Tsitsipas (`KXITFMATCH-26OCT16VANTSI-TSI`) | 0.70 / 0.81 (21) | 75.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jip Van Assendelft (`KXITFMATCH-26OCT16VANTSI-VAN`) | 0.26 / 0.31 (3) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mika Buchnik vs Elena Ruxandra Bertea -- W35 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-16T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:238205:246493:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elena Ruxandra Bertea (`KXITFWMATCH-26OCT16BUCBER-BER`) | 0.90 / 0.91 (1) | 90.5% | -- | 90.5% | 88.6% [85.7%-91.2%] | 86.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.9 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mika Buchnik (`KXITFWMATCH-26OCT16BUCBER-BUC`) | 0.07 / 0.10 (39) | 8.5% | -- | 9.5% | 11.4% [8.8%-14.3%] | 13.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.9 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 770.0, B 3327.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0273
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luciano / Mariani vs Bohrer Martins / Ezzat -- W35 Santa Margherita di Pula SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16LUCMARBOHEZZ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bohrer Martins / Ezzat (`KXITFWDOUBLES-26OCT16LUCMARBOHEZZ-BOHEZZ`) | 0.28 / 0.61 (64) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luciano / Mariani (`KXITFWDOUBLES-26OCT16LUCMARBOHEZZ-LUCMAR`) | 0.21 / 0.49 (49) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Lucie Havlickova vs Jil Teichmann -- WTA 125K Rovereto QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-16 19:00Z
* Current expected start: 2026-10-16 16:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: 2026-10-16 15:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Hard · scheduled 2026-10-16T19:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:213525:222980:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucie Havlickova (`KXWTACHALLENGERMATCH-26OCT16HAVTEI-HAV`) | 0.60 / 0.61 (10828) | 60.5% | -- | 69.0% | 61.8% [49.5%-67.1%] | 59.9% | 59.6% | 59.7% | MODEL_LONE_OUTLIER | PASS | +1.3 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Jil Teichmann (`KXWTACHALLENGERMATCH-26OCT16HAVTEI-TEI`) | 0.39 / 0.40 (951) | 39.5% | -- | 31.1% | 38.2% [32.9%-50.5%] | 40.1% | 39.9% | 40.0% | MODEL_LONE_OUTLIER | PASS | -1.3 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 2440.0, B 2567.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.088
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.020, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Baybars / Bueno Gil vs Biletic / Kajin -- M15 Bol SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16BAYBUEBILKAJ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Baybars / Bueno Gil (`KXITFDOUBLES-26OCT16BAYBUEBILKAJ-BAYBUE`) | 0.11 / 0.42 (43) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Biletic / Kajin (`KXITFDOUBLES-26OCT16BAYBUEBILKAJ-BILKAJ`) | 0.20 / 0.68 (78) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Sergio Callejon Hernando vs Luca Castagnola -- M15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-16T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209337:212090:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sergio Callejon Hernando (`KXITFMATCH-26OCT16CALCAS-CAL`) | 0.84 / 0.85 (810) | 84.5% | 63.2% | 67.7% | 58.8% [54.1%-63.9%] | 82.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -21.3 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luca Castagnola (`KXITFMATCH-26OCT16CALCAS-CAS`) | 0.16 / 0.18 (2734) | 17.0% | 36.8% | 32.3% | 41.2% [36.1%-45.9%] | 17.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +19.8 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 632.0, B 439.0; serve-point win A 58.9%, B 43.6%; Elo A 1382.9, B 1336.6; model uncertainty 0.049
* Form inputs: days since last match A 32, B 144; matches on record A 64, B 148; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT16CALCAS-CAS  (YES = Luca Castagnola)
Model: 37%
Kalshi: 17%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jacob Fearnley vs Maxim Mrva -- ATP Challenger Olbia QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-16T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207985:211617:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jacob Fearnley (`KXATPCHALLENGERMATCH-26OCT16FEAMRV-FEA`) | 0.72 / 0.73 (2205) | 72.5% | 72.0% | 67.4% | 73.3% [70.6%-76.3%] | 70.6% | 73.4% | -- | INSUFFICIENT_INPUTS | PASS | -0.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maxim Mrva (`KXATPCHALLENGERMATCH-26OCT16FEAMRV-MRV`) | 0.27 / 0.28 (18150) | 27.5% | 28.0% | 32.6% | 26.7% [23.7%-29.4%] | 29.4% | 26.0% | -- | INSUFFICIENT_INPUTS | PASS | +0.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4058.0, B 3391.0; serve-point win A 58.4%, B 46.0%; Elo A 1871.8, B 1580.7; model uncertainty 0.0281
* Form inputs: days since last match A 18, B 25; matches on record A 178, B 101; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.013, surface_dev_loose -0.022, surface_dev_tight +0.017
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Samir Hamza Reguig vs Luca Wiedenmann -- M15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16HAMWIE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Samir Hamza Reguig (`KXITFMATCH-26OCT16HAMWIE-HAM`) | 0.19 / 0.20 (399) | 19.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luca Wiedenmann (`KXITFMATCH-26OCT16HAMWIE-WIE`) | 0.78 / 0.80 (2) | 79.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Louis Larue vs Jack Loge -- M25 Luanda QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211504:211646:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Louis Larue (`KXITFMATCH-26OCT16LARLOG-LAR`) | 0.09 / 0.10 (344) | 9.5% | 11.1% | 47.9% | 22.6% [22.4%-22.8%] | 11.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Jack Loge (`KXITFMATCH-26OCT16LARLOG-LOG`) | 0.90 / 0.91 (401) | 90.5% | 88.9% | 52.1% | 77.4% [77.2%-77.6%] | 88.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 467.0; serve-point win A 54.9%, B 35.7%; Elo A 1168.5, B 1378.5; model uncertainty 0.0017
* Form inputs: days since last match A 753, B 74; matches on record A 8, B 89; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Isaac Nortey vs Thomas Faurel -- M25 Luanda QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210751:212225:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thomas Faurel (`KXITFMATCH-26OCT16NORFAU-FAU`) | 0.92 / 0.94 (1331) | 93.0% | 95.8% | 57.6% | 89.5% [88.8%-90.3%] | 91.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Isaac Nortey (`KXITFMATCH-26OCT16NORFAU-NOR`) | 0.07 / 0.08 (1249) | 7.5% | 4.2% | 42.4% | 10.4% [9.7%-11.2%] | 8.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 53.0, B 1707.0; serve-point win A 55.2%, B 31.2%; Elo A 1105.9, B 1495.8; model uncertainty 0.0074
* Form inputs: days since last match A 697, B 18; matches on record A 16, B 54; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Leonardo Rossi vs Mika Petkovic -- M15 Offenbach SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210223:213001:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mika Petkovic (`KXITFMATCH-26OCT16ROSPET-PET`) | 0.59 / 0.62 (204) | 60.5% | 55.1% | 51.5% | 45.9% [45.9%-47.4%] | 60.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Leonardo Rossi (`KXITFMATCH-26OCT16ROSPET-ROS`) | 0.37 / 0.40 (101) | 38.5% | 44.9% | 48.5% | 54.1% [52.6%-54.1%] | 39.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 84.0, B 972.0; serve-point win A 60.2%, B 38.8%; Elo A 1368.0, B 1338.0; model uncertainty 0.0077
* Form inputs: days since last match A 53, B 18; matches on record A 132, B 25; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matthias Ujvary vs Alan Wazny -- M15 Bol QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-16T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210745:213048:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthias Ujvary (`KXITFMATCH-26OCT16UJVWAZ-UJV`) | 0.22 / 0.25 (38) | 23.5% | 50.0% | 29.2% | 44.8% [42.2%-46.9%] | 25.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +26.4 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alan Wazny (`KXITFMATCH-26OCT16UJVWAZ-WAZ`) | 0.75 / 0.77 (2) | 76.0% | 50.0% | 70.8% | 55.2% [53.1%-57.8%] | 74.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -25.9 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 163.0, B 252.0; serve-point win A 59.0%, B 41.0%; Elo A 1197.2, B 1217.0; model uncertainty 0.0237
* Form inputs: days since last match A 172, B 32; matches on record A 71, B 7; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT16UJVWAZ-UJV  (YES = Matthias Ujvary)
Model: 50%
Kalshi: 24%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cirotte / Leon vs Xi Wu / Yodpetch -- W15 Islamabad SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16CIRLEOXIWYOD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cirotte / Leon (`KXITFWDOUBLES-26OCT16CIRLEOXIWYOD-CIRLEO`) | 0.21 / 0.47 (47) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xi Wu / Yodpetch (`KXITFWDOUBLES-26OCT16CIRLEOXIWYOD-XIWYOD`) | 0.43 / 0.64 (69) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Ivanova / Stankovic vs Elena Barbulescu / Simionescu -- W50 Stara Zagora SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16IVASTAELESIM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elena Barbulescu / Simionescu (`KXITFWDOUBLES-26OCT16IVASTAELESIM-ELESIM`) | 0.06 / 0.72 (0) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ivanova / Stankovic (`KXITFWDOUBLES-26OCT16IVASTAELESIM-IVASTA`) | 0.26 / 0.92 (0) | 59.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Karatancheva / Velikova vs Ivanovic / Veleva -- W50 Stara Zagora SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16KARVELIVAVEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ivanovic / Veleva (`KXITFWDOUBLES-26OCT16KARVELIVAVEL-IVAVEL`) | 0.28 / 0.53 (53) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Karatancheva / Velikova (`KXITFWDOUBLES-26OCT16KARVELIVAVEL-KARVEL`) | 0.26 / 0.57 (58) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Astrid Lew Yan Foon vs Charlotte Pikkaart -- W35 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-16T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:235159:267723:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Astrid Lew Yan Foon (`KXITFWMATCH-26OCT16LEWPIK-LEW`) | 0.93 / 0.95 (799) | 94.0% | -- | 59.0% | 76.5% [72.7%-82.5%] | 92.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -17.4 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Charlotte Pikkaart (`KXITFWMATCH-26OCT16LEWPIK-PIK`) | 0.05 / 0.06 (50) | 5.5% | -- | 41.0% | 23.4% [17.5%-27.3%] | 7.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +17.9 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1722.0, B 565.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0492
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT16LEWPIK-PIK  (YES = Charlotte Pikkaart)
Model: 23%
Kalshi: 6%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.024, surface_pool_high -0.021, surface_dev_loose +0.004, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mdlulwa / Mdlulwa vs Kuparev / Yuldasheva -- W15 Islamabad SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16MDLMDLKUPYUL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kuparev / Yuldasheva (`KXITFWDOUBLES-26OCT16MDLMDLKUPYUL-KUPYUL`) | 0.65 / 0.73 (92) | 69.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mdlulwa / Mdlulwa (`KXITFWDOUBLES-26OCT16MDLMDLKUPYUL-MDLMDL`) | 0.06 / 0.35 (0) | 20.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Izan Almazan Valiente / Pavel Lagutin vs Ignasi Forcano Aparicio / Younes Lalami Laaroussi -- ATP Challenger Catania SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 16:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-16T16:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16ALMLAGFORLAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Izan Almazan Valiente / Pavel Lagutin (`KXATPCHALLENGERDOUBLES-26OCT16ALMLAGFORLAL-ALMLAG`) | 0.34 / 0.52 (21) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ignasi Forcano Aparicio / Younes Lalami Laaroussi (`KXATPCHALLENGERDOUBLES-26OCT16ALMLAGFORLAL-FORLAL`) | 0.50 / 0.62 (100) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Hrazdil / Lakshmanan vs Dahlberg / Marek -- M15 Szabolcsveresmart SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16HRALAKDAHMAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dahlberg / Marek (`KXITFDOUBLES-26OCT16HRALAKDAHMAR-DAHMAR`) | 0.06 / 0.94 (100) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hrazdil / Lakshmanan (`KXITFDOUBLES-26OCT16HRALAKDAHMAR-HRALAK`) | 0.05 / 0.95 (175) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Orlando Fellin / Manukyan vs Krajci / Poritskyy -- M15 Szabolcsveresmart SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16ORLMANKRAPOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Krajci / Poritskyy (`KXITFDOUBLES-26OCT16ORLMANKRAPOR-KRAPOR`) | 0.13 / 0.43 (100) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Orlando Fellin / Manukyan (`KXITFDOUBLES-26OCT16ORLMANKRAPOR-ORLMAN`) | 0.06 / 0.67 (75) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Felix Balshaw vs Mika Brunold -- ATP Challenger Roanne QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-16T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209983:213149:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felix Balshaw (`KXATPCHALLENGERMATCH-26OCT16BALBRU-BAL`) | 0.52 / 0.53 (2835) | 52.5% | 55.7% | 58.5% | 58.0% [52.5%-61.0%] | 52.0% | 53.4% | 52.7% | MODEL_LONE_OUTLIER | PASS | +3.2 pp | NORMAL | FRESH | F / POOR | ALL_AGREE | VERIFIED |
| Mika Brunold (`KXATPCHALLENGERMATCH-26OCT16BALBRU-BRU`) | 0.46 / 0.47 (94) | 46.5% | 44.3% | 41.5% | 42.0% [39.0%-47.5%] | 48.0% | 46.5% | 47.2% | MODEL_LONE_OUTLIER | PASS | -2.2 pp | NORMAL | FRESH | F / POOR | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 1807.0, B 1536.0; serve-point win A 63.2%, B 37.9%; Elo A 1561.1, B 1510.5; model uncertainty 0.0422
* Form inputs: days since last match A 11, B 676; matches on record A 44, B 128; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.025, surface_pool_high +0.025, surface_dev_loose -0.015, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Marco Trungelliti vs Francesco Passaro -- ATP Challenger Maia QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-16T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105477:208859:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesco Passaro (`KXATPCHALLENGERMATCH-26OCT16TRUPAS-PAS`) | 0.48 / 0.49 (193) | 48.5% | 53.0% | 49.0% | 47.5% [46.5%-48.5%] | 48.0% | 48.6% | 48.3% | MARKETS_AGREE | PASS | +4.5 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Marco Trungelliti (`KXATPCHALLENGERMATCH-26OCT16TRUPAS-TRU`) | 0.51 / 0.52 (3704) | 51.5% | 47.0% | 51.0% | 52.5% [51.5%-53.5%] | 52.0% | 51.7% | 51.9% | MARKETS_AGREE | PASS | -4.5 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4986.0, B 3936.0; serve-point win A 62.8%, B 36.6%; Elo A 1774.7, B 1730.9; model uncertainty 0.01
* Form inputs: days since last match A 9, B 11; matches on record A 985, B 355; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Belibova / Gamretkaia vs Jovanovic / Kroitor -- W15 Chisinau SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16BELGAMJOVKRO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Belibova / Gamretkaia (`KXITFWDOUBLES-26OCT16BELGAMJOVKRO-BELGAM`) | 0.26 / 0.59 (31) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jovanovic / Kroitor (`KXITFWDOUBLES-26OCT16BELGAMJOVKRO-JOVKRO`) | 0.48 / 0.59 (31) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Biro / Wanja Brune Olsen vs Agureeva / Dorofeeva-Rybas -- W15 Chisinau SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16BIRWANAGUDOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Agureeva / Dorofeeva-Rybas (`KXITFWDOUBLES-26OCT16BIRWANAGUDOR-AGUDOR`) | 0.30 / 0.72 (100) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Biro / Wanja Brune Olsen (`KXITFWDOUBLES-26OCT16BIRWANAGUDOR-BIRWAN`) | 0.05 / 0.38 (40) | 21.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Manon Leonard vs Jessika Ponchet -- W35 Birmingham SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Grass · scheduled 2026-10-16T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211316:215807:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Manon Leonard (`KXITFWMATCH-26OCT16LEOPON-LEO`) | 0.41 / 0.43 (49) | 42.0% | -- | 40.7% | 34.3% [28.1%-37.7%] | 43.0% | -- | 43.0% | ALL_THREE_DISAGREE | PASS | -7.7 pp | NORMAL | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Jessika Ponchet (`KXITFWMATCH-26OCT16LEOPON-PON`) | 0.56 / 0.60 (227) | 58.0% | -- | 59.3% | 65.7% [62.3%-71.9%] | 57.0% | -- | 57.0% | MODEL_LONE_OUTLIER | WATCH | +7.7 pp | NORMAL | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3201.0, B 4138.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0481
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.010, surface_dev_loose -0.023, surface_dev_tight +0.019
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mika Stojsavljevic vs Alicia Dudeney -- W35 Birmingham SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Grass · scheduled 2026-10-16T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260206:261963:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alicia Dudeney (`KXITFWMATCH-26OCT16STODUD-DUD`) | 0.50 / 0.51 (27) | 50.5% | -- | 78.7% | 68.1% [55.3%-73.4%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +17.6 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mika Stojsavljevic (`KXITFWMATCH-26OCT16STODUD-STO`) | 0.49 / 0.51 (99) | 50.0% | -- | 21.3% | 31.9% [26.6%-44.7%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -18.1 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2019.0, B 3238.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0908
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT16STODUD-DUD  (YES = Alicia Dudeney)
Model: 68%
Kalshi: 50%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Taraba Wallberg / Zeltina vs Senic / Vladson -- W35 Santa Margherita di Pula SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16TARZELSENVLA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Senic / Vladson (`KXITFWDOUBLES-26OCT16TARZELSENVLA-SENVLA`) | 0.24 / 0.50 (50) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Taraba Wallberg / Zeltina (`KXITFWDOUBLES-26OCT16TARZELSENVLA-TARZEL`) | 0.26 / 0.60 (62) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Bianca Andreescu vs Lucrezia Stefanini -- WTA 125K Rovereto QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-16 20:30Z
* Current expected start: 2026-10-16 17:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: 2026-10-16 16:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-16T20:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT16ANDSTE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bianca Andreescu (`KXWTACHALLENGERMATCH-26OCT16ANDSTE-AND`) | 0.57 / 0.58 (2007) | 57.5% | -- | -- | -- [-----] | 58.4% | 58.5% | 58.4% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lucrezia Stefanini (`KXWTACHALLENGERMATCH-26OCT16ANDSTE-STE`) | 0.42 / 0.43 (5162) | 42.5% | -- | -- | -- [-----] | 41.6% | 41.2% | 41.4% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Agwi / Vega vs Hoffmann / Mueller -- M15 Offenbach F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16AGWVEGHOFMUE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Agwi / Vega (`KXITFDOUBLES-26OCT16AGWVEGHOFMUE-AGWVEG`) | 0.11 / 0.62 (10) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hoffmann / Mueller (`KXITFDOUBLES-26OCT16AGWVEGHOFMUE-HOFMUE`) | 0.44 / 0.45 (45) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Bernardo / Domingos vs Bajurko / Motta -- M25 Luanda SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16BERDOMBAJMOT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bajurko / Motta (`KXITFDOUBLES-26OCT16BERDOMBAJMOT-BAJMOT`) | 0.08 / 0.94 (100) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bernardo / Domingos (`KXITFDOUBLES-26OCT16BERDOMBAJMOT-BERDOM`) | 0.05 / 0.93 (1) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Gianluca Cadenasso vs Marvin Moeller -- ATP Challenger Catania QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-16T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202359:211533:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gianluca Cadenasso (`KXATPCHALLENGERMATCH-26OCT16CADMOE-CAD`) | 0.48 / 0.49 (249) | 48.5% | 41.6% | 42.7% | 40.7% [39.7%-41.7%] | 48.0% | 49.0% | 49.0% | MODEL_LONE_OUTLIER | PASS | -6.9 pp | NORMAL | FRESH | A / LIMITED | EXTERNAL_STALE | VERIFIED |
| Marvin Moeller (`KXATPCHALLENGERMATCH-26OCT16CADMOE-MOE`) | 0.51 / 0.52 (5183) | 51.5% | 58.4% | 57.3% | 59.3% [58.3%-60.3%] | 52.0% | 51.0% | 51.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.9 pp | NORMAL | FRESH | A / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 1540.0, B 2414.0; serve-point win A 57.7%, B 40.7%; Elo A 1572.1, B 1656.7; model uncertainty 0.0101
* Form inputs: days since last match A 11, B 11; matches on record A 118, B 308; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Mashtakov / Radjenovic vs Juhas / Popovic -- M15 Bol SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16MASRADJUHPOP:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juhas / Popovic (`KXITFDOUBLES-26OCT16MASRADJUHPOP-JUHPOP`) | 0.44 / 0.59 (6) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mashtakov / Radjenovic (`KXITFDOUBLES-26OCT16MASRADJUHPOP-MASRAD`) | 0.11 / 0.50 (55) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Michael Mmoh vs Luca Nardi -- ATP Challenger Olbia QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-16T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111581:208134:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michael Mmoh (`KXATPCHALLENGERMATCH-26OCT16MMONAR-MMO`) | 0.55 / 0.56 (10645) | 55.5% | 41.5% | 51.5% | 44.8% [41.8%-47.4%] | 54.1% | 54.7% | 54.7% | MODEL_LONE_OUTLIER | PASS | -14.0 pp | REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Luca Nardi (`KXATPCHALLENGERMATCH-26OCT16MMONAR-NAR`) | 0.44 / 0.45 (1726) | 44.5% | 58.5% | 48.4% | 55.2% [52.6%-58.2%] | 45.9% | 45.3% | 45.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +14.0 pp | REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 2931.0, B 3056.0; serve-point win A 58.7%, B 39.7%; Elo A 1529.5, B 1659.3; model uncertainty 0.0282
* Form inputs: days since last match A 18, B 11; matches on record A 552, B 346; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.026, surface_pool_high -0.026, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Breaz / Georgiana Goina vs Sabadi / Stabauer -- W15 Bol SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16BREGEOSABSTA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Breaz / Georgiana Goina (`KXITFWDOUBLES-26OCT16BREGEOSABSTA-BREGEO`) | 0.05 / 0.94 (100) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sabadi / Stabauer (`KXITFWDOUBLES-26OCT16BREGEOSABSTA-SABSTA`) | 0.08 / 0.92 (100) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Matej Dodig vs Tristan Boyer -- ATP Challenger Maia QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 18:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-16T18:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207729:212063:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tristan Boyer (`KXATPCHALLENGERMATCH-26OCT16DODBOY-BOY`) | 0.33 / 0.34 (3403) | 33.5% | 35.1% | 28.6% | 32.1% [28.6%-38.6%] | 34.8% | 33.4% | 33.4% | MODEL_LONE_OUTLIER | PASS | +1.6 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Matej Dodig (`KXATPCHALLENGERMATCH-26OCT16DODBOY-DOD`) | 0.66 / 0.67 (1197) | 66.5% | 64.9% | 71.4% | 67.9% [61.4%-71.4%] | 65.1% | 66.7% | 66.7% | MODEL_LONE_OUTLIER | PASS | -1.6 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3779.0, B 2991.0; serve-point win A 64.8%, B 38.3%; Elo A 1738.9, B 1659.4; model uncertainty 0.05
* Form inputs: days since last match A 11, B 11; matches on record A 215, B 220; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.027, surface_pool_high +0.026, surface_dev_loose +0.018, surface_dev_tight -0.018
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Freire Da Silva / Rivet vs Arce Fernandez / Peiro Serrano -- M15 Monastir SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16FRERIVARCPEI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arce Fernandez / Peiro Serrano (`KXITFDOUBLES-26OCT16FRERIVARCPEI-ARCPEI`) | 0.12 / 0.41 (100) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Freire Da Silva / Rivet (`KXITFDOUBLES-26OCT16FRERIVARCPEI-FRERIV`) | 0.11 / 0.71 (86) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Nagoudi / Piatti vs Nirundorn / van Wyk -- M15 Monastir SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16NAGPIANIRVAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nagoudi / Piatti (`KXITFDOUBLES-26OCT16NAGPIANIRVAN-NAGPIA`) | 0.49 / 0.52 (52) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nirundorn / van Wyk (`KXITFDOUBLES-26OCT16NAGPIANIRVAN-NIRVAN`) | 0.24 / 0.50 (5) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Barrera Aguirre / Zhu vs Krejcova / Lemaitre -- W35 Monastir SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16BARZHUKRELEM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barrera Aguirre / Zhu (`KXITFWDOUBLES-26OCT16BARZHUKRELEM-BARZHU`) | 0.05 / 0.42 (43) | 23.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Krejcova / Lemaitre (`KXITFWDOUBLES-26OCT16BARZHUKRELEM-KRELEM`) | 0.28 / 0.70 (41) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Kuzmova / Milovanovic vs Gniewkowska / Villet -- W35 Monastir SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16KUZMILGNIVIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gniewkowska / Villet (`KXITFWDOUBLES-26OCT16KUZMILGNIVIL-GNIVIL`) | 0.06 / 0.25 (100) | 15.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kuzmova / Milovanovic (`KXITFWDOUBLES-26OCT16KUZMILGNIVIL-KUZMIL`) | 0.26 / 0.85 (166) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Julia Konishi Camargo Silva vs Luna Maria Cinalli -- W15 Maceio QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220578:260711:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luna Maria Cinalli (`KXITFWMATCH-26OCT16KONCIN-CIN`) | 0.85 / 0.88 (2407) | 86.5% | -- | 75.3% | 72.7% [71.3%-75.3%] | 86.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.8 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Julia Konishi Camargo Silva (`KXITFWMATCH-26OCT16KONCIN-KON`) | 0.12 / 0.14 (2340) | 13.0% | -- | 24.7% | 27.3% [24.7%-28.7%] | 13.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +14.3 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1748.0, B 795.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.02
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ana Sofia Sanchez vs Marjorie Souza -- W15 Maceio QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:204419:260455:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ana Sofia Sanchez (`KXITFWMATCH-26OCT16SANSOU-SAN`) | 0.82 / 0.85 (471) | 83.5% | -- | 75.3% | 86.2% [83.7%-88.1%] | 82.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marjorie Souza (`KXITFWMATCH-26OCT16SANSOU-SOU`) | 0.15 / 0.18 (2332) | 16.5% | -- | 24.6% | 13.8% [11.9%-16.4%] | 17.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3191.0, B 670.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0222
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hugo Gaston vs Nicolai Budkov Kjaer -- ATP Challenger Roanne QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-16T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:149282:200384:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolai Budkov Kjaer (`KXATPCHALLENGERMATCH-26OCT16GASBUD-BUD`) | 0.44 / 0.45 (3310) | 44.5% | -- | 46.5% | 44.5% [39.0%-47.0%] | 45.9% | 45.5% | 45.5% | MODEL_LONE_OUTLIER | PASS | -0.0 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Hugo Gaston (`KXATPCHALLENGERMATCH-26OCT16GASBUD-GAS`) | 0.55 / 0.56 (2399) | 55.5% | -- | 53.5% | 55.5% [53.0%-61.0%] | 54.1% | 54.7% | 54.7% | MODEL_LONE_OUTLIER | PASS | +0.0 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4582.0, B 3085.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0397
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.030, surface_pool_high -0.020, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Pedro Henrique Chabalgoity vs Rafael Tosetto -- M15 Maringa QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16CHATOS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pedro Henrique Chabalgoity (`KXITFMATCH-26OCT16CHATOS-CHA`) | 0.40 / 0.43 (150) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rafael Tosetto (`KXITFMATCH-26OCT16CHATOS-TOS`) | 0.56 / 0.57 (58) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Josefina Estevez vs Fernanda Labrana -- W15 Maceio QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:219625:260717:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Josefina Estevez (`KXITFWMATCH-26OCT16ESTLAB-EST`) | 0.31 / 0.32 (36) | 31.5% | -- | 18.1% | 21.8% [19.1%-24.3%] | 32.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Fernanda Labrana (`KXITFWMATCH-26OCT16ESTLAB-LAB`) | 0.67 / 0.69 (505) | 68.0% | -- | 81.9% | 78.2% [75.7%-80.9%] | 67.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +10.2 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 732.0, B 2901.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0259
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Barbara Gatica vs Maria Florencia Urrutia -- W15 Maceio QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211903:220447:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barbara Gatica (`KXITFWMATCH-26OCT16GATURR-GAT`) | 0.46 / 0.48 (68) | 47.0% | -- | 37.4% | 61.1% [55.9%-70.4%] | -- | -- | -- | -- | PASS | +14.1 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Maria Florencia Urrutia (`KXITFWMATCH-26OCT16GATURR-URR`) | 0.52 / 0.53 (5832) | 52.5% | -- | 62.6% | 38.9% [29.6%-44.1%] | -- | -- | -- | -- | PASS | -13.6 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 633.0, B 2454.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0727
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matteo Martineau vs Sascha Gueymard Wayenburg -- ATP Challenger Roanne QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 20:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-16T20:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16MARGUE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sascha Gueymard Wayenburg (`KXATPCHALLENGERMATCH-26OCT16MARGUE-GUE`) | 0.69 / 0.70 (80) | 69.5% | -- | -- | -- [-----] | 68.8% | 70.2% | 70.2% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matteo Martineau (`KXATPCHALLENGERMATCH-26OCT16MARGUE-MAR`) | 0.29 / 0.31 (4142) | 30.0% | -- | -- | -- [-----] | 31.2% | 29.9% | 29.9% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Francisco Comesana vs Genaro Alberto Olivieri -- ATP Challenger Santa Cruz 2 QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-16T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16COMOLI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francisco Comesana (`KXATPCHALLENGERMATCH-26OCT16COMOLI-COM`) | 0.83 / 0.84 (231) | 83.5% | -- | -- | -- [-----] | 81.2% | 83.4% | 82.3% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Genaro Alberto Olivieri (`KXATPCHALLENGERMATCH-26OCT16COMOLI-OLI`) | 0.16 / 0.17 (2592) | 16.5% | -- | -- | -- [-----] | 18.8% | 17.1% | 17.9% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Oscar Jose Gutierrez vs Joao Eduardo Schiessl -- M15 Maringa QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:121264:210214:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oscar Jose Gutierrez (`KXITFMATCH-26OCT16GUTSCH-GUT`) | 0.34 / 0.37 (34) | 35.5% | 25.6% | 38.8% | 38.3% [36.8%-39.8%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Joao Eduardo Schiessl (`KXITFMATCH-26OCT16GUTSCH-SCH`) | 0.61 / 0.65 (416) | 63.0% | 74.4% | 61.2% | 61.7% [60.2%-63.2%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +11.4 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 982.0, B 1048.0; serve-point win A 57.4%, B 37.6%; Elo A 1306.3, B 1397.9; model uncertainty 0.0152
* Form inputs: days since last match A 676, B 11; matches on record A 549, B 131; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pedro Sakamoto vs Nicolas Bruna -- M15 Maringa QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106203:202220:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Bruna (`KXITFMATCH-26OCT16SAKBRU-BRU`) | 0.10 / 0.11 (105) | 10.5% | 12.6% | 21.7% | 11.5% [10.1%-12.5%] | 13.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pedro Sakamoto (`KXITFMATCH-26OCT16SAKBRU-SAK`) | 0.88 / 0.89 (2) | 88.5% | 87.5% | 78.3% | 88.5% [87.5%-89.9%] | 86.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1912.0, B 232.0; serve-point win A 65.5%, B 43.4%; Elo A 1566.3, B 1187.6; model uncertainty 0.0117
* Form inputs: days since last match A 18, B 683; matches on record A 670, B 89; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lucas Andrade Da Silva vs Juan Sebastian Gomez -- M15 Quito QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-16T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105944:212455:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucas Andrade Da Silva (`KXITFMATCH-26OCT16ANDGOM-AND`) | 0.86 / 0.87 (0) | 86.5% | 63.0% | 76.2% | 56.7% [52.0%-62.7%] | 83.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -23.5 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Juan Sebastian Gomez (`KXITFMATCH-26OCT16ANDGOM-GOM`) | 0.12 / 0.13 (140) | 12.5% | 37.0% | 23.8% | 43.3% [37.3%-47.9%] | 16.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +24.5 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 387.0, B 933.0; serve-point win A 61.0%, B 41.5%; Elo A 1401.0, B 1391.0; model uncertainty 0.0534
* Form inputs: days since last match A 18, B 102; matches on record A 10, B 466; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT16ANDGOM-GOM  (YES = Juan Sebastian Gomez)
Model: 37%
Kalshi: 12%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pepijn Bastiaansen vs Jack Anthrop -- M15 Lexington KY QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-16T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210294:212310:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jack Anthrop (`KXITFMATCH-26OCT16BASANT-ANT`) | 0.81 / 0.85 (325) | 83.0% | 79.5% | 54.5% | 70.9% [70.0%-71.2%] | 82.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pepijn Bastiaansen (`KXITFMATCH-26OCT16BASANT-BAS`) | 0.15 / 0.18 (749) | 16.5% | 20.5% | 45.5% | 29.1% [28.8%-30.0%] | 17.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 204.0; serve-point win A 60.1%, B 33.4%; Elo A 1255.2, B 1409.7; model uncertainty 0.0061
* Form inputs: days since last match A 711, B 396; matches on record A 3, B 59; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.009, surface_dev_loose +0.000, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hernando Jose Escurra Isnardi vs Julian Cundom -- M15 Maringa QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200622:208424:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julian Cundom (`KXITFMATCH-26OCT16ESCCUN-CUN`) | 0.44 / 0.47 (11) | 45.5% | 49.6% | 56.1% | 46.9% [45.9%-46.9%] | -- | -- | -- | -- | PASS | +4.1 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hernando Jose Escurra Isnardi (`KXITFMATCH-26OCT16ESCCUN-ESC`) | 0.50 / 0.54 (22) | 52.0% | 50.4% | 43.9% | 53.0% [53.0%-54.1%] | -- | -- | -- | -- | PASS | -1.6 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 342.0, B 87.0; serve-point win A 61.7%, B 38.4%; Elo A 1211.6, B 1183.1; model uncertainty 0.0051
* Form inputs: days since last match A 27, B 130; matches on record A 54, B 29; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mwendwa Mbithi vs Daniel Salazar -- M15 Quito QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-16T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132017:202369:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mwendwa Mbithi (`KXITFMATCH-26OCT16MBISAL-MBI`) | 0.38 / 0.42 (30) | 40.0% | 43.4% | 35.9% | 54.1% [53.1%-55.1%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Daniel Salazar (`KXITFMATCH-26OCT16MBISAL-SAL`) | 0.53 / 0.60 (34) | 56.5% | 56.6% | 64.1% | 45.9% [44.9%-46.9%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 166.0; serve-point win A 60.0%, B 38.8%; Elo A 1277.7, B 1249.2; model uncertainty 0.0102
* Form inputs: days since last match A 676, B 207; matches on record A 130, B 41; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Theo Papamalamis vs Johan Oscar Lien -- M15 Lexington KY QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16PAPLIE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Johan Oscar Lien (`KXITFMATCH-26OCT16PAPLIE-LIE`) | 0.20 / 0.24 (254) | 22.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Theo Papamalamis (`KXITFMATCH-26OCT16PAPLIE-PAP`) | 0.75 / 0.79 (92) | 77.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nikola Slavic vs Felix Corwin -- M15 Lexington KY QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-16T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200228:208302:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felix Corwin (`KXITFMATCH-26OCT16SLACOR-COR`) | 0.61 / 0.64 (13) | 62.5% | 82.1% | 66.1% | 74.4% [74.0%-75.5%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +19.6 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nikola Slavic (`KXITFMATCH-26OCT16SLACOR-SLA`) | 0.33 / 0.37 (75) | 35.0% | 17.9% | 33.9% | 25.6% [24.5%-26.1%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -17.1 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 99.0, B 760.0; serve-point win A 59.5%, B 33.2%; Elo A 1251.3, B 1441.2; model uncertainty 0.0076
* Form inputs: days since last match A 96, B 207; matches on record A 17, B 313; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT16SLACOR-COR  (YES = Felix Corwin)
Model: 82%
Kalshi: 62%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high +0.000, surface_dev_loose -0.007, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eli Stephenson vs Noah Zamora -- M15 Lexington KY QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16STEZAM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eli Stephenson (`KXITFMATCH-26OCT16STEZAM-STE`) | 0.25 / 0.28 (110) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Noah Zamora (`KXITFMATCH-26OCT16STEZAM-ZAM`) | 0.72 / 0.74 (130) | 73.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ayana Akli vs Ariana Arseneault -- W50 Quebec City QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-16T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220502:264149:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ayana Akli (`KXITFWMATCH-26OCT16AKLARS-AKL`) | 0.58 / 0.61 (19) | 59.5% | -- | 54.2% | 59.5% [57.4%-63.5%] | 59.1% | -- | 59.1% | MODEL_LONE_OUTLIER | PASS | -0.1 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Ariana Arseneault (`KXITFWMATCH-26OCT16AKLARS-ARS`) | 0.38 / 0.41 (47) | 39.5% | -- | 45.8% | 40.6% [36.5%-42.6%] | 40.9% | -- | 40.9% | EXTERNAL_LONE_OUTLIER | PASS | +1.1 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 2838.0, B 2049.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0308
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luis Guto Miguel vs Hugo Dellien -- ATP Challenger Santa Cruz 2 QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 22:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-16T22:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16MIGDEL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Dellien (`KXATPCHALLENGERMATCH-26OCT16MIGDEL-DEL`) | 0.67 / 0.68 (3216) | 67.5% | -- | -- | -- [-----] | 66.4% | 67.6% | 67.6% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luis Guto Miguel (`KXATPCHALLENGERMATCH-26OCT16MIGDEL-MIG`) | 0.32 / 0.34 (2991) | 33.0% | -- | -- | -- [-----] | 33.6% | 32.2% | 32.2% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Ayala / Romero vs Krajmer / Souza -- W15 Maceio SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16AYAROMKRASOU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ayala / Romero (`KXITFWDOUBLES-26OCT16AYAROMKRASOU-AYAROM`) | 0.08 / 0.91 (277) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Krajmer / Souza (`KXITFWDOUBLES-26OCT16AYAROMKRASOU-KRASOU`) | 0.05 / 0.26 (33) | 15.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Juan Manuel La Serna vs Franco Roncadelli -- ATP Challenger Santa Cruz 2 QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-16T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16LARON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Manuel La Serna (`KXATPCHALLENGERMATCH-26OCT16LARON-LA`) | 0.47 / 0.49 (5018) | 48.0% | -- | -- | -- [-----] | -- | 47.3% | 47.3% | MARKETS_AGREE | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Franco Roncadelli (`KXATPCHALLENGERMATCH-26OCT16LARON-RON`) | 0.52 / 0.53 (11555) | 52.5% | -- | -- | -- [-----] | -- | 52.9% | 52.9% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Lui Maxted vs Andrew Fenty -- M25 Austin TX QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-16T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208649:210747:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrew Fenty (`KXITFMATCH-26OCT16MAXFEN-FEN`) | 0.40 / 0.42 (14) | 41.0% | 53.6% | 42.4% | 48.0% [46.0%-49.0%] | 40.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +12.6 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lui Maxted (`KXITFMATCH-26OCT16MAXFEN-MAX`) | 0.56 / 0.59 (51) | 57.5% | 46.4% | 57.6% | 52.0% [51.0%-54.0%] | 59.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.1 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 1001.0; serve-point win A 61.6%, B 37.7%; Elo A 1353.4, B 1337.4; model uncertainty 0.0152
* Form inputs: days since last match A 725, B 53; matches on record A 16, B 95; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.020, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Benjamin Willwerth vs Cosme Rolland de Ravel -- M25 Austin TX QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-16T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213653:tml:R0KE:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cosme Rolland de Ravel (`KXITFMATCH-26OCT16WILROL-ROL`) | 0.51 / 0.53 (1) | 52.0% | 61.1% | 61.1% | 65.5% [64.5%-66.5%] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +9.1 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Benjamin Willwerth (`KXITFMATCH-26OCT16WILROL-WIL`) | 0.46 / 0.47 (342) | 46.5% | 38.9% | 38.9% | 34.5% [33.5%-35.5%] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.6 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 352.0, B 473.0; serve-point win A 59.7%, B 38.1%; Elo A 1342.8, B 1459.5; model uncertainty 0.0098
* Form inputs: days since last match A 53, B 109; matches on record A 11, B 7; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.009, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Thara Gowda vs Reese Brantmeier -- W50 Quebec City QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-16T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222034:270453:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Reese Brantmeier (`KXITFWMATCH-26OCT16GOWBRA-BRA`) | 0.93 / 0.95 (692) | 94.0% | -- | 25.0% | 72.0% [61.9%-78.8%] | 92.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -22.0 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Thara Gowda (`KXITFWMATCH-26OCT16GOWBRA-GOW`) | 0.06 / 0.08 (3780) | 7.0% | -- | 75.0% | 28.0% [21.2%-38.1%] | 7.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +21.0 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 169.0, B 133.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0846
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT16GOWBRA-GOW  (YES = Thara Gowda)
Model: 28%
Kalshi: 7%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.039, surface_pool_high +0.056, surface_dev_loose +0.005, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Thiago Seyboth Wild vs Nicolas Kicker -- ATP Challenger Santa Cruz 2 QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 23:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-16T23:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16SEYKIC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Kicker (`KXATPCHALLENGERMATCH-26OCT16SEYKIC-KIC`) | 0.14 / 0.15 (1952) | 14.5% | -- | -- | -- [-----] | 16.4% | 17.1% | 16.4% | KALSHI_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Thiago Seyboth Wild (`KXATPCHALLENGERMATCH-26OCT16SEYKIC-SEY`) | 0.85 / 0.86 (606) | 85.5% | -- | -- | -- [-----] | 83.6% | 83.8% | 83.6% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Alex Hernandez vs Ivan Dreycopp -- M15 Quito QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 23:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16HERDRE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ivan Dreycopp (`KXITFMATCH-26OCT16HERDRE-DRE`) | 0.26 / 0.29 (96) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alex Hernandez (`KXITFMATCH-26OCT16HERDRE-HER`) | 0.69 / 0.73 (1) | 71.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Juan Sebastian Osorio vs Tristan McCormick -- M15 Quito QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 23:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16OSOMCC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tristan McCormick (`KXITFMATCH-26OCT16OSOMCC-MCC`) | 0.58 / 0.61 (22) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Juan Sebastian Osorio (`KXITFMATCH-26OCT16OSOMCC-OSO`) | 0.38 / 0.40 (13) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuki Naito vs Mimi Xu -- W50 Quebec City QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 23:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-16T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216044:259685:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuki Naito (`KXITFWMATCH-26OCT16NAIXUX-NAI`) | 0.42 / 0.44 (5) | 43.0% | -- | 53.2% | 44.2% [39.5%-47.9%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.2 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Mimi Xu (`KXITFWMATCH-26OCT16NAIXUX-XUX`) | 0.52 / 0.55 (55) | 53.5% | -- | 46.8% | 55.8% [52.1%-60.5%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.3 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 2186.0, B 1841.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0418
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.037, surface_pool_high -0.031, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Fuchs / Hopper vs Roddick / Tokac -- M25 Austin TX SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-17T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16FUCHOPRODTOK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fuchs / Hopper (`KXITFDOUBLES-26OCT16FUCHOPRODTOK-FUCHOP`) | 0.08 / 0.72 (79) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Roddick / Tokac (`KXITFDOUBLES-26OCT16FUCHOPRODTOK-RODTOK`) | 0.11 / 0.43 (10) | 27.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Iker Urribarrens Ramirez vs Dominick Mosejczuk -- M25 Austin TX QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-17T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16URRMOS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dominick Mosejczuk (`KXITFMATCH-26OCT16URRMOS-MOS`) | 0.76 / 0.78 (32) | 77.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Iker Urribarrens Ramirez (`KXITFMATCH-26OCT16URRMOS-URR`) | 0.21 / 0.24 (57) | 22.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mediorreal Arias / Sofia Sanchez vs Gatica / Pereira -- W15 Maceio SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-17T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16MEDSOFGATPER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gatica / Pereira (`KXITFWDOUBLES-26OCT16MEDSOFGATPER-GATPER`) | 0.08 / 0.76 (104) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mediorreal Arias / Sofia Sanchez (`KXITFWDOUBLES-26OCT16MEDSOFGATPER-MEDSOF`) | 0.08 / 0.41 (42) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Kajsa Rinaldo Persson vs Sara Saito -- W50 Quebec City QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-17T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211643:260170:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kajsa Rinaldo Persson (`KXITFWMATCH-26OCT16RINSAI-RIN`) | 0.61 / 0.65 (2) | 63.0% | -- | 71.3% | 64.6% [58.5%-67.5%] | -- | -- | -- | -- | PASS | +1.6 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sara Saito (`KXITFWMATCH-26OCT16RINSAI-SAI`) | 0.34 / 0.35 (193) | 34.5% | -- | 28.7% | 35.4% [32.5%-41.5%] | -- | -- | -- | -- | PASS | +0.9 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3104.0, B 3341.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0452
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose +0.010, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Inoue / Naito vs Brantmeier / Xu -- W50 Quebec City SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 00:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-17T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16INONAIBRAXUX:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brantmeier / Xu (`KXITFWDOUBLES-26OCT16INONAIBRAXUX-BRAXUX`) | 0.08 / 0.78 (113) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Inoue / Naito (`KXITFWDOUBLES-26OCT16INONAIBRAXUX-INONAI`) | 0.08 / 0.39 (40) | 23.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Alvarado / Mbithi vs Covato / Voelzke -- M15 Quito SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-17T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16ALVMBICOVVOE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alvarado / Mbithi (`KXITFDOUBLES-26OCT16ALVMBICOVVOE-ALVMBI`) | 0.08 / 0.61 (64) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Covato / Voelzke (`KXITFDOUBLES-26OCT16ALVMBICOVVOE-COVVOE`) | 0.31 / 0.57 (58) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Del Pino / Mouilleron Salvo vs Sebastian Gomez / Urrea -- M15 Quito SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-17T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16DELMOUSEBURR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Del Pino / Mouilleron Salvo (`KXITFDOUBLES-26OCT16DELMOUSEBURR-DELMOU`) | 0.08 / 0.49 (49) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sebastian Gomez / Urrea (`KXITFDOUBLES-26OCT16DELMOUSEBURR-SEBURR`) | 0.08 / 0.68 (78) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Sayaka Ishii vs Elina Avanesyan -- WTA Osaka Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 05:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 02:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: 2026-10-17 01:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T05:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT16ISHAVA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elina Avanesyan (`KXWTAMATCH-26OCT16ISHAVA-AVA`) | 0.17 / 0.85 (1) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sayaka Ishii (`KXWTAMATCH-26OCT16ISHAVA-ISH`) | 0.16 / 0.74 (1) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Maya Joint vs Kyoka Okamura -- WTA Osaka Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 05:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 02:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: 2026-10-17 01:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T05:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT16JOIOKA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maya Joint (`KXWTAMATCH-26OCT16JOIOKA-JOI`) | 0.24 / 0.85 (1) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kyoka Okamura (`KXWTAMATCH-26OCT16JOIOKA-OKA`) | 0.16 / 0.60 (1) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ena Koike vs Kayla Day -- WTA Osaka Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 05:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 02:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: 2026-10-17 01:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T05:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT16KOIDAY:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kayla Day (`KXWTAMATCH-26OCT16KOIDAY-DAY`) | 0.30 / 0.74 (1) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ena Koike (`KXWTAMATCH-26OCT16KOIDAY-KOI`) | 0.16 / 0.56 (1) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mary Stoiana vs Rinko Matsuda -- WTA Osaka Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 05:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 02:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: 2026-10-17 01:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T05:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT16STOMAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rinko Matsuda (`KXWTAMATCH-26OCT16STOMAT-MAT`) | 0.16 / 0.55 (50) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mary Stoiana (`KXWTAMATCH-26OCT16STOMAT-STO`) | 0.31 / 0.85 (1) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Harriet Dart vs Rina Saigo -- WTA Osaka Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 06:40Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 04:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: 2026-10-17 03:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T06:40:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT16DARSAI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Harriet Dart (`KXWTAMATCH-26OCT16DARSAI-DAR`) | 0.28 / 0.85 (1) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rina Saigo (`KXWTAMATCH-26OCT16DARSAI-SAI`) | 0.16 / 0.58 (1) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Aoi Ito vs Tyra Caterina Grant -- WTA Osaka Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 06:40Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 04:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: 2026-10-17 03:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T06:40:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT16ITOGRA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tyra Caterina Grant (`KXWTAMATCH-26OCT16ITOGRA-GRA`) | 0.22 / 0.85 (1) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aoi Ito (`KXWTAMATCH-26OCT16ITOGRA-ITO`) | 0.16 / 0.82 (1) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sinja Kraus vs Momoko Kobori -- WTA Osaka Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 06:40Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 04:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: 2026-10-17 03:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T06:40:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT16KRAKOB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Momoko Kobori (`KXWTAMATCH-26OCT16KRAKOB-KOB`) | 0.16 / 0.66 (40) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sinja Kraus (`KXWTAMATCH-26OCT16KRAKOB-KRA`) | 0.25 / 0.74 (1) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Claire Liu vs Kanon Sawashiro -- WTA Osaka Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 06:40Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 04:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: 2026-10-17 03:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T06:40:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT16LIUSAW:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Claire Liu (`KXWTAMATCH-26OCT16LIUSAW-LIU`) | 0.16 / 0.74 (1) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kanon Sawashiro (`KXWTAMATCH-26OCT16LIUSAW-SAW`) | 0.16 / 0.85 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Debru / Marionneau vs Poling / Vance -- M25 Austin TX SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-17T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16DEBMARPOLVAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Debru / Marionneau (`KXITFDOUBLES-26OCT16DEBMARPOLVAN-DEBMAR`) | 0.08 / 0.66 (73) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Poling / Vance (`KXITFDOUBLES-26OCT16DEBMARPOLVAN-POLVAN`) | 0.08 / 0.57 (58) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Alastair Gray vs Sebastian Gorzny -- M25 Austin TX QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-17T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16GRAGOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sebastian Gorzny (`KXITFMATCH-26OCT16GRAGOR-GOR`) | 0.59 / 0.64 (73) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alastair Gray (`KXITFMATCH-26OCT16GRAGOR-GRA`) | 0.35 / 0.39 (5) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arseneault / Lacasse vs Abe / Yoshioka -- W50 Quebec City SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-17T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16ARSLACABEYOS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Abe / Yoshioka (`KXITFWDOUBLES-26OCT16ARSLACABEYOS-ABEYOS`) | 0.08 / 0.62 (65) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arseneault / Lacasse (`KXITFWDOUBLES-26OCT16ARSLACABEYOS-ARSLAC`) | 0.08 / 0.61 (64) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Salma Drugdova vs Lea Ma -- W35 Redding CA QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-17T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16DRUMAX:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Salma Drugdova (`KXITFWMATCH-26OCT16DRUMAX-DRU`) | 0.08 / 0.12 (1040) | 10.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lea Ma (`KXITFWMATCH-26OCT16DRUMAX-MAX`) | 0.87 / 0.92 (100) | 89.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maria Sholokhova vs Connie Ma -- W35 Redding CA QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-17T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16SHOMAX:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Connie Ma (`KXITFWMATCH-26OCT16SHOMAX-MAX`) | 0.73 / 0.79 (35) | 76.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maria Sholokhova (`KXITFWMATCH-26OCT16SHOMAX-SHO`) | 0.20 / 0.26 (52) | 23.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vivian Wolff vs Nao Nishino -- W35 Redding CA QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-17T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16WOLNIS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nao Nishino (`KXITFWMATCH-26OCT16WOLNIS-NIS`) | 0.26 / 0.33 (30) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vivian Wolff (`KXITFWMATCH-26OCT16WOLNIS-WOL`) | 0.66 / 0.71 (36) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Taylah Preston vs Haruka Kaji -- WTA Osaka Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 07:50Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 05:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: 2026-10-17 04:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T07:50:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT17PREKAJ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Haruka Kaji (`KXWTAMATCH-26OCT17PREKAJ-KAJ`) | 0.08 / 0.92 (33) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Taylah Preston (`KXWTAMATCH-26OCT17PREKAJ-PRE`) | 0.08 / 0.93 (200) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Sara Sorribes Tormo vs Maddison Inglis -- WTA Osaka Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 07:50Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 05:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: 2026-10-17 04:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T07:50:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT17SORING:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maddison Inglis (`KXWTAMATCH-26OCT17SORING-ING`) | 0.08 / 0.82 (30) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sara Sorribes Tormo (`KXWTAMATCH-26OCT17SORING-SOR`) | 0.08 / 0.93 (200) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Heather Watson vs Emerson Jones -- WTA Osaka Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 07:50Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 05:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: 2026-10-17 04:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T07:50:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT17WATJON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emerson Jones (`KXWTAMATCH-26OCT17WATJON-JON`) | 0.08 / 0.93 (222) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Heather Watson (`KXWTAMATCH-26OCT17WATJON-WAT`) | 0.08 / 0.93 (200) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Mei Yamaguchi vs Sofia Kenin -- WTA Osaka Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 07:50Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: 2026-10-17 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T07:50:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT17YAMKEN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Kenin (`KXWTAMATCH-26OCT17YAMKEN-KEN`) | 0.09 / 0.93 (222) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mei Yamaguchi (`KXWTAMATCH-26OCT17YAMKEN-YAM`) | 0.08 / 0.93 (200) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Rencheli / Sholokhova vs Elizabeth Reasco Gonzalez / Rodriguez -- W35 Redding CA SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-17T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16RENSHOELIROD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elizabeth Reasco Gonzalez / Rodriguez (`KXITFWDOUBLES-26OCT16RENSHOELIROD-ELIROD`) | 0.08 / 0.56 (56) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rencheli / Sholokhova (`KXITFWDOUBLES-26OCT16RENSHOELIROD-RENSHO`) | 0.08 / 0.69 (80) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Alexander Zverev vs Alejandro Davidovich Fokina -- ATP Shanghai SF

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-10-17 07:00Z
* Current expected start: 2026-10-17 07:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: 2026-10-17 06:15Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-17T04:00:00+00:00 as not a valid time

ATP (MASTERS_1000) · Hard · scheduled 2026-10-17T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:100644:200221:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alejandro Davidovich Fokina (`KXATPMATCH-26OCT17ZVEDAV-DAV`) | 0.24 / 0.26 (136884) | 25.0% | -- | 19.8% | 20.8% [20.1%-21.5%] | 25.5% | 24.6% | 25.1% | MODEL_LONE_OUTLIER | PASS | -4.2 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Alexander Zverev (`KXATPMATCH-26OCT17ZVEDAV-ZVE`) | 0.74 / 0.75 (7196) | 74.5% | -- | 80.2% | 79.2% [78.5%-79.9%] | 74.5% | 75.5% | 75.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +4.7 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 7502.0, B 4905.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0068
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.007, surface_dev_loose -0.001, surface_dev_tight +0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 4 carry a model probability
  * `KXATPEXACTMATCH-26OCT17ZVEDAV-ZVE21` Will Alexander Zverev win the Alexander Zverev vs Alejandro Davidovich Fokina match by a set score of 2-1?: 0.01/0.28 mid 14.5%, model 29.6% (market_conditioned_v1 (model4_board_v1)) -- gap +15.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17ZVEDAV-DAV21` Will Alejandro Davidovich Fokina win the Alexander Zverev vs Alejandro Davidovich Fokina match by a set score of 2-1?: 0.01/0.15 mid 8.0%, model 14.6% (market_conditioned_v1 (model4_board_v1)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17ZVEDAV-ZVE20` Will Alexander Zverev win the Alexander Zverev vs Alejandro Davidovich Fokina match by a set score of 2-0?: 0.46/0.52 mid 49.0%, model 44.9% (market_conditioned_v1 (model4_board_v1)) -- gap -4.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17ZVEDAV-DAV20` Will Alejandro Davidovich Fokina win the Alexander Zverev vs Alejandro Davidovich Fokina match by a set score of 2-0?: 0.08/0.15 mid 11.5%, model 10.9% (market_conditioned_v1 (model4_board_v1)) -- gap -0.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jakob Schnaitter / Mark Wallner vs Lucas Miedler / Neil Oberleitner -- ATP Shanghai SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-17T04:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-17T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT17SCHWALMIEOBE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucas Miedler / Neil Oberleitner (`KXATPDOUBLES-26OCT17SCHWALMIEOBE-MIEOBE`) | 0.64 / 0.66 (348) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jakob Schnaitter / Mark Wallner (`KXATPDOUBLES-26OCT17SCHWALMIEOBE-SCHWAL`) | 0.34 / 0.35 (42) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Sonay Kartal vs Jelena Ostapenko -- WTA Wuhan SF

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-10-17 10:00Z
* Current expected start: 2026-10-17 10:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 08:52Z
* Recommended handicap-by time: 2026-10-17 09:15Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-17T04:00:00+00:00 as not a valid time

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-17T10:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT17KAROST:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sonay Kartal (`KXWTAMATCH-26OCT17KAROST-KAR`) | 0.53 / 0.57 (3796) | 55.0% | -- | -- | -- [-----] | -- | 54.9% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jelena Ostapenko (`KXWTAMATCH-26OCT17KAROST-OST`) | 0.41 / 0.46 (791) | 43.5% | -- | -- | -- [-----] | -- | 44.3% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
