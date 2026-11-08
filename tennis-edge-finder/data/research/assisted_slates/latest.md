# ASSISTED SLATE -- 2026-11-08T07:33Z (`SL-20261108T073322Z-de92232d`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

114 open matches not seen started, 324 markets. Skipped: {"first_ball_already_observed": 1}. Sources: shadow board 2026-11-08T07:13:11.394559+00:00, Model 4 2026-11-08T07:13:22.583972+00:00, Gen-1 ledger 2026-11-08T07:13:07.587580+00:00, external 2026-11-08T06:43:28.487499+00:00, capture 20261108T064215Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-11-08 11:00Z**
* Recommended RUN TENNIS time: **2026-11-08 10:15Z**
* Final price/status check time: **2026-11-08 10:50Z**
* Number of matches in window: 3 (Nikoloz Basilashvili vs Borna Gojo, Inaki Montes-de la Torre vs Lorenzo Sonego, Adrian Mannarino vs Toby Samuel)

* **1 main-tour match(es) have NO verified start status** (STATUS_AMBIGUOUS): BET blocked until a live status check.

Slate built 2026-11-08T07:33Z. Refresh due by: 2026-11-08 10:15Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 20, "HIGH_REVIEW": 17, "NORMAL": 156, "REVIEW": 32, "UNPRICED": 99}; match winners: {"EXTREME": 20, "HIGH_REVIEW": 14, "NORMAL": 73, "REVIEW": 22, "UNPRICED": 99}; quote freshness at build: {"STALE": 225}.

## Evan Zhu vs Thomas Fancutt -- ATP Challenger Brisbane Semi F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-08T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126573:200632:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thomas Fancutt (`KXATPCHALLENGERMATCH-26NOV07ZHUFAN-FAN`) | 0.83 / 0.84 (32284) | 83.5% | 56.6% | 61.2% | 58.8% [57.9%-59.8%] | -- | 29.5% | -- | INSUFFICIENT_INPUTS | PASS | -26.9 pp | EXTREME (DATA_WARNING) | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Evan Zhu (`KXATPCHALLENGERMATCH-26NOV07ZHUFAN-ZHU`) | 0.16 / 0.17 (5982) | 16.5% | 43.4% | 38.8% | 41.2% [40.2%-42.1%] | -- | 70.6% | -- | INSUFFICIENT_INPUTS | PASS | +26.9 pp | EXTREME (DATA_WARNING) | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3487.0, B 1210.0; serve-point win A 63.8%, B 34.9%; Elo A 1340.7, B 1389.7; model uncertainty 0.0097
* Form inputs: days since last match A 39, B 54; matches on record A 418, B 431; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV07ZHUFAN-ZHU  (YES = Evan Zhu)
Model: 43%
Kalshi: 16%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STALE_QUOTE

