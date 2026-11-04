# ASSISTED SLATE -- 2026-11-04T23:08Z (`SL-20261104T230812Z-67b2c53a`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

288 open matches not seen started, 744 markets. Skipped: {"scheduled_start_over_24h_past": 4, "first_ball_already_observed": 1}. Sources: shadow board 2026-11-04T20:50:56.720149+00:00, Model 4 2026-11-04T20:52:03.795032+00:00, Gen-1 ledger 2026-11-04T20:50:53.140142+00:00, external 2026-11-04T22:42:38.306963+00:00, capture 20261104T224105Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-11-05 06:00Z**
* Recommended RUN TENNIS time: **2026-11-05 05:15Z**
* Final price/status check time: **2026-11-05 05:50Z**
* Number of matches in window: 3 (Elena Pridankina vs Alexandra Shubladze, Xinyu Wang vs Antonia Ruzic, Mika Stojsavljevic vs Zeynep Sonmez)

Slate built 2026-11-04T23:08Z. Refresh due by: 2026-11-05 05:15Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 37, "HIGH_REVIEW": 66, "NORMAL": 268, "REVIEW": 55, "UNPRICED": 318}; match winners: {"EXTREME": 26, "HIGH_REVIEW": 49, "NORMAL": 188, "REVIEW": 31, "UNPRICED": 282}; quote freshness at build: {"FRESH": 426}.

## Adrian Andreev vs Matteo Martineau -- ATP Challenger Taranto R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-04T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200188:202090:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Andreev (`KXATPCHALLENGERMATCH-26NOV04ANDMAR-AND`) | 0.40 / 0.41 (63) | 40.5% | -- | 45.0% | 46.0% [45.5%-46.5%] | -- | -- | -- | -- | SHADOW_BET | +5.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matteo Martineau (`KXATPCHALLENGERMATCH-26NOV04ANDMAR-MAR`) | 0.59 / 0.60 (1914) | 59.5% | -- | 55.0% | 54.0% [53.5%-54.5%] | -- | -- | -- | -- | PASS | -5.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2392.0, B 5600.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.005
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE

## Benjamin Bonzi / Arthur Rinderknech vs Kevin Krawietz / Tim Putz -- ATP Paris R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-04T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04BONRINKRAPUT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Benjamin Bonzi / Arthur Rinderknech (`KXATPDOUBLES-26NOV04BONRINKRAPUT-BONRIN`) | 0.37 / 0.39 (5) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kevin Krawietz / Tim Putz (`KXATPDOUBLES-26NOV04BONRINKRAPUT-KRAPUT`) | 0.60 / 0.64 (379) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Lautaro Midon vs Marcelo Tomas Barrios Vera -- ATP Challenger Costa do Sauipe R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-04T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04MIDBAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcelo Tomas Barrios Vera (`KXATPCHALLENGERMATCH-26NOV04MIDBAR-BAR`) | -- / 0.01 (138900) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lautaro Midon (`KXATPCHALLENGERMATCH-26NOV04MIDBAR-MID`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE

## Tom Hands / Matthew Summers vs Ben Jones / Joshua Sheehy -- ATP Challenger Charlottesville R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 22:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-04T22:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04HANSUMJONSHE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tom Hands / Matthew Summers (`KXATPCHALLENGERDOUBLES-26NOV04HANSUMJONSHE-HANSUM`) | 0.51 / 0.56 (152) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ben Jones / Joshua Sheehy (`KXATPCHALLENGERDOUBLES-26NOV04HANSUMJONSHE-JONSHE`) | 0.49 / 0.50 (5156) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Jack Kennedy vs Clement Chidekh -- ATP Challenger Charlottesville R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 22:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-04T22:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206889:213605:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Clement Chidekh (`KXATPCHALLENGERMATCH-26NOV04KENCHI-CHI`) | 0.94 / 0.95 (27640) | 94.5% | 77.6% | 86.3% | 82.8% [74.7%-85.4%] | -- | 88.9% | 88.9% | MODEL_LONE_OUTLIER | PASS | -16.9 pp | HIGH_REVIEW | FRESH | B / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Jack Kennedy (`KXATPCHALLENGERMATCH-26NOV04KENCHI-KEN`) | 0.05 / 0.06 (40631) | 5.5% | 22.4% | 13.7% | 17.2% [14.6%-25.3%] | -- | 11.0% | 11.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +16.9 pp | HIGH_REVIEW | FRESH | B / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 2751.0, B 5040.0; serve-point win A 54.2%, B 40.1%; Elo A 1543.8, B 1734.9; model uncertainty 0.0535
* Form inputs: days since last match A 198, B 12; matches on record A 51, B 331; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV04KENCHI-KEN  (YES = Jack Kennedy)
Model: 22%
Kalshi: 6%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: SUPPORTS_MODEL_DIRECTION
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.013, surface_dev_loose -0.016, surface_dev_tight +0.017
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED

