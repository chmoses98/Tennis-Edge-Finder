# ASSISTED SLATE -- 2026-11-10T18:21Z (`SL-20261110T182103Z-ab841816`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

371 open matches not seen started, 820 markets. Skipped: {"first_ball_already_observed": 4, "scheduled_start_over_24h_past": 10}. Sources: shadow board 2026-11-10T18:00:33.719298+00:00, Model 4 2026-11-10T18:02:09.753428+00:00, Gen-1 ledger 2026-11-10T18:00:29.068767+00:00, external 2026-11-10T17:29:29.559126+00:00, capture 20261110T172614Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-11-10 18:26Z**
* Recommended RUN TENNIS time: **2026-11-10 17:41Z**  (**OVERDUE -- run now**)
* Final price/status check time: **2026-11-10 18:16Z**
* Number of matches in window: 1 (Lorenzo Musetti vs Toby Samuel)

* **4 main-tour match(es) have NO verified start status** (START_UNKNOWN): BET blocked until a live status check.

Slate built 2026-11-10T18:21Z. Refresh due by: 2026-11-10 17:41Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 69, "HIGH_REVIEW": 117, "NORMAL": 259, "REVIEW": 86, "UNPRICED": 289}; match winners: {"EXTREME": 67, "HIGH_REVIEW": 111, "NORMAL": 206, "REVIEW": 74, "UNPRICED": 284}; quote freshness at build: {"STALE": 531}.

## James McCabe vs Jan Kumstat -- ATP Challenger Brisbane 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 03:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210317:211618:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jan Kumstat (`KXATPCHALLENGERMATCH-26NOV09MCCKUM-KUM`) | 0.64 / 0.66 (4782) | 65.0% | 68.1% | 66.1% | 63.0% [59.4%-67.4%] | -- | -- | -- | -- | PASS | +3.1 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| James McCabe (`KXATPCHALLENGERMATCH-26NOV09MCCKUM-MCC`) | 0.34 / 0.35 (663) | 34.5% | 31.9% | 33.9% | 37.0% [32.6%-40.6%] | -- | -- | -- | -- | PASS | -2.6 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4552.0, B 3055.0; serve-point win A 66.7%, B 29.3%; Elo A 1579.4, B 1631.9; model uncertainty 0.0401
* Form inputs: days since last match A 7, B 7; matches on record A 336, B 89; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.044, surface_pool_high +0.036, surface_dev_loose +0.010, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE

## Jean-Julien Rojer / Theodore Winegar vs William Rejchtman Vinciguerra / Olle Wallin -- ATP Stockholm 1/8 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-10 17:21Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-11T05:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-10T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10ROJWINREJWAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| William Rejchtman Vinciguerra / Olle Wallin (`KXATPDOUBLES-26NOV10ROJWINREJWAL-REJWAL`) | 0.07 / 0.11 (0) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jean-Julien Rojer / Theodore Winegar (`KXATPDOUBLES-26NOV10ROJWINREJWAL-ROJWIN`) | 0.89 / 0.91 (5) | 90.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Carlo Alberto Caniato vs Gilles Arnaud Bailly -- ATP Challenger Hersonissos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211451:212241:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gilles Arnaud Bailly (`KXATPCHALLENGERMATCH-26NOV10CANARN-ARN`) | 0.04 / 0.05 (16318) | 4.5% | 41.3% | 32.7% | 39.7% [36.9%-45.5%] | 37.5% | 36.9% | 36.9% | MODEL_LONE_OUTLIER | WATCH | +36.8 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Carlo Alberto Caniato (`KXATPCHALLENGERMATCH-26NOV10CANARN-CAN`) | 0.95 / 0.96 (34867) | 95.5% | 58.7% | 67.3% | 60.3% [54.5%-63.1%] | 62.5% | 62.9% | 62.9% | MODEL_LONE_OUTLIER | PASS | -36.8 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3539.0, B 3897.0; serve-point win A 65.3%, B 36.4%; Elo A 1462.2, B 1517.4; model uncertainty 0.0433
* Form inputs: days since last match A 22, B 24; matches on record A 154, B 212; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV10CANARN-ARN  (YES = Gilles Arnaud Bailly)
Model: 41%
Kalshi: 4%
Gap: +37 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: EXTERNAL_STALE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.010, surface_dev_loose +0.009, surface_dev_tight -0.019
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Andrej Nedic vs Michele Ribecai -- ATP Challenger Hersonissos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T15:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210119:212020:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrej Nedic (`KXATPCHALLENGERMATCH-26NOV10NEDRIB-NED`) | 0.31 / 0.34 (54) | 32.5% | 45.5% | 42.7% | 45.3% [43.2%-46.9%] | 35.4% | -- | 35.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +12.9 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Michele Ribecai (`KXATPCHALLENGERMATCH-26NOV10NEDRIB-RIB`) | 0.65 / 0.69 (168) | 67.0% | 54.5% | 57.3% | 54.7% [53.1%-56.8%] | 64.6% | -- | 64.6% | MODEL_LONE_OUTLIER | PASS | -12.4 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4081.0, B 4673.0; serve-point win A 56.5%, B 42.6%; Elo A 1548.9, B 1536.3; model uncertainty 0.0183
* Form inputs: days since last match A 22, B 22; matches on record A 236, B 191; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.011, surface_dev_loose -0.021, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STALE_QUOTE

## Radu Mihai Papoe vs Philip Henning -- ATP Challenger Hersonissos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T15:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202475:208457:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Philip Henning (`KXATPCHALLENGERMATCH-26NOV10PAPHEN-HEN`) | 0.87 / 0.88 (1) | 87.5% | 55.5% | 65.3% | 62.3% [57.8%-65.3%] | 57.2% | -- | 57.2% | KALSHI_LONE_OUTLIER | PASS | -32.0 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Radu Mihai Papoe (`KXATPCHALLENGERMATCH-26NOV10PAPHEN-PAP`) | 0.11 / 0.13 (1547) | 12.0% | 44.5% | 34.7% | 37.7% [34.7%-42.2%] | 42.8% | -- | 42.8% | KALSHI_LONE_OUTLIER | WATCH | +32.5 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 2539.0, B 3868.0; serve-point win A 57.8%, B 41.1%; Elo A 1543.1, B 1598.6; model uncertainty 0.0376
* Form inputs: days since last match A 22, B 29; matches on record A 182, B 215; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV10PAPHEN-PAP  (YES = Radu Mihai Papoe)
Model: 45%
Kalshi: 12%
Gap: +33 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_MODEL
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.029, surface_dev_loose -0.000, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Zsombor Piros vs Luca Nardi -- ATP Challenger Orleans R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200436:208134:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luca Nardi (`KXATPCHALLENGERMATCH-26NOV10PIRNAR-NAR`) | -- / 0.01 (125444) | -- | 43.9% | 43.9% | 45.4% [41.9%-47.5%] | 52.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | STALE | A / ADEQUATE | INSUFFICIENT_INPUTS | VERIFIED |
| Zsombor Piros (`KXATPCHALLENGERMATCH-26NOV10PIRNAR-PIR`) | 0.99 / -- (0) | -- | 56.1% | 56.1% | 54.6% [52.5%-58.1%] | 48.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | STALE | A / ADEQUATE | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 5512.0, B 4120.0; serve-point win A 62.5%, B 38.8%; Elo A 1703.4, B 1692.9; model uncertainty 0.0277
* Form inputs: days since last match A 8, B 29; matches on record A 564, B 380; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.020, surface_dev_loose -0.005, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE

## Sebastian Baez vs Daniil Glinka -- ATP Challenger Orleans R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T16:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202104:206750:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sebastian Baez (`KXATPCHALLENGERMATCH-26NOV10BAEGLI-BAE`) | 0.72 / 0.73 (28474) | 72.5% | 52.5% | 38.9% | 43.4% [39.4%-51.5%] | -- | 50.4% | 50.4% | MODEL_LONE_OUTLIER | PASS | -20.0 pp | HIGH_REVIEW | STALE | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Daniil Glinka (`KXATPCHALLENGERMATCH-26NOV10BAEGLI-GLI`) | 0.27 / 0.28 (86213) | 27.5% | 47.5% | 61.1% | 56.6% [48.5%-60.6%] | -- | 49.4% | 49.4% | MODEL_LONE_OUTLIER | WATCH | +20.0 pp | HIGH_REVIEW | STALE | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 5268.0, B 5152.0; serve-point win A 61.4%, B 39.1%; Elo A 1709.8, B 1648.5; model uncertainty 0.0607
* Form inputs: days since last match A 8, B 15; matches on record A 509, B 387; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV10BAEGLI-GLI  (YES = Daniil Glinka)
Model: 48%
Kalshi: 28%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_MODEL
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.030, surface_pool_high -0.030, surface_dev_loose -0.020, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STALE_QUOTE

## Katrina Scott vs Andrea Lazaro Garcia -- WTA Challenger Sopo R32

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-11-10 19:10Z
* Current expected start: 2026-11-10 17:20Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-10 17:21Z
* Recommended handicap-by time: 2026-11-10 16:35Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA125 (CHALLENGER) · surface ? · scheduled 2026-11-10T19:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26NOV10SCOLAZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrea Lazaro Garcia (`KXWTACHALLENGERMATCH-26NOV10SCOLAZ-LAZ`) | 0.80 / 0.81 (4576) | 80.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Katrina Scott (`KXWTACHALLENGERMATCH-26NOV10SCOLAZ-SCO`) | 0.19 / 0.20 (7082) | 19.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; STATUS_AMBIGUOUS; NO_EXTERNAL_PRICE; STALE_QUOTE

## Duje Ajdukovic vs Moez Echargui -- ATP Challenger Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 17:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T17:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:121411:207213:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Duje Ajdukovic (`KXATPCHALLENGERMATCH-26NOV10AJDECH-AJD`) | 0.35 / 0.36 (20029) | 35.5% | 51.0% | 47.0% | 46.0% [44.9%-47.0%] | -- | 44.5% | 44.5% | MODEL_LONE_OUTLIER | SHADOW_BET | +15.5 pp | HIGH_REVIEW | STALE | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Moez Echargui (`KXATPCHALLENGERMATCH-26NOV10AJDECH-ECH`) | 0.64 / 0.65 (14882) | 64.5% | 49.0% | 53.0% | 54.0% [53.0%-55.1%] | -- | 55.6% | 55.6% | MODEL_LONE_OUTLIER | PASS | -15.5 pp | HIGH_REVIEW | STALE | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 4622.0, B 4631.0; serve-point win A 62.5%, B 37.7%; Elo A 1549.1, B 1595.1; model uncertainty 0.0101
* Form inputs: days since last match A 36, B 15; matches on record A 479, B 656; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV10AJDECH-AJD  (YES = Duje Ajdukovic)
Model: 51%
Kalshi: 36%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: SUPPORTS_MODEL_DIRECTION
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STALE_QUOTE

## Marvin Moeller vs Nikolai Barsukov -- ATP Challenger Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 17:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T17:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202359:213062:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikolai Barsukov (`KXATPCHALLENGERMATCH-26NOV10MOEBAR-BAR`) | 0.10 / 0.11 (33610) | 10.5% | 21.1% | 20.2% | 20.5% [19.5%-21.6%] | -- | 33.5% | 33.5% | MODEL_LONE_OUTLIER | WATCH | +10.6 pp | REVIEW | STALE | C / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Marvin Moeller (`KXATPCHALLENGERMATCH-26NOV10MOEBAR-MOE`) | 0.89 / 0.90 (38961) | 89.5% | 78.9% | 79.8% | 79.5% [78.4%-80.5%] | -- | 66.9% | 66.9% | MODEL_LONE_OUTLIER | PASS | -10.6 pp | REVIEW | STALE | C / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 5348.0, B 2385.0; serve-point win A 65.5%, B 40.8%; Elo A 1597.8, B 1366.9; model uncertainty 0.0108
* Form inputs: days since last match A 29, B 197; matches on record A 405, B 48; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose -0.004, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; STALE_QUOTE

## Mika Petkovic vs Gianluca Cadenasso -- ATP Challenger Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 17:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T17:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211533:213001:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gianluca Cadenasso (`KXATPCHALLENGERMATCH-26NOV10PETCAD-CAD`) | 0.61 / 0.63 (7320) | 62.0% | 64.3% | 63.7% | 65.2% [63.3%-67.5%] | 61.6% | -- | 61.6% | MODEL_LONE_OUTLIER | WATCH | +2.3 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Mika Petkovic (`KXATPCHALLENGERMATCH-26NOV10PETCAD-PET`) | 0.37 / 0.39 (0) | 38.0% | 35.7% | 36.3% | 34.8% [32.5%-36.7%] | 38.4% | -- | 38.4% | MODEL_LONE_OUTLIER | PASS | -2.3 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3316.0, B 3346.0; serve-point win A 57.8%, B 39.4%; Elo A 1441.2, B 1566.3; model uncertainty 0.0213
* Form inputs: days since last match A 43, B 22; matches on record A 102, B 177; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.010, surface_dev_loose +0.019, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Bianca Andreescu vs Rebeka Masarova -- WTA Challenger Sopo R32

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-11-10 19:10Z
* Current expected start: 2026-11-10 17:35Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-10 17:21Z
* Recommended handicap-by time: 2026-11-10 16:50Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA125 (CHALLENGER) · surface ? · scheduled 2026-11-10T19:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26NOV10ANDMAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bianca Andreescu (`KXWTACHALLENGERMATCH-26NOV10ANDMAS-AND`) | 0.75 / 0.76 (5515) | 75.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rebeka Masarova (`KXWTACHALLENGERMATCH-26NOV10ANDMAS-MAS`) | 0.25 / 0.26 (14352) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; STATUS_AMBIGUOUS; NO_EXTERNAL_PRICE; STALE_QUOTE

## Shintaro Mochizuki vs Calvin Hemery -- ATP Challenger Orleans R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 17:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T17:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:123921:208278:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Calvin Hemery (`KXATPCHALLENGERMATCH-26NOV10MOCHEM-HEM`) | 0.42 / 0.43 (39) | 42.5% | 35.7% | 49.0% | 45.4% [42.4%-47.4%] | -- | 43.7% | 43.7% | MARKETS_AGREE | WATCH | -6.8 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Shintaro Mochizuki (`KXATPCHALLENGERMATCH-26NOV10MOCHEM-MOC`) | 0.57 / 0.58 (1041) | 57.5% | 64.3% | 51.0% | 54.6% [52.6%-57.6%] | -- | 56.2% | 56.2% | MARKETS_AGREE | PASS | +6.8 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5013.0, B 4976.0; serve-point win A 62.3%, B 40.6%; Elo A 1650.0, B 1549.6; model uncertainty 0.0255
* Form inputs: days since last match A 8, B 22; matches on record A 456, B 754; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STALE_QUOTE

## Lui Maxted vs Hynek Barton -- ATP Challenger Knoxville R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210558:210747:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hynek Barton (`KXATPCHALLENGERMATCH-26NOV10MAXBAR-BAR`) | 0.07 / 0.09 (135) | 8.0% | 53.7% | 43.5% | 48.5% [45.0%-59.5%] | 42.8% | 41.9% | 41.9% | MODEL_LONE_OUTLIER | WATCH | +45.7 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | EXTERNAL_STALE | VERIFIED |
| Lui Maxted (`KXATPCHALLENGERMATCH-26NOV10MAXBAR-MAX`) | 0.91 / 0.93 (172) | 92.0% | 46.3% | 56.5% | 51.5% [40.5%-55.0%] | 57.2% | 58.2% | 58.2% | MODEL_LONE_OUTLIER | PASS | -45.7 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 2751.0, B 5420.0; serve-point win A 62.7%, B 36.5%; Elo A 1553.0, B 1609.2; model uncertainty 0.0723
* Form inputs: days since last match A 246, B 15; matches on record A 70, B 273; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV10MAXBAR-BAR  (YES = Hynek Barton)
Model: 54%
Kalshi: 8%
Gap: +46 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: EXTERNAL_STALE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Daniel Rincon vs Santiago De la Fuente -- ATP Challenger Lima R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-10T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208099:209405:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Santiago De la Fuente (`KXATPCHALLENGERMATCH-26NOV10RINDLF-DLF`) | 0.05 / 0.07 (13983) | 6.0% | 16.0% | 20.6% | 17.8% [16.2%-19.2%] | 20.8% | -- | 20.8% | MARKETS_AGREE | SHADOW_BET | +10.0 pp | NORMAL | STALE | B / LIMITED | AGREES_WITH_MODEL | VERIFIED |
| Daniel Rincon (`KXATPCHALLENGERMATCH-26NOV10RINDLF-RIN`) | 0.93 / 0.94 (1194) | 93.5% | 84.0% | 79.4% | 82.2% [80.8%-83.8%] | 79.2% | -- | 79.2% | MARKETS_AGREE | PASS | -9.5 pp | NORMAL | STALE | B / LIMITED | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 5169.0, B 2660.0; serve-point win A 60.3%, B 47.2%; Elo A 1654.3, B 1338.9; model uncertainty 0.0146
* Form inputs: days since last match A 29, B 148; matches on record A 360, B 136; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.007, surface_dev_loose +0.007, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STALE_QUOTE

## Lorenzo Musetti vs Toby Samuel -- ATP Stockholm R16

**START STATUS: START_IMMINENT** -- BET BLOCKED
* Nominal schedule: 2026-11-10 21:10Z
* Current expected start: 2026-11-10 18:26Z
* Source: COURT_PROGRESSION: preceding match on Center Court in progress (set 1 of best-of-5); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-10 17:21Z
* Recommended handicap-by time: 2026-11-10 17:41Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-164_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-11-10T21:10:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207518:210389:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Musetti (`KXATPMATCH-26NOV10MUSSAM-MUS`) | 0.77 / 0.78 (8542) | 77.5% | 69.3% | 50.5% | 56.5% [51.0%-66.0%] | 75.5% | 77.6% | 76.5% | MODEL_LONE_OUTLIER | PASS | -8.2 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Toby Samuel (`KXATPMATCH-26NOV10MUSSAM-SAM`) | 0.22 / 0.23 (56442) | 22.5% | 30.7% | 49.5% | 43.5% [34.0%-49.0%] | 24.5% | 22.5% | 23.5% | MODEL_LONE_OUTLIER | WATCH | +8.2 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5369.0, B 4150.0; serve-point win A 66.0%, B 38.0%; Elo A 1960.0, B 1800.9; model uncertainty 0.0749
* Form inputs: days since last match A 5, B 1; matches on record A 493, B 197; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.039, surface_pool_high -0.040, surface_dev_loose -0.015, surface_dev_tight +0.020
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV10MUSSAM-23` Over 22.5 games: 0.42/0.44 mid 43.0%, model 57.7% (projection_v2.0 (prediction ledger)) -- gap +14.7 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10MUSSAM-MUS20` Will Lorenzo Musetti win the Lorenzo Musetti vs Toby Samuel match by a set score of 2-0?: 0.53/0.56 mid 54.5%, model 39.9% (projection_v2.0 (prediction ledger)) -- gap -14.6 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV10MUSSAM-MUS4` Will Lorenzo Musetti win at least 3.5 more games than Toby Samuel?: 0.56/0.58 mid 57.0%, model 42.9% (projection_v2.0 (prediction ledger)) -- gap -14.1 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV10MUSSAM-MUS7` Will Lorenzo Musetti win at least 6.5 more games than Toby Samuel?: 0.17/0.22 mid 19.5%, model 8.4% (projection_v2.0 (prediction ledger)) -- gap -11.1 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV10MUSSAM-18` Over 17.5 games: 0.82/0.85 mid 83.5%, model 92.1% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV10MUSSAM-28` Over 27.5 games: 0.30/0.31 mid 30.5%, model 37.9% (projection_v2.0 (prediction ledger)) -- gap +7.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV10MUSSAM-2-MUS` Will Lorenzo Musetti win set 2 in the Lorenzo Musetti vs Toby Samuel match: 0.70/0.71 mid 70.5%, model 63.2% (projection_v2.0 (prediction ledger)) -- gap -7.3 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV10MUSSAM-2-SAM` Will Toby Samuel win set 2 in the Lorenzo Musetti vs Toby Samuel match: 0.29/0.30 mid 29.5%, model 36.8% (projection_v2.0 (prediction ledger)) -- gap +7.3 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10MUSSAM-SAM21` Will Toby Samuel win the Lorenzo Musetti vs Toby Samuel match by a set score of 2-1?: 0.09/0.11 mid 10.0%, model 17.1% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10MUSSAM-MUS21` Will Lorenzo Musetti win the Lorenzo Musetti vs Toby Samuel match by a set score of 2-1?: 0.22/0.24 mid 23.0%, model 29.4% (projection_v2.0 (prediction ledger)) -- gap +6.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV10MUSSAM-1-MUS` Will Lorenzo Musetti win set 1 in the Lorenzo Musetti vs Toby Samuel match: 0.68/0.71 mid 69.5%, model 63.2% (projection_v2.0 (prediction ledger)) -- gap -6.3 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV10MUSSAM-1-SAM` Will Toby Samuel win set 1 in the Lorenzo Musetti vs Toby Samuel match: 0.30/0.31 mid 30.5%, model 36.8% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV10MUSSAM-SAM2` Will Toby Samuel win at least 1.5 more games than Lorenzo Musetti?: 0.17/0.20 mid 18.5%, model 24.3% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10MUSSAM-SAM20` Will Toby Samuel win the Lorenzo Musetti vs Toby Samuel match by a set score of 2-0?: 0.11/0.12 mid 11.5%, model 13.6% (projection_v2.0 (prediction ledger)) -- gap +2.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Maria Carle vs Valentina Mediorreal Arias -- WTA Challenger Sopo R32

**START STATUS: START_IMMINENT** -- BET BLOCKED
* Nominal schedule: 2026-11-10 20:20Z
* Current expected start: 2026-11-10 18:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-10 17:21Z
* Recommended handicap-by time: 2026-11-10 17:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (CHALLENGER) · surface ? · scheduled 2026-11-10T20:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26NOV10CARMED:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Carle (`KXWTACHALLENGERMATCH-26NOV10CARMED-CAR`) | 0.98 / 0.99 (25218) | 98.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Valentina Mediorreal Arias (`KXWTACHALLENGERMATCH-26NOV10CARMED-MED`) | 0.01 / 0.02 (3273) | 1.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Laura Samson vs Carolina Alves -- WTA Challenger Sopo R32

**START STATUS: START_IMMINENT** -- BET BLOCKED
* Nominal schedule: 2026-11-10 20:20Z
* Current expected start: 2026-11-10 18:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-10 17:21Z
* Recommended handicap-by time: 2026-11-10 17:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (CHALLENGER) · surface ? · scheduled 2026-11-10T20:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26NOV10SAMALV:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carolina Alves (`KXWTACHALLENGERMATCH-26NOV10SAMALV-ALV`) | 0.20 / 0.21 (341) | 20.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Laura Samson (`KXWTACHALLENGERMATCH-26NOV10SAMALV-SAM`) | 0.79 / 0.80 (1035) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Dali Blanch vs Marko ToPo -- ATP Challenger Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209898:209916:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dali Blanch (`KXATPCHALLENGERMATCH-26NOV10BLATOP-BLA`) | 0.52 / 0.53 (1701) | 52.5% | 44.7% | 54.0% | 47.5% [44.5%-50.5%] | 53.1% | 53.1% | 53.1% | MARKETS_AGREE | PASS | -7.8 pp | NORMAL | STALE | A / LIMITED | EXTERNAL_STALE | VERIFIED |
| Marko ToPo (`KXATPCHALLENGERMATCH-26NOV10BLATOP-TOP`) | 0.46 / 0.48 (17249) | 47.0% | 55.3% | 46.0% | 52.5% [49.5%-55.5%] | 46.9% | 46.5% | 46.5% | MARKETS_AGREE | WATCH | +8.3 pp | NORMAL | STALE | A / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4305.0, B 3741.0; serve-point win A 62.7%, B 36.2%; Elo A 1447.5, B 1570.4; model uncertainty 0.03
* Form inputs: days since last match A 22, B 64; matches on record A 301, B 266; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Gabriel Debru vs Mae Malige -- ATP Challenger Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210120:211898:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriel Debru (`KXATPCHALLENGERMATCH-26NOV10DEBMAL-DEB`) | 0.78 / 0.80 (7480) | 79.0% | 75.2% | 73.2% | 71.4% [67.7%-76.0%] | -- | 79.4% | 79.4% | MODEL_LONE_OUTLIER | PASS | -3.8 pp | NORMAL | STALE | A / LIMITED | ALL_AGREE | VERIFIED |
| Mae Malige (`KXATPCHALLENGERMATCH-26NOV10DEBMAL-MAL`) | 0.20 / 0.22 (14019) | 21.0% | 24.8% | 26.9% | 28.6% [24.0%-32.3%] | -- | 20.9% | 20.9% | MODEL_LONE_OUTLIER | SHADOW_BET | +3.8 pp | NORMAL | STALE | A / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 1491.0, B 2579.0; serve-point win A 60.3%, B 44.9%; Elo A 1602.7, B 1450.4; model uncertainty 0.0412
* Form inputs: days since last match A 22, B 64; matches on record A 188, B 139; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.043, surface_pool_high -0.037, surface_dev_loose +0.013, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Nicolas Tepmahc vs Lorenzo Giustino -- ATP Challenger Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105841:208168:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Giustino (`KXATPCHALLENGERMATCH-26NOV10TEPGIU-GIU`) | 0.78 / 0.79 (300) | 78.5% | 63.0% | 53.6% | 60.3% [55.2%-74.2%] | 78.0% | 79.1% | 79.1% | MODEL_LONE_OUTLIER | PASS | -15.5 pp | HIGH_REVIEW | STALE | B / LIMITED | EXTERNAL_STALE | VERIFIED |
| Nicolas Tepmahc (`KXATPCHALLENGERMATCH-26NOV10TEPGIU-TEP`) | 0.21 / 0.22 (9732) | 21.5% | 37.0% | 46.4% | 39.7% [25.8%-44.8%] | 22.0% | 21.4% | 21.4% | MODEL_LONE_OUTLIER | WATCH | +15.5 pp | HIGH_REVIEW | STALE | B / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3348.0, B 5720.0; serve-point win A 57.6%, B 39.9%; Elo A 1365.3, B 1534.9; model uncertainty 0.0949
* Form inputs: days since last match A 197, B 22; matches on record A 237, B 1095; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV10TEPGIU-TEP  (YES = Nicolas Tepmahc)
Model: 37%
Kalshi: 22%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: EXTERNAL_STALE
Data quality: B (LIMITED)
Reasons: STALE_KALSHI_QUOTE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.030, surface_pool_high +0.041, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Ariel Behar / Joshua Paris vs Admir Kalender / Nino Serdarusic -- ATP Challenger Orleans R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:50Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-10T18:50:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10BEHPARKALSER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ariel Behar / Joshua Paris (`KXATPCHALLENGERDOUBLES-26NOV10BEHPARKALSER-BEHPAR`) | 0.56 / 0.61 (41) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Admir Kalender / Nino Serdarusic (`KXATPCHALLENGERDOUBLES-26NOV10BEHPARKALSER-KALSER`) | 0.36 / 0.44 (45) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Carles Cordoba vs Valentin Gonzalez-Galino -- M15 Las Palmas de Gran Canaria R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213059:213228:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carles Cordoba (`KXITFMATCH-26NOV10CORGON-COR`) | 0.26 / 0.27 (9990) | 26.5% | 76.2% | 54.2% | 64.5% [63.4%-65.7%] | 71.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +49.7 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valentin Gonzalez-Galino (`KXITFMATCH-26NOV10CORGON-GON`) | 0.73 / 0.74 (985) | 73.5% | 23.8% | 45.8% | 35.5% [34.3%-36.6%] | 28.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -49.7 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1490.0, B 169.0; serve-point win A 58.7%, B 46.7%; Elo A 1289.8, B 1178.6; model uncertainty 0.0115
* Form inputs: days since last match A 204, B 365; matches on record A 42, B 4; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10CORGON-COR  (YES = Carles Cordoba)
Model: 76%
Kalshi: 26%
Gap: +50 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Leal / Lima Sanches vs Da Rosa Castro / Monteiro -- M25 Vale do Lobo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10LEALIMDARMON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Da Rosa Castro / Monteiro (`KXITFDOUBLES-26NOV10LEALIMDARMON-DARMON`) | 0.21 / 0.85 (1) | 53.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Leal / Lima Sanches (`KXITFDOUBLES-26NOV10LEALIMDARMON-LEALIM`) | 0.03 / 0.64 (1) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Pablo Perez Ramos vs Tyler Zink -- M25 Vale do Lobo R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10PERZIN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pablo Perez Ramos (`KXITFMATCH-26NOV10PERZIN-PER`) | 0.29 / 0.30 (1131) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tyler Zink (`KXITFMATCH-26NOV10PERZIN-ZIN`) | 0.70 / 0.71 (869) | 70.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alan Magadan vs Oriol Roca Batalla -- ATP Challenger Lima R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 19:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-10T19:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106177:209246:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alan Magadan (`KXATPCHALLENGERMATCH-26NOV10MAGROC-MAG`) | 0.13 / 0.19 (0) | 16.0% | 24.3% | 19.1% | 19.5% [18.4%-20.6%] | -- | 15.4% | -- | INSUFFICIENT_INPUTS | PASS | +8.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oriol Roca Batalla (`KXATPCHALLENGERMATCH-26NOV10MAGROC-ROC`) | 0.78 / 0.81 (25) | 79.5% | 75.7% | 80.9% | 80.5% [79.4%-81.5%] | -- | 83.7% | -- | INSUFFICIENT_INPUTS | PASS | -3.8 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2107.0, B 4899.0; serve-point win A 58.1%, B 36.5%; Elo A 1361.6, B 1599.4; model uncertainty 0.0107
* Form inputs: days since last match A 8, B 8; matches on record A 86, B 1042; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.001, surface_dev_tight +0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Thiago Monteiro vs Filip Misolic -- ATP Challenger Lima R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 19:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-10T19:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106329:209209:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Filip Misolic (`KXATPCHALLENGERMATCH-26NOV10MONMIS-MIS`) | 0.42 / 0.43 (35515) | 42.5% | 63.9% | 59.0% | 60.4% [58.5%-62.4%] | 57.2% | -- | 57.2% | KALSHI_LONE_OUTLIER | WATCH | +21.4 pp | HIGH_REVIEW | STALE | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Thiago Monteiro (`KXATPCHALLENGERMATCH-26NOV10MONMIS-MON`) | 0.57 / 0.58 (31958) | 57.5% | 36.1% | 41.0% | 39.6% [37.6%-41.5%] | 42.8% | -- | 42.8% | KALSHI_LONE_OUTLIER | PASS | -21.4 pp | HIGH_REVIEW | STALE | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 5148.0, B 3485.0; serve-point win A 61.7%, B 35.4%; Elo A 1710.7, B 1815.1; model uncertainty 0.0196
* Form inputs: days since last match A 8, B 8; matches on record A 950, B 332; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV10MONMIS-MIS  (YES = Filip Misolic)
Model: 64%
Kalshi: 42%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: SUPPORTS_MODEL_DIRECTION
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.019, surface_dev_loose -0.019, surface_dev_tight +0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Pyotr Nesterov vs Timo Legout -- ATP Challenger Knoxville R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 19:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T19:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209318:209355:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Timo Legout (`KXATPCHALLENGERMATCH-26NOV10NESLEG-LEG`) | 0.73 / 0.75 (14338) | 74.0% | 59.6% | 61.3% | 58.8% [54.7%-62.3%] | -- | 73.9% | 73.9% | MODEL_LONE_OUTLIER | PASS | -14.4 pp | REVIEW | STALE | B / ADEQUATE | AGREES_WITH_KALSHI | AMBIGUOUS |
| Pyotr Nesterov (`KXATPCHALLENGERMATCH-26NOV10NESLEG-NES`) | 0.25 / 0.27 (7585) | 26.0% | 40.4% | 38.7% | 41.2% [37.7%-45.3%] | -- | 26.7% | 26.7% | MODEL_LONE_OUTLIER | PASS | +14.4 pp | REVIEW | STALE | B / ADEQUATE | AGREES_WITH_KALSHI | AMBIGUOUS |

