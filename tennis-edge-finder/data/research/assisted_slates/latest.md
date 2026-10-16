# ASSISTED SLATE -- 2026-10-16T12:22Z (`SL-20261016T122252Z-ffc79117`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

139 open matches not seen started, 395 markets. Skipped: {"scheduled_start_over_24h_past": 12, "first_ball_already_observed": 6}. Sources: shadow board 2026-10-16T05:03:16.849492+00:00, Model 4 2026-10-16T05:03:35.739621+00:00, Gen-1 ledger 2026-10-16T05:03:13.374223+00:00, external 2026-10-16T12:09:23.978294+00:00, capture 20261016T120647Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-10-17 02:30Z**
* Recommended RUN TENNIS time: **2026-10-17 01:45Z**
* Final price/status check time: **2026-10-17 02:20Z**
* Number of matches in window: 11 (Sayaka Ishii vs Elina Avanesyan, Maya Joint vs Kyoka Okamura, Ena Koike vs Kayla Day, Mary Stoiana vs Rinko Matsuda, Katarzyna Kawa vs Katie Volynets, Daria Snigur vs Yu Jun Lin ...)

Slate built 2026-10-16T12:22Z. Refresh due by: 2026-10-17 01:45Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 16, "HIGH_REVIEW": 8, "NORMAL": 51, "REVIEW": 13, "UNPRICED": 307}; match winners: {"EXTREME": 16, "HIGH_REVIEW": 8, "NORMAL": 47, "REVIEW": 13, "UNPRICED": 194}; quote freshness at build: {"FRESH": 88}.

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
| Madison Brengle (`KXITFWMATCH-26OCT15BRESTE-BRE`) | 0.34 / 0.36 (157) | 35.0% | -- | 67.1% | 56.9% [41.5%-63.6%] | -- | -- | -- | -- | WATCH | +21.9 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sloane Stephens (`KXITFWMATCH-26OCT15BRESTE-STE`) | 0.63 / 0.65 (3) | 64.0% | -- | 32.9% | 43.1% [36.4%-58.5%] | -- | -- | -- | -- | PASS | -20.9 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

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
Reasons: LOW_DISPLAYED_LIQUIDITY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.032, surface_pool_high +0.031, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Yeonwoo Ku (`KXITFWMATCH-26OCT15KUXRUS-KUX`) | 0.57 / 0.60 (1) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arantxa Rus (`KXITFWMATCH-26OCT15KUXRUS-RUS`) | 0.40 / 0.42 (6426) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Kapasi / Sheldon (`KXITFDOUBLES-26OCT15ARSMESKAPSHE-KAPSHE`) | 0.12 / 0.78 (37) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Gogineni / Young (`KXITFDOUBLES-26OCT15ARUPIEGOGYOU-GOGYOU`) | 0.12 / 0.74 (100) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Johnson / Rapolu (`KXITFWDOUBLES-26OCT15MCASTRJOHRAP-JOHRAP`) | 0.01 / 0.64 (12) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
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
| Brostrom Poulsen / Slavic (`KXITFDOUBLES-26OCT15BROSLAMERWEE-BROSLA`) | 0.05 / 0.94 (25) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mercer / Weekes (`KXITFDOUBLES-26OCT15BROSLAMERWEE-MERWEE`) | 0.07 / 0.73 (1) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Andrea Lazaro Garcia vs Laura Samson -- WTA 125K Mallorca QF

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-16 15:30Z
* Current expected start: 2026-10-16 12:19Z
* Source: COURT_PROGRESSION: preceding match on Centre Court in progress (set 2 of best-of-3); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-16 11:34Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA125 (WTA_125) · Grass · scheduled 2026-10-16T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:210622:266671:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrea Lazaro Garcia (`KXWTACHALLENGERMATCH-26OCT16LAZSAM-LAZ`) | 0.41 / 0.42 (9064) | 41.5% | 50.4% | 43.1% | 47.3% [45.2%-53.2%] | 40.8% | 41.7% | 41.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +8.9 pp | NORMAL | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Laura Samson (`KXWTACHALLENGERMATCH-26OCT16LAZSAM-SAM`) | 0.59 / 0.60 (22148) | 59.5% | 49.6% | 56.9% | 52.7% [46.8%-54.8%] | 59.2% | 58.0% | 58.6% | MODEL_LONE_OUTLIER | PASS | -9.9 pp | NORMAL | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3043.0, B 2910.0; serve-point win A 53.2%, B 46.9%; Elo A 1816.8, B 1780.7; model uncertainty 0.04
* Form inputs: days since last match A 4, B 25; matches on record A 509, B 132; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose -0.016, surface_dev_tight +0.011
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; STATUS_AMBIGUOUS

## Dominika Salkova vs Lea Boskovic -- WTA 125K Rovereto QF

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-16 14:40Z
* Current expected start: 2026-10-16 12:19Z
* Source: COURT_PROGRESSION: preceding match on Centre Court in progress (set 2 of best-of-3); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-16 11:34Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA125 (WTA_125) · Hard · scheduled 2026-10-16T14:40:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:214521:222966:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lea Boskovic (`KXWTACHALLENGERMATCH-26OCT16SALBOS-BOS`) | 0.39 / 0.40 (5174) | 39.5% | 34.9% | 30.7% | 33.5% [32.6%-36.0%] | 40.1% | 39.0% | 39.5% | MODEL_LONE_OUTLIER | PASS | -4.6 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Dominika Salkova (`KXWTACHALLENGERMATCH-26OCT16SALBOS-SAL`) | 0.60 / 0.62 (10113) | 61.0% | 65.1% | 69.3% | 66.5% [64.0%-67.4%] | 59.9% | 61.0% | 60.5% | MODEL_LONE_OUTLIER | SHADOW_BET | +4.1 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3665.0, B 2773.0; serve-point win A 57.0%, B 46.0%; Elo A 1720.7, B 1642.4; model uncertainty 0.0169
* Form inputs: days since last match A 3, B 3; matches on record A 295, B 438; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; STATUS_AMBIGUOUS

## Sara Errani / Jasmine Paolini vs Anna Danilina / Shuai Zhang -- WTA Wuhan QF

