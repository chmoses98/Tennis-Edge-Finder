# ASSISTED SLATE -- 2026-11-09T05:01Z (`SL-20261109T050151Z-4e27288a`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

132 open matches not seen started, 363 markets. Skipped: {"first_ball_already_observed": 1}. Sources: shadow board 2026-11-09T04:41:49.995294+00:00, Model 4 2026-11-09T04:42:02.371627+00:00, Gen-1 ledger 2026-11-09T04:41:46.108962+00:00, external 2026-11-09T04:10:12.608915+00:00, capture 20261109T040838Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-11-09 05:30Z**
* Recommended RUN TENNIS time: **2026-11-09 04:45Z**  (**OVERDUE -- run now**)
* Final price/status check time: **2026-11-09 05:20Z**
* Number of matches in window: 1 (Janice Tjen vs Magda Linette)

* **2 main-tour match(es) have NO verified start status** (START_UNKNOWN): BET blocked until a live status check.

Slate built 2026-11-09T05:01Z. Refresh due by: 2026-11-09 04:45Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 20, "HIGH_REVIEW": 32, "NORMAL": 171, "REVIEW": 39, "UNPRICED": 101}; match winners: {"EXTREME": 19, "HIGH_REVIEW": 27, "NORMAL": 92, "REVIEW": 30, "UNPRICED": 96}; quote freshness at build: {"STALE": 262}.

## Kosuke Ogura vs Hikaru Shiraishi -- ATP Challenger Matsuyama F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202113:202124:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kosuke Ogura (`KXATPCHALLENGERMATCH-26NOV08OGUSHI-OGU`) | 0.31 / 0.33 (9687) | 32.0% | 22.1% | 23.3% | 23.7% [22.5%-25.3%] | 26.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.9 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hikaru Shiraishi (`KXATPCHALLENGERMATCH-26NOV08OGUSHI-SHI`) | 0.68 / 0.69 (7202) | 68.5% | 77.9% | 76.7% | 76.3% [74.7%-77.5%] | 73.1% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +9.4 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3125.0, B 2976.0; serve-point win A 58.4%, B 35.6%; Elo A 1235.7, B 1438.1; model uncertainty 0.014
* Form inputs: days since last match A 202, B 55; matches on record A 245, B 210; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose -0.004, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Janice Tjen vs Magda Linette -- WTA Chennai F

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-08 16:00Z
* Current expected start: 2026-11-09 05:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-09 04:02Z
* Recommended handicap-by time: 2026-11-09 04:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+810_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-11-08T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202663:222145:2026-11-08`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Magda Linette (`KXWTAMATCH-26NOV08TJELIN-LIN`) | 0.35 / 0.37 (55804) | 36.0% | 41.5% | 23.5% | 29.7% [25.1%-42.3%] | -- | -- | -- | -- | PASS | +5.5 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Janice Tjen (`KXWTAMATCH-26NOV08TJELIN-TJE`) | 0.63 / 0.65 (33270) | 64.0% | 58.5% | 76.5% | 70.3% [57.7%-74.9%] | -- | -- | -- | -- | WATCH | -5.5 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3631.0, B 4278.0; serve-point win A 63.0%, B 38.7%; Elo A 1908.7, B 1884.3; model uncertainty 0.0861
* Form inputs: days since last match A 1, B 1; matches on record A 190, B 917; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose +0.004, surface_dev_tight +0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV08TJELIN-21` Over 20.5 games: 0.54/0.55 mid 54.5%, model 71.8% (projection_v2.0 (prediction ledger)) -- gap +17.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV08TJELIN-1-LIN` Will Magda Linette win set 1 in the Janice Tjen vs Magda Linette match: 0.25/0.38 mid 31.5%, model 44.3% (projection_v2.0 (prediction ledger)) -- gap +12.8 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26NOV08TJELIN-26` Over 25.5 games: 0.37/0.38 mid 37.5%, model 47.9% (projection_v2.0 (prediction ledger)) -- gap +10.4 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV08TJELIN-2-LIN` Will Magda Linette win set 2 in the Janice Tjen vs Magda Linette match: 0.19/0.55 mid 37.0%, model 44.3% (projection_v2.0 (prediction ledger)) -- gap +7.3 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV08TJELIN-1-TJE` Will Janice Tjen win set 1 in the Janice Tjen vs Magda Linette match: 0.59/0.64 mid 61.5%, model 55.7% (projection_v2.0 (prediction ledger)) -- gap -5.8 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26NOV08TJELIN-16` Over 15.5 games: 0.90/0.97 mid 93.5%, model 98.7% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV08TJELIN-2-TJE` Will Janice Tjen win set 2 in the Janice Tjen vs Magda Linette match: 0.26/0.80 mid 53.0%, model 55.7% (projection_v2.0 (prediction ledger)) -- gap +2.7 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Joel Schwaerzler vs Mitsuki Wei Kang Leong -- ATP Challenger Matsuyama 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 05:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T05:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211324:212082:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mitsuki Wei Kang Leong (`KXATPCHALLENGERMATCH-26NOV08SCHLEO-LEO`) | 0.23 / 0.25 (6669) | 24.0% | 34.5% | 52.0% | 44.5% [35.8%-49.0%] | -- | 24.0% | 24.0% | MODEL_LONE_OUTLIER | WATCH | +10.6 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Joel Schwaerzler (`KXATPCHALLENGERMATCH-26NOV08SCHLEO-SCH`) | 0.75 / 0.76 (151) | 75.5% | 65.5% | 48.0% | 55.5% [51.0%-64.2%] | -- | 76.7% | 76.7% | MODEL_LONE_OUTLIER | PASS | -10.1 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4824.0, B 3674.0; serve-point win A 64.9%, B 38.3%; Elo A 1597.8, B 1437.9; model uncertainty 0.0662
* Form inputs: days since last match A 34, B 55; matches on record A 178, B 204; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Alafia Ayeni vs Edward Winter -- ATP Challenger Brisbane 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200366:210399:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alafia Ayeni (`KXATPCHALLENGERMATCH-26NOV08AVEWIN-AVE`) | 0.32 / 0.35 (12275) | 33.5% | 44.3% | 38.4% | 41.9% [39.9%-43.4%] | 34.3% | 33.4% | 33.8% | MODEL_LONE_OUTLIER | SHADOW_BET | +10.8 pp | REVIEW | STALE | A / LIMITED | AGREES_WITH_KALSHI | AMBIGUOUS |
| Edward Winter (`KXATPCHALLENGERMATCH-26NOV08AVEWIN-WIN`) | 0.65 / 0.66 (88) | 65.5% | 55.7% | 61.6% | 58.1% [56.6%-60.1%] | 65.7% | 66.5% | 66.1% | MODEL_LONE_OUTLIER | PASS | -9.8 pp | NORMAL | STALE | A / LIMITED | AGREES_WITH_KALSHI | AMBIGUOUS |

* Serve evidence (points): A 3164.0, B 2901.0; serve-point win A 60.5%, B 38.4%; Elo A 1471.0, B 1485.9; model uncertainty 0.0175
* Form inputs: days since last match A 62, B 20; matches on record A 318, B 193; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.005, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Keegan Smith vs Yu Hsiou Hsu -- ATP Challenger Matsuyama 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 06:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T06:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200318:202333:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yu Hsiou Hsu (`KXATPCHALLENGERMATCH-26NOV08SMIHSU-HSU`) | 0.46 / 0.47 (23) | 46.5% | 46.1% | 37.0% | 40.8% [39.3%-42.7%] | -- | 46.8% | 46.8% | MODEL_LONE_OUTLIER | PASS | -0.5 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Keegan Smith (`KXATPCHALLENGERMATCH-26NOV08SMIHSU-SMI`) | 0.52 / 0.54 (5396) | 53.0% | 53.9% | 63.0% | 59.2% [57.3%-60.7%] | -- | 53.4% | 53.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +0.9 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5644.0, B 4484.0; serve-point win A 65.8%, B 35.0%; Elo A 1614.6, B 1627.3; model uncertainty 0.0167
* Form inputs: days since last match A 13, B 13; matches on record A 379, B 531; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## JiaYi Wang vs Himari Sato -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 06:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-09T06:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216156:265692:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Himari Sato (`KXITFWMATCH-26NOV08WANSAT-SAT`) | -- / 0.01 (64055) | -- | 7.8% | 1.5% | 12.0% [6.1%-20.0%] | -- | -- | -- | -- | PASS | -- | UNPRICED | STALE | C / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |
| JiaYi Wang (`KXITFWMATCH-26NOV08WANSAT-WAN`) | 0.99 / -- (0) | -- | 92.2% | 98.5% | 88.0% [80.0%-93.9%] | -- | -- | -- | -- | PASS | -- | UNPRICED | STALE | C / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 2216.0, B 578.0; serve-point win A 58.4%, B 52.2%; Elo A 1510.1, B 1280.3; model uncertainty 0.0696
* Form inputs: days since last match A 40, B 209; matches on record A 72, B 200; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high +0.000, surface_dev_loose +0.015, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Billy Harris vs Liam Broady -- ATP Challenger Matsuyama 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106281:126129:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liam Broady (`KXATPCHALLENGERMATCH-26NOV08HARBRO-BRO`) | 0.43 / 0.45 (5656) | 44.0% | 51.1% | 74.1% | 69.4% [62.4%-73.2%] | 44.6% | 43.7% | 44.1% | MODEL_LONE_OUTLIER | WATCH | +7.1 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Billy Harris (`KXATPCHALLENGERMATCH-26NOV08HARBRO-HAR`) | 0.56 / 0.57 (5474) | 56.5% | 48.9% | 25.9% | 30.6% [26.8%-37.6%] | 55.4% | 56.9% | 56.1% | MODEL_LONE_OUTLIER | PASS | -7.6 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5726.0, B 4694.0; serve-point win A 62.5%, B 37.3%; Elo A 1614.3, B 1640.6; model uncertainty 0.054
* Form inputs: days since last match A 13, B 13; matches on record A 638, B 951; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.013, surface_dev_loose -0.009, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Chengyiyi Yuan vs Belle Thompson -- W75 Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-09T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215134:259858:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Belle Thompson (`KXITFWMATCH-26NOV08YUATHO-THO`) | 0.49 / 0.50 (30208) | 49.5% | 23.9% | 21.5% | 24.3% [22.3%-28.7%] | -- | -- | -- | -- | PASS | -25.6 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Chengyiyi Yuan (`KXITFWMATCH-26NOV08YUATHO-YUA`) | 0.50 / 0.51 (2120) | 50.5% | 76.1% | 78.5% | 75.7% [71.3%-77.7%] | -- | -- | -- | -- | WATCH | +25.6 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2947.0, B 1699.0; serve-point win A 55.9%, B 49.4%; Elo A 1478.6, B 1312.7; model uncertainty 0.0322
* Form inputs: days since last match A 43, B 231; matches on record A 239, B 114; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV08YUATHO-YUA  (YES = Chengyiyi Yuan)
Model: 76%
Kalshi: 50%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.012, surface_dev_tight -0.017
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jay Dylan Hara Friend vs Yusuke Kusuhara -- ATP Challenger Matsuyama 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 07:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210221:211550:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jay Dylan Hara Friend (`KXATPCHALLENGERMATCH-26NOV08HARKUS-HAR`) | 0.93 / 0.94 (2053) | 93.5% | -- | 94.9% | 90.9% [85.2%-93.6%] | 91.4% | -- | 91.4% | KALSHI_LONE_OUTLIER | PASS | -2.6 pp | NORMAL | STALE | C / LIMITED | ALL_AGREE | VERIFIED |
| Yusuke Kusuhara (`KXATPCHALLENGERMATCH-26NOV08HARKUS-KUS`) | 0.06 / 0.07 (597) | 6.5% | -- | 5.1% | 9.1% [6.4%-14.8%] | 8.6% | -- | 8.6% | KALSHI_LONE_OUTLIER | WATCH | +2.6 pp | NORMAL | STALE | C / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 1896.0, B 1509.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0421
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.002, surface_pool_high -0.000, surface_dev_loose +0.013, surface_dev_tight -0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; STALE_QUOTE