* Serve evidence (points): A 3494.0, B 1269.0; serve-point win A 57.7%, B 40.5%; Elo A 1514.7, B 1562.6; model uncertainty 0.0384
* Form inputs: days since last match A 8, B 15; matches on record A 264, B 185; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.015, surface_dev_loose -0.020, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Nikolas Sanchez Izquierdo vs Nicolas Jarry -- ATP Challenger Lima R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 19:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-10T19:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111797:207663:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Jarry (`KXATPCHALLENGERMATCH-26NOV10SAIJAR-JAR`) | 0.43 / 0.46 (18) | 44.5% | 60.1% | 42.5% | 53.5% [49.0%-61.0%] | 55.4% | 55.3% | 55.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +15.6 pp | HIGH_REVIEW | STALE | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Nikolas Sanchez Izquierdo (`KXATPCHALLENGERMATCH-26NOV10SAIJAR-SAI`) | 0.53 / 0.59 (4) | 56.0% | 39.9% | 57.5% | 46.5% [39.0%-51.0%] | 44.6% | 44.9% | 44.7% | MODEL_LONE_OUTLIER | PASS | -16.1 pp | HIGH_REVIEW | STALE | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 5051.0, B 2685.0; serve-point win A 62.0%, B 36.0%; Elo A 1661.4, B 1827.1; model uncertainty 0.0598
* Form inputs: days since last match A 8, B 15; matches on record A 583, B 734; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV10SAIJAR-JAR  (YES = Nicolas Jarry)
Model: 60%
Kalshi: 44%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_MODEL
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.015, surface_dev_loose +0.010, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Marta Kostyuk vs Jessica Pegula -- WTA Finals Women Singles Group A

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-10 23:00Z
* Current expected start: 2026-11-10 20:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-10 17:21Z
* Recommended handicap-by time: 2026-11-10 19:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_FINALS) · Hard · scheduled 2026-11-10T23:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202468:216146:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marta Kostyuk (`KXWTAMATCH-26NOV10KOSPEG-KOS`) | 0.37 / 0.38 (213447) | 37.5% | 38.0% | 32.4% | 31.9% [30.5%-36.1%] | 37.7% | 36.6% | 36.6% | MARKETS_AGREE | PASS | +0.5 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Jessica Pegula (`KXWTAMATCH-26NOV10KOSPEG-PEG`) | 0.62 / 0.63 (9936) | 62.5% | 62.0% | 67.7% | 68.1% [63.9%-69.5%] | 62.3% | 63.3% | 63.3% | MARKETS_AGREE | WATCH | -0.5 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4067.0, B 5824.0; serve-point win A 57.2%, B 40.5%; Elo A 2061.9, B 2193.0; model uncertainty 0.0282
* Form inputs: days since last match A 2, B 2; matches on record A 433, B 768; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.014, surface_dev_loose +0.005, surface_dev_tight -0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV10KOSPEG-22` Over 21.5 games: 0.53/0.54 mid 53.5%, model 62.7% (projection_v2.0 (prediction ledger)) -- gap +9.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV10KOSPEG-27` Over 26.5 games: 0.32/0.33 mid 32.5%, model 39.5% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV10KOSPEG-17` Over 16.5 games: 0.91/0.92 mid 91.5%, model 94.1% (projection_v2.0 (prediction ledger)) -- gap +2.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV10KOSPEG-1-KOS` Will Marta Kostyuk win set 1 in the Marta Kostyuk vs Jessica Pegula match: 0.40/0.41 mid 40.5%, model 41.9% (projection_v2.0 (prediction ledger)) -- gap +1.4 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV10KOSPEG-1-PEG` Will Jessica Pegula win set 1 in the Marta Kostyuk vs Jessica Pegula match: 0.59/0.60 mid 59.5%, model 58.1% (projection_v2.0 (prediction ledger)) -- gap -1.4 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV10KOSPEG-2-PEG` Will Jessica Pegula win set 2 in the Marta Kostyuk vs Jessica Pegula match: 0.35/0.79 mid 57.0%, model 58.1% (projection_v2.0 (prediction ledger)) -- gap +1.1 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV10KOSPEG-2-KOS` Will Marta Kostyuk win set 2 in the Marta Kostyuk vs Jessica Pegula match: 0.18/0.65 mid 41.5%, model 41.9% (projection_v2.0 (prediction ledger)) -- gap +0.4 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Brady / Howse vs Marques / Rocha -- M25 Vale do Lobo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10BRAHOWMARROC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brady / Howse (`KXITFDOUBLES-26NOV10BRAHOWMARROC-BRAHOW`) | 0.15 / 0.39 (40) | 27.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marques / Rocha (`KXITFDOUBLES-26NOV10BRAHOWMARROC-MARROC`) | 0.56 / 0.72 (89) | 64.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Forcano / Izquierdo Luque vs Cacao / Dinis Silva -- M25 Vale do Lobo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10FORIZQCACDIN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cacao / Dinis Silva (`KXITFDOUBLES-26NOV10FORIZQCACDIN-CACDIN`) | 0.02 / 0.64 (6) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Forcano / Izquierdo Luque (`KXITFDOUBLES-26NOV10FORIZQCACDIN-FORIZQ`) | 0.50 / 0.95 (16) | 72.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Johns / Rodenas vs Maia / Valdoleiros -- M25 Vale do Lobo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10JOHRODMAIVAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Johns / Rodenas (`KXITFDOUBLES-26NOV10JOHRODMAIVAL-JOHROD`) | 0.08 / 0.84 (5) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maia / Valdoleiros (`KXITFDOUBLES-26NOV10JOHRODMAIVAL-MAIVAL`) | 0.12 / 0.26 (38) | 19.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Augusto Land vs Gabriel Augusto Carvalho -- M25 Santa Cruz do Sul R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10LANCAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriel Augusto Carvalho (`KXITFMATCH-26NOV10LANCAR-CAR`) | 0.58 / 0.59 (10711) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Augusto Land (`KXITFMATCH-26NOV10LANCAR-LAN`) | 0.41 / 0.42 (9877) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofia Merlos Cardoso vs Giulia Gomes Ferreira -- W15 São Carlos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10MERGOM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giulia Gomes Ferreira (`KXITFWMATCH-26NOV10MERGOM-GOM`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sofia Merlos Cardoso (`KXITFWMATCH-26NOV10MERGOM-MER`) | -- / 0.01 (6032) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ozan Baris vs Oliver Tarvet -- ATP Challenger Knoxville R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T20:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210028:210472:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ozan Baris (`KXATPCHALLENGERMATCH-26NOV10BARTAR-BAR`) | 0.19 / 0.20 (22274) | 19.5% | 12.3% | 11.1% | 12.8% [11.3%-14.5%] | 19.7% | 18.7% | 19.2% | MODEL_LONE_OUTLIER | PASS | -7.2 pp | NORMAL | STALE | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Oliver Tarvet (`KXATPCHALLENGERMATCH-26NOV10BARTAR-TAR`) | 0.80 / 0.81 (484) | 80.5% | 87.6% | 88.9% | 87.2% [85.5%-88.7%] | 80.3% | 81.7% | 81.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +7.2 pp | NORMAL | STALE | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1236.0, B 1816.0; serve-point win A 56.9%, B 34.0%; Elo A 1405.9, B 1714.8; model uncertainty 0.016
* Form inputs: days since last match A 15, B 36; matches on record A 93, B 88; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose -0.008, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Daniel Milavsky vs Murphy Cassone -- ATP Challenger Knoxville R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T20:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209326:212251:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Murphy Cassone (`KXATPCHALLENGERMATCH-26NOV10MILCAS-CAS`) | 0.50 / 0.51 (7381) | 50.5% | 51.5% | 41.2% | 46.1% [43.7%-49.5%] | 50.0% | 50.5% | 50.5% | MODEL_LONE_OUTLIER | PASS | +1.0 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Daniel Milavsky (`KXATPCHALLENGERMATCH-26NOV10MILCAS-MIL`) | 0.49 / 0.50 (8409) | 49.5% | 48.5% | 58.8% | 53.9% [50.5%-56.3%] | 50.0% | 49.3% | 49.3% | MODEL_LONE_OUTLIER | WATCH | -1.0 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4004.0, B 4123.0; serve-point win A 65.2%, B 34.4%; Elo A 1562.7, B 1629.4; model uncertainty 0.0292
* Form inputs: days since last match A 8, B 8; matches on record A 126, B 202; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Allen / Kaczmarek vs Garcia Longo / Miletich -- M15 Las Palmas de Gran Canaria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10ALLKACGARMIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Allen / Kaczmarek (`KXITFDOUBLES-26NOV10ALLKACGARMIL-ALLKAC`) | -- / 0.01 (64304) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Garcia Longo / Miletich (`KXITFDOUBLES-26NOV10ALLKACGARMIL-GARMIL`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE

## Camara / Sajjid Koothrat vs Naharro / Pujol Navarro -- M15 Las Palmas de Gran Canaria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10CAMSAJNAHPUJ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Camara / Sajjid Koothrat (`KXITFDOUBLES-26NOV10CAMSAJNAHPUJ-CAMSAJ`) | 0.03 / 0.06 (1) | 4.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Naharro / Pujol Navarro (`KXITFDOUBLES-26NOV10CAMSAJNAHPUJ-NAHPUJ`) | 0.92 / 0.94 (303) | 93.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Thomas Gimenez vs Marcel Zielinski -- M15 Las Palmas de Gran Canaria R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210505:213645:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thomas Gimenez (`KXITFMATCH-26NOV10GIMZIE-GIM`) | -- / 0.01 (65683) | -- | 16.4% | 23.2% | 27.9% [25.2%-30.4%] | 7.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | STALE | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |
| Marcel Zielinski (`KXITFMATCH-26NOV10GIMZIE-ZIE`) | 0.99 / -- (0) | -- | 83.6% | 76.8% | 72.1% [69.6%-74.8%] | 92.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | STALE | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 106.0, B 2564.0; serve-point win A 51.3%, B 41.4%; Elo A 1232.1, B 1392.0; model uncertainty 0.0261
* Form inputs: days since last match A 274, B 225; matches on record A 3, B 151; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.018, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nishesh Basavareddy vs Pierre-Hugues Herbert -- ATP Challenger Orleans R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105732:210460:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nishesh Basavareddy (`KXATPCHALLENGERMATCH-26NOV10BASHER-BAS`) | 0.65 / 0.66 (110) | 65.5% | 75.0% | 67.5% | 67.5% [62.6%-69.3%] | 64.6% | 65.4% | 65.4% | MODEL_LONE_OUTLIER | PASS | +9.5 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Pierre-Hugues Herbert (`KXATPCHALLENGERMATCH-26NOV10BASHER-HER`) | 0.33 / 0.34 (328) | 33.5% | 25.0% | 32.5% | 32.5% [30.7%-37.4%] | 35.4% | 34.9% | 34.9% | MODEL_LONE_OUTLIER | PASS | -8.5 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4072.0, B 3890.0; serve-point win A 68.2%, B 37.3%; Elo A 1806.7, B 1690.2; model uncertainty 0.0335
* Form inputs: days since last match A 8, B 15; matches on record A 189, B 882; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.027, surface_pool_high +0.018, surface_dev_loose -0.000, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Mateo Del Pino vs Valentin Basel -- M15 Roldan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210182:211761:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valentin Basel (`KXITFMATCH-26NOV10DELBAS-BAS`) | 0.18 / 0.53 (1) | 35.5% | 39.4% | 28.5% | 34.6% [31.6%-38.6%] | -- | -- | -- | -- | PASS | +3.9 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mateo Del Pino (`KXITFMATCH-26NOV10DELBAS-DEL`) | 0.36 / 0.74 (1) | 55.0% | 60.6% | 71.5% | 65.4% [61.4%-68.3%] | -- | -- | -- | -- | PASS | +5.6 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1084.0, B 1638.0; serve-point win A 57.5%, B 44.5%; Elo A 1220.0, B 1141.1; model uncertainty 0.0348
* Form inputs: days since last match A 8, B 141; matches on record A 96, B 73; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Juan Estevez vs Federico Aguilar Cardozo -- M15 Roldan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211661:212481:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Federico Aguilar Cardozo (`KXITFMATCH-26NOV10ESTAGU-AGU`) | 0.44 / 0.45 (4728) | 44.5% | 23.8% | 25.3% | 24.4% [23.5%-25.4%] | -- | -- | -- | -- | PASS | -20.7 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Juan Estevez (`KXITFMATCH-26NOV10ESTAGU-EST`) | 0.55 / 0.56 (1861) | 55.5% | 76.2% | 74.7% | 75.5% [74.6%-76.5%] | -- | -- | -- | -- | WATCH | +20.7 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3336.0, B 539.0; serve-point win A 57.6%, B 47.8%; Elo A 1474.8, B 1278.4; model uncertainty 0.0092
* Form inputs: days since last match A 8, B 8; matches on record A 197, B 50; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10ESTAGU-EST  (YES = Juan Estevez)
Model: 76%
Kalshi: 56%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Leote Prata / Morais vs Braynin / Pecak -- M25 Vale do Lobo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10LEOMORBRAPEC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Braynin / Pecak (`KXITFDOUBLES-26NOV10LEOMORBRAPEC-BRAPEC`) | 0.28 / 0.64 (1) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Leote Prata / Morais (`KXITFDOUBLES-26NOV10LEOMORBRAPEC-LEOMOR`) | 0.19 / 0.64 (1) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Perez Ramos / Wright vs Domingues / Marques -- M25 Vale do Lobo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10PERWRIDOMMAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Domingues / Marques (`KXITFDOUBLES-26NOV10PERWRIDOMMAR-DOMMAR`) | 0.18 / 0.32 (36) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Perez Ramos / Wright (`KXITFDOUBLES-26NOV10PERWRIDOMMAR-PERWRI`) | 0.61 / 0.79 (119) | 70.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Tomas Re vs Thiago Cigarran -- M15 Roldan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10REXCIG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thiago Cigarran (`KXITFMATCH-26NOV10REXCIG-CIG`) | 0.75 / 0.76 (4410) | 75.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tomas Re (`KXITFMATCH-26NOV10REXCIG-REX`) | 0.24 / 0.25 (4052) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Coco Gauff vs Linda Noskova -- WTA Finals Women Singles Group A

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-11 00:10Z
* Current expected start: 2026-11-10 21:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-10 17:21Z
* Recommended handicap-by time: 2026-11-10 20:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_FINALS) · Hard · scheduled 2026-11-11T00:10:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:221103:222328:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Coco Gauff (`KXWTAMATCH-26NOV10GAUNOS-GAU`) | 0.60 / 0.62 (106403) | 61.0% | 60.5% | 64.3% | 64.3% [62.8%-66.7%] | -- | -- | -- | -- | WATCH | -0.5 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Linda Noskova (`KXWTAMATCH-26NOV10GAUNOS-NOS`) | 0.38 / 0.39 (3622) | 38.5% | 39.5% | 35.7% | 35.7% [33.3%-37.2%] | -- | -- | -- | -- | PASS | +1.0 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5157.0, B 4568.0; serve-point win A 59.7%, B 42.3%; Elo A 2205.7, B 2101.8; model uncertainty 0.0197
* Form inputs: days since last match A 2, B 2; matches on record A 447, B 336; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.015, surface_dev_loose -0.010, surface_dev_tight +0.010
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV10GAUNOS-23` Over 22.5 games: 0.49/0.51 mid 50.0%, model 56.4% (projection_v2.0 (prediction ledger)) -- gap +6.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV10GAUNOS-28` Over 27.5 games: 0.29/0.30 mid 29.5%, model 35.4% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV10GAUNOS-18` Over 17.5 games: 0.84/0.88 mid 86.0%, model 89.0% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV10GAUNOS-2-NOS` Will Linda Noskova win set 2 in the Coco Gauff vs Linda Noskova match: 0.38/0.43 mid 40.5%, model 43.0% (projection_v2.0 (prediction ledger)) -- gap +2.5 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV10GAUNOS-1-NOS` Will Linda Noskova win set 1 in the Coco Gauff vs Linda Noskova match: 0.42/0.43 mid 42.5%, model 43.0% (projection_v2.0 (prediction ledger)) -- gap +0.5 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV10GAUNOS-1-GAU` Will Coco Gauff win set 1 in the Coco Gauff vs Linda Noskova match: 0.56/0.58 mid 57.0%, model 57.0% (projection_v2.0 (prediction ledger)) -- gap +0.0 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV10GAUNOS-2-GAU` Will Coco Gauff win set 2 in the Coco Gauff vs Linda Noskova match: 0.54/0.60 mid 57.0%, model 57.0% (projection_v2.0 (prediction ledger)) -- gap +0.0 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NO_EXTERNAL_PRICE; STALE_QUOTE