## Claire Liu vs Alexandra Eala -- WTA Hong Kong F

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-11-08 11:00Z
* Current expected start: 2026-11-08 06:54Z
* Source: COURT_PROGRESSION: preceding match on Centre Court in progress (set 2 of best-of-3); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-08 06:39Z
* Recommended handicap-by time: 2026-11-08 06:09Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-246_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA (TOUR_500_250) · Hard · scheduled 2026-11-08T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214906:223253:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandra Eala (`KXWTAMATCH-26NOV08LIUEAL-EAL`) | 0.68 / 0.69 (50991) | 68.5% | 74.7% | 67.0% | 69.3% [67.9%-70.3%] | 67.6% | 68.3% | 68.3% | MODEL_LONE_OUTLIER | PASS | +6.2 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Claire Liu (`KXWTAMATCH-26NOV08LIUEAL-LIU`) | 0.32 / 0.33 (87831) | 32.5% | 25.3% | 33.0% | 30.6% [29.7%-32.1%] | 32.4% | 31.8% | 31.8% | MODEL_LONE_OUTLIER | PASS | -7.2 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3837.0, B 4541.0; serve-point win A 52.7%, B 42.3%; Elo A 1783.0, B 1969.7; model uncertainty 0.0117
* Form inputs: days since last match A 1, B 1; matches on record A 463, B 374; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose -0.004, surface_dev_tight +0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV08LIUEAL-27` Over 26.5 games: 0.29/0.31 mid 30.0%, model 33.6% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV08LIUEAL-2-EAL` Will Alexandra Eala win set 2 in the Claire Liu vs Alexandra Eala match: 0.62/0.65 mid 63.5%, model 67.1% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26NOV08LIUEAL-22` Over 21.5 games: 0.52/0.53 mid 52.5%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap +3.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV08LIUEAL-1-EAL` Will Alexandra Eala win set 1 in the Claire Liu vs Alexandra Eala match: 0.64/0.65 mid 64.5%, model 67.1% (projection_v2.0 (prediction ledger)) -- gap +2.6 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV08LIUEAL-1-LIU` Will Claire Liu win set 1 in the Claire Liu vs Alexandra Eala match: 0.35/0.36 mid 35.5%, model 32.9% (projection_v2.0 (prediction ledger)) -- gap -2.6 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV08LIUEAL-2-LIU` Will Claire Liu win set 2 in the Claire Liu vs Alexandra Eala match: 0.33/0.36 mid 34.5%, model 32.9% (projection_v2.0 (prediction ledger)) -- gap -1.6 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26NOV08LIUEAL-17` Over 16.5 games: 0.86/0.91 mid 88.5%, model 90.0% (projection_v2.0 (prediction ledger)) -- gap +1.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STATUS_AMBIGUOUS; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Shintaro Imai vs Constantin Bittoun Kouzmine -- ATP Challenger Matsuyama Semi F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-08T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:122495:144970:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Constantin Bittoun Kouzmine (`KXATPCHALLENGERMATCH-26NOV07IMABIT-BIT`) | 0.02 / 0.03 (34496) | 2.5% | 38.3% | 33.0% | 31.7% [30.4%-33.0%] | 45.9% | -- | 45.9% | MODEL_LONE_OUTLIER | PASS | +35.8 pp | EXTREME (DATA_WARNING) | STALE | B / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Shintaro Imai (`KXATPCHALLENGERMATCH-26NOV07IMABIT-IMA`) | 0.97 / 0.98 (32128) | 97.5% | 61.7% | 67.0% | 68.3% [67.0%-69.6%] | 54.1% | -- | 54.1% | MODEL_LONE_OUTLIER | PASS | -35.8 pp | EXTREME (DATA_WARNING) | STALE | B / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 1292.0, B 3712.0; serve-point win A 64.5%, B 37.9%; Elo A 1507.2, B 1356.2; model uncertainty 0.0131
* Form inputs: days since last match A 12, B 54; matches on record A 461, B 437; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV07IMABIT-BIT  (YES = Constantin Bittoun Kouzmine)
Model: 38%
Kalshi: 2%
Gap: +36 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: SUPPORTS_MODEL_DIRECTION
Data quality: B (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.009, surface_dev_loose +0.009, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STALE_QUOTE

## Keisuke Saitoh vs Yusuke Takahashi -- ATP Challenger Matsuyama Semi F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-08T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126208:208861:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Keisuke Saitoh (`KXATPCHALLENGERMATCH-26NOV07SAITAK-SAI`) | 0.91 / 0.92 (32347) | 91.5% | 37.8% | 38.9% | 38.9% [37.5%-39.9%] | -- | 60.5% | 60.5% | MODEL_LONE_OUTLIER | PASS | -53.7 pp | EXTREME (DATA_WARNING) | STALE | B / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Yusuke Takahashi (`KXATPCHALLENGERMATCH-26NOV07SAITAK-TAK`) | 0.08 / 0.09 (18241) | 8.5% | 62.2% | 61.1% | 61.1% [60.1%-62.5%] | -- | 39.6% | 39.6% | MODEL_LONE_OUTLIER | WATCH | +53.7 pp | EXTREME (DATA_WARNING) | STALE | B / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 2572.0, B 4105.0; serve-point win A 60.2%, B 37.4%; Elo A 1367.8, B 1454.7; model uncertainty 0.0123
* Form inputs: days since last match A 201, B 159; matches on record A 216, B 551; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV07SAITAK-TAK  (YES = Yusuke Takahashi)
Model: 62%
Kalshi: 8%
Gap: +54 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: SUPPORTS_MODEL_DIRECTION
Data quality: B (LIMITED)
Reasons: STALE_KALSHI_QUOTE, STALE_PLAYER_DATA, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STALE_QUOTE

## Caitlin Baker vs Belle Thompson -- W75 Brisbane R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-08T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259858:263653:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Caitlin Baker (`KXITFWMATCH-26NOV07BAKTHO-BAK`) | 0.46 / 0.47 (15295) | 46.5% | 9.7% | 36.9% | 27.8% [25.2%-30.5%] | -- | -- | -- | -- | PASS | -36.8 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Belle Thompson (`KXITFWMATCH-26NOV07BAKTHO-THO`) | 0.53 / 0.54 (38109) | 53.5% | 90.3% | 63.1% | 72.2% [69.5%-74.8%] | -- | -- | -- | -- | PASS | +36.8 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 160.0, B 1699.0; serve-point win A 48.0%, B 42.3%; Elo A 1140.7, B 1312.7; model uncertainty 0.0268
* Form inputs: days since last match A 250, B 229; matches on record A 26, B 114; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV07BAKTHO-THO  (YES = Belle Thompson)
Model: 90%
Kalshi: 54%
Gap: +37 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.022, surface_pool_high +0.028, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chihiro Muramatsu vs BoYoung Jeong -- W75 Brisbane R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-08T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214540:221109:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BoYoung Jeong (`KXITFWMATCH-26NOV07MURJEO-JEO`) | 0.86 / 0.89 (1) | 87.5% | 74.9% | 89.3% | 79.3% [63.6%-85.2%] | -- | -- | -- | -- | PASS | -12.6 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Chihiro Muramatsu (`KXITFWMATCH-26NOV07MURJEO-MUR`) | 0.11 / 0.13 (0) | 12.0% | 25.1% | 10.7% | 20.7% [14.8%-36.4%] | -- | -- | -- | -- | PASS | +13.1 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1483.0, B 2517.0; serve-point win A 49.5%, B 45.5%; Elo A 1453.5, B 1565.2; model uncertainty 0.108
* Form inputs: days since last match A 307, B 50; matches on record A 418, B 221; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.015, surface_dev_loose -0.022, surface_dev_tight +0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Katie Swan vs Yeonwoo Ku -- W100 Incheon F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV07SWAKUX:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yeonwoo Ku (`KXITFWMATCH-26NOV07SWAKUX-KUX`) | 0.46 / 0.47 (26423) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Katie Swan (`KXITFWMATCH-26NOV07SWAKUX-SWA`) | 0.53 / 0.54 (15054) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yosuke Watanuki vs Jan Kumstat -- ATP Challenger Taipei F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-08T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:133297:211618:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jan Kumstat (`KXATPCHALLENGERMATCH-26NOV08WATKUM-KUM`) | 0.40 / 0.41 (4816) | 40.5% | 54.7% | 63.0% | 53.9% [49.5%-58.8%] | -- | 39.2% | 39.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +14.2 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Yosuke Watanuki (`KXATPCHALLENGERMATCH-26NOV08WATKUM-WAT`) | 0.59 / 0.60 (0) | 59.5% | 45.3% | 37.0% | 46.1% [41.2%-50.5%] | -- | 61.4% | 61.4% | MODEL_LONE_OUTLIER | PASS | -14.2 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3158.0, B 2684.0; serve-point win A 64.6%, B 34.5%; Elo A 1682.9, B 1592.8; model uncertainty 0.0464
* Form inputs: days since last match A 27, B 13; matches on record A 449, B 84; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.049, surface_pool_high +0.044, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Anna Blinkova vs Sofya Lansere -- WTA Challenger Luanda F

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-08 13:00Z
* Current expected start: 2026-11-08 10:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-08 06:39Z
* Recommended handicap-by time: 2026-11-08 09:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (CHALLENGER) · surface ? · scheduled 2026-11-08T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26NOV08BLILAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Blinkova (`KXWTACHALLENGERMATCH-26NOV08BLILAN-BLI`) | 0.73 / 0.74 (8379) | 73.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sofya Lansere (`KXWTACHALLENGERMATCH-26NOV08BLILAN-LAN`) | 0.26 / 0.27 (2290) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Ren Nakamura vs Wang Ziteng -- M15 Hua Hin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV07NAKZIT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ren Nakamura (`KXITFMATCH-26NOV07NAKZIT-NAK`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Wang Ziteng (`KXITFMATCH-26NOV07NAKZIT-ZIT`) | -- / 0.01 (10778) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Guntinun Sootinun-Opart vs Puchit Sukjai -- M15 Hua Hin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV07SOOSUK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Guntinun Sootinun-Opart (`KXITFMATCH-26NOV07SOOSUK-SOO`) | 0.94 / 0.95 (28) | 94.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Puchit Sukjai (`KXITFMATCH-26NOV07SOOSUK-SUK`) | 0.04 / 0.05 (4314) | 4.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tsz Fu Wong vs Baran Soyler -- M15 Hua Hin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-08T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209515:212971:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Baran Soyler (`KXITFMATCH-26NOV07WONSOY-SOY`) | 0.36 / 0.38 (16111) | 37.0% | 70.4% | 75.4% | 69.8% [69.7%-70.8%] | -- | -- | -- | -- | PASS | +33.4 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tsz Fu Wong (`KXITFMATCH-26NOV07WONSOY-WON`) | 0.62 / 0.63 (851) | 62.5% | 29.6% | 24.6% | 30.2% [29.2%-30.3%] | -- | -- | -- | -- | PASS | -32.9 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 498.0, B 112.0; serve-point win A 57.6%, B 38.2%; Elo A 1070.2, B 1214.2; model uncertainty 0.0052
* Form inputs: days since last match A 50, B 320; matches on record A 20, B 11; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV07WONSOY-SOY  (YES = Baran Soyler)
Model: 70%
Kalshi: 37%
Gap: +33 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Naima Karamoko / Simona Waltert vs Vaishnavi Adkar / Rutuja Bhosale -- WTA Chennai F

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-08 13:30Z
* Current expected start: 2026-11-08 10:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-08 06:39Z
* Recommended handicap-by time: 2026-11-08 09:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-08T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV08KARWALADKBHO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vaishnavi Adkar / Rutuja Bhosale (`KXWTADOUBLES-26NOV08KARWALADKBHO-ADKBHO`) | 0.33 / 0.37 (495) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Naima Karamoko / Simona Waltert (`KXWTADOUBLES-26NOV08KARWALADKBHO-KARWAL`) | 0.62 / 0.64 (9) | 63.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Nikoloz Basilashvili vs Borna Gojo -- ATP Stockholm F

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-08 14:00Z
* Current expected start: 2026-11-08 11:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-08 06:39Z
* Recommended handicap-by time: 2026-11-08 10:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-11-08T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105932:127339:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikoloz Basilashvili (`KXATPMATCH-26NOV08BASGOJ-BAS`) | 0.64 / 0.65 (38960) | 64.5% | 50.5% | 46.7% | 47.6% [45.7%-51.4%] | 61.6% | 64.1% | 62.9% | MODEL_LONE_OUTLIER | PASS | -14.0 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Borna Gojo (`KXATPMATCH-26NOV08BASGOJ-GOJ`) | 0.35 / 0.36 (1748) | 35.5% | 49.5% | 53.3% | 52.4% [48.6%-54.3%] | 38.4% | 36.0% | 37.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +14.0 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5168.0, B 3697.0; serve-point win A 68.1%, B 32.0%; Elo A 1762.4, B 1756.9; model uncertainty 0.0285
* Form inputs: days since last match A 1, B 13; matches on record A 970, B 476; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.009, surface_dev_loose +0.010, surface_dev_tight -0.005
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26NOV08BASGOJ-BAS20` Will Nikoloz Basilashvili win the Nikoloz Basilashvili vs Borna Gojo match by a set score of 2-0?: 0.40/0.41 mid 40.5%, model 25.4% (projection_v2.0 (prediction ledger)) -- gap -15.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV08BASGOJ-1-GOJ` Will Borna Gojo win set 1 in the Nikoloz Basilashvili vs Borna Gojo match: 0.39/0.41 mid 40.0%, model 49.6% (projection_v2.0 (prediction ledger)) -- gap +9.7 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV08BASGOJ-2-GOJ` Will Borna Gojo win set 2 in the Nikoloz Basilashvili vs Borna Gojo match: 0.38/0.42 mid 40.0%, model 49.6% (projection_v2.0 (prediction ledger)) -- gap +9.7 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV08BASGOJ-GOJ21` Will Borna Gojo win the Nikoloz Basilashvili vs Borna Gojo match by a set score of 2-1?: 0.14/0.18 mid 16.0%, model 24.8% (projection_v2.0 (prediction ledger)) -- gap +8.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV08BASGOJ-1-BAS` Will Nikoloz Basilashvili win set 1 in the Nikoloz Basilashvili vs Borna Gojo match: 0.58/0.60 mid 59.0%, model 50.3% (projection_v2.0 (prediction ledger)) -- gap -8.7 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV08BASGOJ-2-BAS` Will Nikoloz Basilashvili win set 2 in the Nikoloz Basilashvili vs Borna Gojo match: 0.56/0.60 mid 58.0%, model 50.3% (projection_v2.0 (prediction ledger)) -- gap -7.7 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV08BASGOJ-GOJ20` Will Borna Gojo win the Nikoloz Basilashvili vs Borna Gojo match by a set score of 2-0?: 0.18/0.19 mid 18.5%, model 24.6% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV08BASGOJ-BAS21` Will Nikoloz Basilashvili win the Nikoloz Basilashvili vs Borna Gojo match by a set score of 2-1?: 0.21/0.24 mid 22.5%, model 25.2% (projection_v2.0 (prediction ledger)) -- gap +2.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Inaki Montes-de la Torre vs Lorenzo Sonego -- ATP Stockholm F

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-08 14:00Z
* Current expected start: 2026-11-08 11:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-08 06:39Z
* Recommended handicap-by time: 2026-11-08 10:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-11-08T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:132283:208540:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Inaki Montes-de la Torre (`KXATPMATCH-26NOV08MONSON-MON`) | 0.25 / 0.26 (1100) | 25.5% | 40.9% | 55.0% | 49.0% [43.0%-52.5%] | 27.4% | 26.8% | -- | INSUFFICIENT_INPUTS | WATCH | +15.4 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lorenzo Sonego (`KXATPMATCH-26NOV08MONSON-SON`) | 0.74 / 0.75 (7306) | 74.5% | 59.1% | 45.0% | 51.0% [47.5%-57.0%] | 72.6% | 73.6% | -- | INSUFFICIENT_INPUTS | PASS | -15.4 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4035.0, B 4676.0; serve-point win A 62.1%, B 36.0%; Elo A 1657.2, B 1776.7; model uncertainty 0.0476
* Form inputs: days since last match A 13, B 6; matches on record A 230, B 704; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26NOV08MONSON-MON  (YES = Inaki Montes-de la Torre)
Model: 41%
Kalshi: 26%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight -0.005
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26NOV08MONSON-SON20` Will Lorenzo Sonego win the Inaki Montes-de la Torre vs Lorenzo Sonego match by a set score of 2-0?: 0.49/0.50 mid 49.5%, model 31.4% (projection_v2.0 (prediction ledger)) -- gap -18.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV08MONSON-2-MON` Will Inaki Montes-de la Torre win set 2 in the Inaki Montes-de la Torre vs Lorenzo Sonego match: 0.28/0.33 mid 30.5%, model 43.9% (projection_v2.0 (prediction ledger)) -- gap +13.4 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV08MONSON-2-SON` Will Lorenzo Sonego win set 2 in the Inaki Montes-de la Torre vs Lorenzo Sonego match: 0.66/0.70 mid 68.0%, model 56.1% (projection_v2.0 (prediction ledger)) -- gap -11.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV08MONSON-1-MON` Will Inaki Montes-de la Torre win set 1 in the Inaki Montes-de la Torre vs Lorenzo Sonego match: 0.32/0.34 mid 33.0%, model 43.9% (projection_v2.0 (prediction ledger)) -- gap +10.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV08MONSON-1-SON` Will Lorenzo Sonego win set 1 in the Inaki Montes-de la Torre vs Lorenzo Sonego match: 0.66/0.68 mid 67.0%, model 56.1% (projection_v2.0 (prediction ledger)) -- gap -10.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV08MONSON-MON21` Will Inaki Montes-de la Torre win the Inaki Montes-de la Torre vs Lorenzo Sonego match by a set score of 2-1?: 0.11/0.13 mid 12.0%, model 21.6% (projection_v2.0 (prediction ledger)) -- gap +9.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV08MONSON-MON20` Will Inaki Montes-de la Torre win the Inaki Montes-de la Torre vs Lorenzo Sonego match by a set score of 2-0?: 0.12/0.15 mid 13.5%, model 19.3% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV08MONSON-SON21` Will Lorenzo Sonego win the Inaki Montes-de la Torre vs Lorenzo Sonego match by a set score of 2-1?: 0.23/0.25 mid 24.0%, model 27.6% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Oleksii Krutykh vs Kai Wehnelt -- ATP Challenger Hersonissos Semi F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-08T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132999:208071:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oleksii Krutykh (`KXATPCHALLENGERMATCH-26NOV08KRUWEH-KRU`) | 0.65 / 0.66 (2026) | 65.5% | 71.6% | 62.9% | 65.7% [63.8%-70.3%] | 65.1% | 64.3% | -- | INSUFFICIENT_INPUTS | PASS | +6.1 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kai Wehnelt (`KXATPCHALLENGERMATCH-26NOV08KRUWEH-WEH`) | 0.34 / 0.35 (4137) | 34.5% | 28.4% | 37.1% | 34.3% [29.7%-36.2%] | 34.8% | 35.5% | -- | INSUFFICIENT_INPUTS | PASS | -6.1 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3078.0, B 2278.0; serve-point win A 64.8%, B 39.7%; Elo A 1503.9, B 1358.6; model uncertainty 0.0324
* Form inputs: days since last match A 34, B 27; matches on record A 467, B 412; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.019, surface_dev_loose -0.019, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Digvijay Pratap Singh vs Dmitry Bessonov -- M15 Fergana F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08SINBES:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dmitry Bessonov (`KXITFMATCH-26NOV08SINBES-BES`) | 0.51 / 0.52 (786) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Digvijay Pratap Singh (`KXITFMATCH-26NOV08SINBES-SIN`) | 0.48 / 0.49 (30274) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Natsumi Kawaguchi vs Catherine Aulia -- W75 Brisbane R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-08T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221229:223160:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Catherine Aulia (`KXITFWMATCH-26NOV08KAWAUL-AUL`) | 0.01 / 0.02 (8947) | 1.5% | 28.8% | 31.1% | 33.1% [31.6%-35.5%] | -- | -- | -- | -- | PASS | +27.3 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Natsumi Kawaguchi (`KXITFWMATCH-26NOV08KAWAUL-KAW`) | 0.99 / -- (0) | -- | 71.2% | 68.9% | 67.0% [64.5%-68.5%] | -- | -- | -- | -- | PASS | -- | UNPRICED | STALE | D / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 2084.0, B 286.0; serve-point win A 57.4%, B 46.8%; Elo A 1533.5, B 1418.3; model uncertainty 0.0197
* Form inputs: days since last match A 42, B 327; matches on record A 213, B 47; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV08KAWAUL-AUL  (YES = Catherine Aulia)
Model: 29%
Kalshi: 2%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.024, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hikaru Sato vs Elyse Tse -- W75 Brisbane R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-08T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221141:223163:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hikaru Sato (`KXITFWMATCH-26NOV08SATTSE-SAT`) | 0.62 / 0.64 (15) | 63.0% | 71.5% | 56.2% | 64.8% [62.3%-67.6%] | -- | -- | -- | -- | PASS | +8.5 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elyse Tse (`KXITFWMATCH-26NOV08SATTSE-TSE`) | 0.35 / 0.36 (4) | 35.5% | 28.5% | 43.8% | 35.2% [32.4%-37.7%] | -- | -- | -- | -- | PASS | -7.0 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1807.0, B 1193.0; serve-point win A 60.5%, B 43.9%; Elo A 1465.8, B 1308.3; model uncertainty 0.0266
* Form inputs: days since last match A 201, B 194; matches on record A 175, B 59; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.014, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Quentin Halys / Pierre-Hugues Herbert vs Christian Harrison / Neal Skupski -- ATP Paris F

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-08 14:30Z
* Current expected start: 2026-11-08 11:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-08 06:39Z
* Recommended handicap-by time: 2026-11-08 10:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-08T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08HALHERHARSKU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Quentin Halys / Pierre-Hugues Herbert (`KXATPDOUBLES-26NOV08HALHERHARSKU-HALHER`) | 0.46 / 0.47 (69) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Christian Harrison / Neal Skupski (`KXATPDOUBLES-26NOV08HALHERHARSKU-HARSKU`) | 0.53 / 0.55 (82) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Vraj Gohil vs Khomtat Kitthachok -- M15 Hua Hin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08GOHKIT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vraj Gohil (`KXITFMATCH-26NOV08GOHKIT-GOH`) | 0.68 / 0.69 (0) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Khomtat Kitthachok (`KXITFMATCH-26NOV08GOHKIT-KIT`) | 0.29 / 0.31 (100) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hendrik Thada Grohbruegge vs Zitawe Kulphisanrat -- M15 Hua Hin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08GROKUL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hendrik Thada Grohbruegge (`KXITFMATCH-26NOV08GROKUL-GRO`) | 0.76 / 0.81 (15) | 78.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Zitawe Kulphisanrat (`KXITFMATCH-26NOV08GROKUL-KUL`) | 0.16 / 0.24 (33) | 20.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Max Houkes vs Robin Catry -- ATP Challenger Orleans Semi F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-08T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208069:210714:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Robin Catry (`KXATPCHALLENGERMATCH-26NOV08HOUCAT-CAT`) | 0.38 / 0.40 (3137) | 39.0% | 35.4% | 29.5% | 35.8% [31.2%-40.6%] | 40.1% | 40.8% | 40.5% | MODEL_LONE_OUTLIER | PASS | -3.5 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Max Houkes (`KXATPCHALLENGERMATCH-26NOV08HOUCAT-HOU`) | 0.60 / 0.62 (4053) | 61.0% | 64.5% | 70.5% | 64.2% [59.4%-68.8%] | 59.9% | 61.0% | 60.5% | MODEL_LONE_OUTLIER | WATCH | +3.5 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4345.0, B 2266.0; serve-point win A 64.9%, B 38.0%; Elo A 1480.4, B 1453.8; model uncertainty 0.0467
* Form inputs: days since last match A 20, B 13; matches on record A 407, B 118; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.046, surface_pool_high -0.048, surface_dev_loose +0.009, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Ryu Kotikula vs Penn Charusorn -- M15 Hua Hin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08KOTCHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Penn Charusorn (`KXITFMATCH-26NOV08KOTCHA-CHA`) | 0.69 / 0.71 (33) | 70.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ryu Kotikula (`KXITFMATCH-26NOV08KOTCHA-KOT`) | 0.25 / 0.31 (7) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tawan Rattaseri vs Rishabhdev Rajshekar Raman -- M15 Hua Hin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08RATRAJ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rishabhdev Rajshekar Raman (`KXITFMATCH-26NOV08RATRAJ-RAJ`) | 0.68 / 0.69 (10) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tawan Rattaseri (`KXITFMATCH-26NOV08RATRAJ-RAT`) | 0.29 / 0.31 (3) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Adrian Mannarino vs Toby Samuel -- ATP Stockholm F

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-08 15:30Z
* Current expected start: 2026-11-08 12:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-08 06:39Z
* Recommended handicap-by time: 2026-11-08 11:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-11-08T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105173:210389:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Mannarino (`KXATPMATCH-26NOV08MANSAM-MAN`) | 0.50 / 0.51 (1124) | 50.5% | 36.2% | 19.6% | 26.4% [22.1%-33.0%] | 50.0% | 51.2% | 50.6% | MODEL_LONE_OUTLIER | PASS | -14.3 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Toby Samuel (`KXATPMATCH-26NOV08MANSAM-SAM`) | 0.49 / 0.50 (5927) | 49.5% | 63.8% | 80.4% | 73.6% [67.0%-77.9%] | 50.0% | 48.6% | 49.3% | MODEL_LONE_OUTLIER | WATCH | +14.3 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5623.0, B 4065.0; serve-point win A 61.5%, B 35.7%; Elo A 1799.9, B 1801.0; model uncertainty 0.0543
* Form inputs: days since last match A 8, B 13; matches on record A 1325, B 192; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.016, surface_dev_tight +0.021
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26NOV08MANSAM-MAN20` Will Adrian Mannarino win the Adrian Mannarino vs Toby Samuel match by a set score of 2-0?: 0.28/0.31 mid 29.5%, model 16.6% (projection_v2.0 (prediction ledger)) -- gap -12.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV08MANSAM-2-SAM` Will Toby Samuel win set 2 in the Adrian Mannarino vs Toby Samuel match: 0.47/0.52 mid 49.5%, model 59.3% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV08MANSAM-SAM21` Will Toby Samuel win the Adrian Mannarino vs Toby Samuel match by a set score of 2-1?: 0.19/0.20 mid 19.5%, model 28.6% (projection_v2.0 (prediction ledger)) -- gap +9.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV08MANSAM-1-SAM` Will Toby Samuel win set 1 in the Adrian Mannarino vs Toby Samuel match: 0.49/0.52 mid 50.5%, model 59.3% (projection_v2.0 (prediction ledger)) -- gap +8.8 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV08MANSAM-1-MAN` Will Adrian Mannarino win set 1 in the Adrian Mannarino vs Toby Samuel match: 0.48/0.50 mid 49.0%, model 40.7% (projection_v2.0 (prediction ledger)) -- gap -8.3 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV08MANSAM-2-MAN` Will Adrian Mannarino win set 2 in the Adrian Mannarino vs Toby Samuel match: 0.47/0.50 mid 48.5%, model 40.7% (projection_v2.0 (prediction ledger)) -- gap -7.8 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV08MANSAM-SAM20` Will Toby Samuel win the Adrian Mannarino vs Toby Samuel match by a set score of 2-0?: 0.28/0.29 mid 28.5%, model 35.1% (projection_v2.0 (prediction ledger)) -- gap +6.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV08MANSAM-MAN21` Will Adrian Mannarino win the Adrian Mannarino vs Toby Samuel match by a set score of 2-1?: 0.19/0.22 mid 20.5%, model 19.7% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Janice Tjen vs Magda Linette -- WTA Chennai F

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-08 16:00Z
* Current expected start: 2026-11-08 13:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-08 06:39Z
* Recommended handicap-by time: 2026-11-08 12:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-11-08T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202663:222145:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Magda Linette (`KXWTAMATCH-26NOV08TJELIN-LIN`) | 0.35 / 0.36 (39147) | 35.5% | 42.3% | 23.5% | 29.7% [25.1%-43.4%] | 34.2% | 34.9% | 34.9% | MODEL_LONE_OUTLIER | PASS | +6.8 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Janice Tjen (`KXWTAMATCH-26NOV08TJELIN-TJE`) | 0.65 / 0.66 (2985) | 65.5% | 57.7% | 76.5% | 70.3% [56.6%-74.9%] | 65.8% | 65.0% | 65.0% | MARKETS_AGREE | WATCH | -7.8 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3631.0, B 4278.0; serve-point win A 62.9%, B 38.6%; Elo A 1902.1, B 1881.7; model uncertainty 0.0912
* Form inputs: days since last match A 2, B 2; matches on record A 189, B 916; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose +0.004, surface_dev_tight +0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV08TJELIN-21` Over 20.5 games: 0.55/0.56 mid 55.5%, model 71.9% (projection_v2.0 (prediction ledger)) -- gap +16.4 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV08TJELIN-26` Over 25.5 games: 0.33/0.35 mid 34.0%, model 48.0% (projection_v2.0 (prediction ledger)) -- gap +14.0 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV08TJELIN-1-LIN` Will Magda Linette win set 1 in the Janice Tjen vs Magda Linette match: 0.35/0.36 mid 35.5%, model 44.8% (projection_v2.0 (prediction ledger)) -- gap +9.3 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV08TJELIN-1-TJE` Will Janice Tjen win set 1 in the Janice Tjen vs Magda Linette match: 0.63/0.65 mid 64.0%, model 55.2% (projection_v2.0 (prediction ledger)) -- gap -8.8 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26NOV08TJELIN-16` Over 15.5 games: 0.88/0.93 mid 90.5%, model 98.7% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV08TJELIN-2-LIN` Will Magda Linette win set 2 in the Janice Tjen vs Magda Linette match: 0.35/0.40 mid 37.5%, model 44.8% (projection_v2.0 (prediction ledger)) -- gap +7.3 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV08TJELIN-2-TJE` Will Janice Tjen win set 2 in the Janice Tjen vs Magda Linette match: 0.60/0.62 mid 61.0%, model 55.2% (projection_v2.0 (prediction ledger)) -- gap -5.8 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Kilian Feldbausch vs Matteo Martineau -- ATP Challenger Taranto F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-08T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200188:210005:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kilian Feldbausch (`KXATPCHALLENGERMATCH-26NOV08FELMAR-FEL`) | 0.58 / 0.60 (11719) | 59.0% | 64.7% | 69.7% | 65.6% [61.7%-68.4%] | 58.4% | 58.6% | -- | INSUFFICIENT_INPUTS | WATCH | +5.7 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matteo Martineau (`KXATPCHALLENGERMATCH-26NOV08FELMAR-MAR`) | 0.41 / 0.42 (11620) | 41.5% | 35.3% | 30.3% | 34.4% [31.6%-38.4%] | 41.6% | 41.3% | -- | INSUFFICIENT_INPUTS | PASS | -6.2 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3610.0, B 5600.0; serve-point win A 61.6%, B 41.3%; Elo A 1692.9, B 1658.7; model uncertainty 0.0337
* Form inputs: days since last match A 13, B 13; matches on record A 190, B 584; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Filip Cristian Jianu vs Mattia Nannelli -- M15 Antalya F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-08T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202262:213617:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Filip Cristian Jianu (`KXITFMATCH-26NOV08JIANAN-JIA`) | 0.83 / 0.85 (224) | 84.0% | 91.8% | 83.8% | 87.6% [87.0%-88.4%] | -- | -- | -- | -- | PASS | +7.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mattia Nannelli (`KXITFMATCH-26NOV08JIANAN-NAN`) | 0.14 / 0.16 (124) | 15.0% | 8.2% | 16.2% | 12.4% [11.6%-13.0%] | -- | -- | -- | -- | PASS | -6.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4620.0, B 425.0; serve-point win A 64.5%, B 46.2%; Elo A 1563.0, B 1206.3; model uncertainty 0.0069
* Form inputs: days since last match A 20, B 258; matches on record A 612, B 9; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.003, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valeriia Iushchenko vs Jana Bojovic -- W15 Antalya F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV08IUSBOJ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jana Bojovic (`KXITFWMATCH-26NOV08IUSBOJ-BOJ`) | 0.24 / 0.25 (33) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Valeriia Iushchenko (`KXITFWMATCH-26NOV08IUSBOJ-IUS`) | 0.72 / 0.73 (4) | 72.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniele Augenti vs Felix Romeo -- M15 Antalya R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08AUGROM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniele Augenti (`KXITFMATCH-26NOV08AUGROM-AUG`) | 0.17 / 0.18 (16) | 17.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Felix Romeo (`KXITFMATCH-26NOV08AUGROM-ROM`) | 0.81 / 0.85 (20) | 83.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Max Benaim vs Ari Feig -- M15 Hua Hin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08BENFEI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Max Benaim (`KXITFMATCH-26NOV08BENFEI-BEN`) | 0.88 / 0.90 (262) | 89.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ari Feig (`KXITFMATCH-26NOV08BENFEI-FEI`) | 0.11 / 0.13 (229) | 12.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eduardo Ecker vs Alexandru Constantin -- M15 Antalya R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08ECKCON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandru Constantin (`KXITFMATCH-26NOV08ECKCON-CON`) | 0.48 / 0.61 (6) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eduardo Ecker (`KXITFMATCH-26NOV08ECKCON-ECK`) | 0.37 / 0.48 (6) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nathan Fekadu vs Vitek Horak -- M15 Hua Hin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08FEKHOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nathan Fekadu (`KXITFMATCH-26NOV08FEKHOR-FEK`) | 0.24 / 0.27 (104) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vitek Horak (`KXITFMATCH-26NOV08FEKHOR-HOR`) | 0.70 / 0.75 (225) | 72.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jakov Frankovic vs Keanu Elias Immler -- M15 Antalya R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08FRAIMM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jakov Frankovic (`KXITFMATCH-26NOV08FRAIMM-FRA`) | 0.39 / 0.56 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Keanu Elias Immler (`KXITFMATCH-26NOV08FRAIMM-IMM`) | 0.43 / 0.60 (41) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hong-Lin Fu vs Teerapat Khantiweerawat -- M15 Hua Hin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-08T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207748:212209:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hong-Lin Fu (`KXITFMATCH-26NOV08FUXKHA-FUX`) | 0.77 / 0.78 (252) | 77.5% | 57.3% | 69.4% | 49.0% [45.9%-53.1%] | -- | -- | -- | -- | PASS | -20.2 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Teerapat Khantiweerawat (`KXITFMATCH-26NOV08FUXKHA-KHA`) | 0.20 / 0.23 (149) | 21.5% | 42.7% | 30.6% | 51.0% [46.9%-54.1%] | -- | -- | -- | -- | PASS | +21.2 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 214.0, B 197.0; serve-point win A 60.0%, B 41.4%; Elo A 1068.3, B 1095.3; model uncertainty 0.0362
* Form inputs: days since last match A 370, B 377; matches on record A 24, B 6; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV08FUXKHA-KHA  (YES = Teerapat Khantiweerawat)
Model: 43%
Kalshi: 22%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Buvaysar Gadamauri vs Vadym Ursu -- ATP Challenger Orleans Semi F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 13:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-08T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:134068:207527:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Buvaysar Gadamauri (`KXATPCHALLENGERMATCH-26NOV08GADURS-GAD`) | 0.73 / 0.75 (42) | 74.0% | 69.2% | 69.7% | 68.3% [66.0%-71.0%] | -- | 72.3% | -- | INSUFFICIENT_INPUTS | PASS | -4.8 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Vadym Ursu (`KXATPCHALLENGERMATCH-26NOV08GADURS-URS`) | 0.25 / 0.27 (12) | 26.0% | 30.8% | 30.3% | 31.7% [29.0%-34.0%] | -- | 27.5% | -- | INSUFFICIENT_INPUTS | WATCH | +4.8 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4560.0, B 3850.0; serve-point win A 62.4%, B 41.5%; Elo A 1574.5, B 1465.1; model uncertainty 0.0251
* Form inputs: days since last match A 27, B 48; matches on record A 312, B 441; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.027, surface_pool_high -0.023, surface_dev_loose +0.009, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Aditya Kothari vs Pitchayapong Soponpisut -- M15 Hua Hin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08KOTSOP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aditya Kothari (`KXITFMATCH-26NOV08KOTSOP-KOT`) | 0.70 / 0.71 (5) | 70.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pitchayapong Soponpisut (`KXITFMATCH-26NOV08KOTSOP-SOP`) | 0.24 / 0.31 (15) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rares Ioan Poiana vs Utku Kerem Biberli -- M15 Antalya R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08POIBIB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Utku Kerem Biberli (`KXITFMATCH-26NOV08POIBIB-BIB`) | 0.63 / 0.75 (6) | 69.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rares Ioan Poiana (`KXITFMATCH-26NOV08POIBIB-POI`) | 0.27 / 0.33 (124) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valentin Vanta vs Jonah Haidarian -- M15 Antalya R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08VANHAI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jonah Haidarian (`KXITFMATCH-26NOV08VANHAI-HAI`) | 0.06 / 0.08 (29) | 7.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Valentin Vanta (`KXITFMATCH-26NOV08VANHAI-VAN`) | 0.94 / 0.95 (301) | 94.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexander Wagner vs Fabio Luis Guth -- M15 Antalya R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-08T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213138:214412:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fabio Luis Guth (`KXITFMATCH-26NOV08WAGGUT-GUT`) | 0.07 / 0.14 (51) | 10.5% | 50.8% | 67.8% | 61.5% [61.3%-63.0%] | -- | -- | -- | -- | PASS | +40.3 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexander Wagner (`KXITFMATCH-26NOV08WAGGUT-WAG`) | 0.86 / 0.91 (10) | 88.5% | 49.2% | 32.2% | 38.6% [37.0%-38.7%] | -- | -- | -- | -- | PASS | -39.3 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 861.0, B 104.0; serve-point win A 56.5%, B 43.4%; Elo A 1196.5, B 1277.6; model uncertainty 0.0085
* Form inputs: days since last match A 195, B 279; matches on record A 22, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV08WAGGUT-GUT  (YES = Fabio Luis Guth)
Model: 51%
Kalshi: 10%
Gap: +40 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## N. Sriram Balaji / Evan King vs Sander Arends / Luke Johnson -- ATP Stockholm 1/8 F

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-08 17:00Z
* Current expected start: 2026-11-08 14:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-08 06:39Z
* Recommended handicap-by time: 2026-11-08 13:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-08T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08BALKINAREJOH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sander Arends / Luke Johnson (`KXATPDOUBLES-26NOV08BALKINAREJOH-AREJOH`) | 0.54 / 0.57 (90) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| N. Sriram Balaji / Evan King (`KXATPDOUBLES-26NOV08BALKINAREJOH-BALKIN`) | 0.42 / 0.45 (40) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Ben Shelton vs Carlos Alcaraz -- ATP Paris F

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-08 17:00Z
* Current expected start: 2026-11-08 14:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-08 06:39Z
* Recommended handicap-by time: 2026-11-08 13:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-11-08T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207989:210097:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlos Alcaraz (`KXATPMATCH-26NOV08SHEALC-ALC`) | 0.76 / 0.77 (1005) | 76.5% | 78.3% | 78.8% | 78.1% [75.5%-80.1%] | 76.2% | 76.7% | 76.4% | MODEL_LONE_OUTLIER | PASS | +1.8 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Ben Shelton (`KXATPMATCH-26NOV08SHEALC-SHE`) | 0.23 / 0.24 (212203) | 23.5% | 21.7% | 21.2% | 21.9% [19.9%-24.5%] | 23.8% | 23.3% | 23.5% | MODEL_LONE_OUTLIER | PASS | -1.8 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 6486.0, B 5572.0; serve-point win A 63.6%, B 30.0%; Elo A 2082.5, B 2273.2; model uncertainty 0.0234
* Form inputs: days since last match A 2, B 2; matches on record A 320, B 483; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.026, surface_dev_loose +0.004, surface_dev_tight -0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26NOV08SHEALC-ALC21` Will Carlos Alcaraz win the Ben Shelton vs Carlos Alcaraz match by a set score of 2-1?: 0.23/0.24 mid 23.5%, model 29.4% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV08SHEALC-ALC20` Will Carlos Alcaraz win the Ben Shelton vs Carlos Alcaraz match by a set score of 2-0?: 0.53/0.54 mid 53.5%, model 48.9% (projection_v2.0 (prediction ledger)) -- gap -4.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV08SHEALC-24` Over 23.5 games: 0.44/0.45 mid 44.5%, model 48.4% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV08SHEALC-29` Over 28.5 games: 0.30/0.31 mid 30.5%, model 32.9% (projection_v2.0 (prediction ledger)) -- gap +2.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV08SHEALC-19` Over 18.5 games: 0.89/0.90 mid 89.5%, model 87.2% (projection_v2.0 (prediction ledger)) -- gap -2.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV08SHEALC-SHE21` Will Ben Shelton win the Ben Shelton vs Carlos Alcaraz match by a set score of 2-1?: 0.11/0.19 mid 15.0%, model 12.7% (projection_v2.0 (prediction ledger)) -- gap -2.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV08SHEALC-1-ALC` Will Carlos Alcaraz win set 1 in the Ben Shelton vs Carlos Alcaraz match: 0.71/0.73 mid 72.0%, model 69.9% (projection_v2.0 (prediction ledger)) -- gap -2.1 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV08SHEALC-ALC4` Will Carlos Alcaraz win at least 3.5 more games than Ben Shelton?: 0.50/0.51 mid 50.5%, model 48.6% (projection_v2.0 (prediction ledger)) -- gap -1.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV08SHEALC-ALC7` Will Carlos Alcaraz win at least 6.5 more games than Ben Shelton?: 0.06/0.14 mid 10.0%, model 8.3% (projection_v2.0 (prediction ledger)) -- gap -1.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV08SHEALC-1-SHE` Will Ben Shelton win set 1 in the Ben Shelton vs Carlos Alcaraz match: 0.28/0.29 mid 28.5%, model 30.1% (projection_v2.0 (prediction ledger)) -- gap +1.6 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV08SHEALC-2-SHE` Will Ben Shelton win set 2 in the Ben Shelton vs Carlos Alcaraz match: 0.27/0.30 mid 28.5%, model 30.1% (projection_v2.0 (prediction ledger)) -- gap +1.6 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV08SHEALC-2-ALC` Will Carlos Alcaraz win set 2 in the Ben Shelton vs Carlos Alcaraz match: 0.70/0.72 mid 71.0%, model 69.9% (projection_v2.0 (prediction ledger)) -- gap -1.1 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV08SHEALC-SHE2` Will Ben Shelton win at least 1.5 more games than Carlos Alcaraz?: 0.16/0.18 mid 17.0%, model 16.1% (projection_v2.0 (prediction ledger)) -- gap -0.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV08SHEALC-SHE20` Will Ben Shelton win the Ben Shelton vs Carlos Alcaraz match by a set score of 2-0?: 0.08/0.09 mid 8.5%, model 9.1% (projection_v2.0 (prediction ledger)) -- gap +0.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Gilles Arnaud Bailly vs Cezar Cretu -- M25 Heraklion F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-08T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206470:211451:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gilles Arnaud Bailly (`KXITFMATCH-26NOV08BAICRE-BAI`) | 0.46 / 0.47 (205) | 46.5% | 45.5% | 39.6% | 44.2% [42.1%-46.8%] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.0 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Cezar Cretu (`KXITFMATCH-26NOV08BAICRE-CRE`) | 0.53 / 0.54 (119) | 53.5% | 54.5% | 60.4% | 55.8% [53.2%-57.9%] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.0 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3897.0, B 4025.0; serve-point win A 56.3%, B 42.9%; Elo A 1517.4, B 1482.5; model uncertainty 0.0235
* Form inputs: days since last match A 22, B 27; matches on record A 212, B 422; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.011, surface_dev_loose +0.016, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gabi Adrian Boitan vs Alexandre Reco -- ATP Challenger Hersonissos Semi F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-08T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206589:209258:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabi Adrian Boitan (`KXATPCHALLENGERMATCH-26NOV08BOIREC-BOI`) | 0.70 / 0.71 (176) | 70.5% | 71.3% | 76.8% | 72.4% [68.0%-76.8%] | 70.6% | 69.9% | -- | INSUFFICIENT_INPUTS | PASS | +0.8 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexandre Reco (`KXATPCHALLENGERMATCH-26NOV08BOIREC-REC`) | 0.29 / 0.30 (3414) | 29.5% | 28.7% | 23.2% | 27.6% [23.2%-32.0%] | 29.4% | 29.8% | -- | INSUFFICIENT_INPUTS | PASS | -0.8 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3451.0, B 920.0; serve-point win A 64.9%, B 39.5%; Elo A 1455.7, B 1310.7; model uncertainty 0.044
* Form inputs: days since last match A 62, B 41; matches on record A 319, B 112; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.044, surface_pool_high -0.044, surface_dev_loose -0.001, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Nicolas Ifi vs Omar Kandil -- M15 Sharm ElSheikh F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-08T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212552:214191:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Ifi (`KXITFMATCH-26NOV08IFIKAN-IFI`) | 0.66 / 0.68 (189) | 67.0% | 52.6% | 36.2% | 46.0% [44.9%-47.0%] | -- | -- | -- | -- | PASS | -14.3 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Omar Kandil (`KXITFMATCH-26NOV08IFIKAN-KAN`) | 0.33 / 0.34 (139) | 33.5% | 47.3% | 63.8% | 54.0% [53.0%-55.1%] | -- | -- | -- | -- | PASS | +13.8 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1814.0, B 45.0; serve-point win A 63.5%, B 37.1%; Elo A 1220.4, B 1251.2; model uncertainty 0.0103
* Form inputs: days since last match A 202, B 50; matches on record A 75, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yasmin Ezzat vs Karla Popovic -- W15 Sharm ElSheikh F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-08T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:210500:221474:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yasmin Ezzat (`KXITFWMATCH-26NOV08EZZPOP-EZZ`) | 0.46 / 0.49 (3) | 47.5% | 36.9% | 21.9% | 32.9% [26.9%-42.0%] | -- | -- | -- | -- | PASS | -10.7 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Karla Popovic (`KXITFWMATCH-26NOV08EZZPOP-POP`) | 0.51 / 0.53 (165) | 52.0% | 63.1% | 78.1% | 67.1% [58.0%-73.1%] | -- | -- | -- | -- | WATCH | +11.2 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2756.0, B 1204.0; serve-point win A 51.9%, B 45.6%; Elo A 1399.1, B 1454.1; model uncertainty 0.0758
* Form inputs: days since last match A 202, B 195; matches on record A 271, B 82; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose -0.010, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Martha Matoula vs Raluca Georgiana Serban -- W50 Heraklion F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV08MATSER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martha Matoula (`KXITFWMATCH-26NOV08MATSER-MAT`) | 0.49 / 0.51 (289) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Raluca Georgiana Serban (`KXITFWMATCH-26NOV08MATSER-SER`) | 0.49 / 0.50 (174) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ilham Bakhshaliev vs Mircea Mortasifu -- M15 Antalya R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08BAKMOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ilham Bakhshaliev (`KXITFMATCH-26NOV08BAKMOR-BAK`) | 0.15 / 0.32 (6) | 23.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mircea Mortasifu (`KXITFMATCH-26NOV08BAKMOR-MOR`) | 0.64 / 0.85 (6) | 74.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alessandro Bellifemine vs Luca Stefan Prunescu Nita -- M15 Antalya R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08BELPRU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alessandro Bellifemine (`KXITFMATCH-26NOV08BELPRU-BEL`) | 0.87 / 0.90 (60) | 88.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luca Stefan Prunescu Nita (`KXITFMATCH-26NOV08BELPRU-PRU`) | 0.08 / 0.16 (2) | 12.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexander Brown vs Cezar Stefan Bentzel -- M15 Antalya R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-08T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200230:213855:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cezar Stefan Bentzel (`KXITFMATCH-26NOV08BROBEN-BEN`) | 0.85 / 0.92 (44) | 88.5% | 41.9% | 28.1% | 35.9% [33.7%-36.8%] | -- | -- | -- | -- | PASS | -46.6 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexander Brown (`KXITFMATCH-26NOV08BROBEN-BRO`) | 0.06 / 0.10 (0) | 8.0% | 58.1% | 71.9% | 64.1% [63.2%-66.3%] | -- | -- | -- | -- | PASS | +50.1 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 191.0, B 390.0; serve-point win A 61.3%, B 40.3%; Elo A 1220.7, B 1125.9; model uncertainty 0.0156
* Form inputs: days since last match A 713, B 335; matches on record A 56, B 6; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV08BROBEN-BRO  (YES = Alexander Brown)
Model: 58%
Kalshi: 8%
Gap: +50 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.010, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Raffael Gasanov vs Jakub Januchowski -- M15 Antalya R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08GASJAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raffael Gasanov (`KXITFMATCH-26NOV08GASJAN-GAS`) | 0.32 / 0.33 (6) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jakub Januchowski (`KXITFMATCH-26NOV08GASJAN-JAN`) | 0.63 / 0.72 (5) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anton Kartsev vs Andrea Brignacca -- M15 Antalya R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08KARBRI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrea Brignacca (`KXITFMATCH-26NOV08KARBRI-BRI`) | 0.57 / 0.72 (101) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anton Kartsev (`KXITFMATCH-26NOV08KARBRI-KAR`) | 0.29 / 0.32 (16) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gokberk Saritas vs Matei Marius Partal -- M15 Antalya R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08SARPAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matei Marius Partal (`KXITFMATCH-26NOV08SARPAR-PAR`) | 0.41 / 0.48 (1) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gokberk Saritas (`KXITFMATCH-26NOV08SARPAR-SAR`) | 0.54 / 0.59 (6) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elias Ymer vs Juan Manuel Cerundolo -- ATP Stockholm 1/16 F

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-08 18:00Z
* Current expected start: 2026-11-08 15:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-08 06:39Z
* Recommended handicap-by time: 2026-11-08 14:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-11-08T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111200:207678:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Manuel Cerundolo (`KXATPMATCH-26NOV08YMECER-CER`) | 0.75 / 0.77 (7649) | 76.0% | 74.4% | 62.1% | 63.9% [62.4%-65.7%] | 74.5% | 75.5% | 75.0% | MODEL_LONE_OUTLIER | PASS | -1.6 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Elias Ymer (`KXATPMATCH-26NOV08YMECER-YME`) | 0.23 / 0.24 (378) | 23.5% | 25.6% | 38.0% | 36.1% [34.3%-37.6%] | 25.5% | 24.4% | 25.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +2.1 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4820.0, B 6194.0; serve-point win A 62.9%, B 31.8%; Elo A 1600.6, B 1747.6; model uncertainty 0.0166
* Form inputs: days since last match A 13, B 6; matches on record A 822, B 548; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose +0.015, surface_dev_tight -0.015
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26NOV08YMECER-CER7` Will Juan Manuel Cerundolo win at least 6.5 more games than Elias Ymer?: 0.06/0.34 mid 20.0%, model 8.5% (projection_v2.0 (prediction ledger)) -- gap -11.6 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV08YMECER-22` Over 21.5 games: 0.55/0.57 mid 56.0%, model 65.9% (projection_v2.0 (prediction ledger)) -- gap +9.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV08YMECER-CER4` Will Juan Manuel Cerundolo win at least 3.5 more games than Elias Ymer?: 0.53/0.55 mid 54.0%, model 46.2% (projection_v2.0 (prediction ledger)) -- gap -7.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV08YMECER-CER20` Will Juan Manuel Cerundolo win the Elias Ymer vs Juan Manuel Cerundolo match by a set score of 2-0?: 0.50/0.55 mid 52.5%, model 44.8% (projection_v2.0 (prediction ledger)) -- gap -7.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV08YMECER-27` Over 26.5 games: 0.33/0.34 mid 33.5%, model 40.3% (projection_v2.0 (prediction ledger)) -- gap +6.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV08YMECER-CER21` Will Juan Manuel Cerundolo win the Elias Ymer vs Juan Manuel Cerundolo match by a set score of 2-1?: 0.22/0.25 mid 23.5%, model 29.6% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV08YMECER-17` Over 16.5 games: 0.91/0.94 mid 92.5%, model 97.1% (projection_v2.0 (prediction ledger)) -- gap +4.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV08YMECER-2-YME` Will Elias Ymer win set 2 in the Elias Ymer vs Juan Manuel Cerundolo match: 0.27/0.31 mid 29.0%, model 33.1% (projection_v2.0 (prediction ledger)) -- gap +4.1 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV08YMECER-YME21` Will Elias Ymer win the Elias Ymer vs Juan Manuel Cerundolo match by a set score of 2-1?: 0.10/0.13 mid 11.5%, model 14.6% (projection_v2.0 (prediction ledger)) -- gap +3.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV08YMECER-2-CER` Will Juan Manuel Cerundolo win set 2 in the Elias Ymer vs Juan Manuel Cerundolo match: 0.68/0.72 mid 70.0%, model 66.9% (projection_v2.0 (prediction ledger)) -- gap -3.1 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV08YMECER-1-YME` Will Elias Ymer win set 1 in the Elias Ymer vs Juan Manuel Cerundolo match: 0.30/0.33 mid 31.5%, model 33.1% (projection_v2.0 (prediction ledger)) -- gap +1.6 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV08YMECER-YME20` Will Elias Ymer win the Elias Ymer vs Juan Manuel Cerundolo match by a set score of 2-0?: 0.11/0.14 mid 12.5%, model 10.9% (projection_v2.0 (prediction ledger)) -- gap -1.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV08YMECER-1-CER` Will Juan Manuel Cerundolo win set 1 in the Elias Ymer vs Juan Manuel Cerundolo match: 0.67/0.69 mid 68.0%, model 66.9% (projection_v2.0 (prediction ledger)) -- gap -1.1 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV08YMECER-YME2` Will Elias Ymer win at least 1.5 more games than Juan Manuel Cerundolo?: 0.18/0.20 mid 19.0%, model 19.6% (projection_v2.0 (prediction ledger)) -- gap +0.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STALE_QUOTE; WIDE_SPREAD

