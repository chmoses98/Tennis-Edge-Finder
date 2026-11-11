# ASSISTED SLATE -- 2026-11-11T21:36Z (`SL-20261111T213623Z-1c2fe2f3`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

314 open matches not seen started, 688 markets. Skipped: {"scheduled_start_over_24h_past": 7, "first_ball_already_observed": 1}. Sources: shadow board 2026-11-11T17:15:01.596265+00:00, Model 4 2026-11-11T17:16:15.169484+00:00, Gen-1 ledger 2026-11-11T17:14:56.490480+00:00, external 2026-11-11T21:08:49.697418+00:00, capture 20261111T210658Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-11-12 12:00Z**
* Recommended RUN TENNIS time: **2026-11-12 11:15Z**
* Final price/status check time: **2026-11-12 11:50Z**
* Number of matches in window: 1 (Alex Michelsen vs Alejandro Tabilo)

* **1 main-tour match(es) have NO verified start status** (STATUS_AMBIGUOUS): BET blocked until a live status check.

Slate built 2026-11-11T21:36Z. Refresh due by: 2026-11-12 11:15Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 20, "HIGH_REVIEW": 28, "NORMAL": 87, "REVIEW": 32, "UNPRICED": 521}; match winners: {"EXTREME": 20, "HIGH_REVIEW": 27, "NORMAL": 80, "REVIEW": 29, "UNPRICED": 472}; quote freshness at build: {"FRESH": 167}.

