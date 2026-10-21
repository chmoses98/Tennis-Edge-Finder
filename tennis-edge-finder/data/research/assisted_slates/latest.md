# ASSISTED SLATE -- 2026-10-21T12:38Z (`SL-20261021T123805Z-1b0616b7`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

361 open matches not seen started, 1007 markets. Skipped: {"scheduled_start_over_24h_past": 15, "first_ball_already_observed": 3, "no_play_confirmed": 1}. Sources: shadow board 2026-10-21T12:24:51.768297+00:00, Model 4 2026-10-21T12:26:06.873223+00:00, Gen-1 ledger 2026-10-21T12:24:47.918285+00:00, external 2026-10-21T12:02:34.674791+00:00, capture 20261021T120014Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-10-21 13:30Z**
* Recommended RUN TENNIS time: **2026-10-21 12:45Z**
* Final price/status check time: **2026-10-21 13:20Z**
* Number of matches in window: 2 (Corentin Moutet vs Felix Balshaw, Pierre-Hugues Herbert vs Taylor Fritz)

* **3 main-tour match(es) have NO verified start status** (STATUS_AMBIGUOUS): BET blocked until a live status check.

Slate built 2026-10-21T12:38Z. Refresh due by: 2026-10-21 12:45Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 56, "HIGH_REVIEW": 116, "NORMAL": 412, "REVIEW": 103, "UNPRICED": 320}; match winners: {"EXTREME": 55, "HIGH_REVIEW": 92, "NORMAL": 211, "REVIEW": 46, "UNPRICED": 318}; quote freshness at build: {"AGING": 687}.

## Yanaki Milev vs Lorenzo Giustino -- ATP Challenger Florence R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-20 15:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-20T15:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105841:210200:2026-10-20`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Giustino (`KXATPCHALLENGERMATCH-26OCT20MILGIU-GIU`) | 0.31 / 0.32 (725) | 31.5% | 53.3% | 66.0% | 60.7% [57.7%-64.1%] | -- | -- | -- | -- | WATCH | +21.8 pp | HIGH_REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yanaki Milev (`KXATPCHALLENGERMATCH-26OCT20MILGIU-MIL`) | 0.68 / 0.69 (12) | 68.5% | 46.7% | 34.0% | 39.3% [35.9%-42.3%] | -- | -- | -- | -- | PASS | -21.8 pp | HIGH_REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1066.0, B 4385.0; serve-point win A 59.9%, B 39.5%; Elo A 1468.7, B 1518.8; model uncertainty 0.0322
* Form inputs: days since last match A 15, B 8; matches on record A 164, B 1038; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT20MILGIU-GIU  (YES = Lorenzo Giustino)
Model: 53%
Kalshi: 32%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: ASYMMETRIC_SAMPLE_SIZE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.034, surface_pool_high +0.030, surface_dev_loose -0.019, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE

## Facundo Mena vs Valerio Aboian -- ATP Challenger Cali R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-20 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-20T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106057:209254:2026-10-20`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valerio Aboian (`KXATPCHALLENGERMATCH-26OCT20MENABO-ABO`) | 0.30 / 0.31 (2820) | 30.5% | 38.2% | 30.3% | 31.6% [30.3%-33.0%] | -- | -- | -- | -- | PASS | +7.7 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Facundo Mena (`KXATPCHALLENGERMATCH-26OCT20MENABO-MEN`) | 0.69 / 0.70 (188) | 69.5% | 61.8% | 69.7% | 68.4% [67.0%-69.7%] | -- | -- | -- | -- | PASS | -7.7 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3789.0, B 2578.0; serve-point win A 61.2%, B 41.1%; Elo A 1630.5, B 1516.1; model uncertainty 0.0138
* Form inputs: days since last match A 8, B 8; matches on record A 907, B 298; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.014, surface_dev_loose +0.005, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE

## Matthew Dellavedova vs Hayden Jones -- M25 Tamworth R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 07:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202354:210436:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthew Dellavedova (`KXITFMATCH-26OCT20DELJON-DEL`) | 0.51 / 0.53 (482) | 52.0% | 73.9% | 47.5% | 72.5% [68.5%-77.8%] | -- | -- | -- | -- | PASS | +21.9 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hayden Jones (`KXITFMATCH-26OCT20DELJON-JON`) | 0.49 / 0.50 (144) | 49.5% | 26.1% | 52.5% | 27.5% [22.2%-31.4%] | -- | -- | -- | -- | PASS | -23.4 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1203.0, B 397.0; serve-point win A 64.4%, B 40.6%; Elo A 1490.7, B 1269.1; model uncertainty 0.0463
* Form inputs: days since last match A 29, B 632; matches on record A 356, B 37; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT20DELJON-DEL  (YES = Matthew Dellavedova)
Model: 74%
Kalshi: 52%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oliver Clark Anderson vs Naoki Nakagawa -- M25 Tamworth R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111788:212849:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oliver Clark Anderson (`KXITFMATCH-26OCT20ANDNAK-AND`) | 0.04 / 0.05 (8) | 4.5% | 38.9% | 49.5% | 36.2% [36.1%-36.2%] | -- | -- | -- | -- | PASS | +34.4 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Naoki Nakagawa (`KXITFMATCH-26OCT20ANDNAK-NAK`) | 0.96 / 0.97 (1579) | 96.5% | 61.1% | 50.5% | 63.8% [63.8%-63.9%] | -- | -- | -- | -- | PASS | -35.4 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 2619.0; serve-point win A 61.9%, B 35.9%; Elo A 1458.5, B 1557.2; model uncertainty 0.0006
* Form inputs: days since last match A 681, B 695; matches on record A 23, B 420; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT20ANDNAK-AND  (YES = Oliver Clark Anderson)
Model: 39%
Kalshi: 4%
Gap: +34 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Blake Ellis vs Benjamin O'Connell -- M25 Tamworth R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT20ELLOCO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Blake Ellis (`KXITFMATCH-26OCT20ELLOCO-ELL`) | 0.66 / 0.73 (1) | 69.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Benjamin O'Connell (`KXITFMATCH-26OCT20ELLOCO-OCO`) | 0.22 / 0.29 (1) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Derek Pham vs Tai Leonard Sach -- M25 Tamworth R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210613:212740:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Derek Pham (`KXITFMATCH-26OCT20PHASAC-PHA`) | 0.65 / 0.66 (210) | 65.5% | 60.4% | 46.4% | 56.1% [56.1%-56.2%] | -- | -- | -- | -- | PASS | -5.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tai Leonard Sach (`KXITFMATCH-26OCT20PHASAC-SAC`) | 0.33 / 0.34 (575) | 33.5% | 39.6% | 53.6% | 43.9% [43.8%-43.9%] | -- | -- | -- | -- | PASS | +6.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 217.0, B 0.0; serve-point win A 61.4%, B 40.7%; Elo A 1298.4, B 1254.8; model uncertainty 0.0006
* Form inputs: days since last match A 674, B 674; matches on record A 68, B 23; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zane Stevens vs Eric Tripathi -- M25 Tamworth R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT20STETRI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zane Stevens (`KXITFMATCH-26OCT20STETRI-STE`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eric Tripathi (`KXITFMATCH-26OCT20STETRI-TRI`) | -- / 0.01 (5102) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nicolas Ifi / Cedric Stanke vs Dominik Recek / Daniel Siniakov -- ATP Challenger Florence R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-21T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21IFISTARECSIN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Ifi / Cedric Stanke (`KXATPCHALLENGERDOUBLES-26OCT21IFISTARECSIN-IFISTA`) | 0.05 / 0.95 (100) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dominik Recek / Daniel Siniakov (`KXATPCHALLENGERDOUBLES-26OCT21IFISTARECSIN-RECSIN`) | 0.05 / 0.88 (1) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Michele Ribecai vs Max Houkes -- ATP Challenger Florence R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-21T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208069:212020:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Max Houkes (`KXATPCHALLENGERMATCH-26OCT21RIBHOU-HOU`) | 0.58 / 0.59 (1) | 58.5% | 54.3% | 57.8% | 57.2% [55.7%-59.2%] | -- | 59.7% | 59.7% | MARKETS_AGREE | PASS | -4.2 pp | NORMAL | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Michele Ribecai (`KXATPCHALLENGERMATCH-26OCT21RIBHOU-RIB`) | 0.40 / 0.42 (1980) | 41.0% | 45.7% | 42.2% | 42.8% [40.8%-44.3%] | -- | 39.9% | 39.9% | MARKETS_AGREE | PASS | +4.7 pp | NORMAL | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2101.0, B 1822.0; serve-point win A 58.4%, B 40.8%; Elo A 1442.7, B 1492.7; model uncertainty 0.0173
* Form inputs: days since last match A 9, B 121; matches on record A 96, B 275; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.010, surface_dev_loose +0.015, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; THIN_DISPLAYED_SIZE

## Oriol Roca Batalla vs Dimitris Sakellaridis -- ATP Challenger Florence R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-21T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106177:212029:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oriol Roca Batalla (`KXATPCHALLENGERMATCH-26OCT21ROCSAK-ROC`) | 0.78 / 0.80 (112) | 79.0% | 85.0% | 65.8% | 84.4% [79.2%-88.8%] | -- | 77.9% | -- | INSUFFICIENT_INPUTS | PASS | +6.0 pp | NORMAL | AGING | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dimitris Sakellaridis (`KXATPCHALLENGERMATCH-26OCT21ROCSAK-SAK`) | 0.18 / 0.22 (0) | 20.0% | 15.0% | 34.2% | 15.6% [11.2%-20.8%] | -- | 16.4% | -- | INSUFFICIENT_INPUTS | PASS | -5.0 pp | NORMAL | AGING | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2870.0, B 114.0; serve-point win A 66.4%, B 41.8%; Elo A 1504.8, B 1196.0; model uncertainty 0.0482
* Form inputs: days since last match A 9, B 16; matches on record A 981, B 39; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.041, surface_pool_high -0.049, surface_dev_loose -0.000, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; THIN_DISPLAYED_SIZE

## Stefanos Tsitsipas vs Mikhail Kukushkin -- ATP Almaty R16

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-21 17:30Z
* Current expected start: 2026-10-21 12:00Z
* Source: COURT_PROGRESSION: preceding match on Center Court in progress (set 3 of best-of-5); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-21 11:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-330_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-21T17:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105062:126774:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mikhail Kukushkin (`KXATPMATCH-26OCT21TSIKUK-KUK`) | 0.07 / 0.08 (19631) | 7.5% | 13.2% | 29.2% | 25.2% [16.8%-28.4%] | 10.1% | 7.4% | 7.4% | MODEL_LONE_OUTLIER | WATCH | +5.7 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Stefanos Tsitsipas (`KXATPMATCH-26OCT21TSIKUK-TSI`) | 0.92 / 0.93 (67704) | 92.5% | 86.8% | 70.8% | 74.8% [71.6%-83.2%] | 89.9% | 92.6% | 92.6% | MODEL_LONE_OUTLIER | PASS | -5.7 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5234.0, B 4018.0; serve-point win A 71.1%, B 38.1%; Elo A 1952.5, B 1681.8; model uncertainty 0.0581
* Form inputs: days since last match A 1, B 2; matches on record A 802, B 1128; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.023, surface_pool_high -0.032, surface_dev_loose -0.008, surface_dev_tight +0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT21TSIKUK-20` Over 19.5 games: 0.50/0.51 mid 50.5%, model 71.8% (projection_v2.0 (prediction ledger)) -- gap +21.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT21TSIKUK-TSI6` Will Stefanos Tsitsipas win at least 5.5 more games than Mikhail Kukushkin?: 0.43/0.44 mid 43.5%, model 25.3% (projection_v2.0 (prediction ledger)) -- gap -18.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21TSIKUK-TSI20` Will Stefanos Tsitsipas win the Stefanos Tsitsipas vs Mikhail Kukushkin match by a set score of 2-0?: 0.76/0.77 mid 76.5%, model 59.7% (projection_v2.0 (prediction ledger)) -- gap -16.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT21TSIKUK-25` Over 24.5 games: 0.23/0.24 mid 23.5%, model 39.5% (projection_v2.0 (prediction ledger)) -- gap +16.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT21TSIKUK-TSI3` Will Stefanos Tsitsipas win at least 2.5 more games than Mikhail Kukushkin?: 0.81/0.91 mid 86.0%, model 74.3% (projection_v2.0 (prediction ledger)) -- gap -11.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21TSIKUK-TSI21` Will Stefanos Tsitsipas win the Stefanos Tsitsipas vs Mikhail Kukushkin match by a set score of 2-1?: 0.14/0.17 mid 15.5%, model 27.2% (projection_v2.0 (prediction ledger)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT21TSIKUK-15` Over 14.5 games: 0.79/0.99 mid 89.0%, model 99.5% (projection_v2.0 (prediction ledger)) -- gap +10.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT21TSIKUK-2-KUK` Will Mikhail Kukushkin win set 2 in the Stefanos Tsitsipas vs Mikhail Kukushkin match: 0.11/0.14 mid 12.5%, model 22.8% (projection_v2.0 (prediction ledger)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT21TSIKUK-1-KUK` Will Mikhail Kukushkin win set 1 in the Stefanos Tsitsipas vs Mikhail Kukushkin match: 0.13/0.14 mid 13.5%, model 22.8% (projection_v2.0 (prediction ledger)) -- gap +9.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT21TSIKUK-2-TSI` Will Stefanos Tsitsipas win set 2 in the Stefanos Tsitsipas vs Mikhail Kukushkin match: 0.85/0.88 mid 86.5%, model 77.2% (projection_v2.0 (prediction ledger)) -- gap -9.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT21TSIKUK-1-TSI` Will Stefanos Tsitsipas win set 1 in the Stefanos Tsitsipas vs Mikhail Kukushkin match: 0.85/0.87 mid 86.0%, model 77.2% (projection_v2.0 (prediction ledger)) -- gap -8.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT21TSIKUK-TSI9` Will Stefanos Tsitsipas win at least 8.5 more games than Mikhail Kukushkin?: 0.09/0.11 mid 10.0%, model 2.0% (projection_v2.0 (prediction ledger)) -- gap -8.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21TSIKUK-KUK21` Will Mikhail Kukushkin win the Stefanos Tsitsipas vs Mikhail Kukushkin match by a set score of 2-1?: 0.02/0.04 mid 3.0%, model 8.0% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21TSIKUK-KUK20` Will Mikhail Kukushkin win the Stefanos Tsitsipas vs Mikhail Kukushkin match by a set score of 2-0?: 0.02/0.04 mid 3.0%, model 5.2% (projection_v2.0 (prediction ledger)) -- gap +2.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STATUS_AMBIGUOUS; EXTERNAL_PRICE_STALE; WIDE_SPREAD

## Matthew Howse / James Mackinlay vs Jacopo Bilardo / Giorgio Ricca -- ATP Challenger Florence R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 12:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-21T12:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21HOWMACBILRIC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jacopo Bilardo / Giorgio Ricca (`KXATPCHALLENGERDOUBLES-26OCT21HOWMACBILRIC-BILRIC`) | 0.06 / 0.88 (100) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matthew Howse / James Mackinlay (`KXATPCHALLENGERDOUBLES-26OCT21HOWMACBILRIC-HOWMAC`) | 0.05 / 0.95 (100) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Filip Misolic vs Izan Almazan Valiente -- ATP Challenger Florence R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 12:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-21T12:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209209:212978:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Izan Almazan Valiente (`KXATPCHALLENGERMATCH-26OCT21MISALM-ALM`) | 0.28 / 0.30 (57) | 29.0% | 15.8% | 30.6% | 21.4% [15.1%-26.7%] | -- | 29.5% | 29.5% | MODEL_LONE_OUTLIER | PASS | -13.2 pp | REVIEW | AGING | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Filip Misolic (`KXATPCHALLENGERMATCH-26OCT21MISALM-MIS`) | 0.70 / 0.72 (431) | 71.0% | 84.2% | 69.4% | 78.6% [73.3%-84.9%] | -- | 70.7% | 70.7% | MODEL_LONE_OUTLIER | WATCH | +13.2 pp | REVIEW | AGING | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2562.0, B 787.0; serve-point win A 63.2%, B 44.6%; Elo A 1600.3, B 1330.3; model uncertainty 0.0579
* Form inputs: days since last match A 44, B 9; matches on record A 293, B 20; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.042, surface_pool_high -0.052, surface_dev_loose -0.011, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY

## Ekaterina Alexandrova vs Marta Kostyuk -- WTA Ningbo R16

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-21 14:00Z
* Current expected start: 2026-10-21 12:25Z
* Source: COURT_PROGRESSION: preceding match on Center Court in progress (set 1 of best-of-3); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-21 11:40Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-95_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-21T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:206420:216146:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Alexandrova (`KXWTAMATCH-26OCT21ALEKOS-ALE`) | 0.40 / 0.41 (11904) | 40.5% | 27.5% | 31.8% | 31.3% [30.4%-34.6%] | 41.7% | 41.5% | 41.6% | MARKETS_AGREE | PASS | -13.0 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Marta Kostyuk (`KXWTAMATCH-26OCT21ALEKOS-KOS`) | 0.59 / 0.60 (34494) | 59.5% | 72.5% | 68.2% | 68.7% [65.4%-69.6%] | 58.3% | 59.0% | 58.7% | MARKETS_AGREE | SHADOW_BET | +13.0 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4877.0, B 4067.0; serve-point win A 55.3%, B 40.1%; Elo A 1938.2, B 2072.0; model uncertainty 0.0209
* Form inputs: days since last match A 1, B 8; matches on record A 746, B 431; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.000, surface_dev_loose -0.009, surface_dev_tight +0.019
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTASETWINNER-26OCT21ALEKOS-1-ALE` Will Ekaterina Alexandrova win set 1 in the Ekaterina Alexandrova vs Marta Kostyuk match: 0.43/0.45 mid 44.0%, model 34.5% (projection_v2.0 (prediction ledger)) -- gap -9.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT21ALEKOS-1-KOS` Will Marta Kostyuk win set 1 in the Ekaterina Alexandrova vs Marta Kostyuk match: 0.55/0.57 mid 56.0%, model 65.5% (projection_v2.0 (prediction ledger)) -- gap +9.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT21ALEKOS-2-ALE` Will Ekaterina Alexandrova win set 2 in the Ekaterina Alexandrova vs Marta Kostyuk match: 0.41/0.45 mid 43.0%, model 34.5% (projection_v2.0 (prediction ledger)) -- gap -8.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT21ALEKOS-2-KOS` Will Marta Kostyuk win set 2 in the Ekaterina Alexandrova vs Marta Kostyuk match: 0.55/0.59 mid 57.0%, model 65.5% (projection_v2.0 (prediction ledger)) -- gap +8.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT21ALEKOS-27` Over 26.5 games: 0.27/0.31 mid 29.0%, model 35.8% (projection_v2.0 (prediction ledger)) -- gap +6.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT21ALEKOS-22` Over 21.5 games: 0.52/0.53 mid 52.5%, model 58.2% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT21ALEKOS-17` Over 16.5 games: 0.85/0.93 mid 89.0%, model 92.0% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STATUS_AMBIGUOUS; WIDE_SPREAD

## Clement Chidekh vs Jacob Fearnley -- ATP Brussels R16

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-21 13:30Z
* Current expected start: 2026-10-21 12:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-21 11:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-60_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-21T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:206889:207985:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Clement Chidekh (`KXATPMATCH-26OCT21CHIFEA-CHI`) | 0.49 / 0.50 (22400) | 49.5% | 40.5% | 51.5% | 47.4% [40.8%-50.5%] | 48.9% | 49.5% | 49.2% | MODEL_LONE_OUTLIER | PASS | -9.0 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Jacob Fearnley (`KXATPMATCH-26OCT21CHIFEA-FEA`) | 0.49 / 0.51 (14223) | 50.0% | 59.5% | 48.4% | 52.6% [49.5%-59.2%] | 51.1% | 50.5% | 50.8% | MODEL_LONE_OUTLIER | PASS | +9.5 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3837.0, B 4197.0; serve-point win A 59.3%, B 38.9%; Elo A 1696.7, B 1790.8; model uncertainty 0.0485
* Form inputs: days since last match A 1, B 1; matches on record A 283, B 184; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.026, surface_pool_high +0.026, surface_dev_loose +0.005, surface_dev_tight -0.015
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT21CHIFEA-CHI2` Will Clement Chidekh win at least 1.5 more games than Jacob Fearnley?: 0.43/0.44 mid 43.5%, model 33.8% (projection_v2.0 (prediction ledger)) -- gap -9.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21CHIFEA-CHI20` Will Clement Chidekh win the Clement Chidekh vs Jacob Fearnley match by a set score of 2-0?: 0.27/0.28 mid 27.5%, model 19.0% (projection_v2.0 (prediction ledger)) -- gap -8.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21CHIFEA-FEA21` Will Jacob Fearnley win the Clement Chidekh vs Jacob Fearnley match by a set score of 2-1?: 0.18/0.22 mid 20.0%, model 27.7% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT21CHIFEA-28` Over 27.5 games: 0.29/0.30 mid 29.5%, model 36.8% (projection_v2.0 (prediction ledger)) -- gap +7.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT21CHIFEA-FEA2` Will Jacob Fearnley win at least 1.5 more games than Clement Chidekh?: 0.45/0.46 mid 45.5%, model 52.6% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT21CHIFEA-23` Over 22.5 games: 0.50/0.51 mid 50.5%, model 57.5% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT21CHIFEA-1-CHI` Will Clement Chidekh win set 1 in the Clement Chidekh vs Jacob Fearnley match: 0.49/0.52 mid 50.5%, model 43.6% (projection_v2.0 (prediction ledger)) -- gap -6.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT21CHIFEA-1-FEA` Will Jacob Fearnley win set 1 in the Clement Chidekh vs Jacob Fearnley match: 0.49/0.51 mid 50.0%, model 56.4% (projection_v2.0 (prediction ledger)) -- gap +6.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT21CHIFEA-2-CHI` Will Clement Chidekh win set 2 in the Clement Chidekh vs Jacob Fearnley match: 0.46/0.52 mid 49.0%, model 43.6% (projection_v2.0 (prediction ledger)) -- gap -5.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT21CHIFEA-2-FEA` Will Jacob Fearnley win set 2 in the Clement Chidekh vs Jacob Fearnley match: 0.49/0.54 mid 51.5%, model 56.4% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT21CHIFEA-FEA5` Will Jacob Fearnley win at least 4.5 more games than Clement Chidekh?: 0.21/0.23 mid 22.0%, model 25.8% (projection_v2.0 (prediction ledger)) -- gap +3.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21CHIFEA-FEA20` Will Jacob Fearnley win the Clement Chidekh vs Jacob Fearnley match by a set score of 2-0?: 0.29/0.31 mid 30.0%, model 31.8% (projection_v2.0 (prediction ledger)) -- gap +1.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21CHIFEA-CHI21` Will Clement Chidekh win the Clement Chidekh vs Jacob Fearnley match by a set score of 2-1?: 0.18/0.22 mid 20.0%, model 21.5% (projection_v2.0 (prediction ledger)) -- gap +1.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT21CHIFEA-18` Over 17.5 games: 0.87/0.91 mid 89.0%, model 90.3% (projection_v2.0 (prediction ledger)) -- gap +1.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STATUS_AMBIGUOUS; THIN_DISPLAYED_SIZE

## Francisco Cerundolo / Alex Michelsen vs Orlando Luz / Rafael Matos -- ATP Brussels QF

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-10-21 14:50Z
* Current expected start: 2026-10-21 13:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-21 12:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-21T14:50:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21CERMICLUZMAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francisco Cerundolo / Alex Michelsen (`KXATPDOUBLES-26OCT21CERMICLUZMAT-CERMIC`) | 0.29 / 0.32 (36) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Orlando Luz / Rafael Matos (`KXATPDOUBLES-26OCT21CERMICLUZMAT-LUZMAT`) | 0.67 / 0.70 (365) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Henry Best vs Alan Wazny -- M15 Bol R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21BESWAZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Henry Best (`KXITFMATCH-26OCT21BESWAZ-BES`) | 0.16 / 0.22 (27) | 19.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alan Wazny (`KXITFMATCH-26OCT21BESWAZ-WAZ`) | 0.77 / 0.81 (42) | 79.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andrea Paolini vs Matthias Ujvary -- M15 Bol R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210745:212900:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrea Paolini (`KXITFMATCH-26OCT21PAOUJV-PAO`) | 0.40 / 0.45 (1) | 42.5% | 65.3% | 74.1% | 65.8% [64.9%-65.8%] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +22.8 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matthias Ujvary (`KXITFMATCH-26OCT21PAOUJV-UJV`) | 0.53 / 0.58 (1) | 55.5% | 34.7% | 25.9% | 34.2% [34.2%-35.1%] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -20.8 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 163.0; serve-point win A 63.7%, B 39.4%; Elo A 1307.3, B 1197.2; model uncertainty 0.0047
* Form inputs: days since last match A 674, B 177; matches on record A 20, B 71; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21PAOUJV-PAO  (YES = Andrea Paolini)
Model: 65%
Kalshi: 42%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.009, surface_dev_loose -0.001, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Facundo Yunis vs Michiel De Krom -- M15 Bol R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202148:209947:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michiel De Krom (`KXITFMATCH-26OCT21YUNDEK-DEK`) | 0.55 / 0.64 (21) | 59.5% | 87.1% | 33.8% | 80.5% [76.7%-83.9%] | 62.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +27.6 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Facundo Yunis (`KXITFMATCH-26OCT21YUNDEK-YUN`) | 0.28 / 0.39 (13) | 33.5% | 12.9% | 66.2% | 19.5% [16.1%-23.3%] | 37.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -20.6 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 403.0; serve-point win A 58.1%, B 33.0%; Elo A 1176.2, B 1421.4; model uncertainty 0.0358
* Form inputs: days since last match A 856, B 233; matches on record A 44, B 245; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21YUNDEK-DEK  (YES = Michiel De Krom)
Model: 87%
Kalshi: 60%
Gap: +28 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.033, surface_pool_high +0.037, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mariia Masiianskaia vs Anna Petkovic -- W15 Bol R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:252571:256682:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mariia Masiianskaia (`KXITFWMATCH-26OCT21MASPET-MAS`) | 0.04 / 0.07 (1) | 5.5% | 11.9% | 14.5% | 18.8% [15.1%-21.1%] | 13.3% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +6.4 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anna Petkovic (`KXITFWMATCH-26OCT21MASPET-PET`) | 0.91 / 0.94 (225) | 92.5% | 88.1% | 85.5% | 81.2% [78.9%-84.9%] | 86.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.4 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 536.0, B 1778.0; serve-point win A 48.1%, B 43.1%; Elo A 1167.3, B 1402.9; model uncertainty 0.0299
* Form inputs: days since last match A 177, B 94; matches on record A 66, B 78; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.007, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aurora Nosei vs Vanesa Mrazova -- W15 Bol R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21NOSMRA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vanesa Mrazova (`KXITFWMATCH-26OCT21NOSMRA-MRA`) | 0.18 / 0.21 (10) | 19.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aurora Nosei (`KXITFWMATCH-26OCT21NOSMRA-NOS`) | 0.79 / 0.80 (1) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Iva Primorac Pavicic vs Tamara Sramkova -- W15 Bol R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206248:261094:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iva Primorac Pavicic (`KXITFWMATCH-26OCT21PRISRA-PRI`) | 0.93 / 0.98 (750) | 95.5% | 91.5% | 83.9% | 83.9% [81.5%-85.4%] | 92.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.0 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Tamara Sramkova (`KXITFWMATCH-26OCT21PRISRA-SRA`) | 0.02 / 0.03 (20) | 2.5% | 8.5% | 16.1% | 16.1% [14.6%-18.5%] | 7.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +6.0 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1407.0, B 843.0; serve-point win A 58.4%, B 51.8%; Elo A 1490.7, B 1209.3; model uncertainty 0.0198
* Form inputs: days since last match A 9, B 177; matches on record A 415, B 69; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.024, surface_dev_loose +0.013, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anita Tu vs Diana Petrasova -- W15 Bol R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21TUXPET:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diana Petrasova (`KXITFWMATCH-26OCT21TUXPET-PET`) | 0.22 / 0.28 (5) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anita Tu (`KXITFWMATCH-26OCT21TUXPET-TUX`) | 0.71 / 0.77 (55) | 74.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Viktoria Varga vs Nika Stor -- W15 Bol R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21VARSTO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nika Stor (`KXITFWMATCH-26OCT21VARSTO-STO`) | 0.20 / 0.25 (15) | 22.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Viktoria Varga (`KXITFWMATCH-26OCT21VARSTO-VAR`) | 0.72 / 0.79 (72) | 75.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Juan Jose Bianchi / Jakub Vrba vs Alessio de Bernardis / Jacopo Vasami -- ATP Challenger Florence R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 13:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-21T13:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21BIAVRBDEVAS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Jose Bianchi / Jakub Vrba (`KXATPCHALLENGERDOUBLES-26OCT21BIAVRBDEVAS-BIAVRB`) | 0.05 / 0.78 (42) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alessio de Bernardis / Jacopo Vasami (`KXATPCHALLENGERDOUBLES-26OCT21BIAVRBDEVAS-DEVAS`) | 0.05 / 0.75 (100) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Federico Bondioli vs Francesco Forti -- ATP Challenger Florence R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 13:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-21T13:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209506:210682:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Federico Bondioli (`KXATPCHALLENGERMATCH-26OCT21BONFOR-BON`) | 0.40 / 0.42 (8048) | 41.0% | 38.0% | 25.1% | 33.8% [30.6%-38.9%] | -- | 41.3% | 41.3% | MODEL_LONE_OUTLIER | PASS | -3.0 pp | NORMAL | AGING | B / LIMITED | ALL_AGREE | VERIFIED |
| Francesco Forti (`KXATPCHALLENGERMATCH-26OCT21BONFOR-FOR`) | 0.59 / 0.60 (6730) | 59.5% | 62.0% | 74.9% | 66.2% [61.1%-69.5%] | -- | 59.2% | 59.2% | MODEL_LONE_OUTLIER | WATCH | +2.5 pp | NORMAL | AGING | B / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 797.0, B 1932.0; serve-point win A 61.0%, B 36.6%; Elo A 1416.1, B 1495.2; model uncertainty 0.0419
* Form inputs: days since last match A 123, B 9; matches on record A 99, B 373; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.018, surface_pool_high +0.019, surface_dev_loose -0.008, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Mats Hermans / Max Houkes vs Cosimo Banti / Matteo Mesaglio -- ATP Challenger Florence R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 13:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-21T13:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21HERHOUBANMES:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cosimo Banti / Matteo Mesaglio (`KXATPCHALLENGERDOUBLES-26OCT21HERHOUBANMES-BANMES`) | 0.05 / 0.95 (100) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mats Hermans / Max Houkes (`KXATPCHALLENGERDOUBLES-26OCT21HERHOUBANMES-HERHOU`) | 0.05 / 0.95 (100) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Corentin Moutet vs Felix Balshaw -- ATP Lyon R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-21 16:10Z
* Current expected start: 2026-10-21 13:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-21 12:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Clay · scheduled 2026-10-21T16:10:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144895:213149:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felix Balshaw (`KXATPMATCH-26OCT21MOUBAL-BAL`) | 0.51 / 0.52 (52874) | 51.5% | 29.6% | 39.5% | 31.4% [26.7%-35.6%] | 50.0% | 50.5% | 50.3% | MODEL_LONE_OUTLIER | PASS | -21.9 pp | HIGH_REVIEW | AGING | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Corentin Moutet (`KXATPMATCH-26OCT21MOUBAL-MOU`) | 0.48 / 0.49 (26440) | 48.5% | 70.3% | 60.5% | 68.5% [64.4%-73.3%] | 50.0% | 48.8% | 49.4% | MODEL_LONE_OUTLIER | WATCH | +21.9 pp | HIGH_REVIEW | AGING | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4547.0, B 1938.0; serve-point win A 64.1%, B 40.1%; Elo A 1835.1, B 1614.4; model uncertainty 0.0447
* Form inputs: days since last match A 1, B 2; matches on record A 585, B 47; data quality B

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT21MOUBAL-MOU  (YES = Corentin Moutet)
Model: 70%
Kalshi: 48%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: B (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.014, surface_dev_loose -0.009, surface_dev_tight +0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT21MOUBAL-BAL2` Will Felix Balshaw win at least 1.5 more games than Corentin Moutet?: 0.43/0.45 mid 44.0%, model 23.6% (projection_v2.0 (prediction ledger)) -- gap -20.4 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT21MOUBAL-MOU2` Will Corentin Moutet win at least 1.5 more games than Felix Balshaw?: 0.43/0.45 mid 44.0%, model 63.9% (projection_v2.0 (prediction ledger)) -- gap +19.9 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21MOUBAL-BAL20` Will Felix Balshaw win the Corentin Moutet vs Felix Balshaw match by a set score of 2-0?: 0.28/0.30 mid 29.0%, model 13.0% (projection_v2.0 (prediction ledger)) -- gap -16.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT21MOUBAL-2-MOU` Will Corentin Moutet win set 2 in the Corentin Moutet vs Felix Balshaw match: 0.47/0.50 mid 48.5%, model 63.9% (projection_v2.0 (prediction ledger)) -- gap +15.4 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT21MOUBAL-2-BAL` Will Felix Balshaw win set 2 in the Corentin Moutet vs Felix Balshaw match: 0.48/0.52 mid 50.0%, model 36.1% (projection_v2.0 (prediction ledger)) -- gap -13.9 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT21MOUBAL-1-BAL` Will Felix Balshaw win set 1 in the Corentin Moutet vs Felix Balshaw match: 0.48/0.49 mid 48.5%, model 36.1% (projection_v2.0 (prediction ledger)) -- gap -12.4 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT21MOUBAL-1-MOU` Will Corentin Moutet win set 1 in the Corentin Moutet vs Felix Balshaw match: 0.51/0.52 mid 51.5%, model 63.9% (projection_v2.0 (prediction ledger)) -- gap +12.4 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21MOUBAL-MOU20` Will Corentin Moutet win the Corentin Moutet vs Felix Balshaw match by a set score of 2-0?: 0.27/0.31 mid 29.0%, model 40.9% (projection_v2.0 (prediction ledger)) -- gap +11.9 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21MOUBAL-MOU21` Will Corentin Moutet win the Corentin Moutet vs Felix Balshaw match by a set score of 2-1?: 0.18/0.20 mid 19.0%, model 29.5% (projection_v2.0 (prediction ledger)) -- gap +10.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT21MOUBAL-MOU5` Will Corentin Moutet win at least 4.5 more games than Felix Balshaw?: 0.23/0.26 mid 24.5%, model 32.5% (projection_v2.0 (prediction ledger)) -- gap +8.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT21MOUBAL-28` Over 27.5 games: 0.28/0.32 mid 30.0%, model 35.6% (projection_v2.0 (prediction ledger)) -- gap +5.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT21MOUBAL-23` Over 22.5 games: 0.51/0.53 mid 52.0%, model 55.4% (projection_v2.0 (prediction ledger)) -- gap +3.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21MOUBAL-BAL21` Will Felix Balshaw win the Corentin Moutet vs Felix Balshaw match by a set score of 2-1?: 0.19/0.21 mid 20.0%, model 16.6% (projection_v2.0 (prediction ledger)) -- gap -3.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT21MOUBAL-18` Over 17.5 games: 0.87/0.91 mid 89.0%, model 89.9% (projection_v2.0 (prediction ledger)) -- gap +0.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS

## Henri Haupt vs Hugo Car -- M15 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 13:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-21T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210590:213098:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Car (`KXITFMATCH-26OCT21HAUCAR-CAR`) | 0.98 / 0.99 (2633) | 98.5% | 74.7% | 66.3% | 68.5% [68.5%-68.5%] | 90.7% | -- | 90.7% | KALSHI_LONE_OUTLIER | PASS | -23.8 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | SUPPORTS_MODEL_DIRECTION | AMBIGUOUS |
| Henri Haupt (`KXITFMATCH-26OCT21HAUCAR-HAU`) | 0.01 / 0.02 (463) | 1.5% | 25.3% | 33.7% | 31.4% [31.4%-31.4%] | 9.3% | -- | 9.3% | MODEL_LONE_OUTLIER | PASS | +23.8 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | SUPPORTS_MODEL_DIRECTION | AMBIGUOUS |

* Serve evidence (points): A 72.0, B 0.0; serve-point win A 59.2%, B 35.5%; Elo A 1158.1, B 1294.0; model uncertainty 0.0
* Form inputs: days since last match A 58, B 821; matches on record A 8, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21HAUCAR-HAU  (YES = Henri Haupt)
Model: 25%
Kalshi: 2%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: SUPPORTS_MODEL_DIRECTION
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bianca Jolie Fernandez vs Carlota Martinez Cirez -- W35 Santa Margherita di Pula R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 13:34Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-21T13:34:41Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220781:221988:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bianca Jolie Fernandez (`KXITFWMATCH-26OCT21FERMAR-FER`) | 0.15 / 0.19 (6342) | 17.0% | 19.3% | 20.2% | 23.0% [19.5%-26.9%] | -- | -- | -- | -- | PASS | +2.3 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carlota Martinez Cirez (`KXITFWMATCH-26OCT21FERMAR-MAR`) | 0.76 / 0.85 (6256) | 80.5% | 80.7% | 79.8% | 77.0% [73.2%-80.5%] | -- | -- | -- | -- | PASS | +0.2 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 334.0, B 3122.0; serve-point win A 48.0%, B 45.6%; Elo A 1362.6, B 1565.9; model uncertainty 0.0367
* Form inputs: days since last match A 429, B 37; matches on record A 150, B 422; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.020, surface_dev_loose -0.008, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Karol Drzewiecki / Piotr Matuszewski vs Joao Domingues / Tiago Torres -- ATP Challenger Lisbon R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 14:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-21T14:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21DRZMATDOMTOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joao Domingues / Tiago Torres (`KXATPCHALLENGERDOUBLES-26OCT21DRZMATDOMTOR-DOMTOR`) | 0.06 / 0.88 (12) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Karol Drzewiecki / Piotr Matuszewski (`KXATPCHALLENGERDOUBLES-26OCT21DRZMATDOMTOR-DRZMAT`) | 0.05 / 0.95 (100) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Finn Reynolds / James Watt vs Ariel Behar / Joshua Paris -- ATP Lyon QF

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-10-21 13:00Z
* Current expected start: 2026-10-21 14:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-21 13:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-21T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21REYWATBEHPAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ariel Behar / Joshua Paris (`KXATPDOUBLES-26OCT21REYWATBEHPAR-BEHPAR`) | 0.44 / 0.47 (11) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Finn Reynolds / James Watt (`KXATPDOUBLES-26OCT21REYWATBEHPAR-REYWAT`) | 0.52 / 0.54 (9) | 53.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Simone Agostini / Riccardo Perin vs Michele Ribecai / Gabriele Volpi -- ATP Challenger Florence R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-21T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21AGOPERRIBVOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Simone Agostini / Riccardo Perin (`KXATPCHALLENGERDOUBLES-26OCT21AGOPERRIBVOL-AGOPER`) | 0.05 / 0.70 (83) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Michele Ribecai / Gabriele Volpi (`KXATPCHALLENGERDOUBLES-26OCT21AGOPERRIBVOL-RIBVOL`) | 0.05 / 0.43 (44) | 24.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Geoffrey Blancaneaux vs Matej Sabanov -- M15 Bol R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106022:144972:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Geoffrey Blancaneaux (`KXITFMATCH-26OCT21BLASAB-BLA`) | 0.91 / 0.94 (1) | 92.5% | 73.9% | 43.3% | 70.7% [66.6%-76.3%] | -- | -- | -- | -- | PASS | -18.6 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Matej Sabanov (`KXITFMATCH-26OCT21BLASAB-SAB`) | 0.06 / 0.10 (13) | 8.0% | 26.1% | 56.7% | 29.3% [23.7%-33.4%] | -- | -- | -- | -- | PASS | +18.1 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 3141.0, B 337.0; serve-point win A 61.9%, B 43.0%; Elo A 1522.5, B 1319.6; model uncertainty 0.0484
* Form inputs: days since last match A 23, B 1542; matches on record A 630, B 227; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21BLASAB-SAB  (YES = Matej Sabanov)
Model: 26%
Kalshi: 8%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.013, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ivan Sabanov vs Stefan Popovic -- M15 Bol R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106049:209251:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefan Popovic (`KXITFMATCH-26OCT21SABPOP-POP`) | 0.49 / 0.86 (9) | 67.5% | 78.8% | 64.6% | 71.5% [69.7%-74.7%] | -- | -- | -- | -- | PASS | +11.3 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Ivan Sabanov (`KXITFMATCH-26OCT21SABPOP-SAB`) | 0.23 / 0.38 (11) | 30.5% | 21.2% | 35.4% | 28.5% [25.3%-30.3%] | -- | -- | -- | -- | PASS | -9.3 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 44.0, B 216.0; serve-point win A 57.1%, B 36.6%; Elo A 1179.9, B 1345.4; model uncertainty 0.0246
* Form inputs: days since last match A 842, B 51; matches on record A 119, B 192; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.026, surface_pool_high +0.018, surface_dev_loose +0.000, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## David Tixhon vs Carles Cordoba -- M15 Bol R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21TIXCOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carles Cordoba (`KXITFMATCH-26OCT21TIXCOR-COR`) | 0.85 / 0.88 (1) | 86.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| David Tixhon (`KXITFMATCH-26OCT21TIXCOR-TIX`) | 0.07 / 0.14 (63) | 10.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lejla Hana Golubovic vs Maja Radenkovic -- W15 Bol R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222041:263914:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lejla Hana Golubovic (`KXITFWMATCH-26OCT21GOLRAD-GOL`) | 0.06 / 0.08 (425) | 7.0% | 32.4% | 50.0% | 44.7% [42.6%-46.8%] | 10.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +25.4 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Maja Radenkovic (`KXITFWMATCH-26OCT21GOLRAD-RAD`) | 0.92 / 0.95 (151) | 93.5% | 67.7% | 50.0% | 55.3% [53.2%-57.4%] | 89.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -25.9 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 52.2%, B 44.4%; Elo A 1250.6, B 1286.2; model uncertainty 0.0211
* Form inputs: days since last match A 730, B 912; matches on record A 26, B 120; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21GOLRAD-GOL  (YES = Lejla Hana Golubovic)
Model: 32%
Kalshi: 7%
Gap: +25 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.021, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daria Gorska vs Mariya Yemshanova -- W15 Bol R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:239484:270167:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daria Gorska (`KXITFWMATCH-26OCT21GORYEM-GOR`) | 0.90 / 0.93 (12) | 91.5% | 77.7% | 60.5% | 59.5% [57.4%-62.6%] | 89.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.8 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mariya Yemshanova (`KXITFWMATCH-26OCT21GORYEM-YEM`) | 0.06 / 0.10 (77) | 8.0% | 22.3% | 39.5% | 40.5% [37.4%-42.6%] | 11.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +14.3 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 685.0, B 91.0; serve-point win A 57.4%, B 48.4%; Elo A 1294.9, B 1226.5; model uncertainty 0.0259
* Form inputs: days since last match A 80, B 177; matches on record A 63, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.021, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lea Sabadi vs Mia Horvit -- W15 Bol R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21SABHOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mia Horvit (`KXITFWMATCH-26OCT21SABHOR-HOR`) | 0.92 / 0.94 (557) | 93.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lea Sabadi (`KXITFWMATCH-26OCT21SABHOR-SAB`) | 0.07 / 0.08 (675) | 7.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tara Wuerth vs Lara Seric -- W15 Bol R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21WUESER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lara Seric (`KXITFWMATCH-26OCT21WUESER-SER`) | 0.01 / 0.03 (359) | 2.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tara Wuerth (`KXITFWMATCH-26OCT21WUESER-WUE`) | 0.97 / 0.99 (8990) | 98.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sonja Zhenikhova vs Masa Jankovic -- W15 Bol R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21ZHEJAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Masa Jankovic (`KXITFWMATCH-26OCT21ZHEJAN-JAN`) | 0.22 / 0.23 (8) | 22.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sonja Zhenikhova (`KXITFWMATCH-26OCT21ZHEJAN-ZHE`) | 0.75 / 0.80 (28) | 77.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pierre-Hugues Herbert vs Taylor Fritz -- ATP Lyon R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-21 15:00Z
* Current expected start: 2026-10-21 15:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-21 14:15Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-22T04:00:00+00:00 as not a valid time; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Clay · scheduled 2026-10-21T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105732:126203:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Taylor Fritz (`KXATPMATCH-26OCT21HERFRI-FRI`) | 0.83 / 0.84 (13417) | 83.5% | 85.8% | 86.0% | 84.9% [82.8%-86.6%] | -- | -- | -- | -- | PASS | +2.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pierre-Hugues Herbert (`KXATPMATCH-26OCT21HERFRI-HER`) | 0.16 / 0.17 (1909) | 16.5% | 14.2% | 14.0% | 15.1% [13.4%-17.2%] | -- | -- | -- | -- | PASS | -2.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2803.0, B 6022.0; serve-point win A 62.9%, B 28.1%; Elo A 1617.3, B 1883.7; model uncertainty 0.0189
* Form inputs: days since last match A 1, B 9; matches on record A 851, B 739; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.021, surface_dev_loose +0.006, surface_dev_tight -0.003
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT21HERFRI-FRI8` Will Taylor Fritz win at least 7.5 more games than Pierre-Hugues Herbert?: 0.04/0.26 mid 15.0%, model 4.1% (projection_v2.0 (prediction ledger)) -- gap -10.9 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21HERFRI-FRI21` Will Taylor Fritz win the Pierre-Hugues Herbert vs Taylor Fritz match by a set score of 2-1?: 0.14/0.24 mid 19.0%, model 27.6% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT21HERFRI-18` Over 17.5 games: 0.81/0.88 mid 84.5%, model 90.8% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT21HERFRI-28` Over 27.5 games: 0.22/0.29 mid 25.5%, model 31.2% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT21HERFRI-FRI2` Will Taylor Fritz win at least 1.5 more games than Pierre-Hugues Herbert?: 0.69/0.84 mid 76.5%, model 80.5% (projection_v2.0 (prediction ledger)) -- gap +4.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21HERFRI-FRI20` Will Taylor Fritz win the Pierre-Hugues Herbert vs Taylor Fritz match by a set score of 2-0?: 0.59/0.63 mid 61.0%, model 58.2% (projection_v2.0 (prediction ledger)) -- gap -2.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT21HERFRI-23` Over 22.5 games: 0.47/0.48 mid 47.5%, model 50.2% (projection_v2.0 (prediction ledger)) -- gap +2.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21HERFRI-HER21` Will Pierre-Hugues Herbert win the Pierre-Hugues Herbert vs Taylor Fritz match by a set score of 2-1?: 0.02/0.10 mid 6.0%, model 8.6% (projection_v2.0 (prediction ledger)) -- gap +2.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT21HERFRI-2-HER` Will Pierre-Hugues Herbert win set 2 in the Pierre-Hugues Herbert vs Taylor Fritz match: 0.08/0.43 mid 25.5%, model 23.7% (projection_v2.0 (prediction ledger)) -- gap -1.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21HERFRI-HER20` Will Pierre-Hugues Herbert win the Pierre-Hugues Herbert vs Taylor Fritz match by a set score of 2-0?: 0.04/0.09 mid 6.5%, model 5.6% (projection_v2.0 (prediction ledger)) -- gap -0.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT21HERFRI-1-FRI` Will Taylor Fritz win set 1 in the Pierre-Hugues Herbert vs Taylor Fritz match: 0.74/0.77 mid 75.5%, model 76.3% (projection_v2.0 (prediction ledger)) -- gap +0.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT21HERFRI-1-HER` Will Pierre-Hugues Herbert win set 1 in the Pierre-Hugues Herbert vs Taylor Fritz match: 0.23/0.26 mid 24.5%, model 23.7% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT21HERFRI-2-FRI` Will Taylor Fritz win set 2 in the Pierre-Hugues Herbert vs Taylor Fritz match: 0.56/0.95 mid 75.5%, model 76.3% (projection_v2.0 (prediction ledger)) -- gap +0.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT21HERFRI-FRI5` Will Taylor Fritz win at least 4.5 more games than Pierre-Hugues Herbert?: 0.38/0.39 mid 38.5%, model 38.2% (projection_v2.0 (prediction ledger)) -- gap -0.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Arthur Bellegy vs Lorenzo Angelini -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-21T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:149117:213004:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Angelini (`KXITFMATCH-26OCT21BELANG-ANG`) | 0.98 / 0.99 (6711) | 98.5% | 61.6% | 50.0% | 52.0% [51.0%-53.0%] | 86.2% | -- | 86.2% | KALSHI_LONE_OUTLIER | PASS | -36.9 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Arthur Bellegy (`KXITFMATCH-26OCT21BELANG-BEL`) | 0.01 / 0.02 (9357) | 1.5% | 38.4% | 50.0% | 48.0% [47.0%-49.0%] | 13.8% | -- | 13.8% | KALSHI_LONE_OUTLIER | PASS | +36.9 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 60.8%, B 36.9%; Elo A 1199.8, B 1211.4; model uncertainty 0.0101
* Form inputs: days since last match A 709, B 674; matches on record A 3, B 13; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21BELANG-BEL  (YES = Arthur Bellegy)
Model: 38%
Kalshi: 2%
Gap: +37 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: SUPPORTS_MODEL_DIRECTION
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Branko Djuric vs Andrea De Marchi -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-21T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210025:212972:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrea De Marchi (`KXITFMATCH-26OCT21DJUDEM-DEM`) | 0.17 / 0.42 (1) | 29.5% | 28.6% | 54.5% | 30.7% [30.6%-31.6%] | 30.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Branko Djuric (`KXITFMATCH-26OCT21DJUDEM-DJU`) | 0.50 / 0.85 (1) | 67.5% | 71.4% | 45.5% | 69.3% [68.4%-69.5%] | 69.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.9 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 387.0, B 0.0; serve-point win A 65.0%, B 39.5%; Elo A 1416.1, B 1273.8; model uncertainty 0.0053
* Form inputs: days since last match A 404, B 751; matches on record A 69, B 7; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Younes Lalami Laaroussi / Mario Mansilla Diez vs Max Alcala Gurri / Nikolas Sanchez Izquierdo -- ATP Challenger Lisbon R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-21T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21LALMANALCSAI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Max Alcala Gurri / Nikolas Sanchez Izquierdo (`KXATPCHALLENGERDOUBLES-26OCT21LALMANALCSAI-ALCSAI`) | 0.05 / 0.95 (100) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Younes Lalami Laaroussi / Mario Mansilla Diez (`KXATPCHALLENGERDOUBLES-26OCT21LALMANALCSAI-LALMAN`) | 0.05 / 0.88 (1) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Manuel Mazza vs Andrey Chepelev -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-21T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200184:207601:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrey Chepelev (`KXITFMATCH-26OCT21MAZCHE-CHE`) | 0.51 / 0.52 (4157) | 51.5% | 36.0% | 56.1% | 51.5% [46.9%-56.1%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.4 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Manuel Mazza (`KXITFMATCH-26OCT21MAZCHE-MAZ`) | 0.48 / 0.49 (4392) | 48.5% | 63.9% | 43.9% | 48.5% [43.9%-53.1%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +15.4 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 249.0, B 285.0; serve-point win A 62.2%, B 40.6%; Elo A 1384.7, B 1388.9; model uncertainty 0.0461
* Form inputs: days since last match A 674, B 65; matches on record A 94, B 488; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21MAZCHE-MAZ  (YES = Manuel Mazza)
Model: 64%
Kalshi: 48%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.031, surface_pool_high -0.036, surface_dev_loose -0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Thiago Monteiro vs Henrique Rocha -- ATP Challenger Lisbon R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-21T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106329:210012:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thiago Monteiro (`KXATPCHALLENGERMATCH-26OCT21MONROC-MON`) | 0.38 / 0.39 (0) | 38.5% | 43.5% | 39.1% | 44.5% [42.5%-47.0%] | 36.2% | -- | 36.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +5.0 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Henrique Rocha (`KXATPCHALLENGERMATCH-26OCT21MONROC-ROC`) | 0.61 / 0.62 (72) | 61.5% | 56.5% | 60.9% | 55.5% [53.0%-57.5%] | 63.8% | -- | 63.8% | MODEL_LONE_OUTLIER | PASS | -5.0 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4367.0, B 3624.0; serve-point win A 62.6%, B 36.1%; Elo A 1711.8, B 1672.0; model uncertainty 0.0224
* Form inputs: days since last match A 9, B 9; matches on record A 921, B 287; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.010, surface_dev_loose -0.010, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; THIN_DISPLAYED_SIZE

## Kaat Coppez vs Isabella Shinikova -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:202688:266467:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kaat Coppez (`KXITFWMATCH-26OCT21COPSHI-COP`) | 0.99 / -- (0) | -- | 15.5% | 23.1% | 20.0% [19.0%-20.8%] | -- | -- | -- | -- | PASS | -- | UNPRICED | AGING | C / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |
| Isabella Shinikova (`KXITFWMATCH-26OCT21COPSHI-SHI`) | -- / 0.01 (158879) | -- | 84.5% | 76.9% | 80.0% [79.2%-81.0%] | -- | -- | -- | -- | WATCH | -- | UNPRICED | AGING | C / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 759.0, B 3553.0; serve-point win A 50.3%, B 42.1%; Elo A 1298.8, B 1558.1; model uncertainty 0.0092
* Form inputs: days since last match A 177, B 10; matches on record A 70, B 1028; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.004, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jian Ibrahim vs Sofiia Suslova -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:248662:252582:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jian Ibrahim (`KXITFWMATCH-26OCT21IBRSUS-IBR`) | 0.60 / 0.63 (3) | 61.5% | 31.6% | 25.6% | 36.4% [31.5%-39.5%] | -- | -- | -- | -- | PASS | -29.9 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sofiia Suslova (`KXITFWMATCH-26OCT21IBRSUS-SUS`) | 0.36 / 0.38 (1) | 37.0% | 68.4% | 74.4% | 63.6% [60.6%-68.5%] | -- | -- | -- | -- | PASS | +31.4 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 382.0, B 719.0; serve-point win A 51.1%, B 45.3%; Elo A 1212.8, B 1288.2; model uncertainty 0.0399
* Form inputs: days since last match A 352, B 233; matches on record A 34, B 38; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21IBRSUS-SUS  (YES = Sofiia Suslova)
Model: 68%
Kalshi: 37%
Gap: +31 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marylee Longpre vs Emilia Carlotta Brune -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21LONBRU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emilia Carlotta Brune (`KXITFWMATCH-26OCT21LONBRU-BRU`) | 0.98 / 0.99 (2209) | 98.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marylee Longpre (`KXITFWMATCH-26OCT21LONBRU-LON`) | 0.01 / 0.02 (489) | 1.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ginevra Parentini Vallega Montebruno vs Matilde Paoletti -- W35 Santa Margherita di Pula R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-21T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222396:237481:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matilde Paoletti (`KXITFWMATCH-26OCT21PARPAO-PAO`) | 0.98 / 0.99 (496) | 98.5% | 94.8% | 80.8% | 88.3% [87.3%-89.4%] | 95.7% | -- | 95.7% | MODEL_LONE_OUTLIER | PASS | -3.6 pp | NORMAL | AGING | D / POOR | ALL_AGREE | VERIFIED |
| Ginevra Parentini Vallega Montebruno (`KXITFWMATCH-26OCT21PARPAO-PAR`) | 0.01 / 0.05 (1380) | 3.0% | 5.1% | 19.2% | 11.7% [10.6%-12.7%] | 4.3% | -- | 4.3% | MODEL_LONE_OUTLIER | PASS | +2.1 pp | NORMAL | AGING | D / POOR | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 813.0, B 466.0; serve-point win A 46.1%, B 41.7%; Elo A 1271.0, B 1663.3; model uncertainty 0.0105
* Form inputs: days since last match A 254, B 198; matches on record A 143, B 103; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ilary Pistola vs Yasmin Ezzat -- W35 Santa Margherita di Pula R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-21T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221474:270265:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yasmin Ezzat (`KXITFWMATCH-26OCT21PISEZZ-EZZ`) | 0.01 / 0.02 (171) | 1.5% | 74.2% | 69.4% | 65.1% [64.6%-66.6%] | 27.6% | -- | 27.6% | KALSHI_LONE_OUTLIER | PASS | +72.7 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Ilary Pistola (`KXITFWMATCH-26OCT21PISEZZ-PIS`) | 0.98 / 0.99 (92) | 98.5% | 25.8% | 30.6% | 34.9% [33.4%-35.4%] | 72.4% | -- | 72.4% | MODEL_LONE_OUTLIER | PASS | -72.7 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 175.0, B 2756.0; serve-point win A 51.5%, B 43.7%; Elo A 1281.7, B 1389.5; model uncertainty 0.0099
* Form inputs: days since last match A 92, B 184; matches on record A 5, B 271; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21PISEZZ-EZZ  (YES = Yasmin Ezzat)
Model: 74%
Kalshi: 2%
Gap: +73 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: SUPPORTS_MODEL_DIRECTION
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nina Radovanovic vs Laura Boehner -- W35 Santa Margherita di Pula R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-21T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221258:222602:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Laura Boehner (`KXITFWMATCH-26OCT21RADBOE-BOE`) | 0.04 / 0.07 (33) | 5.5% | 27.0% | 13.1% | 27.4% [21.9%-33.9%] | 7.8% | -- | 7.8% | KALSHI_LONE_OUTLIER | WATCH | +21.5 pp | HIGH_REVIEW | AGING | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Nina Radovanovic (`KXITFWMATCH-26OCT21RADBOE-RAD`) | 0.93 / 0.96 (14) | 94.5% | 73.0% | 86.9% | 72.6% [66.1%-78.1%] | 92.2% | -- | 92.2% | KALSHI_LONE_OUTLIER | PASS | -21.5 pp | HIGH_REVIEW | AGING | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 976.0, B 824.0; serve-point win A 55.6%, B 49.0%; Elo A 1386.2, B 1298.6; model uncertainty 0.0602
* Form inputs: days since last match A 177, B 191; matches on record A 247, B 221; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21RADBOE-BOE  (YES = Laura Boehner)
Model: 27%
Kalshi: 6%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.034, surface_pool_high -0.037, surface_dev_loose +0.018, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tommaso Compagnucci vs Lorenzo Carboni -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 15:03Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-21T15:03:43Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206867:212077:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Carboni (`KXITFMATCH-26OCT21COMCAR-CAR`) | 0.71 / 0.72 (2894) | 71.5% | 40.7% | 49.5% | 37.8% [33.3%-39.8%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -30.8 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tommaso Compagnucci (`KXITFMATCH-26OCT21COMCAR-COM`) | 0.28 / 0.29 (2583) | 28.5% | 59.3% | 50.5% | 62.2% [60.2%-66.7%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +30.8 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 515.0, B 448.0; serve-point win A 61.0%, B 40.9%; Elo A 1489.9, B 1371.5; model uncertainty 0.0326
* Form inputs: days since last match A 674, B 170; matches on record A 85, B 79; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21COMCAR-COM  (YES = Tommaso Compagnucci)
Model: 59%
Kalshi: 28%
Gap: +31 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Saveliy Ivanov vs Volodymyr Iakubenko -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211676:212246:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Volodymyr Iakubenko (`KXITFMATCH-26OCT21IVAIAK-IAK`) | 0.66 / 0.68 (1951) | 67.0% | 66.0% | 46.5% | 63.7% [62.7%-63.9%] | -- | -- | -- | -- | PASS | -1.0 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Saveliy Ivanov (`KXITFMATCH-26OCT21IVAIAK-IVA`) | 0.32 / 0.34 (2667) | 33.0% | 34.0% | 53.5% | 36.3% [36.1%-37.3%] | -- | -- | -- | -- | PASS | +1.0 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 204.0, B 0.0; serve-point win A 61.8%, B 34.9%; Elo A 1207.6, B 1305.7; model uncertainty 0.006
* Form inputs: days since last match A 723, B 821; matches on record A 65, B 18; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.009, surface_dev_loose +0.001, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Miles Jones vs Ewen Lumsden -- M15 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-21T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202077:207404:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miles Jones (`KXITFMATCH-26OCT21JONLUM-JON`) | 0.69 / 0.70 (1) | 69.5% | 30.8% | 50.0% | 38.0% [38.0%-38.0%] | 50.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -38.7 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ewen Lumsden (`KXITFMATCH-26OCT21JONLUM-LUM`) | 0.28 / 0.30 (19) | 29.0% | 69.2% | 50.0% | 62.0% [62.0%-62.0%] | 50.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +40.2 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 60.0%, B 36.0%; Elo A 1322.1, B 1408.2; model uncertainty 0.0
* Form inputs: days since last match A 695, B 695; matches on record A 78, B 60; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21JONLUM-LUM  (YES = Ewen Lumsden)
Model: 69%
Kalshi: 29%
Gap: +40 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matthew Thomson vs Ioannis Xilas -- M15 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-21T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207452:209354:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthew Thomson (`KXITFMATCH-26OCT21THOXIL-THO`) | -- / 0.01 (6414) | -- | 26.1% | 62.8% | 37.7% [34.8%-41.7%] | 16.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | AGING | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |
| Ioannis Xilas (`KXITFMATCH-26OCT21THOXIL-XIL`) | 0.99 / -- (0) | -- | 73.9% | 37.2% | 62.3% [58.3%-65.2%] | 83.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | AGING | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 0.0, B 992.0; serve-point win A 56.3%, B 38.8%; Elo A 1260.0, B 1344.8; model uncertainty 0.0348
* Form inputs: days since last match A 709, B 100; matches on record A 12, B 90; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.029, surface_pool_high +0.040, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Benoit Torcq vs Sidane Pontjodikromo -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207412:212498:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sidane Pontjodikromo (`KXITFMATCH-26OCT21TORPON-PON`) | 0.07 / 0.08 (5) | 7.5% | 84.5% | 41.0% | 81.8% [80.4%-82.4%] | -- | -- | -- | -- | PASS | +77.0 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Benoit Torcq (`KXITFMATCH-26OCT21TORPON-TOR`) | 0.92 / 0.93 (19) | 92.5% | 15.5% | 59.0% | 18.2% [17.6%-19.6%] | -- | -- | -- | -- | PASS | -77.0 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 189.0; serve-point win A 58.8%, B 33.1%; Elo A 1178.5, B 1435.8; model uncertainty 0.0101
* Form inputs: days since last match A 793, B 716; matches on record A 9, B 240; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21TORPON-PON  (YES = Sidane Pontjodikromo)
Model: 84%
Kalshi: 8%
Gap: +77 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.007, surface_dev_loose +0.000, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aleksandra Pozarenko vs Anastasia Bertacchi -- W15 Villena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21POZBER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasia Bertacchi (`KXITFWMATCH-26OCT21POZBER-BER`) | 0.90 / 0.91 (6) | 90.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aleksandra Pozarenko (`KXITFWMATCH-26OCT21POZBER-POZ`) | 0.09 / 0.10 (10) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sabine Rutlauka vs Chelsea Fontenel -- W35 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-21T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223404:239454:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chelsea Fontenel (`KXITFWMATCH-26OCT21RUTFON-FON`) | 0.84 / 0.85 (6230) | 84.5% | 39.3% | 47.9% | 40.0% [36.9%-42.1%] | 53.8% | -- | 53.8% | MODEL_LONE_OUTLIER | PASS | -45.2 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Sabine Rutlauka (`KXITFWMATCH-26OCT21RUTFON-RUT`) | 0.15 / 0.16 (4857) | 15.5% | 60.7% | 52.1% | 60.0% [57.9%-63.1%] | 46.2% | -- | 46.2% | KALSHI_LONE_OUTLIER | PASS | +45.2 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 1315.0, B 2027.0; serve-point win A 55.2%, B 46.8%; Elo A 1438.3, B 1321.2; model uncertainty 0.0257
* Form inputs: days since last match A 177, B 184; matches on record A 93, B 114; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21RUTFON-RUT  (YES = Sabine Rutlauka)
Model: 61%
Kalshi: 16%
Gap: +45 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: SUPPORTS_MODEL_DIRECTION
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Demi Tran vs Eleejah Inisan -- W35 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-21T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221994:260966:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eleejah Inisan (`KXITFWMATCH-26OCT21TRAINI-INI`) | 0.22 / 0.24 (30) | 23.0% | 77.8% | 71.8% | 70.0% [66.1%-72.3%] | 65.2% | -- | 65.2% | MODEL_LONE_OUTLIER | WATCH | +54.9 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Demi Tran (`KXITFWMATCH-26OCT21TRAINI-TRA`) | 0.74 / 0.78 (73) | 76.0% | 22.1% | 28.2% | 30.0% [27.7%-33.9%] | 34.8% | -- | 34.8% | MODEL_LONE_OUTLIER | PASS | -53.9 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 1766.0, B 1565.0; serve-point win A 48.3%, B 46.0%; Elo A 1342.5, B 1467.8; model uncertainty 0.0308
* Form inputs: days since last match A 191, B 156; matches on record A 290, B 87; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21TRAINI-INI  (YES = Eleejah Inisan)
Model: 78%
Kalshi: 23%
Gap: +55 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: SUPPORTS_MODEL_DIRECTION
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maja Wrobel vs Lola Giza -- W15 Karlovy Vary R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260503:270208:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lola Giza (`KXITFWMATCH-26OCT21WROGIZ-GIZ`) | 0.99 / -- (0) | -- | 57.0% | 38.4% | 47.9% [46.8%-47.9%] | 75.3% | -- | 75.3% | KALSHI_LONE_OUTLIER | PASS | -- | UNPRICED | AGING | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |
| Maja Wrobel (`KXITFWMATCH-26OCT21WROGIZ-WRO`) | -- / 0.01 (5382) | -- | 43.0% | 61.6% | 52.1% [52.1%-53.2%] | 24.7% | -- | 24.7% | KALSHI_LONE_OUTLIER | PASS | -- | UNPRICED | AGING | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 62.0, B 432.0; serve-point win A 52.5%, B 46.2%; Elo A 1264.4, B 1249.9; model uncertainty 0.0054
* Form inputs: days since last match A 429, B 443; matches on record A 1, B 14; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Francesco Forti / Filippo Romano vs Marko Maric / Tadija Radovanovic -- ATP Challenger Florence R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 15:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-21T15:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21FORROMMARRAD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesco Forti / Filippo Romano (`KXATPCHALLENGERDOUBLES-26OCT21FORROMMARRAD-FORROM`) | 0.05 / 0.95 (223) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marko Maric / Tadija Radovanovic (`KXATPCHALLENGERDOUBLES-26OCT21FORROMMARRAD-MARRAD`) | 0.05 / 0.95 (223) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## David Goffin vs Remy Bertola -- ATP Brussels R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-20 13:00Z
* Current expected start: 2026-10-21 16:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-21 15:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1620_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-10-20T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105676:200329:2026-10-20`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Remy Bertola (`KXATPMATCH-26OCT20GOFBER-BER`) | 0.63 / 0.64 (30125) | 63.5% | 44.8% | 48.0% | 38.1% [33.4%-42.0%] | -- | -- | -- | -- | PASS | -18.7 pp | HIGH_REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| David Goffin (`KXATPMATCH-26OCT20GOFBER-GOF`) | 0.36 / 0.37 (2621) | 36.5% | 55.2% | 52.0% | 61.9% [58.0%-66.6%] | -- | -- | -- | -- | WATCH | +18.7 pp | HIGH_REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2091.0, B 3345.0; serve-point win A 63.2%, B 37.9%; Elo A 1759.6, B 1574.3; model uncertainty 0.0431
* Form inputs: days since last match A 22, B 2; matches on record A 1047, B 408; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT20GOFBER-GOF  (YES = David Goffin)
Model: 55%
Kalshi: 36%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.010, surface_dev_loose -0.025, surface_dev_tight +0.019
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT20GOFBER-BER4` Will Remy Bertola win at least 3.5 more games than David Goffin?: 0.45/0.47 mid 46.0%, model 23.4% (projection_v2.0 (prediction ledger)) -- gap -22.6 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT20GOFBER-BER20` Will Remy Bertola win the David Goffin vs Remy Bertola match by a set score of 2-0?: 0.39/0.42 mid 40.5%, model 21.6% (projection_v2.0 (prediction ledger)) -- gap -18.9 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT20GOFBER-BER7` Will Remy Bertola win at least 6.5 more games than David Goffin?: 0.09/0.35 mid 22.0%, model 3.8% (projection_v2.0 (prediction ledger)) -- gap -18.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT20GOFBER-GOF2` Will David Goffin win at least 1.5 more games than Remy Bertola?: 0.29/0.32 mid 30.5%, model 47.9% (projection_v2.0 (prediction ledger)) -- gap +17.4 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT20GOFBER-2-GOF` Will David Goffin win set 2 in the David Goffin vs Remy Bertola match: 0.36/0.40 mid 38.0%, model 53.5% (projection_v2.0 (prediction ledger)) -- gap +15.5 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT20GOFBER-1-GOF` Will David Goffin win set 1 in the David Goffin vs Remy Bertola match: 0.37/0.40 mid 38.5%, model 53.5% (projection_v2.0 (prediction ledger)) -- gap +15.0 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT20GOFBER-1-BER` Will Remy Bertola win set 1 in the David Goffin vs Remy Bertola match: 0.59/0.62 mid 60.5%, model 46.5% (projection_v2.0 (prediction ledger)) -- gap -14.0 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT20GOFBER-2-BER` Will Remy Bertola win set 2 in the David Goffin vs Remy Bertola match: 0.58/0.62 mid 60.0%, model 46.5% (projection_v2.0 (prediction ledger)) -- gap -13.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT20GOFBER-23` Over 22.5 games: 0.46/0.48 mid 47.0%, model 60.1% (projection_v2.0 (prediction ledger)) -- gap +13.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT20GOFBER-GOF21` Will David Goffin win the David Goffin vs Remy Bertola match by a set score of 2-1?: 0.14/0.17 mid 15.5%, model 26.6% (projection_v2.0 (prediction ledger)) -- gap +11.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT20GOFBER-28` Over 27.5 games: 0.28/0.29 mid 28.5%, model 39.6% (projection_v2.0 (prediction ledger)) -- gap +11.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT20GOFBER-GOF20` Will David Goffin win the David Goffin vs Remy Bertola match by a set score of 2-0?: 0.18/0.22 mid 20.0%, model 28.6% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT20GOFBER-18` Over 17.5 games: 0.83/0.86 mid 84.5%, model 92.6% (projection_v2.0 (prediction ledger)) -- gap +8.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT20GOFBER-BER21` Will Remy Bertola win the David Goffin vs Remy Bertola match by a set score of 2-1?: 0.20/0.24 mid 22.0%, model 23.1% (projection_v2.0 (prediction ledger)) -- gap +1.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dan Added vs Daniel Domingos -- M25 Luanda R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200385:213637:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dan Added (`KXITFMATCH-26OCT21ADDDOM-ADD`) | 0.42 / 0.43 (3448) | 42.5% | 90.7% | 48.5% | 85.7% [85.7%-85.7%] | 83.0% | -- | 83.0% | MODEL_LONE_OUTLIER | PASS | +48.2 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Daniel Domingos (`KXITFMATCH-26OCT21ADDDOM-DOM`) | 0.57 / 0.58 (5586) | 57.5% | 9.3% | 51.5% | 14.3% [14.3%-14.3%] | 17.0% | -- | 17.0% | KALSHI_LONE_OUTLIER | PASS | -48.2 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 2646.0, B 0.0; serve-point win A 67.2%, B 43.3%; Elo A 1548.9, B 1237.8; model uncertainty 0.0
* Form inputs: days since last match A 23, B 695; matches on record A 529, B 5; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21ADDDOM-ADD  (YES = Dan Added)
Model: 91%
Kalshi: 42%
Gap: +48 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: SUPPORTS_MODEL_DIRECTION
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_CALIBRATION_OUTLIER, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hugo Grenier vs Marcus Walters -- M25 Redbridge R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126409:126971:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Grenier (`KXITFMATCH-26OCT21GREWAL-GRE`) | 0.86 / 0.87 (5623) | 86.5% | 95.5% | 76.3% | 94.3% [93.7%-94.5%] | 83.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +9.0 pp | NORMAL | AGING | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marcus Walters (`KXITFMATCH-26OCT21GREWAL-WAL`) | 0.13 / 0.14 (5564) | 13.5% | 4.5% | 23.7% | 5.7% [5.5%-6.3%] | 16.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.0 pp | NORMAL | AGING | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3226.0, B 91.0; serve-point win A 68.2%, B 45.2%; Elo A 1654.5, B 1158.4; model uncertainty 0.0044
* Form inputs: days since last match A 9, B 107; matches on record A 753, B 53; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nikita Ianin vs Ruslan Serazhetdinov -- M25 Luanda R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210394:213135:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikita Ianin (`KXITFMATCH-26OCT21IANSER-IAN`) | 0.98 / 0.99 (6224) | 98.5% | 40.2% | 50.0% | 34.2% [34.2%-34.2%] | 80.5% | -- | 80.5% | MODEL_LONE_OUTLIER | PASS | -58.3 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | SUPPORTS_MODEL_DIRECTION | AMBIGUOUS |
| Ruslan Serazhetdinov (`KXITFMATCH-26OCT21IANSER-SER`) | 0.01 / 0.02 (5913) | 1.5% | 59.8% | 50.0% | 65.8% [65.8%-65.8%] | 19.5% | -- | 19.5% | KALSHI_LONE_OUTLIER | PASS | +58.3 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | SUPPORTS_MODEL_DIRECTION | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 61.0%, B 37.0%; Elo A 1138.7, B 1250.8; model uncertainty 0.0
* Form inputs: days since last match A 716, B 779; matches on record A 37, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21IANSER-SER  (YES = Ruslan Serazhetdinov)
Model: 60%
Kalshi: 2%
Gap: +58 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: SUPPORTS_MODEL_DIRECTION
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sebastian Sorger vs Finn Murgett -- M25 Redbridge R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208818:210285:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Finn Murgett (`KXITFMATCH-26OCT21SORMUR-MUR`) | 0.36 / 0.37 (4391) | 36.5% | 15.8% | 45.4% | 23.6% [23.6%-23.7%] | 29.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -20.6 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Sebastian Sorger (`KXITFMATCH-26OCT21SORMUR-SOR`) | 0.63 / 0.64 (4253) | 63.5% | 84.2% | 54.6% | 76.4% [76.3%-76.4%] | 70.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +20.6 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 572.0, B 0.0; serve-point win A 65.0%, B 42.9%; Elo A 1428.2, B 1222.1; model uncertainty 0.0005
* Form inputs: days since last match A 44, B 1073; matches on record A 154, B 15; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21SORMUR-SOR  (YES = Sebastian Sorger)
Model: 84%
Kalshi: 64%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kamilla Bartone vs Anastasia Efremova -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221886:267540:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kamilla Bartone (`KXITFWMATCH-26OCT21BAREFR-BAR`) | 0.69 / 0.80 (33) | 74.5% | 79.1% | 64.5% | 71.2% [69.8%-73.9%] | -- | -- | -- | -- | PASS | +4.6 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anastasia Efremova (`KXITFWMATCH-26OCT21BAREFR-EFR`) | 0.22 / 0.24 (1) | 23.0% | 20.9% | 35.5% | 28.8% [26.2%-30.2%] | -- | -- | -- | -- | PASS | -2.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1376.0, B 611.0; serve-point win A 58.6%, B 47.5%; Elo A 1529.0, B 1345.5; model uncertainty 0.0204
* Form inputs: days since last match A 191, B 191; matches on record A 228, B 14; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.005, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Clarissa Blomqvist vs Federica Sacco -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221864:241745:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Clarissa Blomqvist (`KXITFWMATCH-26OCT21BLOSAC-BLO`) | 0.16 / 0.23 (10) | 19.5% | 20.8% | 16.9% | 24.4% [20.8%-30.1%] | -- | -- | -- | -- | PASS | +1.4 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Federica Sacco (`KXITFWMATCH-26OCT21BLOSAC-SAC`) | 0.79 / 0.83 (43) | 81.0% | 79.1% | 83.1% | 75.6% [69.9%-79.2%] | -- | -- | -- | -- | PASS | -1.9 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1520.0, B 1826.0; serve-point win A 51.5%, B 42.4%; Elo A 1313.9, B 1431.3; model uncertainty 0.0466
* Form inputs: days since last match A 177, B 184; matches on record A 84, B 104; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.012, surface_pool_high +0.013, surface_dev_loose -0.016, surface_dev_tight +0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Victoria Brand vs Daria Barsukov -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21BRABAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daria Barsukov (`KXITFWMATCH-26OCT21BRABAR-BAR`) | 0.03 / 0.04 (424) | 3.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Victoria Brand (`KXITFWMATCH-26OCT21BRABAR-BRA`) | 0.96 / 0.98 (858) | 97.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofya Lansere vs Elsa Jacquemot -- W100 Wrexham R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216139:221039:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elsa Jacquemot (`KXITFWMATCH-26OCT21LANJAC-JAC`) | 0.93 / 0.94 (2305) | 93.5% | 61.5% | 39.9% | 51.6% [46.3%-64.1%] | 68.1% | -- | 68.1% | MODEL_LONE_OUTLIER | PASS | -32.0 pp | EXTREME (DATA_WARNING) | AGING | A / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Sofya Lansere (`KXITFWMATCH-26OCT21LANJAC-LAN`) | 0.05 / 0.06 (6) | 5.5% | 38.5% | 60.1% | 48.4% [35.9%-53.7%] | 31.9% | -- | 31.9% | KALSHI_LONE_OUTLIER | WATCH | +33.0 pp | EXTREME (DATA_WARNING) | AGING | A / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 3253.0, B 4592.0; serve-point win A 51.3%, B 46.5%; Elo A 1594.9, B 1779.0; model uncertainty 0.0894
* Form inputs: days since last match A 19, B 8; matches on record A 351, B 402; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21LANJAC-LAN  (YES = Sofya Lansere)
Model: 38%
Kalshi: 6%
Gap: +33 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: SUPPORTS_MODEL_DIRECTION
Data quality: A (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LEVEL_TRANSFER_RISK, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elena Malygina vs Susan Bandecchi -- W100 Wrexham R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214826:216116:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Susan Bandecchi (`KXITFWMATCH-26OCT21MALBAN-BAN`) | 0.80 / 0.81 (4109) | 80.5% | 68.9% | 35.5% | 49.5% [42.6%-63.5%] | 60.6% | -- | 60.6% | MODEL_LONE_OUTLIER | PASS | -11.6 pp | REVIEW | AGING | A / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Elena Malygina (`KXITFWMATCH-26OCT21MALBAN-MAL`) | 0.19 / 0.20 (4235) | 19.5% | 31.1% | 64.5% | 50.5% [36.5%-57.4%] | 39.4% | -- | 39.4% | MODEL_LONE_OUTLIER | WATCH | +11.6 pp | REVIEW | AGING | A / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 2298.0, B 3884.0; serve-point win A 53.5%, B 42.8%; Elo A 1689.5, B 1847.7; model uncertainty 0.1046
* Form inputs: days since last match A 26, B 9; matches on record A 440, B 525; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matej Dodig vs Marco Cecchinato -- ATP Challenger Lisbon R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-21T16:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106065:212063:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marco Cecchinato (`KXATPCHALLENGERMATCH-26OCT21DODCEC-CEC`) | 0.29 / 0.31 (6508) | 30.0% | 27.0% | 31.9% | 34.2% [32.4%-36.0%] | 30.3% | 30.3% | 30.3% | MODEL_LONE_OUTLIER | SHADOW_BET | -3.0 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Matej Dodig (`KXATPCHALLENGERMATCH-26OCT21DODCEC-DOD`) | 0.70 / 0.71 (13117) | 70.5% | 73.0% | 68.1% | 65.8% [64.0%-67.6%] | 69.7% | 69.7% | 69.7% | MODEL_LONE_OUTLIER | PASS | +2.5 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4026.0, B 4786.0; serve-point win A 67.3%, B 37.7%; Elo A 1754.4, B 1678.0; model uncertainty 0.0179
* Form inputs: days since last match A 9, B 9; matches on record A 219, B 954; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose +0.018, surface_dev_tight -0.018
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Alessandro Battiston vs Ramazan Kaan Oktay -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21BATOKT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alessandro Battiston (`KXITFMATCH-26OCT21BATOKT-BAT`) | 0.71 / 0.72 (2755) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ramazan Kaan Oktay (`KXITFMATCH-26OCT21BATOKT-OKT`) | 0.28 / 0.29 (2653) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Robin Bertrand vs Mario Arce Fernandez -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-21T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209850:213535:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mario Arce Fernandez (`KXITFMATCH-26OCT21BERARC-ARC`) | 0.07 / 0.09 (435) | 8.0% | 8.1% | 51.5% | 15.9% [13.2%-18.5%] | 10.4% | -- | 10.4% | MODEL_LONE_OUTLIER | PASS | +0.1 pp | NORMAL | AGING | F / POOR | ALL_AGREE | AMBIGUOUS |
| Robin Bertrand (`KXITFMATCH-26OCT21BERARC-BER`) | 0.90 / 0.92 (100) | 91.0% | 91.9% | 48.5% | 84.1% [81.5%-86.8%] | 89.6% | -- | 89.6% | KALSHI_LONE_OUTLIER | PASS | +0.9 pp | NORMAL | AGING | F / POOR | ALL_AGREE | AMBIGUOUS |

* Serve evidence (points): A 2130.0, B 0.0; serve-point win A 66.5%, B 44.5%; Elo A 1543.6, B 1250.4; model uncertainty 0.0264
* Form inputs: days since last match A 156, B 744; matches on record A 313, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.024, surface_pool_high -0.026, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gabriele Bosio vs Luis Carlos Alvarez Valdes -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-21T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208152:211468:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luis Carlos Alvarez Valdes (`KXITFMATCH-26OCT21BOSALV-ALV`) | 0.70 / 0.73 (39) | 71.5% | 56.9% | 67.9% | 57.2% [56.1%-58.2%] | 69.2% | -- | 69.2% | MODEL_LONE_OUTLIER | PASS | -14.6 pp | REVIEW | AGING | F / POOR | AGREES_WITH_KALSHI | AMBIGUOUS |
| Gabriele Bosio (`KXITFMATCH-26OCT21BOSALV-BOS`) | 0.25 / 0.28 (34) | 26.5% | 43.1% | 32.1% | 42.8% [41.8%-43.9%] | 30.8% | -- | 30.8% | KALSHI_LONE_OUTLIER | PASS | +16.6 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | AGREES_WITH_KALSHI | AMBIGUOUS |

* Serve evidence (points): A 128.0, B 0.0; serve-point win A 59.8%, B 38.9%; Elo A 1260.5, B 1307.7; model uncertainty 0.0108
* Form inputs: days since last match A 765, B 730; matches on record A 131, B 27; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21BOSALV-BOS  (YES = Gabriele Bosio)
Model: 43%
Kalshi: 26%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maxi Carrascosa Diaz vs Fnu Nidunjianzan -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21CARNID:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maxi Carrascosa Diaz (`KXITFMATCH-26OCT21CARNID-CAR`) | 0.19 / 0.21 (2184) | 20.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fnu Nidunjianzan (`KXITFMATCH-26OCT21CARNID-NID`) | 0.79 / 0.80 (261) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Despotovic / Jutresa vs Miletich / Todoran -- M15 Bol R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21DESJUTMILTOD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Despotovic / Jutresa (`KXITFDOUBLES-26OCT21DESJUTMILTOD-DESJUT`) | 0.05 / 0.95 (38) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Miletich / Todoran (`KXITFDOUBLES-26OCT21DESJUTMILTOD-MILTOD`) | 0.06 / 0.95 (38) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Nikola Djukic Valera vs Tim Hammes -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21DJUHAM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikola Djukic Valera (`KXITFMATCH-26OCT21DJUHAM-DJU`) | 0.51 / 0.55 (22) | 53.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tim Hammes (`KXITFMATCH-26OCT21DJUHAM-HAM`) | 0.45 / 0.47 (1) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Galus / Homola vs Mavracic / Zuberbuehler -- M15 Bol R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21GALHOMMAVZUB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Galus / Homola (`KXITFDOUBLES-26OCT21GALHOMMAVZUB-GALHOM`) | 0.05 / 0.95 (38) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mavracic / Zuberbuehler (`KXITFDOUBLES-26OCT21GALHOMMAVZUB-MAVZUB`) | 0.05 / 0.92 (28) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Aljaz Jeran vs Alessio Basile -- M15 Bol R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211334:211450:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alessio Basile (`KXITFMATCH-26OCT21JERBAS-BAS`) | 0.55 / 0.58 (59) | 56.5% | 75.1% | 50.0% | 69.5% [69.5%-69.5%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +18.6 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Aljaz Jeran (`KXITFMATCH-26OCT21JERBAS-JER`) | 0.39 / 0.45 (2) | 42.0% | 24.9% | 50.0% | 30.6% [30.6%-30.6%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -17.1 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 59.3%, B 35.4%; Elo A 1095.0, B 1236.3; model uncertainty 0.0
* Form inputs: days since last match A 786, B 793; matches on record A 11, B 23; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21JERBAS-BAS  (YES = Alessio Basile)
Model: 75%
Kalshi: 56%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jannik Maute vs John Bothma -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210339:213011:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| John Bothma (`KXITFMATCH-26OCT21MAUBOT-BOT`) | 0.34 / 0.73 (1) | 53.5% | 66.7% | 58.0% | 67.5% [67.4%-67.6%] | -- | -- | -- | -- | PASS | +13.2 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Jannik Maute (`KXITFMATCH-26OCT21MAUBOT-MAU`) | 0.43 / 0.69 (2) | 56.0% | 33.3% | 42.0% | 32.5% [32.4%-32.6%] | -- | -- | -- | -- | PASS | -22.7 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 63.0, B 0.0; serve-point win A 61.2%, B 35.4%; Elo A 1166.9, B 1295.0; model uncertainty 0.0012
* Form inputs: days since last match A 800, B 842; matches on record A 26, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rihards Neimanis vs Oskari Paldanius -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21NEIPAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rihards Neimanis (`KXITFMATCH-26OCT21NEIPAL-NEI`) | 0.32 / 0.33 (1) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Oskari Paldanius (`KXITFMATCH-26OCT21NEIPAL-PAL`) | 0.66 / 0.67 (2358) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marko Nikolic vs Ivan Biletic -- M15 Bol R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:149141:212919:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ivan Biletic (`KXITFMATCH-26OCT21NIKBIL-BIL`) | 0.62 / 0.63 (92) | 62.5% | 52.8% | 64.0% | 51.0% [51.0%-51.0%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Marko Nikolic (`KXITFMATCH-26OCT21NIKBIL-NIK`) | 0.33 / 0.39 (2) | 36.0% | 47.2% | 36.0% | 49.0% [49.0%-49.0%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +11.2 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 48.0, B 0.0; serve-point win A 61.1%, B 38.4%; Elo A 1247.8, B 1254.8; model uncertainty 0.0
* Form inputs: days since last match A 877, B 877; matches on record A 4, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rocco Piatti vs Kylian Collignon -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-21T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211497:212262:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kylian Collignon (`KXITFMATCH-26OCT21PIACOL-COL`) | 0.29 / 0.32 (49) | 30.5% | 51.8% | 73.9% | 59.1% [59.1%-60.1%] | 28.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +21.3 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rocco Piatti (`KXITFMATCH-26OCT21PIACOL-PIA`) | 0.70 / 0.71 (8) | 70.5% | 48.2% | 26.1% | 40.9% [39.9%-40.9%] | 71.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -22.3 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 160.0, B 0.0; serve-point win A 61.1%, B 38.6%; Elo A 1086.6, B 1154.8; model uncertainty 0.0051
* Form inputs: days since last match A 730, B 695; matches on record A 29, B 17; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21PIACOL-COL  (YES = Kylian Collignon)
Model: 52%
Kalshi: 30%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ruslan Tiukaev vs Melih Anavatan -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211700:212903:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Melih Anavatan (`KXITFMATCH-26OCT21TIUANA-ANA`) | 0.31 / 0.50 (1) | 40.5% | 43.2% | 50.0% | 49.0% [49.0%-50.0%] | -- | -- | -- | -- | PASS | +2.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Ruslan Tiukaev (`KXITFMATCH-26OCT21TIUANA-TIU`) | 0.57 / 0.59 (4) | 58.0% | 56.8% | 50.0% | 51.0% [50.0%-51.0%] | -- | -- | -- | -- | PASS | -1.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 62.7%, B 38.7%; Elo A 1254.4, B 1250.6; model uncertainty 0.0051
* Form inputs: days since last match A 681, B 891; matches on record A 18, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eero Vasa vs Matteo Gribaldo -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21VASGRI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Gribaldo (`KXITFMATCH-26OCT21VASGRI-GRI`) | 0.19 / 0.22 (2) | 20.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eero Vasa (`KXITFMATCH-26OCT21VASGRI-VAS`) | 0.77 / 0.79 (53) | 78.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Victor Chelemen / Lacis vs Bielinskyi / Simundza -- M15 Bol R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21VICLACBIESIM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bielinskyi / Simundza (`KXITFDOUBLES-26OCT21VICLACBIESIM-BIESIM`) | 0.08 / 0.95 (38) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Victor Chelemen / Lacis (`KXITFDOUBLES-26OCT21VICLACBIESIM-VICLAC`) | 0.05 / 0.95 (40) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Vaishnavi Adkar vs Anna Shkutova -- W35 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-21T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:261038:270216:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vaishnavi Adkar (`KXITFWMATCH-26OCT21ADKSHK-ADK`) | 0.91 / 0.93 (5) | 92.0% | 91.4% | 76.1% | 80.8% [79.7%-81.5%] | 89.6% | -- | 89.6% | KALSHI_LONE_OUTLIER | PASS | -0.6 pp | NORMAL | AGING | D / POOR | ALL_AGREE | VERIFIED |
| Anna Shkutova (`KXITFWMATCH-26OCT21ADKSHK-SHK`) | 0.04 / 0.09 (7) | 6.5% | 8.6% | 23.9% | 19.2% [18.5%-20.3%] | 10.4% | -- | 10.4% | KALSHI_LONE_OUTLIER | PASS | +2.1 pp | NORMAL | AGING | D / POOR | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 2186.0, B 401.0; serve-point win A 57.7%, B 52.6%; Elo A 1514.8, B 1257.4; model uncertainty 0.0093
* Form inputs: days since last match A 177, B 177; matches on record A 143, B 9; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.011, surface_dev_loose -0.004, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mariia Drobysheva vs Sapfo Sakellaridi -- W15 Bol R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220364:261061:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mariia Drobysheva (`KXITFWMATCH-26OCT21DROSAK-DRO`) | 0.24 / 0.25 (33) | 24.5% | 13.8% | 18.2% | 26.8% [21.5%-32.7%] | 27.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -10.7 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sapfo Sakellaridi (`KXITFWMATCH-26OCT21DROSAK-SAK`) | 0.71 / 0.75 (232) | 73.0% | 86.2% | 81.8% | 73.2% [67.3%-78.5%] | 72.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.2 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 310.0, B 4165.0; serve-point win A 52.9%, B 38.8%; Elo A 1273.3, B 1432.1; model uncertainty 0.0562
* Form inputs: days since last match A 387, B 10; matches on record A 7, B 704; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.053, surface_pool_high +0.059, surface_dev_loose -0.004, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alicia Dudeney vs Tessa Johanna Brockmann -- W100 Wrexham R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260206:260598:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tessa Johanna Brockmann (`KXITFWMATCH-26OCT21DUDBRO-BRO`) | 0.01 / 0.02 (4878) | 1.5% | 46.5% | 26.6% | 36.5% [31.1%-50.5%] | 34.8% | -- | 34.8% | KALSHI_LONE_OUTLIER | WATCH | +45.0 pp | EXTREME (DATA_WARNING) | AGING | A / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Alicia Dudeney (`KXITFWMATCH-26OCT21DUDBRO-DUD`) | 0.98 / 0.99 (54) | 98.5% | 53.5% | 73.4% | 63.5% [49.5%-68.8%] | 65.2% | -- | 65.2% | KALSHI_LONE_OUTLIER | PASS | -45.0 pp | EXTREME (DATA_WARNING) | AGING | A / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 3238.0, B 3426.0; serve-point win A 55.7%, B 45.0%; Elo A 1651.5, B 1727.2; model uncertainty 0.0969
* Form inputs: days since last match A 13, B 8; matches on record A 94, B 169; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21DUDBRO-BRO  (YES = Tessa Johanna Brockmann)
Model: 47%
Kalshi: 2%
Gap: +45 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: SUPPORTS_MODEL_DIRECTION
Data quality: A (LIMITED)
Reasons: LEVEL_TRANSFER_RISK, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniela Darta Feldmane vs Joy De Zeeuw -- W35 Loule R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260159:260226:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joy De Zeeuw (`KXITFWMATCH-26OCT21FELDEZ-DEZ`) | 0.98 / 0.99 (806) | 98.5% | 78.3% | 58.4% | 69.3% [66.9%-72.6%] | 82.2% | -- | 82.2% | MODEL_LONE_OUTLIER | PASS | -20.2 pp | HIGH_REVIEW | AGING | D / POOR | AGREES_WITH_MODEL | VERIFIED |
| Daniela Darta Feldmane (`KXITFWMATCH-26OCT21FELDEZ-FEL`) | 0.01 / 0.02 (1104) | 1.5% | 21.7% | 41.6% | 30.7% [27.4%-33.1%] | 17.8% | -- | 17.8% | MODEL_LONE_OUTLIER | PASS | +20.2 pp | HIGH_REVIEW | AGING | D / POOR | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 630.0, B 2042.0; serve-point win A 53.0%, B 41.1%; Elo A 1226.1, B 1406.8; model uncertainty 0.0283
* Form inputs: days since last match A 282, B 387; matches on record A 20, B 70; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21FELDEZ-FEL  (YES = Daniela Darta Feldmane)
Model: 22%
Kalshi: 2%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_MODEL
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.009, surface_dev_loose -0.004, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anastasia Gasanova vs Maaya Rajeshwaran Revathi -- W35 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-21T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214181:266722:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasia Gasanova (`KXITFWMATCH-26OCT21GASRAJ-GAS`) | 0.87 / 0.89 (288) | 88.0% | 87.7% | 88.9% | 83.3% [79.0%-87.0%] | 76.8% | -- | 76.8% | ALL_THREE_DISAGREE | PASS | -0.3 pp | NORMAL | AGING | D / POOR | EXTERNAL_OUTLIER | VERIFIED |
| Maaya Rajeshwaran Revathi (`KXITFWMATCH-26OCT21GASRAJ-RAJ`) | 0.11 / 0.12 (1) | 11.5% | 12.3% | 11.1% | 16.7% [13.0%-21.0%] | 23.2% | -- | 23.2% | ALL_THREE_DISAGREE | PASS | +0.8 pp | NORMAL | AGING | D / POOR | EXTERNAL_OUTLIER | VERIFIED |

* Serve evidence (points): A 3279.0, B 796.0; serve-point win A 55.8%, B 52.8%; Elo A 1679.0, B 1442.7; model uncertainty 0.0401
* Form inputs: days since last match A 23, B 247; matches on record A 502, B 23; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.037, surface_pool_high -0.043, surface_dev_loose -0.000, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Iva Ivanovic vs Maria Garcia Cid -- W35 Santa Margherita di Pula R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-21T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:225850:266569:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Garcia Cid (`KXITFWMATCH-26OCT21IVAGAR-GAR`) | 0.95 / 0.97 (110) | 96.0% | 99.0% | 94.1% | 91.0% [89.9%-91.9%] | 93.7% | -- | 93.7% | KALSHI_LONE_OUTLIER | PASS | +3.0 pp | NORMAL | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Iva Ivanovic (`KXITFWMATCH-26OCT21IVAGAR-IVA`) | 0.03 / 0.04 (16) | 3.5% | 1.0% | 5.9% | 9.0% [8.1%-10.1%] | 6.3% | -- | 6.3% | KALSHI_LONE_OUTLIER | PASS | -2.5 pp | NORMAL | AGING | D / POOR | EXTERNAL_OUTLIER | VERIFIED |

* Serve evidence (points): A 274.0, B 1857.0; serve-point win A 45.9%, B 36.5%; Elo A 1163.3, B 1548.4; model uncertainty 0.0097
* Form inputs: days since last match A 184, B 9; matches on record A 9, B 87; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.011, surface_dev_loose -0.004, surface_dev_tight +0.002
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Min Liu vs Federica Urgesi -- W35 Loule R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206205:223415:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Min Liu (`KXITFWMATCH-26OCT21LIUURG-LIU`) | 0.01 / 0.02 (42) | 1.5% | 2.4% | 4.2% | 7.1% [5.7%-9.5%] | -- | -- | -- | -- | PASS | +0.9 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Federica Urgesi (`KXITFWMATCH-26OCT21LIUURG-URG`) | 0.98 / 0.99 (3757) | 98.5% | 97.6% | 95.8% | 92.9% [90.5%-94.3%] | -- | -- | -- | -- | PASS | -0.9 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 746.0, B 2635.0; serve-point win A 48.7%, B 36.3%; Elo A 1192.3, B 1586.9; model uncertainty 0.0189
* Form inputs: days since last match A 129, B 30; matches on record A 143, B 169; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.015, surface_dev_loose -0.006, surface_dev_tight +0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Victoria Milovanova vs Anna Kubareva -- W35 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-21T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215707:269870:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Kubareva (`KXITFWMATCH-26OCT21MILKUB-KUB`) | 0.15 / 0.23 (3746) | 19.0% | 33.2% | 57.4% | 46.8% [40.5%-50.5%] | 51.9% | -- | 51.9% | KALSHI_LONE_OUTLIER | PASS | +14.2 pp | REVIEW | AGING | C / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Victoria Milovanova (`KXITFWMATCH-26OCT21MILKUB-MIL`) | 0.77 / 0.81 (167) | 79.0% | 66.8% | 42.6% | 53.2% [49.5%-59.5%] | 48.1% | -- | 48.1% | MODEL_LONE_OUTLIER | WATCH | -12.2 pp | REVIEW | AGING | C / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 2145.0, B 2121.0; serve-point win A 55.2%, B 48.0%; Elo A 1535.9, B 1409.0; model uncertainty 0.0502
* Form inputs: days since last match A 198, B 198; matches on record A 54, B 345; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.026, surface_dev_loose -0.016, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nguyen Tan / Yesypchuk vs Gennaro / Mariani -- W35 Santa Margherita di Pula QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21NGUYESGENMAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gennaro / Mariani (`KXITFWDOUBLES-26OCT21NGUYESGENMAR-GENMAR`) | 0.10 / 0.73 (32) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nguyen Tan / Yesypchuk (`KXITFWDOUBLES-26OCT21NGUYESGENMAR-NGUYES`) | 0.05 / 0.88 (208) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Laia Petretic vs Madalena Matias -- W35 Loule R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222346:270133:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Madalena Matias (`KXITFWMATCH-26OCT21PETMAT-MAT`) | 0.01 / 0.02 (610) | 1.5% | 18.7% | 5.1% | 22.6% [17.4%-26.8%] | 8.5% | -- | 8.5% | KALSHI_LONE_OUTLIER | PASS | +17.2 pp | HIGH_REVIEW | AGING | D / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Laia Petretic (`KXITFWMATCH-26OCT21PETMAT-PET`) | 0.97 / 0.98 (9) | 97.5% | 81.3% | 94.9% | 77.4% [73.2%-82.6%] | 91.5% | -- | 91.5% | KALSHI_LONE_OUTLIER | PASS | -16.2 pp | HIGH_REVIEW | AGING | D / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 1964.0, B 252.0; serve-point win A 54.1%, B 52.5%; Elo A 1409.9, B 1235.9; model uncertainty 0.0474
* Form inputs: days since last match A 177, B 8; matches on record A 203, B 9; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21PETMAT-MAT  (YES = Madalena Matias)
Model: 19%
Kalshi: 2%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: SUPPORTS_MODEL_DIRECTION
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.021, surface_dev_loose +0.012, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chen Yun Tsai vs Carlotta Moccia -- W35 Loule R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21TSAMOC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlotta Moccia (`KXITFWMATCH-26OCT21TSAMOC-MOC`) | 0.87 / 0.88 (304) | 87.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Chen Yun Tsai (`KXITFWMATCH-26OCT21TSAMOC-TSA`) | 0.11 / 0.12 (31) | 11.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Baotong Xu vs Teodora Miron -- W35 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21XUXMIR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Teodora Miron (`KXITFWMATCH-26OCT21XUXMIR-MIR`) | 0.78 / 0.88 (92) | 83.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Baotong Xu (`KXITFWMATCH-26OCT21XUXMIR-XUX`) | 0.12 / 0.19 (22) | 15.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Beatrise Zeltina vs Ane Mintegi Del Olmo -- W35 Santa Margherita di Pula R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-21T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221213:260339:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ane Mintegi Del Olmo (`KXITFWMATCH-26OCT21ZELMIN-MIN`) | 0.81 / 0.91 (1) | 86.0% | 73.2% | 64.1% | 69.0% [67.6%-70.9%] | 80.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.8 pp | REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Beatrise Zeltina (`KXITFWMATCH-26OCT21ZELMIN-ZEL`) | 0.15 / 0.18 (31) | 16.5% | 26.8% | 35.9% | 31.0% [29.1%-32.4%] | 19.5% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +10.3 pp | REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1940.0, B 2133.0; serve-point win A 49.9%, B 45.5%; Elo A 1523.4, B 1712.1; model uncertainty 0.0165
* Form inputs: days since last match A 191, B 5; matches on record A 64, B 167; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.005, surface_dev_loose +0.005, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Moise Kouame vs Lorenzo Musetti -- ATP Lyon R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-21 13:00Z
* Current expected start: 2026-10-21 17:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-21 16:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+240_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Clay · scheduled 2026-10-21T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207518:213608:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Moise Kouame (`KXATPMATCH-26OCT21KOUMUS-KOU`) | 0.22 / 0.23 (3735) | 22.5% | 10.5% | 13.5% | 7.9% [6.0%-9.7%] | 24.5% | 23.0% | 23.8% | MODEL_LONE_OUTLIER | PASS | -12.0 pp | REVIEW | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Lorenzo Musetti (`KXATPMATCH-26OCT21KOUMUS-MUS`) | 0.76 / 0.77 (1006) | 76.5% | 89.5% | 86.6% | 92.1% [90.3%-94.0%] | 75.5% | 76.7% | 76.1% | MODEL_LONE_OUTLIER | SHADOW_BET | +13.0 pp | REVIEW | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1672.0, B 4401.0; serve-point win A 55.6%, B 34.6%; Elo A 1553.8, B 2103.7; model uncertainty 0.0187
* Form inputs: days since last match A 2, B 2; matches on record A 36, B 467; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.008, surface_dev_loose -0.004, surface_dev_tight +0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT21KOUMUS-MUS2` Will Lorenzo Musetti win at least 1.5 more games than Moise Kouame?: 0.70/0.72 mid 71.0%, model 86.2% (projection_v2.0 (prediction ledger)) -- gap +15.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data LIMITED
  * `KXATPGSPREAD-26OCT21KOUMUS-MUS5` Will Lorenzo Musetti win at least 4.5 more games than Moise Kouame?: 0.45/0.47 mid 46.0%, model 58.4% (projection_v2.0 (prediction ledger)) -- gap +12.4 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data LIMITED
  * `KXATPEXACTMATCH-26OCT21KOUMUS-MUS20` Will Lorenzo Musetti win the Moise Kouame vs Lorenzo Musetti match by a set score of 2-0?: 0.53/0.54 mid 53.5%, model 63.9% (projection_v2.0 (prediction ledger)) -- gap +10.4 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data LIMITED
  * `KXATPSETWINNER-26OCT21KOUMUS-1-KOU` Will Moise Kouame win set 1 in the Moise Kouame vs Lorenzo Musetti match: 0.29/0.31 mid 30.0%, model 20.1% (projection_v2.0 (prediction ledger)) -- gap -9.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT21KOUMUS-1-MUS` Will Lorenzo Musetti win set 1 in the Moise Kouame vs Lorenzo Musetti match: 0.69/0.71 mid 70.0%, model 79.9% (projection_v2.0 (prediction ledger)) -- gap +9.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT21KOUMUS-2-MUS` Will Lorenzo Musetti win set 2 in the Moise Kouame vs Lorenzo Musetti match: 0.69/0.72 mid 70.5%, model 79.9% (projection_v2.0 (prediction ledger)) -- gap +9.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT21KOUMUS-2-KOU` Will Moise Kouame win set 2 in the Moise Kouame vs Lorenzo Musetti match: 0.26/0.31 mid 28.5%, model 20.1% (projection_v2.0 (prediction ledger)) -- gap -8.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXATPEXACTMATCH-26OCT21KOUMUS-KOU20` Will Moise Kouame win the Moise Kouame vs Lorenzo Musetti match by a set score of 2-0?: 0.10/0.12 mid 11.0%, model 4.0% (projection_v2.0 (prediction ledger)) -- gap -7.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
  * `KXATPEXACTMATCH-26OCT21KOUMUS-KOU21` Will Moise Kouame win the Moise Kouame vs Lorenzo Musetti match by a set score of 2-1?: 0.10/0.13 mid 11.5%, model 6.4% (projection_v2.0 (prediction ledger)) -- gap -5.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
  * `KXATPGTOTAL-26OCT21KOUMUS-17` Over 16.5 games: 0.88/0.94 mid 91.0%, model 86.8% (projection_v2.0 (prediction ledger)) -- gap -4.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
  * `KXATPEXACTMATCH-26OCT21KOUMUS-MUS21` Will Lorenzo Musetti win the Moise Kouame vs Lorenzo Musetti match by a set score of 2-1?: 0.20/0.24 mid 22.0%, model 25.6% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
  * `KXATPGSPREAD-26OCT21KOUMUS-MUS8` Will Lorenzo Musetti win at least 7.5 more games than Moise Kouame?: 0.03/0.32 mid 17.5%, model 14.4% (projection_v2.0 (prediction ledger)) -- gap -3.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
  * `KXATPGTOTAL-26OCT21KOUMUS-27` Over 26.5 games: 0.26/0.29 mid 27.5%, model 25.2% (projection_v2.0 (prediction ledger)) -- gap -2.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
  * `KXATPGTOTAL-26OCT21KOUMUS-22` Over 21.5 games: 0.46/0.47 mid 46.5%, model 44.7% (projection_v2.0 (prediction ledger)) -- gap -1.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; WIDE_SPREAD

## Caripi / Elamin vs Gschwendtner / Valle -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21CARELAGSCVAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Caripi / Elamin (`KXITFDOUBLES-26OCT21CARELAGSCVAL-CARELA`) | 0.03 / 0.45 (45) | 24.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gschwendtner / Valle (`KXITFDOUBLES-26OCT21CARELAGSCVAL-GSCVAL`) | 0.55 / 0.66 (56) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Car / Pietri vs Kountourakis / Tsitsipas -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21CARPIEKOUTSI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Car / Pietri (`KXITFDOUBLES-26OCT21CARPIEKOUTSI-CARPIE`) | 0.02 / 0.92 (1) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kountourakis / Tsitsipas (`KXITFDOUBLES-26OCT21CARPIEKOUTSI-KOUTSI`) | 0.02 / 0.69 (1) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jake Evans vs Oliver Tarvet -- M25 Redbridge R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21EVATAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jake Evans (`KXITFMATCH-26OCT21EVATAR-EVA`) | 0.01 / 0.02 (54265) | 1.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Oliver Tarvet (`KXITFMATCH-26OCT21EVATAR-TAR`) | 0.98 / 0.99 (4215) | 98.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Conor Gannon vs George Loffhagen -- M25 Redbridge R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:149843:207785:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Conor Gannon (`KXITFMATCH-26OCT21GANLOF-GAN`) | 0.06 / 0.11 (279) | 8.5% | 12.2% | 24.1% | 15.8% [15.1%-16.4%] | 8.5% | -- | 8.5% | KALSHI_LONE_OUTLIER | PASS | +3.7 pp | NORMAL | AGING | D / POOR | ALL_AGREE | VERIFIED |
| George Loffhagen (`KXITFMATCH-26OCT21GANLOF-LOF`) | 0.91 / 0.93 (5) | 92.0% | 87.8% | 75.9% | 84.2% [83.6%-84.9%] | 91.5% | -- | 91.5% | MODEL_LONE_OUTLIER | PASS | -4.2 pp | NORMAL | AGING | D / POOR | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 188.0, B 1163.0; serve-point win A 58.8%, B 31.9%; Elo A 1321.6, B 1626.3; model uncertainty 0.0066
* Form inputs: days since last match A 128, B 9; matches on record A 16, B 204; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Geenen / Sels vs Vijay Sundar Prashanth / Sharan -- M25 Redbridge QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21GEESELVIJSHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Geenen / Sels (`KXITFDOUBLES-26OCT21GEESELVIJSHA-GEESEL`) | 0.16 / 0.77 (1) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vijay Sundar Prashanth / Sharan (`KXITFDOUBLES-26OCT21GEESELVIJSHA-VIJSHA`) | 0.01 / 0.84 (1) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Chytilova / Drozdz vs Pulchartova / Wirges -- W15 Karlovy Vary QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21CHYDROPULWIR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chytilova / Drozdz (`KXITFWDOUBLES-26OCT21CHYDROPULWIR-CHYDRO`) | -- / 0.02 (336) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pulchartova / Wirges (`KXITFWDOUBLES-26OCT21CHYDROPULWIR-PULWIR`) | 0.98 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE

## Dore / Levicki vs Paredes Perez / Ros Parres -- W15 Villena QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21DORLEVPARROS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dore / Levicki (`KXITFWDOUBLES-26OCT21DORLEVPARROS-DORLEV`) | 0.01 / 0.99 (812) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Paredes Perez / Ros Parres (`KXITFWDOUBLES-26OCT21DORLEVPARROS-PARROS`) | 0.01 / 0.99 (61) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Ana Giraldi Requena vs Zi Ying Ruan -- W15 Villena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216198:267462:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ana Giraldi Requena (`KXITFWMATCH-26OCT21GIRRUA-GIR`) | 0.37 / 0.44 (3) | 40.5% | 49.4% | 46.2% | 44.6% [43.1%-46.8%] | 32.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +8.9 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zi Ying Ruan (`KXITFWMATCH-26OCT21GIRRUA-RUA`) | 0.58 / 0.66 (13) | 62.0% | 50.6% | 53.8% | 55.4% [53.2%-56.9%] | 67.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.4 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 883.0, B 832.0; serve-point win A 50.0%, B 49.9%; Elo A 1269.3, B 1312.8; model uncertainty 0.0187
* Form inputs: days since last match A 338, B 310; matches on record A 195, B 48; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.011, surface_dev_loose +0.011, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Isabel Pascual Montalvo vs Maria Andrienko -- W15 Villena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221515:240161:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Andrienko (`KXITFWMATCH-26OCT21PASAND-AND`) | 0.80 / 0.85 (1) | 82.5% | 83.0% | 67.1% | 71.3% [70.4%-72.3%] | 80.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.5 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Isabel Pascual Montalvo (`KXITFWMATCH-26OCT21PASAND-PAS`) | 0.05 / 0.20 (1) | 12.5% | 17.0% | 32.9% | 28.7% [27.7%-29.6%] | 19.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.5 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 207.0, B 611.0; serve-point win A 48.9%, B 44.0%; Elo A 1221.7, B 1387.8; model uncertainty 0.0092
* Form inputs: days since last match A 331, B 429; matches on record A 25, B 149; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Emma Slavikova vs Ella Haavisto -- W15 Karlovy Vary R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216107:239126:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ella Haavisto (`KXITFWMATCH-26OCT21SLAHAA-HAA`) | 0.75 / 0.77 (90) | 76.0% | 69.5% | 50.0% | 63.6% [59.6%-69.5%] | 63.8% | -- | 63.8% | MARKETS_AGREE | PASS | -6.5 pp | NORMAL | AGING | C / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Emma Slavikova (`KXITFWMATCH-26OCT21SLAHAA-SLA`) | 0.23 / 0.24 (16) | 23.5% | 30.6% | 50.0% | 36.4% [30.5%-40.5%] | 36.2% | -- | 36.2% | MARKETS_AGREE | PASS | +7.0 pp | NORMAL | AGING | C / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 1128.0, B 1672.0; serve-point win A 50.1%, B 46.1%; Elo A 1315.8, B 1485.3; model uncertainty 0.0496
* Form inputs: days since last match A 177, B 233; matches on record A 137, B 139; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pavla Sviglerova vs Selina Dal -- W15 Karlovy Vary R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21SVIDAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Selina Dal (`KXITFWMATCH-26OCT21SVIDAL-DAL`) | 0.77 / 0.83 (2) | 80.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pavla Sviglerova (`KXITFWMATCH-26OCT21SVIDAL-SVI`) | 0.09 / 0.23 (1) | 16.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lian Tran vs Sara Cakarevic -- W50 Cherbourg-en-Cotentin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214319:220560:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Cakarevic (`KXITFWMATCH-26OCT21TRACAK-CAK`) | 0.01 / 0.02 (94) | 1.5% | 45.9% | 62.6% | 52.1% [47.9%-55.8%] | 59.9% | -- | 59.9% | MODEL_LONE_OUTLIER | WATCH | +44.4 pp | EXTREME (DATA_WARNING) | AGING | B / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Lian Tran (`KXITFWMATCH-26OCT21TRACAK-TRA`) | 0.97 / 0.99 (8937) | 98.0% | 54.1% | 37.4% | 47.9% [44.2%-52.1%] | 40.1% | -- | 40.1% | KALSHI_LONE_OUTLIER | PASS | -43.9 pp | EXTREME (DATA_WARNING) | AGING | B / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 1204.0, B 1791.0; serve-point win A 54.6%, B 46.2%; Elo A 1505.4, B 1460.0; model uncertainty 0.0399
* Form inputs: days since last match A 177, B 9; matches on record A 307, B 475; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21TRACAK-CAK  (YES = Sara Cakarevic)
Model: 46%
Kalshi: 2%
Gap: +44 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: SUPPORTS_MODEL_DIRECTION
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.032, surface_pool_high +0.032, surface_dev_loose -0.011, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marco Trungelliti vs Carlo Alberto Caniato -- ATP Challenger Lisbon R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 17:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-21T17:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105477:212241:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlo Alberto Caniato (`KXATPCHALLENGERMATCH-26OCT21TRUCAN-CAN`) | 0.38 / 0.39 (581) | 38.5% | 31.2% | 48.0% | 29.7% [21.6%-37.4%] | 39.1% | 38.8% | 38.9% | MODEL_LONE_OUTLIER | PASS | -7.3 pp | NORMAL | AGING | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Marco Trungelliti (`KXATPCHALLENGERMATCH-26OCT21TRUCAN-TRU`) | 0.60 / 0.61 (558) | 60.5% | 68.8% | 52.0% | 70.3% [62.6%-78.4%] | 60.9% | 61.8% | 61.3% | MODEL_LONE_OUTLIER | WATCH | +8.3 pp | NORMAL | AGING | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4942.0, B 1591.0; serve-point win A 66.6%, B 37.4%; Elo A 1773.3, B 1469.8; model uncertainty 0.0789
* Form inputs: days since last match A 9, B 9; matches on record A 987, B 90; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.017, surface_pool_high -0.017, surface_dev_loose -0.009, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Gauthier Onclin vs Jan-Lennard Struff -- ATP Brussels R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-21 20:10Z
* Current expected start: 2026-10-21 17:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-21 16:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-10-21T20:10:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105526:206904:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gauthier Onclin (`KXATPMATCH-26OCT21ONCSTR-ONC`) | 0.25 / 0.26 (9710) | 25.5% | 33.8% | 34.5% | 31.4% [25.4%-35.4%] | 25.5% | 25.8% | 25.7% | MODEL_LONE_OUTLIER | WATCH | +8.3 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Jan-Lennard Struff (`KXATPMATCH-26OCT21ONCSTR-STR`) | 0.75 / 0.76 (74811) | 75.5% | 66.2% | 65.5% | 68.6% [64.6%-74.6%] | 74.5% | 74.1% | 74.3% | MARKETS_AGREE | PASS | -9.3 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3146.0, B 4793.0; serve-point win A 62.5%, B 34.1%; Elo A 1597.8, B 1782.0; model uncertainty 0.0499
* Form inputs: days since last match A 3, B 1; matches on record A 409, B 1055; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.034, surface_pool_high +0.041, surface_dev_loose +0.010, surface_dev_tight -0.009
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT21ONCSTR-STR20` Will Jan-Lennard Struff win the Gauthier Onclin vs Jan-Lennard Struff match by a set score of 2-0?: 0.51/0.53 mid 52.0%, model 37.2% (projection_v2.0 (prediction ledger)) -- gap -14.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT21ONCSTR-27` Over 26.5 games: 0.27/0.31 mid 29.0%, model 42.6% (projection_v2.0 (prediction ledger)) -- gap +13.6 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT21ONCSTR-STR8` Will Jan-Lennard Struff win at least 7.5 more games than Gauthier Onclin?: 0.03/0.27 mid 15.0%, model 2.7% (projection_v2.0 (prediction ledger)) -- gap -12.3 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT21ONCSTR-STR5` Will Jan-Lennard Struff win at least 4.5 more games than Gauthier Onclin?: 0.37/0.38 mid 37.5%, model 25.9% (projection_v2.0 (prediction ledger)) -- gap -11.6 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT21ONCSTR-STR2` Will Jan-Lennard Struff win at least 1.5 more games than Gauthier Onclin?: 0.69/0.71 mid 70.0%, model 59.0% (projection_v2.0 (prediction ledger)) -- gap -11.0 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT21ONCSTR-22` Over 21.5 games: 0.57/0.58 mid 57.5%, model 67.5% (projection_v2.0 (prediction ledger)) -- gap +10.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT21ONCSTR-2-ONC` Will Gauthier Onclin win set 2 in the Gauthier Onclin vs Jan-Lennard Struff match: 0.27/0.32 mid 29.5%, model 39.0% (projection_v2.0 (prediction ledger)) -- gap +9.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT21ONCSTR-1-ONC` Will Gauthier Onclin win set 1 in the Gauthier Onclin vs Jan-Lennard Struff match: 0.29/0.32 mid 30.5%, model 39.0% (projection_v2.0 (prediction ledger)) -- gap +8.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT21ONCSTR-2-STR` Will Jan-Lennard Struff win set 2 in the Gauthier Onclin vs Jan-Lennard Struff match: 0.68/0.71 mid 69.5%, model 61.0% (projection_v2.0 (prediction ledger)) -- gap -8.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT21ONCSTR-1-STR` Will Jan-Lennard Struff win set 1 in the Gauthier Onclin vs Jan-Lennard Struff match: 0.67/0.70 mid 68.5%, model 61.0% (projection_v2.0 (prediction ledger)) -- gap -7.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21ONCSTR-ONC21` Will Gauthier Onclin win the Gauthier Onclin vs Jan-Lennard Struff match by a set score of 2-1?: 0.10/0.13 mid 11.5%, model 18.6% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21ONCSTR-STR21` Will Jan-Lennard Struff win the Gauthier Onclin vs Jan-Lennard Struff match by a set score of 2-1?: 0.21/0.25 mid 23.0%, model 29.0% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT21ONCSTR-17` Over 16.5 games: 0.92/0.95 mid 93.5%, model 97.1% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21ONCSTR-ONC20` Will Gauthier Onclin win the Gauthier Onclin vs Jan-Lennard Struff match by a set score of 2-0?: 0.11/0.13 mid 12.0%, model 15.2% (projection_v2.0 (prediction ledger)) -- gap +3.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Bajurko / GONCALVES FRANCA vs Chaurasia / Gatoto -- M25 Luanda R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21BAJGONCHAGAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bajurko / GONCALVES FRANCA (`KXITFDOUBLES-26OCT21BAJGONCHAGAT-BAJGON`) | 0.02 / 0.95 (2) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Chaurasia / Gatoto (`KXITFDOUBLES-26OCT21BAJGONCHAGAT-CHAGAT`) | 0.02 / 0.92 (1) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Martim Bernardo vs Nicolas Jadoun -- M25 Luanda R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21BERJAD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martim Bernardo (`KXITFMATCH-26OCT21BERJAD-BER`) | -- / 0.01 (6132) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nicolas Jadoun (`KXITFMATCH-26OCT21BERJAD-JAD`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## De Marchi / Mecarelli vs Spinolo / Stella -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21DEMMECSPISTE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| De Marchi / Mecarelli (`KXITFDOUBLES-26OCT21DEMMECSPISTE-DEMMEC`) | 0.05 / 0.92 (28) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Spinolo / Stella (`KXITFDOUBLES-26OCT21DEMMECSPISTE-SPISTE`) | 0.05 / 0.90 (8) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kivattsev / Lee Barr vs Cicma / Dessi -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21KIVLEECICDES:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cicma / Dessi (`KXITFDOUBLES-26OCT21KIVLEECICDES-CICDES`) | 0.27 / 0.46 (5) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kivattsev / Lee Barr (`KXITFDOUBLES-26OCT21KIVLEECICDES-KIVLEE`) | 0.29 / 0.78 (23) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Skvortcov / Tremblay vs Rodrigues / Makiesse Miguel Feijo Simao -- M25 Luanda R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21SKVTRERODMAK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rodrigues / Makiesse Miguel Feijo Simao (`KXITFDOUBLES-26OCT21SKVTRERODMAK-RODMAK`) | 0.05 / 0.46 (9) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Skvortcov / Tremblay (`KXITFDOUBLES-26OCT21SKVTRERODMAK-SKVTRE`) | 0.60 / 0.97 (27) | 78.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Boehner / Sziedat vs Sveva Fumagalli / Ye -- W35 Santa Margherita di Pula QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21BOESZISVEYEX:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Boehner / Sziedat (`KXITFWDOUBLES-26OCT21BOESZISVEYEX-BOESZI`) | 0.01 / 0.96 (16) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sveva Fumagalli / Ye (`KXITFWDOUBLES-26OCT21BOESZISVEYEX-SVEYEX`) | 0.06 / 0.91 (20) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Dessolis / Parentini Vallega Montebruno vs Bohrer Martins / Ezzat -- W35 Santa Margherita di Pula QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21DESPARBOHEZZ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bohrer Martins / Ezzat (`KXITFWDOUBLES-26OCT21DESPARBOHEZZ-BOHEZZ`) | 0.17 / 0.95 (78) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dessolis / Parentini Vallega Montebruno (`KXITFWDOUBLES-26OCT21DESPARBOHEZZ-DESPAR`) | 0.06 / 0.73 (2) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Feng / Li vs Maria Ciocan / Gardiner -- W50 Cherbourg-en-Cotentin QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21FENLIXMARGAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Feng / Li (`KXITFWDOUBLES-26OCT21FENLIXMARGAR-FENLIX`) | 0.96 / 0.98 (568) | 97.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maria Ciocan / Gardiner (`KXITFWDOUBLES-26OCT21FENLIXMARGAR-MARGAR`) | -- / 0.04 (7) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE

## Giambelli / Pedone vs Argyrokastriti / Cortez Llorca -- W35 Santa Margherita di Pula QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21GIAPEDARGCOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Argyrokastriti / Cortez Llorca (`KXITFWDOUBLES-26OCT21GIAPEDARGCOR-ARGCOR`) | 0.18 / 0.79 (12) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Giambelli / Pedone (`KXITFWDOUBLES-26OCT21GIAPEDARGCOR-GIAPED`) | 0.04 / 0.30 (36) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Milana Ivantsiv vs Carmen Gallardo Guevara -- W35 Loule R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222239:270481:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carmen Gallardo Guevara (`KXITFWMATCH-26OCT21IVAGAL-GAL`) | 0.95 / 0.97 (642) | 96.0% | 72.9% | 89.0% | 57.4% [55.3%-60.6%] | 93.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -23.1 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Milana Ivantsiv (`KXITFWMATCH-26OCT21IVAGAL-IVA`) | 0.04 / 0.06 (12) | 5.0% | 27.1% | 11.0% | 42.6% [39.5%-44.7%] | 6.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +22.1 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 64.0, B 1358.0; serve-point win A 51.7%, B 43.7%; Elo A 1375.7, B 1410.1; model uncertainty 0.0262
* Form inputs: days since last match A 8, B 177; matches on record A 3, B 48; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21IVAGAL-IVA  (YES = Milana Ivantsiv)
Model: 27%
Kalshi: 5%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carmen Lopez Martinez vs Sofia Iakukhina -- W35 Loule R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:225854:270379:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Iakukhina (`KXITFWMATCH-26OCT21LOPIAK-IAK`) | 0.20 / 0.23 (3) | 21.5% | 14.6% | 24.7% | 30.5% [29.5%-31.4%] | 24.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carmen Lopez Martinez (`KXITFWMATCH-26OCT21LOPIAK-LOP`) | 0.77 / 0.78 (42) | 77.5% | 85.4% | 75.3% | 69.5% [68.6%-70.5%] | 76.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1135.0, B 94.0; serve-point win A 55.7%, B 52.2%; Elo A 1394.4, B 1255.9; model uncertainty 0.0094
* Form inputs: days since last match A 129, B 331; matches on record A 147, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anna Siskova vs Alina Charaeva -- W100 Wrexham R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216074:221406:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alina Charaeva (`KXITFWMATCH-26OCT21SISCHA-CHA`) | 0.72 / 0.76 (66) | 74.0% | 71.6% | 33.5% | 46.8% [40.0%-62.6%] | 72.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.4 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anna Siskova (`KXITFWMATCH-26OCT21SISCHA-SIS`) | 0.25 / 0.28 (80) | 26.5% | 28.4% | 66.5% | 53.2% [37.4%-60.0%] | 27.6% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +1.9 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3067.0, B 3668.0; serve-point win A 52.5%, B 43.2%; Elo A 1717.9, B 1897.7; model uncertainty 0.1128
* Form inputs: days since last match A 8, B 8; matches on record A 435, B 330; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aran Teixido Garcia vs Polina Isakova -- W35 Loule R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21TEIISA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Isakova (`KXITFWMATCH-26OCT21TEIISA-ISA`) | 0.03 / 0.05 (94) | 4.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aran Teixido Garcia (`KXITFWMATCH-26OCT21TEIISA-TEI`) | 0.95 / 0.97 (39) | 96.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Fryer / McKay vs Blaydes / Hignett -- M25 Redbridge QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21FRYMCKBLAHIG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Blaydes / Hignett (`KXITFDOUBLES-26OCT21FRYMCKBLAHIG-BLAHIG`) | 0.02 / 0.90 (12) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fryer / McKay (`KXITFDOUBLES-26OCT21FRYMCKBLAHIG-FRYMCK`) | 0.01 / 0.95 (3) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Juan Manuel La Serna vs Juan Bautista Torres -- ATP Challenger Cali R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-21T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208913:210412:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Manuel La Serna (`KXATPCHALLENGERMATCH-26OCT21LATOR-LA`) | 0.58 / 0.59 (1037) | 58.5% | 33.9% | 31.6% | 33.1% [32.6%-38.6%] | 58.4% | 60.1% | 59.2% | MODEL_LONE_OUTLIER | PASS | -24.6 pp | HIGH_REVIEW | AGING | F / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Juan Bautista Torres (`KXATPCHALLENGERMATCH-26OCT21LATOR-TOR`) | 0.39 / 0.40 (2454) | 39.5% | 66.1% | 68.3% | 66.9% [61.4%-67.4%] | 41.6% | 40.3% | 41.0% | MODEL_LONE_OUTLIER | PASS | +26.6 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2366.0, B 4379.0; serve-point win A 54.2%, B 42.6%; Elo A 1551.0, B 1652.7; model uncertainty 0.0304
* Form inputs: days since last match A 9, B 695; matches on record A 142, B 274; data quality F

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT21LATOR-TOR  (YES = Juan Bautista Torres)
Model: 66%
Kalshi: 40%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Alan Magadan / Rodrigo Pacheco Mendez vs Mateo Del Pino / Manuel Mouilleron Salvo -- ATP Challenger Cali R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-21T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21MAGPACDELMOU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mateo Del Pino / Manuel Mouilleron Salvo (`KXATPCHALLENGERDOUBLES-26OCT21MAGPACDELMOU-DELMOU`) | 0.06 / 0.94 (850) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alan Magadan / Rodrigo Pacheco Mendez (`KXATPCHALLENGERDOUBLES-26OCT21MAGPACDELMOU-MAGPAC`) | 0.06 / 0.94 (850) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Murgett / Walters vs Martin / Melnic -- M25 Redbridge QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21MURWALMARMEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martin / Melnic (`KXITFDOUBLES-26OCT21MURWALMARMEL-MARMEL`) | 0.07 / 0.15 (29) | 11.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Murgett / Walters (`KXITFDOUBLES-26OCT21MURWALMARMEL-MURWAL`) | -- / 0.98 (3) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Nirundorn / Perez Ramos vs Dhokia / Jones -- M25 Redbridge QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21NIRPERDHOJON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dhokia / Jones (`KXITFDOUBLES-26OCT21NIRPERDHOJON-DHOJON`) | 0.43 / 0.71 (100) | 57.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nirundorn / Perez Ramos (`KXITFDOUBLES-26OCT21NIRPERDHOJON-NIRPER`) | 0.06 / 0.65 (6) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kristina Dmitruk vs Selina Atay -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220297:220808:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Selina Atay (`KXITFWMATCH-26OCT21DMIATA-ATA`) | 0.07 / 0.10 (6167) | 8.5% | 2.4% | 5.3% | 5.3% [4.4%-6.9%] | -- | -- | -- | -- | PASS | -6.1 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kristina Dmitruk (`KXITFWMATCH-26OCT21DMIATA-DMI`) | 0.90 / 0.95 (8) | 92.5% | 97.6% | 94.7% | 94.7% [93.1%-95.6%] | -- | -- | -- | -- | PASS | +5.1 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1766.0, B 1670.0; serve-point win A 59.6%, B 55.1%; Elo A 1675.9, B 1176.4; model uncertainty 0.0127
* Form inputs: days since last match A 275, B 177; matches on record A 214, B 207; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.006, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amandine Hesse vs Francisca Jorge -- W50 Cherbourg-en-Cotentin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:203281:216055:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amandine Hesse (`KXITFWMATCH-26OCT21HESJOR-HES`) | 0.34 / 0.36 (78) | 35.0% | 28.0% | 26.5% | 31.1% [29.2%-35.4%] | 36.2% | -- | 36.2% | MARKETS_AGREE | PASS | -7.0 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Francisca Jorge (`KXITFWMATCH-26OCT21HESJOR-JOR`) | 0.63 / 0.64 (69) | 63.5% | 72.0% | 73.5% | 69.0% [64.6%-70.8%] | 63.8% | -- | 63.8% | MODEL_LONE_OUTLIER | WATCH | +8.5 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2021.0, B 3145.0; serve-point win A 51.8%, B 43.9%; Elo A 1575.8, B 1661.5; model uncertainty 0.0311
* Form inputs: days since last match A 10, B 6; matches on record A 777, B 460; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.009, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Manon Leonard vs Salma Djoubri -- W50 Cherbourg-en-Cotentin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215807:220305:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Salma Djoubri (`KXITFWMATCH-26OCT21LEODJO-DJO`) | 0.30 / 0.33 (1379) | 31.5% | 27.0% | 20.8% | 27.9% [19.7%-39.5%] | 28.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.5 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Manon Leonard (`KXITFWMATCH-26OCT21LEODJO-LEO`) | 0.67 / 0.70 (1553) | 68.5% | 73.0% | 79.2% | 72.1% [60.5%-80.3%] | 71.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.5 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3201.0, B 169.0; serve-point win A 56.7%, B 47.9%; Elo A 1624.9, B 1467.4; model uncertainty 0.0992
* Form inputs: days since last match A 128, B 338; matches on record A 348, B 168; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.096, surface_pool_high +0.082, surface_dev_loose +0.000, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Victoria Pohle vs Andrea Roots -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222918:260433:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Victoria Pohle (`KXITFWMATCH-26OCT21POHROO-POH`) | 0.91 / 0.95 (7436) | 93.0% | 93.1% | 75.3% | 83.9% [83.2%-85.2%] | -- | -- | -- | -- | PASS | +0.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Andrea Roots (`KXITFWMATCH-26OCT21POHROO-ROO`) | 0.05 / 0.09 (6582) | 7.0% | 6.9% | 24.7% | 16.1% [14.8%-16.8%] | -- | -- | -- | -- | PASS | -0.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1323.0, B 163.0; serve-point win A 58.5%, B 52.6%; Elo A 1367.6, B 1063.9; model uncertainty 0.0098
* Form inputs: days since last match A 191, B 380; matches on record A 46, B 54; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.006, surface_pool_high -0.000, surface_dev_loose +0.007, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Teodora Vlajic vs Stefaniya Neporent -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:270264:270428:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefaniya Neporent (`KXITFWMATCH-26OCT21VLANEP-NEP`) | 0.48 / 0.49 (49) | 48.5% | 57.6% | 43.6% | 51.1% [51.1%-52.1%] | -- | -- | -- | -- | PASS | +9.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Teodora Vlajic (`KXITFWMATCH-26OCT21VLANEP-VLA`) | 0.46 / 0.50 (17) | 48.0% | 42.4% | 56.4% | 48.9% [47.9%-48.9%] | -- | -- | -- | -- | PASS | -5.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 116.0, B 234.0; serve-point win A 53.8%, B 44.8%; Elo A 1254.8, B 1271.4; model uncertainty 0.0053
* Form inputs: days since last match A 184, B 331; matches on record A 2, B 4; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Benjamin Bonzi vs Tommy Paul -- ATP Lyon R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-21 21:10Z
* Current expected start: 2026-10-21 18:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-21 17:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Clay · scheduled 2026-10-21T21:10:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126127:126205:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Benjamin Bonzi (`KXATPMATCH-26OCT21BONPAU-BON`) | 0.28 / 0.29 (18146) | 28.5% | 23.3% | 29.5% | 26.5% [24.5%-27.8%] | 29.9% | 29.2% | 29.5% | MODEL_LONE_OUTLIER | PASS | -5.2 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Tommy Paul (`KXATPMATCH-26OCT21BONPAU-PAU`) | 0.72 / 0.73 (50215) | 72.5% | 76.7% | 70.5% | 73.5% [72.2%-75.5%] | 70.1% | 70.5% | 70.3% | EXTERNAL_LONE_OUTLIER | PASS | +4.2 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4434.0, B 5709.0; serve-point win A 60.4%, B 33.7%; Elo A 1734.7, B 1994.0; model uncertainty 0.0162
* Form inputs: days since last match A 1, B 5; matches on record A 772, B 720; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high -0.000, surface_dev_loose -0.001, surface_dev_tight +0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT21BONPAU-PAU7` Will Tommy Paul win at least 6.5 more games than Benjamin Bonzi?: 0.06/0.35 mid 20.5%, model 12.2% (projection_v2.0 (prediction ledger)) -- gap -8.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21BONPAU-PAU21` Will Tommy Paul win the Benjamin Bonzi vs Tommy Paul match by a set score of 2-1?: 0.22/0.26 mid 24.0%, model 29.5% (projection_v2.0 (prediction ledger)) -- gap +5.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT21BONPAU-28` Over 27.5 games: 0.28/0.30 mid 29.0%, model 34.0% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT21BONPAU-23` Over 22.5 games: 0.48/0.49 mid 48.5%, model 53.0% (projection_v2.0 (prediction ledger)) -- gap +4.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT21BONPAU-BON2` Will Benjamin Bonzi win at least 1.5 more games than Tommy Paul?: 0.20/0.24 mid 22.0%, model 17.8% (projection_v2.0 (prediction ledger)) -- gap -4.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21BONPAU-BON20` Will Benjamin Bonzi win the Benjamin Bonzi vs Tommy Paul match by a set score of 2-0?: 0.12/0.15 mid 13.5%, model 9.8% (projection_v2.0 (prediction ledger)) -- gap -3.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT21BONPAU-1-BON` Will Benjamin Bonzi win set 1 in the Benjamin Bonzi vs Tommy Paul match: 0.34/0.36 mid 35.0%, model 31.3% (projection_v2.0 (prediction ledger)) -- gap -3.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT21BONPAU-1-PAU` Will Tommy Paul win set 1 in the Benjamin Bonzi vs Tommy Paul match: 0.64/0.67 mid 65.5%, model 68.7% (projection_v2.0 (prediction ledger)) -- gap +3.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT21BONPAU-18` Over 17.5 games: 0.84/0.89 mid 86.5%, model 89.4% (projection_v2.0 (prediction ledger)) -- gap +2.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT21BONPAU-PAU4` Will Tommy Paul win at least 3.5 more games than Benjamin Bonzi?: 0.49/0.50 mid 49.5%, model 51.8% (projection_v2.0 (prediction ledger)) -- gap +2.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT21BONPAU-2-BON` Will Benjamin Bonzi win set 2 in the Benjamin Bonzi vs Tommy Paul match: 0.31/0.34 mid 32.5%, model 31.3% (projection_v2.0 (prediction ledger)) -- gap -1.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT21BONPAU-2-PAU` Will Tommy Paul win set 2 in the Benjamin Bonzi vs Tommy Paul match: 0.66/0.69 mid 67.5%, model 68.7% (projection_v2.0 (prediction ledger)) -- gap +1.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21BONPAU-PAU20` Will Tommy Paul win the Benjamin Bonzi vs Tommy Paul match by a set score of 2-0?: 0.47/0.49 mid 48.0%, model 47.2% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21BONPAU-BON21` Will Benjamin Bonzi win the Benjamin Bonzi vs Tommy Paul match by a set score of 2-1?: 0.12/0.15 mid 13.5%, model 13.5% (projection_v2.0 (prediction ledger)) -- gap -0.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Compagnucci / DI VITA vs Costanzo Baragiola Mordini / Teodor Pieleanu -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21COMDIVCOSTEO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Compagnucci / DI VITA (`KXITFDOUBLES-26OCT21COMDIVCOSTEO-COMDIV`) | 0.05 / 0.68 (78) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Costanzo Baragiola Mordini / Teodor Pieleanu (`KXITFDOUBLES-26OCT21COMDIVCOSTEO-COSTEO`) | 0.29 / 0.58 (1) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Da Rosa Castro / Monteiro vs Juhas / Popovic -- M15 Bol R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21DARMONJUHPOP:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Da Rosa Castro / Monteiro (`KXITFDOUBLES-26OCT21DARMONJUHPOP-DARMON`) | 0.05 / 0.06 (26) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Juhas / Popovic (`KXITFDOUBLES-26OCT21DARMONJUHPOP-JUHPOP`) | 0.90 / 0.95 (38) | 92.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Lopez Morillo / Torres Ramis vs Bertimon / Blancaneaux -- M15 Bol R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21LOPTORBERBLA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bertimon / Blancaneaux (`KXITFDOUBLES-26OCT21LOPTORBERBLA-BERBLA`) | 0.07 / 0.80 (125) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lopez Morillo / Torres Ramis (`KXITFDOUBLES-26OCT21LOPTORBERBLA-LOPTOR`) | 0.08 / 0.33 (37) | 20.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Rosenkranz Koenig / Ujvary vs Al-Amin / Allen -- M15 Bol R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21ROSUJVALAALL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Al-Amin / Allen (`KXITFDOUBLES-26OCT21ROSUJVALAALL-ALAALL`) | 0.08 / 0.51 (51) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rosenkranz Koenig / Ujvary (`KXITFDOUBLES-26OCT21ROSUJVALAALL-ROSUJV`) | 0.05 / 0.61 (64) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Angelina Abendroth / Angelique Abendroth vs Bokova / Ehrenbergerova -- W15 Karlovy Vary QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21ANGANGBOKEHR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Angelina Abendroth / Angelique Abendroth (`KXITFWDOUBLES-26OCT21ANGANGBOKEHR-ANGANG`) | 0.05 / 0.95 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bokova / Ehrenbergerova (`KXITFWDOUBLES-26OCT21ANGANGBOKEHR-BOKEHR`) | 0.05 / 0.95 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Julia Avdeeva vs Noma Noha Akugue -- W100 Wrexham R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222919:223333:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julia Avdeeva (`KXITFWMATCH-26OCT21AVDNOH-AVD`) | 0.38 / 0.40 (7051) | 39.0% | 42.9% | 39.8% | 42.3% [41.3%-45.3%] | -- | -- | -- | -- | WATCH | +3.9 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Noma Noha Akugue (`KXITFWMATCH-26OCT21AVDNOH-NOH`) | 0.59 / 0.60 (62) | 59.5% | 57.1% | 60.2% | 57.7% [54.7%-58.7%] | -- | -- | -- | -- | PASS | -2.4 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2898.0, B 4975.0; serve-point win A 59.9%, B 38.7%; Elo A 1736.4, B 1749.0; model uncertainty 0.0199
* Form inputs: days since last match A 9, B 8; matches on record A 331, B 345; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cabrera / Lamens vs Britton / Klugman -- W100 Wrexham R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21CABLAMBRIKLU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Britton / Klugman (`KXITFWDOUBLES-26OCT21CABLAMBRIKLU-BRIKLU`) | 0.24 / 0.55 (100) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cabrera / Lamens (`KXITFWDOUBLES-26OCT21CABLAMBRIKLU-CABLAM`) | 0.06 / 0.53 (53) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Cherny / Obradovic vs Tichackova / Tu -- W15 Bol R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21CHEOBRTICTUX:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cherny / Obradovic (`KXITFWDOUBLES-26OCT21CHEOBRTICTUX-CHEOBR`) | 0.05 / 0.95 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tichackova / Tu (`KXITFWDOUBLES-26OCT21CHEOBRTICTUX-TICTUX`) | 0.05 / 0.95 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## De Oliveira Pinto / Montesinos Vilanova vs Cabassers Morros / Cabassers Morros -- W15 Villena QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21DEOMONCABCAB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cabassers Morros / Cabassers Morros (`KXITFWDOUBLES-26OCT21DEOMONCABCAB-CABCAB`) | 0.05 / 0.95 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| De Oliveira Pinto / Montesinos Vilanova (`KXITFWDOUBLES-26OCT21DEOMONCABCAB-DEOMON`) | 0.05 / 0.95 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Esquiva Banuls / Torner Sensano vs Heddar / Kaegi -- W15 Villena QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21ESQTORHEDKAE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Esquiva Banuls / Torner Sensano (`KXITFWDOUBLES-26OCT21ESQTORHEDKAE-ESQTOR`) | 0.05 / 0.95 (9) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Heddar / Kaegi (`KXITFWDOUBLES-26OCT21ESQTORHEDKAE-HEDKAE`) | 0.06 / 0.46 (99) | 26.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Gadient / Wildgruber vs Hermanova / Sucha -- W15 Karlovy Vary QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21GADWILHERSUC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gadient / Wildgruber (`KXITFWDOUBLES-26OCT21GADWILHERSUC-GADWIL`) | 0.05 / 0.93 (51) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hermanova / Sucha (`KXITFWDOUBLES-26OCT21GADWILHERSUC-HERSUC`) | 0.09 / 0.89 (100) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Fernanda Labrana vs Gabriela Kawano Cho -- W15 Campina Grande R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-21T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:219625:259599:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriela Kawano Cho (`KXITFWMATCH-26OCT21LABKAW-KAW`) | 0.02 / 0.03 (1583) | 2.5% | 7.4% | 1.9% | 15.9% [11.6%-18.2%] | 4.3% | -- | 4.3% | KALSHI_LONE_OUTLIER | PASS | +4.9 pp | NORMAL | AGING | F / POOR | ALL_AGREE | VERIFIED |
| Fernanda Labrana (`KXITFWMATCH-26OCT21LABKAW-LAB`) | 0.97 / 0.99 (10881) | 98.0% | 92.6% | 98.1% | 84.1% [81.8%-88.4%] | 95.7% | -- | 95.7% | MODEL_LONE_OUTLIER | PASS | -5.4 pp | NORMAL | AGING | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2901.0, B 126.0; serve-point win A 59.9%, B 51.0%; Elo A 1511.7, B 1247.9; model uncertainty 0.0331
* Form inputs: days since last match A 39, B 380; matches on record A 271, B 17; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.003, surface_dev_loose +0.003, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Les / Seric vs Kajtazi / Sumak -- W15 Bol R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21LESSERKAJSUM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kajtazi / Sumak (`KXITFWDOUBLES-26OCT21LESSERKAJSUM-KAJSUM`) | 0.05 / 0.95 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Les / Seric (`KXITFWDOUBLES-26OCT21LESSERKAJSUM-LESSER`) | 0.05 / 0.95 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Manuela Maia Citolino vs Rebeca Pereira -- W15 Campina Grande R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21MAIPER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Manuela Maia Citolino (`KXITFWMATCH-26OCT21MAIPER-MAI`) | 0.03 / 0.04 (51010) | 3.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rebeca Pereira (`KXITFWMATCH-26OCT21MAIPER-PER`) | 0.97 / 0.98 (928) | 97.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maria Coromina Boluda / Paun vs Peet / Sarganella Verdu -- W15 Villena QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21MARPAUPEESAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Coromina Boluda / Paun (`KXITFWDOUBLES-26OCT21MARPAUPEESAR-MARPAU`) | 0.05 / 0.95 (58) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Peet / Sarganella Verdu (`KXITFWDOUBLES-26OCT21MARPAUPEESAR-PEESAR`) | 0.06 / 0.23 (1) | 14.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Catarina Melleiro vs sofia omati albieri -- W15 Campina Grande R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-21T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260959:266574:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| sofia omati albieri (`KXITFWMATCH-26OCT21MELALB-ALB`) | 0.57 / 0.58 (59) | 57.5% | 52.7% | 94.6% | 62.6% [62.6%-63.6%] | 59.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Catarina Melleiro (`KXITFWMATCH-26OCT21MELALB-MEL`) | 0.39 / 0.40 (6) | 39.5% | 47.3% | 5.4% | 37.4% [36.4%-37.4%] | 40.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 986.0, B 0.0; serve-point win A 51.7%, B 47.7%; Elo A 1119.3, B 1211.5; model uncertainty 0.0051
* Form inputs: days since last match A 212, B 947; matches on record A 71, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ana Sofia Sanchez vs Isadora Sigrist -- W15 Campina Grande R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21SANSIG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ana Sofia Sanchez (`KXITFWMATCH-26OCT21SANSIG-SAN`) | 0.97 / 0.99 (6731) | 98.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Isadora Sigrist (`KXITFWMATCH-26OCT21SANSIG-SIG`) | 0.02 / 0.03 (4988) | 2.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Schunk / Steiner vs Ruxandra Bertea / Firman -- W50 Cherbourg-en-Cotentin QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21SCHSTERUXFIR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ruxandra Bertea / Firman (`KXITFWDOUBLES-26OCT21SCHSTERUXFIR-RUXFIR`) | 0.30 / 0.42 (43) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Schunk / Steiner (`KXITFWDOUBLES-26OCT21SCHSTERUXFIR-SCHSTE`) | 0.06 / 0.70 (83) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Victoria Eigelsbach / Solakov vs Bosman / Akasha Ceuca -- W15 Karlovy Vary QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21VICSOLBOSAKA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bosman / Akasha Ceuca (`KXITFWDOUBLES-26OCT21VICSOLBOSAKA-BOSAKA`) | 0.16 / 0.58 (59) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Victoria Eigelsbach / Solakov (`KXITFWDOUBLES-26OCT21VICSOLBOSAKA-VICSOL`) | 0.05 / 0.54 (54) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Adrian Oetzbach vs Leonardo Iemmi -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 18:39Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T18:39:40Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21OETIEM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leonardo Iemmi (`KXITFMATCH-26OCT21OETIEM-IEM`) | 0.08 / 0.43 (1) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Adrian Oetzbach (`KXITFMATCH-26OCT21OETIEM-OET`) | 0.74 / 0.88 (1) | 81.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valentin Basel vs Pedro Sakamoto -- M15 Maceio R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106203:211761:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valentin Basel (`KXITFMATCH-26OCT21BASSAK-BAS`) | 0.14 / 0.17 (6864) | 15.5% | 18.1% | 37.9% | 14.7% [13.4%-16.5%] | 18.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.6 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pedro Sakamoto (`KXITFMATCH-26OCT21BASSAK-SAK`) | 0.84 / 0.85 (72) | 84.5% | 81.9% | 62.1% | 85.3% [83.5%-86.6%] | 81.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.6 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 178.0, B 1912.0; serve-point win A 57.5%, B 35.4%; Elo A 1230.4, B 1566.6; model uncertainty 0.0158
* Form inputs: days since last match A 121, B 23; matches on record A 36, B 670; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bonalumi / Maina vs Ciocca / Rahmani -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21BONMAICIORAH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bonalumi / Maina (`KXITFDOUBLES-26OCT21BONMAICIORAH-BONMAI`) | 0.05 / 0.92 (29) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ciocca / Rahmani (`KXITFDOUBLES-26OCT21BONMAICIORAH-CIORAH`) | 0.04 / 0.96 (93) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Bouchelaghem / Tepmahc vs Isik Kosaner / Massellani -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21BOUTEPISIMAS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bouchelaghem / Tepmahc (`KXITFDOUBLES-26OCT21BOUTEPISIMAS-BOUTEP`) | 0.04 / 0.70 (83) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Isik Kosaner / Massellani (`KXITFDOUBLES-26OCT21BOUTEPISIMAS-ISIMAS`) | 0.20 / 0.41 (67) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Nicolas Bruna vs Joao Vitor Scramin do Lago -- M15 Maceio R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21BRUSCR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Bruna (`KXITFMATCH-26OCT21BRUSCR-BRU`) | 0.80 / 0.82 (6108) | 81.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Joao Vitor Scramin do Lago (`KXITFMATCH-26OCT21BRUSCR-SCR`) | 0.17 / 0.19 (31) | 18.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ciurnelli / Gribaldo vs Lagerbohm / Vasa -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21CIUGRILAGVAS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ciurnelli / Gribaldo (`KXITFDOUBLES-26OCT21CIUGRILAGVAS-CIUGRI`) | 0.04 / 0.90 (80) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lagerbohm / Vasa (`KXITFDOUBLES-26OCT21CIUGRILAGVAS-LAGVAS`) | 0.12 / 0.90 (12) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Francisco Fontes Damorim vs bautista de la Pena -- M15 Maceio R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21FONDEL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bautista de la Pena (`KXITFMATCH-26OCT21FONDEL-DEL`) | 0.28 / 0.31 (6288) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Francisco Fontes Damorim (`KXITFMATCH-26OCT21FONDEL-FON`) | 0.69 / 0.70 (84) | 69.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jamji / Nagoudi vs De Carvalho / Rivet -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21JAMNAGDECRIV:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| De Carvalho / Rivet (`KXITFDOUBLES-26OCT21JAMNAGDECRIV-DECRIV`) | 0.10 / 0.36 (39) | 23.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jamji / Nagoudi (`KXITFDOUBLES-26OCT21JAMNAGDECRIV-JAMNAG`) | 0.04 / 0.75 (100) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Patrick Maloney vs Kenta Miyoshi (b. 2004) -- ATP Challenger Fort Worth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-21T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:135753:211501:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Patrick Maloney (`KXATPCHALLENGERMATCH-26OCT21MALMIY-MAL`) | 0.40 / 0.41 (3978) | 40.5% | 44.6% | 39.9% | 52.5% [48.0%-58.1%] | 40.1% | -- | 40.1% | MODEL_LONE_OUTLIER | PASS | +4.1 pp | NORMAL | AGING | F / POOR | ALL_AGREE | AMBIGUOUS |
| Kenta Miyoshi (b. 2004) (`KXATPCHALLENGERMATCH-26OCT21MALMIY-MIY`) | 0.59 / 0.61 (6857) | 60.0% | 55.4% | 60.1% | 47.5% [41.9%-52.0%] | 59.9% | -- | 59.9% | MODEL_LONE_OUTLIER | PASS | -4.6 pp | NORMAL | AGING | F / POOR | ALL_AGREE | AMBIGUOUS |

* Serve evidence (points): A 1164.0, B 675.0; serve-point win A 61.3%, B 37.6%; Elo A 1499.7, B 1444.8; model uncertainty 0.0505
* Form inputs: days since last match A 702, B 29; matches on record A 86, B 54; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Daniel Milavsky vs Darwin Blanch -- ATP Challenger Fort Worth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-21T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210464:212251:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Darwin Blanch (`KXATPCHALLENGERMATCH-26OCT21MILBLA-BLA`) | 0.64 / 0.65 (526) | 64.5% | 66.1% | 54.5% | 63.3% [60.5%-66.2%] | 64.6% | 64.1% | 64.1% | MARKETS_AGREE | PASS | +1.6 pp | NORMAL | AGING | B / LIMITED | EXTERNAL_STALE | VERIFIED |
| Daniel Milavsky (`KXATPCHALLENGERMATCH-26OCT21MILBLA-MIL`) | 0.34 / 0.35 (6188) | 34.5% | 33.9% | 45.5% | 36.7% [33.8%-39.6%] | 35.4% | 35.2% | 35.2% | MODEL_LONE_OUTLIER | PASS | -0.6 pp | NORMAL | AGING | B / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 1675.0, B 3314.0; serve-point win A 61.1%, B 35.6%; Elo A 1511.1, B 1674.4; model uncertainty 0.0287
* Form inputs: days since last match A 23, B 23; matches on record A 46, B 125; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Ravasio / Goran Verwerft vs Manuel / Smiej -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21RAVGORMANSMI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Manuel / Smiej (`KXITFDOUBLES-26OCT21RAVGORMANSMI-MANSMI`) | 0.05 / 0.77 (108) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ravasio / Goran Verwerft (`KXITFDOUBLES-26OCT21RAVGORMANSMI-RAVGOR`) | 0.06 / 0.34 (37) | 20.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Bhopal / sahnoun vs Dho / Moneva -- W35 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21BHOSAHDHOMON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bhopal / sahnoun (`KXITFWDOUBLES-26OCT21BHOSAHDHOMON-BHOSAH`) | 0.05 / 0.85 (40) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dho / Moneva (`KXITFWDOUBLES-26OCT21BHOSAHDHOMON-DHOMON`) | 0.14 / 0.42 (0) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Denisenko / Maria Mihail vs Lazarenko / Rutlauka -- W35 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21DENMARLAZRUT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Denisenko / Maria Mihail (`KXITFWDOUBLES-26OCT21DENMARLAZRUT-DENMAR`) | 0.05 / 0.11 (28) | 8.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lazarenko / Rutlauka (`KXITFWDOUBLES-26OCT21DENMARLAZRUT-LAZRUT`) | 0.08 / 0.95 (2) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Gniewkowska / Zhu vs Kumru / Paszun -- W35 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21GNIZHUKUMPAS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gniewkowska / Zhu (`KXITFWDOUBLES-26OCT21GNIZHUKUMPAS-GNIZHU`) | 0.06 / 0.72 (0) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kumru / Paszun (`KXITFWDOUBLES-26OCT21GNIZHUKUMPAS-KUMPAS`) | 0.12 / 0.34 (1) | 23.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Husar / Lacinova vs Vogt / Yashina -- W35 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21HUSLACVOGYAS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Husar / Lacinova (`KXITFWDOUBLES-26OCT21HUSLACVOGYAS-HUSLAC`) | 0.08 / 0.30 (35) | 19.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vogt / Yashina (`KXITFWDOUBLES-26OCT21HUSLACVOGYAS-VOGYAS`) | 0.15 / 0.81 (131) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Victoria Jimenez Kasintseva vs Oceane Babel -- W50 Cherbourg-en-Cotentin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221746:223286:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oceane Babel (`KXITFWMATCH-26OCT21JIMBAB-BAB`) | 0.28 / 0.29 (6875) | 28.5% | 13.4% | 42.0% | 31.0% [21.5%-36.9%] | 29.8% | -- | 29.8% | MODEL_LONE_OUTLIER | PASS | -15.1 pp | HIGH_REVIEW | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Victoria Jimenez Kasintseva (`KXITFWMATCH-26OCT21JIMBAB-JIM`) | 0.70 / 0.72 (38) | 71.0% | 86.6% | 58.0% | 69.0% [63.1%-78.5%] | 70.2% | -- | 70.2% | MODEL_LONE_OUTLIER | PASS | +15.6 pp | HIGH_REVIEW | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4373.0, B 1826.0; serve-point win A 56.7%, B 51.6%; Elo A 1683.6, B 1437.7; model uncertainty 0.0769
* Form inputs: days since last match A 29, B 177; matches on record A 335, B 160; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21JIMBAB-JIM  (YES = Victoria Jimenez Kasintseva)
Model: 87%
Kalshi: 71%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: B (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.023, surface_pool_high -0.019, surface_dev_loose +0.032, surface_dev_tight -0.024
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marcelo Tomas Barrios Vera / Nicolas Villalon Valdes vs Federico Zeballos / Marcelo Zormann -- ATP Challenger Cali R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 19:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-21T19:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21BARVILZEBZOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcelo Tomas Barrios Vera / Nicolas Villalon Valdes (`KXATPCHALLENGERDOUBLES-26OCT21BARVILZEBZOR-BARVIL`) | 0.05 / 0.95 (223) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Federico Zeballos / Marcelo Zormann (`KXATPCHALLENGERDOUBLES-26OCT21BARVILZEBZOR-ZEBZOR`) | 0.05 / 0.95 (223) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Gustavo Heide vs Juan Pablo Varillas -- ATP Challenger Cali R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 19:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-21T19:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:122669:208361:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gustavo Heide (`KXATPCHALLENGERMATCH-26OCT21HEIVAR-HEI`) | 0.70 / 0.72 (2234) | 71.0% | 65.9% | 76.4% | 72.4% [68.9%-74.4%] | 69.7% | 70.0% | 69.8% | MODEL_LONE_OUTLIER | PASS | -5.1 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Juan Pablo Varillas (`KXATPCHALLENGERMATCH-26OCT21HEIVAR-VAR`) | 0.28 / 0.29 (397) | 28.5% | 34.1% | 23.6% | 27.6% [25.6%-31.1%] | 30.3% | 29.7% | 30.0% | MODEL_LONE_OUTLIER | PASS | +5.6 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3721.0, B 4350.0; serve-point win A 64.3%, B 38.9%; Elo A 1742.0, B 1669.5; model uncertainty 0.0275
* Form inputs: days since last match A 16, B 16; matches on record A 281, B 764; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.009, surface_dev_loose +0.008, surface_dev_tight -0.018
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Santiago Rodriguez Taverna vs Gonzalo Bueno -- ATP Challenger Cali R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 19:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-21T19:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21RODBUE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gonzalo Bueno (`KXATPCHALLENGERMATCH-26OCT21RODBUE-BUE`) | 0.65 / 0.66 (208) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Santiago Rodriguez Taverna (`KXATPCHALLENGERMATCH-26OCT21RODBUE-ROD`) | 0.34 / 0.35 (3595) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Allen / Maloney vs Cascino / Vedder -- W100 Wrexham R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21ALLMALCASVED:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Allen / Maloney (`KXITFWDOUBLES-26OCT21ALLMALCASVED-ALLMAL`) | 0.10 / 0.29 (1) | 19.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cascino / Vedder (`KXITFWDOUBLES-26OCT21ALLMALCASVED-CASVED`) | 0.07 / 0.82 (138) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lourdes Ayala vs Bianca Bernardes -- W15 Campina Grande R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 19:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-21T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:236968:259691:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lourdes Ayala (`KXITFWMATCH-26OCT21AYABER-AYA`) | 0.93 / 0.94 (8) | 93.5% | 69.2% | 60.6% | 63.7% [62.6%-67.6%] | 90.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -24.3 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Bianca Bernardes (`KXITFWMATCH-26OCT21AYABER-BER`) | 0.05 / 0.06 (30) | 5.5% | 30.8% | 39.4% | 36.3% [32.4%-37.4%] | 9.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +25.3 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 813.0, B 348.0; serve-point win A 53.2%, B 50.5%; Elo A 1220.6, B 1115.7; model uncertainty 0.025
* Form inputs: days since last match A 205, B 331; matches on record A 105, B 58; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21AYABER-BER  (YES = Bianca Bernardes)
Model: 31%
Kalshi: 6%
Gap: +25 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.020, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Brooks / Rajecki vs Crawley / Daniel -- W100 Wrexham R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21BRORAJCRADAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brooks / Rajecki (`KXITFWDOUBLES-26OCT21BRORAJCRADAN-BRORAJ`) | 0.05 / 0.75 (100) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Crawley / Daniel (`KXITFWDOUBLES-26OCT21BRORAJCRADAN-CRADAN`) | 0.09 / 0.37 (39) | 23.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Josefina Estevez vs Maria Florencia Urrutia -- W15 Campina Grande R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 19:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-21T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220447:260717:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Josefina Estevez (`KXITFWMATCH-26OCT21ESTURR-EST`) | 0.21 / 0.22 (4) | 21.5% | 18.9% | 19.5% | 22.2% [20.3%-23.8%] | -- | -- | -- | -- | PASS | -2.6 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Florencia Urrutia (`KXITFWMATCH-26OCT21ESTURR-URR`) | 0.77 / 0.80 (7177) | 78.5% | 81.1% | 80.5% | 77.8% [76.2%-79.7%] | -- | -- | -- | -- | PASS | +2.6 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 732.0, B 2454.0; serve-point win A 45.4%, B 48.1%; Elo A 1294.6, B 1496.2; model uncertainty 0.0177
* Form inputs: days since last match A 282, B 177; matches on record A 55, B 106; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Barbara Gatica vs Giovana Schincariol Delatorre Barbosa -- W15 Campina Grande R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 19:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-21T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211903:266781:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barbara Gatica (`KXITFWMATCH-26OCT21GATSCH-GAT`) | 0.94 / 0.96 (384) | 95.0% | 95.8% | 89.1% | 89.6% [88.3%-91.4%] | 94.7% | -- | 94.7% | MODEL_LONE_OUTLIER | PASS | +0.8 pp | NORMAL | AGING | F / POOR | ALL_AGREE | AMBIGUOUS |
| Giovana Schincariol Delatorre Barbosa (`KXITFWMATCH-26OCT21GATSCH-SCH`) | 0.05 / 0.06 (69) | 5.5% | 4.2% | 10.9% | 10.4% [8.6%-11.7%] | 5.3% | -- | 5.3% | MODEL_LONE_OUTLIER | PASS | -1.3 pp | NORMAL | AGING | F / POOR | ALL_AGREE | AMBIGUOUS |

* Serve evidence (points): A 633.0, B 533.0; serve-point win A 58.0%, B 54.9%; Elo A 1628.4, B 1250.5; model uncertainty 0.0154
* Form inputs: days since last match A 1612, B 212; matches on record A 388, B 20; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.002, surface_dev_loose +0.012, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Karolina Krajmer vs Maria Jose Sanchez Uribe -- W15 Campina Grande R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 19:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-21T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260865:263775:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karolina Krajmer (`KXITFWMATCH-26OCT21KRASAN-KRA`) | 0.40 / 0.43 (40) | 41.5% | 57.1% | 52.7% | 56.9% [55.9%-58.5%] | 40.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +15.6 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Jose Sanchez Uribe (`KXITFWMATCH-26OCT21KRASAN-SAN`) | 0.55 / 0.56 (56) | 55.5% | 42.9% | 47.3% | 43.1% [41.5%-44.1%] | 59.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.6 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 620.0, B 618.0; serve-point win A 53.6%, B 47.7%; Elo A 1292.5, B 1235.9; model uncertainty 0.0131
* Form inputs: days since last match A 331, B 359; matches on record A 50, B 39; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21KRASAN-KRA  (YES = Karolina Krajmer)
Model: 57%
Kalshi: 42%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Beaven / Zeuch vs Ruehl / Wessels -- M25 Sarreguemines QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 19:45Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T19:45:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21BEAZEURUEWES:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Beaven / Zeuch (`KXITFDOUBLES-26OCT21BEAZEURUEWES-BEAZEU`) | 0.05 / 0.92 (28) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ruehl / Wessels (`KXITFDOUBLES-26OCT21BEAZEURUEWES-RUEWES`) | 0.07 / 0.95 (100) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Philip Henning vs Robin Catry -- M25 Sarreguemines R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 19:45Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T19:45:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202475:210714:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Robin Catry (`KXITFMATCH-26OCT21HENCAT-CAT`) | 0.23 / 0.25 (37) | 24.0% | 22.2% | 36.0% | 24.9% [23.4%-26.6%] | 26.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.8 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Philip Henning (`KXITFMATCH-26OCT21HENCAT-HEN`) | 0.76 / 0.77 (23) | 76.5% | 77.8% | 64.0% | 75.1% [73.4%-76.6%] | 73.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.3 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1821.0, B 431.0; serve-point win A 64.3%, B 41.7%; Elo A 1522.4, B 1305.1; model uncertainty 0.0161
* Form inputs: days since last match A 9, B 107; matches on record A 143, B 54; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nagel / Visker vs Mueller / Senn -- M25 Sarreguemines QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 19:45Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T19:45:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21NAGVISMUESEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mueller / Senn (`KXITFDOUBLES-26OCT21NAGVISMUESEN-MUESEN`) | 0.07 / 0.94 (100) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nagel / Visker (`KXITFDOUBLES-26OCT21NAGVISMUESEN-NAGVIS`) | 0.04 / 0.95 (130) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Gabriel Debru / Igor Marcondes vs Oskar Brostrom Poulsen / Nikola Slavic -- ATP Challenger Fort Worth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-21T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21DEBMARPOUSLA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriel Debru / Igor Marcondes (`KXATPCHALLENGERDOUBLES-26OCT21DEBMARPOUSLA-DEBMAR`) | 0.06 / 0.74 (946) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Oskar Brostrom Poulsen / Nikola Slavic (`KXATPCHALLENGERDOUBLES-26OCT21DEBMARPOUSLA-POUSLA`) | 0.06 / 0.74 (446) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Alec Deckers vs Joshua Adamson -- M15 Ithaca R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21DECADA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joshua Adamson (`KXITFMATCH-26OCT21DECADA-ADA`) | 0.10 / 0.12 (310) | 11.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alec Deckers (`KXITFMATCH-26OCT21DECADA-DEC`) | 0.88 / 0.91 (6150) | 89.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Enzo Lima vs Leonardo Storck Franca -- M15 Maceio R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211478:tml:S1F4:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Enzo Lima (`KXITFMATCH-26OCT21LIMSTO-LIM`) | 0.34 / 0.35 (6532) | 34.5% | 11.6% | 55.1% | 13.9% [13.1%-15.1%] | 34.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -22.9 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Leonardo Storck Franca (`KXITFMATCH-26OCT21LIMSTO-STO`) | 0.65 / 0.66 (74) | 65.5% | 88.4% | 44.9% | 86.1% [84.9%-86.9%] | 65.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +22.9 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 107.0, B 51.0; serve-point win A 55.3%, B 35.4%; Elo A 1059.7, B 1387.4; model uncertainty 0.0099
* Form inputs: days since last match A 709, B 338; matches on record A 19, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21LIMSTO-STO  (YES = Leonardo Storck Franca)
Model: 88%
Kalshi: 66%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rafael Tosetto vs Tomas Farjat -- M15 Maceio R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208006:208078:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tomas Farjat (`KXITFMATCH-26OCT21TOSFAR-FAR`) | 0.51 / 0.54 (42) | 52.5% | 72.5% | 56.6% | 69.5% [68.2%-71.2%] | 53.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +20.0 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rafael Tosetto (`KXITFMATCH-26OCT21TOSFAR-TOS`) | 0.45 / 0.48 (44) | 46.5% | 27.5% | 43.4% | 30.5% [28.8%-31.8%] | 46.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -19.0 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 251.0, B 671.0; serve-point win A 59.3%, B 36.0%; Elo A 1206.5, B 1367.1; model uncertainty 0.0152
* Form inputs: days since last match A 170, B 30; matches on record A 66, B 242; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21TOSFAR-FAR  (YES = Tomas Farjat)
Model: 72%
Kalshi: 52%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Drew Van Orderlain vs Noa Vukadin -- M15 Ithaca R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132018:210538:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Drew Van Orderlain (`KXITFMATCH-26OCT21VANVUK-VAN`) | 0.18 / 0.21 (80) | 19.5% | 38.9% | 31.8% | 41.9% [41.9%-41.9%] | 23.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +19.4 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Noa Vukadin (`KXITFMATCH-26OCT21VANVUK-VUK`) | 0.79 / 0.81 (6458) | 80.0% | 61.1% | 68.2% | 58.1% [58.1%-58.1%] | 76.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -18.9 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 185.0, B 0.0; serve-point win A 60.4%, B 37.4%; Elo A 1128.8, B 1184.0; model uncertainty 0.0002
* Form inputs: days since last match A 702, B 102; matches on record A 42, B 9; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21VANVUK-VAN  (YES = Drew Van Orderlain)
Model: 39%
Kalshi: 20%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eric David Verdes vs Rodrigo Fernandes -- M15 Ithaca R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210653:212075:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rodrigo Fernandes (`KXITFMATCH-26OCT21VERFER-FER`) | 0.66 / 0.68 (1) | 67.0% | 55.8% | 28.1% | 49.0% [49.0%-49.0%] | 65.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.2 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Eric David Verdes (`KXITFMATCH-26OCT21VERFER-VER`) | 0.31 / 0.34 (86) | 32.5% | 44.2% | 71.9% | 51.0% [51.0%-51.0%] | 34.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +11.7 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 311.0; serve-point win A 60.1%, B 38.8%; Elo A 1207.5, B 1201.1; model uncertainty 0.0001
* Form inputs: days since last match A 849, B 709; matches on record A 8, B 29; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Benjamin Willwerth vs Noah Zamora -- M15 Ithaca R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212235:213653:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Benjamin Willwerth (`KXITFMATCH-26OCT21WILZAM-WIL`) | 0.57 / 0.60 (35) | 58.5% | 61.7% | 41.9% | 54.1% [54.1%-54.1%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Noah Zamora (`KXITFMATCH-26OCT21WILZAM-ZAM`) | 0.38 / 0.42 (27) | 40.0% | 38.3% | 58.1% | 45.9% [45.9%-45.9%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 352.0, B 0.0; serve-point win A 61.9%, B 40.5%; Elo A 1338.7, B 1311.1; model uncertainty 0.0003
* Form inputs: days since last match A 58, B 842; matches on record A 11, B 13; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nicolas Zanellato vs Mateo Barreiros Reyes -- M15 Maceio R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207595:210052:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mateo Barreiros Reyes (`KXITFMATCH-26OCT21ZANBAR-BAR`) | 0.19 / 0.22 (72) | 20.5% | 45.4% | 63.7% | 53.6% [49.0%-58.3%] | 21.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +24.9 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Nicolas Zanellato (`KXITFMATCH-26OCT21ZANBAR-ZAN`) | 0.78 / 0.80 (46) | 79.0% | 54.6% | 36.3% | 46.4% [41.7%-51.0%] | 78.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -24.4 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 741.0, B 1258.0; serve-point win A 59.6%, B 41.3%; Elo A 1359.3, B 1354.3; model uncertainty 0.0465
* Form inputs: days since last match A 121, B 751; matches on record A 173, B 106; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21ZANBAR-BAR  (YES = Mateo Barreiros Reyes)
Model: 45%
Kalshi: 20%
Gap: +25 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Adeshina / Zanolini vs Mair / Peer -- W35 Loule R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21ADEZANMAIPEE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adeshina / Zanolini (`KXITFWDOUBLES-26OCT21ADEZANMAIPEE-ADEZAN`) | 0.05 / 0.72 (89) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mair / Peer (`KXITFWDOUBLES-26OCT21ADEZANMAIPEE-MAIPEE`) | 0.10 / 0.40 (41) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Linea Bajraliu vs Carson Tanguilig -- W75 Saguenay R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221624:259996:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Linea Bajraliu (`KXITFWMATCH-26OCT21BAJTAN-BAJ`) | 0.57 / 0.60 (44) | 58.5% | 53.3% | 56.3% | 50.5% [46.8%-52.6%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.2 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carson Tanguilig (`KXITFWMATCH-26OCT21BAJTAN-TAN`) | 0.41 / 0.42 (34) | 41.5% | 46.7% | 43.7% | 49.5% [47.3%-53.2%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +5.2 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1577.0, B 1314.0; serve-point win A 55.7%, B 45.0%; Elo A 1440.7, B 1468.5; model uncertainty 0.0292
* Form inputs: days since last match A 106, B 184; matches on record A 46, B 33; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Reese Brantmeier vs Carolyn Ansari -- W75 Saguenay R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222034:258199:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carolyn Ansari (`KXITFWMATCH-26OCT21BRAANS-ANS`) | 0.12 / 0.14 (4) | 13.0% | 23.8% | 81.9% | 43.7% [40.5%-47.4%] | 14.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +10.8 pp | REVIEW | AGING | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Reese Brantmeier (`KXITFWMATCH-26OCT21BRAANS-BRA`) | 0.85 / 0.88 (7245) | 86.5% | 76.2% | 18.1% | 56.3% [52.6%-59.5%] | 85.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -10.3 pp | REVIEW | AGING | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 133.0, B 4315.0; serve-point win A 58.9%, B 46.6%; Elo A 1649.0, B 1576.2; model uncertainty 0.0343
* Form inputs: days since last match A 24, B 29; matches on record A 89, B 181; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luescher / Matias vs Cervino Ruiz / Rey Garcia -- W35 Loule R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21LUEMATCERREY:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cervino Ruiz / Rey Garcia (`KXITFWDOUBLES-26OCT21LUEMATCERREY-CERREY`) | 0.10 / 0.95 (2) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luescher / Matias (`KXITFWDOUBLES-26OCT21LUEMATCERREY-LUEMAT`) | 0.05 / 0.22 (1) | 13.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Medvedeva / Tian vs De Zeeuw / Louise Van den Broek -- W35 Loule R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21MEDTIADEZLOU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| De Zeeuw / Louise Van den Broek (`KXITFWDOUBLES-26OCT21MEDTIADEZLOU-DEZLOU`) | 0.05 / 0.95 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Medvedeva / Tian (`KXITFWDOUBLES-26OCT21MEDTIADEZLOU-MEDTIA`) | 0.05 / 0.17 (128) | 11.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sequeira / Tomai vs Liu / Moccia -- W35 Loule R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21SEQTOMLIUMOC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liu / Moccia (`KXITFWDOUBLES-26OCT21SEQTOMLIUMOC-LIUMOC`) | 0.90 / 0.95 (2) | 92.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sequeira / Tomai (`KXITFWDOUBLES-26OCT21SEQTOMLIUMOC-SEQTOM`) | 0.05 / 0.06 (26) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Keshav Chopra / Andres Martin vs James Hopper / Shunsuke Mitsui -- ATP Challenger Fort Worth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 20:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-21T20:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21CHOMARHOPMIT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Keshav Chopra / Andres Martin (`KXATPCHALLENGERDOUBLES-26OCT21CHOMARHOPMIT-CHOMAR`) | 0.06 / 0.94 (850) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| James Hopper / Shunsuke Mitsui (`KXATPCHALLENGERDOUBLES-26OCT21CHOMARHOPMIT-HOPMIT`) | 0.06 / 0.94 (850) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Mees Rottgering vs Cosme Rolland de Ravel -- ATP Challenger Fort Worth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 20:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-21T20:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212219:tml:R0KE:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cosme Rolland de Ravel (`KXATPCHALLENGERMATCH-26OCT21ROTROL-ROL`) | 0.31 / 0.33 (1435) | 32.0% | 28.1% | 46.9% | 40.3% [38.9%-41.3%] | 32.9% | 29.6% | -- | INSUFFICIENT_INPUTS | PASS | -3.9 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mees Rottgering (`KXATPCHALLENGERMATCH-26OCT21ROTROL-ROT`) | 0.67 / 0.68 (375) | 67.5% | 71.9% | 53.1% | 59.7% [58.7%-61.1%] | 67.1% | 69.0% | 69.0% | MODEL_LONE_OUTLIER | PASS | +4.4 pp | NORMAL | AGING | D / POOR | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 1162.0, B 473.0; serve-point win A 62.9%, B 41.6%; Elo A 1541.3, B 1459.5; model uncertainty 0.0122
* Form inputs: days since last match A 23, B 114; matches on record A 68, B 7; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE

## Valerio Aboian / Juan Manuel La Serna vs Boris Arias / Ignacio Carou -- ATP Challenger Cali R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 20:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-21T20:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21ABOLAARICAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valerio Aboian / Juan Manuel La Serna (`KXATPCHALLENGERDOUBLES-26OCT21ABOLAARICAR-ABOLA`) | 0.05 / 0.95 (223) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Boris Arias / Ignacio Carou (`KXATPCHALLENGERDOUBLES-26OCT21ABOLAARICAR-ARICAR`) | 0.05 / 0.95 (223) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Matteo Covato / Alex Hernandez vs Mateus Alves / Cristian Rodriguez -- ATP Challenger Cali R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 20:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-21T20:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21COVHERALVROC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mateus Alves / Cristian Rodriguez (`KXATPCHALLENGERDOUBLES-26OCT21COVHERALVROC-ALVROC`) | 0.06 / 0.94 (850) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matteo Covato / Alex Hernandez (`KXATPCHALLENGERDOUBLES-26OCT21COVHERALVROC-COVHER`) | 0.06 / 0.94 (850) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Bruno (2002) Oliveira / Natan Rodrigues vs Samuel Heredia / Adria Soriano Barrera -- ATP Challenger Cali R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 20:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-21T20:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21OLIRODHERSOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Samuel Heredia / Adria Soriano Barrera (`KXATPCHALLENGERDOUBLES-26OCT21OLIRODHERSOR-HERSOR`) | 0.06 / 0.94 (850) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bruno (2002) Oliveira / Natan Rodrigues (`KXATPCHALLENGERDOUBLES-26OCT21OLIRODHERSOR-OLIROD`) | 0.06 / 0.94 (850) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jennifer Rosa Dourado vs Camila Romero -- W15 Campina Grande R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-21T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214713:215854:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jennifer Rosa Dourado (`KXITFWMATCH-26OCT21DOUROM-DOU`) | 0.08 / 0.09 (39) | 8.5% | 24.7% | 36.5% | 28.4% [26.2%-30.3%] | 12.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +16.2 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Camila Romero (`KXITFWMATCH-26OCT21DOUROM-ROM`) | 0.89 / 0.91 (34) | 90.0% | 75.3% | 63.5% | 71.6% [69.7%-73.9%] | 87.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -14.7 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 723.0, B 1526.0; serve-point win A 53.3%, B 41.5%; Elo A 1191.3, B 1380.5; model uncertainty 0.0205
* Form inputs: days since last match A 212, B 184; matches on record A 134, B 225; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21DOUROM-DOU  (YES = Jennifer Rosa Dourado)
Model: 25%
Kalshi: 8%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.009, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ilinca Burcescu / Stusek vs Nahimana / Tran -- W50 Cherbourg-en-Cotentin QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21ILISTUNAHTRA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ilinca Burcescu / Stusek (`KXITFWDOUBLES-26OCT21ILISTUNAHTRA-ILISTU`) | 0.12 / 0.31 (5) | 21.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nahimana / Tran (`KXITFWDOUBLES-26OCT21ILISTUNAHTRA-NAHTRA`) | 0.05 / 0.80 (125) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dalmasso / Pawlak vs Ghazouani Durand / Walch -- M25 Sarreguemines QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 20:45Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T20:45:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21DALPAWGHAWAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dalmasso / Pawlak (`KXITFDOUBLES-26OCT21DALPAWGHAWAL-DALPAW`) | 0.05 / 0.95 (38) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ghazouani Durand / Walch (`KXITFDOUBLES-26OCT21DALPAWGHAWAL-GHAWAL`) | 0.05 / 0.95 (38) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Gabet / Prihodko vs Freire Da Silva / Ponchet -- M25 Sarreguemines QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 20:45Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T20:45:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21GABPRIFREPON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Freire Da Silva / Ponchet (`KXITFDOUBLES-26OCT21GABPRIFREPON-FREPON`) | 0.05 / 0.92 (29) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gabet / Prihodko (`KXITFDOUBLES-26OCT21GABPRIFREPON-GABPRI`) | 0.05 / 0.95 (38) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Martina Capurro Taborda vs Elizabeth Mandlik -- W50 Austin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211920:216097:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martina Capurro Taborda (`KXITFWMATCH-26OCT21CAPMAN-CAP`) | 0.18 / 0.19 (0) | 18.5% | 31.1% | 67.1% | 55.3% [41.5%-60.6%] | 20.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +12.6 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elizabeth Mandlik (`KXITFWMATCH-26OCT21CAPMAN-MAN`) | 0.80 / 0.83 (75) | 81.5% | 68.9% | 32.9% | 44.7% [39.4%-58.5%] | 79.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.6 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3440.0, B 3798.0; serve-point win A 51.3%, B 45.0%; Elo A 1509.9, B 1673.1; model uncertainty 0.0953
* Form inputs: days since last match A 39, B 57; matches on record A 383, B 367; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose +0.005, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ninon Carpentier vs Alice Robbe -- W50 Cherbourg-en-Cotentin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215806:270156:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ninon Carpentier (`KXITFWMATCH-26OCT21CARROB-CAR`) | 0.41 / 0.44 (6697) | 42.5% | 4.9% | 34.4% | 16.1% [12.5%-19.2%] | 43.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -37.6 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alice Robbe (`KXITFWMATCH-26OCT21CARROB-ROB`) | 0.56 / 0.59 (114) | 57.5% | 95.1% | 65.6% | 83.9% [80.8%-87.5%] | 56.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +37.6 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 188.0, B 1055.0; serve-point win A 47.0%, B 40.6%; Elo A 1186.7, B 1492.2; model uncertainty 0.0334
* Form inputs: days since last match A 289, B 191; matches on record A 4, B 385; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21CARROB-ROB  (YES = Alice Robbe)
Model: 95%
Kalshi: 57%
Gap: +38 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.022, surface_pool_high +0.031, surface_dev_loose -0.003, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sakura Hosogi vs Hina Inoue -- W75 Saguenay R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220718:222080:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sakura Hosogi (`KXITFWMATCH-26OCT21HOSINO-HOS`) | 0.35 / 0.38 (39) | 36.5% | 41.6% | 54.2% | 48.4% [43.1%-51.1%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +5.1 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hina Inoue (`KXITFWMATCH-26OCT21HOSINO-INO`) | 0.61 / 0.64 (31) | 62.5% | 58.4% | 45.8% | 51.6% [48.9%-56.9%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.1 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2576.0, B 2804.0; serve-point win A 54.5%, B 43.9%; Elo A 1554.1, B 1627.1; model uncertainty 0.0397
* Form inputs: days since last match A 177, B 184; matches on record A 392, B 325; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Justina Mikulskyte vs Hiromi Abe -- W75 Saguenay R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:212303:221362:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hiromi Abe (`KXITFWMATCH-26OCT21MIKABE-ABE`) | 0.68 / 0.69 (80) | 68.5% | 59.2% | 64.1% | 59.5% [53.7%-62.6%] | 68.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.3 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Justina Mikulskyte (`KXITFWMATCH-26OCT21MIKABE-MIK`) | 0.28 / 0.31 (6594) | 29.5% | 40.8% | 35.9% | 40.5% [37.4%-46.3%] | 31.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +11.3 pp | REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3227.0, B 2555.0; serve-point win A 52.1%, B 46.1%; Elo A 1680.9, B 1691.9; model uncertainty 0.0444
* Form inputs: days since last match A 35, B 219; matches on record A 492, B 200; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Barbora Palicova vs Malaika Rapolu -- W50 Austin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222837:223323:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barbora Palicova (`KXITFWMATCH-26OCT21PALRAP-PAL`) | 0.39 / 0.42 (13) | 40.5% | 33.2% | 14.4% | 25.7% [19.0%-42.1%] | 40.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Malaika Rapolu (`KXITFWMATCH-26OCT21PALRAP-RAP`) | 0.56 / 0.57 (58) | 56.5% | 66.8% | 85.6% | 74.3% [57.9%-81.0%] | 59.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +10.3 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2850.0, B 1761.0; serve-point win A 53.5%, B 43.3%; Elo A 1576.8, B 1619.4; model uncertainty 0.1153
* Form inputs: days since last match A 9, B 34; matches on record A 350, B 134; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.017, surface_pool_high -0.017, surface_dev_loose -0.017, surface_dev_tight +0.026
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amelie Van Impe vs Rebecca Munk Mortensen -- W50 Austin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:228909:241714:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rebecca Munk Mortensen (`KXITFWMATCH-26OCT21VANMUN-MUN`) | 0.35 / 0.38 (6188) | 36.5% | 50.8% | 54.8% | 53.2% [49.5%-56.3%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +14.3 pp | REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amelie Van Impe (`KXITFWMATCH-26OCT21VANMUN-VAN`) | 0.62 / 0.64 (70) | 63.0% | 49.1% | 45.2% | 46.8% [43.7%-50.5%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.8 pp | REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1949.0, B 1668.0; serve-point win A 55.0%, B 44.8%; Elo A 1462.5, B 1472.8; model uncertainty 0.0343
* Form inputs: days since last match A 198, B 177; matches on record A 185, B 166; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.016, surface_dev_loose -0.032, surface_dev_tight +0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Wally Thayne / Jamie Vance vs Ozan Baris / Kenta (2004) Miyoshi -- ATP Challenger Fort Worth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 21:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-21T21:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21THAVANBARMIY:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ozan Baris / Kenta (2004) Miyoshi (`KXATPCHALLENGERDOUBLES-26OCT21THAVANBARMIY-BARMIY`) | 0.05 / 0.95 (223) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Wally Thayne / Jamie Vance (`KXATPCHALLENGERDOUBLES-26OCT21THAVANBARMIY-THAVAN`) | 0.05 / 0.95 (223) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jenson Brooksby vs Timo Legout -- ATP Challenger Fort Worth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 21:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-21T21:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202385:209355:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jenson Brooksby (`KXATPCHALLENGERMATCH-26OCT21BROLEG-BRO`) | 0.72 / 0.74 (8092) | 73.0% | 74.7% | 58.8% | 72.5% [68.1%-76.1%] | 71.1% | 72.5% | 72.5% | MARKETS_AGREE | PASS | +1.7 pp | NORMAL | AGING | B / LIMITED | EXTERNAL_STALE | VERIFIED |
| Timo Legout (`KXATPCHALLENGERMATCH-26OCT21BROLEG-LEG`) | 0.26 / 0.28 (7449) | 27.0% | 25.3% | 41.2% | 27.5% [23.9%-31.9%] | 28.9% | 27.6% | 27.6% | MARKETS_AGREE | PASS | -1.7 pp | NORMAL | AGING | B / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 2946.0, B 894.0; serve-point win A 61.7%, B 43.4%; Elo A 1812.4, B 1577.6; model uncertainty 0.0403
* Form inputs: days since last match A 12, B 30; matches on record A 271, B 175; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Luis David Martinez / Alex Rybakov vs Jason Jung / Joshua Sheehy -- ATP Challenger Fort Worth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 21:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-21T21:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21MARRYBJUNSHE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jason Jung / Joshua Sheehy (`KXATPCHALLENGERDOUBLES-26OCT21MARRYBJUNSHE-JUNSHE`) | 0.05 / 0.95 (223) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luis David Martinez / Alex Rybakov (`KXATPCHALLENGERDOUBLES-26OCT21MARRYBJUNSHE-MARRYB`) | 0.05 / 0.95 (223) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Diego Hidalgo / Mariano Kestelboim vs Hernan Casanova / Santiago Rodriguez Taverna -- ATP Challenger Cali R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-21T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21HIDKESCASROD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hernan Casanova / Santiago Rodriguez Taverna (`KXATPCHALLENGERDOUBLES-26OCT21HIDKESCASROD-CASROD`) | 0.06 / 0.94 (850) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Diego Hidalgo / Mariano Kestelboim (`KXATPCHALLENGERDOUBLES-26OCT21HIDKESCASROD-HIDKES`) | 0.06 / 0.94 (850) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Franco Ribero / Gonzalo Villanueva vs Zachary Fuchs / Brandon Perez -- ATP Challenger Cali R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-21T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21RIBVILFUCPER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zachary Fuchs / Brandon Perez (`KXATPCHALLENGERDOUBLES-26OCT21RIBVILFUCPER-FUCPER`) | 0.05 / 0.95 (223) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Franco Ribero / Gonzalo Villanueva (`KXATPCHALLENGERDOUBLES-26OCT21RIBVILFUCPER-RIBVIL`) | 0.05 / 0.95 (223) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Thijs Boogaard vs Matteo Martineau -- M25 Sarreguemines R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 21:45Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T21:45:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200188:212275:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thijs Boogaard (`KXITFMATCH-26OCT21BOOMAR-BOO`) | 0.19 / 0.22 (26) | 20.5% | 20.2% | 46.0% | 25.1% [21.2%-29.3%] | 23.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.3 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matteo Martineau (`KXITFMATCH-26OCT21BOOMAR-MAR`) | 0.78 / 0.80 (39) | 79.0% | 79.8% | 54.0% | 74.9% [70.7%-78.8%] | 76.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.8 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 514.0, B 4215.0; serve-point win A 61.1%, B 32.1%; Elo A 1398.2, B 1645.4; model uncertainty 0.0401
* Form inputs: days since last match A 100, B 9; matches on record A 10, B 543; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jonah Braswell vs Eli Stephenson -- M15 Ithaca R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21BRASTE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jonah Braswell (`KXITFMATCH-26OCT21BRASTE-BRA`) | 0.62 / 0.64 (69) | 63.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eli Stephenson (`KXITFMATCH-26OCT21BRASTE-STE`) | 0.33 / 0.36 (38) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pedro Henrique Chabalgoity vs Dante Pagani -- M15 Maceio R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21CHAPAG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pedro Henrique Chabalgoity (`KXITFMATCH-26OCT21CHAPAG-CHA`) | 0.44 / 0.45 (86) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dante Pagani (`KXITFMATCH-26OCT21CHAPAG-PAG`) | 0.54 / 0.55 (55) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Julian Cundom vs Joao Victor Couto Loureiro -- M15 Maceio R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208424:208533:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joao Victor Couto Loureiro (`KXITFMATCH-26OCT21CUNCOU-COU`) | 0.50 / 0.53 (277) | 51.5% | 43.9% | 33.1% | 43.9% [43.3%-44.9%] | 52.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Julian Cundom (`KXITFMATCH-26OCT21CUNCOU-CUN`) | 0.45 / 0.48 (6303) | 46.5% | 56.1% | 66.8% | 56.1% [55.1%-56.7%] | 47.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +9.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 87.0, B 509.0; serve-point win A 61.7%, B 39.5%; Elo A 1183.1, B 1147.4; model uncertainty 0.008
* Form inputs: days since last match A 135, B 695; matches on record A 29, B 92; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Benjamin Thomas George vs Oliver Ojakaar -- M15 Ithaca R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210312:212259:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Benjamin Thomas George (`KXITFMATCH-26OCT21GEOOJA-GEO`) | 0.25 / 0.26 (937) | 25.5% | 38.4% | 43.3% | 39.8% [38.8%-40.3%] | 28.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +12.9 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oliver Ojakaar (`KXITFMATCH-26OCT21GEOOJA-OJA`) | 0.71 / 0.75 (156) | 73.0% | 61.6% | 56.7% | 60.2% [59.7%-61.2%] | 71.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.4 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 259.0, B 188.0; serve-point win A 58.2%, B 39.5%; Elo A 1299.1, B 1378.5; model uncertainty 0.0071
* Form inputs: days since last match A 212, B 628; matches on record A 39, B 44; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vignesh Gogineni vs Cezar Gabriel Papoe -- M15 Ithaca R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212885:espn:espn:18858:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vignesh Gogineni (`KXITFMATCH-26OCT21GOGPAP-GOG`) | 0.71 / 0.73 (1) | 72.0% | 75.6% | 50.0% | 79.9% [79.9%-79.9%] | 69.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Cezar Gabriel Papoe (`KXITFMATCH-26OCT21GOGPAP-PAP`) | 0.26 / 0.30 (6584) | 28.0% | 24.4% | 50.0% | 20.1% [20.1%-20.1%] | 30.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 64.7%, B 40.7%; Elo A 1530.6, B 1288.1; model uncertainty 0.0
* Form inputs: days since last match A 71, B 772; matches on record A 1, B 12; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## FELIPE PINZON MORENO vs Jack Anthrop -- M15 Ithaca R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210294:210361:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jack Anthrop (`KXITFMATCH-26OCT21PINANT-ANT`) | 0.90 / 0.92 (23) | 91.0% | 89.9% | 53.0% | 79.7% [79.2%-79.8%] | 86.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| FELIPE PINZON MORENO (`KXITFMATCH-26OCT21PINANT-PIN`) | 0.07 / 0.08 (946) | 7.5% | 10.1% | 47.0% | 20.3% [20.2%-20.8%] | 13.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 204.0; serve-point win A 57.9%, B 31.9%; Elo A 1182.8, B 1417.2; model uncertainty 0.0031
* Form inputs: days since last match A 1115, B 401; matches on record A 4, B 59; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kaua Lorenzo Santos Gava vs Enzo Crevelaro -- M15 Maceio R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211732:212787:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Enzo Crevelaro (`KXITFMATCH-26OCT21SANCRE-CRE`) | 0.07 / 0.09 (12) | 8.0% | 50.3% | 61.6% | 51.0% [51.0%-51.0%] | 12.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +42.4 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Kaua Lorenzo Santos Gava (`KXITFMATCH-26OCT21SANCRE-SAN`) | 0.90 / 0.92 (27) | 91.0% | 49.6% | 38.4% | 49.0% [49.0%-49.0%] | 87.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -41.4 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 49.0, B 0.0; serve-point win A 61.1%, B 38.9%; Elo A 1211.3, B 1215.0; model uncertainty 0.0001
* Form inputs: days since last match A 758, B 709; matches on record A 5, B 3; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21SANCRE-CRE  (YES = Enzo Crevelaro)
Model: 50%
Kalshi: 8%
Gap: +42 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bayerlova / Gimbrere vs Dartron / Rouvroy -- W75 Saguenay QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21BAYGIMDARROU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bayerlova / Gimbrere (`KXITFWDOUBLES-26OCT21BAYGIMDARROU-BAYGIM`) | 0.05 / 0.65 (71) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dartron / Rouvroy (`KXITFWDOUBLES-26OCT21BAYGIMDARROU-DARROU`) | 0.09 / 0.48 (48) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Kylie Collins vs Yeonwoo Ku -- W50 Austin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21COLKUX:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kylie Collins (`KXITFWMATCH-26OCT21COLKUX-COL`) | 0.28 / 0.29 (1099) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yeonwoo Ku (`KXITFWMATCH-26OCT21COLKUX-KUX`) | 0.68 / 0.72 (229) | 70.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Salma Drugdova vs Brandy Walker -- W35 Bakersfield CA R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:235160:249659:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Salma Drugdova (`KXITFWMATCH-26OCT21DRUWAL-DRU`) | 0.75 / 0.77 (37) | 76.0% | 78.1% | 82.5% | 74.8% [71.3%-79.2%] | 73.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Brandy Walker (`KXITFWMATCH-26OCT21DRUWAL-WAL`) | 0.21 / 0.25 (6282) | 23.0% | 21.9% | 17.5% | 25.2% [20.8%-28.7%] | 26.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1429.0, B 421.0; serve-point win A 56.9%, B 48.9%; Elo A 1459.7, B 1295.6; model uncertainty 0.0398
* Form inputs: days since last match A 443, B 184; matches on record A 158, B 103; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xinyu Gao vs Anastasia Tikhonova -- W50 Austin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214386:221073:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xinyu Gao (`KXITFWMATCH-26OCT21GAOTIK-GAO`) | 0.68 / 0.70 (118) | 69.0% | 77.3% | 80.9% | 76.7% [72.9%-78.3%] | 66.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +8.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anastasia Tikhonova (`KXITFWMATCH-26OCT21GAOTIK-TIK`) | 0.29 / 0.32 (6458) | 30.5% | 22.7% | 19.1% | 23.3% [21.7%-27.1%] | 33.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.8 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3203.0, B 2660.0; serve-point win A 58.9%, B 46.7%; Elo A 1711.8, B 1574.6; model uncertainty 0.0267
* Form inputs: days since last match A 18, B 17; matches on record A 419, B 387; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.012, surface_pool_high -0.012, surface_dev_loose +0.004, surface_dev_tight -0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jana Hossam Salah vs Valeriya Strakhova -- W35 Bakersfield CA R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211063:266764:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jana Hossam Salah (`KXITFWMATCH-26OCT21HOSSTR-HOS`) | 0.31 / 0.34 (37) | 32.5% | 32.1% | 65.6% | 38.4% [32.5%-44.1%] | 31.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.4 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valeriya Strakhova (`KXITFWMATCH-26OCT21HOSSTR-STR`) | 0.65 / 0.66 (73) | 65.5% | 67.9% | 34.4% | 61.6% [55.9%-67.5%] | 68.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.4 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 378.0, B 2323.0; serve-point win A 51.8%, B 44.7%; Elo A 1371.0, B 1506.9; model uncertainty 0.0585
* Form inputs: days since last match A 303, B 94; matches on record A 19, B 766; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ella McDonald vs Rose Marie Nijkamp -- W50 Austin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259591:260225:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ella McDonald (`KXITFWMATCH-26OCT21MCDNIJ-MCD`) | 0.77 / 0.78 (48) | 77.5% | 69.1% | 61.1% | 64.7% [63.6%-66.1%] | 74.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.4 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rose Marie Nijkamp (`KXITFWMATCH-26OCT21MCDNIJ-NIJ`) | 0.21 / 0.23 (343) | 22.0% | 30.9% | 38.9% | 35.3% [33.9%-36.4%] | 25.7% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +8.9 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1341.0, B 1080.0; serve-point win A 53.7%, B 50.0%; Elo A 1577.6, B 1447.9; model uncertainty 0.0125
* Form inputs: days since last match A 120, B 184; matches on record A 146, B 54; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.015, surface_dev_loose +0.015, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Briana Szabo vs Sophie Suh -- W35 Bakersfield CA R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223120:267469:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sophie Suh (`KXITFWMATCH-26OCT21SZASUH-SUH`) | 0.39 / 0.41 (150) | 40.0% | 16.8% | 44.2% | 33.0% [31.5%-34.5%] | 39.4% | -- | 39.4% | MODEL_LONE_OUTLIER | PASS | -23.2 pp | HIGH_REVIEW | AGING | F / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Briana Szabo (`KXITFWMATCH-26OCT21SZASUH-SZA`) | 0.57 / 0.58 (59) | 57.5% | 83.2% | 55.8% | 67.0% [65.5%-68.5%] | 60.6% | -- | 60.6% | KALSHI_LONE_OUTLIER | PASS | +25.7 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1762.0, B 350.0; serve-point win A 58.4%, B 48.9%; Elo A 1369.9, B 1230.6; model uncertainty 0.0147
* Form inputs: days since last match A 86, B 471; matches on record A 212, B 9; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21SZASUH-SZA  (YES = Briana Szabo)
Model: 83%
Kalshi: 57%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sahaja Yamalapalli vs Natalie Kha -- W35 Bakersfield CA R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21YAMKHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Natalie Kha (`KXITFWMATCH-26OCT21YAMKHA-KHA`) | 0.28 / 0.32 (35) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sahaja Yamalapalli (`KXITFWMATCH-26OCT21YAMKHA-YAM`) | 0.67 / 0.70 (39) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniel Milavsky / Braden Shick vs Erik Arutiunian / Daniil Ostapenkov -- ATP Challenger Fort Worth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-21T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21MILSHIARUOST:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Erik Arutiunian / Daniil Ostapenkov (`KXATPCHALLENGERDOUBLES-26OCT21MILSHIARUOST-ARUOST`) | 0.05 / 0.95 (223) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daniel Milavsky / Braden Shick (`KXATPCHALLENGERDOUBLES-26OCT21MILSHIARUOST-MILSHI`) | 0.05 / 0.95 (223) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Albert Pedrico Kravtsov / Cooper Woestendick vs Jeevan Nedunchezhiyan / Christopher Papa -- ATP Challenger Fort Worth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-21T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21PEDWOENEDPAP:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jeevan Nedunchezhiyan / Christopher Papa (`KXATPCHALLENGERDOUBLES-26OCT21PEDWOENEDPAP-NEDPAP`) | 0.08 / 0.95 (223) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Albert Pedrico Kravtsov / Cooper Woestendick (`KXATPCHALLENGERDOUBLES-26OCT21PEDWOENEDPAP-PEDWOE`) | 0.05 / 0.75 (24) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Tomasz Berkieta vs Nicolas Arseneault -- M15 Ithaca R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211530:212531:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Arseneault (`KXITFMATCH-26OCT21BERARS-ARS`) | 0.52 / 0.53 (6502) | 52.5% | 44.9% | 45.4% | 51.5% [49.5%-52.5%] | 53.8% | -- | 53.8% | MARKETS_AGREE | PASS | -7.6 pp | NORMAL | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Tomasz Berkieta (`KXITFMATCH-26OCT21BERARS-BER`) | 0.44 / 0.47 (62) | 45.5% | 55.1% | 54.6% | 48.5% [47.4%-50.5%] | 46.2% | -- | 46.2% | MODEL_LONE_OUTLIER | PASS | +9.6 pp | NORMAL | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 668.0, B 401.0; serve-point win A 61.9%, B 39.1%; Elo A 1287.8, B 1310.9; model uncertainty 0.0153
* Form inputs: days since last match A 79, B 93; matches on record A 60, B 17; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dahlberg / Velcz vs Casciato / Gold -- M15 Ithaca R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21DAHVELCASGOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Casciato / Gold (`KXITFDOUBLES-26OCT21DAHVELCASGOL-CASGOL`) | 0.05 / 0.95 (38) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dahlberg / Velcz (`KXITFDOUBLES-26OCT21DAHVELCASGOL-DAHVEL`) | 0.05 / 0.95 (38) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Tomas Martinez vs Giovanni Branchetti -- M15 Maceio R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21MARBRA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giovanni Branchetti (`KXITFMATCH-26OCT21MARBRA-BRA`) | 0.42 / 0.43 (43) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tomas Martinez (`KXITFMATCH-26OCT21MARBRA-MAR`) | 0.55 / 0.57 (6141) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mateus Nogueira vs Victor Pagotto -- M15 Maceio R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21NOGPAG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mateus Nogueira (`KXITFMATCH-26OCT21NOGPAG-NOG`) | 0.04 / 0.05 (198) | 4.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Victor Pagotto (`KXITFMATCH-26OCT21NOGPAG-PAG`) | 0.95 / 0.97 (804) | 96.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Felix Roussel vs Jaden Weekes -- M15 Ithaca R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21ROUWEE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felix Roussel (`KXITFMATCH-26OCT21ROUWEE-ROU`) | 0.66 / 0.67 (75) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jaden Weekes (`KXITFMATCH-26OCT21ROUWEE-WEE`) | 0.30 / 0.32 (52) | 31.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Paulo Andre Saraiva Dos Santos vs Bastian Malla -- M15 Maceio R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:109334:208063:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bastian Malla (`KXITFMATCH-26OCT21SARMAL-MAL`) | 0.48 / 0.49 (49) | 48.5% | 69.0% | 59.1% | 70.9% [69.1%-73.7%] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +20.5 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Paulo Andre Saraiva Dos Santos (`KXITFMATCH-26OCT21SARMAL-SAR`) | 0.48 / 0.50 (75) | 49.0% | 31.0% | 40.9% | 29.1% [26.3%-30.9%] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -18.0 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 990.0, B 367.0; serve-point win A 59.5%, B 36.7%; Elo A 1303.9, B 1479.3; model uncertainty 0.0233
* Form inputs: days since last match A 688, B 1486; matches on record A 115, B 408; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21SARMAL-MAL  (YES = Bastian Malla)
Model: 69%
Kalshi: 48%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rafael Ymer vs Connor Plunkett -- M15 Ithaca R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21YMEPLU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Connor Plunkett (`KXITFMATCH-26OCT21YMEPLU-PLU`) | 0.57 / 0.58 (40) | 57.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rafael Ymer (`KXITFMATCH-26OCT21YMEPLU-YME`) | 0.39 / 0.42 (260) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Diletta Cherubini vs Amelie Justine Hejtmanek -- W35 Bakersfield CA R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221000:260323:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diletta Cherubini (`KXITFWMATCH-26OCT21CHEHEJ-CHE`) | 0.75 / 0.76 (104) | 75.5% | 84.0% | 64.6% | 70.4% [68.5%-72.6%] | 76.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +8.5 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amelie Justine Hejtmanek (`KXITFWMATCH-26OCT21CHEHEJ-HEJ`) | 0.19 / 0.23 (87) | 21.0% | 16.0% | 35.4% | 29.6% [27.4%-31.5%] | 23.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -5.0 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2494.0, B 1296.0; serve-point win A 57.4%, B 50.0%; Elo A 1572.3, B 1379.2; model uncertainty 0.0207
* Form inputs: days since last match A 38, B 184; matches on record A 314, B 54; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lahey / Vagramov vs Hatouka / Laskevich -- W50 Austin QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21LAHVAGHATLAS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hatouka / Laskevich (`KXITFWDOUBLES-26OCT21LAHVAGHATLAS-HATLAS`) | 0.05 / 0.60 (62) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lahey / Vagramov (`KXITFWDOUBLES-26OCT21LAHVAGHATLAS-LAHVAG`) | 0.05 / 0.54 (54) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## McAdoo / Tikhonova vs Munk Mortensen / Nilsson -- W50 Austin QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21MCATIKMUNNIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| McAdoo / Tikhonova (`KXITFWDOUBLES-26OCT21MCATIKMUNNIL-MCATIK`) | 0.05 / 0.92 (30) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Munk Mortensen / Nilsson (`KXITFWDOUBLES-26OCT21MCATIKMUNNIL-MUNNIL`) | 0.05 / 0.20 (35) | 12.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Sara Saito vs Clervie Ngounoue -- W75 Saguenay R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:238064:260170:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Clervie Ngounoue (`KXITFWMATCH-26OCT21SAINGO-NGO`) | 0.67 / 0.69 (6179) | 68.0% | 67.3% | 61.5% | 63.6% [63.1%-65.1%] | 65.7% | -- | 65.7% | KALSHI_LONE_OUTLIER | PASS | -0.7 pp | NORMAL | AGING | A / LIMITED | ALL_AGREE | VERIFIED |
| Sara Saito (`KXITFWMATCH-26OCT21SAINGO-SAI`) | 0.31 / 0.33 (427) | 32.0% | 32.7% | 38.5% | 36.4% [34.9%-36.9%] | 34.3% | -- | 34.3% | KALSHI_LONE_OUTLIER | WATCH | +0.7 pp | NORMAL | AGING | A / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3341.0, B 2509.0; serve-point win A 52.8%, B 43.8%; Elo A 1658.8, B 1783.6; model uncertainty 0.0101
* Form inputs: days since last match A 23, B 58; matches on record A 198, B 153; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Saito / Xu vs Abe / Yoshioka -- W75 Saguenay QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-21T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21SAIXUXABEYOS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Abe / Yoshioka (`KXITFWDOUBLES-26OCT21SAIXUXABEYOS-ABEYOS`) | 0.05 / 0.92 (0) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Saito / Xu (`KXITFWDOUBLES-26OCT21SAIXUXABEYOS-SAIXUX`) | 0.06 / 0.67 (0) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Aspen Schuman vs Connie Ma -- W35 Bakersfield CA R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221143:260767:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Connie Ma (`KXITFWMATCH-26OCT21SCHMAX-MAX`) | 0.87 / 0.90 (214) | 88.5% | 62.4% | 35.9% | 51.1% [51.1%-51.1%] | 85.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -26.1 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Aspen Schuman (`KXITFWMATCH-26OCT21SCHMAX-SCH`) | 0.10 / 0.14 (6157) | 12.0% | 37.6% | 64.1% | 48.9% [48.9%-48.9%] | 14.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +25.6 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 437.0, B 0.0; serve-point win A 53.2%, B 44.5%; Elo A 1474.8, B 1482.1; model uncertainty 0.0
* Form inputs: days since last match A 345, B 1843; matches on record A 46, B 21; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21SCHMAX-SCH  (YES = Aspen Schuman)
Model: 38%
Kalshi: 12%
Gap: +26 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Astra Sharma vs Imogen Haddad -- W35 Bakersfield CA R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206292:260559:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Imogen Haddad (`KXITFWMATCH-26OCT21SHAHAD-HAD`) | 0.05 / 0.08 (66) | 6.5% | 2.4% | 36.5% | 8.9% [8.8%-8.9%] | 8.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Astra Sharma (`KXITFWMATCH-26OCT21SHAHAD-SHA`) | 0.92 / 0.95 (180) | 93.5% | 97.6% | 63.5% | 91.1% [91.1%-91.2%] | 91.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2800.0, B 0.0; serve-point win A 63.7%, B 51.3%; Elo A 1698.5, B 1292.0; model uncertainty 0.0005
* Form inputs: days since last match A 35, B 709; matches on record A 423, B 35; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Margaret Sohns vs Lan Mi -- W35 Bakersfield CA R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-21T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260141:269734:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lan Mi (`KXITFWMATCH-26OCT21SOHMIX-MIX`) | 0.86 / 0.87 (192) | 86.5% | 85.2% | 66.6% | 73.2% [72.7%-74.1%] | 86.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.3 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Margaret Sohns (`KXITFWMATCH-26OCT21SOHMIX-SOH`) | 0.11 / 0.14 (6166) | 12.5% | 14.8% | 33.4% | 26.8% [25.9%-27.3%] | 13.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.3 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 287.0, B 2699.0; serve-point win A 46.7%, B 45.5%; Elo A 1245.7, B 1429.6; model uncertainty 0.0067
* Form inputs: days since last match A 198, B 177; matches on record A 9, B 89; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sloane Stephens vs Thea Frodin -- W50 Austin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-21 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-21T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:201585:264140:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thea Frodin (`KXITFWMATCH-26OCT21STEFRO-FRO`) | 0.13 / 0.15 (6370) | 14.0% | 9.7% | 53.7% | 22.2% [8.6%-33.1%] | 16.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -4.3 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sloane Stephens (`KXITFWMATCH-26OCT21STEFRO-STE`) | 0.86 / 0.88 (1168) | 87.0% | 90.3% | 46.3% | 77.8% [66.9%-91.4%] | 83.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.3 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2061.0, B 1232.0; serve-point win A 61.2%, B 48.7%; Elo A 1813.0, B 1374.0; model uncertainty 0.1227
* Form inputs: days since last match A 33, B 50; matches on record A 685, B 36; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.030, surface_pool_high -0.037, surface_dev_loose -0.013, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Djosic / Kuhar vs Anthrop / Gogineni -- M15 Ithaca R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-22T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21DJOKUHANTGOG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anthrop / Gogineni (`KXITFDOUBLES-26OCT21DJOKUHANTGOG-ANTGOG`) | 0.05 / 0.92 (28) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Djosic / Kuhar (`KXITFDOUBLES-26OCT21DJOKUHANTGOG-DJOKUH`) | 0.05 / 0.22 (36) | 13.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jan Klimas vs Andreja Petrovic -- M15 Ithaca R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209914:213579:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jan Klimas (`KXITFMATCH-26OCT21KLIPET-KLI`) | 0.14 / 0.16 (6898) | 15.0% | 38.2% | 50.0% | 43.9% [43.9%-43.9%] | -- | -- | -- | -- | PASS | +23.2 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Andreja Petrovic (`KXITFMATCH-26OCT21KLIPET-PET`) | 0.84 / 0.86 (83) | 85.0% | 61.8% | 50.0% | 56.1% [56.1%-56.1%] | -- | -- | -- | -- | PASS | -23.2 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 60.8%, B 36.8%; Elo A 1293.8, B 1332.7; model uncertainty 0.0
* Form inputs: days since last match A 723, B 1206; matches on record A 3, B 12; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21KLIPET-KLI  (YES = Jan Klimas)
Model: 38%
Kalshi: 15%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Krall / Gabriel Papoe vs Barrett / Thomas George -- M15 Ithaca R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-22T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21KRAGABBARTHO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barrett / Thomas George (`KXITFDOUBLES-26OCT21KRAGABBARTHO-BARTHO`) | 0.06 / 0.69 (0) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Krall / Gabriel Papoe (`KXITFDOUBLES-26OCT21KRAGABBARTHO-KRAGAB`) | 0.05 / 0.82 (0) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Matheus Pucinelli de Almeida vs Nicolas Jarry -- ATP Challenger Cali R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-22T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111797:207799:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Jarry (`KXATPCHALLENGERMATCH-26OCT21PDAJAR-JAR`) | 0.49 / 0.50 (4) | 49.5% | 75.3% | 57.0% | 66.1% [62.3%-74.1%] | -- | -- | -- | -- | SHADOW_BET | +25.8 pp | EXTREME (DATA_WARNING) | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matheus Pucinelli de Almeida (`KXATPCHALLENGERMATCH-26OCT21PDAJAR-PDA`) | 0.49 / 0.50 (3022) | 49.5% | 24.7% | 43.0% | 33.9% [25.9%-37.7%] | -- | -- | -- | -- | PASS | -24.8 pp | HIGH_REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3555.0, B 3241.0; serve-point win A 60.5%, B 34.1%; Elo A 1598.3, B 1861.0; model uncertainty 0.0586
* Form inputs: days since last match A 16, B 191; matches on record A 371, B 718; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT21PDAJAR-JAR  (YES = Nicolas Jarry)
Model: 75%
Kalshi: 50%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Rethin Pranav Senthil Kumar vs Micah Braswell -- M15 Ithaca R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209334:213633:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Micah Braswell (`KXITFMATCH-26OCT21SENBRA-BRA`) | 0.69 / 0.72 (67) | 70.5% | 90.2% | 62.9% | 86.2% [86.2%-86.2%] | -- | -- | -- | -- | PASS | +19.7 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rethin Pranav Senthil Kumar (`KXITFMATCH-26OCT21SENBRA-SEN`) | 0.26 / 0.31 (21) | 28.5% | 9.8% | 37.1% | 13.8% [13.8%-13.8%] | -- | -- | -- | -- | PASS | -18.7 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 1799.0; serve-point win A 57.1%, B 32.7%; Elo A 1282.2, B 1598.9; model uncertainty 0.0
* Form inputs: days since last match A 709, B 709; matches on record A 4, B 62; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21SENBRA-BRA  (YES = Micah Braswell)
Model: 90%
Kalshi: 70%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Leticia Garcia Vidal vs Justina Maria Gonzalez Daniele -- W15 Campina Grande R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-22T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211592:260708:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leticia Garcia Vidal (`KXITFWMATCH-26OCT21GARGON-GAR`) | 0.13 / 0.15 (184) | 14.0% | 13.4% | 6.3% | 18.1% [12.2%-27.7%] | -- | -- | -- | -- | WATCH | -0.6 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Justina Maria Gonzalez Daniele (`KXITFWMATCH-26OCT21GARGON-GON`) | 0.85 / 0.88 (6124) | 86.5% | 86.6% | 93.7% | 82.0% [72.3%-87.8%] | -- | -- | -- | -- | PASS | +0.1 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 804.0, B 2911.0; serve-point win A 46.4%, B 45.4%; Elo A 1287.7, B 1445.0; model uncertainty 0.0779
* Form inputs: days since last match A 212, B 177; matches on record A 126, B 154; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.010, surface_dev_tight +0.018
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Niemeier / Ryser vs Brantmeier / Tanguilig -- W75 Saguenay QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-22T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21NIERYSBRATAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brantmeier / Tanguilig (`KXITFWDOUBLES-26OCT21NIERYSBRATAN-BRATAN`) | 0.08 / 0.80 (125) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Niemeier / Ryser (`KXITFWDOUBLES-26OCT21NIERYSBRATAN-NIERYS`) | 0.05 / 0.33 (37) | 19.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Mell Elizabeth Reasco Gonzalez vs Madison Brengle -- W50 Austin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:201483:221242:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Madison Brengle (`KXITFWMATCH-26OCT21REABRE-BRE`) | 0.82 / 0.83 (173) | 82.5% | 82.4% | 50.0% | 62.7% [58.0%-72.7%] | -- | -- | -- | -- | PASS | -0.1 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mell Elizabeth Reasco Gonzalez (`KXITFWMATCH-26OCT21REABRE-REA`) | 0.16 / 0.18 (6474) | 17.0% | 17.6% | 50.0% | 37.3% [27.3%-42.0%] | -- | -- | -- | -- | WATCH | +0.6 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2361.0, B 2464.0; serve-point win A 47.3%, B 45.8%; Elo A 1519.0, B 1752.5; model uncertainty 0.0736
* Form inputs: days since last match A 177, B 56; matches on record A 178, B 1012; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.015, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Allegre / Camila Torres Murcia vs Fairclough / Christine Lutkemeyer -- W35 Bakersfield CA R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-22T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21ALLCAMFAICHR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Allegre / Camila Torres Murcia (`KXITFWDOUBLES-26OCT21ALLCAMFAICHR-ALLCAM`) | 0.05 / 0.95 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fairclough / Christine Lutkemeyer (`KXITFWDOUBLES-26OCT21ALLCAMFAICHR-FAICHR`) | 0.06 / 0.95 (2) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Yara Bartashevich vs Ema Burgic -- W35 Bakersfield CA R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21BARBUR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yara Bartashevich (`KXITFWMATCH-26OCT21BARBUR-BAR`) | 0.49 / 0.51 (158) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ema Burgic (`KXITFWMATCH-26OCT21BARBUR-BUR`) | 0.49 / 0.52 (6126) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Duru Soke vs Berta Passola -- W35 Bakersfield CA R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:224488:260926:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Berta Passola (`KXITFWMATCH-26OCT21SOKPAS-PAS`) | 0.42 / 0.45 (4) | 43.5% | 51.9% | 52.1% | 59.5% [58.5%-61.1%] | -- | -- | -- | -- | PASS | +8.4 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Duru Soke (`KXITFWMATCH-26OCT21SOKPAS-SOK`) | 0.55 / 0.56 (126) | 55.5% | 48.1% | 47.9% | 40.5% [39.0%-41.5%] | -- | -- | -- | -- | PASS | -7.4 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 316.0, B 705.0; serve-point win A 53.4%, B 46.2%; Elo A 1387.3, B 1466.2; model uncertainty 0.0129
* Form inputs: days since last match A 303, B 429; matches on record A 71, B 48; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vivian Wolff vs Stefani Webb -- W35 Bakersfield CA R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215386:259567:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefani Webb (`KXITFWMATCH-26OCT21WOLWEB-WEB`) | 0.13 / 0.14 (0) | 13.5% | 12.1% | 41.5% | 28.2% [19.2%-32.4%] | -- | -- | -- | -- | PASS | -1.4 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Vivian Wolff (`KXITFWMATCH-26OCT21WOLWEB-WOL`) | 0.85 / 0.87 (64) | 86.0% | 87.9% | 58.5% | 71.8% [67.6%-80.8%] | -- | -- | -- | -- | PASS | +1.9 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2229.0, B 1878.0; serve-point win A 57.2%, B 51.5%; Elo A 1700.6, B 1405.8; model uncertainty 0.0661
* Form inputs: days since last match A 22, B 275; matches on record A 284, B 101; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gonzalo Bueno / Carlos Maria Zarate vs Juan Sebastian Gomez / Andres Urrea -- ATP Challenger Cali R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 01:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-22T01:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21BUEZARGOMURR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gonzalo Bueno / Carlos Maria Zarate (`KXATPCHALLENGERDOUBLES-26OCT21BUEZARGOMURR-BUEZAR`) | 0.06 / 0.94 (350) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Juan Sebastian Gomez / Andres Urrea (`KXATPCHALLENGERDOUBLES-26OCT21BUEZARGOMURR-GOMURR`) | 0.06 / 0.94 (850) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Collins / McDonald vs Osborne / Urhobo -- W50 Austin QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-22T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21COLMCDOSBURH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Collins / McDonald (`KXITFWDOUBLES-26OCT21COLMCDOSBURH-COLMCD`) | 0.08 / 0.77 (108) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Osborne / Urhobo (`KXITFWDOUBLES-26OCT21COLMCDOSBURH-OSBURH`) | 0.08 / 0.38 (40) | 23.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## El Jardi / Frodin vs Gomez Pezuela Cano / Shymanovich -- W50 Austin QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-22T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21ELJFROGOMSHY:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| El Jardi / Frodin (`KXITFWDOUBLES-26OCT21ELJFROGOMSHY-ELJFRO`) | 0.08 / 0.68 (78) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gomez Pezuela Cano / Shymanovich (`KXITFWDOUBLES-26OCT21ELJFROGOMSHY-GOMSHY`) | 0.08 / 0.49 (49) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Haddad / Hurkacz vs Chang / Rowley -- W35 Bakersfield CA R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-22T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21HADHURCHAROW:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chang / Rowley (`KXITFWDOUBLES-26OCT21HADHURCHAROW-CHAROW`) | 0.05 / 0.95 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Haddad / Hurkacz (`KXITFWDOUBLES-26OCT21HADHURCHAROW-HADHUR`) | 0.05 / 0.95 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ann Li vs Zeynep Sonmez -- WTA Osaka R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-21 05:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-22 02:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-22 01:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-21T05:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215983:220309:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ann Li (`KXWTAMATCH-26OCT20ANNSON-ANN`) | 0.63 / 0.65 (6876) | 64.0% | 59.1% | 52.6% | 55.2% [53.7%-56.3%] | -- | -- | -- | -- | PASS | -4.9 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zeynep Sonmez (`KXWTAMATCH-26OCT20ANNSON-SON`) | 0.36 / 0.37 (26989) | 36.5% | 40.9% | 47.4% | 44.8% [43.7%-46.3%] | -- | -- | -- | -- | SHADOW_BET | +4.4 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4567.0, B 4355.0; serve-point win A 57.7%, B 44.0%; Elo A 1915.2, B 1835.4; model uncertainty 0.0131
* Form inputs: days since last match A 1, B 1; matches on record A 472, B 428; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight +0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT20ANNSON-21` Over 20.5 games: 0.54/0.56 mid 55.0%, model 67.5% (projection_v2.0 (prediction ledger)) -- gap +12.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT20ANNSON-26` Over 25.5 games: 0.28/0.36 mid 32.0%, model 44.3% (projection_v2.0 (prediction ledger)) -- gap +12.3 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT20ANNSON-2-ANN` Will Ann Li win set 2 in the Ann Li vs Zeynep Sonmez match: 0.42/0.83 mid 62.5%, model 56.1% (projection_v2.0 (prediction ledger)) -- gap -6.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT20ANNSON-2-SON` Will Zeynep Sonmez win set 2 in the Ann Li vs Zeynep Sonmez match: 0.17/0.58 mid 37.5%, model 43.9% (projection_v2.0 (prediction ledger)) -- gap +6.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT20ANNSON-1-ANN` Will Ann Li win set 1 in the Ann Li vs Zeynep Sonmez match: 0.58/0.62 mid 60.0%, model 56.1% (projection_v2.0 (prediction ledger)) -- gap -3.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT20ANNSON-1-SON` Will Zeynep Sonmez win set 1 in the Ann Li vs Zeynep Sonmez match: 0.38/0.42 mid 40.0%, model 43.9% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT20ANNSON-16` Over 15.5 games: 0.92/0.97 mid 94.5%, model 97.2% (projection_v2.0 (prediction ledger)) -- gap +2.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Antonia Ruzic vs Kayla Day -- WTA Osaka R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-21 05:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-22 02:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-22 01:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-21T05:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215037:222045:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kayla Day (`KXWTAMATCH-26OCT20RUZDAY-DAY`) | 0.50 / 0.51 (272) | 50.5% | 48.3% | 71.3% | 61.8% [49.5%-66.2%] | -- | -- | -- | -- | WATCH | -2.2 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Antonia Ruzic (`KXWTAMATCH-26OCT20RUZDAY-RUZ`) | 0.48 / 0.50 (11882) | 49.0% | 51.7% | 28.7% | 38.2% [33.8%-50.5%] | -- | -- | -- | -- | PASS | +2.7 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4066.0, B 3639.0; serve-point win A 58.5%, B 41.8%; Elo A 1846.1, B 1750.6; model uncertainty 0.0837
* Form inputs: days since last match A 1, B 1; matches on record A 360, B 480; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.020, surface_dev_tight +0.015
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT20RUZDAY-27` Over 26.5 games: 0.23/0.34 mid 28.5%, model 40.7% (projection_v2.0 (prediction ledger)) -- gap +12.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT20RUZDAY-22` Over 21.5 games: 0.51/0.53 mid 52.0%, model 64.2% (projection_v2.0 (prediction ledger)) -- gap +12.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT20RUZDAY-17` Over 16.5 games: 0.86/0.95 mid 90.5%, model 94.7% (projection_v2.0 (prediction ledger)) -- gap +4.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT20RUZDAY-2-DAY` Will Kayla Day win set 2 in the Antonia Ruzic vs Kayla Day match: 0.31/0.71 mid 51.0%, model 48.9% (projection_v2.0 (prediction ledger)) -- gap -2.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT20RUZDAY-2-RUZ` Will Antonia Ruzic win set 2 in the Antonia Ruzic vs Kayla Day match: 0.29/0.69 mid 49.0%, model 51.1% (projection_v2.0 (prediction ledger)) -- gap +2.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT20RUZDAY-1-DAY` Will Kayla Day win set 1 in the Antonia Ruzic vs Kayla Day match: 0.47/0.51 mid 49.0%, model 48.9% (projection_v2.0 (prediction ledger)) -- gap -0.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT20RUZDAY-1-RUZ` Will Antonia Ruzic win set 1 in the Antonia Ruzic vs Kayla Day match: 0.49/0.53 mid 51.0%, model 51.1% (projection_v2.0 (prediction ledger)) -- gap +0.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Mary Stoiana vs Moyuka Uchijima -- WTA Osaka R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-21 05:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-22 04:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-22 03:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-21T05:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:220416:223168:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mary Stoiana (`KXWTAMATCH-26OCT20STOUCH-STO`) | 0.61 / 0.62 (1452) | 61.5% | 60.2% | 52.1% | 54.7% [53.7%-56.3%] | -- | -- | -- | -- | PASS | -1.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Moyuka Uchijima (`KXWTAMATCH-26OCT20STOUCH-UCH`) | 0.38 / 0.39 (515) | 38.5% | 39.8% | 47.9% | 45.3% [43.7%-46.3%] | -- | -- | -- | -- | SHADOW_BET | +1.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2840.0, B 4591.0; serve-point win A 58.2%, B 43.8%; Elo A 1812.8, B 1745.8; model uncertainty 0.013
* Form inputs: days since last match A 1, B 1; matches on record A 143, B 474; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.016, surface_dev_loose +0.010, surface_dev_tight +0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT20STOUCH-15` Over 14.5 games: 0.27/0.99 mid 63.0%, model 99.1% (projection_v2.0 (prediction ledger)) -- gap +36.1 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT20STOUCH-20` Over 19.5 games: 0.52/0.65 mid 58.5%, model 74.1% (projection_v2.0 (prediction ledger)) -- gap +15.6 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT20STOUCH-25` Over 24.5 games: 0.31/0.39 mid 35.0%, model 48.7% (projection_v2.0 (prediction ledger)) -- gap +13.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT20STOUCH-1-STO` Will Mary Stoiana win set 1 in the Mary Stoiana vs Moyuka Uchijima match: 0.59/0.62 mid 60.5%, model 56.8% (projection_v2.0 (prediction ledger)) -- gap -3.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT20STOUCH-1-UCH` Will Moyuka Uchijima win set 1 in the Mary Stoiana vs Moyuka Uchijima match: 0.38/0.42 mid 40.0%, model 43.2% (projection_v2.0 (prediction ledger)) -- gap +3.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT20STOUCH-2-STO` Will Mary Stoiana win set 2 in the Mary Stoiana vs Moyuka Uchijima match: 0.39/0.80 mid 59.5%, model 56.8% (projection_v2.0 (prediction ledger)) -- gap -2.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT20STOUCH-2-UCH` Will Moyuka Uchijima win set 2 in the Mary Stoiana vs Moyuka Uchijima match: 0.22/0.59 mid 40.5%, model 43.2% (projection_v2.0 (prediction ledger)) -- gap +2.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ingrid Neel / Giuliana Olmos vs Isabelle Haverlag / Lilli Tagger -- WTA Osaka QF

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-10-22 05:30Z
* Current expected start: 2026-10-22 04:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-22 03:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-22T05:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21NEEOLMHAVTAG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isabelle Haverlag / Lilli Tagger (`KXWTADOUBLES-26OCT21NEEOLMHAVTAG-HAVTAG`) | 0.31 / 0.34 (44) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ingrid Neel / Giuliana Olmos (`KXWTADOUBLES-26OCT21NEEOLMHAVTAG-NEEOLM`) | 0.68 / 0.69 (2464) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Kajsa Rinaldo Persson vs Clemence Mercier -- W75 Saguenay R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 04:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T04:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211643:260855:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Clemence Mercier (`KXITFWMATCH-26OCT21RINMER-MER`) | 0.11 / 0.12 (7994) | 11.5% | 5.1% | 28.9% | 10.8% [8.8%-12.3%] | -- | -- | -- | -- | PASS | -6.4 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kajsa Rinaldo Persson (`KXITFWMATCH-26OCT21RINMER-RIN`) | 0.87 / 0.88 (26) | 87.5% | 94.9% | 71.1% | 89.2% [87.7%-91.2%] | -- | -- | -- | -- | PASS | +7.4 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3104.0, B 263.0; serve-point win A 62.6%, B 49.9%; Elo A 1755.2, B 1340.0; model uncertainty 0.0175
* Form inputs: days since last match A 28, B 373; matches on record A 430, B 26; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Iva Jovic vs Jasmine Paolini -- WTA Ningbo R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-21 08:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-22 05:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-22 04:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-21T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211148:260300:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iva Jovic (`KXWTAMATCH-26OCT21JOVPAO-JOV`) | 0.64 / 0.65 (159) | 64.5% | 61.6% | 63.9% | 59.9% [48.9%-63.4%] | -- | -- | -- | -- | PASS | -2.9 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jasmine Paolini (`KXWTAMATCH-26OCT21JOVPAO-PAO`) | 0.35 / 0.36 (31564) | 35.5% | 38.4% | 36.1% | 40.1% [36.6%-51.0%] | -- | -- | -- | -- | WATCH | +2.9 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3602.0, B 4852.0; serve-point win A 58.6%, B 43.7%; Elo A 1998.5, B 2007.2; model uncertainty 0.0722
* Form inputs: days since last match A 6, B 1; matches on record A 170, B 712; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.010, surface_dev_loose +0.015, surface_dev_tight -0.020
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT21JOVPAO-26` Over 25.5 games: 0.25/0.34 mid 29.5%, model 44.1% (projection_v2.0 (prediction ledger)) -- gap +14.6 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT21JOVPAO-21` Over 20.5 games: 0.52/0.54 mid 53.0%, model 67.3% (projection_v2.0 (prediction ledger)) -- gap +14.3 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT21JOVPAO-1-JOV` Will Iva Jovic win set 1 in the Iva Jovic vs Jasmine Paolini match: 0.61/0.64 mid 62.5%, model 57.8% (projection_v2.0 (prediction ledger)) -- gap -4.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT21JOVPAO-1-PAO` Will Jasmine Paolini win set 1 in the Iva Jovic vs Jasmine Paolini match: 0.36/0.41 mid 38.5%, model 42.2% (projection_v2.0 (prediction ledger)) -- gap +3.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT21JOVPAO-2-PAO` Will Jasmine Paolini win set 2 in the Iva Jovic vs Jasmine Paolini match: 0.20/0.58 mid 39.0%, model 42.2% (projection_v2.0 (prediction ledger)) -- gap +3.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT21JOVPAO-16` Over 15.5 games: 0.92/0.97 mid 94.5%, model 97.2% (projection_v2.0 (prediction ledger)) -- gap +2.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT21JOVPAO-2-JOV` Will Iva Jovic win set 2 in the Iva Jovic vs Jasmine Paolini match: 0.42/0.76 mid 59.0%, model 57.8% (projection_v2.0 (prediction ledger)) -- gap -1.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Leyla Fiorella Britez Risso vs Miho Kuramochi -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222513:246478:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leyla Fiorella Britez Risso (`KXITFWMATCH-26OCT21BRIKUR-BRI`) | 0.57 / 0.67 (37) | 62.0% | 26.3% | 14.8% | 27.3% [24.3%-30.0%] | -- | -- | -- | -- | PASS | -35.7 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Miho Kuramochi (`KXITFWMATCH-26OCT21BRIKUR-KUR`) | 0.33 / 0.36 (40) | 34.5% | 73.7% | 85.2% | 72.7% [70.0%-75.7%] | -- | -- | -- | -- | PASS | +39.2 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 257.0, B 3111.0; serve-point win A 49.9%, B 45.3%; Elo A 1408.3, B 1555.6; model uncertainty 0.0288
* Form inputs: days since last match A 863, B 31; matches on record A 44, B 279; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21BRIKUR-KUR  (YES = Miho Kuramochi)
Model: 74%
Kalshi: 34%
Gap: +39 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.030, surface_pool_high +0.027, surface_dev_loose -0.009, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuno Kitahara vs I Wen Wan -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:263881:267449:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuno Kitahara (`KXITFWMATCH-26OCT21KITWAN-KIT`) | 0.33 / 0.43 (13) | 38.0% | 79.6% | 78.2% | 72.3% [69.5%-75.7%] | -- | -- | -- | -- | PASS | +41.6 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| I Wen Wan (`KXITFWMATCH-26OCT21KITWAN-WAN`) | 0.56 / 0.61 (92) | 58.5% | 20.4% | 21.8% | 27.7% [24.3%-30.5%] | -- | -- | -- | -- | PASS | -38.1 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2068.0, B 553.0; serve-point win A 55.2%, B 51.0%; Elo A 1428.6, B 1276.4; model uncertainty 0.0314
* Form inputs: days since last match A 184, B 233; matches on record A 119, B 26; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21KITWAN-KIT  (YES = Yuno Kitahara)
Model: 80%
Kalshi: 38%
Gap: +42 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.009, surface_dev_loose +0.004, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tahlia Kokkinis vs Ava Beck -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260667:269872:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ava Beck (`KXITFWMATCH-26OCT21KOKBEC-BEC`) | 0.03 / 0.13 (79) | 8.0% | 7.6% | 5.9% | 13.5% [9.7%-18.6%] | -- | -- | -- | -- | PASS | -0.4 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tahlia Kokkinis (`KXITFWMATCH-26OCT21KOKBEC-KOK`) | 0.74 / 0.92 (39) | 83.0% | 92.4% | 94.1% | 86.5% [81.4%-90.3%] | -- | -- | -- | -- | PASS | +9.4 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1935.0, B 734.0; serve-point win A 60.6%, B 50.2%; Elo A 1514.8, B 1267.0; model uncertainty 0.0449
* Form inputs: days since last match A 155, B 212; matches on record A 101, B 15; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high -0.009, surface_dev_loose +0.011, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sera Nishimoto vs Vaidehee Chaudhari -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21NISCHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vaidehee Chaudhari (`KXITFWMATCH-26OCT21NISCHA-CHA`) | 0.76 / 0.85 (6194) | 80.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sera Nishimoto (`KXITFWMATCH-26OCT21NISCHA-NIS`) | 0.03 / 0.20 (5) | 11.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Magda Linette vs Katerina Siniakova -- WTA Osaka R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-21 05:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-22 05:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-22 04:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-21T05:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202663:211701:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Magda Linette (`KXWTAMATCH-26OCT20LINSIN-LIN`) | 0.34 / 0.35 (1296) | 34.5% | 35.8% | 27.8% | 32.3% [30.4%-36.1%] | -- | -- | -- | -- | PASS | +1.3 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Katerina Siniakova (`KXWTAMATCH-26OCT20LINSIN-SIN`) | 0.65 / 0.66 (7938) | 65.5% | 64.2% | 72.2% | 67.7% [63.9%-69.5%] | -- | -- | -- | -- | PASS | -1.3 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4278.0, B 4278.0; serve-point win A 56.5%, B 40.7%; Elo A 1878.3, B 1917.6; model uncertainty 0.0284
* Form inputs: days since last match A 1, B 1; matches on record A 910, B 721; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.009, surface_dev_loose -0.009, surface_dev_tight +0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT20LINSIN-15` Over 14.5 games: 0.62/0.99 mid 80.5%, model 99.1% (projection_v2.0 (prediction ledger)) -- gap +18.6 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT20LINSIN-20` Over 19.5 games: 0.61/0.62 mid 61.5%, model 73.7% (projection_v2.0 (prediction ledger)) -- gap +12.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT20LINSIN-25` Over 24.5 games: 0.32/0.44 mid 38.0%, model 48.1% (projection_v2.0 (prediction ledger)) -- gap +10.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT20LINSIN-2-LIN` Will Magda Linette win set 2 in the Magda Linette vs Katerina Siniakova match: 0.30/0.42 mid 36.0%, model 40.4% (projection_v2.0 (prediction ledger)) -- gap +4.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT20LINSIN-2-SIN` Will Katerina Siniakova win set 2 in the Magda Linette vs Katerina Siniakova match: 0.59/0.69 mid 64.0%, model 59.6% (projection_v2.0 (prediction ledger)) -- gap -4.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT20LINSIN-1-LIN` Will Magda Linette win set 1 in the Magda Linette vs Katerina Siniakova match: 0.36/0.40 mid 38.0%, model 40.4% (projection_v2.0 (prediction ledger)) -- gap +2.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT20LINSIN-1-SIN` Will Katerina Siniakova win set 1 in the Magda Linette vs Katerina Siniakova match: 0.60/0.64 mid 62.0%, model 59.6% (projection_v2.0 (prediction ledger)) -- gap -2.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Emma Dong vs Ayana Akli -- W75 Saguenay R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 05:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T05:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264149:266761:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ayana Akli (`KXITFWMATCH-26OCT21DONAKL-AKL`) | 0.71 / 0.75 (125) | 73.0% | 94.7% | 70.3% | 85.7% [85.7%-85.7%] | -- | -- | -- | -- | PASS | +21.7 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Emma Dong (`KXITFWMATCH-26OCT21DONAKL-DON`) | 0.22 / 0.30 (75) | 26.0% | 5.3% | 29.7% | 14.3% [14.3%-14.3%] | -- | -- | -- | -- | PASS | -20.7 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 2838.0; serve-point win A 48.4%, B 39.4%; Elo A 1307.0, B 1616.6; model uncertainty 0.0
* Form inputs: days since last match A 723, B 30; matches on record A 7, B 123; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21DONAKL-AKL  (YES = Ayana Akli)
Model: 95%
Kalshi: 73%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hanyu Guo / Kristina Mladenovic vs Ellen Perez / Demi Schuurs -- WTA Ningbo QF

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-10-22 08:00Z
* Current expected start: 2026-10-22 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-22 05:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-22T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT22GUOMLAPERSCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hanyu Guo / Kristina Mladenovic (`KXWTADOUBLES-26OCT22GUOMLAPERSCH-GUOMLA`) | 0.61 / 0.65 (429) | 63.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ellen Perez / Demi Schuurs (`KXWTADOUBLES-26OCT22GUOMLAPERSCH-PERSCH`) | 0.35 / 0.39 (481) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Oscar Brown vs Toshiki Karigyo -- M15 Tanagura R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21BROKAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oscar Brown (`KXITFMATCH-26OCT21BROKAR-BRO`) | 0.81 / 0.84 (1089) | 82.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Toshiki Karigyo (`KXITFMATCH-26OCT21BROKAR-KAR`) | 0.14 / 0.20 (6203) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Herman Hoeyeraal vs Moerani Bouzige -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207728:208382:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Moerani Bouzige (`KXITFMATCH-26OCT21HOEBOU-BOU`) | 0.53 / 0.55 (32) | 54.0% | 83.6% | 50.0% | 73.5% [72.2%-73.7%] | -- | -- | -- | -- | PASS | +29.6 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Herman Hoeyeraal (`KXITFMATCH-26OCT21HOEBOU-HOE`) | 0.43 / 0.47 (29) | 45.0% | 16.4% | 50.0% | 26.6% [26.4%-27.8%] | -- | -- | -- | -- | PASS | -28.6 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 74.0, B 1093.0; serve-point win A 59.4%, B 32.8%; Elo A 1211.8, B 1397.2; model uncertainty 0.0072
* Form inputs: days since last match A 107, B 674; matches on record A 8, B 213; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21HOEBOU-BOU  (YES = Moerani Bouzige)
Model: 84%
Kalshi: 54%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chun-Chien Hou vs Kanta Watanabe -- M15 Tanagura R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21HOUWAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chun-Chien Hou (`KXITFMATCH-26OCT21HOUWAT-HOU`) | 0.35 / 0.39 (75) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kanta Watanabe (`KXITFMATCH-26OCT21HOUWAT-WAT`) | 0.62 / 0.65 (6182) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hyu Kawanishi vs Yu Tanaka -- M15 Tanagura R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212092:213213:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hyu Kawanishi (`KXITFMATCH-26OCT21KAWTAN-KAW`) | 0.35 / 0.39 (55) | 37.0% | 45.1% | 50.0% | 51.0% [51.0%-51.0%] | -- | -- | -- | -- | PASS | +8.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Yu Tanaka (`KXITFMATCH-26OCT21KAWTAN-TAN`) | 0.59 / 0.63 (44) | 61.0% | 54.9% | 50.0% | 49.0% [49.0%-49.0%] | -- | -- | -- | -- | PASS | -6.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 61.5%, B 37.5%; Elo A 1272.3, B 1266.3; model uncertainty 0.0
* Form inputs: days since last match A 772, B 940; matches on record A 1, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Noritaka Koizumi vs Takuya Kumasaka -- M15 Tanagura R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207998:212476:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Noritaka Koizumi (`KXITFMATCH-26OCT21KOIKUM-KOI`) | 0.27 / 0.30 (332) | 28.5% | 23.1% | 63.0% | 40.9% [40.9%-40.9%] | -- | -- | -- | -- | PASS | -5.4 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Takuya Kumasaka (`KXITFMATCH-26OCT21KOIKUM-KUM`) | 0.69 / 0.72 (25) | 70.5% | 76.9% | 37.0% | 59.1% [59.1%-59.1%] | -- | -- | -- | -- | PASS | +6.4 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 862.0; serve-point win A 58.2%, B 36.0%; Elo A 1273.5, B 1338.1; model uncertainty 0.0002
* Form inputs: days since last match A 821, B 72; matches on record A 3, B 151; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sam Ryan Ziegann vs Enzo Aguiard -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208160:212174:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Enzo Aguiard (`KXITFMATCH-26OCT21RYAAGU-AGU`) | 0.80 / 0.84 (51) | 82.0% | 74.1% | 42.5% | 73.7% [71.9%-74.5%] | -- | -- | -- | -- | PASS | -7.9 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sam Ryan Ziegann (`KXITFMATCH-26OCT21RYAAGU-RYA`) | 0.16 / 0.18 (16) | 17.0% | 25.9% | 57.5% | 26.4% [25.5%-28.1%] | -- | -- | -- | -- | PASS | +8.9 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 85.0, B 258.0; serve-point win A 60.1%, B 34.8%; Elo A 1144.2, B 1335.8; model uncertainty 0.0129
* Form inputs: days since last match A 44, B 37; matches on record A 51, B 19; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anton Shepp vs Isaac Becroft -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208653:209394:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isaac Becroft (`KXITFMATCH-26OCT21SHEBEC-BEC`) | 0.41 / 0.47 (39) | 44.0% | 68.7% | 57.5% | 67.6% [67.6%-68.5%] | -- | -- | -- | -- | PASS | +24.7 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anton Shepp (`KXITFMATCH-26OCT21SHEBEC-SHE`) | 0.53 / 0.55 (37) | 54.0% | 31.3% | 42.5% | 32.4% [31.4%-32.4%] | -- | -- | -- | -- | PASS | -22.7 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 349.0, B 69.0; serve-point win A 60.4%, B 35.7%; Elo A 1243.3, B 1375.8; model uncertainty 0.0049
* Form inputs: days since last match A 31, B 653; matches on record A 20, B 70; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21SHEBEC-BEC  (YES = Isaac Becroft)
Model: 69%
Kalshi: 44%
Gap: +25 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Naiktha Bains vs Alana Subasic -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206362:261049:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naiktha Bains (`KXITFWMATCH-26OCT21BAISUB-BAI`) | 0.77 / 0.84 (88) | 80.5% | 73.0% | 60.0% | 61.6% [58.5%-68.5%] | -- | -- | -- | -- | PASS | -7.5 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alana Subasic (`KXITFWMATCH-26OCT21BAISUB-SUB`) | 0.04 / 0.20 (24) | 12.0% | 27.1% | 40.0% | 38.5% [31.5%-41.5%] | -- | -- | -- | -- | PASS | +15.1 pp | HIGH_REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2400.0, B 2964.0; serve-point win A 56.6%, B 48.0%; Elo A 1570.3, B 1463.4; model uncertainty 0.0501
* Form inputs: days since last match A 27, B 177; matches on record A 483, B 101; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21BAISUB-SUB  (YES = Alana Subasic)
Model: 27%
Kalshi: 12%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: WIDE_SPREAD, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.035, surface_pool_high -0.031, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Monique Barry vs Ya Yi Yang -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222390:222667:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Monique Barry (`KXITFWMATCH-26OCT21BARYAN-BAR`) | 0.03 / 0.16 (78) | 9.5% | 25.8% | 23.5% | 27.4% [25.2%-31.5%] | -- | -- | -- | -- | PASS | +16.3 pp | HIGH_REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ya Yi Yang (`KXITFWMATCH-26OCT21BARYAN-YAN`) | 0.84 / 0.89 (76) | 86.5% | 74.2% | 76.4% | 72.6% [68.5%-74.8%] | -- | -- | -- | -- | PASS | -12.3 pp | REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1840.0, B 1965.0; serve-point win A 51.7%, B 43.5%; Elo A 1331.5, B 1456.4; model uncertainty 0.0315
* Form inputs: days since last match A 212, B 191; matches on record A 209, B 226; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21BARYAN-BAR  (YES = Monique Barry)
Model: 26%
Kalshi: 10%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: WIDE_SPREAD, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose -0.018, surface_dev_tight +0.018
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nanari Katsumi vs Hikaru Sato -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221141:253679:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nanari Katsumi (`KXITFWMATCH-26OCT21KATSAT-KAT`) | 0.08 / 0.11 (45) | 9.5% | 21.6% | 38.6% | 29.5% [27.1%-31.8%] | -- | -- | -- | -- | PASS | +12.1 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hikaru Sato (`KXITFWMATCH-26OCT21KATSAT-SAT`) | 0.89 / 0.92 (6164) | 90.5% | 78.4% | 61.4% | 70.5% [68.2%-72.9%] | -- | -- | -- | -- | PASS | -12.1 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1096.0, B 1807.0; serve-point win A 54.3%, B 39.7%; Elo A 1260.6, B 1465.8; model uncertainty 0.0234
* Form inputs: days since last match A 212, B 184; matches on record A 139, B 175; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.005, surface_dev_loose -0.004, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mio Mushika vs Erika Sema -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:202454:222986:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mio Mushika (`KXITFWMATCH-26OCT21MUSSEM-MUS`) | 0.62 / 0.67 (41) | 64.5% | 68.3% | 68.5% | 62.6% [55.3%-66.5%] | -- | -- | -- | -- | PASS | +3.8 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Erika Sema (`KXITFWMATCH-26OCT21MUSSEM-SEM`) | 0.28 / 0.37 (80) | 32.5% | 31.7% | 31.5% | 37.4% [33.5%-44.7%] | -- | -- | -- | -- | PASS | -0.8 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2224.0, B 1873.0; serve-point win A 55.8%, B 47.8%; Elo A 1520.7, B 1485.0; model uncertainty 0.0562
* Form inputs: days since last match A 184, B 177; matches on record A 201, B 930; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Terence Atmane vs Mattia Bellucci -- ATP Almaty R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-22 09:30Z
* Current expected start: 2026-10-22 06:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-22 05:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-10-22T09:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208233:209279:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Terence Atmane (`KXATPMATCH-26OCT22ATMBEL-ATM`) | 0.39 / 0.40 (829) | 39.5% | 34.7% | 37.4% | 39.2% [37.4%-41.0%] | -- | 38.8% | 38.8% | MARKETS_AGREE | PASS | -4.8 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Mattia Bellucci (`KXATPMATCH-26OCT22ATMBEL-BEL`) | 0.59 / 0.61 (270) | 60.0% | 65.3% | 62.6% | 60.8% [59.0%-62.6%] | -- | 59.8% | -- | INSUFFICIENT_INPUTS | PASS | +5.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4446.0, B 4581.0; serve-point win A 66.4%, B 30.3%; Elo A 1769.8, B 1813.1; model uncertainty 0.0183
* Form inputs: days since last match A 1, B 0; matches on record A 398, B 398; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.018, surface_pool_high +0.018, surface_dev_loose -0.004, surface_dev_tight +0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT22ATMBEL-BEL20` Will Mattia Bellucci win the Terence Atmane vs Mattia Bellucci match by a set score of 2-0?: 0.04/0.48 mid 26.0%, model 36.4% (projection_v2.0 (prediction ledger)) -- gap +10.4 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT22ATMBEL-2-ATM` Will Terence Atmane win set 2 in the Terence Atmane vs Mattia Bellucci match: 0.03/0.97 mid 50.0%, model 39.6% (projection_v2.0 (prediction ledger)) -- gap -10.3 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT22ATMBEL-2-BEL` Will Mattia Bellucci win set 2 in the Terence Atmane vs Mattia Bellucci match: 0.03/0.97 mid 50.0%, model 60.4% (projection_v2.0 (prediction ledger)) -- gap +10.3 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT22ATMBEL-23` Over 22.5 games: 0.54/0.56 mid 55.0%, model 64.8% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT22ATMBEL-18` Over 17.5 games: 0.75/0.98 mid 86.5%, model 96.3% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT22ATMBEL-28` Over 27.5 games: 0.29/0.38 mid 33.5%, model 43.2% (projection_v2.0 (prediction ledger)) -- gap +9.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT22ATMBEL-ATM2` Will Terence Atmane win at least 1.5 more games than Mattia Bellucci?: 0.31/0.38 mid 34.5%, model 27.1% (projection_v2.0 (prediction ledger)) -- gap -7.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT22ATMBEL-BEL21` Will Mattia Bellucci win the Terence Atmane vs Mattia Bellucci match by a set score of 2-1?: 0.03/0.44 mid 23.5%, model 28.9% (projection_v2.0 (prediction ledger)) -- gap +5.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT22ATMBEL-ATM20` Will Terence Atmane win the Terence Atmane vs Mattia Bellucci match by a set score of 2-0?: 0.03/0.37 mid 20.0%, model 15.7% (projection_v2.0 (prediction ledger)) -- gap -4.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT22ATMBEL-BEL2` Will Mattia Bellucci win at least 1.5 more games than Terence Atmane?: 0.54/0.55 mid 54.5%, model 57.0% (projection_v2.0 (prediction ledger)) -- gap +2.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT22ATMBEL-BEL5` Will Mattia Bellucci win at least 4.5 more games than Terence Atmane?: 0.11/0.22 mid 16.5%, model 18.9% (projection_v2.0 (prediction ledger)) -- gap +2.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT22ATMBEL-1-ATM` Will Terence Atmane win set 1 in the Terence Atmane vs Mattia Bellucci match: 0.40/0.44 mid 42.0%, model 39.6% (projection_v2.0 (prediction ledger)) -- gap -2.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT22ATMBEL-1-BEL` Will Mattia Bellucci win set 1 in the Terence Atmane vs Mattia Bellucci match: 0.57/0.60 mid 58.5%, model 60.4% (projection_v2.0 (prediction ledger)) -- gap +1.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT22ATMBEL-ATM21` Will Terence Atmane win the Terence Atmane vs Mattia Bellucci match by a set score of 2-1?: 0.04/0.37 mid 20.5%, model 19.0% (projection_v2.0 (prediction ledger)) -- gap -1.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alexander Donski / Filip Pieczonka vs Yuki Bhambri / Ryan Seggerman -- ATP Almaty QF

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-10-22 09:30Z
* Current expected start: 2026-10-22 06:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-22 05:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-22T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT22DONPIEBHASEG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuki Bhambri / Ryan Seggerman (`KXATPDOUBLES-26OCT22DONPIEBHASEG-BHASEG`) | 0.51 / 0.54 (273) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexander Donski / Filip Pieczonka (`KXATPDOUBLES-26OCT22DONPIEBHASEG-DONPIE`) | 0.45 / 0.48 (263) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Katarzyna Kawa vs Belinda Bencic -- WTA Ningbo R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-22 08:00Z
* Current expected start: 2026-10-22 06:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-22 05:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-90_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-22T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202505:203514:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Belinda Bencic (`KXWTAMATCH-26OCT22KAWBEN-BEN`) | 0.88 / 0.89 (1235) | 88.5% | 92.0% | 94.9% | 94.5% [91.6%-95.7%] | 87.7% | 89.3% | 88.5% | MARKETS_AGREE | SHADOW_BET | +3.5 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Katarzyna Kawa (`KXWTAMATCH-26OCT22KAWBEN-KAW`) | 0.10 / 0.11 (4499) | 10.5% | 8.0% | 5.1% | 5.5% [4.3%-8.4%] | 12.3% | 10.0% | 11.2% | MARKETS_AGREE | PASS | -2.5 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4311.0, B 3571.0; serve-point win A 50.5%, B 38.9%; Elo A 1613.7, B 2076.7; model uncertainty 0.0206
* Form inputs: days since last match A 1, B 1; matches on record A 704, B 675; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.001, surface_pool_high +0.000, surface_dev_loose -0.012, surface_dev_tight +0.016
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 6 carry a model probability
  * `KXWTAGTOTAL-26OCT22KAWBEN-19` Over 18.5 games: 0.47/0.48 mid 47.5%, model 58.3% (projection_v2.0 (prediction ledger)) -- gap +10.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT22KAWBEN-24` Over 23.5 games: 0.15/0.29 mid 22.0%, model 29.0% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT22KAWBEN-2-BEN` Will Belinda Bencic win set 2 in the Katarzyna Kawa vs Belinda Bencic match: 0.61/0.97 mid 79.0%, model 82.7% (projection_v2.0 (prediction ledger)) -- gap +3.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT22KAWBEN-2-KAW` Will Katarzyna Kawa win set 2 in the Katarzyna Kawa vs Belinda Bencic match: 0.03/0.39 mid 21.0%, model 17.3% (projection_v2.0 (prediction ledger)) -- gap -3.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT22KAWBEN-1-BEN` Will Belinda Bencic win set 1 in the Katarzyna Kawa vs Belinda Bencic match: 0.82/0.85 mid 83.5%, model 82.7% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT22KAWBEN-1-KAW` Will Katarzyna Kawa win set 1 in the Katarzyna Kawa vs Belinda Bencic match: 0.15/0.19 mid 17.0%, model 17.3% (projection_v2.0 (prediction ledger)) -- gap +0.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; WIDE_SPREAD

## Chen Dong vs Philip Sekulic -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210340:211317:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chen Dong (`KXITFMATCH-26OCT21DONSEK-DON`) | 0.06 / 0.10 (13) | 8.0% | 24.9% | 44.4% | 32.4% [32.4%-32.4%] | -- | -- | -- | -- | PASS | +16.9 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Philip Sekulic (`KXITFMATCH-26OCT21DONSEK-SEK`) | 0.87 / 0.94 (6320) | 90.5% | 75.1% | 55.6% | 67.6% [67.6%-67.6%] | -- | -- | -- | -- | PASS | -15.4 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 2777.0; serve-point win A 59.3%, B 35.3%; Elo A 1386.1, B 1513.1; model uncertainty 0.0
* Form inputs: days since last match A 674, B 29; matches on record A 12, B 238; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21DONSEK-DON  (YES = Chen Dong)
Model: 25%
Kalshi: 8%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yusuke Kusuhara vs Makoto Ochi -- M15 Tanagura R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200024:211550:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yusuke Kusuhara (`KXITFMATCH-26OCT21KUSOCH-KUS`) | 0.51 / 0.55 (80) | 53.0% | 29.6% | 40.5% | 31.5% [30.6%-32.0%] | -- | -- | -- | -- | PASS | -23.4 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Makoto Ochi (`KXITFMATCH-26OCT21KUSOCH-OCH`) | 0.44 / 0.50 (50) | 47.0% | 70.4% | 59.5% | 68.5% [68.0%-69.5%] | -- | -- | -- | -- | PASS | +23.4 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 93.0, B 985.0; serve-point win A 60.5%, B 35.3%; Elo A 1207.0, B 1345.7; model uncertainty 0.0072
* Form inputs: days since last match A 716, B 674; matches on record A 18, B 501; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21KUSOCH-OCH  (YES = Makoto Ochi)
Model: 70%
Kalshi: 47%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Markus Malaszszak vs Jumpei Yamasaki -- M15 Tanagura R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126135:212308:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Markus Malaszszak (`KXITFMATCH-26OCT21MALYAM-MAL`) | 0.30 / 0.35 (85) | 32.5% | 30.5% | 56.6% | 35.1% [35.1%-35.1%] | -- | -- | -- | -- | PASS | -2.0 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Jumpei Yamasaki (`KXITFMATCH-26OCT21MALYAM-YAM`) | 0.66 / 0.70 (61) | 68.0% | 69.5% | 43.4% | 64.9% [64.9%-64.9%] | -- | -- | -- | -- | PASS | +1.5 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 123.0; serve-point win A 59.6%, B 36.4%; Elo A 1229.7, B 1331.4; model uncertainty 0.0003
* Form inputs: days since last match A 730, B 891; matches on record A 13, B 314; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuto Oki vs Shotaro Yamamoto -- M15 Tanagura R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21OKIYAM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuto Oki (`KXITFMATCH-26OCT21OKIYAM-OKI`) | 0.65 / 0.95 (5536) | 80.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Shotaro Yamamoto (`KXITFMATCH-26OCT21OKIYAM-YAM`) | 0.03 / 0.17 (23) | 10.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hikaru Shiraishi vs Hugo Hashimoto -- M15 Tanagura R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202113:213074:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Hashimoto (`KXITFMATCH-26OCT21SHIHAS-HAS`) | 0.24 / 0.32 (37) | 28.0% | 31.5% | 64.1% | 33.0% [32.3%-33.1%] | -- | -- | -- | -- | PASS | +3.5 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Hikaru Shiraishi (`KXITFMATCH-26OCT21SHIHAS-SHI`) | 0.68 / 0.73 (70) | 70.5% | 68.5% | 35.9% | 67.0% [66.9%-67.7%] | -- | -- | -- | -- | PASS | -2.0 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 743.0, B 0.0; serve-point win A 61.9%, B 41.8%; Elo A 1444.2, B 1315.4; model uncertainty 0.0043
* Form inputs: days since last match A 695, B 828; matches on record A 113, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Li Tu vs Casey Hoole -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111454:211315:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Casey Hoole (`KXITFMATCH-26OCT21TUXHOO-HOO`) | 0.34 / 0.38 (24) | 36.0% | 23.2% | 43.0% | 19.4% [17.0%-22.0%] | -- | -- | -- | -- | PASS | -12.8 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Li Tu (`KXITFMATCH-26OCT21TUXHOO-TUX`) | 0.62 / 0.66 (85) | 64.0% | 76.8% | 57.0% | 80.6% [78.0%-83.0%] | -- | -- | -- | -- | PASS | +12.8 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2962.0, B 175.0; serve-point win A 66.6%, B 39.2%; Elo A 1649.3, B 1374.7; model uncertainty 0.0252
* Form inputs: days since last match A 60, B 674; matches on record A 309, B 16; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Barry / Sato vs Di Tommaso / Nishimoto -- W35 Sydney QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-22T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21BARSATDITNIS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barry / Sato (`KXITFWDOUBLES-26OCT21BARSATDITNIS-BARSAT`) | 0.08 / 0.82 (138) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Di Tommaso / Nishimoto (`KXITFWDOUBLES-26OCT21BARSATDITNIS-DITNIS`) | 0.05 / 0.37 (39) | 21.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Sohns / Walker vs Chan / Ma -- W35 Bakersfield CA R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-22T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21SOHWALCHAMAX:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chan / Ma (`KXITFWDOUBLES-26OCT21SOHWALCHAMAX-CHAMAX`) | 0.05 / 0.95 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sohns / Walker (`KXITFWDOUBLES-26OCT21SOHWALCHAMAX-SOHWAL`) | 0.05 / 0.95 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Cristina Bucsa / Nicole Melichar-Martinez vs Leylah Fernandez / Marta Kostyuk -- WTA Ningbo QF

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-10-22 08:00Z
* Current expected start: 2026-10-22 07:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-22 06:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-22T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT22BUCMELFERKOS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cristina Bucsa / Nicole Melichar-Martinez (`KXWTADOUBLES-26OCT22BUCMELFERKOS-BUCMEL`) | 0.57 / 0.61 (2248) | 59.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Leylah Fernandez / Marta Kostyuk (`KXWTADOUBLES-26OCT22BUCMELFERKOS-FERKOS`) | 0.39 / 0.43 (21) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Adams / Dodaj vs Stevens / Thompson -- W35 Sydney QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 07:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-22T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21ADADODSTETHO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adams / Dodaj (`KXITFWDOUBLES-26OCT21ADADODSTETHO-ADADOD`) | 0.05 / 0.95 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stevens / Thompson (`KXITFWDOUBLES-26OCT21ADADODSTETHO-STETHO`) | 0.05 / 0.95 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Violet Apisah vs Jiho Shin -- W15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21APISHI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Violet Apisah (`KXITFWMATCH-26OCT21APISHI-API`) | 0.03 / 0.97 (105) | 50.0% | 51.0% | -- | -- [-----] | -- | -- | -- | -- | -- | +1.0 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Jiho Shin (`KXITFWMATCH-26OCT21APISHI-SHI`) | 0.03 / 0.97 (105) | 50.0% | 49.0% | -- | -- [-----] | -- | -- | -- | -- | -- | -1.0 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 56.7%, B 43.5%; Elo A 1379.7, B 1319.5; model uncertainty None
* Form inputs: days since last match A 2813, B 177; matches on record A 2, B 152; data quality F
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aulia / Fiorella Britez Risso vs Hosoki / Tse -- W35 Sydney QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 07:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-22T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21AULFIOHOSTSE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aulia / Fiorella Britez Risso (`KXITFWDOUBLES-26OCT21AULFIOHOSTSE-AULFIO`) | 0.05 / 0.95 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hosoki / Tse (`KXITFWDOUBLES-26OCT21AULFIOHOSTSE-HOSTSE`) | 0.05 / 0.95 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Danilova / Liu vs Beck / Sibai -- W35 Sydney QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 07:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-22T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21DANLIUBECSIB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Beck / Sibai (`KXITFWDOUBLES-26OCT21DANLIUBECSIB-BECSIB`) | 0.05 / 0.92 (30) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Danilova / Liu (`KXITFWDOUBLES-26OCT21DANLIUBECSIB-DANLIU`) | 0.05 / 0.95 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kurea Hayasaka vs Kai Ning Chanya Ng -- W15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21HAYNGX:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kurea Hayasaka (`KXITFWMATCH-26OCT21HAYNGX-HAY`) | 0.03 / 0.97 (105) | 50.0% | 73.3% | -- | -- [-----] | -- | -- | -- | -- | -- | +23.3 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Kai Ning Chanya Ng (`KXITFWMATCH-26OCT21HAYNGX-NGX`) | 0.03 / 0.97 (105) | 50.0% | 26.7% | -- | -- [-----] | -- | -- | -- | -- | -- | -23.3 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 57.5%, B 47.2%; Elo A 1229.3, B 1192.4; model uncertainty None
* Form inputs: days since last match A 191, B 32; matches on record A 9, B 5; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21HAYNGX-HAY  (YES = Kurea Hayasaka)
Model: 73%
Kalshi: 50%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rion Itaya vs Fang An Lin -- W15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21ITALIN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rion Itaya (`KXITFWMATCH-26OCT21ITALIN-ITA`) | 0.03 / 0.97 (105) | 50.0% | 32.1% | -- | -- [-----] | -- | -- | -- | -- | -- | -17.9 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Fang An Lin (`KXITFWMATCH-26OCT21ITALIN-LIN`) | 0.03 / 0.97 (105) | 50.0% | 67.9% | -- | -- [-----] | -- | -- | -- | -- | -- | +17.9 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 52.7%, B 43.8%; Elo A 1251.7, B 1341.7; model uncertainty None
* Form inputs: days since last match A 352, B 184; matches on record A 6, B 114; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21ITALIN-LIN  (YES = Fang An Lin)
Model: 68%
Kalshi: 50%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ekaterina Khodzhaeva vs Thasaporn Naklo -- W15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21KHONAK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Khodzhaeva (`KXITFWMATCH-26OCT21KHONAK-KHO`) | 0.03 / 0.97 (105) | 50.0% | 16.7% | -- | -- [-----] | -- | -- | -- | -- | -- | -33.3 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Thasaporn Naklo (`KXITFWMATCH-26OCT21KHONAK-NAK`) | 0.03 / 0.97 (105) | 50.0% | 83.3% | -- | -- [-----] | -- | -- | -- | -- | -- | +33.3 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 50.1%, B 42.6%; Elo A 1270.1, B 1456.9; model uncertainty None
* Form inputs: days since last match A 177, B 177; matches on record A 13, B 166; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21KHONAK-NAK  (YES = Thasaporn Naklo)
Model: 83%
Kalshi: 50%
Gap: +33 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aruzhan Sagandykova vs Moeka Miyata -- W15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21SAGMIY:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Moeka Miyata (`KXITFWMATCH-26OCT21SAGMIY-MIY`) | 0.03 / 0.97 (105) | 50.0% | 46.1% | -- | -- [-----] | -- | -- | -- | -- | -- | -3.9 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Aruzhan Sagandykova (`KXITFWMATCH-26OCT21SAGMIY-SAG`) | 0.03 / 0.97 (105) | 50.0% | 53.9% | -- | -- [-----] | -- | -- | -- | -- | -- | +3.9 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 57.3%, B 43.4%; Elo A 1403.7, B 1398.3; model uncertainty None
* Form inputs: days since last match A 25, B 219; matches on record A 45, B 42; data quality D
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tomas Machac vs Karen Khachanov -- ATP Almaty R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-22 11:00Z
* Current expected start: 2026-10-22 08:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-22 07:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-10-22T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111575:207830:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karen Khachanov (`KXATPMATCH-26OCT22MACKHA-KHA`) | 0.68 / 0.70 (19449) | 69.0% | 63.0% | 75.7% | 70.0% [66.6%-72.5%] | -- | -- | -- | -- | PASS | -6.0 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tomas Machac (`KXATPMATCH-26OCT22MACKHA-MAC`) | 0.31 / 0.32 (447) | 31.5% | 37.0% | 24.3% | 30.0% [27.5%-33.4%] | -- | -- | -- | -- | PASS | +5.5 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3720.0, B 5284.0; serve-point win A 64.6%, B 32.7%; Elo A 1922.0, B 1944.3; model uncertainty 0.0299
* Form inputs: days since last match A 0, B 1; matches on record A 444, B 752; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.009, surface_dev_loose -0.004, surface_dev_tight +0.017
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT22MACKHA-24` Over 23.5 games: 0.42/0.44 mid 43.0%, model 54.7% (projection_v2.0 (prediction ledger)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT22MACKHA-2-MAC` Will Tomas Machac win set 2 in the Tomas Machac vs Karen Khachanov match: 0.21/0.40 mid 30.5%, model 41.2% (projection_v2.0 (prediction ledger)) -- gap +10.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT22MACKHA-29` Over 28.5 games: 0.24/0.31 mid 27.5%, model 37.7% (projection_v2.0 (prediction ledger)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT22MACKHA-KHA3` Will Karen Khachanov win at least 2.5 more games than Tomas Machac?: 0.54/0.56 mid 55.0%, model 46.5% (projection_v2.0 (prediction ledger)) -- gap -8.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT22MACKHA-19` Over 18.5 games: 0.78/0.87 mid 82.5%, model 90.2% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT22MACKHA-KHA6` Will Karen Khachanov win at least 5.5 more games than Tomas Machac?: 0.13/0.24 mid 18.5%, model 10.8% (projection_v2.0 (prediction ledger)) -- gap -7.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT22MACKHA-KHA21` Will Karen Khachanov win the Tomas Machac vs Karen Khachanov match by a set score of 2-1?: 0.06/0.37 mid 21.5%, model 28.5% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT22MACKHA-1-KHA` Will Karen Khachanov win set 1 in the Tomas Machac vs Karen Khachanov match: 0.62/0.66 mid 64.0%, model 58.8% (projection_v2.0 (prediction ledger)) -- gap -5.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT22MACKHA-1-MAC` Will Tomas Machac win set 1 in the Tomas Machac vs Karen Khachanov match: 0.34/0.38 mid 36.0%, model 41.2% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT22MACKHA-2-KHA` Will Karen Khachanov win set 2 in the Tomas Machac vs Karen Khachanov match: 0.57/0.70 mid 63.5%, model 58.8% (projection_v2.0 (prediction ledger)) -- gap -4.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT22MACKHA-MAC2` Will Tomas Machac win at least 1.5 more games than Karen Khachanov?: 0.21/0.29 mid 25.0%, model 29.7% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT22MACKHA-KHA20` Will Karen Khachanov win the Tomas Machac vs Karen Khachanov match by a set score of 2-0?: 0.23/0.47 mid 35.0%, model 34.5% (projection_v2.0 (prediction ledger)) -- gap -0.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alexandra Eala vs Diana Shnaider -- WTA Ningbo R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-21 08:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-22 08:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-22 07:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-21T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:223253:223670:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandra Eala (`KXWTAMATCH-26OCT21EALSHN-EAL`) | 0.40 / 0.42 (39575) | 41.0% | 48.9% | 46.8% | 46.8% [44.2%-48.4%] | -- | -- | -- | -- | SHADOW_BET | +7.9 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Diana Shnaider (`KXWTAMATCH-26OCT21EALSHN-SHN`) | 0.58 / 0.60 (32341) | 59.0% | 51.1% | 53.2% | 53.2% [51.6%-55.8%] | -- | -- | -- | -- | PASS | -7.9 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4541.0, B 4846.0; serve-point win A 56.8%, B 43.0%; Elo A 1960.0, B 1972.3; model uncertainty 0.021
* Form inputs: days since last match A 2, B 1; matches on record A 366, B 321; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.016, surface_dev_loose +0.005, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT21EALSHN-21` Over 20.5 games: 0.53/0.54 mid 53.5%, model 68.3% (projection_v2.0 (prediction ledger)) -- gap +14.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT21EALSHN-26` Over 25.5 games: 0.28/0.37 mid 32.5%, model 45.0% (projection_v2.0 (prediction ledger)) -- gap +12.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT21EALSHN-2-EAL` Will Alexandra Eala win set 2 in the Alexandra Eala vs Diana Shnaider match: 0.23/0.59 mid 41.0%, model 49.3% (projection_v2.0 (prediction ledger)) -- gap +8.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT21EALSHN-2-SHN` Will Diana Shnaider win set 2 in the Alexandra Eala vs Diana Shnaider match: 0.37/0.76 mid 56.5%, model 50.7% (projection_v2.0 (prediction ledger)) -- gap -5.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT21EALSHN-1-EAL` Will Alexandra Eala win set 1 in the Alexandra Eala vs Diana Shnaider match: 0.42/0.46 mid 44.0%, model 49.3% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT21EALSHN-1-SHN` Will Diana Shnaider win set 1 in the Alexandra Eala vs Diana Shnaider match: 0.54/0.58 mid 56.0%, model 50.7% (projection_v2.0 (prediction ledger)) -- gap -5.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT21EALSHN-16` Over 15.5 games: 0.92/0.97 mid 94.5%, model 97.4% (projection_v2.0 (prediction ledger)) -- gap +2.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Atkinson / Bouzige vs Cook / Walkin -- M25 Tamworth QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-22T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21ATKBOUCOOWAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Atkinson / Bouzige (`KXITFDOUBLES-26OCT21ATKBOUCOOWAL-ATKBOU`) | 0.05 / 0.95 (38) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cook / Walkin (`KXITFDOUBLES-26OCT21ATKBOUCOOWAL-COOWAL`) | 0.05 / 0.95 (38) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Timofei Derepasko vs Linang Xiao -- M15 Shenzhen R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209038:212157:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Timofei Derepasko (`KXITFMATCH-26OCT21DERXIA-DER`) | 0.51 / 0.54 (83) | 52.5% | 28.4% | 41.9% | 36.5% [34.5%-38.0%] | -- | -- | -- | -- | PASS | -24.1 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Linang Xiao (`KXITFMATCH-26OCT21DERXIA-XIA`) | 0.42 / 0.50 (50) | 46.0% | 71.6% | 58.1% | 63.5% [62.0%-65.5%] | -- | -- | -- | -- | PASS | +25.6 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 262.0, B 607.0; serve-point win A 59.1%, B 36.5%; Elo A 1241.9, B 1346.7; model uncertainty 0.017
* Form inputs: days since last match A 37, B 16; matches on record A 12, B 99; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21DERXIA-XIA  (YES = Linang Xiao)
Model: 72%
Kalshi: 46%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.019, surface_dev_loose -0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ruochen Gao vs Daniil Sarksian -- M15 Shenzhen R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21GAOSAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ruochen Gao (`KXITFMATCH-26OCT21GAOSAR-GAO`) | 0.09 / 0.12 (5) | 10.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daniil Sarksian (`KXITFMATCH-26OCT21GAOSAR-SAR`) | 0.88 / 0.91 (152) | 89.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xirui Han vs Filip Peliwo -- M15 Shenzhen R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106290:212472:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xirui Han (`KXITFMATCH-26OCT21HANPEL-HAN`) | 0.08 / 0.21 (13) | 14.5% | 29.0% | 71.0% | 33.1% [30.3%-35.0%] | -- | -- | -- | -- | PASS | +14.5 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Filip Peliwo (`KXITFMATCH-26OCT21HANPEL-PEL`) | 0.76 / 0.83 (107) | 79.5% | 71.0% | 29.0% | 66.9% [65.0%-69.7%] | -- | -- | -- | -- | PASS | -8.5 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 952.0; serve-point win A 58.2%, B 37.5%; Elo A 1259.6, B 1382.6; model uncertainty 0.0238
* Form inputs: days since last match A 765, B 37; matches on record A 5, B 732; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.028, surface_dev_loose -0.001, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luca Staeheli vs Maxim Shin -- M15 Shenzhen R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207664:210535:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maxim Shin (`KXITFMATCH-26OCT21STASHI-SHI`) | 0.08 / 0.16 (6) | 12.0% | 30.1% | 56.7% | 46.9% [43.9%-47.9%] | -- | -- | -- | -- | PASS | +18.1 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luca Staeheli (`KXITFMATCH-26OCT21STASHI-STA`) | 0.81 / 0.94 (451) | 87.5% | 69.9% | 43.3% | 53.1% [52.1%-56.1%] | -- | -- | -- | -- | PASS | -17.6 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 545.0, B 81.0; serve-point win A 61.8%, B 42.2%; Elo A 1265.3, B 1234.1; model uncertainty 0.0203
* Form inputs: days since last match A 23, B 450; matches on record A 65, B 50; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21STASHI-SHI  (YES = Maxim Shin)
Model: 30%
Kalshi: 12%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.005, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Wishaya Trongcharoenchaikul vs Kuan-Shou Chen -- M15 Shenzhen R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21TROCHE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kuan-Shou Chen (`KXITFMATCH-26OCT21TROCHE-CHE`) | 0.82 / 0.85 (23) | 83.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Wishaya Trongcharoenchaikul (`KXITFMATCH-26OCT21TROCHE-TRO`) | 0.15 / 0.19 (68) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yujia Huang vs Xinxin Yao -- W35 Qian Daohu R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:252587:264207:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yujia Huang (`KXITFWMATCH-26OCT21HUAYAO-HUA`) | 0.49 / 0.52 (70) | 50.5% | 29.6% | 64.5% | 48.9% [36.5%-55.8%] | -- | -- | -- | -- | PASS | -20.9 pp | HIGH_REVIEW | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Xinxin Yao (`KXITFWMATCH-26OCT21HUAYAO-YAO`) | 0.43 / 0.52 (49) | 47.5% | 70.4% | 35.5% | 51.1% [44.2%-63.5%] | -- | -- | -- | -- | PASS | +22.9 pp | HIGH_REVIEW | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1640.0, B 2972.0; serve-point win A 53.9%, B 42.1%; Elo A 1447.1, B 1573.7; model uncertainty 0.0967
* Form inputs: days since last match A 17, B 16; matches on record A 88, B 320; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21HUAYAO-YAO  (YES = Xinxin Yao)
Model: 70%
Kalshi: 48%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Allegra Korpanec Davies vs Lea Ma -- W35 Bakersfield CA R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221220:260914:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Allegra Korpanec Davies (`KXITFWMATCH-26OCT21KORMAX-KOR`) | 0.07 / 0.11 (6144) | 9.0% | 9.8% | 20.1% | 17.0% [15.7%-18.6%] | 12.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.8 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lea Ma (`KXITFWMATCH-26OCT21KORMAX-MAX`) | 0.89 / 0.92 (116) | 90.5% | 90.2% | 79.9% | 83.0% [81.4%-84.3%] | 87.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.3 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1796.0, B 2727.0; serve-point win A 53.0%, B 37.1%; Elo A 1332.2, B 1655.2; model uncertainty 0.0145
* Form inputs: days since last match A 177, B 38; matches on record A 48, B 168; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yidi Yang vs Chengyiyi Yuan -- W35 Qian Daohu R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215134:215820:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yidi Yang (`KXITFWMATCH-26OCT21YANYUA-YAN`) | 0.58 / 0.62 (85) | 60.0% | 68.3% | 55.9% | 59.5% [58.0%-62.1%] | -- | -- | -- | -- | PASS | +8.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Chengyiyi Yuan (`KXITFWMATCH-26OCT21YANYUA-YUA`) | 0.34 / 0.42 (2) | 38.0% | 31.7% | 44.1% | 40.5% [37.9%-42.0%] | -- | -- | -- | -- | PASS | -6.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3495.0, B 2947.0; serve-point win A 55.6%, B 47.9%; Elo A 1589.5, B 1478.6; model uncertainty 0.0206
* Form inputs: days since last match A 17, B 24; matches on record A 317, B 239; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Junhan Zhang vs Jiaqi Wang -- W35 Qian Daohu R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221181:260694:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jiaqi Wang (`KXITFWMATCH-26OCT21ZHAWAN-WAN`) | 0.51 / 0.59 (5) | 55.0% | 74.9% | 82.5% | 78.1% [71.6%-81.0%] | -- | -- | -- | -- | PASS | +19.9 pp | HIGH_REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Junhan Zhang (`KXITFWMATCH-26OCT21ZHAWAN-ZHA`) | 0.40 / 0.45 (71) | 42.5% | 25.1% | 17.5% | 21.9% [18.9%-28.4%] | -- | -- | -- | -- | PASS | -17.4 pp | HIGH_REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2226.0, B 2849.0; serve-point win A 54.8%, B 40.1%; Elo A 1384.4, B 1543.7; model uncertainty 0.0475
* Form inputs: days since last match A 23, B 177; matches on record A 95, B 250; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21ZHAWAN-WAN  (YES = Jiaqi Wang)
Model: 75%
Kalshi: 55%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.004, surface_dev_loose -0.011, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rada Zolotareva vs Junlu Sun -- W35 Qian Daohu R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260951:264970:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Junlu Sun (`KXITFWMATCH-26OCT21ZOLSUN-SUN`) | 0.04 / 0.09 (7) | 6.5% | 3.7% | 27.8% | 16.8% [13.6%-20.3%] | -- | -- | -- | -- | PASS | -2.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Rada Zolotareva (`KXITFWMATCH-26OCT21ZOLSUN-ZOL`) | 0.89 / 0.94 (166) | 91.5% | 96.3% | 72.2% | 83.2% [79.7%-86.4%] | -- | -- | -- | -- | PASS | +4.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1811.0, B 0.0; serve-point win A 59.8%, B 53.6%; Elo A 1579.7, B 1304.4; model uncertainty 0.0334
* Form inputs: days since last match A 44, B 765; matches on record A 96, B 15; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.031, surface_pool_high -0.036, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexey Aleshchev vs Pranav Karthik -- M15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 08:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21ALEKAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexey Aleshchev (`KXITFMATCH-26OCT21ALEKAR-ALE`) | 0.03 / 0.97 (78) | 50.0% | 20.4% | -- | -- [-----] | -- | -- | -- | -- | -- | -29.6 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Pranav Karthik (`KXITFMATCH-26OCT21ALEKAR-KAR`) | 0.03 / 0.97 (78) | 50.0% | 79.6% | -- | -- [-----] | -- | -- | -- | -- | -- | +29.6 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 58.4%, B 35.1%; Elo A 1045.3, B 1300.4; model uncertainty None
* Form inputs: days since last match A 331, B 702; matches on record A 43, B 4; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21ALEKAR-KAR  (YES = Pranav Karthik)
Model: 80%
Kalshi: 50%
Gap: +30 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Noah Karma vs Taisei Ichikawa -- M15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 08:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21KARICH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Taisei Ichikawa (`KXITFMATCH-26OCT21KARICH-ICH`) | 0.03 / 0.97 (105) | 50.0% | 72.9% | -- | -- [-----] | -- | -- | -- | -- | -- | +22.9 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Noah Karma (`KXITFMATCH-26OCT21KARICH-KAR`) | 0.03 / 0.97 (105) | 50.0% | 27.1% | -- | -- [-----] | -- | -- | -- | -- | -- | -22.9 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 57.9%, B 37.4%; Elo A 1251.4, B 1329.6; model uncertainty None
* Form inputs: days since last match A 709, B 695; matches on record A 2, B 170; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21KARICH-ICH  (YES = Taisei Ichikawa)
Model: 73%
Kalshi: 50%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yeri Hong vs Yingqun Sun -- W15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 08:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21HONSUN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yeri Hong (`KXITFWMATCH-26OCT21HONSUN-HON`) | 0.03 / 0.97 (105) | 50.0% | 25.7% | -- | -- [-----] | -- | -- | -- | -- | -- | -24.3 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Yingqun Sun (`KXITFWMATCH-26OCT21HONSUN-SUN`) | 0.03 / 0.97 (105) | 50.0% | 74.3% | -- | -- [-----] | -- | -- | -- | -- | -- | +24.3 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 52.0%, B 43.1%; Elo A 1309.3, B 1387.9; model uncertainty None
* Form inputs: days since last match A 177, B 177; matches on record A 4, B 99; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21HONSUN-SUN  (YES = Yingqun Sun)
Model: 74%
Kalshi: 50%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jing-Jing Lu vs Hong Yi Cody Wong -- W15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 08:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21LUXWON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jing-Jing Lu (`KXITFWMATCH-26OCT21LUXWON-LUX`) | 0.03 / 0.95 (32) | 49.0% | 29.6% | -- | -- [-----] | -- | -- | -- | -- | -- | -19.4 pp | HIGH_REVIEW (DATA_WARNING) | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Hong Yi Cody Wong (`KXITFWMATCH-26OCT21LUXWON-WON`) | 0.03 / 0.97 (105) | 50.0% | 70.3% | -- | -- [-----] | -- | -- | -- | -- | -- | +20.4 pp | HIGH_REVIEW (DATA_WARNING) | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 52.8%, B 43.2%; Elo A 1463.4, B 1531.8; model uncertainty None
* Form inputs: days since last match A 198, B 59; matches on record A 544, B 280; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21LUXWON-WON  (YES = Hong Yi Cody Wong)
Model: 70%
Kalshi: 50%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: WIDE_SPREAD, EVENT_MAPPING_RISK, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexandra Malova vs Melany Solange Krywoj -- W15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 08:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT21MALKRY:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Melany Solange Krywoj (`KXITFWMATCH-26OCT21MALKRY-KRY`) | 0.03 / 0.97 (105) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexandra Malova (`KXITFWMATCH-26OCT21MALKRY-MAL`) | 0.03 / 0.97 (105) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mikalai Haliak vs You Du -- M15 Shenzhen R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144915:213610:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| You Du (`KXITFMATCH-26OCT21HALDUX-DUX`) | 0.06 / 0.09 (20) | 7.5% | 27.7% | 79.2% | 38.9% [36.0%-42.9%] | -- | -- | -- | -- | PASS | +20.2 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mikalai Haliak (`KXITFMATCH-26OCT21HALDUX-HAL`) | 0.81 / 0.95 (79) | 88.0% | 72.3% | 20.8% | 61.1% [57.1%-64.0%] | -- | -- | -- | -- | PASS | -15.7 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2107.0, B 0.0; serve-point win A 64.0%, B 40.6%; Elo A 1351.0, B 1274.6; model uncertainty 0.0344
* Form inputs: days since last match A 702, B 730; matches on record A 302, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21HALDUX-DUX  (YES = You Du)
Model: 28%
Kalshi: 8%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.029, surface_pool_high -0.040, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lin Hao-Yu vs Corban Crowther -- M15 Shenzhen R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21HAOCRO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Corban Crowther (`KXITFMATCH-26OCT21HAOCRO-CRO`) | 0.57 / 0.96 (22) | 76.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lin Hao-Yu (`KXITFMATCH-26OCT21HAOCRO-HAO`) | 0.03 / 0.36 (15) | 19.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Takahata / Tanaka vs Fukuda / Noguchi -- M15 Tanagura QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-22T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21TAKTANFUKNOG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fukuda / Noguchi (`KXITFDOUBLES-26OCT21TAKTANFUKNOG-FUKNOG`) | 0.05 / 0.95 (38) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Takahata / Tanaka (`KXITFDOUBLES-26OCT21TAKTANFUKNOG-TAKTAN`) | 0.05 / 0.95 (38) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Yue Xia vs Boris Butulija -- M15 Shenzhen R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21XIABUT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Boris Butulija (`KXITFMATCH-26OCT21XIABUT-BUT`) | 0.05 / 0.68 (4) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yue Xia (`KXITFMATCH-26OCT21XIABUT-XIA`) | 0.28 / 0.49 (2) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daria KHOMUTSIANSKAYA vs Meiqi Guo -- W35 Qian Daohu R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216162:222944:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Meiqi Guo (`KXITFWMATCH-26OCT21KHOGUO-GUO`) | 0.04 / 0.22 (6) | 13.0% | 24.6% | 11.1% | 17.2% [14.1%-28.0%] | -- | -- | -- | -- | PASS | +11.6 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daria KHOMUTSIANSKAYA (`KXITFWMATCH-26OCT21KHOGUO-KHO`) | 0.68 / 0.94 (6449) | 81.0% | 75.4% | 88.9% | 82.8% [72.0%-85.9%] | -- | -- | -- | -- | PASS | -5.6 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3178.0, B 2729.0; serve-point win A 59.8%, B 45.4%; Elo A 1665.8, B 1542.5; model uncertainty 0.0696
* Form inputs: days since last match A 275, B 24; matches on record A 171, B 272; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.010, surface_dev_loose +0.009, surface_dev_tight -0.017
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xi Luo vs Jiangxue HAN -- W35 Qian Daohu R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220497:264069:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jiangxue HAN (`KXITFWMATCH-26OCT21LUOHAN-HAN`) | 0.36 / 0.44 (0) | 40.0% | 42.1% | 28.6% | 45.7% [39.4%-54.3%] | -- | -- | -- | -- | PASS | +2.1 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Xi Luo (`KXITFWMATCH-26OCT21LUOHAN-LUO`) | 0.55 / 0.59 (4) | 57.0% | 57.9% | 71.4% | 54.3% [45.7%-60.6%] | -- | -- | -- | -- | PASS | +0.9 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 827.0, B 1410.0; serve-point win A 51.0%, B 50.5%; Elo A 1415.7, B 1458.9; model uncertainty 0.0744
* Form inputs: days since last match A 177, B 177; matches on record A 43, B 174; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.016, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Varvara Panshina vs Chihiro Muramatsu -- W35 Qian Daohu R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214540:267420:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chihiro Muramatsu (`KXITFWMATCH-26OCT21PANMUR-MUR`) | 0.04 / 0.94 (416) | 49.0% | 24.9% | 19.9% | 27.8% [23.9%-36.4%] | -- | -- | -- | -- | PASS | -24.1 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Varvara Panshina (`KXITFWMATCH-26OCT21PANMUR-PAN`) | 0.03 / 0.96 (625) | 49.5% | 75.1% | 80.1% | 72.2% [63.6%-76.1%] | -- | -- | -- | -- | PASS | +25.6 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2447.0, B 1483.0; serve-point win A 55.1%, B 50.0%; Elo A 1546.4, B 1453.5; model uncertainty 0.0625
* Form inputs: days since last match A 100, B 289; matches on record A 102, B 418; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT21PANMUR-PAN  (YES = Varvara Panshina)
Model: 75%
Kalshi: 50%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.000, surface_dev_loose +0.009, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Wushuang Zheng vs Priska Madelyn Nugroho -- W35 Qian Daohu R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213821:221187:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Priska Madelyn Nugroho (`KXITFWMATCH-26OCT21ZHENUG-NUG`) | 0.04 / 0.94 (416) | 49.0% | 52.9% | 75.2% | 66.5% [54.8%-71.7%] | -- | -- | -- | -- | PASS | +3.9 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Wushuang Zheng (`KXITFWMATCH-26OCT21ZHENUG-ZHE`) | 0.03 / 0.96 (625) | 49.5% | 47.1% | 24.8% | 33.5% [28.3%-45.2%] | -- | -- | -- | -- | PASS | -2.4 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2161.0, B 2457.0; serve-point win A 54.2%, B 45.2%; Elo A 1552.0, B 1567.2; model uncertainty 0.0845
* Form inputs: days since last match A 15, B 205; matches on record A 302, B 235; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniil Medvedev vs Sho Shimabukuro -- ATP Almaty R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-21 09:30Z
* Current expected start: 2026-10-22 09:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-22 08:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1440_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-10-21T09:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:106421:200647:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniil Medvedev (`KXATPMATCH-26OCT21MEDSHI-MED`) | 0.91 / 0.92 (4603) | 91.5% | 89.9% | 93.8% | 93.3% [92.5%-93.8%] | -- | -- | -- | -- | WATCH | -1.6 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sho Shimabukuro (`KXATPMATCH-26OCT21MEDSHI-SHI`) | 0.08 / 0.09 (6063) | 8.5% | 10.1% | 6.2% | 6.7% [6.2%-7.5%] | -- | -- | -- | -- | PASS | +1.6 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5908.0, B 4312.0; serve-point win A 68.5%, B 41.7%; Elo A 2100.3, B 1679.7; model uncertainty 0.0065
* Form inputs: days since last match A 4, B 1; matches on record A 858, B 434; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.002, surface_pool_high -0.002, surface_dev_loose +0.003, surface_dev_tight -0.007
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT21MEDSHI-MED9` Will Daniil Medvedev win at least 8.5 more games than Sho Shimabukuro?: 0.04/0.28 mid 16.0%, model 4.6% (projection_v2.0 (prediction ledger)) -- gap -11.4 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT21MEDSHI-15` Over 14.5 games: 0.77/0.99 mid 88.0%, model 98.6% (projection_v2.0 (prediction ledger)) -- gap +10.6 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT21MEDSHI-20` Over 19.5 games: 0.52/0.54 mid 53.0%, model 62.2% (projection_v2.0 (prediction ledger)) -- gap +9.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21MEDSHI-MED21` Will Daniil Medvedev win the Daniil Medvedev vs Sho Shimabukuro match by a set score of 2-1?: 0.14/0.20 mid 17.0%, model 25.4% (projection_v2.0 (prediction ledger)) -- gap +8.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21MEDSHI-MED20` Will Daniil Medvedev win the Daniil Medvedev vs Sho Shimabukuro match by a set score of 2-0?: 0.70/0.75 mid 72.5%, model 64.5% (projection_v2.0 (prediction ledger)) -- gap -8.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT21MEDSHI-25` Over 24.5 games: 0.23/0.28 mid 25.5%, model 33.4% (projection_v2.0 (prediction ledger)) -- gap +7.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT21MEDSHI-MED6` Will Daniil Medvedev win at least 5.5 more games than Sho Shimabukuro?: 0.44/0.45 mid 44.5%, model 37.1% (projection_v2.0 (prediction ledger)) -- gap -7.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT21MEDSHI-2-MED` Will Daniil Medvedev win set 2 in the Daniil Medvedev vs Sho Shimabukuro match: 0.78/0.93 mid 85.5%, model 80.3% (projection_v2.0 (prediction ledger)) -- gap -5.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT21MEDSHI-MED3` Will Daniil Medvedev win at least 2.5 more games than Sho Shimabukuro?: 0.77/0.92 mid 84.5%, model 80.8% (projection_v2.0 (prediction ledger)) -- gap -3.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT21MEDSHI-1-SHI` Will Sho Shimabukuro win set 1 in the Daniil Medvedev vs Sho Shimabukuro match: 0.15/0.17 mid 16.0%, model 19.7% (projection_v2.0 (prediction ledger)) -- gap +3.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT21MEDSHI-1-MED` Will Daniil Medvedev win set 1 in the Daniil Medvedev vs Sho Shimabukuro match: 0.82/0.85 mid 83.5%, model 80.3% (projection_v2.0 (prediction ledger)) -- gap -3.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21MEDSHI-SHI21` Will Sho Shimabukuro win the Daniil Medvedev vs Sho Shimabukuro match by a set score of 2-1?: 0.01/0.06 mid 3.5%, model 6.2% (projection_v2.0 (prediction ledger)) -- gap +2.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT21MEDSHI-2-SHI` Will Sho Shimabukuro win set 2 in the Daniil Medvedev vs Sho Shimabukuro match: 0.11/0.24 mid 17.5%, model 19.7% (projection_v2.0 (prediction ledger)) -- gap +2.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21MEDSHI-SHI20` Will Sho Shimabukuro win the Daniil Medvedev vs Sho Shimabukuro match by a set score of 2-0?: 0.01/0.06 mid 3.5%, model 3.9% (projection_v2.0 (prediction ledger)) -- gap +0.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Thanapet Chanta vs Arnav Paparkar -- M25 Mumbai R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 09:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21CHAPAP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thanapet Chanta (`KXITFMATCH-26OCT21CHAPAP-CHA`) | 0.05 / 0.95 (7) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arnav Paparkar (`KXITFMATCH-26OCT21CHAPAP-PAP`) | 0.04 / 0.96 (7) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Adhithya Ganesan vs Digvijay Pratap Singh -- M25 Mumbai R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 09:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21GANSIN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adhithya Ganesan (`KXITFMATCH-26OCT21GANSIN-GAN`) | 0.05 / 0.95 (4) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Digvijay Pratap Singh (`KXITFMATCH-26OCT21GANSIN-SIN`) | 0.04 / 0.96 (4) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Karan Singh vs Adil Kalyanpur -- M25 Mumbai R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 09:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200681:210000:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adil Kalyanpur (`KXITFMATCH-26OCT21SINKAL-KAL`) | 0.04 / 0.71 (31) | 37.5% | 23.0% | 62.3% | 25.7% [24.1%-27.4%] | -- | -- | -- | -- | PASS | -14.5 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Karan Singh (`KXITFMATCH-26OCT21SINKAL-SIN`) | 0.20 / 0.97 (342) | 58.5% | 77.0% | 37.7% | 74.3% [72.6%-75.9%] | -- | -- | -- | -- | PASS | +18.5 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1167.0, B 84.0; serve-point win A 66.5%, B 39.4%; Elo A 1330.3, B 1128.5; model uncertainty 0.0161
* Form inputs: days since last match A 86, B 555; matches on record A 179, B 139; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21SINKAL-SIN  (YES = Karan Singh)
Model: 77%
Kalshi: 58%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Manish Sureshkumar vs Garrett Johns -- M25 Mumbai R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 09:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200176:208143:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Garrett Johns (`KXITFMATCH-26OCT21SURJOH-JOH`) | 0.05 / 0.95 (9) | 50.0% | 75.0% | 63.5% | 70.0% [67.3%-73.1%] | -- | -- | -- | -- | PASS | +25.0 pp | EXTREME (DATA_WARNING) | AGING | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Manish Sureshkumar (`KXITFMATCH-26OCT21SURJOH-SUR`) | 0.04 / 0.96 (9) | 50.0% | 25.0% | 36.5% | 30.0% [26.9%-32.7%] | -- | -- | -- | -- | PASS | -25.0 pp | EXTREME (DATA_WARNING) | AGING | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 275.0, B 2198.0; serve-point win A 58.6%, B 36.1%; Elo A 1309.1, B 1466.4; model uncertainty 0.0288
* Form inputs: days since last match A 156, B 58; matches on record A 291, B 198; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT21SURJOH-JOH  (YES = Garrett Johns)
Model: 75%
Kalshi: 50%
Gap: +25 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.027, surface_pool_high -0.018, surface_dev_loose -0.004, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kazuma Kawachi vs Ali Habib -- M15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT22KAWHAB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ali Habib (`KXITFMATCH-26OCT22KAWHAB-HAB`) | 0.03 / 0.97 (78) | 50.0% | 59.1% | -- | -- [-----] | -- | -- | -- | -- | -- | +9.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Kazuma Kawachi (`KXITFMATCH-26OCT22KAWHAB-KAW`) | 0.03 / 0.97 (78) | 50.0% | 40.9% | -- | -- [-----] | -- | -- | -- | -- | -- | -9.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 60.0%, B 38.2%; Elo A 1178.2, B 1177.6; model uncertainty None
* Form inputs: days since last match A 723, B 681; matches on record A 220, B 62; data quality F
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lorenzo Lorusso vs Azuma Visaya -- M15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT22LORVIS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Lorusso (`KXITFMATCH-26OCT22LORVIS-LOR`) | 0.03 / 0.97 (78) | 50.0% | 62.9% | -- | -- [-----] | -- | -- | -- | -- | -- | +12.9 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Azuma Visaya (`KXITFMATCH-26OCT22LORVIS-VIS`) | 0.03 / 0.97 (78) | 50.0% | 37.1% | -- | -- [-----] | -- | -- | -- | -- | -- | -12.9 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 63.3%, B 39.3%; Elo A 1247.7, B 1216.6; model uncertainty None
* Form inputs: days since last match A 681, B 842; matches on record A 54, B 5; data quality F
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kosuke Ogura vs Seonyong Han -- M15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT22OGUHAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Seonyong Han (`KXITFMATCH-26OCT22OGUHAN-HAN`) | 0.03 / 0.97 (78) | 50.0% | 31.6% | -- | -- [-----] | -- | -- | -- | -- | -- | -18.4 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Kosuke Ogura (`KXITFMATCH-26OCT22OGUHAN-OGU`) | 0.05 / 0.97 (78) | 51.0% | 68.4% | -- | -- [-----] | -- | -- | -- | -- | -- | +17.4 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 63.5%, B 40.2%; Elo A 1291.8, B 1197.2; model uncertainty None
* Form inputs: days since last match A 289, B 723; matches on record A 178, B 3; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT22OGUHAN-OGU  (YES = Kosuke Ogura)
Model: 68%
Kalshi: 51%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eric Jr Olivarez vs Ergi Kirkin -- M15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-22T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT22OLIKIR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ergi Kirkin (`KXITFMATCH-26OCT22OLIKIR-KIR`) | 0.03 / 0.97 (78) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eric Jr Olivarez (`KXITFMATCH-26OCT22OLIKIR-OLI`) | 0.03 / 0.97 (78) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Thantub Suksumrarn vs Cooper Kose -- M15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-22T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT22SUKKOS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cooper Kose (`KXITFMATCH-26OCT22SUKKOS-KOS`) | 0.03 / 0.97 (78) | 50.0% | 33.4% | -- | -- [-----] | -- | -- | -- | -- | -- | -16.6 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Thantub Suksumrarn (`KXITFMATCH-26OCT22SUKKOS-SUK`) | 0.03 / 0.97 (78) | 50.0% | 66.6% | -- | -- [-----] | -- | -- | -- | -- | -- | +16.6 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 63.0%, B 40.4%; Elo A 1266.9, B 1235.7; model uncertainty None
* Form inputs: days since last match A 674, B 723; matches on record A 66, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT22SUKKOS-SUK  (YES = Thantub Suksumrarn)
Model: 67%
Kalshi: 50%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elena Rybakina vs Polina Kudermetova -- WTA Ningbo R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-21 08:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-22 11:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-22 10:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-21T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214981:221236:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Kudermetova (`KXWTAMATCH-26OCT21RYBKUD-KUD`) | 0.11 / 0.12 (8236) | 11.5% | 11.5% | 8.8% | 8.4% [8.0%-9.3%] | -- | -- | -- | -- | PASS | +0.0 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elena Rybakina (`KXWTAMATCH-26OCT21RYBKUD-RYB`) | 0.87 / 0.88 (3167) | 87.5% | 88.5% | 91.2% | 91.6% [90.7%-92.0%] | -- | -- | -- | -- | SHADOW_BET | +1.0 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6087.0, B 4285.0; serve-point win A 65.7%, B 43.7%; Elo A 2248.5, B 1814.5; model uncertainty 0.0066
* Form inputs: days since last match A 18, B 1; matches on record A 589, B 390; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.002, surface_pool_high -0.004, surface_dev_loose -0.002, surface_dev_tight -0.001
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 6 carry a model probability
  * `KXWTAGTOTAL-26OCT21RYBKUD-19` Over 18.5 games: 0.59/0.60 mid 59.5%, model 69.6% (projection_v2.0 (prediction ledger)) -- gap +10.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT21RYBKUD-24` Over 23.5 games: 0.23/0.37 mid 30.0%, model 35.6% (projection_v2.0 (prediction ledger)) -- gap +5.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT21RYBKUD-1-KUD` Will Polina Kudermetova win set 1 in the Elena Rybakina vs Polina Kudermetova match: 0.14/0.22 mid 18.0%, model 21.2% (projection_v2.0 (prediction ledger)) -- gap +3.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT21RYBKUD-2-KUD` Will Polina Kudermetova win set 2 in the Elena Rybakina vs Polina Kudermetova match: 0.08/0.40 mid 24.0%, model 21.2% (projection_v2.0 (prediction ledger)) -- gap -2.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT21RYBKUD-2-RYB` Will Elena Rybakina win set 2 in the Elena Rybakina vs Polina Kudermetova match: 0.60/0.94 mid 77.0%, model 78.8% (projection_v2.0 (prediction ledger)) -- gap +1.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT21RYBKUD-1-RYB` Will Elena Rybakina win set 1 in the Elena Rybakina vs Polina Kudermetova match: 0.78/0.82 mid 80.0%, model 78.8% (projection_v2.0 (prediction ledger)) -- gap -1.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Maria Kozyreva / Maia Lumsden vs Desirae Krawczyk / Fanny Stollar -- WTA Ningbo QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 11:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-22T11:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT22KOZLUMKRASTO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Kozyreva / Maia Lumsden (`KXWTADOUBLES-26OCT22KOZLUMKRASTO-KOZLUM`) | 0.05 / 0.95 (100) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Desirae Krawczyk / Fanny Stollar (`KXWTADOUBLES-26OCT22KOZLUMKRASTO-KRASTO`) | 0.05 / 0.95 (100) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Raphael Collignon vs Jiri Lehecka -- ATP Brussels R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-22 12:30Z
* Current expected start: 2026-10-22 11:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-22 10:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-60_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-10-22T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208103:209920:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raphael Collignon (`KXATPMATCH-26OCT22COLLEH-COL`) | 0.24 / 0.25 (120) | 24.5% | 30.8% | 29.1% | 29.5% [28.7%-31.1%] | 25.5% | -- | 25.5% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.3 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Jiri Lehecka (`KXATPMATCH-26OCT22COLLEH-LEH`) | 0.75 / 0.76 (24870) | 75.5% | 69.2% | 70.9% | 70.5% [68.9%-71.2%] | 74.5% | -- | 74.5% | MODEL_LONE_OUTLIER | PASS | -6.3 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5214.0, B 5336.0; serve-point win A 65.8%, B 30.1%; Elo A 1827.7, B 1963.5; model uncertainty 0.0119
* Form inputs: days since last match A 1, B 9; matches on record A 352, B 446; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.004, surface_dev_loose -0.008, surface_dev_tight +0.016
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT22COLLEH-23` Over 22.5 games: 0.48/0.50 mid 49.0%, model 63.0% (projection_v2.0 (prediction ledger)) -- gap +14.0 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT22COLLEH-LEH4` Will Jiri Lehecka win at least 3.5 more games than Raphael Collignon?: 0.50/0.51 mid 50.5%, model 37.1% (projection_v2.0 (prediction ledger)) -- gap -13.4 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT22COLLEH-LEH21` Will Jiri Lehecka win the Raphael Collignon vs Jiri Lehecka match by a set score of 2-1?: 0.07/0.26 mid 16.5%, model 29.4% (projection_v2.0 (prediction ledger)) -- gap +12.9 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT22COLLEH-LEH7` Will Jiri Lehecka win at least 6.5 more games than Raphael Collignon?: 0.03/0.32 mid 17.5%, model 4.7% (projection_v2.0 (prediction ledger)) -- gap -12.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT22COLLEH-28` Over 27.5 games: 0.26/0.33 mid 29.5%, model 41.7% (projection_v2.0 (prediction ledger)) -- gap +12.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT22COLLEH-LEH20` Will Jiri Lehecka win the Raphael Collignon vs Jiri Lehecka match by a set score of 2-0?: 0.46/0.54 mid 50.0%, model 39.8% (projection_v2.0 (prediction ledger)) -- gap -10.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT22COLLEH-COL21` Will Raphael Collignon win the Raphael Collignon vs Jiri Lehecka match by a set score of 2-1?: 0.01/0.14 mid 7.5%, model 17.2% (projection_v2.0 (prediction ledger)) -- gap +9.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT22COLLEH-COL2` Will Raphael Collignon win at least 1.5 more games than Jiri Lehecka?: 0.11/0.20 mid 15.5%, model 23.7% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT22COLLEH-18` Over 17.5 games: 0.77/0.98 mid 87.5%, model 95.7% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT22COLLEH-2-LEH` Will Jiri Lehecka win set 2 in the Raphael Collignon vs Jiri Lehecka match: 0.67/0.75 mid 71.0%, model 63.1% (projection_v2.0 (prediction ledger)) -- gap -7.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT22COLLEH-1-LEH` Will Jiri Lehecka win set 1 in the Raphael Collignon vs Jiri Lehecka match: 0.69/0.72 mid 70.5%, model 63.1% (projection_v2.0 (prediction ledger)) -- gap -7.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT22COLLEH-1-COL` Will Raphael Collignon win set 1 in the Raphael Collignon vs Jiri Lehecka match: 0.28/0.32 mid 30.0%, model 36.9% (projection_v2.0 (prediction ledger)) -- gap +6.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT22COLLEH-2-COL` Will Raphael Collignon win set 2 in the Raphael Collignon vs Jiri Lehecka match: 0.27/0.33 mid 30.0%, model 36.9% (projection_v2.0 (prediction ledger)) -- gap +6.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT22COLLEH-COL20` Will Raphael Collignon win the Raphael Collignon vs Jiri Lehecka match by a set score of 2-0?: 0.01/0.13 mid 7.0%, model 13.6% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Borna Gojo vs Daniel Altmaier -- ATP Lyon R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-22 13:00Z
* Current expected start: 2026-10-22 13:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-22 12:15Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-22T04:00:00+00:00 as not a valid time; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Clay · scheduled 2026-10-22T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:127157:127339:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Altmaier (`KXATPMATCH-26OCT22GOJALT-ALT`) | 0.44 / 0.45 (47) | 44.5% | 67.2% | 51.0% | 59.2% [55.9%-63.0%] | 44.4% | -- | 44.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +22.7 pp | HIGH_REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Borna Gojo (`KXATPMATCH-26OCT22GOJALT-GOJ`) | 0.54 / 0.55 (46) | 54.5% | 32.8% | 49.0% | 40.8% [37.0%-44.1%] | 55.6% | -- | 55.6% | MODEL_LONE_OUTLIER | PASS | -21.7 pp | HIGH_REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2777.0, B 5258.0; serve-point win A 63.8%, B 32.6%; Elo A 1633.1, B 1809.7; model uncertainty 0.0357
* Form inputs: days since last match A 1, B 1; matches on record A 445, B 706; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT22GOJALT-ALT  (YES = Daniel Altmaier)
Model: 67%
Kalshi: 44%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: EXTERNAL_MARKET_REJECTION, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.019, surface_dev_loose -0.010, surface_dev_tight +0.015
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT22GOJALT-GOJ2` Will Borna Gojo win at least 1.5 more games than Daniel Altmaier?: 0.48/0.50 mid 49.0%, model 25.9% (projection_v2.0 (prediction ledger)) -- gap -23.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT22GOJALT-ALT2` Will Daniel Altmaier win at least 1.5 more games than Borna Gojo?: 0.33/0.48 mid 40.5%, model 59.8% (projection_v2.0 (prediction ledger)) -- gap +19.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT22GOJALT-ALT20` Will Daniel Altmaier win the Borna Gojo vs Daniel Altmaier match by a set score of 2-0?: 0.13/0.29 mid 21.0%, model 38.1% (projection_v2.0 (prediction ledger)) -- gap +17.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT22GOJALT-1-GOJ` Will Borna Gojo win set 1 in the Borna Gojo vs Daniel Altmaier match: 0.53/0.56 mid 54.5%, model 38.3% (projection_v2.0 (prediction ledger)) -- gap -16.2 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT22GOJALT-1-ALT` Will Daniel Altmaier win set 1 in the Borna Gojo vs Daniel Altmaier match: 0.44/0.48 mid 46.0%, model 61.7% (projection_v2.0 (prediction ledger)) -- gap +15.7 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT22GOJALT-ALT21` Will Daniel Altmaier win the Borna Gojo vs Daniel Altmaier match by a set score of 2-1?: 0.04/0.23 mid 13.5%, model 29.2% (projection_v2.0 (prediction ledger)) -- gap +15.7 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT22GOJALT-2-GOJ` Will Borna Gojo win set 2 in the Borna Gojo vs Daniel Altmaier match: 0.51/0.56 mid 53.5%, model 38.3% (projection_v2.0 (prediction ledger)) -- gap -15.2 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT22GOJALT-2-ALT` Will Daniel Altmaier win set 2 in the Borna Gojo vs Daniel Altmaier match: 0.44/0.50 mid 47.0%, model 61.7% (projection_v2.0 (prediction ledger)) -- gap +14.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT22GOJALT-GOJ5` Will Borna Gojo win at least 4.5 more games than Daniel Altmaier?: 0.13/0.28 mid 20.5%, model 7.4% (projection_v2.0 (prediction ledger)) -- gap -13.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT22GOJALT-GOJ20` Will Borna Gojo win the Borna Gojo vs Daniel Altmaier match by a set score of 2-0?: 0.16/0.33 mid 24.5%, model 14.7% (projection_v2.0 (prediction ledger)) -- gap -9.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT22GOJALT-31` Over 30.5 games: 0.17/0.26 mid 21.5%, model 27.3% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT22GOJALT-21` Over 20.5 games: 0.65/0.74 mid 69.5%, model 74.2% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT22GOJALT-26` Over 25.5 games: 0.45/0.47 mid 46.0%, model 48.6% (projection_v2.0 (prediction ledger)) -- gap +2.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT22GOJALT-GOJ21` Will Borna Gojo win the Borna Gojo vs Daniel Altmaier match by a set score of 2-1?: 0.09/0.25 mid 17.0%, model 18.1% (projection_v2.0 (prediction ledger)) -- gap +1.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; WIDE_SPREAD

## Kyrian Jacquet vs Brandon Nakashima -- ATP Lyon R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-22 13:00Z
* Current expected start: 2026-10-22 13:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-22 12:15Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-22T04:00:00+00:00 as not a valid time; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Clay · scheduled 2026-10-22T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:206909:208021:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kyrian Jacquet (`KXATPMATCH-26OCT22JACNAK-JAC`) | 0.35 / 0.37 (714) | 36.0% | 27.3% | 25.2% | 26.4% [25.2%-28.4%] | 37.7% | -- | 37.7% | MODEL_LONE_OUTLIER | PASS | -8.7 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Brandon Nakashima (`KXATPMATCH-26OCT22JACNAK-NAK`) | 0.62 / 0.63 (9) | 62.5% | 72.7% | 74.8% | 73.6% [71.6%-74.8%] | 62.3% | -- | 62.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +10.2 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3771.0, B 5606.0; serve-point win A 62.2%, B 33.0%; Elo A 1702.6, B 1852.4; model uncertainty 0.0162
* Form inputs: days since last match A 1, B 1; matches on record A 391, B 457; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.008, surface_dev_loose -0.005, surface_dev_tight +0.001
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT22JACNAK-NAK21` Will Brandon Nakashima win the Kyrian Jacquet vs Brandon Nakashima match by a set score of 2-1?: 0.07/0.26 mid 16.5%, model 29.6% (projection_v2.0 (prediction ledger)) -- gap +13.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT22JACNAK-NAK20` Will Brandon Nakashima win the Kyrian Jacquet vs Brandon Nakashima match by a set score of 2-0?: 0.27/0.40 mid 33.5%, model 43.1% (projection_v2.0 (prediction ledger)) -- gap +9.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT22JACNAK-JAC2` Will Kyrian Jacquet win at least 1.5 more games than Brandon Nakashima?: 0.22/0.37 mid 29.5%, model 21.2% (projection_v2.0 (prediction ledger)) -- gap -8.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT22JACNAK-NAK3` Will Brandon Nakashima win at least 2.5 more games than Kyrian Jacquet?: 0.49/0.51 mid 50.0%, model 58.0% (projection_v2.0 (prediction ledger)) -- gap +8.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT22JACNAK-1-JAC` Will Kyrian Jacquet win set 1 in the Kyrian Jacquet vs Brandon Nakashima match: 0.40/0.42 mid 41.0%, model 34.3% (projection_v2.0 (prediction ledger)) -- gap -6.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT22JACNAK-JAC20` Will Kyrian Jacquet win the Kyrian Jacquet vs Brandon Nakashima match by a set score of 2-0?: 0.15/0.21 mid 18.0%, model 11.8% (projection_v2.0 (prediction ledger)) -- gap -6.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT22JACNAK-1-NAK` Will Brandon Nakashima win set 1 in the Kyrian Jacquet vs Brandon Nakashima match: 0.58/0.61 mid 59.5%, model 65.7% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT22JACNAK-2-NAK` Will Brandon Nakashima win set 2 in the Kyrian Jacquet vs Brandon Nakashima match: 0.57/0.62 mid 59.5%, model 65.7% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT22JACNAK-2-JAC` Will Kyrian Jacquet win set 2 in the Kyrian Jacquet vs Brandon Nakashima match: 0.38/0.42 mid 40.0%, model 34.3% (projection_v2.0 (prediction ledger)) -- gap -5.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT22JACNAK-24` Over 23.5 games: 0.46/0.47 mid 46.5%, model 50.1% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT22JACNAK-29` Over 28.5 games: 0.26/0.34 mid 30.0%, model 33.0% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT22JACNAK-JAC21` Will Kyrian Jacquet win the Kyrian Jacquet vs Brandon Nakashima match by a set score of 2-1?: 0.09/0.18 mid 13.5%, model 15.5% (projection_v2.0 (prediction ledger)) -- gap +2.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT22JACNAK-NAK6` Will Brandon Nakashima win at least 5.5 more games than Kyrian Jacquet?: 0.03/0.35 mid 19.0%, model 17.6% (projection_v2.0 (prediction ledger)) -- gap -1.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT22JACNAK-19` Over 18.5 games: 0.83/0.90 mid 86.5%, model 86.0% (projection_v2.0 (prediction ledger)) -- gap -0.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Valentin Vacherot vs Luca Van Assche -- ATP Lyon R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-22 13:00Z
* Current expected start: 2026-10-22 13:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-22 12:15Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-22T04:00:00+00:00 as not a valid time; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Clay · scheduled 2026-10-22T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200473:209414:2026-10-22`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valentin Vacherot (`KXATPMATCH-26OCT22VACVAN-VAC`) | 0.55 / 0.56 (6467) | 55.5% | 52.5% | 56.1% | 54.1% [52.6%-55.1%] | 56.6% | -- | 56.6% | MARKETS_AGREE | PASS | -3.0 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Luca Van Assche (`KXATPMATCH-26OCT22VACVAN-VAN`) | 0.43 / 0.45 (1798) | 44.0% | 47.5% | 43.9% | 45.9% [44.9%-47.4%] | 43.4% | -- | 43.4% | MARKETS_AGREE | PASS | +3.5 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3983.0, B 4895.0; serve-point win A 61.2%, B 39.3%; Elo A 1804.7, B 1820.8; model uncertainty 0.0127
* Form inputs: days since last match A 9, B 1; matches on record A 388, B 357; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.000, surface_dev_tight -0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT22VACVAN-VAC21` Will Valentin Vacherot win the Valentin Vacherot vs Luca Van Assche match by a set score of 2-1?: 0.05/0.25 mid 15.0%, model 25.8% (projection_v2.0 (prediction ledger)) -- gap +10.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT22VACVAN-VAN2` Will Luca Van Assche win at least 1.5 more games than Valentin Vacherot?: 0.23/0.37 mid 30.0%, model 40.5% (projection_v2.0 (prediction ledger)) -- gap +10.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT22VACVAN-VAN20` Will Luca Van Assche win the Valentin Vacherot vs Luca Van Assche match by a set score of 2-0?: 0.06/0.24 mid 15.0%, model 23.4% (projection_v2.0 (prediction ledger)) -- gap +8.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT22VACVAN-VAN21` Will Luca Van Assche win the Valentin Vacherot vs Luca Van Assche match by a set score of 2-1?: 0.12/0.20 mid 16.0%, model 24.1% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT22VACVAN-24` Over 23.5 games: 0.45/0.46 mid 45.5%, model 53.4% (projection_v2.0 (prediction ledger)) -- gap +7.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT22VACVAN-VAC6` Will Valentin Vacherot win at least 5.5 more games than Luca Van Assche?: 0.03/0.35 mid 19.0%, model 12.0% (projection_v2.0 (prediction ledger)) -- gap -7.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT22VACVAN-VAC3` Will Valentin Vacherot win at least 2.5 more games than Luca Van Assche?: 0.45/0.47 mid 46.0%, model 39.0% (projection_v2.0 (prediction ledger)) -- gap -7.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT22VACVAN-29` Over 28.5 games: 0.25/0.30 mid 27.5%, model 33.0% (projection_v2.0 (prediction ledger)) -- gap +5.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT22VACVAN-VAC20` Will Valentin Vacherot win the Valentin Vacherot vs Luca Van Assche match by a set score of 2-0?: 0.25/0.39 mid 32.0%, model 26.7% (projection_v2.0 (prediction ledger)) -- gap -5.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT22VACVAN-1-VAC` Will Valentin Vacherot win set 1 in the Valentin Vacherot vs Luca Van Assche match: 0.55/0.58 mid 56.5%, model 51.6% (projection_v2.0 (prediction ledger)) -- gap -4.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT22VACVAN-1-VAN` Will Luca Van Assche win set 1 in the Valentin Vacherot vs Luca Van Assche match: 0.42/0.46 mid 44.0%, model 48.4% (projection_v2.0 (prediction ledger)) -- gap +4.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT22VACVAN-2-VAC` Will Valentin Vacherot win set 2 in the Valentin Vacherot vs Luca Van Assche match: 0.52/0.59 mid 55.5%, model 51.6% (projection_v2.0 (prediction ledger)) -- gap -3.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT22VACVAN-19` Over 18.5 games: 0.83/0.92 mid 87.5%, model 85.3% (projection_v2.0 (prediction ledger)) -- gap -2.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT22VACVAN-2-VAN` Will Luca Van Assche win set 2 in the Valentin Vacherot vs Luca Van Assche match: 0.41/0.56 mid 48.5%, model 48.4% (projection_v2.0 (prediction ledger)) -- gap -0.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Romain Arneodo / Ugo Blanchet vs Matisse Bobichon / Kilian Feldbausch -- ATP Lyon QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-22 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-22T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT22ARNBLABOBFEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Romain Arneodo / Ugo Blanchet (`KXATPDOUBLES-26OCT22ARNBLABOBFEL-ARNBLA`) | 0.05 / 0.95 (156) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matisse Bobichon / Kilian Feldbausch (`KXATPDOUBLES-26OCT22ARNBLABOBFEL-BOBFEL`) | 0.05 / 0.95 (156) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Alexander Bublik vs Fabian Marozsan -- ATP Almaty R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-21 09:30Z
* Current expected start: 2026-10-22 14:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-22 13:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1740_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-10-21T09:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:122330:206681:2026-10-21`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Bublik (`KXATPMATCH-26OCT21BUBMAR-BUB`) | 0.72 / 0.73 (106) | 72.5% | 72.3% | 66.2% | 67.9% [67.1%-69.3%] | -- | -- | -- | -- | PASS | -0.2 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Fabian Marozsan (`KXATPMATCH-26OCT21BUBMAR-MAR`) | 0.26 / 0.28 (14939) | 27.0% | 27.7% | 33.8% | 32.1% [30.7%-32.9%] | -- | -- | -- | -- | WATCH | +0.7 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5279.0, B 4525.0; serve-point win A 70.6%, B 34.4%; Elo A 1950.5, B 1778.2; model uncertainty 0.0111
* Form inputs: days since last match A 8, B 13; matches on record A 705, B 439; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.001, surface_dev_tight -0.008
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT21BUBMAR-23` Over 22.5 games: 0.47/0.50 mid 48.5%, model 62.9% (projection_v2.0 (prediction ledger)) -- gap +14.4 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT21BUBMAR-BUB7` Will Alexander Bublik win at least 6.5 more games than Fabian Marozsan?: 0.03/0.32 mid 17.5%, model 4.7% (projection_v2.0 (prediction ledger)) -- gap -12.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT21BUBMAR-28` Over 27.5 games: 0.27/0.34 mid 30.5%, model 41.5% (projection_v2.0 (prediction ledger)) -- gap +11.0 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT21BUBMAR-BUB4` Will Alexander Bublik win at least 3.5 more games than Fabian Marozsan?: 0.47/0.48 mid 47.5%, model 37.6% (projection_v2.0 (prediction ledger)) -- gap -9.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT21BUBMAR-18` Over 17.5 games: 0.76/0.98 mid 87.0%, model 95.7% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21BUBMAR-BUB21` Will Alexander Bublik win the Alexander Bublik vs Fabian Marozsan match by a set score of 2-1?: 0.19/0.28 mid 23.5%, model 29.6% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21BUBMAR-MAR21` Will Fabian Marozsan win the Alexander Bublik vs Fabian Marozsan match by a set score of 2-1?: 0.08/0.16 mid 12.0%, model 15.7% (projection_v2.0 (prediction ledger)) -- gap +3.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT21BUBMAR-1-MAR` Will Fabian Marozsan win set 1 in the Alexander Bublik vs Fabian Marozsan match: 0.28/0.35 mid 31.5%, model 34.7% (projection_v2.0 (prediction ledger)) -- gap +3.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT21BUBMAR-2-BUB` Will Alexander Bublik win set 2 in the Alexander Bublik vs Fabian Marozsan match: 0.65/0.70 mid 67.5%, model 65.3% (projection_v2.0 (prediction ledger)) -- gap -2.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT21BUBMAR-2-MAR` Will Fabian Marozsan win set 2 in the Alexander Bublik vs Fabian Marozsan match: 0.30/0.35 mid 32.5%, model 34.7% (projection_v2.0 (prediction ledger)) -- gap +2.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT21BUBMAR-MAR2` Will Fabian Marozsan win at least 1.5 more games than Alexander Bublik?: 0.21/0.28 mid 24.5%, model 22.7% (projection_v2.0 (prediction ledger)) -- gap -1.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21BUBMAR-BUB20` Will Alexander Bublik win the Alexander Bublik vs Fabian Marozsan match by a set score of 2-0?: 0.41/0.47 mid 44.0%, model 42.7% (projection_v2.0 (prediction ledger)) -- gap -1.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT21BUBMAR-1-BUB` Will Alexander Bublik win set 1 in the Alexander Bublik vs Fabian Marozsan match: 0.64/0.68 mid 66.0%, model 65.3% (projection_v2.0 (prediction ledger)) -- gap -0.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT21BUBMAR-MAR20` Will Fabian Marozsan win the Alexander Bublik vs Fabian Marozsan match by a set score of 2-0?: 0.08/0.16 mid 12.0%, model 12.0% (projection_v2.0 (prediction ledger)) -- gap +0.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Constantin Frantzen / Robert Galloway vs Raphael Collignon / David Goffin -- ATP Brussels QF

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-10-21 12:30Z
* Current expected start: 2026-10-22 16:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-21 11:45Z
* Recommended handicap-by time: 2026-10-22 15:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-21T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT21FRAGALCOLGOF:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raphael Collignon / David Goffin (`KXATPDOUBLES-26OCT21FRAGALCOLGOF-COLGOF`) | 0.16 / 0.57 (2) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Constantin Frantzen / Robert Galloway (`KXATPDOUBLES-26OCT21FRAGALCOLGOF-FRAGAL`) | 0.33 / 0.79 (5) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