## Merna Refaat vs Edda Mamedova -- W35 Orlando FL R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 23:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-04T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221473:239422:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Edda Mamedova (`KXITFWMATCH-26NOV04REFMAM-MAM`) | 0.95 / 0.96 (1842) | 95.5% | 78.9% | 85.2% | 76.2% [70.4%-81.6%] | 59.1% | -- | 59.1% | MODEL_LONE_OUTLIER | PASS | -16.6 pp | HIGH_REVIEW | FRESH | D / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Merna Refaat (`KXITFWMATCH-26NOV04REFMAM-REF`) | 0.04 / 0.05 (17829) | 4.5% | 21.1% | 14.8% | 23.8% [18.4%-29.6%] | 40.9% | -- | 40.9% | MODEL_LONE_OUTLIER | PASS | +16.6 pp | HIGH_REVIEW | FRESH | D / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 556.0, B 879.0; serve-point win A 48.4%, B 45.6%; Elo A 1309.5, B 1473.3; model uncertainty 0.0559
* Form inputs: days since last match A 387, B 261; matches on record A 201, B 91; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV04REFMAM-REF  (YES = Merna Refaat)
Model: 21%
Kalshi: 4%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: SUPPORTS_MODEL_DIRECTION
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.008, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mans Dahlberg / Dylan Dietrich vs Jarno Jans / Joran Vliegen -- ATP Challenger Charlottesville R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 23:50Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-04T23:50:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04DAHDIEJANVLI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mans Dahlberg / Dylan Dietrich (`KXATPCHALLENGERDOUBLES-26NOV04DAHDIEJANVLI-DAHDIE`) | 0.20 / 0.26 (2) | 23.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jarno Jans / Joran Vliegen (`KXATPCHALLENGERDOUBLES-26NOV04DAHDIEJANVLI-JANVLI`) | 0.72 / 0.76 (44) | 74.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Daniel Milavsky / Braden Shick vs Justin Boulais / Jannik Opitz -- ATP Challenger Charlottesville R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 23:50Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-04T23:50:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04MILSHIBOUOPI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Justin Boulais / Jannik Opitz (`KXATPCHALLENGERDOUBLES-26NOV04MILSHIBOUOPI-BOUOPI`) | 0.29 / 0.34 (130) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daniel Milavsky / Braden Shick (`KXATPCHALLENGERDOUBLES-26NOV04MILSHIBOUOPI-MILSHI`) | 0.62 / 0.71 (69) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Lafors / Yeung vs Krall / Watane -- M15 Hilton Head Island SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04LAFYEUKRAWAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Krall / Watane (`KXITFDOUBLES-26NOV04LAFYEUKRAWAT-KRAWAT`) | 0.61 / 0.69 (16) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lafors / Yeung (`KXITFDOUBLES-26NOV04LAFYEUKRAWAT-LAFYEU`) | 0.12 / 0.36 (26) | 24.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## O'Brien / Wang vs Evtimova / Harding -- W15 Hilton Head Island SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV04OBRWANEVTHAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Evtimova / Harding (`KXITFWDOUBLES-26NOV04OBRWANEVTHAR-EVTHAR`) | 0.89 / 0.90 (0) | 89.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| O'Brien / Wang (`KXITFWDOUBLES-26NOV04OBRWANEVTHAR-OBRWAN`) | 0.10 / 0.11 (77) | 10.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Igor Marcondes vs Camilo Ugo Carabelli -- ATP Challenger Costa do Sauipe R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 00:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-05T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04MARUGO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Igor Marcondes (`KXATPCHALLENGERMATCH-26NOV04MARUGO-MAR`) | 0.01 / 0.02 (52) | 1.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Camilo Ugo Carabelli (`KXATPCHALLENGERMATCH-26NOV04MARUGO-UGO`) | 0.98 / 0.99 (155) | 98.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Brooke Black vs Annika Penickova -- W35 Orlando FL R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 00:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV04BLAPEN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brooke Black (`KXITFWMATCH-26NOV04BLAPEN-BLA`) | 0.19 / 0.20 (11) | 19.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Annika Penickova (`KXITFWMATCH-26NOV04BLAPEN-PEN`) | 0.79 / 0.80 (0) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ashton Bowers vs Julia Adams -- W35 Orlando FL R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 00:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:248665:266450:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julia Adams (`KXITFWMATCH-26NOV04BOWADA-ADA`) | 0.56 / 0.57 (200) | 56.5% | 45.6% | 47.9% | 52.1% [51.1%-53.2%] | -- | -- | -- | -- | PASS | -10.9 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Ashton Bowers (`KXITFWMATCH-26NOV04BOWADA-BOW`) | 0.43 / 0.44 (10) | 43.5% | 54.4% | 52.1% | 47.9% [46.8%-48.9%] | -- | -- | -- | -- | PASS | +10.9 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 2996.0; serve-point win A 54.7%, B 46.1%; Elo A 1375.1, B 1390.9; model uncertainty 0.0106
* Form inputs: days since last match A 744, B 191; matches on record A 46, B 163; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ema Burgic vs Luciana Perry -- W35 Orlando FL R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 00:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:202619:267920:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ema Burgic (`KXITFWMATCH-26NOV04BURPER-BUR`) | 0.63 / 0.64 (14) | 63.5% | 68.9% | 80.5% | 66.1% [64.6%-69.0%] | -- | -- | -- | -- | PASS | +5.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luciana Perry (`KXITFWMATCH-26NOV04BURPER-PER`) | 0.37 / 0.38 (570) | 37.5% | 31.1% | 19.5% | 33.9% [31.0%-35.4%] | -- | -- | -- | -- | PASS | -6.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1373.0, B 141.0; serve-point win A 53.8%, B 49.9%; Elo A 1455.8, B 1351.9; model uncertainty 0.0221
* Form inputs: days since last match A 254, B 520; matches on record A 225, B 4; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Artnak / Snitari vs Bellorio Pinheiro / Hudjec -- M25 Harlingen TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04ARTSNIBELHUD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Artnak / Snitari (`KXITFDOUBLES-26NOV04ARTSNIBELHUD-ARTSNI`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bellorio Pinheiro / Hudjec (`KXITFDOUBLES-26NOV04ARTSNIBELHUD-BELHUD`) | -- / 0.01 (62605) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE

## Gustavo Heide vs Juan Carlos Prado Angelo -- ATP Challenger Costa do Sauipe R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-05T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208361:210178:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gustavo Heide (`KXATPCHALLENGERMATCH-26NOV04HEIPRA-HEI`) | 0.58 / 0.59 (8011) | 58.5% | 64.0% | 76.9% | 74.0% [71.5%-76.1%] | -- | -- | -- | -- | SHADOW_BET | +5.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Juan Carlos Prado Angelo (`KXATPCHALLENGERMATCH-26NOV04HEIPRA-PRA`) | 0.42 / 0.43 (18428) | 42.5% | 36.0% | 23.1% | 26.0% [23.9%-28.5%] | -- | -- | -- | -- | PASS | -6.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4649.0, B 4827.0; serve-point win A 61.8%, B 41.0%; Elo A 1763.6, B 1655.7; model uncertainty 0.0231
* Form inputs: days since last match A 16, B 9; matches on record A 316, B 257; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.000, surface_dev_loose +0.008, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Lucio Ratti vs Carlos Maria Zarate -- ATP Challenger Villa Maria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-05T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211636:212785:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucio Ratti (`KXATPCHALLENGERMATCH-26NOV04RATZAR-RAT`) | 0.19 / 0.20 (22002) | 19.5% | 49.0% | 61.7% | 55.1% [52.1%-57.7%] | -- | -- | -- | -- | SHADOW_BET | +29.5 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carlos Maria Zarate (`KXATPCHALLENGERMATCH-26NOV04RATZAR-ZAR`) | 0.80 / 0.81 (20205) | 80.5% | 51.0% | 38.3% | 44.9% [42.3%-47.9%] | -- | -- | -- | -- | PASS | -29.5 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2633.0, B 2988.0; serve-point win A 59.7%, B 40.1%; Elo A 1452.3, B 1494.7; model uncertainty 0.0283
* Form inputs: days since last match A 23, B 9; matches on record A 113, B 90; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV04RATZAR-RAT  (YES = Lucio Ratti)
Model: 49%
Kalshi: 20%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Hiroki Sakagawa vs Max Wiskandt -- M25 Harlingen TX R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208328:212243:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hiroki Sakagawa (`KXITFMATCH-26NOV04SAKWIS-SAK`) | 0.39 / 0.42 (0) | 40.5% | 13.0% | 36.9% | 19.7% [19.0%-20.4%] | -- | -- | -- | -- | PASS | -27.5 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Max Wiskandt (`KXITFMATCH-26NOV04SAKWIS-WIS`) | 0.58 / 0.59 (26) | 58.5% | 87.0% | 63.1% | 80.3% [79.6%-81.0%] | -- | -- | -- | -- | PASS | +28.5 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 42.0, B 3286.0; serve-point win A 55.7%, B 35.5%; Elo A 1202.3, B 1451.5; model uncertainty 0.0071
* Form inputs: days since last match A 352, B 23; matches on record A 9, B 237; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV04SAKWIS-WIS  (YES = Max Wiskandt)
Model: 87%
Kalshi: 58%
Gap: +29 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.007, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mateus Alves / Lucas Andrade Da Silva vs Anthony Genov / Younes Lalami Laaroussi -- ATP Challenger Costa do Sauipe R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 01:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-05T01:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04ALVANDGENLAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mateus Alves / Lucas Andrade Da Silva (`KXATPCHALLENGERDOUBLES-26NOV04ALVANDGENLAL-ALVAND`) | 0.72 / 0.80 (0) | 76.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anthony Genov / Younes Lalami Laaroussi (`KXATPCHALLENGERDOUBLES-26NOV04ALVANDGENLAL-GENLAL`) | 0.15 / 0.23 (2) | 19.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Brostrom Poulsen / Slavic vs Massotte / Roussel -- M15 Trois-Rivières QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04BROSLAMASROU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brostrom Poulsen / Slavic (`KXITFDOUBLES-26NOV04BROSLAMASROU-BROSLA`) | 0.92 / 0.94 (64) | 93.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Massotte / Roussel (`KXITFDOUBLES-26NOV04BROSLAMASROU-MASROU`) | 0.06 / 0.07 (0) | 6.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Colombo / Gaines Jr vs Secord / Thompson -- M15 Hilton Head Island SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04COLGAISECTHO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Colombo / Gaines Jr (`KXITFDOUBLES-26NOV04COLGAISECTHO-COLGAI`) | 0.56 / 0.60 (10) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Secord / Thompson (`KXITFDOUBLES-26NOV04COLGAISECTHO-SECTHO`) | 0.37 / 0.39 (0) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Marcelo Tomas Barrios Vera / Matheus Pucinelli de Almeida vs Eduardo Ribeiro / Natan Rodrigues -- ATP Challenger Costa do Sauipe R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 01:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-05T01:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04BARPDARIBROD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcelo Tomas Barrios Vera / Matheus Pucinelli de Almeida (`KXATPCHALLENGERDOUBLES-26NOV04BARPDARIBROD-BARPDA`) | 0.33 / 0.45 (100) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eduardo Ribeiro / Natan Rodrigues (`KXATPCHALLENGERDOUBLES-26NOV04BARPDARIBROD-RIBROD`) | 0.56 / 0.63 (100) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Cundom / Jose Escurra Isnardi vs Andre De Almeida Santos / Ortenblad Nogueira -- M15 Salvador R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04CUNJOSANDORT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andre De Almeida Santos / Ortenblad Nogueira (`KXITFDOUBLES-26NOV04CUNJOSANDORT-ANDORT`) | 0.06 / 0.30 (24) | 18.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cundom / Jose Escurra Isnardi (`KXITFDOUBLES-26NOV04CUNJOSANDORT-CUNJOS`) | 0.63 / 0.83 (7) | 73.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Karol Drzewiecki / Piotr Matuszewski vs Igor Marcondes / Felipe Meligeni Alves -- ATP Challenger Costa do Sauipe R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 02:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-05T02:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04DRZMATMARMEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karol Drzewiecki / Piotr Matuszewski (`KXATPCHALLENGERDOUBLES-26NOV04DRZMATMARMEL-DRZMAT`) | 0.51 / 0.52 (179) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Igor Marcondes / Felipe Meligeni Alves (`KXATPCHALLENGERDOUBLES-26NOV04DRZMATMARMEL-MARMEL`) | 0.48 / 0.49 (25) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Prince / Vakalapudi vs Drugdova / Zucchini -- W35 Orlando FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 02:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T02:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV04PRIVAKDRUZUC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Drugdova / Zucchini (`KXITFWDOUBLES-26NOV04PRIVAKDRUZUC-DRUZUC`) | 0.09 / 0.93 (1) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Prince / Vakalapudi (`KXITFWDOUBLES-26NOV04PRIVAKDRUZUC-PRIVAK`) | 0.04 / 0.85 (10) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Rodriguez / Tran vs Capurro Taborda / Colmegna -- W50 Huamantla QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 02:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T02:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV04RODTRACAPCOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Capurro Taborda / Colmegna (`KXITFWDOUBLES-26NOV04RODTRACAPCOL-CAPCOL`) | 0.17 / 0.55 (29) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rodriguez / Tran (`KXITFWDOUBLES-26NOV04RODTRACAPCOL-RODTRA`) | 0.38 / 0.76 (25) | 57.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Slama / Tanasie vs Hossam Salah / Korpanec Davies -- W35 Orlando FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 02:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T02:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV04SLATANHOSKOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hossam Salah / Korpanec Davies (`KXITFWDOUBLES-26NOV04SLATANHOSKOR-HOSKOR`) | 0.03 / 0.65 (1) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Slama / Tanasie (`KXITFWDOUBLES-26NOV04SLATANHOSKOR-SLATAN`) | 0.29 / 0.93 (0) | 61.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Souza / Sverzut Corsini vs Badaro / De Magalhaes Oliveira Sousa -- M15 Salvador R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 03:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04SOUSVEBADDEM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Badaro / De Magalhaes Oliveira Sousa (`KXITFDOUBLES-26NOV04SOUSVEBADDEM-BADDEM`) | 0.18 / 0.19 (11) | 18.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Souza / Sverzut Corsini (`KXITFDOUBLES-26NOV04SOUSVEBADDEM-SOUSVE`) | 0.80 / 0.81 (0) | 80.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Thomas George / Peck vs Gales / Markov -- M15 Trois-Rivières QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 03:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04THOPECGALMAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gales / Markov (`KXITFDOUBLES-26NOV04THOPECGALMAR-GALMAR`) | 0.45 / 0.49 (49) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Thomas George / Peck (`KXITFDOUBLES-26NOV04THOPECGALMAR-THOPEC`) | 0.44 / 0.54 (22) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Eliot Nobel vs Mathias Roy -- M15 Trois-Rivières R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04NOBROY:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eliot Nobel (`KXITFMATCH-26NOV04NOBROY-NOB`) | 0.90 / 0.91 (5706) | 90.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mathias Roy (`KXITFMATCH-26NOV04NOBROY-ROY`) | 0.09 / 0.10 (11166) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sloane Stephens vs Carolina Kuhl -- W35 Orlando FL R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:201585:230882:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carolina Kuhl (`KXITFWMATCH-26NOV04STEKUH-KUH`) | 0.01 / 0.02 (8626) | 1.5% | 8.6% | 37.0% | 19.1% [11.3%-23.7%] | -- | -- | -- | -- | WATCH | +7.1 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sloane Stephens (`KXITFWMATCH-26NOV04STEKUH-STE`) | 0.98 / 0.99 (15258) | 98.5% | 91.4% | 63.0% | 80.9% [76.3%-88.7%] | -- | -- | -- | -- | PASS | -7.1 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2061.0, B 1139.0; serve-point win A 60.8%, B 49.5%; Elo A 1865.6, B 1482.7; model uncertainty 0.0619
* Form inputs: days since last match A 47, B 198; matches on record A 685, B 165; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.018, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carlevato / Vartak vs Lieberman / Sheldon -- M15 Hilton Head Island SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 04:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T04:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04CARVARLIESHE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlevato / Vartak (`KXITFDOUBLES-26NOV04CARVARLIESHE-CARVAR`) | 0.01 / 0.02 (120) | 1.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lieberman / Sheldon (`KXITFDOUBLES-26NOV04CARVARLIESHE-LIESHE`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE

## Delattre / Mirarchi vs Bybel / Jaen -- M15 Hilton Head Island SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 04:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T04:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04DELMIRBYBJAE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bybel / Jaen (`KXITFDOUBLES-26NOV04DELMIRBYBJAE-BYBJAE`) | 0.35 / 0.36 (0) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Delattre / Mirarchi (`KXITFDOUBLES-26NOV04DELMIRBYBJAE-DELMIR`) | 0.64 / 0.65 (2) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Alujas / Benson vs Cooper / McKennon -- M25 Guadalajara QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04ALUBENCOOMCK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alujas / Benson (`KXITFDOUBLES-26NOV04ALUBENCOOMCK-ALUBEN`) | 0.21 / 0.42 (0) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cooper / McKennon (`KXITFDOUBLES-26NOV04ALUBENCOOMCK-COOMCK`) | 0.50 / 0.68 (78) | 59.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Fuchs / Perez vs Jarvis / Matta -- M25 Guadalajara QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04FUCPERJARMAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fuchs / Perez (`KXITFDOUBLES-26NOV04FUCPERJARMAT-FUCPER`) | 0.70 / 0.83 (22) | 76.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jarvis / Matta (`KXITFDOUBLES-26NOV04FUCPERJARMAT-JARMAT`) | 0.08 / 0.23 (22) | 15.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Schiessl / Henry Van Schalkwyk vs Patil / Quattro -- M25 Harlingen TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 05:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T05:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04SCHHENPATQUA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Patil / Quattro (`KXITFDOUBLES-26NOV04SCHHENPATQUA-PATQUA`) | 0.16 / 0.37 (0) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Schiessl / Henry Van Schalkwyk (`KXITFDOUBLES-26NOV04SCHHENPATQUA-SCHHEN`) | 0.66 / 0.89 (5) | 77.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Elena Pridankina vs Alexandra Shubladze -- WTA Hong Kong R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-05 09:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-05 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: 2026-11-05 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-11-05T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:239389:260168:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elena Pridankina (`KXWTAMATCH-26NOV05PRISHU-PRI`) | 0.33 / 0.34 (22660) | 33.5% | 35.9% | 18.2% | 25.2% [20.3%-37.4%] | 34.2% | 33.6% | 33.9% | MODEL_LONE_OUTLIER | PASS | +2.4 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Alexandra Shubladze (`KXWTAMATCH-26NOV05PRISHU-SHU`) | 0.66 / 0.67 (1954) | 66.5% | 64.1% | 81.8% | 74.8% [62.6%-79.7%] | 65.8% | 66.5% | 66.1% | MODEL_LONE_OUTLIER | WATCH | -2.4 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3685.0, B 3247.0; serve-point win A 52.0%, B 45.3%; Elo A 1723.2, B 1769.1; model uncertainty 0.0854
* Form inputs: days since last match A 1, B 1; matches on record A 292, B 210; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.004, surface_dev_loose -0.000, surface_dev_tight -0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV05PRISHU-22` Over 21.5 games: 0.44/0.45 mid 44.5%, model 59.8% (projection_v2.0 (prediction ledger)) -- gap +15.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV05PRISHU-27` Over 26.5 games: 0.22/0.25 mid 23.5%, model 36.8% (projection_v2.0 (prediction ledger)) -- gap +13.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV05PRISHU-17` Over 16.5 games: 0.80/0.86 mid 83.0%, model 91.7% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV05PRISHU-2-PRI` Will Elena Pridankina win set 2 in the Elena Pridankina vs Alexandra Shubladze match: 0.34/0.38 mid 36.0%, model 40.5% (projection_v2.0 (prediction ledger)) -- gap +4.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV05PRISHU-1-PRI` Will Elena Pridankina win set 1 in the Elena Pridankina vs Alexandra Shubladze match: 0.36/0.39 mid 37.5%, model 40.5% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV05PRISHU-2-SHU` Will Alexandra Shubladze win set 2 in the Elena Pridankina vs Alexandra Shubladze match: 0.61/0.64 mid 62.5%, model 59.5% (projection_v2.0 (prediction ledger)) -- gap -3.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV05PRISHU-1-SHU` Will Alexandra Shubladze win set 1 in the Elena Pridankina vs Alexandra Shubladze match: 0.61/0.63 mid 62.0%, model 59.5% (projection_v2.0 (prediction ledger)) -- gap -2.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER

## Xinyu Wang vs Antonia Ruzic -- WTA Hong Kong R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-05 09:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-05 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: 2026-11-05 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · surface ? · scheduled 2026-11-05T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26NOV05WANRUZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Antonia Ruzic (`KXWTAMATCH-26NOV05WANRUZ-RUZ`) | 0.42 / 0.43 (365) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xinyu Wang (`KXWTAMATCH-26NOV05WANRUZ-WAN`) | 0.57 / 0.58 (2523) | 57.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Charles Broom vs Alexandre Muller -- ATP Challenger Taipei R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-05T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:124186:200277:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charles Broom (`KXATPCHALLENGERMATCH-26NOV04BROMUL-BRO`) | 0.44 / 0.45 (6227) | 44.5% | 51.4% | 80.4% | 71.9% [60.0%-77.5%] | 44.6% | 45.1% | 45.1% | MODEL_LONE_OUTLIER | WATCH | +6.9 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Alexandre Muller (`KXATPCHALLENGERMATCH-26NOV04BROMUL-MUL`) | 0.56 / 0.57 (6131) | 56.5% | 48.6% | 19.6% | 28.1% [22.5%-40.1%] | 55.4% | 55.1% | 55.1% | MODEL_LONE_OUTLIER | PASS | -7.9 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4307.0, B 4505.0; serve-point win A 63.1%, B 37.1%; Elo A 1636.7, B 1713.7; model uncertainty 0.0877
* Form inputs: days since last match A 9, B 9; matches on record A 395, B 787; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.026, surface_pool_high +0.017, surface_dev_loose +0.017, surface_dev_tight -0.030
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Jake Delaney vs Omar Jasika -- ATP Challenger Taipei R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-05T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:117357:117359:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jake Delaney (`KXATPCHALLENGERMATCH-26NOV04DELJAS-DEL`) | 0.36 / 0.37 (127) | 36.5% | 35.9% | 43.1% | 40.7% [39.8%-41.7%] | 37.5% | 36.8% | 36.8% | MODEL_LONE_OUTLIER | WATCH | -0.6 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Omar Jasika (`KXATPCHALLENGERMATCH-26NOV04DELJAS-JAS`) | 0.63 / 0.64 (6034) | 63.5% | 64.1% | 56.9% | 59.3% [58.3%-60.2%] | 62.5% | 63.7% | 63.7% | MODEL_LONE_OUTLIER | PASS | +0.6 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3349.0, B 3977.0; serve-point win A 63.6%, B 33.4%; Elo A 1432.1, B 1522.2; model uncertainty 0.0097
* Form inputs: days since last match A 9, B 9; matches on record A 343, B 520; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Rengifo / Esteban Rico Arias vs De Alba / Sau Franco -- M25 Guadalajara QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 06:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T06:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04RENESTDEASAU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| De Alba / Sau Franco (`KXITFDOUBLES-26NOV04RENESTDEASAU-DEASAU`) | 0.15 / 0.82 (138) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rengifo / Esteban Rico Arias (`KXITFDOUBLES-26NOV04RENESTDEASAU-RENEST`) | 0.12 / 0.79 (2) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alan Fernando Rubio Fierros vs Elijah Strode -- M25 Guadalajara R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 06:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T06:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200214:210565:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alan Fernando Rubio Fierros (`KXITFMATCH-26NOV04RUBSTR-RUB`) | 0.74 / 0.76 (362) | 75.0% | 65.3% | 66.6% | 64.8% [63.0%-66.6%] | 72.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elijah Strode (`KXITFMATCH-26NOV04RUBSTR-STR`) | 0.24 / 0.25 (226) | 24.5% | 34.7% | 33.4% | 35.2% [33.4%-37.0%] | 27.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +10.2 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1893.0, B 869.0; serve-point win A 67.5%, B 35.7%; Elo A 1403.1, B 1301.0; model uncertainty 0.0177
* Form inputs: days since last match A 45, B 478; matches on record A 179, B 57; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.000, surface_dev_loose +0.012, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Harold Mayot vs Sho Shimabukuro -- ATP Challenger Taipei R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 07:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-05T07:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200647:208004:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Harold Mayot (`KXATPCHALLENGERMATCH-26NOV04MAYSHI-MAY`) | 0.54 / 0.55 (1256) | 54.5% | 58.6% | 74.0% | 69.7% [67.0%-71.9%] | 54.1% | 54.8% | 54.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +4.1 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Sho Shimabukuro (`KXATPCHALLENGERMATCH-26NOV04MAYSHI-SHI`) | 0.45 / 0.46 (2936) | 45.5% | 41.4% | 26.0% | 30.3% [28.1%-33.0%] | 45.9% | 45.5% | 45.7% | MODEL_LONE_OUTLIER | PASS | -4.1 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4935.0, B 5296.0; serve-point win A 63.8%, B 37.9%; Elo A 1731.6, B 1701.9; model uncertainty 0.0242
* Form inputs: days since last match A 9, B 9; matches on record A 412, B 467; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.004, surface_dev_loose +0.017, surface_dev_tight -0.018
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Yosuke Watanuki vs Masamichi Imamura -- ATP Challenger Taipei R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 07:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-05T07:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:133297:201987:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Masamichi Imamura (`KXATPCHALLENGERMATCH-26NOV04WATIMA-IMA`) | 0.15 / 0.17 (4684) | 16.0% | 26.8% | 44.9% | 36.9% [33.6%-39.9%] | 17.9% | 16.5% | 17.2% | MODEL_LONE_OUTLIER | WATCH | +10.8 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Yosuke Watanuki (`KXATPCHALLENGERMATCH-26NOV04WATIMA-WAT`) | 0.83 / 0.84 (435) | 83.5% | 73.2% | 55.1% | 63.1% [60.1%-66.4%] | 82.1% | 83.7% | 82.9% | MODEL_LONE_OUTLIER | PASS | -10.3 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3158.0, B 3187.0; serve-point win A 63.3%, B 41.5%; Elo A 1682.9, B 1472.8; model uncertainty 0.0313
* Form inputs: days since last match A 23, B 9; matches on record A 449, B 251; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.015, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Talia Gibson / Maddison Inglis vs Qianhui Tang / Qiu Yu Ye -- WTA Hong Kong QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-05 10:10Z
* Current expected start: 2026-11-05 07:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: 2026-11-05 06:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-05T10:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05GIBINGTANQIU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Talia Gibson / Maddison Inglis (`KXWTADOUBLES-26NOV05GIBINGTANQIU-GIBING`) | 0.62 / 0.66 (25) | 64.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Qianhui Tang / Qiu Yu Ye (`KXWTADOUBLES-26NOV05GIBINGTANQIU-TANQIU`) | 0.34 / 0.36 (50) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Mika Stojsavljevic vs Zeynep Sonmez -- WTA Hong Kong R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-05 09:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-05 07:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: 2026-11-05 06:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-11-05T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:220309:261963:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zeynep Sonmez (`KXWTAMATCH-26NOV05STOSON-SON`) | 0.76 / 0.77 (36) | 76.5% | 69.3% | 65.7% | 68.1% [64.8%-74.1%] | 75.5% | 76.7% | 76.1% | MODEL_LONE_OUTLIER | PASS | -7.2 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Mika Stojsavljevic (`KXWTAMATCH-26NOV05STOSON-STO`) | 0.23 / 0.24 (1463) | 23.5% | 30.6% | 34.3% | 31.9% [25.9%-35.2%] | 24.5% | 24.3% | 24.4% | MODEL_LONE_OUTLIER | WATCH | +7.2 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2019.0, B 4355.0; serve-point win A 56.5%, B 39.6%; Elo A 1678.7, B 1833.9; model uncertainty 0.0466
* Form inputs: days since last match A 0, B 1; matches on record A 79, B 432; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.023, surface_pool_high +0.033, surface_dev_loose +0.000, surface_dev_tight +0.004
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV05STOSON-16` Over 15.5 games: 0.41/0.93 mid 67.0%, model 97.0% (projection_v2.0 (prediction ledger)) -- gap +30.0 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV05STOSON-21` Over 20.5 games: 0.45/0.47 mid 46.0%, model 65.4% (projection_v2.0 (prediction ledger)) -- gap +19.4 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV05STOSON-26` Over 25.5 games: 0.25/0.28 mid 26.5%, model 42.3% (projection_v2.0 (prediction ledger)) -- gap +15.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV05STOSON-2-STO` Will Mika Stojsavljevic win set 2 in the Mika Stojsavljevic vs Zeynep Sonmez match: 0.26/0.29 mid 27.5%, model 36.8% (projection_v2.0 (prediction ledger)) -- gap +9.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV05STOSON-2-SON` Will Zeynep Sonmez win set 2 in the Mika Stojsavljevic vs Zeynep Sonmez match: 0.70/0.73 mid 71.5%, model 63.2% (projection_v2.0 (prediction ledger)) -- gap -8.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV05STOSON-1-SON` Will Zeynep Sonmez win set 1 in the Mika Stojsavljevic vs Zeynep Sonmez match: 0.69/0.71 mid 70.0%, model 63.2% (projection_v2.0 (prediction ledger)) -- gap -6.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV05STOSON-1-STO` Will Mika Stojsavljevic win set 1 in the Mika Stojsavljevic vs Zeynep Sonmez match: 0.29/0.31 mid 30.0%, model 36.8% (projection_v2.0 (prediction ledger)) -- gap +6.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kristjan Tamm vs Filip Peliwo -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106290:144932:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Filip Peliwo (`KXITFMATCH-26NOV04TAMPEL-PEL`) | 0.49 / 0.52 (290) | 50.5% | 67.1% | 68.4% | 68.4% [66.3%-70.1%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +16.6 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kristjan Tamm (`KXITFMATCH-26NOV04TAMPEL-TAM`) | 0.48 / 0.50 (295) | 49.0% | 32.9% | 31.6% | 31.6% [29.9%-33.7%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -16.1 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1552.0, B 3377.0; serve-point win A 61.3%, B 35.2%; Elo A 1248.5, B 1385.5; model uncertainty 0.0188
* Form inputs: days since last match A 47, B 9; matches on record A 257, B 825; data quality A

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV04TAMPEL-PEL  (YES = Filip Peliwo)
Model: 67%
Kalshi: 50%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.008, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maxim Zhukov vs Yue Xia -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210393:213883:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yue Xia (`KXITFMATCH-26NOV04ZHUXIA-XIA`) | 0.15 / 0.18 (811) | 16.5% | 9.3% | 6.9% | 17.7% [13.6%-19.5%] | 17.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maxim Zhukov (`KXITFMATCH-26NOV04ZHUXIA-ZHU`) | 0.82 / 0.85 (133) | 83.5% | 90.7% | 93.1% | 82.3% [80.5%-86.4%] | 82.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2791.0, B 202.0; serve-point win A 63.3%, B 46.8%; Elo A 1452.3, B 1205.9; model uncertainty 0.0297
* Form inputs: days since last match A 86, B 422; matches on record A 199, B 4; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.011, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tiana Tian Deng vs Nanari Katsumi -- W35 Hamamatsu R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Carpet · scheduled 2026-11-05T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:253679:260528:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tiana Tian Deng (`KXITFWMATCH-26NOV04DENKAT-DEN`) | 0.79 / 0.81 (231) | 80.0% | 62.5% | 48.9% | 50.5% [50.0%-52.7%] | 76.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -17.5 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nanari Katsumi (`KXITFWMATCH-26NOV04DENKAT-KAT`) | 0.19 / 0.21 (130) | 20.0% | 37.5% | 51.1% | 49.5% [47.3%-50.0%] | 23.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +17.5 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 853.0, B 1096.0; serve-point win A 55.1%, B 47.3%; Elo A 1297.9, B 1280.3; model uncertainty 0.0133
* Form inputs: days since last match A 121, B 226; matches on record A 41, B 139; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV04DENKAT-KAT  (YES = Nanari Katsumi)
Model: 38%
Kalshi: 20%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xinyu Gao vs Priska Madelyn Nugroho -- W100 Incheon R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214386:221187:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xinyu Gao (`KXITFWMATCH-26NOV04GAONUG-GAO`) | 0.61 / 0.63 (227) | 62.0% | 80.2% | 71.2% | 70.3% [68.9%-71.6%] | 61.5% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +18.2 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Priska Madelyn Nugroho (`KXITFWMATCH-26NOV04GAONUG-NUG`) | 0.37 / 0.39 (137) | 38.0% | 19.8% | 28.8% | 29.7% [28.4%-31.1%] | 38.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -18.2 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3203.0, B 2457.0; serve-point win A 58.4%, B 48.0%; Elo A 1711.8, B 1567.2; model uncertainty 0.0136
* Form inputs: days since last match A 32, B 219; matches on record A 419, B 235; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV04GAONUG-GAO  (YES = Xinyu Gao)
Model: 80%
Kalshi: 62%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.000, surface_dev_loose +0.013, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kurea Hayasaka vs Yuno Kitahara -- W35 Hamamatsu R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Carpet · scheduled 2026-11-05T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:263865:263881:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kurea Hayasaka (`KXITFWMATCH-26NOV04HAYKIT-HAY`) | 0.60 / 0.62 (33) | 61.0% | 21.2% | 35.5% | 31.2% [29.7%-33.1%] | 60.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -39.8 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuno Kitahara (`KXITFWMATCH-26NOV04HAYKIT-KIT`) | 0.37 / 0.40 (469) | 38.5% | 78.8% | 64.5% | 68.8% [66.9%-70.3%] | 39.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +40.2 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 337.0, B 2068.0; serve-point win A 52.7%, B 41.3%; Elo A 1231.3, B 1370.5; model uncertainty 0.0169
* Form inputs: days since last match A 205, B 198; matches on record A 9, B 119; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV04HAYKIT-KIT  (YES = Yuno Kitahara)
Model: 79%
Kalshi: 38%
Gap: +40 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.019, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ayano Shimizu vs Haruna Arakawa -- W35 Hamamatsu R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Carpet · scheduled 2026-11-05T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214505:215550:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Haruna Arakawa (`KXITFWMATCH-26NOV04SHIARA-ARA`) | 0.24 / 0.25 (26) | 24.5% | 26.8% | 45.2% | 34.4% [28.7%-37.9%] | 24.7% | -- | 24.7% | MODEL_LONE_OUTLIER | PASS | +2.3 pp | NORMAL | FRESH | D / POOR | ALL_AGREE | VERIFIED |
| Ayano Shimizu (`KXITFWMATCH-26NOV04SHIARA-SHI`) | 0.74 / 0.76 (228) | 75.0% | 73.2% | 54.8% | 65.6% [62.1%-71.3%] | 75.3% | -- | 75.3% | MODEL_LONE_OUTLIER | PASS | -1.8 pp | NORMAL | FRESH | D / POOR | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 1770.0, B 2195.0; serve-point win A 55.3%, B 49.4%; Elo A 1677.5, B 1466.1; model uncertainty 0.0459
* Form inputs: days since last match A 191, B 366; matches on record A 430, B 411; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose +0.019, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maiko Uchijima vs Koharu Ito -- W35 Hamamatsu R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Carpet · scheduled 2026-11-05T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264134:270096:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Koharu Ito (`KXITFWMATCH-26NOV04UCHITO-ITO`) | 0.14 / 0.17 (127) | 15.5% | 22.9% | 23.9% | 35.4% [35.4%-36.4%] | 18.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Maiko Uchijima (`KXITFWMATCH-26NOV04UCHITO-UCH`) | 0.83 / 0.84 (27) | 83.5% | 77.1% | 76.1% | 64.6% [63.6%-64.6%] | 81.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 31.0; serve-point win A 56.6%, B 49.0%; Elo A 1346.7, B 1247.1; model uncertainty 0.005
* Form inputs: days since last match A 1234, B 366; matches on record A 10, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jiaqi Wang vs Zijun Jiang -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221181:223214:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zijun Jiang (`KXITFWMATCH-26NOV04WANJIA-JIA`) | 0.24 / 0.26 (5) | 25.0% | 16.7% | 19.7% | 25.2% [23.6%-26.1%] | 25.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jiaqi Wang (`KXITFWMATCH-26NOV04WANJIA-WAN`) | 0.73 / 0.76 (16) | 74.5% | 83.3% | 80.3% | 74.8% [73.9%-76.4%] | 74.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +8.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2849.0, B 178.0; serve-point win A 58.1%, B 49.1%; Elo A 1543.7, B 1360.3; model uncertainty 0.0126
* Form inputs: days since last match A 191, B 191; matches on record A 250, B 73; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.017, surface_pool_high -0.009, surface_dev_loose +0.000, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sara Yoshida vs Yuhan Wang -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264205:267419:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuhan Wang (`KXITFWMATCH-26NOV04YOSWAN-WAN`) | 0.82 / 0.83 (153) | 82.5% | 92.4% | 81.8% | 78.8% [78.1%-80.3%] | 81.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +9.9 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sara Yoshida (`KXITFWMATCH-26NOV04YOSWAN-YOS`) | 0.16 / 0.17 (8) | 16.5% | 7.6% | 18.2% | 21.1% [19.7%-21.9%] | 18.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.9 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 151.0, B 1724.0; serve-point win A 48.5%, B 40.7%; Elo A 1200.0, B 1428.1; model uncertainty 0.0114
* Form inputs: days since last match A 198, B 34; matches on record A 8, B 44; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose -0.008, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexander Donski / David Poljak vs Ray Ho / Mili Poljicak -- ATP Challenger Taipei QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 08:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-05T08:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05DONPOLRAYPOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Donski / David Poljak (`KXATPCHALLENGERDOUBLES-26NOV05DONPOLRAYPOL-DONPOL`) | 0.45 / 0.52 (25) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ray Ho / Mili Poljicak (`KXATPCHALLENGERDOUBLES-26NOV05DONPOLRAYPOL-RAYPOL`) | 0.48 / 0.55 (25) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Nathaniel Lammons / Jackson Withrow vs Anirudh Chandrasekar / Ajeet Rai -- ATP Challenger Taipei QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 08:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-05T08:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05LAMWITCHARAI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anirudh Chandrasekar / Ajeet Rai (`KXATPCHALLENGERDOUBLES-26NOV05LAMWITCHARAI-CHARAI`) | 0.25 / 0.29 (5) | 27.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nathaniel Lammons / Jackson Withrow (`KXATPCHALLENGERDOUBLES-26NOV05LAMWITCHARAI-LAMWIT`) | 0.68 / 0.75 (25) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Katie Swan vs Rina Saigo -- W100 Incheon R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 08:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215042:221099:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rina Saigo (`KXITFWMATCH-26NOV04SWASAI-SAI`) | 0.12 / 0.13 (4) | 12.5% | 17.7% | 15.0% | 19.1% [15.7%-26.6%] | -- | -- | -- | -- | WATCH | +5.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Katie Swan (`KXITFWMATCH-26NOV04SWASAI-SWA`) | 0.85 / 0.87 (150) | 86.0% | 82.3% | 85.0% | 81.0% [73.4%-84.3%] | -- | -- | -- | -- | PASS | -3.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2343.0, B 3065.0; serve-point win A 59.0%, B 48.0%; Elo A 1722.0, B 1547.5; model uncertainty 0.0545
* Form inputs: days since last match A 40, B 11; matches on record A 387, B 396; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.004, surface_dev_tight -0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anna Blinkova vs Zongyu Li -- WTA 125K Luanda R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-05 12:00Z
* Current expected start: 2026-11-05 09:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: 2026-11-05 08:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-11-05T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26NOV05BLIZON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Blinkova (`KXWTACHALLENGERMATCH-26NOV05BLIZON-BLI`) | 0.89 / 0.91 (1097) | 90.0% | -- | -- | -- [-----] | 88.2% | 90.1% | 90.1% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Zongyu Li (`KXWTACHALLENGERMATCH-26NOV05BLIZON-ZON`) | 0.09 / 0.10 (93) | 9.5% | -- | -- | -- [-----] | 11.8% | 9.7% | 9.7% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## I-Hsuan Cho / Yi Tsen Cho vs Xinyu Jiang / Hong Yi Cody Wong -- WTA Hong Kong QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-05 11:20Z
* Current expected start: 2026-11-05 09:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: 2026-11-05 08:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-05T11:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05CHOCHOJIAWON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I-Hsuan Cho / Yi Tsen Cho (`KXWTADOUBLES-26NOV05CHOCHOJIAWON-CHOCHO`) | 0.44 / 0.47 (9) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xinyu Jiang / Hong Yi Cody Wong (`KXWTADOUBLES-26NOV05CHOCHOJIAWON-JIAWON`) | 0.53 / 0.56 (227) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Kristina Kroitor vs Ksenia Zaytseva -- WTA 125K Luanda R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-05 12:00Z
* Current expected start: 2026-11-05 09:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: 2026-11-05 08:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-11-05T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26NOV05KROZAY:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kristina Kroitor (`KXWTACHALLENGERMATCH-26NOV05KROZAY-KRO`) | 0.30 / 0.33 (696) | 31.5% | -- | -- | -- [-----] | -- | 32.4% | 32.4% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ksenia Zaytseva (`KXWTACHALLENGERMATCH-26NOV05KROZAY-ZAY`) | 0.68 / 0.70 (1068) | 69.0% | -- | -- | -- [-----] | -- | 69.1% | 69.1% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Jesika Maleckova / Miriam Skoch vs Venus Williams / Yifan Xu -- WTA Hong Kong QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-05 12:30Z
* Current expected start: 2026-11-05 09:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: 2026-11-05 08:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-05T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05MALSKOWILYIF:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jesika Maleckova / Miriam Skoch (`KXWTADOUBLES-26NOV05MALSKOWILYIF-MALSKO`) | 0.46 / 0.58 (52) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Venus Williams / Yifan Xu (`KXWTADOUBLES-26NOV05MALSKOWILYIF-WILYIF`) | 0.37 / 0.48 (25) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Zhuoxuan Bai vs Sara Saito -- W100 Incheon R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222296:260170:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zhuoxuan Bai (`KXITFWMATCH-26NOV04BAISAI-BAI`) | 0.61 / 0.64 (74) | 62.5% | 81.3% | 79.7% | 77.4% [69.5%-80.9%] | 62.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +18.8 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sara Saito (`KXITFWMATCH-26NOV04BAISAI-SAI`) | 0.35 / 0.37 (224) | 36.0% | 18.7% | 20.3% | 22.6% [19.1%-30.5%] | 37.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -17.3 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1601.0, B 3341.0; serve-point win A 54.8%, B 51.8%; Elo A 1765.4, B 1574.9; model uncertainty 0.0568
* Form inputs: days since last match A 26, B 37; matches on record A 213, B 198; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV04BAISAI-BAI  (YES = Zhuoxuan Bai)
Model: 81%
Kalshi: 62%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.023, surface_dev_loose +0.016, surface_dev_tight -0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yujin Kim vs Berfu Cengiz -- W100 Incheon R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214507:264973:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Berfu Cengiz (`KXITFWMATCH-26NOV04KIMCEN-CEN`) | 0.83 / 0.86 (824) | 84.5% | 73.9% | 54.8% | 61.5% [57.4%-70.3%] | 80.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -10.6 pp | REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yujin Kim (`KXITFWMATCH-26NOV04KIMCEN-KIM`) | 0.15 / 0.17 (16) | 16.0% | 26.1% | 45.2% | 38.5% [29.7%-42.6%] | 19.5% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +10.1 pp | REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1654.0, B 1612.0; serve-point win A 52.4%, B 42.8%; Elo A 1434.1, B 1571.0; model uncertainty 0.0646
* Form inputs: days since last match A 191, B 36; matches on record A 103, B 455; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.035, surface_pool_high +0.031, surface_dev_loose -0.015, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Funa Kozaki vs Mio Mushika -- W35 Hamamatsu R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Carpet · scheduled 2026-11-05T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216260:222986:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Funa Kozaki (`KXITFWMATCH-26NOV04KOZMUS-KOZ`) | 0.44 / 0.47 (14) | 45.5% | 44.5% | 17.9% | 46.3% [42.1%-50.0%] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.0 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mio Mushika (`KXITFWMATCH-26NOV04KOZMUS-MUS`) | 0.53 / 0.55 (44) | 54.0% | 55.5% | 82.1% | 53.7% [50.0%-57.9%] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 166.0, B 2224.0; serve-point win A 54.1%, B 44.8%; Elo A 1477.7, B 1475.3; model uncertainty 0.0397
* Form inputs: days since last match A 198, B 198; matches on record A 222, B 201; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.011, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kanon Sawashiro vs Sae Noguchi -- W35 Hamamatsu R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Carpet · scheduled 2026-11-05T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:263905:269866:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sae Noguchi (`KXITFWMATCH-26NOV04SAWNOG-NOG`) | 0.48 / 0.49 (16) | 48.5% | 51.3% | 43.6% | 54.8% [51.6%-60.1%] | 50.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +2.8 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kanon Sawashiro (`KXITFWMATCH-26NOV04SAWNOG-SAW`) | 0.50 / 0.51 (225) | 50.5% | 48.7% | 56.4% | 45.2% [40.0%-48.4%] | 50.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.8 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 827.0, B 1076.0; serve-point win A 51.8%, B 48.0%; Elo A 1351.6, B 1429.2; model uncertainty 0.0422
* Form inputs: days since last match A 18, B 205; matches on record A 37, B 33; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.021, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chia Yi Tsao vs Kisa Yoshioka -- W35 Hamamatsu R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Carpet · scheduled 2026-11-05T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215616:259623:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chia Yi Tsao (`KXITFWMATCH-26NOV04TSAYOS-TSA`) | 0.49 / 0.50 (70) | 49.5% | 71.3% | 62.5% | 65.5% [64.0%-65.9%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +21.8 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kisa Yoshioka (`KXITFWMATCH-26NOV04TSAYOS-YOS`) | 0.49 / 0.51 (116) | 50.0% | 28.7% | 37.5% | 34.5% [34.1%-36.0%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -21.3 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 824.0, B 1530.0; serve-point win A 58.1%, B 46.1%; Elo A 1478.6, B 1360.9; model uncertainty 0.0094
* Form inputs: days since last match A 198, B 198; matches on record A 145, B 159; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV04TSAYOS-TSA  (YES = Chia Yi Tsao)
Model: 71%
Kalshi: 50%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Shiho Tsujioka vs Sera Nishimoto -- W35 Hamamatsu R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Carpet · scheduled 2026-11-05T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221621:263801:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sera Nishimoto (`KXITFWMATCH-26NOV04TSUNIS-NIS`) | 0.18 / 0.20 (26) | 19.0% | 28.0% | 29.6% | 35.9% [32.4%-38.4%] | 21.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +9.0 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Shiho Tsujioka (`KXITFWMATCH-26NOV04TSUNIS-TSU`) | 0.79 / 0.81 (22) | 80.0% | 72.0% | 70.4% | 64.1% [61.6%-67.6%] | 78.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.0 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1131.0, B 590.0; serve-point win A 54.4%, B 50.0%; Elo A 1368.7, B 1288.4; model uncertainty 0.03
* Form inputs: days since last match A 11, B 191; matches on record A 43, B 53; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Moyuka Uchijima vs Magda Linette -- WTA Chennai R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-04 12:30Z
* Current expected start: 2026-11-05 09:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: 2026-11-05 08:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1260_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-11-04T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202663:220416:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Magda Linette (`KXWTAMATCH-26NOV04UCHLIN-LIN`) | 0.55 / 0.57 (7808) | 56.0% | 56.8% | 46.4% | 52.1% [50.0%-57.8%] | -- | -- | -- | -- | PASS | +0.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Moyuka Uchijima (`KXWTAMATCH-26NOV04UCHLIN-UCH`) | 0.43 / 0.45 (2492) | 44.0% | 43.2% | 53.6% | 47.9% [42.2%-50.0%] | -- | -- | -- | -- | WATCH | -0.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4591.0, B 4278.0; serve-point win A 57.8%, B 40.9%; Elo A 1740.3, B 1876.0; model uncertainty 0.0391
* Form inputs: days since last match A 9, B 6; matches on record A 476, B 913; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose +0.005, surface_dev_tight -0.010
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV04UCHLIN-20` Over 19.5 games: 0.63/0.65 mid 64.0%, model 75.6% (projection_v2.0 (prediction ledger)) -- gap +11.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV04UCHLIN-25` Over 24.5 games: 0.39/0.40 mid 39.5%, model 49.9% (projection_v2.0 (prediction ledger)) -- gap +10.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV04UCHLIN-15` Over 14.5 games: 0.91/0.97 mid 94.0%, model 99.3% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV04UCHLIN-1-LIN` Will Magda Linette win set 1 in the Moyuka Uchijima vs Magda Linette match: 0.53/0.55 mid 54.0%, model 54.5% (projection_v2.0 (prediction ledger)) -- gap +0.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV04UCHLIN-1-UCH` Will Moyuka Uchijima win set 1 in the Moyuka Uchijima vs Magda Linette match: 0.44/0.47 mid 45.5%, model 45.5% (projection_v2.0 (prediction ledger)) -- gap -0.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV04UCHLIN-2-LIN` Will Magda Linette win set 2 in the Moyuka Uchijima vs Magda Linette match: 0.51/0.58 mid 54.5%, model 54.5% (projection_v2.0 (prediction ledger)) -- gap +0.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV04UCHLIN-2-UCH` Will Moyuka Uchijima win set 2 in the Moyuka Uchijima vs Magda Linette match: 0.42/0.49 mid 45.5%, model 45.5% (projection_v2.0 (prediction ledger)) -- gap -0.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mai Hontama vs Zhibek Kulambayeva -- WTA Chennai R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-05 12:30Z
* Current expected start: 2026-11-05 09:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: 2026-11-05 08:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-11-05T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214992:215988:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mai Hontama (`KXWTAMATCH-26NOV05HONKUL-HON`) | 0.80 / 0.81 (163) | 80.5% | 74.8% | 42.6% | 58.0% [52.7%-65.6%] | 78.6% | 81.0% | 79.8% | MODEL_LONE_OUTLIER | PASS | -5.8 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Zhibek Kulambayeva (`KXWTAMATCH-26NOV05HONKUL-KUL`) | 0.19 / 0.20 (6211) | 19.5% | 25.2% | 57.4% | 42.0% [34.4%-47.3%] | 21.4% | 19.7% | 20.5% | MODEL_LONE_OUTLIER | WATCH | +5.8 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4001.0, B 2176.0; serve-point win A 56.2%, B 48.8%; Elo A 1680.0, B 1460.5; model uncertainty 0.0645
* Form inputs: days since last match A 1, B 1; matches on record A 493, B 438; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.026, surface_pool_high +0.031, surface_dev_loose +0.026, surface_dev_tight -0.016
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV05HONKUL-15` Over 14.5 games: 0.44/0.94 mid 69.0%, model 98.0% (projection_v2.0 (prediction ledger)) -- gap +29.0 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV05HONKUL-20` Over 19.5 games: 0.48/0.50 mid 49.0%, model 67.0% (projection_v2.0 (prediction ledger)) -- gap +17.9 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV05HONKUL-25` Over 24.5 games: 0.26/0.29 mid 27.5%, model 42.3% (projection_v2.0 (prediction ledger)) -- gap +14.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV05HONKUL-2-KUL` Will Zhibek Kulambayeva win set 2 in the Mai Hontama vs Zhibek Kulambayeva match: 0.21/0.25 mid 23.0%, model 32.8% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV05HONKUL-2-HON` Will Mai Hontama win set 2 in the Mai Hontama vs Zhibek Kulambayeva match: 0.73/0.79 mid 76.0%, model 67.2% (projection_v2.0 (prediction ledger)) -- gap -8.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV05HONKUL-1-HON` Will Mai Hontama win set 1 in the Mai Hontama vs Zhibek Kulambayeva match: 0.73/0.75 mid 74.0%, model 67.2% (projection_v2.0 (prediction ledger)) -- gap -6.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV05HONKUL-1-KUL` Will Zhibek Kulambayeva win set 1 in the Mai Hontama vs Zhibek Kulambayeva match: 0.25/0.27 mid 26.0%, model 32.8% (projection_v2.0 (prediction ledger)) -- gap +6.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Cheng-Peng Hsieh / Yu Hsiou Hsu vs Thijmen Loof / Kaito Uesugi -- ATP Challenger Taipei QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-05T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05HSIHSULOOUES:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cheng-Peng Hsieh / Yu Hsiou Hsu (`KXATPCHALLENGERDOUBLES-26NOV05HSIHSULOOUES-HSIHSU`) | 0.14 / 0.21 (25) | 17.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Thijmen Loof / Kaito Uesugi (`KXATPCHALLENGERDOUBLES-26NOV05HSIHSULOOUES-LOOUES`) | 0.79 / 0.86 (25) | 82.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Alexandru Jecan / Szymon Kielan vs Finn Reynolds / James Watt -- ATP Challenger Taipei QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-05T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05JECKIEREYWAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandru Jecan / Szymon Kielan (`KXATPCHALLENGERDOUBLES-26NOV05JECKIEREYWAT-JECKIE`) | 0.23 / 0.29 (28) | 26.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Finn Reynolds / James Watt (`KXATPCHALLENGERDOUBLES-26NOV05JECKIEREYWAT-REYWAT`) | 0.70 / 0.77 (112) | 73.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Han Shi vs Yujia Huang -- W100 Incheon R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222559:264207:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yujia Huang (`KXITFWMATCH-26NOV04SHIHUA-HUA`) | 0.25 / 0.28 (5) | 26.5% | 21.1% | 36.0% | 32.5% [29.2%-35.0%] | 28.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -5.4 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Han Shi (`KXITFWMATCH-26NOV04SHIHUA-SHI`) | 0.72 / 0.75 (745) | 73.5% | 78.9% | 64.0% | 67.5% [65.0%-70.8%] | 72.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.4 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3226.0, B 1640.0; serve-point win A 58.1%, B 48.0%; Elo A 1600.6, B 1447.1; model uncertainty 0.0288
* Form inputs: days since last match A 191, B 31; matches on record A 228, B 88; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.010, surface_dev_loose +0.009, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Petr Nouza / Michael Venus vs Marcelo Arevalo / Mate Pavic -- ATP Paris R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-04 12:00Z
* Current expected start: 2026-11-05 10:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: 2026-11-05 09:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-04T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04NOUVENAREPAV:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcelo Arevalo / Mate Pavic (`KXATPDOUBLES-26NOV04NOUVENAREPAV-AREPAV`) | 0.64 / 0.67 (703) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Petr Nouza / Michael Venus (`KXATPDOUBLES-26NOV04NOUVENAREPAV-NOUVEN`) | 0.33 / 0.35 (285) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Orlando Luz / Rafael Matos vs Lucas Miedler / Neil Oberleitner -- ATP Paris R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-05 13:00Z
* Current expected start: 2026-11-05 10:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: 2026-11-05 09:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-05T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05LUZMATMIEOBE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Orlando Luz / Rafael Matos (`KXATPDOUBLES-26NOV05LUZMATMIEOBE-LUZMAT`) | 0.36 / 0.39 (203) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lucas Miedler / Neil Oberleitner (`KXATPDOUBLES-26NOV05LUZMATMIEOBE-MIEOBE`) | 0.62 / 0.63 (38) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Tommy Paul vs Quentin Halys -- ATP Paris R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-05 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-05 10:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: 2026-11-05 09:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · Hard · scheduled 2026-11-05T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111460:126205:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Quentin Halys (`KXATPMATCH-26NOV05PAUHAL-HAL`) | 0.26 / 0.27 (89) | 26.5% | 29.0% | 30.2% | 29.0% [27.7%-29.4%] | 28.2% | 26.7% | 26.7% | MARKETS_AGREE | PASS | +2.5 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Tommy Paul (`KXATPMATCH-26NOV05PAUHAL-PAU`) | 0.73 / 0.74 (61743) | 73.5% | 71.0% | 69.8% | 71.0% [70.6%-72.3%] | 71.8% | 73.3% | 73.3% | MARKETS_AGREE | PASS | -2.5 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 6173.0, B 6312.0; serve-point win A 69.6%, B 35.0%; Elo A 2042.0, B 1846.7; model uncertainty 0.0085
* Form inputs: days since last match A 0, B 0; matches on record A 734, B 842; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high +0.000, surface_dev_loose +0.004, surface_dev_tight +0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26NOV05PAUHAL-HAL20` Will Quentin Halys win the Tommy Paul vs Quentin Halys match by a set score of 2-0?: 0.10/0.91 mid 50.5%, model 12.7% (projection_v2.0 (prediction ledger)) -- gap -37.8 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV05PAUHAL-HAL2` Will Quentin Halys win at least 1.5 more games than Tommy Paul?: 0.03/0.91 mid 47.0%, model 22.3% (projection_v2.0 (prediction ledger)) -- gap -24.7 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV05PAUHAL-PAU7` Will Tommy Paul win at least 6.5 more games than Quentin Halys?: 0.02/0.53 mid 27.5%, model 5.6% (projection_v2.0 (prediction ledger)) -- gap -21.9 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05PAUHAL-PAU21` Will Tommy Paul win the Tommy Paul vs Quentin Halys match by a set score of 2-1?: 0.01/0.29 mid 15.0%, model 29.5% (projection_v2.0 (prediction ledger)) -- gap +14.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05PAUHAL-HAL21` Will Quentin Halys win the Tommy Paul vs Quentin Halys match by a set score of 2-1?: 0.02/0.52 mid 27.0%, model 16.3% (projection_v2.0 (prediction ledger)) -- gap -10.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV05PAUHAL-23` Over 22.5 games: 0.53/0.54 mid 53.5%, model 61.2% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV05PAUHAL-28` Over 27.5 games: 0.32/0.35 mid 33.5%, model 40.5% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV05PAUHAL-PAU4` Will Tommy Paul win at least 3.5 more games than Quentin Halys?: 0.46/0.47 mid 46.5%, model 39.8% (projection_v2.0 (prediction ledger)) -- gap -6.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV05PAUHAL-2-HAL` Will Quentin Halys win set 2 in the Tommy Paul vs Quentin Halys match: 0.29/0.33 mid 31.0%, model 35.6% (projection_v2.0 (prediction ledger)) -- gap +4.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV05PAUHAL-2-PAU` Will Tommy Paul win set 2 in the Tommy Paul vs Quentin Halys match: 0.67/0.71 mid 69.0%, model 64.4% (projection_v2.0 (prediction ledger)) -- gap -4.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV05PAUHAL-1-PAU` Will Tommy Paul win set 1 in the Tommy Paul vs Quentin Halys match: 0.66/0.70 mid 68.0%, model 64.4% (projection_v2.0 (prediction ledger)) -- gap -3.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV05PAUHAL-18` Over 17.5 games: 0.90/0.93 mid 91.5%, model 94.9% (projection_v2.0 (prediction ledger)) -- gap +3.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV05PAUHAL-1-HAL` Will Quentin Halys win set 1 in the Tommy Paul vs Quentin Halys match: 0.32/0.34 mid 33.0%, model 35.6% (projection_v2.0 (prediction ledger)) -- gap +2.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05PAUHAL-PAU20` Will Tommy Paul win the Tommy Paul vs Quentin Halys match by a set score of 2-0?: 0.23/0.55 mid 39.0%, model 41.4% (projection_v2.0 (prediction ledger)) -- gap +2.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Daniil Sarksian vs Boxiong Zhang -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212022:214025:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniil Sarksian (`KXITFMATCH-26NOV04SARZHA-SAR`) | 0.65 / 0.69 (715) | 67.0% | 57.4% | 48.4% | 46.8% [45.2%-50.0%] | 65.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.7 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Boxiong Zhang (`KXITFMATCH-26NOV04SARZHA-ZHA`) | 0.30 / 0.32 (100) | 31.0% | 42.6% | 51.6% | 53.2% [50.0%-54.8%] | 34.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +11.7 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2188.0, B 109.0; serve-point win A 56.8%, B 44.6%; Elo A 1227.8, B 1247.1; model uncertainty 0.0237
* Form inputs: days since last match A 205, B 198; matches on record A 62, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.032, surface_pool_high -0.016, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yushan Shao vs Yihan Qu -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264086:269253:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yihan Qu (`KXITFWMATCH-26NOV04SHAQUX-QUX`) | 0.49 / 0.52 (83) | 50.5% | 10.9% | 9.6% | 20.4% [15.2%-24.3%] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -39.5 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yushan Shao (`KXITFWMATCH-26NOV04SHAQUX-SHA`) | 0.47 / 0.48 (48) | 47.5% | 89.0% | 90.5% | 79.6% [75.7%-84.8%] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +41.5 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1123.0, B 377.0; serve-point win A 58.2%, B 51.0%; Elo A 1398.2, B 1191.1; model uncertainty 0.0458
* Form inputs: days since last match A 29, B 11; matches on record A 29, B 17; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV04SHAQUX-SHA  (YES = Yushan Shao)
Model: 89%
Kalshi: 48%
Gap: +42 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.007, surface_dev_loose +0.015, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yingqun Sun vs Marianna Shikhanova -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264029:269845:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marianna Shikhanova (`KXITFWMATCH-26NOV04SUNSHI-SHI`) | 0.28 / 0.30 (127) | 29.0% | 9.3% | 47.9% | 27.0% [26.1%-27.0%] | 32.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -19.7 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yingqun Sun (`KXITFWMATCH-26NOV04SUNSHI-SUN`) | 0.69 / 0.70 (100) | 69.5% | 90.7% | 52.1% | 73.0% [73.0%-73.9%] | 67.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +21.2 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1826.0, B 49.0; serve-point win A 60.0%, B 50.0%; Elo A 1387.9, B 1210.1; model uncertainty 0.0046
* Form inputs: days since last match A 191, B 373; matches on record A 99, B 6; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV04SUNSHI-SUN  (YES = Yingqun Sun)
Model: 91%
Kalshi: 70%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ru Xi Wu vs Alina Tikhonova -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:270262:270431:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alina Tikhonova (`KXITFWMATCH-26NOV04WUXTIK-TIK`) | 0.81 / 0.83 (24) | 82.0% | 69.4% | 83.3% | 58.5% [55.3%-63.7%] | 83.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.6 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ru Xi Wu (`KXITFWMATCH-26NOV04WUXTIK-WUX`) | 0.16 / 0.17 (1) | 16.5% | 30.6% | 16.7% | 41.5% [36.3%-44.7%] | 17.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +14.1 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 171.0, B 349.0; serve-point win A 49.8%, B 46.4%; Elo A 1417.8, B 1453.2; model uncertainty 0.0417
* Form inputs: days since last match A 36, B 275; matches on record A 3, B 5; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.011, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ikumi Yamazaki vs Wenfei Yu -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221265:264184:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ikumi Yamazaki (`KXITFWMATCH-26NOV04YAMYUX-YAM`) | 0.70 / 0.73 (36) | 71.5% | 76.8% | 74.4% | 68.5% [61.6%-74.9%] | 70.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Wenfei Yu (`KXITFWMATCH-26NOV04YAMYUX-YUX`) | 0.26 / 0.29 (28) | 27.5% | 23.2% | 25.6% | 31.5% [25.1%-38.4%] | 29.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1933.0, B 238.0; serve-point win A 55.7%, B 49.8%; Elo A 1477.0, B 1351.8; model uncertainty 0.0663
* Form inputs: days since last match A 191, B 191; matches on record A 215, B 35; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.063, surface_pool_high -0.069, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anna Yang vs Thasaporn Naklo -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220597:264242:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thasaporn Naklo (`KXITFWMATCH-26NOV04YANNAK-NAK`) | 0.84 / 0.86 (100) | 85.0% | 82.5% | 57.4% | 69.3% [66.4%-72.1%] | 82.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anna Yang (`KXITFWMATCH-26NOV04YANNAK-YAN`) | 0.13 / 0.14 (30) | 13.5% | 17.5% | 42.6% | 30.7% [27.9%-33.6%] | 17.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 270.0, B 2173.0; serve-point win A 52.1%, B 40.8%; Elo A 1302.6, B 1456.9; model uncertainty 0.0285
* Form inputs: days since last match A 373, B 191; matches on record A 21, B 166; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.019, surface_dev_loose +0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xinxin Yao vs Xiaodi You -- W100 Incheon R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214646:252587:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xinxin Yao (`KXITFWMATCH-26NOV04YAOYOU-YAO`) | 0.47 / 0.50 (125) | 48.5% | 33.1% | 20.3% | 26.0% [22.6%-34.9%] | 50.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.4 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Xiaodi You (`KXITFWMATCH-26NOV04YAOYOU-YOU`) | 0.50 / 0.52 (100) | 51.0% | 66.9% | 79.7% | 74.0% [65.1%-77.4%] | 50.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +15.9 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2972.0, B 3618.0; serve-point win A 50.9%, B 45.9%; Elo A 1573.7, B 1650.7; model uncertainty 0.0612
* Form inputs: days since last match A 30, B 11; matches on record A 320, B 580; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV04YAOYOU-YOU  (YES = Xiaodi You)
Model: 67%
Kalshi: 51%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: LOW_DISPLAYED_LIQUIDITY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.004, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Justina Mikulskyte vs Tiphanie Lemaitre -- WTA 125K Luanda R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-05 13:10Z
* Current expected start: 2026-11-05 10:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: 2026-11-05 09:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-11-05T13:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26NOV05MIKLEM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tiphanie Lemaitre (`KXWTACHALLENGERMATCH-26NOV05MIKLEM-LEM`) | 0.58 / 0.59 (15) | 58.5% | -- | -- | -- [-----] | 58.4% | 58.3% | 58.3% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Justina Mikulskyte (`KXWTACHALLENGERMATCH-26NOV05MIKLEM-MIK`) | 0.41 / 0.42 (1211) | 41.5% | -- | -- | -- [-----] | 41.6% | 41.0% | 41.3% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Tereza Valentova vs Alexandra Eala -- WTA Hong Kong R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-05 09:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-05 10:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: 2026-11-05 09:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-11-05T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:223253:238184:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandra Eala (`KXWTAMATCH-26NOV05VALEAL-EAL`) | 0.63 / 0.64 (21070) | 63.5% | 60.8% | 40.0% | 45.8% [42.6%-53.7%] | 62.3% | 62.5% | 62.4% | MODEL_LONE_OUTLIER | PASS | -2.7 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Tereza Valentova (`KXWTAMATCH-26NOV05VALEAL-VAL`) | 0.37 / 0.38 (55477) | 37.5% | 39.2% | 60.0% | 54.2% [46.3%-57.4%] | 37.7% | 37.5% | 37.6% | MODEL_LONE_OUTLIER | SHADOW_BET | +1.7 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3231.0, B 4541.0; serve-point win A 54.0%, B 43.9%; Elo A 1896.8, B 1958.3; model uncertainty 0.0555
* Form inputs: days since last match A 1, B 1; matches on record A 172, B 371; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.011, surface_dev_loose -0.005, surface_dev_tight +0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV05VALEAL-23` Over 22.5 games: 0.42/0.43 mid 42.5%, model 54.8% (projection_v2.0 (prediction ledger)) -- gap +12.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV05VALEAL-28` Over 27.5 games: 0.23/0.25 mid 24.0%, model 33.1% (projection_v2.0 (prediction ledger)) -- gap +9.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV05VALEAL-18` Over 17.5 games: 0.76/0.81 mid 78.5%, model 86.8% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV05VALEAL-2-EAL` Will Alexandra Eala win set 2 in the Tereza Valentova vs Alexandra Eala match: 0.63/0.64 mid 63.5%, model 57.2% (projection_v2.0 (prediction ledger)) -- gap -6.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV05VALEAL-2-VAL` Will Tereza Valentova win set 2 in the Tereza Valentova vs Alexandra Eala match: 0.36/0.40 mid 38.0%, model 42.8% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV05VALEAL-1-VAL` Will Tereza Valentova win set 1 in the Tereza Valentova vs Alexandra Eala match: 0.38/0.41 mid 39.5%, model 42.8% (projection_v2.0 (prediction ledger)) -- gap +3.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV05VALEAL-1-EAL` Will Alexandra Eala win set 1 in the Tereza Valentova vs Alexandra Eala match: 0.59/0.61 mid 60.0%, model 57.2% (projection_v2.0 (prediction ledger)) -- gap -2.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE

## Jia-Jing Lu vs Yeonwoo Ku -- W100 Incheon R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 10:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV04LUXKUX:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yeonwoo Ku (`KXITFWMATCH-26NOV04LUXKUX-KUX`) | 0.70 / 0.74 (603) | 72.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jia-Jing Lu (`KXITFWMATCH-26NOV04LUXKUX-LUX`) | 0.26 / 0.28 (33) | 27.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## JiaYi Wang vs BoYoung Jeong -- W100 Incheon R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 10:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221109:265692:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BoYoung Jeong (`KXITFWMATCH-26NOV04WANJEO-JEO`) | 0.36 / 0.40 (403) | 38.0% | 57.7% | 55.3% | 56.4% [54.8%-58.0%] | 39.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +19.7 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| JiaYi Wang (`KXITFWMATCH-26NOV04WANJEO-WAN`) | 0.60 / 0.63 (6) | 61.5% | 42.3% | 44.7% | 43.6% [42.0%-45.2%] | 60.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -19.2 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2216.0, B 2517.0; serve-point win A 52.3%, B 46.2%; Elo A 1510.1, B 1565.2; model uncertainty 0.0159
* Form inputs: days since last match A 36, B 46; matches on record A 72, B 221; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV04WANJEO-JEO  (YES = BoYoung Jeong)
Model: 58%
Kalshi: 38%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.016, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carl Emil Overbeck vs Kasidit Samrej -- ATP Challenger Taipei R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 10:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-05T10:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208937:209274:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carl Emil Overbeck (`KXATPCHALLENGERMATCH-26NOV05OVESAM-OVE`) | 0.53 / 0.54 (2250) | 53.5% | 45.2% | 62.1% | 52.4% [48.0%-56.3%] | 54.1% | 54.9% | 54.5% | MODEL_LONE_OUTLIER | PASS | -8.2 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Kasidit Samrej (`KXATPCHALLENGERMATCH-26NOV05OVESAM-SAM`) | 0.45 / 0.47 (2285) | 46.0% | 54.8% | 37.9% | 47.5% [43.7%-52.0%] | 45.9% | 45.7% | 45.9% | MARKETS_AGREE | WATCH | +8.8 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2090.0, B 4012.0; serve-point win A 65.0%, B 34.0%; Elo A 1498.7, B 1573.8; model uncertainty 0.0415
* Form inputs: days since last match A 37, B 9; matches on record A 83, B 295; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.015, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Simona Waltert vs Lucrezia Stefanini -- WTA Chennai R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-05 12:30Z
* Current expected start: 2026-11-05 11:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: 2026-11-05 10:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-90_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-11-05T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214593:215899:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucrezia Stefanini (`KXWTAMATCH-26NOV05WALSTE-STE`) | 0.64 / 0.65 (106) | 64.5% | 50.0% | 34.4% | 38.4% [36.4%-46.3%] | 64.6% | 65.6% | 65.6% | MODEL_LONE_OUTLIER | PASS | -14.5 pp | REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Simona Waltert (`KXWTAMATCH-26NOV05WALSTE-WAL`) | 0.34 / 0.35 (97) | 34.5% | 50.0% | 65.6% | 61.6% [53.7%-63.6%] | 35.4% | 34.4% | 34.4% | MODEL_LONE_OUTLIER | WATCH | +15.5 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4747.0, B 4432.0; serve-point win A 52.5%, B 47.5%; Elo A 1725.4, B 1750.2; model uncertainty 0.0495
* Form inputs: days since last match A 1, B 1; matches on record A 522, B 616; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26NOV05WALSTE-WAL  (YES = Simona Waltert)
Model: 50%
Kalshi: 34%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: EXTERNAL_STALE
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV05WALSTE-16` Over 15.5 games: 0.24/0.93 mid 58.5%, model 96.6% (projection_v2.0 (prediction ledger)) -- gap +38.1 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV05WALSTE-21` Over 20.5 games: 0.48/0.50 mid 49.0%, model 66.6% (projection_v2.0 (prediction ledger)) -- gap +17.6 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV05WALSTE-26` Over 25.5 games: 0.28/0.29 mid 28.5%, model 43.4% (projection_v2.0 (prediction ledger)) -- gap +14.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV05WALSTE-2-WAL` Will Simona Waltert win set 2 in the Simona Waltert vs Lucrezia Stefanini match: 0.35/0.39 mid 37.0%, model 50.0% (projection_v2.0 (prediction ledger)) -- gap +13.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV05WALSTE-2-STE` Will Lucrezia Stefanini win set 2 in the Simona Waltert vs Lucrezia Stefanini match: 0.61/0.64 mid 62.5%, model 50.0% (projection_v2.0 (prediction ledger)) -- gap -12.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV05WALSTE-1-WAL` Will Simona Waltert win set 1 in the Simona Waltert vs Lucrezia Stefanini match: 0.37/0.39 mid 38.0%, model 50.0% (projection_v2.0 (prediction ledger)) -- gap +12.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV05WALSTE-1-STE` Will Lucrezia Stefanini win set 1 in the Simona Waltert vs Lucrezia Stefanini match: 0.60/0.62 mid 61.0%, model 50.0% (projection_v2.0 (prediction ledger)) -- gap -11.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Adrian Arcon vs Amir Omarkhanov -- M15 Fergana R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210417:212788:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Arcon (`KXITFMATCH-26NOV05ARCOMA-ARC`) | 0.04 / 0.06 (595) | 5.0% | 4.9% | 10.5% | 9.0% [7.3%-10.9%] | -- | -- | -- | -- | PASS | -0.1 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amir Omarkhanov (`KXITFMATCH-26NOV05ARCOMA-OMA`) | 0.91 / 0.95 (427) | 93.0% | 95.1% | 89.5% | 91.0% [89.1%-92.7%] | -- | -- | -- | -- | PASS | +2.1 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 522.0, B 2497.0; serve-point win A 54.8%, B 32.2%; Elo A 997.6, B 1405.3; model uncertainty 0.0181
* Form inputs: days since last match A 184, B 18; matches on record A 22, B 76; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dmitry Bessonov vs Makar Krivoshchekov -- M15 Fergana R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213185:213614:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dmitry Bessonov (`KXITFMATCH-26NOV05BESKRI-BES`) | 0.77 / 0.80 (139) | 78.5% | 49.0% | 29.3% | 46.9% [42.8%-51.0%] | 78.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -29.5 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Makar Krivoshchekov (`KXITFMATCH-26NOV05BESKRI-KRI`) | 0.18 / 0.21 (32) | 19.5% | 51.0% | 70.7% | 53.1% [49.0%-57.2%] | 21.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +31.5 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 961.0, B 400.0; serve-point win A 59.3%, B 40.5%; Elo A 1137.5, B 1125.3; model uncertainty 0.0413
* Form inputs: days since last match A 205, B 219; matches on record A 25, B 14; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV05BESKRI-KRI  (YES = Makar Krivoshchekov)
Model: 51%
Kalshi: 20%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aryan Lakshmanan vs David Eichenseher -- M15 Fergana R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212631:212767:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| David Eichenseher (`KXITFMATCH-26NOV05LAKEIC-EIC`) | 0.74 / 0.78 (176) | 76.0% | 53.8% | 49.0% | 54.5% [53.5%-56.1%] | 75.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -22.2 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aryan Lakshmanan (`KXITFMATCH-26NOV05LAKEIC-LAK`) | 0.23 / 0.24 (163) | 23.5% | 46.2% | 51.0% | 45.5% [43.9%-46.5%] | 24.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +22.7 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 548.0, B 1106.0; serve-point win A 62.0%, B 37.2%; Elo A 1145.6, B 1191.7; model uncertainty 0.0129
* Form inputs: days since last match A 226, B 191; matches on record A 18, B 30; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV05LAKEIC-LAK  (YES = Aryan Lakshmanan)
Model: 46%
Kalshi: 24%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Digvijay Pratap Singh vs Jan Hrazdil -- M15 Fergana R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05SINHRA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jan Hrazdil (`KXITFMATCH-26NOV05SINHRA-HRA`) | 0.15 / 0.19 (238) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Digvijay Pratap Singh (`KXITFMATCH-26NOV05SINHRA-SIN`) | 0.81 / 0.83 (169) | 82.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arakawa / Katsumi vs Kosaka / Uchijima -- W35 Hamamatsu QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05ARAKATKOSUCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arakawa / Katsumi (`KXITFWDOUBLES-26NOV05ARAKATKOSUCH-ARAKAT`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kosaka / Uchijima (`KXITFWDOUBLES-26NOV05ARAKATKOSUCH-KOSUCH`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Arakawa / Suzuki vs Miyamoto / Nagata -- W35 Hamamatsu QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05ARASUZMIYNAG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arakawa / Suzuki (`KXITFWDOUBLES-26NOV05ARASUZMIYNAG-ARASUZ`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Miyamoto / Nagata (`KXITFWDOUBLES-26NOV05ARASUZMIYNAG-MIYNAG`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Li / Park vs Madelyn Nugroho / Sidorova -- W100 Incheon QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05LIXPARMADSID:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Li / Park (`KXITFWDOUBLES-26NOV05LIXPARMADSID-LIXPAR`) | 0.35 / 0.55 (55) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Madelyn Nugroho / Sidorova (`KXITFWDOUBLES-26NOV05LIXPARMADSID-MADSID`) | 0.38 / 0.60 (56) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Harri Heliovaara / Henry Patten vs Sadio Doumbia / David Pel -- ATP Paris R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-05 13:00Z
* Current expected start: 2026-11-05 11:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: 2026-11-05 10:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-05T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05HELPATDOUPEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sadio Doumbia / David Pel (`KXATPDOUBLES-26NOV05HELPATDOUPEL-DOUPEL`) | 0.19 / 0.23 (2730) | 21.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Harri Heliovaara / Henry Patten (`KXATPDOUBLES-26NOV05HELPATDOUPEL-HELPAT`) | 0.77 / 0.81 (333) | 79.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Adam Pavlasek / Patrik Rikl vs Theo Arribage / Albano Olivetti -- ATP Paris R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-05 12:00Z
* Current expected start: 2026-11-05 11:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: 2026-11-05 10:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-05T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05PAVRIKARROLI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theo Arribage / Albano Olivetti (`KXATPDOUBLES-26NOV05PAVRIKARROLI-ARROLI`) | 0.54 / 0.56 (46) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Adam Pavlasek / Patrik Rikl (`KXATPDOUBLES-26NOV05PAVRIKARROLI-PAVRIK`) | 0.41 / 0.45 (277) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Ben Shelton vs Arthur Rinderknech -- ATP Paris R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-05 12:00Z
* Current expected start: 2026-11-05 11:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: 2026-11-05 10:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-30_MIN

ATP (MASTERS_1000) · Hard · scheduled 2026-11-05T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126239:210097:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arthur Rinderknech (`KXATPMATCH-26NOV05SHERIN-RIN`) | 0.27 / 0.28 (10389) | 27.5% | 28.2% | 32.7% | 29.8% [28.3%-31.1%] | 26.7% | 27.4% | 27.0% | MODEL_LONE_OUTLIER | WATCH | +0.7 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Ben Shelton (`KXATPMATCH-26NOV05SHERIN-SHE`) | 0.73 / 0.74 (88691) | 73.5% | 71.8% | 67.3% | 70.2% [68.9%-71.7%] | 73.4% | 72.8% | 73.1% | MODEL_LONE_OUTLIER | PASS | -1.7 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 6486.0, B 5481.0; serve-point win A 73.7%, B 31.3%; Elo A 2070.8, B 1833.1; model uncertainty 0.014
* Form inputs: days since last match A 1, B 0; matches on record A 318, B 571; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose +0.003, surface_dev_tight -0.008
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26NOV05SHERIN-RIN21` Will Arthur Rinderknech win the Ben Shelton vs Arthur Rinderknech match by a set score of 2-1?: 0.08/0.89 mid 48.5%, model 16.0% (projection_v2.0 (prediction ledger)) -- gap -32.5 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV05SHERIN-RIN2` Will Arthur Rinderknech win at least 1.5 more games than Ben Shelton?: 0.02/0.91 mid 46.5%, model 20.5% (projection_v2.0 (prediction ledger)) -- gap -25.9 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV05SHERIN-20` Over 19.5 games: 0.49/0.93 mid 71.0%, model 89.2% (projection_v2.0 (prediction ledger)) -- gap +18.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05SHERIN-SHE21` Will Ben Shelton win the Ben Shelton vs Arthur Rinderknech match by a set score of 2-1?: 0.01/0.28 mid 14.5%, model 29.6% (projection_v2.0 (prediction ledger)) -- gap +15.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05SHERIN-RIN20` Will Arthur Rinderknech win the Ben Shelton vs Arthur Rinderknech match by a set score of 2-0?: 0.02/0.52 mid 27.0%, model 12.3% (projection_v2.0 (prediction ledger)) -- gap -14.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV05SHERIN-30` Over 29.5 games: 0.29/0.32 mid 30.5%, model 38.8% (projection_v2.0 (prediction ledger)) -- gap +8.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV05SHERIN-25` Over 24.5 games: 0.48/0.50 mid 49.0%, model 57.1% (projection_v2.0 (prediction ledger)) -- gap +8.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV05SHERIN-SHE4` Will Ben Shelton win at least 3.5 more games than Arthur Rinderknech?: 0.38/0.40 mid 39.0%, model 32.7% (projection_v2.0 (prediction ledger)) -- gap -6.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV05SHERIN-1-RIN` Will Arthur Rinderknech win set 1 in the Ben Shelton vs Arthur Rinderknech match: 0.30/0.34 mid 32.0%, model 35.0% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV05SHERIN-1-SHE` Will Ben Shelton win set 1 in the Ben Shelton vs Arthur Rinderknech match: 0.67/0.69 mid 68.0%, model 65.0% (projection_v2.0 (prediction ledger)) -- gap -3.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV05SHERIN-2-RIN` Will Arthur Rinderknech win set 2 in the Ben Shelton vs Arthur Rinderknech match: 0.30/0.34 mid 32.0%, model 35.0% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV05SHERIN-2-SHE` Will Ben Shelton win set 2 in the Ben Shelton vs Arthur Rinderknech match: 0.66/0.70 mid 68.0%, model 65.0% (projection_v2.0 (prediction ledger)) -- gap -3.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05SHERIN-SHE20` Will Ben Shelton win the Ben Shelton vs Arthur Rinderknech match by a set score of 2-0?: 0.23/0.56 mid 39.5%, model 42.2% (projection_v2.0 (prediction ledger)) -- gap +2.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Xirui Han vs Qian Sun -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208229:212472:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xirui Han (`KXITFMATCH-26NOV05HANSUN-HAN`) | 0.25 / 0.28 (27) | 26.5% | 35.8% | 39.7% | 43.8% [40.6%-45.9%] | 27.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +9.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Qian Sun (`KXITFMATCH-26NOV05HANSUN-SUN`) | 0.70 / 0.75 (134) | 72.5% | 64.2% | 60.3% | 56.2% [54.1%-59.4%] | 72.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 542.0, B 1071.0; serve-point win A 56.6%, B 40.6%; Elo A 1153.8, B 1192.1; model uncertainty 0.0262
* Form inputs: days since last match A 380, B 16; matches on record A 15, B 76; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Seongchan Hong vs Pawit Sornlaksup -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05HONSOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Seongchan Hong (`KXITFMATCH-26NOV05HONSOR-HON`) | 0.77 / 0.78 (10) | 77.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pawit Sornlaksup (`KXITFMATCH-26NOV05HONSOR-SOR`) | 0.19 / 0.23 (103) | 21.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Millen Hurrion vs Lingxi Zhao -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206789:209140:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Millen Hurrion (`KXITFMATCH-26NOV05HURZHA-HUR`) | 0.69 / 0.74 (208) | 71.5% | 72.3% | 70.5% | 71.8% [69.1%-75.1%] | 72.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lingxi Zhao (`KXITFMATCH-26NOV05HURZHA-ZHA`) | 0.26 / 0.29 (100) | 27.5% | 27.7% | 29.5% | 28.2% [24.9%-30.9%] | 27.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.2 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2993.0, B 337.0; serve-point win A 60.3%, B 44.2%; Elo A 1434.9, B 1269.4; model uncertainty 0.03
* Form inputs: days since last match A 93, B 380; matches on record A 179, B 39; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.026, surface_pool_high -0.027, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rigele Te vs Zhao Zhao -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144751:206888:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rigele Te (`KXITFMATCH-26NOV05TEXZHA-TEX`) | 0.80 / 0.85 (100) | 82.5% | 83.8% | 40.1% | 76.7% [73.8%-79.1%] | 83.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zhao Zhao (`KXITFMATCH-26NOV05TEXZHA-ZHA`) | 0.15 / 0.17 (13) | 16.0% | 16.2% | 59.9% | 23.3% [20.9%-26.2%] | 17.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.2 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1492.0, B 155.0; serve-point win A 67.1%, B 40.7%; Elo A 1414.4, B 1177.3; model uncertainty 0.0266
* Form inputs: days since last match A 9, B 212; matches on record A 319, B 25; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.008, surface_dev_loose -0.001, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xin Zhou vs Tianhui Zhang -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05ZHOZHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tianhui Zhang (`KXITFMATCH-26NOV05ZHOZHA-ZHA`) | 0.81 / 0.84 (128) | 82.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xin Zhou (`KXITFMATCH-26NOV05ZHOZHA-ZHO`) | 0.13 / 0.17 (173) | 15.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maria Pankratova vs Jiayu Xu -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05PANXUX:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Pankratova (`KXITFWMATCH-26NOV05PANXUX-PAN`) | 0.67 / 0.71 (33) | 69.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jiayu Xu (`KXITFWMATCH-26NOV05PANXUX-XUX`) | 0.26 / 0.31 (29) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sorana Cirstea vs Mary Stoiana -- WTA Hong Kong R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-05 09:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-05 12:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: 2026-11-05 11:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-11-05T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:201514:223168:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sorana Cirstea (`KXWTAMATCH-26NOV05CIRSTO-CIR`) | 0.77 / 0.78 (8861) | 77.5% | 68.7% | 84.2% | 80.9% [77.2%-82.3%] | 75.5% | 77.6% | 77.6% | MARKETS_AGREE | WATCH | -8.8 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Mary Stoiana (`KXWTAMATCH-26NOV05CIRSTO-STO`) | 0.22 / 0.23 (1328) | 22.5% | 31.3% | 15.8% | 19.1% [17.7%-22.8%] | 24.5% | 22.5% | 22.5% | MARKETS_AGREE | PASS | +8.8 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4410.0, B 2840.0; serve-point win A 60.6%, B 43.2%; Elo A 2008.5, B 1825.3; model uncertainty 0.0251
* Form inputs: days since last match A 1, B 2; matches on record A 1065, B 146; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.004, surface_dev_loose +0.006, surface_dev_tight -0.007
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV05CIRSTO-15` Over 14.5 games: 0.48/0.95 mid 71.5%, model 99.1% (projection_v2.0 (prediction ledger)) -- gap +27.6 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV05CIRSTO-20` Over 19.5 games: 0.52/0.53 mid 52.5%, model 72.8% (projection_v2.0 (prediction ledger)) -- gap +20.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV05CIRSTO-25` Over 24.5 games: 0.28/0.31 mid 29.5%, model 47.0% (projection_v2.0 (prediction ledger)) -- gap +17.5 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV05CIRSTO-2-CIR` Will Sorana Cirstea win set 2 in the Sorana Cirstea vs Mary Stoiana match: 0.71/0.75 mid 73.0%, model 62.7% (projection_v2.0 (prediction ledger)) -- gap -10.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV05CIRSTO-2-STO` Will Mary Stoiana win set 2 in the Sorana Cirstea vs Mary Stoiana match: 0.25/0.29 mid 27.0%, model 37.3% (projection_v2.0 (prediction ledger)) -- gap +10.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV05CIRSTO-1-CIR` Will Sorana Cirstea win set 1 in the Sorana Cirstea vs Mary Stoiana match: 0.71/0.74 mid 72.5%, model 62.7% (projection_v2.0 (prediction ledger)) -- gap -9.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV05CIRSTO-1-STO` Will Mary Stoiana win set 1 in the Sorana Cirstea vs Mary Stoiana match: 0.26/0.30 mid 28.0%, model 37.3% (projection_v2.0 (prediction ledger)) -- gap +9.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Chirag Duhan vs Muzammil Murtaza -- M15 Fergana R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207836:210003:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chirag Duhan (`KXITFMATCH-26NOV05DUHMUR-DUH`) | 0.73 / 0.77 (396) | 75.0% | 70.7% | 49.0% | 66.4% [65.0%-67.8%] | 72.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Muzammil Murtaza (`KXITFMATCH-26NOV05DUHMUR-MUR`) | 0.22 / 0.24 (5) | 23.0% | 29.3% | 51.0% | 33.6% [32.1%-35.0%] | 27.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1525.0, B 170.0; serve-point win A 63.2%, B 41.0%; Elo A 1258.0, B 1123.8; model uncertainty 0.0144
* Form inputs: days since last match A 226, B 47; matches on record A 96, B 35; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Calvin Mueller vs Edoardo Cherie Ligniere -- M15 Fergana R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209166:212122:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Edoardo Cherie Ligniere (`KXITFMATCH-26NOV05MUECHE-CHE`) | 0.27 / 0.32 (5) | 29.5% | 33.7% | 38.8% | 34.4% [33.4%-35.4%] | 31.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.2 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Calvin Mueller (`KXITFMATCH-26NOV05MUECHE-MUE`) | 0.67 / 0.68 (78) | 67.5% | 66.3% | 61.2% | 65.6% [64.6%-66.6%] | 68.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.2 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1075.0, B 266.0; serve-point win A 61.8%, B 41.4%; Elo A 1312.1, B 1192.7; model uncertainty 0.0098
* Form inputs: days since last match A 191, B 191; matches on record A 24, B 17; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aristarkh Safonov vs Nikita Ianin -- M15 Fergana R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210011:210394:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikita Ianin (`KXITFMATCH-26NOV05SAFIAN-IAN`) | 0.38 / 0.41 (148) | 39.5% | 44.8% | 57.5% | 43.5% [40.9%-48.5%] | -- | -- | -- | -- | PASS | +5.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aristarkh Safonov (`KXITFMATCH-26NOV05SAFIAN-SAF`) | 0.58 / 0.59 (60) | 58.5% | 55.2% | 42.5% | 56.5% [51.5%-59.1%] | -- | -- | -- | -- | PASS | -3.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 401.0, B 2048.0; serve-point win A 62.8%, B 38.2%; Elo A 1274.7, B 1204.4; model uncertainty 0.0381
* Form inputs: days since last match A 191, B 191; matches on record A 44, B 74; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Guo / Shi vs Back / Ren -- W100 Incheon QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05GUOSHIBACREN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Back / Ren (`KXITFWDOUBLES-26NOV05GUOSHIBACREN-BACREN`) | 0.36 / 0.56 (47) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Guo / Shi (`KXITFWDOUBLES-26NOV05GUOSHIBACREN-GUOSHI`) | 0.39 / 0.58 (24) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Kawaguchi / Sato vs Ito / Saito -- W100 Incheon QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05KAWSATITOSAI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ito / Saito (`KXITFWDOUBLES-26NOV05KAWSATITOSAI-ITOSAI`) | 0.23 / 0.65 (71) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kawaguchi / Sato (`KXITFWDOUBLES-26NOV05KAWSATITOSAI-KAWSAT`) | 0.28 / 0.51 (51) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Ovcharenko / Savinykh vs Feng / Huang -- W100 Incheon QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05OVCSAVFENHUA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Feng / Huang (`KXITFWDOUBLES-26NOV05OVCSAVFENHUA-FENHUA`) | 0.57 / 0.78 (113) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ovcharenko / Savinykh (`KXITFWDOUBLES-26NOV05OVCSAVFENHUA-OVCSAV`) | 0.17 / 0.37 (39) | 27.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Ozeki / Sato vs Sawashiro / Yodpetch -- W35 Hamamatsu QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05OZESATSAWYOD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ozeki / Sato (`KXITFWDOUBLES-26NOV05OZESATSAWYOD-OZESAT`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sawashiro / Yodpetch (`KXITFWDOUBLES-26NOV05OZESATSAWYOD-SAWYOD`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Shimizu / Yoshioka vs Kawamura / Kozaki -- W35 Hamamatsu QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05SHIYOSKAWKOZ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kawamura / Kozaki (`KXITFWDOUBLES-26NOV05SHIYOSKAWKOZ-KAWKOZ`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Shimizu / Yoshioka (`KXITFWDOUBLES-26NOV05SHIYOSKAWKOZ-SHIYOS`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Anastasia Zakharova vs Vaishnavi Adkar -- WTA Chennai R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-04 12:30Z
* Current expected start: 2026-11-05 12:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: 2026-11-05 11:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1440_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-11-04T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:220435:261038:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vaishnavi Adkar (`KXWTAMATCH-26NOV04ZAKADK-ADK`) | 0.12 / 0.13 (14037) | 12.5% | 20.1% | 34.0% | 27.0% [20.5%-30.1%] | -- | -- | -- | -- | SHADOW_BET | +7.6 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anastasia Zakharova (`KXWTAMATCH-26NOV04ZAKADK-ZAK`) | 0.88 / 0.89 (3437) | 88.5% | 79.9% | 66.0% | 73.0% [69.8%-79.5%] | -- | -- | -- | -- | PASS | -8.6 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4628.0, B 2186.0; serve-point win A 57.8%, B 48.5%; Elo A 1807.2, B 1540.6; model uncertainty 0.0484
* Form inputs: days since last match A 1, B 191; matches on record A 485, B 143; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.018, surface_dev_loose -0.004, surface_dev_tight +0.000
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 6 carry a model probability
  * `KXWTAGTOTAL-26NOV04ZAKADK-19` Over 18.5 games: 0.47/0.49 mid 48.0%, model 71.7% (projection_v2.0 (prediction ledger)) -- gap +23.7 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26NOV04ZAKADK-24` Over 23.5 games: 0.21/0.24 mid 22.5%, model 41.9% (projection_v2.0 (prediction ledger)) -- gap +19.4 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26NOV04ZAKADK-1-ADK` Will Vaishnavi Adkar win set 1 in the Anastasia Zakharova vs Vaishnavi Adkar match: 0.16/0.19 mid 17.5%, model 28.8% (projection_v2.0 (prediction ledger)) -- gap +11.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV04ZAKADK-1-ZAK` Will Anastasia Zakharova win set 1 in the Anastasia Zakharova vs Vaishnavi Adkar match: 0.81/0.84 mid 82.5%, model 71.2% (projection_v2.0 (prediction ledger)) -- gap -11.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV04ZAKADK-2-ZAK` Will Anastasia Zakharova win set 2 in the Anastasia Zakharova vs Vaishnavi Adkar match: 0.37/0.91 mid 64.0%, model 71.2% (projection_v2.0 (prediction ledger)) -- gap +7.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV04ZAKADK-2-ADK` Will Vaishnavi Adkar win set 2 in the Anastasia Zakharova vs Vaishnavi Adkar match: 0.08/0.44 mid 26.0%, model 28.8% (projection_v2.0 (prediction ledger)) -- gap +2.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jay Clarke vs Gianluca Cadenasso -- ATP Challenger Taranto R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-05T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05CLACAD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gianluca Cadenasso (`KXATPCHALLENGERMATCH-26NOV05CLACAD-CAD`) | 0.50 / 0.51 (1025) | 50.5% | -- | -- | -- [-----] | 51.0% | 51.2% | 51.1% | MARKETS_AGREE | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jay Clarke (`KXATPCHALLENGERMATCH-26NOV05CLACAD-CLA`) | 0.49 / 0.50 (2026) | 49.5% | -- | -- | -- [-----] | 49.0% | 49.7% | 49.3% | MARKETS_AGREE | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Felix Gill vs Buvaysar Gadamauri -- ATP Challenger Taranto R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-05T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05GILGAD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Buvaysar Gadamauri (`KXATPCHALLENGERMATCH-26NOV05GILGAD-GAD`) | 0.44 / 0.46 (2356) | 45.0% | -- | -- | -- [-----] | 44.6% | 45.3% | 45.3% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Felix Gill (`KXATPCHALLENGERMATCH-26NOV05GILGAD-GIL`) | 0.54 / 0.56 (1025) | 55.0% | -- | -- | -- [-----] | 55.4% | 55.8% | 55.8% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Jodie Burrage / Robin Montgomery vs Vaishnavi Adkar / Rutuja Bhosale -- WTA Chennai QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-06T05:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-05T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05BURMONADKBHO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vaishnavi Adkar / Rutuja Bhosale (`KXWTADOUBLES-26NOV05BURMONADKBHO-ADKBHO`) | 0.03 / 0.93 (10) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jodie Burrage / Robin Montgomery (`KXWTADOUBLES-26NOV05BURMONADKBHO-BURMON`) | 0.03 / 0.93 (10) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Rinky Hijikata vs Tomas Martin Etcheverry -- ATP Paris R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-05 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-05 13:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: 2026-11-05 12:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · Hard · scheduled 2026-11-05T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144869:208014:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tomas Martin Etcheverry (`KXATPMATCH-26NOV05HIJETC-ETC`) | 0.53 / 0.55 (1189) | 54.0% | 53.3% | 66.7% | 62.1% [57.9%-64.9%] | 54.3% | 55.3% | 54.3% | MODEL_LONE_OUTLIER | WATCH | -0.7 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Rinky Hijikata (`KXATPMATCH-26NOV05HIJETC-HIJ`) | 0.46 / 0.47 (1741) | 46.5% | 46.7% | 33.3% | 37.9% [35.1%-42.1%] | 45.7% | 44.8% | 45.7% | MODEL_LONE_OUTLIER | PASS | +0.2 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5968.0, B 5577.0; serve-point win A 64.5%, B 34.8%; Elo A 1822.5, B 1775.7; model uncertainty 0.0352
* Form inputs: days since last match A 2, B 1; matches on record A 469, B 650; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.004, surface_dev_tight -0.001
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26NOV05HIJETC-ETC5` Will Tomas Martin Etcheverry win at least 4.5 more games than Rinky Hijikata?: 0.20/0.56 mid 38.0%, model 16.9% (projection_v2.0 (prediction ledger)) -- gap -21.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05HIJETC-ETC21` Will Tomas Martin Etcheverry win the Rinky Hijikata vs Tomas Martin Etcheverry match by a set score of 2-1?: 0.01/0.30 mid 15.5%, model 26.1% (projection_v2.0 (prediction ledger)) -- gap +10.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05HIJETC-HIJ21` Will Rinky Hijikata win the Rinky Hijikata vs Tomas Martin Etcheverry match by a set score of 2-1?: 0.01/0.27 mid 14.0%, model 23.8% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05HIJETC-ETC20` Will Tomas Martin Etcheverry win the Rinky Hijikata vs Tomas Martin Etcheverry match by a set score of 2-0?: 0.01/0.36 mid 18.5%, model 27.3% (projection_v2.0 (prediction ledger)) -- gap +8.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV05HIJETC-19` Over 18.5 games: 0.77/0.86 mid 81.5%, model 89.8% (projection_v2.0 (prediction ledger)) -- gap +8.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV05HIJETC-24` Over 23.5 games: 0.47/0.48 mid 47.5%, model 55.5% (projection_v2.0 (prediction ledger)) -- gap +8.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05HIJETC-HIJ20` Will Rinky Hijikata win the Rinky Hijikata vs Tomas Martin Etcheverry match by a set score of 2-0?: 0.01/0.31 mid 16.0%, model 22.9% (projection_v2.0 (prediction ledger)) -- gap +6.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV05HIJETC-29` Over 28.5 games: 0.32/0.36 mid 34.0%, model 37.6% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV05HIJETC-ETC2` Will Tomas Martin Etcheverry win at least 1.5 more games than Rinky Hijikata?: 0.46/0.49 mid 47.5%, model 45.5% (projection_v2.0 (prediction ledger)) -- gap -2.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV05HIJETC-HIJ2` Will Rinky Hijikata win at least 1.5 more games than Tomas Martin Etcheverry?: 0.38/0.41 mid 39.5%, model 39.0% (projection_v2.0 (prediction ledger)) -- gap -0.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV05HIJETC-1-ETC` Will Tomas Martin Etcheverry win set 1 in the Rinky Hijikata vs Tomas Martin Etcheverry match: 0.49/0.56 mid 52.5%, model 52.2% (projection_v2.0 (prediction ledger)) -- gap -0.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV05HIJETC-1-HIJ` Will Rinky Hijikata win set 1 in the Rinky Hijikata vs Tomas Martin Etcheverry match: 0.44/0.51 mid 47.5%, model 47.8% (projection_v2.0 (prediction ledger)) -- gap +0.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV05HIJETC-2-ETC` Will Tomas Martin Etcheverry win set 2 in the Rinky Hijikata vs Tomas Martin Etcheverry match: 0.49/0.56 mid 52.5%, model 52.2% (projection_v2.0 (prediction ledger)) -- gap -0.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV05HIJETC-2-HIJ` Will Rinky Hijikata win set 2 in the Rinky Hijikata vs Tomas Martin Etcheverry match: 0.44/0.51 mid 47.5%, model 47.8% (projection_v2.0 (prediction ledger)) -- gap +0.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lorenzo Musetti vs Luca Van Assche -- ATP Paris R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-05 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-05 13:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: 2026-11-05 12:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · Hard · scheduled 2026-11-05T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207518:209414:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Musetti (`KXATPMATCH-26NOV05MUSVAN-MUS`) | 0.72 / 0.73 (62466) | 72.5% | 68.0% | 71.7% | 71.2% [69.5%-73.8%] | 70.6% | 72.2% | 71.4% | MODEL_LONE_OUTLIER | PASS | -4.5 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Luca Van Assche (`KXATPMATCH-26NOV05MUSVAN-VAN`) | 0.27 / 0.29 (45714) | 28.0% | 31.9% | 28.3% | 28.7% [26.2%-30.5%] | 29.4% | 28.7% | 29.0% | MODEL_LONE_OUTLIER | PASS | +4.0 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5227.0, B 6055.0; serve-point win A 63.6%, B 40.1%; Elo A 1959.7, B 1807.2; model uncertainty 0.0215
* Form inputs: days since last match A 2, B 2; matches on record A 491, B 395; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.018, surface_dev_loose +0.004, surface_dev_tight +0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26NOV05MUSVAN-VAN20` Will Luca Van Assche win the Lorenzo Musetti vs Luca Van Assche match by a set score of 2-0?: 0.12/0.93 mid 52.5%, model 14.2% (projection_v2.0 (prediction ledger)) -- gap -38.3 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05MUSVAN-VAN21` Will Luca Van Assche win the Lorenzo Musetti vs Luca Van Assche match by a set score of 2-1?: 0.09/0.91 mid 50.0%, model 17.7% (projection_v2.0 (prediction ledger)) -- gap -32.3 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV05MUSVAN-VAN2` Will Luca Van Assche win at least 1.5 more games than Lorenzo Musetti?: 0.03/0.93 mid 48.0%, model 25.7% (projection_v2.0 (prediction ledger)) -- gap -22.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV05MUSVAN-MUS7` Will Lorenzo Musetti win at least 6.5 more games than Luca Van Assche?: 0.03/0.57 mid 30.0%, model 10.2% (projection_v2.0 (prediction ledger)) -- gap -19.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05MUSVAN-MUS21` Will Lorenzo Musetti win the Lorenzo Musetti vs Luca Van Assche match by a set score of 2-1?: 0.01/0.30 mid 15.5%, model 29.3% (projection_v2.0 (prediction ledger)) -- gap +13.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05MUSVAN-MUS20` Will Lorenzo Musetti win the Lorenzo Musetti vs Luca Van Assche match by a set score of 2-0?: 0.01/0.54 mid 27.5%, model 38.8% (projection_v2.0 (prediction ledger)) -- gap +11.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV05MUSVAN-23` Over 22.5 games: 0.48/0.49 mid 48.5%, model 56.2% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV05MUSVAN-28` Over 27.5 games: 0.27/0.30 mid 28.5%, model 36.2% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV05MUSVAN-MUS4` Will Lorenzo Musetti win at least 3.5 more games than Luca Van Assche?: 0.49/0.51 mid 50.0%, model 44.0% (projection_v2.0 (prediction ledger)) -- gap -6.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV05MUSVAN-1-MUS` Will Lorenzo Musetti win set 1 in the Lorenzo Musetti vs Luca Van Assche match: 0.65/0.69 mid 67.0%, model 62.3% (projection_v2.0 (prediction ledger)) -- gap -4.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV05MUSVAN-2-MUS` Will Lorenzo Musetti win set 2 in the Lorenzo Musetti vs Luca Van Assche match: 0.65/0.69 mid 67.0%, model 62.3% (projection_v2.0 (prediction ledger)) -- gap -4.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV05MUSVAN-2-VAN` Will Luca Van Assche win set 2 in the Lorenzo Musetti vs Luca Van Assche match: 0.31/0.35 mid 33.0%, model 37.7% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV05MUSVAN-1-VAN` Will Luca Van Assche win set 1 in the Lorenzo Musetti vs Luca Van Assche match: 0.33/0.35 mid 34.0%, model 37.7% (projection_v2.0 (prediction ledger)) -- gap +3.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV05MUSVAN-18` Over 17.5 games: 0.86/0.88 mid 87.0%, model 90.2% (projection_v2.0 (prediction ledger)) -- gap +3.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Aleshchev / Storch vs Jeong / Yang -- M15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05ALESTOJEOYAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aleshchev / Storch (`KXITFDOUBLES-26NOV05ALESTOJEOYAN-ALESTO`) | 0.06 / 0.27 (34) | 16.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jeong / Yang (`KXITFDOUBLES-26NOV05ALESTOJEOYAN-JEOYAN`) | 0.67 / 0.90 (1) | 78.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alessio Basile vs Mattia Nannelli -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211450:213617:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alessio Basile (`KXITFMATCH-26NOV05BASNAN-BAS`) | 0.58 / 0.61 (64) | 59.5% | 64.0% | 62.2% | 57.7% [54.1%-61.2%] | -- | -- | -- | -- | PASS | +4.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mattia Nannelli (`KXITFMATCH-26NOV05BASNAN-NAN`) | 0.33 / 0.42 (8) | 37.5% | 36.0% | 37.8% | 42.3% [38.8%-45.9%] | -- | -- | -- | -- | PASS | -1.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 952.0, B 425.0; serve-point win A 61.1%, B 41.7%; Elo A 1252.5, B 1206.3; model uncertainty 0.0356
* Form inputs: days since last match A 345, B 254; matches on record A 43, B 9; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.020, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hsun Lin / Lorusso vs Dong / Yang -- M15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05HSULORDONYAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dong / Yang (`KXITFDOUBLES-26NOV05HSULORDONYAN-DONYAN`) | 0.22 / 0.46 (46) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hsun Lin / Lorusso (`KXITFDOUBLES-26NOV05HSULORDONYAN-HSULOR`) | 0.47 / 0.71 (86) | 59.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Filip Cristian Jianu vs Alexander Wagner -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202262:213138:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Filip Cristian Jianu (`KXITFMATCH-26NOV05JIAWAG-JIA`) | 0.87 / 0.91 (125) | 89.0% | 89.6% | 89.3% | 89.3% [88.0%-90.7%] | -- | -- | -- | -- | PASS | +0.6 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexander Wagner (`KXITFMATCH-26NOV05JIAWAG-WAG`) | 0.08 / 0.09 (27) | 8.5% | 10.4% | 10.7% | 10.7% [9.3%-11.9%] | -- | -- | -- | -- | PASS | +1.9 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4620.0, B 861.0; serve-point win A 61.1%, B 48.5%; Elo A 1563.0, B 1196.5; model uncertainty 0.0134
* Form inputs: days since last match A 16, B 191; matches on record A 612, B 22; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.002, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## William Kjellberg vs Andrey Chepelev -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05KJECHE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrey Chepelev (`KXITFMATCH-26NOV05KJECHE-CHE`) | 0.87 / 0.93 (25) | 90.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| William Kjellberg (`KXITFMATCH-26NOV05KJECHE-KJE`) | 0.07 / 0.15 (215) | 11.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Martin Van Der Meerschen vs Antoni Fabre -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207592:212934:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Antoni Fabre (`KXITFMATCH-26NOV05VANFAB-FAB`) | 0.27 / 0.37 (9) | 32.0% | 41.1% | 48.9% | 43.7% [41.2%-45.2%] | -- | -- | -- | -- | PASS | +9.1 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Martin Van Der Meerschen (`KXITFMATCH-26NOV05VANFAB-VAN`) | 0.64 / 0.73 (2) | 68.5% | 58.9% | 51.1% | 56.3% [54.8%-58.8%] | -- | -- | -- | -- | PASS | -9.6 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2032.0, B 944.0; serve-point win A 56.8%, B 44.9%; Elo A 1326.4, B 1264.7; model uncertainty 0.0204
* Form inputs: days since last match A 191, B 191; matches on record A 103, B 24; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.016, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Coleman Wong vs Chun-Chien Hou -- ATP Challenger Taipei R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-05T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05WONHOU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chun-Chien Hou (`KXATPCHALLENGERMATCH-26NOV05WONHOU-HOU`) | 0.03 / 0.05 (1375) | 4.0% | -- | -- | -- [-----] | -- | 3.5% | 3.5% | MARKETS_AGREE | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Coleman Wong (`KXATPCHALLENGERMATCH-26NOV05WONHOU-WON`) | 0.95 / 0.97 (1810) | 96.0% | -- | -- | -- [-----] | -- | 96.2% | 96.2% | MARKETS_AGREE | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## An / Cao vs Yi Liu / Luo -- W15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05ANXCAOYILLUO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| An / Cao (`KXITFWDOUBLES-26NOV05ANXCAOYILLUO-ANXCAO`) | 0.06 / 0.18 (30) | 12.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yi Liu / Luo (`KXITFWDOUBLES-26NOV05ANXCAOYILLUO-YILLUO`) | 0.77 / 0.90 (1) | 83.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jana Bojovic vs Alesia Breaz -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215293:270165:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jana Bojovic (`KXITFWMATCH-26NOV05BOJBRE-BOJ`) | 0.25 / 0.32 (105) | 28.5% | 70.4% | 46.8% | 62.7% [60.6%-64.7%] | -- | -- | -- | -- | PASS | +41.9 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Alesia Breaz (`KXITFWMATCH-26NOV05BOJBRE-BRE`) | 0.64 / 0.75 (6) | 69.5% | 29.6% | 53.2% | 37.3% [35.3%-39.4%] | -- | -- | -- | -- | PASS | -39.9 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 933.0; serve-point win A 52.6%, B 51.4%; Elo A 1511.8, B 1423.6; model uncertainty 0.0204
* Form inputs: days since last match A 800, B 99; matches on record A 187, B 21; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05BOJBRE-BOJ  (YES = Jana Bojovic)
Model: 70%
Kalshi: 28%
Gap: +42 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.021, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniela Darta Feldmane vs Valeriia Iushchenko -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05FELIUS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniela Darta Feldmane (`KXITFWMATCH-26NOV05FELIUS-FEL`) | 0.05 / 0.08 (134) | 6.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Valeriia Iushchenko (`KXITFWMATCH-26NOV05FELIUS-IUS`) | 0.88 / 0.94 (100) | 91.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ksenia Laskutova vs Julia Stamatova -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206336:215372:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ksenia Laskutova (`KXITFWMATCH-26NOV05LASSTA-LAS`) | 0.61 / 0.75 (1) | 68.0% | 65.0% | 71.8% | 65.1% [55.9%-70.4%] | -- | -- | -- | -- | PASS | -3.0 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Julia Stamatova (`KXITFWMATCH-26NOV05LASSTA-STA`) | 0.24 / 0.33 (1) | 28.5% | 35.0% | 28.2% | 34.9% [29.6%-44.1%] | -- | -- | -- | -- | PASS | +6.5 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1449.0, B 1367.0; serve-point win A 54.9%, B 48.0%; Elo A 1439.0, B 1382.9; model uncertainty 0.0726
* Form inputs: days since last match A 191, B 191; matches on record A 372, B 862; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.015, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Shao / Ye vs Chen / Tang -- W15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05SHAYEXCHETAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chen / Tang (`KXITFWDOUBLES-26NOV05SHAYEXCHETAN-CHETAN`) | 0.26 / 0.49 (49) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Shao / Ye (`KXITFWDOUBLES-26NOV05SHAYEXCHETAN-SHAYEX`) | 0.44 / 0.68 (78) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Diana-Ioana Simionescu vs Ilary Pistola -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264978:270265:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ilary Pistola (`KXITFWMATCH-26NOV05SIMPIS-PIS`) | 0.50 / 0.56 (100) | 53.0% | 14.9% | 33.4% | 31.0% [29.6%-31.5%] | -- | -- | -- | -- | PASS | -38.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Diana-Ioana Simionescu (`KXITFWMATCH-26NOV05SIMPIS-SIM`) | 0.43 / 0.48 (13) | 45.5% | 85.1% | 66.6% | 69.0% [68.5%-70.4%] | -- | -- | -- | -- | PASS | +39.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1418.0, B 175.0; serve-point win A 56.7%, B 51.1%; Elo A 1427.4, B 1281.7; model uncertainty 0.0093
* Form inputs: days since last match A 261, B 106; matches on record A 46, B 5; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05SIMPIS-SIM  (YES = Diana-Ioana Simionescu)
Model: 85%
Kalshi: 46%
Gap: +40 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Momoko Kobori / Peangtarn Plipuech vs Naima Karamoko / Simona Waltert -- WTA Chennai QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-05 12:30Z
* Current expected start: 2026-11-05 13:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: 2026-11-05 12:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-05T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05KOBPLIKARWAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naima Karamoko / Simona Waltert (`KXWTADOUBLES-26NOV05KOBPLIKARWAL-KARWAL`) | 0.05 / 0.83 (1) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Momoko Kobori / Peangtarn Plipuech (`KXWTADOUBLES-26NOV05KOBPLIKARWAL-KOBPLI`) | 0.12 / 0.93 (5) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kilian Feldbausch vs Remy Bertola -- ATP Challenger Taranto R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 13:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-05T13:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05FELBER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Remy Bertola (`KXATPCHALLENGERMATCH-26NOV05FELBER-BER`) | 0.51 / 0.52 (1020) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kilian Feldbausch (`KXATPCHALLENGERMATCH-26NOV05FELBER-FEL`) | 0.48 / 0.49 (994) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Maxim Mrva vs Thomas Faurel -- ATP Challenger Taranto R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 13:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-05T13:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05MRVFAU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thomas Faurel (`KXATPCHALLENGERMATCH-26NOV05MRVFAU-FAU`) | 0.34 / 0.36 (1312) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maxim Mrva (`KXATPCHALLENGERMATCH-26NOV05MRVFAU-MRV`) | 0.64 / 0.66 (1853) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Sumit Nagal vs Hugo Grenier -- ATP Challenger Taranto R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 13:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-05T13:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05NAGGRE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Grenier (`KXATPCHALLENGERMATCH-26NOV05NAGGRE-GRE`) | 0.48 / 0.50 (20) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sumit Nagal (`KXATPCHALLENGERMATCH-26NOV05NAGGRE-NAG`) | 0.50 / 0.52 (1317) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Alam / Eichenseher vs Bessonov / Kharlamov -- M15 Fergana QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05ALAEICBESKHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alam / Eichenseher (`KXITFDOUBLES-26NOV05ALAEICBESKHA-ALAEIC`) | 0.60 / 0.82 (138) | 71.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bessonov / Kharlamov (`KXITFDOUBLES-26NOV05ALAEICBESKHA-BESKHA`) | 0.11 / 0.33 (37) | 22.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Melih Anavatan vs Nicolas Ifi -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212552:212903:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Melih Anavatan (`KXITFMATCH-26NOV05ANAIFI-ANA`) | 0.41 / 0.49 (100) | 45.0% | 49.7% | 56.0% | 51.0% [48.0%-52.5%] | -- | -- | -- | -- | PASS | +4.7 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nicolas Ifi (`KXITFMATCH-26NOV05ANAIFI-IFI`) | 0.56 / 0.59 (104) | 57.5% | 50.3% | 44.0% | 49.0% [47.5%-52.0%] | -- | -- | -- | -- | PASS | -7.2 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1377.0, B 1814.0; serve-point win A 63.2%, B 36.7%; Elo A 1191.9, B 1220.4; model uncertainty 0.0227
* Form inputs: days since last match A 191, B 198; matches on record A 30, B 75; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.010, surface_dev_loose +0.005, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stefan Adrian Andreescu vs Nicolo Toffanin -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210650:211532:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefan Adrian Andreescu (`KXITFMATCH-26NOV05ANDTOF-AND`) | 0.85 / 0.93 (106) | 89.0% | 79.2% | 88.3% | 84.5% [79.4%-87.8%] | -- | -- | -- | -- | PASS | -9.8 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nicolo Toffanin (`KXITFMATCH-26NOV05ANDTOF-TOF`) | 0.06 / 0.13 (12) | 9.5% | 20.8% | 11.7% | 15.5% [12.2%-20.6%] | -- | -- | -- | -- | PASS | +11.3 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3228.0, B 1135.0; serve-point win A 56.2%, B 49.9%; Elo A 1441.5, B 1189.8; model uncertainty 0.0419
* Form inputs: days since last match A 254, B 226; matches on record A 144, B 38; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.003, surface_pool_high +0.003, surface_dev_loose +0.006, surface_dev_tight -0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lorenzo Angelini vs Alexandre Aubriot -- M25 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:149117:208147:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Angelini (`KXITFMATCH-26NOV05ANGAUB-ANG`) | 0.65 / 0.68 (120) | 66.5% | 61.5% | 59.9% | 57.9% [55.2%-58.9%] | -- | -- | -- | -- | PASS | -5.0 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexandre Aubriot (`KXITFMATCH-26NOV05ANGAUB-AUB`) | 0.31 / 0.34 (129) | 32.5% | 38.5% | 40.1% | 42.1% [41.1%-44.8%] | -- | -- | -- | -- | WATCH | +6.0 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2397.0, B 2915.0; serve-point win A 57.1%, B 45.1%; Elo A 1370.3, B 1336.7; model uncertainty 0.0185
* Form inputs: days since last match A 198, B 205; matches on record A 69, B 297; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.005, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arcon / Dolzhenkov vs Hrazdil / Lakshmanan -- M15 Fergana QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05ARCDOLHRALAK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arcon / Dolzhenkov (`KXITFDOUBLES-26NOV05ARCDOLHRALAK-ARCDOL`) | 0.06 / 0.25 (33) | 15.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hrazdil / Lakshmanan (`KXITFDOUBLES-26NOV05ARCDOLHRALAK-HRALAK`) | 0.70 / 0.90 (1) | 80.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lorenzo Bocchi vs John Bothma -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200595:213011:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Bocchi (`KXITFMATCH-26NOV05BOCBOT-BOC`) | 0.77 / 0.85 (295) | 81.0% | 76.6% | 75.9% | 68.6% [64.0%-72.2%] | -- | -- | -- | -- | PASS | -4.4 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| John Bothma (`KXITFMATCH-26NOV05BOCBOT-BOT`) | 0.12 / 0.23 (14) | 17.5% | 23.4% | 24.1% | 31.4% [27.9%-36.0%] | -- | -- | -- | -- | PASS | +5.9 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2132.0, B 278.0; serve-point win A 64.4%, B 41.3%; Elo A 1362.7, B 1245.5; model uncertainty 0.0409
* Form inputs: days since last match A 191, B 198; matches on record A 308, B 10; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.035, surface_pool_high -0.047, surface_dev_loose +0.004, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Connel / Sornlaksup vs He / Song -- M15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05CONSORHEXSON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Connel / Sornlaksup (`KXITFDOUBLES-26NOV05CONSORHEXSON-CONSOR`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| He / Song (`KXITFDOUBLES-26NOV05CONSORHEXSON-HEXSON`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Melios Efstathiou vs Pablo Perez Ramos -- M25 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05EFSPER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Melios Efstathiou (`KXITFMATCH-26NOV05EFSPER-EFS`) | 0.46 / 0.48 (243) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pablo Perez Ramos (`KXITFMATCH-26NOV05EFSPER-PER`) | 0.51 / 0.53 (12) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amr Elsayed vs Artur Kukasian -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209871:210477:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amr Elsayed (`KXITFMATCH-26NOV05ELSKUK-ELS`) | 0.50 / 0.73 (25) | 61.5% | 65.5% | 76.0% | 71.0% [64.1%-73.9%] | -- | -- | -- | -- | PASS | +4.0 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Artur Kukasian (`KXITFMATCH-26NOV05ELSKUK-KUK`) | 0.27 / 0.43 (100) | 35.0% | 34.5% | 24.0% | 29.0% [26.1%-35.9%] | -- | -- | -- | -- | PASS | -0.5 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 3030.0, B 2159.0; serve-point win A 62.3%, B 40.8%; Elo A 1388.9, B 1300.0; model uncertainty 0.0493
* Form inputs: days since last match A 47, B 233; matches on record A 252, B 99; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.004, surface_dev_loose +0.005, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Miles Jones vs Oleksii Krutykh -- M25 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207404:208071:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miles Jones (`KXITFMATCH-26NOV05JONKRU-JON`) | 0.24 / 0.28 (7) | 26.0% | 45.9% | 68.2% | 54.2% [36.7%-61.4%] | -- | -- | -- | -- | PASS | +19.9 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oleksii Krutykh (`KXITFMATCH-26NOV05JONKRU-KRU`) | 0.67 / 0.72 (100) | 69.5% | 54.1% | 31.8% | 45.8% [38.6%-63.3%] | -- | -- | -- | -- | PASS | -15.4 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2182.0, B 3078.0; serve-point win A 56.8%, B 42.4%; Elo A 1391.3, B 1503.9; model uncertainty 0.1238
* Form inputs: days since last match A 198, B 30; matches on record A 132, B 467; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV05JONKRU-JON  (YES = Miles Jones)
Model: 46%
Kalshi: 26%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.021, surface_dev_loose +0.026, surface_dev_tight -0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Veljko Krstic vs Dragos Nicolae Madaras -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200096:210112:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Veljko Krstic (`KXITFMATCH-26NOV05KRSMAD-KRS`) | 0.19 / 0.32 (36) | 25.5% | 3.3% | 0.5% | 6.4% [5.0%-7.7%] | -- | -- | -- | -- | PASS | -22.2 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dragos Nicolae Madaras (`KXITFMATCH-26NOV05KRSMAD-MAD`) | 0.62 / 0.81 (25) | 71.5% | 96.7% | 99.5% | 93.6% [92.3%-95.0%] | -- | -- | -- | -- | PASS | +25.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 106.0, B 1412.0; serve-point win A 50.0%, B 36.0%; Elo A 1205.2, B 1644.1; model uncertainty 0.0136
* Form inputs: days since last match A 513, B 219; matches on record A 7, B 453; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV05KRSMAD-MAD  (YES = Dragos Nicolae Madaras)
Model: 97%
Kalshi: 72%
Gap: +25 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.001, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lomakin / Shin vs Kamath / Suresh -- M15 Fergana QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05LOMSHIKAMSUR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kamath / Suresh (`KXITFDOUBLES-26NOV05LOMSHIKAMSUR-KAMSUR`) | 0.08 / 0.36 (39) | 22.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lomakin / Shin (`KXITFDOUBLES-26NOV05LOMSHIKAMSUR-LOMSHI`) | 0.57 / 0.79 (119) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Andrej Nedic vs Karl Friberg -- M25 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200418:210119:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karl Friberg (`KXITFMATCH-26NOV05NEDFRI-FRI`) | 0.26 / 0.33 (134) | 29.5% | 20.2% | 13.2% | 21.5% [17.5%-26.5%] | 33.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.3 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Andrej Nedic (`KXITFMATCH-26NOV05NEDFRI-NED`) | 0.68 / 0.69 (104) | 68.5% | 79.8% | 86.8% | 78.5% [73.5%-82.5%] | 66.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +11.3 pp | REVIEW | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4081.0, B 1311.0; serve-point win A 60.8%, B 45.5%; Elo A 1548.9, B 1408.8; model uncertainty 0.0446
* Form inputs: days since last match A 16, B 46; matches on record A 236, B 349; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.004, surface_dev_loose -0.001, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vuk Radjenovic vs Lieven Mietusch -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211366:214093:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lieven Mietusch (`KXITFMATCH-26NOV05RADMIE-MIE`) | 0.25 / 0.34 (7) | 29.5% | 50.1% | 55.7% | 56.2% [56.2%-56.2%] | -- | -- | -- | -- | PASS | +20.6 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Vuk Radjenovic (`KXITFMATCH-26NOV05RADMIE-RAD`) | 0.56 / 0.75 (25) | 65.5% | 49.9% | 44.3% | 43.8% [43.8%-43.8%] | -- | -- | -- | -- | PASS | -15.6 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 799.0, B 57.0; serve-point win A 59.8%, B 40.1%; Elo A 1242.8, B 1283.7; model uncertainty 0.0001
* Form inputs: days since last match A 366, B 443; matches on record A 71, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV05RADMIE-MIE  (YES = Lieven Mietusch)
Model: 50%
Kalshi: 30%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Heorhii Shylov vs Alan Wazny -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05SHYWAZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Heorhii Shylov (`KXITFMATCH-26NOV05SHYWAZ-SHY`) | 0.27 / 0.41 (14) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alan Wazny (`KXITFMATCH-26NOV05SHYWAZ-WAZ`) | 0.65 / 0.73 (1) | 69.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Wang / Zheng vs Chen / Te -- M15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05WANZHECHETEX:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chen / Te (`KXITFDOUBLES-26NOV05WANZHECHETEX-CHETEX`) | 0.52 / 0.76 (104) | 64.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Wang / Zheng (`KXITFDOUBLES-26NOV05WANZHECHETEX-WANZHE`) | 0.19 / 0.42 (43) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Oscar Weightman vs Adrien Burdet -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208267:208853:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrien Burdet (`KXITFMATCH-26NOV05WEIBUR-BUR`) | 0.13 / 0.23 (4) | 18.0% | 17.5% | 34.5% | 26.1% [24.4%-27.4%] | -- | -- | -- | -- | PASS | -0.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oscar Weightman (`KXITFMATCH-26NOV05WEIBUR-WEI`) | 0.74 / 0.85 (9) | 79.5% | 82.5% | 65.5% | 73.9% [72.7%-75.6%] | -- | -- | -- | -- | PASS | +3.0 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1253.0, B 480.0; serve-point win A 64.7%, B 42.6%; Elo A 1369.5, B 1163.6; model uncertainty 0.0145
* Form inputs: days since last match A 121, B 191; matches on record A 130, B 27; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose +0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Michael Wright vs Ioannis Xilas -- M25 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05WRIXIL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michael Wright (`KXITFMATCH-26NOV05WRIXIL-WRI`) | 0.05 / 0.10 (17) | 7.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ioannis Xilas (`KXITFMATCH-26NOV05WRIXIL-XIL`) | 0.91 / 0.95 (291) | 93.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Selina Atay vs Theresa Stabauer -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05ATASTA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Selina Atay (`KXITFWMATCH-26NOV05ATASTA-ATA`) | 0.49 / 0.51 (3) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Theresa Stabauer (`KXITFWMATCH-26NOV05ATASTA-STA`) | 0.45 / 0.47 (47) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Deborah Chiesa vs Alisa Oktiabreva -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211328:260765:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Deborah Chiesa (`KXITFWMATCH-26NOV05CHIOKT-CHI`) | 0.15 / 0.16 (35) | 15.5% | 22.2% | 34.3% | 30.9% [27.7%-32.9%] | -- | -- | -- | -- | WATCH | +6.7 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alisa Oktiabreva (`KXITFWMATCH-26NOV05CHIOKT-OKT`) | 0.82 / 0.84 (5) | 83.0% | 77.8% | 65.7% | 69.0% [67.1%-72.3%] | -- | -- | -- | -- | PASS | -5.2 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2456.0, B 1999.0; serve-point win A 48.0%, B 46.3%; Elo A 1473.4, B 1652.3; model uncertainty 0.0258
* Form inputs: days since last match A 23, B 107; matches on record A 551, B 67; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.019, surface_dev_loose -0.032, surface_dev_tight +0.019
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Iveta Dapkute vs Anja Wildgruber -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:210158:222668:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iveta Dapkute (`KXITFWMATCH-26NOV05DAPWIL-DAP`) | 0.54 / 0.65 (9) | 59.5% | 66.8% | 61.1% | 62.6% [60.6%-66.6%] | -- | -- | -- | -- | PASS | +7.3 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anja Wildgruber (`KXITFWMATCH-26NOV05DAPWIL-WIL`) | 0.35 / 0.45 (9) | 40.0% | 33.2% | 38.9% | 37.4% [33.4%-39.4%] | -- | -- | -- | -- | PASS | -6.8 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 792.0, B 2380.0; serve-point win A 53.7%, B 49.5%; Elo A 1404.3, B 1305.7; model uncertainty 0.03
* Form inputs: days since last match A 191, B 191; matches on record A 203, B 348; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.030, surface_pool_high -0.021, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yasmin Ezzat vs Mu Jie Tzeng -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05EZZTZE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yasmin Ezzat (`KXITFWMATCH-26NOV05EZZTZE-EZZ`) | 0.65 / 0.68 (8) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mu Jie Tzeng (`KXITFWMATCH-26NOV05EZZTZE-TZE`) | 0.29 / 0.30 (35) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anais Gabriel vs Ayse Bal -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221155:270062:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ayse Bal (`KXITFWMATCH-26NOV05GABBAL-BAL`) | 0.57 / 0.61 (5) | 59.0% | 51.1% | 56.4% | 55.4% [55.3%-55.4%] | -- | -- | -- | -- | PASS | -7.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anais Gabriel (`KXITFWMATCH-26NOV05GABBAL-GAB`) | 0.37 / 0.40 (210) | 38.5% | 48.9% | 43.6% | 44.6% [44.6%-44.7%] | -- | -- | -- | -- | PASS | +10.4 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 534.0, B 53.0; serve-point win A 50.2%, B 49.6%; Elo A 1217.3, B 1254.7; model uncertainty 0.0001
* Form inputs: days since last match A 240, B 115; matches on record A 13, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gavrila / Sakellaridi vs Andronicou / Sara -- W50 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05GAVSAKANDSAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andronicou / Sara (`KXITFWDOUBLES-26NOV05GAVSAKANDSAR-ANDSAR`) | 0.06 / 0.10 (27) | 8.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gavrila / Sakellaridi (`KXITFWDOUBLES-26NOV05GAVSAKANDSAR-GAVSAK`) | 0.86 / 0.90 (1) | 88.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Polina Kuharenko vs Hollie Smart -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:263626:266393:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Kuharenko (`KXITFWMATCH-26NOV05KUHSMA-KUH`) | 0.49 / 0.54 (8) | 51.5% | 87.6% | 89.9% | 77.2% [73.9%-79.6%] | -- | -- | -- | -- | PASS | +36.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hollie Smart (`KXITFWMATCH-26NOV05KUHSMA-SMA`) | 0.44 / 0.51 (31) | 47.5% | 12.4% | 10.1% | 22.8% [20.4%-26.1%] | -- | -- | -- | -- | PASS | -35.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1767.0, B 282.0; serve-point win A 58.9%, B 49.8%; Elo A 1462.7, B 1286.6; model uncertainty 0.0284
* Form inputs: days since last match A 240, B 450; matches on record A 55, B 10; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05KUHSMA-KUH  (YES = Polina Kuharenko)
Model: 88%
Kalshi: 52%
Gap: +36 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.016, surface_dev_loose +0.008, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ada Kumru vs Anastasia Lepskaya -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05KUMLEP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ada Kumru (`KXITFWMATCH-26NOV05KUMLEP-KUM`) | 0.59 / 0.68 (5) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anastasia Lepskaya (`KXITFWMATCH-26NOV05KUMLEP-LEP`) | 0.32 / 0.35 (141) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marija Lauva vs Adelina Lacinova -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264264:espn:espn:16130:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adelina Lacinova (`KXITFWMATCH-26NOV05LAULAC-LAC`) | 0.72 / 0.78 (204) | 75.0% | 84.9% | 64.6% | 72.2% [72.2%-72.2%] | -- | -- | -- | -- | PASS | +9.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marija Lauva (`KXITFWMATCH-26NOV05LAULAC-LAU`) | 0.22 / 0.24 (5) | 23.0% | 15.1% | 35.4% | 27.8% [27.8%-27.8%] | -- | -- | -- | -- | PASS | -7.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 232.0, B 0.0; serve-point win A 49.5%, B 42.8%; Elo A 1311.7, B 1475.8; model uncertainty 0.0003
* Form inputs: days since last match A 366, B 31; matches on record A 4, B 5; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Qu / Xi Wu vs Li / Zhao -- W15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05QUXXIWLIXZHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Li / Zhao (`KXITFWDOUBLES-26NOV05QUXXIWLIXZHA-LIXZHA`) | 0.15 / 0.37 (39) | 26.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Qu / Xi Wu (`KXITFWDOUBLES-26NOV05QUXXIWLIXZHA-QUXXIW`) | 0.57 / 0.80 (125) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jennifer Ruggeri vs Eliska Tichackova -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221411:254748:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jennifer Ruggeri (`KXITFWMATCH-26NOV05RUGTIC-RUG`) | 0.64 / 0.68 (20) | 66.0% | 24.5% | 29.5% | 30.0% [26.4%-38.4%] | -- | -- | -- | -- | PASS | -41.5 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Eliska Tichackova (`KXITFWMATCH-26NOV05RUGTIC-TIC`) | 0.31 / 0.34 (167) | 32.5% | 75.5% | 70.5% | 70.0% [61.6%-73.6%] | -- | -- | -- | -- | WATCH | +43.0 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3454.0, B 1647.0; serve-point win A 49.0%, B 45.8%; Elo A 1481.3, B 1623.6; model uncertainty 0.06
* Form inputs: days since last match A 23, B 254; matches on record A 244, B 46; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05RUGTIC-TIC  (YES = Eliska Tichackova)
Model: 76%
Kalshi: 32%
Gap: +43 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.029, surface_pool_high -0.027, surface_dev_loose -0.018, surface_dev_tight +0.019
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Joelle Lilly Sophie Steur vs Lucie Nguyen Tan -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221259:221468:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucie Nguyen Tan (`KXITFWMATCH-26NOV05STENGU-NGU`) | 0.23 / 0.24 (100) | 23.5% | 31.6% | 31.0% | 31.5% [30.5%-34.4%] | -- | -- | -- | -- | WATCH | +8.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Joelle Lilly Sophie Steur (`KXITFWMATCH-26NOV05STENGU-STE`) | 0.74 / 0.77 (18) | 75.5% | 68.4% | 69.0% | 68.5% [65.6%-69.5%] | -- | -- | -- | -- | PASS | -7.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2592.0, B 1887.0; serve-point win A 54.1%, B 49.5%; Elo A 1564.8, B 1438.0; model uncertainty 0.0194
* Form inputs: days since last match A 20, B 20; matches on record A 223, B 293; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alisa Terentyeva vs Aya El Sayed -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221083:270104:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aya El Sayed (`KXITFWMATCH-26NOV05TERELS-ELS`) | 0.66 / 0.67 (75) | 66.5% | 62.6% | 45.8% | 47.9% [44.7%-51.1%] | -- | -- | -- | -- | PASS | -3.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alisa Terentyeva (`KXITFWMATCH-26NOV05TERELS-TER`) | 0.28 / 0.34 (8) | 31.0% | 37.4% | 54.2% | 52.1% [48.9%-55.3%] | -- | -- | -- | -- | PASS | +6.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 198.0, B 698.0; serve-point win A 53.9%, B 43.7%; Elo A 1214.7, B 1200.5; model uncertainty 0.0318
* Form inputs: days since last match A 191, B 331; matches on record A 4, B 81; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.027, surface_pool_high +0.032, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tikhonova / Yamazaki vs Sun / Xu -- W15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05TIKYAMSUNXUX:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun / Xu (`KXITFWDOUBLES-26NOV05TIKYAMSUNXUX-SUNXUX`) | 0.29 / 0.55 (55) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tikhonova / Yamazaki (`KXITFWDOUBLES-26NOV05TIKYAMSUNXUX-TIKYAM`) | 0.37 / 0.64 (69) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Nuno Borges vs Ignacio Buse -- ATP Paris R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-05 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-05 14:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: 2026-11-05 13:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · Hard · scheduled 2026-11-05T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:132686:209860:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nuno Borges (`KXATPMATCH-26NOV05BORBUS-BOR`) | 0.58 / 0.59 (606) | 58.5% | 61.8% | 61.9% | 62.3% [61.4%-62.3%] | 56.6% | 57.3% | 56.9% | MODEL_LONE_OUTLIER | SHADOW_BET | +3.3 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Ignacio Buse (`KXATPMATCH-26NOV05BORBUS-BUS`) | 0.42 / 0.43 (732) | 42.5% | 38.2% | 38.1% | 37.7% [37.7%-38.6%] | 43.4% | 43.9% | 43.7% | MODEL_LONE_OUTLIER | PASS | -4.3 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5796.0, B 5542.0; serve-point win A 64.4%, B 38.0%; Elo A 1865.0, B 1763.6; model uncertainty 0.0048
* Form inputs: days since last match A 1, B 2; matches on record A 556, B 288; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26NOV05BORBUS-BOR5` Will Nuno Borges win at least 4.5 more games than Ignacio Buse?: 0.01/0.93 mid 47.0%, model 24.1% (projection_v2.0 (prediction ledger)) -- gap -22.9 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05BORBUS-BOR20` Will Nuno Borges win the Nuno Borges vs Ignacio Buse match by a set score of 2-0?: 0.01/0.39 mid 20.0%, model 33.6% (projection_v2.0 (prediction ledger)) -- gap +13.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05BORBUS-BOR21` Will Nuno Borges win the Nuno Borges vs Ignacio Buse match by a set score of 2-1?: 0.01/0.30 mid 15.5%, model 28.2% (projection_v2.0 (prediction ledger)) -- gap +12.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV05BORBUS-20` Over 19.5 games: 0.41/0.93 mid 67.0%, model 79.6% (projection_v2.0 (prediction ledger)) -- gap +12.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05BORBUS-BUS21` Will Ignacio Buse win the Nuno Borges vs Ignacio Buse match by a set score of 2-1?: 0.01/0.26 mid 13.5%, model 20.5% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV05BORBUS-BUS2` Will Ignacio Buse win at least 1.5 more games than Nuno Borges?: 0.33/0.39 mid 36.0%, model 31.3% (projection_v2.0 (prediction ledger)) -- gap -4.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV05BORBUS-BOR2` Will Nuno Borges win at least 1.5 more games than Ignacio Buse?: 0.49/0.54 mid 51.5%, model 54.5% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV05BORBUS-25` Over 24.5 games: 0.48/0.50 mid 49.0%, model 51.9% (projection_v2.0 (prediction ledger)) -- gap +2.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05BORBUS-BUS20` Will Ignacio Buse win the Nuno Borges vs Ignacio Buse match by a set score of 2-0?: 0.01/0.29 mid 15.0%, model 17.7% (projection_v2.0 (prediction ledger)) -- gap +2.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV05BORBUS-1-BOR` Will Nuno Borges win set 1 in the Nuno Borges vs Ignacio Buse match: 0.53/0.59 mid 56.0%, model 57.9% (projection_v2.0 (prediction ledger)) -- gap +1.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV05BORBUS-1-BUS` Will Ignacio Buse win set 1 in the Nuno Borges vs Ignacio Buse match: 0.41/0.47 mid 44.0%, model 42.1% (projection_v2.0 (prediction ledger)) -- gap -1.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV05BORBUS-2-BOR` Will Nuno Borges win set 2 in the Nuno Borges vs Ignacio Buse match: 0.53/0.60 mid 56.5%, model 57.9% (projection_v2.0 (prediction ledger)) -- gap +1.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV05BORBUS-2-BUS` Will Ignacio Buse win set 2 in the Nuno Borges vs Ignacio Buse match: 0.40/0.47 mid 43.5%, model 42.1% (projection_v2.0 (prediction ledger)) -- gap -1.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV05BORBUS-30` Over 29.5 games: 0.29/0.31 mid 30.0%, model 29.6% (projection_v2.0 (prediction ledger)) -- gap -0.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Duje Ajdukovic vs Kris van Wyk -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144748:207213:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Duje Ajdukovic (`KXITFMATCH-26NOV05AJDVAN-AJD`) | 0.80 / 0.84 (229) | 82.0% | 87.5% | 88.4% | 86.0% [81.9%-87.6%] | -- | -- | -- | -- | PASS | +5.5 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kris van Wyk (`KXITFMATCH-26NOV05AJDVAN-VAN`) | 0.15 / 0.17 (167) | 16.0% | 12.5% | 11.6% | 14.0% [12.4%-18.1%] | -- | -- | -- | -- | PASS | -3.5 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4622.0, B 2875.0; serve-point win A 63.3%, B 45.5%; Elo A 1549.1, B 1319.6; model uncertainty 0.0288
* Form inputs: days since last match A 30, B 198; matches on record A 479, B 324; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.017, surface_pool_high -0.024, surface_dev_loose +0.008, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andrea Bacaloni vs John Echeverria -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208126:211407:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrea Bacaloni (`KXITFMATCH-26NOV05BACECH-BAC`) | 0.13 / 0.15 (65) | 14.0% | 7.1% | 5.6% | 9.2% [6.1%-13.9%] | -- | -- | -- | -- | PASS | -6.8 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| John Echeverria (`KXITFMATCH-26NOV05BACECH-ECH`) | 0.83 / 0.88 (230) | 85.5% | 92.8% | 94.4% | 90.8% [86.1%-93.9%] | -- | -- | -- | -- | PASS | +7.3 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 858.0, B 2252.0; serve-point win A 51.0%, B 37.9%; Elo A 1169.8, B 1517.6; model uncertainty 0.0391
* Form inputs: days since last match A 233, B 79; matches on record A 103, B 248; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.008, surface_dev_loose -0.006, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nino Ehrenschneider vs Wissam Abderrahman -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209510:210230:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wissam Abderrahman (`KXITFMATCH-26NOV05EHRABD-ABD`) | 0.28 / 0.30 (28) | 29.0% | 28.4% | 29.1% | 30.4% [27.8%-32.7%] | -- | -- | -- | -- | PASS | -0.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nino Ehrenschneider (`KXITFMATCH-26NOV05EHRABD-EHR`) | 0.69 / 0.70 (83) | 69.5% | 71.6% | 70.9% | 69.6% [67.3%-72.2%] | -- | -- | -- | -- | PASS | +2.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3493.0, B 236.0; serve-point win A 63.2%, B 41.2%; Elo A 1374.1, B 1233.2; model uncertainty 0.0245
* Form inputs: days since last match A 191, B 464; matches on record A 129, B 75; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.026, surface_pool_high -0.023, surface_dev_loose +0.004, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kasra Rahmani vs Aziz Dougaz -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144826:212071:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aziz Dougaz (`KXITFMATCH-26NOV05RAHDOU-DOU`) | 0.74 / 0.78 (100) | 76.0% | 73.1% | 66.7% | 69.9% [68.5%-74.2%] | -- | -- | -- | -- | PASS | -2.9 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kasra Rahmani (`KXITFMATCH-26NOV05RAHDOU-RAH`) | 0.21 / 0.23 (26) | 22.0% | 26.9% | 33.3% | 30.1% [25.9%-31.5%] | -- | -- | -- | -- | PASS | +4.9 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2554.0, B 2640.0; serve-point win A 59.8%, B 35.4%; Elo A 1437.6, B 1614.8; model uncertainty 0.0283
* Form inputs: days since last match A 191, B 17; matches on record A 63, B 656; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.013, surface_dev_loose -0.004, surface_dev_tight +0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maxence Rivet vs Cesar Bouchelaghem -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210726:212134:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cesar Bouchelaghem (`KXITFMATCH-26NOV05RIVBOU-BOU`) | 0.68 / 0.70 (5) | 69.0% | 79.4% | 90.0% | 80.5% [72.3%-85.7%] | -- | -- | -- | -- | PASS | +10.4 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maxence Rivet (`KXITFMATCH-26NOV05RIVBOU-RIV`) | 0.30 / 0.31 (152) | 30.5% | 20.6% | 10.0% | 19.4% [14.3%-27.7%] | -- | -- | -- | -- | PASS | -9.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1073.0, B 2340.0; serve-point win A 57.3%, B 36.3%; Elo A 1275.3, B 1431.8; model uncertainty 0.067
* Form inputs: days since last match A 191, B 191; matches on record A 113, B 80; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.010, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Toufik Sahtali vs Giulio Perego -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200086:212280:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giulio Perego (`KXITFMATCH-26NOV05SAHPER-PER`) | 0.60 / 0.62 (65) | 61.0% | 36.6% | 37.1% | 37.6% [36.1%-41.7%] | -- | -- | -- | -- | PASS | -24.4 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Toufik Sahtali (`KXITFMATCH-26NOV05SAHPER-SAH`) | 0.33 / 0.36 (40) | 34.5% | 63.4% | 62.9% | 62.4% [58.3%-63.9%] | -- | -- | -- | -- | PASS | +28.9 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3339.0, B 1511.0; serve-point win A 58.5%, B 44.1%; Elo A 1404.3, B 1325.0; model uncertainty 0.028
* Form inputs: days since last match A 191, B 191; matches on record A 92, B 51; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV05SAHPER-SAH  (YES = Toufik Sahtali)
Model: 63%
Kalshi: 34%
Gap: +29 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oceane Babel vs Jana Denisenko -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221746:259971:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oceane Babel (`KXITFWMATCH-26NOV05BABDEN-BAB`) | 0.94 / 0.97 (406) | 95.5% | 93.1% | 74.9% | 83.9% [82.2%-85.7%] | -- | -- | -- | -- | PASS | -2.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jana Denisenko (`KXITFWMATCH-26NOV05BABDEN-DEN`) | 0.04 / 0.05 (79) | 4.5% | 6.9% | 25.1% | 16.1% [14.3%-17.8%] | -- | -- | -- | -- | PASS | +2.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1826.0, B 161.0; serve-point win A 58.1%, B 53.0%; Elo A 1437.7, B 1140.7; model uncertainty 0.0175
* Form inputs: days since last match A 191, B 408; matches on record A 160, B 9; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.017, surface_dev_loose -0.000, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lya Fernandez vs Astrid Cirotte -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:236980:259749:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Astrid Cirotte (`KXITFWMATCH-26NOV05FERCIR-CIR`) | 0.76 / 0.77 (100) | 76.5% | 61.5% | 72.3% | 56.9% [52.7%-63.2%] | -- | -- | -- | -- | PASS | -15.0 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lya Fernandez (`KXITFWMATCH-26NOV05FERCIR-FER`) | 0.22 / 0.26 (100) | 24.0% | 38.5% | 27.7% | 43.1% [36.8%-47.3%] | -- | -- | -- | -- | PASS | +14.5 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 463.0, B 2379.0; serve-point win A 50.8%, B 47.0%; Elo A 1351.0, B 1366.7; model uncertainty 0.0525
* Form inputs: days since last match A 191, B 205; matches on record A 66, B 227; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.011, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anastasia Lizunova vs Serena Paris -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260118:261073:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasia Lizunova (`KXITFWMATCH-26NOV05LIZPAR-LIZ`) | 0.87 / 0.94 (10) | 90.5% | 87.7% | 51.1% | 74.8% [73.9%-74.8%] | -- | -- | -- | -- | PASS | -2.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Serena Paris (`KXITFWMATCH-26NOV05LIZPAR-PAR`) | 0.04 / 0.13 (8) | 8.5% | 12.3% | 48.9% | 25.2% [25.2%-26.1%] | -- | -- | -- | -- | PASS | +3.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 647.0, B 0.0; serve-point win A 58.5%, B 50.2%; Elo A 1408.9, B 1224.7; model uncertainty 0.0043
* Form inputs: days since last match A 219, B 702; matches on record A 21, B 5; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Izan Almazan Valiente vs Iliyan Radulov -- M25 Valencia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210721:212978:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Izan Almazan Valiente (`KXITFMATCH-26NOV05ALMRAD-ALM`) | 0.56 / 0.58 (22) | 57.0% | 50.6% | 49.5% | 45.2% [44.2%-47.3%] | -- | -- | -- | -- | PASS | -6.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Iliyan Radulov (`KXITFMATCH-26NOV05ALMRAD-RAD`) | 0.39 / 0.43 (7) | 41.0% | 49.4% | 50.5% | 54.8% [52.7%-55.8%] | -- | -- | -- | -- | WATCH | +8.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2749.0, B 2013.0; serve-point win A 55.0%, B 45.1%; Elo A 1455.6, B 1523.1; model uncertainty 0.0158
* Form inputs: days since last match A 16, B 44; matches on record A 79, B 147; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose -0.005, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gilles Arnaud Bailly vs Benjamin Pietri -- M25 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202125:211451:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gilles Arnaud Bailly (`KXITFMATCH-26NOV05BAIPIE-BAI`) | 0.57 / 0.61 (1) | 59.0% | 76.1% | 60.8% | 70.4% [66.7%-76.8%] | -- | -- | -- | -- | PASS | +17.1 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Benjamin Pietri (`KXITFMATCH-26NOV05BAIPIE-PIE`) | 0.40 / 0.42 (138) | 41.0% | 23.9% | 39.2% | 29.6% [23.2%-33.3%] | -- | -- | -- | -- | PASS | -17.1 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3897.0, B 1540.0; serve-point win A 61.2%, B 44.3%; Elo A 1517.4, B 1291.0; model uncertainty 0.0504
* Form inputs: days since last match A 18, B 58; matches on record A 212, B 233; data quality A

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV05BAIPIE-BAI  (YES = Gilles Arnaud Bailly)
Model: 76%
Kalshi: 59%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: LOW_DISPLAYED_LIQUIDITY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.018, surface_dev_loose -0.018, surface_dev_tight +0.018
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aleksandre Bakshi vs Kerem Yilmaz -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126762:212030:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aleksandre Bakshi (`KXITFMATCH-26NOV05BAKYIL-BAK`) | 0.35 / 0.41 (4) | 38.0% | 61.8% | 64.1% | 69.7% [67.4%-72.0%] | -- | -- | -- | -- | PASS | +23.8 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kerem Yilmaz (`KXITFMATCH-26NOV05BAKYIL-YIL`) | 0.59 / 0.65 (25) | 62.0% | 38.2% | 35.9% | 30.3% [28.1%-32.6%] | -- | -- | -- | -- | PASS | -23.8 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3194.0, B 1334.0; serve-point win A 61.5%, B 40.9%; Elo A 1430.3, B 1248.5; model uncertainty 0.0228
* Form inputs: days since last match A 233, B 93; matches on record A 276, B 42; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV05BAKYIL-BAK  (YES = Aleksandre Bakshi)
Model: 62%
Kalshi: 38%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose -0.014, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alberto Barroso Campos vs Alejandro Manzanera Pertusa -- M25 Valencia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132744:209904:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alberto Barroso Campos (`KXITFMATCH-26NOV05BARMAN-BAR`) | 0.30 / 0.34 (29) | 32.0% | 35.6% | 46.9% | 39.8% [35.4%-44.4%] | -- | -- | -- | -- | PASS | +3.6 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alejandro Manzanera Pertusa (`KXITFMATCH-26NOV05BARMAN-MAN`) | 0.64 / 0.69 (164) | 66.5% | 64.4% | 53.1% | 60.2% [55.6%-64.6%] | -- | -- | -- | -- | PASS | -2.1 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2471.0, B 1670.0; serve-point win A 58.7%, B 38.5%; Elo A 1325.2, B 1453.7; model uncertainty 0.0448
* Form inputs: days since last match A 37, B 198; matches on record A 365, B 190; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.045, surface_pool_high -0.044, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andrea De Marchi vs Marcello Serafini -- M15 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209997:212972:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrea De Marchi (`KXITFMATCH-26NOV05DEMSER-DEM`) | 0.60 / 0.65 (75) | 62.5% | 38.5% | 40.1% | 34.1% [32.2%-35.5%] | -- | -- | -- | -- | PASS | -24.0 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marcello Serafini (`KXITFMATCH-26NOV05DEMSER-SER`) | 0.33 / 0.37 (100) | 35.0% | 61.5% | 59.9% | 65.9% [64.5%-67.8%] | -- | -- | -- | -- | PASS | +26.5 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1480.0, B 1638.0; serve-point win A 55.3%, B 42.5%; Elo A 1227.7, B 1390.2; model uncertainty 0.0169
* Form inputs: days since last match A 198, B 191; matches on record A 38, B 238; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV05DEMSER-SER  (YES = Marcello Serafini)
Model: 61%
Kalshi: 35%
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
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.019, surface_dev_loose -0.015, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Robert Guna vs Robin Bertrand -- M25 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209850:211491:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Robin Bertrand (`KXITFMATCH-26NOV05GUNBER-BER`) | 0.80 / 0.83 (147) | 81.5% | 83.3% | 82.9% | 84.2% [83.5%-84.8%] | -- | -- | -- | -- | PASS | +1.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Robert Guna (`KXITFMATCH-26NOV05GUNBER-GUN`) | 0.15 / 0.18 (25) | 16.5% | 16.7% | 17.1% | 15.8% [15.2%-16.5%] | -- | -- | -- | -- | PASS | +0.2 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1036.0, B 5699.0; serve-point win A 53.1%, B 39.6%; Elo A 1235.7, B 1536.1; model uncertainty 0.0064
* Form inputs: days since last match A 275, B 170; matches on record A 27, B 440; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.006, surface_pool_high +0.006, surface_dev_loose -0.004, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hermans / Wehnelt vs Caripi / Thomson -- M25 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05HERWEHCARTHO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Caripi / Thomson (`KXITFDOUBLES-26NOV05HERWEHCARTHO-CARTHO`) | 0.06 / 0.16 (29) | 11.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hermans / Wehnelt (`KXITFDOUBLES-26NOV05HERWEHCARTHO-HERWEH`) | 0.79 / 0.90 (1) | 84.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ignatov / Serazhetdinov vs Duhan / Murtaza -- M15 Fergana QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05IGNSERDUHMUR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Duhan / Murtaza (`KXITFDOUBLES-26NOV05IGNSERDUHMUR-DUHMUR`) | 0.77 / 0.90 (1) | 83.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ignatov / Serazhetdinov (`KXITFDOUBLES-26NOV05IGNSERDUHMUR-IGNSER`) | 0.06 / 0.18 (30) | 12.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Omar Kandil vs Saba Purtseladze -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208182:214191:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Omar Kandil (`KXITFMATCH-26NOV05KANPUR-KAN`) | 0.06 / 0.14 (7) | 10.0% | 10.8% | 33.5% | 16.0% [14.5%-17.9%] | -- | -- | -- | -- | PASS | +0.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Saba Purtseladze (`KXITFMATCH-26NOV05KANPUR-PUR`) | 0.81 / 0.94 (25) | 87.5% | 89.2% | 66.5% | 84.0% [82.1%-85.5%] | -- | -- | -- | -- | PASS | +1.7 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 45.0, B 3485.0; serve-point win A 58.3%, B 31.8%; Elo A 1251.2, B 1542.5; model uncertainty 0.0169
* Form inputs: days since last match A 46, B 86; matches on record A 2, B 354; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.015, surface_dev_loose -0.002, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yshai Oliel vs Ignacio Parisca -- M25 Valencia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200075:212306:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yshai Oliel (`KXITFMATCH-26NOV05OLIPAR-OLI`) | 0.33 / 0.38 (140) | 35.5% | 41.8% | 12.8% | 41.7% [28.3%-62.3%] | -- | -- | -- | -- | PASS | +6.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ignacio Parisca (`KXITFMATCH-26NOV05OLIPAR-PAR`) | 0.61 / 0.65 (17) | 63.0% | 58.2% | 87.2% | 58.3% [37.7%-71.7%] | -- | -- | -- | -- | PASS | -4.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 703.0, B 1927.0; serve-point win A 57.6%, B 40.8%; Elo A 1449.6, B 1383.1; model uncertainty 0.1701
* Form inputs: days since last match A 359, B 65; matches on record A 433, B 98; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.036, surface_pool_high -0.025, surface_dev_loose -0.010, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jorge Plans vs Sidane Pontjodikromo -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207412:208094:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jorge Plans (`KXITFMATCH-26NOV05PLAPON-PLA`) | 0.05 / 0.93 (50) | 49.0% | 27.7% | 46.4% | 29.9% [27.6%-32.7%] | -- | -- | -- | -- | PASS | -21.3 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Sidane Pontjodikromo (`KXITFMATCH-26NOV05PLAPON-PON`) | 0.05 / 0.94 (25) | 49.5% | 72.3% | 53.6% | 70.0% [67.3%-72.4%] | -- | -- | -- | -- | PASS | +22.8 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1951.0, B 189.0; serve-point win A 58.5%, B 36.8%; Elo A 1273.8, B 1435.8; model uncertainty 0.0256
* Form inputs: days since last match A 205, B 730; matches on record A 54, B 240; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV05PLAPON-PON  (YES = Sidane Pontjodikromo)
Model: 72%
Kalshi: 50%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.009, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matias Reyniak vs Cezar Cretu -- M25 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05REYCRE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cezar Cretu (`KXITFMATCH-26NOV05REYCRE-CRE`) | 0.86 / 0.94 (25) | 90.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matias Reyniak (`KXITFMATCH-26NOV05REYCRE-REY`) | 0.05 / 0.14 (7) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lorenzo Rottoli vs Maxence Bertimon -- M15 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202230:209164:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maxence Bertimon (`KXITFMATCH-26NOV05ROTBER-BER`) | 0.43 / 0.51 (57) | 47.0% | 44.8% | 46.4% | 45.3% [43.3%-46.9%] | -- | -- | -- | -- | PASS | -2.2 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lorenzo Rottoli (`KXITFMATCH-26NOV05ROTBER-ROT`) | 0.46 / 0.57 (23) | 51.5% | 55.2% | 53.6% | 54.7% [53.1%-56.7%] | -- | -- | -- | -- | PASS | +3.7 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2517.0, B 2659.0; serve-point win A 59.4%, B 41.6%; Elo A 1338.7, B 1298.1; model uncertainty 0.0179
* Form inputs: days since last match A 170, B 191; matches on record A 241, B 133; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.015, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luka Talan Lopatic vs Miguel Damas -- M25 Valencia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207732:212589:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miguel Damas (`KXITFMATCH-26NOV05TALDAM-DAM`) | 0.70 / 0.75 (151) | 72.5% | 88.2% | 86.1% | 86.4% [84.8%-87.8%] | -- | -- | -- | -- | PASS | +15.7 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luka Talan Lopatic (`KXITFMATCH-26NOV05TALDAM-TAL`) | 0.22 / 0.25 (33) | 23.5% | 11.8% | 13.9% | 13.6% [12.2%-15.2%] | -- | -- | -- | -- | PASS | -11.7 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 927.0, B 5219.0; serve-point win A 51.7%, B 39.3%; Elo A 1239.8, B 1566.6; model uncertainty 0.0147
* Form inputs: days since last match A 338, B 16; matches on record A 16, B 388; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV05TALDAM-DAM  (YES = Miguel Damas)
Model: 88%
Kalshi: 72%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.003, surface_pool_high +0.000, surface_dev_loose -0.008, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Louis Van Herck vs Pierre Yves Bailly -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206646:210048:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pierre Yves Bailly (`KXITFMATCH-26NOV05VANBAI-BAI`) | 0.83 / 0.93 (22) | 88.0% | 95.0% | 98.8% | 94.9% [90.2%-97.6%] | -- | -- | -- | -- | PASS | +7.0 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Louis Van Herck (`KXITFMATCH-26NOV05VANBAI-VAN`) | 0.07 / 0.17 (8) | 12.0% | 5.0% | 1.2% | 5.1% [2.4%-9.8%] | -- | -- | -- | -- | PASS | -7.0 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 786.0, B 1192.0; serve-point win A 50.2%, B 37.3%; Elo A 1138.7, B 1529.6; model uncertainty 0.0372
* Form inputs: days since last match A 47, B 275; matches on record A 39, B 55; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.007, surface_dev_tight +0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hania Abouelsaad vs Anastasia Efremova -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220394:267540:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hania Abouelsaad (`KXITFWMATCH-26NOV05ABOEFR-ABO`) | 0.55 / 0.59 (1) | 57.0% | 40.1% | 43.6% | 44.1% [43.1%-45.7%] | -- | -- | -- | -- | PASS | -16.9 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anastasia Efremova (`KXITFWMATCH-26NOV05ABOEFR-EFR`) | 0.40 / 0.48 (14) | 44.0% | 59.9% | 56.4% | 55.9% [54.3%-56.9%] | -- | -- | -- | -- | PASS | +15.9 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 897.0, B 611.0; serve-point win A 50.8%, B 47.4%; Elo A 1303.1, B 1345.5; model uncertainty 0.0133
* Form inputs: days since last match A 261, B 205; matches on record A 56, B 14; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05ABOEFR-EFR  (YES = Anastasia Efremova)
Model: 60%
Kalshi: 44%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Coco Bosman vs Luca Kalman -- W15 Szabolcsveresmart R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223421:267645:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Coco Bosman (`KXITFWMATCH-26NOV05BOSKAL-BOS`) | 0.71 / 0.76 (100) | 73.5% | 74.1% | 78.3% | 61.5% [58.4%-65.0%] | -- | -- | -- | -- | PASS | +0.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luca Kalman (`KXITFWMATCH-26NOV05BOSKAL-KAL`) | 0.24 / 0.34 (17) | 29.0% | 25.9% | 21.7% | 38.5% [35.0%-41.6%] | -- | -- | -- | -- | PASS | -3.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2097.0, B 227.0; serve-point win A 58.5%, B 46.4%; Elo A 1352.6, B 1295.2; model uncertainty 0.0329
* Form inputs: days since last match A 191, B 366; matches on record A 69, B 5; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Angela Fita Boluda vs Loes Ebeling Koning -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214236:266901:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Loes Ebeling Koning (`KXITFWMATCH-26NOV05FITEBE-EBE`) | 0.59 / 0.60 (20) | 59.5% | 27.3% | 25.2% | 30.0% [25.6%-34.7%] | -- | -- | -- | -- | PASS | -32.2 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Angela Fita Boluda (`KXITFWMATCH-26NOV05FITEBE-FIT`) | 0.38 / 0.41 (14) | 39.5% | 72.7% | 74.8% | 70.0% [65.3%-74.4%] | -- | -- | -- | -- | PASS | +33.2 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4603.0, B 1642.0; serve-point win A 60.2%, B 44.5%; Elo A 1544.4, B 1444.0; model uncertainty 0.0455
* Form inputs: days since last match A 50, B 23; matches on record A 483, B 87; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05FITEBE-FIT  (YES = Angela Fita Boluda)
Model: 73%
Kalshi: 40%
Gap: +33 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.044, surface_pool_high -0.047, surface_dev_loose +0.018, surface_dev_tight -0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alena Kovackova vs Lenka Munzarova -- W35 Liberec R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222982:266800:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alena Kovackova (`KXITFWMATCH-26NOV05KOVMUN-KOV`) | 0.87 / 0.93 (100) | 90.0% | 96.1% | 82.5% | 85.7% [85.1%-86.3%] | -- | -- | -- | -- | PASS | +6.1 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lenka Munzarova (`KXITFWMATCH-26NOV05KOVMUN-MUN`) | 0.06 / 0.09 (3) | 7.5% | 3.9% | 17.5% | 14.3% [13.7%-14.9%] | -- | -- | -- | -- | PASS | -3.6 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2074.0, B 269.0; serve-point win A 60.3%, B 52.9%; Elo A 1639.8, B 1320.6; model uncertainty 0.006
* Form inputs: days since last match A 212, B 191; matches on record A 72, B 13; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.006, surface_pool_high -0.003, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tereza Krejcova vs Lea Boskovic -- W35 Liberec R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214521:264971:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lea Boskovic (`KXITFWMATCH-26NOV05KREBOS-BOS`) | 0.81 / 0.84 (288) | 82.5% | 91.5% | 64.1% | 81.8% [78.0%-87.4%] | -- | -- | -- | -- | PASS | +9.0 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tereza Krejcova (`KXITFWMATCH-26NOV05KREBOS-KRE`) | 0.14 / 0.17 (23) | 15.5% | 8.5% | 35.9% | 18.2% [12.6%-22.0%] | -- | -- | -- | -- | PASS | -7.0 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 535.0, B 2773.0; serve-point win A 49.3%, B 40.4%; Elo A 1318.4, B 1638.8; model uncertainty 0.0472
* Form inputs: days since last match A 109, B 19; matches on record A 13, B 440; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.018, surface_dev_loose -0.000, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carlota Martinez Cirez vs Nuria Brancaccio -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215572:220781:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nuria Brancaccio (`KXITFWMATCH-26NOV05MARBRA-BRA`) | 0.81 / 0.85 (145) | 83.0% | 71.7% | 70.9% | 67.1% [63.7%-70.0%] | -- | -- | -- | -- | PASS | -11.3 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carlota Martinez Cirez (`KXITFWMATCH-26NOV05MARBRA-MAR`) | 0.13 / 0.14 (22) | 13.5% | 28.3% | 29.1% | 32.9% [30.0%-36.3%] | -- | -- | -- | -- | PASS | +14.8 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3122.0, B 3905.0; serve-point win A 49.1%, B 46.6%; Elo A 1472.5, B 1536.3; model uncertainty 0.0316
* Form inputs: days since last match A 51, B 20; matches on record A 422, B 487; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.029, surface_pool_high +0.030, surface_dev_loose -0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marie Dittmann / Otzipka vs Cascino / Garcia-Perez -- W75 Petange QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05MAROTZCASGAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cascino / Garcia-Perez (`KXITFWDOUBLES-26NOV05MAROTZCASGAR-CASGAR`) | 0.28 / 0.54 (54) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marie Dittmann / Otzipka (`KXITFWDOUBLES-26NOV05MAROTZCASGAR-MAROTZ`) | 0.39 / 0.65 (71) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Kitti Molnar vs Amarissa Kiara Toth -- W15 Szabolcsveresmart R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221004:249667:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kitti Molnar (`KXITFWMATCH-26NOV05MOLTOT-MOL`) | 0.10 / 0.18 (12) | 14.0% | 4.1% | 23.0% | 13.0% [9.5%-16.1%] | -- | -- | -- | -- | PASS | -9.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amarissa Kiara Toth (`KXITFWMATCH-26NOV05MOLTOT-TOT`) | 0.81 / 0.88 (17) | 84.5% | 95.9% | 77.0% | 87.0% [83.9%-90.5%] | -- | -- | -- | -- | PASS | +11.4 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 277.0, B 2701.0; serve-point win A 45.5%, B 41.5%; Elo A 1293.5, B 1647.8; model uncertainty 0.0328
* Form inputs: days since last match A 233, B 205; matches on record A 7, B 265; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.026, surface_pool_high +0.030, surface_dev_loose +0.003, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ngounoue / Ngounoue vs Morderger / Morderger -- W75 Petange QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05NGONGOMORMOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Morderger / Morderger (`KXITFWDOUBLES-26NOV05NGONGOMORMOR-MORMOR`) | 0.10 / 0.32 (36) | 21.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ngounoue / Ngounoue (`KXITFWDOUBLES-26NOV05NGONGOMORMOR-NGONGO`) | 0.61 / 0.84 (156) | 72.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Matilde Paoletti vs Martha Matoula -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213657:222396:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martha Matoula (`KXITFWMATCH-26NOV05PAOMAT-MAT`) | 0.37 / 0.40 (175) | 38.5% | 30.3% | 62.6% | 40.5% [36.4%-44.7%] | -- | -- | -- | -- | PASS | -8.2 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matilde Paoletti (`KXITFWMATCH-26NOV05PAOMAT-PAO`) | 0.57 / 0.62 (128) | 59.5% | 69.7% | 37.4% | 59.6% [55.3%-63.6%] | -- | -- | -- | -- | PASS | +10.2 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 466.0, B 2717.0; serve-point win A 53.9%, B 49.9%; Elo A 1577.0, B 1458.5; model uncertainty 0.0415
* Form inputs: days since last match A 212, B 21; matches on record A 103, B 339; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Raluca Georgiana Serban vs Elena Ruxandra Bertea -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05SERBER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elena Ruxandra Bertea (`KXITFWMATCH-26NOV05SERBER-BER`) | 0.49 / 0.50 (146) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Raluca Georgiana Serban (`KXITFWMATCH-26NOV05SERBER-SER`) | 0.48 / 0.51 (172) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yu Shan vs Irem Kurt -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220031:253681:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Irem Kurt (`KXITFWMATCH-26NOV05SHAKUR-KUR`) | 0.86 / 0.93 (101) | 89.5% | 75.2% | 86.1% | 69.9% [65.6%-76.1%] | -- | -- | -- | -- | PASS | -14.3 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yu Shan (`KXITFWMATCH-26NOV05SHAKUR-SHA`) | 0.05 / 0.09 (3) | 7.0% | 24.8% | 13.9% | 30.1% [23.9%-34.4%] | -- | -- | -- | -- | PASS | +17.8 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 408.0, B 1948.0; serve-point win A 50.5%, B 44.4%; Elo A 1186.3, B 1293.0; model uncertainty 0.0524
* Form inputs: days since last match A 191, B 191; matches on record A 153, B 82; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05SHAKUR-SHA  (YES = Yu Shan)
Model: 25%
Kalshi: 7%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.023, surface_pool_high +0.014, surface_dev_loose -0.014, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anna Snigireva vs Carol Plakk -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216115:263980:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carol Plakk (`KXITFWMATCH-26NOV05SNIPLA-PLA`) | 0.11 / 0.17 (130) | 14.0% | 8.6% | 15.1% | 13.6% [12.0%-14.4%] | -- | -- | -- | -- | PASS | -5.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anna Snigireva (`KXITFWMATCH-26NOV05SNIPLA-SNI`) | 0.82 / 0.89 (20) | 85.5% | 91.5% | 84.9% | 86.4% [85.5%-88.0%] | -- | -- | -- | -- | PASS | +6.0 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1889.0, B 320.0; serve-point win A 52.6%, B 57.7%; Elo A 1441.4, B 1116.8; model uncertainty 0.0121
* Form inputs: days since last match A 191, B 359; matches on record A 86, B 28; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Viktoria Varga vs Ann Akasha Ceuca -- W15 Szabolcsveresmart R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:249669:261097:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ann Akasha Ceuca (`KXITFWMATCH-26NOV05VARCEU-CEU`) | 0.55 / 0.67 (106) | 61.0% | 88.5% | 90.2% | 77.7% [76.5%-80.4%] | -- | -- | -- | -- | PASS | +27.5 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Viktoria Varga (`KXITFWMATCH-26NOV05VARCEU-VAR`) | 0.33 / 0.39 (100) | 36.0% | 11.5% | 9.8% | 22.3% [19.6%-23.5%] | -- | -- | -- | -- | PASS | -24.5 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 139.0, B 2679.0; serve-point win A 48.9%, B 42.2%; Elo A 1251.1, B 1457.1; model uncertainty 0.0193
* Form inputs: days since last match A 366, B 191; matches on record A 14, B 120; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05VARCEU-CEU  (YES = Ann Akasha Ceuca)
Model: 88%
Kalshi: 61%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.000, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## chetouane / Alexandru Teglas vs Corbinais / Penzlin -- M15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05CHEALECORPEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| chetouane / Alexandru Teglas (`KXITFDOUBLES-26NOV05CHEALECORPEN-CHEALE`) | 0.06 / 0.14 (2) | 10.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Corbinais / Penzlin (`KXITFDOUBLES-26NOV05CHEALECORPEN-CORPEN`) | 0.81 / 0.90 (1) | 85.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tuncay Duran vs Nazim Makhlouf -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05DURMAK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tuncay Duran (`KXITFMATCH-26NOV05DURMAK-DUR`) | 0.86 / 0.90 (227) | 88.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nazim Makhlouf (`KXITFMATCH-26NOV05DURMAK-MAK`) | 0.11 / 0.13 (69) | 12.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alejandro Moro Canas vs Mae Malige -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208279:211898:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mae Malige (`KXITFMATCH-26NOV05MORMAL-MAL`) | 0.12 / 0.17 (18) | 14.5% | 23.2% | 28.1% | 27.3% [22.8%-30.4%] | -- | -- | -- | -- | PASS | +8.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alejandro Moro Canas (`KXITFMATCH-26NOV05MORMAL-MOR`) | 0.82 / 0.89 (10) | 85.5% | 76.8% | 71.9% | 72.7% [69.6%-77.2%] | -- | -- | -- | -- | PASS | -8.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5775.0, B 2579.0; serve-point win A 60.1%, B 45.5%; Elo A 1635.1, B 1450.4; model uncertainty 0.0382
* Form inputs: days since last match A 16, B 58; matches on record A 362, B 139; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.031, surface_dev_loose -0.004, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amarni Banks vs Marta Soriano Santiago -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222675:259105:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amarni Banks (`KXITFWMATCH-26NOV05BANSOR-BAN`) | 0.66 / 0.67 (175) | 66.5% | 84.4% | 66.3% | 74.9% [72.3%-77.5%] | -- | -- | -- | -- | PASS | +17.9 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marta Soriano Santiago (`KXITFWMATCH-26NOV05BANSOR-SOR`) | 0.30 / 0.33 (9) | 31.5% | 15.6% | 33.7% | 25.1% [22.5%-27.7%] | -- | -- | -- | -- | PASS | -15.9 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1833.0, B 1358.0; serve-point win A 61.5%, B 46.2%; Elo A 1652.6, B 1390.4; model uncertainty 0.0262
* Form inputs: days since last match A 282, B 191; matches on record A 216, B 98; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05BANSOR-BAN  (YES = Amarni Banks)
Model: 84%
Kalshi: 66%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.008, surface_dev_loose +0.004, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Donnell / Mewett vs Moneva / Srutwa -- W15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05DONMEWMONSRU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Donnell / Mewett (`KXITFWDOUBLES-26NOV05DONMEWMONSRU-DONMEW`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Moneva / Srutwa (`KXITFWDOUBLES-26NOV05DONMEWMONSRU-MONSRU`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sophie Ehrenbergerova vs Nahjime Dho -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05EHRDHO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nahjime Dho (`KXITFWMATCH-26NOV05EHRDHO-DHO`) | 0.52 / 0.55 (135) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sophie Ehrenbergerova (`KXITFWMATCH-26NOV05EHRDHO-EHR`) | 0.42 / 0.43 (3) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Delia Gaillard vs Mariia Lazarenko -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05GAILAZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Delia Gaillard (`KXITFWMATCH-26NOV05GAILAZ-GAI`) | 0.07 / 0.09 (8) | 8.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mariia Lazarenko (`KXITFWMATCH-26NOV05GAILAZ-LAZ`) | 0.87 / 0.91 (13) | 89.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Francesca Gandolfi vs Mailuodi Lei -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260984:264985:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesca Gandolfi (`KXITFWMATCH-26NOV05GANLEI-GAN`) | 0.68 / 0.74 (239) | 71.0% | 88.8% | 57.5% | 73.1% [72.2%-73.1%] | -- | -- | -- | -- | PASS | +17.8 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Mailuodi Lei (`KXITFWMATCH-26NOV05GANLEI-LEI`) | 0.25 / 0.31 (28) | 28.0% | 11.2% | 42.5% | 26.9% [26.9%-27.8%] | -- | -- | -- | -- | PASS | -16.8 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1436.0, B 0.0; serve-point win A 57.2%, B 51.9%; Elo A 1382.7, B 1212.4; model uncertainty 0.0046
* Form inputs: days since last match A 115, B 1122; matches on record A 41, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05GANLEI-GAN  (YES = Francesca Gandolfi)
Model: 89%
Kalshi: 71%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mia Horvit vs Ela Nala Milic -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213551:223308:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mia Horvit (`KXITFWMATCH-26NOV05HORMIL-HOR`) | 0.70 / 0.73 (201) | 71.5% | 44.4% | 50.5% | 52.1% [51.1%-52.7%] | -- | -- | -- | -- | PASS | -27.1 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ela Nala Milic (`KXITFWMATCH-26NOV05HORMIL-MIL`) | 0.28 / 0.32 (137) | 30.0% | 55.6% | 49.5% | 47.9% [47.3%-48.9%] | -- | -- | -- | -- | PASS | +25.6 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1568.0, B 1113.0; serve-point win A 53.5%, B 45.5%; Elo A 1412.5, B 1392.8; model uncertainty 0.008
* Form inputs: days since last match A 261, B 233; matches on record A 110, B 108; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05HORMIL-MIL  (YES = Ela Nala Milic)
Model: 56%
Kalshi: 30%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.005, surface_dev_loose -0.011, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jan-Lennard Struff vs Casper Ruud -- ATP Paris R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-05 18:20Z
* Current expected start: 2026-11-05 16:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: 2026-11-05 15:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-140_MIN

ATP (MASTERS_1000) · Hard · scheduled 2026-11-05T18:20:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26NOV05STRRUU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Casper Ruud (`KXATPMATCH-26NOV05STRRUU-RUU`) | 0.61 / 0.66 (2252) | 63.5% | 69.4% | -- | -- [-----] | -- | 64.8% | -- | INSUFFICIENT_INPUTS | -- | +5.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Jan-Lennard Struff (`KXATPMATCH-26NOV05STRRUU-STR`) | 0.36 / 0.37 (2095) | 36.5% | 30.6% | -- | -- [-----] | -- | 36.2% | 36.2% | MODEL_LONE_OUTLIER | -- | -5.9 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 65.8%, B 29.9%; Elo A 1842.3, B 1951.6; model uncertainty None
* Form inputs: days since last match A 1, B 1; matches on record A 1076, B 721; data quality A
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Burdet / Senn vs Bennani / Yilmaz -- M15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05BURSENBENYIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bennani / Yilmaz (`KXITFDOUBLES-26NOV05BURSENBENYIL-BENYIL`) | 0.26 / 0.51 (51) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Burdet / Senn (`KXITFDOUBLES-26NOV05BURSENBENYIL-BURSEN`) | 0.43 / 0.69 (80) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Chepelev / Fufygin vs Kerem Biberli / Christopher Kucukhuseyin -- M15 Antalya QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05CHEFUFKERCHR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chepelev / Fufygin (`KXITFDOUBLES-26NOV05CHEFUFKERCHR-CHEFUF`) | 0.75 / 0.90 (1) | 82.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kerem Biberli / Christopher Kucukhuseyin (`KXITFDOUBLES-26NOV05CHEFUFKERCHR-KERCHR`) | 0.06 / 0.20 (31) | 13.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Fabre / Tixhon vs Augenti / Saritas -- M15 Antalya QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05FABTIXAUGSAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Augenti / Saritas (`KXITFDOUBLES-26NOV05FABTIXAUGSAR-AUGSAR`) | 0.28 / 0.58 (59) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fabre / Tixhon (`KXITFDOUBLES-26NOV05FABTIXAUGSAR-FABTIX`) | 0.35 / 0.60 (62) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Svyatoslav Gulin vs Enrique Carrascosa Diaz -- M25 Valencia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210425:213766:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Enrique Carrascosa Diaz (`KXITFMATCH-26NOV05GULCAR-CAR`) | 0.06 / 0.17 (109) | 11.5% | 10.7% | 14.1% | 14.0% [12.3%-15.3%] | -- | -- | -- | -- | PASS | -0.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Svyatoslav Gulin (`KXITFMATCH-26NOV05GULCAR-GUL`) | 0.81 / 0.94 (110) | 87.5% | 89.3% | 86.0% | 86.0% [84.7%-87.7%] | -- | -- | -- | -- | PASS | +1.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2956.0, B 922.0; serve-point win A 62.0%, B 47.5%; Elo A 1587.3, B 1270.7; model uncertainty 0.0149
* Form inputs: days since last match A 16, B 254; matches on record A 266, B 17; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.003, surface_pool_high +0.006, surface_dev_loose +0.003, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ifi / Stanke vs Bakshi / Purtseladze -- M15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05IFISTABAKPUR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bakshi / Purtseladze (`KXITFDOUBLES-26NOV05IFISTABAKPUR-BAKPUR`) | 0.31 / 0.58 (59) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ifi / Stanke (`KXITFDOUBLES-26NOV05IFISTABAKPUR-IFISTA`) | 0.36 / 0.63 (67) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Khotchenkov / Yazdani vs Januchowski / Sotikovs -- M15 Antalya QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05KHOYAZJANSOT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Januchowski / Sotikovs (`KXITFDOUBLES-26NOV05KHOYAZJANSOT-JANSOT`) | 0.04 / 0.16 (29) | 10.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Khotchenkov / Yazdani (`KXITFDOUBLES-26NOV05KHOYAZJANSOT-KHOYAZ`) | 0.79 / 0.90 (1) | 84.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kukasian / Plans vs Bocchi / Mugelli -- M15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05KUKPLABOCMUG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bocchi / Mugelli (`KXITFDOUBLES-26NOV05KUKPLABOCMUG-BOCMUG`) | 0.26 / 0.51 (51) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kukasian / Plans (`KXITFDOUBLES-26NOV05KUKPLABOCMUG-KUKPLA`) | 0.43 / 0.69 (80) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Simone Massucco vs Adrian Oetzbach -- M15 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144907:213179:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Simone Massucco (`KXITFMATCH-26NOV05MASOET-MAS`) | 0.17 / 0.21 (25) | 19.0% | 23.8% | 32.4% | 30.1% [29.1%-31.1%] | -- | -- | -- | -- | PASS | +4.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Adrian Oetzbach (`KXITFMATCH-26NOV05MASOET-OET`) | 0.75 / 0.81 (201) | 78.0% | 76.2% | 67.6% | 69.9% [68.9%-70.9%] | -- | -- | -- | -- | PASS | -1.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 69.0, B 3595.0; serve-point win A 55.9%, B 38.6%; Elo A 1245.3, B 1388.5; model uncertainty 0.01
* Form inputs: days since last match A 359, B 191; matches on record A 2, B 303; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Samuele Pieri vs Marcel Zielinski -- M25 Valencia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210129:210505:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Samuele Pieri (`KXITFMATCH-26NOV05PIEZIE-PIE`) | 0.66 / 0.71 (28) | 68.5% | 65.5% | 63.9% | 66.4% [65.4%-68.6%] | -- | -- | -- | -- | PASS | -3.0 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marcel Zielinski (`KXITFMATCH-26NOV05PIEZIE-ZIE`) | 0.26 / 0.30 (135) | 28.0% | 34.5% | 36.1% | 33.6% [31.4%-34.6%] | -- | -- | -- | -- | PASS | +6.5 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3983.0, B 2564.0; serve-point win A 58.2%, B 44.8%; Elo A 1534.6, B 1392.0; model uncertainty 0.016
* Form inputs: days since last match A 16, B 219; matches on record A 208, B 151; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Julio Cesar Porras vs Ivan Gakhov -- M25 Valencia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:123809:210132:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ivan Gakhov (`KXITFMATCH-26NOV05PORGAK-GAK`) | 0.63 / 0.69 (132) | 66.0% | 58.7% | 50.0% | 56.8% [54.2%-62.3%] | -- | -- | -- | -- | PASS | -7.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Julio Cesar Porras (`KXITFMATCH-26NOV05PORGAK-POR`) | 0.31 / 0.35 (31) | 33.0% | 41.3% | 50.0% | 43.2% [37.7%-45.8%] | -- | -- | -- | -- | PASS | +8.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1554.0, B 4154.0; serve-point win A 56.8%, B 41.6%; Elo A 1499.8, B 1590.5; model uncertainty 0.0406
* Form inputs: days since last match A 345, B 30; matches on record A 115, B 857; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.010, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniele Rapagnetta vs Michele Mecarelli -- M15 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212461:213356:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michele Mecarelli (`KXITFMATCH-26NOV05RAPMEC-MEC`) | 0.33 / 0.45 (6) | 39.0% | 54.9% | 53.2% | 54.2% [52.1%-56.8%] | -- | -- | -- | -- | PASS | +15.9 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daniele Rapagnetta (`KXITFMATCH-26NOV05RAPMEC-RAP`) | 0.56 / 0.67 (25) | 61.5% | 45.1% | 46.8% | 45.8% [43.2%-47.9%] | -- | -- | -- | -- | PASS | -16.4 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1887.0, B 981.0; serve-point win A 55.6%, B 43.5%; Elo A 1292.2, B 1326.4; model uncertainty 0.0234
* Form inputs: days since last match A 128, B 86; matches on record A 81, B 23; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV05RAPMEC-MEC  (YES = Michele Mecarelli)
Model: 55%
Kalshi: 39%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.021, surface_dev_loose +0.011, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Leonid Sheyngezikht vs Sergi Perez Contri -- M25 Valencia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:133997:208866:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sergi Perez Contri (`KXITFMATCH-26NOV05SHEPER-PER`) | 0.80 / 0.86 (143) | 83.0% | 85.9% | 90.9% | 87.2% [83.1%-89.5%] | -- | -- | -- | -- | PASS | +2.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Leonid Sheyngezikht (`KXITFMATCH-26NOV05SHEPER-SHE`) | 0.13 / 0.17 (24) | 15.0% | 14.1% | 9.1% | 12.8% [10.4%-16.9%] | -- | -- | -- | -- | PASS | -0.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1472.0, B 3673.0; serve-point win A 49.7%, B 42.3%; Elo A 1212.9, B 1483.0; model uncertainty 0.0323
* Form inputs: days since last match A 219, B 191; matches on record A 130, B 359; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.006, surface_dev_loose -0.013, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Wagner / Yunis vs Basile / Van Der Meerschen -- M15 Antalya QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05WAGYUNBASVAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Basile / Van Der Meerschen (`KXITFDOUBLES-26NOV05WAGYUNBASVAN-BASVAN`) | 0.64 / 0.89 (227) | 76.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Wagner / Yunis (`KXITFDOUBLES-26NOV05WAGYUNBASVAN-WAGYUN`) | 0.05 / 0.29 (35) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Darta Feldmane / Nemcsek vs Breaz / Simionescu -- W15 Antalya QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05DARNEMBRESIM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Breaz / Simionescu (`KXITFWDOUBLES-26NOV05DARNEMBRESIM-BRESIM`) | 0.67 / 0.90 (1) | 78.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Darta Feldmane / Nemcsek (`KXITFWDOUBLES-26NOV05DARNEMBRESIM-DARNEM`) | 0.05 / 0.26 (33) | 15.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Gasparini / Mikhailova vs Kharlanova / Laskutova -- W15 Antalya QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05GASMIKKHALAS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gasparini / Mikhailova (`KXITFWDOUBLES-26NOV05GASMIKKHALAS-GASMIK`) | 0.05 / 0.29 (35) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kharlanova / Laskutova (`KXITFWDOUBLES-26NOV05GASMIKKHALAS-KHALAS`) | 0.64 / 0.89 (227) | 76.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Pistola / Yemshanova vs Iushchenko / Turkmen -- W15 Antalya QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05PISYEMIUSTUR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iushchenko / Turkmen (`KXITFWDOUBLES-26NOV05PISYEMIUSTUR-IUSTUR`) | 0.80 / 0.90 (1) | 85.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pistola / Yemshanova (`KXITFWDOUBLES-26NOV05PISYEMIUSTUR-PISYEM`) | 0.05 / 0.14 (29) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Iva Primorac Pavicic vs Julia Stusek -- W35 Liberec R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206248:260847:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iva Primorac Pavicic (`KXITFWMATCH-26NOV05PRISTU-PRI`) | 0.47 / 0.50 (20) | 48.5% | 41.9% | 36.4% | 44.7% [42.1%-48.9%] | -- | -- | -- | -- | PASS | -6.6 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Julia Stusek (`KXITFWMATCH-26NOV05PRISTU-STU`) | 0.45 / 0.52 (191) | 48.5% | 58.1% | 63.5% | 55.3% [51.1%-57.9%] | -- | -- | -- | -- | PASS | +9.6 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1407.0, B 1952.0; serve-point win A 54.1%, B 44.4%; Elo A 1581.9, B 1557.4; model uncertainty 0.0343
* Form inputs: days since last match A 23, B 59; matches on record A 415, B 74; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.021, surface_dev_loose +0.011, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stamatova / Wirges vs Maria Capuzu / Kartseva -- W15 Antalya QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05STAWIRMARKAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Capuzu / Kartseva (`KXITFWDOUBLES-26NOV05STAWIRMARKAR-MARKAR`) | 0.18 / 0.44 (44) | 31.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stamatova / Wirges (`KXITFWDOUBLES-26NOV05STAWIRMARKAR-STAWIR`) | 0.49 / 0.75 (100) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Anastasia Zhilina vs Karla Popovic -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:210500:259622:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karla Popovic (`KXITFWMATCH-26NOV05ZHIPOP-POP`) | 0.85 / 0.93 (150) | 89.0% | 85.5% | 80.5% | 76.6% [75.7%-78.2%] | -- | -- | -- | -- | PASS | -3.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Anastasia Zhilina (`KXITFWMATCH-26NOV05ZHIPOP-ZHI`) | 0.07 / 0.16 (15) | 11.5% | 14.5% | 19.5% | 23.4% [21.8%-24.3%] | -- | -- | -- | -- | PASS | +3.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 1204.0; serve-point win A 48.1%, B 44.0%; Elo A 1249.1, B 1454.1; model uncertainty 0.0124
* Form inputs: days since last match A 1423, B 191; matches on record A 42, B 82; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.016, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Denisa Zoldakova vs Federica Urgesi -- W35 Liberec R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223415:267616:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Federica Urgesi (`KXITFWMATCH-26NOV05ZOLURG-URG`) | 0.55 / 0.58 (100) | 56.5% | 60.4% | 27.3% | 51.6% [38.9%-67.1%] | -- | -- | -- | -- | PASS | +3.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Denisa Zoldakova (`KXITFWMATCH-26NOV05ZOLURG-ZOL`) | 0.40 / 0.43 (87) | 41.5% | 39.6% | 72.7% | 48.4% [32.9%-61.1%] | -- | -- | -- | -- | PASS | -1.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 870.0, B 2635.0; serve-point win A 51.6%, B 46.4%; Elo A 1456.0, B 1564.6; model uncertainty 0.1409
* Form inputs: days since last match A 49, B 44; matches on record A 20, B 169; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.032, surface_pool_high +0.043, surface_dev_loose +0.043, surface_dev_tight -0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofia Barhacova vs Greta Fenyves -- W15 Szabolcsveresmart R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05BARFEN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Barhacova (`KXITFWMATCH-26NOV05BARFEN-BAR`) | 0.65 / 0.85 (166) | 75.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Greta Fenyves (`KXITFWMATCH-26NOV05BARFEN-FEN`) | 0.10 / 0.30 (35) | 20.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Milena Maria Ciocan vs Alexandra Biot -- W15 Szabolcsveresmart R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260548:270134:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandra Biot (`KXITFWMATCH-26NOV05CIOBIO-BIO`) | 0.31 / 0.35 (5) | 33.0% | 45.0% | 41.5% | 38.9% [36.9%-40.5%] | -- | -- | -- | -- | PASS | +11.9 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Milena Maria Ciocan (`KXITFWMATCH-26NOV05CIOBIO-CIO`) | 0.65 / 0.69 (7) | 67.0% | 55.0% | 58.5% | 61.1% [59.5%-63.1%] | -- | -- | -- | -- | PASS | -11.9 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 217.0, B 177.0; serve-point win A 54.2%, B 46.8%; Elo A 1236.2, B 1157.0; model uncertainty 0.0179
* Form inputs: days since last match A 247, B 191; matches on record A 6, B 50; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Katarina Kuzmova vs Melinda Biro -- W15 Szabolcsveresmart R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221382:267406:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Melinda Biro (`KXITFWMATCH-26NOV05KUZBIR-BIR`) | 0.14 / 0.21 (139) | 17.5% | 3.9% | 10.9% | 9.5% [8.8%-10.0%] | -- | -- | -- | -- | PASS | -13.6 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Katarina Kuzmova (`KXITFWMATCH-26NOV05KUZBIR-KUZ`) | 0.77 / 0.86 (15) | 81.5% | 96.1% | 89.0% | 90.5% [90.0%-91.2%] | -- | -- | -- | -- | PASS | +14.6 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4079.0, B 292.0; serve-point win A 62.8%, B 50.5%; Elo A 1646.6, B 1248.7; model uncertainty 0.0058
* Form inputs: days since last match A 43, B 345; matches on record A 486, B 6; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.004, surface_dev_loose +0.002, surface_dev_tight -0.002
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jessika Ponchet vs Veronika Podrez -- W75 Petange R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211316:247669:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Veronika Podrez (`KXITFWMATCH-26NOV05PONPOD-POD`) | 0.62 / 0.68 (140) | 65.0% | 62.6% | 74.7% | 68.6% [56.8%-73.0%] | -- | -- | -- | -- | PASS | -2.4 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jessika Ponchet (`KXITFWMATCH-26NOV05PONPOD-PON`) | 0.31 / 0.34 (129) | 32.5% | 37.4% | 25.3% | 31.4% [27.0%-43.2%] | -- | -- | -- | -- | PASS | +4.9 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4138.0, B 3466.0; serve-point win A 57.3%, B 40.2%; Elo A 1691.4, B 1719.9; model uncertainty 0.081
* Form inputs: days since last match A 134, B 41; matches on record A 607, B 227; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.009, surface_dev_loose -0.009, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lisa Zaar vs Lea Nilsson -- W75 Petange R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221369:263909:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lea Nilsson (`KXITFWMATCH-26NOV05ZAANIL-NIL`) | 0.42 / 0.47 (11) | 44.5% | 41.1% | 50.5% | 45.2% [37.9%-49.5%] | -- | -- | -- | -- | PASS | -3.4 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lisa Zaar (`KXITFWMATCH-26NOV05ZAANIL-ZAA`) | 0.49 / 0.54 (9) | 51.5% | 58.9% | 49.5% | 54.8% [50.5%-62.1%] | -- | -- | -- | -- | PASS | +7.4 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2200.0, B 1096.0; serve-point win A 51.0%, B 50.7%; Elo A 1528.1, B 1469.5; model uncertainty 0.058
* Form inputs: days since last match A 9, B 121; matches on record A 191, B 33; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.032, surface_pool_high -0.032, surface_dev_loose -0.016, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bothma / Gabet vs Anavatan / Mert Ozdemir -- M15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05BOTGABANAMER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anavatan / Mert Ozdemir (`KXITFDOUBLES-26NOV05BOTGABANAMER-ANAMER`) | 0.46 / 0.73 (92) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bothma / Gabet (`KXITFDOUBLES-26NOV05BOTGABANAMER-BOTGAB`) | 0.16 / 0.47 (47) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Gabriele Crivellaro vs Pietro Marino -- M15 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209233:213927:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriele Crivellaro (`KXITFMATCH-26NOV05CRIMAR-CRI`) | 0.56 / 0.61 (6) | 58.5% | 48.9% | 40.7% | 44.3% [40.2%-47.9%] | -- | -- | -- | -- | PASS | -9.6 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pietro Marino (`KXITFMATCH-26NOV05CRIMAR-MAR`) | 0.39 / 0.41 (100) | 40.0% | 51.1% | 59.3% | 55.7% [52.1%-59.8%] | -- | -- | -- | -- | PASS | +11.1 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 464.0, B 1636.0; serve-point win A 58.6%, B 41.2%; Elo A 1235.5, B 1264.5; model uncertainty 0.0386
* Form inputs: days since last match A 58, B 93; matches on record A 16, B 149; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gianmarco Ferrari vs Jacopo Berrettini -- M15 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202235:208189:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jacopo Berrettini (`KXITFMATCH-26NOV05FERBER-BER`) | 0.44 / 0.51 (27) | 47.5% | 60.4% | 54.1% | 58.2% [56.7%-59.8%] | -- | -- | -- | -- | PASS | +12.8 pp | REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gianmarco Ferrari (`KXITFMATCH-26NOV05FERBER-FER`) | 0.49 / 0.55 (7) | 52.0% | 39.6% | 45.9% | 41.8% [40.2%-43.3%] | -- | -- | -- | -- | PASS | -12.3 pp | REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2506.0, B 3742.0; serve-point win A 58.2%, B 39.8%; Elo A 1474.0, B 1571.4; model uncertainty 0.0153
* Form inputs: days since last match A 58, B 219; matches on record A 294, B 386; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose +0.010, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ganchev / Maes vs Perez Ramos / Wright -- M25 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05GANMAEPERWRI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ganchev / Maes (`KXITFDOUBLES-26NOV05GANMAEPERWRI-GANMAE`) | 0.04 / 0.83 (5) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Perez Ramos / Wright (`KXITFDOUBLES-26NOV05GANMAEPERWRI-PERWRI`) | 0.26 / 0.90 (1) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## G. Capitanio / Tsitsipas vs Neos / Tsitsipas -- M25 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05GCATSINEOTSI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| G. Capitanio / Tsitsipas (`KXITFDOUBLES-26NOV05GCATSINEOTSI-GCATSI`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Neos / Tsitsipas (`KXITFDOUBLES-26NOV05GCATSINEOTSI-NEOTSI`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jones / Jones vs Angelini / Gschwendtner -- M25 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05JONJONANGGSC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Angelini / Gschwendtner (`KXITFDOUBLES-26NOV05JONJONANGGSC-ANGGSC`) | 0.17 / 0.44 (44) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jones / Jones (`KXITFDOUBLES-26NOV05JONJONANGGSC-JONJON`) | 0.49 / 0.76 (104) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## El Sayed / Ezzat vs Moutama / Suslova -- W15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05ELSEZZMOUSUS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| El Sayed / Ezzat (`KXITFWDOUBLES-26NOV05ELSEZZMOUSUS-ELSEZZ`) | 0.80 / 0.90 (1) | 85.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Moutama / Suslova (`KXITFWDOUBLES-26NOV05ELSEZZMOUSUS-MOUSUS`) | 0.05 / 0.14 (29) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Maria Golovina vs Caijsa Wilda Hennemann -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216385:261015:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Golovina (`KXITFWMATCH-26NOV05GOLHEN-GOL`) | 0.26 / 0.33 (37) | 29.5% | 39.3% | 48.9% | 45.7% [35.4%-51.1%] | -- | -- | -- | -- | PASS | +9.8 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Caijsa Wilda Hennemann (`KXITFWMATCH-26NOV05GOLHEN-HEN`) | 0.71 / 0.74 (5) | 72.5% | 60.7% | 51.1% | 54.3% [48.9%-64.6%] | -- | -- | -- | -- | PASS | -11.8 pp | REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2344.0, B 2350.0; serve-point win A 52.5%, B 45.5%; Elo A 1551.0, B 1608.5; model uncertainty 0.0784
* Form inputs: days since last match A 191, B 191; matches on record A 97, B 313; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.042, surface_pool_high +0.053, surface_dev_loose +0.011, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tessa Johanna Brockmann vs Anna-Lena Friedsam -- W75 Petange R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:204431:260598:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tessa Johanna Brockmann (`KXITFWMATCH-26NOV05BROFRI-BRO`) | 0.43 / 0.48 (148) | 45.5% | 46.1% | 55.2% | 49.0% [44.2%-51.6%] | -- | -- | -- | -- | PASS | +0.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anna-Lena Friedsam (`KXITFWMATCH-26NOV05BROFRI-FRI`) | 0.50 / 0.57 (153) | 53.5% | 53.9% | 44.8% | 51.0% [48.4%-55.8%] | -- | -- | -- | -- | PASS | +0.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3426.0, B 3834.0; serve-point win A 58.1%, B 41.1%; Elo A 1598.4, B 1702.3; model uncertainty 0.0367
* Form inputs: days since last match A 22, B 23; matches on record A 169, B 669; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oriana Gniewkowska vs Pia Lovric -- W35 Liberec R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222458:264215:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oriana Gniewkowska (`KXITFWMATCH-26NOV05GNILOV-GNI`) | 0.15 / 0.22 (7) | 18.5% | 14.0% | 22.6% | 21.8% [19.5%-25.1%] | -- | -- | -- | -- | PASS | -4.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pia Lovric (`KXITFWMATCH-26NOV05GNILOV-LOV`) | 0.80 / 0.82 (42) | 81.0% | 86.1% | 77.4% | 78.2% [74.9%-80.5%] | -- | -- | -- | -- | PASS | +5.0 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 810.0, B 1631.0; serve-point win A 44.8%, B 47.2%; Elo A 1310.9, B 1535.5; model uncertainty 0.0279
* Form inputs: days since last match A 387, B 24; matches on record A 34, B 300; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.015, surface_dev_loose -0.011, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mina Hodzic vs Lola Radivojevic -- W75 Petange R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216095:236957:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mina Hodzic (`KXITFWMATCH-26NOV05HODRAD-HOD`) | 0.28 / 0.32 (100) | 30.0% | 30.6% | 26.5% | 29.0% [26.6%-33.3%] | -- | -- | -- | -- | PASS | +0.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lola Radivojevic (`KXITFWMATCH-26NOV05HODRAD-RAD`) | 0.64 / 0.72 (145) | 68.0% | 69.4% | 73.6% | 71.0% [66.7%-73.4%] | -- | -- | -- | -- | PASS | +1.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2700.0, B 3394.0; serve-point win A 58.8%, B 37.3%; Elo A 1489.5, B 1605.3; model uncertainty 0.0335
* Form inputs: days since last match A 22, B 29; matches on record A 288, B 294; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.024, surface_dev_tight +0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Laura Mair vs Elena Milovanovic -- W35 Liberec R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220429:220827:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Laura Mair (`KXITFWMATCH-26NOV05MAIMIL-MAI`) | 0.35 / 0.39 (100) | 37.0% | 53.0% | 41.0% | 45.7% [43.1%-48.9%] | 37.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +16.0 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elena Milovanovic (`KXITFWMATCH-26NOV05MAIMIL-MIL`) | 0.60 / 0.64 (100) | 62.0% | 47.0% | 59.0% | 54.3% [51.1%-56.9%] | 62.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.0 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2387.0, B 2475.0; serve-point win A 54.2%, B 46.4%; Elo A 1460.8, B 1435.0; model uncertainty 0.0292
* Form inputs: days since last match A 7, B 198; matches on record A 243, B 299; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05MAIMIL-MAI  (YES = Laura Mair)
Model: 53%
Kalshi: 37%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.026, surface_pool_high +0.032, surface_dev_loose +0.027, surface_dev_tight -0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matteo Berrettini vs Carlos Alcaraz -- ATP Paris R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-05 21:00Z
* Current expected start: 2026-11-05 18:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: 2026-11-05 17:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (MASTERS_1000) · Hard · scheduled 2026-11-05T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126610:207989:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlos Alcaraz (`KXATPMATCH-26NOV05BERALC-ALC`) | 0.86 / 0.89 (1041) | 87.5% | 85.8% | 87.3% | 87.8% [87.1%-88.0%] | 87.3% | 85.5% | 87.3% | MODEL_LONE_OUTLIER | PASS | -1.7 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Matteo Berrettini (`KXATPMATCH-26NOV05BERALC-BER`) | 0.11 / 0.14 (1739) | 12.5% | 14.2% | 12.7% | 12.2% [12.0%-12.9%] | 12.7% | 15.0% | 12.7% | MODEL_LONE_OUTLIER | PASS | +1.7 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4209.0, B 5572.0; serve-point win A 62.1%, B 29.1%; Elo A 1919.7, B 2267.5; model uncertainty 0.0046
* Form inputs: days since last match A 1, B 3; matches on record A 566, B 481; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.007
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 8 carry a model probability
  * `KXATPEXACTMATCH-26NOV05BERALC-BER20` Will Matteo Berrettini win the Matteo Berrettini vs Carlos Alcaraz match by a set score of 2-0?: 0.02/0.91 mid 46.5%, model 5.6% (projection_v2.0 (prediction ledger)) -- gap -40.9 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05BERALC-BER21` Will Matteo Berrettini win the Matteo Berrettini vs Carlos Alcaraz match by a set score of 2-1?: 0.02/0.91 mid 46.5%, model 8.6% (projection_v2.0 (prediction ledger)) -- gap -37.9 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05BERALC-ALC21` Will Carlos Alcaraz win the Matteo Berrettini vs Carlos Alcaraz match by a set score of 2-1?: 0.01/0.27 mid 14.0%, model 27.6% (projection_v2.0 (prediction ledger)) -- gap +13.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV05BERALC-1-ALC` Will Carlos Alcaraz win set 1 in the Matteo Berrettini vs Carlos Alcaraz match: 0.79/0.84 mid 81.5%, model 76.3% (projection_v2.0 (prediction ledger)) -- gap -5.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV05BERALC-1-BER` Will Matteo Berrettini win set 1 in the Matteo Berrettini vs Carlos Alcaraz match: 0.16/0.21 mid 18.5%, model 23.7% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV05BERALC-2-ALC` Will Carlos Alcaraz win set 2 in the Matteo Berrettini vs Carlos Alcaraz match: 0.79/0.84 mid 81.5%, model 76.3% (projection_v2.0 (prediction ledger)) -- gap -5.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV05BERALC-2-BER` Will Matteo Berrettini win set 2 in the Matteo Berrettini vs Carlos Alcaraz match: 0.16/0.21 mid 18.5%, model 23.7% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05BERALC-ALC20` Will Carlos Alcaraz win the Matteo Berrettini vs Carlos Alcaraz match by a set score of 2-0?: 0.48/0.72 mid 60.0%, model 58.2% (projection_v2.0 (prediction ledger)) -- gap -1.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Abderrahman / Ouakaa vs Nagoudi / Rahmani -- M15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05ABDOUANAGRAH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Abderrahman / Ouakaa (`KXITFDOUBLES-26NOV05ABDOUANAGRAH-ABDOUA`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nagoudi / Rahmani (`KXITFDOUBLES-26NOV05ABDOUANAGRAH-NAGRAH`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ali Abibsi / Mondazzi vs Barsukov / Ehrenschneider -- M15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05ALIMONBAREHR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ali Abibsi / Mondazzi (`KXITFDOUBLES-26NOV05ALIMONBAREHR-ALIMON`) | 0.06 / 0.20 (31) | 13.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Barsukov / Ehrenschneider (`KXITFDOUBLES-26NOV05ALIMONBAREHR-BAREHR`) | 0.75 / 0.90 (1) | 82.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Stepan Baum vs Giuseppe La Vela -- M15 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208153:212068:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stepan Baum (`KXITFMATCH-26NOV05BAULAV-BAU`) | 0.32 / 0.45 (11) | 38.5% | 38.3% | 37.1% | 40.1% [39.1%-40.7%] | -- | -- | -- | -- | PASS | -0.2 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Giuseppe La Vela (`KXITFMATCH-26NOV05BAULAV-LAV`) | 0.59 / 0.65 (171) | 62.0% | 61.7% | 62.9% | 59.9% [59.3%-60.9%] | -- | -- | -- | -- | PASS | -0.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 461.0, B 2431.0; serve-point win A 56.2%, B 41.5%; Elo A 1370.5, B 1436.7; model uncertainty 0.0083
* Form inputs: days since last match A 345, B 44; matches on record A 24, B 183; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.005, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nortey / Sahtali vs Bouchelaghem / van Wyk -- M15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05NORSAHBOUVAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bouchelaghem / van Wyk (`KXITFDOUBLES-26NOV05NORSAHBOUVAN-BOUVAN`) | 0.39 / 0.68 (78) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nortey / Sahtali (`KXITFDOUBLES-26NOV05NORSAHBOUVAN-NORSAH`) | 0.27 / 0.55 (55) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## John Sperle vs Antonio Caruso -- M15 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209206:210145:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Antonio Caruso (`KXITFMATCH-26NOV05SPECAR-CAR`) | 0.15 / 0.18 (13) | 16.5% | 15.7% | 33.1% | 21.0% [20.2%-22.2%] | -- | -- | -- | -- | PASS | -0.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| John Sperle (`KXITFMATCH-26NOV05SPECAR-SPE`) | 0.82 / 0.85 (1) | 83.5% | 84.3% | 66.9% | 79.0% [77.8%-79.8%] | -- | -- | -- | -- | PASS | +0.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2038.0, B 204.0; serve-point win A 60.5%, B 47.2%; Elo A 1418.7, B 1173.6; model uncertainty 0.01
* Form inputs: days since last match A 37, B 415; matches on record A 177, B 37; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.004, surface_dev_loose +0.001, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Babel / Delaunay vs Arcangioli / Cirotte -- W15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05BABDELARCCIR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arcangioli / Cirotte (`KXITFWDOUBLES-26NOV05BABDELARCCIR-ARCCIR`) | 0.71 / 0.90 (1) | 80.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Babel / Delaunay (`KXITFWDOUBLES-26NOV05BABDELARCCIR-BABDEL`) | 0.05 / 0.22 (32) | 13.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Matylda Burylo vs Romane Longueville -- W15 Szabolcsveresmart R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222845:245079:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matylda Burylo (`KXITFWMATCH-26NOV05BURLON-BUR`) | 0.35 / 0.45 (9) | 40.0% | 41.9% | 61.5% | 50.5% [47.9%-53.2%] | -- | -- | -- | -- | PASS | +1.9 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Romane Longueville (`KXITFWMATCH-26NOV05BURLON-LON`) | 0.56 / 0.65 (1) | 60.5% | 58.1% | 38.5% | 49.5% [46.8%-52.1%] | -- | -- | -- | -- | PASS | -2.4 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 498.0, B 1160.0; serve-point win A 54.9%, B 43.5%; Elo A 1246.2, B 1266.8; model uncertainty 0.0265
* Form inputs: days since last match A 247, B 233; matches on record A 42, B 68; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.011, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cassani / Cavelli vs Lizunova / Masiianskaia -- W15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05CASCAVLIZMAS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cassani / Cavelli (`KXITFWDOUBLES-26NOV05CASCAVLIZMAS-CASCAV`) | 0.14 / 0.42 (43) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lizunova / Masiianskaia (`KXITFWDOUBLES-26NOV05CASCAVLIZMAS-LIZMAS`) | 0.51 / 0.79 (119) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Chiesa / Pedone vs Grammatikopoulou / Yardley -- W50 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05CHIPEDGRAYAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chiesa / Pedone (`KXITFWDOUBLES-26NOV05CHIPEDGRAYAR-CHIPED`) | 0.52 / 0.89 (1) | 70.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Grammatikopoulou / Yardley (`KXITFWDOUBLES-26NOV05CHIPEDGRAYAR-GRAYAR`) | 0.08 / 0.48 (1) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Fernandez / Garcia-Patron Canals vs Fusil / Husar -- W15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05FERGARFUSHUS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fernandez / Garcia-Patron Canals (`KXITFWDOUBLES-26NOV05FERGARFUSHUS-FERGAR`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fusil / Husar (`KXITFWDOUBLES-26NOV05FERGARFUSHUS-FUSHUS`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lea Fojcik vs Emese Serkedi -- W15 Szabolcsveresmart R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05FOJSER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lea Fojcik (`KXITFWMATCH-26NOV05FOJSER-FOJ`) | 0.31 / 0.38 (100) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Emese Serkedi (`KXITFWMATCH-26NOV05FOJSER-SER`) | 0.56 / 0.69 (26) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pawelska / Rabl vs Georgiana Goina / Molnar -- W15 Szabolcsveresmart QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05PAWRABGEOMOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Georgiana Goina / Molnar (`KXITFWDOUBLES-26NOV05PAWRABGEOMOL-GEOMOL`) | 0.30 / 0.60 (62) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pawelska / Rabl (`KXITFWDOUBLES-26NOV05PAWRABGEOMOL-PAWRAB`) | 0.32 / 0.63 (67) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Stoyanov / Yesypchuk vs Lilly Sophie Steur / Van Emst -- W50 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05STOYESLILVAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lilly Sophie Steur / Van Emst (`KXITFWDOUBLES-26NOV05STOYESLILVAN-LILVAN`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stoyanov / Yesypchuk (`KXITFWDOUBLES-26NOV05STOYESLILVAN-STOYES`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Svatikova / Tichackova vs Allen / Karatancheva -- W50 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05SVATICALLKAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Allen / Karatancheva (`KXITFWDOUBLES-26NOV05SVATICALLKAR-ALLKAR`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Svatikova / Tichackova (`KXITFWDOUBLES-26NOV05SVATICALLKAR-SVATIC`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Barroso Campos / Pujol Navarro vs Naharro / Talan Lopatic -- M25 Valencia SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05BARPUJNAHTAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barroso Campos / Pujol Navarro (`KXITFDOUBLES-26NOV05BARPUJNAHTAL-BARPUJ`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Naharro / Talan Lopatic (`KXITFDOUBLES-26NOV05BARPUJNAHTAL-NAHTAL`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Milev / Parisca vs Garcia Carbajal / Mansilla Diez -- M25 Valencia SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05MILPARGARMAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Garcia Carbajal / Mansilla Diez (`KXITFDOUBLES-26NOV05MILPARGARMAN-GARMAN`) | 0.41 / 0.68 (78) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Milev / Parisca (`KXITFDOUBLES-26NOV05MILPARGARMAN-MILPAR`) | 0.27 / 0.53 (53) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Berta Bonardi vs Sol Ailin Larraya Guidi -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05BONLAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Berta Bonardi (`KXITFWMATCH-26NOV05BONLAR-BON`) | 0.30 / 0.34 (37) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sol Ailin Larraya Guidi (`KXITFWMATCH-26NOV05BONLAR-LAR`) | 0.61 / 0.71 (9) | 66.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Victoria Bosio vs Sofia Meabe -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05BOSMEA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Victoria Bosio (`KXITFWMATCH-26NOV05BOSMEA-BOS`) | 0.80 / 0.93 (5) | 86.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sofia Meabe (`KXITFWMATCH-26NOV05BOSMEA-MEA`) | 0.05 / 0.15 (29) | 10.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Manon Leonard vs Weronika Ewald -- W35 Liberec R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05LEOEWA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Weronika Ewald (`KXITFWMATCH-26NOV05LEOEWA-EWA`) | 0.33 / 0.36 (24) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Manon Leonard (`KXITFWMATCH-26NOV05LEOEWA-LEO`) | 0.63 / 0.66 (3) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Florencia Belen Moron vs Camila Romero -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05MORROM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Florencia Belen Moron (`KXITFWMATCH-26NOV05MORROM-MOR`) | 0.04 / 0.05 (158) | 4.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Camila Romero (`KXITFWMATCH-26NOV05MORROM-ROM`) | 0.93 / 0.95 (5) | 94.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valentina Ryser vs Josy Daems -- W35 Liberec R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05RYSDAE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Josy Daems (`KXITFWMATCH-26NOV05RYSDAE-DAE`) | 0.28 / 0.32 (28) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Valentina Ryser (`KXITFWMATCH-26NOV05RYSDAE-RYS`) | 0.68 / 0.70 (100) | 69.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arthur Fils vs Taylor Fritz -- ATP Paris R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-05 22:30Z
* Current expected start: 2026-11-05 19:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-04 22:41Z
* Recommended handicap-by time: 2026-11-05 18:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (MASTERS_1000) · surface ? · scheduled 2026-11-05T22:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26NOV05FILFRI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arthur Fils (`KXATPMATCH-26NOV05FILFRI-FIL`) | 0.44 / 0.49 (19) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Taylor Fritz (`KXATPMATCH-26NOV05FILFRI-FRI`) | 0.50 / 0.54 (2000) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Biot / Boron vs Kalman / Mihalka -- W15 Szabolcsveresmart QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05BIOBORKALMIH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Biot / Boron (`KXITFWDOUBLES-26NOV05BIOBORKALMIH-BIOBOR`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kalman / Mihalka (`KXITFWDOUBLES-26NOV05BIOBORKALMIH-KALMIH`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Biro / Marlies Rothensteiner vs Kardos / Salaiova -- W15 Szabolcsveresmart QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05BIRMARKARSAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Biro / Marlies Rothensteiner (`KXITFWDOUBLES-26NOV05BIRMARKARSAL-BIRMAR`) | 0.66 / 0.90 (1) | 78.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kardos / Salaiova (`KXITFWDOUBLES-26NOV05BIRMARKARSAL-KARSAL`) | 0.05 / 0.27 (34) | 16.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Fenyves / Vlajic vs Bosman / Akasha Ceuca -- W15 Szabolcsveresmart QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05FENVLABOSAKA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bosman / Akasha Ceuca (`KXITFWDOUBLES-26NOV05FENVLABOSAKA-BOSAKA`) | 0.51 / 0.79 (119) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fenyves / Vlajic (`KXITFWDOUBLES-26NOV05FENVLABOSAKA-FENVLA`) | 0.14 / 0.42 (43) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Appleton / Zaar vs Dal / Judith Visscher -- W75 Petange QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05APPZAADALJUD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Appleton / Zaar (`KXITFWDOUBLES-26NOV05APPZAADALJUD-APPZAA`) | 0.44 / 0.76 (33) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dal / Judith Visscher (`KXITFWDOUBLES-26NOV05APPZAADALJUD-DALJUD`) | 0.30 / 0.41 (42) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Melissa Boyden vs Fernanda Labrana -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05BOYLAB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Melissa Boyden (`KXITFWMATCH-26NOV05BOYLAB-BOY`) | 0.04 / 0.05 (27) | 4.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fernanda Labrana (`KXITFWMATCH-26NOV05BOYLAB-LAB`) | 0.90 / 0.96 (90) | 93.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luciana Moyano vs Alisa Danilova -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05MOYDAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alisa Danilova (`KXITFWMATCH-26NOV05MOYDAN-DAN`) | 0.06 / 0.93 (50) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luciana Moyano (`KXITFWMATCH-26NOV05MOYDAN-MOY`) | 0.07 / 0.94 (10) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Antonia Vergara Rivera vs Zoe Doldan -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05VERDOL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zoe Doldan (`KXITFWMATCH-26NOV05VERDOL-DOL`) | 0.06 / 0.19 (15) | 12.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Antonia Vergara Rivera (`KXITFWMATCH-26NOV05VERDOL-VER`) | 0.81 / 0.93 (5) | 87.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Charvatova / Munzarova vs Kovackova / Krejcova -- W35 Liberec QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05CHAMUNKOVKRE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charvatova / Munzarova (`KXITFWDOUBLES-26NOV05CHAMUNKOVKRE-CHAMUN`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kovackova / Krejcova (`KXITFWDOUBLES-26NOV05CHAMUNKOVKRE-KOVKRE`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dalma Galfi vs Amandine Hesse -- W75 Petange R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05GALHES:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dalma Galfi (`KXITFWMATCH-26NOV05GALHES-GAL`) | 0.73 / 0.80 (46) | 76.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Amandine Hesse (`KXITFWMATCH-26NOV05GALHES-HES`) | 0.18 / 0.25 (26) | 21.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Justine Hejtmanek / Sucha vs Chytilova / Hsu -- W35 Liberec QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05JUSSUCCHYHSU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chytilova / Hsu (`KXITFWDOUBLES-26NOV05JUSSUCCHYHSU-CHYHSU`) | 0.05 / 0.08 (27) | 6.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Justine Hejtmanek / Sucha (`KXITFWDOUBLES-26NOV05JUSSUCCHYHSU-JUSSUC`) | 0.86 / 0.93 (1) | 89.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
