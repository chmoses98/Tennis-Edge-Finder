# ASSISTED SLATE -- 2026-10-31T03:27Z (`SL-20261031T032752Z-fe419356`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

137 open matches not seen started, 522 markets. Skipped: {"scheduled_start_over_24h_past": 3, "first_ball_already_observed": 4}. Sources: shadow board 2026-10-31T03:10:52.667715+00:00, Model 4 2026-10-31T03:11:04.940916+00:00, Gen-1 ledger 2026-10-31T03:10:49.262508+00:00, external 2026-10-31T02:40:48.410333+00:00, capture 20261031T023859Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-10-31 04:30Z**
* Recommended RUN TENNIS time: **2026-10-31 03:45Z**
* Final price/status check time: **2026-10-31 04:20Z**
* Number of matches in window: 4 (Diana Shnaider vs Mia Pohankova, Ching Laam Lai vs Carol Young Suh Lee, Ying Zhang vs Alexandra Shubladze, Leylah Fernandez vs Kamilla Rakhimova)

* **3 main-tour match(es) have NO verified start status** (STATUS_AMBIGUOUS): BET blocked until a live status check.

Slate built 2026-10-31T03:27Z. Refresh due by: 2026-10-31 03:45Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 27, "HIGH_REVIEW": 37, "NORMAL": 313, "REVIEW": 59, "UNPRICED": 86}; match winners: {"EXTREME": 18, "HIGH_REVIEW": 26, "NORMAL": 123, "REVIEW": 21, "UNPRICED": 86}; quote freshness at build: {"AGING": 436}.

## Kevin Krawietz / Tim Putz vs Henry Bernet / Dominic Stricker -- ATP Basel SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-30 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-30T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT30KRAPUTBERSTR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Henry Bernet / Dominic Stricker (`KXATPDOUBLES-26OCT30KRAPUTBERSTR-BERSTR`) | 0.22 / 0.25 (435) | 23.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kevin Krawietz / Tim Putz (`KXATPDOUBLES-26OCT30KRAPUTBERSTR-KRAPUT`) | 0.74 / 0.77 (462) | 75.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Blaise Bicknell vs Noah Schachter -- M15 Pembroke QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-30 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-30T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208132:209080:2026-10-30`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Blaise Bicknell (`KXITFMATCH-26OCT30BICSCH-BIC`) | 0.71 / 0.78 (20) | 74.5% | 82.6% | 73.0% | 76.3% [74.7%-77.8%] | -- | -- | -- | -- | PASS | +8.1 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Noah Schachter (`KXITFMATCH-26OCT30BICSCH-SCH`) | 0.17 / 0.26 (5) | 21.5% | 17.4% | 27.0% | 23.7% [22.2%-25.3%] | -- | -- | -- | -- | PASS | -4.1 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3719.0, B 2699.0; serve-point win A 65.2%, B 42.2%; Elo A 1497.2, B 1243.3; model uncertainty 0.0157
* Form inputs: days since last match A 32, B 186; matches on record A 233, B 184; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jacob Brumm vs Matt Kuhar -- M15 Pembroke QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-30 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-30T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:134276:208386:2026-10-30`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jacob Brumm (`KXITFMATCH-26OCT30BRUKUH-BRU`) | 0.37 / 0.43 (5) | 40.0% | 49.2% | 39.1% | 47.4% [43.2%-55.7%] | -- | -- | -- | -- | PASS | +9.2 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matt Kuhar (`KXITFMATCH-26OCT30BRUKUH-KUH`) | 0.54 / 0.64 (126) | 59.0% | 50.8% | 60.9% | 52.6% [44.3%-56.8%] | -- | -- | -- | -- | PASS | -8.2 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2191.0, B 2644.0; serve-point win A 57.4%, B 42.5%; Elo A 1319.0, B 1249.2; model uncertainty 0.0626
* Form inputs: days since last match A 186, B 186; matches on record A 213, B 138; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kacper Szymkowiak vs Keshav Chopra -- M15 Pembroke QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-30 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-30T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208844:212852:2026-10-30`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Keshav Chopra (`KXITFMATCH-26OCT30SZYCHO-CHO`) | 0.48 / 0.56 (1) | 52.0% | 29.7% | 19.9% | 25.7% [20.9%-31.1%] | -- | -- | -- | -- | PASS | -22.3 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kacper Szymkowiak (`KXITFMATCH-26OCT30SZYCHO-SZY`) | 0.43 / 0.50 (17) | 46.5% | 70.3% | 80.1% | 74.3% [68.9%-79.1%] | -- | -- | -- | -- | PASS | +23.8 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1216.0, B 1264.0; serve-point win A 60.9%, B 43.2%; Elo A 1370.4, B 1232.7; model uncertainty 0.0509
* Form inputs: days since last match A 235, B 67; matches on record A 41, B 89; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT30SZYCHO-SZY  (YES = Kacper Szymkowiak)
Model: 70%
Kalshi: 46%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alvin Nicholas Tudorica vs Paul Colin -- M15 Pembroke QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-30 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-30T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT30TUDCOL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Paul Colin (`KXITFMATCH-26OCT30TUDCOL-COL`) | 0.52 / 0.61 (29) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alvin Nicholas Tudorica (`KXITFMATCH-26OCT30TUDCOL-TUD`) | 0.38 / 0.47 (12) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Connie Ma vs Kristina Liutova -- W100 New Braunfels TX QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-30 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-30T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221143:269714:2026-10-30`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kristina Liutova (`KXITFWMATCH-26OCT30MAXLIU-LIU`) | 0.66 / 0.69 (225) | 67.5% | 86.5% | 80.4% | 78.9% [77.3%-80.4%] | -- | -- | -- | -- | PASS | +19.0 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Connie Ma (`KXITFWMATCH-26OCT30MAXLIU-MAX`) | 0.31 / 0.34 (399) | 32.5% | 13.5% | 19.6% | 21.1% [19.6%-22.7%] | -- | -- | -- | -- | PASS | -19.0 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 754.0; serve-point win A 49.2%, B 42.6%; Elo A 1475.0, B 1701.6; model uncertainty 0.0154
* Form inputs: days since last match A 1852, B 60; matches on record A 21, B 37; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT30MAXLIU-LIU  (YES = Kristina Liutova)
Model: 86%
Kalshi: 68%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.016, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuki Naito vs Caroline Dolehide -- W100 New Braunfels TX QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-30 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-30T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214452:216044:2026-10-30`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Caroline Dolehide (`KXITFWMATCH-26OCT30NAIDOL-DOL`) | 0.74 / 0.77 (281) | 75.5% | 83.9% | 59.9% | 70.6% [66.9%-76.7%] | -- | -- | -- | -- | PASS | +8.4 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuki Naito (`KXITFWMATCH-26OCT30NAIDOL-NAI`) | 0.23 / 0.25 (919) | 24.0% | 16.1% | 40.1% | 29.4% [23.3%-33.1%] | -- | -- | -- | -- | WATCH | -7.9 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2186.0, B 3771.0; serve-point win A 52.8%, B 39.7%; Elo A 1477.3, B 1758.6; model uncertainty 0.0493
* Form inputs: days since last match A 39, B 44; matches on record A 359, B 494; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose +0.001, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sloane Stephens vs Julieta Pareja -- W100 New Braunfels TX QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-30 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-30T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:201585:264075:2026-10-30`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julieta Pareja (`KXITFWMATCH-26OCT30STEPAR-PAR`) | 0.50 / 0.52 (239) | 51.0% | 42.9% | 62.0% | 46.3% [30.6%-54.8%] | -- | -- | -- | -- | PASS | -8.1 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sloane Stephens (`KXITFWMATCH-26OCT30STEPAR-STE`) | 0.48 / 0.49 (150) | 48.5% | 57.1% | 38.0% | 53.7% [45.2%-69.4%] | -- | -- | -- | -- | WATCH | +8.6 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2061.0, B 1273.0; serve-point win A 56.0%, B 45.3%; Elo A 1813.0, B 1696.0; model uncertainty 0.1207
* Form inputs: days since last match A 42, B 51; matches on record A 685, B 63; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.042, surface_pool_high -0.048, surface_dev_loose -0.016, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alicia Herrero Linana vs Bianca Andreescu -- WTA 125K Queretaro QF

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-31 04:10Z
* Current expected start: 2026-10-31 02:40Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 01:55Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA125 (WTA_125) · Clay · scheduled 2026-10-31T04:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:214189:215370:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bianca Andreescu (`KXWTACHALLENGERMATCH-26OCT30HERAND-AND`) | 0.74 / 0.75 (2591) | 74.5% | 75.0% | 62.6% | 68.9% [66.5%-72.1%] | -- | 76.1% | 76.1% | MODEL_LONE_OUTLIER | PASS | +0.5 pp | NORMAL | AGING | A / LIMITED | ALL_AGREE | VERIFIED |
| Alicia Herrero Linana (`KXWTACHALLENGERMATCH-26OCT30HERAND-HER`) | 0.25 / 0.26 (5659) | 25.5% | 25.0% | 37.4% | 31.1% [27.9%-33.5%] | -- | 24.0% | 24.0% | MODEL_LONE_OUTLIER | SHADOW_BET | -0.5 pp | NORMAL | AGING | A / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3011.0, B 2877.0; serve-point win A 51.9%, B 43.1%; Elo A 1597.0, B 1825.3; model uncertainty 0.028
* Form inputs: days since last match A 1, B 1; matches on record A 234, B 373; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.005, surface_dev_loose +0.004, surface_dev_tight -0.005
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; STATUS_AMBIGUOUS

## Emerson Jones vs Heather Watson -- WTA Hong Kong Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-31 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-31 03:10Z
* Source: COURT_PROGRESSION: preceding match on Court 1 in progress (set 1 of best-of-3); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 02:25Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-31T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:201586:263644:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emerson Jones (`KXWTAMATCH-26OCT30JONWAT-JON`) | 0.68 / 0.69 (4982) | 68.5% | 68.1% | 78.8% | 70.9% [57.8%-76.0%] | 67.6% | 68.1% | 67.8% | MODEL_LONE_OUTLIER | PASS | -0.4 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Heather Watson (`KXWTAMATCH-26OCT30JONWAT-WAT`) | 0.31 / 0.32 (773) | 31.5% | 31.9% | 21.2% | 29.1% [24.0%-42.2%] | 32.4% | 32.0% | 32.2% | MODEL_LONE_OUTLIER | PASS | +0.4 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3547.0, B 2194.0; serve-point win A 59.7%, B 43.8%; Elo A 1790.7, B 1736.1; model uncertainty 0.0909
* Form inputs: days since last match A 6, B 6; matches on record A 153, B 823; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.023, surface_pool_high +0.022, surface_dev_loose +0.004, surface_dev_tight -0.009
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT30JONWAT-2-WAT` Will Heather Watson win set 2 in the Emerson Jones vs Heather Watson match: 0.33/0.36 mid 34.5%, model 37.7% (projection_v2.0 (prediction ledger)) -- gap +3.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT30JONWAT-1-WAT` Will Heather Watson win set 1 in the Emerson Jones vs Heather Watson match: 0.35/0.36 mid 35.5%, model 37.7% (projection_v2.0 (prediction ledger)) -- gap +2.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT30JONWAT-1-JON` Will Emerson Jones win set 1 in the Emerson Jones vs Heather Watson match: 0.63/0.65 mid 64.0%, model 62.3% (projection_v2.0 (prediction ledger)) -- gap -1.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT30JONWAT-2-JON` Will Emerson Jones win set 2 in the Emerson Jones vs Heather Watson match: 0.62/0.65 mid 63.5%, model 62.3% (projection_v2.0 (prediction ledger)) -- gap -1.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; STATUS_AMBIGUOUS; THIN_DISPLAYED_SIZE

## Elena Pridankina vs Ekaterine Gorgodze -- WTA Hong Kong Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-31 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-31 03:10Z
* Source: COURT_PROGRESSION: preceding match on Court 2 in progress (set 1 of best-of-3); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 02:25Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-31T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202493:239389:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterine Gorgodze (`KXWTAMATCH-26OCT30PRIGOR-GOR`) | 0.29 / 0.30 (272) | 29.5% | 24.0% | 32.0% | 31.1% [29.7%-33.5%] | 30.9% | 29.7% | 30.3% | MODEL_LONE_OUTLIER | PASS | -5.5 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Elena Pridankina (`KXWTAMATCH-26OCT30PRIGOR-PRI`) | 0.70 / 0.71 (808) | 70.5% | 76.0% | 68.0% | 68.9% [66.5%-70.3%] | 69.1% | 70.5% | 69.8% | MODEL_LONE_OUTLIER | PASS | +5.5 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3685.0, B 4075.0; serve-point win A 57.2%, B 48.1%; Elo A 1721.4, B 1576.3; model uncertainty 0.0187
* Form inputs: days since last match A 6, B 7; matches on record A 289, B 950; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.009, surface_dev_loose +0.014, surface_dev_tight -0.024
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT30PRIGOR-1-PRI` Will Elena Pridankina win set 1 in the Elena Pridankina vs Ekaterine Gorgodze match: 0.64/0.66 mid 65.0%, model 68.1% (projection_v2.0 (prediction ledger)) -- gap +3.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT30PRIGOR-1-GOR` Will Ekaterine Gorgodze win set 1 in the Elena Pridankina vs Ekaterine Gorgodze match: 0.33/0.35 mid 34.0%, model 31.9% (projection_v2.0 (prediction ledger)) -- gap -2.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT30PRIGOR-2-PRI` Will Elena Pridankina win set 2 in the Elena Pridankina vs Ekaterine Gorgodze match: 0.64/0.70 mid 67.0%, model 68.1% (projection_v2.0 (prediction ledger)) -- gap +1.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT30PRIGOR-2-GOR` Will Ekaterine Gorgodze win set 2 in the Elena Pridankina vs Ekaterine Gorgodze match: 0.30/0.35 mid 32.5%, model 31.9% (projection_v2.0 (prediction ledger)) -- gap -0.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; STATUS_AMBIGUOUS

## Aliaksandra Sasnovich vs Cheuk Ying Shek -- WTA Hong Kong Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-31 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-31 03:10Z
* Source: COURT_PROGRESSION: preceding match on Centre Court in progress (set 1 of best-of-3); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 02:25Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-31T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:205925:263941:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aliaksandra Sasnovich (`KXWTAMATCH-26OCT30SASSHE-SAS`) | 0.94 / 0.95 (2360) | 94.5% | 89.2% | 66.0% | 80.3% [73.5%-90.1%] | 93.6% | 93.5% | 93.5% | MODEL_LONE_OUTLIER | PASS | -5.3 pp | NORMAL | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Cheuk Ying Shek (`KXWTAMATCH-26OCT30SASSHE-SHE`) | 0.05 / 0.06 (1905) | 5.5% | 10.8% | 34.0% | 19.7% [9.9%-26.5%] | 6.4% | 6.5% | 6.4% | MODEL_LONE_OUTLIER | WATCH | +5.3 pp | NORMAL | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4822.0, B 1558.0; serve-point win A 58.9%, B 50.4%; Elo A 1849.5, B 1459.5; model uncertainty 0.0831
* Form inputs: days since last match A 3, B 7; matches on record A 796, B 48; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.027, surface_dev_loose -0.000, surface_dev_tight -0.000
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT30SASSHE-1-SAS` Will Aliaksandra Sasnovich win set 1 in the Aliaksandra Sasnovich vs Cheuk Ying Shek match: 0.91/0.92 mid 91.5%, model 79.6% (projection_v2.0 (prediction ledger)) -- gap -11.9 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT30SASSHE-1-SHE` Will Cheuk Ying Shek win set 1 in the Aliaksandra Sasnovich vs Cheuk Ying Shek match: 0.08/0.09 mid 8.5%, model 20.4% (projection_v2.0 (prediction ledger)) -- gap +11.9 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT30SASSHE-2-SHE` Will Cheuk Ying Shek win set 2 in the Aliaksandra Sasnovich vs Cheuk Ying Shek match: 0.06/0.12 mid 9.0%, model 20.4% (projection_v2.0 (prediction ledger)) -- gap +11.4 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT30SASSHE-2-SAS` Will Aliaksandra Sasnovich win set 2 in the Aliaksandra Sasnovich vs Cheuk Ying Shek match: 0.88/0.92 mid 90.0%, model 79.6% (projection_v2.0 (prediction ledger)) -- gap -10.4 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; STATUS_AMBIGUOUS; THIN_DISPLAYED_SIZE

## Diana Shnaider vs Mia Pohankova -- WTA Tokyo SF

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 07:10Z
* Current expected start: 2026-10-31 04:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 03:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-31T07:10:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:223670:266376:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mia Pohankova (`KXWTAMATCH-26OCT31SHNPOH-POH`) | 0.27 / 0.29 (104350) | 28.0% | 41.0% | 46.4% | 41.3% [28.7%-48.4%] | 28.2% | 27.2% | 27.7% | MARKETS_AGREE | WATCH | +13.0 pp | REVIEW | AGING | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Diana Shnaider (`KXWTAMATCH-26OCT31SHNPOH-SHN`) | 0.71 / 0.72 (695) | 71.5% | 59.0% | 53.6% | 58.7% [51.5%-71.3%] | 71.8% | 72.5% | 72.2% | MARKETS_AGREE | PASS | -12.5 pp | REVIEW | AGING | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4846.0, B 1596.0; serve-point win A 60.8%, B 40.9%; Elo A 1984.4, B 1888.8; model uncertainty 0.0987
* Form inputs: days since last match A 1, B 1; matches on record A 326, B 65; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.050, surface_pool_high -0.061, surface_dev_loose -0.015, surface_dev_tight +0.010
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT31SHNPOH-21` Over 20.5 games: 0.50/0.51 mid 50.5%, model 69.6% (projection_v2.0 (prediction ledger)) -- gap +19.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT31SHNPOH-26` Over 25.5 games: 0.32/0.34 mid 33.0%, model 46.1% (projection_v2.0 (prediction ledger)) -- gap +13.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT31SHNPOH-2-POH` Will Mia Pohankova win set 2 in the Diana Shnaider vs Mia Pohankova match: 0.30/0.35 mid 32.5%, model 44.0% (projection_v2.0 (prediction ledger)) -- gap +11.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT31SHNPOH-2-SHN` Will Diana Shnaider win set 2 in the Diana Shnaider vs Mia Pohankova match: 0.65/0.68 mid 66.5%, model 56.0% (projection_v2.0 (prediction ledger)) -- gap -10.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT31SHNPOH-1-POH` Will Mia Pohankova win set 1 in the Diana Shnaider vs Mia Pohankova match: 0.34/0.35 mid 34.5%, model 44.0% (projection_v2.0 (prediction ledger)) -- gap +9.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT31SHNPOH-1-SHN` Will Diana Shnaider win set 1 in the Diana Shnaider vs Mia Pohankova match: 0.64/0.65 mid 64.5%, model 56.0% (projection_v2.0 (prediction ledger)) -- gap -8.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT31SHNPOH-16` Over 15.5 games: 0.88/0.93 mid 90.5%, model 98.1% (projection_v2.0 (prediction ledger)) -- gap +7.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE

## Broadus / Zamarripa vs Christine Lutkemeyer / Miroshnichenko -- W100 New Braunfels TX SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 04:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-31T04:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT30BROZAMCHRMIR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Broadus / Zamarripa (`KXITFWDOUBLES-26OCT30BROZAMCHRMIR-BROZAM`) | 0.58 / 0.82 (138) | 70.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Christine Lutkemeyer / Miroshnichenko (`KXITFWDOUBLES-26OCT30BROZAMCHRMIR-CHRMIR`) | 0.13 / 0.36 (39) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Ching Laam Lai vs Carol Young Suh Lee -- WTA Hong Kong Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-31 05:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 04:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-31T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:221803:264250:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ching Laam Lai (`KXWTAMATCH-26OCT30LAILEE-LAI`) | 0.02 / 0.04 (13885) | 3.0% | 1.3% | 8.3% | 4.2% [3.8%-4.5%] | -- | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carol Young Suh Lee (`KXWTAMATCH-26OCT30LAILEE-LEE`) | 0.97 / 0.98 (1168) | 97.5% | 98.7% | 91.6% | 95.8% [95.5%-96.2%] | -- | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 188.0, B 4047.0; serve-point win A 49.8%, B 33.1%; Elo A 1217.8, B 1779.1; model uncertainty 0.0039
* Form inputs: days since last match A 488, B 5; matches on record A 9, B 157; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.002, surface_pool_high +0.002, surface_dev_loose -0.001, surface_dev_tight -0.000
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT30LAILEE-1-LAI` Will Ching Laam Lai win set 1 in the Ching Laam Lai vs Carol Young Suh Lee match: 0.02/0.03 mid 2.5%, model 6.8% (projection_v2.0 (prediction ledger)) -- gap +4.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data POOR
  * `KXWTASETWINNER-26OCT30LAILEE-1-LEE` Will Carol Young Suh Lee win set 1 in the Ching Laam Lai vs Carol Young Suh Lee match: 0.97/0.98 mid 97.5%, model 93.2% (projection_v2.0 (prediction ledger)) -- gap -4.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data POOR
  * `KXWTASETWINNER-26OCT30LAILEE-2-LEE` Will Carol Young Suh Lee win set 2 in the Ching Laam Lai vs Carol Young Suh Lee match: 0.81/0.98 mid 89.5%, model 93.2% (projection_v2.0 (prediction ledger)) -- gap +3.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data POOR
  * `KXWTASETWINNER-26OCT30LAILEE-2-LAI` Will Ching Laam Lai win set 2 in the Ching Laam Lai vs Carol Young Suh Lee match: 0.01/0.14 mid 7.5%, model 6.8% (projection_v2.0 (prediction ledger)) -- gap -0.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data POOR
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ying Zhang vs Alexandra Shubladze -- WTA Hong Kong Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-31 05:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 04:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-31T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213947:260168:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandra Shubladze (`KXWTAMATCH-26OCT30ZHASHU-SHU`) | 0.95 / 0.96 (2302) | 95.5% | 90.8% | 92.4% | 89.0% [85.9%-90.8%] | 94.7% | 94.9% | 94.7% | MODEL_LONE_OUTLIER | PASS | -4.7 pp | NORMAL | AGING | A / LIMITED | ALL_AGREE | VERIFIED |
| Ying Zhang (`KXWTAMATCH-26OCT30ZHASHU-ZHA`) | 0.04 / 0.05 (20908) | 4.5% | 9.2% | 7.6% | 11.0% [9.2%-14.1%] | 5.3% | 4.5% | 4.9% | MODEL_LONE_OUTLIER | SHADOW_BET | +4.7 pp | NORMAL | AGING | A / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 1998.0, B 3247.0; serve-point win A 53.1%, B 36.7%; Elo A 1464.6, B 1751.6; model uncertainty 0.0246
* Form inputs: days since last match A 110, B 7; matches on record A 329, B 207; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.010, surface_dev_loose -0.007, surface_dev_tight +0.005
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT30ZHASHU-1-SHU` Will Alexandra Shubladze win set 1 in the Ying Zhang vs Alexandra Shubladze match: 0.93/0.94 mid 93.5%, model 81.3% (projection_v2.0 (prediction ledger)) -- gap -12.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT30ZHASHU-1-ZHA` Will Ying Zhang win set 1 in the Ying Zhang vs Alexandra Shubladze match: 0.06/0.07 mid 6.5%, model 18.7% (projection_v2.0 (prediction ledger)) -- gap +12.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT30ZHASHU-2-ZHA` Will Ying Zhang win set 2 in the Ying Zhang vs Alexandra Shubladze match: 0.05/0.12 mid 8.5%, model 18.7% (projection_v2.0 (prediction ledger)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT30ZHASHU-2-SHU` Will Alexandra Shubladze win set 2 in the Ying Zhang vs Alexandra Shubladze match: 0.84/0.94 mid 89.0%, model 81.3% (projection_v2.0 (prediction ledger)) -- gap -7.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Gabriela Dabrowski / Luisa Stefani vs Storm Hunter / Maya Joint -- WTA Tokyo SF

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-10-31 06:00Z
* Current expected start: 2026-10-31 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 05:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-31T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT30DABSTEHUNJOI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriela Dabrowski / Luisa Stefani (`KXWTADOUBLES-26OCT30DABSTEHUNJOI-DABSTE`) | 0.75 / 0.76 (244) | 75.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Storm Hunter / Maya Joint (`KXWTADOUBLES-26OCT30DABSTEHUNJOI-HUNJOI`) | 0.23 / 0.25 (23) | 24.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Leylah Fernandez vs Kamilla Rakhimova -- WTA Tokyo SF

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 06:00Z
* Current expected start: 2026-10-31 06:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-30 06:54Z
* Recommended handicap-by time: 2026-10-31 05:15Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-31T04:00:00+00:00 as not a valid time; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-31T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215872:220367:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leylah Fernandez (`KXWTAMATCH-26OCT30FERRAK-FER`) | 0.71 / 0.72 (21841) | 71.5% | 64.9% | 65.8% | 66.7% [63.4%-67.7%] | 73.4% | 73.8% | 73.6% | MODEL_LONE_OUTLIER | PASS | -6.6 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Kamilla Rakhimova (`KXWTAMATCH-26OCT30FERRAK-RAK`) | 0.28 / 0.29 (29613) | 28.5% | 35.1% | 34.2% | 33.3% [32.3%-36.6%] | 26.7% | 26.0% | 26.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.6 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4828.0, B 5718.0; serve-point win A 59.4%, B 43.5%; Elo A 1983.9, B 1851.1; model uncertainty 0.0215
* Form inputs: days since last match A 2, B 1; matches on record A 407, B 482; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.005, surface_dev_loose -0.000, surface_dev_tight +0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT30FERRAK-22` Over 21.5 games: 0.48/0.51 mid 49.5%, model 61.6% (projection_v2.0 (prediction ledger)) -- gap +12.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT30FERRAK-27` Over 26.5 games: 0.26/0.32 mid 29.0%, model 38.6% (projection_v2.0 (prediction ledger)) -- gap +9.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT30FERRAK-2-RAK` Will Kamilla Rakhimova win set 2 in the Leylah Annie Fernandez vs Kamilla Rakhimova match: 0.32/0.34 mid 33.0%, model 39.9% (projection_v2.0 (prediction ledger)) -- gap +6.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT30FERRAK-2-FER` Will Leylah Annie Fernandez win set 2 in the Leylah Annie Fernandez vs Kamilla Rakhimova match: 0.65/0.68 mid 66.5%, model 60.1% (projection_v2.0 (prediction ledger)) -- gap -6.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT30FERRAK-17` Over 16.5 games: 0.91/0.92 mid 91.5%, model 93.6% (projection_v2.0 (prediction ledger)) -- gap +2.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT30FERRAK-1-FER` Will Leylah Annie Fernandez win set 1 in the Leylah Annie Fernandez vs Kamilla Rakhimova match: 0.61/0.63 mid 62.0%, model 60.1% (projection_v2.0 (prediction ledger)) -- gap -1.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT30FERRAK-1-RAK` Will Kamilla Rakhimova win set 1 in the Leylah Annie Fernandez vs Kamilla Rakhimova match: 0.37/0.39 mid 38.0%, model 39.9% (projection_v2.0 (prediction ledger)) -- gap +1.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE

## Polina Kudermetova / Maria Timofeeva vs Janice Tjen / Venus Williams -- WTA Guangzhou SF

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-10-30 08:00Z
* Current expected start: 2026-10-31 06:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 05:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-30T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT30KUDTIMTJEWIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Kudermetova / Maria Timofeeva (`KXWTADOUBLES-26OCT30KUDTIMTJEWIL-KUDTIM`) | 0.27 / 0.29 (883) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Janice Tjen / Venus Williams (`KXWTADOUBLES-26OCT30KUDTIMTJEWIL-TJEWIL`) | 0.70 / 0.73 (1251) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Back / Yamazaki vs Sato / Tse -- W35 Sydney F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 06:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-31T06:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT30BACYAMSATTSE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Back / Yamazaki (`KXITFWDOUBLES-26OCT30BACYAMSATTSE-BACYAM`) | 0.31 / 0.39 (2) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sato / Tse (`KXITFWDOUBLES-26OCT30BACYAMSATTSE-SATTSE`) | 0.62 / 0.68 (39) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Becroft / Shepp vs Dong / Leonard Sach -- M25 Tamworth F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-31T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT30BECSHEDONLEO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Becroft / Shepp (`KXITFDOUBLES-26OCT30BECSHEDONLEO-BECSHE`) | 0.80 / 0.81 (3) | 80.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dong / Leonard Sach (`KXITFDOUBLES-26OCT30BECSHEDONLEO-DONLEO`) | 0.21 / 0.23 (1) | 22.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Coleman Wong vs Omar Jasika -- ATP Challenger Seoul SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 07:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-31T07:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:117357:209409:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Omar Jasika (`KXATPCHALLENGERMATCH-26OCT31WONJAS-JAS`) | 0.17 / 0.18 (1) | 17.5% | 19.1% | 21.3% | 20.9% [20.2%-21.6%] | -- | 17.5% | -- | INSUFFICIENT_INPUTS | PASS | +1.6 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Coleman Wong (`KXATPCHALLENGERMATCH-26OCT31WONJAS-WON`) | 0.81 / 0.82 (3154) | 81.5% | 80.8% | 78.7% | 79.1% [78.4%-79.8%] | -- | 82.6% | -- | INSUFFICIENT_INPUTS | PASS | -0.7 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5943.0, B 3991.0; serve-point win A 67.6%, B 39.4%; Elo A 1745.2, B 1501.6; model uncertainty 0.007
* Form inputs: days since last match A 12, B 32; matches on record A 336, B 516; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.007, surface_dev_tight -0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; THIN_DISPLAYED_SIZE

## Tereza Mihalikova / Olivia Nicholls vs Sara Errani / Jasmine Paolini -- WTA Tokyo SF

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-10-31 06:00Z
* Current expected start: 2026-10-31 07:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 06:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-31T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT30MIHNICERRPAO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Errani / Jasmine Paolini (`KXWTADOUBLES-26OCT30MIHNICERRPAO-ERRPAO`) | 0.71 / 0.72 (2033) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tereza Mihalikova / Olivia Nicholls (`KXWTADOUBLES-26OCT30MIHNICERRPAO-MIHNIC`) | 0.27 / 0.29 (116) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Hikaru Shiraishi vs Yuto Oki -- M15 Yanagawa City SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202113:212639:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuto Oki (`KXITFMATCH-26OCT30SHIOKI-OKI`) | 0.12 / 0.13 (2575) | 12.5% | 32.3% | 36.8% | 32.9% [31.1%-34.3%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +19.8 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hikaru Shiraishi (`KXITFMATCH-26OCT30SHIOKI-SHI`) | 0.87 / 0.88 (13528) | 87.5% | 67.7% | 63.2% | 67.1% [65.7%-68.9%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -19.8 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2976.0, B 1766.0; serve-point win A 61.0%, B 42.5%; Elo A 1438.1, B 1280.4; model uncertainty 0.0162
* Form inputs: days since last match A 47, B 215; matches on record A 210, B 42; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT30SHIOKI-OKI  (YES = Yuto Oki)
Model: 32%
Kalshi: 12%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.009, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Taiyo Yamanaka vs Shinji Hazawa -- M15 Yanagawa City SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206923:208277:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shinji Hazawa (`KXITFMATCH-26OCT30YAMHAZ-HAZ`) | 0.68 / 0.69 (8009) | 68.5% | 61.0% | 58.6% | 59.6% [56.6%-61.0%] | 46.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.5 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Taiyo Yamanaka (`KXITFMATCH-26OCT30YAMHAZ-YAM`) | 0.31 / 0.32 (14378) | 31.5% | 39.0% | 41.4% | 40.5% [39.0%-43.4%] | 53.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +7.5 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2208.0, B 3455.0; serve-point win A 60.8%, B 37.0%; Elo A 1281.4, B 1358.1; model uncertainty 0.0221
* Form inputs: days since last match A 166, B 187; matches on record A 184, B 227; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.015, surface_dev_loose -0.015, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yeri Hong vs Violet Apisah -- W15 Singapore SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221802:270097:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Violet Apisah (`KXITFWMATCH-26OCT30HONAPI-API`) | 0.89 / 0.90 (14199) | 89.5% | 53.5% | 31.5% | 58.5% [55.3%-60.6%] | 69.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -36.0 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Yeri Hong (`KXITFWMATCH-26OCT30HONAPI-HON`) | 0.10 / 0.11 (5283) | 10.5% | 46.5% | 68.5% | 41.5% [39.5%-44.7%] | 30.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +36.0 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 172.0, B 122.0; serve-point win A 53.1%, B 46.2%; Elo A 1309.3, B 1379.7; model uncertainty 0.0261
* Form inputs: days since last match A 187, B 2823; matches on record A 4, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT30HONAPI-HON  (YES = Yeri Hong)
Model: 47%
Kalshi: 10%
Gap: +36 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexandra Malova vs Thasaporn Naklo -- W15 Singapore SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-31T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT30MALNAK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandra Malova (`KXITFWMATCH-26OCT30MALNAK-MAL`) | 0.53 / 0.54 (4) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Thasaporn Naklo (`KXITFWMATCH-26OCT30MALNAK-NAK`) | 0.46 / 0.47 (3096) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matta / Peck vs De Alba / Sau Franco -- M15 Mazatlan SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 08:15Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-31T08:15:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT30MATPECDEASAU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| De Alba / Sau Franco (`KXITFDOUBLES-26OCT30MATPECDEASAU-DEASAU`) | 0.16 / 0.36 (2) | 26.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matta / Peck (`KXITFDOUBLES-26OCT30MATPECDEASAU-MATPEC`) | 0.60 / 0.76 (1) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Billy Harris vs Terence Atmane -- ATP Challenger Seoul SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 08:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-31T08:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126129:209279:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Terence Atmane (`KXATPCHALLENGERMATCH-26OCT31HARATM-ATM`) | 0.72 / 0.74 (14999) | 73.0% | 71.5% | 62.3% | 65.4% [64.1%-67.6%] | 71.6% | 73.3% | 72.5% | MODEL_LONE_OUTLIER | PASS | -1.5 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Billy Harris (`KXATPCHALLENGERMATCH-26OCT31HARATM-HAR`) | 0.26 / 0.28 (13427) | 27.0% | 28.5% | 37.7% | 34.6% [32.4%-35.9%] | 28.4% | 26.9% | 27.6% | MODEL_LONE_OUTLIER | SHADOW_BET | +1.5 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5716.0, B 5304.0; serve-point win A 65.0%, B 30.3%; Elo A 1602.4, B 1805.6; model uncertainty 0.0176
* Form inputs: days since last match A 19, B 8; matches on record A 634, B 437; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.018, surface_dev_loose -0.009, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Xinran Sun vs Harriet Dart -- WTA Guangzhou SF

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 11:30Z
* Current expected start: 2026-10-31 08:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 07:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-31T11:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211279:270082:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Harriet Dart (`KXWTAMATCH-26OCT31SUNDAR-DAR`) | 0.48 / 0.49 (15321) | 48.5% | 61.8% | 44.1% | 55.3% [46.3%-66.5%] | 48.9% | 48.1% | 48.5% | MODEL_LONE_OUTLIER | WATCH | +13.3 pp | REVIEW | AGING | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Xinran Sun (`KXWTAMATCH-26OCT31SUNDAR-SUN`) | 0.51 / 0.52 (6157) | 51.5% | 38.2% | 55.9% | 44.7% [33.5%-53.7%] | 51.1% | 51.6% | 51.3% | MODEL_LONE_OUTLIER | PASS | -13.3 pp | REVIEW | AGING | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1001.0, B 4244.0; serve-point win A 51.6%, B 46.1%; Elo A 1715.6, B 1802.7; model uncertainty 0.1015
* Form inputs: days since last match A 2, B 1; matches on record A 27, B 681; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.032, surface_pool_high +0.043, surface_dev_loose +0.016, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT31SUNDAR-22` Over 21.5 games: 0.50/0.51 mid 50.5%, model 60.3% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT31SUNDAR-1-DAR` Will Harriet Dart win set 1 in the Xinran Sun vs Harriet Dart match: 0.49/0.50 mid 49.5%, model 57.9% (projection_v2.0 (prediction ledger)) -- gap +8.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT31SUNDAR-2-DAR` Will Harriet Dart win set 2 in the Xinran Sun vs Harriet Dart match: 0.47/0.52 mid 49.5%, model 57.9% (projection_v2.0 (prediction ledger)) -- gap +8.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT31SUNDAR-2-SUN` Will Xinran Sun win set 2 in the Xinran Sun vs Harriet Dart match: 0.48/0.53 mid 50.5%, model 42.1% (projection_v2.0 (prediction ledger)) -- gap -8.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT31SUNDAR-1-SUN` Will Xinran Sun win set 1 in the Xinran Sun vs Harriet Dart match: 0.49/0.51 mid 50.0%, model 42.1% (projection_v2.0 (prediction ledger)) -- gap -7.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26OCT31SUNDAR-27` Over 26.5 games: 0.27/0.33 mid 30.0%, model 37.1% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT31SUNDAR-17` Over 16.5 games: 0.83/0.88 mid 85.5%, model 91.9% (projection_v2.0 (prediction ledger)) -- gap +6.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; LOW_DATA_QUALITY

## Akira Santillan / Baoluo Zheng vs Cheng-Peng Hsieh / Kaichi Uchida -- ATP Challenger Ningbo F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 08:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-31T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT31SANZHEHSIUCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cheng-Peng Hsieh / Kaichi Uchida (`KXATPCHALLENGERDOUBLES-26OCT31SANZHEHSIUCH-HSIUCH`) | 0.35 / 0.45 (28) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Akira Santillan / Baoluo Zheng (`KXATPCHALLENGERDOUBLES-26OCT31SANZHEHSIUCH-SANZHE`) | 0.49 / 0.60 (50) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Hanatani / Lu vs Kim / An Lin -- W15 Singapore F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 08:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-31T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT30HANLUXKIMANL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hanatani / Lu (`KXITFWDOUBLES-26OCT30HANLUXKIMANL-HANLUX`) | 0.01 / 0.04 (1) | 2.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kim / An Lin (`KXITFWDOUBLES-26OCT30HANLUXKIMANL-KIMANL`) | 0.93 / 0.97 (1) | 95.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Koizumi / Taka vs Kawachi / Yamanaka -- M15 Yanagawa City F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-31T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT30KOITAKKAWYAM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kawachi / Yamanaka (`KXITFDOUBLES-26OCT30KOITAKKAWYAM-KAWYAM`) | 0.36 / 0.89 (2) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Koizumi / Taka (`KXITFDOUBLES-26OCT30KOITAKKAWYAM-KOITAK`) | 0.11 / 0.65 (1) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sijia Wei vs Wushuang Zheng -- W35 Kunshan SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213821:221096:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sijia Wei (`KXITFWMATCH-26OCT30WEIZHE-WEI`) | 0.02 / 0.03 (26828) | 2.5% | 75.0% | 78.1% | 75.6% [67.0%-78.8%] | 66.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +72.5 pp | EXTREME (DATA_WARNING) | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Wushuang Zheng (`KXITFWMATCH-26OCT30WEIZHE-ZHE`) | 0.97 / 0.98 (14413) | 97.5% | 25.0% | 21.9% | 24.4% [21.1%-33.0%] | 33.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -72.5 pp | EXTREME (DATA_WARNING) | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2150.0, B 2161.0; serve-point win A 56.5%, B 48.5%; Elo A 1716.7, B 1552.0; model uncertainty 0.059
* Form inputs: days since last match A 26, B 25; matches on record A 308, B 302; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT30WEIZHE-WEI  (YES = Sijia Wei)
Model: 75%
Kalshi: 2%
Gap: +73 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.017, surface_pool_high +0.024, surface_dev_loose +0.020, surface_dev_tight -0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chengyiyi Yuan vs Yu Jun Lin -- W35 Kunshan SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215134:268787:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yu Jun Lin (`KXITFWMATCH-26OCT30YUALIN-LIN`) | 0.55 / 0.56 (12424) | 55.5% | 30.4% | 35.9% | 32.5% [32.0%-34.0%] | 52.9% | -- | 52.9% | MODEL_LONE_OUTLIER | PASS | -25.1 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Chengyiyi Yuan (`KXITFWMATCH-26OCT30YUALIN-YUA`) | 0.44 / 0.45 (2840) | 44.5% | 69.6% | 64.0% | 67.5% [66.0%-68.0%] | 47.1% | -- | 47.1% | MODEL_LONE_OUTLIER | WATCH | +25.1 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2947.0, B 515.0; serve-point win A 56.8%, B 47.0%; Elo A 1478.6, B 1346.6; model uncertainty 0.0098
* Form inputs: days since last match A 34, B 14; matches on record A 239, B 14; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT30YUALIN-YUA  (YES = Chengyiyi Yuan)
Model: 70%
Kalshi: 44%
Gap: +25 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aliona Falei vs Ekaterina Yashina -- WTA Chennai Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 12:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-31 09:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 08:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-31T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202672:221434:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aliona Falei (`KXWTAMATCH-26OCT31FALYAS-FAL`) | 0.94 / 0.95 (2110) | 94.5% | 90.5% | 88.6% | 87.5% [85.0%-88.6%] | 94.7% | 94.5% | 94.7% | MODEL_LONE_OUTLIER | PASS | -4.0 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Ekaterina Yashina (`KXWTAMATCH-26OCT31FALYAS-YAS`) | 0.05 / 0.06 (1660) | 5.5% | 9.5% | 11.4% | 12.5% [11.4%-15.0%] | 5.3% | 52.1% | 28.7% | KALSHI_LONE_OUTLIER | SHADOW_BET | +4.0 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_OUTLIER | VERIFIED |

* Serve evidence (points): A 3528.0, B 2932.0; serve-point win A 63.0%, B 47.0%; Elo A 1746.0, B 1432.9; model uncertainty 0.0177
* Form inputs: days since last match A 22, B 27; matches on record A 288, B 745; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.011, surface_dev_loose +0.003, surface_dev_tight -0.005
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT31FALYAS-2-FAL` Will Aliona Falei win set 2 in the Aliona Falei vs Ekaterina Yashina match: 0.03/0.97 mid 50.0%, model 80.9% (projection_v2.0 (prediction ledger)) -- gap +30.9 pp, EXTREME, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT31FALYAS-2-YAS` Will Ekaterina Yashina win set 2 in the Aliona Falei vs Ekaterina Yashina match: 0.02/0.98 mid 50.0%, model 19.1% (projection_v2.0 (prediction ledger)) -- gap -30.9 pp, EXTREME, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT31FALYAS-1-FAL` Will Aliona Falei win set 1 in the Aliona Falei vs Ekaterina Yashina match: 0.08/0.97 mid 52.5%, model 80.9% (projection_v2.0 (prediction ledger)) -- gap +28.4 pp, EXTREME, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT31FALYAS-1-YAS` Will Ekaterina Yashina win set 1 in the Aliona Falei vs Ekaterina Yashina match: 0.02/0.86 mid 44.0%, model 19.1% (projection_v2.0 (prediction ledger)) -- gap -24.9 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kyoka Okamura vs Diya Ramesh Ramesh -- WTA Chennai Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 12:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-31 09:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 08:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-31T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211846:269832:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kyoka Okamura (`KXWTAMATCH-26OCT31OKARAM-OKA`) | 0.96 / 0.97 (610) | 96.5% | 96.7% | 75.5% | 91.5% [89.9%-92.3%] | -- | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Diya Ramesh Ramesh (`KXWTAMATCH-26OCT31OKARAM-RAM`) | 0.03 / 0.04 (9762) | 3.5% | 3.3% | 24.5% | 8.5% [7.7%-10.1%] | -- | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2971.0, B 37.0; serve-point win A 63.0%, B 51.0%; Elo A 1648.3, B 1237.1; model uncertainty 0.0122
* Form inputs: days since last match A 7, B 369; matches on record A 628, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.013, surface_dev_loose -0.002, surface_dev_tight -0.004
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT31OKARAM-1-OKA` Will Kyoka Okamura win set 1 in the Kyoka Okamura vs Diya Ramesh Ramesh match: 0.03/0.98 mid 50.5%, model 89.1% (projection_v2.0 (prediction ledger)) -- gap +38.6 pp, EXTREME, DATA_WARNING, quote AGING, identity AMBIGUOUS, data POOR
  * `KXWTASETWINNER-26OCT31OKARAM-1-RAM` Will Diya Ramesh Ramesh win set 1 in the Kyoka Okamura vs Diya Ramesh Ramesh match: 0.02/0.97 mid 49.5%, model 10.9% (projection_v2.0 (prediction ledger)) -- gap -38.6 pp, EXTREME, DATA_WARNING, quote AGING, identity AMBIGUOUS, data POOR
  * `KXWTASETWINNER-26OCT31OKARAM-2-OKA` Will Kyoka Okamura win set 2 in the Kyoka Okamura vs Diya Ramesh Ramesh match: 0.02/0.99 mid 50.5%, model 89.1% (projection_v2.0 (prediction ledger)) -- gap +38.6 pp, EXTREME, DATA_WARNING, quote AGING, identity AMBIGUOUS, data POOR
  * `KXWTASETWINNER-26OCT31OKARAM-2-RAM` Will Diya Ramesh Ramesh win set 2 in the Kyoka Okamura vs Diya Ramesh Ramesh match: 0.01/0.98 mid 49.5%, model 10.9% (projection_v2.0 (prediction ledger)) -- gap -38.6 pp, EXTREME, DATA_WARNING, quote AGING, identity AMBIGUOUS, data POOR
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Mariia Tkacheva vs Rada Zolotareva -- WTA Chennai Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 12:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-31 09:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 08:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-31T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:221086:260951:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mariia Tkacheva (`KXWTAMATCH-26OCT31TKAZOL-TKA`) | 0.43 / 0.44 (124) | 43.5% | 49.3% | 53.2% | 55.8% [51.6%-59.4%] | 44.4% | 44.3% | 44.3% | MARKETS_AGREE | SHADOW_BET | +5.8 pp | NORMAL | AGING | B / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Rada Zolotareva (`KXWTAMATCH-26OCT31TKAZOL-ZOL`) | 0.55 / 0.57 (3006) | 56.0% | 50.7% | 46.8% | 44.2% [40.6%-48.4%] | 55.6% | 55.8% | 55.8% | MARKETS_AGREE | PASS | -5.3 pp | NORMAL | AGING | B / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 1420.0, B 1811.0; serve-point win A 56.1%, B 43.7%; Elo A 1640.1, B 1579.7; model uncertainty 0.0392
* Form inputs: days since last match A 26, B 54; matches on record A 237, B 96; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.037, surface_pool_high +0.036, surface_dev_loose +0.021, surface_dev_tight -0.021
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT31TKAZOL-1-TKA` Will Mariia Tkacheva win set 1 in the Mariia Tkacheva vs Rada Zolotareva match: 0.44/0.47 mid 45.5%, model 49.5% (projection_v2.0 (prediction ledger)) -- gap +4.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT31TKAZOL-1-ZOL` Will Rada Zolotareva win set 1 in the Mariia Tkacheva vs Rada Zolotareva match: 0.53/0.54 mid 53.5%, model 50.5% (projection_v2.0 (prediction ledger)) -- gap -3.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT31TKAZOL-2-TKA` Will Mariia Tkacheva win set 2 in the Mariia Tkacheva vs Rada Zolotareva match: 0.03/0.97 mid 50.0%, model 49.5% (projection_v2.0 (prediction ledger)) -- gap -0.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT31TKAZOL-2-ZOL` Will Rada Zolotareva win set 2 in the Mariia Tkacheva vs Rada Zolotareva match: 0.03/0.97 mid 50.0%, model 50.5% (projection_v2.0 (prediction ledger)) -- gap +0.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; WIDE_SPREAD

## M Rifqi Fitriadi vs Madhwin Kamath -- M15 Singapore SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-31T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT30FITKAM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M Rifqi Fitriadi (`KXITFMATCH-26OCT30FITKAM-FIT`) | 0.83 / 0.85 (624) | 84.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Madhwin Kamath (`KXITFMATCH-26OCT30FITKAM-KAM`) | 0.14 / 0.15 (122) | 14.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maxime Janvier vs Adhithya Ganesan -- M15 Singapore SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126125:212258:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adhithya Ganesan (`KXITFMATCH-26OCT30JANGAN-GAN`) | 0.33 / 0.34 (37) | 33.5% | 42.2% | 44.9% | 42.4% [36.6%-43.9%] | 35.6% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +8.7 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maxime Janvier (`KXITFMATCH-26OCT30JANGAN-JAN`) | 0.63 / 0.64 (102) | 63.5% | 57.8% | 55.1% | 57.6% [56.1%-63.4%] | 64.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.7 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4068.0, B 2730.0; serve-point win A 62.9%, B 38.7%; Elo A 1467.8, B 1381.1; model uncertainty 0.0369
* Form inputs: days since last match A 47, B 299; matches on record A 773, B 95; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.010, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yaroslav Demin vs Yu Hsiou Hsu -- ATP Challenger Ningbo SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 09:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-31T09:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200318:211596:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yaroslav Demin (`KXATPCHALLENGERMATCH-26OCT31DEMHSU-DEM`) | 0.41 / 0.42 (2419) | 41.5% | 40.9% | 44.9% | 40.8% [34.9%-42.3%] | 42.8% | 41.3% | 42.1% | MODEL_LONE_OUTLIER | PASS | -0.6 pp | NORMAL | AGING | B / LIMITED | ALL_AGREE | VERIFIED |
| Yu Hsiou Hsu (`KXATPCHALLENGERMATCH-26OCT31DEMHSU-HSU`) | 0.58 / 0.59 (2436) | 58.5% | 59.1% | 55.1% | 59.2% [57.7%-65.0%] | 57.2% | 58.5% | 57.9% | MODEL_LONE_OUTLIER | PASS | +0.6 pp | NORMAL | AGING | B / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 2769.0, B 4308.0; serve-point win A 59.6%, B 38.6%; Elo A 1479.2, B 1608.7; model uncertainty 0.037
* Form inputs: days since last match A 215, B 12; matches on record A 121, B 528; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.020, surface_dev_loose +0.015, surface_dev_tight -0.025
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Pablo Carreno Busta vs Mattia Bellucci -- ATP Paris Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-31 10:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 09:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-10-31T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105807:208233:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mattia Bellucci (`KXATPMATCH-26OCT31CARBEL-BEL`) | 0.56 / 0.57 (264) | 56.5% | 61.7% | 54.5% | 53.0% [51.0%-54.0%] | 58.3% | 57.2% | 57.8% | MODEL_LONE_OUTLIER | PASS | +5.2 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Pablo Carreno Busta (`KXATPMATCH-26OCT31CARBEL-CAR`) | 0.43 / 0.44 (12894) | 43.5% | 38.3% | 45.5% | 47.0% [46.0%-49.0%] | 41.7% | 43.7% | 42.7% | MODEL_LONE_OUTLIER | WATCH | -5.2 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4853.0, B 5542.0; serve-point win A 62.0%, B 35.7%; Elo A 1836.2, B 1811.0; model uncertainty 0.015
* Form inputs: days since last match A 7, B 9; matches on record A 992, B 431; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.015
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT31CARBEL-2-BEL` Will Mattia Bellucci win set 2 in the Pablo Carreno Busta vs Mattia Bellucci match: 0.13/0.80 mid 46.5%, model 57.9% (projection_v2.0 (prediction ledger)) -- gap +11.4 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31CARBEL-CAR20` Will Pablo Carreno Busta win the Pablo Carreno Busta vs Mattia Bellucci match by a set score of 2-0?: 0.20/0.30 mid 25.0%, model 17.8% (projection_v2.0 (prediction ledger)) -- gap -7.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31CARBEL-2-CAR` Will Pablo Carreno Busta win set 2 in the Pablo Carreno Busta vs Mattia Bellucci match: 0.13/0.80 mid 46.5%, model 42.1% (projection_v2.0 (prediction ledger)) -- gap -4.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31CARBEL-CAR21` Will Pablo Carreno Busta win the Pablo Carreno Busta vs Mattia Bellucci match by a set score of 2-1?: 0.11/0.38 mid 24.5%, model 20.5% (projection_v2.0 (prediction ledger)) -- gap -4.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31CARBEL-BEL20` Will Mattia Bellucci win the Pablo Carreno Busta vs Mattia Bellucci match by a set score of 2-0?: 0.26/0.44 mid 35.0%, model 33.5% (projection_v2.0 (prediction ledger)) -- gap -1.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31CARBEL-1-BEL` Will Mattia Bellucci win set 1 in the Pablo Carreno Busta vs Mattia Bellucci match: 0.55/0.58 mid 56.5%, model 57.9% (projection_v2.0 (prediction ledger)) -- gap +1.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31CARBEL-BEL21` Will Mattia Bellucci win the Pablo Carreno Busta vs Mattia Bellucci match by a set score of 2-1?: 0.16/0.38 mid 27.0%, model 28.2% (projection_v2.0 (prediction ledger)) -- gap +1.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31CARBEL-1-CAR` Will Pablo Carreno Busta win set 1 in the Pablo Carreno Busta vs Mattia Bellucci match: 0.42/0.44 mid 43.0%, model 42.1% (projection_v2.0 (prediction ledger)) -- gap -0.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jaime Faria vs Rinky Hijikata -- ATP Paris Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-31 10:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 09:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-10-31T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208014:210262:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jaime Faria (`KXATPMATCH-26OCT31FARHIJ-FAR`) | 0.45 / 0.47 (10791) | 46.0% | 49.6% | 51.5% | 51.0% [50.5%-52.0%] | 46.8% | 45.5% | 46.8% | MODEL_LONE_OUTLIER | SHADOW_BET | +3.6 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Rinky Hijikata (`KXATPMATCH-26OCT31FARHIJ-HIJ`) | 0.53 / 0.54 (488) | 53.5% | 50.4% | 48.5% | 49.0% [48.0%-49.5%] | 53.2% | 52.9% | 53.2% | MODEL_LONE_OUTLIER | PASS | -3.1 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5885.0, B 6001.0; serve-point win A 62.5%, B 37.4%; Elo A 1789.7, B 1805.7; model uncertainty 0.0076
* Form inputs: days since last match A 7, B 3; matches on record A 346, B 466; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight +0.010
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT31FARHIJ-HIJ21` Will Rinky Hijikata win the Jaime Faria vs Rinky Hijikata match by a set score of 2-1?: 0.01/0.27 mid 14.0%, model 25.1% (projection_v2.0 (prediction ledger)) -- gap +11.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31FARHIJ-FAR20` Will Jaime Faria win the Jaime Faria vs Rinky Hijikata match by a set score of 2-0?: 0.01/0.33 mid 17.0%, model 24.8% (projection_v2.0 (prediction ledger)) -- gap +7.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31FARHIJ-FAR21` Will Jaime Faria win the Jaime Faria vs Rinky Hijikata match by a set score of 2-1?: 0.10/0.28 mid 19.0%, model 24.9% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31FARHIJ-HIJ20` Will Rinky Hijikata win the Jaime Faria vs Rinky Hijikata match by a set score of 2-0?: 0.01/0.38 mid 19.5%, model 25.2% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31FARHIJ-2-HIJ` Will Rinky Hijikata win set 2 in the Jaime Faria vs Rinky Hijikata match: 0.15/0.79 mid 47.0%, model 50.2% (projection_v2.0 (prediction ledger)) -- gap +3.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31FARHIJ-1-FAR` Will Jaime Faria win set 1 in the Jaime Faria vs Rinky Hijikata match: 0.46/0.48 mid 47.0%, model 49.8% (projection_v2.0 (prediction ledger)) -- gap +2.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31FARHIJ-2-FAR` Will Jaime Faria win set 2 in the Jaime Faria vs Rinky Hijikata match: 0.15/0.79 mid 47.0%, model 49.8% (projection_v2.0 (prediction ledger)) -- gap +2.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31FARHIJ-1-HIJ` Will Rinky Hijikata win set 1 in the Jaime Faria vs Rinky Hijikata match: 0.51/0.54 mid 52.5%, model 50.2% (projection_v2.0 (prediction ledger)) -- gap -2.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Thiago Agustin Tirante vs Zachary Svajda -- ATP Paris Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-31 10:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 09:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-10-31T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:202058:208260:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zachary Svajda (`KXATPMATCH-26OCT31TIRSVA-SVA`) | 0.54 / 0.55 (344) | 54.5% | 52.3% | 46.1% | 49.5% [46.6%-52.4%] | 55.6% | 53.8% | 54.7% | MODEL_LONE_OUTLIER | PASS | -2.2 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Thiago Agustin Tirante (`KXATPMATCH-26OCT31TIRSVA-TIR`) | 0.45 / 0.46 (1598) | 45.5% | 47.7% | 53.9% | 50.5% [47.6%-53.4%] | 44.4% | 47.2% | 45.8% | MODEL_LONE_OUTLIER | WATCH | +2.2 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5742.0, B 4783.0; serve-point win A 66.0%, B 33.5%; Elo A 1737.0, B 1811.8; model uncertainty 0.0292
* Form inputs: days since last match A 7, B 7; matches on record A 490, B 362; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.029, surface_pool_high -0.029, surface_dev_loose -0.000, surface_dev_tight -0.005
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT31TIRSVA-SVA21` Will Zachary Svajda win the Thiago Agustin Tirante vs Zachary Svajda match by a set score of 2-1?: 0.10/0.25 mid 17.5%, model 25.7% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31TIRSVA-TIR21` Will Thiago Agustin Tirante win the Thiago Agustin Tirante vs Zachary Svajda match by a set score of 2-1?: 0.10/0.22 mid 16.0%, model 24.2% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31TIRSVA-TIR20` Will Thiago Agustin Tirante win the Thiago Agustin Tirante vs Zachary Svajda match by a set score of 2-0?: 0.01/0.32 mid 16.5%, model 23.5% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31TIRSVA-SVA20` Will Zachary Svajda win the Thiago Agustin Tirante vs Zachary Svajda match by a set score of 2-0?: 0.01/0.39 mid 20.0%, model 26.6% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31TIRSVA-2-SVA` Will Zachary Svajda win set 2 in the Thiago Agustin Tirante vs Zachary Svajda match: 0.13/0.80 mid 46.5%, model 51.5% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31TIRSVA-1-TIR` Will Thiago Agustin Tirante win set 1 in the Thiago Agustin Tirante vs Zachary Svajda match: 0.44/0.47 mid 45.5%, model 48.5% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31TIRSVA-1-SVA` Will Zachary Svajda win set 1 in the Thiago Agustin Tirante vs Zachary Svajda match: 0.53/0.55 mid 54.0%, model 51.5% (projection_v2.0 (prediction ledger)) -- gap -2.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31TIRSVA-2-TIR` Will Thiago Agustin Tirante win set 2 in the Thiago Agustin Tirante vs Zachary Svajda match: 0.13/0.80 mid 46.5%, model 48.5% (projection_v2.0 (prediction ledger)) -- gap +2.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kaitlin Quevedo vs Lilli Tagger -- WTA Guangzhou SF

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 12:40Z
* Current expected start: 2026-10-31 10:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 09:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-31T12:40:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:259733:260172:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kaitlin Quevedo (`KXWTAMATCH-26OCT31QUETAG-QUE`) | 0.33 / 0.34 (50516) | 33.5% | 36.9% | 34.9% | 38.8% [35.9%-42.7%] | 33.6% | 32.9% | 33.3% | MARKETS_AGREE | WATCH | +3.4 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Lilli Tagger (`KXWTAMATCH-26OCT31QUETAG-TAG`) | 0.67 / 0.68 (29665) | 67.5% | 63.1% | 65.1% | 61.2% [57.3%-64.1%] | 66.4% | 66.9% | 66.6% | MODEL_LONE_OUTLIER | PASS | -4.4 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3270.0, B 2552.0; serve-point win A 58.4%, B 39.0%; Elo A 1783.1, B 1820.0; model uncertainty 0.0343
* Form inputs: days since last match A 1, B 2; matches on record A 231, B 134; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight -0.010
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT31QUETAG-22` Over 21.5 games: 0.46/0.47 mid 46.5%, model 63.4% (projection_v2.0 (prediction ledger)) -- gap +16.9 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT31QUETAG-17` Over 16.5 games: 0.82/0.94 mid 88.0%, model 94.8% (projection_v2.0 (prediction ledger)) -- gap +6.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT31QUETAG-27` Over 26.5 games: 0.27/0.40 mid 33.5%, model 40.1% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT31QUETAG-1-QUE` Will Kaitlin Quevedo win set 1 in the Kaitlin Quevedo vs Lilli Tagger match: 0.34/0.37 mid 35.5%, model 41.2% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT31QUETAG-2-QUE` Will Kaitlin Quevedo win set 2 in the Kaitlin Quevedo vs Lilli Tagger match: 0.34/0.38 mid 36.0%, model 41.2% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT31QUETAG-1-TAG` Will Lilli Tagger win set 1 in the Kaitlin Quevedo vs Lilli Tagger match: 0.63/0.64 mid 63.5%, model 58.8% (projection_v2.0 (prediction ledger)) -- gap -4.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT31QUETAG-2-TAG` Will Lilli Tagger win set 2 in the Kaitlin Quevedo vs Lilli Tagger match: 0.61/0.64 mid 62.5%, model 58.8% (projection_v2.0 (prediction ledger)) -- gap -3.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Petr Bar Biryukov vs Liam Broady -- ATP Challenger Ningbo SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 10:50Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-31T10:50:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106281:209951:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Petr Bar Biryukov (`KXATPCHALLENGERMATCH-26OCT31BARBRO-BAR`) | 0.33 / 0.34 (3657) | 33.5% | 35.6% | 16.5% | 21.0% [18.7%-23.9%] | 33.6% | 33.4% | 33.5% | MODEL_LONE_OUTLIER | PASS | +2.1 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Liam Broady (`KXATPCHALLENGERMATCH-26OCT31BARBRO-BRO`) | 0.66 / 0.67 (1115) | 66.5% | 64.4% | 83.5% | 79.0% [76.1%-81.3%] | 66.4% | 66.3% | 66.3% | MODEL_LONE_OUTLIER | SHADOW_BET | -2.1 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4232.0, B 4440.0; serve-point win A 65.8%, B 31.2%; Elo A 1539.3, B 1639.6; model uncertainty 0.0261
* Form inputs: days since last match A 14, B 12; matches on record A 242, B 947; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.007, surface_dev_loose -0.007, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Hugo Gaston vs Vit Kopriva -- ATP Paris Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-31 11:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 10:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-10-31T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200240:200384:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Gaston (`KXATPMATCH-26OCT31GASKOP-GAS`) | 0.67 / 0.68 (8976) | 67.5% | 54.9% | 59.7% | 59.2% [56.6%-60.7%] | 66.9% | 66.9% | 66.9% | MODEL_LONE_OUTLIER | PASS | -12.6 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Vit Kopriva (`KXATPMATCH-26OCT31GASKOP-KOP`) | 0.32 / 0.33 (786) | 32.5% | 45.1% | 40.3% | 40.8% [39.3%-43.4%] | 33.1% | 34.4% | 33.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +12.6 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5258.0, B 5742.0; serve-point win A 60.7%, B 40.3%; Elo A 1733.6, B 1675.9; model uncertainty 0.0201
* Form inputs: days since last match A 11, B 7; matches on record A 529, B 725; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.010, surface_dev_loose +0.015, surface_dev_tight -0.025
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT31GASKOP-1-KOP` Will Vit Kopriva win set 1 in the Hugo Gaston vs Vit Kopriva match: 0.34/0.37 mid 35.5%, model 46.8% (projection_v2.0 (prediction ledger)) -- gap +11.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31GASKOP-1-GAS` Will Hugo Gaston win set 1 in the Hugo Gaston vs Vit Kopriva match: 0.63/0.65 mid 64.0%, model 53.2% (projection_v2.0 (prediction ledger)) -- gap -10.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31GASKOP-GAS21` Will Hugo Gaston win the Hugo Gaston vs Vit Kopriva match by a set score of 2-1?: 0.10/0.29 mid 19.5%, model 26.5% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31GASKOP-2-GAS` Will Hugo Gaston win set 2 in the Hugo Gaston vs Vit Kopriva match: 0.15/0.79 mid 47.0%, model 53.2% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31GASKOP-KOP20` Will Vit Kopriva win the Hugo Gaston vs Vit Kopriva match by a set score of 2-0?: 0.11/0.23 mid 17.0%, model 21.9% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31GASKOP-GAS20` Will Hugo Gaston win the Hugo Gaston vs Vit Kopriva match by a set score of 2-0?: 0.01/0.52 mid 26.5%, model 28.3% (projection_v2.0 (prediction ledger)) -- gap +1.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31GASKOP-KOP21` Will Vit Kopriva win the Hugo Gaston vs Vit Kopriva match by a set score of 2-1?: 0.06/0.38 mid 22.0%, model 23.3% (projection_v2.0 (prediction ledger)) -- gap +1.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31GASKOP-2-KOP` Will Vit Kopriva win set 2 in the Hugo Gaston vs Vit Kopriva match: 0.15/0.79 mid 47.0%, model 46.8% (projection_v2.0 (prediction ledger)) -- gap -0.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jensi Dipakbhai Kanabar vs Weronika Falkowska -- WTA Chennai Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 12:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-31 11:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 10:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-31T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:216579:270404:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Weronika Falkowska (`KXWTAMATCH-26OCT31KANFAL-FAL`) | 0.87 / 0.88 (2152) | 87.5% | 82.7% | 68.4% | 77.2% [74.3%-78.7%] | 87.3% | 86.6% | 87.0% | MODEL_LONE_OUTLIER | PASS | -4.8 pp | NORMAL | AGING | F / POOR | ALL_AGREE | VERIFIED |
| Jensi Dipakbhai Kanabar (`KXWTAMATCH-26OCT31KANFAL-KAN`) | 0.12 / 0.13 (121) | 12.5% | 17.3% | 31.6% | 22.8% [21.3%-25.7%] | 12.7% | 13.2% | 12.9% | MODEL_LONE_OUTLIER | PASS | +4.8 pp | NORMAL | AGING | F / POOR | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 298.0, B 2031.0; serve-point win A 51.6%, B 41.3%; Elo A 1350.6, B 1576.2; model uncertainty 0.022
* Form inputs: days since last match A 187, B 26; matches on record A 5, B 372; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.012, surface_dev_loose +0.000, surface_dev_tight +0.004
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT31KANFAL-2-FAL` Will Weronika Falkowska win set 2 in the Jensi Dipakbhai Kanabar vs Weronika Falkowska match: 0.03/0.97 mid 50.0%, model 73.5% (projection_v2.0 (prediction ledger)) -- gap +23.5 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data POOR
  * `KXWTASETWINNER-26OCT31KANFAL-2-KAN` Will Jensi Dipakbhai Kanabar win set 2 in the Jensi Dipakbhai Kanabar vs Weronika Falkowska match: 0.03/0.97 mid 50.0%, model 26.5% (projection_v2.0 (prediction ledger)) -- gap -23.5 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data POOR
  * `KXWTASETWINNER-26OCT31KANFAL-1-FAL` Will Weronika Falkowska win set 1 in the Jensi Dipakbhai Kanabar vs Weronika Falkowska match: 0.81/0.85 mid 83.0%, model 73.5% (projection_v2.0 (prediction ledger)) -- gap -9.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data POOR
  * `KXWTASETWINNER-26OCT31KANFAL-1-KAN` Will Jensi Dipakbhai Kanabar win set 1 in the Jensi Dipakbhai Kanabar vs Weronika Falkowska match: 0.16/0.19 mid 17.5%, model 26.5% (projection_v2.0 (prediction ledger)) -- gap +9.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data POOR
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; WIDE_SPREAD

## Rinko Matsuda vs Momoko Kobori -- WTA Chennai Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 12:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-31 11:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 10:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-31T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215468:259690:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Momoko Kobori (`KXWTAMATCH-26OCT31MATKOB-KOB`) | 0.43 / 0.44 (721) | 43.5% | 51.1% | 43.1% | 52.1% [48.4%-58.9%] | 44.4% | 44.3% | 44.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +7.6 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Rinko Matsuda (`KXWTAMATCH-26OCT31MATKOB-MAT`) | 0.55 / 0.57 (820) | 56.0% | 48.9% | 56.9% | 47.9% [41.1%-51.6%] | 55.6% | 56.5% | 56.1% | MODEL_LONE_OUTLIER | PASS | -7.1 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2804.0, B 1427.0; serve-point win A 55.3%, B 44.5%; Elo A 1498.5, B 1569.0; model uncertainty 0.0526
* Form inputs: days since last match A 14, B 14; matches on record A 203, B 372; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.016, surface_dev_loose -0.000, surface_dev_tight +0.000
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT31MATKOB-1-KOB` Will Momoko Kobori win set 1 in the Rinko Matsuda vs Momoko Kobori match: 0.45/0.47 mid 46.0%, model 50.7% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT31MATKOB-1-MAT` Will Rinko Matsuda win set 1 in the Rinko Matsuda vs Momoko Kobori match: 0.53/0.55 mid 54.0%, model 49.3% (projection_v2.0 (prediction ledger)) -- gap -4.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT31MATKOB-2-MAT` Will Rinko Matsuda win set 2 in the Rinko Matsuda vs Momoko Kobori match: 0.02/0.98 mid 50.0%, model 49.3% (projection_v2.0 (prediction ledger)) -- gap -0.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT31MATKOB-2-KOB` Will Momoko Kobori win set 2 in the Rinko Matsuda vs Momoko Kobori match: 0.02/0.99 mid 50.5%, model 50.7% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; WIDE_SPREAD

## Viktoria Morvayova vs Shrivalli Rashmikaa Bhamidipaty -- WTA Chennai Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 12:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-31 11:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 10:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-31T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215077:220842:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shrivalli Rashmikaa Bhamidipaty (`KXWTAMATCH-26OCT31MORBHA-BHA`) | 0.26 / 0.27 (701) | 26.5% | 47.2% | 32.4% | 41.2% [38.7%-45.3%] | 28.2% | 28.5% | 28.2% | MODEL_LONE_OUTLIER | WATCH | +20.7 pp | HIGH_REVIEW | AGING | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Viktoria Morvayova (`KXWTAMATCH-26OCT31MORBHA-MOR`) | 0.73 / 0.74 (925) | 73.5% | 52.8% | 67.7% | 58.8% [54.7%-61.3%] | 71.8% | 74.2% | 71.8% | MODEL_LONE_OUTLIER | PASS | -20.7 pp | HIGH_REVIEW | AGING | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3267.0, B 1402.0; serve-point win A 58.6%, B 41.9%; Elo A 1556.2, B 1552.4; model uncertainty 0.0331
* Form inputs: days since last match A 18, B 243; matches on record A 465, B 214; data quality C

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT31MORBHA-BHA  (YES = Shrivalli Rashmikaa Bhamidipaty)
Model: 47%
Kalshi: 26%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, EXTERNAL_MARKET_REJECTION
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.021, surface_dev_loose -0.000, surface_dev_tight -0.005
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT31MORBHA-1-MOR` Will Viktoria Morvayova win set 1 in the Viktoria Morvayova vs Shrivalli Rashmikaa Bhamidipaty match: 0.67/0.70 mid 68.5%, model 51.8% (projection_v2.0 (prediction ledger)) -- gap -16.7 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT31MORBHA-1-BHA` Will Shrivalli Rashmikaa Bhamidipaty win set 1 in the Viktoria Morvayova vs Shrivalli Rashmikaa Bhamidipaty match: 0.31/0.33 mid 32.0%, model 48.2% (projection_v2.0 (prediction ledger)) -- gap +16.2 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT31MORBHA-2-BHA` Will Shrivalli Rashmikaa Bhamidipaty win set 2 in the Viktoria Morvayova vs Shrivalli Rashmikaa Bhamidipaty match: 0.02/0.99 mid 50.5%, model 48.2% (projection_v2.0 (prediction ledger)) -- gap -2.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT31MORBHA-2-MOR` Will Viktoria Morvayova win set 2 in the Viktoria Morvayova vs Shrivalli Rashmikaa Bhamidipaty match: 0.02/0.99 mid 50.5%, model 51.8% (projection_v2.0 (prediction ledger)) -- gap +1.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Digvijay Pratap Singh vs David Eichenseher -- M15 Fergana SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-31T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT31SINEIC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| David Eichenseher (`KXITFMATCH-26OCT31SINEIC-EIC`) | 0.24 / 0.25 (692) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Digvijay Pratap Singh (`KXITFMATCH-26OCT31SINEIC-SIN`) | 0.74 / 0.75 (200) | 74.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Juan Manuel Cerundolo vs Aleksandar Kovacevic -- ATP Paris Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-31 11:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 10:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-10-31T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:206499:207678:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Manuel Cerundolo (`KXATPMATCH-26OCT31CERKOV-CER`) | 0.45 / 0.47 (14328) | 46.0% | 54.2% | 59.0% | 56.7% [54.8%-58.6%] | 46.8% | 46.0% | 46.8% | MODEL_LONE_OUTLIER | SHADOW_BET | +8.2 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Aleksandar Kovacevic (`KXATPMATCH-26OCT31CERKOV-KOV`) | 0.53 / 0.54 (1979) | 53.5% | 45.8% | 41.0% | 43.3% [41.4%-45.2%] | 53.2% | 51.7% | 53.2% | MODEL_LONE_OUTLIER | PASS | -7.7 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 6168.0, B 5407.0; serve-point win A 68.1%, B 32.8%; Elo A 1741.5, B 1755.1; model uncertainty 0.0189
* Form inputs: days since last match A 5, B 4; matches on record A 545, B 425; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.019, surface_dev_loose -0.015, surface_dev_tight +0.010
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT31CERKOV-CER21` Will Juan Manuel Cerundolo win the Juan Manuel Cerundolo vs Aleksandar Kovacevic match by a set score of 2-1?: 0.01/0.26 mid 13.5%, model 26.3% (projection_v2.0 (prediction ledger)) -- gap +12.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31CERKOV-CER20` Will Juan Manuel Cerundolo win the Juan Manuel Cerundolo vs Aleksandar Kovacevic match by a set score of 2-0?: 0.01/0.33 mid 17.0%, model 27.9% (projection_v2.0 (prediction ledger)) -- gap +10.9 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31CERKOV-2-CER` Will Juan Manuel Cerundolo win set 2 in the Juan Manuel Cerundolo vs Aleksandar Kovacevic match: 0.15/0.79 mid 47.0%, model 52.8% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31CERKOV-1-CER` Will Juan Manuel Cerundolo win set 1 in the Juan Manuel Cerundolo vs Aleksandar Kovacevic match: 0.46/0.49 mid 47.5%, model 52.8% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31CERKOV-1-KOV` Will Aleksandar Kovacevic win set 1 in the Juan Manuel Cerundolo vs Aleksandar Kovacevic match: 0.51/0.54 mid 52.5%, model 47.2% (projection_v2.0 (prediction ledger)) -- gap -5.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31CERKOV-KOV21` Will Aleksandar Kovacevic win the Juan Manuel Cerundolo vs Aleksandar Kovacevic match by a set score of 2-1?: 0.10/0.27 mid 18.5%, model 23.5% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31CERKOV-KOV20` Will Aleksandar Kovacevic win the Juan Manuel Cerundolo vs Aleksandar Kovacevic match by a set score of 2-0?: 0.01/0.37 mid 19.0%, model 22.3% (projection_v2.0 (prediction ledger)) -- gap +3.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31CERKOV-2-KOV` Will Aleksandar Kovacevic win set 2 in the Juan Manuel Cerundolo vs Aleksandar Kovacevic match: 0.15/0.79 mid 47.0%, model 47.2% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## James Duckworth vs Miomir Kecmanovic -- ATP Paris Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-31 11:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 10:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-10-31T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105902:200175:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| James Duckworth (`KXATPMATCH-26OCT31DUCKEC-DUC`) | 0.43 / 0.44 (18531) | 43.5% | 42.9% | 51.9% | 50.5% [50.0%-51.5%] | 43.4% | 43.9% | 43.4% | MODEL_LONE_OUTLIER | SHADOW_BET | -0.6 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Miomir Kecmanovic (`KXATPMATCH-26OCT31DUCKEC-KEC`) | 0.57 / 0.59 (1087) | 58.0% | 57.1% | 48.0% | 49.5% [48.5%-50.0%] | 56.6% | 55.9% | 56.6% | MODEL_LONE_OUTLIER | PASS | -0.9 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 6236.0, B 5445.0; serve-point win A 65.1%, B 33.4%; Elo A 1749.8, B 1772.3; model uncertainty 0.0073
* Form inputs: days since last match A 7, B 7; matches on record A 941, B 617; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.010, surface_dev_tight -0.000
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT31DUCKEC-KEC21` Will Miomir Kecmanovic win the James Duckworth vs Miomir Kecmanovic match by a set score of 2-1?: 0.01/0.26 mid 13.5%, model 27.1% (projection_v2.0 (prediction ledger)) -- gap +13.6 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31DUCKEC-KEC20` Will Miomir Kecmanovic win the James Duckworth vs Miomir Kecmanovic match by a set score of 2-0?: 0.01/0.41 mid 21.0%, model 30.0% (projection_v2.0 (prediction ledger)) -- gap +9.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31DUCKEC-2-KEC` Will Miomir Kecmanovic win set 2 in the James Duckworth vs Miomir Kecmanovic match: 0.13/0.80 mid 46.5%, model 54.8% (projection_v2.0 (prediction ledger)) -- gap +8.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31DUCKEC-DUC21` Will James Duckworth win the James Duckworth vs Miomir Kecmanovic match by a set score of 2-1?: 0.08/0.24 mid 16.0%, model 22.4% (projection_v2.0 (prediction ledger)) -- gap +6.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31DUCKEC-DUC20` Will James Duckworth win the James Duckworth vs Miomir Kecmanovic match by a set score of 2-0?: 0.17/0.30 mid 23.5%, model 20.4% (projection_v2.0 (prediction ledger)) -- gap -3.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31DUCKEC-1-DUC` Will James Duckworth win set 1 in the James Duckworth vs Miomir Kecmanovic match: 0.41/0.44 mid 42.5%, model 45.2% (projection_v2.0 (prediction ledger)) -- gap +2.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31DUCKEC-1-KEC` Will Miomir Kecmanovic win set 1 in the James Duckworth vs Miomir Kecmanovic match: 0.56/0.58 mid 57.0%, model 54.8% (projection_v2.0 (prediction ledger)) -- gap -2.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31DUCKEC-2-DUC` Will James Duckworth win set 2 in the James Duckworth vs Miomir Kecmanovic match: 0.13/0.80 mid 46.5%, model 45.2% (projection_v2.0 (prediction ledger)) -- gap -1.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tomas Machac vs Martin Landaluce -- ATP Paris Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-31 11:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 10:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-10-31T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207830:212021:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martin Landaluce (`KXATPMATCH-26OCT31MACLAN-LAN`) | 0.34 / 0.35 (8628) | 34.5% | 23.3% | 58.5% | 51.0% [39.0%-54.0%] | 36.1% | 36.3% | 36.1% | MODEL_LONE_OUTLIER | SHADOW_BET | -11.2 pp | REVIEW | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Tomas Machac (`KXATPMATCH-26OCT31MACLAN-MAC`) | 0.65 / 0.66 (688) | 65.5% | 76.7% | 41.5% | 49.0% [46.0%-61.0%] | 63.9% | 63.7% | 63.9% | MODEL_LONE_OUTLIER | PASS | +11.2 pp | REVIEW | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4045.0, B 5447.0; serve-point win A 65.8%, B 40.0%; Elo A 1912.3, B 1780.2; model uncertainty 0.0749
* Form inputs: days since last match A 5, B 186; matches on record A 458, B 210; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.020, surface_dev_tight +0.025
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT31MACLAN-2-MAC` Will Tomas Machac win set 2 in the Tomas Machac vs Martin Landaluce match: 0.13/0.80 mid 46.5%, model 68.7% (projection_v2.0 (prediction ledger)) -- gap +22.2 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT31MACLAN-2-LAN` Will Martin Landaluce win set 2 in the Tomas Machac vs Martin Landaluce match: 0.13/0.80 mid 46.5%, model 31.3% (projection_v2.0 (prediction ledger)) -- gap -15.2 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXATPEXACTMATCH-26OCT31MACLAN-MAC21` Will Tomas Machac win the Tomas Machac vs Martin Landaluce match by a set score of 2-1?: 0.14/0.28 mid 21.0%, model 29.5% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
  * `KXATPSETWINNER-26OCT31MACLAN-1-MAC` Will Tomas Machac win set 1 in the Tomas Machac vs Martin Landaluce match: 0.60/0.62 mid 61.0%, model 68.7% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT31MACLAN-1-LAN` Will Martin Landaluce win set 1 in the Tomas Machac vs Martin Landaluce match: 0.37/0.40 mid 38.5%, model 31.3% (projection_v2.0 (prediction ledger)) -- gap -7.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXATPEXACTMATCH-26OCT31MACLAN-LAN20` Will Martin Landaluce win the Tomas Machac vs Martin Landaluce match by a set score of 2-0?: 0.01/0.26 mid 13.5%, model 9.8% (projection_v2.0 (prediction ledger)) -- gap -3.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
  * `KXATPEXACTMATCH-26OCT31MACLAN-MAC20` Will Tomas Machac win the Tomas Machac vs Martin Landaluce match by a set score of 2-0?: 0.45/0.47 mid 46.0%, model 47.2% (projection_v2.0 (prediction ledger)) -- gap +1.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
  * `KXATPEXACTMATCH-26OCT31MACLAN-LAN21` Will Martin Landaluce win the Tomas Machac vs Martin Landaluce match by a set score of 2-1?: 0.08/0.19 mid 13.5%, model 13.5% (projection_v2.0 (prediction ledger)) -- gap -0.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ogura / Tamm vs Rifqi Fitriadi / Han -- M15 Singapore F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-31T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT31OGUTAMRIFHAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ogura / Tamm (`KXITFDOUBLES-26OCT31OGUTAMRIFHAN-OGUTAM`) | 0.42 / 0.60 (62) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rifqi Fitriadi / Han (`KXITFDOUBLES-26OCT31OGUTAMRIFHAN-RIFHAN`) | 0.34 / 0.52 (52) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Theo Arribage / Albano Olivetti vs Constantin Frantzen / Robin Haase -- ATP Basel SF

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-10-31 15:00Z
* Current expected start: 2026-10-31 12:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 11:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-31T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT31ARROLIFRAHAA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theo Arribage / Albano Olivetti (`KXATPDOUBLES-26OCT31ARROLIFRAHAA-ARROLI`) | 0.62 / 0.64 (1417) | 63.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Constantin Frantzen / Robin Haase (`KXATPDOUBLES-26OCT31ARROLIFRAHAA-FRAHAA`) | 0.35 / 0.37 (119) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Lucas Miedler / Neil Oberleitner vs Guido Andreozzi / Manuel Guinard -- ATP Vienna SF

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-10-31 15:00Z
* Current expected start: 2026-10-31 12:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 11:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-31T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT31MIEOBEANDGUI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Guido Andreozzi / Manuel Guinard (`KXATPDOUBLES-26OCT31MIEOBEANDGUI-ANDGUI`) | 0.35 / 0.41 (22) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lucas Miedler / Neil Oberleitner (`KXATPDOUBLES-26OCT31MIEOBEANDGUI-MIEOBE`) | 0.53 / 0.61 (283) | 57.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Aristarkh Safonov vs Amir Omarkhanov -- M15 Fergana SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-31T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210011:212788:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amir Omarkhanov (`KXITFMATCH-26OCT31SAFOMA-OMA`) | 0.90 / 0.91 (81) | 90.5% | 77.6% | 77.8% | 70.3% [68.0%-74.6%] | 89.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.9 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aristarkh Safonov (`KXITFMATCH-26OCT31SAFOMA-SAF`) | 0.07 / 0.10 (507) | 8.5% | 22.4% | 22.2% | 29.7% [25.4%-32.0%] | 10.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.9 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 401.0, B 2497.0; serve-point win A 56.5%, B 37.7%; Elo A 1274.7, B 1405.3; model uncertainty 0.0327
* Form inputs: days since last match A 187, B 14; matches on record A 44, B 76; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Guo / Yang vs Huang / Zelinskaya -- W35 Kunshan F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-31T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT31GUOYANHUAZEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Guo / Yang (`KXITFWDOUBLES-26OCT31GUOYANHUAZEL-GUOYAN`) | 0.21 / 0.41 (42) | 31.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Huang / Zelinskaya (`KXITFWDOUBLES-26OCT31GUOYANHUAZEL-HUAZEL`) | 0.52 / 0.71 (86) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Tallon Griekspoor vs Benjamin Bonzi -- ATP Paris Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-31 12:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 11:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-10-31T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126127:134868:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Benjamin Bonzi (`KXATPMATCH-26OCT31GRIBON-BON`) | 0.38 / 0.40 (1742) | 39.0% | 42.0% | 46.2% | 45.3% [42.9%-46.7%] | 38.4% | 37.4% | 38.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +3.0 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Tallon Griekspoor (`KXATPMATCH-26OCT31GRIBON-GRI`) | 0.60 / 0.61 (1504) | 60.5% | 58.0% | 53.8% | 54.7% [53.3%-57.1%] | 61.6% | 61.4% | 61.6% | MODEL_LONE_OUTLIER | PASS | -2.5 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5028.0, B 5634.0; serve-point win A 69.2%, B 32.4%; Elo A 1885.8, B 1823.5; model uncertainty 0.019
* Form inputs: days since last match A 2, B 10; matches on record A 693, B 800; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.014, surface_dev_loose +0.005, surface_dev_tight -0.004
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT31GRIBON-BON21` Will Benjamin Bonzi win the Tallon Griekspoor vs Benjamin Bonzi match by a set score of 2-1?: 0.01/0.23 mid 12.0%, model 22.1% (projection_v2.0 (prediction ledger)) -- gap +10.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31GRIBON-2-GRI` Will Tallon Griekspoor win set 2 in the Tallon Griekspoor vs Benjamin Bonzi match: 0.13/0.80 mid 46.5%, model 55.3% (projection_v2.0 (prediction ledger)) -- gap +8.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31GRIBON-GRI21` Will Tallon Griekspoor win the Tallon Griekspoor vs Benjamin Bonzi match by a set score of 2-1?: 0.11/0.28 mid 19.5%, model 27.4% (projection_v2.0 (prediction ledger)) -- gap +7.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31GRIBON-GRI20` Will Tallon Griekspoor win the Tallon Griekspoor vs Benjamin Bonzi match by a set score of 2-0?: 0.05/0.42 mid 23.5%, model 30.6% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31GRIBON-BON20` Will Benjamin Bonzi win the Tallon Griekspoor vs Benjamin Bonzi match by a set score of 2-0?: 0.06/0.27 mid 16.5%, model 20.0% (projection_v2.0 (prediction ledger)) -- gap +3.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31GRIBON-1-BON` Will Benjamin Bonzi win set 1 in the Tallon Griekspoor vs Benjamin Bonzi match: 0.41/0.44 mid 42.5%, model 44.7% (projection_v2.0 (prediction ledger)) -- gap +2.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31GRIBON-2-BON` Will Benjamin Bonzi win set 2 in the Tallon Griekspoor vs Benjamin Bonzi match: 0.13/0.80 mid 46.5%, model 44.7% (projection_v2.0 (prediction ledger)) -- gap -1.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31GRIBON-1-GRI` Will Tallon Griekspoor win set 1 in the Tallon Griekspoor vs Benjamin Bonzi match: 0.56/0.58 mid 57.0%, model 55.3% (projection_v2.0 (prediction ledger)) -- gap -1.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Zhibek Kulambayeva vs Yelyzaveta Kotliar -- WTA Chennai Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 12:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-31 12:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 11:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-31T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214992:245077:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yelyzaveta Kotliar (`KXWTAMATCH-26OCT31KULKOT-KOT`) | 0.57 / 0.58 (1066) | 57.5% | 63.7% | 53.2% | 57.5% [55.3%-60.6%] | 58.3% | 59.2% | 58.8% | MODEL_LONE_OUTLIER | PASS | +6.2 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Zhibek Kulambayeva (`KXWTAMATCH-26OCT31KULKOT-KUL`) | 0.41 / 0.42 (2008) | 41.5% | 36.2% | 46.8% | 42.5% [39.4%-44.7%] | 41.7% | 41.1% | 41.4% | MODEL_LONE_OUTLIER | PASS | -5.2 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2176.0, B 2950.0; serve-point win A 51.2%, B 46.2%; Elo A 1446.3, B 1545.2; model uncertainty 0.0262
* Form inputs: days since last match A 18, B 3; matches on record A 435, B 138; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.031, surface_dev_loose -0.026, surface_dev_tight +0.011
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT31KULKOT-2-KUL` Will Zhibek Kulambayeva win set 2 in the Zhibek Kulambayeva vs Yelyzaveta Kotliar match: 0.02/0.99 mid 50.5%, model 40.7% (projection_v2.0 (prediction ledger)) -- gap -9.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT31KULKOT-2-KOT` Will Yelyzaveta Kotliar win set 2 in the Zhibek Kulambayeva vs Yelyzaveta Kotliar match: 0.02/0.99 mid 50.5%, model 59.3% (projection_v2.0 (prediction ledger)) -- gap +8.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT31KULKOT-1-KOT` Will Yelyzaveta Kotliar win set 1 in the Zhibek Kulambayeva vs Yelyzaveta Kotliar match: 0.55/0.57 mid 56.0%, model 59.3% (projection_v2.0 (prediction ledger)) -- gap +3.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT31KULKOT-1-KUL` Will Zhibek Kulambayeva win set 1 in the Zhibek Kulambayeva vs Yelyzaveta Kotliar match: 0.43/0.45 mid 44.0%, model 40.7% (projection_v2.0 (prediction ledger)) -- gap -3.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; WIDE_SPREAD

## Mei Yamaguchi vs Zeel Desai -- WTA Chennai Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 12:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-31 12:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 11:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-31T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215163:215614:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zeel Desai (`KXWTAMATCH-26OCT31YAMDES-DES`) | 0.09 / 0.10 (124) | 9.5% | 37.9% | 69.3% | 56.9% [41.1%-63.5%] | 10.9% | 10.0% | 10.9% | MODEL_LONE_OUTLIER | WATCH | +28.4 pp | EXTREME (DATA_WARNING) | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Mei Yamaguchi (`KXWTAMATCH-26OCT31YAMDES-YAM`) | 0.89 / 0.90 (10) | 89.5% | 62.1% | 30.6% | 43.1% [36.5%-58.9%] | 89.1% | 88.8% | 89.1% | MODEL_LONE_OUTLIER | PASS | -27.4 pp | EXTREME (DATA_WARNING) | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3409.0, B 2475.0; serve-point win A 56.2%, B 46.1%; Elo A 1579.4, B 1470.8; model uncertainty 0.1124
* Form inputs: days since last match A 6, B 187; matches on record A 352, B 389; data quality B

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT31YAMDES-DES  (YES = Zeel Desai)
Model: 38%
Kalshi: 10%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight +0.011
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT31YAMDES-1-YAM` Will Mei Yamaguchi win set 1 in the Mei Yamaguchi vs Zeel Desai match: 0.83/0.85 mid 84.0%, model 58.2% (projection_v2.0 (prediction ledger)) -- gap -25.8 pp, EXTREME, DATA_WARNING, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT31YAMDES-1-DES` Will Zeel Desai win set 1 in the Mei Yamaguchi vs Zeel Desai match: 0.16/0.17 mid 16.5%, model 41.8% (projection_v2.0 (prediction ledger)) -- gap +25.3 pp, EXTREME, DATA_WARNING, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT31YAMDES-2-DES` Will Zeel Desai win set 2 in the Mei Yamaguchi vs Zeel Desai match: 0.03/0.98 mid 50.5%, model 41.8% (projection_v2.0 (prediction ledger)) -- gap -8.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT31YAMDES-2-YAM` Will Mei Yamaguchi win set 2 in the Mei Yamaguchi vs Zeel Desai match: 0.03/0.97 mid 50.0%, model 58.2% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sebastian Baez vs Damir Dzumhur -- ATP Paris Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-31 13:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 12:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-10-31T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:106000:202104:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sebastian Baez (`KXATPMATCH-26OCT31BAEDZU-BAE`) | 0.43 / 0.44 (8499) | 43.5% | 52.4% | 43.8% | 44.8% [43.3%-47.4%] | 44.4% | 43.3% | 44.4% | MODEL_LONE_OUTLIER | PASS | +8.9 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Damir Dzumhur (`KXATPMATCH-26OCT31BAEDZU-DZU`) | 0.56 / 0.57 (149) | 56.5% | 47.6% | 56.2% | 55.2% [52.6%-56.7%] | 55.6% | 55.2% | 55.6% | MODEL_LONE_OUTLIER | PASS | -8.9 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5268.0, B 5681.0; serve-point win A 58.7%, B 41.7%; Elo A 1712.8, B 1717.8; model uncertainty 0.0207
* Form inputs: days since last match A 7, B 9; matches on record A 506, B 1084; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.015, surface_dev_tight +0.021
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT31BAEDZU-BAE21` Will Sebastian Baez win the Sebastian Baez vs Damir Dzumhur match by a set score of 2-1?: 0.01/0.25 mid 13.0%, model 25.8% (projection_v2.0 (prediction ledger)) -- gap +12.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31BAEDZU-DZU21` Will Damir Dzumhur win the Sebastian Baez vs Damir Dzumhur match by a set score of 2-1?: 0.01/0.27 mid 14.0%, model 24.2% (projection_v2.0 (prediction ledger)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31BAEDZU-BAE20` Will Sebastian Baez win the Sebastian Baez vs Damir Dzumhur match by a set score of 2-0?: 0.01/0.32 mid 16.5%, model 26.6% (projection_v2.0 (prediction ledger)) -- gap +10.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31BAEDZU-1-BAE` Will Sebastian Baez win set 1 in the Sebastian Baez vs Damir Dzumhur match: 0.44/0.47 mid 45.5%, model 51.6% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31BAEDZU-1-DZU` Will Damir Dzumhur win set 1 in the Sebastian Baez vs Damir Dzumhur match: 0.53/0.55 mid 54.0%, model 48.4% (projection_v2.0 (prediction ledger)) -- gap -5.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31BAEDZU-2-BAE` Will Sebastian Baez win set 2 in the Sebastian Baez vs Damir Dzumhur match: 0.13/0.80 mid 46.5%, model 51.6% (projection_v2.0 (prediction ledger)) -- gap +5.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31BAEDZU-DZU20` Will Damir Dzumhur win the Sebastian Baez vs Damir Dzumhur match by a set score of 2-0?: 0.01/0.41 mid 21.0%, model 23.4% (projection_v2.0 (prediction ledger)) -- gap +2.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31BAEDZU-2-DZU` Will Damir Dzumhur win set 2 in the Sebastian Baez vs Damir Dzumhur match: 0.13/0.80 mid 46.5%, model 48.4% (projection_v2.0 (prediction ledger)) -- gap +1.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Felix Balshaw vs Yannick Hanfmann -- ATP Paris Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-31 13:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 12:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-10-31T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105870:213149:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felix Balshaw (`KXATPMATCH-26OCT31BALHAN-BAL`) | 0.40 / 0.41 (5) | 40.5% | 39.3% | 36.2% | 33.1% [28.8%-35.4%] | 40.6% | 39.0% | 40.6% | MODEL_LONE_OUTLIER | PASS | -1.2 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Yannick Hanfmann (`KXATPMATCH-26OCT31BALHAN-HAN`) | 0.58 / 0.59 (863) | 58.5% | 60.7% | 63.7% | 66.9% [64.6%-71.2%] | 59.4% | 59.2% | 59.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +2.2 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4110.0, B 5488.0; serve-point win A 65.5%, B 32.2%; Elo A 1607.2, B 1788.7; model uncertainty 0.0329
* Form inputs: days since last match A 10, B 3; matches on record A 116, B 705; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.017, surface_pool_high +0.018, surface_dev_loose +0.001, surface_dev_tight -0.001
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT31BALHAN-HAN21` Will Yannick Hanfmann win the Felix Balshaw vs Yannick Hanfmann match by a set score of 2-1?: 0.01/0.28 mid 14.5%, model 28.0% (projection_v2.0 (prediction ledger)) -- gap +13.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31BALHAN-2-HAN` Will Yannick Hanfmann win set 2 in the Felix Balshaw vs Yannick Hanfmann match: 0.13/0.80 mid 46.5%, model 57.2% (projection_v2.0 (prediction ledger)) -- gap +10.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31BALHAN-BAL21` Will Felix Balshaw win the Felix Balshaw vs Yannick Hanfmann match by a set score of 2-1?: 0.01/0.23 mid 12.0%, model 21.0% (projection_v2.0 (prediction ledger)) -- gap +9.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31BALHAN-HAN20` Will Yannick Hanfmann win the Felix Balshaw vs Yannick Hanfmann match by a set score of 2-0?: 0.04/0.46 mid 25.0%, model 32.7% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31BALHAN-2-BAL` Will Felix Balshaw win set 2 in the Felix Balshaw vs Yannick Hanfmann match: 0.13/0.80 mid 46.5%, model 42.8% (projection_v2.0 (prediction ledger)) -- gap -3.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31BALHAN-BAL20` Will Felix Balshaw win the Felix Balshaw vs Yannick Hanfmann match by a set score of 2-0?: 0.01/0.29 mid 15.0%, model 18.3% (projection_v2.0 (prediction ledger)) -- gap +3.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31BALHAN-1-HAN` Will Yannick Hanfmann win set 1 in the Felix Balshaw vs Yannick Hanfmann match: 0.55/0.58 mid 56.5%, model 57.2% (projection_v2.0 (prediction ledger)) -- gap +0.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31BALHAN-1-BAL` Will Felix Balshaw win set 1 in the Felix Balshaw vs Yannick Hanfmann match: 0.42/0.44 mid 43.0%, model 42.8% (projection_v2.0 (prediction ledger)) -- gap -0.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lorenzo Sonego vs Jaume Munar -- ATP Paris Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-31 13:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 12:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-10-31T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:132283:144719:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jaume Munar (`KXATPMATCH-26OCT31SONMUN-MUN`) | 0.61 / 0.62 (1465) | 61.5% | 63.7% | 66.8% | 64.0% [62.2%-65.8%] | 63.2% | 61.8% | 62.5% | MARKETS_AGREE | WATCH | +2.2 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Lorenzo Sonego (`KXATPMATCH-26OCT31SONMUN-SON`) | 0.38 / 0.39 (1035) | 38.5% | 36.3% | 33.2% | 36.0% [34.2%-37.8%] | 36.8% | 38.0% | 37.4% | MARKETS_AGREE | PASS | -2.2 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4676.0, B 4745.0; serve-point win A 63.3%, B 33.9%; Elo A 1769.7, B 1807.6; model uncertainty 0.0184
* Form inputs: days since last match A 6, B 12; matches on record A 701, B 746; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.000, surface_dev_loose -0.004, surface_dev_tight +0.014
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT31SONMUN-MUN21` Will Jaume Munar win the Lorenzo Sonego vs Jaume Munar match by a set score of 2-1?: 0.01/0.29 mid 15.0%, model 28.6% (projection_v2.0 (prediction ledger)) -- gap +13.6 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31SONMUN-MUN20` Will Jaume Munar win the Lorenzo Sonego vs Jaume Munar match by a set score of 2-0?: 0.01/0.47 mid 24.0%, model 35.1% (projection_v2.0 (prediction ledger)) -- gap +11.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31SONMUN-2-SON` Will Lorenzo Sonego win set 2 in the Lorenzo Sonego vs Jaume Munar match: 0.03/0.57 mid 30.0%, model 40.8% (projection_v2.0 (prediction ledger)) -- gap +10.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31SONMUN-SON21` Will Lorenzo Sonego win the Lorenzo Sonego vs Jaume Munar match by a set score of 2-1?: 0.02/0.21 mid 11.5%, model 19.7% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31SONMUN-2-MUN` Will Jaume Munar win set 2 in the Lorenzo Sonego vs Jaume Munar match: 0.36/0.97 mid 66.5%, model 59.2% (projection_v2.0 (prediction ledger)) -- gap -7.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31SONMUN-SON20` Will Lorenzo Sonego win the Lorenzo Sonego vs Jaume Munar match by a set score of 2-0?: 0.01/0.26 mid 13.5%, model 16.6% (projection_v2.0 (prediction ledger)) -- gap +3.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31SONMUN-1-MUN` Will Jaume Munar win set 1 in the Lorenzo Sonego vs Jaume Munar match: 0.57/0.59 mid 58.0%, model 59.2% (projection_v2.0 (prediction ledger)) -- gap +1.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31SONMUN-1-SON` Will Lorenzo Sonego win set 1 in the Lorenzo Sonego vs Jaume Munar match: 0.41/0.42 mid 41.5%, model 40.8% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Francisco Cerundolo / Tomas Martin Etcheverry vs Ryan Seggerman / Learner Tien -- ATP Vienna SF

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-10-31 16:10Z
* Current expected start: 2026-10-31 13:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 12:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-31T16:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT31CERETCSEGTIE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francisco Cerundolo / Tomas Martin Etcheverry (`KXATPDOUBLES-26OCT31CERETCSEGTIE-CERETC`) | 0.32 / 0.40 (13) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ryan Seggerman / Learner Tien (`KXATPDOUBLES-26OCT31CERETCSEGTIE-SEGTIE`) | 0.55 / 0.61 (60) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Anna Blinkova vs Noma Noha Akugue -- WTA 125K Courmayeur SF

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 16:30Z
* Current expected start: 2026-10-31 13:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 12:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · surface ? · scheduled 2026-10-31T16:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:215020:223333:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Blinkova (`KXWTACHALLENGERMATCH-26OCT31BLINOH-BLI`) | 0.67 / 0.68 (5933) | 67.5% | 64.2% | 30.6% | 41.0% [35.9%-57.4%] | -- | 67.4% | 67.4% | MODEL_LONE_OUTLIER | PASS | -3.3 pp | NORMAL | AGING | A / LIMITED | ALL_AGREE | VERIFIED |
| Noma Noha Akugue (`KXWTACHALLENGERMATCH-26OCT31BLINOH-NOH`) | 0.32 / 0.33 (5) | 32.5% | 35.8% | 69.4% | 59.0% [42.6%-64.1%] | -- | 32.5% | 32.5% | MODEL_LONE_OUTLIER | WATCH | +3.3 pp | NORMAL | AGING | A / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4417.0, B 4975.0; serve-point win A 55.8%, B 46.9%; Elo A 1940.9, B 1766.7; model uncertainty 0.1074
* Form inputs: days since last match A 2, B 3; matches on record A 634, B 347; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; THIN_DISPLAYED_SIZE

## Daniil Medvedev vs Carlos Alcaraz -- ATP Vienna SF

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 17:00Z
* Current expected start: 2026-10-31 14:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 13:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Clay · scheduled 2026-10-31T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:106421:207989:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlos Alcaraz (`KXATPMATCH-26OCT31MEDALC-ALC`) | 0.66 / 0.67 (132006) | 66.5% | 81.1% | 81.7% | 84.3% [80.9%-86.5%] | 65.8% | 66.3% | 66.0% | MODEL_LONE_OUTLIER | WATCH | +14.6 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Daniil Medvedev (`KXATPMATCH-26OCT31MEDALC-MED`) | 0.34 / 0.35 (103934) | 34.5% | 18.9% | 18.3% | 15.7% [13.5%-19.1%] | 34.2% | 33.8% | 34.0% | MODEL_LONE_OUTLIER | PASS | -15.6 pp | HIGH_REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 6370.0, B 5488.0; serve-point win A 56.4%, B 36.8%; Elo A 1936.1, B 2345.5; model uncertainty 0.0281
* Form inputs: days since last match A 2, B 2; matches on record A 877, B 478; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose -0.022, surface_dev_tight +0.024
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT31MEDALC-ALC4` Will Carlos Alcaraz win at least 3.5 more games than Daniil Medvedev?: 0.43/0.44 mid 43.5%, model 60.7% (projection_v2.0 (prediction ledger)) -- gap +17.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT31MEDALC-MED2` Will Daniil Medvedev win at least 1.5 more games than Carlos Alcaraz?: 0.23/0.37 mid 30.0%, model 14.4% (projection_v2.0 (prediction ledger)) -- gap -15.6 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31MEDALC-1-ALC` Will Carlos Alcaraz win set 1 in the Daniil Medvedev vs Carlos Alcaraz match: 0.58/0.59 mid 58.5%, model 72.2% (projection_v2.0 (prediction ledger)) -- gap +13.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31MEDALC-1-MED` Will Daniil Medvedev win set 1 in the Daniil Medvedev vs Carlos Alcaraz match: 0.39/0.42 mid 40.5%, model 27.8% (projection_v2.0 (prediction ledger)) -- gap -12.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31MEDALC-ALC20` Will Carlos Alcaraz win the Daniil Medvedev vs Carlos Alcaraz match by a set score of 2-0?: 0.39/0.40 mid 39.5%, model 52.1% (projection_v2.0 (prediction ledger)) -- gap +12.6 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31MEDALC-2-ALC` Will Carlos Alcaraz win set 2 in the Daniil Medvedev vs Carlos Alcaraz match: 0.59/0.62 mid 60.5%, model 72.2% (projection_v2.0 (prediction ledger)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31MEDALC-2-MED` Will Daniil Medvedev win set 2 in the Daniil Medvedev vs Carlos Alcaraz match: 0.36/0.40 mid 38.0%, model 27.8% (projection_v2.0 (prediction ledger)) -- gap -10.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31MEDALC-MED20` Will Daniil Medvedev win the Daniil Medvedev vs Carlos Alcaraz match by a set score of 2-0?: 0.17/0.18 mid 17.5%, model 7.8% (projection_v2.0 (prediction ledger)) -- gap -9.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT31MEDALC-18` Over 17.5 games: 0.86/0.94 mid 90.0%, model 83.4% (projection_v2.0 (prediction ledger)) -- gap -6.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT31MEDALC-23` Over 22.5 games: 0.52/0.54 mid 53.0%, model 47.0% (projection_v2.0 (prediction ledger)) -- gap -6.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31MEDALC-ALC21` Will Carlos Alcaraz win the Daniil Medvedev vs Carlos Alcaraz match by a set score of 2-1?: 0.23/0.24 mid 23.5%, model 29.0% (projection_v2.0 (prediction ledger)) -- gap +5.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31MEDALC-MED21` Will Daniil Medvedev win the Daniil Medvedev vs Carlos Alcaraz match by a set score of 2-1?: 0.14/0.17 mid 15.5%, model 11.2% (projection_v2.0 (prediction ledger)) -- gap -4.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT31MEDALC-28` Over 27.5 games: 0.28/0.32 mid 30.0%, model 28.4% (projection_v2.0 (prediction ledger)) -- gap -1.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT31MEDALC-ALC7` Will Carlos Alcaraz win at least 6.5 more games than Daniil Medvedev?: 0.01/0.36 mid 18.5%, model 19.6% (projection_v2.0 (prediction ledger)) -- gap +1.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Valentin Vacherot vs Taylor Fritz -- ATP Basel SF

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 17:00Z
* Current expected start: 2026-10-31 14:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 13:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-10-31T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126203:200473:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Taylor Fritz (`KXATPMATCH-26OCT31VACFRI-FRI`) | 0.73 / 0.74 (1854) | 73.5% | 70.3% | 71.3% | 71.2% [70.8%-72.1%] | 73.4% | 73.3% | 73.3% | MARKETS_AGREE | PASS | -3.2 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Valentin Vacherot (`KXATPMATCH-26OCT31VACFRI-VAC`) | 0.26 / 0.27 (19775) | 26.5% | 29.7% | 28.7% | 28.8% [27.9%-29.2%] | 26.7% | 26.9% | 26.8% | MARKETS_AGREE | PASS | +3.2 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4676.0, B 6643.0; serve-point win A 67.5%, B 27.9%; Elo A 1891.2, B 2055.6; model uncertainty 0.0067
* Form inputs: days since last match A 2, B 2; matches on record A 424, B 766; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.004, surface_dev_loose +0.004, surface_dev_tight -0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT31VACFRI-FRI20` Will Taylor Fritz win the Valentin Vacherot vs Taylor Fritz match by a set score of 2-0?: 0.48/0.51 mid 49.5%, model 40.8% (projection_v2.0 (prediction ledger)) -- gap -8.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT31VACFRI-21` Over 20.5 games: 0.70/0.76 mid 73.0%, model 80.7% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT31VACFRI-26` Over 25.5 games: 0.43/0.46 mid 44.5%, model 52.2% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT31VACFRI-FRI3` Will Taylor Fritz win at least 2.5 more games than Valentin Vacherot?: 0.56/0.57 mid 56.5%, model 50.0% (projection_v2.0 (prediction ledger)) -- gap -6.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31VACFRI-FRI21` Will Taylor Fritz win the Valentin Vacherot vs Taylor Fritz match by a set score of 2-1?: 0.21/0.25 mid 23.0%, model 29.5% (projection_v2.0 (prediction ledger)) -- gap +6.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31VACFRI-2-VAC` Will Valentin Vacherot win set 2 in the Valentin Vacherot vs Taylor Fritz match: 0.29/0.33 mid 31.0%, model 36.1% (projection_v2.0 (prediction ledger)) -- gap +5.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT31VACFRI-FRI6` Will Taylor Fritz win at least 5.5 more games than Valentin Vacherot?: 0.06/0.20 mid 13.0%, model 8.1% (projection_v2.0 (prediction ledger)) -- gap -4.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31VACFRI-2-FRI` Will Taylor Fritz win set 2 in the Valentin Vacherot vs Taylor Fritz match: 0.66/0.71 mid 68.5%, model 63.9% (projection_v2.0 (prediction ledger)) -- gap -4.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31VACFRI-VAC21` Will Valentin Vacherot win the Valentin Vacherot vs Taylor Fritz match by a set score of 2-1?: 0.11/0.15 mid 13.0%, model 16.7% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31VACFRI-1-FRI` Will Taylor Fritz win set 1 in the Valentin Vacherot vs Taylor Fritz match: 0.66/0.68 mid 67.0%, model 63.9% (projection_v2.0 (prediction ledger)) -- gap -3.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31VACFRI-1-VAC` Will Valentin Vacherot win set 1 in the Valentin Vacherot vs Taylor Fritz match: 0.32/0.34 mid 33.0%, model 36.1% (projection_v2.0 (prediction ledger)) -- gap +3.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT31VACFRI-31` Over 30.5 games: 0.27/0.36 mid 31.5%, model 34.3% (projection_v2.0 (prediction ledger)) -- gap +2.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31VACFRI-VAC20` Will Valentin Vacherot win the Valentin Vacherot vs Taylor Fritz match by a set score of 2-0?: 0.11/0.14 mid 12.5%, model 13.0% (projection_v2.0 (prediction ledger)) -- gap +0.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT31VACFRI-VAC2` Will Valentin Vacherot win at least 1.5 more games than Taylor Fritz?: 0.15/0.29 mid 22.0%, model 22.2% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; WIDE_SPREAD

## Julia Riera vs Julia Grabher -- WTA 125K Curitiba SF

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 17:00Z
* Current expected start: 2026-10-31 14:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 13:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · Clay · scheduled 2026-10-31T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:211814:220699:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julia Grabher (`KXWTACHALLENGERMATCH-26OCT31RIEGRA-GRA`) | 0.52 / 0.54 (591) | 53.0% | 61.3% | 61.6% | 63.1% [61.1%-63.6%] | 52.0% | 53.3% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +8.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Julia Riera (`KXWTACHALLENGERMATCH-26OCT31RIEGRA-RIE`) | 0.46 / 0.48 (34) | 47.0% | 38.7% | 38.4% | 36.9% [36.4%-39.0%] | 48.0% | 47.9% | -- | INSUFFICIENT_INPUTS | PASS | -8.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3855.0, B 3872.0; serve-point win A 52.9%, B 44.9%; Elo A 1719.9, B 1837.1; model uncertainty 0.0127
* Form inputs: days since last match A 2, B 2; matches on record A 387, B 704; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.005, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Gijs Brouwer vs Volodymyr Iakubenko -- M15 Sharm ElSheikh SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:133835:212246:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gijs Brouwer (`KXITFMATCH-26OCT31BROIAK-BRO`) | 0.58 / 0.64 (2101) | 61.0% | 80.3% | 61.3% | 75.9% [69.4%-86.3%] | -- | -- | -- | -- | PASS | +19.3 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Volodymyr Iakubenko (`KXITFMATCH-26OCT31BROIAK-IAK`) | 0.35 / 0.38 (165) | 36.5% | 19.7% | 38.7% | 24.1% [13.7%-30.6%] | -- | -- | -- | -- | PASS | -16.8 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1950.0, B 1388.0; serve-point win A 62.3%, B 44.3%; Elo A 1610.4, B 1301.7; model uncertainty 0.0841
* Form inputs: days since last match A 54, B 194; matches on record A 513, B 47; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT31BROIAK-BRO  (YES = Gijs Brouwer)
Model: 80%
Kalshi: 61%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.031, surface_pool_high -0.042, surface_dev_loose -0.004, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Miles Jones vs Pablo Perez Ramos -- M15 Heraklion SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-31T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT31JONPER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miles Jones (`KXITFMATCH-26OCT31JONPER-JON`) | 0.54 / 0.55 (179) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pablo Perez Ramos (`KXITFMATCH-26OCT31JONPER-PER`) | 0.43 / 0.46 (543) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jannik Maute vs Yurii Dzhavakian -- M15 Sharm ElSheikh SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:122113:210339:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yurii Dzhavakian (`KXITFMATCH-26OCT31MAUDZH-DZH`) | 0.29 / 0.35 (0) | 32.0% | 79.7% | 72.9% | 79.4% [77.1%-82.1%] | -- | -- | -- | -- | PASS | +47.7 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jannik Maute (`KXITFMATCH-26OCT31MAUDZH-MAU`) | 0.62 / 0.69 (1) | 65.5% | 20.3% | 27.1% | 20.6% [17.9%-22.9%] | -- | -- | -- | -- | PASS | -45.2 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 181.0, B 5142.0; serve-point win A 52.9%, B 40.8%; Elo A 1138.3, B 1383.3; model uncertainty 0.0251
* Form inputs: days since last match A 201, B 187; matches on record A 29, B 436; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT31MAUDZH-DZH  (YES = Yurii Dzhavakian)
Model: 80%
Kalshi: 32%
Gap: +48 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.022, surface_pool_high +0.023, surface_dev_loose -0.008, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Benjamin Pietri vs Alexander Chang -- M15 Heraklion SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202125:212959:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Chang (`KXITFMATCH-26OCT31PIECHA-CHA`) | 0.46 / 0.49 (136) | 47.5% | 44.4% | 53.6% | 46.9% [45.4%-49.0%] | 47.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Benjamin Pietri (`KXITFMATCH-26OCT31PIECHA-PIE`) | 0.50 / 0.54 (308) | 52.0% | 55.6% | 46.4% | 53.1% [51.0%-54.6%] | 52.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1540.0, B 562.0; serve-point win A 61.6%, B 39.5%; Elo A 1291.0, B 1253.8; model uncertainty 0.0181
* Form inputs: days since last match A 54, B 425; matches on record A 233, B 10; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.010, surface_dev_loose -0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daria Egorova vs Viktoria Hruncakova -- W50 Istanbul SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214149:266864:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daria Egorova (`KXITFWMATCH-26OCT31EGOHRU-EGO`) | 0.56 / 0.59 (133) | 57.5% | 50.1% | 76.9% | 66.8% [50.5%-73.6%] | 57.0% | -- | 57.0% | MARKETS_AGREE | WATCH | -7.4 pp | NORMAL | AGING | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Viktoria Hruncakova (`KXITFWMATCH-26OCT31EGOHRU-HRU`) | 0.40 / 0.42 (19) | 41.0% | 49.9% | 23.1% | 33.2% [26.4%-49.5%] | 43.0% | -- | 43.0% | EXTERNAL_LONE_OUTLIER | PASS | +8.9 pp | NORMAL | AGING | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2142.0, B 3899.0; serve-point win A 57.6%, B 42.4%; Elo A 1672.8, B 1669.1; model uncertainty 0.1152
* Form inputs: days since last match A 32, B 16; matches on record A 86, B 723; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.019, surface_dev_loose +0.009, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aya El Sayed vs Kristina Dmitruk -- W15 Sharm ElSheikh SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220808:221083:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kristina Dmitruk (`KXITFWMATCH-26OCT31ELSDMI-DMI`) | 0.91 / 0.94 (230) | 92.5% | 96.7% | 91.7% | 93.2% [92.3%-94.0%] | -- | -- | -- | -- | PASS | +4.2 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aya El Sayed (`KXITFWMATCH-26OCT31ELSDMI-ELS`) | 0.06 / 0.10 (14) | 8.0% | 3.3% | 8.3% | 6.8% [6.0%-7.7%] | -- | -- | -- | -- | PASS | -4.7 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 698.0, B 1766.0; serve-point win A 47.3%, B 38.8%; Elo A 1200.5, B 1675.9; model uncertainty 0.0086
* Form inputs: days since last match A 327, B 285; matches on record A 81, B 214; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.004, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Polina Kuharenko vs Rikke De Koning -- W15 Sharm ElSheikh SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:252584:263626:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rikke De Koning (`KXITFWMATCH-26OCT31KUHDEK-DEK`) | 0.42 / 0.43 (224) | 42.5% | 14.9% | 10.0% | 16.5% [12.5%-24.8%] | -- | -- | -- | -- | PASS | -27.6 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Polina Kuharenko (`KXITFWMATCH-26OCT31KUHDEK-KUH`) | 0.52 / 0.56 (56) | 54.0% | 85.1% | 90.0% | 83.5% [75.2%-87.5%] | -- | -- | -- | -- | WATCH | +31.1 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1767.0, B 1253.0; serve-point win A 57.6%, B 50.2%; Elo A 1462.7, B 1256.5; model uncertainty 0.0612
* Form inputs: days since last match A 236, B 187; matches on record A 55, B 139; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT31KUHDEK-KUH  (YES = Polina Kuharenko)
Model: 85%
Kalshi: 54%
Gap: +31 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.003, surface_pool_high +0.003, surface_dev_loose +0.022, surface_dev_tight -0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alex Molcan vs Daniel Altmaier -- ATP Paris Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-31 14:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 13:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-10-31T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:127157:144684:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Altmaier (`KXATPMATCH-26OCT31MOLALT-ALT`) | 0.43 / 0.44 (147) | 43.5% | 42.7% | 33.5% | 37.2% [34.9%-41.6%] | 44.4% | 43.5% | -- | INSUFFICIENT_INPUTS | PASS | -0.8 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alex Molcan (`KXATPMATCH-26OCT31MOLALT-MOL`) | 0.55 / 0.57 (82) | 56.0% | 57.3% | 66.5% | 62.8% [58.4%-65.1%] | 55.6% | 56.4% | -- | INSUFFICIENT_INPUTS | WATCH | +1.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4355.0, B 5885.0; serve-point win A 64.4%, B 37.1%; Elo A 1749.1, B 1740.3; model uncertainty 0.0334
* Form inputs: days since last match A 6, B 2; matches on record A 554, B 732; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.001
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT31MOLALT-MOL21` Will Alex Molcan win the Alex Molcan vs Daniel Altmaier match by a set score of 2-1?: 0.01/0.28 mid 14.5%, model 27.2% (projection_v2.0 (prediction ledger)) -- gap +12.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31MOLALT-ALT21` Will Daniel Altmaier win the Alex Molcan vs Daniel Altmaier match by a set score of 2-1?: 0.01/0.24 mid 12.5%, model 22.3% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31MOLALT-MOL20` Will Alex Molcan win the Alex Molcan vs Daniel Altmaier match by a set score of 2-0?: 0.01/0.41 mid 21.0%, model 30.1% (projection_v2.0 (prediction ledger)) -- gap +9.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31MOLALT-2-MOL` Will Alex Molcan win set 2 in the Alex Molcan vs Daniel Altmaier match: 0.13/0.80 mid 46.5%, model 54.9% (projection_v2.0 (prediction ledger)) -- gap +8.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31MOLALT-ALT20` Will Daniel Altmaier win the Alex Molcan vs Daniel Altmaier match by a set score of 2-0?: 0.06/0.31 mid 18.5%, model 20.3% (projection_v2.0 (prediction ledger)) -- gap +1.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31MOLALT-2-ALT` Will Daniel Altmaier win set 2 in the Alex Molcan vs Daniel Altmaier match: 0.13/0.80 mid 46.5%, model 45.1% (projection_v2.0 (prediction ledger)) -- gap -1.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31MOLALT-1-ALT` Will Daniel Altmaier win set 1 in the Alex Molcan vs Daniel Altmaier match: 0.43/0.46 mid 44.5%, model 45.1% (projection_v2.0 (prediction ledger)) -- gap +0.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31MOLALT-1-MOL` Will Alex Molcan win set 1 in the Alex Molcan vs Daniel Altmaier match: 0.54/0.56 mid 55.0%, model 54.9% (projection_v2.0 (prediction ledger)) -- gap -0.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Adolfo Daniel Vallejo vs Grigor Dimitrov -- ATP Paris Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-31 14:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 13:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-10-31T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105777:209226:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Grigor Dimitrov (`KXATPMATCH-26OCT31VALDIM-DIM`) | 0.49 / 0.51 (1281) | 50.0% | 55.3% | 57.0% | 65.1% [61.8%-70.5%] | 46.8% | 46.8% | 46.8% | ALL_THREE_DISAGREE | SHADOW_BET | +5.3 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Adolfo Daniel Vallejo (`KXATPMATCH-26OCT31VALDIM-VAL`) | 0.49 / 0.51 (3794) | 50.0% | 44.7% | 43.0% | 34.9% [29.5%-38.2%] | 53.2% | 53.2% | 53.2% | ALL_THREE_DISAGREE | PASS | -5.3 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5609.0, B 3456.0; serve-point win A 63.2%, B 35.8%; Elo A 1709.1, B 1959.6; model uncertainty 0.0435
* Form inputs: days since last match A 7, B 4; matches on record A 229, B 993; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose +0.001, surface_dev_tight -0.010
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT31VALDIM-DIM21` Will Grigor Dimitrov win the Adolfo Daniel Vallejo vs Grigor Dimitrov match by a set score of 2-1?: 0.01/0.26 mid 13.5%, model 26.6% (projection_v2.0 (prediction ledger)) -- gap +13.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31VALDIM-DIM20` Will Grigor Dimitrov win the Adolfo Daniel Vallejo vs Grigor Dimitrov match by a set score of 2-0?: 0.01/0.33 mid 17.0%, model 28.7% (projection_v2.0 (prediction ledger)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31VALDIM-VAL21` Will Adolfo Daniel Vallejo win the Adolfo Daniel Vallejo vs Grigor Dimitrov match by a set score of 2-1?: 0.01/0.28 mid 14.5%, model 23.1% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31VALDIM-2-DIM` Will Grigor Dimitrov win set 2 in the Adolfo Daniel Vallejo vs Grigor Dimitrov match: 0.13/0.80 mid 46.5%, model 53.5% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31VALDIM-VAL20` Will Adolfo Daniel Vallejo win the Adolfo Daniel Vallejo vs Grigor Dimitrov match by a set score of 2-0?: 0.01/0.38 mid 19.5%, model 21.6% (projection_v2.0 (prediction ledger)) -- gap +2.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31VALDIM-1-DIM` Will Grigor Dimitrov win set 1 in the Adolfo Daniel Vallejo vs Grigor Dimitrov match: 0.50/0.53 mid 51.5%, model 53.5% (projection_v2.0 (prediction ledger)) -- gap +2.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31VALDIM-1-VAL` Will Adolfo Daniel Vallejo win set 1 in the Adolfo Daniel Vallejo vs Grigor Dimitrov match: 0.47/0.50 mid 48.5%, model 46.5% (projection_v2.0 (prediction ledger)) -- gap -2.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31VALDIM-2-VAL` Will Adolfo Daniel Vallejo win set 2 in the Adolfo Daniel Vallejo vs Grigor Dimitrov match: 0.13/0.80 mid 46.5%, model 46.5% (projection_v2.0 (prediction ledger)) -- gap -0.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Burtsev / Filaretov vs Hrazdil / Lakshmanan -- M15 Fergana F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-31T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT31BURFILHRALAK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Burtsev / Filaretov (`KXITFDOUBLES-26OCT31BURFILHRALAK-BURFIL`) | 0.05 / 0.90 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hrazdil / Lakshmanan (`KXITFDOUBLES-26OCT31BURFILHRALAK-HRALAK`) | 0.05 / 0.90 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nuno Borges vs Adrian Mannarino -- ATP Paris Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-31 15:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 14:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-10-31T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105173:132686:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nuno Borges (`KXATPMATCH-26OCT31BORMAN-BOR`) | 0.61 / 0.62 (139) | 61.5% | 64.5% | 61.6% | 60.7% [59.7%-61.6%] | 61.6% | 61.0% | 61.6% | MODEL_LONE_OUTLIER | PASS | +3.0 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Adrian Mannarino (`KXATPMATCH-26OCT31BORMAN-MAN`) | 0.37 / 0.39 (935) | 38.0% | 35.5% | 38.4% | 39.4% [38.4%-40.3%] | 38.4% | 38.9% | 38.4% | MARKETS_AGREE | PASS | -2.5 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5889.0, B 5560.0; serve-point win A 67.0%, B 36.0%; Elo A 1868.6, B 1804.1; model uncertainty 0.0095
* Form inputs: days since last match A 3, B 4; matches on record A 552, B 1323; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose +0.004, surface_dev_tight +0.000
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT31BORMAN-2-BOR` Will Nuno Borges win set 2 in the Nuno Borges vs Adrian Mannarino match: 0.13/0.80 mid 46.5%, model 59.8% (projection_v2.0 (prediction ledger)) -- gap +13.3 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31BORMAN-BOR20` Will Nuno Borges win the Nuno Borges vs Adrian Mannarino match by a set score of 2-0?: 0.01/0.44 mid 22.5%, model 35.8% (projection_v2.0 (prediction ledger)) -- gap +13.3 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31BORMAN-BOR21` Will Nuno Borges win the Nuno Borges vs Adrian Mannarino match by a set score of 2-1?: 0.01/0.30 mid 15.5%, model 28.7% (projection_v2.0 (prediction ledger)) -- gap +13.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31BORMAN-MAN21` Will Adrian Mannarino win the Nuno Borges vs Adrian Mannarino match by a set score of 2-1?: 0.01/0.23 mid 12.0%, model 19.3% (projection_v2.0 (prediction ledger)) -- gap +7.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31BORMAN-2-MAN` Will Adrian Mannarino win set 2 in the Nuno Borges vs Adrian Mannarino match: 0.13/0.80 mid 46.5%, model 40.2% (projection_v2.0 (prediction ledger)) -- gap -6.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31BORMAN-MAN20` Will Adrian Mannarino win the Nuno Borges vs Adrian Mannarino match by a set score of 2-0?: 0.01/0.27 mid 14.0%, model 16.2% (projection_v2.0 (prediction ledger)) -- gap +2.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31BORMAN-1-BOR` Will Nuno Borges win set 1 in the Nuno Borges vs Adrian Mannarino match: 0.57/0.59 mid 58.0%, model 59.8% (projection_v2.0 (prediction ledger)) -- gap +1.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31BORMAN-1-MAN` Will Adrian Mannarino win set 1 in the Nuno Borges vs Adrian Mannarino match: 0.41/0.43 mid 42.0%, model 40.2% (projection_v2.0 (prediction ledger)) -- gap -1.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## N. Sriram Balaji / Evan King vs Gonzalo Escobar / Niki Kaliyanda Poonacha -- ATP Challenger Brest F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-31T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT31BALKINESCKAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N. Sriram Balaji / Evan King (`KXATPCHALLENGERDOUBLES-26OCT31BALKINESCKAL-BALKIN`) | 0.05 / 0.95 (216) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gonzalo Escobar / Niki Kaliyanda Poonacha (`KXATPCHALLENGERDOUBLES-26OCT31BALKINESCKAL-ESCKAL`) | 0.05 / 0.95 (216) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Lilian Marmousez vs Benito Sanchez Martinez -- M15 Monastir SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208421:209917:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lilian Marmousez (`KXITFMATCH-26OCT31MARSAN-MAR`) | 0.46 / 0.49 (212) | 47.5% | 65.4% | 71.1% | 68.8% [63.6%-74.1%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +17.9 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Benito Sanchez Martinez (`KXITFMATCH-26OCT31MARSAN-SAN`) | 0.50 / 0.52 (189) | 51.0% | 34.6% | 28.9% | 31.2% [25.9%-36.4%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -16.4 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2574.0, B 681.0; serve-point win A 61.5%, B 41.6%; Elo A 1554.5, B 1423.3; model uncertainty 0.0522
* Form inputs: days since last match A 159, B 26; matches on record A 272, B 38; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT31MARSAN-MAR  (YES = Lilian Marmousez)
Model: 65%
Kalshi: 48%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.052, surface_pool_high -0.052, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Giovanni Oradini vs Simone Massellani -- M15 Selva Gardena F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132831:214436:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Simone Massellani (`KXITFMATCH-26OCT31ORAMAS-MAS`) | 0.34 / 0.38 (545) | 36.0% | 17.1% | 23.5% | 23.9% [21.9%-26.4%] | 36.2% | -- | 36.2% | MODEL_LONE_OUTLIER | PASS | -18.9 pp | HIGH_REVIEW | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Giovanni Oradini (`KXITFMATCH-26OCT31ORAMAS-ORA`) | 0.61 / 0.62 (259) | 61.5% | 82.9% | 76.5% | 76.1% [73.6%-78.1%] | 63.8% | -- | 63.8% | KALSHI_LONE_OUTLIER | PASS | +21.4 pp | HIGH_REVIEW | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2852.0, B 263.0; serve-point win A 64.0%, B 43.4%; Elo A 1436.6, B 1236.9; model uncertainty 0.0224
* Form inputs: days since last match A 40, B 19; matches on record A 337, B 7; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT31ORAMAS-ORA  (YES = Giovanni Oradini)
Model: 83%
Kalshi: 62%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.025, surface_dev_loose +0.004, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sharma / Singh vs Ianin / Ibrahim -- M15 Sharm ElSheikh F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-31T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT31SHASINIANIBR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ianin / Ibrahim (`KXITFDOUBLES-26OCT31SHASINIANIBR-IANIBR`) | 0.41 / 0.63 (67) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sharma / Singh (`KXITFDOUBLES-26OCT31SHASINIANIBR-SHASIN`) | 0.31 / 0.53 (53) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Nicolas Tepmahc vs Aziz Ouakaa -- M15 Monastir SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200297:208168:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aziz Ouakaa (`KXITFMATCH-26OCT31TEPOUA-OUA`) | 0.48 / 0.51 (233) | 49.5% | 42.8% | 30.7% | 36.0% [32.1%-47.4%] | 50.0% | -- | 50.0% | MODEL_LONE_OUTLIER | PASS | -6.7 pp | NORMAL | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Nicolas Tepmahc (`KXITFMATCH-26OCT31TEPOUA-TEP`) | 0.47 / 0.51 (203) | 49.0% | 57.2% | 69.3% | 64.0% [52.6%-67.9%] | 50.0% | -- | 50.0% | MODEL_LONE_OUTLIER | WATCH | +8.2 pp | NORMAL | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3348.0, B 3444.0; serve-point win A 56.1%, B 45.3%; Elo A 1365.3, B 1357.4; model uncertainty 0.0765
* Form inputs: days since last match A 187, B 82; matches on record A 237, B 439; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## El Sayed / Popovic vs Sedenkova / Shmeleva -- W15 Sharm ElSheikh F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-31T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT31ELSPOPSEDSHM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| El Sayed / Popovic (`KXITFWDOUBLES-26OCT31ELSPOPSEDSHM-ELSPOP`) | 0.05 / 0.90 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sedenkova / Shmeleva (`KXITFWDOUBLES-26OCT31ELSPOPSEDSHM-SEDSHM`) | 0.05 / 0.90 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Anna Kubareva vs Nastasja Schunk -- W50 Istanbul SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215707:221768:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Kubareva (`KXITFWMATCH-26OCT31KUBSCH-KUB`) | 0.36 / 0.38 (241) | 37.0% | 30.9% | 68.0% | 56.4% [36.4%-64.6%] | -- | -- | -- | -- | WATCH | -6.0 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nastasja Schunk (`KXITFWMATCH-26OCT31KUBSCH-SCH`) | 0.60 / 0.63 (141) | 61.5% | 69.0% | 32.0% | 43.6% [35.4%-63.6%] | -- | -- | -- | -- | PASS | +7.5 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2121.0, B 2120.0; serve-point win A 51.3%, B 45.0%; Elo A 1482.6, B 1548.5; model uncertainty 0.1411
* Form inputs: days since last match A 208, B 44; matches on record A 345, B 249; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.043, surface_pool_high +0.052, surface_dev_loose +0.016, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marie Vogt vs Mariia Lazarenko -- W15 Monastir SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-31T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT31VOGLAZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mariia Lazarenko (`KXITFWMATCH-26OCT31VOGLAZ-LAZ`) | 0.34 / 0.36 (6) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marie Vogt (`KXITFWMATCH-26OCT31VOGLAZ-VOG`) | 0.63 / 0.66 (2742) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chenting Zhu vs Kayo Nishimura -- W15 Monastir SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260613:264064:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kayo Nishimura (`KXITFWMATCH-26OCT31ZHUNIS-NIS`) | 0.49 / 0.50 (100) | 49.5% | 48.1% | 58.0% | 57.5% [56.9%-58.0%] | -- | -- | -- | -- | WATCH | -1.4 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Chenting Zhu (`KXITFWMATCH-26OCT31ZHUNIS-ZHU`) | 0.48 / 0.50 (11) | 49.0% | 51.9% | 42.0% | 42.5% [42.0%-43.1%] | -- | -- | -- | -- | PASS | +2.9 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2166.0, B 2288.0; serve-point win A 52.6%, B 47.7%; Elo A 1492.8, B 1542.8; model uncertainty 0.0053
* Form inputs: days since last match A 31, B 187; matches on record A 99, B 161; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexander Zverev vs Alex de Minaur -- ATP Vienna SF

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 18:30Z
* Current expected start: 2026-10-31 15:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 14:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Clay · scheduled 2026-10-31T18:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:100644:200282:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex de Minaur (`KXATPMATCH-26OCT31ZVEDE-DE`) | 0.30 / 0.31 (116) | 30.5% | 28.2% | 28.2% | 27.4% [25.7%-29.2%] | 30.9% | 30.6% | 30.7% | MODEL_LONE_OUTLIER | PASS | -2.3 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Alexander Zverev (`KXATPMATCH-26OCT31ZVEDE-ZVE`) | 0.69 / 0.70 (4515) | 69.5% | 71.8% | 71.8% | 72.6% [70.8%-74.4%] | 69.1% | 69.5% | 69.3% | MODEL_LONE_OUTLIER | WATCH | +2.3 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 8170.0, B 6479.0; serve-point win A 65.8%, B 38.8%; Elo A 2158.0, B 1944.3; model uncertainty 0.0175
* Form inputs: days since last match A 2, B 3; matches on record A 938, B 691; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose +0.017, surface_dev_tight -0.018
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT31ZVEDE-ZVE21` Will Alexander Zverev win the Alexander Zverev vs Alex de Minaur match by a set score of 2-1?: 0.17/0.25 mid 21.0%, model 29.6% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT31ZVEDE-23` Over 22.5 games: 0.49/0.51 mid 50.0%, model 56.0% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31ZVEDE-2-ZVE` Will Alexander Zverev win set 2 in the Alexander Zverev vs Alex de Minaur match: 0.54/0.66 mid 60.0%, model 65.0% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT31ZVEDE-28` Over 27.5 games: 0.30/0.35 mid 32.5%, model 36.4% (projection_v2.0 (prediction ledger)) -- gap +4.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT31ZVEDE-ZVE7` Will Alexander Zverev win at least 6.5 more games than Alex de Minaur?: 0.07/0.20 mid 13.5%, model 9.8% (projection_v2.0 (prediction ledger)) -- gap -3.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31ZVEDE-DE21` Will Alex de Minaur win the Alexander Zverev vs Alex de Minaur match by a set score of 2-1?: 0.08/0.18 mid 13.0%, model 15.9% (projection_v2.0 (prediction ledger)) -- gap +2.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31ZVEDE-ZVE20` Will Alexander Zverev win the Alexander Zverev vs Alex de Minaur match by a set score of 2-0?: 0.36/0.44 mid 40.0%, model 42.3% (projection_v2.0 (prediction ledger)) -- gap +2.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31ZVEDE-2-DE` Will Alex de Minaur win set 2 in the Alexander Zverev vs Alex de Minaur match: 0.26/0.48 mid 37.0%, model 35.0% (projection_v2.0 (prediction ledger)) -- gap -2.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT31ZVEDE-DE2` Will Alex de Minaur win at least 1.5 more games than Alexander Zverev?: 0.17/0.31 mid 24.0%, model 22.1% (projection_v2.0 (prediction ledger)) -- gap -1.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT31ZVEDE-18` Over 17.5 games: 0.87/0.94 mid 90.5%, model 91.1% (projection_v2.0 (prediction ledger)) -- gap +0.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31ZVEDE-1-DE` Will Alex de Minaur win set 1 in the Alexander Zverev vs Alex de Minaur match: 0.34/0.37 mid 35.5%, model 35.0% (projection_v2.0 (prediction ledger)) -- gap -0.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31ZVEDE-1-ZVE` Will Alexander Zverev win set 1 in the Alexander Zverev vs Alex de Minaur match: 0.63/0.66 mid 64.5%, model 65.0% (projection_v2.0 (prediction ledger)) -- gap +0.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31ZVEDE-DE20` Will Alex de Minaur win the Alexander Zverev vs Alex de Minaur match by a set score of 2-0?: 0.07/0.17 mid 12.0%, model 12.2% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT31ZVEDE-ZVE4` Will Alexander Zverev win at least 3.5 more games than Alex de Minaur?: 0.45/0.47 mid 46.0%, model 46.1% (projection_v2.0 (prediction ledger)) -- gap +0.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jiri Lehecka vs Jan-Lennard Struff -- ATP Basel SF

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-31 19:00Z
* Current expected start: 2026-10-31 16:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-31 02:30Z
* Recommended handicap-by time: 2026-10-31 15:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-10-31T19:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105526:208103:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jiri Lehecka (`KXATPMATCH-26OCT31LEHSTR-LEH`) | 0.65 / 0.66 (55) | 65.5% | 75.3% | 72.4% | 71.6% [69.6%-73.1%] | 65.8% | 67.4% | 66.6% | MARKETS_AGREE | SHADOW_BET | +9.8 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Jan-Lennard Struff (`KXATPMATCH-26OCT31LEHSTR-STR`) | 0.33 / 0.34 (2484) | 33.5% | 24.7% | 27.7% | 28.4% [26.9%-30.4%] | 34.2% | 32.5% | 33.4% | MODEL_LONE_OUTLIER | PASS | -8.8 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5638.0, B 5412.0; serve-point win A 71.4%, B 34.4%; Elo A 1983.7, B 1825.6; model uncertainty 0.0177
* Form inputs: days since last match A 2, B 2; matches on record A 461, B 1073; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.016, surface_dev_loose +0.012, surface_dev_tight -0.008
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT31LEHSTR-STR2` Will Jan-Lennard Struff win at least 1.5 more games than Jiri Lehecka?: 0.21/0.33 mid 27.0%, model 18.3% (projection_v2.0 (prediction ledger)) -- gap -8.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT31LEHSTR-LEH3` Will Jiri Lehecka win at least 2.5 more games than Jan-Lennard Struff?: 0.50/0.51 mid 50.5%, model 57.3% (projection_v2.0 (prediction ledger)) -- gap +6.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31LEHSTR-LEH21` Will Jiri Lehecka win the Jiri Lehecka vs Jan-Lennard Struff match by a set score of 2-1?: 0.21/0.25 mid 23.0%, model 29.6% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31LEHSTR-STR20` Will Jan-Lennard Struff win the Jiri Lehecka vs Jan-Lennard Struff match by a set score of 2-0?: 0.16/0.18 mid 17.0%, model 10.5% (projection_v2.0 (prediction ledger)) -- gap -6.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT31LEHSTR-1-LEH` Will Jiri Lehecka win set 1 in the Jiri Lehecka vs Jan-Lennard Struff match: 0.61/0.64 mid 62.5%, model 67.6% (projection_v2.0 (prediction ledger)) -- gap +5.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31LEHSTR-1-STR` Will Jan-Lennard Struff win set 1 in the Jiri Lehecka vs Jan-Lennard Struff match: 0.36/0.39 mid 37.5%, model 32.4% (projection_v2.0 (prediction ledger)) -- gap -5.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31LEHSTR-2-LEH` Will Jiri Lehecka win set 2 in the Jiri Lehecka vs Jan-Lennard Struff match: 0.60/0.65 mid 62.5%, model 67.6% (projection_v2.0 (prediction ledger)) -- gap +5.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT31LEHSTR-2-STR` Will Jan-Lennard Struff win set 2 in the Jiri Lehecka vs Jan-Lennard Struff match: 0.35/0.40 mid 37.5%, model 32.4% (projection_v2.0 (prediction ledger)) -- gap -5.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT31LEHSTR-31` Over 30.5 games: 0.22/0.28 mid 25.0%, model 29.7% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT31LEHSTR-21` Over 20.5 games: 0.70/0.73 mid 71.5%, model 75.9% (projection_v2.0 (prediction ledger)) -- gap +4.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31LEHSTR-LEH20` Will Jiri Lehecka win the Jiri Lehecka vs Jan-Lennard Struff match by a set score of 2-0?: 0.40/0.43 mid 41.5%, model 45.7% (projection_v2.0 (prediction ledger)) -- gap +4.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT31LEHSTR-26` Over 25.5 games: 0.45/0.47 mid 46.0%, model 47.9% (projection_v2.0 (prediction ledger)) -- gap +1.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT31LEHSTR-STR21` Will Jan-Lennard Struff win the Jiri Lehecka vs Jan-Lennard Struff match by a set score of 2-1?: 0.14/0.17 mid 15.5%, model 14.2% (projection_v2.0 (prediction ledger)) -- gap -1.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT31LEHSTR-LEH6` Will Jiri Lehecka win at least 5.5 more games than Jan-Lennard Struff?: 0.06/0.20 mid 13.0%, model 12.2% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Elizaveta Anikina vs Klara Veldman -- W15 Taby SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-31T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT31ANIVEL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elizaveta Anikina (`KXITFWMATCH-26OCT31ANIVEL-ANI`) | 0.43 / 0.46 (54) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Klara Veldman (`KXITFWMATCH-26OCT31ANIVEL-VEL`) | 0.54 / 0.55 (55) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dada-Mascoll / Okutoyi vs Malygina / Rajecki -- W75 Glasgow F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-31T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT31DADOKUMALRAJ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dada-Mascoll / Okutoyi (`KXITFWDOUBLES-26OCT31DADOKUMALRAJ-DADOKU`) | 0.15 / 0.62 (0) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Malygina / Rajecki (`KXITFWDOUBLES-26OCT31DADOKUMALRAJ-MALRAJ`) | 0.38 / 0.78 (1) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Iva Marinkovic vs Ella Haavisto -- W15 Taby SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216107:267845:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ella Haavisto (`KXITFWMATCH-26OCT31MARHAA-HAA`) | 0.43 / 0.48 (105) | 45.5% | 67.6% | 54.8% | 61.5% [56.4%-67.5%] | 47.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +22.1 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Iva Marinkovic (`KXITFWMATCH-26OCT31MARHAA-MAR`) | 0.52 / 0.54 (5) | 53.0% | 32.4% | 45.2% | 38.5% [32.5%-43.6%] | 52.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -20.6 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 542.0, B 1672.0; serve-point win A 52.8%, B 43.8%; Elo A 1321.3, B 1414.5; model uncertainty 0.0558
* Form inputs: days since last match A 187, B 243; matches on record A 17, B 139; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT31MARHAA-HAA  (YES = Ella Haavisto)
Model: 68%
Kalshi: 46%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.035, surface_pool_high +0.052, surface_dev_loose +0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jones / Jones vs Perez Ramos / Wright -- M15 Heraklion F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-31T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT31JONJONPERWRI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jones / Jones (`KXITFDOUBLES-26OCT31JONJONPERWRI-JONJON`) | 0.26 / 0.48 (48) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Perez Ramos / Wright (`KXITFDOUBLES-26OCT31JONJONPERWRI-PERWRI`) | 0.46 / 0.69 (80) | 57.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Georgii Kravchenko vs Garrett Johns -- M25 Malta SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206662:208143:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Garrett Johns (`KXITFMATCH-26OCT31KRAJOH-JOH`) | 0.40 / 0.44 (182) | 42.0% | 51.4% | 32.5% | 41.3% [37.8%-45.9%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +9.4 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Georgii Kravchenko (`KXITFMATCH-26OCT31KRAJOH-KRA`) | 0.57 / 0.59 (144) | 58.0% | 48.6% | 67.5% | 58.7% [54.1%-62.2%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.4 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3083.0, B 4190.0; serve-point win A 59.7%, B 40.1%; Elo A 1444.6, B 1515.3; model uncertainty 0.0404
* Form inputs: days since last match A 19, B 68; matches on record A 390, B 270; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose +0.010, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## James MacKinlay vs Daniel Masur -- M25 Malta SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:109054:208905:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| James MacKinlay (`KXITFMATCH-26OCT31MACMAS-MAC`) | 0.08 / 0.10 (100) | 9.0% | 4.8% | 6.9% | 8.4% [6.8%-10.4%] | 11.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daniel Masur (`KXITFMATCH-26OCT31MACMAS-MAS`) | 0.90 / 0.91 (100) | 90.5% | 95.2% | 93.1% | 91.6% [89.6%-93.2%] | 88.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 153.0, B 4231.0; serve-point win A 57.1%, B 29.6%; Elo A 1157.1, B 1563.3; model uncertainty 0.0182
* Form inputs: days since last match A 481, B 40; matches on record A 7, B 772; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.021, surface_dev_loose -0.002, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Josy Daems vs Lian Tran -- W15 Essen F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220560:260539:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Josy Daems (`KXITFWMATCH-26OCT31DAETRA-DAE`) | 0.57 / 0.58 (66) | 57.5% | 52.4% | 86.6% | 67.5% [51.6%-76.5%] | 59.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -5.1 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lian Tran (`KXITFWMATCH-26OCT31DAETRA-TRA`) | 0.38 / 0.42 (122) | 40.0% | 47.6% | 13.4% | 32.5% [23.5%-48.4%] | 40.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.6 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2580.0, B 1204.0; serve-point win A 53.7%, B 46.7%; Elo A 1484.9, B 1505.4; model uncertainty 0.1245
* Form inputs: days since last match A 229, B 187; matches on record A 103, B 307; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.010, surface_dev_loose +0.019, surface_dev_tight -0.019
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Martin Damm Jr vs Dino Prizmic -- ATP Challenger Brest SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-31T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:102093:209976:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martin Damm Jr (`KXATPCHALLENGERMATCH-26OCT31DAMPRI-DAM`) | 0.46 / 0.48 (3242) | 47.0% | 34.9% | 51.4% | 47.2% [32.4%-50.5%] | 46.9% | 46.6% | 46.8% | MODEL_LONE_OUTLIER | PASS | -12.1 pp | REVIEW | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Dino Prizmic (`KXATPCHALLENGERMATCH-26OCT31DAMPRI-PRI`) | 0.52 / 0.54 (2068) | 53.0% | 65.1% | 48.6% | 52.8% [49.5%-67.6%] | 53.1% | 53.4% | 53.2% | MODEL_LONE_OUTLIER | PASS | +12.1 pp | REVIEW | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4928.0, B 4419.0; serve-point win A 67.3%, B 29.4%; Elo A 1725.4, B 1839.6; model uncertainty 0.0903
* Form inputs: days since last match A 192, B 10; matches on record A 347, B 254; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.037, surface_pool_high +0.033, surface_dev_loose +0.014, surface_dev_tight -0.024
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Biot / Kapcia vs Bosman / Veldman -- W15 Taby F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-31T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT31BIOKAPBOSVEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Biot / Kapcia (`KXITFWDOUBLES-26OCT31BIOKAPBOSVEL-BIOKAP`) | 0.11 / 0.32 (36) | 21.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bosman / Veldman (`KXITFWDOUBLES-26OCT31BIOKAPBOSVEL-BOSVEL`) | 0.61 / 0.82 (138) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Suzan Lamens vs Alicia Dudeney -- W75 Glasgow SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215480:260206:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alicia Dudeney (`KXITFWMATCH-26OCT31LAMDUD-DUD`) | 0.43 / 0.45 (112) | 44.0% | 49.5% | 85.4% | 74.8% [48.4%-82.2%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +5.5 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Suzan Lamens (`KXITFWMATCH-26OCT31LAMDUD-LAM`) | 0.55 / 0.56 (230) | 55.5% | 50.5% | 14.6% | 25.2% [17.8%-51.6%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.0 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3938.0, B 3238.0; serve-point win A 53.9%, B 46.2%; Elo A 1724.8, B 1665.7; model uncertainty 0.1688
* Form inputs: days since last match A 26, B 23; matches on record A 545, B 94; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.026, surface_pool_high -0.021, surface_dev_loose -0.008, surface_dev_tight +0.022
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oliver Tarvet vs Matt Ponchet -- M25 Sheffield F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210328:210472:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matt Ponchet (`KXITFMATCH-26OCT31TARPON-PON`) | 0.05 / 0.07 (3142) | 6.0% | 7.2% | 12.0% | 8.7% [7.2%-9.6%] | 5.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +1.2 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oliver Tarvet (`KXITFMATCH-26OCT31TARPON-TAR`) | 0.93 / 0.95 (399) | 94.0% | 92.8% | 88.0% | 91.3% [90.5%-92.8%] | 94.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.2 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1816.0, B 1205.0; serve-point win A 69.4%, B 42.3%; Elo A 1714.8, B 1253.5; model uncertainty 0.0115
* Form inputs: days since last match A 26, B 236; matches on record A 88, B 56; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.002, surface_pool_high -0.004, surface_dev_loose +0.008, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elsa Jacquemot vs Alina Charaeva -- WTA 125K Courmayeur SF

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-31 17:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

WTA125 (WTA_125) · surface ? · scheduled 2026-10-31T17:40:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT31JACCHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alina Charaeva (`KXWTACHALLENGERMATCH-26OCT31JACCHA-CHA`) | 0.58 / 0.60 (4762) | 59.0% | 71.9% | -- | -- [-----] | -- | -- | -- | -- | -- | +12.9 pp | REVIEW | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Elsa Jacquemot (`KXWTACHALLENGERMATCH-26OCT31JACCHA-JAC`) | 0.40 / 0.42 (27) | 41.0% | 28.1% | -- | -- [-----] | -- | -- | -- | -- | -- | -12.9 pp | REVIEW | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 54.5%, B 41.1%; Elo A 1792.6, B 1899.1; model uncertainty None
* Form inputs: days since last match A 2, B 4; matches on record A 404, B 331; data quality A
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Bouchelaghem / Goran Verwerft vs Hammes / Sanchez Martinez -- M15 Monastir F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-31T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT31BOUGORHAMSAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bouchelaghem / Goran Verwerft (`KXITFDOUBLES-26OCT31BOUGORHAMSAN-BOUGOR`) | 0.22 / 0.48 (48) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hammes / Sanchez Martinez (`KXITFDOUBLES-26OCT31BOUGORHAMSAN-HAMSAN`) | 0.43 / 0.70 (83) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Pia Lovric vs Weronika Ewald -- W35 Malta SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222458:260541:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Weronika Ewald (`KXITFWMATCH-26OCT31LOVEWA-EWA`) | 0.50 / 0.53 (3) | 51.5% | 74.4% | 69.5% | 68.5% [66.6%-69.5%] | 52.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +22.9 pp | HIGH_REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pia Lovric (`KXITFWMATCH-26OCT31LOVEWA-LOV`) | 0.46 / 0.47 (5) | 46.5% | 25.6% | 30.5% | 31.5% [30.5%-33.4%] | 47.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -20.9 pp | HIGH_REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1631.0, B 2476.0; serve-point win A 50.2%, B 44.9%; Elo A 1467.6, B 1594.6; model uncertainty 0.0144
* Form inputs: days since last match A 20, B 187; matches on record A 300, B 129; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT31LOVEWA-EWA  (YES = Weronika Ewald)
Model: 74%
Kalshi: 52%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.010, surface_dev_loose -0.009, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nishimura / Zhu vs Husar / Srutwa -- W15 Monastir F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-31T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT31NISZHUHUSSRU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Husar / Srutwa (`KXITFWDOUBLES-26OCT31NISZHUHUSSRU-HUSSRU`) | 0.05 / 0.20 (31) | 12.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nishimura / Zhu (`KXITFWDOUBLES-26OCT31NISZHUHUSSRU-NISZHU`) | 0.73 / 0.96 (37) | 84.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Sedysheva / Smirnova vs Egorova / Zaytseva -- W50 Istanbul F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-31T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT31SEDSMIEGOZAY:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Egorova / Zaytseva (`KXITFWDOUBLES-26OCT31SEDSMIEGOZAY-EGOZAY`) | 0.05 / 0.96 (2) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sedysheva / Smirnova (`KXITFWDOUBLES-26OCT31SEDSMIEGOZAY-SEDSMI`) | 0.05 / 0.96 (2) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Federica Urgesi vs Valentini Grammatikopoulou -- W35 Malta SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:204394:223415:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valentini Grammatikopoulou (`KXITFWMATCH-26OCT31URGGRA-GRA`) | 0.24 / 0.28 (10) | 26.0% | 31.7% | 47.9% | 44.7% [41.5%-47.3%] | 28.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +5.7 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Federica Urgesi (`KXITFWMATCH-26OCT31URGGRA-URG`) | 0.71 / 0.75 (236) | 73.0% | 68.3% | 52.1% | 55.3% [52.7%-58.5%] | 71.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.7 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2635.0, B 2942.0; serve-point win A 54.9%, B 48.7%; Elo A 1586.9, B 1508.1; model uncertainty 0.0291
* Form inputs: days since last match A 40, B 110; matches on record A 169, B 724; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.027, surface_pool_high +0.032, surface_dev_loose +0.026, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daems / Reusch vs Schuknecht / Schweika -- W15 Essen F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-31T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT31DAEREUSCHSCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daems / Reusch (`KXITFWDOUBLES-26OCT31DAEREUSCHSCH-DAEREU`) | 0.05 / 0.96 (2) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Schuknecht / Schweika (`KXITFWDOUBLES-26OCT31DAEREUSCHSCH-SCHSCH`) | 0.05 / 0.96 (2) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Veronika Podrez vs Francesca Curmi -- W75 Poitiers SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221014:247669:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesca Curmi (`KXITFWMATCH-26OCT31PODCUR-CUR`) | 0.33 / 0.34 (3) | 33.5% | 32.2% | 28.7% | 32.0% [29.6%-39.0%] | 32.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Veronika Podrez (`KXITFWMATCH-26OCT31PODCUR-POD`) | 0.65 / 0.66 (229) | 65.5% | 67.8% | 71.3% | 68.0% [61.1%-70.3%] | 67.5% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +2.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3466.0, B 2628.0; serve-point win A 55.6%, B 47.8%; Elo A 1719.9, B 1633.4; model uncertainty 0.0465
* Form inputs: days since last match A 37, B 14; matches on record A 227, B 324; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.019, surface_dev_loose +0.009, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hannah Klugman vs Fiona Crawley -- W75 Glasgow SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220680:263872:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fiona Crawley (`KXITFWMATCH-26OCT31KLUCRA-CRA`) | 0.28 / 0.30 (200) | 29.0% | 66.7% | 57.9% | 62.0% [60.4%-65.5%] | 29.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +37.7 pp | EXTREME (DATA_WARNING) | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hannah Klugman (`KXITFWMATCH-26OCT31KLUCRA-KLU`) | 0.69 / 0.72 (290) | 70.5% | 33.3% | 42.1% | 38.0% [34.5%-39.6%] | 70.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -37.2 pp | EXTREME (DATA_WARNING) | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1658.0, B 2695.0; serve-point win A 54.5%, B 42.2%; Elo A 1636.2, B 1754.6; model uncertainty 0.0255
* Form inputs: days since last match A 124, B 22; matches on record A 78, B 131; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT31KLUCRA-CRA  (YES = Fiona Crawley)
Model: 67%
Kalshi: 29%
Gap: +38 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.015, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Neos / Tsitsipas vs Howse / MacKinlay -- M25 Malta F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-31T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT31NEOTSIHOWMAC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Howse / MacKinlay (`KXITFDOUBLES-26OCT31NEOTSIHOWMAC-HOWMAC`) | 0.04 / 0.95 (2) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Neos / Tsitsipas (`KXITFDOUBLES-26OCT31NEOTSIHOWMAC-NEOTSI`) | 0.04 / 0.95 (2) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alastair Gray vs Lui Maxted -- M25 Norman OK SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-31T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202400:210747:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alastair Gray (`KXITFMATCH-26OCT31GRAMAX-GRA`) | 0.54 / 0.57 (133) | 55.5% | 53.2% | 54.6% | 54.6% [54.6%-56.6%] | 55.2% | -- | 55.2% | MARKETS_AGREE | PASS | -2.3 pp | NORMAL | AGING | C / LIMITED | ALL_AGREE | VERIFIED |
| Lui Maxted (`KXITFMATCH-26OCT31GRAMAX-MAX`) | 0.38 / 0.46 (21) | 42.0% | 46.8% | 45.4% | 45.4% [43.4%-45.4%] | 44.8% | -- | 44.8% | KALSHI_LONE_OUTLIER | PASS | +4.8 pp | NORMAL | AGING | C / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3694.0, B 2751.0; serve-point win A 61.8%, B 38.9%; Elo A 1601.1, B 1566.3; model uncertainty 0.0102
* Form inputs: days since last match A 47, B 236; matches on record A 326, B 70; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Harazaki / Papa vs Hussey / Mchugh -- M25 Norman OK F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-31T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT31HARPAPHUSMCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Harazaki / Papa (`KXITFDOUBLES-26OCT31HARPAPHUSMCH-HARPAP`) | 0.04 / 0.95 (2) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hussey / Mchugh (`KXITFDOUBLES-26OCT31HARPAPHUSMCH-HUSMCH`) | 0.04 / 0.95 (2) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tomas Martinez vs Ignacio Monzon -- M15 João Pessoa SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-31T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:133820:211658:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tomas Martinez (`KXITFMATCH-26OCT31MARMON-MAR`) | 0.40 / 0.45 (45) | 42.5% | 37.5% | 43.1% | 39.0% [37.4%-40.0%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.0 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ignacio Monzon (`KXITFMATCH-26OCT31MARMON-MON`) | 0.50 / 0.60 (44) | 55.0% | 62.5% | 56.9% | 61.0% [60.0%-62.6%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.5 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1526.0, B 3341.0; serve-point win A 53.1%, B 44.5%; Elo A 1246.6, B 1356.6; model uncertainty 0.0128
* Form inputs: days since last match A 40, B 117; matches on record A 59, B 427; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Filip Jeff Planinsek vs Tyler Zink -- M25 Norman OK SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-31T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208342:210731:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Filip Jeff Planinsek (`KXITFMATCH-26OCT31PLAZIN-PLA`) | 0.33 / 0.36 (26) | 34.5% | 24.6% | 37.7% | 33.0% [31.2%-34.9%] | 33.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.9 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tyler Zink (`KXITFMATCH-26OCT31PLAZIN-ZIN`) | 0.65 / 0.66 (302) | 65.5% | 75.4% | 62.3% | 67.0% [65.1%-68.8%] | 66.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +9.9 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1932.0, B 4139.0; serve-point win A 60.4%, B 34.1%; Elo A 1434.1, B 1601.9; model uncertainty 0.0185
* Form inputs: days since last match A 43, B 168; matches on record A 102, B 197; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ayana Akli vs Katherine Sebov -- W75 Toronto SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214684:264149:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ayana Akli (`KXITFWMATCH-26OCT31AKLSEB-AKL`) | 0.55 / 0.58 (135) | 56.5% | 37.1% | 40.6% | 40.1% [39.1%-41.1%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -19.4 pp | HIGH_REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Katherine Sebov (`KXITFWMATCH-26OCT31AKLSEB-SEB`) | 0.38 / 0.43 (100) | 40.5% | 62.9% | 59.4% | 59.9% [58.9%-60.9%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +22.4 pp | HIGH_REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2838.0, B 3407.0; serve-point win A 55.2%, B 42.4%; Elo A 1612.6, B 1691.4; model uncertainty 0.0101
* Form inputs: days since last match A 40, B 46; matches on record A 123, B 461; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT31AKLSEB-SEB  (YES = Katherine Sebov)
Model: 63%
Kalshi: 40%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: LOW_DISPLAYED_LIQUIDITY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.005, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Emery Combs vs Anita Sahdiieva -- W15 Sumter SC SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221370:270089:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emery Combs (`KXITFWMATCH-26OCT31COMSAH-COM`) | 0.50 / 0.52 (139) | 51.0% | 41.5% | 46.8% | 47.9% [47.3%-48.9%] | 50.9% | -- | 50.9% | MARKETS_AGREE | PASS | -9.5 pp | NORMAL | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Anita Sahdiieva (`KXITFWMATCH-26OCT31COMSAH-SAH`) | 0.45 / 0.50 (124) | 47.5% | 58.5% | 53.2% | 52.1% [51.1%-52.6%] | 49.0% | -- | 49.0% | MARKETS_AGREE | PASS | +11.0 pp | REVIEW | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 528.0, B 1325.0; serve-point win A 54.2%, B 44.2%; Elo A 1384.8, B 1390.1; model uncertainty 0.008
* Form inputs: days since last match A 194, B 187; matches on record A 8, B 111; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.011, surface_dev_loose -0.005, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oceane Dodin vs Clara Burel -- W75 Poitiers SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206219:216262:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Clara Burel (`KXITFWMATCH-26OCT31DODBUR-BUR`) | 0.78 / 0.80 (10) | 79.0% | 67.5% | 54.7% | 58.4% [55.3%-63.5%] | 78.6% | -- | 78.6% | MODEL_LONE_OUTLIER | PASS | -11.5 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Oceane Dodin (`KXITFWMATCH-26OCT31DODBUR-DOD`) | 0.19 / 0.21 (15) | 20.0% | 32.5% | 45.3% | 41.6% [36.5%-44.7%] | 21.4% | -- | 21.4% | MODEL_LONE_OUTLIER | WATCH | +12.5 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1969.0, B 1472.0; serve-point win A 54.8%, B 41.8%; Elo A 1748.1, B 1825.7; model uncertainty 0.0413
* Form inputs: days since last match A 38, B 13; matches on record A 714, B 308; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.031, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ashley Lahey vs Dana Guzman -- W35 Norman OK SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-31T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216076:221834:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dana Guzman (`KXITFWMATCH-26OCT31LAHGUZ-GUZ`) | 0.74 / 0.78 (133) | 76.0% | 43.2% | 48.4% | 43.1% [41.5%-45.8%] | 74.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -32.8 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ashley Lahey (`KXITFWMATCH-26OCT31LAHGUZ-LAH`) | 0.21 / 0.24 (100) | 22.5% | 56.8% | 51.6% | 56.9% [54.2%-58.5%] | 25.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +34.3 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1883.0, B 812.0; serve-point win A 56.2%, B 45.1%; Elo A 1627.6, B 1563.9; model uncertainty 0.0211
* Form inputs: days since last match A 411, B 257; matches on record A 239, B 42; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT31LAHGUZ-LAH  (YES = Ashley Lahey)
Model: 57%
Kalshi: 22%
Gap: +34 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luciana Moyano vs Emily Zornada -- W15 Neuquén SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-31T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:237454:270329:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luciana Moyano (`KXITFWMATCH-26OCT31MOYZOR-MOY`) | 0.80 / 0.83 (2) | 81.5% | 81.6% | 80.9% | 71.4% [70.5%-72.3%] | 79.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Emily Zornada (`KXITFWMATCH-26OCT31MOYZOR-ZOR`) | 0.15 / 0.18 (249) | 16.5% | 18.4% | 19.1% | 28.6% [27.7%-29.5%] | 20.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.9 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2452.0, B 106.0; serve-point win A 53.7%, B 53.0%; Elo A 1454.4, B 1300.7; model uncertainty 0.0092
* Form inputs: days since last match A 187, B 215; matches on record A 106, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Salakthip Ounmuang vs Alina Shcherbinina -- W35 Norman OK SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-31T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221278:259905:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Salakthip Ounmuang (`KXITFWMATCH-26OCT31OUNSHC-OUN`) | 0.27 / 0.29 (128) | 28.0% | 49.4% | 31.5% | 52.1% [49.5%-54.3%] | 28.9% | -- | 28.9% | MODEL_LONE_OUTLIER | PASS | +21.4 pp | HIGH_REVIEW | AGING | F / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Alina Shcherbinina (`KXITFWMATCH-26OCT31OUNSHC-SHC`) | 0.70 / 0.73 (132) | 71.5% | 50.6% | 68.5% | 47.9% [45.7%-50.5%] | 71.1% | -- | 71.1% | MODEL_LONE_OUTLIER | PASS | -20.9 pp | HIGH_REVIEW | AGING | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 193.0, B 127.0; serve-point win A 54.1%, B 45.8%; Elo A 1356.3, B 1330.3; model uncertainty 0.024
* Form inputs: days since last match A 439, B 257; matches on record A 73, B 55; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT31OUNSHC-OUN  (YES = Salakthip Ounmuang)
Model: 49%
Kalshi: 28%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Malwina Rowinska vs Lani Chang -- W15 Sumter SC SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260764:270091:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lani Chang (`KXITFWMATCH-26OCT31ROWCHA-CHA`) | 0.65 / 0.69 (106) | 67.0% | 80.9% | 72.7% | 73.2% [71.8%-75.8%] | 68.1% | -- | 68.1% | MODEL_LONE_OUTLIER | PASS | +13.9 pp | REVIEW | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Malwina Rowinska (`KXITFWMATCH-26OCT31ROWCHA-ROW`) | 0.29 / 0.33 (31) | 31.0% | 19.1% | 27.3% | 26.9% [24.2%-28.2%] | 31.9% | -- | 31.9% | MODEL_LONE_OUTLIER | PASS | -11.9 pp | REVIEW | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 297.0, B 310.0; serve-point win A 48.7%, B 44.8%; Elo A 1193.6, B 1368.8; model uncertainty 0.0199
* Form inputs: days since last match A 208, B 201; matches on record A 27, B 9; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.004, surface_dev_loose +0.000, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Paganetti / Urgesi vs Adeshina / Grammatikopoulou -- W35 Malta F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-31T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT31PAGURGADEGRA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adeshina / Grammatikopoulou (`KXITFWDOUBLES-26OCT31PAGURGADEGRA-ADEGRA`) | 0.05 / 0.96 (2) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Paganetti / Urgesi (`KXITFWDOUBLES-26OCT31PAGURGADEGRA-PAGURG`) | 0.05 / 0.96 (2) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Reese Brantmeier vs Kajsa Rinaldo Persson -- W75 Toronto SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211643:222034:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Reese Brantmeier (`KXITFWMATCH-26OCT31BRARIN-BRA`) | 0.79 / 0.82 (220) | 80.5% | 62.1% | 15.7% | 46.9% [39.7%-53.1%] | -- | -- | -- | -- | PASS | -18.4 pp | HIGH_REVIEW | AGING | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kajsa Rinaldo Persson (`KXITFWMATCH-26OCT31BRARIN-RIN`) | 0.18 / 0.20 (25) | 19.0% | 37.9% | 84.3% | 53.1% [46.9%-60.3%] | -- | -- | -- | -- | WATCH | +18.9 pp | HIGH_REVIEW | AGING | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 133.0, B 3104.0; serve-point win A 59.1%, B 43.2%; Elo A 1565.6, B 1566.1; model uncertainty 0.0674
* Form inputs: days since last match A 34, B 38; matches on record A 89, B 430; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT31BRARIN-RIN  (YES = Kajsa Rinaldo Persson)
Model: 38%
Kalshi: 19%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.072, surface_pool_high +0.063, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cascino / Feng vs Jorge / Jorge -- W75 Poitiers F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-31T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT31CASFENJORJOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cascino / Feng (`KXITFWDOUBLES-26OCT31CASFENJORJOR-CASFEN`) | 0.14 / 0.37 (39) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jorge / Jorge (`KXITFWDOUBLES-26OCT31CASFENJORJOR-JORJOR`) | 0.57 / 0.81 (131) | 69.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Combs / De Los Reyes vs Koreshkova / Simunyu -- W15 Sumter SC F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-31T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT31COMDELKORSIM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Combs / De Los Reyes (`KXITFWDOUBLES-26OCT31COMDELKORSIM-COMDEL`) | 0.05 / 0.96 (2) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Koreshkova / Simunyu (`KXITFWDOUBLES-26OCT31COMDELKORSIM-KORSIM`) | 0.05 / 0.96 (2) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lahey / Vagramov vs Laskevich / Mamedova -- W35 Norman OK F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-31T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT31LAHVAGLASMAM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lahey / Vagramov (`KXITFWDOUBLES-26OCT31LAHVAGLASMAM-LAHVAG`) | 0.05 / 0.96 (2) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Laskevich / Mamedova (`KXITFWDOUBLES-26OCT31LAHVAGLASMAM-LASMAM`) | 0.05 / 0.96 (2) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sol Ailin Larraya Guidi vs Josefina Estevez -- W15 Neuquén SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-31T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260709:260717:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Josefina Estevez (`KXITFWMATCH-26OCT31LAREST-EST`) | 0.50 / 0.58 (134) | 54.0% | 47.9% | 66.2% | 44.1% [40.5%-50.5%] | -- | -- | -- | -- | PASS | -6.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sol Ailin Larraya Guidi (`KXITFWMATCH-26OCT31LAREST-LAR`) | 0.42 / 0.44 (136) | 43.0% | 52.1% | 33.8% | 55.9% [49.5%-59.6%] | -- | -- | -- | -- | PASS | +9.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 409.0, B 732.0; serve-point win A 50.0%, B 50.3%; Elo A 1373.5, B 1294.6; model uncertainty 0.0504
* Form inputs: days since last match A 215, B 292; matches on record A 66, B 55; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.000, surface_dev_loose -0.011, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oscar Jose Gutierrez vs Pedro Sakamoto -- M15 João Pessoa SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-31T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106203:121264:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oscar Jose Gutierrez (`KXITFMATCH-26OCT31GUTSAK-GUT`) | 0.22 / 0.26 (405) | 24.0% | 27.0% | 28.3% | 26.6% [24.5%-28.3%] | -- | -- | -- | -- | PASS | +3.0 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pedro Sakamoto (`KXITFMATCH-26OCT31GUTSAK-SAK`) | 0.72 / 0.78 (154) | 75.0% | 73.0% | 71.7% | 73.4% [71.7%-75.5%] | -- | -- | -- | -- | PASS | -2.0 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2766.0, B 3163.0; serve-point win A 56.5%, B 38.8%; Elo A 1315.8, B 1521.4; model uncertainty 0.0191
* Form inputs: days since last match A 201, B 33; matches on record A 606, B 717; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Boyden / Moyano vs Estevez / Ailin Larraya Guidi -- W15 Neuquén F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-31T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT31BOYMOYESTAIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Boyden / Moyano (`KXITFWDOUBLES-26OCT31BOYMOYESTAIL-BOYMOY`) | 0.05 / 0.96 (2) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Estevez / Ailin Larraya Guidi (`KXITFWDOUBLES-26OCT31BOYMOYESTAIL-ESTAIL`) | 0.05 / 0.96 (2) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Andres Santamarta Roig vs Jack Anthrop -- M25 Las Vegas NV SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210294:212749:2026-10-31`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jack Anthrop (`KXITFMATCH-26OCT31SANANT-ANT`) | 0.51 / 0.60 (100) | 55.5% | 43.1% | 69.4% | 53.6% [42.8%-59.8%] | -- | -- | -- | -- | PASS | -12.4 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Andres Santamarta Roig (`KXITFMATCH-26OCT31SANANT-SAN`) | 0.39 / 0.43 (100) | 41.0% | 56.9% | 30.6% | 46.4% [40.2%-57.2%] | -- | -- | -- | -- | PASS | +15.9 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1785.0, B 1030.0; serve-point win A 59.5%, B 41.8%; Elo A 1501.0, B 1442.4; model uncertainty 0.0852
* Form inputs: days since last match A 110, B 355; matches on record A 62, B 77; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT31SANANT-SAN  (YES = Andres Santamarta Roig)
Model: 57%
Kalshi: 41%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.010, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Akli / Sieg vs Arseneault / Lacasse -- W75 Toronto F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-31T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT31AKLSIEARSLAC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Akli / Sieg (`KXITFWDOUBLES-26OCT31AKLSIEARSLAC-AKLSIE`) | 0.05 / 0.96 (2) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arseneault / Lacasse (`KXITFWDOUBLES-26OCT31AKLSIEARSLAC-ARSLAC`) | 0.05 / 0.96 (2) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Collins / Penickova vs El Jardi / Frodin -- W100 New Braunfels TX SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-31T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT31COLPENELJFRO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Collins / Penickova (`KXITFWDOUBLES-26OCT31COLPENELJFRO-COLPEN`) | 0.05 / 0.96 (2) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| El Jardi / Frodin (`KXITFWDOUBLES-26OCT31COLPENELJFRO-ELJFRO`) | 0.05 / 0.96 (2) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Renata Zarazua vs Akasha Urhobo -- W100 New Braunfels TX QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-31 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-31T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT31ZARURH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Akasha Urhobo (`KXITFWMATCH-26OCT31ZARURH-URH`) | 0.07 / 0.92 (313) | 49.5% | 41.2% | -- | -- [-----] | -- | -- | -- | -- | -- | -8.3 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Renata Zarazua (`KXITFWMATCH-26OCT31ZARURH-ZAR`) | 0.06 / 0.93 (357) | 49.5% | 58.8% | -- | -- [-----] | -- | -- | -- | -- | -- | +9.3 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 56.4%, B 45.3%; Elo A 1765.5, B 1625.7; model uncertainty None
* Form inputs: days since last match A 21, B 68; matches on record A 698, B 174; data quality A
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jerry Roddick vs Nikita Filin -- M25 Las Vegas NV SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-01T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212542:212570:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikita Filin (`KXITFMATCH-26OCT31RODFIL-FIL`) | 0.60 / 0.66 (36) | 63.0% | 30.7% | 46.4% | 37.2% [35.3%-39.7%] | -- | -- | -- | -- | PASS | -32.3 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jerry Roddick (`KXITFMATCH-26OCT31RODFIL-ROD`) | 0.33 / 0.39 (42) | 36.0% | 69.3% | 53.6% | 62.8% [60.3%-64.7%] | -- | -- | -- | -- | PASS | +33.3 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 639.0, B 201.0; serve-point win A 60.8%, B 43.1%; Elo A 1304.6, B 1207.6; model uncertainty 0.0218
* Form inputs: days since last match A 187, B 355; matches on record A 14, B 12; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT31RODFIL-ROD  (YES = Jerry Roddick)
Model: 69%
Kalshi: 36%
Gap: +33 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