## Yannik Alvarez vs Luis Carlos Alvarez Valdes -- M15 Zamora R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211468:214425:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yannik Alvarez (`KXITFMATCH-26NOV10ALVALV2-ALV`) | 0.12 / 0.13 (12271) | 12.5% | 39.9% | 49.5% | 50.0% [49.5%-50.5%] | -- | -- | -- | -- | PASS | +27.4 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luis Carlos Alvarez Valdes (`KXITFMATCH-26NOV10ALVALV2-ALV2`) | 0.87 / 0.88 (13993) | 87.5% | 60.1% | 50.5% | 50.0% [49.5%-50.5%] | -- | -- | -- | -- | PASS | -27.4 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 431.0, B 923.0; serve-point win A 56.6%, B 41.4%; Elo A 1423.3, B 1424.0; model uncertainty 0.0053
* Form inputs: days since last match A 211, B 379; matches on record A 8, B 45; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10ALVALV2-ALV  (YES = Yannik Alvarez)
Model: 40%
Kalshi: 12%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexander Bernard vs Joaquin Bianchi -- M15 Zamora R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209060:214129:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Bernard (`KXITFMATCH-26NOV10BERBIA-BER`) | 0.97 / 0.98 (711) | 97.5% | 87.0% | 71.0% | 76.9% [76.0%-78.6%] | -- | -- | -- | -- | PASS | -10.6 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Joaquin Bianchi (`KXITFMATCH-26NOV10BERBIA-BIA`) | 0.02 / 0.03 (12382) | 2.5% | 13.1% | 29.0% | 23.1% [21.4%-24.0%] | -- | -- | -- | -- | PASS | +10.6 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 733.0, B 179.0; serve-point win A 61.8%, B 46.8%; Elo A 1377.3, B 1162.1; model uncertainty 0.0132
* Form inputs: days since last match A 365, B 239; matches on record A 104, B 4; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jonah Braswell vs Isaac Forde -- M25 Columbus OH R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10BRAFOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jonah Braswell (`KXITFMATCH-26NOV10BRAFOR-BRA`) | 0.98 / 0.99 (8633) | 98.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Isaac Forde (`KXITFMATCH-26NOV10BRAFOR-FOR`) | 0.01 / 0.02 (1408) | 1.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## David Cristian Carteputreda vs Miko Lapalme -- M25 Montreal R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:149161:214465:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| David Cristian Carteputreda (`KXITFMATCH-26NOV10CARLAP-CAR`) | 0.61 / 0.62 (1) | 61.5% | 26.9% | 50.0% | 31.6% [31.2%-32.5%] | -- | -- | -- | -- | PASS | -34.6 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Miko Lapalme (`KXITFMATCH-26NOV10CARLAP-LAP`) | 0.38 / 0.39 (4) | 38.5% | 73.1% | 50.0% | 68.4% [67.5%-68.8%] | -- | -- | -- | -- | PASS | +34.6 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 133.0, B 89.0; serve-point win A 57.5%, B 37.8%; Elo A 1127.9, B 1268.4; model uncertainty 0.0069
* Form inputs: days since last match A 449, B 253; matches on record A 9, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10CARLAP-LAP  (YES = Miko Lapalme)
Model: 73%
Kalshi: 38%
Gap: +35 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.001, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stefan Cooper vs Gray Voelzke -- M15 Zamora R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:138104:213882:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefan Cooper (`KXITFMATCH-26NOV10COOVOE-COO`) | 0.16 / 0.17 (10806) | 16.5% | 70.7% | 76.6% | 68.1% [64.7%-71.5%] | -- | -- | -- | -- | PASS | +54.2 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gray Voelzke (`KXITFMATCH-26NOV10COOVOE-VOE`) | 0.83 / 0.84 (1541) | 83.5% | 29.3% | 23.4% | 31.9% [28.5%-35.3%] | -- | -- | -- | -- | PASS | -54.2 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 556.0, B 817.0; serve-point win A 69.2%, B 35.3%; Elo A 1220.8, B 1115.5; model uncertainty 0.034
* Form inputs: days since last match A 197, B 190; matches on record A 19, B 16; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10COOVOE-COO  (YES = Stefan Cooper)
Model: 71%
Kalshi: 16%
Gap: +54 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ignacio De Armas vs Hernan Casanova -- M15 Roldan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106292:214292:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hernan Casanova (`KXITFMATCH-26NOV10DEACAS-CAS`) | 0.96 / 0.97 (323) | 96.5% | 88.1% | 77.0% | 84.2% [83.2%-84.8%] | -- | -- | -- | -- | PASS | -8.4 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ignacio De Armas (`KXITFMATCH-26NOV10DEACAS-DEA`) | 0.03 / 0.05 (1261) | 4.0% | 11.9% | 23.1% | 15.8% [15.2%-16.8%] | -- | -- | -- | -- | PASS | +7.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 273.0, B 3175.0; serve-point win A 52.8%, B 38.3%; Elo A 1254.7, B 1558.3; model uncertainty 0.008
* Form inputs: days since last match A 351, B 8; matches on record A 4, B 814; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jake Fellows vs Jared Horwood -- M25 Montreal R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212654:214450:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jake Fellows (`KXITFMATCH-26NOV10FELHOR-FEL`) | 0.91 / 0.92 (11246) | 91.5% | 71.9% | 53.1% | 73.4% [73.1%-74.2%] | -- | -- | -- | -- | PASS | -19.6 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jared Horwood (`KXITFMATCH-26NOV10FELHOR-HOR`) | 0.08 / 0.09 (870) | 8.5% | 28.1% | 46.9% | 26.6% [25.8%-26.9%] | -- | -- | -- | -- | PASS | +19.6 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 104.0, B 57.0; serve-point win A 61.3%, B 43.2%; Elo A 1422.8, B 1239.9; model uncertainty 0.0057
* Form inputs: days since last match A 197, B 246; matches on record A 2, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10FELHOR-HOR  (YES = Jared Horwood)
Model: 28%
Kalshi: 8%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.009, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valentino Grippo vs Juan Ignacio Gallego -- M15 Roldan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213200:213201:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Ignacio Gallego (`KXITFMATCH-26NOV10GRIGAL-GAL`) | 0.68 / 0.73 (401) | 70.5% | 61.0% | 57.8% | 56.2% [56.2%-57.3%] | -- | -- | -- | -- | PASS | -9.5 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valentino Grippo (`KXITFMATCH-26NOV10GRIGAL-GRI`) | 0.25 / 0.29 (35) | 27.0% | 39.0% | 42.2% | 43.8% [42.7%-43.8%] | -- | -- | -- | -- | PASS | +12.0 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 452.0, B 356.0; serve-point win A 57.4%, B 40.5%; Elo A 1114.9, B 1158.6; model uncertainty 0.0054
* Form inputs: days since last match A 8, B 8; matches on record A 14, B 11; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Volodymyr Gurenko vs Matthew Michibata -- M25 Montreal R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10GURMIC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Volodymyr Gurenko (`KXITFMATCH-26NOV10GURMIC-GUR`) | 0.96 / 0.97 (8310) | 96.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matthew Michibata (`KXITFMATCH-26NOV10GURMIC-MIC`) | 0.03 / 0.04 (8582) | 3.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tarun Karra vs Mauricio Echazu -- M15 Zamora R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105273:213598:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mauricio Echazu (`KXITFMATCH-26NOV10KARECH-ECH`) | 0.94 / 0.95 (8842) | 94.5% | 81.5% | 78.0% | 79.5% [78.4%-81.6%] | -- | -- | -- | -- | PASS | -12.9 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tarun Karra (`KXITFMATCH-26NOV10KARECH-KAR`) | 0.05 / 0.06 (8942) | 5.5% | 18.4% | 22.0% | 20.5% [18.4%-21.6%] | -- | -- | -- | -- | PASS | +12.9 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 201.0, B 170.0; serve-point win A 56.9%, B 36.1%; Elo A 1132.3, B 1368.9; model uncertainty 0.0161
* Form inputs: days since last match A 239, B 197; matches on record A 8, B 685; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matthias Uwe Kask vs Tiago Silva -- M25 Montreal R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:130493:210490:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthias Uwe Kask (`KXITFMATCH-26NOV10KASSIL-KAS`) | 0.26 / 0.27 (1) | 26.5% | 29.8% | 30.7% | 41.8% [40.8%-41.8%] | -- | -- | -- | -- | PASS | +3.3 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tiago Silva (`KXITFMATCH-26NOV10KASSIL-SIL`) | 0.72 / 0.74 (10675) | 73.0% | 70.2% | 69.3% | 58.2% [58.2%-59.2%] | -- | -- | -- | -- | PASS | -2.8 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 46.0, B 637.0; serve-point win A 57.6%, B 38.3%; Elo A 1210.9, B 1270.1; model uncertainty 0.0052
* Form inputs: days since last match A 729, B 449; matches on record A 4, B 42; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nason Lo vs Rishvanth Krishna -- M25 Columbus OH R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10LOXKRI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rishvanth Krishna (`KXITFMATCH-26NOV10LOXKRI-KRI`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nason Lo (`KXITFMATCH-26NOV10LOXKRI-LOX`) | -- / 0.01 (11627) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Youcef Rihane vs Elias Sumann -- M15 Naples FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209065:213981:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Youcef Rihane (`KXITFMATCH-26NOV10RIHSUM-RIH`) | 0.93 / 0.94 (8201) | 93.5% | 38.9% | 73.6% | 36.7% [36.6%-37.8%] | -- | -- | -- | -- | PASS | -54.6 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Elias Sumann (`KXITFMATCH-26NOV10RIHSUM-SUM`) | 0.06 / 0.07 (10506) | 6.5% | 61.1% | 26.5% | 63.3% [62.2%-63.4%] | -- | -- | -- | -- | PASS | +54.6 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 217.0; serve-point win A 56.8%, B 41.0%; Elo A 1191.5, B 1281.5; model uncertainty 0.0062
* Form inputs: days since last match A 1114, B 477; matches on record A 17, B 3; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10RIHSUM-SUM  (YES = Elias Sumann)
Model: 61%
Kalshi: 6%
Gap: +55 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matthew Segura vs William Nolan -- M15 Naples FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208052:213373:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| William Nolan (`KXITFMATCH-26NOV10SEGNOL-NOL`) | 0.34 / 0.36 (1) | 35.0% | 51.7% | 56.8% | 51.0% [49.0%-53.7%] | -- | -- | -- | -- | PASS | +16.7 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matthew Segura (`KXITFMATCH-26NOV10SEGNOL-SEG`) | 0.58 / 0.65 (37) | 61.5% | 48.3% | 43.2% | 48.9% [46.3%-51.0%] | -- | -- | -- | -- | PASS | -13.2 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 338.0, B 561.0; serve-point win A 56.7%, B 43.0%; Elo A 1167.5, B 1168.6; model uncertainty 0.0237
* Form inputs: days since last match A 197, B 197; matches on record A 37, B 11; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10SEGNOL-NOL  (YES = William Nolan)
Model: 52%
Kalshi: 35%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.011, surface_dev_loose -0.011, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tom Sickenberger vs Agassi Rusher -- M25 Columbus OH R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212289:213837:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Agassi Rusher (`KXITFMATCH-26NOV10SICRUS-RUS`) | 0.28 / 0.30 (5) | 29.0% | 69.1% | 56.8% | 65.4% [64.4%-66.4%] | -- | -- | -- | -- | PASS | +40.1 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tom Sickenberger (`KXITFMATCH-26NOV10SICRUS-SIC`) | 0.70 / 0.73 (3) | 71.5% | 30.9% | 43.2% | 34.6% [33.6%-35.6%] | -- | -- | -- | -- | PASS | -40.6 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 515.0, B 227.0; serve-point win A 54.7%, B 41.5%; Elo A 1178.2, B 1294.6; model uncertainty 0.0097
* Form inputs: days since last match A 197, B 547; matches on record A 15, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10SICRUS-RUS  (YES = Agassi Rusher)
Model: 69%
Kalshi: 29%
Gap: +40 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nikolas Stoot vs Corey Craig -- M15 Naples FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212914:214246:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Corey Craig (`KXITFMATCH-26NOV10STOCRA-CRA`) | 0.47 / 0.49 (9048) | 48.0% | 61.0% | 51.6% | 57.2% [55.2%-58.3%] | -- | -- | -- | -- | PASS | +13.0 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nikolas Stoot (`KXITFMATCH-26NOV10STOCRA-STO`) | 0.51 / 0.53 (7367) | 52.0% | 39.0% | 48.4% | 42.8% [41.7%-44.8%] | -- | -- | -- | -- | PASS | -13.0 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 775.0, B 215.0; serve-point win A 58.2%, B 39.7%; Elo A 1264.0, B 1321.1; model uncertainty 0.0154
* Form inputs: days since last match A 197, B 358; matches on record A 12, B 18; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.010, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rafael Ymer vs Charlie Snow -- M25 Columbus OH R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10YMESNO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charlie Snow (`KXITFMATCH-26NOV10YMESNO-SNO`) | 0.03 / 0.04 (6898) | 3.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rafael Ymer (`KXITFMATCH-26NOV10YMESNO-YME`) | 0.96 / 0.97 (2530) | 96.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Logan Zapp vs Justin Riley Anson -- M15 Naples FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10ZAPANS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Justin Riley Anson (`KXITFMATCH-26NOV10ZAPANS-ANS`) | 0.56 / 0.57 (760) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Logan Zapp (`KXITFMATCH-26NOV10ZAPANS-ZAP`) | 0.43 / 0.44 (5031) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Melissa Boyden vs Sofia Meabe -- W15 São Carlos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222274:266446:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Melissa Boyden (`KXITFWMATCH-26NOV10BOYMEA-BOY`) | 0.11 / 0.13 (105) | 12.0% | 33.9% | 33.8% | 36.8% [34.3%-39.4%] | 15.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +21.9 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sofia Meabe (`KXITFWMATCH-26NOV10BOYMEA-MEA`) | 0.85 / 0.89 (3) | 87.0% | 66.1% | 66.2% | 63.2% [60.6%-65.7%] | 84.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -20.9 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 765.0, B 235.0; serve-point win A 49.4%, B 47.5%; Elo A 1254.1, B 1346.8; model uncertainty 0.0255
* Form inputs: days since last match A 211, B 295; matches on record A 91, B 18; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10BOYMEA-BOY  (YES = Melissa Boyden)
Model: 34%
Kalshi: 12%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.025, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Irina Fetecau vs Carolina Gomez -- W35 Weston FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213584:222312:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Irina Fetecau (`KXITFWMATCH-26NOV10FETGOM-FET`) | 0.20 / 0.22 (84) | 21.0% | 88.8% | 44.7% | 81.9% [81.2%-81.9%] | -- | -- | -- | -- | PASS | +67.8 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Carolina Gomez (`KXITFWMATCH-26NOV10FETGOM-GOM`) | 0.78 / 0.79 (1) | 78.5% | 11.2% | 55.3% | 18.1% [18.1%-18.9%] | -- | -- | -- | -- | PASS | -67.3 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 570.0, B 0.0; serve-point win A 57.8%, B 51.3%; Elo A 1570.6, B 1312.0; model uncertainty 0.0036
* Form inputs: days since last match A 106, B 848; matches on record A 425, B 40; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10FETGOM-FET  (YES = Irina Fetecau)
Model: 89%
Kalshi: 21%
Gap: +68 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.007, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marie Mettraux vs Gabriela Kawano Cho -- W15 São Carlos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221062:259599:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriela Kawano Cho (`KXITFWMATCH-26NOV10METKAW-KAW`) | 0.02 / 0.03 (4872) | 2.5% | 15.2% | 7.7% | 25.2% [19.3%-29.6%] | 4.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +12.7 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marie Mettraux (`KXITFWMATCH-26NOV10METKAW-MET`) | 0.97 / 0.98 (6338) | 97.5% | 84.8% | 92.3% | 74.8% [70.4%-80.7%] | 95.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.7 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1753.0, B 126.0; serve-point win A 57.3%, B 50.3%; Elo A 1418.6, B 1247.9; model uncertainty 0.0516
* Form inputs: days since last match A 30, B 400; matches on record A 308, B 17; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.017, surface_pool_high +0.017, surface_dev_loose +0.008, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rebeca Pereira vs Luisa Meyer auf der Heide -- W15 São Carlos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215721:220053:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luisa Meyer auf der Heide (`KXITFWMATCH-26NOV10PERMEY-MEY`) | 0.99 / -- (0) | -- | 91.4% | 96.9% | 86.5% [82.5%-91.5%] | 91.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | STALE | D / POOR | INSUFFICIENT_INPUTS | VERIFIED |
| Rebeca Pereira (`KXITFWMATCH-26NOV10PERMEY-PER`) | -- / 0.01 (167162) | -- | 8.6% | 3.1% | 13.5% [8.5%-17.5%] | 8.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | STALE | D / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 383.0, B 1401.0; serve-point win A 49.6%, B 40.1%; Elo A 1229.3, B 1491.4; model uncertainty 0.045
* Form inputs: days since last match A 14, B 239; matches on record A 246, B 252; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.006, surface_pool_high +0.000, surface_dev_loose -0.011, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dasha Plekhanova vs Dominika Podhajecka -- W35 Weston FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223203:267424:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dasha Plekhanova (`KXITFWMATCH-26NOV10PLEPOD-PLE`) | 0.96 / 0.97 (6806) | 96.5% | 89.4% | 83.9% | 81.5% [78.9%-83.9%] | -- | -- | -- | -- | PASS | -7.1 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dominika Podhajecka (`KXITFWMATCH-26NOV10PLEPOD-POD`) | 0.03 / 0.04 (9529) | 3.5% | 10.6% | 16.1% | 18.5% [16.1%-21.1%] | -- | -- | -- | -- | PASS | +7.1 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 907.0, B 894.0; serve-point win A 57.8%, B 51.6%; Elo A 1522.2, B 1274.8; model uncertainty 0.0251
* Form inputs: days since last match A 15, B 365; matches on record A 87, B 44; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.011, surface_dev_loose +0.007, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Adriana Reami vs Kolie Allen -- W35 Weston FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220551:222299:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kolie Allen (`KXITFWMATCH-26NOV10REAALL-ALL`) | 0.16 / 0.17 (517) | 16.5% | 26.6% | 32.5% | 30.2% [29.7%-31.6%] | -- | -- | -- | -- | WATCH | +10.1 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Adriana Reami (`KXITFWMATCH-26NOV10REAALL-REA`) | 0.83 / 0.84 (15184) | 83.5% | 73.4% | 67.5% | 69.8% [68.5%-70.3%] | -- | -- | -- | -- | PASS | -10.1 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 549.0, B 697.0; serve-point win A 57.1%, B 47.6%; Elo A 1388.0, B 1235.3; model uncertainty 0.0092
* Form inputs: days since last match A 12, B 197; matches on record A 187, B 86; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anita Sahdiieva vs Ava Catanzarite -- W35 Weston FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221370:260303:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ava Catanzarite (`KXITFWMATCH-26NOV10SAHCAT-CAT`) | 0.39 / 0.40 (16) | 39.5% | 21.6% | 51.1% | 36.5% [34.4%-37.5%] | -- | -- | -- | -- | PASS | -17.9 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anita Sahdiieva (`KXITFWMATCH-26NOV10SAHCAT-SAH`) | 0.58 / 0.61 (1) | 59.5% | 78.4% | 48.9% | 63.5% [62.5%-65.6%] | -- | -- | -- | -- | PASS | +18.9 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1325.0, B 106.0; serve-point win A 57.7%, B 48.1%; Elo A 1381.5, B 1276.9; model uncertainty 0.0153
* Form inputs: days since last match A 197, B 239; matches on record A 111, B 12; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10SAHCAT-SAH  (YES = Anita Sahdiieva)
Model: 78%
Kalshi: 60%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Franco Davila Blotte / Diego Gomez vs Boris Arias / Ignacio Carou -- ATP Challenger Lima R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-10T22:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10DAVGOMARICAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Boris Arias / Ignacio Carou (`KXATPCHALLENGERDOUBLES-26NOV10DAVGOMARICAR-ARICAR`) | 0.86 / 0.95 (625) | 90.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Franco Davila Blotte / Diego Gomez (`KXATPCHALLENGERDOUBLES-26NOV10DAVGOMARICAR-DAVGOM`) | 0.05 / 0.80 (2) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hugo Grenier vs Kyrian Jacquet -- ATP Challenger Orleans R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T22:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126409:208021:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Grenier (`KXATPCHALLENGERMATCH-26NOV10GREJAC-GRE`) | 0.20 / 0.21 (27) | 20.5% | 27.3% | 37.7% | 35.8% [33.4%-36.7%] | 22.3% | 21.2% | 21.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.8 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Kyrian Jacquet (`KXATPCHALLENGERMATCH-26NOV10GREJAC-JAC`) | 0.78 / 0.79 (920) | 78.5% | 72.7% | 62.3% | 64.2% [63.3%-66.6%] | 77.7% | 79.1% | 79.1% | MODEL_LONE_OUTLIER | PASS | -5.8 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4320.0, B 4370.0; serve-point win A 60.9%, B 34.3%; Elo A 1638.3, B 1774.4; model uncertainty 0.0163
* Form inputs: days since last match A 15, B 8; matches on record A 793, B 416; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose +0.000, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Albuquerque Dietrich / Dummer Macedo vs Napoli da Silveira / Felipe Silva -- M25 Santa Cruz do Sul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10ALBDUMNAPFEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Albuquerque Dietrich / Dummer Macedo (`KXITFDOUBLES-26NOV10ALBDUMNAPFEL-ALBDUM`) | 0.17 / 0.23 (5) | 20.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Napoli da Silveira / Felipe Silva (`KXITFDOUBLES-26NOV10ALBDUMNAPFEL-NAPFEL`) | 0.76 / 0.83 (150) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Luka Bojicic Ono vs Guilherme Barbieri Renner -- M25 Santa Cruz do Sul R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212601:214225:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luka Bojicic Ono (`KXITFMATCH-26NOV10BOJREN-BOJ`) | 0.19 / 0.24 (114) | 21.5% | 30.1% | 18.4% | 37.5% [35.5%-37.7%] | 25.7% | -- | 25.7% | KALSHI_LONE_OUTLIER | PASS | +8.6 pp | NORMAL | STALE | F / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Guilherme Barbieri Renner (`KXITFMATCH-26NOV10BOJREN-REN`) | 0.76 / 0.79 (200) | 77.5% | 69.9% | 81.6% | 62.5% [62.3%-64.5%] | 74.3% | -- | 74.3% | KALSHI_LONE_OUTLIER | PASS | -7.6 pp | NORMAL | STALE | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 206.0, B 50.0; serve-point win A 54.4%, B 41.6%; Elo A 1163.5, B 1248.8; model uncertainty 0.0113
* Form inputs: days since last match A 232, B 379; matches on record A 8, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.011, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rafael Tosetto vs Mateus Alves -- M25 Santa Cruz do Sul R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:127123:208006:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mateus Alves (`KXITFMATCH-26NOV10TOSALV-ALV`) | 0.78 / 0.88 (1) | 83.0% | 81.3% | 78.8% | 82.0% [80.2%-83.9%] | 82.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.7 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rafael Tosetto (`KXITFMATCH-26NOV10TOSALV-TOS`) | 0.12 / 0.16 (121) | 14.0% | 18.7% | 21.2% | 18.1% [16.1%-19.8%] | 17.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +4.7 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1174.0, B 2907.0; serve-point win A 58.7%, B 34.3%; Elo A 1200.6, B 1488.2; model uncertainty 0.0182
* Form inputs: days since last match A 8, B 29; matches on record A 102, B 374; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.017, surface_dev_loose -0.006, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Katerina Siniakova / Taylor Townsend vs Ellen Perez / Demi Schuurs -- WTA Finals Women Doubles Group

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-11 01:20Z
* Current expected start: 2026-11-10 23:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-10 17:21Z
* Recommended handicap-by time: 2026-11-10 22:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_FINALS) · surface ? · scheduled 2026-11-11T01:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10SINTOWPERSCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ellen Perez / Demi Schuurs (`KXWTADOUBLES-26NOV10SINTOWPERSCH-PERSCH`) | 0.12 / 0.14 (123) | 13.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Katerina Siniakova / Taylor Townsend (`KXWTADOUBLES-26NOV10SINTOWPERSCH-SINTOW`) | 0.84 / 0.87 (1407) | 85.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Joaquim Almeida vs Dakotah Bobo -- M15 Naples FL R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212760:212860:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joaquim Almeida (`KXITFMATCH-26NOV10ALMBOB-ALM`) | 0.63 / 0.65 (0) | 64.0% | 47.3% | 53.2% | 52.1% [51.0%-52.1%] | -- | -- | -- | -- | PASS | -16.7 pp | HIGH_REVIEW (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Dakotah Bobo (`KXITFMATCH-26NOV10ALMBOB-BOB`) | 0.33 / 0.34 (37) | 33.5% | 52.7% | 46.8% | 47.9% [47.9%-49.0%] | -- | -- | -- | -- | PASS | +19.2 pp | HIGH_REVIEW (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 86.0, B 547.0; serve-point win A 56.0%, B 43.4%; Elo A 1204.8, B 1193.5; model uncertainty 0.0054
* Form inputs: days since last match A 757, B 169; matches on record A 15, B 15; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10ALMBOB-BOB  (YES = Dakotah Bobo)
Model: 53%
Kalshi: 34%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nicolas Arseneault vs Niels Visker -- M25 Montreal R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208253:212531:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Arseneault (`KXITFMATCH-26NOV10ARSVIS-ARS`) | 0.43 / 0.45 (1774) | 44.0% | 38.9% | 37.7% | 38.1% [36.6%-40.9%] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.1 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Niels Visker (`KXITFMATCH-26NOV10ARSVIS-VIS`) | 0.55 / 0.57 (0) | 56.0% | 61.1% | 62.3% | 61.9% [59.1%-63.4%] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.1 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1460.0, B 3283.0; serve-point win A 65.8%, B 31.9%; Elo A 1424.6, B 1499.0; model uncertainty 0.0215
* Form inputs: days since last match A 113, B 29; matches on record A 59, B 252; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.028, surface_dev_loose -0.004, surface_dev_tight +0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Patricio Betancourt vs Matteo Covato -- M15 Zamora R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:149145:213666:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Patricio Betancourt (`KXITFMATCH-26NOV10BETCOV-BET`) | 0.10 / 0.13 (85) | 11.5% | 56.5% | 48.5% | 57.5% [53.5%-60.0%] | -- | -- | -- | -- | PASS | +45.0 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matteo Covato (`KXITFMATCH-26NOV10BETCOV-COV`) | 0.84 / 0.89 (1) | 86.5% | 43.5% | 51.5% | 42.5% [40.0%-46.5%] | -- | -- | -- | -- | PASS | -43.0 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 393.0, B 2229.0; serve-point win A 64.0%, B 37.3%; Elo A 1201.2, B 1129.1; model uncertainty 0.0327
* Form inputs: days since last match A 197, B 190; matches on record A 9, B 72; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10BETCOV-BET  (YES = Patricio Betancourt)
Model: 56%
Kalshi: 12%
Gap: +45 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Fadi Bidan vs Koki Nara -- M15 Naples FL R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:149266:213611:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fadi Bidan (`KXITFMATCH-26NOV10BIDNAR-BID`) | 0.52 / 0.55 (14) | 53.5% | 62.8% | 27.6% | 49.0% [46.9%-51.0%] | -- | -- | -- | -- | PASS | +9.3 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Koki Nara (`KXITFMATCH-26NOV10BIDNAR-NAR`) | 0.45 / 0.49 (1) | 47.0% | 37.2% | 72.4% | 51.0% [49.0%-53.1%] | -- | -- | -- | -- | PASS | -9.8 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 919.0, B 0.0; serve-point win A 61.2%, B 41.4%; Elo A 1258.8, B 1266.1; model uncertainty 0.0206
* Form inputs: days since last match A 344, B 750; matches on record A 50, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.021, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ryan Cozad vs Jesse Flores -- M15 Zamora R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132374:213743:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ryan Cozad (`KXITFMATCH-26NOV10COZFLO-COZ`) | 0.45 / 0.49 (1) | 47.0% | 28.1% | 35.3% | 38.1% [36.2%-38.1%] | -- | -- | -- | -- | PASS | -18.9 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jesse Flores (`KXITFMATCH-26NOV10COZFLO-FLO`) | 0.50 / 0.54 (100) | 52.0% | 71.9% | 64.7% | 61.9% [61.9%-63.8%] | -- | -- | -- | -- | PASS | +19.9 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 157.0, B 2047.0; serve-point win A 60.6%, B 34.8%; Elo A 1228.1, B 1309.5; model uncertainty 0.0095
* Form inputs: days since last match A 211, B 197; matches on record A 3, B 190; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10COZFLO-FLO  (YES = Jesse Flores)
Model: 72%
Kalshi: 52%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rafael De Alba vs Mauricio Schtulmann Gasca -- M15 Zamora R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208908:214271:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rafael De Alba (`KXITFMATCH-26NOV10DEASCH-DEA`) | 0.83 / 0.86 (1) | 84.5% | 31.8% | 34.2% | 28.1% [28.1%-29.0%] | -- | -- | -- | -- | PASS | -52.7 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mauricio Schtulmann Gasca (`KXITFMATCH-26NOV10DEASCH-SCH`) | 0.13 / 0.15 (100) | 14.0% | 68.2% | 65.8% | 71.9% [71.0%-71.9%] | -- | -- | -- | -- | PASS | +54.2 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1439.0, B 64.0; serve-point win A 55.7%, B 40.7%; Elo A 1198.5, B 1360.7; model uncertainty 0.0045
* Form inputs: days since last match A 197, B 218; matches on record A 35, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10DEASCH-SCH  (YES = Mauricio Schtulmann Gasca)
Model: 68%
Kalshi: 14%
Gap: +54 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Santiago Giamichelle vs Vihaan Reddy -- M15 Naples FL R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213839:214247:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Santiago Giamichelle (`KXITFMATCH-26NOV10GIARED-GIA`) | 0.51 / 0.55 (1) | 53.0% | 49.4% | 56.8% | 50.0% [49.0%-51.6%] | 53.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.6 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Vihaan Reddy (`KXITFMATCH-26NOV10GIARED-RED`) | 0.45 / 0.47 (141) | 46.0% | 50.6% | 43.2% | 50.0% [48.4%-51.0%] | 46.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.7 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 263.0, B 276.0; serve-point win A 57.1%, B 42.8%; Elo A 1209.3, B 1215.2; model uncertainty 0.0131
* Form inputs: days since last match A 351, B 211; matches on record A 5, B 4; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maximilian Marterer vs Benjamin Thomas George -- M25 Montreal R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:109739:212259:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Benjamin Thomas George (`KXITFMATCH-26NOV10MARGEO-GEO`) | 0.18 / 0.19 (19) | 18.5% | 11.8% | 34.7% | 21.9% [8.3%-26.8%] | 19.5% | -- | 19.5% | MODEL_LONE_OUTLIER | PASS | -6.7 pp | NORMAL | STALE | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Maximilian Marterer (`KXITFMATCH-26NOV10MARGEO-MAR`) | 0.78 / 0.79 (119) | 78.5% | 88.2% | 65.3% | 78.1% [73.2%-91.7%] | 80.5% | -- | 80.5% | MODEL_LONE_OUTLIER | PASS | +9.7 pp | NORMAL | STALE | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3468.0, B 2447.0; serve-point win A 62.1%, B 46.9%; Elo A 1678.1, B 1248.9; model uncertainty 0.0926
* Form inputs: days since last match A 449, B 211; matches on record A 679, B 88; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.022, surface_pool_high -0.024, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vladislav Melnic vs Antoine Genereux -- M25 Montreal R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10MELGEN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Antoine Genereux (`KXITFMATCH-26NOV10MELGEN-GEN`) | 0.31 / 0.34 (28) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vladislav Melnic (`KXITFMATCH-26NOV10MELGEN-MEL`) | 0.63 / 0.68 (1) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alejandro Moreno vs Jan Klimas -- M25 Columbus OH R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:204737:213579:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jan Klimas (`KXITFMATCH-26NOV10MORKLI-KLI`) | 0.29 / 0.40 (1) | 34.5% | 44.6% | 29.0% | 42.7% [42.1%-43.8%] | -- | -- | -- | -- | PASS | +10.1 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alejandro Moreno (`KXITFMATCH-26NOV10MORKLI-MOR`) | 0.58 / 0.66 (1) | 62.0% | 55.4% | 71.0% | 57.3% [56.2%-57.9%] | -- | -- | -- | -- | PASS | -6.6 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 107.0, B 704.0; serve-point win A 57.3%, B 43.7%; Elo A 1268.8, B 1225.0; model uncertainty 0.008
* Form inputs: days since last match A 372, B 197; matches on record A 7, B 21; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.010, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Axel Nefve vs Alvin Nicholas Tudorica -- M25 Montreal R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208051:212202:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Axel Nefve (`KXITFMATCH-26NOV10NEFTUD-NEF`) | 0.40 / 0.41 (42) | 40.5% | 46.0% | 44.2% | 39.6% [37.2%-41.7%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.5 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alvin Nicholas Tudorica (`KXITFMATCH-26NOV10NEFTUD-TUD`) | 0.58 / 0.60 (224) | 59.0% | 54.0% | 55.8% | 60.4% [58.3%-62.8%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.0 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2734.0, B 1789.0; serve-point win A 57.3%, B 41.9%; Elo A 1297.1, B 1407.9; model uncertainty 0.0226
* Form inputs: days since last match A 225, B 246; matches on record A 148, B 106; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ilija Palavestra vs Emanuel Ivanisevic -- M25 Columbus OH R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212924:212953:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emanuel Ivanisevic (`KXITFMATCH-26NOV10PALIVA-IVA`) | 0.60 / 0.62 (49) | 61.0% | 52.8% | 29.8% | 50.0% [44.9%-56.2%] | -- | -- | -- | -- | PASS | -8.2 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ilija Palavestra (`KXITFMATCH-26NOV10PALIVA-PAL`) | 0.35 / 0.41 (27) | 38.0% | 47.2% | 70.2% | 50.0% [43.8%-55.1%] | -- | -- | -- | -- | PASS | +9.2 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 484.0, B 679.0; serve-point win A 59.9%, B 39.6%; Elo A 1176.0, B 1224.5; model uncertainty 0.0565
* Form inputs: days since last match A 218, B 183; matches on record A 11, B 19; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.015, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## David Perret vs Simon Caldwell -- M25 Columbus OH R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10PERCAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Simon Caldwell (`KXITFMATCH-26NOV10PERCAL-CAL`) | 0.86 / 0.89 (0) | 87.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| David Perret (`KXITFMATCH-26NOV10PERCAL-PER`) | 0.10 / 0.12 (100) | 11.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Justin Roberts vs Gavin Goode -- M15 Naples FL R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:134490:213836:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gavin Goode (`KXITFMATCH-26NOV10ROBGOO-GOO`) | 0.79 / 0.81 (8) | 80.0% | 54.7% | 37.5% | 56.1% [51.0%-61.1%] | 78.6% | -- | 78.6% | MODEL_LONE_OUTLIER | PASS | -25.3 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Justin Roberts (`KXITFMATCH-26NOV10ROBGOO-ROB`) | 0.17 / 0.21 (203) | 19.0% | 45.3% | 62.5% | 43.9% [38.9%-49.0%] | 21.4% | -- | 21.4% | KALSHI_LONE_OUTLIER | PASS | +26.3 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 930.0, B 444.0; serve-point win A 61.5%, B 37.6%; Elo A 1241.1, B 1320.1; model uncertainty 0.0505
* Form inputs: days since last match A 211, B 197; matches on record A 152, B 10; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10ROBGOO-ROB  (YES = Justin Roberts)
Model: 45%
Kalshi: 19%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_KALSHI
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hiroki Sakagawa vs Hanamichi Carvajal Suazo -- M25 Columbus OH R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209991:212243:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hanamichi Carvajal Suazo (`KXITFMATCH-26NOV10SAKCAR-CAR`) | 0.09 / 0.16 (26) | 12.5% | 58.8% | 56.2% | 62.8% [62.2%-63.3%] | -- | -- | -- | -- | PASS | +46.3 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Hiroki Sakagawa (`KXITFMATCH-26NOV10SAKCAR-SAK`) | 0.86 / 0.88 (35) | 87.0% | 41.2% | 43.8% | 37.2% [36.7%-37.8%] | -- | -- | -- | -- | PASS | -45.8 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 42.0, B 121.0; serve-point win A 58.4%, B 39.9%; Elo A 1202.3, B 1293.2; model uncertainty 0.0051
* Form inputs: days since last match A 358, B 302; matches on record A 9, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10SAKCAR-CAR  (YES = Hanamichi Carvajal Suazo)
Model: 59%
Kalshi: 12%
Gap: +46 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matias Soto vs Oswaldo Alejandro Reyes Tirado -- M15 Zamora R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207130:213783:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oswaldo Alejandro Reyes Tirado (`KXITFMATCH-26NOV10SOTREY-REY`) | 0.05 / 0.06 (275) | 5.5% | 8.9% | 13.2% | 11.3% [9.4%-12.4%] | -- | -- | -- | -- | PASS | +3.4 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matias Soto (`KXITFMATCH-26NOV10SOTREY-SOT`) | 0.92 / 0.94 (0) | 93.0% | 91.1% | 86.9% | 88.7% [87.6%-90.6%] | -- | -- | -- | -- | PASS | -1.9 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4186.0, B 411.0; serve-point win A 64.0%, B 46.4%; Elo A 1586.6, B 1215.7; model uncertainty 0.0149
* Form inputs: days since last match A 22, B 197; matches on record A 288, B 9; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marlon Vankan vs Dante Pagani -- M15 Roldan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207535:213677:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dante Pagani (`KXITFMATCH-26NOV10VANPAG-PAG`) | 0.54 / 0.58 (24) | 56.0% | 39.0% | 34.6% | 36.6% [34.6%-37.6%] | -- | -- | -- | -- | PASS | -17.1 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marlon Vankan (`KXITFMATCH-26NOV10VANPAG-VAN`) | 0.41 / 0.47 (33) | 44.0% | 61.1% | 65.4% | 63.4% [62.4%-65.4%] | -- | -- | -- | -- | PASS | +17.1 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2564.0, B 701.0; serve-point win A 58.1%, B 44.1%; Elo A 1358.3, B 1270.6; model uncertainty 0.0154
* Form inputs: days since last match A 204, B 8; matches on record A 226, B 24; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10VANPAG-VAN  (YES = Marlon Vankan)
Model: 61%
Kalshi: 44%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofia Elena Cabezas Dominguez vs Dasha Ivanova -- W35 Weston FL R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214007:221982:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Elena Cabezas Dominguez (`KXITFWMATCH-26NOV10CABIVA-CAB`) | 0.66 / 0.69 (407) | 67.5% | 67.4% | 59.5% | 60.5% [55.8%-67.0%] | -- | -- | -- | -- | PASS | -0.1 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dasha Ivanova (`KXITFWMATCH-26NOV10CABIVA-IVA`) | 0.31 / 0.34 (1) | 32.5% | 32.6% | 40.5% | 39.5% [33.0%-44.2%] | -- | -- | -- | -- | WATCH | +0.1 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1826.0, B 2204.0; serve-point win A 56.0%, B 47.4%; Elo A 1456.8, B 1377.3; model uncertainty 0.056
* Form inputs: days since last match A 204, B 197; matches on record A 71, B 503; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.015, surface_dev_loose +0.065, surface_dev_tight -0.047
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zaire Clarke vs Ilinca Dalina Amariei -- W35 Weston FL R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221168:269838:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ilinca Dalina Amariei (`KXITFWMATCH-26NOV10CLAAMA-AMA`) | 0.67 / 0.69 (4) | 68.0% | 88.4% | 88.0% | 81.8% [80.4%-84.2%] | -- | -- | -- | -- | PASS | +20.4 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zaire Clarke (`KXITFWMATCH-26NOV10CLAAMA-CLA`) | 0.30 / 0.32 (5) | 31.0% | 11.6% | 12.0% | 18.2% [15.8%-19.6%] | -- | -- | -- | -- | PASS | -19.4 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 234.0, B 2360.0; serve-point win A 49.4%, B 41.6%; Elo A 1356.4, B 1601.5; model uncertainty 0.0188
* Form inputs: days since last match A 561, B 337; matches on record A 5, B 325; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10CLAAMA-AMA  (YES = Ilinca Dalina Amariei)
Model: 88%
Kalshi: 68%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Martina Colmegna vs Ipek Oz -- W50 Chihuahua R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211820:213998:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martina Colmegna (`KXITFWMATCH-26NOV10COLOZX-COL`) | 0.15 / 0.17 (1) | 16.0% | 46.4% | 80.3% | 66.1% [45.7%-74.8%] | 21.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +30.4 pp | EXTREME (DATA_WARNING) | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ipek Oz (`KXITFWMATCH-26NOV10COLOZX-OZX`) | 0.81 / 0.85 (295) | 83.0% | 53.6% | 19.7% | 33.9% [25.2%-54.3%] | 78.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -29.4 pp | EXTREME (DATA_WARNING) | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1755.0, B 2398.0; serve-point win A 53.8%, B 45.5%; Elo A 1568.8, B 1597.1; model uncertainty 0.1452
* Form inputs: days since last match A 12, B 63; matches on record A 460, B 487; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10COLOZX-COL  (YES = Martina Colmegna)
Model: 46%
Kalshi: 16%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.030, surface_pool_high +0.024, surface_dev_loose +0.010, surface_dev_tight -0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Salma Djoubri vs Alina Shcherbinina -- W35 Weston FL R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220305:221278:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Salma Djoubri (`KXITFWMATCH-26NOV10DJOSHC-DJO`) | 0.25 / 0.26 (1005) | 25.5% | 70.2% | 43.1% | 65.6% [59.6%-72.2%] | 26.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +44.7 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alina Shcherbinina (`KXITFWMATCH-26NOV10DJOSHC-SHC`) | 0.73 / 0.76 (108) | 74.5% | 29.8% | 56.9% | 34.4% [27.8%-40.4%] | 73.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -44.7 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 169.0, B 127.0; serve-point win A 54.0%, B 50.0%; Elo A 1456.4, B 1328.9; model uncertainty 0.0632
* Form inputs: days since last match A 358, B 267; matches on record A 168, B 55; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10DJOSHC-DJO  (YES = Salma Djoubri)
Model: 70%
Kalshi: 26%
Gap: +45 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.048, surface_pool_high -0.040, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Catarina Melleiro vs Sabrina Dias -- W15 São Carlos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223226:260959:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sabrina Dias (`KXITFWMATCH-26NOV10MELDIA-DIA`) | 0.74 / 0.78 (277) | 76.0% | 51.1% | 85.5% | 62.6% [61.6%-63.6%] | -- | -- | -- | -- | PASS | -24.9 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Catarina Melleiro (`KXITFWMATCH-26NOV10MELDIA-MEL`) | 0.21 / 0.22 (32) | 21.5% | 48.9% | 14.5% | 37.4% [36.4%-38.4%] | -- | -- | -- | -- | PASS | +27.4 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 986.0, B 47.0; serve-point win A 53.1%, B 46.7%; Elo A 1119.3, B 1201.1; model uncertainty 0.0101
* Form inputs: days since last match A 232, B 491; matches on record A 71, B 3; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10MELDIA-MEL  (YES = Catarina Melleiro)
Model: 49%
Kalshi: 22%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amanda Carolina Nava Elkin vs Anastasia Zolotareva -- W50 Chihuahua R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221209:222158:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amanda Carolina Nava Elkin (`KXITFWMATCH-26NOV10NAVZOL-NAV`) | 0.02 / 0.03 (535) | 2.5% | 2.0% | 2.9% | 4.6% [3.1%-6.4%] | -- | -- | -- | -- | WATCH | -0.5 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anastasia Zolotareva (`KXITFWMATCH-26NOV10NAVZOL-ZOL`) | 0.97 / 0.98 (279) | 97.5% | 98.0% | 97.1% | 95.4% [93.6%-96.9%] | -- | -- | -- | -- | PASS | +0.5 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 845.0, B 3371.0; serve-point win A 43.7%, B 40.9%; Elo A 1172.9, B 1660.9; model uncertainty 0.0165
* Form inputs: days since last match A 246, B 64; matches on record A 106, B 407; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.001, surface_dev_loose -0.004, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Noatto / Pinheiro da Cruz Junior vs Marcos Angelico / Rodrigues Longobardi -- M25 Santa Cruz do Sul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 23:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10NOAPINMARROD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcos Angelico / Rodrigues Longobardi (`KXITFDOUBLES-26NOV10NOAPINMARROD-MARROD`) | 0.12 / 0.21 (24) | 16.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Noatto / Pinheiro da Cruz Junior (`KXITFDOUBLES-26NOV10NOAPINMARROD-NOAPIN`) | 0.78 / 0.84 (61) | 81.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Alessandro Rubini vs Franco Roncadelli -- ATP Challenger Lima R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 23:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-10T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208364:214240:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Franco Roncadelli (`KXATPCHALLENGERMATCH-26NOV10RUBRON-RON`) | 0.94 / 0.97 (8626) | 95.5% | 87.5% | 95.9% | 82.3% [78.5%-86.8%] | 93.6% | 93.4% | -- | INSUFFICIENT_INPUTS | PASS | -8.0 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alessandro Rubini (`KXATPCHALLENGERMATCH-26NOV10RUBRON-RUB`) | 0.03 / 0.05 (31) | 4.0% | 12.5% | 4.1% | 17.6% [13.2%-21.5%] | 6.4% | 5.0% | 5.0% | MODEL_LONE_OUTLIER | PASS | +8.5 pp | NORMAL | STALE | F / POOR | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 160.0, B 4282.0; serve-point win A 51.3%, B 40.1%; Elo A 1335.9, B 1578.4; model uncertainty 0.0418
* Form inputs: days since last match A 337, B 8; matches on record A 3, B 326; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.007, surface_dev_loose -0.007, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Bernardes / Rosa Dourado vs Gomes Ferreira / Schincariol Delatorre Barbosa -- W15 São Carlos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 23:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10BERROSGOMSCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bernardes / Rosa Dourado (`KXITFWDOUBLES-26NOV10BERROSGOMSCH-BERROS`) | 0.43 / 0.89 (1) | 66.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gomes Ferreira / Schincariol Delatorre Barbosa (`KXITFWDOUBLES-26NOV10BERROSGOMSCH-GOMSCH`) | 0.11 / 0.31 (12) | 21.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Konishi Camargo Silva / Souza vs Maia Citolino / de Jesus Ribeiro Silveira -- W15 São Carlos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 23:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10KONSOUMAIDEJ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Konishi Camargo Silva / Souza (`KXITFWDOUBLES-26NOV10KONSOUMAIDEJ-KONSOU`) | 0.76 / 0.90 (1) | 83.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maia Citolino / de Jesus Ribeiro Silveira (`KXITFWDOUBLES-26NOV10KONSOUMAIDEJ-MAIDEJ`) | 0.09 / 0.19 (5) | 14.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Apostolou / Syed vs Sebastian Dominguez Collado / Greschner -- M15 Naples FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10APOSYESEBGRE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Apostolou / Syed (`KXITFDOUBLES-26NOV10APOSYESEBGRE-APOSYE`) | 0.43 / 0.51 (48) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sebastian Dominguez Collado / Greschner (`KXITFDOUBLES-26NOV10APOSYESEBGRE-SEBGRE`) | 0.52 / 0.54 (53) | 53.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Alfonso Costamagna vs Tomas Martinez -- M15 Roldan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10COSMAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alfonso Costamagna (`KXITFMATCH-26NOV10COSMAR-COS`) | 0.06 / 0.07 (229) | 6.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tomas Martinez (`KXITFMATCH-26NOV10COSMAR-MAR`) | 0.93 / 0.95 (8) | 94.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Leite / Sakamoto vs Eduardo Cuellar Lorberg / Horacio Messa -- M25 Santa Cruz do Sul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10LEISAKEDUHOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eduardo Cuellar Lorberg / Horacio Messa (`KXITFDOUBLES-26NOV10LEISAKEDUHOR-EDUHOR`) | 0.11 / 0.19 (33) | 15.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Leite / Sakamoto (`KXITFDOUBLES-26NOV10LEISAKEDUHOR-LEISAK`) | 0.83 / 0.86 (52) | 84.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## McCormick / Witten vs Colby / Dollenberg -- M15 Naples FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10MCCWITCOLDOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Colby / Dollenberg (`KXITFDOUBLES-26NOV10MCCWITCOLDOL-COLDOL`) | 0.12 / 0.20 (24) | 16.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| McCormick / Witten (`KXITFDOUBLES-26NOV10MCCWITCOLDOL-MCCWIT`) | 0.75 / 0.84 (3) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nittmann / Watzka vs Barrett / Corwin -- M15 Naples FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10NITWATBARCOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barrett / Corwin (`KXITFDOUBLES-26NOV10NITWATBARCOR-BARCOR`) | 0.48 / 0.69 (11) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nittmann / Watzka (`KXITFDOUBLES-26NOV10NITWATBARCOR-NITWAT`) | 0.36 / 0.46 (21) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Rogelio Madrazo Morales / Orsanic vs Sheldon / Sheldon -- M15 Naples FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10ROGORSSHESHE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rogelio Madrazo Morales / Orsanic (`KXITFDOUBLES-26NOV10ROGORSSHESHE-ROGORS`) | 0.05 / 0.14 (22) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sheldon / Sheldon (`KXITFDOUBLES-26NOV10ROGORSSHESHE-SHESHE`) | 0.80 / 0.90 (1) | 85.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Victor Couto Loureiro / Ribeiro vs Domarco Carlos / Fortes -- M25 Santa Cruz do Sul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10VICRIBDOMFOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Domarco Carlos / Fortes (`KXITFDOUBLES-26NOV10VICRIBDOMFOR-DOMFOR`) | 0.04 / 0.14 (30) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Victor Couto Loureiro / Ribeiro (`KXITFDOUBLES-26NOV10VICRIBDOMFOR-VICRIB`) | 0.89 / 0.91 (3) | 90.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Bohrer Martins / Ccuno vs Hossam Salah / Korpanec Davies -- W35 Weston FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10BOHCCUHOSKOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bohrer Martins / Ccuno (`KXITFWDOUBLES-26NOV10BOHCCUHOSKOR-BOHCCU`) | 0.55 / 0.66 (55) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hossam Salah / Korpanec Davies (`KXITFWDOUBLES-26NOV10BOHCCUHOSKOR-HOSKOR`) | 0.40 / 0.41 (74) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Kayla Cross vs Judith Hernandez Miranda -- W50 Chihuahua R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222665:239436:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kayla Cross (`KXITFWMATCH-26NOV10CROHER-CRO`) | 0.93 / 0.96 (314) | 94.5% | 93.4% | 92.5% | 81.1% [75.7%-85.7%] | -- | -- | -- | -- | PASS | -1.1 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Judith Hernandez Miranda (`KXITFWMATCH-26NOV10CROHER-HER`) | 0.04 / 0.05 (137) | 4.5% | 6.6% | 7.5% | 18.9% [14.3%-24.3%] | -- | -- | -- | -- | PASS | +2.1 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2619.0, B 185.0; serve-point win A 59.1%, B 52.2%; Elo A 1541.9, B 1309.8; model uncertainty 0.0504
* Form inputs: days since last match A 57, B 197; matches on record A 237, B 110; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.046, surface_pool_high -0.055, surface_dev_loose +0.004, surface_dev_tight -0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rinon Okuwaki vs Neda Rahimkhani -- W15 Lincoln NE R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:239477:260856:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rinon Okuwaki (`KXITFWMATCH-26NOV10OKURAH-OKU`) | 0.80 / 0.84 (6) | 82.0% | 79.7% | 30.5% | 63.6% [61.6%-66.6%] | -- | -- | -- | -- | PASS | -2.3 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Neda Rahimkhani (`KXITFWMATCH-26NOV10OKURAH-RAH`) | 0.14 / 0.17 (23) | 15.5% | 20.3% | 69.5% | 36.4% [33.4%-38.4%] | -- | -- | -- | -- | PASS | +4.8 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 739.0, B 0.0; serve-point win A 56.1%, B 50.1%; Elo A 1368.7, B 1268.9; model uncertainty 0.025
* Form inputs: days since last match A 365, B 1485; matches on record A 168, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.030, surface_pool_high -0.020, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Catherine Rennard vs Reya Coe -- W15 Lincoln NE R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264061:269911:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Reya Coe (`KXITFWMATCH-26NOV10RENCOE-COE`) | 0.06 / 0.08 (10) | 7.0% | 41.4% | 69.9% | 48.9% [48.9%-48.9%] | -- | -- | -- | -- | PASS | +34.4 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Catherine Rennard (`KXITFWMATCH-26NOV10RENCOE-REN`) | 0.90 / 0.92 (25) | 91.0% | 58.6% | 30.1% | 51.1% [51.1%-51.1%] | -- | -- | -- | -- | PASS | -32.4 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 378.0, B 0.0; serve-point win A 55.0%, B 46.7%; Elo A 1283.4, B 1277.9; model uncertainty 0.0
* Form inputs: days since last match A 204, B 736; matches on record A 7, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10RENCOE-COE  (YES = Reya Coe)
Model: 41%
Kalshi: 7%
Gap: +34 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Karlin Schock vs Abigail Schumann -- W15 Lincoln NE R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10SCHSCH2:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karlin Schock (`KXITFWMATCH-26NOV10SCHSCH2-SCH`) | 0.94 / 0.97 (200) | 95.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Abigail Schumann (`KXITFWMATCH-26NOV10SCHSCH2-SCH2`) | 0.03 / 0.05 (201) | 4.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sophie Suh vs Meghan Rowley -- W15 Lincoln NE R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10SUHROW:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Meghan Rowley (`KXITFWMATCH-26NOV10SUHROW-ROW`) | 0.03 / 0.05 (94) | 4.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sophie Suh (`KXITFWMATCH-26NOV10SUHROW-SUH`) | 0.93 / 0.96 (61) | 94.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anastasia Tikhonova vs Miriana Tona -- W50 Chihuahua R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:210847:221073:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasia Tikhonova (`KXITFWMATCH-26NOV10TIKTON-TIK`) | 0.68 / 0.70 (23) | 69.0% | 50.6% | 41.0% | 42.6% [40.5%-47.3%] | -- | -- | -- | -- | PASS | -18.4 pp | HIGH_REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Miriana Tona (`KXITFWMATCH-26NOV10TIKTON-TON`) | 0.29 / 0.32 (144) | 30.5% | 49.4% | 59.0% | 57.4% [52.7%-59.5%] | -- | -- | -- | -- | WATCH | +18.9 pp | HIGH_REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2660.0, B 2556.0; serve-point win A 55.2%, B 44.9%; Elo A 1479.7, B 1511.0; model uncertainty 0.034
* Form inputs: days since last match A 37, B 64; matches on record A 387, B 410; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10TIKTON-TON  (YES = Miriana Tona)
Model: 49%
Kalshi: 30%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: STALE_KALSHI_QUOTE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cristina Bucsa / Nicole Melichar-Martinez vs Sara Errani / Jasmine Paolini -- WTA Finals Women Doubles Group

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-11 02:30Z
* Current expected start: 2026-11-11 00:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-10 17:21Z
* Recommended handicap-by time: 2026-11-10 23:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_FINALS) · surface ? · scheduled 2026-11-11T02:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10BUCMELERRPAO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cristina Bucsa / Nicole Melichar-Martinez (`KXWTADOUBLES-26NOV10BUCMELERRPAO-BUCMEL`) | 0.42 / 0.46 (400) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sara Errani / Jasmine Paolini (`KXWTADOUBLES-26NOV10BUCMELERRPAO-ERRPAO`) | 0.53 / 0.57 (85) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Aguilar Cardozo / Del Pino vs Bruna / Dellien -- M15 Roldan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 00:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10AGUDELBRUDEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aguilar Cardozo / Del Pino (`KXITFDOUBLES-26NOV10AGUDELBRUDEL-AGUDEL`) | 0.29 / 0.69 (82) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bruna / Dellien (`KXITFDOUBLES-26NOV10AGUDELBRUDEL-BRUDEL`) | 0.45 / 0.82 (139) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Arseneault / Horwood vs De Jonge / Opitz -- M25 Montreal R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 00:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10ARSHORDEJOPI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arseneault / Horwood (`KXITFDOUBLES-26NOV10ARSHORDEJOPI-ARSHOR`) | 0.17 / 0.30 (31) | 23.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| De Jonge / Opitz (`KXITFDOUBLES-26NOV10ARSHORDEJOPI-DEJOPI`) | 0.69 / 0.81 (132) | 75.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Brostrom Poulsen / Slavic vs Lapalme / Roussel -- M25 Montreal R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 00:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10BROSLALAPROU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brostrom Poulsen / Slavic (`KXITFDOUBLES-26NOV10BROSLALAPROU-BROSLA`) | 0.88 / 0.94 (125) | 91.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lapalme / Roussel (`KXITFDOUBLES-26NOV10BROSLALAPROU-LAPROU`) | 0.05 / 0.06 (26) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Cigarran / Farjat vs Agustin Pernas / Ariel Vazquez -- M15 Roldan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 00:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10CIGFARAGUARI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Agustin Pernas / Ariel Vazquez (`KXITFDOUBLES-26NOV10CIGFARAGUARI-AGUARI`) | 0.14 / 0.78 (400) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cigarran / Farjat (`KXITFDOUBLES-26NOV10CIGFARAGUARI-CIGFAR`) | 0.72 / 0.90 (1) | 81.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## David Cassan / Sabina vs Perlov / Ratti -- M15 Roldan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 00:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10DAVSABPERRAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| David Cassan / Sabina (`KXITFDOUBLES-26NOV10DAVSABPERRAT-DAVSAB`) | 0.04 / 0.89 (4) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Perlov / Ratti (`KXITFDOUBLES-26NOV10DAVSABPERRAT-PERRAT`) | 0.04 / 0.89 (4) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dean / Tripathi vs Nobel / St-Hilaire -- M25 Montreal R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 00:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10DEATRINOBSTH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dean / Tripathi (`KXITFDOUBLES-26NOV10DEATRINOBSTH-DEATRI`) | 0.84 / 0.90 (1) | 87.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nobel / St-Hilaire (`KXITFDOUBLES-26NOV10DEATRINOBSTH-NOBSTH`) | 0.05 / 0.10 (21) | 7.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Giles Hussey vs Michael Zheng -- ATP Challenger Knoxville R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 00:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-11T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208144:210116:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giles Hussey (`KXATPCHALLENGERMATCH-26NOV10HUSZHE-HUS`) | 0.23 / 0.24 (967) | 23.5% | 29.9% | 34.9% | 32.6% [29.9%-34.5%] | -- | -- | -- | -- | SHADOW_BET | +6.4 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Michael Zheng (`KXATPCHALLENGERMATCH-26NOV10HUSZHE-ZHE`) | 0.76 / 0.77 (1936) | 76.5% | 70.1% | 65.1% | 67.4% [65.5%-70.1%] | -- | -- | -- | -- | PASS | -6.4 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4682.0, B 3352.0; serve-point win A 58.2%, B 37.7%; Elo A 1601.3, B 1755.6; model uncertainty 0.023
* Form inputs: days since last match A 134, B 8; matches on record A 310, B 142; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.019, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Rybakov / Vance vs Kuhar / Roh -- M25 Montreal R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 00:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10RYBVANKUHROH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kuhar / Roh (`KXITFDOUBLES-26NOV10RYBVANKUHROH-KUHROH`) | 0.34 / 0.46 (46) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rybakov / Vance (`KXITFDOUBLES-26NOV10RYBVANKUHROH-RYBVAN`) | 0.50 / 0.62 (65) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Alize Lim vs Victoria Rodriguez -- W50 Chihuahua R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 00:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:202430:211874:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alize Lim (`KXITFWMATCH-26NOV10LIMROD-LIM`) | 0.23 / 0.24 (32) | 23.5% | 46.4% | 69.9% | 61.1% [55.4%-65.1%] | -- | -- | -- | -- | WATCH | +22.9 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Victoria Rodriguez (`KXITFWMATCH-26NOV10LIMROD-ROD`) | 0.75 / 0.77 (180) | 76.0% | 53.6% | 30.1% | 38.9% [34.9%-44.6%] | -- | -- | -- | -- | PASS | -22.4 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1334.0, B 2050.0; serve-point win A 46.1%, B 53.2%; Elo A 1515.3, B 1501.0; model uncertainty 0.0486
* Form inputs: days since last match A 239, B 14; matches on record A 584, B 576; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10LIMROD-LIM  (YES = Alize Lim)
Model: 46%
Kalshi: 24%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Isabella Marton vs Demi Tran -- W50 Chihuahua R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 00:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221994:260400:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isabella Marton (`KXITFWMATCH-26NOV10MARTRA-MAR`) | 0.40 / 0.42 (197) | 41.0% | 41.4% | 48.4% | 41.5% [36.4%-44.1%] | -- | -- | -- | -- | PASS | +0.4 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Demi Tran (`KXITFWMATCH-26NOV10MARTRA-TRA`) | 0.57 / 0.58 (59) | 57.5% | 58.6% | 51.6% | 58.5% [55.9%-63.6%] | -- | -- | -- | -- | PASS | +1.1 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1055.0, B 1766.0; serve-point win A 51.7%, B 46.7%; Elo A 1253.9, B 1339.3; model uncertainty 0.0388
* Form inputs: days since last match A 101, B 15; matches on record A 32, B 291; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.026, surface_dev_loose +0.026, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alberto Odiseo Alvarado Berrospi vs Alan Sau Franco -- M15 Zamora R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206827:208726:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alberto Odiseo Alvarado Berrospi (`KXITFMATCH-26NOV10ALVSAU-ALV`) | 0.65 / 0.66 (73) | 65.5% | 41.4% | 46.9% | 42.8% [41.8%-43.8%] | -- | -- | -- | -- | PASS | -24.1 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alan Sau Franco (`KXITFMATCH-26NOV10ALVSAU-SAU`) | 0.32 / 0.35 (199) | 33.5% | 58.6% | 53.1% | 57.2% [56.2%-58.2%] | -- | -- | -- | -- | PASS | +25.1 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 570.0, B 649.0; serve-point win A 58.4%, B 39.9%; Elo A 1088.9, B 1147.7; model uncertainty 0.0101
* Form inputs: days since last match A 344, B 204; matches on record A 63, B 35; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10ALVSAU-SAU  (YES = Alan Sau Franco)
Model: 59%
Kalshi: 34%
Gap: +25 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Michael Antonius vs Michael Bassem Sobhy -- M25 Columbus OH R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209971:214004:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michael Antonius (`KXITFMATCH-26NOV10ANTBAS-ANT`) | 0.88 / 0.91 (498) | 89.5% | 60.8% | 46.9% | 53.0% [51.0%-56.1%] | -- | -- | -- | -- | PASS | -28.7 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Michael Bassem Sobhy (`KXITFMATCH-26NOV10ANTBAS-BAS`) | 0.09 / 0.11 (28) | 10.0% | 39.2% | 53.0% | 46.9% [43.9%-49.0%] | -- | -- | -- | -- | PASS | +29.2 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 903.0, B 3195.0; serve-point win A 62.7%, B 39.5%; Elo A 1423.2, B 1376.1; model uncertainty 0.0255
* Form inputs: days since last match A 8, B 204; matches on record A 22, B 157; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10ANTBAS-BAS  (YES = Michael Bassem Sobhy)
Model: 39%
Kalshi: 10%
Gap: +29 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.015, surface_dev_loose +0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Micah Braswell vs Theo Papamalamis -- M25 Columbus OH R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209334:210494:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Micah Braswell (`KXITFMATCH-26NOV10BRAPAP-BRA`) | 0.28 / 0.32 (233) | 30.0% | 43.5% | 27.7% | 42.7% [36.1%-57.2%] | -- | -- | -- | -- | WATCH | +13.5 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Theo Papamalamis (`KXITFMATCH-26NOV10BRAPAP-PAP`) | 0.67 / 0.68 (78) | 67.5% | 56.5% | 72.3% | 57.3% [42.8%-63.9%] | -- | -- | -- | -- | PASS | -11.0 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1914.0, B 1714.0; serve-point win A 56.9%, B 41.8%; Elo A 1518.9, B 1441.4; model uncertainty 0.1056
* Form inputs: days since last match A 281, B 309; matches on record A 89, B 89; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose -0.016, surface_dev_tight +0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ian Lucca Cervantes Tomas vs Elijah Strode -- M15 Zamora R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210565:212486:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ian Lucca Cervantes Tomas (`KXITFMATCH-26NOV10CERSTR-CER`) | 0.50 / 0.53 (180) | 51.5% | 30.3% | 36.4% | 33.7% [32.5%-34.9%] | -- | -- | -- | -- | PASS | -21.2 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elijah Strode (`KXITFMATCH-26NOV10CERSTR-STR`) | 0.47 / 0.48 (72) | 47.5% | 69.7% | 63.6% | 66.3% [65.1%-67.5%] | -- | -- | -- | -- | PASS | +22.2 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 529.0, B 869.0; serve-point win A 62.4%, B 33.4%; Elo A 1159.9, B 1288.4; model uncertainty 0.012
* Form inputs: days since last match A 414, B 484; matches on record A 24, B 57; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10CERSTR-STR  (YES = Elijah Strode)
Model: 70%
Kalshi: 48%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hamill / Meyers vs Heck / Young -- M25 Columbus OH R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10HAMMEYHECYOU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hamill / Meyers (`KXITFDOUBLES-26NOV10HAMMEYHECYOU-HAMMEY`) | 0.04 / 0.15 (30) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Heck / Young (`KXITFDOUBLES-26NOV10HAMMEYHECYOU-HECYOU`) | 0.91 / 0.92 (1) | 91.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Anders Matta vs Maxwell McKennon -- M15 Zamora R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208297:212988:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anders Matta (`KXITFMATCH-26NOV10MATMCK-MAT`) | 0.04 / 0.05 (1334) | 4.5% | 10.4% | 15.9% | 21.6% [18.8%-23.2%] | -- | -- | -- | -- | PASS | +5.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maxwell McKennon (`KXITFMATCH-26NOV10MATMCK-MCK`) | 0.93 / 0.96 (846) | 94.5% | 89.6% | 84.1% | 78.3% [76.8%-81.2%] | -- | -- | -- | -- | PASS | -4.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 169.0, B 3096.0; serve-point win A 57.6%, B 32.5%; Elo A 1184.8, B 1399.2; model uncertainty 0.0218
* Form inputs: days since last match A 246, B 197; matches on record A 7, B 140; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luis Patino vs Blu Baker -- M15 Zamora R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106250:209124:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Blu Baker (`KXITFMATCH-26NOV10PATBAK-BAK`) | 0.88 / 0.93 (403) | 90.5% | 62.7% | 78.4% | 65.3% [59.2%-71.9%] | -- | -- | -- | -- | PASS | -27.8 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Luis Patino (`KXITFMATCH-26NOV10PATBAK-PAT`) | 0.06 / 0.13 (111) | 9.5% | 37.2% | 21.6% | 34.7% [28.1%-40.8%] | -- | -- | -- | -- | PASS | +27.8 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 673.0, B 1707.0; serve-point win A 56.8%, B 40.8%; Elo A 1342.9, B 1402.1; model uncertainty 0.0631
* Form inputs: days since last match A 1625, B 211; matches on record A 354, B 119; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10PATBAK-PAT  (YES = Luis Patino)
Model: 37%
Kalshi: 10%
Gap: +28 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Raphael Perot vs Preston Stearns -- M25 Columbus OH R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210475:212222:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raphael Perot (`KXITFMATCH-26NOV10PERSTE-PER`) | 0.61 / 0.63 (377) | 62.0% | 82.2% | 74.4% | 78.8% [77.6%-80.2%] | -- | -- | -- | -- | PASS | +20.2 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Preston Stearns (`KXITFMATCH-26NOV10PERSTE-STE`) | 0.37 / 0.39 (176) | 38.0% | 17.8% | 25.6% | 21.2% [19.8%-22.4%] | -- | -- | -- | -- | PASS | -20.2 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2367.0, B 667.0; serve-point win A 64.1%, B 43.1%; Elo A 1518.3, B 1269.8; model uncertainty 0.0129
* Form inputs: days since last match A 43, B 365; matches on record A 86, B 22; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10PERSTE-PER  (YES = Raphael Perot)
Model: 82%
Kalshi: 62%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.015, surface_dev_loose -0.001, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Allen / Reami vs Evtimova / Harding -- W35 Weston FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10ALLREAEVTHAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Allen / Reami (`KXITFWDOUBLES-26NOV10ALLREAEVTHAR-ALLREA`) | 0.69 / 0.80 (125) | 74.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Evtimova / Harding (`KXITFWDOUBLES-26NOV10ALLREAEVTHAR-EVTHAR`) | 0.18 / 0.31 (36) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Julie Bedard vs Ava Esposito Cogan -- W15 Lincoln NE R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10BEDESP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julie Bedard (`KXITFWMATCH-26NOV10BEDESP-BED`) | 0.05 / 0.06 (27) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ava Esposito Cogan (`KXITFWMATCH-26NOV10BEDESP-ESP`) | 0.92 / 0.95 (76) | 93.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Black / Jauffret vs Eisch / Eisch -- W35 Weston FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10BLAJAUEISEIS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Black / Jauffret (`KXITFWDOUBLES-26NOV10BLAJAUEISEIS-BLAJAU`) | 0.06 / 0.69 (3) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eisch / Eisch (`KXITFWDOUBLES-26NOV10BLAJAUEISEIS-EISEIS`) | 0.89 / 0.91 (143) | 90.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Catherine Gagnon vs Tiziana Rossini -- W15 Lincoln NE R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222689:263675:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Catherine Gagnon (`KXITFWMATCH-26NOV10GAGROS-GAG`) | 0.64 / 0.69 (10) | 66.5% | 48.3% | 68.0% | 52.7% [51.1%-53.7%] | -- | -- | -- | -- | PASS | -18.2 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tiziana Rossini (`KXITFWMATCH-26NOV10GAGROS-ROS`) | 0.32 / 0.33 (10) | 32.5% | 51.7% | 32.0% | 47.3% [46.3%-48.9%] | -- | -- | -- | -- | PASS | +19.2 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 56.0, B 178.0; serve-point win A 52.9%, B 46.8%; Elo A 1274.3, B 1262.6; model uncertainty 0.0134
* Form inputs: days since last match A 372, B 372; matches on record A 8, B 69; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10GAGROS-ROS  (YES = Tiziana Rossini)
Model: 52%
Kalshi: 32%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hu / Lahey vs Alicea / Snells -- W35 Weston FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10HUXLAHALISNE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alicea / Snells (`KXITFWDOUBLES-26NOV10HUXLAHALISNE-ALISNE`) | 0.24 / 0.39 (42) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hu / Lahey (`KXITFWDOUBLES-26NOV10HUXLAHALISNE-HUXLAH`) | 0.57 / 0.71 (86) | 64.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Kawano Cho / Meabe vs Tiemi Sakada da Costa / Santos -- W15 São Carlos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10KAWMEATIESAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kawano Cho / Meabe (`KXITFWDOUBLES-26NOV10KAWMEATIESAN-KAWMEA`) | 0.09 / 0.89 (4) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tiemi Sakada da Costa / Santos (`KXITFWDOUBLES-26NOV10KAWMEATIESAN-TIESAN`) | 0.05 / 0.64 (1) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Aleksandra Kyselova vs Katelynn Kock -- W15 Lincoln NE R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10KYSKOC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katelynn Kock (`KXITFWMATCH-26NOV10KYSKOC-KOC`) | 0.39 / 0.42 (79) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aleksandra Kyselova (`KXITFWMATCH-26NOV10KYSKOC-KYS`) | 0.56 / 0.62 (59) | 59.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Martinez / Reed vs Pulchartova / Tahiri -- W35 Weston FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10MARREEPULTAH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martinez / Reed (`KXITFWDOUBLES-26NOV10MARREEPULTAH-MARREE`) | 0.77 / 0.88 (208) | 82.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pulchartova / Tahiri (`KXITFWDOUBLES-26NOV10MARREEPULTAH-PULTAH`) | 0.10 / 0.23 (60) | 16.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Sara Shumate vs Briana Rademacher -- W15 Lincoln NE R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10SHURAD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Briana Rademacher (`KXITFWMATCH-26NOV10SHURAD-RAD`) | 0.05 / 0.09 (276) | 7.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sara Shumate (`KXITFWMATCH-26NOV10SHURAD-SHU`) | 0.90 / 0.94 (130) | 92.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rodrigo Alujas vs Patricio Alvarado -- M15 Zamora R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105419:212286:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rodrigo Alujas (`KXITFMATCH-26NOV10ALUALV-ALU`) | 0.56 / 0.69 (6) | 62.5% | 85.9% | 80.0% | 80.7% [78.4%-83.2%] | -- | -- | -- | -- | PASS | +23.4 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Patricio Alvarado (`KXITFMATCH-26NOV10ALUALV-ALV`) | 0.27 / 0.47 (601) | 37.0% | 14.1% | 20.0% | 19.3% [16.8%-21.6%] | -- | -- | -- | -- | PASS | -22.9 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2335.0, B 867.0; serve-point win A 61.6%, B 46.6%; Elo A 1295.7, B 1045.8; model uncertainty 0.0238
* Form inputs: days since last match A 204, B 225; matches on record A 83, B 82; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10ALUALV-ALU  (YES = Rodrigo Alujas)
Model: 86%
Kalshi: 62%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dante Carlos Teramo vs Nicolas Esteban Rico Arias -- M15 Zamora R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208381:213929:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Esteban Rico Arias (`KXITFMATCH-26NOV10TERRIC-RIC`) | 0.31 / 0.47 (28) | 39.0% | 24.0% | 34.7% | 27.3% [26.5%-27.7%] | -- | -- | -- | -- | PASS | -15.0 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dante Carlos Teramo (`KXITFMATCH-26NOV10TERRIC-TER`) | 0.52 / 0.63 (2) | 57.5% | 76.0% | 65.3% | 72.7% [72.3%-73.5%] | -- | -- | -- | -- | PASS | +18.5 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 114.0, B 684.0; serve-point win A 60.7%, B 44.6%; Elo A 1236.4, B 1061.1; model uncertainty 0.0062
* Form inputs: days since last match A 386, B 197; matches on record A 2, B 20; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10TERRIC-TER  (YES = Dante Carlos Teramo)
Model: 76%
Kalshi: 57%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jessica Hinojosa Gomez vs Midori Castillo Meza -- W50 Chihuahua R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 02:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213739:221915:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Midori Castillo Meza (`KXITFWMATCH-26NOV10HINCAS-CAS`) | 0.25 / 0.28 (41) | 26.5% | 34.8% | 36.4% | 37.4% [35.4%-40.0%] | -- | -- | -- | -- | WATCH | +8.3 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jessica Hinojosa Gomez (`KXITFWMATCH-26NOV10HINCAS-HIN`) | 0.70 / 0.71 (86) | 70.5% | 65.2% | 63.6% | 62.6% [60.0%-64.6%] | -- | -- | -- | -- | PASS | -5.3 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1620.0, B 835.0; serve-point win A 54.4%, B 48.5%; Elo A 1369.3, B 1281.9; model uncertainty 0.0229
* Form inputs: days since last match A 15, B 211; matches on record A 177, B 65; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.010, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kelly Keller vs Jenna Dean -- W15 Lincoln NE R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 02:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221148:260103:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jenna Dean (`KXITFWMATCH-26NOV10KELDEA-DEA`) | 0.33 / 0.34 (161) | 33.5% | 30.6% | 38.9% | 37.4% [36.3%-37.4%] | -- | -- | -- | -- | PASS | -2.9 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kelly Keller (`KXITFWMATCH-26NOV10KELDEA-KEL`) | 0.64 / 0.66 (36) | 65.0% | 69.4% | 61.1% | 62.6% [62.6%-63.7%] | -- | -- | -- | -- | PASS | +4.4 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 436.0, B 801.0; serve-point win A 52.9%, B 50.9%; Elo A 1334.0, B 1235.8; model uncertainty 0.0053
* Form inputs: days since last match A 267, B 218; matches on record A 54, B 50; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.010, surface_dev_loose +0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Adla Lopez vs Kristina Paskauskas -- W15 Lincoln NE R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 02:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:258195:262884:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adla Lopez (`KXITFWMATCH-26NOV10LOPPAS-LOP`) | 0.19 / 0.21 (3) | 20.0% | 12.8% | 59.4% | 28.8% [28.0%-28.9%] | -- | -- | -- | -- | PASS | -7.2 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Kristina Paskauskas (`KXITFWMATCH-26NOV10LOPPAS-PAS`) | 0.78 / 0.80 (91) | 79.0% | 87.2% | 40.6% | 71.2% [71.1%-72.0%] | -- | -- | -- | -- | PASS | +8.2 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 382.0; serve-point win A 51.4%, B 40.0%; Elo A 1282.3, B 1443.3; model uncertainty 0.0047
* Form inputs: days since last match A 1387, B 344; matches on record A 2, B 101; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.009, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arina Malygina vs Thara Gowda -- W15 Lincoln NE R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 02:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10MALGOW:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thara Gowda (`KXITFWMATCH-26NOV10MALGOW-GOW`) | 0.62 / 0.65 (16) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arina Malygina (`KXITFWMATCH-26NOV10MALGOW-MAL`) | 0.33 / 0.36 (190) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ingrid Carolina Millan Acosta vs Ana Carmen Zamburek -- W50 Chihuahua R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 02:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216311:221979:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ingrid Carolina Millan Acosta (`KXITFWMATCH-26NOV10MILZAM-MIL`) | 0.32 / 0.33 (3) | 32.5% | 40.8% | 42.5% | 39.9% [39.4%-40.4%] | -- | -- | -- | -- | PASS | +8.3 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Ana Carmen Zamburek (`KXITFWMATCH-26NOV10MILZAM-ZAM`) | 0.65 / 0.67 (42) | 66.0% | 59.2% | 57.5% | 60.1% [59.6%-60.6%] | -- | -- | -- | -- | PASS | -6.8 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 792.0, B 216.0; serve-point win A 50.3%, B 48.0%; Elo A 1269.8, B 1341.3; model uncertainty 0.0052
* Form inputs: days since last match A 246, B 372; matches on record A 18, B 27; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.005, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kaya Moe vs Josephine Kunz -- W15 Lincoln NE R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 02:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264960:270454:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Josephine Kunz (`KXITFWMATCH-26NOV10MOEKUN-KUN`) | 0.26 / 0.27 (149) | 26.5% | 19.3% | 17.8% | 23.9% [20.3%-26.0%] | -- | -- | -- | -- | PASS | -7.2 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kaya Moe (`KXITFWMATCH-26NOV10MOEKUN-MOE`) | 0.72 / 0.73 (1) | 72.5% | 80.7% | 82.2% | 76.1% [74.0%-79.7%] | -- | -- | -- | -- | PASS | +8.2 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 339.0, B 728.0; serve-point win A 55.8%, B 50.7%; Elo A 1376.5, B 1187.9; model uncertainty 0.0286
* Form inputs: days since last match A 246, B 197; matches on record A 6, B 34; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.008, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zuzanna Pawlikowska vs Sofia Johnson -- W50 Chihuahua R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 02:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260338:264187:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Johnson (`KXITFWMATCH-26NOV10PAWJOH-JOH`) | 0.67 / 0.71 (499) | 69.0% | 68.4% | 79.3% | 67.1% [55.3%-74.5%] | -- | -- | -- | -- | PASS | -0.6 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zuzanna Pawlikowska (`KXITFWMATCH-26NOV10PAWJOH-PAW`) | 0.29 / 0.32 (36) | 30.5% | 31.6% | 20.7% | 32.9% [25.5%-44.7%] | -- | -- | -- | -- | PASS | +1.1 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2671.0, B 1199.0; serve-point win A 50.5%, B 45.9%; Elo A 1487.4, B 1524.4; model uncertainty 0.0956
* Form inputs: days since last match A 14, B 14; matches on record A 146, B 46; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.019, surface_dev_tight +0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Fernanda Guadalupe Regalado Macias vs Vivian Wolff -- W50 Chihuahua R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 02:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215386:221923:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fernanda Guadalupe Regalado Macias (`KXITFWMATCH-26NOV10REGWOL-REG`) | 0.02 / 0.03 (7725) | 2.5% | 0.2% | 3.4% | 2.3% [1.9%-2.6%] | -- | -- | -- | -- | PASS | -2.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Vivian Wolff (`KXITFWMATCH-26NOV10REGWOL-WOL`) | 0.97 / 0.98 (4464) | 97.5% | 99.8% | 96.7% | 97.7% [97.4%-98.1%] | -- | -- | -- | -- | PASS | +2.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 168.0, B 2229.0; serve-point win A 39.2%, B 38.7%; Elo A 977.0, B 1638.5; model uncertainty 0.0037
* Form inputs: days since last match A 253, B 42; matches on record A 26, B 284; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.003, surface_dev_loose -0.001, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gonzalo Bueno vs Carlos Sanchez Jover -- ATP Challenger Lima R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 02:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-11T02:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202199:208293:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gonzalo Bueno (`KXATPCHALLENGERMATCH-26NOV10BUESAN-BUE`) | 0.61 / 0.62 (5016) | 61.5% | 60.1% | 49.5% | 53.2% [51.1%-55.8%] | -- | -- | -- | -- | PASS | -1.4 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carlos Sanchez Jover (`KXATPCHALLENGERMATCH-26NOV10BUESAN-SAN`) | 0.38 / 0.40 (630) | 39.0% | 39.9% | 50.5% | 46.8% [44.2%-48.9%] | -- | -- | -- | -- | SHADOW_BET | +0.9 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4995.0, B 4399.0; serve-point win A 56.0%, B 46.0%; Elo A 1668.7, B 1571.3; model uncertainty 0.0237
* Form inputs: days since last match A 8, B 22; matches on record A 324, B 493; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.005, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Battistone / Vance vs Komolpisut / Suttisomboon -- M25 Columbus OH R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10BATVANKOMSUT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Battistone / Vance (`KXITFDOUBLES-26NOV10BATVANKOMSUT-BATVAN`) | 0.63 / 0.79 (119) | 71.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Komolpisut / Suttisomboon (`KXITFDOUBLES-26NOV10BATVANKOMSUT-KOMSUT`) | 0.18 / 0.32 (28) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Carpico / Filin vs Carvajal Suazo / Perret -- M25 Columbus OH R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10CARFILCARPER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpico / Filin (`KXITFDOUBLES-26NOV10CARFILCARPER-CARFIL`) | 0.05 / 0.89 (4) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Carvajal Suazo / Perret (`KXITFDOUBLES-26NOV10CARFILCARPER-CARPER`) | 0.04 / 0.89 (56) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Matthew Dellavedova vs Sebastian Gorzny -- ATP Challenger Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 03:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-11T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202354:210478:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthew Dellavedova (`KXATPCHALLENGERMATCH-26NOV10DELGOR-DEL`) | 0.44 / 0.46 (222) | 45.0% | 42.7% | 48.5% | 45.0% [44.0%-46.5%] | -- | 46.1% | 46.1% | MARKETS_AGREE | PASS | -2.3 pp | NORMAL | STALE | B / ADEQUATE | ALL_AGREE | VERIFIED |
| Sebastian Gorzny (`KXATPCHALLENGERMATCH-26NOV10DELGOR-GOR`) | 0.54 / 0.57 (134) | 55.5% | 57.3% | 51.5% | 55.0% [53.5%-56.0%] | -- | 52.0% | -- | INSUFFICIENT_INPUTS | PASS | +1.8 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3884.0, B 1167.0; serve-point win A 62.0%, B 36.5%; Elo A 1455.0, B 1502.6; model uncertainty 0.0125
* Form inputs: days since last match A 49, B 15; matches on record A 451, B 41; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.010, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Forbes / Okonkwo vs Lessard / Miller -- M25 Columbus OH R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10FOROKOLESMIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Forbes / Okonkwo (`KXITFDOUBLES-26NOV10FOROKOLESMIL-FOROKO`) | 0.87 / 0.90 (1) | 88.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lessard / Miller (`KXITFDOUBLES-26NOV10FOROKOLESMIL-LESMIL`) | 0.05 / 0.48 (56) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Shinji Hazawa / Yamato Sueoka vs Moerani Bouzige / Casey Hoole -- ATP Challenger Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 03:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-11T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10HAZSUEBOUHOO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Moerani Bouzige / Casey Hoole (`KXATPCHALLENGERDOUBLES-26NOV10HAZSUEBOUHOO-BOUHOO`) | 0.25 / 0.32 (37) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Shinji Hazawa / Yamato Sueoka (`KXATPCHALLENGERDOUBLES-26NOV10HAZSUEBOUHOO-HAZSUE`) | 0.62 / 0.82 (65) | 72.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Kim / Nakashima vs Heuwekemeijer / Snow -- M25 Columbus OH R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10KIMNAKHEUSNO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Heuwekemeijer / Snow (`KXITFDOUBLES-26NOV10KIMNAKHEUSNO-HEUSNO`) | 0.04 / 0.89 (56) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kim / Nakashima (`KXITFDOUBLES-26NOV10KIMNAKHEUSNO-KIMNAK`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Andre Souza vs Pedro Boscardin Dias -- M25 Santa Cruz do Sul R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 03:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208046:214328:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pedro Boscardin Dias (`KXITFMATCH-26NOV10SOUBOS-BOS`) | 0.93 / 0.96 (401) | 94.5% | 93.0% | 82.8% | 86.2% [85.5%-88.4%] | -- | -- | -- | -- | PASS | -1.5 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Andre Souza (`KXITFMATCH-26NOV10SOUBOS-SOU`) | 0.04 / 0.06 (1604) | 5.0% | 7.0% | 17.2% | 13.8% [11.6%-14.5%] | -- | -- | -- | -- | PASS | +2.0 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 167.0, B 4677.0; serve-point win A 52.1%, B 36.6%; Elo A 1236.0, B 1562.4; model uncertainty 0.0145
* Form inputs: days since last match A 232, B 8; matches on record A 4, B 349; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high -0.011, surface_dev_loose -0.003, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nicolas Zanellato vs Santiago Fa Rodriguez Taverna -- M25 Santa Cruz do Sul R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 03:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144973:210052:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Santiago Fa Rodriguez Taverna (`KXITFMATCH-26NOV10ZANROD-ROD`) | 0.77 / 0.79 (192) | 78.0% | 63.5% | 51.0% | 58.8% [55.2%-66.6%] | -- | -- | -- | -- | PASS | -14.5 pp | REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nicolas Zanellato (`KXITFMATCH-26NOV10ZANROD-ZAN`) | 0.20 / 0.23 (191) | 21.5% | 36.5% | 49.0% | 41.2% [33.4%-44.8%] | -- | -- | -- | -- | WATCH | +15.0 pp | HIGH_REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2702.0, B 5925.0; serve-point win A 57.0%, B 40.4%; Elo A 1381.4, B 1538.2; model uncertainty 0.0571
* Form inputs: days since last match A 141, B 204; matches on record A 221, B 601; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10ZANROD-ZAN  (YES = Nicolas Zanellato)
Model: 37%
Kalshi: 22%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_KALSHI_QUOTE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.015, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofia Avataneo vs Miriam Bianca Bulgaru -- W50 Chihuahua R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 03:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214480:242450:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Avataneo (`KXITFWMATCH-26NOV10AVABUL-AVA`) | 0.03 / 0.05 (709) | 4.0% | 2.1% | 7.4% | 7.0% [5.4%-8.6%] | -- | -- | -- | -- | WATCH | -1.9 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Miriam Bianca Bulgaru (`KXITFWMATCH-26NOV10AVABUL-BUL`) | 0.94 / 0.96 (3) | 95.0% | 97.9% | 92.6% | 93.0% [91.4%-94.6%] | -- | -- | -- | -- | PASS | +2.9 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 821.0, B 3417.0; serve-point win A 43.5%, B 41.3%; Elo A 1218.6, B 1669.5; model uncertainty 0.0161
* Form inputs: days since last match A 197, B 197; matches on record A 143, B 517; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.002, surface_dev_loose -0.007, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Caterina Odorizzi vs Jessica Marmorstein -- W50 Chihuahua R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 03:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221478:222613:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jessica Marmorstein (`KXITFWMATCH-26NOV10ODOMAR-MAR`) | 0.10 / 0.14 (86) | 12.0% | 32.0% | 88.6% | 47.9% [45.7%-50.0%] | -- | -- | -- | -- | PASS | +20.0 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Caterina Odorizzi (`KXITFWMATCH-26NOV10ODOMAR-ODO`) | 0.86 / 0.89 (255) | 87.5% | 68.0% | 11.4% | 52.1% [50.0%-54.3%] | -- | -- | -- | -- | PASS | -19.5 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1069.0, B 71.0; serve-point win A 54.5%, B 48.9%; Elo A 1209.7, B 1177.4; model uncertainty 0.0213
* Form inputs: days since last match A 197, B 491; matches on record A 126, B 52; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10ODOMAR-MAR  (YES = Jessica Marmorstein)
Model: 32%
Kalshi: 12%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.021, surface_dev_loose -0.011, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Plaza / Rodriguez vs Gatica / Pereira -- W15 São Carlos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 03:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10PLARODGATPER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gatica / Pereira (`KXITFWDOUBLES-26NOV10PLARODGATPER-GATPER`) | 0.93 / 0.95 (202) | 94.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Plaza / Rodriguez (`KXITFWDOUBLES-26NOV10PLARODGATPER-PLAROD`) | 0.04 / 0.05 (419) | 4.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Alvarez / Cozad vs Bianchi / Schtulmann Gasca -- M15 Zamora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 03:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T03:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10ALVCOZBIASCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alvarez / Cozad (`KXITFDOUBLES-26NOV10ALVCOZBIASCH-ALVCOZ`) | 0.87 / 0.90 (1) | 88.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bianchi / Schtulmann Gasca (`KXITFDOUBLES-26NOV10ALVCOZBIASCH-BIASCH`) | 0.05 / 0.45 (211) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lage / Martinez Miranda vs Covato / Voelzke -- M15 Zamora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 03:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T03:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10LAGMARCOVVOE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Covato / Voelzke (`KXITFDOUBLES-26NOV10LAGMARCOVVOE-COVVOE`) | 0.77 / 0.89 (14) | 83.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lage / Martinez Miranda (`KXITFDOUBLES-26NOV10LAGMARCOVVOE-LAGMAR`) | 0.10 / 0.55 (34) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Malaika Rapolu vs Diletta Cherubini -- W50 Chihuahua R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221000:222837:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diletta Cherubini (`KXITFWMATCH-26NOV10RAPCHE-CHE`) | 0.36 / 0.38 (150) | 37.0% | 37.8% | 38.9% | 41.0% [38.4%-44.6%] | -- | -- | -- | -- | WATCH | +0.8 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Malaika Rapolu (`KXITFWMATCH-26NOV10RAPCHE-RAP`) | 0.61 / 0.63 (18) | 62.0% | 62.2% | 61.1% | 59.0% [55.4%-61.6%] | -- | -- | -- | -- | PASS | +0.2 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1761.0, B 2494.0; serve-point win A 53.4%, B 48.9%; Elo A 1586.8, B 1544.4; model uncertainty 0.0313
* Form inputs: days since last match A 54, B 11; matches on record A 134, B 315; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.011, surface_dev_loose -0.037, surface_dev_tight +0.026
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Isaac Becroft / Anton Shepp vs Calum Puttergill / Dane Sweeny -- ATP Challenger Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 04:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-11T04:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10BECSHEPUTSWE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isaac Becroft / Anton Shepp (`KXATPCHALLENGERDOUBLES-26NOV10BECSHEPUTSWE-BECSHE`) | 0.61 / 0.80 (4) | 70.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Calum Puttergill / Dane Sweeny (`KXATPCHALLENGERDOUBLES-26NOV10BECSHEPUTSWE-PUTSWE`) | 0.26 / 0.52 (3) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Bernard Tomic vs Omar Jasika -- ATP Challenger Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 04:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-11T04:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106071:117357:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Omar Jasika (`KXATPCHALLENGERMATCH-26NOV10TOMJAS-JAS`) | 0.43 / 0.45 (2299) | 44.0% | 38.4% | 33.9% | 33.4% [31.6%-34.8%] | -- | 57.2% | -- | INSUFFICIENT_INPUTS | PASS | -5.6 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Bernard Tomic (`KXATPCHALLENGERMATCH-26NOV10TOMJAS-TOM`) | 0.55 / 0.57 (3492) | 56.0% | 61.6% | 66.1% | 66.6% [65.2%-68.4%] | -- | 56.1% | 56.1% | MODEL_LONE_OUTLIER | SHADOW_BET | +5.6 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5260.0, B 4159.0; serve-point win A 64.1%, B 38.2%; Elo A 1666.8, B 1530.4; model uncertainty 0.016
* Form inputs: days since last match A 29, B 8; matches on record A 887, B 523; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.014, surface_dev_loose +0.004, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Ia Reyes Romero vs Despina Papamichail -- W50 Chihuahua R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 04:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T04:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:202604:269949:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Despina Papamichail (`KXITFWMATCH-26NOV10REYPAP-PAP`) | 0.97 / 0.98 (1874) | 97.5% | 96.9% | 90.8% | 89.6% [88.6%-90.5%] | -- | -- | -- | -- | PASS | -0.6 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ia Reyes Romero (`KXITFWMATCH-26NOV10REYPAP-REY`) | 0.02 / 0.03 (7581) | 2.5% | 3.1% | 9.2% | 10.4% [9.5%-11.4%] | -- | -- | -- | -- | PASS | +0.6 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 39.0, B 4365.0; serve-point win A 44.8%, B 41.3%; Elo A 1269.0, B 1641.6; model uncertainty 0.0096
* Form inputs: days since last match A 617, B 6; matches on record A 2, B 993; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Leonardo Aguilar vs Kai Thompson -- M15 Zamora R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10AGUTHO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leonardo Aguilar (`KXITFMATCH-26NOV10AGUTHO-AGU`) | 0.08 / 0.16 (68) | 12.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kai Thompson (`KXITFMATCH-26NOV10AGUTHO-THO`) | 0.80 / 0.89 (1) | 84.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Finn Bass / Scott Duncan vs Thijmen Loof / Kaito Uesugi -- ATP Challenger Matsuyama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-11T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10BASDUNLOOUES:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Finn Bass / Scott Duncan (`KXATPCHALLENGERDOUBLES-26NOV10BASDUNLOOUES-BASDUN`) | 0.16 / 0.37 (56) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Thijmen Loof / Kaito Uesugi (`KXATPCHALLENGERDOUBLES-26NOV10BASDUNLOOUES-LOOUES`) | 0.70 / 0.92 (1) | 81.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jay Friend vs Naoya Honda -- ATP Challenger Matsuyama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-11T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10HARHON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jay Friend (`KXATPCHALLENGERMATCH-26NOV10HARHON-HAR`) | 0.78 / 0.80 (1322) | 79.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Naoya Honda (`KXATPCHALLENGERMATCH-26NOV10HARHON-HON`) | 0.20 / 0.22 (493) | 21.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Finn Reynolds / James Watt vs S D Prajwal Dev / Nitin Kumar Sinha -- ATP Challenger Matsuyama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-11T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10REYWATDEVSIN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S D Prajwal Dev / Nitin Kumar Sinha (`KXATPCHALLENGERDOUBLES-26NOV10REYWATDEVSIN-DEVSIN`) | 0.07 / 0.71 (56) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Finn Reynolds / James Watt (`KXATPCHALLENGERDOUBLES-26NOV10REYWATDEVSIN-REYWAT`) | 0.81 / 0.95 (325) | 88.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Enzo Aguiard / Pavle Marinkov vs Jeffrey Chuan En Hsu / Evan Zhu -- ATP Challenger Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 05:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-11T05:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10AGUMARHSUZHU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Enzo Aguiard / Pavle Marinkov (`KXATPCHALLENGERDOUBLES-26NOV10AGUMARHSUZHU-AGUMAR`) | 0.40 / 0.94 (56) | 67.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jeffrey Chuan En Hsu / Evan Zhu (`KXATPCHALLENGERDOUBLES-26NOV10AGUMARHSUZHU-HSUZHU`) | 0.45 / 0.72 (3) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Akira Santillan / Baoluo Zheng vs Blake Ellis / Li Tu -- ATP Challenger Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 05:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-11T05:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10SANZHEELLTUL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Blake Ellis / Li Tu (`KXATPCHALLENGERDOUBLES-26NOV10SANZHEELLTUL-ELLTUL`) | 0.06 / 0.94 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Akira Santillan / Baoluo Zheng (`KXATPCHALLENGERDOUBLES-26NOV10SANZHEELLTUL-SANZHE`) | 0.06 / 0.94 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Emiliano Aguilera Guerrero vs Francisco Moreno Rico -- M15 Zamora R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10AGUMOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emiliano Aguilera Guerrero (`KXITFMATCH-26NOV10AGUMOR-AGU`) | 0.87 / 0.94 (133) | 90.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Francisco Moreno Rico (`KXITFMATCH-26NOV10AGUMOR-MOR`) | 0.06 / 0.13 (174) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Savannah Broadus vs Maddison Inglis -- W75 Brisbane R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213666:221221:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Savannah Broadus (`KXITFWMATCH-26NOV10BROING-BRO`) | 0.24 / 0.27 (47) | 25.5% | 19.9% | 60.9% | 31.4% [20.6%-41.7%] | -- | -- | -- | -- | WATCH | -5.6 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maddison Inglis (`KXITFWMATCH-26NOV10BROING-ING`) | 0.71 / 0.74 (85) | 72.5% | 80.1% | 39.1% | 68.6% [58.3%-79.4%] | -- | -- | -- | -- | PASS | +7.6 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 898.0, B 3027.0; serve-point win A 54.6%, B 38.9%; Elo A 1496.9, B 1762.2; model uncertainty 0.1053
* Form inputs: days since last match A 78, B 7; matches on record A 63, B 485; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.009, surface_dev_loose +0.009, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Grubor / Liu vs Coe / Taranova -- W15 Lincoln NE R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10GRULIUCOETAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Coe / Taranova (`KXITFWDOUBLES-26NOV10GRULIUCOETAR-COETAR`) | 0.13 / 0.74 (66) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Grubor / Liu (`KXITFWDOUBLES-26NOV10GRULIUCOETAR-GRULIU`) | 0.11 / 0.83 (56) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Hsu / Rademacher vs Raidt / Spencer -- W15 Lincoln NE R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10HSURADRAISPE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hsu / Rademacher (`KXITFWDOUBLES-26NOV10HSURADRAISPE-HSURAD`) | 0.05 / 0.32 (56) | 18.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Raidt / Spencer (`KXITFWDOUBLES-26NOV10HSURADRAISPE-RAISPE`) | 0.63 / 0.88 (1) | 75.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Maunupau / Maunupau vs Rahimkhani / Rizzetto -- W15 Lincoln NE R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10MAUMAURAHRIZ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maunupau / Maunupau (`KXITFWDOUBLES-26NOV10MAUMAURAHRIZ-MAUMAU`) | 0.08 / 0.89 (56) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rahimkhani / Rizzetto (`KXITFWDOUBLES-26NOV10MAUMAURAHRIZ-RAHRIZ`) | 0.06 / 0.89 (56) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Yuki Naito vs Mei Yamaguchi -- W75 Brisbane R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215614:216044:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuki Naito (`KXITFWMATCH-26NOV10NAIYAM-NAI`) | 0.61 / 0.64 (13) | 62.5% | 42.0% | 52.6% | 45.8% [42.6%-48.4%] | -- | -- | -- | -- | PASS | -20.5 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mei Yamaguchi (`KXITFWMATCH-26NOV10NAIYAM-YAM`) | 0.35 / 0.37 (21) | 36.0% | 58.0% | 47.3% | 54.2% [51.6%-57.4%] | -- | -- | -- | -- | WATCH | +22.0 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2186.0, B 3409.0; serve-point win A 54.6%, B 43.9%; Elo A 1477.3, B 1572.0; model uncertainty 0.0291
* Form inputs: days since last match A 50, B 7; matches on record A 359, B 355; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10NAIYAM-YAM  (YES = Mei Yamaguchi)
Model: 58%
Kalshi: 36%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.021, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sahaja Yamalapalli vs Olivia Gadecki -- W75 Brisbane R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216265:246481:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Olivia Gadecki (`KXITFWMATCH-26NOV10YAMGAD-GAD`) | 0.58 / 0.60 (197) | 59.0% | 72.3% | 64.6% | 67.5% [66.1%-69.9%] | -- | -- | -- | -- | WATCH | +13.3 pp | REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sahaja Yamalapalli (`KXITFWMATCH-26NOV10YAMGAD-YAM`) | 0.40 / 0.42 (185) | 41.0% | 27.7% | 35.4% | 32.5% [30.1%-33.9%] | -- | -- | -- | -- | PASS | -13.3 pp | REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2258.0, B 3148.0; serve-point win A 52.0%, B 43.6%; Elo A 1568.2, B 1735.5; model uncertainty 0.0191
* Form inputs: days since last match A 7, B 197; matches on record A 234, B 342; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xinxin Yao vs Renee Alame -- W75 Brisbane R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:252587:266383:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Renee Alame (`KXITFWMATCH-26NOV10YAOALA-ALA`) | 0.06 / 0.08 (405) | 7.0% | 4.5% | 14.8% | 12.5% [10.9%-13.4%] | -- | -- | -- | -- | PASS | -2.5 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Xinxin Yao (`KXITFWMATCH-26NOV10YAOALA-YAO`) | 0.90 / 0.94 (556) | 92.0% | 95.5% | 85.2% | 87.5% [86.7%-89.1%] | -- | -- | -- | -- | PASS | +3.5 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2972.0, B 291.0; serve-point win A 59.3%, B 53.4%; Elo A 1573.7, B 1228.7; model uncertainty 0.0122
* Form inputs: days since last match A 36, B 274; matches on record A 320, B 9; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.005, surface_dev_loose +0.005, surface_dev_tight -0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cheng-Peng Hsieh / Mili Poljicak vs Pruchya Isaro / Yuta Shimizu -- ATP Challenger Matsuyama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 06:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-11T06:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10HSIPOLISASHI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cheng-Peng Hsieh / Mili Poljicak (`KXATPCHALLENGERDOUBLES-26NOV10HSIPOLISASHI-HSIPOL`) | 0.06 / 0.94 (56) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pruchya Isaro / Yuta Shimizu (`KXATPCHALLENGERDOUBLES-26NOV10HSIPOLISASHI-ISASHI`) | 0.06 / 0.94 (4) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Yu Hsiou Hsu vs Niels McDonald -- ATP Challenger Matsuyama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 06:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-11T06:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200318:213360:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yu Hsiou Hsu (`KXATPCHALLENGERMATCH-26NOV10HSUMCD-HSU`) | 0.72 / 0.73 (1989) | 72.5% | 69.9% | 78.6% | 78.6% [74.4%-80.5%] | -- | 72.5% | -- | INSUFFICIENT_INPUTS | WATCH | -2.6 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Niels McDonald (`KXATPCHALLENGERMATCH-26NOV10HSUMCD-MCD`) | 0.27 / 0.28 (1981) | 27.5% | 30.1% | 21.4% | 21.4% [19.5%-25.6%] | -- | 27.9% | -- | INSUFFICIENT_INPUTS | PASS | +2.6 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4515.0, B 2065.0; serve-point win A 63.2%, B 40.8%; Elo A 1618.8, B 1396.0; model uncertainty 0.0302
* Form inputs: days since last match A 8, B 71; matches on record A 532, B 41; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.023, surface_pool_high +0.015, surface_dev_loose +0.006, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Joel Schwaerzler vs Kaichi Uchida -- ATP Challenger Matsuyama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 06:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-11T06:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111187:212082:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joel Schwaerzler (`KXATPCHALLENGERMATCH-26NOV10SCHUCH-SCH`) | 0.80 / 0.81 (22) | 80.5% | 71.3% | 58.6% | 60.0% [59.5%-60.9%] | -- | 80.4% | 80.4% | MODEL_LONE_OUTLIER | PASS | -9.2 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Kaichi Uchida (`KXATPCHALLENGERMATCH-26NOV10SCHUCH-UCH`) | 0.18 / 0.20 (2012) | 19.0% | 28.7% | 41.4% | 40.0% [39.1%-40.5%] | -- | 19.9% | 19.9% | MODEL_LONE_OUTLIER | WATCH | +9.7 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4626.0, B 4273.0; serve-point win A 69.6%, B 35.0%; Elo A 1587.0, B 1489.3; model uncertainty 0.007
* Form inputs: days since last match A 8, B 15; matches on record A 179, B 836; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## August Holmgren vs Christopher O'Connell -- ATP Challenger Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 06:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-11T06:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200416:tml:O483:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| August Holmgren (`KXATPCHALLENGERMATCH-26NOV10HOLOCO-HOL`) | 0.37 / 0.38 (32) | 37.5% | 48.8% | 58.0% | 46.2% [40.1%-50.9%] | -- | 38.5% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +11.3 pp | REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Christopher O'Connell (`KXATPCHALLENGERMATCH-26NOV10HOLOCO-OCO`) | 0.61 / 0.63 (2361) | 62.0% | 51.2% | 42.0% | 53.8% [49.0%-59.9%] | -- | 61.6% | -- | INSUFFICIENT_INPUTS | PASS | -10.8 pp | REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4476.0, B 2972.0; serve-point win A 68.0%, B 31.7%; Elo A 1609.9, B 1800.7; model uncertainty 0.0542
* Form inputs: days since last match A 8, B 74; matches on record A 320, B 319; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.019, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Jason Jung / Ajeet Rai vs Ethan Cook / Tai Leonard Sach -- ATP Challenger Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 06:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-11T06:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10JUNRAICOOSAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ethan Cook / Tai Leonard Sach (`KXATPCHALLENGERDOUBLES-26NOV10JUNRAICOOSAT-COOSAT`) | 0.23 / 0.71 (64) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jason Jung / Ajeet Rai (`KXATPCHALLENGERDOUBLES-26NOV10JUNRAICOOSAT-JUNRAI`) | 0.63 / 0.82 (2) | 72.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ammar Faleh Alhogbani vs Calvin Mueller -- M15 Kuala Lumpur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209166:212249:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ammar Faleh Alhogbani (`KXITFMATCH-26NOV10ALHMUE-ALH`) | 0.14 / 0.15 (10) | 14.5% | 36.7% | 32.6% | 29.9% [28.6%-31.2%] | -- | -- | -- | -- | PASS | +22.2 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Calvin Mueller (`KXITFMATCH-26NOV10ALHMUE-MUE`) | 0.83 / 0.88 (4) | 85.5% | 63.3% | 67.4% | 70.1% [68.8%-71.4%] | -- | -- | -- | -- | PASS | -22.2 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1359.0, B 1075.0; serve-point win A 59.2%, B 38.1%; Elo A 1160.7, B 1324.2; model uncertainty 0.0128
* Form inputs: days since last match A 316, B 197; matches on record A 37, B 24; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10ALHMUE-ALH  (YES = Ammar Faleh Alhogbani)
Model: 37%
Kalshi: 14%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.004, surface_dev_loose +0.008, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mikaeel Ali Baig vs Tin Chen -- M15 Kuala Lumpur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144844:214515:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mikaeel Ali Baig (`KXITFMATCH-26NOV10ALICHE-ALI`) | 0.12 / 0.22 (1) | 17.0% | 61.1% | 35.9% | 60.2% [59.2%-60.2%] | -- | -- | -- | -- | PASS | +44.1 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Tin Chen (`KXITFMATCH-26NOV10ALICHE-CHE`) | 0.77 / 0.86 (3) | 81.5% | 38.9% | 64.1% | 39.8% [39.8%-40.8%] | -- | -- | -- | -- | PASS | -42.6 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 47.0, B 0.0; serve-point win A 61.6%, B 40.6%; Elo A 1254.1, B 1186.6; model uncertainty 0.0052
* Form inputs: days since last match A 197, B 1289; matches on record A 1, B 7; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10ALICHE-ALI  (YES = Mikaeel Ali Baig)
Model: 61%
Kalshi: 17%
Gap: +44 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Edoardo Cherie Ligniere vs Adhithya Ganesan -- M15 Kuala Lumpur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212122:212258:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Edoardo Cherie Ligniere (`KXITFMATCH-26NOV10CHEGAN-CHE`) | 0.29 / 0.42 (43) | 35.5% | 18.7% | 30.9% | 26.1% [25.0%-27.0%] | -- | -- | -- | -- | PASS | -16.8 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Adhithya Ganesan (`KXITFMATCH-26NOV10CHEGAN-GAN`) | 0.61 / 0.68 (4) | 64.5% | 81.3% | 69.0% | 73.9% [73.0%-75.0%] | -- | -- | -- | -- | PASS | +16.8 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 266.0, B 2730.0; serve-point win A 54.9%, B 38.3%; Elo A 1191.9, B 1381.1; model uncertainty 0.0102
* Form inputs: days since last match A 197, B 309; matches on record A 17, B 95; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10CHEGAN-GAN  (YES = Adhithya Ganesan)
Model: 81%
Kalshi: 64%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chen Dong vs Yuto Oki -- M15 Kuala Lumpur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211317:212639:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chen Dong (`KXITFMATCH-26NOV10DONOKI-DON`) | 0.25 / 0.30 (50) | 27.5% | 52.4% | 48.4% | 51.0% [50.5%-52.6%] | -- | -- | -- | -- | WATCH | +24.9 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuto Oki (`KXITFMATCH-26NOV10DONOKI-OKI`) | 0.65 / 0.77 (2) | 71.0% | 47.5% | 51.5% | 49.0% [47.4%-49.5%] | -- | -- | -- | -- | PASS | -23.4 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1294.0, B 1766.0; serve-point win A 60.0%, B 40.5%; Elo A 1305.5, B 1280.4; model uncertainty 0.0103
* Form inputs: days since last match A 211, B 225; matches on record A 42, B 42; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10DONOKI-DON  (YES = Chen Dong)
Model: 52%
Kalshi: 28%
Gap: +25 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sasikumar Mukund vs Takumi Katsuda -- M15 Kuala Lumpur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10MUKKAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Takumi Katsuda (`KXITFMATCH-26NOV10MUKKAT-KAT`) | 0.06 / 0.11 (142) | 8.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sasikumar Mukund (`KXITFMATCH-26NOV10MUKKAT-MUK`) | 0.87 / 0.93 (6) | 90.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yua Taka vs Grigoriy Lomakin -- M15 Kuala Lumpur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200441:212196:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Grigoriy Lomakin (`KXITFMATCH-26NOV10TAKLOM-LOM`) | 0.31 / 0.37 (39) | 34.0% | 46.4% | 57.3% | 47.9% [41.8%-54.7%] | -- | -- | -- | -- | PASS | +12.4 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yua Taka (`KXITFMATCH-26NOV10TAKLOM-TAK`) | 0.58 / 0.71 (4) | 64.5% | 53.6% | 42.7% | 52.1% [45.3%-58.2%] | -- | -- | -- | -- | PASS | -10.9 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 485.0, B 2308.0; serve-point win A 58.8%, B 41.9%; Elo A 1205.9, B 1172.7; model uncertainty 0.0646
* Form inputs: days since last match A 274, B 57; matches on record A 21, B 336; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.026, surface_dev_loose -0.016, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Camille Allegre vs Galia Garcia Anzures -- W50 Chihuahua R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10ALLGAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Camille Allegre (`KXITFWMATCH-26NOV10ALLGAR-ALL`) | 0.88 / 0.92 (1) | 90.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Galia Garcia Anzures (`KXITFWMATCH-26NOV10ALLGAR-GAR`) | 0.06 / 0.12 (75) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eva Bennemann vs Sijia Wei -- W75 Brisbane R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221096:266622:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eva Bennemann (`KXITFWMATCH-26NOV10BENWEI-BEN`) | 0.24 / 0.28 (101) | 26.0% | 44.7% | 74.0% | 60.6% [46.3%-66.6%] | -- | -- | -- | -- | WATCH | +18.7 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sijia Wei (`KXITFWMATCH-26NOV10BENWEI-WEI`) | 0.71 / 0.72 (89) | 71.5% | 55.3% | 26.0% | 39.4% [33.4%-53.7%] | -- | -- | -- | -- | PASS | -16.2 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2212.0, B 2150.0; serve-point win A 51.8%, B 47.2%; Elo A 1632.8, B 1716.7; model uncertainty 0.1018
* Form inputs: days since last match A 28, B 36; matches on record A 67, B 308; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10BENWEI-BEN  (YES = Eva Bennemann)
Model: 45%
Kalshi: 26%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.010, surface_dev_loose +0.005, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Joanna Garland vs Hikaru Sato -- W75 Brisbane R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220466:221141:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joanna Garland (`KXITFWMATCH-26NOV10GARSAT-GAR`) | 0.77 / 0.83 (13) | 80.0% | 91.2% | 79.7% | 82.5% [80.6%-84.6%] | -- | -- | -- | -- | PASS | +11.2 pp | REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hikaru Sato (`KXITFWMATCH-26NOV10GARSAT-SAT`) | 0.16 / 0.23 (7) | 19.5% | 8.8% | 20.3% | 17.5% [15.4%-19.4%] | -- | -- | -- | -- | PASS | -10.7 pp | REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2480.0, B 1807.0; serve-point win A 66.3%, B 44.2%; Elo A 1772.3, B 1465.8; model uncertainty 0.0202
* Form inputs: days since last match A 6, B 204; matches on record A 397, B 175; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.017, surface_dev_loose -0.008, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuno Kitahara vs Heather Watson -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:201586:263881:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuno Kitahara (`KXITFWMATCH-26NOV10KITWAT-KIT`) | 0.12 / 0.14 (126) | 13.0% | 15.0% | 58.4% | 37.5% [17.9%-47.3%] | -- | -- | -- | -- | WATCH | +2.0 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Heather Watson (`KXITFWMATCH-26NOV10KITWAT-WAT`) | 0.84 / 0.88 (31) | 86.0% | 85.0% | 41.6% | 62.5% [52.7%-82.1%] | -- | -- | -- | -- | PASS | -1.0 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2068.0, B 2194.0; serve-point win A 50.9%, B 41.3%; Elo A 1428.6, B 1732.8; model uncertainty 0.1473
* Form inputs: days since last match A 204, B 10; matches on record A 119, B 824; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.030, surface_pool_high +0.031, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yeonwoo Ku vs Eri Shimizu -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10KUXSHI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yeonwoo Ku (`KXITFWMATCH-26NOV10KUXSHI-KUX`) | 0.79 / 0.82 (33) | 80.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eri Shimizu (`KXITFWMATCH-26NOV10KUXSHI-SHI`) | 0.18 / 0.19 (30) | 18.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kyoka Okamura vs Ena Koike -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211846:260514:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ena Koike (`KXITFWMATCH-26NOV10OKAKOI-KOI`) | 0.36 / 0.38 (34) | 37.0% | 45.6% | 57.7% | 47.9% [39.1%-52.6%] | -- | -- | -- | -- | WATCH | +8.7 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kyoka Okamura (`KXITFWMATCH-26NOV10OKAKOI-OKA`) | 0.59 / 0.64 (86) | 61.5% | 54.4% | 42.3% | 52.1% [47.4%-60.9%] | -- | -- | -- | -- | PASS | -7.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2971.0, B 1979.0; serve-point win A 59.5%, B 41.4%; Elo A 1649.2, B 1548.5; model uncertainty 0.0675
* Form inputs: days since last match A 7, B 24; matches on record A 631, B 120; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Astra Sharma vs Tahlia Kokkinis -- W75 Brisbane R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206292:260667:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tahlia Kokkinis (`KXITFWMATCH-26NOV10SHAKOK-KOK`) | 0.20 / 0.22 (133) | 21.0% | 38.5% | 67.9% | 52.6% [34.2%-60.1%] | -- | -- | -- | -- | WATCH | +17.5 pp | HIGH_REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Astra Sharma (`KXITFWMATCH-26NOV10SHAKOK-SHA`) | 0.76 / 0.78 (113) | 77.0% | 61.5% | 32.1% | 47.4% [39.9%-65.8%] | -- | -- | -- | -- | PASS | -15.5 pp | HIGH_REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2800.0, B 1935.0; serve-point win A 61.5%, B 40.7%; Elo A 1638.0, B 1514.8; model uncertainty 0.1298
* Form inputs: days since last match A 55, B 175; matches on record A 423, B 101; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10SHAKOK-KOK  (YES = Tahlia Kokkinis)
Model: 38%
Kalshi: 21%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.021, surface_dev_loose -0.015, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valeriya Strakhova vs Julia Garcia -- W50 Chihuahua R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211063:222049:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julia Garcia (`KXITFWMATCH-26NOV10STRGAR-GAR`) | 0.23 / 0.26 (9) | 24.5% | 35.1% | 64.1% | 36.4% [28.7%-42.6%] | -- | -- | -- | -- | PASS | +10.6 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valeriya Strakhova (`KXITFWMATCH-26NOV10STRGAR-STR`) | 0.72 / 0.73 (5) | 72.5% | 64.9% | 35.9% | 63.6% [57.4%-71.3%] | -- | -- | -- | -- | PASS | -7.6 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2323.0, B 492.0; serve-point win A 54.6%, B 48.3%; Elo A 1546.8, B 1383.1; model uncertainty 0.0694
* Form inputs: days since last match A 11, B 484; matches on record A 770, B 33; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.005, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mutsumi Uemura vs Hanna Chang -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213949:260828:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hanna Chang (`KXITFWMATCH-26NOV10UEMCHA-CHA`) | 0.74 / 0.78 (120) | 76.0% | 90.2% | 83.5% | 84.2% [83.2%-85.1%] | -- | -- | -- | -- | PASS | +14.2 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mutsumi Uemura (`KXITFWMATCH-26NOV10UEMCHA-UEM`) | 0.19 / 0.23 (126) | 21.0% | 9.8% | 16.5% | 15.8% [14.9%-16.8%] | -- | -- | -- | -- | PASS | -11.2 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 824.0, B 3084.0; serve-point win A 49.2%, B 41.1%; Elo A 1314.4, B 1608.7; model uncertainty 0.0097
* Form inputs: days since last match A 204, B 204; matches on record A 22, B 519; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.006, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chengyiyi Yuan vs Emerson Jones -- W75 Brisbane R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215134:263644:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emerson Jones (`KXITFWMATCH-26NOV10YUAJON-JON`) | 0.89 / 0.92 (5) | 90.5% | 91.1% | 75.6% | 79.6% [78.0%-81.4%] | -- | -- | -- | -- | PASS | +0.6 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Chengyiyi Yuan (`KXITFWMATCH-26NOV10YUAJON-YUA`) | 0.06 / 0.09 (6) | 7.5% | 8.9% | 24.4% | 20.4% [18.6%-22.0%] | -- | -- | -- | -- | WATCH | +1.4 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2947.0, B 3547.0; serve-point win A 49.4%, B 40.4%; Elo A 1478.6, B 1788.5; model uncertainty 0.0169
* Form inputs: days since last match A 44, B 7; matches on record A 239, B 156; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Masamichi Imamura / Rio Noguchi vs Constantin Bittoun Kouzmine / David Poljak -- ATP Challenger Matsuyama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 07:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-11T07:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10IMANOGBITPOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Constantin Bittoun Kouzmine / David Poljak (`KXATPCHALLENGERDOUBLES-26NOV10IMANOGBITPOL-BITPOL`) | 0.42 / 0.59 (4) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Masamichi Imamura / Rio Noguchi (`KXATPCHALLENGERDOUBLES-26NOV10IMANOGBITPOL-IMANOG`) | 0.44 / 0.56 (4) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alexandru Jecan / Szymon Kielan vs Toshihide Matsui / Ramkumar Ramanathan -- ATP Challenger Matsuyama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 07:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-11T07:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10JECKIEMATRAM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandru Jecan / Szymon Kielan (`KXATPCHALLENGERDOUBLES-26NOV10JECKIEMATRAM-JECKIE`) | 0.67 / 0.91 (1) | 79.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Toshihide Matsui / Ramkumar Ramanathan (`KXATPCHALLENGERDOUBLES-26NOV10JECKIEMATRAM-MATRAM`) | 0.19 / 0.62 (64) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Fajing Sun vs Billy Harris -- ATP Challenger Matsuyama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 07:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-11T07:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111806:126129:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Billy Harris (`KXATPCHALLENGERMATCH-26NOV10SUNHAR-HAR`) | 0.66 / 0.68 (2677) | 67.0% | 56.3% | 49.0% | 51.0% [48.5%-56.0%] | -- | 66.2% | -- | INSUFFICIENT_INPUTS | PASS | -10.7 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Fajing Sun (`KXATPCHALLENGERMATCH-26NOV10SUNHAR-SUN`) | 0.32 / 0.34 (2396) | 33.0% | 43.7% | 51.0% | 49.0% [44.0%-51.5%] | -- | 33.9% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +10.7 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4332.0, B 5763.0; serve-point win A 63.3%, B 35.5%; Elo A 1555.7, B 1608.9; model uncertainty 0.0373
* Form inputs: days since last match A 15, B 8; matches on record A 528, B 640; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.020, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## M Rifqi Fitriadi vs Corban Crowther -- M15 Kuala Lumpur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10FITCRO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Corban Crowther (`KXITFMATCH-26NOV10FITCRO-CRO`) | 0.07 / 0.13 (28) | 10.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| M Rifqi Fitriadi (`KXITFMATCH-26NOV10FITCRO-FIT`) | 0.80 / 0.93 (2) | 86.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuquan Jin vs Xiaoyin Yang -- M15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212183:212466:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuquan Jin (`KXITFMATCH-26NOV10JINYAN-JIN`) | 0.48 / 0.50 (7) | 49.0% | 41.7% | 37.6% | 40.9% [40.4%-44.0%] | -- | -- | -- | -- | PASS | -7.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Xiaoyin Yang (`KXITFMATCH-26NOV10JINYAN-YAN`) | 0.47 / 0.52 (156) | 49.5% | 58.3% | 62.4% | 59.1% [56.0%-59.6%] | -- | -- | -- | -- | PASS | +8.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1269.0, B 817.0; serve-point win A 65.5%, B 32.8%; Elo A 1120.7, B 1172.5; model uncertainty 0.0181
* Form inputs: days since last match A 386, B 211; matches on record A 52, B 21; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Madhwin Kamath vs Kazuma Kawachi -- M15 Kuala Lumpur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:124074:209979:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Madhwin Kamath (`KXITFMATCH-26NOV10KAMKAW-KAM`) | 0.47 / 0.57 (58) | 52.0% | 61.3% | 47.4% | 54.1% [53.1%-56.2%] | -- | -- | -- | -- | PASS | +9.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kazuma Kawachi (`KXITFMATCH-26NOV10KAMKAW-KAW`) | 0.36 / 0.44 (2) | 40.0% | 38.7% | 52.6% | 45.9% [43.8%-46.9%] | -- | -- | -- | -- | PASS | -1.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 843.0, B 531.0; serve-point win A 60.2%, B 42.0%; Elo A 1186.8, B 1138.0; model uncertainty 0.0155
* Form inputs: days since last match A 197, B 232; matches on record A 53, B 234; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.021, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Geun Jun Kim vs Cooper Kose -- M15 Kuala Lumpur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208130:213566:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Geun Jun Kim (`KXITFMATCH-26NOV10KIMKOS-KIM`) | 0.83 / 0.91 (2) | 87.0% | 77.8% | 77.3% | 65.3% [63.3%-70.1%] | -- | -- | -- | -- | PASS | -9.2 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Cooper Kose (`KXITFMATCH-26NOV10KIMKOS-KOS`) | 0.07 / 0.17 (7) | 12.0% | 22.2% | 22.7% | 34.7% [29.9%-36.7%] | -- | -- | -- | -- | PASS | +10.2 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1129.0, B 204.0; serve-point win A 60.4%, B 45.5%; Elo A 1273.7, B 1173.5; model uncertainty 0.034
* Form inputs: days since last match A 225, B 274; matches on record A 49, B 5; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.010, surface_dev_loose +0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## jintao Lan vs Noritaka Koizumi -- M15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212476:213834:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Noritaka Koizumi (`KXITFMATCH-26NOV10LANKOI-KOI`) | 0.87 / 0.89 (486) | 88.0% | 50.3% | 51.5% | 51.0% [51.0%-51.0%] | -- | -- | -- | -- | PASS | -37.7 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| jintao Lan (`KXITFMATCH-26NOV10LANKOI-LAN`) | 0.09 / 0.13 (475) | 11.0% | 49.7% | 48.5% | 49.0% [49.0%-49.0%] | -- | -- | -- | -- | PASS | +38.7 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 66.0, B 190.0; serve-point win A 60.9%, B 39.0%; Elo A 1277.8, B 1285.6; model uncertainty 0.0
* Form inputs: days since last match A 547, B 225; matches on record A 1, B 8; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10LANKOI-LAN  (YES = jintao Lan)
Model: 50%
Kalshi: 11%
Gap: +39 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lorenzo Lorusso vs masaki ishikawa -- M15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10LORISH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| masaki ishikawa (`KXITFMATCH-26NOV10LORISH-ISH`) | 0.18 / 0.22 (69) | 20.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lorenzo Lorusso (`KXITFMATCH-26NOV10LORISH-LOR`) | 0.74 / 0.79 (2) | 76.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Muzammil Murtaza vs Dev Javia -- M15 Kuala Lumpur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207836:209956:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dev Javia (`KXITFMATCH-26NOV10MURJAV-JAV`) | 0.85 / 0.92 (1) | 88.5% | 76.8% | 67.2% | 66.8% [61.1%-73.1%] | -- | -- | -- | -- | PASS | -11.7 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Muzammil Murtaza (`KXITFMATCH-26NOV10MURJAV-MUR`) | 0.06 / 0.13 (31) | 9.5% | 23.2% | 32.8% | 33.2% [26.9%-38.9%] | -- | -- | -- | -- | PASS | +13.7 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 170.0, B 1847.0; serve-point win A 58.8%, B 35.5%; Elo A 1144.9, B 1268.6; model uncertainty 0.0601
* Form inputs: days since last match A 53, B 183; matches on record A 35, B 144; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.062, surface_pool_high +0.057, surface_dev_loose +0.001, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniil Sarksian vs Zaharije-Zak Talic -- M15 Kuala Lumpur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210580:212022:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniil Sarksian (`KXITFMATCH-26NOV10SARTAL-SAR`) | 0.80 / 0.82 (47) | 81.0% | 76.0% | 62.3% | 65.3% [63.3%-67.2%] | -- | -- | -- | -- | PASS | -5.0 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zaharije-Zak Talic (`KXITFMATCH-26NOV10SARTAL-TAL`) | 0.12 / 0.20 (25) | 16.0% | 24.0% | 37.7% | 34.7% [32.8%-36.7%] | -- | -- | -- | -- | PASS | +8.0 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2188.0, B 62.0; serve-point win A 60.9%, B 44.5%; Elo A 1227.8, B 1115.0; model uncertainty 0.0193
* Form inputs: days since last match A 211, B 197; matches on record A 62, B 28; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.019, surface_dev_loose +0.005, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Azuma Visaya vs Aqil Adibi Rahiman -- M15 Kuala Lumpur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10VISADI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aqil Adibi Rahiman (`KXITFMATCH-26NOV10VISADI-ADI`) | 0.12 / 0.67 (16) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Azuma Visaya (`KXITFMATCH-26NOV10VISADI-VIS`) | 0.69 / 0.89 (1) | 79.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Boxiong Zhang vs Shaoyun Liu -- M15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212180:214025:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shaoyun Liu (`KXITFMATCH-26NOV10ZHALIU-LIU`) | 0.29 / 0.32 (0) | 30.5% | 38.6% | 32.4% | 34.8% [33.8%-35.3%] | -- | -- | -- | -- | PASS | +8.1 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Boxiong Zhang (`KXITFMATCH-26NOV10ZHALIU-ZHA`) | 0.67 / 0.70 (198) | 68.5% | 61.4% | 67.6% | 65.2% [64.7%-66.2%] | -- | -- | -- | -- | PASS | -7.1 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 109.0, B 496.0; serve-point win A 59.9%, B 42.3%; Elo A 1247.1, B 1138.5; model uncertainty 0.0072
* Form inputs: days since last match A 204, B 204; matches on record A 2, B 21; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose +0.001, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mayuka Aikawa vs Momoko Kobori -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215468:219892:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mayuka Aikawa (`KXITFWMATCH-26NOV10AIKKOB-AIK`) | 0.38 / 0.40 (99) | 39.0% | 22.3% | 18.0% | 24.1% [20.2%-32.1%] | -- | -- | -- | -- | PASS | -16.7 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Momoko Kobori (`KXITFWMATCH-26NOV10AIKKOB-KOB`) | 0.61 / 0.62 (168) | 61.5% | 77.7% | 82.0% | 75.9% [67.9%-79.8%] | -- | -- | -- | -- | WATCH | +16.2 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1667.0, B 1427.0; serve-point win A 52.6%, B 41.7%; Elo A 1428.9, B 1568.5; model uncertainty 0.0595
* Form inputs: days since last match A 232, B 9; matches on record A 303, B 374; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10AIKKOB-KOB  (YES = Momoko Kobori)
Model: 78%
Kalshi: 62%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.004, surface_dev_loose -0.016, surface_dev_tight +0.017
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rinko Matsuda vs Yuka Naito -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259690:267695:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rinko Matsuda (`KXITFWMATCH-26NOV10MATNAI-MAT`) | 0.76 / 0.85 (5) | 80.5% | 89.1% | 83.1% | 80.0% [79.2%-80.7%] | -- | -- | -- | -- | PASS | +8.7 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuka Naito (`KXITFWMATCH-26NOV10MATNAI-NAI`) | 0.14 / 0.18 (5) | 16.0% | 10.8% | 16.9% | 20.1% [19.3%-20.8%] | -- | -- | -- | -- | PASS | -5.2 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2804.0, B 274.0; serve-point win A 59.0%, B 50.3%; Elo A 1494.2, B 1259.9; model uncertainty 0.0075
* Form inputs: days since last match A 10, B 302; matches on record A 204, B 8; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.007, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Priska Madelyn Nugroho vs Chia Yi Tsao -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221187:259623:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Priska Madelyn Nugroho (`KXITFWMATCH-26NOV10NUGTSA-NUG`) | 0.81 / 0.85 (25) | 83.0% | 61.8% | 54.7% | 59.3% [57.3%-63.5%] | -- | -- | -- | -- | PASS | -21.2 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Chia Yi Tsao (`KXITFWMATCH-26NOV10NUGTSA-TSA`) | 0.13 / 0.17 (31) | 15.0% | 38.2% | 45.3% | 40.7% [36.5%-42.7%] | -- | -- | -- | -- | WATCH | +23.2 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2457.0, B 824.0; serve-point win A 59.2%, B 43.1%; Elo A 1567.2, B 1482.7; model uncertainty 0.0311
* Form inputs: days since last match A 225, B 204; matches on record A 235, B 145; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10NUGTSA-TSA  (YES = Chia Yi Tsao)
Model: 38%
Kalshi: 15%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.015, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ke Ren vs Maria Pankratova -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10RENPAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Pankratova (`KXITFWMATCH-26NOV10RENPAN-PAN`) | 0.66 / 0.76 (78) | 71.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ke Ren (`KXITFWMATCH-26NOV10RENPAN-REN`) | 0.24 / 0.27 (5) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kanon Sawashiro vs Ayano Shimizu -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215550:263905:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanon Sawashiro (`KXITFWMATCH-26NOV10SAWSHI-SAW`) | 0.46 / 0.49 (56) | 47.5% | 35.6% | 59.6% | 36.4% [22.3%-46.2%] | -- | -- | -- | -- | PASS | -11.9 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ayano Shimizu (`KXITFWMATCH-26NOV10SAWSHI-SHI`) | 0.49 / 0.54 (301) | 51.5% | 64.4% | 40.5% | 63.6% [53.8%-77.7%] | -- | -- | -- | -- | WATCH | +12.9 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 827.0, B 1770.0; serve-point win A 50.8%, B 46.4%; Elo A 1347.9, B 1539.0; model uncertainty 0.1199
* Form inputs: days since last match A 24, B 197; matches on record A 37, B 430; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.049, surface_pool_high +0.046, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yushan Shao vs Fang An Lin -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:252586:269253:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fang An Lin (`KXITFWMATCH-26NOV10SHALIN-LIN`) | 0.14 / 0.17 (7) | 15.5% | 32.1% | 29.6% | 37.4% [35.4%-40.5%] | -- | -- | -- | -- | PASS | +16.6 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yushan Shao (`KXITFWMATCH-26NOV10SHALIN-SHA`) | 0.79 / 0.85 (74) | 82.0% | 67.9% | 70.4% | 62.6% [59.5%-64.6%] | -- | -- | -- | -- | PASS | -14.1 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1123.0, B 762.0; serve-point win A 55.1%, B 48.4%; Elo A 1398.2, B 1341.7; model uncertainty 0.0255
* Form inputs: days since last match A 35, B 204; matches on record A 29, B 114; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10SHALIN-LIN  (YES = Fang An Lin)
Model: 32%
Kalshi: 16%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.015, surface_dev_loose +0.015, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Huang / Zhang vs Ito / Kinoshita -- W75 Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 08:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10HUAZHAITOKIN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Huang / Zhang (`KXITFWDOUBLES-26NOV10HUAZHAITOKIN-HUAZHA`) | 0.27 / 0.67 (75) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ito / Kinoshita (`KXITFWDOUBLES-26NOV10HUAZHAITOKIN-ITOKIN`) | 0.24 / 0.50 (2) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Simes / Subasic vs Gadecki / Wen Wan -- W75 Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 08:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10SIMSUBGADWEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gadecki / Wen Wan (`KXITFWDOUBLES-26NOV10SIMSUBGADWEN-GADWEN`) | 0.62 / 0.86 (178) | 74.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Simes / Subasic (`KXITFWDOUBLES-26NOV10SIMSUBGADWEN-SIMSUB`) | 0.11 / 0.27 (56) | 19.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Stevens / Thompson vs Abe / Zheng -- W75 Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 08:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10STETHOABEZHE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Abe / Zheng (`KXITFWDOUBLES-26NOV10STETHOABEZHE-ABEZHE`) | 0.62 / 0.89 (56) | 75.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stevens / Thompson (`KXITFWDOUBLES-26NOV10STETHOABEZHE-STETHO`) | 0.06 / 0.23 (31) | 14.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Penn Charusorn vs Adrian Arcon -- M15 Hua Hin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210417:214094:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Arcon (`KXITFMATCH-26NOV10CHAARC-ARC`) | 0.39 / 0.43 (197) | 41.0% | 19.7% | 16.8% | 23.9% [22.1%-24.9%] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -21.3 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Penn Charusorn (`KXITFMATCH-26NOV10CHAARC-CHA`) | 0.56 / 0.59 (35) | 57.5% | 80.3% | 83.2% | 76.1% [75.1%-77.9%] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +22.8 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 193.0, B 522.0; serve-point win A 65.9%, B 40.9%; Elo A 1198.6, B 1008.6; model uncertainty 0.0136
* Form inputs: days since last match A 379, B 190; matches on record A 5, B 22; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10CHAARC-CHA  (YES = Penn Charusorn)
Model: 80%
Kalshi: 57%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.008, surface_dev_loose +0.008, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yeongseok Jeong vs Seongchan Hong -- M15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10JEOHON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Seongchan Hong (`KXITFMATCH-26NOV10JEOHON-HON`) | 0.88 / 0.97 (495) | 92.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yeongseok Jeong (`KXITFMATCH-26NOV10JEOHON-JEO`) | 0.04 / 0.06 (433) | 5.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aryan Lakshmanan vs Jordan Hasson -- M15 Hua Hin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200487:212767:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jordan Hasson (`KXITFMATCH-26NOV10LAKHAS-HAS`) | 0.68 / 0.73 (50) | 70.5% | 71.4% | 85.5% | 66.8% [61.2%-72.5%] | -- | -- | -- | -- | PASS | +0.9 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aryan Lakshmanan (`KXITFMATCH-26NOV10LAKHAS-LAK`) | 0.26 / 0.29 (63) | 27.5% | 28.6% | 14.5% | 33.2% [27.5%-38.8%] | -- | -- | -- | -- | PASS | +1.1 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 548.0, B 311.0; serve-point win A 59.5%, B 36.0%; Elo A 1134.0, B 1216.0; model uncertainty 0.0566
* Form inputs: days since last match A 232, B 197; matches on record A 18, B 118; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high +0.000, surface_dev_loose -0.009, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Markus Malaszszak vs Daisuke Sumizawa -- M15 Hua Hin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200671:212308:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Markus Malaszszak (`KXITFMATCH-26NOV10MALSUM-MAL`) | 0.71 / 0.73 (132) | 72.0% | 49.4% | 62.1% | 54.6% [50.0%-57.6%] | 72.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -22.6 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daisuke Sumizawa (`KXITFMATCH-26NOV10MALSUM-SUM`) | 0.26 / 0.28 (18) | 27.0% | 50.6% | 37.9% | 45.4% [42.4%-50.0%] | 28.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +23.6 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1157.0, B 1327.0; serve-point win A 60.8%, B 39.0%; Elo A 1255.9, B 1265.2; model uncertainty 0.0382
* Form inputs: days since last match A 197, B 225; matches on record A 40, B 202; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10MALSUM-SUM  (YES = Daisuke Sumizawa)
Model: 51%
Kalshi: 27%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stefan Storch vs Yue Xia -- M15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213532:213883:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefan Storch (`KXITFMATCH-26NOV10STOXIA-STO`) | 0.30 / 0.34 (43) | 32.0% | 58.6% | 51.0% | 49.0% [49.0%-51.0%] | -- | -- | -- | -- | PASS | +26.6 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yue Xia (`KXITFMATCH-26NOV10STOXIA-XIA`) | 0.62 / 0.69 (219) | 65.5% | 41.4% | 49.0% | 51.0% [49.0%-51.0%] | -- | -- | -- | -- | PASS | -24.1 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 469.0, B 202.0; serve-point win A 62.8%, B 38.9%; Elo A 1199.1, B 1205.9; model uncertainty 0.0102
* Form inputs: days since last match A 232, B 428; matches on record A 12, B 4; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10STOXIA-STO  (YES = Stefan Storch)
Model: 59%
Kalshi: 32%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zhengyu Sun vs Jordan Chiu -- M15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207780:212875:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jordan Chiu (`KXITFMATCH-26NOV10SUNCHI-CHI`) | 0.69 / 0.76 (118) | 72.5% | 28.3% | 64.4% | 30.8% [25.7%-37.5%] | -- | -- | -- | -- | PASS | -44.2 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zhengyu Sun (`KXITFMATCH-26NOV10SUNCHI-SUN`) | 0.22 / 0.25 (33) | 23.5% | 71.7% | 35.6% | 69.2% [62.5%-74.3%] | -- | -- | -- | -- | PASS | +48.2 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 367.0, B 402.0; serve-point win A 58.7%, B 45.7%; Elo A 1206.1, B 1004.9; model uncertainty 0.059
* Form inputs: days since last match A 197, B 197; matches on record A 12, B 30; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10SUNCHI-SUN  (YES = Zhengyu Sun)
Model: 72%
Kalshi: 24%
Gap: +48 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.013, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rigele Te vs Alexey Aleshchev -- M15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:134310:144751:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexey Aleshchev (`KXITFMATCH-26NOV10TEXALE-ALE`) | 0.05 / 0.07 (21) | 6.0% | 13.5% | 23.9% | 16.2% [13.2%-18.1%] | -- | -- | -- | -- | WATCH | +7.5 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rigele Te (`KXITFMATCH-26NOV10TEXALE-TEX`) | 0.92 / 0.95 (10) | 93.5% | 86.5% | 76.1% | 83.8% [81.9%-86.8%] | -- | -- | -- | -- | PASS | -7.0 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1492.0, B 1173.0; serve-point win A 66.9%, B 41.8%; Elo A 1414.4, B 1059.7; model uncertainty 0.0246
* Form inputs: days since last match A 15, B 197; matches on record A 319, B 69; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.006, surface_dev_loose +0.011, surface_dev_tight -0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## James Van Herzeele vs Ren Nakamura -- M15 Hua Hin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:125843:211329:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ren Nakamura (`KXITFMATCH-26NOV10VANNAK-NAK`) | 0.20 / 0.27 (5) | 23.5% | 28.0% | 30.9% | 29.5% [27.8%-30.8%] | -- | -- | -- | -- | PASS | +4.5 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| James Van Herzeele (`KXITFMATCH-26NOV10VANNAK-VAN`) | 0.70 / 0.76 (243) | 73.0% | 72.0% | 69.1% | 70.5% [69.2%-72.2%] | -- | -- | -- | -- | PASS | -1.0 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 879.0, B 514.0; serve-point win A 63.4%, B 41.2%; Elo A 1193.2, B 1036.6; model uncertainty 0.015
* Form inputs: days since last match A 239, B 197; matches on record A 24, B 98; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.009, surface_dev_loose +0.004, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jialan Cai vs Valeria Savinykh -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:202443:267498:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jialan Cai (`KXITFWMATCH-26NOV10CAISAV-CAI`) | 0.03 / 0.10 (79) | 6.5% | 4.9% | 47.3% | 12.1% [10.5%-14.3%] | -- | -- | -- | -- | PASS | -1.6 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valeria Savinykh (`KXITFWMATCH-26NOV10CAISAV-SAV`) | 0.88 / 0.94 (10) | 91.0% | 95.1% | 52.7% | 87.9% [85.7%-89.5%] | -- | -- | -- | -- | PASS | +4.1 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 204.0, B 1181.0; serve-point win A 48.2%, B 39.3%; Elo A 1218.7, B 1611.5; model uncertainty 0.0189
* Form inputs: days since last match A 211, B 42; matches on record A 11, B 735; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.005, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Junlu Sun vs Ru Xi Wu -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264970:270262:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Junlu Sun (`KXITFWMATCH-26NOV10SUNWUX-SUN`) | 0.49 / 0.52 (5) | 50.5% | 26.2% | 56.9% | 34.4% [33.4%-34.4%] | -- | -- | -- | -- | PASS | -24.3 pp | HIGH_REVIEW (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Ru Xi Wu (`KXITFWMATCH-26NOV10SUNWUX-WUX`) | 0.46 / 0.48 (48) | 47.0% | 73.8% | 43.1% | 65.6% [65.6%-66.6%] | -- | -- | -- | -- | PASS | +26.8 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 171.0; serve-point win A 50.5%, B 44.7%; Elo A 1304.4, B 1417.8; model uncertainty 0.005
* Form inputs: days since last match A 785, B 42; matches on record A 15, B 3; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10SUNWUX-WUX  (YES = Ru Xi Wu)
Model: 74%
Kalshi: 47%
Gap: +27 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jayson Blando vs Natsuki Yamamoto -- M15 Kuala Lumpur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10BLAYAM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jayson Blando (`KXITFMATCH-26NOV10BLAYAM-BLA`) | 0.54 / 0.59 (1) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Natsuki Yamamoto (`KXITFMATCH-26NOV10BLAYAM-YAM`) | 0.38 / 0.45 (1) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hien Pham vs Gunawan Trismuwantara -- M15 Kuala Lumpur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10PHATRI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hien Pham (`KXITFMATCH-26NOV10PHATRI-PHA`) | 0.19 / 0.30 (7) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gunawan Trismuwantara (`KXITFMATCH-26NOV10PHATRI-TRI`) | 0.70 / 0.82 (11) | 76.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aulia / Micic vs Barry / Kawaguchi -- W75 Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10AULMICBARKAW:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aulia / Micic (`KXITFWDOUBLES-26NOV10AULMICBARKAW-AULMIC`) | 0.46 / 0.58 (59) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Barry / Kawaguchi (`KXITFWDOUBLES-26NOV10AULMICBARKAW-BARKAW`) | 0.40 / 0.61 (20) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Chaudhari / Hoedt vs Jeong / Young Suh Lee -- W75 Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10CHAHOEJEOYOU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chaudhari / Hoedt (`KXITFWDOUBLES-26NOV10CHAHOEJEOYOU-CHAHOE`) | 0.07 / 0.62 (3) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jeong / Young Suh Lee (`KXITFWDOUBLES-26NOV10CHAHOEJEOYOU-JEOYOU`) | 0.51 / 0.52 (52) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ali Baig / Siddiq Kamaruzzaman vs Alam / Sheng Koay -- M15 Kuala Lumpur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10ALISIDALASHE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alam / Sheng Koay (`KXITFDOUBLES-26NOV10ALISIDALASHE-ALASHE`) | 0.06 / 0.89 (33) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ali Baig / Siddiq Kamaruzzaman (`KXITFDOUBLES-26NOV10ALISIDALASHE-ALISID`) | 0.11 / 0.89 (37) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Julien De Cuyper vs Congsup Congcar -- M15 Hua Hin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:133667:207761:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Congsup Congcar (`KXITFMATCH-26NOV10DECCON-CON`) | 0.29 / 0.32 (15) | 30.5% | 45.5% | 24.1% | 44.3% [38.2%-50.0%] | -- | -- | -- | -- | PASS | +15.0 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Julien De Cuyper (`KXITFMATCH-26NOV10DECCON-DEC`) | 0.65 / 0.67 (75) | 66.0% | 54.5% | 75.9% | 55.7% [50.0%-61.8%] | -- | -- | -- | -- | PASS | -11.5 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 549.0, B 318.0; serve-point win A 59.5%, B 41.4%; Elo A 1128.6, B 1122.8; model uncertainty 0.0591
* Form inputs: days since last match A 232, B 302; matches on record A 46, B 121; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10DECCON-CON  (YES = Congsup Congcar)
Model: 46%
Kalshi: 30%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.000, surface_dev_loose +0.015, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Krittin Koaykul vs Leo Vithoontien -- M15 Hua Hin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111772:210672:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Krittin Koaykul (`KXITFMATCH-26NOV10KOAVIT-KOA`) | 0.04 / 0.11 (21) | 7.5% | 9.0% | 2.0% | 11.3% [6.1%-17.3%] | -- | -- | -- | -- | PASS | +1.5 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Leo Vithoontien (`KXITFMATCH-26NOV10KOAVIT-VIT`) | 0.86 / 0.94 (62) | 90.0% | 91.0% | 98.0% | 88.7% [82.7%-93.9%] | -- | -- | -- | -- | PASS | +1.0 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 442.0, B 2997.0; serve-point win A 57.0%, B 32.3%; Elo A 1087.5, B 1363.6; model uncertainty 0.056
* Form inputs: days since last match A 379, B 176; matches on record A 62, B 165; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.011, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lomakin / Mukund vs Oki / Taka -- M15 Kuala Lumpur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10LOMMUKOKITAK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lomakin / Mukund (`KXITFDOUBLES-26NOV10LOMMUKOKITAK-LOMMUK`) | 0.10 / 0.78 (5) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Oki / Taka (`KXITFDOUBLES-26NOV10LOMMUKOKITAK-OKITAK`) | 0.15 / 0.38 (56) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tsz Fu Wong vs Pawit Sornlaksup -- M15 Hua Hin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210687:212971:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pawit Sornlaksup (`KXITFMATCH-26NOV10WONSOR-SOR`) | 0.92 / 0.94 (60) | 93.0% | 88.0% | 87.7% | 86.6% [84.8%-89.7%] | 92.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.0 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tsz Fu Wong (`KXITFMATCH-26NOV10WONSOR-WON`) | 0.05 / 0.10 (79) | 7.5% | 12.0% | 12.3% | 13.4% [10.3%-15.2%] | 7.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.5 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 498.0, B 2078.0; serve-point win A 54.2%, B 36.8%; Elo A 1070.2, B 1391.4; model uncertainty 0.0245
* Form inputs: days since last match A 53, B 197; matches on record A 20, B 94; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.005, surface_dev_loose -0.008, surface_dev_tight +0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Denis Yevseyev vs Jirat Navasirisomboon -- M15 Hua Hin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106187:127143:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jirat Navasirisomboon (`KXITFMATCH-26NOV10YEVNAV-NAV`) | 0.14 / 0.33 (26) | 23.5% | 14.6% | 7.9% | 13.9% [11.4%-16.0%] | -- | -- | -- | -- | PASS | -8.9 pp | NORMAL | STALE | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Denis Yevseyev (`KXITFMATCH-26NOV10YEVNAV-YEV`) | 0.61 / 0.89 (25) | 75.0% | 85.4% | 92.1% | 86.1% [84.0%-88.6%] | -- | -- | -- | -- | PASS | +10.4 pp | REVIEW | STALE | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5377.0, B 409.0; serve-point win A 61.8%, B 46.2%; Elo A 1524.8, B 1232.6; model uncertainty 0.0231
* Form inputs: days since last match A 64, B 197; matches on record A 911, B 138; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.017, surface_pool_high -0.018, surface_dev_loose +0.011, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sae Noguchi vs Sara Saito -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260170:269866:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sae Noguchi (`KXITFWMATCH-26NOV10NOGSAI-NOG`) | 0.24 / 0.26 (30) | 25.0% | 31.9% | 52.7% | 41.0% [29.6%-47.3%] | -- | -- | -- | -- | WATCH | +6.9 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sara Saito (`KXITFWMATCH-26NOV10NOGSAI-SAI`) | 0.72 / 0.73 (224) | 72.5% | 68.1% | 47.3% | 59.0% [52.7%-70.4%] | -- | -- | -- | -- | PASS | -4.4 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1076.0, B 3341.0; serve-point win A 49.9%, B 46.6%; Elo A 1452.4, B 1574.9; model uncertainty 0.0887
* Form inputs: days since last match A 211, B 43; matches on record A 33, B 198; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.041, surface_pool_high +0.042, surface_dev_loose +0.021, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rina Saigo vs JiaYi Wang -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221099:265692:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rina Saigo (`KXITFWMATCH-26NOV10SAIWAN-SAI`) | 0.49 / 0.50 (248) | 49.5% | 47.0% | 29.2% | 39.0% [33.9%-52.7%] | -- | -- | -- | -- | PASS | -2.5 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| JiaYi Wang (`KXITFWMATCH-26NOV10SAIWAN-WAN`) | 0.49 / 0.55 (136) | 52.0% | 53.0% | 70.8% | 61.1% [47.3%-66.1%] | -- | -- | -- | -- | PASS | +1.0 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3065.0, B 2216.0; serve-point win A 53.6%, B 45.8%; Elo A 1547.5, B 1510.1; model uncertainty 0.0937
* Form inputs: days since last match A 17, B 42; matches on record A 396, B 72; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.010, surface_dev_loose -0.015, surface_dev_tight +0.026
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Naho Sato vs Anri Nagata -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216315:220997:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anri Nagata (`KXITFWMATCH-26NOV10SATNAG-NAG`) | 0.05 / 0.09 (33) | 7.0% | 30.5% | 35.4% | 32.9% [31.0%-34.4%] | -- | -- | -- | -- | WATCH | +23.5 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Naho Sato (`KXITFWMATCH-26NOV10SATNAG-SAT`) | 0.89 / 0.94 (48) | 91.5% | 69.5% | 64.6% | 67.1% [65.6%-69.0%] | -- | -- | -- | -- | PASS | -22.0 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1522.0, B 1011.0; serve-point win A 54.8%, B 49.0%; Elo A 1476.0, B 1339.1; model uncertainty 0.0169
* Form inputs: days since last match A 204, B 260; matches on record A 304, B 192; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10SATNAG-NAG  (YES = Anri Nagata)
Model: 30%
Kalshi: 7%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuhan Wang vs Sayaka Ishii -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259967:264205:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sayaka Ishii (`KXITFWMATCH-26NOV10WANISH-ISH`) | 0.50 / 0.53 (134) | 51.5% | 74.3% | 40.6% | 58.9% [52.6%-70.3%] | -- | -- | -- | -- | WATCH | +22.8 pp | HIGH_REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuhan Wang (`KXITFWMATCH-26NOV10WANISH-WAN`) | 0.47 / 0.49 (160) | 48.0% | 25.7% | 59.4% | 41.1% [29.7%-47.3%] | -- | -- | -- | -- | PASS | -22.3 pp | HIGH_REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1724.0, B 1713.0; serve-point win A 53.3%, B 41.8%; Elo A 1428.1, B 1644.8; model uncertainty 0.0882
* Form inputs: days since last match A 40, B 16; matches on record A 44, B 193; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10WANISH-ISH  (YES = Sayaka Ishii)
Model: 74%
Kalshi: 52%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.010, surface_dev_loose +0.011, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## James Connel vs Zhenxiong Dong -- M15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 10:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207478:212250:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| James Connel (`KXITFMATCH-26NOV10CONDON-CON`) | 0.77 / 0.84 (50) | 80.5% | 88.2% | 95.7% | 87.8% [81.0%-93.2%] | -- | -- | -- | -- | PASS | +7.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zhenxiong Dong (`KXITFMATCH-26NOV10CONDON-DON`) | 0.17 / 0.23 (8) | 20.0% | 11.8% | 4.3% | 12.2% [6.9%-19.0%] | -- | -- | -- | -- | PASS | -8.2 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 844.0, B 739.0; serve-point win A 64.1%, B 45.1%; Elo A 1378.7, B 1121.3; model uncertainty 0.0607
* Form inputs: days since last match A 197, B 204; matches on record A 26, B 66; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.003, surface_dev_loose +0.010, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maxim Zhukov vs Xirui Han -- M15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 10:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210393:212472:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xirui Han (`KXITFMATCH-26NOV10ZHUHAN-HAN`) | 0.22 / 0.23 (50) | 22.5% | 10.7% | 13.9% | 14.8% [12.7%-16.2%] | -- | -- | -- | -- | PASS | -11.8 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maxim Zhukov (`KXITFMATCH-26NOV10ZHUHAN-ZHU`) | 0.77 / 0.80 (132) | 78.5% | 89.3% | 86.1% | 85.2% [83.8%-87.3%] | -- | -- | -- | -- | PASS | +10.8 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2791.0, B 542.0; serve-point win A 61.0%, B 48.4%; Elo A 1452.3, B 1153.8; model uncertainty 0.0173
* Form inputs: days since last match A 92, B 386; matches on record A 199, B 15; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.003, surface_pool_high +0.000, surface_dev_loose +0.009, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xi Luo vs Marianna Shikhanova -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 10:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264069:269845:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xi Luo (`KXITFWMATCH-26NOV10LUOSHI-LUO`) | 0.64 / 0.69 (170) | 66.5% | 93.2% | 69.0% | 76.1% [75.3%-76.9%] | -- | -- | -- | -- | PASS | +26.7 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marianna Shikhanova (`KXITFWMATCH-26NOV10LUOSHI-SHI`) | 0.28 / 0.33 (34) | 30.5% | 6.8% | 31.0% | 23.9% [23.1%-24.7%] | -- | -- | -- | -- | PASS | -23.7 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 827.0, B 49.0; serve-point win A 58.8%, B 52.3%; Elo A 1415.7, B 1210.1; model uncertainty 0.0083
* Form inputs: days since last match A 197, B 379; matches on record A 43, B 6; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10LUOSHI-LUO  (YES = Xi Luo)
Model: 93%
Kalshi: 66%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yingqun Sun vs Yuyao Li -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 10:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264029:264986:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuyao Li (`KXITFWMATCH-26NOV10SUNLIX-LIX`) | 0.17 / 0.20 (75) | 18.5% | 20.6% | 23.4% | 29.8% [25.9%-33.5%] | -- | -- | -- | -- | PASS | +2.1 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yingqun Sun (`KXITFWMATCH-26NOV10SUNLIX-SUN`) | 0.77 / 0.82 (3) | 79.5% | 79.4% | 76.6% | 70.2% [66.5%-74.1%] | -- | -- | -- | -- | PASS | -0.1 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1826.0, B 606.0; serve-point win A 59.7%, B 46.6%; Elo A 1387.9, B 1258.4; model uncertainty 0.0381
* Form inputs: days since last match A 197, B 197; matches on record A 99, B 19; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.005, surface_dev_loose +0.013, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ho Ching Wu vs Arina Varaksina -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 10:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211208:255662:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arina Varaksina (`KXITFWMATCH-26NOV10WUXVAR-VAR`) | 0.53 / 0.54 (54) | 53.5% | 45.0% | 56.9% | 40.0% [35.4%-43.6%] | -- | -- | -- | -- | PASS | -8.5 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ho Ching Wu (`KXITFWMATCH-26NOV10WUXVAR-WUX`) | 0.42 / 0.46 (11) | 44.0% | 55.0% | 43.1% | 60.0% [56.4%-64.6%] | -- | -- | -- | -- | PASS | +11.0 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 678.0, B 586.0; serve-point win A 53.7%, B 47.2%; Elo A 1398.9, B 1277.4; model uncertainty 0.0411
* Form inputs: days since last match A 197, B 204; matches on record A 414, B 27; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ziyu Zhou vs Xiao Tang -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 10:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10ZHOTAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xiao Tang (`KXITFWMATCH-26NOV10ZHOTAN-TAN`) | 0.76 / 0.78 (140) | 77.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ziyu Zhou (`KXITFWMATCH-26NOV10ZHOTAN-ZHO`) | 0.21 / 0.22 (85) | 21.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arakawa / Ozeki vs Ishijima / Okawa -- W50 Yokohama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11ARAOZEISHOKA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arakawa / Ozeki (`KXITFWDOUBLES-26NOV11ARAOZEISHOKA-ARAOZE`) | 0.06 / 0.89 (4) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ishijima / Okawa (`KXITFWDOUBLES-26NOV11ARAOZEISHOKA-ISHOKA`) | 0.05 / 0.89 (4) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kuwata / Shimizu vs Aikawa / Yodpetch -- W50 Yokohama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11KUWSHIAIKYOD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aikawa / Yodpetch (`KXITFWDOUBLES-26NOV11KUWSHIAIKYOD-AIKYOD`) | 0.41 / 0.58 (56) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kuwata / Shimizu (`KXITFWDOUBLES-26NOV11KUWSHIAIKYOD-KUWSHI`) | 0.46 / 0.63 (67) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Sawashiro / Uemura vs Madelyn Nugroho / Ovcharenko -- W50 Yokohama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11SAWUEMMADOVC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Madelyn Nugroho / Ovcharenko (`KXITFWDOUBLES-26NOV11SAWUEMMADOVC-MADOVC`) | 0.76 / 0.90 (1) | 83.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sawashiro / Uemura (`KXITFWDOUBLES-26NOV11SAWUEMMADOVC-SAWUEM`) | 0.10 / 0.23 (56) | 16.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tian Deng / Sato vs Hosoki / Katsumi -- W50 Yokohama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11TIASATHOSKAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hosoki / Katsumi (`KXITFWDOUBLES-26NOV11TIASATHOSKAT-HOSKAT`) | 0.53 / 0.67 (56) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tian Deng / Sato (`KXITFWDOUBLES-26NOV11TIASATHOSKAT-TIASAT`) | 0.35 / 0.53 (57) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Yan Cheng Chen vs Tianhui Zhang -- M15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212221:212460:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yan Cheng Chen (`KXITFMATCH-26NOV11CHEZHA-CHE`) | 0.19 / 0.28 (5) | 23.5% | 24.6% | 27.9% | 27.5% [24.0%-30.2%] | -- | -- | -- | -- | PASS | +1.1 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tianhui Zhang (`KXITFMATCH-26NOV11CHEZHA-ZHA`) | 0.73 / 0.74 (96) | 73.5% | 75.4% | 72.1% | 72.5% [69.8%-76.0%] | -- | -- | -- | -- | PASS | +1.9 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 550.0, B 1273.0; serve-point win A 56.1%, B 38.6%; Elo A 1164.0, B 1331.9; model uncertainty 0.0308
* Form inputs: days since last match A 211, B 15; matches on record A 19, B 78; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.004, surface_dev_loose -0.009, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vraj Gohil vs Sanhui Shin -- M15 Hua Hin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11GOHSHI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vraj Gohil (`KXITFMATCH-26NOV11GOHSHI-GOH`) | 0.04 / 0.05 (1) | 4.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sanhui Shin (`KXITFMATCH-26NOV11GOHSHI-SHI`) | 0.90 / 0.96 (61) | 93.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hasson / Van Sambeek vs Charusorn / Chen -- M15 Hua Hin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11HASVANCHACHE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charusorn / Chen (`KXITFDOUBLES-26NOV11HASVANCHACHE-CHACHE`) | 0.19 / 0.41 (56) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hasson / Van Sambeek (`KXITFDOUBLES-26NOV11HASVANCHACHE-HASVAN`) | 0.67 / 0.78 (113) | 72.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Veerawit Kamput vs Ergi Kirkin -- M15 Hua Hin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11KAMKIR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Veerawit Kamput (`KXITFMATCH-26NOV11KAMKIR-KAM`) | 0.03 / 0.06 (15) | 4.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ergi Kirkin (`KXITFMATCH-26NOV11KAMKIR-KIR`) | 0.88 / 0.95 (10) | 91.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Liangxuan Liu vs Dong Ju Kim -- M15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11LIUKIM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dong Ju Kim (`KXITFMATCH-26NOV11LIUKIM-KIM`) | 0.91 / 0.97 (301) | 94.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Liangxuan Liu (`KXITFMATCH-26NOV11LIUKIM-LIU`) | 0.03 / 0.09 (55) | 6.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Thada Grohbruegge / Sootinun-Opart vs Taddeo Majoli Maggioli / Van Herzeele -- M15 Hua Hin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11THASOOTADVAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Taddeo Majoli Maggioli / Van Herzeele (`KXITFDOUBLES-26NOV11THASOOTADVAN-TADVAN`) | 0.05 / 0.89 (4) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Thada Grohbruegge / Sootinun-Opart (`KXITFDOUBLES-26NOV11THASOOTADVAN-THASOO`) | 0.04 / 0.89 (4) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Xinle Geng vs Xichen Zhao -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:252494:270132:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xinle Geng (`KXITFWMATCH-26NOV11GENZHA-GEN`) | 0.57 / 0.78 (1) | 67.5% | 76.6% | 76.8% | 67.5% [63.6%-72.1%] | -- | -- | -- | -- | PASS | +9.1 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Xichen Zhao (`KXITFWMATCH-26NOV11GENZHA-ZHA`) | 0.28 / 0.37 (39) | 32.5% | 23.4% | 23.2% | 32.5% [27.9%-36.4%] | -- | -- | -- | -- | PASS | -9.1 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 429.0, B 896.0; serve-point win A 57.5%, B 48.0%; Elo A 1396.9, B 1293.3; model uncertainty 0.0424
* Form inputs: days since last match A 386, B 197; matches on record A 8, B 133; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Peangtarn Plipuech vs Alina Tikhonova -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:204223:270431:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Peangtarn Plipuech (`KXITFWMATCH-26NOV11PLITIK-PLI`) | 0.26 / 0.27 (78) | 26.5% | 43.4% | 20.8% | 47.9% [40.0%-54.3%] | -- | -- | -- | -- | PASS | +16.9 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alina Tikhonova (`KXITFWMATCH-26NOV11PLITIK-TIK`) | 0.71 / 0.72 (1) | 71.5% | 56.6% | 79.2% | 52.1% [45.7%-60.0%] | -- | -- | -- | -- | PASS | -14.9 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1391.0, B 349.0; serve-point win A 53.0%, B 45.8%; Elo A 1488.6, B 1453.2; model uncertainty 0.0715
* Form inputs: days since last match A 191, B 281; matches on record A 629, B 5; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV11PLITIK-PLI  (YES = Peangtarn Plipuech)
Model: 43%
Kalshi: 26%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high -0.000, surface_dev_loose -0.011, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Wenfei Yu vs Ikumi Yamazaki -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221265:264184:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ikumi Yamazaki (`KXITFWMATCH-26NOV11YUXYAM-YAM`) | 0.68 / 0.79 (126) | 73.5% | 76.8% | 74.4% | 68.5% [61.6%-74.9%] | -- | -- | -- | -- | PASS | +3.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Wenfei Yu (`KXITFWMATCH-26NOV11YUXYAM-YUX`) | 0.22 / 0.34 (8) | 28.0% | 23.2% | 25.6% | 31.5% [25.1%-38.4%] | -- | -- | -- | -- | PASS | -4.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 238.0, B 1933.0; serve-point win A 50.2%, B 44.3%; Elo A 1351.8, B 1477.0; model uncertainty 0.0663
* Form inputs: days since last match A 197, B 197; matches on record A 35, B 215; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.063, surface_pool_high +0.069, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tang / Zhao vs Jin / Sun -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11TANZHAJINSUN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jin / Sun (`KXITFDOUBLES-26NOV11TANZHAJINSUN-JINSUN`) | 0.43 / 0.70 (83) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tang / Zhao (`KXITFDOUBLES-26NOV11TANZHAJINSUN-TANZHA`) | 0.21 / 0.51 (56) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Tobia Costanzo Baragiola Mordini vs Stefan Ilie Bogdan Petre -- M15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213701:214266:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tobia Costanzo Baragiola Mordini (`KXITFMATCH-26NOV11BARPET-BAR`) | 0.74 / 0.79 (102) | 76.5% | 45.6% | 36.0% | 42.1% [40.6%-44.8%] | -- | -- | -- | -- | PASS | -30.9 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Stefan Ilie Bogdan Petre (`KXITFMATCH-26NOV11BARPET-PET`) | 0.17 / 0.26 (1) | 21.5% | 54.4% | 64.0% | 57.9% [55.2%-59.5%] | -- | -- | -- | -- | PASS | +33.0 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1087.0, B 426.0; serve-point win A 55.7%, B 43.5%; Elo A 1181.4, B 1222.1; model uncertainty 0.0213
* Form inputs: days since last match A 211, B 281; matches on record A 26, B 7; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV11BARPET-PET  (YES = Stefan Ilie Bogdan Petre)
Model: 54%
Kalshi: 22%
Gap: +33 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.000, surface_dev_loose -0.016, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alessio Basile vs Jannik Maute -- M15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210339:211450:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alessio Basile (`KXITFMATCH-26NOV11BASMAU-BAS`) | 0.55 / 0.58 (7) | 56.5% | 71.3% | 69.5% | 65.2% [63.2%-69.6%] | -- | -- | -- | -- | PASS | +14.8 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jannik Maute (`KXITFMATCH-26NOV11BASMAU-MAU`) | 0.44 / 0.51 (6) | 47.5% | 28.7% | 30.5% | 34.8% [30.4%-36.8%] | -- | -- | -- | -- | PASS | -18.8 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 952.0, B 181.0; serve-point win A 60.6%, B 43.7%; Elo A 1252.5, B 1143.9; model uncertainty 0.0319
* Form inputs: days since last match A 351, B 211; matches on record A 43, B 29; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.019, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stepan Baum vs Dmitry Popko -- M15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:122078:212068:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stepan Baum (`KXITFMATCH-26NOV11BAUPOP-BAU`) | 0.32 / 0.42 (43) | 37.0% | 22.5% | 34.6% | 26.8% [19.5%-32.3%] | -- | -- | -- | -- | PASS | -14.5 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dmitry Popko (`KXITFMATCH-26NOV11BAUPOP-POP`) | 0.53 / 0.77 (4) | 65.0% | 77.5% | 65.4% | 73.2% [67.7%-80.5%] | -- | -- | -- | -- | PASS | +12.5 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 461.0, B 3275.0; serve-point win A 54.4%, B 39.8%; Elo A 1370.5, B 1567.7; model uncertainty 0.0637
* Form inputs: days since last match A 351, B 127; matches on record A 24, B 828; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.049, surface_pool_high +0.054, surface_dev_loose -0.001, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cezar Stefan Bentzel vs Mattia Nannelli -- M15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213617:213855:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cezar Stefan Bentzel (`KXITFMATCH-26NOV11BENNAN-BEN`) | 0.18 / 0.27 (6) | 22.5% | 40.0% | 37.6% | 38.6% [36.6%-39.8%] | -- | -- | -- | -- | PASS | +17.5 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mattia Nannelli (`KXITFMATCH-26NOV11BENNAN-NAN`) | 0.72 / 0.82 (108) | 77.0% | 60.0% | 62.4% | 61.4% [60.2%-63.4%] | -- | -- | -- | -- | PASS | -17.0 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 390.0, B 425.0; serve-point win A 56.9%, B 41.2%; Elo A 1125.9, B 1206.3; model uncertainty 0.0158
* Form inputs: days since last match A 337, B 260; matches on record A 6, B 9; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV11BENNAN-BEN  (YES = Cezar Stefan Bentzel)
Model: 40%
Kalshi: 22%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stefan Horia Haita vs Vuk Radjenovic -- M15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211366:213066:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefan Horia Haita (`KXITFMATCH-26NOV11HAIRAD-HAI`) | 0.63 / 0.75 (100) | 69.0% | 41.1% | 30.8% | 42.3% [37.9%-45.9%] | -- | -- | -- | -- | PASS | -27.9 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Vuk Radjenovic (`KXITFMATCH-26NOV11HAIRAD-RAD`) | 0.22 / 0.45 (45) | 33.5% | 58.9% | 69.2% | 57.7% [54.1%-62.1%] | -- | -- | -- | -- | PASS | +25.4 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 614.0, B 799.0; serve-point win A 59.8%, B 38.5%; Elo A 1224.1, B 1242.8; model uncertainty 0.0399
* Form inputs: days since last match A 127, B 372; matches on record A 21, B 71; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV11HAIRAD-RAD  (YES = Vuk Radjenovic)
Model: 59%
Kalshi: 34%
Gap: +25 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.020, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Heorhii Shylov vs Erkut Aydin -- M15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11SHYAYD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Erkut Aydin (`KXITFMATCH-26NOV11SHYAYD-AYD`) | 0.03 / 0.05 (26) | 4.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Heorhii Shylov (`KXITFMATCH-26NOV11SHYAYD-SHY`) | 0.90 / 0.95 (10) | 92.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Evgenii Tiurnev vs Alessandro Bellifemine -- M15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126185:210110:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alessandro Bellifemine (`KXITFMATCH-26NOV11TIUBEL-BEL`) | 0.29 / 0.55 (4) | 42.0% | 12.5% | 3.8% | 8.8% [6.2%-14.0%] | -- | -- | -- | -- | PASS | -29.5 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Evgenii Tiurnev (`KXITFMATCH-26NOV11TIUBEL-TIU`) | 0.55 / 0.61 (64) | 58.0% | 87.5% | 96.2% | 91.2% [86.0%-93.8%] | -- | -- | -- | -- | PASS | +29.5 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1478.0, B 859.0; serve-point win A 66.9%, B 42.2%; Elo A 1505.2, B 1176.5; model uncertainty 0.0392
* Form inputs: days since last match A 232, B 337; matches on record A 579, B 65; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV11TIUBEL-TIU  (YES = Evgenii Tiurnev)
Model: 88%
Kalshi: 58%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.008, surface_dev_loose +0.015, surface_dev_tight -0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Diana-Ioana Simionescu vs Denise Valente -- W15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223416:264978:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diana-Ioana Simionescu (`KXITFWMATCH-26NOV11SIMVAL-SIM`) | 0.83 / 0.88 (1) | 85.5% | 84.1% | 86.3% | 76.0% [69.4%-81.4%] | -- | -- | -- | -- | PASS | -1.4 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Denise Valente (`KXITFWMATCH-26NOV11SIMVAL-VAL`) | 0.15 / 0.19 (13) | 17.0% | 15.9% | 13.7% | 23.9% [18.6%-30.6%] | -- | -- | -- | -- | PASS | -1.1 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1418.0, B 1031.0; serve-point win A 57.6%, B 49.9%; Elo A 1427.4, B 1297.3; model uncertainty 0.0601
* Form inputs: days since last match A 267, B 204; matches on record A 46, B 157; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.012, surface_pool_high -0.008, surface_dev_loose +0.017, surface_dev_tight -0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Robert Guna vs Lars Wagenaar -- M15 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211491:212735:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Robert Guna (`KXITFMATCH-26NOV11GUNWAG-GUN`) | 0.85 / 0.89 (100) | 87.0% | 70.7% | 59.2% | 59.2% [58.2%-59.2%] | -- | -- | -- | -- | PASS | -16.3 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lars Wagenaar (`KXITFMATCH-26NOV11GUNWAG-WAG`) | 0.12 / 0.13 (5) | 12.5% | 29.3% | 40.8% | 40.8% [40.8%-41.8%] | -- | -- | -- | -- | PASS | +16.8 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1036.0, B 53.0; serve-point win A 62.0%, B 42.2%; Elo A 1235.7, B 1174.6; model uncertainty 0.005
* Form inputs: days since last match A 281, B 449; matches on record A 27, B 6; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV11GUNWAG-WAG  (YES = Lars Wagenaar)
Model: 29%
Kalshi: 12%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matyas Kozlovsky vs Josip Simundza -- M15 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210537:214076:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matyas Kozlovsky (`KXITFMATCH-26NOV11KOZSIM-KOZ`) | 0.16 / 0.19 (3) | 17.5% | 34.4% | 39.6% | 45.3% [42.7%-48.9%] | -- | -- | -- | -- | PASS | +16.9 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Josip Simundza (`KXITFMATCH-26NOV11KOZSIM-SIM`) | 0.79 / 0.84 (9) | 81.5% | 65.6% | 60.4% | 54.7% [51.0%-57.3%] | -- | -- | -- | -- | PASS | -15.9 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 172.0, B 2596.0; serve-point win A 55.7%, B 41.2%; Elo A 1273.5, B 1298.8; model uncertainty 0.0314
* Form inputs: days since last match A 211, B 183; matches on record A 3, B 111; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV11KOZSIM-KOZ  (YES = Matyas Kozlovsky)
Model: 34%
Kalshi: 18%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.026, surface_pool_high +0.037, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Timeo Trufelli vs Mac Visser -- M15 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212770:213829:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Timeo Trufelli (`KXITFMATCH-26NOV11TRUVIS-TRU`) | 0.60 / 0.64 (69) | 62.0% | 45.5% | 49.0% | 46.4% [45.4%-46.9%] | -- | -- | -- | -- | PASS | -16.6 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mac Visser (`KXITFMATCH-26NOV11TRUVIS-VIS`) | 0.32 / 0.38 (40) | 35.0% | 54.5% | 51.0% | 53.6% [53.1%-54.6%] | -- | -- | -- | -- | PASS | +19.6 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1101.0, B 752.0; serve-point win A 58.3%, B 40.8%; Elo A 1257.8, B 1295.9; model uncertainty 0.0077
* Form inputs: days since last match A 197, B 157; matches on record A 21, B 16; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV11TRUVIS-VIS  (YES = Mac Visser)
Model: 55%
Kalshi: 35%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.005, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Richard Zusman vs George Lazarov -- M15 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208890:210198:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| George Lazarov (`KXITFMATCH-26NOV11ZUSLAZ-LAZ`) | 0.77 / 0.86 (182) | 81.5% | 83.5% | 67.7% | 74.5% [72.7%-76.0%] | -- | -- | -- | -- | PASS | +2.0 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Richard Zusman (`KXITFMATCH-26NOV11ZUSLAZ-ZUS`) | 0.16 / 0.17 (24) | 16.5% | 16.5% | 32.3% | 25.6% [24.0%-27.3%] | -- | -- | -- | -- | PASS | +0.0 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 633.0, B 822.0; serve-point win A 53.8%, B 38.8%; Elo A 1045.7, B 1256.2; model uncertainty 0.0162
* Form inputs: days since last match A 442, B 71; matches on record A 61, B 45; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.004, surface_dev_loose +0.004, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Victoria Allen vs Eliska Tichackova -- W35 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216253:254748:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Victoria Allen (`KXITFWMATCH-26NOV11ALLTIC-ALL`) | 0.16 / 0.17 (54) | 16.5% | 20.8% | 24.3% | 27.2% [25.1%-31.7%] | -- | -- | -- | -- | WATCH | +4.3 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Eliska Tichackova (`KXITFWMATCH-26NOV11ALLTIC-TIC`) | 0.83 / 0.87 (1) | 85.0% | 79.2% | 75.7% | 72.8% [68.3%-74.9%] | -- | -- | -- | -- | PASS | -5.8 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1893.0, B 1647.0; serve-point win A 54.1%, B 39.7%; Elo A 1480.5, B 1623.6; model uncertainty 0.0329
* Form inputs: days since last match A 164, B 260; matches on record A 83, B 46; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.009, surface_dev_loose -0.008, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ane Mintegi Del Olmo vs Laura Svatikova -- W35 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215505:221213:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ane Mintegi Del Olmo (`KXITFWMATCH-26NOV11MINSVA-MIN`) | 0.93 / 0.94 (5) | 93.5% | 93.8% | 89.1% | 87.5% [85.2%-89.3%] | -- | -- | -- | -- | PASS | +0.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Laura Svatikova (`KXITFWMATCH-26NOV11MINSVA-SVA`) | 0.05 / 0.06 (48) | 5.5% | 6.2% | 10.9% | 12.5% [10.7%-14.8%] | -- | -- | -- | -- | PASS | +0.7 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2133.0, B 1657.0; serve-point win A 58.8%, B 52.8%; Elo A 1614.1, B 1303.4; model uncertainty 0.0208
* Form inputs: days since last match A 25, B 358; matches on record A 167, B 244; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.006, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Angella Okutoyi vs Jennifer Ruggeri -- W35 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221411:222454:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Angella Okutoyi (`KXITFWMATCH-26NOV11OKURUG-OKU`) | 0.27 / 0.32 (38) | 29.5% | 64.1% | 64.1% | 63.6% [59.0%-67.5%] | -- | -- | -- | -- | WATCH | +34.6 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jennifer Ruggeri (`KXITFWMATCH-26NOV11OKURUG-RUG`) | 0.67 / 0.71 (2) | 69.0% | 35.9% | 35.9% | 36.4% [32.5%-41.0%] | -- | -- | -- | -- | PASS | -33.1 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1838.0, B 3454.0; serve-point win A 54.7%, B 48.0%; Elo A 1576.1, B 1481.3; model uncertainty 0.0427
* Form inputs: days since last match A 7, B 29; matches on record A 110, B 244; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV11OKURUG-OKU  (YES = Angella Okutoyi)
Model: 64%
Kalshi: 30%
Gap: +35 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.020, surface_dev_loose -0.005, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vicky Van de Peer vs Anastasija Cvetkovic -- W35 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220614:264167:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasija Cvetkovic (`KXITFWMATCH-26NOV11VANCVE-CVE`) | 0.84 / 0.93 (72) | 88.5% | 75.9% | 67.1% | 66.6% [62.6%-68.5%] | -- | -- | -- | -- | PASS | -12.6 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Vicky Van de Peer (`KXITFWMATCH-26NOV11VANCVE-VAN`) | 0.13 / 0.14 (34) | 13.5% | 24.1% | 32.9% | 33.4% [31.5%-37.4%] | -- | -- | -- | -- | PASS | +10.6 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1898.0, B 1234.0; serve-point win A 50.8%, B 43.9%; Elo A 1398.5, B 1511.8; model uncertainty 0.0296
* Form inputs: days since last match A 428, B 232; matches on record A 239, B 43; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.010, surface_dev_loose -0.019, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vito Dell'elba vs Alan Wazny -- M15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 13:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11DELWAZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vito Dell'elba (`KXITFMATCH-26NOV11DELWAZ-DEL`) | 0.05 / 0.14 (45) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alan Wazny (`KXITFMATCH-26NOV11DELWAZ-WAZ`) | 0.86 / 0.95 (14) | 90.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Selina Atay vs Mariia Drobysheva -- W15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220297:261061:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Selina Atay (`KXITFWMATCH-26NOV11ATADRO-ATA`) | 0.17 / 0.33 (14) | 25.0% | 40.6% | 17.4% | 34.3% [31.4%-38.4%] | -- | -- | -- | -- | PASS | +15.6 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mariia Drobysheva (`KXITFWMATCH-26NOV11ATADRO-DRO`) | 0.69 / 0.84 (16) | 76.5% | 59.4% | 82.6% | 65.7% [61.6%-68.6%] | -- | -- | -- | -- | PASS | -17.1 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1670.0, B 310.0; serve-point win A 49.8%, B 48.4%; Elo A 1205.0, B 1283.7; model uncertainty 0.0349
* Form inputs: days since last match A 197, B 407; matches on record A 207, B 7; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV11ATADRO-ATA  (YES = Selina Atay)
Model: 41%
Kalshi: 25%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.005, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stefanie Auer vs Karina Maria Capuzu -- W15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11AUECAP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefanie Auer (`KXITFWMATCH-26NOV11AUECAP-AUE`) | 0.70 / 0.79 (2) | 74.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Karina Maria Capuzu (`KXITFWMATCH-26NOV11AUECAP-CAP`) | 0.24 / 0.31 (8) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Joody Elkady vs Alyssa Reguer -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:234474:241003:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joody Elkady (`KXITFWMATCH-26NOV11ELKREG-ELK`) | 0.07 / 0.22 (55) | 14.5% | 17.0% | 18.9% | 22.3% [18.5%-26.0%] | -- | -- | -- | -- | PASS | +2.5 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alyssa Reguer (`KXITFWMATCH-26NOV11ELKREG-REG`) | 0.84 / 0.95 (12) | 89.5% | 83.0% | 81.1% | 77.7% [74.0%-81.5%] | -- | -- | -- | -- | PASS | -6.5 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 990.0, B 2738.0; serve-point win A 50.0%, B 42.8%; Elo A 1174.0, B 1371.4; model uncertainty 0.0375
* Form inputs: days since last match A 197, B 197; matches on record A 41, B 233; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.012, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yasmin Ezzat vs Dana Charintceva -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221474:260274:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dana Charintceva (`KXITFWMATCH-26NOV11EZZCHA-CHA`) | 0.03 / 0.11 (17) | 7.0% | 29.1% | 27.5% | 36.5% [34.0%-37.5%] | -- | -- | -- | -- | PASS | +22.1 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yasmin Ezzat (`KXITFWMATCH-26NOV11EZZCHA-EZZ`) | 0.91 / 0.94 (5) | 92.5% | 70.9% | 72.5% | 63.5% [62.5%-66.0%] | -- | -- | -- | -- | PASS | -21.6 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2756.0, B 145.0; serve-point win A 57.2%, B 46.9%; Elo A 1399.1, B 1307.9; model uncertainty 0.0172
* Form inputs: days since last match A 204, B 232; matches on record A 271, B 23; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV11EZZCHA-CHA  (YES = Dana Charintceva)
Model: 29%
Kalshi: 7%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniela Darta Feldmane vs Asylzhan Arystanbekova -- W15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:237465:260159:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Asylzhan Arystanbekova (`KXITFWMATCH-26NOV11FELARY-ARY`) | 0.89 / 0.95 (10) | 92.0% | 72.4% | 68.6% | 66.2% [65.1%-68.1%] | -- | -- | -- | -- | PASS | -19.6 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daniela Darta Feldmane (`KXITFWMATCH-26NOV11FELARY-FEL`) | 0.07 / 0.11 (40) | 9.0% | 27.6% | 31.4% | 33.8% [31.9%-34.9%] | -- | -- | -- | -- | PASS | +18.6 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 630.0, B 1328.0; serve-point win A 48.6%, B 47.0%; Elo A 1221.8, B 1337.1; model uncertainty 0.0148
* Form inputs: days since last match A 302, B 197; matches on record A 20, B 67; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV11FELARY-FEL  (YES = Daniela Darta Feldmane)
Model: 28%
Kalshi: 9%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.000, surface_dev_loose -0.010, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aurora Nosei vs Irem Kurt -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:253681:270258:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Irem Kurt (`KXITFWMATCH-26NOV11NOSKUR-KUR`) | 0.74 / 0.84 (101) | 79.0% | 56.1% | 50.0% | 51.6% [51.6%-52.1%] | -- | -- | -- | -- | PASS | -22.9 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aurora Nosei (`KXITFWMATCH-26NOV11NOSKUR-NOS`) | 0.13 / 0.28 (12) | 20.5% | 43.9% | 50.0% | 48.4% [47.9%-48.4%] | -- | -- | -- | -- | PASS | +23.4 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 480.0, B 1948.0; serve-point win A 50.8%, B 48.0%; Elo A 1279.2, B 1293.0; model uncertainty 0.0027
* Form inputs: days since last match A 232, B 197; matches on record A 10, B 82; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV11NOSKUR-NOS  (YES = Aurora Nosei)
Model: 44%
Kalshi: 20%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lorena Solar Donoso vs Melinda Biro -- W15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260860:267406:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Melinda Biro (`KXITFWMATCH-26NOV11SOLBIR-BIR`) | 0.68 / 0.72 (89) | 70.0% | 23.0% | 44.7% | 36.9% [34.4%-37.9%] | -- | -- | -- | -- | PASS | -47.0 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lorena Solar Donoso (`KXITFWMATCH-26NOV11SOLBIR-SOL`) | 0.22 / 0.30 (5) | 26.0% | 77.0% | 55.3% | 63.1% [62.1%-65.6%] | -- | -- | -- | -- | PASS | +51.0 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1848.0, B 292.0; serve-point win A 55.2%, B 50.3%; Elo A 1353.1, B 1248.2; model uncertainty 0.0173
* Form inputs: days since last match A 225, B 351; matches on record A 63, B 6; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV11SOLBIR-SOL  (YES = Lorena Solar Donoso)
Model: 77%
Kalshi: 26%
Gap: +51 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Julia Stamatova vs Theresa Stabauer -- W15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11STASTA2:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julia Stamatova (`KXITFWMATCH-26NOV11STASTA2-STA`) | 0.55 / 0.60 (6) | 57.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Theresa Stabauer (`KXITFWMATCH-26NOV11STASTA2-STA2`) | 0.37 / 0.40 (41) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Doga Turkmen vs Ekaterina Agureeva -- W15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220356:266852:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Agureeva (`KXITFWMATCH-26NOV11TURAGU-AGU`) | 0.47 / 0.56 (2) | 51.5% | 60.3% | 67.6% | 63.1% [62.6%-63.6%] | -- | -- | -- | -- | PASS | +8.8 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Doga Turkmen (`KXITFWMATCH-26NOV11TURAGU-TUR`) | 0.46 / 0.54 (6) | 50.0% | 39.7% | 32.4% | 36.9% [36.4%-37.4%] | -- | -- | -- | -- | PASS | -10.3 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 739.0, B 144.0; serve-point win A 51.3%, B 46.7%; Elo A 1294.0, B 1386.4; model uncertainty 0.0052
* Form inputs: days since last match A 37, B 435; matches on record A 260, B 17; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elena Utkina vs Lamis Alhussein Abdel Aziz -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11UTKALH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lamis Alhussein Abdel Aziz (`KXITFWMATCH-26NOV11UTKALH-ALH`) | 0.90 / 0.95 (10) | 92.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Elena Utkina (`KXITFWMATCH-26NOV11UTKALH-UTK`) | 0.03 / 0.77 (3) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daria Yesypchuk vs Laura Boehner -- W15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221258:260032:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Laura Boehner (`KXITFWMATCH-26NOV11YESBOE-BOE`) | 0.04 / 0.14 (13) | 9.0% | 18.7% | 15.8% | 23.5% [19.3%-28.3%] | -- | -- | -- | -- | PASS | +9.7 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daria Yesypchuk (`KXITFWMATCH-26NOV11YESBOE-YES`) | 0.83 / 0.93 (5) | 88.0% | 81.3% | 84.2% | 76.5% [71.7%-80.7%] | -- | -- | -- | -- | PASS | -6.7 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2518.0, B 824.0; serve-point win A 57.2%, B 49.5%; Elo A 1455.1, B 1298.6; model uncertainty 0.045
* Form inputs: days since last match A 15, B 211; matches on record A 153, B 221; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.004, surface_dev_loose +0.008, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mohamed Ali Abibsi vs Martin Hammond -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11ABIHAM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mohamed Ali Abibsi (`KXITFMATCH-26NOV11ABIHAM-ABI`) | 0.06 / 0.95 (12) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Martin Hammond (`KXITFMATCH-26NOV11ABIHAM-HAM`) | 0.03 / 0.95 (10) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Filippo Alfano vs John Bothma -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11ALFBOT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Filippo Alfano (`KXITFMATCH-26NOV11ALFBOT-ALF`) | 0.21 / 0.32 (1) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| John Bothma (`KXITFMATCH-26NOV11ALFBOT-BOT`) | 0.70 / 0.79 (4) | 74.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pierre Yves Bailly vs Louis Van Herck -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206646:210048:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pierre Yves Bailly (`KXITFMATCH-26NOV11BAIVAN-BAI`) | 0.72 / 0.86 (5) | 79.0% | 95.0% | 98.8% | 94.9% [90.2%-97.6%] | -- | -- | -- | -- | PASS | +16.1 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Louis Van Herck (`KXITFMATCH-26NOV11BAIVAN-VAN`) | 0.14 / 0.23 (3) | 18.5% | 5.0% | 1.2% | 5.1% [2.4%-9.8%] | -- | -- | -- | -- | PASS | -13.6 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1192.0, B 786.0; serve-point win A 62.7%, B 49.8%; Elo A 1529.6, B 1138.7; model uncertainty 0.0372
* Form inputs: days since last match A 281, B 53; matches on record A 55, B 39; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV11BAIVAN-BAI  (YES = Pierre Yves Bailly)
Model: 95%
Kalshi: 79%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.007, surface_dev_tight -0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chen / Te vs Aleshchev / Storch -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11CHETEXALESTO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aleshchev / Storch (`KXITFDOUBLES-26NOV11CHETEXALESTO-ALESTO`) | 0.07 / 0.42 (56) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Chen / Te (`KXITFDOUBLES-26NOV11CHETEXALESTO-CHETEX`) | 0.52 / 0.79 (119) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Julian DeSousa vs Evangelos Kypriotis -- M15 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212304:212595:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julian DeSousa (`KXITFMATCH-26NOV11DESKYP-DES`) | 0.19 / 0.26 (68) | 22.5% | 63.9% | 85.9% | 60.9% [58.3%-64.9%] | -- | -- | -- | -- | PASS | +41.4 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Evangelos Kypriotis (`KXITFMATCH-26NOV11DESKYP-KYP`) | 0.75 / 0.79 (54) | 77.0% | 36.1% | 14.1% | 39.1% [35.1%-41.7%] | -- | -- | -- | -- | PASS | -40.9 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 137.0, B 317.0; serve-point win A 59.2%, B 43.5%; Elo A 1109.7, B 1053.5; model uncertainty 0.0332
* Form inputs: days since last match A 463, B 204; matches on record A 15, B 12; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV11DESKYP-DES  (YES = Julian DeSousa)
Model: 64%
Kalshi: 22%
Gap: +41 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marek Gengel vs Achilles Belkovics -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200309:212937:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Achilles Belkovics (`KXITFMATCH-26NOV11GENBEL-BEL`) | 0.07 / 0.22 (32) | 14.5% | 13.7% | 16.7% | 15.2% [13.8%-17.2%] | -- | -- | -- | -- | PASS | -0.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marek Gengel (`KXITFMATCH-26NOV11GENBEL-GEN`) | 0.78 / 0.95 (10) | 86.5% | 86.4% | 83.3% | 84.8% [82.8%-86.2%] | -- | -- | -- | -- | PASS | -0.1 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3291.0, B 592.0; serve-point win A 66.1%, B 42.5%; Elo A 1578.0, B 1272.7; model uncertainty 0.017
* Form inputs: days since last match A 57, B 260; matches on record A 628, B 12; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.012, surface_dev_loose +0.006, surface_dev_tight -0.002
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jeong / Yang vs Kong / Song -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11JEOYANKONSON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jeong / Yang (`KXITFDOUBLES-26NOV11JEOYANKONSON-JEOYAN`) | 0.82 / 0.90 (1) | 86.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kong / Song (`KXITFDOUBLES-26NOV11JEOYANKONSON-KONSON`) | 0.05 / 0.14 (50) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kacper Knitter vs Imanol Lopez Morillo -- M15 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202209:213198:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kacper Knitter (`KXITFMATCH-26NOV11KNILOP-KNI`) | 0.14 / 0.23 (6) | 18.5% | 24.6% | 25.2% | 28.5% [23.5%-33.1%] | -- | -- | -- | -- | PASS | +6.1 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Imanol Lopez Morillo (`KXITFMATCH-26NOV11KNILOP-LOP`) | 0.74 / 0.86 (12) | 80.0% | 75.4% | 74.8% | 71.5% [66.9%-76.4%] | -- | -- | -- | -- | PASS | -4.6 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 695.0, B 2512.0; serve-point win A 57.8%, B 36.9%; Elo A 1217.1, B 1365.3; model uncertainty 0.0476
* Form inputs: days since last match A 57, B 43; matches on record A 23, B 357; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.050, surface_pool_high +0.045, surface_dev_loose +0.006, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kuan Lai / Yang vs Nima / Pan -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11KUAYANNIMPAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kuan Lai / Yang (`KXITFDOUBLES-26NOV11KUAYANNIMPAN-KUAYAN`) | 0.17 / 0.84 (156) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nima / Pan (`KXITFDOUBLES-26NOV11KUAYANNIMPAN-NIMPAN`) | 0.05 / 0.35 (2) | 20.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Liu / Xiao vs Hsun Lin / Lorusso -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11LIUXIAHSULOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hsun Lin / Lorusso (`KXITFDOUBLES-26NOV11LIUXIAHSULOR-HSULOR`) | 0.25 / 0.70 (4) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Liu / Xiao (`KXITFDOUBLES-26NOV11LIUXIAHSULOR-LIUXIA`) | 0.23 / 0.52 (56) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Thando Longwe-Smit vs Mickael Kaouk -- M15 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207927:213174:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mickael Kaouk (`KXITFMATCH-26NOV11LONKAO-KAO`) | 0.52 / 0.63 (6) | 57.5% | 62.3% | 47.4% | 55.6% [53.1%-57.6%] | -- | -- | -- | -- | PASS | +4.8 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Thando Longwe-Smit (`KXITFMATCH-26NOV11LONKAO-LON`) | 0.38 / 0.41 (47) | 39.5% | 37.8% | 52.6% | 44.4% [42.4%-46.9%] | -- | -- | -- | -- | WATCH | -1.8 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1098.0, B 803.0; serve-point win A 59.6%, B 38.0%; Elo A 1208.1, B 1280.1; model uncertainty 0.0228
* Form inputs: days since last match A 51, B 57; matches on record A 38, B 21; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anas Mazdrashki vs Michel Hopp -- M15 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210424:212748:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michel Hopp (`KXITFMATCH-26NOV11MAZHOP-HOP`) | 0.41 / 0.43 (17) | 42.0% | 53.1% | 54.2% | 57.9% [55.8%-59.4%] | -- | -- | -- | -- | WATCH | +11.1 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anas Mazdrashki (`KXITFMATCH-26NOV11MAZHOP-MAZ`) | 0.51 / 0.61 (144) | 56.0% | 46.9% | 45.8% | 42.1% [40.6%-44.2%] | -- | -- | -- | -- | PASS | -9.1 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1972.0, B 2320.0; serve-point win A 55.3%, B 44.1%; Elo A 1265.2, B 1346.6; model uncertainty 0.018
* Form inputs: days since last match A 239, B 211; matches on record A 47, B 83; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.005, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rocco Piatti vs Adam Lynch -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211497:213060:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adam Lynch (`KXITFMATCH-26NOV11PIALYN-LYN`) | 0.31 / 0.43 (12) | 37.0% | 56.8% | 59.7% | 59.2% [57.2%-62.2%] | -- | -- | -- | -- | PASS | +19.8 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rocco Piatti (`KXITFMATCH-26NOV11PIALYN-PIA`) | 0.58 / 0.69 (80) | 63.5% | 43.2% | 40.3% | 40.8% [37.8%-42.8%] | -- | -- | -- | -- | PASS | -20.3 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1580.0, B 494.0; serve-point win A 59.3%, B 39.4%; Elo A 1221.4, B 1286.5; model uncertainty 0.025
* Form inputs: days since last match A 197, B 211; matches on record A 57, B 11; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV11PIALYN-LYN  (YES = Adam Lynch)
Model: 57%
Kalshi: 37%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.030, surface_pool_high +0.020, surface_dev_loose +0.015, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jan Sadzik vs Jack Karlsson Wistrand -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210575:214087:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jack Karlsson Wistrand (`KXITFMATCH-26NOV11SADKAR-KAR`) | 0.28 / 0.39 (4) | 33.5% | 22.1% | 29.3% | 27.6% [25.9%-28.5%] | -- | -- | -- | -- | PASS | -11.4 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jan Sadzik (`KXITFMATCH-26NOV11SADKAR-SAD`) | 0.61 / 0.78 (73) | 69.5% | 77.9% | 70.7% | 72.4% [71.5%-74.1%] | -- | -- | -- | -- | PASS | +8.4 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 276.0, B 336.0; serve-point win A 62.9%, B 43.1%; Elo A 1250.5, B 1078.7; model uncertainty 0.0128
* Form inputs: days since last match A 442, B 232; matches on record A 3, B 40; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.017, surface_pool_high -0.009, surface_dev_loose +0.009, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nicola Senn vs Cedric Stanke -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210453:213173:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicola Senn (`KXITFMATCH-26NOV11SENSTA-SEN`) | 0.52 / 0.70 (1) | 61.0% | 53.5% | 67.6% | 58.5% [56.1%-60.4%] | -- | -- | -- | -- | PASS | -7.5 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Cedric Stanke (`KXITFMATCH-26NOV11SENSTA-STA`) | 0.35 / 0.43 (7) | 39.0% | 46.5% | 32.4% | 41.5% [39.6%-43.9%] | -- | -- | -- | -- | PASS | +7.5 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 400.0, B 375.0; serve-point win A 62.8%, B 37.9%; Elo A 1196.4, B 1152.8; model uncertainty 0.0215
* Form inputs: days since last match A 204, B 204; matches on record A 9, B 30; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.010, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elena Ruxandra Bertea vs Teodora Miron -- W35 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:246493:270171:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elena Ruxandra Bertea (`KXITFWMATCH-26NOV11BERMIR-BER`) | 0.69 / 0.78 (42) | 73.5% | 93.8% | 65.0% | 80.3% [78.0%-83.8%] | -- | -- | -- | -- | PASS | +20.3 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Teodora Miron (`KXITFWMATCH-26NOV11BERMIR-MIR`) | 0.20 / 0.25 (10) | 22.5% | 6.2% | 35.0% | 19.7% [16.2%-22.0%] | -- | -- | -- | -- | PASS | -16.3 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3327.0, B 136.0; serve-point win A 60.7%, B 50.9%; Elo A 1581.0, B 1320.1; model uncertainty 0.0288
* Form inputs: days since last match A 43, B 477; matches on record A 156, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV11BERMIR-BER  (YES = Elena Ruxandra Bertea)
Model: 94%
Kalshi: 74%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.015, surface_dev_loose -0.001, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cai / Yang vs Ren / Tang -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11CAIYANRENTAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cai / Yang (`KXITFWDOUBLES-26NOV11CAIYANRENTAN-CAIYAN`) | 0.14 / 0.49 (56) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ren / Tang (`KXITFWDOUBLES-26NOV11CAIYANRENTAN-RENTAN`) | 0.45 / 0.73 (92) | 59.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Ariadna Garcia-Patron Canals vs Yui Watanabe -- W15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11GARWAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ariadna Garcia-Patron Canals (`KXITFWMATCH-26NOV11GARWAT-GAR`) | 0.18 / 0.24 (10) | 21.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yui Watanabe (`KXITFWMATCH-26NOV11GARWAT-WAT`) | 0.77 / 0.83 (147) | 80.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Denislava Glushkova vs Lucie Nguyen Tan -- W35 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221364:221468:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Denislava Glushkova (`KXITFWMATCH-26NOV11GLUNGU-GLU`) | 0.23 / 0.24 (34) | 23.5% | 56.1% | 51.1% | 59.6% [56.9%-62.6%] | -- | -- | -- | -- | WATCH | +32.6 pp | EXTREME (DATA_WARNING) | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lucie Nguyen Tan (`KXITFWMATCH-26NOV11GLUNGU-NGU`) | 0.69 / 0.75 (7) | 72.0% | 43.9% | 48.9% | 40.4% [37.4%-43.1%] | -- | -- | -- | -- | PASS | -28.1 pp | EXTREME (DATA_WARNING) | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2333.0, B 1887.0; serve-point win A 51.4%, B 49.8%; Elo A 1581.0, B 1438.0; model uncertainty 0.0286
* Form inputs: days since last match A 65, B 26; matches on record A 240, B 293; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV11GLUNGU-GLU  (YES = Denislava Glushkova)
Model: 56%
Kalshi: 24%
Gap: +33 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: STALE_KALSHI_QUOTE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.021, surface_dev_loose +0.015, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hu / Xu vs Yi Liu / Lu -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11HUXXUXYILLUX:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hu / Xu (`KXITFWDOUBLES-26NOV11HUXXUXYILLUX-HUXXUX`) | 0.09 / 0.71 (86) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yi Liu / Lu (`KXITFWDOUBLES-26NOV11HUXXUXYILLUX-YILLUX`) | 0.12 / 0.53 (53) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Victoria Kapcia vs Sophie Ehrenbergerova -- W15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11KAPEHR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sophie Ehrenbergerova (`KXITFWMATCH-26NOV11KAPEHR-EHR`) | 0.74 / 0.77 (108) | 75.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Victoria Kapcia (`KXITFWMATCH-26NOV11KAPEHR-KAP`) | 0.17 / 0.29 (19) | 23.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ela Nala Milic vs Leila Fabbri -- W15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223032:223308:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leila Fabbri (`KXITFWMATCH-26NOV11MILFAB-FAB`) | 0.05 / 0.12 (11) | 8.5% | 11.3% | 50.0% | 29.6% [26.9%-33.4%] | -- | -- | -- | -- | PASS | +2.8 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Ela Nala Milic (`KXITFWMATCH-26NOV11MILFAB-MIL`) | 0.88 / 0.93 (4) | 90.5% | 88.7% | 50.0% | 70.4% [66.6%-73.1%] | -- | -- | -- | -- | PASS | -1.8 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1113.0, B 0.0; serve-point win A 58.1%, B 50.9%; Elo A 1392.8, B 1247.6; model uncertainty 0.0325
* Form inputs: days since last match A 239, B 736; matches on record A 108, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.027, surface_pool_high -0.038, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Serena Paris vs Rira Kosaka -- W15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260118:263861:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rira Kosaka (`KXITFWMATCH-26NOV11PARKOS-KOS`) | 0.71 / 0.76 (4) | 73.5% | 57.8% | 47.3% | 47.9% [47.9%-47.9%] | -- | -- | -- | -- | PASS | -15.7 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Serena Paris (`KXITFWMATCH-26NOV11PARKOS-PAR`) | 0.21 / 0.40 (11) | 30.5% | 42.2% | 52.7% | 52.1% [52.1%-52.1%] | -- | -- | -- | -- | PASS | +11.7 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 126.0; serve-point win A 52.7%, B 45.9%; Elo A 1224.7, B 1209.2; model uncertainty 0.0
* Form inputs: days since last match A 708, B 204; matches on record A 5, B 9; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Giorgia Pedone vs Marianna Argyrokastriti -- W35 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11PEDARG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marianna Argyrokastriti (`KXITFWMATCH-26NOV11PEDARG-ARG`) | 0.23 / 0.27 (26) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Giorgia Pedone (`KXITFWMATCH-26NOV11PEDARG-PED`) | 0.66 / 0.77 (13) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Giulia Safina Popa vs Maria Golovina -- W35 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:261015:267428:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Golovina (`KXITFWMATCH-26NOV11POPGOL-GOL`) | 0.43 / 0.49 (49) | 46.0% | 57.6% | 78.5% | 64.1% [53.2%-69.5%] | -- | -- | -- | -- | PASS | +11.6 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Giulia Safina Popa (`KXITFWMATCH-26NOV11POPGOL-POP`) | 0.49 / 0.56 (43) | 52.5% | 42.4% | 21.5% | 35.9% [30.5%-46.8%] | -- | -- | -- | -- | PASS | -10.1 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1013.0, B 2344.0; serve-point win A 52.1%, B 46.5%; Elo A 1526.2, B 1551.0; model uncertainty 0.0814
* Form inputs: days since last match A 407, B 197; matches on record A 38, B 97; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.015, surface_dev_loose -0.030, surface_dev_tight +0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Martyna Zaremba vs Lavinia Luciano -- W15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:241750:266758:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lavinia Luciano (`KXITFWMATCH-26NOV11ZARLUC-LUC`) | 0.90 / 0.95 (11) | 92.5% | 94.8% | 72.2% | 83.9% [83.9%-84.6%] | -- | -- | -- | -- | PASS | +2.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Martyna Zaremba (`KXITFWMATCH-26NOV11ZARLUC-ZAR`) | 0.03 / 0.11 (46) | 7.0% | 5.2% | 27.8% | 16.1% [15.4%-16.1%] | -- | -- | -- | -- | PASS | -1.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 53.0, B 1465.0; serve-point win A 47.0%, B 40.8%; Elo A 1062.7, B 1353.9; model uncertainty 0.0035
* Form inputs: days since last match A 197, B 204; matches on record A 67, B 83; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hania Abouelsaad vs Anastasia Efremova -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220394:267540:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hania Abouelsaad (`KXITFWMATCH-26NOV11ABOEFR-ABO`) | 0.55 / 0.67 (3) | 61.0% | 40.1% | 43.6% | 44.1% [43.1%-45.7%] | -- | -- | -- | -- | PASS | -20.9 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anastasia Efremova (`KXITFWMATCH-26NOV11ABOEFR-EFR`) | 0.35 / 0.49 (12) | 42.0% | 59.9% | 56.4% | 55.9% [54.3%-56.9%] | -- | -- | -- | -- | PASS | +17.9 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 897.0, B 611.0; serve-point win A 50.8%, B 47.4%; Elo A 1303.1, B 1345.5; model uncertainty 0.0133
* Form inputs: days since last match A 267, B 211; matches on record A 56, B 14; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV11ABOEFR-EFR  (YES = Anastasia Efremova)
Model: 60%
Kalshi: 42%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Coco Bosman vs Gala Ivanovic -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223421:270115:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Coco Bosman (`KXITFWMATCH-26NOV11BOSIVA-BOS`) | 0.28 / 0.57 (6) | 42.5% | 48.4% | 58.4% | 51.6% [49.5%-53.2%] | -- | -- | -- | -- | PASS | +6.0 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gala Ivanovic (`KXITFWMATCH-26NOV11BOSIVA-IVA`) | 0.50 / 0.72 (12) | 61.0% | 51.5% | 41.6% | 48.4% [46.8%-50.5%] | -- | -- | -- | -- | PASS | -9.4 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2097.0, B 844.0; serve-point win A 56.6%, B 43.1%; Elo A 1352.6, B 1366.1; model uncertainty 0.0185
* Form inputs: days since last match A 197, B 225; matches on record A 69, B 15; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.016, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aurora Corvi vs Sofia Camila Rojas -- W15 Nules R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264998:266630:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aurora Corvi (`KXITFWMATCH-26NOV11CORROJ-COR`) | 0.24 / 0.30 (35) | 27.0% | 6.3% | 6.2% | 13.0% [8.5%-16.9%] | -- | -- | -- | -- | PASS | -20.7 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sofia Camila Rojas (`KXITFWMATCH-26NOV11CORROJ-ROJ`) | 0.64 / 0.74 (2) | 69.0% | 93.7% | 93.8% | 87.0% [83.1%-91.5%] | -- | -- | -- | -- | PASS | +24.7 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 531.0, B 553.0; serve-point win A 49.5%, B 38.9%; Elo A 1227.9, B 1510.6; model uncertainty 0.0421
* Form inputs: days since last match A 218, B 365; matches on record A 24, B 44; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV11CORROJ-ROJ  (YES = Sofia Camila Rojas)
Model: 94%
Kalshi: 69%
Gap: +25 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.006, surface_dev_loose -0.006, surface_dev_tight +0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Claudia Ferrer Perez vs Ginevra Parentini Vallega Montebruno -- W15 Nules R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:237481:260062:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Claudia Ferrer Perez (`KXITFWMATCH-26NOV11FERPAR-FER`) | 0.34 / 0.39 (26) | 36.5% | 67.2% | 67.0% | 63.6% [60.5%-66.1%] | -- | -- | -- | -- | PASS | +30.8 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ginevra Parentini Vallega Montebruno (`KXITFWMATCH-26NOV11FERPAR-PAR`) | 0.54 / 0.65 (60) | 59.5% | 32.8% | 33.0% | 36.4% [33.9%-39.5%] | -- | -- | -- | -- | PASS | -26.8 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1739.0, B 813.0; serve-point win A 55.6%, B 47.7%; Elo A 1355.9, B 1271.0; model uncertainty 0.0276
* Form inputs: days since last match A 197, B 274; matches on record A 82, B 143; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV11FERPAR-FER  (YES = Claudia Ferrer Perez)
Model: 67%
Kalshi: 36%
Gap: +31 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.030, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofia Montesinos Vilanova vs Adriana Monlleo Ramos -- W15 Nules R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:266464:269696:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Montesinos Vilanova (`KXITFWMATCH-26NOV11MONMON2-MON`) | 0.19 / 0.26 (4) | 22.5% | 47.9% | 63.6% | 51.1% [50.0%-51.6%] | -- | -- | -- | -- | PASS | +25.4 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Adriana Monlleo Ramos (`KXITFWMATCH-26NOV11MONMON2-MON2`) | 0.69 / 0.78 (57) | 73.5% | 52.1% | 36.4% | 48.9% [48.4%-50.0%] | -- | -- | -- | -- | PASS | -21.4 pp | HIGH_REVIEW (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 92.0, B 264.0; serve-point win A 54.0%, B 45.6%; Elo A 1203.5, B 1203.3; model uncertainty 0.008
* Form inputs: days since last match A 344, B 351; matches on record A 6, B 7; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV11MONMON2-MON  (YES = Sofia Montesinos Vilanova)
Model: 48%
Kalshi: 22%
Gap: +25 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aleksandra Pozarenko vs Marina Quesada Oyonarte -- W15 Nules R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11POZQUE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aleksandra Pozarenko (`KXITFWMATCH-26NOV11POZQUE-POZ`) | 0.57 / 0.68 (57) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marina Quesada Oyonarte (`KXITFWMATCH-26NOV11POZQUE-QUE`) | 0.31 / 0.36 (3) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sandra Samir vs Anastasia Zhilina -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211529:259622:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sandra Samir (`KXITFWMATCH-26NOV11SAMZHI-SAM`) | 0.71 / 0.88 (9) | 79.5% | 91.4% | 79.3% | 85.8% [83.9%-87.0%] | -- | -- | -- | -- | PASS | +11.9 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Anastasia Zhilina (`KXITFWMATCH-26NOV11SAMZHI-ZHI`) | 0.07 / 0.30 (18) | 18.5% | 8.6% | 20.7% | 14.2% [13.0%-16.1%] | -- | -- | -- | -- | PASS | -9.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 4604.0, B 0.0; serve-point win A 57.7%, B 52.5%; Elo A 1556.7, B 1249.1; model uncertainty 0.0152
* Form inputs: days since last match A 8, B 1429; matches on record A 807, B 42; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.012, surface_pool_high -0.019, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Wissam Abderrahman vs Kris van Wyk -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144748:210230:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wissam Abderrahman (`KXITFMATCH-26NOV11ABDVAN-ABD`) | 0.57 / 0.77 (15) | 67.0% | 47.1% | 64.9% | 41.7% [37.6%-44.8%] | -- | -- | -- | -- | PASS | -19.9 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kris van Wyk (`KXITFMATCH-26NOV11ABDVAN-VAN`) | 0.27 / 0.46 (46) | 36.5% | 52.9% | 35.1% | 58.3% [55.2%-62.4%] | -- | -- | -- | -- | PASS | +16.4 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 236.0, B 2875.0; serve-point win A 57.2%, B 42.3%; Elo A 1233.2, B 1319.6; model uncertainty 0.0358
* Form inputs: days since last match A 470, B 204; matches on record A 75, B 324; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV11ABDVAN-VAN  (YES = Kris van Wyk)
Model: 53%
Kalshi: 36%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.031, surface_pool_high -0.041, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aytekin / Christopher Kucukhuseyin vs Alvarez Velis / Bakhshaliev -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11AYTCHRALVBAK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alvarez Velis / Bakhshaliev (`KXITFDOUBLES-26NOV11AYTCHRALVBAK-ALVBAK`) | 0.04 / 0.89 (56) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aytekin / Christopher Kucukhuseyin (`KXITFDOUBLES-26NOV11AYTCHRALVBAK-AYTCHR`) | 0.05 / 0.94 (56) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Bozo Barun vs Andrei Radu -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11BARRAD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bozo Barun (`KXITFMATCH-26NOV11BARRAD-BAR`) | 0.42 / 0.86 (16) | 64.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Andrei Radu (`KXITFMATCH-26NOV11BARRAD-RAD`) | 0.14 / 0.56 (2) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Baum / Cerny vs Avanoglu / Aydin -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11BAUCERAVAAYD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Avanoglu / Aydin (`KXITFDOUBLES-26NOV11BAUCERAVAAYD-AVAAYD`) | 0.04 / 0.94 (56) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Baum / Cerny (`KXITFDOUBLES-26NOV11BAUCERAVAAYD-BAUCER`) | 0.05 / 0.95 (10) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Andrey Chepelev vs Andrea Paolini -- M15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200184:212900:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrey Chepelev (`KXITFMATCH-26NOV11CHEPAO-CHE`) | 0.79 / 0.94 (7) | 86.5% | 85.3% | 81.6% | 80.5% [78.4%-83.4%] | -- | -- | -- | -- | PASS | -1.2 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Andrea Paolini (`KXITFMATCH-26NOV11CHEPAO-PAO`) | 0.06 / 0.25 (2) | 15.5% | 14.7% | 18.4% | 19.5% [16.6%-21.6%] | -- | -- | -- | -- | PASS | -0.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3714.0, B 516.0; serve-point win A 59.9%, B 48.1%; Elo A 1452.1, B 1208.3; model uncertainty 0.025
* Form inputs: days since last match A 50, B 267; matches on record A 605, B 31; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.011, surface_dev_loose +0.004, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sebastiano Cocola vs Raffaele Ciurnelli -- M25 San Gregorio di Catania R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213717:214125:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raffaele Ciurnelli (`KXITFMATCH-26NOV11COCCIU-CIU`) | 0.57 / 0.65 (71) | 61.0% | 47.9% | 63.0% | 57.4% [57.2%-58.4%] | -- | -- | -- | -- | PASS | -13.1 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sebastiano Cocola (`KXITFMATCH-26NOV11COCCIU-COC`) | 0.31 / 0.51 (12) | 41.0% | 52.0% | 37.0% | 42.6% [41.6%-42.8%] | -- | -- | -- | -- | PASS | +11.1 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 734.0, B 44.0; serve-point win A 56.6%, B 43.8%; Elo A 1216.3, B 1267.2; model uncertainty 0.006
* Form inputs: days since last match A 197, B 435; matches on record A 18, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tommaso Compagnucci vs Mak Mikovic -- M25 San Gregorio di Catania R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206867:212951:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tommaso Compagnucci (`KXITFMATCH-26NOV11COMMIK-COM`) | 0.82 / 0.91 (117) | 86.5% | 90.2% | 93.6% | 89.2% [87.1%-91.7%] | -- | -- | -- | -- | PASS | +3.7 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mak Mikovic (`KXITFMATCH-26NOV11COMMIK-MIK`) | 0.07 / 0.13 (3) | 10.0% | 9.8% | 6.4% | 10.8% [8.3%-13.0%] | -- | -- | -- | -- | PASS | -0.2 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3698.0, B 397.0; serve-point win A 60.1%, B 49.7%; Elo A 1518.7, B 1176.2; model uncertainty 0.0231
* Form inputs: days since last match A 196, B 211; matches on record A 176, B 12; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Remy Dugardin vs Stefano D'Agostino -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:214112:tml:D0D9:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefano D'Agostino (`KXITFMATCH-26NOV11DUGDAG-DAG`) | 0.53 / 0.79 (48) | 66.0% | 54.6% | 47.5% | 62.2% [61.0%-63.9%] | -- | -- | -- | -- | PASS | -11.4 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Remy Dugardin (`KXITFMATCH-26NOV11DUGDAG-DUG`) | 0.22 / 0.54 (9) | 38.0% | 45.4% | 52.5% | 37.8% [36.1%-39.0%] | -- | -- | -- | -- | PASS | +7.4 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 604.0, B 81.0; serve-point win A 64.2%, B 34.9%; Elo A 1294.1, B 1388.9; model uncertainty 0.0145
* Form inputs: days since last match A 211, B 50; matches on record A 12, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.000, surface_dev_loose +0.001, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andrea Fiorentini vs Alex Marti Pujolras -- M25 San Gregorio di Catania R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207704:209253:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrea Fiorentini (`KXITFMATCH-26NOV11FIOMAR-FIO`) | 0.06 / 0.14 (50) | 10.0% | 24.2% | 30.3% | 27.1% [24.6%-28.5%] | -- | -- | -- | -- | PASS | +14.2 pp | REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alex Marti Pujolras (`KXITFMATCH-26NOV11FIOMAR-MAR`) | 0.82 / 0.93 (330) | 87.5% | 75.8% | 69.7% | 72.9% [71.5%-75.3%] | -- | -- | -- | -- | PASS | -11.7 pp | REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2736.0, B 2643.0; serve-point win A 53.5%, B 41.2%; Elo A 1305.5, B 1529.9; model uncertainty 0.0192
* Form inputs: days since last match A 197, B 22; matches on record A 112, B 415; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Constantin Frantzen / Bart Stevens vs Robert Galloway / Andre Goransson -- ATP Stockholm QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-10 17:21Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-11T05:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11FRASTEGALGOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Constantin Frantzen / Bart Stevens (`KXATPDOUBLES-26NOV11FRASTEGALGOR-FRASTE`) | 0.05 / 0.95 (108) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Robert Galloway / Andre Goransson (`KXATPDOUBLES-26NOV11FRASTEGALGOR-GALGOR`) | 0.05 / 0.95 (108) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Taylor Fritz vs Cameron Norrie -- ATP Stockholm R16

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-11 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-10 17:21Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-11T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-11-11T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111815:126203:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Taylor Fritz (`KXATPMATCH-26NOV11FRINOR-FRI`) | 0.74 / 0.75 (505) | 74.5% | 73.8% | 81.5% | 79.6% [78.3%-80.5%] | 73.4% | 75.5% | 75.5% | MODEL_LONE_OUTLIER | SHADOW_BET | -0.8 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Cameron Norrie (`KXATPMATCH-26NOV11FRINOR-NOR`) | 0.25 / 0.26 (1171) | 25.5% | 26.2% | 18.4% | 20.4% [19.5%-21.7%] | 26.7% | 25.9% | 25.9% | MODEL_LONE_OUTLIER | PASS | +0.8 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 7020.0, B 5521.0; serve-point win A 70.3%, B 35.0%; Elo A 2061.7, B 1891.8; model uncertainty 0.0113
* Form inputs: days since last match A 4, B 1; matches on record A 772, B 682; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.003, surface_dev_loose +0.003, surface_dev_tight -0.003
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV11FRINOR-18` Over 17.5 games: 0.42/0.92 mid 67.0%, model 94.8% (projection_v2.0 (prediction ledger)) -- gap +27.8 pp, EXTREME, DATA_WARNING, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV11FRINOR-2-FRI` Will Taylor Fritz win set 2 in the Taylor Fritz vs Cameron Norrie match: 0.04/0.94 mid 49.0%, model 66.4% (projection_v2.0 (prediction ledger)) -- gap +17.4 pp, HIGH_REVIEW, DATA_WARNING, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV11FRINOR-FRI21` Will Taylor Fritz win the Taylor Fritz vs Cameron Norrie match by a set score of 2-1?: 0.03/0.24 mid 13.5%, model 29.6% (projection_v2.0 (prediction ledger)) -- gap +16.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV11FRINOR-2-NOR` Will Cameron Norrie win set 2 in the Taylor Fritz vs Cameron Norrie match: 0.04/0.94 mid 49.0%, model 33.6% (projection_v2.0 (prediction ledger)) -- gap -15.4 pp, HIGH_REVIEW, DATA_WARNING, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV11FRINOR-NOR20` Will Cameron Norrie win the Taylor Fritz vs Cameron Norrie match by a set score of 2-0?: 0.13/0.36 mid 24.5%, model 11.3% (projection_v2.0 (prediction ledger)) -- gap -13.2 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV11FRINOR-FRI7` Will Taylor Fritz win at least 6.5 more games than Cameron Norrie?: 0.09/0.23 mid 16.0%, model 5.9% (projection_v2.0 (prediction ledger)) -- gap -10.1 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV11FRINOR-23` Over 22.5 games: 0.49/0.52 mid 50.5%, model 60.4% (projection_v2.0 (prediction ledger)) -- gap +9.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV11FRINOR-NOR21` Will Cameron Norrie win the Taylor Fritz vs Cameron Norrie match by a set score of 2-1?: 0.11/0.36 mid 23.5%, model 15.0% (projection_v2.0 (prediction ledger)) -- gap -8.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV11FRINOR-28` Over 27.5 games: 0.28/0.37 mid 32.5%, model 39.6% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV11FRINOR-FRI4` Will Taylor Fritz win at least 3.5 more games than Cameron Norrie?: 0.48/0.50 mid 49.0%, model 42.0% (projection_v2.0 (prediction ledger)) -- gap -7.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV11FRINOR-FRI20` Will Taylor Fritz win the Taylor Fritz vs Cameron Norrie match by a set score of 2-0?: 0.49/0.51 mid 50.0%, model 44.1% (projection_v2.0 (prediction ledger)) -- gap -5.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV11FRINOR-NOR2` Will Cameron Norrie win at least 1.5 more games than Taylor Fritz?: 0.17/0.28 mid 22.5%, model 19.8% (projection_v2.0 (prediction ledger)) -- gap -2.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV11FRINOR-1-NOR` Will Cameron Norrie win set 1 in the Taylor Fritz vs Cameron Norrie match: 0.31/0.33 mid 32.0%, model 33.6% (projection_v2.0 (prediction ledger)) -- gap +1.6 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV11FRINOR-1-FRI` Will Taylor Fritz win set 1 in the Taylor Fritz vs Cameron Norrie match: 0.66/0.69 mid 67.5%, model 66.4% (projection_v2.0 (prediction ledger)) -- gap -1.1 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Axel Garcian vs Julien Penzlin -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209247:210114:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Axel Garcian (`KXITFMATCH-26NOV11GARPEN-GAR`) | 0.07 / 0.60 (62) | 33.5% | 80.5% | 74.2% | 77.5% [76.6%-78.8%] | -- | -- | -- | -- | PASS | +47.0 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Julien Penzlin (`KXITFMATCH-26NOV11GARPEN-PEN`) | 0.06 / 0.66 (73) | 36.0% | 19.4% | 25.8% | 22.5% [21.2%-23.4%] | -- | -- | -- | -- | PASS | -16.6 pp | HIGH_REVIEW (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 2369.0, B 317.0; serve-point win A 59.1%, B 47.4%; Elo A 1397.1, B 1176.4; model uncertainty 0.0107
* Form inputs: days since last match A 414, B 351; matches on record A 174, B 10; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV11GARPEN-GAR  (YES = Axel Garcian)
Model: 81%
Kalshi: 34%
Gap: +47 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.004, surface_dev_loose +0.008, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Borna Gojo vs Ugo Humbert -- ATP Stockholm R16

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-11 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-10 17:21Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-11T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-11-11T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:127339:200005:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Borna Gojo (`KXATPMATCH-26NOV11GOJHUM-GOJ`) | 0.32 / 0.33 (75) | 32.5% | 31.0% | 41.2% | 37.6% [34.0%-39.4%] | 33.6% | 33.3% | 33.3% | MODEL_LONE_OUTLIER | WATCH | -1.5 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Ugo Humbert (`KXATPMATCH-26NOV11GOJHUM-HUM`) | 0.66 / 0.67 (73) | 66.5% | 69.0% | 58.8% | 62.4% [60.6%-66.0%] | 66.4% | 66.9% | 66.9% | MODEL_LONE_OUTLIER | PASS | +2.5 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3697.0, B 4987.0; serve-point win A 67.3%, B 28.4%; Elo A 1771.8, B 1937.2; model uncertainty 0.0271
* Form inputs: days since last match A 1, B 1; matches on record A 479, B 628; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight -0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV11GOJHUM-19` Over 18.5 games: 0.25/0.91 mid 58.0%, model 93.6% (projection_v2.0 (prediction ledger)) -- gap +35.6 pp, EXTREME, DATA_WARNING, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV11GOJHUM-HUM6` Will Ugo Humbert win at least 5.5 more games than Borna Gojo?: 0.11/0.40 mid 25.5%, model 8.2% (projection_v2.0 (prediction ledger)) -- gap -17.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV11GOJHUM-2-HUM` Will Ugo Humbert win set 2 in the Borna Gojo vs Ugo Humbert match: 0.03/0.94 mid 48.5%, model 63.0% (projection_v2.0 (prediction ledger)) -- gap +14.5 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV11GOJHUM-2-GOJ` Will Borna Gojo win set 2 in the Borna Gojo vs Ugo Humbert match: 0.03/0.94 mid 48.5%, model 37.0% (projection_v2.0 (prediction ledger)) -- gap -11.5 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV11GOJHUM-24` Over 23.5 games: 0.45/0.48 mid 46.5%, model 56.2% (projection_v2.0 (prediction ledger)) -- gap +9.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV11GOJHUM-HUM21` Will Ugo Humbert win the Borna Gojo vs Ugo Humbert match by a set score of 2-1?: 0.20/0.29 mid 24.5%, model 29.4% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV11GOJHUM-29` Over 28.5 games: 0.29/0.42 mid 35.5%, model 40.4% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV11GOJHUM-GOJ2` Will Borna Gojo win at least 1.5 more games than Ugo Humbert?: 0.22/0.34 mid 28.0%, model 23.4% (projection_v2.0 (prediction ledger)) -- gap -4.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV11GOJHUM-HUM3` Will Ugo Humbert win at least 2.5 more games than Borna Gojo?: 0.51/0.54 mid 52.5%, model 49.1% (projection_v2.0 (prediction ledger)) -- gap -3.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV11GOJHUM-GOJ20` Will Borna Gojo win the Borna Gojo vs Ugo Humbert match by a set score of 2-0?: 0.11/0.22 mid 16.5%, model 13.7% (projection_v2.0 (prediction ledger)) -- gap -2.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV11GOJHUM-HUM20` Will Ugo Humbert win the Borna Gojo vs Ugo Humbert match by a set score of 2-0?: 0.26/0.50 mid 38.0%, model 39.7% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV11GOJHUM-1-HUM` Will Ugo Humbert win set 1 in the Borna Gojo vs Ugo Humbert match: 0.62/0.65 mid 63.5%, model 63.0% (projection_v2.0 (prediction ledger)) -- gap -0.5 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV11GOJHUM-GOJ21` Will Borna Gojo win the Borna Gojo vs Ugo Humbert match by a set score of 2-1?: 0.14/0.21 mid 17.5%, model 17.3% (projection_v2.0 (prediction ledger)) -- gap -0.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV11GOJHUM-1-GOJ` Will Borna Gojo win set 1 in the Borna Gojo vs Ugo Humbert match: 0.35/0.39 mid 37.0%, model 37.0% (projection_v2.0 (prediction ledger)) -- gap +0.0 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Gundacker / Wagner vs Krstic / Radjenovic -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11GUNWAGKRSRAD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gundacker / Wagner (`KXITFDOUBLES-26NOV11GUNWAGKRSRAD-GUNWAG`) | 0.04 / 0.95 (10) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Krstic / Radjenovic (`KXITFDOUBLES-26NOV11GUNWAGKRSRAD-KRSRAD`) | 0.04 / 0.95 (10) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Karim Ibrahim vs Nikita Ianin -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210394:210456:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikita Ianin (`KXITFMATCH-26NOV11IBRIAN-IAN`) | 0.07 / 0.45 (45) | 26.0% | 43.7% | 51.9% | 49.0% [47.5%-49.5%] | -- | -- | -- | -- | PASS | +17.7 pp | HIGH_REVIEW (DATA_WARNING) | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Karim Ibrahim (`KXITFMATCH-26NOV11IBRIAN-IBR`) | 0.06 / 0.78 (113) | 42.0% | 56.3% | 48.1% | 51.0% [50.5%-52.5%] | -- | -- | -- | -- | PASS | +14.3 pp | REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 2455.0, B 2048.0; serve-point win A 67.4%, B 33.9%; Elo A 1227.6, B 1192.3; model uncertainty 0.01
* Form inputs: days since last match A 197, B 197; matches on record A 90, B 74; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV11IBRIAN-IAN  (YES = Nikita Ianin)
Model: 44%
Kalshi: 26%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, EVENT_MAPPING_RISK, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hendrik Jebens / Ryan Seggerman vs Erik Grevelius / Adam Heinonen -- ATP Stockholm QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-10 17:21Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-11T05:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11JEBSEGGREHEI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Erik Grevelius / Adam Heinonen (`KXATPDOUBLES-26NOV11JEBSEGGREHEI-GREHEI`) | 0.37 / 0.42 (451) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hendrik Jebens / Ryan Seggerman (`KXATPDOUBLES-26NOV11JEBSEGGREHEI-JEBSEG`) | 0.57 / 0.62 (278) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Artur Kukasian vs Amir Omarkhanov -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210477:212788:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Artur Kukasian (`KXITFMATCH-26NOV11KUKOMA-KUK`) | 0.12 / 0.44 (56) | 28.0% | 32.2% | 35.7% | 34.2% [33.3%-34.7%] | -- | -- | -- | -- | PASS | +4.2 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Amir Omarkhanov (`KXITFMATCH-26NOV11KUKOMA-OMA`) | 0.09 / 0.78 (56) | 43.5% | 67.8% | 64.3% | 65.8% [65.3%-66.7%] | -- | -- | -- | -- | PASS | +24.3 pp | HIGH_REVIEW (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 2159.0, B 2497.0; serve-point win A 56.4%, B 40.1%; Elo A 1300.0, B 1433.9; model uncertainty 0.0074
* Form inputs: days since last match A 239, B 24; matches on record A 99, B 76; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV11KUKOMA-OMA  (YES = Amir Omarkhanov)
Model: 68%
Kalshi: 44%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nazim Makhlouf vs Ammar Elamin -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11MAKELA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ammar Elamin (`KXITFMATCH-26NOV11MAKELA-ELA`) | 0.14 / 0.45 (68) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nazim Makhlouf (`KXITFMATCH-26NOV11MAKELA-MAK`) | 0.66 / 0.89 (25) | 77.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ramazan Kaan Oktay vs Ole Bredschneijder -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213958:214089:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ole Bredschneijder (`KXITFMATCH-26NOV11OKTBRE-BRE`) | 0.53 / 0.58 (1) | 55.5% | 33.3% | 48.9% | 42.7% [41.8%-43.2%] | -- | -- | -- | -- | PASS | -22.2 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ramazan Kaan Oktay (`KXITFMATCH-26NOV11OKTBRE-OKT`) | 0.41 / 0.49 (5) | 45.0% | 66.7% | 51.0% | 57.3% [56.8%-58.2%] | -- | -- | -- | -- | PASS | +21.7 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 266.0, B 147.0; serve-point win A 59.6%, B 43.7%; Elo A 1249.0, B 1193.6; model uncertainty 0.0073
* Form inputs: days since last match A 260, B 197; matches on record A 6, B 3; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV11OKTBRE-OKT  (YES = Ramazan Kaan Oktay)
Model: 67%
Kalshi: 45%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oleksandr Ovcharenko vs Pietro Marino -- M25 San Gregorio di Catania R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209191:209233:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pietro Marino (`KXITFMATCH-26NOV11OVCMAR-MAR`) | 0.16 / 0.37 (6) | 26.5% | 17.6% | 9.6% | 13.0% [10.2%-17.3%] | -- | -- | -- | -- | PASS | -8.8 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oleksandr Ovcharenko (`KXITFMATCH-26NOV11OVCMAR-OVC`) | 0.57 / 0.79 (119) | 68.0% | 82.3% | 90.5% | 87.0% [82.7%-89.8%] | -- | -- | -- | -- | PASS | +14.3 pp | REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2402.0, B 1636.0; serve-point win A 63.1%, B 44.1%; Elo A 1533.3, B 1264.5; model uncertainty 0.0354
* Form inputs: days since last match A 71, B 99; matches on record A 323, B 149; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.011, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Adam Pavlasek / Patrik Rikl vs Sander Arends / Luke Johnson -- ATP Stockholm QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-10 17:21Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-11T05:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11PAVRIKAREJOH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sander Arends / Luke Johnson (`KXATPDOUBLES-26NOV11PAVRIKAREJOH-AREJOH`) | 0.36 / 0.39 (44) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Adam Pavlasek / Patrik Rikl (`KXATPDOUBLES-26NOV11PAVRIKAREJOH-PAVRIK`) | 0.59 / 0.63 (313) | 61.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Aleksandr Shevchenko vs Casper Ruud -- ATP Stockholm R16

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-11 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-10 17:21Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-11T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-11-11T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:134770:207686:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Casper Ruud (`KXATPMATCH-26NOV11SHERUU-RUU`) | 0.77 / 0.78 (20297) | 77.5% | 81.0% | 80.6% | 80.6% [78.5%-82.5%] | -- | 76.7% | -- | INSUFFICIENT_INPUTS | PASS | +3.5 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Aleksandr Shevchenko (`KXATPMATCH-26NOV11SHERUU-SHE`) | 0.23 / 0.24 (18852) | 23.5% | 19.0% | 19.4% | 19.4% [17.5%-21.5%] | -- | 23.0% | -- | INSUFFICIENT_INPUTS | PASS | -4.5 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 5333.0, B 5349.0; serve-point win A 64.1%, B 28.6%; Elo A 1720.3, B 1959.3; model uncertainty 0.02
* Form inputs: days since last match A 8, B 3; matches on record A 510, B 724; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.020, surface_dev_loose +0.005, surface_dev_tight -0.002
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPSETWINNER-26NOV11SHERUU-2-RUU` Will Casper Ruud win set 2 in the Alexander Shevchenko vs Casper Ruud match: 0.05/0.94 mid 49.5%, model 72.1% (projection_v2.0 (prediction ledger)) -- gap +22.6 pp, HIGH_REVIEW, DATA_WARNING, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV11SHERUU-2-SHE` Will Alexander Shevchenko win set 2 in the Alexander Shevchenko vs Casper Ruud match: 0.04/0.94 mid 49.0%, model 27.9% (projection_v2.0 (prediction ledger)) -- gap -21.1 pp, HIGH_REVIEW, DATA_WARNING, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV11SHERUU-RUU21` Will Casper Ruud win the Alexander Shevchenko vs Casper Ruud match by a set score of 2-1?: 0.01/0.82 mid 41.5%, model 29.0% (projection_v2.0 (prediction ledger)) -- gap -12.5 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV11SHERUU-RUU5` Will Casper Ruud win at least 4.5 more games than Alexander Shevchenko?: 0.43/0.44 mid 43.5%, model 31.7% (projection_v2.0 (prediction ledger)) -- gap -11.8 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV11SHERUU-RUU20` Will Casper Ruud win the Alexander Shevchenko vs Casper Ruud match by a set score of 2-0?: 0.01/0.82 mid 41.5%, model 52.0% (projection_v2.0 (prediction ledger)) -- gap +10.5 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV11SHERUU-22` Over 21.5 games: 0.54/0.57 mid 55.5%, model 65.5% (projection_v2.0 (prediction ledger)) -- gap +10.0 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV11SHERUU-27` Over 26.5 games: 0.22/0.37 mid 29.5%, model 37.7% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV11SHERUU-17` Over 16.5 games: 0.86/0.94 mid 90.0%, model 97.5% (projection_v2.0 (prediction ledger)) -- gap +7.5 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV11SHERUU-SHE20` Will Alexander Shevchenko win the Alexander Shevchenko vs Casper Ruud match by a set score of 2-0?: 0.01/0.27 mid 14.0%, model 7.8% (projection_v2.0 (prediction ledger)) -- gap -6.2 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV11SHERUU-SHE21` Will Alexander Shevchenko win the Alexander Shevchenko vs Casper Ruud match by a set score of 2-1?: 0.01/0.27 mid 14.0%, model 11.2% (projection_v2.0 (prediction ledger)) -- gap -2.8 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV11SHERUU-1-SHE` Will Alexander Shevchenko win set 1 in the Alexander Shevchenko vs Casper Ruud match: 0.27/0.32 mid 29.5%, model 27.9% (projection_v2.0 (prediction ledger)) -- gap -1.6 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV11SHERUU-1-RUU` Will Casper Ruud win set 1 in the Alexander Shevchenko vs Casper Ruud match: 0.70/0.73 mid 71.5%, model 72.1% (projection_v2.0 (prediction ledger)) -- gap +0.6 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV11SHERUU-RUU2` Will Casper Ruud win at least 1.5 more games than Alexander Shevchenko?: 0.69/0.81 mid 75.0%, model 74.6% (projection_v2.0 (prediction ledger)) -- gap -0.4 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lorenzo Sonego vs Alejandro Tabilo -- ATP Stockholm R16

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-11 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-10 17:21Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-11T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-11-11T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126214:132283:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Sonego (`KXATPMATCH-26NOV11SONTAB-SON`) | 0.45 / 0.58 (1) | 51.5% | 40.8% | 41.4% | 41.9% [40.9%-41.9%] | -- | 57.1% | -- | INSUFFICIENT_INPUTS | PASS | -10.7 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alejandro Tabilo (`KXATPMATCH-26NOV11SONTAB-TAB`) | 0.40 / 0.53 (35) | 46.5% | 59.2% | 58.6% | 58.1% [58.1%-59.1%] | -- | 43.0% | -- | INSUFFICIENT_INPUTS | PASS | +12.7 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4585.0, B 5932.0; serve-point win A 66.5%, B 31.6%; Elo A 1779.2, B 1831.2; model uncertainty 0.005
* Form inputs: days since last match A 2, B 8; matches on record A 706, B 656; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26NOV11SONTAB-1-TAB` Will Alejandro Tabilo win set 1 in the Lorenzo Sonego vs Alejandro Tabilo match: 0.01/0.95 mid 48.0%, model 56.2% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV11SONTAB-2-TAB` Will Alejandro Tabilo win set 2 in the Lorenzo Sonego vs Alejandro Tabilo match: 0.01/0.95 mid 48.0%, model 56.2% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV11SONTAB-1-SON` Will Lorenzo Sonego win set 1 in the Lorenzo Sonego vs Alejandro Tabilo match: 0.01/0.95 mid 48.0%, model 43.8% (projection_v2.0 (prediction ledger)) -- gap -4.2 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV11SONTAB-2-SON` Will Lorenzo Sonego win set 2 in the Lorenzo Sonego vs Alejandro Tabilo match: 0.01/0.95 mid 48.0%, model 43.8% (projection_v2.0 (prediction ledger)) -- gap -4.2 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Wishaya Trongcharoenchaikul vs Jan Wygona -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106397:214037:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wishaya Trongcharoenchaikul (`KXITFMATCH-26NOV11TROWYG-TRO`) | 0.53 / 0.63 (104) | 58.0% | 68.6% | 63.7% | 59.4% [57.5%-61.9%] | -- | -- | -- | -- | PASS | +10.6 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jan Wygona (`KXITFMATCH-26NOV11TROWYG-WYG`) | 0.36 / 0.50 (2) | 43.0% | 31.4% | 36.2% | 40.6% [38.1%-42.5%] | -- | -- | -- | -- | PASS | -11.6 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2725.0, B 415.0; serve-point win A 65.2%, B 38.6%; Elo A 1265.7, B 1205.8; model uncertainty 0.0221
* Form inputs: days since last match A 197, B 232; matches on record A 524, B 9; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.020, surface_dev_loose +0.005, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zeinab Ayadi vs Mia Horvit -- W15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213551:267857:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zeinab Ayadi (`KXITFWMATCH-26NOV11AYAHOR-AYA`) | 0.04 / 0.16 (22) | 10.0% | 6.9% | 38.5% | 25.3% [22.4%-27.2%] | -- | -- | -- | -- | PASS | -3.1 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mia Horvit (`KXITFWMATCH-26NOV11AYAHOR-HOR`) | 0.85 / 0.95 (10) | 90.0% | 93.1% | 61.5% | 74.7% [72.8%-77.6%] | -- | -- | -- | -- | PASS | +3.1 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 140.0, B 1568.0; serve-point win A 50.1%, B 38.7%; Elo A 1214.0, B 1412.5; model uncertainty 0.024
* Form inputs: days since last match A 316, B 267; matches on record A 4, B 110; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.017, surface_dev_loose +0.001, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Abigeyle Bhopal vs Marta Soriano Santiago -- W15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259105:266474:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Abigeyle Bhopal (`KXITFWMATCH-26NOV11BHOSOR-BHO`) | 0.04 / 0.08 (27) | 6.0% | 8.7% | 12.5% | 21.1% [18.1%-22.7%] | -- | -- | -- | -- | PASS | +2.7 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marta Soriano Santiago (`KXITFWMATCH-26NOV11BHOSOR-SOR`) | 0.86 / 0.94 (5) | 90.0% | 91.3% | 87.5% | 78.9% [77.3%-81.9%] | -- | -- | -- | -- | PASS | +1.3 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 107.0, B 1358.0; serve-point win A 48.2%, B 41.6%; Elo A 1168.9, B 1390.4; model uncertainty 0.0228
* Form inputs: days since last match A 246, B 197; matches on record A 5, B 98; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.008, surface_dev_loose -0.004, surface_dev_tight +0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sophia Biolay vs Anna Burchak -- W15 Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221192:270253:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sophia Biolay (`KXITFWMATCH-26NOV11BIOBUR-BIO`) | 0.74 / 0.85 (89) | 79.5% | 91.3% | 96.0% | 81.8% [78.8%-85.3%] | -- | -- | -- | -- | PASS | +11.8 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anna Burchak (`KXITFWMATCH-26NOV11BIOBUR-BUR`) | 0.13 / 0.19 (8) | 16.0% | 8.7% | 4.0% | 18.2% [14.7%-21.1%] | -- | -- | -- | -- | PASS | -7.3 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 766.0, B 191.0; serve-point win A 59.6%, B 50.6%; Elo A 1456.2, B 1224.9; model uncertainty 0.0321
* Form inputs: days since last match A 267, B 386; matches on record A 133, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.018, surface_dev_loose +0.007, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stefania Bojica vs Valeriia Iushchenko -- W15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11BOJIUS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefania Bojica (`KXITFWMATCH-26NOV11BOJIUS-BOJ`) | 0.09 / 0.23 (6) | 16.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Valeriia Iushchenko (`KXITFWMATCH-26NOV11BOJIUS-IUS`) | 0.75 / 0.87 (11) | 81.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alesia Breaz vs Anais Gabriel -- W15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221155:270165:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alesia Breaz (`KXITFWMATCH-26NOV11BREGAB-BRE`) | 0.76 / 0.87 (20) | 81.5% | 83.1% | 76.1% | 76.1% [74.9%-78.8%] | -- | -- | -- | -- | PASS | +1.6 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anais Gabriel (`KXITFWMATCH-26NOV11BREGAB-GAB`) | 0.14 / 0.25 (6) | 19.5% | 16.9% | 23.9% | 23.9% [21.2%-25.1%] | -- | -- | -- | -- | PASS | -2.6 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 933.0, B 534.0; serve-point win A 50.4%, B 56.8%; Elo A 1423.6, B 1217.3; model uncertainty 0.0195
* Form inputs: days since last match A 105, B 246; matches on record A 21, B 13; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.008, surface_dev_loose +0.008, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yekaterina Krupina vs Jana Bojovic -- W15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11KRUBOJ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jana Bojovic (`KXITFWMATCH-26NOV11KRUBOJ-BOJ`) | 0.84 / 0.95 (10) | 89.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yekaterina Krupina (`KXITFWMATCH-26NOV11KRUBOJ-KRU`) | 0.03 / 0.14 (24) | 8.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marinescu / Asya Yilmaz vs Andrei / Maria Brotea -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11MARASYANDMAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrei / Maria Brotea (`KXITFWDOUBLES-26NOV11MARASYANDMAR-ANDMAR`) | 0.05 / 0.90 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marinescu / Asya Yilmaz (`KXITFWDOUBLES-26NOV11MARASYANDMAR-MARASY`) | 0.05 / 0.90 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Matilde Mariani vs Carla Giambelli -- W15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220343:270266:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carla Giambelli (`KXITFWMATCH-26NOV11MARGIA-GIA`) | 0.46 / 0.84 (20) | 65.0% | 42.9% | 61.1% | 44.6% [40.5%-50.0%] | -- | -- | -- | -- | PASS | -22.1 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matilde Mariani (`KXITFWMATCH-26NOV11MARGIA-MAR`) | 0.35 / 0.54 (7) | 44.5% | 57.1% | 38.9% | 55.4% [50.0%-59.5%] | -- | -- | -- | -- | PASS | +12.6 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 616.0, B 120.0; serve-point win A 52.0%, B 49.3%; Elo A 1368.6, B 1325.0; model uncertainty 0.0477
* Form inputs: days since last match A 211, B 115; matches on record A 146, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.026, surface_pool_high -0.043, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Francesca Parcelli vs Isis Louise Van den Broek -- W15 Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11PARVAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesca Parcelli (`KXITFWMATCH-26NOV11PARVAN-PAR`) | 0.15 / 0.20 (51) | 17.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Isis Louise Van den Broek (`KXITFWMATCH-26NOV11PARVAN-VAN`) | 0.75 / 0.85 (62) | 80.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kira Pavlova vs Lian Tran -- W15 Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220560:223302:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kira Pavlova (`KXITFWMATCH-26NOV11PAVTRA-PAV`) | 0.60 / 0.72 (8) | 66.0% | 66.6% | 87.0% | 71.8% [57.5%-79.8%] | -- | -- | -- | -- | PASS | +0.6 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lian Tran (`KXITFWMATCH-26NOV11PAVTRA-TRA`) | 0.26 / 0.38 (40) | 32.0% | 33.4% | 13.0% | 28.2% [20.2%-42.5%] | -- | -- | -- | -- | PASS | +1.4 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2405.0, B 1204.0; serve-point win A 52.1%, B 51.1%; Elo A 1542.5, B 1506.8; model uncertainty 0.1115
* Form inputs: days since last match A 218, B 197; matches on record A 230, B 307; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high -0.000, surface_dev_loose +0.013, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