## Alejandro Moro Canas vs Wissam Abderrahman -- M15 Monastir F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-08T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208279:210230:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wissam Abderrahman (`KXITFMATCH-26NOV08MORABD-ABD`) | 0.19 / 0.21 (124) | 20.0% | 5.9% | 15.7% | 9.9% [7.2%-11.8%] | 21.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -14.1 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alejandro Moro Canas (`KXITFMATCH-26NOV08MORABD-MOR`) | 0.78 / 0.79 (54) | 78.5% | 94.1% | 84.3% | 90.1% [88.2%-92.8%] | 78.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +15.6 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5775.0, B 236.0; serve-point win A 66.0%, B 46.2%; Elo A 1635.1, B 1233.2; model uncertainty 0.023
* Form inputs: days since last match A 20, B 468; matches on record A 362, B 75; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV08MORABD-MOR  (YES = Alejandro Moro Canas)
Model: 94%
Kalshi: 78%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.017, surface_pool_high -0.019, surface_dev_loose +0.004, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cosme Rolland de Ravel vs Norbert Gombos -- ATP Challenger Orleans Semi F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-08T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105613:213977:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Norbert Gombos (`KXATPCHALLENGERMATCH-26NOV08ROLGOM-GOM`) | 0.48 / 0.49 (20) | 48.5% | 48.9% | 45.5% | 57.5% [50.5%-63.8%] | 49.0% | 50.0% | -- | INSUFFICIENT_INPUTS | PASS | +0.4 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Cosme Rolland de Ravel (`KXATPCHALLENGERMATCH-26NOV08ROLGOM-ROL`) | 0.50 / 0.52 (1998) | 51.0% | 51.1% | 54.5% | 42.5% [36.1%-49.5%] | 51.0% | 50.0% | -- | INSUFFICIENT_INPUTS | PASS | +0.1 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 625.0, B 4496.0; serve-point win A 62.9%, B 37.3%; Elo A 1508.9, B 1595.8; model uncertainty 0.0667
* Form inputs: days since last match A 20, B 27; matches on record A 14, B 1035; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.034, surface_pool_high +0.030, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Capucine Cedillo- Vayson de Pradenne vs Emma Mazzoni -- W15 Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-08T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220790:266808:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Capucine Cedillo- Vayson de Pradenne (`KXITFWMATCH-26NOV08CEDMAZ-CED`) | 0.78 / 0.79 (51) | 78.5% | 68.5% | 79.2% | 72.2% [71.3%-73.1%] | -- | -- | -- | -- | PASS | -10.0 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Emma Mazzoni (`KXITFWMATCH-26NOV08CEDMAZ-MAZ`) | 0.18 / 0.20 (43) | 19.0% | 31.5% | 20.8% | 27.8% [26.9%-28.7%] | -- | -- | -- | -- | PASS | +12.5 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 168.0; serve-point win A 55.4%, B 48.2%; Elo A 1216.2, B 1049.4; model uncertainty 0.009
* Form inputs: days since last match A 965, B 195; matches on record A 2, B 135; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mariia Lazarenko vs Anastasia Lizunova -- W15 Monastir F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV08LAZLIZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mariia Lazarenko (`KXITFWMATCH-26NOV08LAZLIZ-LAZ`) | 0.61 / 0.62 (770) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anastasia Lizunova (`KXITFWMATCH-26NOV08LAZLIZ-LIZ`) | 0.38 / 0.40 (154) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stefaniya Pushkar vs Charline Bressan -- W15 Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV08PUSBRE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charline Bressan (`KXITFWMATCH-26NOV08PUSBRE-BRE`) | 0.26 / 0.32 (71) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stefaniya Pushkar (`KXITFWMATCH-26NOV08PUSBRE-PUS`) | 0.69 / 0.72 (87) | 70.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Julia Stusek vs Weronika Ewald -- W35 Liberec F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-08T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260541:260847:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Weronika Ewald (`KXITFWMATCH-26NOV08STUEWA-EWA`) | 0.61 / 0.62 (354) | 61.5% | 56.0% | 62.1% | 58.0% [54.3%-61.1%] | 59.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.5 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Julia Stusek (`KXITFWMATCH-26NOV08STUEWA-STU`) | 0.38 / 0.39 (40) | 38.5% | 44.0% | 37.9% | 42.0% [38.9%-45.7%] | 40.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.5 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1952.0, B 2476.0; serve-point win A 52.9%, B 46.0%; Elo A 1557.4, B 1581.0; model uncertainty 0.0341
* Form inputs: days since last match A 63, B 195; matches on record A 74, B 129; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.000, surface_dev_loose -0.031, surface_dev_tight +0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Summer Yardley vs Liana Cammilleri -- W15 Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-08T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216405:260589:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liana Cammilleri (`KXITFWMATCH-26NOV08YARCAM-CAM`) | 0.40 / 0.44 (136) | 42.0% | 49.3% | 89.0% | 54.3% [54.3%-54.3%] | -- | -- | -- | -- | PASS | +7.3 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Summer Yardley (`KXITFWMATCH-26NOV08YARCAM-YAR`) | 0.55 / 0.58 (136) | 56.5% | 50.7% | 11.0% | 45.7% [45.7%-45.7%] | -- | -- | -- | -- | PASS | -5.8 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 504.0, B 0.0; serve-point win A 53.8%, B 46.3%; Elo A 1108.4, B 1137.1; model uncertainty 0.0
* Form inputs: days since last match A 391, B 720; matches on record A 80, B 41; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jacob Fearnley vs Alexander Shevchenko -- ATP Stockholm F

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-08 15:30Z
* Current expected start: 2026-11-08 15:30Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: 2026-11-08 14:45Z