## Yuzu Ishijima vs Natsuki Yoshimoto -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV08ISHYOS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuzu Ishijima (`KXITFWMATCH-26NOV08ISHYOS-ISH`) | 0.03 / 0.05 (459) | 4.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Natsuki Yoshimoto (`KXITFWMATCH-26NOV08ISHYOS-YOS`) | 0.93 / 0.98 (306) | 95.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nanari Katsumi vs Yuhan Wang -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-09T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:253679:264205:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nanari Katsumi (`KXITFWMATCH-26NOV08KATWAN-KAT`) | 0.04 / 0.05 (9523) | 4.5% | 20.0% | 28.7% | 28.3% [26.9%-30.1%] | -- | -- | -- | -- | WATCH | +15.4 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuhan Wang (`KXITFWMATCH-26NOV08KATWAN-WAN`) | 0.95 / 0.96 (7348) | 95.5% | 80.0% | 71.3% | 71.7% [69.9%-73.1%] | -- | -- | -- | -- | PASS | -15.4 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1096.0, B 1724.0; serve-point win A 50.5%, B 43.2%; Elo A 1260.6, B 1428.1; model uncertainty 0.0159
* Form inputs: days since last match A 231, B 39; matches on record A 139, B 44; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV08KATWAN-KAT  (YES = Nanari Katsumi)
Model: 20%
Kalshi: 4%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high -0.000, surface_dev_loose -0.013, surface_dev_tight +0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Priska Madelyn Nugroho vs Ayumi Miyamoto -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-09T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216316:221187:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ayumi Miyamoto (`KXITFWMATCH-26NOV08NUGMIY-MIY`) | 0.16 / 0.17 (7) | 16.5% | 28.2% | 51.1% | 38.9% [31.0%-44.1%] | -- | -- | -- | -- | WATCH | +11.7 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Priska Madelyn Nugroho (`KXITFWMATCH-26NOV08NUGMIY-NUG`) | 0.79 / 0.83 (155) | 81.0% | 71.8% | 48.9% | 61.1% [55.9%-69.0%] | -- | -- | -- | -- | PASS | -9.2 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2457.0, B 1256.0; serve-point win A 54.0%, B 50.2%; Elo A 1567.2, B 1420.7; model uncertainty 0.0656
* Form inputs: days since last match A 224, B 203; matches on record A 235, B 140; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.021, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Erika Sema vs Tiana Tian Deng -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-09T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:202454:260528:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tiana Tian Deng (`KXITFWMATCH-26NOV08SEMDEN-DEN`) | 0.51 / 0.54 (49) | 52.5% | 29.2% | 19.6% | 22.7% [20.0%-25.2%] | -- | -- | -- | -- | PASS | -23.3 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Erika Sema (`KXITFWMATCH-26NOV08SEMDEN-SEM`) | 0.46 / 0.50 (59) | 48.0% | 70.8% | 80.4% | 77.3% [74.8%-80.0%] | -- | -- | -- | -- | WATCH | +22.8 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1873.0, B 853.0; serve-point win A 55.4%, B 48.7%; Elo A 1485.0, B 1288.7; model uncertainty 0.0261
* Form inputs: days since last match A 196, B 126; matches on record A 930, B 41; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV08SEMDEN-SEM  (YES = Erika Sema)
Model: 71%
Kalshi: 48%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.012, surface_dev_tight -0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kareem Abdul Hakim vs Darcy Nicholls -- M15 Kuala Lumpur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08ABDNIC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kareem Abdul Hakim (`KXITFMATCH-26NOV08ABDNIC-ABD`) | 0.05 / 0.06 (490) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Darcy Nicholls (`KXITFMATCH-26NOV08ABDNIC-NIC`) | 0.94 / 0.95 (3459) | 94.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Finnian Bult vs Shaheed Alam -- M15 Kuala Lumpur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08BULALA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shaheed Alam (`KXITFMATCH-26NOV08BULALA-ALA`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Finnian Bult (`KXITFMATCH-26NOV08BULALA-BUL`) | -- / 0.01 (11431) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mohammad Farhanuddin Fariz vs Darrshan Suresh -- M15 Kuala Lumpur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08FARSUR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mohammad Farhanuddin Fariz (`KXITFMATCH-26NOV08FARSUR-FAR`) | 0.11 / 0.15 (1) | 13.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Darrshan Suresh (`KXITFMATCH-26NOV08FARSUR-SUR`) | 0.85 / 0.88 (13) | 86.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Konstantinos Loukopoulos vs Jerome Estephan -- M15 Kuala Lumpur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-09T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:214144:214325:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jerome Estephan (`KXITFMATCH-26NOV08LOUEST-EST`) | 0.60 / 0.61 (8625) | 60.5% | 64.3% | 63.6% | 51.0% [50.0%-52.6%] | 65.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.8 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Konstantinos Loukopoulos (`KXITFMATCH-26NOV08LOUEST-LOU`) | 0.39 / 0.40 (1425) | 39.5% | 35.7% | 36.4% | 49.0% [47.4%-50.0%] | 34.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.8 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 91.0, B 167.0; serve-point win A 59.5%, B 37.7%; Elo A 1220.6, B 1222.1; model uncertainty 0.0128
* Form inputs: days since last match A 342, B 209; matches on record A 2, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Azuma Visaya vs Maximus Zavier Wong -- M15 Kuala Lumpur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-09T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210405:212102:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Azuma Visaya (`KXITFMATCH-26NOV08VISWON-VIS`) | 0.99 / -- (0) | -- | 65.8% | 69.3% | 55.1% [54.1%-58.7%] | -- | -- | -- | -- | PASS | -- | UNPRICED | STALE | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |
| Maximus Zavier Wong (`KXITFMATCH-26NOV08VISWON-WON`) | -- / 0.01 (38558) | -- | 34.2% | 30.7% | 44.9% [41.3%-45.9%] | -- | -- | -- | -- | PASS | -- | UNPRICED | STALE | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 253.0, B 157.0; serve-point win A 61.4%, B 41.7%; Elo A 1230.0, B 1201.9; model uncertainty 0.0229
* Form inputs: days since last match A 349, B 202; matches on record A 11, B 5; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Natsumi Kawaguchi vs BoYoung Jeong -- W75 Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-09T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221109:221229:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BoYoung Jeong (`KXITFWMATCH-26NOV08KAWJEO-JEO`) | 0.85 / 0.87 (21812) | 86.0% | 58.7% | 70.4% | 64.1% [53.7%-68.5%] | -- | -- | -- | -- | PASS | -27.3 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Natsumi Kawaguchi (`KXITFWMATCH-26NOV08KAWJEO-KAW`) | 0.14 / 0.15 (20945) | 14.5% | 41.3% | 29.6% | 35.9% [31.5%-46.3%] | -- | -- | -- | -- | WATCH | +26.8 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2084.0, B 2517.0; serve-point win A 52.7%, B 45.7%; Elo A 1533.5, B 1565.2; model uncertainty 0.0738
* Form inputs: days since last match A 43, B 50; matches on record A 213, B 221; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV08KAWJEO-KAW  (YES = Natsumi Kawaguchi)
Model: 41%
Kalshi: 14%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.025, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hikaru Sato vs Jizelle Sibai -- W75 Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-09T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221141:270195:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hikaru Sato (`KXITFWMATCH-26NOV08SATSIB-SAT`) | 0.74 / 0.75 (722) | 74.5% | 58.6% | 60.9% | 58.4% [56.8%-60.4%] | -- | -- | -- | -- | PASS | -15.9 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jizelle Sibai (`KXITFWMATCH-26NOV08SATSIB-SIB`) | 0.24 / 0.25 (1445) | 24.5% | 41.4% | 39.1% | 41.6% [39.6%-43.2%] | -- | -- | -- | -- | PASS | +16.9 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1807.0, B 571.0; serve-point win A 57.7%, B 44.0%; Elo A 1465.8, B 1415.0; model uncertainty 0.0178
* Form inputs: days since last match A 203, B 273; matches on record A 175, B 11; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV08SATSIB-SIB  (YES = Jizelle Sibai)
Model: 41%
Kalshi: 24%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kuan-Shou Chen vs Dharma Pantaratorn -- M15 Hua Hin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08CHEPAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kuan-Shou Chen (`KXITFMATCH-26NOV08CHEPAN-CHE`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dharma Pantaratorn (`KXITFMATCH-26NOV08CHEPAN-PAN`) | -- / 0.01 (31764) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ren Nakamura vs Perawat Sukjai -- M15 Hua Hin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08NAKSUK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ren Nakamura (`KXITFMATCH-26NOV08NAKSUK-NAK`) | 0.97 / 0.98 (202) | 97.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Perawat Sukjai (`KXITFMATCH-26NOV08NAKSUK-SUK`) | 0.01 / 0.02 (1045) | 1.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nazar Oliynykov vs Rishabhdev Rajshekar Raman -- M15 Hua Hin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-09T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212138:213581:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nazar Oliynykov (`KXITFMATCH-26NOV08OLIRAJ-OLI`) | 0.98 / 0.99 (9042) | 98.5% | 30.6% | 23.2% | 36.7% [34.8%-36.7%] | -- | -- | -- | -- | PASS | -67.9 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rishabhdev Rajshekar Raman (`KXITFMATCH-26NOV08OLIRAJ-RAJ`) | 0.01 / 0.02 (1654) | 1.5% | 69.4% | 76.8% | 63.3% [63.3%-65.1%] | -- | -- | -- | -- | PASS | +67.9 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 203.0, B 0.0; serve-point win A 56.2%, B 39.9%; Elo A 1114.2, B 1216.6; model uncertainty 0.009
* Form inputs: days since last match A 237, B 720; matches on record A 8, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV08OLIRAJ-RAJ  (YES = Rishabhdev Rajshekar Raman)
Model: 69%
Kalshi: 2%
Gap: +68 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tsz Fu Wong vs Guntinun Sootinun-Opart -- M15 Hua Hin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-09T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210655:212971:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Guntinun Sootinun-Opart (`KXITFMATCH-26NOV08WONSOO-SOO`) | 0.07 / 0.08 (5559) | 7.5% | 68.8% | 86.2% | 71.4% [70.5%-71.5%] | -- | -- | -- | -- | PASS | +61.4 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Tsz Fu Wong (`KXITFMATCH-26NOV08WONSOO-WON`) | 0.91 / 0.92 (12) | 91.5% | 31.1% | 13.8% | 28.6% [28.5%-29.5%] | -- | -- | -- | -- | PASS | -60.4 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 498.0, B 0.0; serve-point win A 58.9%, B 37.2%; Elo A 1070.2, B 1223.6; model uncertainty 0.0048
* Form inputs: days since last match A 51, B 797; matches on record A 20, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV08WONSOO-SOO  (YES = Guntinun Sootinun-Opart)
Model: 69%
Kalshi: 8%
Gap: +61 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.009, surface_dev_loose +0.000, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jiangxue Han vs Kisa Yoshioka -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-09T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215616:220497:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jiangxue Han (`KXITFWMATCH-26NOV08HANYOS-HAN`) | 0.51 / 0.55 (105) | 53.0% | 58.6% | 44.6% | 54.3% [51.6%-60.6%] | -- | -- | -- | -- | PASS | +5.6 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kisa Yoshioka (`KXITFWMATCH-26NOV08HANYOS-YOS`) | 0.42 / 0.48 (100) | 45.0% | 41.4% | 55.4% | 45.7% [39.4%-48.4%] | -- | -- | -- | -- | PASS | -3.6 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1410.0, B 1530.0; serve-point win A 50.5%, B 51.1%; Elo A 1458.9, B 1360.1; model uncertainty 0.0449
* Form inputs: days since last match A 196, B 203; matches on record A 174, B 159; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.011, surface_dev_loose -0.011, surface_dev_tight +0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Riko Kikawada vs Mutsumi Uemura -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-09T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260828:262883:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Riko Kikawada (`KXITFWMATCH-26NOV08KIKUEM-KIK`) | 0.18 / 0.21 (137) | 19.5% | 32.3% | 35.4% | 41.0% [38.9%-43.1%] | -- | -- | -- | -- | PASS | +12.8 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mutsumi Uemura (`KXITFWMATCH-26NOV08KIKUEM-UEM`) | 0.76 / 0.83 (6) | 79.5% | 67.7% | 64.6% | 59.0% [56.9%-61.1%] | -- | -- | -- | -- | PASS | -11.8 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 892.0, B 824.0; serve-point win A 50.7%, B 45.9%; Elo A 1273.1, B 1314.4; model uncertainty 0.0209
* Form inputs: days since last match A 245, B 203; matches on record A 79, B 22; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.016, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuno Kitahara vs Hiroko Kuwata -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-09T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206075:263881:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuno Kitahara (`KXITFWMATCH-26NOV08KITKUW-KIT`) | 0.78 / 0.83 (100) | 80.5% | 69.8% | 83.9% | 69.0% [59.0%-74.9%] | -- | -- | -- | -- | PASS | -10.7 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hiroko Kuwata (`KXITFWMATCH-26NOV08KITKUW-KUW`) | 0.15 / 0.18 (5) | 16.5% | 30.2% | 16.1% | 31.0% [25.1%-41.0%] | -- | -- | -- | -- | WATCH | +13.7 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2068.0, B 1256.0; serve-point win A 54.5%, B 49.4%; Elo A 1428.6, B 1407.9; model uncertainty 0.0793
* Form inputs: days since last match A 203, B 44; matches on record A 119, B 756; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.019, surface_dev_loose +0.009, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ena Shibahara vs Ayane Sagawa -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV08SHISAG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ayane Sagawa (`KXITFWMATCH-26NOV08SHISAG-SAG`) | 0.02 / 0.03 (22478) | 2.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ena Shibahara (`KXITFWMATCH-26NOV08SHISAG-SHI`) | 0.97 / 0.98 (445) | 97.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Max Benaim vs Congsup Congcar -- M15 Hua Hin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-09T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:133667:206299:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Max Benaim (`KXITFMATCH-26NOV08BENCON-BEN`) | 0.48 / 0.59 (1) | 53.5% | 40.9% | 75.1% | 51.6% [49.0%-53.6%] | -- | -- | -- | -- | PASS | -12.6 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Congsup Congcar (`KXITFMATCH-26NOV08BENCON-CON`) | 0.37 / 0.45 (62) | 41.0% | 59.1% | 24.9% | 48.4% [46.4%-51.0%] | -- | -- | -- | -- | PASS | +18.1 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 150.0, B 318.0; serve-point win A 58.2%, B 40.0%; Elo A 1117.4, B 1122.8; model uncertainty 0.0233
* Form inputs: days since last match A 608, B 300; matches on record A 24, B 121; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV08BENCON-CON  (YES = Congsup Congcar)
Model: 59%
Kalshi: 41%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jayson Blando vs Jules Melot -- M15 Kuala Lumpur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08BLAMEL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jayson Blando (`KXITFMATCH-26NOV08BLAMEL-BLA`) | 0.59 / 0.64 (29) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jules Melot (`KXITFMATCH-26NOV08BLAMEL-MEL`) | 0.37 / 0.42 (13) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vraj Gohil vs Vitek Horak -- M15 Hua Hin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08GOHHOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vraj Gohil (`KXITFMATCH-26NOV08GOHHOR-GOH`) | 0.32 / 0.34 (139) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vitek Horak (`KXITFMATCH-26NOV08GOHHOR-HOR`) | 0.62 / 0.68 (100) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hendrik Thada Grohbruegge vs Penn Charusorn -- M15 Hua Hin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-09T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:214094:214228:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Penn Charusorn (`KXITFMATCH-26NOV08GROCHA-CHA`) | 0.47 / 0.52 (100) | 49.5% | 46.3% | 46.4% | 42.8% [42.8%-43.3%] | -- | -- | -- | -- | PASS | -3.2 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hendrik Thada Grohbruegge (`KXITFMATCH-26NOV08GROCHA-GRO`) | 0.49 / 0.51 (100) | 50.0% | 53.7% | 53.6% | 57.2% [56.7%-57.2%] | -- | -- | -- | -- | PASS | +3.7 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 96.0, B 193.0; serve-point win A 60.2%, B 40.5%; Elo A 1250.1, B 1198.6; model uncertainty 0.0025
* Form inputs: days since last match A 377, B 377; matches on record A 1, B 5; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kazuma Kawachi vs Daniel Wright -- M15 Kuala Lumpur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08KAWWRI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kazuma Kawachi (`KXITFMATCH-26NOV08KAWWRI-KAW`) | 0.89 / 0.90 (104) | 89.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daniel Wright (`KXITFMATCH-26NOV08KAWWRI-WRI`) | 0.10 / 0.13 (105) | 11.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aditya Kothari vs Hong-Lin Fu -- M15 Hua Hin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08KOTFUX:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hong-Lin Fu (`KXITFMATCH-26NOV08KOTFUX-FUX`) | 0.94 / 0.96 (258) | 95.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aditya Kothari (`KXITFMATCH-26NOV08KOTFUX-KOT`) | 0.05 / 0.06 (187) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eshant Patra vs Ryo Minakata -- M15 Kuala Lumpur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08PATMIN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ryo Minakata (`KXITFMATCH-26NOV08PATMIN-MIN`) | 0.92 / 0.95 (23) | 93.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eshant Patra (`KXITFMATCH-26NOV08PATMIN-PAT`) | 0.03 / 0.10 (25) | 6.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gunawan Trismuwantara vs Harshit Yadav -- M15 Kuala Lumpur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08TRIYAD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gunawan Trismuwantara (`KXITFMATCH-26NOV08TRIYAD-TRI`) | 0.93 / 0.96 (22) | 94.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Harshit Yadav (`KXITFMATCH-26NOV08TRIYAD-YAD`) | 0.05 / 0.06 (636) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Natsuki Yamamoto vs Vishal Vasudev M -- M15 Kuala Lumpur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV08YAMVAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vishal Vasudev M (`KXITFMATCH-26NOV08YAMVAS-VAS`) | 0.06 / 0.24 (2) | 15.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Natsuki Yamamoto (`KXITFMATCH-26NOV08YAMVAS-YAM`) | 0.71 / 0.91 (3) | 81.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mayuka Aikawa vs Karen Tsutsumi -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-09T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:219892:223271:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mayuka Aikawa (`KXITFWMATCH-26NOV08AIKTSU-AIK`) | 0.94 / 0.95 (19) | 94.5% | 71.9% | 51.1% | 62.5% [57.9%-68.4%] | -- | -- | -- | -- | PASS | -22.6 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Karen Tsutsumi (`KXITFWMATCH-26NOV08AIKTSU-TSU`) | 0.05 / 0.07 (450) | 6.0% | 28.1% | 48.9% | 37.5% [31.6%-42.1%] | -- | -- | -- | -- | PASS | +22.1 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1667.0, B 138.0; serve-point win A 57.8%, B 46.6%; Elo A 1428.9, B 1333.7; model uncertainty 0.0526
* Form inputs: days since last match A 231, B 525; matches on record A 303, B 22; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV08AIKTSU-TSU  (YES = Karen Tsutsumi)
Model: 28%
Kalshi: 6%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.049, surface_pool_high -0.046, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Haruna Arakawa vs Kamonwan Yodpetch -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-09T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214505:259907:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Haruna Arakawa (`KXITFWMATCH-26NOV08ARAYOD-ARA`) | 0.39 / 0.42 (1) | 40.5% | 67.7% | 69.0% | 71.3% [70.3%-72.6%] | -- | -- | -- | -- | PASS | +27.2 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kamonwan Yodpetch (`KXITFWMATCH-26NOV08ARAYOD-YOD`) | 0.57 / 0.60 (6) | 58.5% | 32.3% | 31.1% | 28.7% [27.4%-29.6%] | -- | -- | -- | -- | PASS | -26.2 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2195.0, B 1037.0; serve-point win A 55.7%, B 47.8%; Elo A 1502.0, B 1326.6; model uncertainty 0.0113
* Form inputs: days since last match A 371, B 196; matches on record A 411, B 72; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV08ARAYOD-ARA  (YES = Haruna Arakawa)
Model: 68%
Kalshi: 40%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.009, surface_dev_loose +0.013, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Michika Ozeki vs Nagi Hanatani -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-09T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:210537:211544:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nagi Hanatani (`KXITFWMATCH-26NOV08OZEHAN-HAN`) | 0.45 / 0.48 (66) | 46.5% | 42.1% | 17.1% | 29.1% [21.1%-44.1%] | -- | -- | -- | -- | PASS | -4.3 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Michika Ozeki (`KXITFWMATCH-26NOV08OZEHAN-OZE`) | 0.49 / 0.53 (100) | 51.0% | 57.9% | 82.9% | 70.9% [55.9%-78.9%] | -- | -- | -- | -- | WATCH | +6.8 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2363.0, B 1219.0; serve-point win A 53.4%, B 48.1%; Elo A 1389.6, B 1328.0; model uncertainty 0.1154
* Form inputs: days since last match A 196, B 196; matches on record A 490, B 446; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.028, surface_pool_high +0.022, surface_dev_loose +0.009, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Shiho Tsujioka vs Sae Noguchi -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-09T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:263801:269866:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sae Noguchi (`KXITFWMATCH-26NOV08TSUNOG-NOG`) | 0.52 / 0.56 (122) | 54.0% | 58.7% | 53.2% | 56.9% [55.9%-58.5%] | -- | -- | -- | -- | PASS | +4.7 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Shiho Tsujioka (`KXITFWMATCH-26NOV08TSUNOG-TSU`) | 0.43 / 0.46 (103) | 44.5% | 41.3% | 46.8% | 43.1% [41.5%-44.1%] | -- | -- | -- | -- | PASS | -3.2 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1131.0, B 1076.0; serve-point win A 49.8%, B 48.6%; Elo A 1383.7, B 1452.4; model uncertainty 0.0131
* Form inputs: days since last match A 16, B 210; matches on record A 43, B 33; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.011, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oleksii Krutykh vs Oskari Paldanius -- ATP Challenger Hersonissos F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208071:213619:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oleksii Krutykh (`KXATPCHALLENGERMATCH-26NOV09KRUPAL-KRU`) | 0.54 / 0.55 (68) | 54.5% | -- | 65.5% | 67.8% [64.6%-71.8%] | 55.4% | 53.8% | 53.8% | MODEL_LONE_OUTLIER | WATCH | +13.3 pp | REVIEW | STALE | C / LIMITED | EXTERNAL_STALE | VERIFIED |
| Oskari Paldanius (`KXATPCHALLENGERMATCH-26NOV09KRUPAL-PAL`) | 0.44 / 0.46 (1117) | 45.0% | -- | 34.5% | 32.2% [28.2%-35.4%] | 44.6% | 46.3% | 46.3% | MODEL_LONE_OUTLIER | PASS | -12.8 pp | REVIEW | STALE | C / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3078.0, B 1146.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0363
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.023, surface_pool_high -0.033, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Jack Loge vs Odysseas Geladaris -- ATP Challenger Hersonissos F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211504:214243:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Odysseas Geladaris (`KXATPCHALLENGERMATCH-26NOV09LOGGEL-GEL`) | 0.14 / 0.15 (39) | 14.5% | -- | 21.1% | 20.8% [18.3%-24.3%] | 16.4% | 15.0% | -- | INSUFFICIENT_INPUTS | PASS | +6.3 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jack Loge (`KXATPCHALLENGERMATCH-26NOV09LOGGEL-LOG`) | 0.85 / 0.86 (1082) | 85.5% | -- | 78.8% | 79.2% [75.7%-81.7%] | 83.6% | 85.8% | -- | INSUFFICIENT_INPUTS | PASS | -6.3 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3551.0, B 188.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.03
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.022, surface_pool_high -0.035, surface_dev_loose +0.001, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Benjamin Pietri vs Alexander Vasilev -- ATP Challenger Hersonissos F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202125:211651:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Benjamin Pietri (`KXATPCHALLENGERMATCH-26NOV09PIEVAS-PIE`) | 0.62 / 0.63 (1337) | 62.5% | -- | 61.8% | 48.4% [41.3%-54.7%] | 61.6% | 61.1% | -- | INSUFFICIENT_INPUTS | PASS | -14.1 pp | REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexander Vasilev (`KXATPCHALLENGERMATCH-26NOV09PIEVAS-VAS`) | 0.37 / 0.39 (733) | 38.0% | -- | 38.2% | 51.6% [45.3%-58.7%] | 38.4% | 38.7% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +13.6 pp | REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1540.0, B 1101.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0671
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.021, surface_dev_loose +0.016, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Alex Michelsen vs Yannick Hanfmann -- ATP Stockholm 1/16 F

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-09 14:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-09 11:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-09 04:02Z
* Recommended handicap-by time: 2026-11-09 10:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-11-09T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105870:210506:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yannick Hanfmann (`KXATPMATCH-26NOV09MICHAN-HAN`) | 0.25 / 0.26 (385) | 25.5% | 25.6% | 35.8% | 33.5% [30.9%-36.2%] | 26.7% | 26.2% | 26.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +0.1 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Alex Michelsen (`KXATPMATCH-26NOV09MICHAN-MIC`) | 0.74 / 0.75 (18043) | 74.5% | 74.4% | 64.2% | 66.5% [63.8%-69.1%] | 73.4% | 74.4% | 73.9% | MODEL_LONE_OUTLIER | PASS | -0.1 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5855.0, B 5300.0; serve-point win A 69.3%, B 36.1%; Elo A 1963.8, B 1782.6; model uncertainty 0.0265
* Form inputs: days since last match A 5, B 8; matches on record A 320, B 707; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.027, surface_pool_high +0.026, surface_dev_loose +0.008, surface_dev_tight -0.013
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV09MICHAN-19` Over 18.5 games: 0.78/0.79 mid 78.5%, model 88.3% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV09MICHAN-24` Over 23.5 games: 0.40/0.42 mid 41.0%, model 50.6% (projection_v2.0 (prediction ledger)) -- gap +9.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV09MICHAN-MIC7` Will Alex Michelsen win at least 6.5 more games than Yannick Hanfmann?: 0.14/0.18 mid 16.0%, model 7.3% (projection_v2.0 (prediction ledger)) -- gap -8.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09MICHAN-MIC20` Will Alex Michelsen win the Alex Michelsen vs Yannick Hanfmann match by a set score of 2-0?: 0.52/0.53 mid 52.5%, model 44.8% (projection_v2.0 (prediction ledger)) -- gap -7.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV09MICHAN-MIC4` Will Alex Michelsen win at least 3.5 more games than Yannick Hanfmann?: 0.51/0.52 mid 51.5%, model 44.6% (projection_v2.0 (prediction ledger)) -- gap -6.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV09MICHAN-29` Over 28.5 games: 0.27/0.29 mid 28.0%, model 34.7% (projection_v2.0 (prediction ledger)) -- gap +6.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09MICHAN-MIC21` Will Alex Michelsen win the Alex Michelsen vs Yannick Hanfmann match by a set score of 2-1?: 0.21/0.25 mid 23.0%, model 29.6% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV09MICHAN-2-MIC` Will Alex Michelsen win set 2 in the Alex Michelsen vs Yannick Hanfmann match: 0.46/0.81 mid 63.5%, model 66.9% (projection_v2.0 (prediction ledger)) -- gap +3.4 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09MICHAN-HAN21` Will Yannick Hanfmann win the Alex Michelsen vs Yannick Hanfmann match by a set score of 2-1?: 0.11/0.13 mid 12.0%, model 14.6% (projection_v2.0 (prediction ledger)) -- gap +2.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09MICHAN-HAN20` Will Yannick Hanfmann win the Alex Michelsen vs Yannick Hanfmann match by a set score of 2-0?: 0.12/0.14 mid 13.0%, model 10.9% (projection_v2.0 (prediction ledger)) -- gap -2.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV09MICHAN-HAN2` Will Yannick Hanfmann win at least 1.5 more games than Alex Michelsen?: 0.19/0.22 mid 20.5%, model 19.4% (projection_v2.0 (prediction ledger)) -- gap -1.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV09MICHAN-1-HAN` Will Yannick Hanfmann win set 1 in the Alex Michelsen vs Yannick Hanfmann match: 0.31/0.33 mid 32.0%, model 33.1% (projection_v2.0 (prediction ledger)) -- gap +1.1 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV09MICHAN-1-MIC` Will Alex Michelsen win set 1 in the Alex Michelsen vs Yannick Hanfmann match: 0.67/0.69 mid 68.0%, model 66.9% (projection_v2.0 (prediction ledger)) -- gap -1.1 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV09MICHAN-2-HAN` Will Yannick Hanfmann win set 2 in the Alex Michelsen vs Yannick Hanfmann match: 0.15/0.49 mid 32.0%, model 33.1% (projection_v2.0 (prediction ledger)) -- gap +1.1 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## James Duckworth vs Cameron Norrie -- ATP Stockholm 1/16 F

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-09 14:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-09 12:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-09 04:02Z
* Recommended handicap-by time: 2026-11-09 11:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-11-09T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105902:111815:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| James Duckworth (`KXATPMATCH-26NOV09DUCNOR-DUC`) | 0.30 / 0.31 (90) | 30.5% | 28.8% | 43.2% | 40.4% [38.5%-41.3%] | 30.9% | 30.8% | 30.8% | MODEL_LONE_OUTLIER | SHADOW_BET | -1.7 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Cameron Norrie (`KXATPMATCH-26NOV09DUCNOR-NOR`) | 0.69 / 0.70 (10933) | 69.5% | 71.2% | 56.8% | 59.6% [58.7%-61.5%] | 69.1% | 69.5% | 69.5% | MODEL_LONE_OUTLIER | PASS | +1.7 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 6236.0, B 5450.0; serve-point win A 64.0%, B 31.4%; Elo A 1744.4, B 1889.6; model uncertainty 0.0143
* Form inputs: days since last match A 9, B 6; matches on record A 942, B 681; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight +0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26NOV09DUCNOR-NOR21` Will Cameron Norrie win the James Duckworth vs Cameron Norrie match by a set score of 2-1?: 0.03/0.26 mid 14.5%, model 29.5% (projection_v2.0 (prediction ledger)) -- gap +15.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09DUCNOR-DUC21` Will James Duckworth win the James Duckworth vs Cameron Norrie match by a set score of 2-1?: 0.13/0.44 mid 28.5%, model 16.2% (projection_v2.0 (prediction ledger)) -- gap -12.3 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV09DUCNOR-2-NOR` Will Cameron Norrie win set 2 in the James Duckworth vs Cameron Norrie match: 0.34/0.78 mid 56.0%, model 64.5% (projection_v2.0 (prediction ledger)) -- gap +8.5 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV09DUCNOR-23` Over 22.5 games: 0.51/0.52 mid 51.5%, model 59.7% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV09DUCNOR-28` Over 27.5 games: 0.31/0.34 mid 32.5%, model 39.5% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV09DUCNOR-18` Over 17.5 games: 0.87/0.91 mid 89.0%, model 94.0% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV09DUCNOR-NOR4` Will Cameron Norrie win at least 3.5 more games than James Duckworth?: 0.46/0.47 mid 46.5%, model 41.6% (projection_v2.0 (prediction ledger)) -- gap -4.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV09DUCNOR-DUC2` Will James Duckworth win at least 1.5 more games than Cameron Norrie?: 0.25/0.27 mid 26.0%, model 22.2% (projection_v2.0 (prediction ledger)) -- gap -3.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV09DUCNOR-2-DUC` Will James Duckworth win set 2 in the James Duckworth vs Cameron Norrie match: 0.19/0.59 mid 39.0%, model 35.5% (projection_v2.0 (prediction ledger)) -- gap -3.5 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09DUCNOR-DUC20` Will James Duckworth win the James Duckworth vs Cameron Norrie match by a set score of 2-0?: 0.15/0.17 mid 16.0%, model 12.6% (projection_v2.0 (prediction ledger)) -- gap -3.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09DUCNOR-NOR20` Will Cameron Norrie win the James Duckworth vs Cameron Norrie match by a set score of 2-0?: 0.44/0.46 mid 45.0%, model 41.6% (projection_v2.0 (prediction ledger)) -- gap -3.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV09DUCNOR-1-NOR` Will Cameron Norrie win set 1 in the James Duckworth vs Cameron Norrie match: 0.63/0.65 mid 64.0%, model 64.5% (projection_v2.0 (prediction ledger)) -- gap +0.5 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV09DUCNOR-1-DUC` Will James Duckworth win set 1 in the James Duckworth vs Cameron Norrie match: 0.34/0.37 mid 35.5%, model 35.5% (projection_v2.0 (prediction ledger)) -- gap -0.0 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Vladyslav Orlov vs Lorenzo Angelini -- ATP Challenger Hersonissos F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:149117:200550:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Angelini (`KXATPCHALLENGERMATCH-26NOV09ORLANG-ANG`) | 0.57 / 0.58 (2044) | 57.5% | 59.9% | 62.0% | 56.3% [46.3%-61.0%] | 55.4% | 57.7% | 57.7% | MODEL_LONE_OUTLIER | PASS | +2.4 pp | NORMAL | STALE | B / LIMITED | EXTERNAL_STALE | VERIFIED |
| Vladyslav Orlov (`KXATPCHALLENGERMATCH-26NOV09ORLANG-ORL`) | 0.43 / 0.45 (1760) | 44.0% | 40.1% | 38.0% | 43.7% [39.0%-53.7%] | 44.6% | 43.2% | -- | INSUFFICIENT_INPUTS | PASS | -3.9 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3570.0, B 2397.0; serve-point win A 54.6%, B 43.5%; Elo A 1391.2, B 1370.3; model uncertainty 0.0733
* Form inputs: days since last match A 195, B 202; matches on record A 550, B 69; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.021, surface_dev_loose -0.047, surface_dev_tight +0.042
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Buvaysar Gadamauri vs Ugo Blanchet -- ATP Challenger Orleans F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200259:207527:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ugo Blanchet (`KXATPCHALLENGERMATCH-26NOV09GADBLA-BLA`) | 0.63 / 0.64 (1418) | 63.5% | 52.5% | 38.0% | 43.2% [40.8%-47.5%] | 61.6% | 63.3% | 63.3% | MODEL_LONE_OUTLIER | PASS | -11.0 pp | REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Buvaysar Gadamauri (`KXATPCHALLENGERMATCH-26NOV09GADBLA-GAD`) | 0.37 / 0.38 (1111) | 37.5% | 47.5% | 62.1% | 56.8% [52.5%-59.2%] | 38.4% | 37.2% | 37.2% | MODEL_LONE_OUTLIER | WATCH | +10.0 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4560.0, B 4311.0; serve-point win A 65.3%, B 34.2%; Elo A 1574.5, B 1638.2; model uncertainty 0.0338
* Form inputs: days since last match A 27, B 13; matches on record A 312, B 393; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.005, surface_dev_loose +0.009, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Benjamin Kittay vs Adrien Gobat -- ATP Challenger Orleans F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210254:210296:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrien Gobat (`KXATPCHALLENGERMATCH-26NOV09KITGOB-GOB`) | 0.75 / 0.77 (1094) | 76.0% | -- | 67.0% | 79.0% [77.9%-79.8%] | 75.0% | 76.7% | 75.0% | MARKETS_AGREE | PASS | +3.0 pp | NORMAL | STALE | F / POOR | ALL_AGREE | VERIFIED |
| Benjamin Kittay (`KXATPCHALLENGERMATCH-26NOV09KITGOB-KIT`) | 0.23 / 0.25 (4434) | 24.0% | -- | 33.0% | 21.0% [20.2%-22.1%] | 25.0% | 23.4% | 25.0% | MARKETS_AGREE | PASS | -3.0 pp | NORMAL | STALE | F / POOR | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 203.0, B 2410.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0097
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.007, surface_dev_loose +0.001, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Adolfo Daniel Vallejo vs Ugo Humbert -- ATP Stockholm 1/16 F

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-09 14:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-09 13:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-09 04:02Z
* Recommended handicap-by time: 2026-11-09 12:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-11-09T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200005:209226:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ugo Humbert (`KXATPMATCH-26NOV09VALHUM-HUM`) | 0.67 / 0.68 (7444) | 67.5% | 67.0% | 66.3% | 69.5% [68.1%-71.2%] | 67.6% | 68.3% | 67.9% | MODEL_LONE_OUTLIER | PASS | -0.5 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Adolfo Daniel Vallejo (`KXATPMATCH-26NOV09VALHUM-VAL`) | 0.33 / 0.34 (29831) | 33.5% | 33.0% | 33.7% | 30.6% [28.8%-31.9%] | 32.4% | 31.8% | 32.1% | MODEL_LONE_OUTLIER | PASS | -0.6 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5609.0, B 4891.0; serve-point win A 62.8%, B 33.6%; Elo A 1709.4, B 1935.1; model uncertainty 0.0152
* Form inputs: days since last match A 6, B 5; matches on record A 232, B 627; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose -0.012, surface_dev_tight +0.012
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26NOV09VALHUM-HUM7` Will Ugo Humbert win at least 6.5 more games than Adolfo Daniel Vallejo?: 0.06/0.35 mid 20.5%, model 7.2% (projection_v2.0 (prediction ledger)) -- gap -13.3 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV09VALHUM-23` Over 22.5 games: 0.46/0.47 mid 46.5%, model 59.3% (projection_v2.0 (prediction ledger)) -- gap +12.8 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV09VALHUM-28` Over 27.5 games: 0.27/0.30 mid 28.5%, model 39.3% (projection_v2.0 (prediction ledger)) -- gap +10.8 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV09VALHUM-18` Over 17.5 games: 0.85/0.87 mid 86.0%, model 93.1% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09VALHUM-HUM20` Will Ugo Humbert win the Adolfo Daniel Vallejo vs Ugo Humbert match by a set score of 2-0?: 0.44/0.46 mid 45.0%, model 37.9% (projection_v2.0 (prediction ledger)) -- gap -7.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV09VALHUM-HUM4` Will Ugo Humbert win at least 3.5 more games than Adolfo Daniel Vallejo?: 0.46/0.48 mid 47.0%, model 39.9% (projection_v2.0 (prediction ledger)) -- gap -7.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV09VALHUM-2-VAL` Will Adolfo Daniel Vallejo win set 2 in the Adolfo Daniel Vallejo vs Ugo Humbert match: 0.15/0.48 mid 31.5%, model 38.4% (projection_v2.0 (prediction ledger)) -- gap +6.9 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09VALHUM-HUM21` Will Ugo Humbert win the Adolfo Daniel Vallejo vs Ugo Humbert match by a set score of 2-1?: 0.20/0.25 mid 22.5%, model 29.1% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09VALHUM-VAL21` Will Adolfo Daniel Vallejo win the Adolfo Daniel Vallejo vs Ugo Humbert match by a set score of 2-1?: 0.12/0.15 mid 13.5%, model 18.2% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09VALHUM-VAL20` Will Adolfo Daniel Vallejo win the Adolfo Daniel Vallejo vs Ugo Humbert match by a set score of 2-0?: 0.16/0.19 mid 17.5%, model 14.8% (projection_v2.0 (prediction ledger)) -- gap -2.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV09VALHUM-1-HUM` Will Ugo Humbert win set 1 in the Adolfo Daniel Vallejo vs Ugo Humbert match: 0.63/0.65 mid 64.0%, model 61.6% (projection_v2.0 (prediction ledger)) -- gap -2.4 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV09VALHUM-1-VAL` Will Adolfo Daniel Vallejo win set 1 in the Adolfo Daniel Vallejo vs Ugo Humbert match: 0.35/0.37 mid 36.0%, model 38.4% (projection_v2.0 (prediction ledger)) -- gap +2.4 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV09VALHUM-2-HUM` Will Ugo Humbert win set 2 in the Adolfo Daniel Vallejo vs Ugo Humbert match: 0.47/0.81 mid 64.0%, model 61.6% (projection_v2.0 (prediction ledger)) -- gap -2.4 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV09VALHUM-VAL2` Will Adolfo Daniel Vallejo win at least 1.5 more games than Ugo Humbert?: 0.25/0.27 mid 26.0%, model 26.2% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Massimo Giunta vs Francesco Forti -- ATP Challenger Hersonissos 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209506:210668:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesco Forti (`KXATPCHALLENGERMATCH-26NOV09GIUFOR-FOR`) | 0.44 / 0.45 (1639) | 44.5% | 54.5% | 47.1% | 50.5% [48.1%-55.4%] | 43.7% | 45.7% | 44.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +10.0 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Massimo Giunta (`KXATPCHALLENGERMATCH-26NOV09GIUFOR-GIU`) | 0.55 / 0.56 (1419) | 55.5% | 45.5% | 52.9% | 49.5% [44.6%-51.9%] | 56.3% | 54.4% | 55.4% | MODEL_LONE_OUTLIER | PASS | -10.0 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3654.0, B 3864.0; serve-point win A 66.6%, B 32.5%; Elo A 1449.7, B 1516.4; model uncertainty 0.0363
* Form inputs: days since last match A 20, B 20; matches on record A 179, B 429; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose +0.010, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Johannus Monday vs Georgii Kravchenko -- ATP Challenger Hersonissos 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206662:208902:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Georgii Kravchenko (`KXATPCHALLENGERMATCH-26NOV09MONKRA-KRA`) | 0.55 / 0.56 (2555) | 55.5% | -- | 51.9% | 43.3% [38.6%-46.2%] | 54.1% | 53.5% | 53.8% | MODEL_LONE_OUTLIER | PASS | -12.2 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Johannus Monday (`KXATPCHALLENGERMATCH-26NOV09MONKRA-MON`) | 0.44 / 0.45 (5) | 44.5% | -- | 48.1% | 56.7% [53.8%-61.4%] | 45.9% | 46.6% | 46.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +12.2 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3169.0, B 3083.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0378
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.029, surface_pool_high +0.028, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Arthur Rinderknech vs Miomir Kecmanovic -- ATP Stockholm 1/16 F

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-09 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-09 04:02Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-10T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-11-09T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126239:200175:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miomir Kecmanovic (`KXATPMATCH-26NOV09RINKEC-KEC`) | 0.33 / 0.35 (11668) | 34.0% | 45.5% | 41.5% | 41.9% [41.0%-42.9%] | -- | -- | -- | -- | SHADOW_BET | +11.5 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Arthur Rinderknech (`KXATPMATCH-26NOV09RINKEC-RIN`) | 0.65 / 0.66 (98) | 65.5% | 54.5% | 58.5% | 58.1% [57.1%-59.0%] | -- | -- | -- | -- | PASS | -11.0 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5481.0, B 5445.0; serve-point win A 68.2%, B 32.8%; Elo A 1830.2, B 1771.1; model uncertainty 0.0093
* Form inputs: days since last match A 4, B 8; matches on record A 572, B 619; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.009, surface_dev_loose +0.009, surface_dev_tight -0.009
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26NOV09RINKEC-RIN3` Will Arthur Rinderknech win at least 2.5 more games than Miomir Kecmanovic?: 0.51/0.54 mid 52.5%, model 36.8% (projection_v2.0 (prediction ledger)) -- gap -15.7 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09RINKEC-RIN20` Will Arthur Rinderknech win the Arthur Rinderknech vs Miomir Kecmanovic match by a set score of 2-0?: 0.41/0.43 mid 42.0%, model 28.1% (projection_v2.0 (prediction ledger)) -- gap -13.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV09RINKEC-23` Over 22.5 games: 0.54/0.55 mid 54.5%, model 66.4% (projection_v2.0 (prediction ledger)) -- gap +11.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV09RINKEC-RIN6` Will Arthur Rinderknech win at least 5.5 more games than Miomir Kecmanovic?: 0.15/0.18 mid 16.5%, model 6.2% (projection_v2.0 (prediction ledger)) -- gap -10.3 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV09RINKEC-28` Over 27.5 games: 0.34/0.36 mid 35.0%, model 44.8% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV09RINKEC-1-KEC` Will Miomir Kecmanovic win set 1 in the Arthur Rinderknech vs Miomir Kecmanovic match: 0.37/0.40 mid 38.5%, model 47.0% (projection_v2.0 (prediction ledger)) -- gap +8.5 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09RINKEC-KEC21` Will Miomir Kecmanovic win the Arthur Rinderknech vs Miomir Kecmanovic match by a set score of 2-1?: 0.14/0.16 mid 15.0%, model 23.4% (projection_v2.0 (prediction ledger)) -- gap +8.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV09RINKEC-KEC2` Will Miomir Kecmanovic win at least 1.5 more games than Arthur Rinderknech?: 0.27/0.31 mid 29.0%, model 37.2% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV09RINKEC-1-RIN` Will Arthur Rinderknech win set 1 in the Arthur Rinderknech vs Miomir Kecmanovic match: 0.60/0.62 mid 61.0%, model 53.0% (projection_v2.0 (prediction ledger)) -- gap -8.0 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV09RINKEC-18` Over 17.5 games: 0.86/0.93 mid 89.5%, model 96.7% (projection_v2.0 (prediction ledger)) -- gap +7.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV09RINKEC-2-RIN` Will Arthur Rinderknech win set 2 in the Arthur Rinderknech vs Miomir Kecmanovic match: 0.13/0.80 mid 46.5%, model 53.0% (projection_v2.0 (prediction ledger)) -- gap +6.5 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09RINKEC-KEC20` Will Miomir Kecmanovic win the Arthur Rinderknech vs Miomir Kecmanovic match by a set score of 2-0?: 0.17/0.19 mid 18.0%, model 22.1% (projection_v2.0 (prediction ledger)) -- gap +4.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09RINKEC-RIN21` Will Arthur Rinderknech win the Arthur Rinderknech vs Miomir Kecmanovic match by a set score of 2-1?: 0.23/0.25 mid 24.0%, model 26.4% (projection_v2.0 (prediction ledger)) -- gap +2.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV09RINKEC-2-KEC` Will Miomir Kecmanovic win set 2 in the Arthur Rinderknech vs Miomir Kecmanovic match: 0.13/0.80 mid 46.5%, model 47.0% (projection_v2.0 (prediction ledger)) -- gap +0.5 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Holger Rune vs Zizou Bergs -- ATP Stockholm 1/16 F

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-09 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-09 04:02Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-10T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-11-09T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200267:208029:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zizou Bergs (`KXATPMATCH-26NOV09RUNBER-BER`) | 0.41 / 0.42 (93) | 41.5% | 43.9% | 52.0% | 45.6% [42.2%-48.0%] | -- | -- | -- | -- | WATCH | +2.4 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Holger Rune (`KXATPMATCH-26NOV09RUNBER-RUN`) | 0.58 / 0.59 (600) | 58.5% | 56.1% | 48.0% | 54.4% [52.0%-57.8%] | -- | -- | -- | -- | PASS | -2.4 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3214.0, B 5882.0; serve-point win A 66.2%, B 35.1%; Elo A 1959.8, B 1830.4; model uncertainty 0.0292
* Form inputs: days since last match A 6, B 7; matches on record A 449, B 573; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.005, surface_dev_loose -0.000, surface_dev_tight +0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV09RUNBER-24` Over 23.5 games: 0.46/0.47 mid 46.5%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap +9.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV09RUNBER-2-RUN` Will Holger Rune win set 2 in the Holger Rune vs Zizou Bergs match: 0.16/0.78 mid 47.0%, model 54.1% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV09RUNBER-RUN5` Will Holger Rune win at least 4.5 more games than Zizou Bergs?: 0.23/0.26 mid 24.5%, model 17.5% (projection_v2.0 (prediction ledger)) -- gap -7.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV09RUNBER-RUN2` Will Holger Rune win at least 1.5 more games than Zizou Bergs?: 0.52/0.54 mid 53.0%, model 48.2% (projection_v2.0 (prediction ledger)) -- gap -4.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09RUNBER-RUN20` Will Holger Rune win the Holger Rune vs Zizou Bergs match by a set score of 2-0?: 0.33/0.35 mid 34.0%, model 29.2% (projection_v2.0 (prediction ledger)) -- gap -4.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09RUNBER-RUN21` Will Holger Rune win the Holger Rune vs Zizou Bergs match by a set score of 2-1?: 0.20/0.25 mid 22.5%, model 26.9% (projection_v2.0 (prediction ledger)) -- gap +4.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09RUNBER-BER21` Will Zizou Bergs win the Holger Rune vs Zizou Bergs match by a set score of 2-1?: 0.17/0.20 mid 18.5%, model 22.8% (projection_v2.0 (prediction ledger)) -- gap +4.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV09RUNBER-2-BER` Will Zizou Bergs win set 2 in the Holger Rune vs Zizou Bergs match: 0.21/0.77 mid 49.0%, model 45.9% (projection_v2.0 (prediction ledger)) -- gap -3.1 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV09RUNBER-29` Over 28.5 games: 0.32/0.41 mid 36.5%, model 38.3% (projection_v2.0 (prediction ledger)) -- gap +1.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV09RUNBER-19` Over 18.5 games: 0.85/0.93 mid 89.0%, model 90.5% (projection_v2.0 (prediction ledger)) -- gap +1.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV09RUNBER-1-BER` Will Zizou Bergs win set 1 in the Holger Rune vs Zizou Bergs match: 0.43/0.46 mid 44.5%, model 45.9% (projection_v2.0 (prediction ledger)) -- gap +1.4 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09RUNBER-BER20` Will Zizou Bergs win the Holger Rune vs Zizou Bergs match by a set score of 2-0?: 0.22/0.23 mid 22.5%, model 21.1% (projection_v2.0 (prediction ledger)) -- gap -1.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV09RUNBER-1-RUN` Will Holger Rune win set 1 in the Holger Rune vs Zizou Bergs match: 0.54/0.56 mid 55.0%, model 54.1% (projection_v2.0 (prediction ledger)) -- gap -0.9 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV09RUNBER-BER2` Will Zizou Bergs win at least 1.5 more games than Holger Rune?: 0.35/0.39 mid 37.0%, model 36.2% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Erik Grevelius / Adam Heinonen vs Sadio Doumbia / David Pel -- ATP Stockholm 1/8 F

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-09 17:30Z
* Current expected start: 2026-11-09 14:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-09 04:02Z
* Recommended handicap-by time: 2026-11-09 13:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-09T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09GREHEIDOUPEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sadio Doumbia / David Pel (`KXATPDOUBLES-26NOV09GREHEIDOUPEL-DOUPEL`) | 0.59 / 0.62 (267) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Erik Grevelius / Adam Heinonen (`KXATPDOUBLES-26NOV09GREHEIDOUPEL-GREHEI`) | 0.37 / 0.40 (29) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Edas Butvilas vs Cosme Rolland de Ravel -- ATP Challenger Orleans F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210220:213977:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Edas Butvilas (`KXATPCHALLENGERMATCH-26NOV09BUTROL-BUT`) | 0.53 / 0.54 (218) | 53.5% | -- | 70.3% | 69.8% [67.1%-72.1%] | 53.1% | 54.4% | -- | INSUFFICIENT_INPUTS | WATCH | +16.3 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Cosme Rolland de Ravel (`KXATPCHALLENGERMATCH-26NOV09BUTROL-ROL`) | 0.46 / 0.47 (84) | 46.5% | -- | 29.7% | 30.2% [27.9%-32.9%] | 46.9% | 47.5% | -- | INSUFFICIENT_INPUTS | PASS | -16.3 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4862.0, B 625.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0247
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV09BUTROL-BUT  (YES = Edas Butvilas)
Model: 70%
Kalshi: 54%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.017, surface_pool_high -0.018, surface_dev_loose -0.000, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Branko Djuric vs Nicolas Tepmahc -- ATP Challenger Monastir F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208168:210025:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Branko Djuric (`KXATPCHALLENGERMATCH-26NOV09DJUTEP-DJU`) | 0.64 / 0.66 (1193) | 65.0% | -- | 66.4% | 65.5% [63.5%-67.3%] | 63.8% | 63.5% | -- | INSUFFICIENT_INPUTS | PASS | +0.5 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nicolas Tepmahc (`KXATPCHALLENGERMATCH-26NOV09DJUTEP-TEP`) | 0.34 / 0.36 (2054) | 35.0% | -- | 33.6% | 34.5% [32.7%-36.5%] | 36.2% | 35.3% | -- | INSUFFICIENT_INPUTS | PASS | -0.5 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2635.0, B 3348.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0189
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.019, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE

## John Echeverria vs Guillaume Dalmasso -- ATP Challenger Monastir F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208126:211409:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Guillaume Dalmasso (`KXATPCHALLENGERMATCH-26NOV09ECHDAL-DAL`) | 0.24 / 0.26 (19) | 25.0% | -- | 16.1% | 19.4% [16.7%-25.0%] | 26.5% | 22.8% | -- | INSUFFICIENT_INPUTS | PASS | -5.6 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| John Echeverria (`KXATPCHALLENGERMATCH-26NOV09ECHDAL-ECH`) | 0.74 / 0.77 (2383) | 75.5% | -- | 83.9% | 80.6% [75.0%-83.3%] | 73.5% | 76.4% | 76.4% | MODEL_LONE_OUTLIER | WATCH | +5.1 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 2252.0, B 3044.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0416
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.003, surface_dev_loose +0.010, surface_dev_tight -0.018
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Yannik Kelm vs Pedro Vives Marcos -- ATP Challenger Monastir F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206325:212025:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yannik Kelm (`KXATPCHALLENGERMATCH-26NOV09KELVIV-KEL`) | 0.30 / 0.32 (2018) | 31.0% | -- | 26.9% | 24.4% [20.6%-26.9%] | 32.3% | 33.5% | 32.9% | MODEL_LONE_OUTLIER | PASS | -6.6 pp | NORMAL | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Pedro Vives Marcos (`KXATPCHALLENGERMATCH-26NOV09KELVIV-VIV`) | 0.68 / 0.70 (485) | 69.0% | -- | 73.1% | 75.6% [73.1%-79.4%] | 67.7% | 67.9% | 67.8% | MODEL_LONE_OUTLIER | WATCH | +6.6 pp | NORMAL | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2489.0, B 1701.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0314
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.024, surface_pool_high +0.025, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; STALE_QUOTE

## Alina Nesmianovych vs Capucine Dournes -- W15 Paris R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV09NESDOU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Capucine Dournes (`KXITFWMATCH-26NOV09NESDOU-DOU`) | 0.31 / 0.36 (91) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alina Nesmianovych (`KXITFWMATCH-26NOV09NESDOU-NES`) | 0.63 / 0.65 (24) | 64.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stefaniya Pushkar vs Anna Burchak -- W15 Paris R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-09T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:265040:270253:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Burchak (`KXITFWMATCH-26NOV09PUSBUR-BUR`) | 0.76 / 0.78 (172) | 77.0% | 37.3% | 37.3% | 39.8% [37.9%-40.8%] | 73.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -39.7 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Stefaniya Pushkar (`KXITFWMATCH-26NOV09PUSBUR-PUS`) | 0.21 / 0.24 (26) | 22.5% | 62.7% | 62.7% | 60.2% [59.2%-62.1%] | 26.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +40.2 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 897.0, B 191.0; serve-point win A 60.7%, B 41.8%; Elo A 1293.6, B 1224.9; model uncertainty 0.0143
* Form inputs: days since last match A 196, B 385; matches on record A 23, B 3; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV09PUSBUR-PUS  (YES = Stefaniya Pushkar)
Model: 63%
Kalshi: 22%
Gap: +40 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Summer Yardley vs Capucine Cedillo- Vayson de Pradenne -- W15 Paris R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-09T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216405:266808:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Capucine Cedillo- Vayson de Pradenne (`KXITFWMATCH-26NOV09YARCED-CED`) | 0.66 / 0.68 (143) | 67.0% | 58.2% | 89.0% | 64.6% [64.6%-65.6%] | 59.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.8 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Summer Yardley (`KXITFWMATCH-26NOV09YARCED-YAR`) | 0.33 / 0.35 (117) | 34.0% | 41.8% | 11.0% | 35.4% [34.4%-35.4%] | 40.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.8 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 504.0, B 0.0; serve-point win A 53.0%, B 45.5%; Elo A 1108.4, B 1216.2; model uncertainty 0.0049
* Form inputs: days since last match A 392, B 966; matches on record A 80, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ryan Peniston vs Henry Searle -- ATP Challenger Hersonissos 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126106:211902:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ryan Peniston (`KXATPCHALLENGERMATCH-26NOV09PENSEA-PEN`) | 0.27 / 0.28 (3278) | 27.5% | -- | 32.9% | 39.5% [36.6%-43.5%] | 28.4% | 28.2% | 28.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +12.0 pp | REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Henry Searle (`KXATPCHALLENGERMATCH-26NOV09PENSEA-SEA`) | 0.72 / 0.73 (1067) | 72.5% | -- | 67.2% | 60.5% [56.5%-63.4%] | 71.6% | 72.8% | 72.8% | MODEL_LONE_OUTLIER | PASS | -12.0 pp | REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 2785.0, B 4437.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0343
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Hanna Bougouffa vs Ninon Carpentier -- W15 Paris R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-09T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:230121:270156:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hanna Bougouffa (`KXITFWMATCH-26NOV09BOUCAR-BOU`) | 0.48 / 0.49 (59) | 48.5% | 71.2% | 51.1% | 58.5% [57.4%-60.5%] | -- | -- | -- | -- | PASS | +22.7 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ninon Carpentier (`KXITFWMATCH-26NOV09BOUCAR-CAR`) | 0.48 / 0.51 (108) | 49.5% | 28.8% | 48.9% | 41.5% [39.5%-42.6%] | -- | -- | -- | -- | PASS | -20.7 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 245.0, B 188.0; serve-point win A 55.4%, B 48.8%; Elo A 1259.9, B 1190.2; model uncertainty 0.0155
* Form inputs: days since last match A 469, B 308; matches on record A 134, B 4; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV09BOUCAR-BOU  (YES = Hanna Bougouffa)
Model: 71%
Kalshi: 48%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.011, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amelie Brooks vs Coline Briand -- W15 Paris R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-09T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259608:266697:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Coline Briand (`KXITFWMATCH-26NOV09BROBRI-BRI`) | 0.25 / 0.32 (29) | 28.5% | 44.6% | 39.4% | 48.9% [46.8%-48.9%] | 31.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +16.1 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amelie Brooks (`KXITFWMATCH-26NOV09BROBRI-BRO`) | 0.64 / 0.71 (270) | 67.5% | 55.4% | 60.6% | 51.1% [51.1%-53.2%] | 68.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.1 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 164.0, B 73.0; serve-point win A 53.6%, B 47.4%; Elo A 1211.6, B 1206.6; model uncertainty 0.0107
* Form inputs: days since last match A 196, B 294; matches on record A 19, B 11; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV09BROBRI-BRI  (YES = Coline Briand)
Model: 45%
Kalshi: 28%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Francesca Parcelli vs Teodora Vlajic -- W15 Paris R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV09PARVLA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesca Parcelli (`KXITFWMATCH-26NOV09PARVLA-PAR`) | 0.79 / 0.82 (65) | 80.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Teodora Vlajic (`KXITFWMATCH-26NOV09PARVLA-VLA`) | 0.14 / 0.18 (235) | 16.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nino Ehrenschneider vs Mae Malige -- ATP Challenger Monastir F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209510:211898:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nino Ehrenschneider (`KXATPCHALLENGERMATCH-26NOV09EHRMAL-EHR`) | 0.48 / 0.50 (23) | 49.0% | -- | 54.1% | 48.4% [46.4%-51.0%] | 50.0% | 49.3% | -- | INSUFFICIENT_INPUTS | PASS | -0.6 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mae Malige (`KXATPCHALLENGERMATCH-26NOV09EHRMAL-MAL`) | 0.51 / 0.52 (276) | 51.5% | -- | 45.9% | 51.5% [49.0%-53.6%] | 50.0% | 52.2% | -- | INSUFFICIENT_INPUTS | PASS | +0.1 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3493.0, B 2579.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0232
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.021, surface_dev_loose -0.005, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Semen Pankin vs Maxime Janvier -- ATP Challenger Monastir F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126125:208431:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maxime Janvier (`KXATPCHALLENGERMATCH-26NOV09PANJAN-JAN`) | 0.60 / 0.61 (78) | 60.5% | -- | 33.2% | 38.8% [35.1%-45.1%] | 59.2% | 61.4% | 61.4% | MODEL_LONE_OUTLIER | PASS | -21.7 pp | HIGH_REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Semen Pankin (`KXATPCHALLENGERMATCH-26NOV09PANJAN-PAN`) | 0.39 / 0.41 (256) | 40.0% | -- | 66.8% | 61.2% [54.9%-64.9%] | 40.8% | 41.6% | -- | INSUFFICIENT_INPUTS | WATCH | +21.2 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3375.0, B 4068.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0499
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV09PANJAN-PAN  (YES = Semen Pankin)
Model: 61%
Kalshi: 40%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.005, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Toufik Sahtali vs Nikolai Barsukov -- ATP Challenger Monastir F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200086:213062:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikolai Barsukov (`KXATPCHALLENGERMATCH-26NOV09SAHBAR-BAR`) | 0.47 / 0.49 (2056) | 48.0% | -- | 33.8% | 37.7% [35.3%-44.3%] | 48.0% | 47.2% | -- | INSUFFICIENT_INPUTS | PASS | -10.3 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Toufik Sahtali (`KXATPCHALLENGERMATCH-26NOV09SAHBAR-SAH`) | 0.51 / 0.54 (334) | 52.5% | -- | 66.2% | 62.3% [55.7%-64.7%] | 52.0% | 52.9% | -- | INSUFFICIENT_INPUTS | WATCH | +9.8 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3339.0, B 2385.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0453
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.005, surface_dev_loose -0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Tomas Martin Etcheverry vs Max Dahlin -- ATP Stockholm 1/16 F

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-09 20:00Z
* Current expected start: 2026-11-09 17:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-09 04:02Z
* Recommended handicap-by time: 2026-11-09 16:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-11-09T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144869:211609:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Max Dahlin (`KXATPMATCH-26NOV09ETCDAH-DAH`) | 0.23 / 0.24 (12389) | 23.5% | -- | 22.3% | 13.6% [10.1%-17.5%] | 24.5% | 23.0% | 23.8% | MODEL_LONE_OUTLIER | PASS | -9.9 pp | NORMAL | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Tomas Martin Etcheverry (`KXATPMATCH-26NOV09ETCDAH-ETC`) | 0.76 / 0.77 (5) | 76.5% | -- | 77.7% | 86.4% [82.5%-90.0%] | 75.5% | 76.4% | 75.9% | MODEL_LONE_OUTLIER | WATCH | +9.9 pp | NORMAL | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5577.0, B 651.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0371
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.017, surface_pool_high -0.022, surface_dev_loose -0.000, surface_dev_tight -0.002
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPEXACTMATCH-26NOV09ETCDAH-DAH21` Will Max Dahlin win the Tomas Martin Etcheverry vs Max Dahlin match by a set score of 2-1?: 0.04/0.78 mid 41.0%, model 13.7% (market_conditioned_v1 (model4_board_v1)) -- gap -27.3 pp, EXTREME, DATA_WARNING, quote STALE, identity VERIFIED, data LIMITED
  * `KXATPEXACTMATCH-26NOV09ETCDAH-ETC20` Will Tomas Martin Etcheverry win the Tomas Martin Etcheverry vs Max Dahlin match by a set score of 2-0?: 0.02/0.53 mid 27.5%, model 46.7% (market_conditioned_v1 (model4_board_v1)) -- gap +19.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data LIMITED
  * `KXATPEXACTMATCH-26NOV09ETCDAH-DAH20` Will Max Dahlin win the Tomas Martin Etcheverry vs Max Dahlin match by a set score of 2-0?: 0.04/0.48 mid 26.0%, model 10.0% (market_conditioned_v1 (model4_board_v1)) -- gap -16.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data LIMITED
  * `KXATPGTOTAL-26NOV09ETCDAH-23` Over 22.5 games: 0.47/0.50 mid 48.5%, model 57.8% (market_conditioned_v1 (model4_board_v1)) -- gap +9.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
  * `KXATPGSPREAD-26NOV09ETCDAH-ETC7` Will Tomas Martin Etcheverry win at least 6.5 more games than Max Dahlin?: 0.11/0.20 mid 15.5%, model 7.5% (market_conditioned_v1 (model4_board_v1)) -- gap -8.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
  * `KXATPGTOTAL-26NOV09ETCDAH-28` Over 27.5 games: 0.28/0.32 mid 30.0%, model 37.6% (market_conditioned_v1 (model4_board_v1)) -- gap +7.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
  * `KXATPGTOTAL-26NOV09ETCDAH-18` Over 17.5 games: 0.81/0.93 mid 87.0%, model 93.5% (market_conditioned_v1 (model4_board_v1)) -- gap +6.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
  * `KXATPGSPREAD-26NOV09ETCDAH-ETC4` Will Tomas Martin Etcheverry win at least 3.5 more games than Max Dahlin?: 0.51/0.53 mid 52.0%, model 46.0% (market_conditioned_v1 (model4_board_v1)) -- gap -6.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
  * `KXATPEXACTMATCH-26NOV09ETCDAH-ETC21` Will Tomas Martin Etcheverry win the Tomas Martin Etcheverry vs Max Dahlin match by a set score of 2-1?: 0.21/0.29 mid 25.0%, model 29.6% (market_conditioned_v1 (model4_board_v1)) -- gap +4.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
  * `KXATPGSPREAD-26NOV09ETCDAH-DAH2` Will Max Dahlin win at least 1.5 more games than Tomas Martin Etcheverry?: 0.16/0.23 mid 19.5%, model 17.8% (market_conditioned_v1 (model4_board_v1)) -- gap -1.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; LOW_DATA_QUALITY; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Karol Malirz vs Salvador Monteiro -- M25 Vale do Lobo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-09T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:148670:214260:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karol Malirz (`KXITFMATCH-26NOV09MALMON-MAL`) | 0.59 / 0.66 (100) | 62.5% | 38.2% | 60.2% | 46.4% [42.8%-50.5%] | -- | -- | -- | -- | PASS | -24.3 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Salvador Monteiro (`KXITFMATCH-26NOV09MALMON-MON`) | 0.36 / 0.37 (114) | 36.5% | 61.8% | 39.8% | 53.6% [49.5%-57.2%] | -- | -- | -- | -- | PASS | +25.3 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 410.0, B 279.0; serve-point win A 58.6%, B 39.0%; Elo A 1195.6, B 1239.4; model uncertainty 0.0385
* Form inputs: days since last match A 195, B 258; matches on record A 14, B 5; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV09MALMON-MON  (YES = Salvador Monteiro)
Model: 62%
Kalshi: 36%
Gap: +25 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pierre Antoine Tailleu vs Alex Kobelt -- M25 Vale do Lobo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-09T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206895:210032:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex Kobelt (`KXITFMATCH-26NOV09TAIKOB-KOB`) | 0.40 / 0.44 (194) | 42.0% | -- | 35.4% | 40.2% [36.0%-43.9%] | -- | -- | -- | -- | PASS | -1.9 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pierre Antoine Tailleu (`KXITFMATCH-26NOV09TAIKOB-TAI`) | 0.59 / 0.60 (145) | 59.5% | -- | 64.6% | 59.9% [56.1%-64.0%] | -- | -- | -- | -- | PASS | +0.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 742.0, B 619.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0396
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.019, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jade Groen vs Malkia Ngounoue -- W15 Paris R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV09GRONGO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jade Groen (`KXITFWMATCH-26NOV09GRONGO-GRO`) | 0.50 / 0.56 (238) | 53.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Malkia Ngounoue (`KXITFWMATCH-26NOV09GRONGO-NGO`) | 0.42 / 0.46 (124) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Meline Lataste vs Amahee Charrier -- W15 Paris R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV09LATCHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amahee Charrier (`KXITFWMATCH-26NOV09LATCHA-CHA`) | 0.45 / 0.47 (128) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Meline Lataste (`KXITFWMATCH-26NOV09LATCHA-LAT`) | 0.53 / 0.54 (5) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gonzalo Bueno vs Thiago Seyboth Wild -- ATP Challenger Lima 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:205734:208293:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gonzalo Bueno (`KXATPCHALLENGERMATCH-26NOV09BUESEY-BUE`) | 0.16 / 0.17 (21) | 16.5% | -- | 12.6% | 16.7% [13.9%-21.2%] | -- | -- | -- | -- | PASS | +0.1 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Thiago Seyboth Wild (`KXATPCHALLENGERMATCH-26NOV09BUESEY-SEY`) | 0.81 / 0.87 (33) | 84.0% | -- | 87.5% | 83.4% [78.8%-86.1%] | -- | -- | -- | -- | PASS | -0.7 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4809.0, B 4921.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0363
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.013, surface_dev_tight +0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE

## Marco Cecchinato vs Francisco Comesana -- ATP Challenger Lima 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106065:207681:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marco Cecchinato (`KXATPCHALLENGERMATCH-26NOV09CECCOM-CEC`) | 0.37 / 0.46 (51) | 41.5% | -- | 48.5% | 45.5% [40.5%-47.0%] | -- | -- | -- | -- | PASS | +4.0 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Francisco Comesana (`KXATPCHALLENGERMATCH-26NOV09CECCOM-COM`) | 0.57 / 0.59 (51) | 58.0% | -- | 51.5% | 54.5% [53.0%-59.5%] | -- | -- | -- | -- | PASS | -3.5 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5742.0, B 5246.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0322
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Liam Draxl vs Duncan Chan -- ATP Challenger Knoxville 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208119:211673:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Duncan Chan (`KXATPCHALLENGERMATCH-26NOV09DRACHA-CHA`) | 0.21 / 0.25 (9) | 23.0% | -- | 18.1% | 14.9% [14.3%-15.8%] | 25.0% | 22.9% | -- | INSUFFICIENT_INPUTS | PASS | -8.1 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Liam Draxl (`KXATPCHALLENGERMATCH-26NOV09DRACHA-DRA`) | 0.73 / 0.79 (63) | 76.0% | -- | 81.9% | 85.1% [84.2%-85.7%] | 75.0% | 76.3% | -- | INSUFFICIENT_INPUTS | PASS | +9.1 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4925.0, B 890.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0075
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alexis Galarneau vs Stefan Kozlov -- ATP Challenger Knoxville 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111578:200008:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexis Galarneau (`KXATPCHALLENGERMATCH-26NOV09GALKOZ-GAL`) | 0.39 / 0.46 (98) | 42.5% | -- | 46.4% | 51.5% [49.0%-53.6%] | -- | -- | -- | -- | PASS | +9.1 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Stefan Kozlov (`KXATPCHALLENGERMATCH-26NOV09GALKOZ-KOZ`) | 0.54 / 0.59 (51) | 56.5% | -- | 53.6% | 48.4% [46.4%-51.0%] | -- | -- | -- | -- | PASS | -8.1 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5304.0, B 3563.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0233
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.010, surface_dev_loose -0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Marcos Giron vs Maks Kasnikowski -- ATP Challenger Knoxville 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106218:209874:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcos Giron (`KXATPCHALLENGERMATCH-26NOV09GIRKAS-GIR`) | 0.59 / 0.64 (56) | 61.5% | -- | 38.3% | 46.5% [43.1%-52.5%] | -- | -- | -- | -- | PASS | -15.0 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maks Kasnikowski (`KXATPCHALLENGERMATCH-26NOV09GIRKAS-KAS`) | 0.35 / 0.41 (48) | 38.0% | -- | 61.7% | 53.5% [47.5%-56.9%] | -- | -- | -- | -- | SHADOW_BET | +15.5 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4763.0, B 4928.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0469
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV09GIRKAS-KAS  (YES = Maks Kasnikowski)
Model: 53%
Kalshi: 38%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.005, surface_dev_loose -0.015, surface_dev_tight +0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE

## Alastair Gray vs Darwin Blanch -- ATP Challenger Knoxville 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202400:210464:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Darwin Blanch (`KXATPCHALLENGERMATCH-26NOV09GRABLA-BLA`) | 0.68 / 0.74 (53) | 71.0% | -- | 43.1% | 49.5% [45.6%-56.4%] | -- | -- | -- | -- | PASS | -21.5 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alastair Gray (`KXATPCHALLENGERMATCH-26NOV09GRABLA-GRA`) | 0.28 / 0.31 (33) | 29.5% | -- | 56.9% | 50.5% [43.6%-54.4%] | -- | -- | -- | -- | WATCH | +21.0 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3694.0, B 4745.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0539
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV09GRABLA-GRA  (YES = Alastair Gray)
Model: 50%
Kalshi: 30%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE

## Zdenek Kolar vs Joao Lucas Reis Da Silva -- ATP Challenger Lima 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144645:206307:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zdenek Kolar (`KXATPCHALLENGERMATCH-26NOV09KOLREI-KOL`) | 0.32 / 0.33 (65) | 32.5% | -- | 48.4% | 46.9% [46.4%-47.9%] | -- | -- | -- | -- | SHADOW_BET | +14.4 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Joao Lucas Reis Da Silva (`KXATPCHALLENGERMATCH-26NOV09KOLREI-REI`) | 0.64 / 0.74 (53) | 69.0% | -- | 51.5% | 53.1% [52.1%-53.6%] | -- | -- | -- | -- | PASS | -15.9 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5521.0, B 4979.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0077
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Sandro Kopp vs Luka Mikrut -- ATP Challenger Monastir 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207491:210053:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sandro Kopp (`KXATPCHALLENGERMATCH-26NOV09KOPMIK-KOP`) | 0.27 / 0.29 (1654) | 28.0% | -- | 44.0% | 42.1% [37.7%-46.0%] | 28.9% | 28.0% | 28.9% | MODEL_LONE_OUTLIER | SHADOW_BET | +14.1 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Luka Mikrut (`KXATPCHALLENGERMATCH-26NOV09KOPMIK-MIK`) | 0.71 / 0.72 (1028) | 71.5% | -- | 56.0% | 57.9% [54.0%-62.3%] | 71.1% | 72.7% | 71.1% | MODEL_LONE_OUTLIER | PASS | -13.6 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4878.0, B 3647.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0418
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.040, surface_dev_tight -0.029
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Marcel Latak vs Clement Chidekh -- ATP Challenger Knoxville 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206889:214269:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Clement Chidekh (`KXATPCHALLENGERMATCH-26NOV09LATCHI-CHI`) | 0.95 / 0.97 (474) | 96.0% | -- | 93.5% | 93.2% [92.1%-93.5%] | 90.5% | 95.3% | 92.9% | KALSHI_LONE_OUTLIER | PASS | -2.8 pp | NORMAL | STALE | F / POOR | ALL_AGREE | VERIFIED |
| Marcel Latak (`KXATPCHALLENGERMATCH-26NOV09LATCHI-LAT`) | 0.03 / 0.07 (200) | 5.0% | -- | 6.5% | 6.8% [6.5%-7.9%] | 9.5% | 8.5% | 9.5% | KALSHI_LONE_OUTLIER | PASS | +1.8 pp | NORMAL | STALE | F / POOR | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 53.0, B 5040.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.007
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.003, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Aidan Mayo vs Michael Mmoh -- ATP Challenger Knoxville 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111581:208854:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aidan Mayo (`KXATPCHALLENGERMATCH-26NOV09MAYMMO-MAY`) | 0.55 / 0.57 (58) | 56.0% | -- | 49.0% | 42.9% [39.0%-44.9%] | -- | -- | -- | -- | PASS | -13.1 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Michael Mmoh (`KXATPCHALLENGERMATCH-26NOV09MAYMMO-MMO`) | 0.40 / 0.47 (105) | 43.5% | -- | 51.0% | 57.1% [55.1%-61.0%] | -- | -- | -- | -- | PASS | +13.6 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3926.0, B 3733.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0298
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.010, surface_dev_loose +0.005, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Nicolas Mejia vs Jack Kennedy -- ATP Challenger Knoxville 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200711:213605:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jack Kennedy (`KXATPCHALLENGERMATCH-26NOV09MEJKEN-KEN`) | 0.32 / 0.36 (12) | 34.0% | -- | 45.8% | 42.7% [36.3%-45.3%] | 34.8% | 33.9% | 34.8% | MODEL_LONE_OUTLIER | WATCH | +8.7 pp | NORMAL | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Nicolas Mejia (`KXATPCHALLENGERMATCH-26NOV09MEJKEN-MEJ`) | 0.64 / 0.67 (5) | 65.5% | -- | 54.2% | 57.3% [54.7%-63.7%] | 65.1% | 66.2% | 65.1% | MODEL_LONE_OUTLIER | PASS | -8.2 pp | NORMAL | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5047.0, B 2751.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.045
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.021, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Facundo Mena vs Max Alcala Gurri -- ATP Challenger Lima 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106057:208024:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Max Alcala Gurri (`KXATPCHALLENGERMATCH-26NOV09MENALC-ALC`) | 0.68 / 0.72 (45) | 70.0% | -- | 76.3% | 72.1% [66.6%-75.1%] | -- | 70.2% | -- | INSUFFICIENT_INPUTS | PASS | +2.1 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Facundo Mena (`KXATPCHALLENGERMATCH-26NOV09MENALC-MEN`) | 0.27 / 0.32 (10) | 29.5% | -- | 23.7% | 27.9% [24.9%-33.4%] | -- | 29.8% | -- | INSUFFICIENT_INPUTS | PASS | -1.6 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4853.0, B 5263.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0424
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.004, surface_dev_loose -0.004, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Elmer Moller vs Genaro Alberto Olivieri -- ATP Challenger Lima 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144821:209284:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elmer Moller (`KXATPCHALLENGERMATCH-26NOV09MOLOLI-MOL`) | 0.62 / 0.68 (52) | 65.0% | -- | 69.0% | 69.4% [68.5%-69.9%] | -- | -- | -- | -- | PASS | +4.4 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Genaro Alberto Olivieri (`KXATPCHALLENGERMATCH-26NOV09MOLOLI-OLI`) | 0.29 / 0.37 (85) | 33.0% | -- | 31.0% | 30.6% [30.1%-31.6%] | -- | -- | -- | -- | PASS | -2.4 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4766.0, B 5035.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0073
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.009, surface_dev_loose +0.000, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Bernardo Munk Mesa vs Aziz Dougaz -- ATP Challenger Monastir 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144826:212827:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aziz Dougaz (`KXATPCHALLENGERMATCH-26NOV09MUNDOU-DOU`) | 0.85 / 0.86 (10) | 85.5% | -- | 84.0% | 85.8% [84.3%-87.4%] | 84.4% | 84.5% | 84.4% | MARKETS_AGREE | PASS | +0.3 pp | NORMAL | STALE | D / POOR | ALL_AGREE | VERIFIED |
| Bernardo Munk Mesa (`KXATPCHALLENGERMATCH-26NOV09MUNDOU-MUN`) | 0.15 / 0.16 (857) | 15.5% | -- | 16.0% | 14.2% [12.6%-15.7%] | 15.6% | 15.4% | 15.6% | MARKETS_AGREE | PASS | -1.3 pp | NORMAL | STALE | D / POOR | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 814.0, B 2640.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0153
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.014, surface_dev_loose -0.004, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Abdullah Shelbayh vs Harry Wendelken -- ATP Challenger Knoxville 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09SHEWEN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Abdullah Shelbayh (`KXATPCHALLENGERMATCH-26NOV09SHEWEN-SHE`) | 0.47 / 0.52 (45) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Harry Wendelken (`KXATPCHALLENGERMATCH-26NOV09SHEWEN-WEN`) | 0.48 / 0.52 (45) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE

## Braden Shick vs Andres Andrade -- ATP Challenger Knoxville 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200748:211711:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andres Andrade (`KXATPCHALLENGERMATCH-26NOV09SHIAND-AND`) | 0.33 / 0.40 (2) | 36.5% | -- | 55.7% | 58.7% [56.2%-64.6%] | -- | -- | -- | -- | PASS | +22.2 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Braden Shick (`KXATPCHALLENGERMATCH-26NOV09SHIAND-SHI`) | 0.55 / 0.67 (2) | 61.0% | -- | 44.3% | 41.3% [35.4%-43.8%] | -- | -- | -- | -- | PASS | -19.7 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3000.0, B 4704.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0422
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV09SHIAND-AND  (YES = Andres Andrade)
Model: 59%
Kalshi: 36%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.025, surface_pool_high +0.020, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Trevor Svajda vs Max Hans Rehberg -- ATP Challenger Knoxville 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208819:212216:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Max Hans Rehberg (`KXATPCHALLENGERMATCH-26NOV09SVAREH-REH`) | 0.52 / 0.56 (31) | 54.0% | -- | 63.8% | 59.0% [56.0%-62.4%] | 54.1% | 53.8% | -- | INSUFFICIENT_INPUTS | WATCH | +5.0 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Trevor Svajda (`KXATPCHALLENGERMATCH-26NOV09SVAREH-SVA`) | 0.44 / 0.47 (6) | 45.5% | -- | 36.1% | 41.0% [37.6%-44.0%] | 45.9% | 46.3% | -- | INSUFFICIENT_INPUTS | PASS | -4.5 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1651.0, B 3984.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0319
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.034, surface_pool_high +0.030, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Juan Pablo Varillas vs Marcelo Tomas Barrios Vera -- ATP Challenger Lima 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09VARBAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcelo Tomas Barrios Vera (`KXATPCHALLENGERMATCH-26NOV09VARBAR-BAR`) | 0.64 / 0.72 (50) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Juan Pablo Varillas (`KXATPCHALLENGERMATCH-26NOV09VARBAR-VAR`) | 0.27 / 0.33 (46) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Max Houkes vs Tom Gentzsch -- ATP Challenger Orleans 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208069:210167:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tom Gentzsch (`KXATPCHALLENGERMATCH-26NOV09HOUGEN-GEN`) | 0.72 / 0.73 (623) | 72.5% | -- | 36.9% | 43.1% [39.7%-52.0%] | 71.1% | 74.8% | 71.1% | MODEL_LONE_OUTLIER | PASS | -29.4 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Max Houkes (`KXATPCHALLENGERMATCH-26NOV09HOUGEN-HOU`) | 0.27 / 0.28 (584) | 27.5% | -- | 63.1% | 56.9% [48.0%-60.3%] | 28.9% | 28.0% | 28.5% | MODEL_LONE_OUTLIER | WATCH | +29.4 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4345.0, B 5358.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0615
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV09HOUGEN-HOU  (YES = Max Houkes)
Model: 57%
Kalshi: 28%
Gap: +29 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.029, surface_dev_tight -0.029
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Clement Tabur vs Lukas Neumayer -- ATP Challenger Orleans 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202127:209903:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lukas Neumayer (`KXATPCHALLENGERMATCH-26NOV09TABNEU-NEU`) | 0.33 / 0.34 (584) | 33.5% | -- | 37.7% | 38.2% [37.2%-40.1%] | 34.3% | 32.8% | 32.8% | MODEL_LONE_OUTLIER | SHADOW_BET | +4.7 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Clement Tabur (`KXATPCHALLENGERMATCH-26NOV09TABNEU-TAB`) | 0.66 / 0.68 (648) | 67.0% | -- | 62.3% | 61.8% [59.9%-62.8%] | 65.7% | 64.7% | -- | INSUFFICIENT_INPUTS | PASS | -5.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4961.0, B 5459.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0142
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.009, surface_dev_loose +0.009, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Enrique Bogo vs Daniel Vecchio Couldrey Rebelo -- M25 Santa Cruz do Sul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-09T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:109732:210213:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Enrique Bogo (`KXITFMATCH-26NOV09BOGREB-BOG`) | 0.77 / 0.81 (6) | 79.0% | 29.0% | 32.8% | 24.9% [23.9%-24.9%] | -- | -- | -- | -- | PASS | -50.0 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daniel Vecchio Couldrey Rebelo (`KXITFMATCH-26NOV09BOGREB-REB`) | 0.15 / 0.21 (48) | 18.0% | 71.0% | 67.2% | 75.1% [75.1%-76.1%] | -- | -- | -- | -- | PASS | +53.0 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 267.0, B 40.0; serve-point win A 56.3%, B 39.4%; Elo A 1053.0, B 1252.4; model uncertainty 0.0051
* Form inputs: days since last match A 251, B 363; matches on record A 86, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV09BOGREB-REB  (YES = Daniel Vecchio Couldrey Rebelo)
Model: 71%
Kalshi: 18%
Gap: +53 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.008, surface_dev_loose -0.001, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pedro Rodrigues Longobardi vs Enzo Fortes -- M25 Santa Cruz do Sul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-09T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:109946:211748:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Enzo Fortes (`KXITFMATCH-26NOV09RODFOR-FOR`) | 0.33 / 0.34 (100) | 33.5% | -- | 26.6% | 26.2% [25.6%-26.3%] | -- | -- | -- | -- | PASS | -7.3 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Pedro Rodrigues Longobardi (`KXITFMATCH-26NOV09RODFOR-ROD`) | 0.66 / 0.67 (2) | 66.5% | -- | 73.4% | 73.8% [73.7%-74.5%] | -- | -- | -- | -- | PASS | +7.3 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1514.0, B 0.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0037
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Larissa Lopes Missato vs Alice Diamante -- W15 São Carlos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV09LOPDIA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alice Diamante (`KXITFWMATCH-26NOV09LOPDIA-DIA`) | 0.18 / 0.61 (2) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Larissa Lopes Missato (`KXITFWMATCH-26NOV09LOPDIA-LOP`) | 0.32 / 0.78 (1) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sophia Tiemi Sakada da Costa vs Barbara Krupek Soccol -- W15 São Carlos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV09SAKKRU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barbara Krupek Soccol (`KXITFWMATCH-26NOV09SAKKRU-KRU`) | 0.10 / 0.37 (12) | 23.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sophia Tiemi Sakada da Costa (`KXITFWMATCH-26NOV09SAKKRU-SAK`) | 0.68 / 0.91 (10) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maria Clara Souza vs Giulia Gomes Ferreira -- W15 São Carlos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV09SOUGOM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giulia Gomes Ferreira (`KXITFWMATCH-26NOV09SOUGOM-GOM`) | 0.50 / 0.84 (214) | 67.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maria Clara Souza (`KXITFWMATCH-26NOV09SOUGOM-SOU`) | 0.08 / 0.32 (0) | 20.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aryna Sabalenka vs Karolina Muchova -- WTA Finals (Women) RR

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-09 23:00Z
* Current expected start: 2026-11-09 20:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-09 04:02Z
* Recommended handicap-by time: 2026-11-09 19:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_FINALS) · Hard · scheduled 2026-11-09T23:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214096:214544:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karolina Muchova (`KXWTAMATCH-26NOV09SABMUC-MUC`) | 0.34 / 0.35 (1262) | 34.5% | -- | 26.3% | 26.7% [26.3%-27.6%] | 36.1% | 35.9% | 35.9% | MODEL_LONE_OUTLIER | PASS | -7.8 pp | NORMAL | STALE | A / LIMITED | EXTERNAL_STALE | VERIFIED |
| Aryna Sabalenka (`KXWTAMATCH-26NOV09SABMUC-SAB`) | 0.64 / 0.65 (11) | 64.5% | -- | 73.7% | 73.3% [72.4%-73.7%] | 63.9% | 64.3% | 64.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +8.8 pp | NORMAL | STALE | A / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5768.0, B 3972.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0063
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.008, surface_dev_loose -0.004, surface_dev_tight +0.001
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26NOV09SABMUC-2-SAB` Will Aryna Sabalenka win set 2 in the Aryna Sabalenka vs Karolina Muchova match: 0.52/0.66 mid 59.0%, model 66.0% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV09SABMUC-1-MUC` Will Karolina Muchova win set 1 in the Aryna Sabalenka vs Karolina Muchova match: 0.38/0.40 mid 39.0%, model 34.0% (projection_v2.0 (prediction ledger)) -- gap -5.0 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV09SABMUC-1-SAB` Will Aryna Sabalenka win set 1 in the Aryna Sabalenka vs Karolina Muchova match: 0.60/0.63 mid 61.5%, model 66.0% (projection_v2.0 (prediction ledger)) -- gap +4.5 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV09SABMUC-2-MUC` Will Karolina Muchova win set 2 in the Aryna Sabalenka vs Karolina Muchova match: 0.30/0.43 mid 36.5%, model 34.0% (projection_v2.0 (prediction ledger)) -- gap -2.5 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Luka Bojicic Ono vs Augusto Land -- M25 Santa Cruz do Sul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09BOJLAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luka Bojicic Ono (`KXITFMATCH-26NOV09BOJLAN-BOJ`) | 0.56 / 0.57 (5) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Augusto Land (`KXITFMATCH-26NOV09BOJLAN-LAN`) | 0.40 / 0.43 (150) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Franco Marini vs Gabriel Augusto Carvalho -- M25 Santa Cruz do Sul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-09T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211699:214023:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriel Augusto Carvalho (`KXITFMATCH-26NOV09MARCAR-CAR`) | 0.74 / 0.76 (100) | 75.0% | 57.6% | 43.2% | 53.7% [52.1%-55.2%] | -- | -- | -- | -- | PASS | -17.4 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Franco Marini (`KXITFMATCH-26NOV09MARCAR-MAR`) | 0.21 / 0.22 (32) | 21.5% | 42.4% | 56.8% | 46.3% [44.8%-47.9%] | -- | -- | -- | -- | PASS | +20.9 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 173.0, B 282.0; serve-point win A 57.0%, B 41.5%; Elo A 1146.8, B 1179.6; model uncertainty 0.0153
* Form inputs: days since last match A 357, B 350; matches on record A 8, B 4; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV09MARCAR-MAR  (YES = Franco Marini)
Model: 42%
Kalshi: 22%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.005, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Giovana Giannotti vs Julia Pretti -- W15 São Carlos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV09GIAPRE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giovana Giannotti (`KXITFWMATCH-26NOV09GIAPRE-GIA`) | 0.11 / 0.93 (10) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Julia Pretti (`KXITFWMATCH-26NOV09GIAPRE-PRE`) | 0.09 / 0.85 (2) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Leticia Jordana Vidal vs Kauany Rodrigues -- W15 São Carlos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV09JORROD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leticia Jordana Vidal (`KXITFWMATCH-26NOV09JORROD-JOR`) | 0.15 / 0.33 (135) | 24.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kauany Rodrigues (`KXITFWMATCH-26NOV09JORROD-ROD`) | 0.67 / 0.81 (4) | 74.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Laura Goncalves Portela Borges vs Guisella Insfran -- W15 São Carlos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-09T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:269739:269935:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Guisella Insfran (`KXITFWMATCH-26NOV09PORINS-INS`) | 0.67 / 0.92 (5) | 79.5% | 78.6% | 30.6% | 59.5% [59.5%-59.5%] | -- | -- | -- | -- | PASS | -0.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Laura Goncalves Portela Borges (`KXITFWMATCH-26NOV09PORINS-POR`) | 0.05 / 0.37 (6) | 21.0% | 21.4% | 69.4% | 40.5% [40.5%-40.5%] | -- | -- | -- | -- | PASS | +0.4 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 50.0; serve-point win A 51.3%, B 42.7%; Elo A 1139.6, B 1205.4; model uncertainty 0.0001
* Form inputs: days since last match A 700, B 427; matches on record A 4, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tomas Dummer Macedo vs Eduardo Heineberg -- M25 Santa Cruz do Sul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09DUMHEI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tomas Dummer Macedo (`KXITFMATCH-26NOV09DUMHEI-DUM`) | 0.81 / 0.88 (100) | 84.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eduardo Heineberg (`KXITFMATCH-26NOV09DUMHEI-HEI`) | 0.12 / 0.15 (101) | 13.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Volodymyr Gurenko vs Mathias Hamel-Van Dun -- M25 Montreal R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09GURHAM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Volodymyr Gurenko (`KXITFMATCH-26NOV09GURHAM-GUR`) | 0.05 / 0.94 (175) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mathias Hamel-Van Dun (`KXITFMATCH-26NOV09GURHAM-HAM`) | 0.05 / 0.94 (175) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eric Von Marton Martins vs Glauco Pinheiro da Cruz Junior -- M25 Santa Cruz do Sul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09MARPIN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eric Von Marton Martins (`KXITFMATCH-26NOV09MARPIN-MAR`) | 0.14 / 0.19 (10) | 16.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Glauco Pinheiro da Cruz Junior (`KXITFMATCH-26NOV09MARPIN-PIN`) | 0.77 / 0.83 (180) | 80.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lazar Markovic vs Stephen Slocombe -- M25 Montreal R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-09T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210750:213723:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lazar Markovic (`KXITFMATCH-26NOV09MARSLO-MAR`) | 0.05 / 0.94 (175) | 49.5% | 49.4% | 56.7% | 52.1% [51.0%-52.1%] | -- | -- | -- | -- | PASS | -0.1 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Stephen Slocombe (`KXITFMATCH-26NOV09MARSLO-SLO`) | 0.05 / 0.94 (175) | 49.5% | 50.6% | 43.3% | 47.9% [47.9%-49.0%] | -- | -- | -- | -- | PASS | +1.1 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 44.0, B 127.0; serve-point win A 59.1%, B 40.8%; Elo A 1230.2, B 1217.9; model uncertainty 0.0052
* Form inputs: days since last match A 546, B 252; matches on record A 2, B 4; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ranak Pajpani vs Matthew Michibata -- M25 Montreal R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09PAJMIC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthew Michibata (`KXITFMATCH-26NOV09PAJMIC-MIC`) | 0.06 / 0.93 (2) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ranak Pajpani (`KXITFMATCH-26NOV09PAJMIC-PAJ`) | 0.05 / 0.94 (175) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mirra Andreeva vs Elina Svitolina -- WTA Finals (Women) RR

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-10 00:30Z
* Current expected start: 2026-11-09 21:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-09 04:02Z
* Recommended handicap-by time: 2026-11-09 20:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_FINALS) · Hard · scheduled 2026-11-10T00:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202494:259799:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mirra Andreeva (`KXWTAMATCH-26NOV09ANDSVI-AND`) | 0.63 / 0.64 (155) | 63.5% | -- | 60.4% | 56.3% [48.9%-58.8%] | -- | -- | -- | -- | PASS | -7.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elina Svitolina (`KXWTAMATCH-26NOV09ANDSVI-SVI`) | 0.36 / 0.37 (30554) | 36.5% | -- | 39.6% | 43.7% [41.2%-51.0%] | -- | -- | -- | -- | SHADOW_BET | +7.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4895.0, B 4144.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0494
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.010, surface_dev_tight -0.005
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26NOV09ANDSVI-2-SVI` Will Elina Svitolina win set 2 in the Mirra Andreeva vs Elina Svitolina match: 0.31/0.44 mid 37.5%, model 46.0% (projection_v2.0 (prediction ledger)) -- gap +8.4 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV09ANDSVI-1-AND` Will Mirra Andreeva win set 1 in the Mirra Andreeva vs Elina Svitolina match: 0.58/0.62 mid 60.0%, model 54.0% (projection_v2.0 (prediction ledger)) -- gap -6.0 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV09ANDSVI-1-SVI` Will Elina Svitolina win set 1 in the Mirra Andreeva vs Elina Svitolina match: 0.39/0.42 mid 40.5%, model 46.0% (projection_v2.0 (prediction ledger)) -- gap +5.5 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV09ANDSVI-2-AND` Will Mirra Andreeva win set 2 in the Mirra Andreeva vs Elina Svitolina match: 0.51/0.64 mid 57.5%, model 54.0% (projection_v2.0 (prediction ledger)) -- gap -3.5 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## David Cristian Carteputreda vs Mathias Roy -- M25 Montreal R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09CARROY:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| David Cristian Carteputreda (`KXITFMATCH-26NOV09CARROY-CAR`) | 0.06 / 0.94 (175) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mathias Roy (`KXITFMATCH-26NOV09CARROY-ROY`) | 0.05 / 0.94 (175) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Thomas Gerbaud vs Anirudh Rao -- M25 Montreal R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-09T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212840:213652:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thomas Gerbaud (`KXITFMATCH-26NOV09GERRAO-GER`) | 0.06 / 0.94 (197) | 50.0% | 53.7% | 26.5% | 47.1% [47.0%-47.1%] | -- | -- | -- | -- | PASS | +3.7 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anirudh Rao (`KXITFMATCH-26NOV09GERRAO-RAO`) | 0.05 / 0.94 (175) | 49.5% | 46.3% | 73.5% | 52.9% [52.9%-53.0%] | -- | -- | -- | -- | PASS | -3.2 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 568.0, B 0.0; serve-point win A 65.7%, B 35.0%; Elo A 1226.2, B 1247.8; model uncertainty 0.0007
* Form inputs: days since last match A 245, B 728; matches on record A 19, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Michael Glen vs Daniel Kliebhan -- M25 Montreal R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09GLEKLI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michael Glen (`KXITFMATCH-26NOV09GLEKLI-GLE`) | 0.05 / 0.94 (175) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daniel Kliebhan (`KXITFMATCH-26NOV09GLEKLI-KLI`) | 0.06 / 0.93 (10) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kaue Noatto vs Andrey Barbiero -- M25 Santa Cruz do Sul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09NOABAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrey Barbiero (`KXITFMATCH-26NOV09NOABAR-BAR`) | 0.07 / 0.13 (155) | 10.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kaue Noatto (`KXITFMATCH-26NOV09NOABAR-NOA`) | 0.83 / 0.90 (19) | 86.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Barbara Ferrante vs Lais Lobo Assumpcao Euzebio -- W15 São Carlos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV09FERLOB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barbara Ferrante (`KXITFWMATCH-26NOV09FERLOB-FER`) | 0.09 / 0.92 (10) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lais Lobo Assumpcao Euzebio (`KXITFWMATCH-26NOV09FERLOB-LOB`) | 0.06 / 0.92 (10) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eduarda Gomes vs Serena Jhulia Antonio Tofoli Wilson Donizete Tofoli -- W15 São Carlos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV09GOMWIL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eduarda Gomes (`KXITFWMATCH-26NOV09GOMWIL-GOM`) | 0.09 / 0.92 (10) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Serena Jhulia Antonio Tofoli Wilson Donizete Tofoli (`KXITFWMATCH-26NOV09GOMWIL-WIL`) | 0.06 / 0.92 (10) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gabriela Dabrowski / Luisa Stefani vs Elise Mertens / Shuai Zhang -- WTA Finals (Women) RR

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-10 02:00Z
* Current expected start: 2026-11-09 23:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-09 04:02Z
* Recommended handicap-by time: 2026-11-09 22:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_FINALS) · surface ? · scheduled 2026-11-10T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV09DABSTEMERZHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriela Dabrowski / Luisa Stefani (`KXWTADOUBLES-26NOV09DABSTEMERZHA-DABSTE`) | 0.65 / 0.68 (166) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Elise Mertens / Shuai Zhang (`KXWTADOUBLES-26NOV09DABSTEMERZHA-MERZHA`) | 0.32 / 0.36 (240) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Haig Daouidian vs Miko Lapalme -- M25 Montreal R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09DAOLAP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Haig Daouidian (`KXITFMATCH-26NOV09DAOLAP-DAO`) | 0.05 / 0.94 (175) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Miko Lapalme (`KXITFMATCH-26NOV09DAOLAP-LAP`) | 0.05 / 0.94 (175) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eric David Verdes vs Kim Johannes Niethammer -- M25 Montreal R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09VERNIE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kim Johannes Niethammer (`KXITFMATCH-26NOV09VERNIE-NIE`) | 0.06 / 0.94 (197) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eric David Verdes (`KXITFMATCH-26NOV09VERNIE-VER`) | 0.05 / 0.94 (175) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jaden Weekes vs Jonathan Bedard -- M25 Montreal R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09WEEBED:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jonathan Bedard (`KXITFMATCH-26NOV09WEEBED-BED`) | 0.05 / 0.94 (175) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jaden Weekes (`KXITFMATCH-26NOV09WEEBED-WEE`) | 0.05 / 0.93 (10) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Joaquin Bianchi vs Jesus Martinez Miranda -- M15 Zamora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:214129:214407:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joaquin Bianchi (`KXITFMATCH-26NOV09BIAMAR-BIA`) | 0.05 / 0.94 (175) | 49.5% | 40.8% | 39.8% | 42.8% [41.8%-42.8%] | -- | -- | -- | -- | PASS | -8.7 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jesus Martinez Miranda (`KXITFMATCH-26NOV09BIAMAR-MAR`) | 0.05 / 0.94 (175) | 49.5% | 59.2% | 60.2% | 57.2% [57.2%-58.2%] | -- | -- | -- | -- | PASS | +9.7 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 179.0, B 112.0; serve-point win A 58.7%, B 39.5%; Elo A 1162.1, B 1211.2; model uncertainty 0.0052
* Form inputs: days since last match A 238, B 196; matches on record A 4, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matthias Uwe Kask vs Eliot Nobel -- M25 Montreal R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210490:214052:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthias Uwe Kask (`KXITFMATCH-26NOV09KASNOB-KAS`) | 0.06 / 0.94 (197) | 50.0% | 47.0% | 46.9% | 42.8% [42.8%-43.3%] | -- | -- | -- | -- | PASS | -3.0 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Eliot Nobel (`KXITFMATCH-26NOV09KASNOB-NOB`) | 0.05 / 0.93 (10) | 49.0% | 52.9% | 53.1% | 57.2% [56.7%-57.2%] | -- | -- | -- | -- | PASS | +4.0 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 46.0, B 63.0; serve-point win A 59.5%, B 40.0%; Elo A 1210.9, B 1258.3; model uncertainty 0.0026
* Form inputs: days since last match A 728, B 455; matches on record A 4, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stefano Lacroce vs Tiago Silva -- M25 Montreal R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09LACSIL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefano Lacroce (`KXITFMATCH-26NOV09LACSIL-LAC`) | 0.06 / 0.94 (175) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tiago Silva (`KXITFMATCH-26NOV09LACSIL-SIL`) | 0.05 / 0.94 (175) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lance Lage vs Dante Carlos Teramo -- M15 Zamora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09LAGTER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lance Lage (`KXITFMATCH-26NOV09LAGTER-LAG`) | 0.05 / 0.94 (175) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dante Carlos Teramo (`KXITFMATCH-26NOV09LAGTER-TER`) | 0.05 / 0.94 (175) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Steven McCartney vs Jared Horwood -- M25 Montreal R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09MCCHOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jared Horwood (`KXITFMATCH-26NOV09MCCHOR-HOR`) | 0.05 / 0.93 (1) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Steven McCartney (`KXITFMATCH-26NOV09MCCHOR-MCC`) | 0.05 / 0.94 (175) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jack McGary vs Luis Patino -- M15 Zamora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106250:214117:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jack McGary (`KXITFMATCH-26NOV09MCGPAT-MCG`) | 0.05 / 0.94 (175) | 49.5% | 21.5% | 53.6% | 32.1% [28.5%-35.0%] | -- | -- | -- | -- | PASS | -28.0 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Luis Patino (`KXITFMATCH-26NOV09MCGPAT-PAT`) | 0.05 / 0.94 (175) | 49.5% | 78.5% | 46.4% | 67.8% [65.0%-71.5%] | -- | -- | -- | -- | PASS | +29.0 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 281.0, B 673.0; serve-point win A 57.5%, B 36.4%; Elo A 1181.7, B 1342.9; model uncertainty 0.032
* Form inputs: days since last match A 196, B 1624; matches on record A 5, B 354; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV09MCGPAT-PAT  (YES = Luis Patino)
Model: 78%
Kalshi: 50%
Gap: +29 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gabriel Miller vs Lucas Hammond -- M25 Montreal R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09MILHAM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucas Hammond (`KXITFMATCH-26NOV09MILHAM-HAM`) | 0.06 / 0.94 (197) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gabriel Miller (`KXITFMATCH-26NOV09MILHAM-MIL`) | 0.06 / 0.94 (175) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hanyu Guo / Kristina Mladenovic vs Su-Wei Hsieh / Jelena Ostapenko -- WTA Finals (Women) RR

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-10 03:30Z
* Current expected start: 2026-11-10 00:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-09 04:02Z
* Recommended handicap-by time: 2026-11-09 23:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_FINALS) · surface ? · scheduled 2026-11-10T03:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV09GUOMLAHSIOST:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hanyu Guo / Kristina Mladenovic (`KXWTADOUBLES-26NOV09GUOMLAHSIOST-GUOMLA`) | 0.35 / 0.38 (76) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Su-Wei Hsieh / Jelena Ostapenko (`KXWTADOUBLES-26NOV09GUOMLAHSIOST-HSIOST`) | 0.61 / 0.64 (1000) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Alberto Odiseo Alvarado Berrospi vs Axel Cabrera -- M15 Zamora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09ALVCAB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alberto Odiseo Alvarado Berrospi (`KXITFMATCH-26NOV09ALVCAB-ALV`) | 0.06 / 0.94 (175) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Axel Cabrera (`KXITFMATCH-26NOV09ALVCAB-CAB`) | 0.05 / 0.94 (175) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ian Lucca Cervantes Tomas vs Miguel Gamborino -- M15 Zamora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209388:212486:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ian Lucca Cervantes Tomas (`KXITFMATCH-26NOV09CERGAM-CER`) | 0.05 / 0.94 (175) | 49.5% | -- | 39.3% | 39.3% [38.8%-39.8%] | -- | -- | -- | -- | PASS | -10.2 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Miguel Gamborino (`KXITFMATCH-26NOV09CERGAM-GAM`) | 0.05 / 0.94 (175) | 49.5% | -- | 60.7% | 60.7% [60.2%-61.2%] | -- | -- | -- | -- | PASS | +11.2 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 529.0, B 44.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0052
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tarun Karra vs Marcel Hornung -- M15 Zamora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206623:213598:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcel Hornung (`KXITFMATCH-26NOV09KARHOR-HOR`) | 0.06 / 0.94 (197) | 50.0% | -- | 75.2% | 67.2% [67.0%-67.3%] | -- | -- | -- | -- | PASS | +17.2 pp | HIGH_REVIEW (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Tarun Karra (`KXITFMATCH-26NOV09KARHOR-KAR`) | 0.05 / 0.94 (175) | 49.5% | -- | 24.8% | 32.8% [32.7%-33.0%] | -- | -- | -- | -- | PASS | -16.7 pp | HIGH_REVIEW (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 201.0, B 0.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0011
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV09KARHOR-HOR  (YES = Marcel Hornung)
Model: 67%
Kalshi: 50%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