**START STATUS: START_IMMINENT**
* Nominal schedule: 2026-10-16 14:00Z
* Current expected start: 2026-10-16 12:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-16 11:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-16T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16ERRPAODANZHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Danilina / Shuai Zhang (`KXWTADOUBLES-26OCT16ERRPAODANZHA-DANZHA`) | 0.34 / 0.36 (441) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sara Errani / Jasmine Paolini (`KXWTADOUBLES-26OCT16ERRPAODANZHA-ERRPAO`) | 0.63 / 0.65 (237) | 64.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Tamara Zidansek vs Rebeka Masarova -- WTA 125K Mallorca QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-16 16:00Z
* Current expected start: 2026-10-16 12:44Z
* Source: COURT_PROGRESSION: preceding match on Court 1 in progress (set 1 of best-of-3); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-16 11:59Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-16T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT16ZIDMAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rebeka Masarova (`KXWTACHALLENGERMATCH-26OCT16ZIDMAS-MAS`) | 0.51 / 0.52 (1012) | 51.5% | -- | -- | -- [-----] | -- | 50.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tamara Zidansek (`KXWTACHALLENGERMATCH-26OCT16ZIDMAS-ZID`) | 0.48 / 0.49 (978) | 48.5% | -- | -- | -- [-----] | -- | 49.3% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

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
| Lorenzo Giustino (`KXATPCHALLENGERMATCH-26OCT16GIUPIR-GIU`) | 0.36 / 0.37 (3310) | 36.5% | 19.6% | 21.7% | 22.9% [21.7%-24.1%] | 23.1% | 21.3% | 21.3% | MODEL_LONE_OUTLIER | PASS | -16.9 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Zsombor Piros (`KXATPCHALLENGERMATCH-26OCT16GIUPIR-PIR`) | 0.63 / 0.64 (14744) | 63.5% | 80.4% | 78.3% | 77.1% [75.9%-78.3%] | 76.9% | 79.1% | 79.1% | MODEL_LONE_OUTLIER | PASS | +16.9 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4191.0, B 4115.0; serve-point win A 57.7%, B 35.6%; Elo A 1593.7, B 1778.6; model uncertainty 0.0118
* Form inputs: days since last match A 11, B 11; matches on record A 1034, B 526; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT16GIUPIR-PIR  (YES = Zsombor Piros)
Model: 80%
Kalshi: 64%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: EXTERNAL_STALE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.004, surface_dev_loose -0.007, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

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
| Maks Kasnikowski (`KXATPCHALLENGERMATCH-26OCT16KASTRA-KAS`) | 0.75 / 0.76 (23528) | 75.5% | 47.0% | 43.3% | 41.8% [37.4%-43.9%] | 58.4% | 58.3% | 58.3% | MODEL_LONE_OUTLIER | PASS | -28.5 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Stefano Travaglia (`KXATPCHALLENGERMATCH-26OCT16KASTRA-TRA`) | 0.24 / 0.25 (26617) | 24.5% | 53.0% | 56.7% | 58.2% [56.1%-62.6%] | 41.6% | 41.5% | 41.6% | MODEL_LONE_OUTLIER | SHADOW_BET | +28.5 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 3242.0, B 3948.0; serve-point win A 60.1%, B 39.4%; Elo A 1592.6, B 1678.9; model uncertainty 0.0324
* Form inputs: days since last match A 11, B 25; matches on record A 273, B 967; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT16KASTRA-TRA  (YES = Stefano Travaglia)
Model: 53%
Kalshi: 24%
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
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.020, surface_dev_loose +0.005, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

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
| Buvaysar Gadamauri (`KXATPCHALLENGERMATCH-26OCT16GADGIL-GAD`) | 0.15 / 0.18 (180) | 16.5% | 48.3% | 50.5% | 47.0% [45.0%-48.5%] | -- | 36.2% | 36.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +31.8 pp | EXTREME (DATA_WARNING) | FRESH | A / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Felix Gill (`KXATPCHALLENGERMATCH-26OCT16GADGIL-GIL`) | 0.81 / 0.85 (104) | 83.0% | 51.7% | 49.5% | 53.0% [51.5%-55.0%] | -- | 63.5% | 63.5% | MODEL_LONE_OUTLIER | PASS | -31.3 pp | EXTREME (DATA_WARNING) | FRESH | A / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 2063.0, B 2694.0; serve-point win A 62.7%, B 37.0%; Elo A 1585.6, B 1649.8; model uncertainty 0.0176
* Form inputs: days since last match A 11, B 25; matches on record A 234, B 281; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT16GADGIL-GAD  (YES = Buvaysar Gadamauri)
Model: 48%
Kalshi: 16%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: SUPPORTS_MODEL_DIRECTION
Data quality: A (LIMITED)
Reasons: LEVEL_TRANSFER_RISK, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

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
| Zdenek Kolar (`KXATPCHALLENGERMATCH-26OCT16PAPKOL-KOL`) | 0.03 / 0.04 (40296) | 3.5% | 47.7% | 59.4% | 47.4% [43.8%-50.5%] | 43.7% | 43.7% | 43.7% | MODEL_LONE_OUTLIER | WATCH | +44.2 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | EXTERNAL_STALE | VERIFIED |
| Radu Mihai Papoe (`KXATPCHALLENGERMATCH-26OCT16PAPKOL-PAP`) | 0.96 / 0.97 (15738) | 96.5% | 52.3% | 40.6% | 52.6% [49.5%-56.2%] | 56.3% | 56.4% | 56.4% | MODEL_LONE_OUTLIER | PASS | -44.2 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 833.0, B 3944.0; serve-point win A 56.8%, B 43.6%; Elo A 1652.1, B 1582.1; model uncertainty 0.0339
* Form inputs: days since last match A 28, B 11; matches on record A 124, B 769; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT16PAPKOL-KOL  (YES = Zdenek Kolar)
Model: 48%
Kalshi: 4%
Gap: +44 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: EXTERNAL_STALE
Data quality: B (LIMITED)
Reasons: THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

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
| Valeriia Artemeva (`KXITFWMATCH-26OCT16DENART-ART`) | 0.13 / 0.15 (30) | 14.0% | -- | 19.9% | 12.2% [9.7%-14.8%] | 7.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -1.8 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rositsa Dencheva (`KXITFWMATCH-26OCT16DENART-DEN`) | 0.83 / 0.89 (105) | 86.0% | -- | 80.1% | 87.8% [85.2%-90.3%] | 92.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.8 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2446.0, B 1430.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0253
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; WIDE_SPREAD
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
| Ilinca Dalina Amariei (`KXITFWMATCH-26OCT16FITAMA-AMA`) | 0.34 / 0.37 (112) | 35.5% | -- | 39.5% | 37.5% [34.9%-38.5%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Angela Fita Boluda (`KXITFWMATCH-26OCT16FITAMA-FIT`) | 0.57 / 0.60 (25) | 58.5% | -- | 60.5% | 62.5% [61.5%-65.1%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +4.0 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4603.0, B 2360.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0176
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
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
| Denislava Glushkova (`KXITFWMATCH-26OCT16PETGLU-GLU`) | 0.11 / 0.17 (8) | 14.0% | -- | 77.8% | 82.6% [80.8%-84.0%] | 39.4% | -- | 39.4% | MODEL_LONE_OUTLIER | WATCH | +68.6 pp | EXTREME (DATA_WARNING) | FRESH | B / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Lucie Petruzelova (`KXITFWMATCH-26OCT16PETGLU-PET`) | 0.77 / 0.87 (43) | 82.0% | -- | 22.2% | 17.4% [16.0%-19.1%] | 60.6% | -- | 60.6% | ALL_THREE_DISAGREE | PASS | -64.6 pp | EXTREME (DATA_WARNING) | FRESH | B / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 1518.0, B 2333.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0156
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT16PETGLU-GLU  (YES = Denislava Glushkova)
Model: 83%
Kalshi: 14%
Gap: +69 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: SUPPORTS_MODEL_DIRECTION
Data quality: B (ADEQUATE)
Reasons: LOW_DISPLAYED_LIQUIDITY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Alena Kovackova (`KXITFWMATCH-26OCT16ZHEKOV-KOV`) | 0.99 / -- (0) | -- | -- | 79.6% | 80.4% [78.5%-82.2%] | 83.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | FRESH | C / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |
| Sonja Zhenikhova (`KXITFWMATCH-26OCT16ZHEKOV-ZHE`) | -- / 0.02 (285) | -- | -- | 20.4% | 19.6% [17.8%-21.5%] | 17.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -- | UNPRICED | FRESH | C / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 1212.0, B 2074.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0185
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE
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
| Adam Heinonen / Michael Vrbensky (`KXATPCHALLENGERDOUBLES-26OCT16HEIVRBPERWIN-HEIVRB`) | 0.08 / 0.75 (30) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tiago Pereira / Benjamin Winter Lopez (`KXATPCHALLENGERDOUBLES-26OCT16HEIVRBPERWIN-PERWIN`) | 0.21 / 0.86 (100) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Daniel Cukierman / Fernando Romboli (`KXATPCHALLENGERDOUBLES-26OCT16MASRUECUKROM-CUKROM`) | 0.49 / 0.52 (57) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daniel Masur / Tim Ruehl (`KXATPCHALLENGERDOUBLES-26OCT16MASRUECUKROM-MASRUE`) | 0.44 / 0.49 (129) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

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
| Alexandru Jecan / Szymon Kielan (`KXATPCHALLENGERDOUBLES-26OCT16KARPAUJECKIE-JECKIE`) | 0.08 / 0.15 (1) | 11.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Milos Karol / Andrew Paulson (`KXATPCHALLENGERDOUBLES-26OCT16KARPAUJECKIE-KARPAU`) | 0.77 / 0.86 (601) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Juan Jose Bianchi / Kody Pearson (`KXATPCHALLENGERDOUBLES-26OCT16OVCWEHBIAPEA-BIAPEA`) | 0.12 / 0.38 (100) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Oleksandr Ovcharenko / Kai Wehnelt (`KXATPCHALLENGERDOUBLES-26OCT16OVCWEHBIAPEA-OVCWEH`) | 0.06 / 0.83 (65) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Massimo Giunta (`KXATPCHALLENGERMATCH-26OCT16WISGIU-GIU`) | 0.65 / 0.66 (10837) | 65.5% | 38.8% | 33.8% | 36.1% [33.9%-38.4%] | 64.6% | 65.6% | 65.1% | MODEL_LONE_OUTLIER | PASS | -26.7 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Max Wiskandt (`KXATPCHALLENGERMATCH-26OCT16WISGIU-WIS`) | 0.34 / 0.35 (12508) | 34.5% | 61.2% | 66.2% | 63.9% [61.6%-66.1%] | 35.4% | 34.3% | 34.8% | MODEL_LONE_OUTLIER | PASS | +26.7 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

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
| Carlos Alvarez Valdes / Massucco (`KXITFDOUBLES-26OCT16CARMASIFISTA-CARMAS`) | 0.35 / 0.51 (132) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ifi / Stanke (`KXITFDOUBLES-26OCT16CARMASIFISTA-IFISTA`) | 0.41 / 0.58 (5) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jip Van Assendelft vs Petros Tsitsipas -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16VANTSI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Petros Tsitsipas (`KXITFMATCH-26OCT16VANTSI-TSI`) | 0.18 / 0.19 (13858) | 18.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jip Van Assendelft (`KXITFMATCH-26OCT16VANTSI-VAN`) | 0.81 / 0.82 (6089) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lucie Havlickova vs Jil Teichmann -- WTA 125K Rovereto QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-16 19:00Z
* Current expected start: 2026-10-16 16:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-16 15:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Hard · scheduled 2026-10-16T19:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:213525:222980:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucie Havlickova (`KXWTACHALLENGERMATCH-26OCT16HAVTEI-HAV`) | 0.60 / 0.61 (14619) | 60.5% | -- | 69.0% | 61.8% [49.5%-67.1%] | 59.9% | 61.2% | 61.2% | MODEL_LONE_OUTLIER | PASS | +1.3 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Jil Teichmann (`KXWTACHALLENGERMATCH-26OCT16HAVTEI-TEI`) | 0.39 / 0.40 (1510) | 39.5% | -- | 31.1% | 38.2% [32.9%-50.5%] | 40.1% | 39.1% | 39.1% | MODEL_LONE_OUTLIER | PASS | -1.3 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 2440.0, B 2567.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.088
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.020, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Sergio Callejon Hernando vs Luca Castagnola -- M15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-16T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209337:212090:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sergio Callejon Hernando (`KXITFMATCH-26OCT16CALCAS-CAL`) | 0.96 / 0.97 (172) | 96.5% | 63.2% | 67.7% | 58.8% [54.1%-63.9%] | 82.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -33.3 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luca Castagnola (`KXITFMATCH-26OCT16CALCAS-CAS`) | 0.02 / 0.04 (1153) | 3.0% | 36.8% | 32.3% | 41.2% [36.1%-45.9%] | 17.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +33.8 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 632.0, B 439.0; serve-point win A 58.9%, B 43.6%; Elo A 1382.9, B 1336.6; model uncertainty 0.049
* Form inputs: days since last match A 32, B 144; matches on record A 64, B 148; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT16CALCAS-CAS  (YES = Luca Castagnola)
Model: 37%
Kalshi: 3%
Gap: +34 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
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
| Jacob Fearnley (`KXATPCHALLENGERMATCH-26OCT16FEAMRV-FEA`) | 0.73 / 0.74 (11996) | 73.5% | 72.0% | 67.4% | 73.3% [70.6%-76.3%] | 71.1% | 72.8% | 71.9% | MARKETS_AGREE | PASS | -1.4 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Maxim Mrva (`KXATPCHALLENGERMATCH-26OCT16FEAMRV-MRV`) | 0.26 / 0.27 (37110) | 26.5% | 28.0% | 32.6% | 26.7% [23.7%-29.4%] | 28.9% | 27.4% | 28.2% | MARKETS_AGREE | PASS | +1.4 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4058.0, B 3391.0; serve-point win A 58.4%, B 46.0%; Elo A 1871.8, B 1580.7; model uncertainty 0.0281
* Form inputs: days since last match A 18, B 25; matches on record A 178, B 101; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.013, surface_dev_loose -0.022, surface_dev_tight +0.017
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Leonardo Rossi vs Mika Petkovic -- M15 Offenbach SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210223:213001:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mika Petkovic (`KXITFMATCH-26OCT16ROSPET-PET`) | 0.91 / 0.92 (1499) | 91.5% | 55.1% | 51.5% | 45.9% [45.9%-47.4%] | 60.6% | -- | 60.6% | MODEL_LONE_OUTLIER | PASS | -36.4 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Leonardo Rossi (`KXITFMATCH-26OCT16ROSPET-ROS`) | 0.08 / 0.09 (3270) | 8.5% | 44.9% | 48.5% | 54.1% [52.6%-54.1%] | 39.4% | -- | 39.4% | MODEL_LONE_OUTLIER | PASS | +36.4 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 84.0, B 972.0; serve-point win A 60.2%, B 38.8%; Elo A 1368.0, B 1338.0; model uncertainty 0.0077
* Form inputs: days since last match A 53, B 18; matches on record A 132, B 25; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT16ROSPET-ROS  (YES = Leonardo Rossi)
Model: 45%
Kalshi: 8%
Gap: +36 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: SUPPORTS_MODEL_DIRECTION
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, LEVEL_TRANSFER_RISK, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matthias Ujvary vs Alan Wazny -- M15 Bol QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-16T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210745:213048:2026-10-16`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthias Ujvary (`KXITFMATCH-26OCT16UJVWAZ-UJV`) | 0.48 / 0.51 (49) | 49.5% | 50.0% | 29.2% | 44.8% [42.2%-46.9%] | 25.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alan Wazny (`KXITFMATCH-26OCT16UJVWAZ-WAZ`) | 0.49 / 0.52 (1187) | 50.5% | 50.0% | 70.8% | 55.2% [53.1%-57.8%] | 74.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 163.0, B 252.0; serve-point win A 59.0%, B 41.0%; Elo A 1197.2, B 1217.0; model uncertainty 0.0237
* Form inputs: days since last match A 172, B 32; matches on record A 71, B 7; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ivanova / Stankovic vs Elena Barbulescu / Simionescu -- W50 Stara Zagora SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16IVASTAELESIM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elena Barbulescu / Simionescu (`KXITFWDOUBLES-26OCT16IVASTAELESIM-ELESIM`) | 0.05 / 0.74 (1) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ivanova / Stankovic (`KXITFWDOUBLES-26OCT16IVASTAELESIM-IVASTA`) | 0.26 / 0.94 (14) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Karatancheva / Velikova vs Ivanovic / Veleva -- W50 Stara Zagora SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16KARVELIVAVEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ivanovic / Veleva (`KXITFWDOUBLES-26OCT16KARVELIVAVEL-IVAVEL`) | 0.28 / 0.63 (67) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Karatancheva / Velikova (`KXITFWDOUBLES-26OCT16KARVELIVAVEL-KARVEL`) | 0.26 / 0.66 (73) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

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
| Izan Almazan Valiente / Pavel Lagutin (`KXATPCHALLENGERDOUBLES-26OCT16ALMLAGFORLAL-ALMLAG`) | 0.14 / 0.75 (226) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ignasi Forcano Aparicio / Younes Lalami Laaroussi (`KXATPCHALLENGERDOUBLES-26OCT16ALMLAGFORLAL-FORLAL`) | 0.29 / 0.82 (100) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Dahlberg / Marek (`KXITFDOUBLES-26OCT16HRALAKDAHMAR-DAHMAR`) | 0.05 / 0.91 (98) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hrazdil / Lakshmanan (`KXITFDOUBLES-26OCT16HRALAKDAHMAR-HRALAK`) | 0.10 / 0.91 (43) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Krajci / Poritskyy (`KXITFDOUBLES-26OCT16ORLMANKRAPOR-KRAPOR`) | 0.11 / 0.14 (1) | 12.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Orlando Fellin / Manukyan (`KXITFDOUBLES-26OCT16ORLMANKRAPOR-ORLMAN`) | 0.85 / 0.87 (38) | 86.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

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
| Felix Balshaw (`KXATPCHALLENGERMATCH-26OCT16BALBRU-BAL`) | 0.52 / 0.54 (24891) | 53.0% | 55.7% | 58.5% | 58.0% [52.5%-61.0%] | 53.1% | 53.6% | 53.6% | MODEL_LONE_OUTLIER | PASS | +2.7 pp | NORMAL | FRESH | F / POOR | EXTERNAL_STALE | VERIFIED |
| Mika Brunold (`KXATPCHALLENGERMATCH-26OCT16BALBRU-BRU`) | 0.46 / 0.47 (21716) | 46.5% | 44.3% | 41.5% | 42.0% [39.0%-47.5%] | 46.9% | 46.5% | 46.5% | MODEL_LONE_OUTLIER | PASS | -2.2 pp | NORMAL | FRESH | F / POOR | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 1807.0, B 1536.0; serve-point win A 63.2%, B 37.9%; Elo A 1561.1, B 1510.5; model uncertainty 0.0422
* Form inputs: days since last match A 11, B 676; matches on record A 44, B 128; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.025, surface_pool_high +0.025, surface_dev_loose -0.015, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

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
| Francesco Passaro (`KXATPCHALLENGERMATCH-26OCT16TRUPAS-PAS`) | 0.47 / 0.48 (2324) | 47.5% | 53.0% | 49.0% | 47.5% [46.5%-48.5%] | 48.0% | 47.7% | 47.7% | MARKETS_AGREE | PASS | +5.5 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Marco Trungelliti (`KXATPCHALLENGERMATCH-26OCT16TRUPAS-TRU`) | 0.52 / 0.53 (3830) | 52.5% | 47.0% | 51.0% | 52.5% [51.5%-53.5%] | 52.0% | 52.4% | 52.4% | MARKETS_AGREE | PASS | -5.5 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4986.0, B 3936.0; serve-point win A 62.8%, B 36.6%; Elo A 1774.7, B 1730.9; model uncertainty 0.01
* Form inputs: days since last match A 9, B 11; matches on record A 985, B 355; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

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
| Belibova / Gamretkaia (`KXITFWDOUBLES-26OCT16BELGAMJOVKRO-BELGAM`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jovanovic / Kroitor (`KXITFWDOUBLES-26OCT16BELGAMJOVKRO-JOVKRO`) | -- / 0.01 (679) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE

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
| Agureeva / Dorofeeva-Rybas (`KXITFWDOUBLES-26OCT16BIRWANAGUDOR-AGUDOR`) | 0.56 / 0.57 (20) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Biro / Wanja Brune Olsen (`KXITFWDOUBLES-26OCT16BIRWANAGUDOR-BIRWAN`) | 0.44 / 0.45 (22) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

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
| Manon Leonard (`KXITFWMATCH-26OCT16LEOPON-LEO`) | 0.19 / 0.20 (14294) | 19.5% | -- | 40.7% | 34.3% [28.1%-37.7%] | 43.0% | -- | 43.0% | MODEL_LONE_OUTLIER | PASS | +14.8 pp | REVIEW | FRESH | A / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Jessika Ponchet (`KXITFWMATCH-26OCT16LEOPON-PON`) | 0.80 / 0.81 (6668) | 80.5% | -- | 59.3% | 65.7% [62.3%-71.9%] | 57.0% | -- | 57.0% | KALSHI_LONE_OUTLIER | WATCH | -14.8 pp | REVIEW | FRESH | A / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

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
| Alicia Dudeney (`KXITFWMATCH-26OCT16STODUD-DUD`) | 0.66 / 0.67 (4063) | 66.5% | -- | 78.7% | 68.1% [55.3%-73.4%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +1.6 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mika Stojsavljevic (`KXITFWMATCH-26OCT16STODUD-STO`) | 0.33 / 0.34 (3785) | 33.5% | -- | 21.3% | 31.9% [26.6%-44.7%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.6 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2019.0, B 3238.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0908
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bianca Andreescu vs Lucrezia Stefanini -- WTA 125K Rovereto QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-16 20:30Z
* Current expected start: 2026-10-16 17:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-16 16:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-16T20:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT16ANDSTE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bianca Andreescu (`KXWTACHALLENGERMATCH-26OCT16ANDSTE-AND`) | 0.58 / 0.59 (9442) | 58.5% | -- | -- | -- [-----] | 58.4% | 57.2% | 57.8% | MARKETS_AGREE | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lucrezia Stefanini (`KXWTACHALLENGERMATCH-26OCT16ANDSTE-STE`) | 0.41 / 0.43 (7178) | 42.0% | -- | -- | -- [-----] | 41.6% | 42.8% | 42.2% | MARKETS_AGREE | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Agwi / Vega (`KXITFDOUBLES-26OCT16AGWVEGHOFMUE-AGWVEG`) | 0.11 / 0.65 (10) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hoffmann / Mueller (`KXITFDOUBLES-26OCT16AGWVEGHOFMUE-HOFMUE`) | 0.13 / 0.45 (45) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Bajurko / Motta (`KXITFDOUBLES-26OCT16BERDOMBAJMOT-BAJMOT`) | 0.40 / 0.47 (309) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bernardo / Domingos (`KXITFDOUBLES-26OCT16BERDOMBAJMOT-BERDOM`) | 0.53 / 0.58 (20) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

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
| Gianluca Cadenasso (`KXATPCHALLENGERMATCH-26OCT16CADMOE-CAD`) | 0.47 / 0.48 (15315) | 47.5% | 41.6% | 42.7% | 40.7% [39.7%-41.7%] | 48.0% | 46.6% | 46.6% | MODEL_LONE_OUTLIER | PASS | -5.9 pp | NORMAL | FRESH | A / LIMITED | EXTERNAL_STALE | VERIFIED |
| Marvin Moeller (`KXATPCHALLENGERMATCH-26OCT16CADMOE-MOE`) | 0.52 / 0.54 (15219) | 53.0% | 58.4% | 57.3% | 59.3% [58.3%-60.3%] | 52.0% | 53.6% | 53.6% | MODEL_LONE_OUTLIER | SHADOW_BET | +5.4 pp | NORMAL | FRESH | A / LIMITED | EXTERNAL_STALE | VERIFIED |

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
| Juhas / Popovic (`KXITFDOUBLES-26OCT16MASRADJUHPOP-JUHPOP`) | 0.61 / 0.66 (42) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mashtakov / Radjenovic (`KXITFDOUBLES-26OCT16MASRADJUHPOP-MASRAD`) | 0.35 / 0.37 (45) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

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
| Michael Mmoh (`KXATPCHALLENGERMATCH-26OCT16MMONAR-MMO`) | 0.54 / 0.55 (1439) | 54.5% | 41.5% | 51.5% | 44.8% [41.8%-47.4%] | 54.1% | 54.7% | 54.7% | MODEL_LONE_OUTLIER | PASS | -13.0 pp | REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Luca Nardi (`KXATPCHALLENGERMATCH-26OCT16MMONAR-NAR`) | 0.44 / 0.45 (97) | 44.5% | 58.5% | 48.4% | 55.2% [52.6%-58.2%] | 45.9% | 45.1% | 45.1% | MODEL_LONE_OUTLIER | SHADOW_BET | +14.0 pp | REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 2931.0, B 3056.0; serve-point win A 58.7%, B 39.7%; Elo A 1529.5, B 1659.3; model uncertainty 0.0282
* Form inputs: days since last match A 18, B 11; matches on record A 552, B 346; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.026, surface_pool_high -0.026, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Andronicou / Eleni Poulka vs Fehr / Kryvoruchko -- W35 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16ANDELEFEHKRY:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andronicou / Eleni Poulka (`KXITFWDOUBLES-26OCT16ANDELEFEHKRY-ANDELE`) | 0.02 / 0.98 (12) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fehr / Kryvoruchko (`KXITFWDOUBLES-26OCT16ANDELEFEHKRY-FEHKRY`) | 0.01 / 0.99 (561) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

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
| Breaz / Georgiana Goina (`KXITFWDOUBLES-26OCT16BREGEOSABSTA-BREGEO`) | 0.85 / 0.86 (502) | 85.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sabadi / Stabauer (`KXITFWDOUBLES-26OCT16BREGEOSABSTA-SABSTA`) | 0.14 / 0.15 (26) | 14.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Alisa Oktiabreva vs Maria Herazo -- W35 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16OKTHER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Herazo (`KXITFWMATCH-26OCT16OKTHER-HER`) | 0.06 / 0.10 (1534) | 8.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alisa Oktiabreva (`KXITFWMATCH-26OCT16OKTHER-OKT`) | 0.90 / 0.93 (54) | 91.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alice Tubello vs Elena Korokozidi -- W35 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16TUBKOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elena Korokozidi (`KXITFWMATCH-26OCT16TUBKOR-KOR`) | 0.27 / 0.28 (5) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alice Tubello (`KXITFWMATCH-26OCT16TUBKOR-TUB`) | 0.70 / 0.73 (2363) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

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
| Tristan Boyer (`KXATPCHALLENGERMATCH-26OCT16DODBOY-BOY`) | 0.32 / 0.34 (3909) | 33.0% | 35.1% | 28.6% | 32.1% [28.6%-38.6%] | 34.3% | 33.4% | 33.8% | MODEL_LONE_OUTLIER | PASS | +2.1 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Matej Dodig (`KXATPCHALLENGERMATCH-26OCT16DODBOY-DOD`) | 0.66 / 0.67 (6375) | 66.5% | 64.9% | 71.4% | 67.9% [61.4%-71.4%] | 65.7% | 66.7% | 66.2% | MODEL_LONE_OUTLIER | PASS | -1.6 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3779.0, B 2991.0; serve-point win A 64.8%, B 38.3%; Elo A 1738.9, B 1659.4; model uncertainty 0.05
* Form inputs: days since last match A 11, B 11; matches on record A 215, B 220; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.027, surface_pool_high +0.026, surface_dev_loose +0.018, surface_dev_tight -0.018
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Alhussein Abdel Aziz / Ibrahim vs Sacco / Vaissaud -- W15 Sharm ElSheikh SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 18:15Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T18:15:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16ALHIBRSACVAI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alhussein Abdel Aziz / Ibrahim (`KXITFWDOUBLES-26OCT16ALHIBRSACVAI-ALHIBR`) | 0.01 / 0.74 (1) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sacco / Vaissaud (`KXITFWDOUBLES-26OCT16ALHIBRSACVAI-SACVAI`) | 0.01 / 0.74 (1) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Arce Fernandez / Peiro Serrano (`KXITFDOUBLES-26OCT16FRERIVARCPEI-ARCPEI`) | 0.22 / 0.40 (100) | 31.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
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
| Nagoudi / Piatti (`KXITFDOUBLES-26OCT16NAGPIANIRVAN-NAGPIA`) | 0.48 / 0.51 (51) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nirundorn / van Wyk (`KXITFDOUBLES-26OCT16NAGPIANIRVAN-NIRVAN`) | 0.12 / 0.52 (5) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Barrera Aguirre / Zhu (`KXITFWDOUBLES-26OCT16BARZHUKRELEM-BARZHU`) | 0.08 / 0.41 (42) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Krejcova / Lemaitre (`KXITFWDOUBLES-26OCT16BARZHUKRELEM-KRELEM`) | 0.57 / 0.70 (109) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Gniewkowska / Villet (`KXITFWDOUBLES-26OCT16KUZMILGNIVIL-GNIVIL`) | 0.09 / 0.25 (100) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kuzmova / Milovanovic (`KXITFWDOUBLES-26OCT16KUZMILGNIVIL-KUZMIL`) | 0.26 / 0.85 (166) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Maria Sara Popa vs Tilwith Di Girolami -- W35 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16POPDIG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tilwith Di Girolami (`KXITFWMATCH-26OCT16POPDIG-DIG`) | 0.08 / 0.91 (29) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maria Sara Popa (`KXITFWMATCH-26OCT16POPDIG-POP`) | 0.02 / 0.92 (29) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

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
| Luna Maria Cinalli (`KXITFWMATCH-26OCT16KONCIN-CIN`) | 0.87 / 0.88 (60) | 87.5% | -- | 75.3% | 72.7% [71.3%-75.3%] | 86.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -14.8 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Julia Konishi Camargo Silva (`KXITFWMATCH-26OCT16KONCIN-KON`) | 0.13 / 0.14 (14691) | 13.5% | -- | 24.7% | 27.3% [24.7%-28.7%] | 13.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +13.8 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

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
| Ana Sofia Sanchez (`KXITFWMATCH-26OCT16SANSOU-SAN`) | 0.82 / 0.84 (8092) | 83.0% | -- | 75.3% | 86.2% [83.7%-88.1%] | 82.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.2 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marjorie Souza (`KXITFWMATCH-26OCT16SANSOU-SOU`) | 0.16 / 0.17 (30) | 16.5% | -- | 24.6% | 13.8% [11.9%-16.4%] | 17.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

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
| Nicolai Budkov Kjaer (`KXATPCHALLENGERMATCH-26OCT16GASBUD-BUD`) | 0.44 / 0.45 (4932) | 44.5% | -- | 46.5% | 44.5% [39.0%-47.0%] | 44.6% | 44.7% | 44.7% | MODEL_LONE_OUTLIER | PASS | -0.0 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Hugo Gaston (`KXATPCHALLENGERMATCH-26OCT16GASBUD-GAS`) | 0.55 / 0.56 (10259) | 55.5% | -- | 53.5% | 55.5% [53.0%-61.0%] | 55.4% | 55.1% | 55.1% | MODEL_LONE_OUTLIER | PASS | +0.0 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4582.0, B 3085.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0397
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.030, surface_pool_high -0.020, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Astrid Lew Yan Foon vs Elena Ruxandra Bertea -- W35 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-16T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16LEWBER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elena Ruxandra Bertea (`KXITFWMATCH-26OCT16LEWBER-BER`) | 0.02 / 0.98 (85) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Astrid Lew Yan Foon (`KXITFWMATCH-26OCT16LEWBER-LEW`) | 0.02 / 0.98 (85) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

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
| Pedro Henrique Chabalgoity (`KXITFMATCH-26OCT16CHATOS-CHA`) | 0.41 / 0.43 (138) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
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
| Josefina Estevez (`KXITFWMATCH-26OCT16ESTLAB-EST`) | 0.31 / 0.32 (36) | 31.5% | -- | 18.1% | 21.8% [19.1%-24.3%] | 34.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Fernanda Labrana (`KXITFWMATCH-26OCT16ESTLAB-LAB`) | 0.67 / 0.68 (37) | 67.5% | -- | 81.9% | 78.2% [75.7%-80.9%] | 65.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +10.7 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

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
| Barbara Gatica (`KXITFWMATCH-26OCT16GATURR-GAT`) | 0.46 / 0.48 (97) | 47.0% | -- | 37.4% | 61.1% [55.9%-70.4%] | -- | -- | -- | -- | PASS | +14.1 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Maria Florencia Urrutia (`KXITFWMATCH-26OCT16GATURR-URR`) | 0.51 / 0.52 (0) | 51.5% | -- | 62.6% | 38.9% [29.6%-44.1%] | -- | -- | -- | -- | PASS | -12.6 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 633.0, B 2454.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0727
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Sascha Gueymard Wayenburg (`KXATPCHALLENGERMATCH-26OCT16MARGUE-GUE`) | 0.69 / 0.70 (50) | 69.5% | -- | -- | -- [-----] | 67.7% | 70.0% | 68.8% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matteo Martineau (`KXATPCHALLENGERMATCH-26OCT16MARGUE-MAR`) | 0.29 / 0.31 (12220) | 30.0% | -- | -- | -- [-----] | 32.3% | 29.9% | 31.1% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

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
| Francisco Comesana (`KXATPCHALLENGERMATCH-26OCT16COMOLI-COM`) | 0.82 / 0.83 (12683) | 82.5% | -- | -- | -- [-----] | 80.3% | 82.7% | 81.5% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Genaro Alberto Olivieri (`KXATPCHALLENGERMATCH-26OCT16COMOLI-OLI`) | 0.17 / 0.18 (39) | 17.5% | -- | -- | -- [-----] | 19.7% | 17.9% | 18.8% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Oscar Jose Gutierrez (`KXITFMATCH-26OCT16GUTSCH-GUT`) | 0.35 / 0.38 (32) | 36.5% | 25.6% | 38.8% | 38.3% [36.8%-39.8%] | 39.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -10.9 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Joao Eduardo Schiessl (`KXITFMATCH-26OCT16GUTSCH-SCH`) | 0.61 / 0.63 (67) | 62.0% | 74.4% | 61.2% | 61.7% [60.2%-63.2%] | 60.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +12.4 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

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
| Nicolas Bruna (`KXITFMATCH-26OCT16SAKBRU-BRU`) | 0.10 / 0.12 (7776) | 11.0% | 12.6% | 21.7% | 11.5% [10.1%-12.5%] | 13.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pedro Sakamoto (`KXITFMATCH-26OCT16SAKBRU-SAK`) | 0.88 / 0.89 (2) | 88.5% | 87.5% | 78.3% | 88.5% [87.5%-89.9%] | 86.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

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
| Lucas Andrade Da Silva (`KXITFMATCH-26OCT16ANDGOM-AND`) | 0.88 / 0.89 (12755) | 88.5% | 63.0% | 76.2% | 56.7% [52.0%-62.7%] | 83.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -25.5 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Juan Sebastian Gomez (`KXITFMATCH-26OCT16ANDGOM-GOM`) | 0.11 / 0.13 (6810) | 12.0% | 37.0% | 23.8% | 43.3% [37.3%-47.9%] | 16.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +25.0 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 387.0, B 933.0; serve-point win A 61.0%, B 41.5%; Elo A 1401.0, B 1391.0; model uncertainty 0.0534
* Form inputs: days since last match A 18, B 102; matches on record A 10, B 466; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT16ANDGOM-GOM  (YES = Juan Sebastian Gomez)
Model: 37%
Kalshi: 12%
Gap: +25 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
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
| Jack Anthrop (`KXITFMATCH-26OCT16BASANT-ANT`) | 0.81 / 0.84 (6454) | 82.5% | 79.5% | 54.5% | 70.9% [70.0%-71.2%] | 82.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pepijn Bastiaansen (`KXITFMATCH-26OCT16BASANT-BAS`) | 0.15 / 0.17 (399) | 16.0% | 20.5% | 45.5% | 29.1% [28.8%-30.0%] | 17.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

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
| Julian Cundom (`KXITFMATCH-26OCT16ESCCUN-CUN`) | 0.41 / 0.44 (21) | 42.5% | 49.6% | 56.1% | 46.9% [45.9%-46.9%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.1 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hernando Jose Escurra Isnardi (`KXITFMATCH-26OCT16ESCCUN-ESC`) | 0.55 / 0.57 (3) | 56.0% | 50.4% | 43.9% | 53.0% [53.0%-54.1%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.6 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 342.0, B 87.0; serve-point win A 61.7%, B 38.4%; Elo A 1211.6, B 1183.1; model uncertainty 0.0051
* Form inputs: days since last match A 27, B 130; matches on record A 54, B 29; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
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
| Mwendwa Mbithi (`KXITFMATCH-26OCT16MBISAL-MBI`) | 0.38 / 0.40 (13) | 39.0% | 43.4% | 35.9% | 54.1% [53.1%-55.1%] | 39.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Daniel Salazar (`KXITFMATCH-26OCT16MBISAL-SAL`) | 0.58 / 0.61 (316) | 59.5% | 56.6% | 64.1% | 45.9% [44.9%-46.9%] | 60.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 166.0; serve-point win A 60.0%, B 38.8%; Elo A 1277.7, B 1249.2; model uncertainty 0.0102
* Form inputs: days since last match A 676, B 207; matches on record A 130, B 41; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
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
| Johan Oscar Lien (`KXITFMATCH-26OCT16PAPLIE-LIE`) | 0.21 / 0.23 (6342) | 22.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Theo Papamalamis (`KXITFMATCH-26OCT16PAPLIE-PAP`) | 0.76 / 0.78 (13) | 77.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Felix Corwin (`KXITFMATCH-26OCT16SLACOR-COR`) | 0.62 / 0.64 (13) | 63.0% | 82.1% | 66.1% | 74.4% [74.0%-75.5%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +19.1 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nikola Slavic (`KXITFMATCH-26OCT16SLACOR-SLA`) | 0.35 / 0.37 (21) | 36.0% | 17.9% | 33.9% | 25.6% [24.5%-26.1%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -18.1 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 99.0, B 760.0; serve-point win A 59.5%, B 33.2%; Elo A 1251.3, B 1441.2; model uncertainty 0.0076
* Form inputs: days since last match A 96, B 207; matches on record A 17, B 313; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT16SLACOR-COR  (YES = Felix Corwin)
Model: 82%
Kalshi: 63%
Gap: +19 pp
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
| Eli Stephenson (`KXITFMATCH-26OCT16STEZAM-STE`) | 0.26 / 0.28 (8638) | 27.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Noah Zamora (`KXITFMATCH-26OCT16STEZAM-ZAM`) | 0.72 / 0.73 (174) | 72.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Ayana Akli (`KXITFWMATCH-26OCT16AKLARS-AKL`) | 0.61 / 0.62 (363) | 61.5% | -- | 54.2% | 59.5% [57.4%-63.5%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ariana Arseneault (`KXITFWMATCH-26OCT16AKLARS-ARS`) | 0.38 / 0.40 (400) | 39.0% | -- | 45.8% | 40.6% [36.5%-42.6%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2838.0, B 2049.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0308
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
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
| Hugo Dellien (`KXATPCHALLENGERMATCH-26OCT16MIGDEL-DEL`) | 0.66 / 0.68 (11946) | 67.0% | -- | -- | -- [-----] | 65.7% | 67.4% | 66.5% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luis Guto Miguel (`KXATPCHALLENGERMATCH-26OCT16MIGDEL-MIG`) | 0.32 / 0.33 (35) | 32.5% | -- | -- | -- [-----] | 34.3% | 32.7% | 33.5% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

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
| Ayala / Romero (`KXITFWDOUBLES-26OCT16AYAROMKRASOU-AYAROM`) | 0.05 / 0.90 (53) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Krajmer / Souza (`KXITFWDOUBLES-26OCT16AYAROMKRASOU-KRASOU`) | 0.10 / 0.23 (10) | 16.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Juan Manuel La Serna (`KXATPCHALLENGERMATCH-26OCT16LARON-LA`) | 0.48 / 0.49 (2879) | 48.5% | -- | -- | -- [-----] | 48.0% | 48.8% | 48.8% | MARKETS_AGREE | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Franco Roncadelli (`KXATPCHALLENGERMATCH-26OCT16LARON-RON`) | 0.51 / 0.52 (2434) | 51.5% | -- | -- | -- [-----] | 52.0% | 50.7% | 50.7% | MARKETS_AGREE | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

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
| Andrew Fenty (`KXITFMATCH-26OCT16MAXFEN-FEN`) | 0.40 / 0.43 (8244) | 41.5% | 53.6% | 42.4% | 48.0% [46.0%-49.0%] | 40.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +12.1 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lui Maxted (`KXITFMATCH-26OCT16MAXFEN-MAX`) | 0.58 / 0.60 (449) | 59.0% | 46.4% | 57.6% | 52.0% [51.0%-54.0%] | 59.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.6 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

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
| Cosme Rolland de Ravel (`KXITFMATCH-26OCT16WILROL-ROL`) | 0.51 / 0.53 (399) | 52.0% | 61.1% | 61.1% | 65.5% [64.5%-66.5%] | 53.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +9.1 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Benjamin Willwerth (`KXITFMATCH-26OCT16WILROL-WIL`) | 0.45 / 0.47 (342) | 46.0% | 38.9% | 38.9% | 34.5% [33.5%-35.5%] | 46.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.1 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 352.0, B 473.0; serve-point win A 59.7%, B 38.1%; Elo A 1342.8, B 1459.5; model uncertainty 0.0098
* Form inputs: days since last match A 53, B 109; matches on record A 11, B 7; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.009, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
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
| Reese Brantmeier (`KXITFWMATCH-26OCT16GOWBRA-BRA`) | 0.92 / 0.94 (508) | 93.0% | -- | 25.0% | 72.0% [61.9%-78.8%] | 92.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -21.0 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Thara Gowda (`KXITFWMATCH-26OCT16GOWBRA-GOW`) | 0.06 / 0.08 (4475) | 7.0% | -- | 75.0% | 28.0% [21.2%-38.1%] | 7.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +21.0 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

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
| Nicolas Kicker (`KXATPCHALLENGERMATCH-26OCT16SEYKIC-KIC`) | 0.14 / 0.15 (1135) | 14.5% | -- | -- | -- [-----] | 16.4% | 15.6% | 15.6% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Thiago Seyboth Wild (`KXATPCHALLENGERMATCH-26OCT16SEYKIC-SEY`) | 0.84 / 0.86 (14577) | 85.0% | -- | -- | -- [-----] | 83.6% | 85.5% | 85.5% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

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
| Ivan Dreycopp (`KXITFMATCH-26OCT16HERDRE-DRE`) | 0.28 / 0.30 (248) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alex Hernandez (`KXITFMATCH-26OCT16HERDRE-HER`) | 0.70 / 0.72 (6958) | 71.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
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
| Tristan McCormick (`KXITFMATCH-26OCT16OSOMCC-MCC`) | 0.59 / 0.61 (16) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Juan Sebastian Osorio (`KXITFMATCH-26OCT16OSOMCC-OSO`) | 0.37 / 0.40 (62) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Yuki Naito (`KXITFWMATCH-26OCT16NAIXUX-NAI`) | 0.42 / 0.46 (7063) | 44.0% | -- | 53.2% | 44.2% [39.5%-47.9%] | 43.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.2 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Mimi Xu (`KXITFWMATCH-26OCT16NAIXUX-XUX`) | 0.53 / 0.54 (1323) | 53.5% | -- | 46.8% | 55.8% [52.1%-60.5%] | 56.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.3 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 2186.0, B 1841.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0418
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.037, surface_pool_high -0.031, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
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
| Fuchs / Hopper (`KXITFDOUBLES-26OCT16FUCHOPRODTOK-FUCHOP`) | 0.08 / 0.66 (0) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Roddick / Tokac (`KXITFDOUBLES-26OCT16FUCHOPRODTOK-RODTOK`) | 0.34 / 0.53 (81) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Dominick Mosejczuk (`KXITFMATCH-26OCT16URRMOS-MOS`) | 0.75 / 0.78 (28) | 76.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Iker Urribarrens Ramirez (`KXITFMATCH-26OCT16URRMOS-URR`) | 0.21 / 0.24 (6443) | 22.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Gatica / Pereira (`KXITFWDOUBLES-26OCT16MEDSOFGATPER-GATPER`) | 0.08 / 0.75 (100) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mediorreal Arias / Sofia Sanchez (`KXITFWDOUBLES-26OCT16MEDSOFGATPER-MEDSOF`) | 0.12 / 0.39 (40) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Kajsa Rinaldo Persson (`KXITFWMATCH-26OCT16RINSAI-RIN`) | 0.61 / 0.65 (6101) | 63.0% | -- | 71.3% | 64.6% [58.5%-67.5%] | -- | -- | -- | -- | PASS | +1.6 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sara Saito (`KXITFWMATCH-26OCT16RINSAI-SAI`) | 0.35 / 0.37 (570) | 36.0% | -- | 28.7% | 35.4% [32.5%-41.5%] | -- | -- | -- | -- | PASS | -0.6 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3104.0, B 3341.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0452
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose +0.010, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Diego Hidalgo / Mariano Kestelboim vs Hernan Casanova / Santiago Rodriguez Taverna -- ATP Challenger Santa Cruz 2 SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 00:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-17T00:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16HIDKESCASROD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hernan Casanova / Santiago Rodriguez Taverna (`KXATPCHALLENGERDOUBLES-26OCT16HIDKESCASROD-CASROD`) | 0.25 / 0.40 (25) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Diego Hidalgo / Mariano Kestelboim (`KXATPCHALLENGERDOUBLES-26OCT16HIDKESCASROD-HIDKES`) | 0.60 / 0.75 (25) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Boris Arias / Ignacio Carou vs Luis Guto Miguel / Eduardo Ribeiro -- ATP Challenger Santa Cruz 2 SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 00:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-17T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16ARICARMIGRIB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Boris Arias / Ignacio Carou (`KXATPCHALLENGERDOUBLES-26OCT16ARICARMIGRIB-ARICAR`) | 0.21 / 0.37 (57) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luis Guto Miguel / Eduardo Ribeiro (`KXATPCHALLENGERDOUBLES-26OCT16ARICARMIGRIB-MIGRIB`) | 0.63 / 0.79 (120) | 71.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

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
| Inoue / Naito (`KXITFWDOUBLES-26OCT16INONAIBRAXUX-INONAI`) | 0.08 / 0.37 (39) | 22.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Alvarado / Mbithi (`KXITFDOUBLES-26OCT16ALVMBICOVVOE-ALVMBI`) | 0.11 / 0.59 (60) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Covato / Voelzke (`KXITFDOUBLES-26OCT16ALVMBICOVVOE-COVVOE`) | 0.37 / 0.55 (55) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Del Pino / Mouilleron Salvo (`KXITFDOUBLES-26OCT16DELMOUSEBURR-DELMOU`) | 0.08 / 0.47 (47) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sebastian Gomez / Urrea (`KXITFDOUBLES-26OCT16DELMOUSEBURR-SEBURR`) | 0.08 / 0.67 (75) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-17 01:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T05:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT16ISHAVA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elina Avanesyan (`KXWTAMATCH-26OCT16ISHAVA-AVA`) | 0.78 / 0.81 (6901) | 79.5% | -- | -- | -- [-----] | -- | 80.8% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sayaka Ishii (`KXWTAMATCH-26OCT16ISHAVA-ISH`) | 0.20 / 0.22 (491) | 21.0% | -- | -- | -- [-----] | -- | 18.9% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Maya Joint vs Kyoka Okamura -- WTA Osaka Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 05:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 02:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-17 01:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T05:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT16JOIOKA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maya Joint (`KXWTAMATCH-26OCT16JOIOKA-JOI`) | 0.77 / 0.79 (5703) | 78.0% | -- | -- | -- [-----] | -- | 75.9% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kyoka Okamura (`KXWTAMATCH-26OCT16JOIOKA-OKA`) | 0.21 / 0.24 (5451) | 22.5% | -- | -- | -- [-----] | -- | 23.9% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ena Koike vs Kayla Day -- WTA Osaka Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 05:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 02:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-17 01:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T05:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT16KOIDAY:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kayla Day (`KXWTAMATCH-26OCT16KOIDAY-DAY`) | 0.82 / 0.83 (83) | 82.5% | -- | -- | -- [-----] | -- | 82.1% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ena Koike (`KXWTAMATCH-26OCT16KOIDAY-KOI`) | 0.15 / 0.18 (6162) | 16.5% | -- | -- | -- [-----] | -- | 17.7% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mary Stoiana vs Rinko Matsuda -- WTA Osaka Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 05:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 02:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-17 01:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T05:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT16STOMAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rinko Matsuda (`KXWTAMATCH-26OCT16STOMAT-MAT`) | 0.09 / 0.11 (5208) | 10.0% | -- | -- | -- [-----] | -- | 8.9% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mary Stoiana (`KXWTAMATCH-26OCT16STOMAT-STO`) | 0.89 / 0.91 (321) | 90.0% | -- | -- | -- [-----] | -- | 88.9% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Katarzyna Kawa vs Katie Volynets -- WTA Ningbo Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 03:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-17 02:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT16KAWVOL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katarzyna Kawa (`KXWTAMATCH-26OCT16KAWVOL-KAW`) | 0.09 / 0.10 (757) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Katie Volynets (`KXWTAMATCH-26OCT16KAWVOL-VOL`) | 0.89 / 0.90 (8) | 89.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Daria Snigur vs Yu Jun Lin -- WTA Ningbo Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 03:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-17 02:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT16SNILIN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yu Jun Lin (`KXWTAMATCH-26OCT16SNILIN-LIN`) | 0.08 / 0.77 (200) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daria Snigur (`KXWTAMATCH-26OCT16SNILIN-SNI`) | 0.33 / 0.93 (200) | 63.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Yuliia Starodubtseva vs Anastasia Zakharova -- WTA Ningbo Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 03:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-17 02:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT16STAZAK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuliia Starodubtseva (`KXWTAMATCH-26OCT16STAZAK-STA`) | 0.55 / 0.57 (3) | 56.0% | -- | -- | -- [-----] | -- | 55.4% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anastasia Zakharova (`KXWTAMATCH-26OCT16STAZAK-ZAK`) | 0.43 / 0.45 (348) | 44.0% | -- | -- | -- [-----] | -- | 44.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Harriet Dart vs Rina Saigo -- WTA Osaka Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 06:40Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 04:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-17 03:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T06:40:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT16DARSAI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Harriet Dart (`KXWTAMATCH-26OCT16DARSAI-DAR`) | 0.85 / 0.86 (98) | 85.5% | -- | -- | -- [-----] | -- | 86.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rina Saigo (`KXWTAMATCH-26OCT16DARSAI-SAI`) | 0.12 / 0.14 (5649) | 13.0% | -- | -- | -- [-----] | -- | 12.5% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Aoi Ito vs Tyra Caterina Grant -- WTA Osaka Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 06:40Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 04:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-17 03:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T06:40:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT16ITOGRA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tyra Caterina Grant (`KXWTAMATCH-26OCT16ITOGRA-GRA`) | 0.53 / 0.56 (6503) | 54.5% | -- | -- | -- [-----] | -- | 55.4% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aoi Ito (`KXWTAMATCH-26OCT16ITOGRA-ITO`) | 0.44 / 0.47 (5503) | 45.5% | -- | -- | -- [-----] | -- | 44.5% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sinja Kraus vs Momoko Kobori -- WTA Osaka Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 06:40Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 04:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-17 03:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T06:40:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT16KRAKOB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Momoko Kobori (`KXWTAMATCH-26OCT16KRAKOB-KOB`) | 0.09 / 0.12 (6543) | 10.5% | -- | -- | -- [-----] | -- | 9.1% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sinja Kraus (`KXWTAMATCH-26OCT16KRAKOB-KRA`) | 0.88 / 0.90 (106) | 89.0% | -- | -- | -- [-----] | -- | 88.9% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; WIDE_SPREAD

## Claire Liu vs Kanon Sawashiro -- WTA Osaka Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 06:40Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 04:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-17 03:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T06:40:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT16LIUSAW:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Claire Liu (`KXWTAMATCH-26OCT16LIUSAW-LIU`) | 0.92 / 0.93 (197) | 92.5% | -- | -- | -- [-----] | -- | 92.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kanon Sawashiro (`KXWTAMATCH-26OCT16LIUSAW-SAW`) | 0.06 / 0.07 (680) | 6.5% | -- | -- | -- [-----] | -- | 5.9% | 5.9% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Debru / Marionneau (`KXITFDOUBLES-26OCT16DEBMARPOLVAN-DEBMAR`) | 0.08 / 0.64 (69) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Poling / Vance (`KXITFDOUBLES-26OCT16DEBMARPOLVAN-POLVAN`) | 0.26 / 0.55 (55) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Sebastian Gorzny (`KXITFMATCH-26OCT16GRAGOR-GOR`) | 0.60 / 0.61 (38) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alastair Gray (`KXITFMATCH-26OCT16GRAGOR-GRA`) | 0.36 / 0.40 (6151) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
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
| Abe / Yoshioka (`KXITFWDOUBLES-26OCT16ARSLACABEYOS-ABEYOS`) | 0.08 / 0.61 (64) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arseneault / Lacasse (`KXITFWDOUBLES-26OCT16ARSLACABEYOS-ARSLAC`) | 0.08 / 0.59 (60) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Salma Drugdova (`KXITFWMATCH-26OCT16DRUMAX-DRU`) | 0.08 / 0.12 (58) | 10.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lea Ma (`KXITFWMATCH-26OCT16DRUMAX-MAX`) | 0.86 / 0.90 (724) | 88.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Connie Ma (`KXITFWMATCH-26OCT16SHOMAX-MAX`) | 0.73 / 0.79 (6487) | 76.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maria Sholokhova (`KXITFWMATCH-26OCT16SHOMAX-SHO`) | 0.21 / 0.26 (58) | 23.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Nao Nishino (`KXITFWMATCH-26OCT16WOLNIS-NIS`) | 0.33 / 0.35 (15) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vivian Wolff (`KXITFWMATCH-26OCT16WOLNIS-WOL`) | 0.64 / 0.66 (212) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Polina Kudermetova vs Mananchaya Sawangkaew -- WTA Ningbo Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 04:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-17 03:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT16KUDSAW:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Kudermetova (`KXWTAMATCH-26OCT16KUDSAW-KUD`) | 0.47 / 0.49 (9) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mananchaya Sawangkaew (`KXWTAMATCH-26OCT16KUDSAW-SAW`) | 0.50 / 0.54 (141) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alycia Parks vs Jeline Vandromme -- WTA Ningbo Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 04:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-17 03:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT16PARVAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alycia Parks (`KXWTAMATCH-26OCT16PARVAN-PAR`) | 0.35 / 0.38 (806) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jeline Vandromme (`KXWTAMATCH-26OCT16PARVAN-VAN`) | 0.62 / 0.65 (106) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Yihan Qu vs Yulia Putintseva -- WTA Ningbo Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 04:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-17 03:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT16YIHPUT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yulia Putintseva (`KXWTAMATCH-26OCT16YIHPUT-PUT`) | 0.91 / 0.93 (421) | 92.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yihan Qu (`KXWTAMATCH-26OCT16YIHPUT-YIH`) | 0.07 / 0.08 (1) | 7.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Taylah Preston vs Haruka Kaji -- WTA Osaka Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 07:50Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 05:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-17 04:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T07:50:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT17PREKAJ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Haruka Kaji (`KXWTAMATCH-26OCT17PREKAJ-KAJ`) | 0.19 / 0.22 (8764) | 20.5% | -- | -- | -- [-----] | -- | 21.1% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Taylah Preston (`KXWTAMATCH-26OCT17PREKAJ-PRE`) | 0.80 / 0.81 (5685) | 80.5% | -- | -- | -- [-----] | -- | 80.0% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sara Sorribes Tormo vs Maddison Inglis -- WTA Osaka Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 07:50Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 05:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-17 04:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T07:50:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT17SORING:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maddison Inglis (`KXWTAMATCH-26OCT17SORING-ING`) | 0.46 / 0.49 (141) | 47.5% | -- | -- | -- [-----] | -- | 47.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sara Sorribes Tormo (`KXWTAMATCH-26OCT17SORING-SOR`) | 0.51 / 0.54 (5568) | 52.5% | -- | -- | -- [-----] | -- | 52.2% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Heather Watson vs Emerson Jones -- WTA Osaka Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 07:50Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 05:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-17 04:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T07:50:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT17WATJON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emerson Jones (`KXWTAMATCH-26OCT17WATJON-JON`) | 0.70 / 0.73 (101) | 71.5% | -- | -- | -- [-----] | -- | 66.3% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Heather Watson (`KXWTAMATCH-26OCT17WATJON-WAT`) | 0.27 / 0.30 (5648) | 28.5% | -- | -- | -- [-----] | -- | 33.7% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jakob Schnaitter / Mark Wallner vs Lucas Miedler / Neil Oberleitner -- ATP Shanghai SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 07:00Z
* Current expected start: 2026-10-17 06:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-17 05:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-17T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT17SCHWALMIEOBE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucas Miedler / Neil Oberleitner (`KXATPDOUBLES-26OCT17SCHWALMIEOBE-MIEOBE`) | 0.65 / 0.67 (10) | 66.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jakob Schnaitter / Mark Wallner (`KXATPDOUBLES-26OCT17SCHWALMIEOBE-SCHWAL`) | 0.32 / 0.35 (1182) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Jiali Dong vs Alina Korneeva -- WTA Ningbo Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-17 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT16DONKOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jiali Dong (`KXWTAMATCH-26OCT16DONKOR-DON`) | 0.08 / 0.93 (200) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alina Korneeva (`KXWTAMATCH-26OCT16DONKOR-KOR`) | 0.08 / 0.93 (200) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Anhelina Kalinina vs Simona Waltert -- WTA Ningbo Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-17 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT16KALWAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anhelina Kalinina (`KXWTAMATCH-26OCT16KALWAL-KAL`) | 0.65 / 0.66 (13) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Simona Waltert (`KXWTAMATCH-26OCT16KALWAL-WAL`) | 0.33 / 0.34 (1) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Aliaksandra Sasnovich vs Anna Bondar -- WTA Ningbo Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-17 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT16SASBON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Bondar (`KXWTAMATCH-26OCT16SASBON-BON`) | 0.40 / 0.41 (98) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aliaksandra Sasnovich (`KXWTAMATCH-26OCT16SASBON-SAS`) | 0.59 / 0.60 (137) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mei Yamaguchi vs Sofia Kenin -- WTA Osaka Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 07:50Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-17 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T07:50:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT17YAMKEN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Kenin (`KXWTAMATCH-26OCT17YAMKEN-KEN`) | 0.86 / 0.88 (5897) | 87.0% | -- | -- | -- [-----] | -- | 87.1% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mei Yamaguchi (`KXWTAMATCH-26OCT17YAMKEN-YAM`) | 0.12 / 0.15 (6022) | 13.5% | -- | -- | -- [-----] | -- | 15.2% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Elizabeth Reasco Gonzalez / Rodriguez (`KXITFWDOUBLES-26OCT16RENSHOELIROD-ELIROD`) | 0.08 / 0.54 (54) | 31.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rencheli / Sholokhova (`KXITFWDOUBLES-26OCT16RENSHOELIROD-RENSHO`) | 0.08 / 0.67 (75) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Gabriela Dabrowski / Luisa Stefani vs Cristina Bucsa / Nicole Melichar-Martinez -- WTA Wuhan SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 10:00Z
* Current expected start: 2026-10-17 07:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-17 06:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-17T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17DABSTEBUCMEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cristina Bucsa / Nicole Melichar-Martinez (`KXWTADOUBLES-26OCT17DABSTEBUCMEL-BUCMEL`) | 0.05 / 0.94 (50) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gabriela Dabrowski / Luisa Stefani (`KXWTADOUBLES-26OCT17DABSTEBUCMEL-DABSTE`) | 0.05 / 0.95 (100) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Duru Soke vs Annika Penickova -- W35 Redding CA QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 07:15Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-17T07:15:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16SOKPEN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Annika Penickova (`KXITFWMATCH-26OCT16SOKPEN-PEN`) | 0.66 / 0.71 (169) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Duru Soke (`KXITFWMATCH-26OCT16SOKPEN-SOK`) | 0.29 / 0.34 (54) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Magdalena Frech vs Han Shi -- WTA Ningbo Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 07:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-17 06:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT16FRESHI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Magdalena Frech (`KXWTAMATCH-26OCT16FRESHI-FRE`) | 0.63 / 0.66 (110) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Han Shi (`KXWTAMATCH-26OCT16FRESHI-SHI`) | 0.34 / 0.37 (103) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mayar Sherif Ahmed Abdelaziz vs Tatiana Prozorova -- WTA Ningbo Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 07:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-17 06:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT16SHEPRO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tatiana Prozorova (`KXWTAMATCH-26OCT16SHEPRO-PRO`) | 0.64 / 0.67 (329) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mayar Sherif Ahmed Abdelaziz (`KXWTAMATCH-26OCT16SHEPRO-SHE`) | 0.33 / 0.34 (1) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dayana Yastremska vs Kamilla Rakhimova -- WTA Ningbo Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-17 07:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-17 06:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-17T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT16YASRAK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kamilla Rakhimova (`KXWTAMATCH-26OCT16YASRAK-RAK`) | 0.49 / 0.51 (10) | 50.0% | -- | -- | -- [-----] | -- | 49.2% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dayana Yastremska (`KXWTAMATCH-26OCT16YASRAK-YAS`) | 0.48 / 0.52 (240) | 50.0% | -- | -- | -- [-----] | -- | 50.7% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## HAN / Yi Cody Wong vs Zhang / Zheng -- W15 Shenzhen F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-17T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16HANYICZHAZHE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| HAN / Yi Cody Wong (`KXITFWDOUBLES-26OCT16HANYICZHAZHE-HANYIC`) | 0.08 / 0.95 (162) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Zhang / Zheng (`KXITFWDOUBLES-26OCT16HANYICZHAZHE-ZHAZHE`) | 0.05 / 0.29 (35) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Daria KHOMUTSIANSKAYA vs Junhan Zhang -- W15 Shenzhen SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-17T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16KHOZHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daria KHOMUTSIANSKAYA (`KXITFWMATCH-26OCT16KHOZHA-KHO`) | 0.50 / 0.80 (11) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Junhan Zhang (`KXITFWMATCH-26OCT16KHOZHA-ZHA`) | 0.09 / 0.31 (2) | 20.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chengyiyi Yuan vs Sijia Wei -- W15 Shenzhen SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-17T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16YUAWEI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sijia Wei (`KXITFWMATCH-26OCT16YUAWEI-WEI`) | 0.80 / 0.85 (418) | 82.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Chengyiyi Yuan (`KXITFWMATCH-26OCT16YUAWEI-YUA`) | 0.15 / 0.19 (243) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Olmos / Nicole Singeorzan vs Ma / Passola -- W35 Redding CA SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 08:15Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-17T08:15:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16OLMNICMAXPAS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ma / Passola (`KXITFWDOUBLES-26OCT16OLMNICMAXPAS-MAXPAS`) | 0.05 / 0.95 (112) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Olmos / Nicole Singeorzan (`KXITFWDOUBLES-26OCT16OLMNICMAXPAS-OLMNIC`) | 0.05 / 0.95 (112) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Alexander Zverev vs Alejandro Davidovich Fokina -- ATP Shanghai SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 07:00Z
* Current expected start: 2026-10-17 08:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-17 07:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+90_MIN

ATP (MASTERS_1000) · Hard · scheduled 2026-10-17T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:100644:200221:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alejandro Davidovich Fokina (`KXATPMATCH-26OCT17ZVEDAV-DAV`) | 0.24 / 0.25 (1945) | 24.5% | -- | 19.8% | 20.8% [20.1%-21.5%] | 25.5% | 24.1% | 24.8% | MODEL_LONE_OUTLIER | PASS | -3.7 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Alexander Zverev (`KXATPMATCH-26OCT17ZVEDAV-ZVE`) | 0.74 / 0.75 (6359) | 74.5% | -- | 80.2% | 79.2% [78.5%-79.9%] | 74.5% | 75.5% | 75.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +4.7 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 7502.0, B 4905.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0068
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.007, surface_dev_loose -0.001, surface_dev_tight +0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 4 carry a model probability
  * `KXATPEXACTMATCH-26OCT17ZVEDAV-ZVE21` Will Alexander Zverev win the Alexander Zverev vs Alejandro Davidovich Fokina match by a set score of 2-1?: 0.21/0.27 mid 24.0%, model 29.6% (market_conditioned_v1 (model4_board_v1)) -- gap +5.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17ZVEDAV-ZVE20` Will Alexander Zverev win the Alexander Zverev vs Alejandro Davidovich Fokina match by a set score of 2-0?: 0.49/0.50 mid 49.5%, model 44.9% (market_conditioned_v1 (model4_board_v1)) -- gap -4.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17ZVEDAV-DAV21` Will Alejandro Davidovich Fokina win the Alexander Zverev vs Alejandro Davidovich Fokina match by a set score of 2-1?: 0.10/0.14 mid 12.0%, model 14.6% (market_conditioned_v1 (model4_board_v1)) -- gap +2.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17ZVEDAV-DAV20` Will Alejandro Davidovich Fokina win the Alexander Zverev vs Alejandro Davidovich Fokina match by a set score of 2-0?: 0.12/0.14 mid 13.0%, model 10.9% (market_conditioned_v1 (model4_board_v1)) -- gap -2.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sonay Kartal vs Jelena Ostapenko -- WTA Wuhan SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-17 10:00Z
* Current expected start: 2026-10-17 09:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-16 12:04Z
* Recommended handicap-by time: 2026-10-17 08:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-60_MIN

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-17T10:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT17KAROST:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sonay Kartal (`KXWTAMATCH-26OCT17KAROST-KAR`) | 0.55 / 0.56 (34872) | 55.5% | -- | -- | -- [-----] | -- | 55.0% | 55.0% | MARKETS_AGREE | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jelena Ostapenko (`KXWTAMATCH-26OCT17KAROST-OST`) | 0.44 / 0.45 (1) | 44.5% | -- | -- | -- [-----] | -- | 45.3% | 45.3% | MARKETS_AGREE | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Martin Borisiouk vs Sergey Fomin -- M25 Qian Daohu SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-17T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16BORFOM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martin Borisiouk (`KXITFMATCH-26OCT16BORFOM-BOR`) | 0.55 / 0.59 (5) | 57.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sergey Fomin (`KXITFMATCH-26OCT16BORFOM-FOM`) | 0.38 / 0.45 (45) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Egor Pleshivtsev vs Matthew Dellavedova -- M25 Qian Daohu SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-17T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16PLEDEL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthew Dellavedova (`KXITFMATCH-26OCT16PLEDEL-DEL`) | 0.75 / 0.81 (4) | 78.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Egor Pleshivtsev (`KXITFMATCH-26OCT16PLEDEL-PLE`) | 0.18 / 0.22 (4) | 20.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Karan Singh vs Thanapet Chanta -- M25 Solapur SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-17T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT16SINCHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thanapet Chanta (`KXITFMATCH-26OCT16SINCHA-CHA`) | 0.36 / 0.41 (44) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Karan Singh (`KXITFMATCH-26OCT16SINCHA-SIN`) | 0.58 / 0.63 (5) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