* Status notes: NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source)

ATP (TOUR_500_250) · Hard · scheduled 2026-11-08T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207686:207985:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jacob Fearnley (`KXATPMATCH-26NOV08FEASHE-FEA`) | 0.72 / 0.73 (32336) | 72.5% | 67.0% | 70.1% | 67.5% [64.7%-69.3%] | 71.8% | 73.3% | 73.3% | MODEL_LONE_OUTLIER | PASS | -5.5 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Alexander Shevchenko (`KXATPMATCH-26NOV08FEASHE-SHE`) | 0.27 / 0.28 (1280) | 27.5% | 33.0% | 29.9% | 32.5% [30.7%-35.3%] | 28.2% | 28.0% | 28.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +5.5 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4810.0, B 5512.0; serve-point win A 64.9%, B 38.6%; Elo A 1799.7, B 1730.9; model uncertainty 0.0228
* Form inputs: days since last match A 13, B 27; matches on record A 208, B 509; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.004, surface_dev_tight -0.004
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26NOV08FEASHE-FEA20` Will Jacob Fearnley win the Jacob Fearnley vs Alexander Shevchenko match by a set score of 2-0?: 0.47/0.50 mid 48.5%, model 37.9% (projection_v2.0 (prediction ledger)) -- gap -10.6 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV08FEASHE-2-SHE` Will Alexander Shevchenko win set 2 in the Jacob Fearnley vs Alexander Shevchenko match: 0.30/0.34 mid 32.0%, model 38.5% (projection_v2.0 (prediction ledger)) -- gap +6.5 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV08FEASHE-2-FEA` Will Jacob Fearnley win set 2 in the Jacob Fearnley vs Alexander Shevchenko match: 0.65/0.70 mid 67.5%, model 61.5% (projection_v2.0 (prediction ledger)) -- gap -6.0 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV08FEASHE-FEA21` Will Jacob Fearnley win the Jacob Fearnley vs Alexander Shevchenko match by a set score of 2-1?: 0.22/0.25 mid 23.5%, model 29.1% (projection_v2.0 (prediction ledger)) -- gap +5.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV08FEASHE-SHE21` Will Alexander Shevchenko win the Jacob Fearnley vs Alexander Shevchenko match by a set score of 2-1?: 0.12/0.14 mid 13.0%, model 18.2% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV08FEASHE-1-SHE` Will Alexander Shevchenko win set 1 in the Jacob Fearnley vs Alexander Shevchenko match: 0.33/0.36 mid 34.5%, model 38.5% (projection_v2.0 (prediction ledger)) -- gap +4.0 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV08FEASHE-1-FEA` Will Jacob Fearnley win set 1 in the Jacob Fearnley vs Alexander Shevchenko match: 0.64/0.66 mid 65.0%, model 61.5% (projection_v2.0 (prediction ledger)) -- gap -3.5 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV08FEASHE-SHE20` Will Alexander Shevchenko win the Jacob Fearnley vs Alexander Shevchenko match by a set score of 2-0?: 0.14/0.16 mid 15.0%, model 14.8% (projection_v2.0 (prediction ledger)) -- gap -0.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Jakob Schnaitter / Mark Wallner vs Adam Pavlasek / Patrik Rikl -- ATP Stockholm 1/8 F

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-08 18:30Z
* Current expected start: 2026-11-08 15:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-08 06:39Z
* Recommended handicap-by time: 2026-11-08 14:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-08T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08SCHWALPAVRIK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adam Pavlasek / Patrik Rikl (`KXATPDOUBLES-26NOV08SCHWALPAVRIK-PAVRIK`) | 0.59 / 0.62 (1064) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jakob Schnaitter / Mark Wallner (`KXATPDOUBLES-26NOV08SCHWALPAVRIK-SCHWAL`) | 0.37 / 0.40 (1843) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Oriol Alvarez Velis vs Patrick Jozwicki -- M15 Antalya R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08ALVJOZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oriol Alvarez Velis (`KXITFMATCH-26NOV08ALVJOZ-ALV`) | 0.07 / 0.12 (100) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Patrick Jozwicki (`KXITFMATCH-26NOV08ALVJOZ-JOZ`) | 0.88 / 0.94 (33) | 91.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ozan Avanoglu vs Aleksa Oparnica -- M15 Antalya R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-08T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213207:213939:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ozan Avanoglu (`KXITFMATCH-26NOV08AVAOPA-AVA`) | 0.05 / 0.09 (90) | 7.0% | 25.4% | 30.5% | 35.6% [34.3%-36.0%] | -- | -- | -- | -- | PASS | +18.4 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aleksa Oparnica (`KXITFMATCH-26NOV08AVAOPA-OPA`) | 0.92 / 0.93 (6) | 92.5% | 74.6% | 69.5% | 64.4% [64.0%-65.7%] | -- | -- | -- | -- | PASS | -17.9 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 85.0, B 70.0; serve-point win A 59.1%, B 35.7%; Elo A 1158.8, B 1263.3; model uncertainty 0.0088
* Form inputs: days since last match A 496, B 503; matches on record A 4, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV08AVAOPA-AVA  (YES = Ozan Avanoglu)
Model: 25%
Kalshi: 7%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high -0.000, surface_dev_loose -0.004, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mert Aytekin vs Aleksandar Lavrnja -- M15 Antalya R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-08T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213740:214182:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mert Aytekin (`KXITFMATCH-26NOV08AYTLAV-AYT`) | 0.18 / 0.30 (51) | 24.0% | 41.1% | 24.3% | 44.8% [44.7%-45.9%] | -- | -- | -- | -- | PASS | +17.1 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aleksandar Lavrnja (`KXITFMATCH-26NOV08AYTLAV-LAV`) | 0.71 / 0.82 (59) | 76.5% | 58.9% | 75.7% | 55.2% [54.1%-55.3%] | -- | -- | -- | -- | PASS | -17.6 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 226.0, B 49.0; serve-point win A 56.7%, B 41.6%; Elo A 1221.1, B 1247.4; model uncertainty 0.0056
* Form inputs: days since last match A 272, B 412; matches on record A 6, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV08AYTLAV-AYT  (YES = Mert Aytekin)
Model: 41%
Kalshi: 24%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ivan Gakhov vs Ignacio Parisca -- M25 Valencia F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-08T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:123809:212306:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ivan Gakhov (`KXITFMATCH-26NOV08GAKPAR-GAK`) | 0.59 / 0.61 (293) | 60.0% | 65.4% | 45.8% | 60.4% [54.2%-69.1%] | 59.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.4 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ignacio Parisca (`KXITFMATCH-26NOV08GAKPAR-PAR`) | 0.39 / 0.40 (132) | 39.5% | 34.6% | 54.2% | 39.6% [30.9%-45.8%] | 40.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.9 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4154.0, B 1927.0; serve-point win A 59.0%, B 44.0%; Elo A 1590.5, B 1383.1; model uncertainty 0.0744
* Form inputs: days since last match A 34, B 69; matches on record A 857, B 98; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amine Jamji vs Ognjen Jagrovic -- M15 Antalya R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-08T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213026:214146:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ognjen Jagrovic (`KXITFMATCH-26NOV08JAMJAG-JAG`) | 0.16 / 0.25 (105) | 20.5% | 30.2% | 44.8% | 44.8% [43.3%-45.4%] | -- | -- | -- | -- | PASS | +9.7 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amine Jamji (`KXITFMATCH-26NOV08JAMJAG-JAM`) | 0.75 / 0.82 (133) | 78.5% | 69.8% | 55.2% | 55.2% [54.6%-56.7%] | -- | -- | -- | -- | PASS | -8.7 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 659.0, B 139.0; serve-point win A 61.7%, B 42.3%; Elo A 1224.0, B 1189.4; model uncertainty 0.0103
* Form inputs: days since last match A 49, B 356; matches on record A 15, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luka Pavlovic vs Hugo Grenier -- ATP Challenger Orleans Semi F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-08T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126409:202146:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Grenier (`KXATPCHALLENGERMATCH-26NOV08PAVGRE-GRE`) | 0.46 / 0.47 (3127) | 46.5% | 54.5% | 53.9% | 57.8% [55.4%-60.7%] | 45.9% | 45.4% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +8.0 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luka Pavlovic (`KXATPCHALLENGERMATCH-26NOV08PAVGRE-PAV`) | 0.54 / 0.55 (1170) | 54.5% | 45.5% | 46.1% | 42.2% [39.3%-44.6%] | 54.1% | 54.7% | -- | INSUFFICIENT_INPUTS | PASS | -9.0 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3728.0, B 4320.0; serve-point win A 64.5%, B 34.6%; Elo A 1505.3, B 1638.3; model uncertainty 0.0266
* Form inputs: days since last match A 22, B 13; matches on record A 310, B 793; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.024, surface_pool_high -0.029, surface_dev_loose +0.010, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Leo Raquillet vs Lorenzo Carboni -- ATP Challenger Hersonissos Semi F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-08T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210447:212077:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Carboni (`KXATPCHALLENGERMATCH-26NOV08RAQCAR-CAR`) | 0.65 / 0.66 (1150) | 65.5% | 58.4% | 53.7% | 57.3% [55.8%-58.9%] | 65.1% | 64.9% | -- | INSUFFICIENT_INPUTS | PASS | -7.1 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Leo Raquillet (`KXATPCHALLENGERMATCH-26NOV08RAQCAR-RAQ`) | 0.34 / 0.35 (99) | 34.5% | 41.6% | 46.3% | 42.7% [41.1%-44.2%] | 34.8% | 35.1% | -- | INSUFFICIENT_INPUTS | PASS | +7.1 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2695.0, B 3055.0; serve-point win A 55.9%, B 42.5%; Elo A 1378.9, B 1476.3; model uncertainty 0.0156
* Form inputs: days since last match A 55, B 27; matches on record A 129, B 176; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose +0.010, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Yanick Schneider vs Timo Rosenkranz Koenig -- M15 Antalya R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08SCHROS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Timo Rosenkranz Koenig (`KXITFMATCH-26NOV08SCHROS-ROS`) | 0.78 / 0.86 (82) | 82.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yanick Schneider (`KXITFMATCH-26NOV08SCHROS-SCH`) | 0.13 / 0.20 (1) | 16.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexander Ushakov vs Mark Laubic -- M15 Antalya R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08USHLAU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mark Laubic (`KXITFMATCH-26NOV08USHLAU-LAU`) | 0.53 / 0.65 (18) | 59.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexander Ushakov (`KXITFMATCH-26NOV08USHLAU-USH`) | 0.35 / 0.47 (64) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gianmarco Ferrari vs Michele Mecarelli -- M15 San Gregorio di Catania F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-08T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208189:213356:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gianmarco Ferrari (`KXITFMATCH-26NOV08FERMEC-FER`) | 0.61 / 0.62 (230) | 61.5% | 66.6% | 69.4% | 69.4% [68.4%-70.8%] | 62.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +5.1 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Michele Mecarelli (`KXITFMATCH-26NOV08FERMEC-MEC`) | 0.37 / 0.39 (762) | 38.0% | 33.4% | 30.6% | 30.6% [29.2%-31.6%] | 37.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.6 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2506.0, B 981.0; serve-point win A 60.8%, B 42.5%; Elo A 1474.0, B 1326.4; model uncertainty 0.0117
* Form inputs: days since last match A 62, B 90; matches on record A 294, B 23; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.009, surface_dev_loose +0.014, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jerome Kym vs Jurij Rodionov -- ATP Challenger Bratislava F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-08T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200514:208843:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jerome Kym (`KXATPCHALLENGERMATCH-26NOV08KYMROD-KYM`) | 0.67 / 0.69 (10812) | 68.0% | 60.1% | 66.4% | 64.1% [60.8%-66.4%] | 67.1% | 65.2% | -- | INSUFFICIENT_INPUTS | PASS | -7.9 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jurij Rodionov (`KXATPCHALLENGERMATCH-26NOV08KYMROD-ROD`) | 0.31 / 0.33 (6402) | 32.0% | 39.9% | 33.6% | 35.9% [33.6%-39.2%] | 32.9% | 30.5% | -- | INSUFFICIENT_INPUTS | WATCH | +7.9 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3935.0, B 5184.0; serve-point win A 65.3%, B 36.7%; Elo A 1739.2, B 1685.1; model uncertainty 0.0277
* Form inputs: days since last match A 9, B 11; matches on record A 280, B 613; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.005, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Melinda Biro vs Sofia Barhacova -- W15 Szabolcsveresmart F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV08BIRBAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Barhacova (`KXITFWMATCH-26NOV08BIRBAR-BAR`) | 0.48 / 0.49 (102) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Melinda Biro (`KXITFWMATCH-26NOV08BIRBAR-BIR`) | 0.50 / 0.51 (41) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anna Burchak vs Florentine Dekkers -- W15 Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-08T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223334:270253:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Burchak (`KXITFWMATCH-26NOV08BURDEK-BUR`) | 0.58 / 0.61 (184) | 59.5% | 47.8% | 21.7% | 46.8% [46.8%-47.9%] | -- | -- | -- | -- | PASS | -11.7 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Florentine Dekkers (`KXITFWMATCH-26NOV08BURDEK-DEK`) | 0.37 / 0.41 (230) | 39.0% | 52.2% | 78.3% | 53.2% [52.1%-53.2%] | -- | -- | -- | -- | PASS | +13.2 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 191.0, B 0.0; serve-point win A 55.6%, B 43.9%; Elo A 1224.9, B 1244.2; model uncertainty 0.0054
* Form inputs: days since last match A 384, B 818; matches on record A 3, B 21; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Severine Deppner vs Teodora Vlajic -- W15 Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-08T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:266649:270428:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Severine Deppner (`KXITFWMATCH-26NOV08DEPVLA-DEP`) | 0.44 / 0.47 (34) | 45.5% | 50.1% | 44.1% | 50.0% [48.9%-50.5%] | -- | -- | -- | -- | PASS | +4.6 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Teodora Vlajic (`KXITFWMATCH-26NOV08DEPVLA-VLA`) | 0.52 / 0.55 (126) | 53.5% | 49.9% | 55.9% | 50.0% [49.5%-51.1%] | -- | -- | -- | -- | PASS | -3.6 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 295.0, B 116.0; serve-point win A 52.9%, B 47.2%; Elo A 1254.0, B 1255.8; model uncertainty 0.008
* Form inputs: days since last match A 307, B 202; matches on record A 45, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.005, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Francesca Parcelli vs Elisa Rohrbach -- W15 Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV08PARROH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesca Parcelli (`KXITFWMATCH-26NOV08PARROH-PAR`) | 0.86 / 0.90 (106) | 88.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Elisa Rohrbach (`KXITFWMATCH-26NOV08PARROH-ROH`) | 0.09 / 0.14 (31) | 11.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Thiago Agustin Tirante vs Jaume Munar -- ATP Stockholm 1/16 F

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-08 19:30Z
* Current expected start: 2026-11-08 16:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-08 06:39Z
* Recommended handicap-by time: 2026-11-08 15:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-11-08T19:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144719:202058:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jaume Munar (`KXATPMATCH-26NOV08TIRMUN-MUN`) | 0.59 / 0.61 (9555) | 60.0% | 60.2% | 60.2% | 59.7% [57.8%-60.7%] | 60.2% | 59.7% | 59.7% | MODEL_LONE_OUTLIER | PASS | +0.2 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Thiago Agustin Tirante (`KXATPMATCH-26NOV08TIRMUN-TIR`) | 0.39 / 0.41 (2308) | 40.0% | 39.8% | 39.8% | 40.3% [39.3%-42.2%] | 39.8% | 40.0% | 40.0% | MODEL_LONE_OUTLIER | PASS | -0.2 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5742.0, B 4745.0; serve-point win A 64.3%, B 33.6%; Elo A 1734.3, B 1800.5; model uncertainty 0.0142
* Form inputs: days since last match A 4, B 8; matches on record A 493, B 747; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose -0.004, surface_dev_tight -0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26NOV08TIRMUN-MUN6` Will Jaume Munar win at least 5.5 more games than Thiago Agustin Tirante?: 0.10/0.39 mid 24.5%, model 10.4% (projection_v2.0 (prediction ledger)) -- gap -14.1 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV08TIRMUN-23` Over 22.5 games: 0.50/0.51 mid 50.5%, model 62.2% (projection_v2.0 (prediction ledger)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV08TIRMUN-28` Over 27.5 games: 0.31/0.33 mid 32.0%, model 41.8% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV08TIRMUN-18` Over 17.5 games: 0.86/0.90 mid 88.0%, model 94.6% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV08TIRMUN-MUN21` Will Jaume Munar win the Thiago Agustin Tirante vs Jaume Munar match by a set score of 2-1?: 0.20/0.24 mid 22.0%, model 27.9% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV08TIRMUN-MUN20` Will Jaume Munar win the Thiago Agustin Tirante vs Jaume Munar match by a set score of 2-0?: 0.36/0.40 mid 38.0%, model 32.3% (projection_v2.0 (prediction ledger)) -- gap -5.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV08TIRMUN-TIR21` Will Thiago Agustin Tirante win the Thiago Agustin Tirante vs Jaume Munar match by a set score of 2-1?: 0.15/0.17 mid 16.0%, model 21.2% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV08TIRMUN-MUN3` Will Jaume Munar win at least 2.5 more games than Thiago Agustin Tirante?: 0.48/0.50 mid 49.0%, model 44.1% (projection_v2.0 (prediction ledger)) -- gap -4.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV08TIRMUN-TIR20` Will Thiago Agustin Tirante win the Thiago Agustin Tirante vs Jaume Munar match by a set score of 2-0?: 0.21/0.24 mid 22.5%, model 18.6% (projection_v2.0 (prediction ledger)) -- gap -3.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV08TIRMUN-2-TIR` Will Thiago Agustin Tirante win set 2 in the Thiago Agustin Tirante vs Jaume Munar match: 0.39/0.43 mid 41.0%, model 43.2% (projection_v2.0 (prediction ledger)) -- gap +2.2 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV08TIRMUN-2-MUN` Will Jaume Munar win set 2 in the Thiago Agustin Tirante vs Jaume Munar match: 0.56/0.60 mid 58.0%, model 56.8% (projection_v2.0 (prediction ledger)) -- gap -1.2 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV08TIRMUN-TIR2` Will Thiago Agustin Tirante win at least 1.5 more games than Jaume Munar?: 0.32/0.35 mid 33.5%, model 32.4% (projection_v2.0 (prediction ledger)) -- gap -1.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV08TIRMUN-1-TIR` Will Thiago Agustin Tirante win set 1 in the Thiago Agustin Tirante vs Jaume Munar match: 0.41/0.44 mid 42.5%, model 43.2% (projection_v2.0 (prediction ledger)) -- gap +0.7 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV08TIRMUN-1-MUN` Will Jaume Munar win set 1 in the Thiago Agustin Tirante vs Jaume Munar match: 0.56/0.58 mid 57.0%, model 56.8% (projection_v2.0 (prediction ledger)) -- gap -0.2 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Luca Nardi vs Alexander Donski -- ATP Challenger Orleans Semi F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 16:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-08T16:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200574:208134:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Donski (`KXATPCHALLENGERMATCH-26NOV08NARDON-DON`) | 0.14 / 0.15 (53) | 14.5% | 23.8% | 37.5% | 30.7% [26.4%-33.4%] | 15.6% | 14.8% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +9.2 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luca Nardi (`KXATPCHALLENGERMATCH-26NOV08NARDON-NAR`) | 0.85 / 0.86 (7) | 85.5% | 76.2% | 62.5% | 69.3% [66.6%-73.6%] | 84.4% | 85.0% | -- | INSUFFICIENT_INPUTS | PASS | -9.2 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4120.0, B 2695.0; serve-point win A 68.3%, B 37.5%; Elo A 1692.9, B 1449.8; model uncertainty 0.035
* Form inputs: days since last match A 27, B 97; matches on record A 380, B 296; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.009, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Juan Manuel La Serna vs Genaro Alberto Olivieri -- ATP Challenger Villa Maria F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-08T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144821:210412:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Manuel La Serna (`KXATPCHALLENGERMATCH-26NOV08LAOLI-LA`) | 0.50 / 0.51 (2356) | 50.5% | 52.9% | 66.4% | 62.0% [58.4%-64.0%] | 49.0% | 50.7% | 50.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +2.4 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Genaro Alberto Olivieri (`KXATPCHALLENGERMATCH-26NOV08LAOLI-OLI`) | 0.49 / 0.50 (126) | 49.5% | 47.1% | 33.6% | 38.0% [36.0%-41.6%] | 51.0% | 49.3% | 49.3% | MODEL_LONE_OUTLIER | PASS | -2.4 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3904.0, B 5035.0; serve-point win A 56.5%, B 44.0%; Elo A 1577.7, B 1586.5; model uncertainty 0.028
* Form inputs: days since last match A 13, B 13; matches on record A 197, B 609; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.005, surface_dev_loose +0.005, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Agathe Charlot kolb vs Ninon Carpentier -- W15 Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV08CHACAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ninon Carpentier (`KXITFWMATCH-26NOV08CHACAR-CAR`) | 0.87 / 0.91 (5) | 89.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Agathe Charlot kolb (`KXITFWMATCH-26NOV08CHACAR-CHA`) | 0.08 / 0.13 (57) | 10.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kim Chiarello vs Alina Nesmianovych -- W15 Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-08T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:232891:269710:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kim Chiarello (`KXITFWMATCH-26NOV08CHINES-CHI`) | 0.84 / 0.86 (6) | 85.0% | 89.6% | 45.8% | 76.3% [75.5%-76.5%] | -- | -- | -- | -- | PASS | +4.6 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Alina Nesmianovych (`KXITFWMATCH-26NOV08CHINES-NES`) | 0.12 / 0.15 (18) | 13.5% | 10.4% | 54.2% | 23.7% [23.5%-24.5%] | -- | -- | -- | -- | PASS | -3.1 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 458.0, B 0.0; serve-point win A 60.3%, B 49.2%; Elo A 1354.7, B 1153.8; model uncertainty 0.005
* Form inputs: days since last match A 391, B 734; matches on record A 7, B 19; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.008, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Capucine Dournes vs Milena Maria Ciocan -- W15 Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV08DOUCIO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Milena Maria Ciocan (`KXITFWMATCH-26NOV08DOUCIO-CIO`) | 0.80 / 0.81 (30) | 80.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Capucine Dournes (`KXITFWMATCH-26NOV08DOUCIO-DOU`) | 0.16 / 0.21 (127) | 18.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Calvin Hemery vs Yanis Ghazouani Durand -- ATP Challenger Orleans Semi F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 17:50Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-08T17:50:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:123921:211901:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yanis Ghazouani Durand (`KXATPCHALLENGERMATCH-26NOV08HEMGHA-GHA`) | 0.31 / 0.35 (12) | 33.0% | 39.9% | 48.5% | 44.0% [36.1%-48.5%] | -- | 32.3% | -- | INSUFFICIENT_INPUTS | PASS | +6.8 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Calvin Hemery (`KXATPCHALLENGERMATCH-26NOV08HEMGHA-HEM`) | 0.65 / 0.69 (5) | 67.0% | 60.2% | 51.5% | 56.0% [51.5%-63.8%] | -- | 67.5% | -- | INSUFFICIENT_INPUTS | PASS | -6.8 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4976.0, B 2469.0; serve-point win A 63.8%, B 38.3%; Elo A 1549.6, B 1457.6; model uncertainty 0.0617
* Form inputs: days since last match A 20, B 41; matches on record A 754, B 122; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.035, surface_pool_high -0.035, surface_dev_loose -0.005, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Hanna Bougouffa vs Victoire Lansaman -- W15 Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-08T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:230121:266812:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hanna Bougouffa (`KXITFWMATCH-26NOV08BOULAN-BOU`) | 0.66 / 0.74 (125) | 70.0% | 71.6% | 74.0% | 56.4% [54.3%-59.0%] | -- | -- | -- | -- | PASS | +1.6 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Victoire Lansaman (`KXITFWMATCH-26NOV08BOULAN-LAN`) | 0.28 / 0.29 (16) | 28.5% | 28.4% | 26.0% | 43.6% [41.0%-45.7%] | -- | -- | -- | -- | PASS | -0.1 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 245.0, B 155.0; serve-point win A 55.2%, B 49.1%; Elo A 1259.9, B 1231.0; model uncertainty 0.0238
* Form inputs: days since last match A 468, B 237; matches on record A 134, B 10; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.021, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Coline Briand vs Hajar Crinebouch -- W15 Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-08T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:263728:266697:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Coline Briand (`KXITFWMATCH-26NOV08BRICRI-BRI`) | 0.44 / 0.49 (286) | 46.5% | 30.3% | 45.7% | 48.9% [47.9%-48.9%] | -- | -- | -- | -- | PASS | -16.2 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hajar Crinebouch (`KXITFWMATCH-26NOV08BRICRI-CRI`) | 0.49 / 0.56 (148) | 52.5% | 69.7% | 54.3% | 51.1% [51.1%-52.1%] | -- | -- | -- | -- | PASS | +17.2 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 73.0, B 479.0; serve-point win A 49.0%, B 47.2%; Elo A 1206.6, B 1213.8; model uncertainty 0.0054
* Form inputs: days since last match A 293, B 181; matches on record A 11, B 17; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV08BRICRI-CRI  (YES = Hajar Crinebouch)
Model: 70%
Kalshi: 52%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amahee Charrier vs Helena Stevic -- W15 Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV08CHASTE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amahee Charrier (`KXITFWMATCH-26NOV08CHASTE-CHA`) | 0.46 / 0.53 (163) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Helena Stevic (`KXITFWMATCH-26NOV08CHASTE-STE`) | 0.47 / 0.52 (12) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Antonia Vergara Rivera vs Justina Maria Gonzalez Daniele -- W15 Neuquén F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 18:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-08T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:254733:260708:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Justina Maria Gonzalez Daniele (`KXITFWMATCH-26NOV08VERGON-GON`) | 0.41 / 0.42 (185) | 41.5% | 41.0% | 51.6% | 47.3% [41.0%-49.5%] | 40.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -0.5 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Antonia Vergara Rivera (`KXITFWMATCH-26NOV08VERGON-VER`) | 0.57 / 0.58 (125) | 57.5% | 59.0% | 48.4% | 52.7% [50.5%-59.0%] | 59.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.5 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3116.0, B 2911.0; serve-point win A 50.5%, B 51.2%; Elo A 1525.0, B 1445.0; model uncertainty 0.0425
* Form inputs: days since last match A 11, B 195; matches on record A 99, B 154; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.005, surface_dev_loose -0.005, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Davi Domarco Carlos vs Gabriel Augusto Carvalho -- M25 Santa Cruz do Sul R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08DOMCAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriel Augusto Carvalho (`KXITFMATCH-26NOV08DOMCAR-CAR`) | 0.06 / 0.91 (10) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Davi Domarco Carlos (`KXITFMATCH-26NOV08DOMCAR-DOM`) | 0.10 / 0.88 (4) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Enzo Fortes vs Gabriel Ribeiro Pinho -- M25 Santa Cruz do Sul R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08FORPIN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Enzo Fortes (`KXITFMATCH-26NOV08FORPIN-FOR`) | 0.10 / 0.93 (18) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gabriel Ribeiro Pinho (`KXITFMATCH-26NOV08FORPIN-PIN`) | 0.06 / 0.91 (10) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mateus Kuwar Lang vs Daniel Vecchio Couldrey Rebelo -- M25 Santa Cruz do Sul R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08KUWREB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mateus Kuwar Lang (`KXITFMATCH-26NOV08KUWREB-KUW`) | 0.45 / 0.46 (6) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daniel Vecchio Couldrey Rebelo (`KXITFMATCH-26NOV08KUWREB-REB`) | 0.52 / 0.78 (14) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amelie Brooks vs Fanny Pire -- W15 Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-08T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259608:267926:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amelie Brooks (`KXITFWMATCH-26NOV08BROPIR-BRO`) | 0.71 / 0.75 (191) | 73.0% | 45.6% | 48.4% | 44.7% [44.7%-45.7%] | -- | -- | -- | -- | PASS | -27.4 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Fanny Pire (`KXITFWMATCH-26NOV08BROPIR-PIR`) | 0.25 / 0.28 (8) | 26.5% | 54.4% | 51.6% | 55.3% [54.3%-55.3%] | -- | -- | -- | -- | PASS | +27.9 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 164.0, B 0.0; serve-point win A 52.8%, B 46.3%; Elo A 1211.6, B 1245.7; model uncertainty 0.0053
* Form inputs: days since last match A 195, B 811; matches on record A 19, B 5; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV08BROPIR-PIR  (YES = Fanny Pire)
Model: 54%
Kalshi: 26%
Gap: +28 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.011, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jade Groen vs Hena Cehajic -- W15 Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-08T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:267722:270136:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hena Cehajic (`KXITFWMATCH-26NOV08GROCEH-CEH`) | 0.16 / 0.28 (12) | 22.0% | 33.8% | 38.9% | 45.2% [43.1%-46.8%] | -- | -- | -- | -- | PASS | +11.8 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jade Groen (`KXITFWMATCH-26NOV08GROCEH-GRO`) | 0.69 / 0.79 (224) | 74.0% | 66.2% | 61.1% | 54.8% [53.2%-56.9%] | -- | -- | -- | -- | PASS | -7.8 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 470.0, B 413.0; serve-point win A 53.4%, B 49.7%; Elo A 1292.1, B 1266.5; model uncertainty 0.0187
* Form inputs: days since last match A 363, B 363; matches on record A 9, B 7; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high +0.000, surface_dev_loose +0.011, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carolin Raschdorf vs Meline Lataste -- W15 Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-08T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:234481:267625:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Meline Lataste (`KXITFWMATCH-26NOV08RASLAT-LAT`) | 0.34 / 0.41 (5) | 37.5% | 16.4% | 46.3% | 36.5% [35.5%-37.5%] | -- | -- | -- | -- | PASS | -21.1 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carolin Raschdorf (`KXITFWMATCH-26NOV08RASLAT-RAS`) | 0.56 / 0.61 (145) | 58.5% | 83.6% | 53.7% | 63.5% [62.5%-64.5%] | -- | -- | -- | -- | PASS | +25.1 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 843.0, B 62.0; serve-point win A 58.5%, B 48.9%; Elo A 1332.6, B 1236.1; model uncertainty 0.01
* Form inputs: days since last match A 258, B 517; matches on record A 85, B 3; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV08RASLAT-RAS  (YES = Carolin Raschdorf)
Model: 84%
Kalshi: 58%
Gap: +25 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marta Kostyuk vs Linda Noskova -- WTA Finals (Women) RR

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-08 23:00Z
* Current expected start: 2026-11-08 20:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-08 06:39Z
* Recommended handicap-by time: 2026-11-08 19:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_FINALS) · Hard · scheduled 2026-11-08T23:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:216146:222328:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marta Kostyuk (`KXWTAMATCH-26NOV08KOSNOS-KOS`) | 0.45 / 0.46 (4706) | 45.5% | 47.1% | 59.2% | 55.6% [52.6%-57.7%] | 46.8% | 45.5% | 46.1% | MODEL_LONE_OUTLIER | SHADOW_BET | +1.6 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Linda Noskova (`KXWTAMATCH-26NOV08KOSNOS-NOS`) | 0.54 / 0.56 (36049) | 55.0% | 52.9% | 40.8% | 44.4% [42.3%-47.4%] | 53.2% | 54.2% | 53.7% | MODEL_LONE_OUTLIER | PASS | -2.1 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4067.0, B 4568.0; serve-point win A 60.3%, B 39.1%; Elo A 2069.3, B 2093.7; model uncertainty 0.0254
* Form inputs: days since last match A 18, B 33; matches on record A 432, B 335; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose +0.005, surface_dev_tight +0.000
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26NOV08KOSNOS-1-NOS` Will Linda Noskova win set 1 in the Marta Kostyuk vs Linda Noskova match: 0.52/0.56 mid 54.0%, model 51.9% (projection_v2.0 (prediction ledger)) -- gap -2.1 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV08KOSNOS-2-KOS` Will Marta Kostyuk win set 2 in the Marta Kostyuk vs Linda Noskova match: 0.44/0.49 mid 46.5%, model 48.1% (projection_v2.0 (prediction ledger)) -- gap +1.6 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV08KOSNOS-2-NOS` Will Linda Noskova win set 2 in the Marta Kostyuk vs Linda Noskova match: 0.51/0.56 mid 53.5%, model 51.9% (projection_v2.0 (prediction ledger)) -- gap -1.6 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV08KOSNOS-1-KOS` Will Marta Kostyuk win set 1 in the Marta Kostyuk vs Linda Noskova match: 0.45/0.49 mid 47.0%, model 48.1% (projection_v2.0 (prediction ledger)) -- gap +1.1 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Blaise Bicknell vs Kacper Szymkowiak -- M15 Pembroke F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209080:212852:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Blaise Bicknell (`KXITFMATCH-26NOV08BICSZY-BIC`) | 0.66 / 0.69 (269) | 67.5% | 60.0% | 46.4% | 58.2% [53.6%-65.0%] | 66.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.5 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kacper Szymkowiak (`KXITFMATCH-26NOV08BICSZY-SZY`) | 0.30 / 0.33 (134) | 31.5% | 40.0% | 53.6% | 41.8% [35.0%-46.4%] | 33.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +8.5 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3719.0, B 1216.0; serve-point win A 60.7%, B 41.2%; Elo A 1497.2, B 1370.4; model uncertainty 0.0571
* Form inputs: days since last match A 41, B 244; matches on record A 233, B 41; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luka Bojicic Ono vs Ryan Char -- M25 Santa Cruz do Sul R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08BOJCHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luka Bojicic Ono (`KXITFMATCH-26NOV08BOJCHA-BOJ`) | 0.10 / 0.91 (10) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ryan Char (`KXITFMATCH-26NOV08BOJCHA-CHA`) | 0.08 / 0.93 (18) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Augusto Land vs Mateus Napoli da Silveira -- M25 Santa Cruz do Sul R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08LANNAP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Augusto Land (`KXITFMATCH-26NOV08LANNAP-LAN`) | 0.06 / 0.93 (10) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mateus Napoli da Silveira (`KXITFMATCH-26NOV08LANNAP-NAP`) | 0.06 / 0.93 (10) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anna Siskova vs Veronika Podrez -- W75 Petange F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-08T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216074:247669:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Veronika Podrez (`KXITFWMATCH-26NOV08SISPOD-POD`) | 0.65 / 0.67 (112) | 66.0% | 61.9% | 50.0% | 52.7% [50.5%-55.8%] | 67.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anna Siskova (`KXITFWMATCH-26NOV08SISPOD-SIS`) | 0.32 / 0.34 (124) | 33.0% | 38.1% | 50.0% | 47.3% [44.2%-49.5%] | 32.5% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +5.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3067.0, B 3466.0; serve-point win A 53.4%, B 44.4%; Elo A 1658.8, B 1719.9; model uncertainty 0.0265
* Form inputs: days since last match A 26, B 45; matches on record A 435, B 227; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.005, surface_dev_loose +0.021, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eduardo Heineberg vs Joao Victor Becker Fabricanti -- M25 Santa Cruz do Sul R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08HEIBEC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joao Victor Becker Fabricanti (`KXITFMATCH-26NOV08HEIBEC-BEC`) | 0.05 / 0.94 (175) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eduardo Heineberg (`KXITFMATCH-26NOV08HEIBEC-HEI`) | 0.05 / 0.94 (175) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stefan Kozlov vs Aidan Mayo -- ATP Challenger Charlottesville F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-08T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111578:208854:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefan Kozlov (`KXATPCHALLENGERMATCH-26NOV08KOZMAY-KOZ`) | 0.37 / 0.38 (1687) | 37.5% | 44.1% | 37.4% | 41.8% [39.3%-45.9%] | 38.4% | 36.5% | 38.4% | MODEL_LONE_OUTLIER | WATCH | +6.6 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Aidan Mayo (`KXATPCHALLENGERMATCH-26NOV08KOZMAY-MAY`) | 0.62 / 0.64 (4797) | 63.0% | 55.9% | 62.6% | 58.2% [54.1%-60.7%] | 61.6% | 63.3% | 61.6% | MODEL_LONE_OUTLIER | PASS | -7.1 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3563.0, B 3926.0; serve-point win A 60.0%, B 38.9%; Elo A 1589.2, B 1573.4; model uncertainty 0.0328
* Form inputs: days since last match A 13, B 13; matches on record A 620, B 260; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.015, surface_dev_tight +0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## William Mirarchi vs Dragos Cazacu -- M15 Hilton Head Island SC F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08MIRCAZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dragos Cazacu (`KXITFMATCH-26NOV08MIRCAZ-CAZ`) | 0.62 / 0.65 (154) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| William Mirarchi (`KXITFMATCH-26NOV08MIRCAZ-MIR`) | 0.33 / 0.37 (122) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## John Paul Baroni Schtz Tankersley vs Thiago Horacio Messa -- M25 Santa Cruz do Sul R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08TANMES:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thiago Horacio Messa (`KXITFMATCH-26NOV08TANMES-MES`) | 0.48 / 0.90 (6) | 69.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| John Paul Baroni Schtz Tankersley (`KXITFMATCH-26NOV08TANMES-TAN`) | 0.07 / 0.48 (1) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aya El Aouni vs Ashley Lahey -- W15 Hilton Head Island SC F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216076:223671:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aya El Aouni (`KXITFWMATCH-26NOV08ELALAH-ELA`) | 0.42 / 0.43 (214) | 42.5% | 28.2% | 22.1% | 28.8% [26.6%-29.8%] | 43.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -14.3 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ashley Lahey (`KXITFWMATCH-26NOV08ELALAH-LAH`) | 0.57 / 0.60 (147) | 58.5% | 71.8% | 77.9% | 71.2% [70.2%-73.4%] | 56.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.3 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 211.0, B 1883.0; serve-point win A 53.4%, B 42.2%; Elo A 1481.8, B 1627.6; model uncertainty 0.0156
* Form inputs: days since last match A 538, B 419; matches on record A 111, B 239; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Leonie Schuknecht vs Malkia Ngounoue -- W15 Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV08SCHNGO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Malkia Ngounoue (`KXITFWMATCH-26NOV08SCHNGO-NGO`) | 0.60 / 0.67 (124) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Leonie Schuknecht (`KXITFWMATCH-26NOV08SCHNGO-SCH`) | 0.31 / 0.34 (5) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Coco Gauff vs Jessica Pegula -- WTA Finals (Women) RR

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-09 00:30Z
* Current expected start: 2026-11-08 21:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-08 06:39Z
* Recommended handicap-by time: 2026-11-08 20:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_FINALS) · Hard · scheduled 2026-11-09T00:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202468:221103:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Coco Gauff (`KXWTAMATCH-26NOV08GAUPEG-GAU`) | 0.57 / 0.58 (1265) | 57.5% | 47.4% | 36.5% | 39.6% [38.0%-47.9%] | -- | -- | -- | -- | PASS | -10.1 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jessica Pegula (`KXWTAMATCH-26NOV08GAUPEG-PEG`) | 0.42 / 0.43 (6051) | 42.5% | 52.6% | 63.5% | 60.4% [52.1%-62.0%] | -- | -- | -- | -- | WATCH | +10.1 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5157.0, B 5824.0; serve-point win A 56.2%, B 43.4%; Elo A 2197.9, B 2199.4; model uncertainty 0.0492
* Form inputs: days since last match A 32, B 25; matches on record A 446, B 767; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.015, surface_dev_tight +0.021
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26NOV08GAUPEG-2-PEG` Will Jessica Pegula win set 2 in the Coco Gauff vs Jessica Pegula match: 0.30/0.56 mid 43.0%, model 51.7% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV08GAUPEG-1-GAU` Will Coco Gauff win set 1 in the Coco Gauff vs Jessica Pegula match: 0.55/0.58 mid 56.5%, model 48.3% (projection_v2.0 (prediction ledger)) -- gap -8.2 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV08GAUPEG-1-PEG` Will Jessica Pegula win set 1 in the Coco Gauff vs Jessica Pegula match: 0.42/0.45 mid 43.5%, model 51.7% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV08GAUPEG-2-GAU` Will Coco Gauff win set 2 in the Coco Gauff vs Jessica Pegula match: 0.39/0.66 mid 52.5%, model 48.3% (projection_v2.0 (prediction ledger)) -- gap -4.2 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Joao Marcos Angelico vs Glauco Pinheiro da Cruz Junior -- M25 Santa Cruz do Sul R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08ANGPIN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joao Marcos Angelico (`KXITFMATCH-26NOV08ANGPIN-ANG`) | 0.14 / 0.39 (6) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Glauco Pinheiro da Cruz Junior (`KXITFMATCH-26NOV08ANGPIN-PIN`) | 0.56 / 0.82 (6) | 69.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andrey Barbiero vs Yuki Ikeda -- M25 Santa Cruz do Sul R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-08T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08BARIKE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrey Barbiero (`KXITFMATCH-26NOV08BARIKE-BAR`) | 0.05 / 0.94 (175) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yuki Ikeda (`KXITFMATCH-26NOV08BARIKE-IKE`) | 0.05 / 0.94 (175) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nikola Slavic vs Johan Oscar Lien -- M15 Trois-Rivières F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-08T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208302:214231:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Johan Oscar Lien (`KXITFMATCH-26NOV08SLALIE-LIE`) | 0.49 / 0.52 (147) | 50.5% | 52.5% | 60.0% | 53.5% [48.0%-56.5%] | 56.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.0 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nikola Slavic (`KXITFMATCH-26NOV08SLALIE-SLA`) | 0.45 / 0.50 (101) | 47.5% | 47.5% | 40.0% | 46.5% [43.5%-52.0%] | 43.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.0 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2270.0, B 812.0; serve-point win A 62.4%, B 37.1%; Elo A 1277.3, B 1275.6; model uncertainty 0.0428
* Form inputs: days since last match A 119, B 216; matches on record A 65, B 15; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Janae Preston vs Evialina Laskevich -- W35 Orlando FL F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-08T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222184:270320:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Evialina Laskevich (`KXITFWMATCH-26NOV08PRELAS-LAS`) | 0.36 / 0.37 (23) | 36.5% | 64.0% | 10.9% | 52.1% [33.4%-76.5%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +27.5 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Janae Preston (`KXITFWMATCH-26NOV08PRELAS-PRE`) | 0.61 / 0.63 (6) | 62.0% | 36.0% | 89.1% | 47.9% [23.4%-66.6%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -26.0 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 739.0, B 737.0; serve-point win A 49.6%, B 47.8%; Elo A 1427.5, B 1625.6; model uncertainty 0.216
* Form inputs: days since last match A 75, B 265; matches on record A 14, B 167; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV08PRELAS-LAS  (YES = Evialina Laskevich)
Model: 64%
Kalshi: 36%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.037, surface_pool_high +0.027, surface_dev_loose +0.021, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Diletta Cherubini vs Malaika Rapolu -- W50 Huamantla F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-08 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-08T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221000:222837:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diletta Cherubini (`KXITFWMATCH-26NOV08CHERAP-CHE`) | 0.15 / 0.17 (123) | 16.0% | 21.3% | 17.4% | 21.9% [17.1%-32.5%] | 17.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +5.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Malaika Rapolu (`KXITFWMATCH-26NOV08CHERAP-RAP`) | 0.84 / 0.85 (20) | 84.5% | 78.7% | 82.6% | 78.1% [67.5%-82.9%] | 82.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.8 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2494.0, B 1761.0; serve-point win A 50.0%, B 44.0%; Elo A 1445.5, B 1619.4; model uncertainty 0.0768
* Form inputs: days since last match A 9, B 52; matches on record A 315, B 134; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.024, surface_pool_high -0.023, surface_dev_loose -0.019, surface_dev_tight +0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bor Artnak vs Connor Henry Van Schalkwyk -- M25 Harlingen TX F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-09T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210107:210227:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bor Artnak (`KXITFMATCH-26NOV08ARTVAN-ART`) | 0.56 / 0.59 (9) | 57.5% | 78.0% | 69.5% | 74.3% [73.5%-75.1%] | -- | -- | -- | -- | PASS | +20.5 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Connor Henry Van Schalkwyk (`KXITFMATCH-26NOV08ARTVAN-VAN`) | 0.41 / 0.42 (238) | 41.5% | 22.0% | 30.5% | 25.7% [24.9%-26.5%] | -- | -- | -- | -- | PASS | -19.5 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3186.0, B 56.0; serve-point win A 61.6%, B 44.3%; Elo A 1469.8, B 1282.3; model uncertainty 0.0084
* Form inputs: days since last match A 51, B 167; matches on record A 251, B 14; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV08ARTVAN-ART  (YES = Bor Artnak)
Model: 78%
Kalshi: 57%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.009, surface_dev_loose -0.000, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