## Rinon Okuwaki vs Neda Rahimkhani -- W15 Lincoln NE R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:239477:260856:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rinon Okuwaki (`KXITFWMATCH-26NOV10OKURAH-OKU`) | 0.49 / 0.51 (20933) | 50.0% | 79.7% | 30.5% | 63.6% [61.6%-66.6%] | -- | -- | -- | -- | PASS | +29.7 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Neda Rahimkhani (`KXITFWMATCH-26NOV10OKURAH-RAH`) | 0.49 / 0.51 (22939) | 50.0% | 20.3% | 69.5% | 36.4% [33.4%-38.4%] | -- | -- | -- | -- | PASS | -29.7 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 739.0, B 0.0; serve-point win A 56.1%, B 50.1%; Elo A 1368.7, B 1268.9; model uncertainty 0.025
* Form inputs: days since last match A 365, B 1485; matches on record A 168, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10OKURAH-OKU  (YES = Rinon Okuwaki)
Model: 80%
Kalshi: 50%
Gap: +30 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.030, surface_pool_high -0.020, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## David Cassan / Sabina vs Perlov / Ratti -- M15 Roldan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 00:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-11T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10DAVSABPERRAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| David Cassan / Sabina (`KXITFDOUBLES-26NOV10DAVSABPERRAT-DAVSAB`) | 0.31 / 0.35 (377) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Perlov / Ratti (`KXITFDOUBLES-26NOV10DAVSABPERRAT-PERRAT`) | 0.64 / 0.68 (8) | 66.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

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
| Alize Lim (`KXITFWMATCH-26NOV10LIMROD-LIM`) | 0.49 / 0.51 (42598) | 50.0% | 46.4% | 69.9% | 61.1% [55.4%-65.1%] | -- | -- | -- | -- | WATCH | -3.6 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Victoria Rodriguez (`KXITFWMATCH-26NOV10LIMROD-ROD`) | 0.49 / 0.51 (44800) | 50.0% | 53.6% | 30.1% | 38.9% [34.9%-44.6%] | -- | -- | -- | -- | PASS | +3.6 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1334.0, B 2050.0; serve-point win A 46.1%, B 53.2%; Elo A 1515.3, B 1501.0; model uncertainty 0.0486
* Form inputs: days since last match A 239, B 14; matches on record A 584, B 576; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Reece Falck / Billy Suarez vs Omar Jasika / Christopher Sousou -- ATP Challenger Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-11T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11FALSUAJASSOU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Reece Falck / Billy Suarez (`KXATPCHALLENGERDOUBLES-26NOV11FALSUAJASSOU-FALSUA`) | 0.78 / 0.94 (1) | 86.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Omar Jasika / Christopher Sousou (`KXATPCHALLENGERDOUBLES-26NOV11FALSUAJASSOU-JASSOU`) | 0.08 / 0.67 (56) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Santiago De la Fuente / Genaro Alberto Olivieri vs Facundo Bagnis / Facundo Mena -- ATP Challenger Lima R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-11T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11DLFOLIBAGMEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Facundo Bagnis / Facundo Mena (`KXATPCHALLENGERDOUBLES-26NOV11DLFOLIBAGMEN-BAGMEN`) | 0.59 / 0.61 (2229) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Santiago De la Fuente / Genaro Alberto Olivieri (`KXATPCHALLENGERDOUBLES-26NOV11DLFOLIBAGMEN-DLFOLI`) | 0.39 / 0.41 (2229) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Aryna Sabalenka vs Mirra Andreeva -- WTA Finals Women Singles Group B

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-11-12 00:10Z
* Current expected start: 2026-11-11 21:29Z
* Source: COURT_PROGRESSION: preceding match on Indian Wells Tennis Garden in progress (set 2 of best-of-3); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-11 21:14Z
* Recommended handicap-by time: 2026-11-11 20:44Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-161_MIN; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA (TOUR_FINALS) · Hard · scheduled 2026-11-12T00:10:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214544:259799:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mirra Andreeva (`KXWTAMATCH-26NOV11SABAND-AND`) | 0.48 / 0.49 (225071) | 48.5% | -- | 29.8% | 28.4% [26.1%-29.3%] | -- | -- | -- | -- | PASS | -20.1 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aryna Sabalenka (`KXWTAMATCH-26NOV11SABAND-SAB`) | 0.51 / 0.52 (4668) | 51.5% | -- | 70.2% | 71.6% [70.7%-73.9%] | -- | -- | -- | -- | WATCH | +20.1 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5768.0, B 4895.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0161
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26NOV11SABAND-SAB  (YES = Aryna Sabalenka)
Model: 72%
Kalshi: 52%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, UNKNOWN
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose -0.000, surface_dev_tight -0.004
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTASETWINNER-26NOV11SABAND-2-SAB` Will Aryna Sabalenka win set 2 in the Aryna Sabalenka vs Mirra Andreeva match: 0.42/0.51 mid 46.5%, model 61.7% (projection_v2.0 (prediction ledger)) -- gap +15.2 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV11SABAND-2-AND` Will Mirra Andreeva win set 2 in the Aryna Sabalenka vs Mirra Andreeva match: 0.46/0.56 mid 51.0%, model 38.3% (projection_v2.0 (prediction ledger)) -- gap -12.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV11SABAND-1-AND` Will Mirra Andreeva win set 1 in the Aryna Sabalenka vs Mirra Andreeva match: 0.49/0.50 mid 49.5%, model 38.3% (projection_v2.0 (prediction ledger)) -- gap -11.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV11SABAND-1-SAB` Will Aryna Sabalenka win set 1 in the Aryna Sabalenka vs Mirra Andreeva match: 0.51/0.52 mid 51.5%, model 61.7% (projection_v2.0 (prediction ledger)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26NOV11SABAND-23` Over 22.5 games: 0.52/0.53 mid 52.5%, model 55.0% (projection_v2.0 (prediction ledger)) -- gap +2.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV11SABAND-28` Over 27.5 games: 0.31/0.34 mid 32.5%, model 34.5% (projection_v2.0 (prediction ledger)) -- gap +2.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV11SABAND-18` Over 17.5 games: 0.88/0.89 mid 88.5%, model 88.5% (projection_v2.0 (prediction ledger)) -- gap +0.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STATUS_AMBIGUOUS; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Joseph hernandez vs Tobia Grandinetti -- M15 Roldan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211634:214279:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tobia Grandinetti (`KXITFMATCH-26NOV11HERGRA-GRA`) | 0.42 / 0.43 (7994) | 42.5% | 60.6% | 67.2% | 51.6% [51.0%-53.1%] | 64.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +18.1 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Joseph hernandez (`KXITFMATCH-26NOV11HERGRA-HER`) | 0.57 / 0.58 (9977) | 57.5% | 39.4% | 32.8% | 48.4% [46.9%-49.0%] | 35.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -18.1 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 59.0, B 160.0; serve-point win A 57.2%, B 40.8%; Elo A 1259.0, B 1265.5; model uncertainty 0.0106
* Form inputs: days since last match A 359, B 359; matches on record A 1, B 5; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV11HERGRA-GRA  (YES = Tobia Grandinetti)
Model: 61%
Kalshi: 42%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arina Bulatova vs Ava Catanzarite -- W35 Weston FL R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:256712:260303:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arina Bulatova (`KXITFWMATCH-26NOV11BULCAT-BUL`) | -- / 0.01 (150224) | -- | 89.5% | 35.4% | 76.6% [73.2%-79.7%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | FRESH | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |
| Ava Catanzarite (`KXITFWMATCH-26NOV11BULCAT-CAT`) | 0.99 / -- (0) | -- | 10.5% | 64.6% | 23.4% [20.3%-26.9%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | FRESH | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 1763.0, B 106.0; serve-point win A 56.7%, B 52.7%; Elo A 1504.5, B 1276.9; model uncertainty 0.0327
* Form inputs: days since last match A 205, B 240; matches on record A 154, B 12; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.017, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yael Saffar vs Dasha Plekhanova -- W35 Weston FL R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223203:270469:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dasha Plekhanova (`KXITFWMATCH-26NOV11SAFPLE-PLE`) | 0.84 / 0.87 (80) | 85.5% | 85.8% | 74.8% | 72.6% [70.4%-74.8%] | 76.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yael Saffar (`KXITFWMATCH-26NOV11SAFPLE-SAF`) | 0.13 / 0.15 (73) | 14.0% | 14.2% | 25.2% | 27.4% [25.2%-29.6%] | 24.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 288.0, B 907.0; serve-point win A 49.7%, B 42.3%; Elo A 1356.2, B 1522.2; model uncertainty 0.0222
* Form inputs: days since last match A 205, B 16; matches on record A 4, B 87; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.022, surface_pool_high +0.023, surface_dev_loose -0.004, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mattia Bellucci vs Sascha Gueymard Wayenburg -- ATP Challenger Orleans R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 22:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-11T22:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208233:209849:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mattia Bellucci (`KXATPCHALLENGERMATCH-26NOV11BELGUE-BEL`) | 0.68 / 0.70 (19382) | 69.0% | -- | 57.3% | 61.1% [59.2%-65.8%] | 66.4% | 68.5% | 68.5% | MARKETS_AGREE | PASS | -7.9 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Sascha Gueymard Wayenburg (`KXATPCHALLENGERMATCH-26NOV11BELGUE-GUE`) | 0.30 / 0.32 (14157) | 31.0% | -- | 42.7% | 38.9% [34.2%-40.8%] | 33.6% | 32.0% | 32.0% | MARKETS_AGREE | WATCH | +7.9 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5469.0, B 4524.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0327
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.009, surface_dev_loose -0.010, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Tristan Boyer / Ryan Nijboer vs Bruno (2002) Oliveira / Natan Rodrigues -- ATP Challenger Lima R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 22:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-11T22:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11BOYNIJOLIROD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tristan Boyer / Ryan Nijboer (`KXATPCHALLENGERDOUBLES-26NOV11BOYNIJOLIROD-BOYNIJ`) | 0.32 / 0.39 (14) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bruno (2002) Oliveira / Natan Rodrigues (`KXATPCHALLENGERDOUBLES-26NOV11BOYNIJOLIROD-OLIROD`) | 0.54 / 0.64 (48) | 59.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Keshav Chopra / Andres Martin vs Arda Azkara / Clement Chidekh -- ATP Challenger Knoxville R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-11T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11CHOMARAZKCHI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arda Azkara / Clement Chidekh (`KXATPCHALLENGERDOUBLES-26NOV11CHOMARAZKCHI-AZKCHI`) | 0.27 / 0.30 (2229) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Keshav Chopra / Andres Martin (`KXATPCHALLENGERDOUBLES-26NOV11CHOMARAZKCHI-CHOMAR`) | 0.70 / 0.73 (2778) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Liam Draxl vs Pyotr Nesterov -- ATP Challenger Knoxville R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-11T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208119:209318:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liam Draxl (`KXATPCHALLENGERMATCH-26NOV11DRANES-DRA`) | 0.78 / 0.79 (7142) | 78.5% | -- | 64.6% | 68.8% [66.9%-71.0%] | 76.6% | 77.8% | 77.8% | MODEL_LONE_OUTLIER | PASS | -9.7 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | AMBIGUOUS |
| Pyotr Nesterov (`KXATPCHALLENGERMATCH-26NOV11DRANES-NES`) | 0.21 / 0.22 (419) | 21.5% | -- | 35.4% | 31.2% [29.0%-33.1%] | 23.4% | 22.5% | 22.5% | MODEL_LONE_OUTLIER | PASS | +9.7 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | AMBIGUOUS |

* Serve evidence (points): A 4913.0, B 3494.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0205
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.014, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Gabriela Dabrowski / Luisa Stefani vs Hanyu Guo / Kristina Mladenovic -- WTA Finals Women Doubles Group

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-12 01:20Z
* Current expected start: 2026-11-11 23:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-11 21:14Z
* Recommended handicap-by time: 2026-11-11 22:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_FINALS) · surface ? · scheduled 2026-11-12T01:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11DABSTEGUOMLA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriela Dabrowski / Luisa Stefani (`KXWTADOUBLES-26NOV11DABSTEGUOMLA-DABSTE`) | 0.65 / 0.68 (541) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hanyu Guo / Kristina Mladenovic (`KXWTADOUBLES-26NOV11DABSTEGUOMLA-GUOMLA`) | 0.32 / 0.34 (437) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Jack Anthrop vs Aidan Mchugh -- M25 Columbus OH R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202420:210294:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jack Anthrop (`KXITFMATCH-26NOV11ANTMCH-ANT`) | 0.88 / 0.90 (137) | 89.0% | 50.1% | 59.2% | 49.5% [42.3%-55.1%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -38.9 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aidan Mchugh (`KXITFMATCH-26NOV11ANTMCH-MCH`) | 0.10 / 0.12 (2186) | 11.0% | 49.9% | 40.8% | 50.5% [44.9%-57.7%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +38.9 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1030.0, B 3842.0; serve-point win A 59.9%, B 40.1%; Elo A 1442.4, B 1488.7; model uncertainty 0.0642
* Form inputs: days since last match A 366, B 310; matches on record A 77, B 477; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV11ANTMCH-MCH  (YES = Aidan Mchugh)
Model: 50%
Kalshi: 11%
Gap: +39 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Youcef Rihane vs Charles Bertimon -- M15 Naples FL R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202293:209065:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charles Bertimon (`KXITFMATCH-26NOV11RIHBER-BER`) | 0.17 / 0.18 (9895) | 17.5% | 56.5% | 19.9% | 50.0% [50.0%-50.0%] | 37.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +39.0 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Youcef Rihane (`KXITFMATCH-26NOV11RIHBER-RIH`) | 0.82 / 0.83 (5327) | 82.5% | 43.5% | 80.1% | 50.0% [50.0%-50.0%] | 62.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -39.0 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 976.0; serve-point win A 58.2%, B 40.5%; Elo A 1191.5, B 1194.9; model uncertainty 0.0
* Form inputs: days since last match A 1115, B 205; matches on record A 17, B 38; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV11RIHBER-BER  (YES = Charles Bertimon)
Model: 56%
Kalshi: 18%
Gap: +39 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maxime St-Hilaire vs Amit Vales -- M25 Montreal R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211707:212636:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maxime St-Hilaire (`KXITFMATCH-26NOV11STHVAL-STH`) | 0.66 / 0.67 (4858) | 66.5% | 14.4% | 26.2% | 26.2% [25.3%-28.0%] | 27.6% | -- | 27.6% | KALSHI_LONE_OUTLIER | PASS | -52.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Amit Vales (`KXITFMATCH-26NOV11STHVAL-VAL`) | 0.33 / 0.34 (17414) | 33.5% | 85.6% | 73.8% | 73.8% [72.0%-74.7%] | 72.4% | -- | 72.4% | KALSHI_LONE_OUTLIER | PASS | +52.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 163.0, B 2461.0; serve-point win A 51.3%, B 40.7%; Elo A 1192.9, B 1368.1; model uncertainty 0.0131
* Form inputs: days since last match A 198, B 54; matches on record A 4, B 124; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV11STHVAL-VAL  (YES = Amit Vales)
Model: 86%
Kalshi: 34%
Gap: +52 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: SUPPORTS_MODEL_DIRECTION
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.018, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Davide Tortora vs Lucca Liu -- M15 Naples FL R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208190:213175:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucca Liu (`KXITFMATCH-26NOV11TORLIU-LIU`) | 0.98 / 0.99 (13524) | 98.5% | 60.2% | 57.8% | 58.3% [57.2%-59.4%] | 40.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -38.3 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Davide Tortora (`KXITFMATCH-26NOV11TORLIU-TOR`) | 0.01 / 0.02 (2703) | 1.5% | 39.8% | 42.2% | 41.7% [40.6%-42.8%] | 59.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +38.3 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 593.0, B 620.0; serve-point win A 56.6%, B 41.4%; Elo A 1222.7, B 1280.2; model uncertainty 0.0108
* Form inputs: days since last match A 198, B 240; matches on record A 24, B 16; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV11TORLIU-TOR  (YES = Davide Tortora)
Model: 40%
Kalshi: 2%
Gap: +38 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.005, surface_dev_loose +0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Max Wiskandt vs Jake Fellows -- M25 Montreal R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-11T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208328:212654:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jake Fellows (`KXITFMATCH-26NOV11WISFEL-FEL`) | 0.28 / 0.32 (18) | 30.0% | 26.2% | 36.9% | 45.4% [43.8%-45.9%] | 20.6% | -- | 20.6% | MODEL_LONE_OUTLIER | PASS | -3.8 pp | NORMAL | FRESH | F / POOR | EXTERNAL_OUTLIER | VERIFIED |
| Max Wiskandt (`KXITFMATCH-26NOV11WISFEL-WIS`) | 0.65 / 0.71 (1) | 68.0% | 73.8% | 63.1% | 54.6% [54.1%-56.2%] | 79.4% | -- | 79.4% | MODEL_LONE_OUTLIER | PASS | +5.8 pp | NORMAL | FRESH | F / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 3286.0, B 104.0; serve-point win A 62.7%, B 42.2%; Elo A 1451.5, B 1422.8; model uncertainty 0.0103
* Form inputs: days since last match A 30, B 198; matches on record A 237, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Brooke Black vs Ashley Lahey -- W35 Weston FL R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-11T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11BLALAH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brooke Black (`KXITFWMATCH-26NOV11BLALAH-BLA`) | 0.25 / 0.34 (6) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ashley Lahey (`KXITFWMATCH-26NOV11BLALAH-LAH`) | 0.69 / 0.73 (13) | 71.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cadence Brace vs Carolina Gomez -- W35 Weston FL R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222312:223335:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cadence Brace (`KXITFWMATCH-26NOV11BRAGOM-BRA`) | 0.90 / 0.91 (10459) | 90.5% | 91.7% | 71.3% | 79.7% [76.5%-83.3%] | 83.8% | -- | 83.8% | KALSHI_LONE_OUTLIER | PASS | +1.2 pp | NORMAL | FRESH | F / POOR | EXTERNAL_OUTLIER | AMBIGUOUS |
| Carolina Gomez (`KXITFWMATCH-26NOV11BRAGOM-GOM`) | 0.09 / 0.10 (7615) | 9.5% | 8.3% | 28.7% | 20.3% [16.7%-23.4%] | 16.2% | -- | 16.2% | KALSHI_LONE_OUTLIER | PASS | -1.2 pp | NORMAL | FRESH | F / POOR | EXTERNAL_OUTLIER | AMBIGUOUS |

* Serve evidence (points): A 2165.0, B 0.0; serve-point win A 57.8%, B 52.6%; Elo A 1550.2, B 1312.0; model uncertainty 0.0336
* Form inputs: days since last match A 56, B 849; matches on record A 222, B 40; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.036, surface_pool_high -0.032, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rachel Gailis vs Carolina Bohrer Martins -- W35 Weston FL R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-11T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222037:260003:2026-11-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carolina Bohrer Martins (`KXITFWMATCH-26NOV11GAIBOH-BOH`) | 0.21 / 0.23 (12) | 22.0% | 26.1% | 51.6% | 35.4% [24.4%-40.5%] | 21.9% | -- | 21.9% | MODEL_LONE_OUTLIER | WATCH | +4.1 pp | NORMAL | FRESH | C / LIMITED | ALL_AGREE | VERIFIED |
| Rachel Gailis (`KXITFWMATCH-26NOV11GAIBOH-GAI`) | 0.72 / 0.79 (7) | 75.5% | 73.9% | 48.4% | 64.6% [59.5%-75.6%] | 78.1% | -- | 78.1% | MODEL_LONE_OUTLIER | PASS | -1.6 pp | NORMAL | FRESH | C / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 857.0, B 1680.0; serve-point win A 56.6%, B 48.2%; Elo A 1473.4, B 1297.4; model uncertainty 0.0806
* Form inputs: days since last match A 106, B 205; matches on record A 113, B 105; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.034, surface_pool_high -0.025, surface_dev_loose -0.025, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniel Milavsky / Braden Shick vs Hynek Barton / Maks Kasnikowski -- ATP Challenger Knoxville R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 23:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-11T23:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11MILSHIBARKAS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hynek Barton / Maks Kasnikowski (`KXATPCHALLENGERDOUBLES-26NOV11MILSHIBARKAS-BARKAS`) | 0.14 / 0.20 (3) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daniel Milavsky / Braden Shick (`KXATPCHALLENGERDOUBLES-26NOV11MILSHIBARKAS-MILSHI`) | 0.75 / 0.82 (45) | 78.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Augusto Carvalho / Iserhard vs Braga / Braga -- M25 Santa Cruz do Sul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11AUGISEBRABRA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Augusto Carvalho / Iserhard (`KXITFDOUBLES-26NOV11AUGISEBRABRA-AUGISE`) | -- / 0.02 (554) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Braga / Braga (`KXITFDOUBLES-26NOV11AUGISEBRABRA-BRABRA`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE

## Azam / Reddy vs Bobo / Mcginnis -- M15 Naples FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11AZAREDBOBMCG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Azam / Reddy (`KXITFDOUBLES-26NOV11AZAREDBOBMCG-AZARED`) | 0.91 / 0.96 (827) | 93.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bobo / Mcginnis (`KXITFDOUBLES-26NOV11AZAREDBOBMCG-BOBMCG`) | 0.04 / 0.08 (387) | 6.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Bojicic Ono / Souza vs Alves / Fa Rodriguez Taverna -- M25 Santa Cruz do Sul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11BOJSOUALVFAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alves / Fa Rodriguez Taverna (`KXITFDOUBLES-26NOV11BOJSOUALVFAR-ALVFAR`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bojicic Ono / Souza (`KXITFDOUBLES-26NOV11BOJSOUALVFAR-BOJSOU`) | -- / 0.01 (1) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE

## Bynoe / Portugal vs Almeida / Vega -- M15 Naples FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11BYNPORALMVEG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Almeida / Vega (`KXITFDOUBLES-26NOV11BYNPORALMVEG-ALMVEG`) | 0.72 / 0.81 (8) | 76.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bynoe / Portugal (`KXITFDOUBLES-26NOV11BYNPORALMVEG-BYNPOR`) | 0.14 / 0.23 (45) | 18.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dahlberg / Velcz vs Kapasi / Zapp -- M15 Naples FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11DAHVELKAPZAP:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dahlberg / Velcz (`KXITFDOUBLES-26NOV11DAHVELKAPZAP-DAHVEL`) | 0.76 / 0.78 (1) | 77.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kapasi / Zapp (`KXITFDOUBLES-26NOV11DAHVELKAPZAP-KAPZAP`) | 0.22 / 0.24 (33) | 23.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Alec Deckers vs Brandon Carpico -- M25 Columbus OH R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207793:211734:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brandon Carpico (`KXITFMATCH-26NOV11DECCAR-CAR`) | 0.35 / 0.36 (16328) | 35.5% | -- | 32.1% | 25.5% [24.7%-26.3%] | -- | -- | -- | -- | PASS | -10.0 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Alec Deckers (`KXITFMATCH-26NOV11DECCAR-DEC`) | 0.64 / 0.65 (12892) | 64.5% | -- | 67.9% | 74.5% [73.7%-75.3%] | -- | -- | -- | -- | PASS | +10.0 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 2380.0, B 0.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0078
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose +0.000, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nikita Filin vs Andreja Petrovic -- M25 Columbus OH R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209914:212570:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikita Filin (`KXITFMATCH-26NOV11FILPET-FIL`) | 0.91 / 0.92 (9573) | 91.5% | -- | 57.8% | 27.3% [23.3%-31.8%] | -- | -- | -- | -- | PASS | -64.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Andreja Petrovic (`KXITFMATCH-26NOV11FILPET-PET`) | 0.08 / 0.09 (2814) | 8.5% | -- | 42.2% | 72.7% [68.2%-76.7%] | -- | -- | -- | -- | PASS | +64.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 201.0, B 2276.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0425
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV11FILPET-PET  (YES = Andreja Petrovic)
Model: 73%
Kalshi: 8%
Gap: +64 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose +0.004, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matthew Forbes vs Gavin Young -- M25 Columbus OH R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212405:212733:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthew Forbes (`KXITFMATCH-26NOV11FORYOU-FOR`) | 0.24 / 0.25 (1336) | 24.5% | -- | 56.4% | 46.6% [44.5%-49.0%] | -- | -- | -- | -- | WATCH | +22.1 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gavin Young (`KXITFMATCH-26NOV11FORYOU-YOU`) | 0.75 / 0.76 (10975) | 75.5% | -- | 43.6% | 53.4% [51.0%-55.5%] | -- | -- | -- | -- | PASS | -22.1 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 594.0, B 823.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0226
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV11FORYOU-FOR  (YES = Matthew Forbes)
Model: 47%
Kalshi: 24%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Giamichelle / Sanchez Bronzetti vs Craig / Nolan -- M15 Naples FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11GIASANCRANOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Craig / Nolan (`KXITFDOUBLES-26NOV11GIASANCRANOL-CRANOL`) | 0.56 / 0.62 (200) | 59.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Giamichelle / Sanchez Bronzetti (`KXITFDOUBLES-26NOV11GIASANCRANOL-GIASAN`) | 0.35 / 0.40 (30) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Aidan Kim vs Jonah Braswell -- M25 Columbus OH R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210077:211738:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jonah Braswell (`KXITFMATCH-26NOV11KIMBRA-BRA`) | 0.17 / 0.22 (250) | 19.5% | -- | 19.4% | 26.3% [24.7%-28.5%] | -- | -- | -- | -- | PASS | +6.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aidan Kim (`KXITFMATCH-26NOV11KIMBRA-KIM`) | 0.77 / 0.80 (4) | 78.5% | -- | 80.6% | 73.7% [71.5%-75.3%] | -- | -- | -- | -- | PASS | -4.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 913.0, B 298.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0194
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.017, surface_pool_high -0.021, surface_dev_loose +0.008, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alan Sau Franco vs Luis Carlos Alvarez Valdes -- M15 Zamora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206827:211468:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luis Carlos Alvarez Valdes (`KXITFMATCH-26NOV11SAUALV-ALV`) | 0.96 / 0.97 (2956) | 96.5% | -- | 87.1% | 84.5% [81.7%-87.8%] | -- | -- | -- | -- | PASS | -12.0 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alan Sau Franco (`KXITFMATCH-26NOV11SAUALV-SAU`) | 0.02 / 0.03 (323) | 2.5% | -- | 12.9% | 15.5% [12.2%-18.3%] | -- | -- | -- | -- | PASS | +13.0 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 649.0, B 923.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0304
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Victoria Hu vs Jana Hossam Salah -- W35 Weston FL R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221023:266764:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jana Hossam Salah (`KXITFWMATCH-26NOV11HUXHOS-HOS`) | 0.39 / 0.42 (105) | 40.5% | -- | 45.8% | 41.6% [36.4%-45.8%] | -- | -- | -- | -- | PASS | +1.1 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Victoria Hu (`KXITFWMATCH-26NOV11HUXHOS-HUX`) | 0.56 / 0.58 (37) | 57.0% | -- | 54.2% | 58.4% [54.2%-63.6%] | -- | -- | -- | -- | PASS | +1.4 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2960.0, B 378.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0467
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.031, surface_pool_high -0.031, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Allegra Korpanec Davies vs Lexington Reed -- W35 Weston FL R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:239186:260914:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Allegra Korpanec Davies (`KXITFWMATCH-26NOV11KORREE-KOR`) | 0.30 / 0.36 (1) | 33.0% | -- | 51.6% | 52.1% [50.0%-54.2%] | -- | -- | -- | -- | PASS | +19.1 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lexington Reed (`KXITFWMATCH-26NOV11KORREE-REE`) | 0.65 / 0.68 (6) | 66.5% | -- | 48.4% | 47.9% [45.8%-50.0%] | -- | -- | -- | -- | PASS | -18.6 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1796.0, B 144.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0211
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV11KORREE-KOR  (YES = Allegra Korpanec Davies)
Model: 52%
Kalshi: 33%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.021, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Su-Wei Hsieh / Jelena Ostapenko vs Elise Mertens / Shuai Zhang -- WTA Finals Women Doubles Group

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-12 02:30Z
* Current expected start: 2026-11-12 00:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-11 21:14Z
* Recommended handicap-by time: 2026-11-11 23:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_FINALS) · surface ? · scheduled 2026-11-12T02:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11HSIOSTMERZHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Su-Wei Hsieh / Jelena Ostapenko (`KXWTADOUBLES-26NOV11HSIOSTMERZHA-HSIOST`) | 0.51 / 0.55 (612) | 53.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Elise Mertens / Shuai Zhang (`KXWTADOUBLES-26NOV11HSIOSTMERZHA-MERZHA`) | 0.45 / 0.47 (257) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Nefve / Peck vs Gurenko / Peter Van Noord -- M25 Montreal R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 00:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11NEFPECGURPET:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gurenko / Peter Van Noord (`KXITFDOUBLES-26NOV11NEFPECGURPET-GURPET`) | 0.37 / 0.42 (47) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nefve / Peck (`KXITFDOUBLES-26NOV11NEFPECGURPET-NEFPEC`) | 0.52 / 0.60 (241) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Rozin / Silva vs Gerbaud / Weekes -- M25 Montreal R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 00:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11ROZSILGERWEE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gerbaud / Weekes (`KXITFDOUBLES-26NOV11ROZSILGERWEE-GERWEE`) | 0.07 / 0.64 (2) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rozin / Silva (`KXITFDOUBLES-26NOV11ROZSILGERWEE-ROZSIL`) | 0.23 / 0.89 (2) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Thomas George / Nicholas Tudorica vs Bedard / Roy -- M25 Montreal R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 00:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11THONICBEDROY:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bedard / Roy (`KXITFDOUBLES-26NOV11THONICBEDROY-BEDROY`) | 0.05 / 0.06 (2) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Thomas George / Nicholas Tudorica (`KXITFDOUBLES-26NOV11THONICBEDROY-THONIC`) | 0.94 / 0.95 (483) | 94.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Andres Andrade / Johannes Ingildsen vs Jody Maginley / Karl Poling -- ATP Challenger Knoxville R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 00:50Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-12T00:50:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11ANDINGMAGPOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andres Andrade / Johannes Ingildsen (`KXATPCHALLENGERDOUBLES-26NOV11ANDINGMAGPOL-ANDING`) | 0.53 / 0.54 (177) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jody Maginley / Karl Poling (`KXATPCHALLENGERDOUBLES-26NOV11ANDINGMAGPOL-MAGPOL`) | 0.44 / 0.48 (701) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

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
| Basel / Martinez (`KXITFDOUBLES-26NOV11DEAGARBASMAR-BASMAR`) | 0.70 / 0.71 (238) | 70.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| De Armas / Garay (`KXITFDOUBLES-26NOV11DEAGARBASMAR-DEAGAR`) | 0.26 / 0.34 (238) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Oscar Lacides / Shunsuke Mitsui vs Miguel Angel Reyes-Varela / Reese Stalder -- ATP Challenger Knoxville R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-12T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11LACMITREYSTA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oscar Lacides / Shunsuke Mitsui (`KXATPCHALLENGERDOUBLES-26NOV11LACMITREYSTA-LACMIT`) | 0.23 / 0.28 (28) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Miguel Angel Reyes-Varela / Reese Stalder (`KXATPCHALLENGERDOUBLES-26NOV11LACMITREYSTA-REYSTA`) | 0.68 / 0.74 (200) | 71.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Pagani / Re vs Branchetti / Mouilleron Salvo -- M15 Roldan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11PAGREXBRAMOU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Branchetti / Mouilleron Salvo (`KXITFDOUBLES-26NOV11PAGREXBRAMOU-BRAMOU`) | 0.46 / 0.52 (252) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pagani / Re (`KXITFDOUBLES-26NOV11PAGREXBRAMOU-PAGREX`) | 0.45 / 0.52 (200) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Kai Thompson vs Matteo Covato -- M15 Zamora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:149145:214142:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Covato (`KXITFMATCH-26NOV11THOCOV-COV`) | 0.46 / 0.47 (19925) | 46.5% | -- | 34.4% | 33.0% [32.4%-34.0%] | -- | -- | -- | -- | PASS | -13.5 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kai Thompson (`KXITFMATCH-26NOV11THOCOV-THO`) | 0.53 / 0.54 (16777) | 53.5% | -- | 65.6% | 67.0% [66.0%-67.6%] | -- | -- | -- | -- | PASS | +13.5 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 164.0, B 2229.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0079
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Adams / Sahdiieva vs Dalina Amariei / Vilar -- W35 Weston FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11ADASAHDALVIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adams / Sahdiieva (`KXITFWDOUBLES-26NOV11ADASAHDALVIL-ADASAH`) | 0.95 / 0.97 (17) | 96.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dalina Amariei / Vilar (`KXITFWDOUBLES-26NOV11ADASAHDALVIL-DALVIL`) | 0.01 / 0.05 (176) | 3.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Atturu / Skegro vs Burgic / Podhajecka -- W35 Weston FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11ATTSKEBURPOD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Atturu / Skegro (`KXITFWDOUBLES-26NOV11ATTSKEBURPOD-ATTSKE`) | 0.03 / 0.07 (8) | 5.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Burgic / Podhajecka (`KXITFWDOUBLES-26NOV11ATTSKEBURPOD-BURPOD`) | 0.88 / 0.93 (2) | 90.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Ana Grubor vs Virginia Crocker -- W15 Lincoln NE R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:258191:270059:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Virginia Crocker (`KXITFWMATCH-26NOV11GRUCRO-CRO`) | 0.13 / 0.14 (255) | 13.5% | -- | 15.9% | 32.0% [24.8%-40.5%] | -- | -- | -- | -- | PASS | +18.5 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ana Grubor (`KXITFWMATCH-26NOV11GRUCRO-GRU`) | 0.86 / 0.87 (5082) | 86.5% | -- | 84.1% | 68.0% [59.5%-75.2%] | -- | -- | -- | -- | PASS | -18.5 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1727.0, B 441.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0783
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV11GRUCRO-CRO  (YES = Virginia Crocker)
Model: 32%
Kalshi: 14%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.028, surface_dev_loose +0.019, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Diego Hidalgo / Andres Molteni vs Arklon Huertas Del Pino Cordova / Alexander Merino -- ATP Challenger Lima R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-12T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11HIDMOLHUEMER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diego Hidalgo / Andres Molteni (`KXATPCHALLENGERDOUBLES-26NOV11HIDMOLHUEMER-HIDMOL`) | 0.07 / 0.92 (7) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arklon Huertas Del Pino Cordova / Alexander Merino (`KXATPCHALLENGERDOUBLES-26NOV11HIDMOLHUEMER-HUEMER`) | 0.05 / 0.91 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hammond / McCartney vs Visker / Wessels -- M25 Montreal R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 01:51Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T01:51:18Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11HAMMCCVISWES:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hammond / McCartney (`KXITFDOUBLES-26NOV11HAMMCCVISWES-HAMMCC`) | 0.02 / 0.91 (2) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Visker / Wessels (`KXITFDOUBLES-26NOV11HAMMCCVISWES-VISWES`) | 0.02 / 0.91 (2) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Moreau / Nations vs Bulatova / Kuhl -- W35 Weston FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11MORNATBULKUH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bulatova / Kuhl (`KXITFWDOUBLES-26NOV11MORNATBULKUH-BULKUH`) | 0.10 / 0.85 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Moreau / Nations (`KXITFWDOUBLES-26NOV11MORNATBULKUH-MORNAT`) | 0.10 / 0.85 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lucca Cervantes Tomas / Alejandro Reyes Tirado vs Dagda Mireles / Manuel Jorquera -- M15 Zamora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 02:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T02:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11LUCALEDAGMAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dagda Mireles / Manuel Jorquera (`KXITFDOUBLES-26NOV11LUCALEDAGMAN-DAGMAN`) | 0.66 / 0.70 (60) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lucca Cervantes Tomas / Alejandro Reyes Tirado (`KXITFDOUBLES-26NOV11LUCALEDAGMAN-LUCALE`) | 0.30 / 0.34 (1) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Nicolas Mejia vs Max Hans Rehberg -- ATP Challenger Knoxville R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 02:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-12T02:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200711:208819:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Mejia (`KXATPCHALLENGERMATCH-26NOV11MEJREH-MEJ`) | 0.37 / 0.38 (4370) | 37.5% | -- | 38.2% | 41.6% [40.2%-44.5%] | -- | -- | -- | -- | SHADOW_BET | +4.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Max Hans Rehberg (`KXATPCHALLENGERMATCH-26NOV11MEJREH-REH`) | 0.62 / 0.63 (509) | 62.5% | -- | 61.8% | 58.4% [55.5%-59.8%] | -- | -- | -- | -- | PASS | -4.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4996.0, B 4177.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0218
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.004, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Alujas / Benson vs Cooper / McKennon -- M15 Zamora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11ALUBENCOOMCK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alujas / Benson (`KXITFDOUBLES-26NOV11ALUBENCOOMCK-ALUBEN`) | 0.49 / 0.59 (60) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cooper / McKennon (`KXITFDOUBLES-26NOV11ALUBENCOOMCK-COOMCK`) | 0.37 / 0.46 (46) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Alvarado / Hornung vs Flores / Matta -- M15 Zamora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11ALVHORFLOMAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alvarado / Hornung (`KXITFDOUBLES-26NOV11ALVHORFLOMAT-ALVHOR`) | 0.04 / 0.79 (2) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Flores / Matta (`KXITFDOUBLES-26NOV11ALVHORFLOMAT-FLOMAT`) | 0.16 / 0.91 (2) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Battistone / Battistone vs Anthrop / Stearns -- M25 Columbus OH R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11BATBATANTSTE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anthrop / Stearns (`KXITFDOUBLES-26NOV11BATBATANTSTE-ANTSTE`) | 0.14 / 0.91 (2) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Battistone / Battistone (`KXITFDOUBLES-26NOV11BATBATANTSTE-BATBAT`) | 0.03 / 0.79 (2) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Simon Caldwell vs William Manning -- M25 Columbus OH R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 03:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213152:214063:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Simon Caldwell (`KXITFMATCH-26NOV11CALMAN-CAL`) | 0.26 / 0.30 (1) | 28.0% | -- | 24.0% | 38.1% [34.0%-40.0%] | -- | -- | -- | -- | PASS | +10.1 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| William Manning (`KXITFMATCH-26NOV11CALMAN-MAN`) | 0.69 / 0.71 (250) | 70.0% | -- | 76.0% | 61.9% [60.0%-66.0%] | -- | -- | -- | -- | PASS | -8.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 192.0, B 296.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0297
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose -0.009, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Agustin Eduardo Cuellar Lorberg vs Eduardo Ribeiro -- M25 Santa Cruz do Sul R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 03:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200495:208273:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Agustin Eduardo Cuellar Lorberg (`KXITFMATCH-26NOV11CUERIB-CUE`) | 0.13 / 0.16 (29) | 14.5% | -- | 21.0% | 8.8% [8.1%-9.6%] | -- | -- | -- | -- | PASS | -5.7 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Eduardo Ribeiro (`KXITFMATCH-26NOV11CUERIB-RIB`) | 0.81 / 0.84 (18) | 82.5% | -- | 79.0% | 91.2% [90.4%-92.0%] | -- | -- | -- | -- | PASS | +8.7 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 169.0, B 3426.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.008
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.004, surface_dev_loose -0.003, surface_dev_tight +0.002
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Juan Pablo Ficovich vs Oscar Jose Gutierrez -- M25 Santa Cruz do Sul R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 03:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:121264:126663:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Pablo Ficovich (`KXITFMATCH-26NOV11FICGUT-FIC`) | 0.61 / 0.70 (5) | 65.5% | -- | 74.7% | 77.9% [75.9%-79.8%] | -- | -- | -- | -- | WATCH | +12.4 pp | REVIEW | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oscar Jose Gutierrez (`KXITFMATCH-26NOV11FICGUT-GUT`) | 0.32 / 0.38 (10) | 35.0% | -- | 25.3% | 22.1% [20.2%-24.1%] | -- | -- | -- | -- | PASS | -12.9 pp | REVIEW | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4225.0, B 2766.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.019
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.004, surface_dev_loose -0.004, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Fuchs / Fuchs vs Bassem Sobhy / Kelly -- M25 Columbus OH R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11FUCFUCBASKEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bassem Sobhy / Kelly (`KXITFDOUBLES-26NOV11FUCFUCBASKEL-BASKEL`) | 0.02 / 0.91 (2) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fuchs / Fuchs (`KXITFDOUBLES-26NOV11FUCFUCBASKEL-FUCFUC`) | 0.02 / 0.91 (2) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jacome Jaramillo / Shalin Shah vs Lilov / Petak -- M25 Columbus OH R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11JACSHALILPET:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jacome Jaramillo / Shalin Shah (`KXITFDOUBLES-26NOV11JACSHALILPET-JACSHA`) | 0.07 / 0.15 (22) | 11.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lilov / Petak (`KXITFDOUBLES-26NOV11JACSHALILPET-LILPET`) | 0.82 / 0.90 (258) | 86.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Lautaro Midon vs Miguel Tobon -- ATP Challenger Lima R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 03:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-12T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:101495:210510:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lautaro Midon (`KXATPCHALLENGERMATCH-26NOV11MIDTOB-MID`) | 0.64 / 0.65 (7905) | 64.5% | -- | 58.2% | 65.6% [62.3%-76.6%] | 63.8% | 64.8% | 64.8% | MODEL_LONE_OUTLIER | PASS | +1.1 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Miguel Tobon (`KXATPCHALLENGERMATCH-26NOV11MIDTOB-TOB`) | 0.36 / 0.37 (1148) | 36.5% | -- | 41.8% | 34.4% [23.4%-37.7%] | 36.2% | 35.5% | 35.5% | MODEL_LONE_OUTLIER | PASS | -2.1 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4759.0, B 3281.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0718
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.010, surface_dev_loose -0.009, surface_dev_tight +0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Karla Bartel vs Conley Raidt -- W15 Lincoln NE R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11BARRAI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karla Bartel (`KXITFWMATCH-26NOV11BARRAI-BAR`) | 0.81 / 0.82 (8605) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Conley Raidt (`KXITFWMATCH-26NOV11BARRAI-RAI`) | 0.18 / 0.19 (3181) | 18.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Barbara Gatica vs Giovana Schincariol Delatorre Barbosa -- W15 São Carlos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211903:266781:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barbara Gatica (`KXITFWMATCH-26NOV11GATSCH-GAT`) | 0.98 / 0.99 (18887) | 98.5% | -- | 89.1% | 89.6% [88.3%-91.4%] | -- | -- | -- | -- | PASS | -8.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Giovana Schincariol Delatorre Barbosa (`KXITFWMATCH-26NOV11GATSCH-SCH`) | 0.01 / 0.02 (7579) | 1.5% | -- | 10.9% | 10.4% [8.6%-11.7%] | -- | -- | -- | -- | PASS | +8.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 633.0, B 533.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0154
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.002, surface_dev_loose +0.012, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maria Kononova vs Catherine Gagnon -- W15 Lincoln NE R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215236:263675:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Catherine Gagnon (`KXITFWMATCH-26NOV11KONGAG-GAG`) | 0.26 / 0.28 (60) | 27.0% | -- | 71.3% | 41.5% [40.5%-42.6%] | -- | -- | -- | -- | PASS | +14.5 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Kononova (`KXITFWMATCH-26NOV11KONGAG-KON`) | 0.71 / 0.75 (4) | 73.0% | -- | 28.7% | 58.5% [57.4%-59.5%] | -- | -- | -- | -- | PASS | -14.5 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 370.0, B 56.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0104
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kallista Liu vs Karlin Schock -- W15 Lincoln NE R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264180:270127:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kallista Liu (`KXITFWMATCH-26NOV11LIUSCH-LIU`) | 0.94 / 0.95 (1136) | 94.5% | -- | 56.9% | 57.4% [56.4%-57.4%] | -- | -- | -- | -- | PASS | -37.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Karlin Schock (`KXITFWMATCH-26NOV11LIUSCH-SCH`) | 0.04 / 0.05 (744) | 4.5% | -- | 43.1% | 42.6% [42.6%-43.6%] | -- | -- | -- | -- | PASS | +38.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1064.0, B 117.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0053
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV11LIUSCH-SCH  (YES = Karlin Schock)
Model: 43%
Kalshi: 4%
Gap: +38 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.011, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Katie Spencer vs Emily Sartz-Lunde -- W15 Lincoln NE R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:253665:270382:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emily Sartz-Lunde (`KXITFWMATCH-26NOV11SPESAR-SAR`) | 0.59 / 0.60 (6276) | 59.5% | -- | 65.6% | 59.0% [58.5%-60.6%] | -- | -- | -- | -- | PASS | -0.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Katie Spencer (`KXITFWMATCH-26NOV11SPESAR-SPE`) | 0.40 / 0.41 (357) | 40.5% | -- | 34.4% | 41.0% [39.4%-41.5%] | -- | -- | -- | -- | PASS | +0.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 128.0, B 502.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0105
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ethan Cook / Tai Leonard Sach vs Blake Ellis / Li Tu -- ATP Challenger Brisbane QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-12T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11COOSATELLTUL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ethan Cook / Tai Leonard Sach (`KXATPCHALLENGERDOUBLES-26NOV11COOSATELLTUL-COOSAT`) | 0.32 / 0.40 (16) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Blake Ellis / Li Tu (`KXATPCHALLENGERDOUBLES-26NOV11COOSATELLTUL-ELLTUL`) | 0.60 / 0.67 (1) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dane Sweeny vs Casey Hoole -- ATP Challenger Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-12T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208013:211315:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Casey Hoole (`KXATPCHALLENGERMATCH-26NOV11SWEHOO-HOO`) | 0.30 / 0.31 (2668) | 30.5% | -- | 17.3% | 17.3% [16.6%-17.7%] | 32.3% | 31.3% | 31.3% | MODEL_LONE_OUTLIER | PASS | -13.2 pp | REVIEW | FRESH | F / POOR | EXTERNAL_STALE | VERIFIED |
| Dane Sweeny (`KXATPCHALLENGERMATCH-26NOV11SWEHOO-SWE`) | 0.70 / 0.71 (17404) | 70.5% | -- | 82.7% | 82.7% [82.3%-83.4%] | 67.7% | 68.8% | 68.8% | MODEL_LONE_OUTLIER | PASS | +12.2 pp | REVIEW | FRESH | F / POOR | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5456.0, B 163.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0055
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.006, surface_pool_high +0.000, surface_dev_loose -0.001, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Garcia / Carolina Millan Acosta vs Colmegna / Zolotareva -- W50 Chihuahua QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11GARCARCOLZOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Colmegna / Zolotareva (`KXITFWDOUBLES-26NOV11GARCARCOLZOL-COLZOL`) | 0.53 / 0.82 (1) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Garcia / Carolina Millan Acosta (`KXITFWDOUBLES-26NOV11GARCARCOLZOL-GARCAR`) | 0.33 / 0.81 (1) | 57.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Strakhova / Tikhonova vs Allegre / Avataneo -- W50 Chihuahua QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11STRTIKALLAVA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Allegre / Avataneo (`KXITFWDOUBLES-26NOV11STRTIKALLAVA-ALLAVA`) | 0.03 / 0.04 (30) | 3.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Strakhova / Tikhonova (`KXITFWDOUBLES-26NOV11STRTIKALLAVA-STRTIK`) | 0.94 / 0.96 (236) | 95.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## De Alba / Sau Franco vs Echazu / Esteban Rico Arias -- M15 Zamora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11DEASAUECHEST:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| De Alba / Sau Franco (`KXITFDOUBLES-26NOV11DEASAUECHEST-DEASAU`) | 0.43 / 0.89 (1) | 66.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Echazu / Esteban Rico Arias (`KXITFDOUBLES-26NOV11DEASAUECHEST-ECHEST`) | 0.06 / 0.76 (1) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Arjun Kadhe / Aoran Wang vs Finn Bass / Scott Duncan -- ATP Challenger Matsuyama QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-12T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11KADWANBASDUN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Finn Bass / Scott Duncan (`KXATPCHALLENGERDOUBLES-26NOV11KADWANBASDUN-BASDUN`) | 0.41 / 0.94 (56) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arjun Kadhe / Aoran Wang (`KXATPCHALLENGERDOUBLES-26NOV11KADWANBASDUN-KADWAN`) | 0.51 / 0.65 (56) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Ognjen Milic vs Shunsuke Nakagawa -- ATP Challenger Matsuyama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-12T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209905:212207:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ognjen Milic (`KXATPCHALLENGERMATCH-26NOV11MILNAK-MIL`) | 0.76 / 0.77 (1745) | 76.5% | -- | 80.9% | 78.1% [75.8%-80.2%] | 75.0% | 76.1% | 76.1% | MARKETS_AGREE | PASS | +1.6 pp | NORMAL | FRESH | B / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Shunsuke Nakagawa (`KXATPCHALLENGERMATCH-26NOV11MILNAK-NAK`) | 0.23 / 0.24 (10) | 23.5% | -- | 19.1% | 21.9% [19.8%-24.2%] | 25.0% | 23.8% | 23.8% | MARKETS_AGREE | PASS | -1.6 pp | NORMAL | FRESH | B / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3142.0, B 1170.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0225
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.003, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Rio Noguchi vs Yi Zhou -- ATP Challenger Matsuyama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-12T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200677:212044:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rio Noguchi (`KXATPCHALLENGERMATCH-26NOV11NOGZHO-NOG`) | 0.36 / 0.37 (3736) | 36.5% | -- | 49.5% | 48.5% [46.5%-51.0%] | 36.2% | 37.1% | 37.1% | MODEL_LONE_OUTLIER | SHADOW_BET | +12.0 pp | REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Yi Zhou (`KXATPCHALLENGERMATCH-26NOV11NOGZHO-ZHO`) | 0.63 / 0.64 (226) | 63.5% | -- | 50.5% | 51.5% [49.0%-53.5%] | 63.8% | 63.3% | 63.3% | MODEL_LONE_OUTLIER | PASS | -12.0 pp | REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4350.0, B 3814.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0226
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.020, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Das / Maria Ionescu vs Kock / Schumann -- W15 Lincoln NE R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11DASMARKOCSCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Das / Maria Ionescu (`KXITFWDOUBLES-26NOV11DASMARKOCSCH-DASMAR`) | 0.69 / 0.85 (2) | 77.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kock / Schumann (`KXITFWDOUBLES-26NOV11DASMARKOCSCH-KOCSCH`) | 0.06 / 0.26 (15) | 16.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Gasparovic / Malygina vs Esposito Cogan / Moe -- W15 Lincoln NE R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11GASMALESPMOE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Esposito Cogan / Moe (`KXITFWDOUBLES-26NOV11GASMALESPMOE-ESPMOE`) | 0.10 / 0.84 (14) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gasparovic / Malygina (`KXITFWDOUBLES-26NOV11GASMALESPMOE-GASMAL`) | 0.09 / 0.83 (1) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kruger / Refaat vs Crocker / Suh -- W15 Lincoln NE R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11KRUREFCROSUH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Crocker / Suh (`KXITFWDOUBLES-26NOV11KRUREFCROSUH-CROSUH`) | 0.09 / 0.68 (48) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kruger / Refaat (`KXITFWDOUBLES-26NOV11KRUREFCROSUH-KRUREF`) | 0.26 / 0.84 (1) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Blake Bayldon / Thomas Fancutt vs Enzo Aguiard / Pavle Marinkov -- ATP Challenger Brisbane QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 05:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-12T05:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11BAYFANAGUMAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Enzo Aguiard / Pavle Marinkov (`KXATPCHALLENGERDOUBLES-26NOV11BAYFANAGUMAR-AGUMAR`) | 0.08 / 0.16 (11) | 12.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Blake Bayldon / Thomas Fancutt (`KXATPCHALLENGERDOUBLES-26NOV11BAYFANAGUMAR-BAYFAN`) | 0.82 / 0.94 (50) | 88.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Christian Langmo vs James McCabe -- ATP Challenger Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 05:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-12T05:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132052:210317:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Christian Langmo (`KXATPCHALLENGERMATCH-26NOV11LANMCC-LAN`) | 0.37 / 0.39 (6176) | 38.0% | -- | 48.1% | 45.2% [43.3%-46.2%] | 38.4% | 38.4% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +7.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| James McCabe (`KXATPCHALLENGERMATCH-26NOV11LANMCC-MCC`) | 0.61 / 0.63 (2964) | 62.0% | -- | 51.9% | 54.8% [53.8%-56.7%] | 61.6% | 61.6% | -- | INSUFFICIENT_INPUTS | PASS | -7.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3910.0, B 4552.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0143
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.009, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Gabrielle Clarke / Clarke vs Cross / Papamichail -- W50 Chihuahua QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 05:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T05:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11GABCLACROPAP:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cross / Papamichail (`KXITFWDOUBLES-26NOV11GABCLACROPAP-CROPAP`) | 0.64 / 0.86 (1) | 75.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gabrielle Clarke / Clarke (`KXITFWDOUBLES-26NOV11GABCLACROPAP-GABCLA`) | 0.07 / 0.32 (1) | 19.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hinojosa Gomez / Tran vs Lillian Chavez / Garcia Anzures -- W50 Chihuahua QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 05:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T05:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11HINTRALILGAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hinojosa Gomez / Tran (`KXITFWDOUBLES-26NOV11HINTRALILGAR-HINTRA`) | 0.79 / 0.85 (2) | 82.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lillian Chavez / Garcia Anzures (`KXITFWDOUBLES-26NOV11HINTRALILGAR-LILGAR`) | 0.08 / 0.18 (231) | 13.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Aguilar / Moreno Rico vs Odiseo Alvarado Berrospi / Betancourt -- M15 Zamora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11AGUMORODIBET:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aguilar / Moreno Rico (`KXITFDOUBLES-26NOV11AGUMORODIBET-AGUMOR`) | 0.75 / 0.78 (1) | 76.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Odiseo Alvarado Berrospi / Betancourt (`KXITFDOUBLES-26NOV11AGUMORODIBET-ODIBET`) | 0.19 / 0.75 (1) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Olivia Gadecki vs Savannah Broadus -- W75 Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216265:221221:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Savannah Broadus (`KXITFWMATCH-26NOV11GADBRO-BRO`) | 0.45 / 0.46 (247) | 45.5% | -- | 61.0% | 34.1% [22.1%-43.7%] | 43.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.4 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Olivia Gadecki (`KXITFWMATCH-26NOV11GADBRO-GAD`) | 0.55 / 0.56 (135) | 55.5% | -- | 39.1% | 65.9% [56.3%-77.9%] | 56.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +10.4 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3148.0, B 898.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.1082
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.005, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carol Young Suh Lee vs BoYoung Jeong -- W75 Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221109:221803:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BoYoung Jeong (`KXITFWMATCH-26NOV11LEEJEO-JEO`) | 0.11 / 0.14 (112) | 12.5% | -- | 38.5% | 32.1% [25.3%-35.0%] | 15.5% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +19.6 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carol Young Suh Lee (`KXITFWMATCH-26NOV11LEEJEO-LEE`) | 0.86 / 0.89 (361) | 87.5% | -- | 61.5% | 67.9% [65.0%-74.7%] | 84.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -19.6 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4047.0, B 2517.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0485
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV11LEEJEO-JEO  (YES = BoYoung Jeong)
Model: 32%
Kalshi: 12%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Himeno Sakatsume vs Yujia Huang -- W75 Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221124:264207:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yujia Huang (`KXITFWMATCH-26NOV11SAKHUA-HUA`) | 0.23 / 0.25 (304) | 24.0% | -- | 29.0% | 20.8% [15.1%-23.9%] | 26.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.2 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Himeno Sakatsume (`KXITFWMATCH-26NOV11SAKHUA-SAK`) | 0.74 / 0.77 (723) | 75.5% | -- | 71.0% | 79.2% [76.1%-84.9%] | 73.6% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +3.8 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3693.0, B 1640.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.044
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.011, surface_dev_loose -0.004, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pruchya Isaro / Yuta Shimizu vs Siddhant Banthia / Anirudh Chandrasekar -- ATP Challenger Matsuyama QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 06:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-12T06:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11ISASHIBANCHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Siddhant Banthia / Anirudh Chandrasekar (`KXATPCHALLENGERDOUBLES-26NOV11ISASHIBANCHA-BANCHA`) | 0.38 / 0.55 (56) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pruchya Isaro / Yuta Shimizu (`KXATPCHALLENGERDOUBLES-26NOV11ISASHIBANCHA-ISASHI`) | 0.51 / 0.68 (56) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Rei Sakamoto vs Kasidit Samrej -- ATP Challenger Matsuyama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 06:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-12T06:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208937:210536:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rei Sakamoto (`KXATPCHALLENGERMATCH-26NOV11SAKSAM-SAK`) | 0.85 / 0.87 (6347) | 86.0% | -- | 68.2% | 70.3% [69.0%-72.0%] | 83.6% | 86.3% | 86.3% | MODEL_LONE_OUTLIER | PASS | -15.7 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Kasidit Samrej (`KXATPCHALLENGERMATCH-26NOV11SAKSAM-SAM`) | 0.14 / 0.15 (6718) | 14.5% | -- | 31.8% | 29.7% [28.0%-31.0%] | 16.4% | 14.0% | 14.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +15.2 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4519.0, B 4164.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0152
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV11SAKSAM-SAM  (YES = Kasidit Samrej)
Model: 30%
Kalshi: 14%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: EXTERNAL_STALE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.008, surface_dev_loose +0.004, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Max Schoenhaus vs Taro Daniel -- ATP Challenger Matsuyama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 06:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-12T06:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106121:212268:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Taro Daniel (`KXATPCHALLENGERMATCH-26NOV11SCHDAN-DAN`) | 0.62 / 0.63 (144) | 62.5% | -- | 46.1% | 52.9% [49.0%-58.8%] | 63.1% | 62.7% | 62.7% | MODEL_LONE_OUTLIER | PASS | -9.6 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Max Schoenhaus (`KXATPCHALLENGERMATCH-26NOV11SCHDAN-SCH`) | 0.36 / 0.38 (4229) | 37.0% | -- | 53.9% | 47.1% [41.2%-51.0%] | 36.9% | 37.4% | 37.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +10.1 pp | REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3062.0, B 4270.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0486
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.019, surface_dev_loose +0.015, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Carl Emil Overbeck vs Juncheng Shang -- ATP Challenger Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 06:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-12T06:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209274:209992:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carl Emil Overbeck (`KXATPCHALLENGERMATCH-26NOV11OVESHA-OVE`) | 0.23 / 0.24 (116) | 23.5% | -- | 60.7% | 38.9% [28.9%-47.5%] | 26.5% | 24.6% | 24.6% | MODEL_LONE_OUTLIER | WATCH | +15.4 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Juncheng Shang (`KXATPCHALLENGERMATCH-26NOV11OVESHA-SHA`) | 0.75 / 0.76 (530) | 75.5% | -- | 39.3% | 61.1% [52.4%-71.1%] | 73.5% | 75.2% | 75.2% | MODEL_LONE_OUTLIER | PASS | -14.4 pp | REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 2038.0, B 2480.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0932
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV11OVESHA-OVE  (YES = Carl Emil Overbeck)
Model: 39%
Kalshi: 24%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: EXTERNAL_STALE
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.010, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Moerani Bouzige / Casey Hoole vs Alafia Ayeni / Kokoro Isomura -- ATP Challenger Brisbane QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 06:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-12T06:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11BOUHOOAVEISO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alafia Ayeni / Kokoro Isomura (`KXATPCHALLENGERDOUBLES-26NOV11BOUHOOAVEISO-AVEISO`) | 0.65 / 0.79 (3) | 72.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Moerani Bouzige / Casey Hoole (`KXATPCHALLENGERDOUBLES-26NOV11BOUHOOAVEISO-BOUHOO`) | 0.29 / 0.92 (16) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Naiktha Bains vs Zhuoxuan Bai -- W75 Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206362:222296:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naiktha Bains (`KXITFWMATCH-26NOV11BAIBAI2-BAI`) | 0.31 / 0.34 (23) | 32.5% | -- | 34.5% | 29.3% [25.7%-34.4%] | 34.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.2 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zhuoxuan Bai (`KXITFWMATCH-26NOV11BAIBAI2-BAI2`) | 0.64 / 0.68 (6) | 66.0% | -- | 65.5% | 70.7% [65.5%-74.3%] | 65.7% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +4.7 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2400.0, B 1601.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0436
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.038, surface_pool_high -0.035, surface_dev_loose -0.009, surface_dev_tight +0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Berfu Cengiz vs Remika Ohashi -- W50 Yokohama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214507:260957:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Berfu Cengiz (`KXITFWMATCH-26NOV11CENOHA-CEN`) | 0.92 / 0.95 (274) | 93.5% | -- | 82.5% | 78.1% [74.8%-82.5%] | 92.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.4 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Remika Ohashi (`KXITFWMATCH-26NOV11CENOHA-OHA`) | 0.05 / 0.06 (298) | 5.5% | -- | 17.5% | 21.9% [17.5%-25.2%] | 7.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +16.4 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1612.0, B 421.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0385
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV11CENOHA-OHA  (YES = Remika Ohashi)
Model: 22%
Kalshi: 6%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.044, surface_pool_high -0.033, surface_dev_loose +0.019, surface_dev_tight -0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Joanna Garland vs Sijia Wei -- W75 Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220466:221096:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joanna Garland (`KXITFWMATCH-26NOV11GARWEI-GAR`) | 0.61 / 0.64 (98) | 62.5% | -- | 60.8% | 59.8% [56.8%-62.5%] | 62.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sijia Wei (`KXITFWMATCH-26NOV11GARWEI-WEI`) | 0.35 / 0.38 (121) | 36.5% | -- | 39.2% | 40.2% [37.5%-43.2%] | 37.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +3.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2480.0, B 2150.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0285
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.031, surface_dev_loose -0.026, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofia Johnson vs Miriam Bianca Bulgaru -- W50 Chihuahua R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214480:260338:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miriam Bianca Bulgaru (`KXITFWMATCH-26NOV11JOHBUL-BUL`) | 0.33 / 0.35 (268) | 34.0% | -- | 14.2% | 42.5% [31.0%-59.5%] | 34.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +8.6 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sofia Johnson (`KXITFWMATCH-26NOV11JOHBUL-JOH`) | 0.64 / 0.67 (65) | 65.5% | -- | 85.8% | 57.5% [40.5%-69.0%] | 65.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.1 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1199.0, B 3417.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.1428
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.031, surface_pool_high -0.032, surface_dev_loose +0.026, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Momoko Kobori vs Sara Saito -- W50 Yokohama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215468:260170:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Momoko Kobori (`KXITFWMATCH-26NOV11KOBSAI-KOB`) | 0.31 / 0.34 (33) | 32.5% | -- | 65.2% | 56.9% [47.9%-61.6%] | -- | -- | -- | -- | PASS | +24.4 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sara Saito (`KXITFWMATCH-26NOV11KOBSAI-SAI`) | 0.66 / 0.68 (435) | 67.0% | -- | 34.8% | 43.1% [38.4%-52.1%] | -- | -- | -- | -- | PASS | -23.9 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1427.0, B 3341.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0688
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV11KOBSAI-KOB  (YES = Momoko Kobori)
Model: 57%
Kalshi: 32%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.011, surface_dev_loose +0.021, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yeonwoo Ku vs Naho Sato -- W50 Yokohama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11KUXSAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yeonwoo Ku (`KXITFWMATCH-26NOV11KUXSAT-KUX`) | 0.73 / 0.74 (7) | 73.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Naho Sato (`KXITFWMATCH-26NOV11KUXSAT-SAT`) | 0.24 / 0.25 (105) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rinko Matsuda vs YeXin Ma -- W50 Yokohama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11MATMAX:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rinko Matsuda (`KXITFWMATCH-26NOV11MATMAX-MAT`) | 0.28 / 0.31 (145) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| YeXin Ma (`KXITFWMATCH-26NOV11MATMAX-MAX`) | 0.66 / 0.70 (4) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuki Naito vs Xinxin Yao -- W75 Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216044:252587:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuki Naito (`KXITFWMATCH-26NOV11NAIYAO-NAI`) | 0.45 / 0.46 (69) | 45.5% | -- | 59.5% | 50.0% [45.2%-54.2%] | 46.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +4.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Xinxin Yao (`KXITFWMATCH-26NOV11NAIYAO-YAO`) | 0.54 / 0.55 (358) | 54.5% | -- | 40.5% | 50.0% [45.8%-54.8%] | 53.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2186.0, B 2972.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0452
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.043, surface_pool_high -0.037, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Victoria Rodriguez vs Vivian Wolff -- W50 Chihuahua R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-12T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211874:215386:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Victoria Rodriguez (`KXITFWMATCH-26NOV11RODWOL-ROD`) | 0.26 / 0.28 (410) | 27.0% | -- | 19.2% | 24.3% [21.4%-30.5%] | 28.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Vivian Wolff (`KXITFWMATCH-26NOV11RODWOL-WOL`) | 0.71 / 0.73 (27) | 72.0% | -- | 80.8% | 75.7% [69.5%-78.5%] | 71.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2050.0, B 2229.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0451
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.004, surface_dev_loose -0.016, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexandru Jecan / Szymon Kielan vs Yusuke Kusuhara / Shunsuke Nakagawa -- ATP Challenger Matsuyama QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 07:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-12T07:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11JECKIEKUSNAK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandru Jecan / Szymon Kielan (`KXATPCHALLENGERDOUBLES-26NOV11JECKIEKUSNAK-JECKIE`) | 0.32 / 0.55 (3) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yusuke Kusuhara / Shunsuke Nakagawa (`KXATPCHALLENGERDOUBLES-26NOV11JECKIEKUSNAK-KUSNAK`) | 0.55 / 0.72 (56) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Finn Reynolds / James Watt vs Masamichi Imamura / Rio Noguchi -- ATP Challenger Matsuyama QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 07:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-12T07:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11REYWATIMANOG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Masamichi Imamura / Rio Noguchi (`KXATPCHALLENGERDOUBLES-26NOV11REYWATIMANOG-IMANOG`) | 0.10 / 0.22 (55) | 16.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Finn Reynolds / James Watt (`KXATPCHALLENGERDOUBLES-26NOV11REYWATIMANOG-REYWAT`) | 0.78 / 0.93 (92) | 85.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jayson Blando vs Dev Javia -- M15 Kuala Lumpur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11BLAJAV:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jayson Blando (`KXITFMATCH-26NOV11BLAJAV-BLA`) | 0.06 / 0.09 (128) | 7.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dev Javia (`KXITFMATCH-26NOV11BLAJAV-JAV`) | 0.90 / 0.92 (50) | 91.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jordan Chiu vs Tianhui Zhang -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207780:212221:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jordan Chiu (`KXITFMATCH-26NOV11CHIZHA-CHI`) | 0.22 / 0.23 (82) | 22.5% | -- | 42.3% | 17.8% [15.6%-21.4%] | 24.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tianhui Zhang (`KXITFMATCH-26NOV11CHIZHA-ZHA`) | 0.77 / 0.78 (133) | 77.5% | -- | 57.7% | 82.2% [78.6%-84.4%] | 75.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 402.0, B 1273.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0288
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.003, surface_dev_loose +0.003, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## James Connel vs Seongchan Hong -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11CONHON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| James Connel (`KXITFMATCH-26NOV11CONHON-CON`) | 0.19 / 0.20 (347) | 19.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Seongchan Hong (`KXITFMATCH-26NOV11CONHON-HON`) | 0.81 / 0.84 (49) | 82.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xirui Han vs Yue Xia -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212472:213883:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xirui Han (`KXITFMATCH-26NOV11HANXIA-HAN`) | 0.52 / 0.54 (306) | 53.0% | -- | 67.3% | 45.8% [42.8%-50.5%] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yue Xia (`KXITFMATCH-26NOV11HANXIA-XIA`) | 0.46 / 0.47 (127) | 46.5% | -- | 32.7% | 54.2% [49.5%-57.2%] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.7 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 542.0, B 202.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0388
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.010, surface_dev_loose +0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cooper Kose vs Yuto Oki -- M15 Kuala Lumpur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212639:213566:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cooper Kose (`KXITFMATCH-26NOV11KOSOKI-KOS`) | 0.10 / 0.11 (343) | 10.5% | -- | 22.3% | 33.5% [31.6%-34.9%] | 12.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +23.0 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuto Oki (`KXITFMATCH-26NOV11KOSOKI-OKI`) | 0.88 / 0.91 (166) | 89.5% | -- | 77.7% | 66.5% [65.1%-68.4%] | 87.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -23.0 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 204.0, B 1766.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0164
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV11KOSOKI-KOS  (YES = Cooper Kose)
Model: 33%
Kalshi: 10%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.014, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sasikumar Mukund vs Hao Sheng Koay -- M15 Kuala Lumpur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11MUKKOA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hao Sheng Koay (`KXITFMATCH-26NOV11MUKKOA-KOA`) | 0.19 / 0.22 (347) | 20.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sasikumar Mukund (`KXITFMATCH-26NOV11MUKKOA-MUK`) | 0.76 / 0.78 (6) | 77.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniil Sarksian vs Madhwin Kamath -- M15 Kuala Lumpur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209979:212022:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Madhwin Kamath (`KXITFMATCH-26NOV11SARKAM-KAM`) | 0.36 / 0.38 (49) | 37.0% | -- | 31.4% | 39.1% [36.6%-42.7%] | 40.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.1 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daniil Sarksian (`KXITFMATCH-26NOV11SARKAM-SAR`) | 0.59 / 0.63 (449) | 61.0% | -- | 68.6% | 60.9% [57.3%-63.3%] | 59.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.1 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2188.0, B 843.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0304
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.025, surface_dev_loose +0.015, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gunawan Trismuwantara vs Edoardo Cherie Ligniere -- M15 Kuala Lumpur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211326:212122:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Edoardo Cherie Ligniere (`KXITFMATCH-26NOV11TRICHE-CHE`) | 0.77 / 0.80 (683) | 78.5% | -- | 52.6% | 64.8% [62.9%-66.2%] | 76.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.7 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gunawan Trismuwantara (`KXITFMATCH-26NOV11TRICHE-TRI`) | 0.19 / 0.22 (122) | 20.5% | -- | 47.4% | 35.1% [33.8%-37.1%] | 23.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +14.7 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 301.0, B 266.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0164
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Azuma Visaya vs Yua Taka -- M15 Kuala Lumpur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210405:212196:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yua Taka (`KXITFMATCH-26NOV11VISTAK-TAK`) | 0.49 / 0.50 (20) | 49.5% | -- | 19.9% | 42.7% [37.0%-46.9%] | 52.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Azuma Visaya (`KXITFMATCH-26NOV11VISTAK-VIS`) | 0.49 / 0.50 (326) | 49.5% | -- | 80.1% | 57.3% [53.1%-63.0%] | 47.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 253.0, B 485.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0494
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.011, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xiaoyin Yang vs Noritaka Koizumi -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212466:212476:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Noritaka Koizumi (`KXITFMATCH-26NOV11YANKOI-KOI`) | 0.69 / 0.71 (250) | 70.0% | -- | 65.5% | 65.5% [64.9%-66.4%] | 69.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Xiaoyin Yang (`KXITFMATCH-26NOV11YANKOI-YAN`) | 0.28 / 0.29 (181) | 28.5% | -- | 34.5% | 34.5% [33.6%-35.1%] | 30.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 817.0, B 190.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0078
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.009, surface_dev_loose +0.002, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xi Luo vs Maria Pankratova -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11LUOPAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xi Luo (`KXITFWMATCH-26NOV11LUOPAN-LUO`) | 0.53 / 0.57 (9) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maria Pankratova (`KXITFWMATCH-26NOV11LUOPAN-PAN`) | 0.43 / 0.45 (50) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Thasaporn Naklo vs Yingqun Sun -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220597:264029:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thasaporn Naklo (`KXITFWMATCH-26NOV11NAKSUN-NAK`) | 0.64 / 0.67 (582) | 65.5% | -- | 58.9% | 58.9% [58.4%-60.0%] | 64.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.6 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yingqun Sun (`KXITFWMATCH-26NOV11NAKSUN-SUN`) | 0.33 / 0.34 (61) | 33.5% | -- | 41.1% | 41.1% [40.0%-41.6%] | 35.6% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +7.6 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2173.0, B 1826.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0078
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.000, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kyoka Okamura vs Yuhan Wang -- W50 Yokohama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211846:264205:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kyoka Okamura (`KXITFWMATCH-26NOV11OKAWAN-OKA`) | 0.57 / 0.59 (241) | 58.0% | -- | 54.2% | 66.0% [61.5%-74.7%] | -- | -- | -- | -- | PASS | +8.0 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuhan Wang (`KXITFWMATCH-26NOV11OKAWAN-WAN`) | 0.40 / 0.42 (4) | 41.0% | -- | 45.8% | 34.0% [25.3%-38.5%] | -- | -- | -- | -- | PASS | -7.0 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2971.0, B 1724.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0661
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rina Saigo vs Chia Yi Tsao -- W50 Yokohama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221099:259623:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rina Saigo (`KXITFWMATCH-26NOV11SAITSA-SAI`) | 0.67 / 0.71 (21) | 69.0% | -- | 48.9% | 55.8% [51.6%-62.5%] | -- | -- | -- | -- | PASS | -13.2 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Chia Yi Tsao (`KXITFWMATCH-26NOV11SAITSA-TSA`) | 0.30 / 0.32 (452) | 31.0% | -- | 51.1% | 44.2% [37.5%-48.4%] | -- | -- | -- | -- | PASS | +13.2 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3065.0, B 824.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0548
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.026, surface_pool_high -0.026, surface_dev_loose -0.011, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kanon Sawashiro vs Caroline Werner -- W50 Yokohama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:263905:espn:espn:4384:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanon Sawashiro (`KXITFWMATCH-26NOV11SAWWER-SAW`) | 0.28 / 0.30 (32) | 29.0% | -- | 52.1% | 18.1% [18.1%-18.1%] | -- | -- | -- | -- | PASS | -10.9 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Caroline Werner (`KXITFWMATCH-26NOV11SAWWER-WER`) | 0.69 / 0.72 (53) | 70.5% | -- | 47.9% | 81.9% [81.9%-81.9%] | -- | -- | -- | -- | PASS | +11.4 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 827.0, B 0.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0003
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Heather Watson vs Hanna Chang -- W50 Yokohama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:201586:213949:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hanna Chang (`KXITFWMATCH-26NOV11WATCHA-CHA`) | 0.36 / 0.37 (139) | 36.5% | -- | 67.4% | 53.2% [35.5%-60.4%] | -- | -- | -- | -- | PASS | +16.7 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Heather Watson (`KXITFWMATCH-26NOV11WATCHA-WAT`) | 0.61 / 0.64 (373) | 62.5% | -- | 32.6% | 46.8% [39.6%-64.5%] | -- | -- | -- | -- | PASS | -15.7 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2194.0, B 3084.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.1247
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV11WATCHA-CHA  (YES = Hanna Chang)
Model: 53%
Kalshi: 36%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.026, surface_dev_loose -0.016, surface_dev_tight +0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Broadus / Ivanov vs Gadecki / Wen Wan -- W75 Brisbane QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 08:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11BROIVAGADWEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Broadus / Ivanov (`KXITFWDOUBLES-26NOV11BROIVAGADWEN-BROIVA`) | 0.08 / 0.84 (56) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gadecki / Wen Wan (`KXITFWDOUBLES-26NOV11BROIVAGADWEN-GADWEN`) | 0.10 / 0.84 (56) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Huang / Zhang vs Beck / Sibai -- W75 Brisbane QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 08:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11HUAZHABECSIB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Beck / Sibai (`KXITFWDOUBLES-26NOV11HUAZHABECSIB-BECSIB`) | 0.10 / 0.55 (56) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Huang / Zhang (`KXITFWDOUBLES-26NOV11HUAZHABECSIB-HUAZHA`) | 0.82 / 0.85 (2) | 83.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jeong / Young Suh Lee vs Barry / Kawaguchi -- W75 Brisbane QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 08:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11JEOYOUBARKAW:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barry / Kawaguchi (`KXITFWDOUBLES-26NOV11JEOYOUBARKAW-BARKAW`) | 0.51 / 0.85 (2) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jeong / Young Suh Lee (`KXITFWDOUBLES-26NOV11JEOYOUBARKAW-JEOYOU`) | 0.35 / 0.83 (1) | 59.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Thanapet Chanta vs Hong-Lin Fu -- M15 Hua Hin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207748:207788:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thanapet Chanta (`KXITFMATCH-26NOV11CHAFUX-CHA`) | 0.93 / 0.95 (181) | 94.0% | -- | 85.4% | 82.5% [81.2%-84.5%] | 92.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.4 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hong-Lin Fu (`KXITFMATCH-26NOV11CHAFUX-FUX`) | 0.05 / 0.06 (187) | 5.5% | -- | 14.6% | 17.4% [15.5%-18.8%] | 7.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +11.9 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2163.0, B 214.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0165
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high -0.000, surface_dev_loose +0.007, surface_dev_tight -0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tin Chen vs Ammar Faleh Alhogbani -- M15 Kuala Lumpur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144844:212249:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ammar Faleh Alhogbani (`KXITFMATCH-26NOV11CHEALH-ALH`) | 0.47 / 0.49 (356) | 48.0% | -- | 24.2% | 45.9% [45.9%-46.9%] | -- | -- | -- | -- | PASS | -2.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Tin Chen (`KXITFMATCH-26NOV11CHEALH-CHE`) | 0.50 / 0.53 (5) | 51.5% | -- | 75.8% | 54.1% [53.1%-54.1%] | -- | -- | -- | -- | PASS | +2.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 1359.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0052
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kuan-Shou Chen vs Penn Charusorn -- M15 Hua Hin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213769:214094:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Penn Charusorn (`KXITFMATCH-26NOV11CHECHA-CHA`) | 0.06 / 0.11 (22) | 8.5% | -- | 55.7% | 54.2% [53.1%-54.7%] | -- | -- | -- | -- | PASS | +45.7 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kuan-Shou Chen (`KXITFMATCH-26NOV11CHECHA-CHE`) | 0.89 / 0.93 (250) | 91.0% | -- | 44.3% | 45.8% [45.3%-46.9%] | -- | -- | -- | -- | PASS | -45.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 224.0, B 193.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0081
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV11CHECHA-CHA  (YES = Penn Charusorn)
Model: 54%
Kalshi: 8%
Gap: +46 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## M Rifqi Fitriadi vs Samarth Sahita -- M15 Kuala Lumpur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11FITSAH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M Rifqi Fitriadi (`KXITFMATCH-26NOV11FITSAH-FIT`) | 0.90 / 0.93 (250) | 91.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Samarth Sahita (`KXITFMATCH-26NOV11FITSAH-SAH`) | 0.06 / 0.10 (300) | 8.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Fons Van Sambeek vs Leo Vithoontien -- M15 Hua Hin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209913:210672:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fons Van Sambeek (`KXITFMATCH-26NOV11VANVIT-VAN`) | 0.57 / 0.61 (62) | 59.0% | -- | 41.9% | 37.9% [32.7%-39.9%] | -- | -- | -- | -- | PASS | -21.1 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Leo Vithoontien (`KXITFMATCH-26NOV11VANVIT-VIT`) | 0.37 / 0.43 (14) | 40.0% | -- | 58.1% | 62.1% [60.1%-67.3%] | -- | -- | -- | -- | PASS | +22.1 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1119.0, B 2997.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0361
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV11VANVIT-VIT  (YES = Leo Vithoontien)
Model: 62%
Kalshi: 40%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.024, surface_pool_high +0.020, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Denis Yevseyev vs Markus Malaszszak -- M15 Hua Hin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106187:212308:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Markus Malaszszak (`KXITFMATCH-26NOV11YEVMAL-MAL`) | 0.22 / 0.25 (139) | 23.5% | -- | 30.3% | 22.6% [18.2%-25.1%] | 26.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Denis Yevseyev (`KXITFMATCH-26NOV11YEVMAL-YEV`) | 0.74 / 0.76 (7) | 75.0% | -- | 69.7% | 77.4% [74.9%-81.8%] | 73.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.4 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5377.0, B 1157.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0341
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.012, surface_pool_high -0.016, surface_dev_loose +0.004, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oscar Brown vs James Van Herzeele -- M15 Hua Hin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211329:214341:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oscar Brown (`KXITFMATCH-26NOV11BROVAN-BRO`) | 0.73 / 0.77 (53) | 75.0% | -- | 42.3% | 59.2% [55.6%-62.2%] | -- | -- | -- | -- | PASS | -15.8 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| James Van Herzeele (`KXITFMATCH-26NOV11BROVAN-VAN`) | 0.22 / 0.25 (27) | 23.5% | -- | 57.7% | 40.8% [37.8%-44.4%] | -- | -- | -- | -- | PASS | +17.3 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 423.0, B 879.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0327
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV11BROVAN-VAN  (YES = James Van Herzeele)
Model: 41%
Kalshi: 24%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Julien De Cuyper vs Ergi Kirkin -- M15 Hua Hin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144985:207761:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julien De Cuyper (`KXITFMATCH-26NOV11DECKIR-DEC`) | 0.06 / 0.08 (9) | 7.0% | -- | 13.7% | 13.4% [9.7%-17.7%] | -- | -- | -- | -- | PASS | +6.4 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ergi Kirkin (`KXITFMATCH-26NOV11DECKIR-KIR`) | 0.87 / 0.94 (59) | 90.5% | -- | 86.4% | 86.6% [82.3%-90.3%] | -- | -- | -- | -- | PASS | -3.9 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 549.0, B 3401.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.04
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.033, surface_pool_high +0.043, surface_dev_loose -0.005, surface_dev_tight +0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jordan Hasson vs Sanhui Shin -- M15 Hua Hin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11HASSHI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jordan Hasson (`KXITFMATCH-26NOV11HASSHI-HAS`) | 0.23 / 0.27 (13) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sanhui Shin (`KXITFMATCH-26NOV11HASSHI-SHI`) | 0.67 / 0.74 (52) | 70.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nazar Oliynykov vs Tsz Fu Wong -- M15 Hua Hin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212138:212971:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nazar Oliynykov (`KXITFMATCH-26NOV11OLIWON-OLI`) | 0.50 / 0.51 (51) | 50.5% | -- | 65.2% | 57.2% [56.2%-58.3%] | -- | -- | -- | -- | PASS | +6.7 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tsz Fu Wong (`KXITFMATCH-26NOV11OLIWON-WON`) | 0.46 / 0.50 (276) | 48.0% | -- | 34.8% | 42.8% [41.7%-43.8%] | -- | -- | -- | -- | PASS | -5.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 203.0, B 498.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0104
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sheng Tang vs Shaoyun Liu -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207463:212180:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shaoyun Liu (`KXITFMATCH-26NOV11TANLIU-LIU`) | 0.36 / 0.38 (0) | 37.0% | -- | 42.4% | 44.4% [42.9%-45.4%] | 38.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.4 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sheng Tang (`KXITFMATCH-26NOV11TANLIU-TAN`) | 0.62 / 0.63 (51) | 62.5% | -- | 57.6% | 55.6% [54.6%-57.1%] | 61.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.9 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 714.0, B 496.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0123
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rigele Te vs Linang Xiao -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144751:209038:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rigele Te (`KXITFMATCH-26NOV11TEXXIA-TEX`) | 0.71 / 0.75 (94) | 73.0% | -- | 30.7% | 46.0% [38.6%-55.5%] | 73.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -27.0 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Linang Xiao (`KXITFMATCH-26NOV11TEXXIA-XIA`) | 0.22 / 0.26 (12) | 24.0% | -- | 69.3% | 54.0% [44.5%-61.4%] | 26.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +30.0 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1492.0, B 1754.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0846
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV11TEXXIA-XIA  (YES = Linang Xiao)
Model: 54%
Kalshi: 24%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.005, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zhao Zhao vs Dingzheng Nima -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206888:212909:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dingzheng Nima (`KXITFMATCH-26NOV11ZHANIM-NIM`) | 0.05 / 0.09 (4) | 7.0% | -- | 46.9% | 53.1% [52.6%-54.1%] | 7.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +46.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zhao Zhao (`KXITFMATCH-26NOV11ZHANIM-ZHA`) | 0.92 / 0.94 (68) | 93.0% | -- | 53.1% | 46.9% [45.9%-47.4%] | 92.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -46.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 155.0, B 174.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0077
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV11ZHANIM-NIM  (YES = Dingzheng Nima)
Model: 53%
Kalshi: 7%
Gap: +46 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kobori / Shimizu vs Kim / Morisaki -- W50 Yokohama QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11KOBSHIKIMMOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kim / Morisaki (`KXITFWDOUBLES-26NOV11KOBSHIKIMMOR-KIMMOR`) | 0.06 / 0.82 (100) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kobori / Shimizu (`KXITFWDOUBLES-26NOV11KOBSHIKIMMOR-KOBSHI`) | 0.06 / 0.85 (2) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kuwata / Shimizu vs Ishijima / Okawa -- W50 Yokohama QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11KUWSHIISHOKA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ishijima / Okawa (`KXITFWDOUBLES-26NOV11KUWSHIISHOKA-ISHOKA`) | 0.11 / 0.84 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kuwata / Shimizu (`KXITFWDOUBLES-26NOV11KUWSHIISHOKA-KUWSHI`) | 0.11 / 0.84 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Matsuda / Nakashima vs Li / Saito -- W50 Yokohama QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11MATNAKLIXSAI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Li / Saito (`KXITFWDOUBLES-26NOV11MATNAKLIXSAI-LIXSAI`) | 0.11 / 0.84 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matsuda / Nakashima (`KXITFWDOUBLES-26NOV11MATNAKLIXSAI-MATNAK`) | 0.11 / 0.84 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sato / Tse vs Stevens / Thompson -- W75 Brisbane QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11SATTSESTETHO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sato / Tse (`KXITFWDOUBLES-26NOV11SATTSESTETHO-SATTSE`) | 0.10 / 0.84 (56) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stevens / Thompson (`KXITFWDOUBLES-26NOV11SATTSESTETHO-STETHO`) | 0.11 / 0.84 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jiaqi Wang vs Anna Yang -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221181:264242:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jiaqi Wang (`KXITFWMATCH-26NOV11WANYAN-WAN`) | 0.85 / 0.86 (17) | 85.5% | -- | 83.7% | 81.0% [80.3%-81.0%] | 80.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anna Yang (`KXITFWMATCH-26NOV11WANYAN-YAN`) | 0.14 / 0.15 (125) | 14.5% | -- | 16.3% | 19.0% [19.0%-19.7%] | 19.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2849.0, B 270.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0036
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.007, surface_dev_loose -0.000, surface_dev_tight -0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ru Xi Wu vs Valeria Savinykh -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:202443:270262:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valeria Savinykh (`KXITFWMATCH-26NOV11WUXSAV-SAV`) | 0.79 / 0.82 (349) | 80.5% | -- | 58.0% | 74.0% [72.6%-74.8%] | 81.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ru Xi Wu (`KXITFWMATCH-26NOV11WUXSAV-WUX`) | 0.17 / 0.19 (75) | 18.0% | -- | 42.0% | 26.0% [25.2%-27.4%] | 18.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +8.0 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 171.0, B 1181.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0109
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ziyu Zhou vs Alina Tikhonova -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV11ZHOTIK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alina Tikhonova (`KXITFWMATCH-26NOV11ZHOTIK-TIK`) | 0.90 / 0.95 (46) | 92.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ziyu Zhou (`KXITFWMATCH-26NOV11ZHOTIK-ZHO`) | 0.04 / 0.13 (31) | 8.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lorenzo Carboni vs Ioannis Xilas -- ATP Challenger Hersonissos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-12T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12CARXIL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Carboni (`KXATPCHALLENGERMATCH-26NOV12CARXIL-CAR`) | 0.42 / 0.43 (1962) | 42.5% | -- | -- | -- [-----] | -- | 42.4% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ioannis Xilas (`KXATPCHALLENGERMATCH-26NOV12CARXIL-XIL`) | 0.57 / 0.58 (1997) | 57.5% | -- | -- | -- [-----] | -- | 57.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Victor Vlad Cornea / Kai Wehnelt vs Alex Ganchev / Sacha Maes -- ATP Challenger Hersonissos QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-12T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12CORWEHGANMAE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Victor Vlad Cornea / Kai Wehnelt (`KXATPCHALLENGERDOUBLES-26NOV12CORWEHGANMAE-CORWEH`) | 0.48 / 0.95 (338) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alex Ganchev / Sacha Maes (`KXATPCHALLENGERDOUBLES-26NOV12CORWEHGANMAE-GANMAE`) | 0.06 / 0.58 (56) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Kamath / Suresh vs Eichenseher / Mueller -- M15 Kuala Lumpur QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12KAMSUREICMUE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eichenseher / Mueller (`KXITFDOUBLES-26NOV12KAMSUREICMUE-EICMUE`) | 0.81 / 0.90 (2) | 85.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kamath / Suresh (`KXITFDOUBLES-26NOV12KAMSUREICMUE-KAMSUR`) | 0.06 / 0.50 (3) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Oki / Taka vs Quoc Cuong / Phat Nguyen -- M15 Kuala Lumpur QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12OKITAKQUOPHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oki / Taka (`KXITFDOUBLES-26NOV12OKITAKQUOPHA-OKITAK`) | 0.27 / 0.90 (2) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Quoc Cuong / Phat Nguyen (`KXITFDOUBLES-26NOV12OKITAKQUOPHA-QUOPHA`) | 0.06 / 0.64 (1) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Michele Ribecai vs Carlo Alberto Caniato -- ATP Challenger Hersonissos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-12T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12RIBCAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlo Alberto Caniato (`KXATPCHALLENGERMATCH-26NOV12RIBCAN-CAN`) | 0.57 / 0.58 (31) | 57.5% | -- | -- | -- [-----] | -- | 58.8% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Michele Ribecai (`KXATPCHALLENGERMATCH-26NOV12RIBCAN-RIB`) | 0.42 / 0.43 (1962) | 42.5% | -- | -- | -- [-----] | -- | 48.0% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Hosoki / Katsumi vs Sawashiro / Uemura -- W50 Yokohama QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12HOSKATSAWUEM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hosoki / Katsumi (`KXITFWDOUBLES-26NOV12HOSKATSAWUEM-HOSKAT`) | 0.44 / 0.68 (1) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sawashiro / Uemura (`KXITFWDOUBLES-26NOV12HOSKATSAWUEM-SAWUEM`) | 0.39 / 0.76 (3) | 57.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Koaykul / Navasirisomboon vs Arcon / Lakshmanan -- M15 Hua Hin QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12KOANAVARCLAK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arcon / Lakshmanan (`KXITFDOUBLES-26NOV12KOANAVARCLAK-ARCLAK`) | 0.53 / 0.73 (1) | 63.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Koaykul / Navasirisomboon (`KXITFDOUBLES-26NOV12KOANAVARCLAK-KOANAV`) | 0.33 / 0.78 (3) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lorenzo Lorusso vs Dong Ju Kim -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207456:210047:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dong Ju Kim (`KXITFMATCH-26NOV12LORKIM-KIM`) | 0.71 / 0.76 (289) | 73.5% | -- | 74.6% | 66.2% [61.1%-69.0%] | -- | -- | -- | -- | PASS | -7.2 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lorenzo Lorusso (`KXITFMATCH-26NOV12LORKIM-LOR`) | 0.24 / 0.26 (59) | 25.0% | -- | 25.4% | 33.8% [31.0%-38.9%] | -- | -- | -- | -- | PASS | +8.8 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1815.0, B 1454.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0396
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.018, surface_pool_high +0.028, surface_dev_loose -0.009, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xinle Geng vs Ikumi Yamazaki -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221265:270132:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xinle Geng (`KXITFWMATCH-26NOV12GENYAM-GEN`) | 0.41 / 0.44 (33) | 42.5% | -- | 38.6% | 38.6% [31.6%-44.7%] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ikumi Yamazaki (`KXITFWMATCH-26NOV12GENYAM-YAM`) | 0.56 / 0.57 (2) | 56.5% | -- | 61.4% | 61.5% [55.3%-68.5%] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 429.0, B 1933.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0659
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.054, surface_pool_high +0.062, surface_dev_loose -0.009, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hou / Plipuech vs Sun / Zhao -- W15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12HOUPLISUNZHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hou / Plipuech (`KXITFWDOUBLES-26NOV12HOUPLISUNZHA-HOUPLI`) | 0.10 / 0.84 (2) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sun / Zhao (`KXITFWDOUBLES-26NOV12HOUPLISUNZHA-SUNZHA`) | 0.10 / 0.84 (2) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jiayu Xu vs Arina Varaksina -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-12T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222606:255662:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arina Varaksina (`KXITFWMATCH-26NOV12XUXVAR-VAR`) | 0.58 / 0.59 (0) | 58.5% | -- | 58.0% | 47.3% [42.6%-50.5%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.2 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jiayu Xu (`KXITFWMATCH-26NOV12XUXVAR-XUX`) | 0.42 / 0.43 (57) | 42.5% | -- | 42.0% | 52.7% [49.5%-57.4%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +10.2 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 444.0, B 586.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0398
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nikola Mektic / Edouard Roger-Vasselin vs Jean-Julien Rojer / Theodore Winegar -- ATP Stockholm QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-12 15:00Z
* Current expected start: 2026-11-12 12:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-11 21:14Z
* Recommended handicap-by time: 2026-11-12 11:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12MEKROGROJWIN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikola Mektic / Edouard Roger-Vasselin (`KXATPDOUBLES-26NOV12MEKROGROJWIN-MEKROG`) | 0.30 / 0.92 (26) | 61.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jean-Julien Rojer / Theodore Winegar (`KXATPDOUBLES-26NOV12MEKROGROJWIN-ROJWIN`) | 0.06 / 0.74 (6) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alex Michelsen vs Alejandro Tabilo -- ATP Stockholm QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-12 15:00Z
* Current expected start: 2026-11-12 12:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-11 21:14Z
* Recommended handicap-by time: 2026-11-12 11:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-11-12T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126214:210506:2026-11-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex Michelsen (`KXATPMATCH-26NOV12MICTAB-MIC`) | 0.76 / 0.77 (19981) | 76.5% | -- | 67.0% | 67.5% [63.9%-69.7%] | 75.5% | 75.5% | 75.5% | MODEL_LONE_OUTLIER | PASS | -9.0 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Alejandro Tabilo (`KXATPMATCH-26NOV12MICTAB-TAB`) | 0.23 / 0.24 (10) | 23.5% | -- | 33.0% | 32.5% [30.3%-36.1%] | 24.5% | 24.4% | 24.4% | MODEL_LONE_OUTLIER | PASS | +9.0 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5933.0, B 5932.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0288
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.022, surface_pool_high +0.022, surface_dev_loose +0.013, surface_dev_tight -0.013
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 4 carry a model probability
  * `KXATPEXACTMATCH-26NOV12MICTAB-MIC21` Will Alex Michelsen win the Alex Michelsen vs Alejandro Tabilo match by a set score of 2-1?: 0.15/0.29 mid 22.0%, model 29.3% (market_conditioned_v1 (model4_board_v1)) -- gap +7.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV12MICTAB-TAB21` Will Alejandro Tabilo win the Alex Michelsen vs Alejandro Tabilo match by a set score of 2-1?: 0.02/0.23 mid 12.5%, model 17.4% (market_conditioned_v1 (model4_board_v1)) -- gap +4.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV12MICTAB-TAB20` Will Alejandro Tabilo win the Alex Michelsen vs Alejandro Tabilo match by a set score of 2-0?: 0.13/0.23 mid 18.0%, model 13.8% (market_conditioned_v1 (model4_board_v1)) -- gap -4.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV12MICTAB-MIC20` Will Alex Michelsen win the Alex Michelsen vs Alejandro Tabilo match by a set score of 2-0?: 0.28/0.59 mid 43.5%, model 39.5% (market_conditioned_v1 (model4_board_v1)) -- gap -4.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Qariaqus / Talic vs Faleh Alhogbani / Cherie Ligniere -- M15 Kuala Lumpur QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12QARTALFALCHE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Faleh Alhogbani / Cherie Ligniere (`KXITFDOUBLES-26NOV12QARTALFALCHE-FALCHE`) | 0.62 / 0.86 (4) | 74.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Qariaqus / Talic (`KXITFDOUBLES-26NOV12QARTALFALCHE-QARTAL`) | 0.26 / 0.67 (3) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Rifqi Fitriadi / Sarksian vs Alam / Sheng Koay -- M15 Kuala Lumpur QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12RIFSARALASHE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alam / Sheng Koay (`KXITFDOUBLES-26NOV12RIFSARALASHE-ALASHE`) | 0.05 / 0.89 (2) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rifqi Fitriadi / Sarksian (`KXITFDOUBLES-26NOV12RIFSARALASHE-RIFSAR`) | 0.09 / 0.89 (1) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Adrian Andreev vs Raul Brancaccio -- ATP Challenger Hersonissos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 12:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-12T12:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12ANDBRA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Andreev (`KXATPCHALLENGERMATCH-26NOV12ANDBRA-AND`) | 0.44 / 0.49 (42) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Raul Brancaccio (`KXATPCHALLENGERMATCH-26NOV12ANDBRA-BRA`) | 0.51 / 0.54 (48) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Vasilios Caripi / Benjamin Pietri vs Menelaos Efstathiou / Eleftherios Neos -- ATP Challenger Hersonissos QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 12:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-12T12:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12CARPIEEFSNEO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vasilios Caripi / Benjamin Pietri (`KXATPCHALLENGERDOUBLES-26NOV12CARPIEEFSNEO-CARPIE`) | 0.20 / 0.38 (6) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Menelaos Efstathiou / Eleftherios Neos (`KXATPCHALLENGERDOUBLES-26NOV12CARPIEEFSNEO-EFSNEO`) | 0.67 / 0.86 (4) | 76.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Cezar Cretu (b. 2001) vs Philip Henning -- ATP Challenger Hersonissos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 12:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-12T12:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12CREHEN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cezar Cretu (b. 2001) (`KXATPCHALLENGERMATCH-26NOV12CREHEN-CRE`) | 0.34 / 0.36 (1992) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Philip Henning (`KXATPCHALLENGERMATCH-26NOV12CREHEN-HEN`) | 0.64 / 0.66 (1952) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Tobia Costanzo Baragiola Mordini vs Dmitry Popko -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12BARPOP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tobia Costanzo Baragiola Mordini (`KXITFMATCH-26NOV12BARPOP-BAR`) | 0.10 / 0.58 (3) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dmitry Popko (`KXITFMATCH-26NOV12BARPOP-POP`) | 0.77 / 0.86 (1) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bunyarit / Kamput vs Chanta / Sornlaksup -- M15 Hua Hin QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12BUNKAMCHASOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bunyarit / Kamput (`KXITFDOUBLES-26NOV12BUNKAMCHASOR-BUNKAM`) | 0.14 / 0.90 (2) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Chanta / Sornlaksup (`KXITFDOUBLES-26NOV12BUNKAMCHASOR-CHASOR`) | 0.04 / 0.78 (1) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Huang / Lu vs Charusorn / Chen -- M15 Hua Hin QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12HUALUXCHACHE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charusorn / Chen (`KXITFDOUBLES-26NOV12HUALUXCHACHE-CHACHE`) | 0.06 / 0.89 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Huang / Lu (`KXITFDOUBLES-26NOV12HUALUXCHACHE-HUALUX`) | 0.08 / 0.89 (1) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Vuk Radjenovic vs Jannik Maute -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12RADMAU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jannik Maute (`KXITFMATCH-26NOV12RADMAU-MAU`) | 0.48 / 0.70 (1) | 59.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vuk Radjenovic (`KXITFMATCH-26NOV12RADMAU-RAD`) | 0.33 / 0.55 (4) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Heorhii Shylov vs Stefan Adrian Andreescu -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12SHYAND:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefan Adrian Andreescu (`KXITFMATCH-26NOV12SHYAND-AND`) | 0.63 / 0.68 (1) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Heorhii Shylov (`KXITFMATCH-26NOV12SHYAND-SHY`) | 0.31 / 0.40 (5) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Thada Grohbruegge / Sootinun-Opart vs Sumizawa / Vithoontien -- M15 Hua Hin QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12THASOOSUMVIT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sumizawa / Vithoontien (`KXITFDOUBLES-26NOV12THASOOSUMVIT-SUMVIT`) | 0.78 / 0.89 (8) | 83.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Thada Grohbruegge / Sootinun-Opart (`KXITFDOUBLES-26NOV12THASOOSUMVIT-THASOO`) | 0.09 / 0.36 (1) | 22.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Martin Van Der Meerschen vs Evgenii Tiurnev -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12VANTIU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Evgenii Tiurnev (`KXITFMATCH-26NOV12VANTIU-TIU`) | 0.31 / 0.65 (3) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Martin Van Der Meerschen (`KXITFMATCH-26NOV12VANTIU-VAN`) | 0.55 / 0.72 (3) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alan Wazny vs Matyas Cerny -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12WAZCER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matyas Cerny (`KXITFMATCH-26NOV12WAZCER-CER`) | 0.50 / 0.58 (52) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alan Wazny (`KXITFMATCH-26NOV12WAZCER-WAZ`) | 0.41 / 0.47 (47) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ali Yazdani vs Jonas Gundacker -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12YAZGUN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jonas Gundacker (`KXITFMATCH-26NOV12YAZGUN-GUN`) | 0.44 / 0.45 (45) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ali Yazdani (`KXITFMATCH-26NOV12YAZGUN-YAZ`) | 0.50 / 0.59 (3) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stefanie Auer vs Andreea Prisacariu -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12AUEPRI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefanie Auer (`KXITFWMATCH-26NOV12AUEPRI-AUE`) | 0.04 / 0.07 (21) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Andreea Prisacariu (`KXITFWMATCH-26NOV12AUEPRI-PRI`) | 0.90 / 0.94 (6) | 92.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Federica Trevisan vs Asylzhan Arystanbekova -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12TREARY:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Asylzhan Arystanbekova (`KXITFWMATCH-26NOV12TREARY-ARY`) | 0.50 / 0.57 (12) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Federica Trevisan (`KXITFWMATCH-26NOV12TREARY-TRE`) | 0.48 / 0.49 (37) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dong / Yang vs Jin / Sun -- M15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12DONYANJINSUN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dong / Yang (`KXITFDOUBLES-26NOV12DONYANJINSUN-DONYAN`) | 0.05 / 0.89 (56) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jin / Sun (`KXITFDOUBLES-26NOV12DONYANJINSUN-JINSUN`) | 0.07 / 0.89 (56) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Cai / Yang vs Im / Shin -- W15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12CAIYANIMXSHI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cai / Yang (`KXITFWDOUBLES-26NOV12CAIYANIMXSHI-CAIYAN`) | 0.10 / 0.84 (1) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Im / Shin (`KXITFWDOUBLES-26NOV12CAIYANIMXSHI-IMXSHI`) | 0.10 / 0.84 (1) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Wang / Yuchi vs Guo / An Lin -- W15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12WANYUCGUOANL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Guo / An Lin (`KXITFWDOUBLES-26NOV12WANYUCGUOANL-GUOANL`) | 0.16 / 0.84 (1) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Wang / Yuchi (`KXITFWDOUBLES-26NOV12WANYUCGUOANL-WANYUC`) | 0.09 / 0.79 (1) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Yi Liu / Lu vs Cao / Tikhonova -- W15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12YILLUXCAOTIK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cao / Tikhonova (`KXITFWDOUBLES-26NOV12YILLUXCAOTIK-CAOTIK`) | 0.10 / 0.84 (1) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yi Liu / Lu (`KXITFWDOUBLES-26NOV12YILLUXCAOTIK-YILLUX`) | 0.10 / 0.84 (1) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Conor Gannon vs Miles Jones -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12GANJON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Conor Gannon (`KXITFMATCH-26NOV12GANJON-GAN`) | 0.27 / 0.31 (29) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Miles Jones (`KXITFMATCH-26NOV12GANJON-JON`) | 0.67 / 0.72 (333) | 69.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mattia Nannelli vs Dragos Nicolae Madaras -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12NANMAD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dragos Nicolae Madaras (`KXITFMATCH-26NOV12NANMAD-MAD`) | 0.74 / 0.85 (1) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mattia Nannelli (`KXITFMATCH-26NOV12NANMAD-NAN`) | 0.13 / 0.63 (4) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andrea Paolini vs Antoni Fabre -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12PAOFAB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Antoni Fabre (`KXITFMATCH-26NOV12PAOFAB-FAB`) | 0.45 / 0.49 (49) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Andrea Paolini (`KXITFMATCH-26NOV12PAOFAB-PAO`) | 0.51 / 0.59 (1) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dominique Rolland vs Flynn Thomas -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12ROLTHO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dominique Rolland (`KXITFMATCH-26NOV12ROLTHO-ROL`) | 0.35 / 0.39 (17) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Flynn Thomas (`KXITFMATCH-26NOV12ROLTHO-THO`) | 0.58 / 0.63 (54) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Josip Simundza vs Dan Brand -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12SIMBRA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dan Brand (`KXITFMATCH-26NOV12SIMBRA-BRA`) | 0.42 / 0.43 (5) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Josip Simundza (`KXITFMATCH-26NOV12SIMBRA-SIM`) | 0.53 / 0.58 (145) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arthur Weber vs Mickael Kaouk -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12WEBKAO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mickael Kaouk (`KXITFMATCH-26NOV12WEBKAO-KAO`) | 0.36 / 0.38 (94) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arthur Weber (`KXITFMATCH-26NOV12WEBKAO-WEB`) | 0.61 / 0.64 (197) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marianna Argyrokastriti vs Anastasija Cvetkovic -- W35 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12ARGCVE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marianna Argyrokastriti (`KXITFWMATCH-26NOV12ARGCVE-ARG`) | 0.31 / 0.34 (44) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anastasija Cvetkovic (`KXITFWMATCH-26NOV12ARGCVE-CVE`) | 0.62 / 0.70 (5) | 66.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sara Victoria Balan vs Valeriia Iushchenko -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12BALIUS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Victoria Balan (`KXITFWMATCH-26NOV12BALIUS-BAL`) | 0.16 / 0.20 (25) | 18.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Valeriia Iushchenko (`KXITFWMATCH-26NOV12BALIUS-IUS`) | 0.76 / 0.83 (6) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elena Ruxandra Bertea vs Sapfo Sakellaridi -- W35 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12BERSAK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elena Ruxandra Bertea (`KXITFWMATCH-26NOV12BERSAK-BER`) | 0.78 / 0.84 (8) | 81.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sapfo Sakellaridi (`KXITFWMATCH-26NOV12BERSAK-SAK`) | 0.14 / 0.18 (42) | 16.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lucia Cortez Llorca vs Giulia Safina Popa -- W35 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12CORPOP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucia Cortez Llorca (`KXITFWMATCH-26NOV12CORPOP-COR`) | 0.49 / 0.52 (4) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Giulia Safina Popa (`KXITFWMATCH-26NOV12CORPOP-POP`) | 0.47 / 0.51 (56) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anais Gabriel vs Lorena Solar Donoso -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12GABSOL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anais Gabriel (`KXITFWMATCH-26NOV12GABSOL-GAB`) | 0.54 / 0.60 (312) | 57.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lorena Solar Donoso (`KXITFWMATCH-26NOV12GABSOL-SOL`) | 0.40 / 0.45 (295) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matilde Paoletti vs Jennifer Ruggeri -- W35 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12PAORUG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matilde Paoletti (`KXITFWMATCH-26NOV12PAORUG-PAO`) | 0.30 / 0.35 (5) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jennifer Ruggeri (`KXITFWMATCH-26NOV12PAORUG-RUG`) | 0.61 / 0.69 (42) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Diana-Ioana Simionescu vs Ekaterina Agureeva -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12SIMAGU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Agureeva (`KXITFWMATCH-26NOV12SIMAGU-AGU`) | 0.11 / 0.13 (30) | 12.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Diana-Ioana Simionescu (`KXITFWMATCH-26NOV12SIMAGU-SIM`) | 0.86 / 0.90 (7) | 88.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Julia Stamatova vs Marija Lauva -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12STALAU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marija Lauva (`KXITFWMATCH-26NOV12STALAU-LAU`) | 0.41 / 0.42 (47) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Julia Stamatova (`KXITFWMATCH-26NOV12STALAU-STA`) | 0.56 / 0.59 (3) | 57.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daria Yesypchuk vs Jana Bojovic -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12YESBOJ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jana Bojovic (`KXITFWMATCH-26NOV12YESBOJ-BOJ`) | 0.31 / 0.43 (4) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daria Yesypchuk (`KXITFWMATCH-26NOV12YESBOJ-YES`) | 0.60 / 0.68 (5) | 64.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ilay Yoruk vs Mariia Drobysheva -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12YORDRO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mariia Drobysheva (`KXITFWMATCH-26NOV12YORDRO-DRO`) | 0.38 / 0.47 (56) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ilay Yoruk (`KXITFWMATCH-26NOV12YORDRO-YOR`) | 0.55 / 0.58 (50) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Thiago Agustin Tirante vs Aleksandr Shevchenko -- ATP Stockholm QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-12 17:00Z
* Current expected start: 2026-11-12 14:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-11 21:14Z
* Recommended handicap-by time: 2026-11-12 13:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · surface ? · scheduled 2026-11-12T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26NOV12TIRSHE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aleksandr Shevchenko (`KXATPMATCH-26NOV12TIRSHE-SHE`) | 0.53 / 0.57 (5) | 55.0% | -- | -- | -- [-----] | -- | 55.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Thiago Agustin Tirante (`KXATPMATCH-26NOV12TIRSHE-TIR`) | 0.45 / 0.47 (1) | 46.0% | -- | -- | -- [-----] | -- | 45.8% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Aleksandre Bakshi vs Hazem Naw -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12BAKNAW:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aleksandre Bakshi (`KXITFMATCH-26NOV12BAKNAW-BAK`) | 0.36 / 0.48 (4) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hazem Naw (`KXITFMATCH-26NOV12BAKNAW-NAW`) | 0.56 / 0.63 (5) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lorenzo Bocchi vs John Bothma -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12BOCBOT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Bocchi (`KXITFMATCH-26NOV12BOCBOT-BOC`) | 0.64 / 0.71 (2) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| John Bothma (`KXITFMATCH-26NOV12BOCBOT-BOT`) | 0.27 / 0.29 (1) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Connel / Hongyu vs Liu / Xiao -- M15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12CONHONLIUXIA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Connel / Hongyu (`KXITFDOUBLES-26NOV12CONHONLIUXIA-CONHON`) | 0.05 / 0.89 (56) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Liu / Xiao (`KXITFDOUBLES-26NOV12CONHONLIUXIA-LIUXIA`) | 0.07 / 0.89 (56) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Filiberto Fumagalli vs Saba Purtseladze -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12FUMPUR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Filiberto Fumagalli (`KXITFMATCH-26NOV12FUMPUR-FUM`) | 0.24 / 0.34 (5) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Saba Purtseladze (`KXITFMATCH-26NOV12FUMPUR-PUR`) | 0.63 / 0.74 (2) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jeong / Yang vs Hong / Ju Kim -- M15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12JEOYANHONJUK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hong / Ju Kim (`KXITFDOUBLES-26NOV12JEOYANHONJUK-HONJUK`) | 0.06 / 0.88 (2) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jeong / Yang (`KXITFDOUBLES-26NOV12JEOYANHONJUK-JEOYAN`) | 0.06 / 0.90 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nima / Pan vs Aleshchev / Storch -- M15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12NIMPANALESTO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aleshchev / Storch (`KXITFDOUBLES-26NOV12NIMPANALESTO-ALESTO`) | 0.06 / 0.88 (103) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nima / Pan (`KXITFDOUBLES-26NOV12NIMPANALESTO-NIMPAN`) | 0.06 / 0.89 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nicola Senn vs Yurii Dzhavakian -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12SENDZH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yurii Dzhavakian (`KXITFMATCH-26NOV12SENDZH-DZH`) | 0.55 / 0.73 (2) | 64.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nicola Senn (`KXITFMATCH-26NOV12SENDZH-SEN`) | 0.31 / 0.48 (2) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Coco Bosman vs Lamis Alhussein Abdel Aziz -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12BOSALH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lamis Alhussein Abdel Aziz (`KXITFWMATCH-26NOV12BOSALH-ALH`) | 0.80 / 0.83 (10) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Coco Bosman (`KXITFWMATCH-26NOV12BOSALH-BOS`) | 0.13 / 0.20 (13) | 16.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yekaterina Dmitrichenko vs Alexandra Chapurina -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12DMICHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandra Chapurina (`KXITFWMATCH-26NOV12DMICHA-CHA`) | 0.05 / 0.12 (27) | 8.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yekaterina Dmitrichenko (`KXITFWMATCH-26NOV12DMICHA-DMI`) | 0.88 / 0.92 (35) | 90.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yasmin Ezzat vs Iveta Dapkute -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12EZZDAP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iveta Dapkute (`KXITFWMATCH-26NOV12EZZDAP-DAP`) | 0.24 / 0.30 (10) | 27.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yasmin Ezzat (`KXITFWMATCH-26NOV12EZZDAP-EZZ`) | 0.70 / 0.72 (32) | 71.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mu Jie Tzeng vs Irem Kurt -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12TZEKUR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Irem Kurt (`KXITFWMATCH-26NOV12TZEKUR-KUR`) | 0.58 / 0.67 (47) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mu Jie Tzeng (`KXITFWMATCH-26NOV12TZEKUR-TZE`) | 0.36 / 0.38 (40) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bozo Barun vs Nikita Belozertsev -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12BARBEL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bozo Barun (`KXITFMATCH-26NOV12BARBEL-BAR`) | 0.14 / 0.23 (37) | 18.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nikita Belozertsev (`KXITFMATCH-26NOV12BARBEL-BEL`) | 0.73 / 0.82 (36) | 77.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andrea Colombo vs Nazim Makhlouf -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12COLMAK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrea Colombo (`KXITFMATCH-26NOV12COLMAK-COL`) | 0.56 / 0.60 (26) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nazim Makhlouf (`KXITFMATCH-26NOV12COLMAK-MAK`) | 0.40 / 0.45 (62) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jack Karlsson Wistrand vs Wissam Abderrahman -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12KARABD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wissam Abderrahman (`KXITFMATCH-26NOV12KARABD-ABD`) | 0.81 / 0.86 (11) | 83.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jack Karlsson Wistrand (`KXITFMATCH-26NOV12KARABD-KAR`) | 0.10 / 0.18 (64) | 14.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amaury Raynel vs Stefano D'Agostino -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12RAYDAG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefano D'Agostino (`KXITFMATCH-26NOV12RAYDAG-DAG`) | 0.66 / 0.71 (310) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Amaury Raynel (`KXITFMATCH-26NOV12RAYDAG-RAY`) | 0.26 / 0.33 (21) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Louanne Djafari vs Marta Soriano Santiago -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12DJASOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Louanne Djafari (`KXITFWMATCH-26NOV12DJASOR-DJA`) | 0.12 / 0.17 (5) | 14.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marta Soriano Santiago (`KXITFWMATCH-26NOV12DJASOR-SOR`) | 0.80 / 0.85 (250) | 82.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rira Kosaka vs Lya Fernandez -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12KOSFER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lya Fernandez (`KXITFWMATCH-26NOV12KOSFER-FER`) | 0.43 / 0.48 (54) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rira Kosaka (`KXITFWMATCH-26NOV12KOSFER-KOS`) | 0.51 / 0.54 (43) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anastasia Lizunova vs Yui Watanabe -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12LIZWAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasia Lizunova (`KXITFWMATCH-26NOV12LIZWAT-LIZ`) | 0.72 / 0.80 (6) | 76.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yui Watanabe (`KXITFWMATCH-26NOV12LIZWAT-WAT`) | 0.20 / 0.31 (6) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matilde Mariani vs Mariia Masiianskaia -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12MARMAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matilde Mariani (`KXITFWMATCH-26NOV12MARMAS-MAR`) | 0.79 / 0.83 (8) | 81.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mariia Masiianskaia (`KXITFWMATCH-26NOV12MARMAS-MAS`) | 0.15 / 0.21 (29) | 18.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pierre Yves Bailly vs Szymon Karpinski -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12BAIKAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pierre Yves Bailly (`KXITFMATCH-26NOV12BAIKAR-BAI`) | 0.88 / 0.95 (169) | 91.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Szymon Karpinski (`KXITFMATCH-26NOV12BAIKAR-KAR`) | 0.05 / 0.11 (17) | 8.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Basile / Van Der Meerschen vs Adrian Andreescu / Ilie Bogdan Petre -- M15 Antalya QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12BASVANADRILI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Andreescu / Ilie Bogdan Petre (`KXITFDOUBLES-26NOV12BASVANADRILI-ADRILI`) | 0.40 / 0.59 (128) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Basile / Van Der Meerschen (`KXITFDOUBLES-26NOV12BASVANADRILI-BASVAN`) | 0.47 / 0.87 (3) | 67.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Baum / Cerny vs Krstic / Radjenovic -- M15 Antalya QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12BAUCERKRSRAD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Baum / Cerny (`KXITFDOUBLES-26NOV12BAUCERKRSRAD-BAUCER`) | 0.70 / 0.88 (1) | 79.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Krstic / Radjenovic (`KXITFDOUBLES-26NOV12BAUCERKRSRAD-KRSRAD`) | 0.16 / 0.70 (3) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Raffaele Ciurnelli vs Alexander Weis -- M25 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12CIUWEI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raffaele Ciurnelli (`KXITFMATCH-26NOV12CIUWEI-CIU`) | 0.35 / 0.41 (78) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexander Weis (`KXITFMATCH-26NOV12CIUWEI-WEI`) | 0.57 / 0.64 (7) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tommaso Compagnucci vs Oleksandr Ovcharenko -- M25 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12COMOVC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tommaso Compagnucci (`KXITFMATCH-26NOV12COMOVC-COM`) | 0.47 / 0.52 (2) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Oleksandr Ovcharenko (`KXITFMATCH-26NOV12COMOVC-OVC`) | 0.47 / 0.52 (4) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gianmarco Ferrari vs Alex Marti Pujolras -- M25 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12FERMAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gianmarco Ferrari (`KXITFMATCH-26NOV12FERMAR-FER`) | 0.35 / 0.39 (2) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alex Marti Pujolras (`KXITFMATCH-26NOV12FERMAR-MAR`) | 0.57 / 0.65 (48) | 61.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marek Gengel vs Ole Bredschneijder -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12GENBRE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ole Bredschneijder (`KXITFMATCH-26NOV12GENBRE-BRE`) | 0.05 / 0.15 (11) | 10.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marek Gengel (`KXITFMATCH-26NOV12GENBRE-GEN`) | 0.86 / 0.95 (47) | 90.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Robert Guna vs Matias Reyniak -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12GUNREY:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Robert Guna (`KXITFMATCH-26NOV12GUNREY-GUN`) | 0.53 / 0.68 (1) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matias Reyniak (`KXITFMATCH-26NOV12GUNREY-REY`) | 0.36 / 0.45 (8) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Michel Hopp vs Julian DeSousa -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12HOPDES:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julian DeSousa (`KXITFMATCH-26NOV12HOPDES-DES`) | 0.05 / 0.06 (494) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Michel Hopp (`KXITFMATCH-26NOV12HOPDES-HOP`) | 0.93 / 0.95 (493) | 94.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Karim Ibrahim vs Artur Kukasian -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12IBRKUK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karim Ibrahim (`KXITFMATCH-26NOV12IBRKUK-IBR`) | 0.46 / 0.54 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Artur Kukasian (`KXITFMATCH-26NOV12IBRKUK-KUK`) | 0.46 / 0.53 (2) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ioannis Kountourakis vs Imanol Lopez Morillo -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12KOULOP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ioannis Kountourakis (`KXITFMATCH-26NOV12KOULOP-KOU`) | 0.24 / 0.27 (36) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Imanol Lopez Morillo (`KXITFMATCH-26NOV12KOULOP-LOP`) | 0.72 / 0.75 (5) | 73.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lopez / Ujvary vs Popko / Tiurnev -- M15 Antalya QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12LOPUJVPOPTIU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lopez / Ujvary (`KXITFDOUBLES-26NOV12LOPUJVPOPTIU-LOPUJV`) | 0.18 / 0.62 (3) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Popko / Tiurnev (`KXITFDOUBLES-26NOV12LOPUJVPOPTIU-POPTIU`) | 0.67 / 0.87 (1) | 77.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Saritas / Yazdani vs Aytekin / Christopher Kucukhuseyin -- M15 Antalya QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12SARYAZAYTCHR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aytekin / Christopher Kucukhuseyin (`KXITFDOUBLES-26NOV12SARYAZAYTCHR-AYTCHR`) | 0.19 / 0.49 (3) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Saritas / Yazdani (`KXITFDOUBLES-26NOV12SARYAZAYTCHR-SARYAZ`) | 0.67 / 0.89 (1) | 78.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mac Visser vs George Lazarov -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12VISLAZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| George Lazarov (`KXITFMATCH-26NOV12VISLAZ-LAZ`) | 0.80 / 0.87 (50) | 83.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mac Visser (`KXITFMATCH-26NOV12VISLAZ-VIS`) | 0.14 / 0.16 (13) | 15.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jan Wygona vs Daniil Piatrouski -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12WYGPIA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniil Piatrouski (`KXITFMATCH-26NOV12WYGPIA-PIA`) | 0.27 / 0.33 (5) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jan Wygona (`KXITFMATCH-26NOV12WYGPIA-WYG`) | 0.66 / 0.72 (5) | 69.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Isabel Adrover Gallego vs Chiara Fornasieri -- W15 Nules R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12ADRFOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isabel Adrover Gallego (`KXITFWMATCH-26NOV12ADRFOR-ADR`) | 0.21 / 0.25 (13) | 23.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Chiara Fornasieri (`KXITFWMATCH-26NOV12ADRFOR-FOR`) | 0.73 / 0.78 (61) | 75.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andrei / Maria Brotea vs Bojica / Safta -- W15 Antalya QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12ANDMARBOJSAF:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrei / Maria Brotea (`KXITFWDOUBLES-26NOV12ANDMARBOJSAF-ANDMAR`) | 0.07 / 0.78 (100) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bojica / Safta (`KXITFWDOUBLES-26NOV12ANDMARBOJSAF-BOJSAF`) | 0.15 / 0.86 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Atay / Turkmen vs Auer / Farzami -- W15 Antalya QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12ATATURAUEFAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Atay / Turkmen (`KXITFWDOUBLES-26NOV12ATATURAUEFAR-ATATUR`) | 0.57 / 0.80 (1) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Auer / Farzami (`KXITFWDOUBLES-26NOV12ATATURAUEFAR-AUEFAR`) | 0.26 / 0.56 (3) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Astrid Wanja Brune Olsen vs Carlotta Moccia -- W15 Nules R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12BRUMOC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Astrid Wanja Brune Olsen (`KXITFWMATCH-26NOV12BRUMOC-BRU`) | 0.57 / 0.63 (50) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Carlotta Moccia (`KXITFWMATCH-26NOV12BRUMOC-MOC`) | 0.35 / 0.40 (24) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ninon Carpentier vs Iva Primorac Pavicic -- W15 Paris R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12CARPRI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ninon Carpentier (`KXITFWMATCH-26NOV12CARPRI-CAR`) | 0.13 / 0.16 (6) | 14.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Iva Primorac Pavicic (`KXITFWMATCH-26NOV12CARPRI-PRI`) | 0.81 / 0.85 (7) | 83.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Iliia Dashkevich vs Anna Snigireva -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12DASSNI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iliia Dashkevich (`KXITFWMATCH-26NOV12DASSNI-DAS`) | 0.07 / 0.20 (1) | 13.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anna Snigireva (`KXITFWMATCH-26NOV12DASSNI-SNI`) | 0.81 / 0.88 (2) | 84.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tilwith Di Girolami vs Anna Brunet-Brady -- W15 Paris R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12DIGBRU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Brunet-Brady (`KXITFWMATCH-26NOV12DIGBRU-BRU`) | 0.05 / 0.11 (20) | 8.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tilwith Di Girolami (`KXITFWMATCH-26NOV12DIGBRU-DIG`) | 0.89 / 0.92 (5) | 90.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jade Groen vs Zoe Ulrich -- W15 Paris R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12GROULR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jade Groen (`KXITFWMATCH-26NOV12GROULR-GRO`) | 0.78 / 0.79 (252) | 78.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Zoe Ulrich (`KXITFWMATCH-26NOV12GROULR-ULR`) | 0.15 / 0.23 (9) | 19.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Polina Kuharenko vs Anastasia Efremova -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12KUHEFR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasia Efremova (`KXITFWMATCH-26NOV12KUHEFR-EFR`) | 0.31 / 0.41 (10) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Polina Kuharenko (`KXITFWMATCH-26NOV12KUHEFR-KUH`) | 0.60 / 0.71 (14) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ane Mintegi Del Olmo vs Eliska Tichackova -- W35 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12MINTIC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ane Mintegi Del Olmo (`KXITFWMATCH-26NOV12MINTIC-MIN`) | 0.73 / 0.78 (6) | 75.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eliska Tichackova (`KXITFWMATCH-26NOV12MINTIC-TIC`) | 0.19 / 0.22 (5) | 20.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sandra Samir vs Ksenia Meshcheryakova -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12SAMMES:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ksenia Meshcheryakova (`KXITFWMATCH-26NOV12SAMMES-MES`) | 0.14 / 0.50 (4) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sandra Samir (`KXITFWMATCH-26NOV12SAMMES-SAM`) | 0.78 / 0.89 (3) | 83.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Natalija Senic vs Alisa Oktiabreva -- W35 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12SENOKT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alisa Oktiabreva (`KXITFWMATCH-26NOV12SENOKT-OKT`) | 0.92 / 0.96 (197) | 94.0% | -- | -- | -- [-----] | 93.7% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Natalija Senic (`KXITFWMATCH-26NOV12SENOKT-SEN`) | 0.04 / 0.06 (557) | 5.0% | -- | -- | -- [-----] | 6.3% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tina Nadine Smith vs Lucie Nguyen Tan -- W35 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12SMINGU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucie Nguyen Tan (`KXITFWMATCH-26NOV12SMINGU-NGU`) | 0.69 / 0.70 (76) | 69.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tina Nadine Smith (`KXITFWMATCH-26NOV12SMINGU-SMI`) | 0.31 / 0.36 (7) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maria Toma vs Mireia Sagrista Bermejo -- W15 Nules R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12TOMSAG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mireia Sagrista Bermejo (`KXITFWMATCH-26NOV12TOMSAG-SAG`) | 0.31 / 0.39 (39) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maria Toma (`KXITFWMATCH-26NOV12TOMSAG-TOM`) | 0.58 / 0.69 (9) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Neus Torner Sensano vs Claudia Ferrer Perez -- W15 Nules R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12TORFER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Claudia Ferrer Perez (`KXITFWMATCH-26NOV12TORFER-FER`) | 0.09 / 0.14 (23) | 11.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Neus Torner Sensano (`KXITFWMATCH-26NOV12TORFER-TOR`) | 0.86 / 0.90 (36) | 88.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aurora Zantedeschi vs Loes Ebeling Koning -- W35 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12ZANEBE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Loes Ebeling Koning (`KXITFWMATCH-26NOV12ZANEBE-EBE`) | 0.58 / 0.63 (65) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aurora Zantedeschi (`KXITFWMATCH-26NOV12ZANEBE-ZAN`) | 0.36 / 0.41 (28) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mohamed Ali Abibsi vs Liam Gavrielides -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12ABIGAV:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mohamed Ali Abibsi (`KXITFMATCH-26NOV12ABIGAV-ABI`) | 0.09 / 0.37 (1) | 23.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Liam Gavrielides (`KXITFMATCH-26NOV12ABIGAV-GAV`) | 0.82 / 0.94 (1) | 88.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tuncay Duran vs Phil Dungs -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12DURDUN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Phil Dungs (`KXITFMATCH-26NOV12DURDUN-DUN`) | 0.05 / 0.10 (12) | 7.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tuncay Duran (`KXITFMATCH-26NOV12DURDUN-DUR`) | 0.86 / 0.92 (1) | 89.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Adam Lynch vs Julien Penzlin -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12LYNPEN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adam Lynch (`KXITFMATCH-26NOV12LYNPEN-LYN`) | 0.24 / 0.33 (1) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Julien Penzlin (`KXITFMATCH-26NOV12LYNPEN-PEN`) | 0.75 / 0.77 (8) | 76.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mathieu Scaglia vs Viktor Frydrych -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12SCAFRY:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Viktor Frydrych (`KXITFMATCH-26NOV12SCAFRY-FRY`) | 0.25 / 0.30 (4) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mathieu Scaglia (`KXITFMATCH-26NOV12SCAFRY-SCA`) | 0.66 / 0.73 (3) | 69.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anastasia Bertacchi vs Emilia Carlotta Brune -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12BERBRU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasia Bertacchi (`KXITFWMATCH-26NOV12BERBRU-BER`) | 0.73 / 0.83 (2) | 78.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Emilia Carlotta Brune (`KXITFWMATCH-26NOV12BERBRU-BRU`) | 0.18 / 0.28 (9) | 23.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Keisija Berzina vs Mia Horvit -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12BERHOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Keisija Berzina (`KXITFWMATCH-26NOV12BERHOR-BER`) | 0.17 / 0.32 (12) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mia Horvit (`KXITFWMATCH-26NOV12BERHOR-HOR`) | 0.73 / 0.80 (3) | 76.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sophie Ehrenbergerova vs Lavinia Luciano -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12EHRLUC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sophie Ehrenbergerova (`KXITFWMATCH-26NOV12EHRLUC-EHR`) | 0.28 / 0.38 (11) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lavinia Luciano (`KXITFWMATCH-26NOV12EHRLUC-LUC`) | 0.62 / 0.72 (7) | 67.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daria Kuczer vs Ela Nala Milic -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12KUCMIL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daria Kuczer (`KXITFWMATCH-26NOV12KUCMIL-KUC`) | 0.68 / 0.78 (6) | 73.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ela Nala Milic (`KXITFWMATCH-26NOV12KUCMIL-MIL`) | 0.23 / 0.34 (16) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mario Arce Fernandez vs Manuel Mazza -- M15 Las Palmas de Gran Canaria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12ARCMAZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mario Arce Fernandez (`KXITFMATCH-26NOV12ARCMAZ-ARC`) | 0.12 / 0.18 (9) | 15.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Manuel Mazza (`KXITFMATCH-26NOV12ARCMAZ-MAZ`) | 0.81 / 0.85 (33) | 83.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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

ITF (ITF) · surface ? · scheduled 2026-11-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12BARAGU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| David Aguiar Johansson (`KXITFMATCH-26NOV12BARAGU-AGU`) | 0.06 / 0.12 (14) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alberto Barroso Campos (`KXITFMATCH-26NOV12BARAGU-BAR`) | 0.87 / 0.92 (48) | 89.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bothma / Gabet vs Senn / Wygona -- M15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12BOTGABSENWYG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bothma / Gabet (`KXITFDOUBLES-26NOV12BOTGABSENWYG-BOTGAB`) | 0.56 / 0.86 (4) | 71.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Senn / Wygona (`KXITFDOUBLES-26NOV12BOTGABSENWYG-SENWYG`) | 0.30 / 0.83 (3) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Carles Cordoba vs Xavi Palomar -- M15 Las Palmas de Gran Canaria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12CORPAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carles Cordoba (`KXITFMATCH-26NOV12CORPAL-COR`) | 0.66 / 0.72 (58) | 69.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xavi Palomar (`KXITFMATCH-26NOV12CORPAL-PAL`) | 0.24 / 0.32 (56) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kenny De Schepper vs Garrett Johns -- M25 Vale do Lobo R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12DESJOH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kenny De Schepper (`KXITFMATCH-26NOV12DESJOH-DES`) | 0.27 / 0.33 (29) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Garrett Johns (`KXITFMATCH-26NOV12DESJOH-JOH`) | 0.66 / 0.71 (1) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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

ITF (ITF) · surface ? · scheduled 2026-11-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12GAKFIT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sergi Fita Juan (`KXITFMATCH-26NOV12GAKFIT-FIT`) | 0.06 / 0.51 (4) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ivan Gakhov (`KXITFMATCH-26NOV12GAKFIT-GAK`) | 0.81 / 0.92 (7) | 86.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Giuseppe La Vela vs Andrej Martin -- M25 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12LAVMAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giuseppe La Vela (`KXITFMATCH-26NOV12LAVMAR-LAV`) | 0.35 / 0.39 (6) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Andrej Martin (`KXITFMATCH-26NOV12LAVMAR-MAR`) | 0.57 / 0.65 (334) | 61.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Diogo Marques vs Duarte Lima Sanches -- M25 Vale do Lobo R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12MARLIM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Duarte Lima Sanches (`KXITFMATCH-26NOV12MARLIM-LIM`) | 0.08 / 0.12 (38) | 10.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Diogo Marques (`KXITFMATCH-26NOV12MARLIM-MAR`) | 0.85 / 0.93 (93) | 89.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Salvador Monteiro vs Pavel Lagutin -- M25 Vale do Lobo R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12MONLAG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pavel Lagutin (`KXITFMATCH-26NOV12MONLAG-LAG`) | 0.93 / 0.97 (513) | 95.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Salvador Monteiro (`KXITFMATCH-26NOV12MONLAG-MON`) | 0.03 / 0.04 (9) | 3.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sergi Perez Contri vs Matteo Gribaldo -- M25 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12PERGRI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Gribaldo (`KXITFMATCH-26NOV12PERGRI-GRI`) | 0.25 / 0.32 (8) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sergi Perez Contri (`KXITFMATCH-26NOV12PERGRI-PER`) | 0.66 / 0.72 (58) | 69.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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

ITF (ITF) · surface ? · scheduled 2026-11-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12PUJPON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matias Ponce de leon gomila (`KXITFMATCH-26NOV12PUJPON-PON`) | 0.52 / 0.63 (3) | 57.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bruno Pujol Navarro (`KXITFMATCH-26NOV12PUJPON-PUJ`) | 0.37 / 0.42 (97) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chelsea Fontenel vs Marie Vogt -- W15 Paris R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12FONVOG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chelsea Fontenel (`KXITFWMATCH-26NOV12FONVOG-FON`) | 0.24 / 0.29 (12) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marie Vogt (`KXITFWMATCH-26NOV12FONVOG-VOG`) | 0.67 / 0.75 (44) | 71.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Delia Gaillard vs Didi Bredberg Canizares -- W15 Nules R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12GAIBRE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Didi Bredberg Canizares (`KXITFWMATCH-26NOV12GAIBRE-BRE`) | 0.88 / 0.92 (21) | 90.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Delia Gaillard (`KXITFWMATCH-26NOV12GAIBRE-GAI`) | 0.06 / 0.12 (72) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kochta / Sousa Salazar vs Starkova / Suslova -- W15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12KOCSOUSTASUS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kochta / Sousa Salazar (`KXITFWDOUBLES-26NOV12KOCSOUSTASUS-KOCSOU`) | 0.35 / 0.69 (3) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Starkova / Suslova (`KXITFWDOUBLES-26NOV12KOCSOUSTASUS-STASUS`) | 0.51 / 0.74 (3) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sofia Montesinos Vilanova vs Aurora Corvi -- W15 Nules R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12MONCOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aurora Corvi (`KXITFWMATCH-26NOV12MONCOR-COR`) | 0.78 / 0.84 (294) | 81.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sofia Montesinos Vilanova (`KXITFWMATCH-26NOV12MONCOR-MON`) | 0.16 / 0.20 (27) | 18.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alina Nesmianovych vs Isis Louise Van den Broek -- W15 Paris R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12NESVAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alina Nesmianovych (`KXITFWMATCH-26NOV12NESVAN-NES`) | 0.05 / 0.10 (20) | 7.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Isis Louise Van den Broek (`KXITFWMATCH-26NOV12NESVAN-VAN`) | 0.89 / 0.94 (42) | 91.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ando Tiantsoa Ratre vs Beatrise Zeltina -- W15 Paris R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12RATZEL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ando Tiantsoa Ratre (`KXITFWMATCH-26NOV12RATZEL-RAT`) | 0.04 / 0.06 (1272) | 5.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Beatrise Zeltina (`KXITFWMATCH-26NOV12RATZEL-ZEL`) | 0.91 / 0.96 (191) | 93.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maria Shmeleva vs Alyssa Reguer -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12SHMREG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alyssa Reguer (`KXITFWMATCH-26NOV12SHMREG-REG`) | 0.66 / 0.76 (1) | 71.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maria Shmeleva (`KXITFWMATCH-26NOV12SHMREG-SHM`) | 0.25 / 0.32 (5) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Katerina Tsygourova vs Aleksandra Pozarenko -- W15 Nules R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12TSYPOZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aleksandra Pozarenko (`KXITFWMATCH-26NOV12TSYPOZ-POZ`) | 0.05 / 0.12 (42) | 8.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Katerina Tsygourova (`KXITFWMATCH-26NOV12TSYPOZ-TSY`) | 0.85 / 0.92 (20) | 88.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Karim Al-Amin vs Marcel Zielinski -- M15 Las Palmas de Gran Canaria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12ALAZIE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karim Al-Amin (`KXITFMATCH-26NOV12ALAZIE-ALA`) | 0.29 / 0.32 (6) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marcel Zielinski (`KXITFMATCH-26NOV12ALAZIE-ZIE`) | 0.64 / 0.67 (6) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ivan Ivanov vs Vasco Leote Prata -- M25 Vale do Lobo R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12IVALEO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ivan Ivanov (`KXITFMATCH-26NOV12IVALEO-IVA`) | 0.71 / 0.74 (9) | 72.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vasco Leote Prata (`KXITFMATCH-26NOV12IVALEO-LEO`) | 0.27 / 0.29 (36) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kaan Oktay / Schlossmann vs Bakshi / Purtseladze -- M15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12KAASCHBAKPUR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bakshi / Purtseladze (`KXITFDOUBLES-26NOV12KAASCHBAKPUR-BAKPUR`) | 0.82 / 0.90 (50) | 86.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kaan Oktay / Schlossmann (`KXITFDOUBLES-26NOV12KAASCHBAKPUR-KAASCH`) | 0.05 / 0.77 (3) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alejandro Lopez Escribano vs Joao Domingues -- M25 Vale do Lobo R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12LOPDOM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joao Domingues (`KXITFMATCH-26NOV12LOPDOM-DOM`) | 0.82 / 0.84 (44) | 83.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alejandro Lopez Escribano (`KXITFMATCH-26NOV12LOPDOM-LOP`) | 0.15 / 0.21 (31) | 18.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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

ITF (ITF) · surface ? · scheduled 2026-11-12T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12MOLCUR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tomas Curras Abasolo (`KXITFMATCH-26NOV12MOLCUR-CUR`) | 0.25 / 0.33 (16) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rudolf Molleker (`KXITFMATCH-26NOV12MOLCUR-MOL`) | 0.64 / 0.71 (7) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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

ITF (ITF) · surface ? · scheduled 2026-11-12T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12PARFIG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maximilian Figl (`KXITFMATCH-26NOV12PARFIG-FIG`) | 0.11 / 0.14 (55) | 12.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ignacio Parisca (`KXITFMATCH-26NOV12PARFIG-PAR`) | 0.84 / 0.89 (5) | 86.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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

ITF (ITF) · surface ? · scheduled 2026-11-12T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12PERGUT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Niklas Guttau (`KXITFMATCH-26NOV12PERGUT-GUT`) | 0.74 / 0.81 (48) | 77.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Roberto Perez socas (`KXITFMATCH-26NOV12PERGUT-PER`) | 0.17 / 0.23 (34) | 20.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luca Potenza vs Eric Vanshelboim -- M25 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12POTVAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luca Potenza (`KXITFMATCH-26NOV12POTVAN-POT`) | 0.08 / 0.93 (100) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eric Vanshelboim (`KXITFMATCH-26NOV12POTVAN-VAN`) | 0.06 / 0.94 (1) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Patrick Schoen vs Diogo Morais -- M25 Vale do Lobo R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12SCHMOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diogo Morais (`KXITFMATCH-26NOV12SCHMOR-MOR`) | 0.14 / 0.18 (6) | 16.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Patrick Schoen (`KXITFMATCH-26NOV12SCHMOR-SCH`) | 0.79 / 0.85 (286) | 82.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stanke / Van Herck vs Bocchi / Mugelli -- M15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12STAVANBOCMUG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bocchi / Mugelli (`KXITFDOUBLES-26NOV12STAVANBOCMUG-BOCMUG`) | 0.30 / 0.60 (1) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stanke / Van Herck (`KXITFDOUBLES-26NOV12STAVANBOCMUG-STAVAN`) | 0.56 / 0.87 (4) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Radu David Turcanu vs Daniele Rapagnetta -- M25 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12TURRAP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniele Rapagnetta (`KXITFMATCH-26NOV12TURRAP-RAP`) | 0.46 / 0.50 (3) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Radu David Turcanu (`KXITFMATCH-26NOV12TURRAP-TUR`) | 0.47 / 0.53 (327) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alhussein Abdel Aziz / Samir vs Khramtsova / Utkina -- W15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12ALHSAMKHRUTK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alhussein Abdel Aziz / Samir (`KXITFWDOUBLES-26NOV12ALHSAMKHRUTK-ALHSAM`) | 0.83 / 0.85 (2) | 84.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Khramtsova / Utkina (`KXITFWDOUBLES-26NOV12ALHSAMKHRUTK-KHRUTK`) | 0.10 / 0.34 (3) | 22.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dorofeeva-Rybas / Zhenikhova vs Allen / Okutoyi -- W35 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12DORZHEALLOKU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Allen / Okutoyi (`KXITFWDOUBLES-26NOV12DORZHEALLOKU-ALLOKU`) | 0.58 / 0.74 (1) | 66.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dorofeeva-Rybas / Zhenikhova (`KXITFWDOUBLES-26NOV12DORZHEALLOKU-DORZHE`) | 0.30 / 0.48 (1) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Constantin Frantzen / Bart Stevens vs Robert Galloway / Andre Goransson -- ATP Stockholm QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-11 15:00Z
* Current expected start: 2026-11-12 17:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-11 21:14Z
* Recommended handicap-by time: 2026-11-12 16:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-11T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV11FRASTEGALGOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Constantin Frantzen / Bart Stevens (`KXATPDOUBLES-26NOV11FRASTEGALGOR-FRASTE`) | 0.40 / 0.43 (150) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Robert Galloway / Andre Goransson (`KXATPDOUBLES-26NOV11FRASTEGALGOR-GALGOR`) | 0.57 / 0.60 (191) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Brooks / Ngounoue vs Abanda / Mattel -- W15 Paris SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12BRONGOABAMAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Abanda / Mattel (`KXITFWDOUBLES-26NOV12BRONGOABAMAT-ABAMAT`) | 0.76 / 0.85 (2) | 80.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Brooks / Ngounoue (`KXITFWDOUBLES-26NOV12BRONGOABAMAT-BRONGO`) | 0.11 / 0.39 (16) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Laura Mair vs Sarah Iliev -- W15 Paris R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12MAIILI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sarah Iliev (`KXITFWMATCH-26NOV12MAIILI-ILI`) | 0.49 / 0.54 (55) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Laura Mair (`KXITFWMATCH-26NOV12MAIILI-MAI`) | 0.41 / 0.51 (47) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kira Pavlova vs Sophia Biolay -- W15 Paris R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12PAVBIO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sophia Biolay (`KXITFWMATCH-26NOV12PAVBIO-BIO`) | 0.16 / 0.22 (14) | 19.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kira Pavlova (`KXITFWMATCH-26NOV12PAVBIO-PAV`) | 0.73 / 0.81 (3) | 77.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Izan Almazan Valiente vs Pierre Antoine Tailleu -- M25 Vale do Lobo R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12ALMTAI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Izan Almazan Valiente (`KXITFMATCH-26NOV12ALMTAI-ALM`) | 0.86 / 0.90 (165) | 88.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pierre Antoine Tailleu (`KXITFMATCH-26NOV12ALMTAI-TAI`) | 0.10 / 0.14 (9) | 12.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Brand / Thomas vs Visser / Wagenaar -- M15 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12BRATHOVISWAG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brand / Thomas (`KXITFDOUBLES-26NOV12BRATHOVISWAG-BRATHO`) | 0.35 / 0.57 (3) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Visser / Wagenaar (`KXITFDOUBLES-26NOV12BRATHOVISWAG-VISWAG`) | 0.52 / 0.74 (3) | 63.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hopp / Longwe-Smit vs Kaouk / Trufelli -- M15 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12HOPLONKAOTRU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hopp / Longwe-Smit (`KXITFDOUBLES-26NOV12HOPLONKAOTRU-HOPLON`) | 0.38 / 0.57 (12) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kaouk / Trufelli (`KXITFDOUBLES-26NOV12HOPLONKAOTRU-KAOTRU`) | 0.49 / 0.70 (34) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Ion / Kountourakis vs Gannon / Taguchi -- M15 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12IONKOUGANTAG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gannon / Taguchi (`KXITFDOUBLES-26NOV12IONKOUGANTAG-GANTAG`) | 0.08 / 0.89 (60) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ion / Kountourakis (`KXITFDOUBLES-26NOV12IONKOUGANTAG-IONKOU`) | 0.05 / 0.86 (60) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jones / Jones vs Dimitriou / Reyniak -- M15 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12JONJONDIMREY:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dimitriou / Reyniak (`KXITFDOUBLES-26NOV12JONJONDIMREY-DIMREY`) | 0.14 / 0.38 (16) | 26.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jones / Jones (`KXITFDOUBLES-26NOV12JONJONDIMREY-JONJON`) | 0.72 / 0.87 (1) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Gavrila / Sakellaridi vs Cvetkovic / Stankovic -- W35 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12GAVSAKCVESTA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cvetkovic / Stankovic (`KXITFWDOUBLES-26NOV12GAVSAKCVESTA-CVESTA`) | 0.34 / 0.69 (3) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gavrila / Sakellaridi (`KXITFWDOUBLES-26NOV12GAVSAKCVESTA-GAVSAK`) | 0.52 / 0.82 (3) | 67.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Karatancheva / Shapatava vs Argyrokastriti / Cortez Llorca -- W35 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12KARSHAARGCOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Argyrokastriti / Cortez Llorca (`KXITFWDOUBLES-26NOV12KARSHAARGCOR-ARGCOR`) | 0.49 / 0.71 (4) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Karatancheva / Shapatava (`KXITFWDOUBLES-26NOV12KARSHAARGCOR-KARSHA`) | 0.37 / 0.64 (3) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ruxandra Bertea / Golovina vs Jovanovic / Spasova -- W35 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12RUXGOLJOVSPA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jovanovic / Spasova (`KXITFWDOUBLES-26NOV12RUXGOLJOVSPA-JOVSPA`) | 0.07 / 0.84 (56) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ruxandra Bertea / Golovina (`KXITFWDOUBLES-26NOV12RUXGOLJOVSPA-RUXGOL`) | 0.11 / 0.85 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Colombo / Piatti vs Raguin / Sadzik -- M15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12COLPIARAGSAD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Colombo / Piatti (`KXITFDOUBLES-26NOV12COLPIARAGSAD-COLPIA`) | 0.49 / 0.68 (1) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Raguin / Sadzik (`KXITFDOUBLES-26NOV12COLPIARAGSAD-RAGSAD`) | 0.37 / 0.74 (1) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Galphin Cossu / David Martinez vs Abderrahman / van Wyk -- M15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12GALDAVABDVAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Abderrahman / van Wyk (`KXITFDOUBLES-26NOV12GALDAVABDVAN-ABDVAN`) | 0.06 / 0.89 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Galphin Cossu / David Martinez (`KXITFDOUBLES-26NOV12GALDAVABDVAN-GALDAV`) | 0.08 / 0.89 (2) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Knis / Robas vs Belozertsev / Schell -- M15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12KNIROBBELSCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Belozertsev / Schell (`KXITFDOUBLES-26NOV12KNIROBBELSCH-BELSCH`) | 0.08 / 0.89 (2) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Knis / Robas (`KXITFDOUBLES-26NOV12KNIROBBELSCH-KNIROB`) | 0.06 / 0.89 (56) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Maurice / Raynel vs Batsabaken / Denitto -- M15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12MAURAYBATDEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Batsabaken / Denitto (`KXITFDOUBLES-26NOV12MAURAYBATDEN-BATDEN`) | 0.48 / 0.87 (3) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maurice / Raynel (`KXITFDOUBLES-26NOV12MAURAYBATDEN-MAURAY`) | 0.39 / 0.74 (8) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Adrover Gallego / Sagrista Bermejo vs Fornasieri / Parentini Vallega Montebruno -- W15 Nules SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12ADRSAGFORPAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrover Gallego / Sagrista Bermejo (`KXITFWDOUBLES-26NOV12ADRSAGFORPAR-ADRSAG`) | 0.43 / 0.78 (3) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fornasieri / Parentini Vallega Montebruno (`KXITFWDOUBLES-26NOV12ADRSAGFORPAR-FORPAR`) | 0.44 / 0.65 (1) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dmitrichenko / Kurt vs Elkady / Nosei -- W15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12DMIKURELKNOS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dmitrichenko / Kurt (`KXITFWDOUBLES-26NOV12DMIKURELKNOS-DMIKUR`) | 0.11 / 0.85 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Elkady / Nosei (`KXITFWDOUBLES-26NOV12DMIKURELKNOS-ELKNOS`) | 0.07 / 0.84 (56) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Fernandez / Garcia-Patron Canals vs Husar / Lizunova -- W15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12FERGARHUSLIZ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fernandez / Garcia-Patron Canals (`KXITFWDOUBLES-26NOV12FERGARHUSLIZ-FERGAR`) | 0.15 / 0.41 (3) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Husar / Lizunova (`KXITFWDOUBLES-26NOV12FERGARHUSLIZ-HUSLIZ`) | 0.67 / 0.85 (2) | 76.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ivanovic / Smart vs Belkova / Kuharenko -- W15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12IVASMABELKUH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Belkova / Kuharenko (`KXITFWDOUBLES-26NOV12IVASMABELKUH-BELKUH`) | 0.41 / 0.62 (1) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ivanovic / Smart (`KXITFWDOUBLES-26NOV12IVASMABELKUH-IVASMA`) | 0.45 / 0.65 (1) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jaeger / Masiianskaia vs De Baene / Djafari -- W15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12JAEMASDEBDJA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| De Baene / Djafari (`KXITFWDOUBLES-26NOV12JAEMASDEBDJA-DEBDJA`) | 0.36 / 0.80 (3) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jaeger / Masiianskaia (`KXITFWDOUBLES-26NOV12JAEMASDEBDJA-JAEMAS`) | 0.51 / 0.76 (3) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Wanja Brune Olsen / Sziedat vs Ferrer Perez / Camila Rojas -- W15 Nules SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12WANSZIFERCAM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ferrer Perez / Camila Rojas (`KXITFWDOUBLES-26NOV12WANSZIFERCAM-FERCAM`) | 0.22 / 0.42 (56) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Wanja Brune Olsen / Sziedat (`KXITFWDOUBLES-26NOV12WANSZIFERCAM-WANSZI`) | 0.64 / 0.79 (1) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lorenzo Musetti vs Ugo Humbert -- ATP Stockholm QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-12 21:40Z
* Current expected start: 2026-11-12 19:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-11 21:14Z
* Recommended handicap-by time: 2026-11-12 18:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN

ATP (TOUR_500_250) · surface ? · scheduled 2026-11-12T21:40:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26NOV12MUSHUM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ugo Humbert (`KXATPMATCH-26NOV12MUSHUM-HUM`) | 0.34 / 0.35 (740) | 34.5% | -- | -- | -- [-----] | 34.8% | 35.4% | 35.4% | MARKETS_AGREE | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lorenzo Musetti (`KXATPMATCH-26NOV12MUSHUM-MUS`) | 0.65 / 0.66 (92) | 65.5% | -- | -- | -- [-----] | 65.2% | 65.0% | 65.0% | MARKETS_AGREE | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Valerio Aboian vs Glauco Pinheiro da Cruz Junior -- M25 Santa Cruz do Sul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12ABOPIN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valerio Aboian (`KXITFMATCH-26NOV12ABOPIN-ABO`) | 0.90 / 0.95 (10) | 92.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Glauco Pinheiro da Cruz Junior (`KXITFMATCH-26NOV12ABOPIN-PIN`) | 0.05 / 0.33 (56) | 19.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pedro Sakamoto vs Augusto Land -- M25 Santa Cruz do Sul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV12SAKLAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Augusto Land (`KXITFMATCH-26NOV12SAKLAN-LAN`) | 0.05 / 0.30 (56) | 17.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pedro Sakamoto (`KXITFMATCH-26NOV12SAKLAN-SAK`) | 0.89 / 0.95 (13) | 92.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Leticia Garcia Vidal vs Julia Julia Cerqueira Carvalho Farias Lima -- W15 São Carlos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12GARJUL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leticia Garcia Vidal (`KXITFWMATCH-26NOV12GARJUL-GAR`) | 0.89 / 0.95 (10) | 92.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Julia Julia Cerqueira Carvalho Farias Lima (`KXITFWMATCH-26NOV12GARJUL-JUL`) | 0.04 / 0.14 (13) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Juliana Giaccio vs Ana Giraldi Requena -- W15 Nules R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12GIAGIR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juliana Giaccio (`KXITFWMATCH-26NOV12GIAGIR-GIA`) | 0.83 / 0.91 (43) | 87.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ana Giraldi Requena (`KXITFWMATCH-26NOV12GIAGIR-GIR`) | 0.12 / 0.14 (33) | 13.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luciano / Mariani vs Nala Milic / Moneva -- W15 Monastir QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-12T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12LUCMARNALMON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luciano / Mariani (`KXITFWDOUBLES-26NOV12LUCMARNALMON-LUCMAR`) | 0.85 / 0.86 (2) | 85.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nala Milic / Moneva (`KXITFWDOUBLES-26NOV12LUCMARNALMON-NALMON`) | 0.06 / 0.76 (3) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Marie Mettraux vs Catarina Melleiro -- W15 São Carlos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12METMEL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Catarina Melleiro (`KXITFWMATCH-26NOV12METMEL-MEL`) | 0.04 / 0.15 (23) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marie Mettraux (`KXITFWMATCH-26NOV12METMEL-MET`) | 0.90 / 0.95 (10) | 92.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Isadora Sigrist vs Marjorie Souza -- W15 São Carlos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-12 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-12T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV12SIGSOU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isadora Sigrist (`KXITFWMATCH-26NOV12SIGSOU-SIG`) | 0.04 / 0.14 (23) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marjorie Souza (`KXITFWMATCH-26NOV12SIGSOU-SOU`) | 0.91 / 0.94 (5) | 92.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marta Kostyuk vs Coco Gauff -- WTA Finals Women Singles Group A

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-11-12 23:00Z
* Current expected start: 2026-11-12 20:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-11 21:14Z
* Recommended handicap-by time: 2026-11-12 19:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

WTA (TOUR_FINALS) · surface ? · scheduled 2026-11-12T23:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26NOV12KOSGAU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Coco Gauff (`KXWTAMATCH-26NOV12KOSGAU-GAU`) | 0.70 / 0.71 (29609) | 70.5% | -- | -- | -- [-----] | 69.1% | 70.7% | 70.7% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marta Kostyuk (`KXWTAMATCH-26NOV12KOSGAU-KOS`) | 0.29 / 0.30 (29546) | 29.5% | -- | -- | -- [-----] | 30.9% | 29.0% | 29.0% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; EXTERNAL_PRICE_STALE; WIDE_SPREAD

## Taylor Fritz vs Holger Rune -- ATP Stockholm QF

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-12 20:30Z
* Current expected start: 2026-11-12 20:30Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: 2026-11-12 19:45Z

* Status notes: NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source)

ATP (TOUR_500_250) · surface ? · scheduled 2026-11-12T20:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26NOV12FRIRUN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Taylor Fritz (`KXATPMATCH-26NOV12FRIRUN-FRI`) | 0.58 / 0.85 (5) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Holger Rune (`KXATPMATCH-26NOV12FRIRUN-RUN`) | 0.21 / 0.78 (14) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jessica Pegula vs Linda Noskova -- WTA Finals Women Singles Group A

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-13 00:10Z
* Current expected start: 2026-11-13 00:10Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: 2026-11-12 23:25Z

* Status notes: NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source)

WTA (TOUR_FINALS) · surface ? · scheduled 2026-11-13T00:10:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26NOV12PEGNOS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Linda Noskova (`KXWTAMATCH-26NOV12PEGNOS-NOS`) | 0.53 / 0.54 (33432) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jessica Pegula (`KXWTAMATCH-26NOV12PEGNOS-PEG`) | 0.46 / 0.47 (10) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NO_EXTERNAL_PRICE; WIDE_SPREAD

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
