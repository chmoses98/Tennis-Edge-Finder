# ASSISTED SLATE -- 2026-10-01T06:37Z (`SL-20261001T063726Z-932c4fe4`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

316 open matches not seen started, 783 markets. Skipped: {"first_ball_already_observed": 39, "scheduled_start_over_24h_past": 10}. Sources: shadow board 2026-10-01T06:33:05.413610+00:00, Model 4 2026-10-01T06:33:44.078835+00:00, Gen-1 ledger 2026-10-01T06:33:01.837258+00:00, external 2026-10-01T05:48:48.900344+00:00, capture 20261001T054334Z.quotes.jsonl.gz.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 67, "HIGH_REVIEW": 102, "NORMAL": 241, "REVIEW": 83, "UNPRICED": 290}; match winners: {"EXTREME": 63, "HIGH_REVIEW": 85, "NORMAL": 228, "REVIEW": 60, "UNPRICED": 196}; quote freshness at build: {"STALE": 493}.

## Ferrari / Valle vs Purtseladze / Shvangiradze -- M15 Telavi QF

DOUBLES (ITF) · surface ? · scheduled 2026-09-30T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26SEP30FERVALPURSHV:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ferrari / Valle (`KXITFDOUBLES-26SEP30FERVALPURSHV-FERVAL`) | 0.04 / 0.89 (2) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Purtseladze / Shvangiradze (`KXITFDOUBLES-26SEP30FERVALPURSHV-PURSHV`) | 0.03 / 0.62 (1) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alexander Ikenna Okonkwo / Preston Stearns vs Reid Jarvis / Jack Vance -- ATP Challenger Columbus R16

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-09-30T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26SEP30OKOSTEJARVAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Reid Jarvis / Jack Vance (`KXATPCHALLENGERDOUBLES-26SEP30OKOSTEJARVAN-JARVAN`) | -- / 0.07 (56) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexander Ikenna Okonkwo / Preston Stearns (`KXATPCHALLENGERDOUBLES-26SEP30OKOSTEJARVAN-OKOSTE`) | 0.94 / 0.99 (426) | 96.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE

## Sadio Doumbia / Fabien Reboul vs Maximo Gonzalez / Andres Molteni -- ATP Beijing R16

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-01T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26SEP30DOUREBGONMOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sadio Doumbia / Fabien Reboul (`KXATPDOUBLES-26SEP30DOUREBGONMOL-DOUREB`) | 0.61 / 0.63 (144) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maximo Gonzalez / Andres Molteni (`KXATPDOUBLES-26SEP30DOUREBGONMOL-GONMOL`) | 0.37 / 0.38 (1256) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE

## Alex Bolt vs Evan Zhu -- ATP Challenger Jingshan R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:106109:200632:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex Bolt (`KXATPCHALLENGERMATCH-26SEP30BOLZHU-BOL`) | 0.59 / 0.60 (31) | 59.5% | -- | 79.1% | 80.8% [79.1%-82.8%] | 65.7% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +21.3 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Evan Zhu (`KXATPCHALLENGERMATCH-26SEP30BOLZHU-ZHU`) | 0.38 / 0.40 (845) | 39.0% | -- | 20.9% | 19.2% [17.2%-20.9%] | 34.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -19.8 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5430.0, B 3955.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0188
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26SEP30BOLZHU-BOL  (YES = Alex Bolt)
Model: 81%
Kalshi: 60%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.018, surface_dev_loose +0.003, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Alevtina Ibragimova vs Kyoka Okamura -- WTA 125K Jingshan R16

WTA125 (WTA_125) · Hard · scheduled 2026-10-01T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:211846:260581:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alevtina Ibragimova (`KXWTACHALLENGERMATCH-26SEP30IBROKA-IBR`) | 0.20 / 0.21 (58180) | 20.5% | -- | 66.3% | 63.8% [61.9%-65.3%] | 73.5% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +43.4 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kyoka Okamura (`KXWTACHALLENGERMATCH-26SEP30IBROKA-OKA`) | 0.79 / 0.80 (6691) | 79.5% | -- | 33.7% | 36.1% [34.7%-38.1%] | 26.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -43.4 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2867.0, B 2971.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0169
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTACHALLENGERMATCH-26SEP30IBROKA-IBR  (YES = Alevtina Ibragimova)
Model: 64%
Kalshi: 20%
Gap: +43 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.010, surface_dev_loose +0.009, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Sofya Lansere vs Sofia Costoulas -- WTA 125K Jingshan R16

WTA125 (WTA_125) · Hard · scheduled 2026-10-01T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:216139:223321:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Costoulas (`KXWTACHALLENGERMATCH-26SEP30LANCOS-COS`) | 0.28 / 0.29 (23856) | 28.5% | -- | 60.5% | 62.5% [61.0%-67.0%] | 73.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +34.0 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sofya Lansere (`KXWTACHALLENGERMATCH-26SEP30LANCOS-LAN`) | 0.71 / 0.72 (13507) | 71.5% | -- | 39.5% | 37.5% [33.0%-39.0%] | 26.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -34.0 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3253.0, B 4020.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0299
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTACHALLENGERMATCH-26SEP30LANCOS-COS  (YES = Sofia Costoulas)
Model: 63%
Kalshi: 28%
Gap: +34 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Andre Ilagan vs Marat Sharipov -- ATP Challenger Jingshan R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T07:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:129911:210318:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andre Ilagan (`KXATPCHALLENGERMATCH-26OCT01ILASHA-ILA`) | 0.26 / 0.27 (190) | 26.5% | 33.1% | 26.8% | 28.5% [26.9%-29.7%] | -- | 26.4% | 26.4% | MODEL_LONE_OUTLIER | PASS | +2.0 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Marat Sharipov (`KXATPCHALLENGERMATCH-26OCT01ILASHA-SHA`) | 0.72 / 0.74 (3078) | 73.0% | 66.9% | 73.2% | 71.5% [70.3%-73.1%] | -- | 74.1% | 74.1% | MODEL_LONE_OUTLIER | PASS | -1.5 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5539.0, B 3891.0; serve-point win A 60.9%, B 35.7%; Elo A 1608.9, B 1737.5; model uncertainty 0.0143
* Form inputs: days since last match A 9, B 17; matches on record A 236, B 317; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high -0.000, surface_dev_loose -0.016, surface_dev_tight +0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Yuta Shimizu vs Bernard Tomic -- ATP Challenger Jingshan R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T07:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:106071:202122:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuta Shimizu (`KXATPCHALLENGERMATCH-26OCT01SHITOM-SHI`) | 0.38 / 0.39 (1208) | 38.5% | 41.8% | 37.7% | 37.7% [37.2%-39.1%] | 40.1% | -- | 40.1% | MODEL_LONE_OUTLIER | PASS | -0.8 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Bernard Tomic (`KXATPCHALLENGERMATCH-26OCT01SHITOM-TOM`) | 0.61 / 0.62 (432) | 61.5% | 58.2% | 62.3% | 62.3% [60.9%-62.8%] | 59.9% | -- | 59.9% | MODEL_LONE_OUTLIER | PASS | +0.8 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4903.0, B 5940.0; serve-point win A 61.8%, B 36.6%; Elo A 1590.1, B 1667.2; model uncertainty 0.0095
* Form inputs: days since last match A 17, B 17; matches on record A 541, B 996; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose -0.005, surface_dev_tight +0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Elias Ymer vs Federico Cina -- ATP Challenger Jingshan R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T07:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:111200:210748:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Federico Cina (`KXATPCHALLENGERMATCH-26OCT01YMECIN-CIN`) | 0.70 / 0.71 (83) | 70.5% | 58.0% | 60.4% | 60.9% [59.4%-62.3%] | -- | 75.0% | 75.0% | MODEL_LONE_OUTLIER | PASS | -9.6 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Elias Ymer (`KXATPCHALLENGERMATCH-26OCT01YMECIN-YME`) | 0.29 / 0.31 (200) | 30.0% | 42.0% | 39.6% | 39.1% [37.8%-40.6%] | -- | 25.4% | 25.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +9.1 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5409.0, B 3635.0; serve-point win A 61.8%, B 36.6%; Elo A 1618.1, B 1702.2; model uncertainty 0.0141
* Form inputs: days since last match A 9, B 5; matches on record A 1064, B 187; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.014, surface_dev_tight +0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Michael Zheng vs Yanki Erel -- ATP Challenger Jingshan R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T07:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:207129:210116:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yanki Erel (`KXATPCHALLENGERMATCH-26OCT01ZHEERE-ERE`) | 0.69 / 0.70 (37242) | 69.5% | 34.4% | 56.6% | 40.5% [32.8%-46.5%] | -- | 18.4% | 18.4% | MODEL_LONE_OUTLIER | PASS | -29.0 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Michael Zheng (`KXATPCHALLENGERMATCH-26OCT01ZHEERE-ZHE`) | 0.30 / 0.31 (21296) | 30.5% | 65.6% | 43.4% | 59.5% [53.5%-67.2%] | -- | 81.7% | 81.7% | MODEL_LONE_OUTLIER | WATCH | +29.0 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 2389.0, B 4118.0; serve-point win A 64.2%, B 39.0%; Elo A 1833.4, B 1579.1; model uncertainty 0.0682
* Form inputs: days since last match A 7, B 24; matches on record A 144, B 419; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT01ZHEERE-ZHE  (YES = Michael Zheng)
Model: 60%
Kalshi: 30%
Gap: +29 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: SUPPORTS_MODEL_DIRECTION
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Kanon Sawashiro vs Ava Beck -- W35 Wagga Wagga R16

ITF (ITF) · Hard · scheduled 2026-10-01T07:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:263905:269872:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ava Beck (`KXITFWMATCH-26SEP30SAWBEC-BEC`) | 0.12 / 0.13 (10079) | 12.5% | 32.8% | 18.4% | 30.9% [25.5%-37.4%] | 18.6% | -- | 18.6% | MODEL_LONE_OUTLIER | PASS | +18.4 pp | HIGH_REVIEW | STALE | D / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Kanon Sawashiro (`KXITFWMATCH-26SEP30SAWBEC-SAW`) | 0.87 / 0.88 (12233) | 87.5% | 67.2% | 81.6% | 69.1% [62.6%-74.5%] | 81.4% | -- | 81.4% | MODEL_LONE_OUTLIER | PASS | -18.4 pp | HIGH_REVIEW | STALE | D / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 827.0, B 734.0; serve-point win A 57.4%, B 46.0%; Elo A 1348.8, B 1267.0; model uncertainty 0.0592
* Form inputs: days since last match A 164, B 192; matches on record A 36, B 15; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26SEP30SAWBEC-BEC  (YES = Ava Beck)
Model: 31%
Kalshi: 12%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: SUPPORTS_MODEL_DIRECTION
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.009, surface_dev_loose +0.009, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lloyd Harris / Cheng-Peng Hsieh vs Nathaniel Lammons / Jackson Withrow -- ATP Challenger Jingshan QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T08:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01HARHSILAMWIT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lloyd Harris / Cheng-Peng Hsieh (`KXATPCHALLENGERDOUBLES-26OCT01HARHSILAMWIT-HARHSI`) | 0.18 / 0.52 (1) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nathaniel Lammons / Jackson Withrow (`KXATPCHALLENGERDOUBLES-26OCT01HARHSILAMWIT-LAMWIT`) | 0.07 / 0.77 (1) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alexandre Muller / Luka Pavlovic vs Miguel Angel Reyes-Varela / Reese Stalder -- ATP Challenger Jingshan QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T08:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01MULPAVREYSTA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandre Muller / Luka Pavlovic (`KXATPCHALLENGERDOUBLES-26OCT01MULPAVREYSTA-MULPAV`) | 0.25 / 0.58 (1) | 41.5% | 93.9% | -- | -- [-----] | -- | -- | -- | -- | -- | +52.4 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Miguel Angel Reyes-Varela / Reese Stalder (`KXATPCHALLENGERDOUBLES-26OCT01MULPAVREYSTA-REYSTA`) | 0.06 / 0.76 (5) | 41.0% | 6.1% | -- | -- [-----] | -- | -- | -- | -- | -- | -34.9 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERDOUBLES-26OCT01MULPAVREYSTA-MULPAV  (YES = Alexandre Muller / Luka Pavlovic)
Model: 94%
Kalshi: 42%
Gap: +52 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Warnings: DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ryan Seggerman / Bart Stevens vs Alex Bolt / Adam Walton -- ATP Challenger Jingshan QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T08:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01SEGSTEBOLWAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex Bolt / Adam Walton (`KXATPCHALLENGERDOUBLES-26OCT01SEGSTEBOLWAL-BOLWAL`) | 0.18 / 0.57 (133) | 37.5% | 91.9% | -- | -- [-----] | -- | -- | -- | -- | -- | +54.4 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Ryan Seggerman / Bart Stevens (`KXATPCHALLENGERDOUBLES-26OCT01SEGSTEBOLWAL-SEGSTE`) | 0.74 / 0.80 (1) | 77.0% | 8.1% | -- | -- [-----] | -- | -- | -- | -- | -- | -68.9 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERDOUBLES-26OCT01SEGSTEBOLWAL-BOLWAL  (YES = Alex Bolt / Adam Walton)
Model: 92%
Kalshi: 38%
Gap: +54 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Warnings: DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jessica Bouzas Maneiro vs Yuhan Wang -- WTA 125K Jingshan R16

WTA125 (WTA_125) · Hard · scheduled 2026-10-01T08:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:222601:264205:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jessica Bouzas Maneiro (`KXWTACHALLENGERMATCH-26OCT01BOUWAN-BOU`) | 0.90 / 0.91 (11186) | 90.5% | 81.5% | 69.0% | 80.8% [75.7%-89.0%] | 87.4% | 89.3% | 89.3% | MODEL_LONE_OUTLIER | PASS | -9.7 pp | NORMAL | STALE | C / LIMITED | EXTERNAL_STALE | VERIFIED |
| Yuhan Wang (`KXWTACHALLENGERMATCH-26OCT01BOUWAN-WAN`) | 0.09 / 0.10 (736) | 9.5% | 18.5% | 31.0% | 19.2% [11.0%-24.3%] | 12.6% | 10.1% | 10.1% | MODEL_LONE_OUTLIER | WATCH | +9.7 pp | NORMAL | STALE | C / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3457.0, B 1724.0; serve-point win A 59.1%, B 47.7%; Elo A 1802.7, B 1410.4; model uncertainty 0.0667
* Form inputs: days since last match A 15, B 157; matches on record A 434, B 42; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.030, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Eva Marie Desvignes vs Honori Koyama -- W15 Maanshan R16

ITF (ITF) · Hard · scheduled 2026-10-01T08:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:260742:261082:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eva Marie Desvignes (`KXITFWMATCH-26SEP30DESKOY-DES`) | 0.95 / 0.96 (2690) | 95.5% | 47.3% | 47.9% | 44.7% [43.6%-46.8%] | 83.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -50.8 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Honori Koyama (`KXITFWMATCH-26SEP30DESKOY-KOY`) | 0.04 / 0.05 (30347) | 4.5% | 52.7% | 52.1% | 55.3% [53.2%-56.4%] | 16.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +50.8 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1379.0, B 626.0; serve-point win A 55.4%, B 44.1%; Elo A 1231.5, B 1273.9; model uncertainty 0.0159
* Form inputs: days since last match A 12, B 213; matches on record A 63, B 66; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26SEP30DESKOY-KOY  (YES = Honori Koyama)
Model: 55%
Kalshi: 4%
Gap: +51 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.011, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Albina Kakenova vs Ha Yoon Son -- W15 Maanshan R16

ITF (ITF) · Hard · scheduled 2026-10-01T08:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:260607:263697:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Albina Kakenova (`KXITFWMATCH-26SEP30KAKSON-KAK`) | 0.88 / 0.89 (910) | 88.5% | 57.6% | 38.9% | 56.4% [55.4%-57.5%] | 38.5% | -- | 38.5% | MODEL_LONE_OUTLIER | PASS | -32.1 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Ha Yoon Son (`KXITFWMATCH-26SEP30KAKSON-SON`) | 0.11 / 0.12 (3748) | 11.5% | 42.4% | 61.1% | 43.6% [42.5%-44.6%] | 61.5% | -- | 61.5% | MODEL_LONE_OUTLIER | PASS | +32.1 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 230.0, B 90.0; serve-point win A 56.4%, B 45.0%; Elo A 1255.3, B 1202.0; model uncertainty 0.0106
* Form inputs: days since last match A 339, B 171; matches on record A 6, B 11; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26SEP30KAKSON-SON  (YES = Ha Yoon Son)
Model: 44%
Kalshi: 12%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: SUPPORTS_MODEL_DIRECTION
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.011, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xi Luo vs Kanna Soeda -- W15 Maanshan R16

ITF (ITF) · Hard · scheduled 2026-10-01T08:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:264069:267412:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xi Luo (`KXITFWMATCH-26SEP30LUOSOE-LUO`) | 0.98 / 0.99 (2902) | 98.5% | 74.0% | 66.6% | 73.1% [73.1%-74.8%] | 92.8% | -- | 92.8% | MODEL_LONE_OUTLIER | PASS | -25.4 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Kanna Soeda (`KXITFWMATCH-26SEP30LUOSOE-SOE`) | 0.01 / 0.02 (3560) | 1.5% | 26.0% | 33.4% | 26.9% [25.2%-26.9%] | 7.2% | -- | 7.2% | MODEL_LONE_OUTLIER | PASS | +25.4 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 827.0, B 117.0; serve-point win A 58.1%, B 46.7%; Elo A 1415.7, B 1233.8; model uncertainty 0.0087
* Form inputs: days since last match A 157, B 472; matches on record A 43, B 28; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26SEP30LUOSOE-SOE  (YES = Kanna Soeda)
Model: 27%
Kalshi: 2%
Gap: +25 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: SUPPORTS_MODEL_DIRECTION
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.000, surface_dev_loose +0.004, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anna Yang vs Zijun Jiang -- W15 Maanshan R16

ITF (ITF) · Hard · scheduled 2026-10-01T08:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:223214:264242:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zijun Jiang (`KXITFWMATCH-26SEP30YANJIA-JIA`) | 0.76 / 0.77 (5312) | 76.5% | 58.2% | 55.3% | 58.4% [57.4%-58.5%] | 71.1% | -- | 71.1% | MODEL_LONE_OUTLIER | PASS | -18.1 pp | HIGH_REVIEW | STALE | F / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Anna Yang (`KXITFWMATCH-26SEP30YANJIA-YAN`) | 0.23 / 0.25 (5945) | 24.0% | 41.8% | 44.7% | 41.6% [41.5%-42.6%] | 28.9% | -- | 28.9% | KALSHI_LONE_OUTLIER | PASS | +17.6 pp | HIGH_REVIEW | STALE | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 270.0, B 178.0; serve-point win A 54.9%, B 43.5%; Elo A 1302.6, B 1360.3; model uncertainty 0.0054
* Form inputs: days since last match A 339, B 157; matches on record A 21, B 73; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26SEP30YANJIA-YAN  (YES = Anna Yang)
Model: 42%
Kalshi: 24%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_KALSHI
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jean-Julien Rojer / Theodore Winegar vs Theo Arribage / Albano Olivetti -- ATP Tokyo R16

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-01T08:40:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01ROJWINARROLI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theo Arribage / Albano Olivetti (`KXATPDOUBLES-26OCT01ROJWINARROLI-ARROLI`) | 0.25 / 0.75 (30) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jean-Julien Rojer / Theodore Winegar (`KXATPDOUBLES-26OCT01ROJWINARROLI-ROJWIN`) | 0.05 / 0.95 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Nino Ehrenschneider vs James Van Herzeele -- M15 Luan R16

ITF (ITF) · Hard · scheduled 2026-10-01T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:209510:211329:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nino Ehrenschneider (`KXITFMATCH-26SEP30EHRVAN-EHR`) | 0.98 / 0.99 (3006) | 98.5% | 75.4% | 75.4% | 75.9% [74.2%-77.5%] | 78.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -22.6 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| James Van Herzeele (`KXITFMATCH-26SEP30EHRVAN-VAN`) | 0.01 / 0.02 (2951) | 1.5% | 24.6% | 24.6% | 24.1% [22.5%-25.8%] | 21.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +22.6 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3879.0, B 966.0; serve-point win A 65.3%, B 40.1%; Elo A 1381.4, B 1175.7; model uncertainty 0.0164
* Form inputs: days since last match A 129, B 122; matches on record A 139, B 27; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26SEP30EHRVAN-VAN  (YES = James Van Herzeele)
Model: 24%
Kalshi: 2%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.016, surface_dev_loose +0.012, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kosuke Ogura vs Dong Ju Kim -- M15 Luan R16

ITF (ITF) · Hard · scheduled 2026-10-01T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:202124:207456:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dong Ju Kim (`KXITFMATCH-26SEP30OGUKIM-KIM`) | 0.66 / 0.67 (2395) | 66.5% | 64.7% | 65.6% | 64.6% [63.2%-66.1%] | -- | -- | -- | -- | PASS | -1.9 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kosuke Ogura (`KXITFMATCH-26SEP30OGUKIM-OGU`) | 0.33 / 0.34 (11) | 33.5% | 35.3% | 34.4% | 35.4% [33.9%-36.8%] | -- | -- | -- | -- | PASS | +1.9 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3515.0, B 1970.0; serve-point win A 61.1%, B 35.9%; Elo A 1257.4, B 1357.6; model uncertainty 0.0146
* Form inputs: days since last match A 122, B 129; matches on record A 256, B 64; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.010, surface_dev_loose -0.004, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yua Taka vs Isaac Becroft -- M15 Luan R16

ITF (ITF) · Hard · scheduled 2026-10-01T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208653:212196:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isaac Becroft (`KXITFMATCH-26SEP30TAKBEC-BEC`) | 0.64 / 0.65 (69) | 64.5% | 72.9% | 85.7% | 75.5% [71.2%-80.9%] | 73.6% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +11.1 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yua Taka (`KXITFMATCH-26SEP30TAKBEC-TAK`) | 0.34 / 0.35 (553) | 34.5% | 27.1% | 14.3% | 24.4% [19.1%-28.8%] | 26.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -10.1 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 614.0, B 1967.0; serve-point win A 60.2%, B 35.0%; Elo A 1175.9, B 1327.7; model uncertainty 0.0488
* Form inputs: days since last match A 129, B 143; matches on record A 25, B 111; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.000, surface_dev_loose -0.012, surface_dev_tight +0.017
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Di Tommaso / Simes vs Hosoki / Sato -- W35 Wagga Wagga QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26SEP30DITSIMHOSSAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Di Tommaso / Simes (`KXITFWDOUBLES-26SEP30DITSIMHOSSAT-DITSIM`) | 0.08 / 0.11 (407) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hosoki / Sato (`KXITFWDOUBLES-26SEP30DITSIMHOSSAT-HOSSAT`) | 0.90 / 0.91 (814) | 90.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Khan / McKenzie vs Arakawa / Tse -- W35 Wagga Wagga QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26SEP30KHAMCKARATSE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arakawa / Tse (`KXITFWDOUBLES-26SEP30KHAMCKARATSE-ARATSE`) | 0.97 / 0.98 (1491) | 97.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Khan / McKenzie (`KXITFWDOUBLES-26SEP30KHAMCKARATSE-KHAMCK`) | 0.02 / 0.03 (159) | 2.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Stevens / Thompson vs Muramatsu / Sato -- W35 Wagga Wagga QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26SEP30STETHOMURSAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Muramatsu / Sato (`KXITFWDOUBLES-26SEP30STETHOMURSAT-MURSAT`) | 0.67 / 0.69 (150) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stevens / Thompson (`KXITFWDOUBLES-26SEP30STETHOMURSAT-STETHO`) | 0.28 / 0.31 (80) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Gonzalo Escobar / Niki Kaliyanda Poonacha vs Mitsuki Wei Kang Leong / Stefanos Sakellaridis -- ATP Challenger Jingshan QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T09:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01ESCKALLEOSAK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gonzalo Escobar / Niki Kaliyanda Poonacha (`KXATPCHALLENGERDOUBLES-26OCT01ESCKALLEOSAK-ESCKAL`) | 0.75 / 0.80 (2500) | 77.5% | 31.8% | -- | -- [-----] | -- | -- | -- | -- | -- | -45.7 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Mitsuki Wei Kang Leong / Stefanos Sakellaridis (`KXATPCHALLENGERDOUBLES-26OCT01ESCKALLEOSAK-LEOSAK`) | 0.20 / 0.24 (34) | 22.0% | 68.2% | -- | -- [-----] | -- | -- | -- | -- | -- | +46.2 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERDOUBLES-26OCT01ESCKALLEOSAK-LEOSAK  (YES = Mitsuki Wei Kang Leong / Stefanos Sakellaridis)
Model: 68%
Kalshi: 22%
Gap: +46 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, PLAYER_IDENTITY_RISK, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Warnings: DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE

## Aliona Falei vs Kristiana Sidorova -- WTA 125K Jingshan R16

WTA125 (WTA_125) · Hard · scheduled 2026-10-01T09:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221434:260006:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aliona Falei (`KXWTACHALLENGERMATCH-26OCT01FALSID-FAL`) | 0.59 / 0.60 (1564) | 59.5% | 73.7% | 85.2% | 81.3% [76.7%-83.3%] | 59.9% | 60.3% | 60.3% | MODEL_LONE_OUTLIER | WATCH | +21.8 pp | HIGH_REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Kristiana Sidorova (`KXWTACHALLENGERMATCH-26OCT01FALSID-SID`) | 0.40 / 0.41 (12750) | 40.5% | 26.3% | 14.8% | 18.7% [16.7%-23.3%] | 40.1% | 39.7% | 39.7% | MODEL_LONE_OUTLIER | PASS | -21.8 pp | HIGH_REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3528.0, B 2506.0; serve-point win A 58.1%, B 46.7%; Elo A 1740.5, B 1565.0; model uncertainty 0.0328
* Form inputs: days since last match A 2, B 2; matches on record A 279, B 137; data quality A

```
DISCREPANCY SANITY CHECK  KXWTACHALLENGERMATCH-26OCT01FALSID-FAL  (YES = Aliona Falei)
Model: 81%
Kalshi: 60%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: EXTERNAL_STALE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.007, surface_dev_loose +0.007, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Barry / Hanatani vs Kitahara / Wen Wan -- W35 Wagga Wagga QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T10:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01BARHANKITWEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barry / Hanatani (`KXITFWDOUBLES-26OCT01BARHANKITWEN-BARHAN`) | 0.47 / 0.56 (68) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kitahara / Wen Wan (`KXITFWDOUBLES-26OCT01BARHANKITWEN-KITWEN`) | 0.40 / 0.48 (173) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Chen / Komagata vs Han / Zhang -- M15 Luan QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01CHEKOMHANZHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chen / Komagata (`KXITFDOUBLES-26OCT01CHEKOMHANZHA-CHEKOM`) | 0.06 / 0.83 (147) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Han / Zhang (`KXITFDOUBLES-26OCT01CHEKOMHANZHA-HANZHA`) | 0.12 / 0.45 (45) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## HSUN LIN / Yang vs KUAN LAI / Wang -- M15 Luan QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01HSUYANKUAWAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| HSUN LIN / Yang (`KXITFDOUBLES-26OCT01HSUYANKUAWAN-HSUYAN`) | 0.12 / 0.57 (53) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| KUAN LAI / Wang (`KXITFDOUBLES-26OCT01HSUYANKUAWAN-KUAWAN`) | 0.42 / 0.51 (41) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Ichikawa / Jeong vs Beamish / Shearer -- M15 Luan QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01ICHJEOBEASHE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Beamish / Shearer (`KXITFDOUBLES-26OCT01ICHJEOBEASHE-BEASHE`) | 0.48 / 0.68 (18) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ichikawa / Jeong (`KXITFDOUBLES-26OCT01ICHJEOBEASHE-ICHJEO`) | 0.32 / 0.49 (474) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Tomida / Yamanaka vs SUN / Wang -- M15 Luan QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01TOMYAMSUNWAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SUN / Wang (`KXITFDOUBLES-26OCT01TOMYAMSUNWAN-SUNWAN`) | 0.25 / 0.30 (11) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tomida / Yamanaka (`KXITFDOUBLES-26OCT01TOMYAMSUNWAN-TOMYAM`) | 0.52 / 0.67 (14) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Hou / Eum Lee vs Yi Liu / Sun -- W15 Maanshan QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01HOUEUMYILSUN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hou / Eum Lee (`KXITFWDOUBLES-26OCT01HOUEUMYILSUN-HOUEUM`) | 0.62 / 0.65 (2) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yi Liu / Sun (`KXITFWDOUBLES-26OCT01HOUEUMYILSUN-YILSUN`) | 0.03 / 0.35 (12) | 19.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hu / Xu vs Chen / Tang -- W15 Maanshan QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01HUXXUXCHETAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chen / Tang (`KXITFWDOUBLES-26OCT01HUXXUXCHETAN-CHETAN`) | 0.20 / 0.30 (14) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hu / Xu (`KXITFWDOUBLES-26OCT01HUXXUXCHETAN-HUXXUX`) | 0.49 / 0.72 (15) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Kakenova / Toregen vs Yi Chen / Luo -- W15 Maanshan QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01KAKTORYICLUO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kakenova / Toregen (`KXITFWDOUBLES-26OCT01KAKTORYICLUO-KAKTOR`) | 0.03 / 0.76 (1) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yi Chen / Luo (`KXITFWDOUBLES-26OCT01KAKTORYICLUO-YICLUO`) | 0.12 / 0.88 (65) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Marie Desvignes / Thamchaiwat vs Choi / Suvirdjonkova -- W15 Maanshan QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01MARTHACHOSUV:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Choi / Suvirdjonkova (`KXITFWDOUBLES-26OCT01MARTHACHOSUV-CHOSUV`) | 0.29 / 0.52 (17) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marie Desvignes / Thamchaiwat (`KXITFWDOUBLES-26OCT01MARTHACHOSUV-MARTHA`) | 0.28 / 0.70 (18) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Jeremy Beale vs Derek Pham -- M25 Darwin R16

ITF (ITF) · Hard · scheduled 2026-10-01T11:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:200003:210613:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jeremy Beale (`KXITFMATCH-26OCT01BEAPHA-BEA`) | 0.50 / 0.52 (2975) | 51.0% | 70.0% | 29.4% | 66.0% [60.7%-70.6%] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +15.0 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Derek Pham (`KXITFMATCH-26OCT01BEAPHA-PHA`) | 0.48 / 0.50 (1940) | 49.0% | 30.0% | 70.6% | 34.0% [29.4%-39.3%] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.0 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 203.0, B 178.0; serve-point win A 64.7%, B 39.5%; Elo A 1459.3, B 1312.3; model uncertainty 0.0495
* Form inputs: days since last match A 1095, B 318; matches on record A 215, B 71; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.009, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Casey Hoole vs Mustafa Ege Sik -- M25 Darwin R16

ITF (ITF) · Hard · scheduled 2026-10-01T11:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:211315:213802:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Casey Hoole (`KXITFMATCH-26OCT01HOOSIK-HOO`) | 0.85 / 0.86 (120) | 85.5% | 69.0% | 72.9% | 69.8% [68.0%-71.5%] | 70.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.7 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mustafa Ege Sik (`KXITFMATCH-26OCT01HOOSIK-SIK`) | 0.13 / 0.15 (2494) | 14.0% | 31.0% | 27.1% | 30.2% [28.5%-32.0%] | 29.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +16.2 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 187.0, B 663.0; serve-point win A 64.5%, B 39.4%; Elo A 1372.4, B 1233.7; model uncertainty 0.0177
* Form inputs: days since last match A 640, B 185; matches on record A 18, B 13; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01HOOSIK-SIK  (YES = Mustafa Ege Sik)
Model: 30%
Kalshi: 14%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.018, surface_pool_high +0.009, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Scott Jones vs Shintaro Imai -- M25 Darwin R16

ITF (ITF) · Hard · scheduled 2026-10-01T11:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:122495:206921:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shintaro Imai (`KXITFMATCH-26OCT01JONIMA-IMA`) | 0.59 / 0.60 (927) | 59.5% | 65.3% | 63.6% | 67.8% [65.9%-69.2%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +8.3 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Scott Jones (`KXITFMATCH-26OCT01JONIMA-JON`) | 0.40 / 0.41 (1770) | 40.5% | 34.7% | 36.4% | 32.2% [30.8%-34.1%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.3 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1787.0, B 2185.0; serve-point win A 61.0%, B 35.9%; Elo A 1333.5, B 1496.4; model uncertainty 0.0164
* Form inputs: days since last match A 192, B 129; matches on record A 62, B 483; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Philip Sekulic vs Zaharije-Zak Talic -- M25 Darwin R16

ITF (ITF) · Hard · scheduled 2026-10-01T11:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210340:210580:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Philip Sekulic (`KXITFMATCH-26OCT01SEKTAL-SEK`) | 0.95 / 0.97 (435) | 96.0% | 93.8% | 93.7% | 93.8% [92.8%-95.1%] | 95.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.2 pp | NORMAL | STALE | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zaharije-Zak Talic (`KXITFMATCH-26OCT01SEKTAL-TAL`) | 0.03 / 0.06 (4320) | 4.5% | 6.2% | 6.3% | 6.2% [4.9%-7.2%] | 4.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.7 pp | NORMAL | STALE | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4539.0, B 375.0; serve-point win A 68.7%, B 43.5%; Elo A 1562.7, B 1092.0; model uncertainty 0.0116
* Form inputs: days since last match A 9, B 136; matches on record A 316, B 32; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.004, surface_dev_loose +0.004, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arda Azkara vs Rohan Mehra -- M15 Baku R16

ITF (ITF) · surface ? · scheduled 2026-10-01T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:207907:210002:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arda Azkara (`KXITFMATCH-26OCT01AZKMEH-AZK`) | 0.77 / 0.80 (5013) | 78.5% | 68.5% | 60.4% | 71.3% [68.2%-75.3%] | 76.8% | -- | 76.8% | MODEL_LONE_OUTLIER | PASS | -7.2 pp | NORMAL | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Rohan Mehra (`KXITFMATCH-26OCT01AZKMEH-MEH`) | 0.20 / 0.23 (659) | 21.5% | 31.4% | 39.6% | 28.7% [24.7%-31.8%] | 23.2% | -- | 23.2% | MODEL_LONE_OUTLIER | WATCH | +7.2 pp | NORMAL | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1821.0, B 1099.0; serve-point win A 65.9%, B 37.9%; Elo A 1438.0, B 1218.9; model uncertainty 0.0352
* Form inputs: days since last match A 59, B 192; matches on record A 94, B 41; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alessio Basile vs Dmitry Popko -- M15 Telavi QF

ITF (ITF) · Clay · scheduled 2026-10-01T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:122078:211450:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alessio Basile (`KXITFMATCH-26OCT01BASPOP-BAS`) | 0.14 / 0.17 (5) | 15.5% | 23.4% | 37.2% | 21.0% [10.7%-27.9%] | -- | -- | -- | -- | PASS | +5.5 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dmitry Popko (`KXITFMATCH-26OCT01BASPOP-POP`) | 0.82 / 0.85 (2308) | 83.5% | 76.6% | 62.7% | 79.0% [72.1%-89.3%] | -- | -- | -- | -- | PASS | -4.5 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 952.0, B 4384.0; serve-point win A 57.1%, B 37.3%; Elo A 1252.3, B 1577.9; model uncertainty 0.086
* Form inputs: days since last match A 311, B 87; matches on record A 43, B 1042; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.039, surface_pool_high +0.043, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gabriele Bosio vs Stijn Paardekooper -- M15 Telavi QF

ITF (ITF) · Clay · scheduled 2026-10-01T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208152:212311:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriele Bosio (`KXITFMATCH-26OCT01BOSPAA-BOS`) | 0.35 / 0.38 (51) | 36.5% | 53.1% | 54.1% | 51.0% [49.0%-54.1%] | 37.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +14.5 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Stijn Paardekooper (`KXITFMATCH-26OCT01BOSPAA-PAA`) | 0.61 / 0.64 (4600) | 62.5% | 46.9% | 45.9% | 49.0% [45.9%-51.0%] | 62.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.5 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2924.0, B 1300.0; serve-point win A 60.2%, B 40.4%; Elo A 1335.5, B 1340.4; model uncertainty 0.0259
* Form inputs: days since last match A 122, B 206; matches on record A 191, B 45; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.031, surface_pool_high -0.021, surface_dev_loose +0.000, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oscar Brown vs Digvijay Pratap Singh -- M15 Baku R16

ITF (ITF) · surface ? · scheduled 2026-10-01T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:200014:214341:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oscar Brown (`KXITFMATCH-26OCT01BROSIN-BRO`) | 0.39 / 0.41 (904) | 40.0% | 39.3% | 34.8% | 38.1% [35.8%-39.1%] | 39.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.9 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Digvijay Pratap Singh (`KXITFMATCH-26OCT01BROSIN-SIN`) | 0.58 / 0.59 (63) | 58.5% | 60.7% | 65.2% | 61.9% [60.9%-64.2%] | 60.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.4 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 423.0, B 2204.0; serve-point win A 62.9%, B 34.9%; Elo A 1284.8, B 1360.6; model uncertainty 0.0167
* Form inputs: days since last match A 157, B 17; matches on record A 8, B 181; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matic Dimic vs Nicola Rispoli -- M15 Telavi QF

ITF (ITF) · Clay · scheduled 2026-10-01T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:206580:210174:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matic Dimic (`KXITFMATCH-26OCT01DIMRIS-DIM`) | 0.22 / 0.24 (332) | 23.0% | 34.5% | 47.9% | 38.2% [34.3%-40.2%] | 24.7% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +15.2 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nicola Rispoli (`KXITFMATCH-26OCT01DIMRIS-RIS`) | 0.76 / 0.79 (8711) | 77.5% | 65.5% | 52.1% | 61.8% [59.8%-65.7%] | 75.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.7 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 459.0, B 480.0; serve-point win A 58.4%, B 38.6%; Elo A 1085.9, B 1196.9; model uncertainty 0.0292
* Form inputs: days since last match A 122, B 129; matches on record A 57, B 30; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01DIMRIS-DIM  (YES = Matic Dimic)
Model: 38%
Kalshi: 23%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Volodymyr Iakubenko vs Makar Krivoshchekov -- M15 Baku R16

ITF (ITF) · surface ? · scheduled 2026-10-01T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:212246:213185:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Volodymyr Iakubenko (`KXITFMATCH-26OCT01IAKKRI-IAK`) | 0.83 / 0.85 (911) | 84.0% | 73.7% | 67.0% | 72.0% [70.6%-73.3%] | 83.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.0 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Makar Krivoshchekov (`KXITFMATCH-26OCT01IAKKRI-KRI`) | 0.15 / 0.16 (3840) | 15.5% | 26.3% | 33.0% | 28.0% [26.7%-29.4%] | 17.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +12.5 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1553.0, B 493.0; serve-point win A 66.5%, B 38.5%; Elo A 1285.6, B 1106.9; model uncertainty 0.0135
* Form inputs: days since last match A 136, B 129; matches on record A 50, B 16; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dragos Nicolae Madaras vs Michele Mecarelli -- M15 Telavi QF

ITF (ITF) · Clay · scheduled 2026-10-01T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:200096:213356:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dragos Nicolae Madaras (`KXITFMATCH-26OCT01MADMEC-MAD`) | 0.73 / 0.75 (1521) | 74.0% | 87.2% | 97.9% | 93.3% [84.0%-96.5%] | 73.6% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +19.3 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Michele Mecarelli (`KXITFMATCH-26OCT01MADMEC-MEC`) | 0.24 / 0.26 (333) | 25.0% | 12.8% | 2.1% | 6.7% [3.5%-16.0%] | 26.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -18.3 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1481.0, B 1390.0; serve-point win A 64.3%, B 44.5%; Elo A 1646.0, B 1356.8; model uncertainty 0.0625
* Form inputs: days since last match A 185, B 52; matches on record A 475, B 30; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01MADMEC-MAD  (YES = Dragos Nicolae Madaras)
Model: 93%
Kalshi: 74%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.002, surface_dev_loose +0.014, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Snir Morag vs Louis Larue -- M15 Baku R16

ITF (ITF) · surface ? · scheduled 2026-10-01T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:211646:214598:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Louis Larue (`KXITFMATCH-26OCT01MORLAR-LAR`) | 0.71 / 0.73 (8) | 72.0% | 50.5% | 39.6% | 50.0% [50.0%-51.0%] | 71.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -22.0 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Snir Morag (`KXITFMATCH-26OCT01MORLAR-MOR`) | 0.26 / 0.28 (806) | 27.0% | 49.5% | 60.4% | 50.0% [48.9%-50.0%] | 28.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +23.0 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 83.0, B 1681.0; serve-point win A 63.9%, B 35.9%; Elo A 1257.6, B 1260.9; model uncertainty 0.0053
* Form inputs: days since last match A 122, B 136; matches on record A 1, B 48; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01MORLAR-MOR  (YES = Snir Morag)
Model: 50%
Kalshi: 27%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Joel Schwaerzler vs Harry Wendelken -- ATP Challenger Mouilleron-Le-Captif R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:207784:212082:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joel Schwaerzler (`KXATPCHALLENGERMATCH-26OCT01SCHWEN-SCH`) | 0.44 / 0.45 (9781) | 44.5% | 38.6% | 26.5% | 30.8% [27.0%-36.7%] | -- | 43.9% | 43.9% | MODEL_LONE_OUTLIER | PASS | -13.7 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Harry Wendelken (`KXATPCHALLENGERMATCH-26OCT01SCHWEN-WEN`) | 0.56 / 0.57 (3841) | 56.5% | 61.4% | 73.5% | 69.2% [63.3%-73.0%] | -- | 56.2% | 56.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +12.7 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4727.0, B 4008.0; serve-point win A 61.5%, B 36.3%; Elo A 1601.4, B 1659.8; model uncertainty 0.0488
* Form inputs: days since last match A 10, B 10; matches on record A 191, B 314; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.017, surface_dev_loose -0.013, surface_dev_tight +0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Franco Agamenone / Giorgio Ricca vs Oleksandr Ovcharenko / Kai Wehnelt -- ATP Challenger Bari QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01AGARICOVCWEH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Franco Agamenone / Giorgio Ricca (`KXATPCHALLENGERDOUBLES-26OCT01AGARICOVCWEH-AGARIC`) | 0.37 / 0.75 (25) | 56.0% | 43.4% | -- | -- [-----] | -- | -- | -- | -- | -- | -12.6 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Oleksandr Ovcharenko / Kai Wehnelt (`KXATPCHALLENGERDOUBLES-26OCT01AGARICOVCWEH-OVCWEH`) | 0.06 / 0.63 (136) | 34.5% | 56.6% | -- | -- [-----] | -- | -- | -- | -- | -- | +22.1 pp | HIGH_REVIEW (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERDOUBLES-26OCT01AGARICOVCWEH-OVCWEH  (YES = Oleksandr Ovcharenko / Kai Wehnelt)
Model: 57%
Kalshi: 34%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, PLAYER_IDENTITY_RISK, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Warnings: DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Chen Dong vs Colin Sinclair -- M25 Darwin R16

ITF (ITF) · Hard · scheduled 2026-10-01T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:124040:211317:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chen Dong (`KXITFMATCH-26OCT01DONSIN-DON`) | 0.30 / 0.32 (4651) | 31.0% | 37.9% | 46.6% | 39.3% [32.8%-42.7%] | 30.8% | -- | 30.8% | MARKETS_AGREE | WATCH | +8.3 pp | NORMAL | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Colin Sinclair (`KXITFMATCH-26OCT01DONSIN-SIN`) | 0.67 / 0.70 (18) | 68.5% | 62.1% | 53.4% | 60.7% [57.3%-67.2%] | 69.2% | -- | 69.2% | MARKETS_AGREE | PASS | -7.8 pp | NORMAL | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1294.0, B 4093.0; serve-point win A 61.4%, B 36.2%; Elo A 1303.9, B 1423.3; model uncertainty 0.0495
* Form inputs: days since last match A 171, B 17; matches on record A 42, B 427; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.024, surface_pool_high +0.024, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Reece Falck vs Herman Hoeyeraal -- M25 Darwin R16

ITF (ITF) · Hard · scheduled 2026-10-01T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208382:209392:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Reece Falck (`KXITFMATCH-26OCT01FALHOE-FAL`) | 0.53 / 0.57 (5981) | 55.0% | 31.7% | 23.2% | 27.3% [25.6%-30.2%] | -- | -- | -- | -- | PASS | -27.7 pp | EXTREME (DATA_WARNING) | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Herman Hoeyeraal (`KXITFMATCH-26OCT01FALHOE-HOE`) | 0.44 / 0.47 (1285) | 45.5% | 68.3% | 76.8% | 72.7% [69.8%-74.4%] | -- | -- | -- | -- | WATCH | +27.2 pp | EXTREME (DATA_WARNING) | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1394.0, B 1869.0; serve-point win A 60.7%, B 35.5%; Elo A 1190.2, B 1322.1; model uncertainty 0.023
* Form inputs: days since last match A 122, B 87; matches on record A 52, B 42; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01FALHOE-HOE  (YES = Herman Hoeyeraal)
Model: 73%
Kalshi: 46%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_KALSHI_QUOTE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.017, surface_pool_high +0.026, surface_dev_loose -0.012, surface_dev_tight +0.017
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Massimo Giunta vs Carlos Taberner -- ATP Challenger Bari R16

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-01T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:126535:210668:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Massimo Giunta (`KXATPCHALLENGERMATCH-26OCT01GIUTAB-GIU`) | 0.36 / 0.37 (3457) | 36.5% | 28.6% | 45.0% | 34.8% [29.3%-39.0%] | 37.5% | 37.4% | 37.4% | MARKETS_AGREE | PASS | -1.8 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Carlos Taberner (`KXATPCHALLENGERMATCH-26OCT01GIUTAB-TAB`) | 0.62 / 0.63 (2013) | 62.5% | 71.4% | 55.0% | 65.2% [61.0%-70.7%] | 62.5% | 62.5% | 62.5% | MODEL_LONE_OUTLIER | WATCH | +2.8 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3586.0, B 4908.0; serve-point win A 57.7%, B 37.9%; Elo A 1453.6, B 1745.9; model uncertainty 0.0487
* Form inputs: days since last match A 17, B 10; matches on record A 179, B 923; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.009, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Laurent Lokoli vs Samuele Pieri -- ATP Challenger Bari R16

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-01T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:106362:210129:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Laurent Lokoli (`KXATPCHALLENGERMATCH-26OCT01LOKPIE-LOK`) | 0.59 / 0.60 (3292) | 59.5% | 48.0% | 32.5% | 40.3% [34.8%-49.5%] | 59.9% | 59.7% | 59.7% | MODEL_LONE_OUTLIER | PASS | -19.2 pp | HIGH_REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Samuele Pieri (`KXATPCHALLENGERMATCH-26OCT01LOKPIE-PIE`) | 0.39 / 0.41 (3426) | 40.0% | 52.0% | 67.5% | 59.7% [50.5%-65.1%] | 40.1% | 40.3% | 40.3% | MODEL_LONE_OUTLIER | WATCH | +19.7 pp | HIGH_REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3540.0, B 4011.0; serve-point win A 59.7%, B 39.9%; Elo A 1580.2, B 1518.3; model uncertainty 0.0732
* Form inputs: days since last match A 24, B 10; matches on record A 756, B 209; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT01LOKPIE-PIE  (YES = Samuele Pieri)
Model: 60%
Kalshi: 40%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: EXTERNAL_STALE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.025, surface_dev_loose -0.005, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Lachlan Vickery vs Jake Delaney -- M25 Darwin R16

ITF (ITF) · Hard · scheduled 2026-10-01T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:117359:212956:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jake Delaney (`KXITFMATCH-26OCT01VICDEL-DEL`) | 0.90 / 0.91 (5372) | 90.5% | 84.2% | 81.2% | 83.8% [83.0%-85.7%] | 89.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.7 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lachlan Vickery (`KXITFMATCH-26OCT01VICDEL-VIC`) | 0.10 / 0.11 (5244) | 10.5% | 15.8% | 18.8% | 16.2% [14.3%-17.0%] | 11.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.7 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 222.0, B 4278.0; serve-point win A 58.6%, B 33.4%; Elo A 1164.6, B 1455.6; model uncertainty 0.0132
* Form inputs: days since last match A 122, B 9; matches on record A 12, B 364; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high -0.006, surface_dev_loose -0.006, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anton Arzhankin vs Yurii Dzhavakian -- M15 Sharm ElSheikh R16

ITF (ITF) · Hard · scheduled 2026-10-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:122113:213996:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anton Arzhankin (`KXITFMATCH-26OCT01ARZDZH-ARZ`) | 0.69 / 0.74 (0) | 71.5% | 66.6% | 84.5% | 74.9% [63.2%-80.2%] | -- | -- | -- | -- | PASS | +3.4 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yurii Dzhavakian (`KXITFMATCH-26OCT01ARZDZH-DZH`) | 0.26 / 0.30 (91) | 28.0% | 33.4% | 15.5% | 25.1% [19.8%-36.8%] | -- | -- | -- | -- | PASS | -2.9 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1841.0, B 5305.0; serve-point win A 64.3%, B 39.1%; Elo A 1441.2, B 1374.7; model uncertainty 0.0853
* Form inputs: days since last match A 122, B 136; matches on record A 34, B 442; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose +0.019, surface_dev_tight -0.025
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gabi Adrian Boitan vs Cezar Stefan Bentzel -- M25 Slobozia R16

ITF (ITF) · surface ? · scheduled 2026-10-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01BOIBEN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cezar Stefan Bentzel (`KXITFMATCH-26OCT01BOIBEN-BEN`) | 0.07 / 0.08 (391) | 7.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gabi Adrian Boitan (`KXITFMATCH-26OCT01BOIBEN-BOI`) | 0.91 / 0.93 (2331) | 92.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dzmitry Dziubailau vs Amr Elsayed -- M15 Sharm ElSheikh R16

ITF (ITF) · surface ? · scheduled 2026-10-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01DZIELS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dzmitry Dziubailau (`KXITFMATCH-26OCT01DZIELS-DZI`) | 0.07 / 0.10 (0) | 8.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Amr Elsayed (`KXITFMATCH-26OCT01DZIELS-ELS`) | 0.90 / 0.93 (10) | 91.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Goncalo Marques vs David Jorda Sanchis -- ATP Challenger Porto 2 R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:122554:149128:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| David Jorda Sanchis (`KXATPCHALLENGERMATCH-26OCT01MARJOR-JOR`) | 0.57 / 0.58 (9481) | 57.5% | 75.6% | 63.9% | 75.4% [68.6%-83.5%] | 56.3% | 57.2% | 57.2% | MODEL_LONE_OUTLIER | WATCH | +17.9 pp | HIGH_REVIEW | STALE | C / LIMITED | EXTERNAL_STALE | VERIFIED |
| Goncalo Marques (`KXATPCHALLENGERMATCH-26OCT01MARJOR-MAR`) | 0.42 / 0.43 (3060) | 42.5% | 24.4% | 36.1% | 24.6% [16.5%-31.4%] | 43.7% | 43.7% | 43.7% | MODEL_LONE_OUTLIER | PASS | -17.9 pp | HIGH_REVIEW | STALE | C / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 897.0, B 5646.0; serve-point win A 59.9%, B 34.7%; Elo A 1245.6, B 1499.8; model uncertainty 0.0744
* Form inputs: days since last match A 31, B 10; matches on record A 35, B 495; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT01MARJOR-JOR  (YES = David Jorda Sanchis)
Model: 75%
Kalshi: 57%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: EXTERNAL_STALE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.052, surface_pool_high +0.055, surface_dev_loose +0.004, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Mishkin / Shvets vs Angeloni / Cherie Ligniere -- M15 Telavi SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01MISSHVANGCHE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Angeloni / Cherie Ligniere (`KXITFDOUBLES-26OCT01MISSHVANGCHE-ANGCHE`) | 0.44 / 0.50 (11) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mishkin / Shvets (`KXITFDOUBLES-26OCT01MISSHVANGCHE-MISSHV`) | 0.42 / 0.52 (2) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jannik Opitz vs Ryo Tabata -- M25 Slobozia R16

ITF (ITF) · Clay · scheduled 2026-10-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:200457:212944:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jannik Opitz (`KXITFMATCH-26OCT01OPITAB-OPI`) | 0.44 / 0.46 (4268) | 45.0% | 46.2% | 47.0% | 39.1% [36.8%-41.1%] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.9 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ryo Tabata (`KXITFMATCH-26OCT01OPITAB-TAB`) | 0.53 / 0.56 (5) | 54.5% | 53.8% | 53.0% | 60.9% [58.9%-63.2%] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +6.4 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 858.0, B 1760.0; serve-point win A 59.5%, B 39.7%; Elo A 1217.8, B 1328.0; model uncertainty 0.0212
* Form inputs: days since last match A 164, B 108; matches on record A 50, B 41; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.014, surface_dev_loose -0.023, surface_dev_tight +0.019
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rares Teodor Pieleanu vs Florian Broska -- M25 Slobozia R16

ITF (ITF) · Clay · scheduled 2026-10-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:202239:212888:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Florian Broska (`KXITFMATCH-26OCT01PIEBRO-BRO`) | 0.77 / 0.78 (2565) | 77.5% | 78.6% | 83.6% | 80.9% [79.1%-82.3%] | 74.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.4 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rares Teodor Pieleanu (`KXITFMATCH-26OCT01PIEBRO-PIE`) | 0.22 / 0.23 (4269) | 22.5% | 21.4% | 16.4% | 19.1% [17.7%-20.9%] | 25.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.4 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1890.0, B 3459.0; serve-point win A 56.8%, B 37.0%; Elo A 1278.2, B 1488.2; model uncertainty 0.0158
* Form inputs: days since last match A 122, B 10; matches on record A 61, B 219; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.018, surface_dev_loose -0.007, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniel Rincon vs Laslo Djere -- ATP Challenger Porto 2 R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:111513:209405:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Laslo Djere (`KXATPCHALLENGERMATCH-26OCT01RINDJE-DJE`) | 0.55 / 0.56 (4015) | 55.5% | 63.4% | 61.1% | 61.6% [59.6%-63.1%] | -- | 55.0% | 55.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.1 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Daniel Rincon (`KXATPCHALLENGERMATCH-26OCT01RINDJE-RIN`) | 0.43 / 0.44 (3920) | 43.5% | 36.6% | 38.9% | 38.4% [36.9%-40.4%] | -- | 45.7% | 45.7% | ALL_THREE_DISAGREE | PASS | -5.1 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5943.0, B 4719.0; serve-point win A 61.2%, B 36.1%; Elo A 1617.2, B 1685.2; model uncertainty 0.0173
* Form inputs: days since last match A 10, B 17; matches on record A 422, B 923; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.020, surface_dev_loose +0.020, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Toby Samuel vs Jerome Kym -- ATP Challenger Porto 2 R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208843:210389:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jerome Kym (`KXATPCHALLENGERMATCH-26OCT01SAMKYM-KYM`) | 0.34 / 0.35 (3418) | 34.5% | 33.2% | 20.1% | 23.0% [20.8%-28.1%] | 36.9% | 34.8% | 34.8% | MODEL_LONE_OUTLIER | PASS | -11.5 pp | REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Toby Samuel (`KXATPCHALLENGERMATCH-26OCT01SAMKYM-SAM`) | 0.65 / 0.66 (4505) | 65.5% | 66.8% | 79.9% | 77.0% [71.9%-79.2%] | 63.1% | 67.2% | 67.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +11.5 pp | REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4028.0, B 3926.0; serve-point win A 64.3%, B 39.1%; Elo A 1834.3, B 1694.4; model uncertainty 0.0367
* Form inputs: days since last match A 29, B 30; matches on record A 189, B 311; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.007, surface_dev_loose +0.018, surface_dev_tight -0.023
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Robert Strombachs vs Luca Castagnola -- M15 Sharm ElSheikh R16

ITF (ITF) · Hard · scheduled 2026-10-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:207669:209337:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luca Castagnola (`KXITFMATCH-26OCT01STRCAS-CAS`) | 0.17 / 0.22 (6005) | 19.5% | 21.1% | 12.6% | 14.3% [12.3%-20.5%] | -- | -- | -- | -- | PASS | -5.2 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Robert Strombachs (`KXITFMATCH-26OCT01STRCAS-STR`) | 0.78 / 0.84 (2024) | 81.0% | 78.9% | 87.4% | 85.7% [79.5%-87.7%] | -- | -- | -- | -- | WATCH | +4.7 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3812.0, B 3309.0; serve-point win A 65.8%, B 40.6%; Elo A 1528.0, B 1267.2; model uncertainty 0.0409
* Form inputs: days since last match A 17, B 122; matches on record A 483, B 219; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.011, surface_dev_loose +0.014, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Radu David Turcanu vs Lukas Pokorny -- M25 Slobozia R16

ITF (ITF) · Clay · scheduled 2026-10-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:209931:212886:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lukas Pokorny (`KXITFMATCH-26OCT01TURPOK-POK`) | 0.53 / 0.55 (57) | 54.0% | 51.5% | 49.5% | 48.5% [43.9%-56.6%] | 53.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.5 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Radu David Turcanu (`KXITFMATCH-26OCT01TURPOK-TUR`) | 0.44 / 0.47 (3) | 45.5% | 48.5% | 50.5% | 51.5% [43.4%-56.1%] | 46.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +6.0 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2393.0, B 3398.0; serve-point win A 59.8%, B 40.0%; Elo A 1462.2, B 1444.2; model uncertainty 0.0637
* Form inputs: days since last match A 122, B 115; matches on record A 70, B 280; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.051, surface_pool_high +0.046, surface_dev_loose +0.010, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Fares Zakaria vs Gawad El Feky -- M15 Sharm ElSheikh R16

ITF (ITF) · surface ? · scheduled 2026-10-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01ZAKELF:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gawad El Feky (`KXITFMATCH-26OCT01ZAKELF-ELF`) | 0.24 / 0.26 (33) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fares Zakaria (`KXITFMATCH-26OCT01ZAKELF-ZAK`) | 0.72 / 0.76 (2998) | 74.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofia Avataneo vs Daria Zelinskaya -- W15 Sharm ElSheikh R16

ITF (ITF) · Hard · scheduled 2026-10-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:239158:242450:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Avataneo (`KXITFWMATCH-26OCT01AVAZEL-AVA`) | 0.09 / 0.12 (4574) | 10.5% | 10.6% | 2.2% | 7.6% [3.9%-13.3%] | -- | -- | -- | -- | PASS | -2.9 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daria Zelinskaya (`KXITFWMATCH-26OCT01AVAZEL-ZEL`) | 0.87 / 0.90 (20) | 88.5% | 89.4% | 97.8% | 92.4% [86.7%-96.1%] | -- | -- | -- | -- | WATCH | +3.9 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 821.0, B 2491.0; serve-point win A 51.0%, B 39.6%; Elo A 1178.7, B 1503.3; model uncertainty 0.0466
* Form inputs: days since last match A 157, B 81; matches on record A 143, B 171; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.004, surface_dev_loose -0.012, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carolina Gasparini vs Sapfo Sakellaridi -- W15 Varna R16

ITF (ITF) · Clay · scheduled 2026-10-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220364:270067:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carolina Gasparini (`KXITFWMATCH-26OCT01GASSAK-GAS`) | 0.14 / 0.17 (3255) | 15.5% | 13.6% | 12.6% | 13.4% [12.3%-14.6%] | 18.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.1 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sapfo Sakellaridi (`KXITFWMATCH-26OCT01GASSAK-SAK`) | 0.83 / 0.85 (32) | 84.0% | 86.4% | 87.4% | 86.6% [85.4%-87.7%] | 81.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.6 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 271.0, B 4165.0; serve-point win A 49.9%, B 41.9%; Elo A 1218.3, B 1539.3; model uncertainty 0.0113
* Form inputs: days since last match A 283, B 79; matches on record A 7, B 703; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.012, surface_dev_loose +0.001, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuliya Hatouka vs Anja Wildgruber -- W15 Sharm ElSheikh R16

ITF (ITF) · Hard · scheduled 2026-10-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:216013:222668:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuliya Hatouka (`KXITFWMATCH-26OCT01HATWIL-HAT`) | 0.88 / 0.90 (1) | 89.0% | 84.1% | 91.2% | 89.4% [86.1%-90.6%] | -- | -- | -- | -- | PASS | +0.4 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anja Wildgruber (`KXITFWMATCH-26OCT01HATWIL-WIL`) | 0.10 / 0.11 (4048) | 10.5% | 15.9% | 8.8% | 10.6% [9.4%-13.9%] | -- | -- | -- | -- | PASS | +0.1 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2126.0, B 2380.0; serve-point win A 59.5%, B 48.1%; Elo A 1626.6, B 1305.7; model uncertainty 0.0221
* Form inputs: days since last match A 178, B 157; matches on record A 378, B 348; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.012, surface_pool_high -0.015, surface_dev_loose +0.012, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elena Jamshidi vs Charlotte Van Zonneveld -- W15 Sharm ElSheikh R16

ITF (ITF) · Hard · scheduled 2026-10-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220048:264252:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elena Jamshidi (`KXITFWMATCH-26OCT01JAMVAN-JAM`) | 0.19 / 0.23 (3846) | 21.0% | 42.8% | 31.0% | 39.9% [37.4%-42.0%] | -- | -- | -- | -- | PASS | +18.9 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Charlotte Van Zonneveld (`KXITFWMATCH-26OCT01JAMVAN-VAN`) | 0.77 / 0.81 (156) | 79.0% | 57.2% | 69.0% | 60.1% [58.0%-62.6%] | -- | -- | -- | -- | PASS | -18.9 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1121.0, B 578.0; serve-point win A 55.0%, B 43.6%; Elo A 1276.0, B 1320.6; model uncertainty 0.0233
* Form inputs: days since last match A 157, B 220; matches on record A 211, B 32; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01JAMVAN-JAM  (YES = Elena Jamshidi)
Model: 40%
Kalshi: 21%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.026, surface_pool_high +0.021, surface_dev_loose -0.005, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sandra Samir vs Jade Groen -- W15 Sharm ElSheikh R16

ITF (ITF) · Hard · scheduled 2026-10-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:211529:267722:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jade Groen (`KXITFWMATCH-26OCT01SAMGRO-GRO`) | 0.40 / 0.43 (1134) | 41.5% | 18.1% | 25.9% | 20.2% [16.7%-22.6%] | -- | -- | -- | -- | PASS | -21.2 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sandra Samir (`KXITFWMATCH-26OCT01SAMGRO-SAM`) | 0.58 / 0.59 (3951) | 58.5% | 81.9% | 74.1% | 79.8% [77.4%-83.3%] | -- | -- | -- | -- | PASS | +21.2 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4604.0, B 470.0; serve-point win A 59.1%, B 47.8%; Elo A 1560.7, B 1298.8; model uncertainty 0.0292
* Form inputs: days since last match A 25, B 325; matches on record A 806, B 9; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01SAMGRO-SAM  (YES = Sandra Samir)
Model: 80%
Kalshi: 58%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.015, surface_dev_loose +0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Viktoria Veleva vs Sonja Zhenikhova -- W15 Varna R16

ITF (ITF) · Clay · scheduled 2026-10-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:225861:264961:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Viktoria Veleva (`KXITFWMATCH-26OCT01VELZHE-VEL`) | 0.13 / 0.15 (3139) | 14.0% | 35.1% | 44.6% | 33.8% [28.6%-36.8%] | 16.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +19.8 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sonja Zhenikhova (`KXITFWMATCH-26OCT01VELZHE-ZHE`) | 0.85 / 0.87 (4304) | 86.0% | 64.9% | 55.4% | 66.2% [63.2%-71.4%] | 83.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -19.8 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1099.0, B 1212.0; serve-point win A 52.6%, B 44.6%; Elo A 1222.5, B 1407.0; model uncertainty 0.041
* Form inputs: days since last match A 157, B 220; matches on record A 85, B 38; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01VELZHE-VEL  (YES = Viktoria Veleva)
Model: 34%
Kalshi: 14%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.010, surface_dev_loose +0.000, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tara Wuerth vs Maia Ilinca Burcescu -- W15 Varna R16

ITF (ITF) · surface ? · scheduled 2026-10-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01WUEBUR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maia Ilinca Burcescu (`KXITFWMATCH-26OCT01WUEBUR-BUR`) | 0.37 / 0.38 (6086) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tara Wuerth (`KXITFWMATCH-26OCT01WUEBUR-WUE`) | 0.61 / 0.63 (2) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Henry Bernet vs Dominic Stricker -- ATP Challenger Mouilleron-Le-Captif R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T13:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:148679:208502:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Henry Bernet (`KXATPCHALLENGERMATCH-26OCT01BERSTR-BER`) | 0.39 / 0.40 (5493) | 39.5% | 27.2% | 18.8% | 21.5% [19.5%-24.0%] | -- | 40.8% | 40.8% | MODEL_LONE_OUTLIER | PASS | -18.0 pp | HIGH_REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Dominic Stricker (`KXATPCHALLENGERMATCH-26OCT01BERSTR-STR`) | 0.61 / 0.62 (7382) | 61.5% | 72.9% | 81.2% | 78.5% [76.0%-80.5%] | -- | 58.8% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +17.0 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2182.0, B 3840.0; serve-point win A 60.2%, B 35.0%; Elo A 1526.8, B 1710.1; model uncertainty 0.0226
* Form inputs: days since last match A 31, B 38; matches on record A 61, B 373; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT01BERSTR-STR  (YES = Dominic Stricker)
Model: 79%
Kalshi: 62%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.017, surface_pool_high +0.022, surface_dev_loose -0.020, surface_dev_tight +0.018
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Lois Boisson vs Anna Blinkova -- WTA 125K Adana QF

WTA125 (WTA_125) · surface ? · scheduled 2026-10-01T13:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:215020:222391:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Blinkova (`KXWTACHALLENGERMATCH-26OCT01BOIBLI-BLI`) | 0.59 / 0.60 (9899) | 59.5% | 46.3% | 31.6% | 43.1% [36.5%-53.2%] | 58.4% | 60.1% | 60.1% | MODEL_LONE_OUTLIER | PASS | -16.4 pp | HIGH_REVIEW | STALE | A / LIMITED | EXTERNAL_STALE | VERIFIED |
| Lois Boisson (`KXWTACHALLENGERMATCH-26OCT01BOIBLI-BOI`) | 0.40 / 0.41 (145) | 40.5% | 53.7% | 68.4% | 56.9% [46.8%-63.5%] | 41.6% | 41.4% | 41.4% | MODEL_LONE_OUTLIER | WATCH | +16.4 pp | HIGH_REVIEW | STALE | A / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 1582.0, B 4417.0; serve-point win A 57.4%, B 43.4%; Elo A 1873.0, B 1920.5; model uncertainty 0.0836
* Form inputs: days since last match A 1, B 3; matches on record A 242, B 634; data quality A

```
DISCREPANCY SANITY CHECK  KXWTACHALLENGERMATCH-26OCT01BOIBLI-BOI  (YES = Lois Boisson)
Model: 57%
Kalshi: 40%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: EXTERNAL_STALE
Data quality: A (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LEVEL_TRANSFER_RISK, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Elena Pridankina vs Erika Andreeva -- WTA 125K Adana QF

WTA125 (WTA_125) · surface ? · scheduled 2026-10-01T13:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:222965:239389:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Erika Andreeva (`KXWTACHALLENGERMATCH-26OCT01PRIAND-AND`) | 0.48 / 0.49 (2274) | 48.5% | 40.9% | 45.2% | 42.6% [41.0%-43.6%] | -- | -- | -- | -- | PASS | -5.9 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elena Pridankina (`KXWTACHALLENGERMATCH-26OCT01PRIAND-PRI`) | 0.51 / 0.52 (2079) | 51.5% | 59.1% | 54.8% | 57.4% [56.4%-59.0%] | -- | -- | -- | -- | SHADOW_BET | +5.9 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3685.0, B 3408.0; serve-point win A 57.9%, B 43.9%; Elo A 1853.3, B 1767.1; model uncertainty 0.013
* Form inputs: days since last match A 2, B 1; matches on record A 289, B 338; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Tamerlan Azizov vs Kerem Yilmaz -- M15 Baku R16

ITF (ITF) · surface ? · scheduled 2026-10-01T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210350:212030:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tamerlan Azizov (`KXITFMATCH-26OCT01AZIYIL-AZI`) | 0.06 / 0.08 (91) | 7.0% | 49.3% | 63.2% | 49.0% [49.0%-49.0%] | 6.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +42.0 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Kerem Yilmaz (`KXITFMATCH-26OCT01AZIYIL-YIL`) | 0.92 / 0.94 (85) | 93.0% | 50.7% | 36.8% | 51.0% [51.0%-51.0%] | 93.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -42.0 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 1537.0; serve-point win A 63.9%, B 35.9%; Elo A 1219.3, B 1224.3; model uncertainty 0.0
* Form inputs: days since last match A 899, B 59; matches on record A 3, B 45; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01AZIYIL-AZI  (YES = Tamerlan Azizov)
Model: 49%
Kalshi: 7%
Gap: +42 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Beale / Vujic vs Imai / Ochi -- M25 Darwin QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01BEAVUJIMAOCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Beale / Vujic (`KXITFDOUBLES-26OCT01BEAVUJIMAOCH-BEAVUJ`) | 0.07 / 0.59 (1098) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Imai / Ochi (`KXITFDOUBLES-26OCT01BEAVUJIMAOCH-IMAOCH`) | 0.14 / 0.52 (1) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Bulte / Talic vs Hoole / Pham -- M25 Darwin QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01BULTALHOOPHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bulte / Talic (`KXITFDOUBLES-26OCT01BULTALHOOPHA-BULTAL`) | 0.43 / 0.49 (505) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hoole / Pham (`KXITFDOUBLES-26OCT01BULTALHOOPHA-HOOPHA`) | 0.49 / 0.55 (32) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## James Connel vs Nicolas Jadoun -- M15 Baku R16

ITF (ITF) · surface ? · scheduled 2026-10-01T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:212171:212250:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| James Connel (`KXITFMATCH-26OCT01CONJAD-CON`) | 0.51 / 0.52 (3595) | 51.5% | 63.2% | 68.5% | 63.3% [60.2%-66.6%] | -- | -- | -- | -- | WATCH | +11.8 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nicolas Jadoun (`KXITFMATCH-26OCT01CONJAD-JAD`) | 0.49 / 0.50 (489) | 49.5% | 36.8% | 31.5% | 36.7% [33.4%-39.8%] | -- | -- | -- | -- | PASS | -12.8 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 868.0, B 2323.0; serve-point win A 65.3%, B 37.4%; Elo A 1362.6, B 1292.5; model uncertainty 0.032
* Form inputs: days since last match A 143, B 136; matches on record A 27, B 99; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Millen Hurrion vs Jordan Hasson -- M15 Baku R16

ITF (ITF) · surface ? · scheduled 2026-10-01T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:200487:209140:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jordan Hasson (`KXITFMATCH-26OCT01HURHAS-HAS`) | 0.14 / 0.16 (2) | 15.0% | 26.7% | 35.3% | 23.3% [20.2%-25.8%] | 16.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +8.3 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Millen Hurrion (`KXITFMATCH-26OCT01HURHAS-HUR`) | 0.84 / 0.86 (350) | 85.0% | 73.3% | 64.7% | 76.7% [74.2%-79.8%] | 83.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.3 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3153.0, B 656.0; serve-point win A 66.5%, B 38.5%; Elo A 1476.4, B 1215.2; model uncertainty 0.0275
* Form inputs: days since last match A 59, B 143; matches on record A 183, B 122; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hayden Jones vs Arjun Mehrotra -- M25 Darwin R16

ITF (ITF) · Hard · scheduled 2026-10-01T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:202323:210436:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hayden Jones (`KXITFMATCH-26OCT01JONMEH-JON`) | 0.77 / 0.79 (25) | 78.0% | 68.4% | 70.1% | 73.6% [72.3%-74.9%] | 78.1% | -- | 78.1% | MODEL_LONE_OUTLIER | PASS | -4.4 pp | NORMAL | STALE | D / POOR | ALL_AGREE | VERIFIED |
| Arjun Mehrotra (`KXITFMATCH-26OCT01JONMEH-MEH`) | 0.22 / 0.23 (25) | 22.5% | 31.6% | 29.9% | 26.4% [25.1%-27.7%] | 21.9% | -- | 21.9% | MODEL_LONE_OUTLIER | PASS | +3.9 pp | NORMAL | STALE | D / POOR | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 1969.0, B 1005.0; serve-point win A 64.5%, B 39.3%; Elo A 1276.0, B 1085.0; model uncertainty 0.0126
* Form inputs: days since last match A 311, B 136; matches on record A 71, B 54; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.004, surface_dev_loose +0.013, surface_dev_tight -0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marcus Walters vs Koray Kirci -- M15 Baku R16

ITF (ITF) · surface ? · scheduled 2026-10-01T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:126971:134405:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Koray Kirci (`KXITFMATCH-26OCT01WALKIR-KIR`) | 0.42 / 0.46 (49) | 44.0% | 45.3% | 34.1% | 46.9% [41.9%-51.5%] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.0 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marcus Walters (`KXITFMATCH-26OCT01WALKIR-WAL`) | 0.55 / 0.58 (4502) | 56.5% | 54.7% | 65.9% | 53.0% [48.5%-58.1%] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.5 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2102.0, B 764.0; serve-point win A 64.5%, B 36.5%; Elo A 1257.0, B 1285.2; model uncertainty 0.0482
* Form inputs: days since last match A 87, B 66; matches on record A 106, B 248; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luis Carlos Alvarez Valdes / Adrian Oetzbach vs Buvaysar Gadamauri / Dimitris Sakellaridis -- ATP Challenger Bari QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T13:40:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01ALVAOETGADSAK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luis Carlos Alvarez Valdes / Adrian Oetzbach (`KXATPCHALLENGERDOUBLES-26OCT01ALVAOETGADSAK-ALVAOET`) | 0.06 / 0.80 (1) | 43.0% | 33.1% | -- | -- [-----] | -- | -- | -- | -- | -- | -9.9 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Buvaysar Gadamauri / Dimitris Sakellaridis (`KXATPCHALLENGERDOUBLES-26OCT01ALVAOETGADSAK-GADSAK`) | 0.06 / 0.94 (110) | 50.0% | 66.9% | -- | -- [-----] | -- | -- | -- | -- | -- | +16.9 pp | HIGH_REVIEW (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERDOUBLES-26OCT01ALVAOETGADSAK-GADSAK  (YES = Buvaysar Gadamauri / Dimitris Sakellaridis)
Model: 67%
Kalshi: 50%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, PLAYER_IDENTITY_RISK, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Warnings: DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Juan Jose Bianchi / Kody Pearson vs Fabrizio Andaloro / Volodoymyr Uzhylovskyi -- ATP Challenger Bari QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T13:40:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01BIAPEAANDUZV:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fabrizio Andaloro / Volodoymyr Uzhylovskyi (`KXATPCHALLENGERDOUBLES-26OCT01BIAPEAANDUZV-ANDUZV`) | 0.17 / 0.94 (110) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Juan Jose Bianchi / Kody Pearson (`KXATPCHALLENGERDOUBLES-26OCT01BIAPEAANDUZV-BIAPEA`) | 0.06 / 0.83 (21) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Lorenzo Giustino vs Matthew William Donald -- ATP Challenger Bari R16

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-01T13:40:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:105841:210054:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthew William Donald (`KXATPCHALLENGERMATCH-26OCT01GIUDON-DON`) | 0.47 / 0.48 (7386) | 47.5% | 35.9% | 47.4% | 39.2% [33.8%-42.7%] | 48.0% | 47.4% | -- | INSUFFICIENT_INPUTS | PASS | -8.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lorenzo Giustino (`KXATPCHALLENGERMATCH-26OCT01GIUDON-GIU`) | 0.52 / 0.53 (3977) | 52.5% | 64.0% | 52.6% | 60.8% [57.3%-66.2%] | 52.0% | 52.1% | 52.1% | MODEL_LONE_OUTLIER | SHADOW_BET | +8.3 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 6491.0, B 2929.0; serve-point win A 61.3%, B 41.5%; Elo A 1636.0, B 1435.7; model uncertainty 0.0445
* Form inputs: days since last match A 37, B 10; matches on record A 1390, B 205; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Ammar Faleh Alhogbani vs Karan Singh -- M15 Sharm ElSheikh R16

ITF (ITF) · Hard · scheduled 2026-10-01T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210000:212249:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ammar Faleh Alhogbani (`KXITFMATCH-26OCT01ALHSIN-ALH`) | 0.17 / 0.30 (16) | 23.5% | 25.9% | 25.8% | 23.8% [22.7%-25.8%] | -- | -- | -- | -- | PASS | +0.3 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Karan Singh (`KXITFMATCH-26OCT01ALHSIN-SIN`) | 0.69 / 0.85 (515) | 77.0% | 74.1% | 74.2% | 76.2% [74.2%-77.3%] | -- | -- | -- | -- | PASS | -0.8 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1476.0, B 3601.0; serve-point win A 60.0%, B 34.8%; Elo A 1182.2, B 1400.5; model uncertainty 0.0155
* Form inputs: days since last match A 129, B 66; matches on record A 42, B 257; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose -0.000, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ivan Biletic vs Charles Bertimon -- M15 Sibenik R16

ITF (ITF) · Clay · scheduled 2026-10-01T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:202293:212919:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charles Bertimon (`KXITFMATCH-26OCT01BILBER-BER`) | 0.58 / 0.59 (1505) | 58.5% | 56.0% | 53.2% | 55.3% [54.7%-56.3%] | 56.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.2 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ivan Biletic (`KXITFMATCH-26OCT01BILBER-BIL`) | 0.39 / 0.40 (41) | 39.5% | 44.0% | 46.8% | 44.7% [43.7%-45.3%] | 43.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.2 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 519.0, B 976.0; serve-point win A 59.3%, B 39.5%; Elo A 1152.5, B 1194.1; model uncertainty 0.008
* Form inputs: days since last match A 129, B 164; matches on record A 14, B 38; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high +0.000, surface_dev_loose -0.011, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matteo Fondriest vs Romain Faucon -- M15 Sharm ElSheikh R16

ITF (ITF) · Hard · scheduled 2026-10-01T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:209940:211667:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Romain Faucon (`KXITFMATCH-26OCT01FONFAU-FAU`) | 0.83 / 0.86 (2386) | 84.5% | 84.8% | 96.4% | 89.7% [83.7%-93.3%] | -- | -- | -- | -- | WATCH | +5.2 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matteo Fondriest (`KXITFMATCH-26OCT01FONFAU-FON`) | 0.14 / 0.17 (3) | 15.5% | 15.2% | 3.6% | 10.3% [6.7%-16.3%] | -- | -- | -- | -- | PASS | -5.2 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1083.0, B 3404.0; serve-point win A 58.5%, B 33.3%; Elo A 1192.1, B 1437.6; model uncertainty 0.0479
* Form inputs: days since last match A 122, B 122; matches on record A 52, B 145; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.007, surface_dev_loose -0.011, surface_dev_tight +0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Niklas Grunewald vs Alec Beckley -- M25 Kigali R16

ITF (ITF) · Clay · scheduled 2026-10-01T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:209278:212741:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alec Beckley (`KXITFMATCH-26OCT01GRUBEC-BEC`) | 0.94 / 0.95 (4941) | 94.5% | 82.2% | 83.7% | 82.4% [80.3%-84.9%] | 92.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.1 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Niklas Grunewald (`KXITFMATCH-26OCT01GRUBEC-GRU`) | 0.05 / 0.07 (4387) | 6.0% | 17.8% | 16.3% | 17.6% [15.1%-19.7%] | 7.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +11.6 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 178.0, B 3000.0; serve-point win A 56.3%, B 36.5%; Elo A 1160.5, B 1426.2; model uncertainty 0.023
* Form inputs: days since last match A 388, B 122; matches on record A 4, B 232; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.025, surface_pool_high +0.021, surface_dev_loose -0.003, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Max Houkes vs Allan Gatoto -- M25 Kigali R16

ITF (ITF) · Clay · scheduled 2026-10-01T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208069:212753:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Allan Gatoto (`KXITFMATCH-26OCT01HOUGAT-GAT`) | 0.05 / 0.07 (271) | 6.0% | 6.9% | 5.6% | 4.6% [4.0%-5.4%] | -- | -- | -- | -- | PASS | -1.4 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Max Houkes (`KXITFMATCH-26OCT01HOUGAT-HOU`) | 0.92 / 0.95 (284) | 93.5% | 93.1% | 94.4% | 95.4% [94.6%-96.0%] | -- | -- | -- | -- | PASS | +1.9 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5070.0, B 647.0; serve-point win A 65.6%, B 45.9%; Elo A 1640.9, B 1099.2; model uncertainty 0.0071
* Form inputs: days since last match A 52, B 136; matches on record A 430, B 15; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.002, surface_dev_tight -0.002
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dev Javia vs Preston Brown -- M25 Kigali R16

ITF (ITF) · Clay · scheduled 2026-10-01T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208186:209956:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Preston Brown (`KXITFMATCH-26OCT01JAVBRO-BRO`) | 0.12 / 0.14 (1145) | 13.0% | 16.9% | 8.8% | 12.0% [9.7%-17.7%] | 14.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.0 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dev Javia (`KXITFMATCH-26OCT01JAVBRO-JAV`) | 0.86 / 0.88 (80) | 87.0% | 83.1% | 91.2% | 88.0% [82.3%-90.3%] | 85.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.0 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2032.0, B 2659.0; serve-point win A 63.6%, B 43.8%; Elo A 1359.7, B 1095.2; model uncertainty 0.04
* Form inputs: days since last match A 136, B 122; matches on record A 147, B 203; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.002, surface_dev_loose +0.017, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Filip Cristian Jianu vs Matei Todoran -- M25 Slobozia R16

ITF (ITF) · Clay · scheduled 2026-10-01T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:202262:212294:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Filip Cristian Jianu (`KXITFMATCH-26OCT01JIATOD-JIA`) | 0.93 / 0.95 (648) | 94.0% | 91.9% | 96.0% | 92.9% [91.6%-95.0%] | 90.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.1 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matei Todoran (`KXITFMATCH-26OCT01JIATOD-TOD`) | 0.05 / 0.06 (780) | 5.5% | 8.1% | 4.0% | 7.1% [5.0%-8.4%] | 9.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.6 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5523.0, B 397.0; serve-point win A 65.3%, B 45.5%; Elo A 1599.3, B 1176.7; model uncertainty 0.0173
* Form inputs: days since last match A 10, B 269; matches on record A 710, B 10; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high -0.000, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Paul Jubb vs Zangar Nurlanuly -- M15 Sharm ElSheikh R16

ITF (ITF) · Hard · scheduled 2026-10-01T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:206703:213930:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Paul Jubb (`KXITFMATCH-26OCT01JUBNUR-JUB`) | 0.92 / 0.93 (805) | 92.5% | 90.7% | 93.3% | 91.2% [90.1%-92.5%] | -- | -- | -- | -- | PASS | -1.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zangar Nurlanuly (`KXITFMATCH-26OCT01JUBNUR-NUR`) | 0.07 / 0.10 (4) | 8.5% | 9.3% | 6.7% | 8.8% [7.5%-9.9%] | -- | -- | -- | -- | PASS | +0.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4251.0, B 453.0; serve-point win A 67.8%, B 42.6%; Elo A 1603.1, B 1207.7; model uncertainty 0.0122
* Form inputs: days since last match A 38, B 52; matches on record A 446, B 11; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.004, surface_dev_loose +0.003, surface_dev_tight -0.002
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Filip Krolo vs Jan Kupcic -- M15 Sibenik R16

ITF (ITF) · Clay · scheduled 2026-10-01T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:209314:212593:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Filip Krolo (`KXITFMATCH-26OCT01KROKUP-KRO`) | 0.33 / 0.35 (36) | 34.0% | 27.3% | 22.5% | 26.2% [22.5%-29.3%] | 35.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jan Kupcic (`KXITFMATCH-26OCT01KROKUP-KUP`) | 0.65 / 0.68 (4179) | 66.5% | 72.7% | 77.5% | 73.8% [70.7%-77.5%] | 64.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 442.0, B 1522.0; serve-point win A 57.6%, B 37.8%; Elo A 1120.9, B 1291.0; model uncertainty 0.0339
* Form inputs: days since last match A 234, B 122; matches on record A 26, B 95; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.013, surface_dev_loose -0.004, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Benjamin Lock vs Toufik Sahtali -- M25 Kigali R16

ITF (ITF) · Clay · scheduled 2026-10-01T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:111761:200086:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Benjamin Lock (`KXITFMATCH-26OCT01LOCSAH-LOC`) | 0.59 / 0.60 (72) | 59.5% | 44.6% | 36.8% | 42.3% [38.7%-57.3%] | 56.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -17.2 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Toufik Sahtali (`KXITFMATCH-26OCT01LOCSAH-SAH`) | 0.39 / 0.40 (807) | 39.5% | 55.4% | 63.2% | 57.7% [42.7%-61.3%] | 43.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +18.2 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4430.0, B 3918.0; serve-point win A 59.4%, B 39.6%; Elo A 1445.6, B 1405.2; model uncertainty 0.0928
* Form inputs: days since last match A 675, B 122; matches on record A 700, B 104; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01LOCSAH-SAH  (YES = Toufik Sahtali)
Model: 58%
Kalshi: 40%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.015, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Noah Lopez vs Daniele Rapagnetta -- M15 Sibenik R16

ITF (ITF) · Clay · scheduled 2026-10-01T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210055:212461:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Noah Lopez (`KXITFMATCH-26OCT01LOPRAP-LOP`) | 0.17 / 0.21 (3869) | 19.0% | 40.4% | 37.5% | 34.5% [32.1%-36.0%] | 21.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +15.5 pp | HIGH_REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daniele Rapagnetta (`KXITFMATCH-26OCT01LOPRAP-RAP`) | 0.79 / 0.82 (194) | 80.5% | 59.6% | 62.5% | 65.5% [64.0%-67.9%] | 78.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.0 pp | HIGH_REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1139.0, B 2233.0; serve-point win A 59.0%, B 39.2%; Elo A 1204.7, B 1331.6; model uncertainty 0.0195
* Form inputs: days since last match A 136, B 94; matches on record A 116, B 86; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01LOPRAP-LOP  (YES = Noah Lopez)
Model: 35%
Kalshi: 19%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_KALSHI_QUOTE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.024, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nikita Mashtakov vs Matthias Ujvary -- M15 Sibenik R16

ITF (ITF) · surface ? · scheduled 2026-10-01T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01MASUJV:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikita Mashtakov (`KXITFMATCH-26OCT01MASUJV-MAS`) | 0.80 / 0.83 (5023) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matthias Ujvary (`KXITFMATCH-26OCT01MASUJV-UJV`) | 0.17 / 0.18 (1205) | 17.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vladislav Melnic vs Radu Mihai Papoe -- M25 Slobozia R16

ITF (ITF) · Clay · scheduled 2026-10-01T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:207331:208457:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vladislav Melnic (`KXITFMATCH-26OCT01MELPAP-MEL`) | 0.04 / 0.05 (976) | 4.5% | 8.6% | 3.6% | 5.8% [4.3%-8.0%] | 7.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.3 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Radu Mihai Papoe (`KXITFMATCH-26OCT01MELPAP-PAP`) | 0.95 / 0.96 (4464) | 95.5% | 91.4% | 96.4% | 94.2% [92.0%-95.7%] | 92.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.3 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1530.0, B 3052.0; serve-point win A 54.6%, B 34.8%; Elo A 1182.1, B 1580.1; model uncertainty 0.0187
* Form inputs: days since last match A 143, B 45; matches on record A 82, B 190; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.003, surface_pool_high +0.006, surface_dev_loose -0.009, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Filip Jeff Planinsek vs Borys Zgola -- M25 Slobozia R16

ITF (ITF) · Clay · scheduled 2026-10-01T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210169:210731:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Filip Jeff Planinsek (`KXITFMATCH-26OCT01PLAZGO-PLA`) | 0.86 / 0.89 (18) | 87.5% | 87.4% | 75.2% | 86.6% [86.0%-87.2%] | 86.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.9 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Borys Zgola (`KXITFMATCH-26OCT01PLAZGO-ZGO`) | 0.11 / 0.13 (991) | 12.0% | 12.6% | 24.8% | 13.4% [12.8%-14.0%] | 13.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.4 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2530.0, B 63.0; serve-point win A 64.3%, B 44.5%; Elo A 1454.7, B 1118.3; model uncertainty 0.0061
* Form inputs: days since last match A 87, B 192; matches on record A 110, B 14; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jan Simonsson vs Michal Krajci -- M15 Sharm ElSheikh R16

ITF (ITF) · Hard · scheduled 2026-10-01T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:211630:211756:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michal Krajci (`KXITFMATCH-26OCT01SIMKRA-KRA`) | 0.78 / 0.83 (155) | 80.5% | 68.2% | 64.9% | 68.2% [64.0%-71.3%] | -- | -- | -- | -- | PASS | -12.3 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jan Simonsson (`KXITFMATCH-26OCT01SIMKRA-SIM`) | 0.18 / 0.21 (3012) | 19.5% | 31.8% | 35.1% | 31.8% [28.7%-36.0%] | -- | -- | -- | -- | PASS | +12.3 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 125.0, B 3305.0; serve-point win A 60.7%, B 35.5%; Elo A 1266.7, B 1399.3; model uncertainty 0.0366
* Form inputs: days since last match A 150, B 122; matches on record A 4, B 123; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.042, surface_pool_high -0.031, surface_dev_loose -0.004, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Petros Tsitsipas vs Sebastian Gima -- M25 Slobozia R16

ITF (ITF) · Clay · scheduled 2026-10-01T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:202065:209142:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sebastian Gima (`KXITFMATCH-26OCT01TSIGIM-GIM`) | 0.70 / 0.74 (4391) | 72.0% | 72.2% | 76.8% | 75.2% [72.3%-77.1%] | 72.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.2 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Petros Tsitsipas (`KXITFMATCH-26OCT01TSIGIM-TSI`) | 0.26 / 0.27 (73) | 26.5% | 27.8% | 23.2% | 24.8% [22.9%-27.7%] | 28.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.7 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2290.0, B 3345.0; serve-point win A 57.6%, B 37.8%; Elo A 1230.7, B 1402.1; model uncertainty 0.0241
* Form inputs: days since last match A 122, B 10; matches on record A 168, B 386; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.003, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hania Abouelsaad vs Esther Adeshina -- W15 Sharm ElSheikh R16

ITF (ITF) · Hard · scheduled 2026-10-01T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220394:221959:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hania Abouelsaad (`KXITFWMATCH-26OCT01ABOADE-ABO`) | 0.12 / 0.16 (51) | 14.0% | 25.4% | 17.7% | 22.2% [18.8%-27.8%] | -- | -- | -- | -- | WATCH | +8.2 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Esther Adeshina (`KXITFWMATCH-26OCT01ABOADE-ADE`) | 0.84 / 0.88 (2700) | 86.0% | 74.7% | 82.3% | 77.8% [72.2%-81.2%] | -- | -- | -- | -- | PASS | -8.2 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 897.0, B 3059.0; serve-point win A 53.2%, B 41.8%; Elo A 1303.1, B 1488.7; model uncertainty 0.0449
* Form inputs: days since last match A 227, B 99; matches on record A 56, B 115; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.008, surface_dev_loose -0.008, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cadence Brace vs Alba Rey Garcia -- W35 Baza R16

ITF (ITF) · Hard · scheduled 2026-10-01T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221454:223335:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cadence Brace (`KXITFWMATCH-26OCT01BRAREY-BRA`) | 0.90 / 0.91 (664) | 90.5% | 73.7% | 76.5% | 77.4% [73.1%-79.7%] | 88.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.1 pp | REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alba Rey Garcia (`KXITFWMATCH-26OCT01BRAREY-REY`) | 0.09 / 0.10 (4200) | 9.5% | 26.3% | 23.4% | 22.6% [20.3%-26.9%] | 11.7% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +13.1 pp | REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2165.0, B 2066.0; serve-point win A 58.1%, B 46.7%; Elo A 1646.6, B 1417.3; model uncertainty 0.033
* Form inputs: days since last match A 15, B 171; matches on record A 222, B 264; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.016, surface_dev_loose +0.012, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Patricia Georgiana Goina vs Astrid Wanja Brune Olsen -- W15 Varna R16

ITF (ITF) · Clay · scheduled 2026-10-01T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:214934:260261:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Astrid Wanja Brune Olsen (`KXITFWMATCH-26OCT01GOIBRU-BRU`) | 0.48 / 0.50 (3722) | 49.0% | 50.0% | 50.5% | 53.8% [51.6%-55.9%] | -- | -- | -- | -- | WATCH | +4.8 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Patricia Georgiana Goina (`KXITFWMATCH-26OCT01GOIBRU-GOI`) | 0.50 / 0.51 (3384) | 50.5% | 50.0% | 49.5% | 46.2% [44.1%-48.4%] | -- | -- | -- | -- | PASS | -4.2 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 925.0, B 1262.0; serve-point win A 54.0%, B 46.0%; Elo A 1341.0, B 1387.2; model uncertainty 0.0214
* Form inputs: days since last match A 157, B 157; matches on record A 67, B 171; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.021, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ksenia Meshcheryakova vs Anna Snigireva -- W15 Sharm ElSheikh R16

ITF (ITF) · Hard · scheduled 2026-10-01T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:222554:263980:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ksenia Meshcheryakova (`KXITFWMATCH-26OCT01MESSNI-MES`) | 0.16 / 0.22 (698) | 19.0% | 6.6% | 18.1% | 8.2% [6.7%-9.2%] | -- | -- | -- | -- | PASS | -10.8 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anna Snigireva (`KXITFWMATCH-26OCT01MESSNI-SNI`) | 0.78 / 0.84 (36) | 81.0% | 93.4% | 81.9% | 91.8% [90.8%-93.3%] | -- | -- | -- | -- | WATCH | +10.8 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 335.0, B 1889.0; serve-point win A 50.0%, B 38.6%; Elo A 980.4, B 1441.4; model uncertainty 0.0126
* Form inputs: days since last match A 157, B 157; matches on record A 75, B 86; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.006, surface_dev_loose -0.004, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Giulia Safina Popa vs Beatris Spasova -- W15 Varna R16

ITF (ITF) · Clay · scheduled 2026-10-01T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221315:267428:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giulia Safina Popa (`KXITFWMATCH-26OCT01POPSPA-POP`) | 0.94 / 0.95 (5485) | 94.5% | 85.4% | 98.4% | 90.5% [85.5%-95.0%] | 90.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.0 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Beatris Spasova (`KXITFWMATCH-26OCT01POPSPA-SPA`) | 0.05 / 0.06 (149) | 5.5% | 14.6% | 1.6% | 9.5% [5.0%-14.5%] | 9.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.0 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1013.0, B 520.0; serve-point win A 58.0%, B 50.0%; Elo A 1546.3, B 1239.2; model uncertainty 0.0476
* Form inputs: days since last match A 367, B 213; matches on record A 38, B 195; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.000, surface_dev_loose +0.017, surface_dev_tight -0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andrea Lola Popovic vs Antonina Sushkova -- W15 Sharm ElSheikh R16

ITF (ITF) · Hard · scheduled 2026-10-01T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:266849:270222:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrea Lola Popovic (`KXITFWMATCH-26OCT01POPSUS-POP`) | 0.23 / 0.28 (13) | 25.5% | 56.4% | 47.9% | 54.3% [53.8%-55.4%] | -- | -- | -- | -- | PASS | +28.8 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Antonina Sushkova (`KXITFWMATCH-26OCT01POPSUS-SUS`) | 0.72 / 0.77 (1533) | 74.5% | 43.6% | 52.1% | 45.7% [44.6%-46.2%] | -- | -- | -- | -- | PASS | -28.8 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 406.0, B 527.0; serve-point win A 56.3%, B 44.9%; Elo A 1333.4, B 1288.5; model uncertainty 0.008
* Form inputs: days since last match A 157, B 227; matches on record A 7, B 11; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01POPSUS-POP  (YES = Andrea Lola Popovic)
Model: 54%
Kalshi: 26%
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
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valentina Ryser vs Daniela Vismane -- W35 Baza R16

ITF (ITF) · Hard · scheduled 2026-10-01T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:215144:220489:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valentina Ryser (`KXITFWMATCH-26OCT01RYSVIS-RYS`) | 0.72 / 0.74 (669) | 73.0% | 66.0% | 83.0% | 69.1% [66.3%-73.0%] | 71.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.9 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daniela Vismane (`KXITFWMATCH-26OCT01RYSVIS-VIS`) | 0.26 / 0.27 (4280) | 26.5% | 34.1% | 17.0% | 30.9% [27.0%-33.7%] | 28.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +4.4 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3017.0, B 336.0; serve-point win A 57.2%, B 45.9%; Elo A 1607.9, B 1493.1; model uncertainty 0.0331
* Form inputs: days since last match A 23, B 157; matches on record A 391, B 354; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.014, surface_dev_loose +0.009, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Darya Velikova vs Felitsata Dorofeeva-Rybas -- W15 Varna R16

ITF (ITF) · Clay · scheduled 2026-10-01T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:223352:267022:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felitsata Dorofeeva-Rybas (`KXITFWMATCH-26OCT01VELDOR-DOR`) | 0.93 / 0.95 (4404) | 94.0% | 83.5% | 94.7% | 86.7% [79.0%-91.8%] | 91.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Darya Velikova (`KXITFWMATCH-26OCT01VELDOR-VEL`) | 0.06 / 0.07 (664) | 6.5% | 16.5% | 5.3% | 13.3% [8.2%-21.0%] | 8.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 683.0, B 923.0; serve-point win A 50.3%, B 42.4%; Elo A 1208.5, B 1460.2; model uncertainty 0.0642
* Form inputs: days since last match A 262, B 304; matches on record A 89, B 19; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.006, surface_pool_high -0.006, surface_dev_loose -0.016, surface_dev_tight +0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Edas Butvilas vs Moez Echargui -- ATP Challenger Porto 2 R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T14:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:121411:210220:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Edas Butvilas (`KXATPCHALLENGERMATCH-26OCT01BUTECH-BUT`) | 0.67 / 0.68 (6034) | 67.5% | 63.3% | 67.2% | 66.2% [65.3%-66.7%] | 66.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Moez Echargui (`KXATPCHALLENGERMATCH-26OCT01BUTECH-ECH`) | 0.32 / 0.33 (3768) | 32.5% | 36.7% | 32.9% | 33.8% [33.3%-34.7%] | 33.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5196.0, B 5190.0; serve-point win A 63.9%, B 38.8%; Elo A 1695.1, B 1598.1; model uncertainty 0.007
* Form inputs: days since last match A 10, B 10; matches on record A 293, B 704; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.000, surface_dev_loose +0.004, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Inaki Montes-de la Torre vs Jacob Fearnley -- ATP Challenger Porto 2 R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T14:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:207985:208540:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jacob Fearnley (`KXATPCHALLENGERMATCH-26OCT01MONFEA-FEA`) | 0.74 / 0.76 (5555) | 75.0% | 59.3% | 45.3% | 51.6% [48.4%-55.7%] | 73.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -23.4 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Inaki Montes-de la Torre (`KXATPCHALLENGERMATCH-26OCT01MONFEA-MON`) | 0.24 / 0.25 (1326) | 24.5% | 40.7% | 54.7% | 48.4% [44.3%-51.6%] | 26.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +23.9 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4378.0, B 5299.0; serve-point win A 61.7%, B 36.5%; Elo A 1650.2, B 1780.7; model uncertainty 0.0365
* Form inputs: days since last match A 17, B 29; matches on record A 245, B 234; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT01MONFEA-MON  (YES = Inaki Montes-de la Torre)
Model: 48%
Kalshi: 24%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.005, surface_dev_loose +0.016, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Felix Balshaw vs Nicolai Budkov Kjaer -- ATP Challenger Mouilleron-Le-Captif R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T14:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:149282:213149:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felix Balshaw (`KXATPCHALLENGERMATCH-26OCT01BALBUD-BAL`) | 0.38 / 0.39 (1681) | 38.5% | 51.9% | 64.7% | 58.0% [53.5%-60.9%] | 39.1% | 40.2% | 39.1% | MODEL_LONE_OUTLIER | WATCH | +19.5 pp | HIGH_REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Nicolai Budkov Kjaer (`KXATPCHALLENGERMATCH-26OCT01BALBUD-BUD`) | 0.61 / 0.62 (4884) | 61.5% | 48.1% | 35.3% | 42.0% [39.1%-46.5%] | 60.9% | 60.9% | 60.9% | MODEL_LONE_OUTLIER | PASS | -19.5 pp | HIGH_REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4079.0, B 4328.0; serve-point win A 62.8%, B 37.6%; Elo A 1604.7, B 1685.3; model uncertainty 0.037
* Form inputs: days since last match A 24, B 10; matches on record A 117, B 192; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT01BALBUD-BAL  (YES = Felix Balshaw)
Model: 58%
Kalshi: 38%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.010, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Liam Branger vs Melih Anavatan -- M15 Monastir R16

ITF (ITF) · Hard · scheduled 2026-10-01T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210605:212903:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Melih Anavatan (`KXITFMATCH-26OCT01BRAANA-ANA`) | 0.32 / 0.33 (4385) | 32.5% | 35.9% | 38.4% | 35.0% [33.1%-36.0%] | 34.3% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +2.5 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Liam Branger (`KXITFMATCH-26OCT01BRAANA-BRA`) | 0.67 / 0.69 (304) | 68.0% | 64.1% | 61.6% | 65.0% [64.0%-66.9%] | 65.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.0 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1201.0, B 1664.0; serve-point win A 64.0%, B 38.8%; Elo A 1301.4, B 1171.4; model uncertainty 0.0145
* Form inputs: days since last match A 171, B 122; matches on record A 32, B 36; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.005, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cook / Leonard Sach vs Domingo / Ege Sik -- M25 Darwin QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01COOLEODOMEGE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cook / Leonard Sach (`KXITFDOUBLES-26OCT01COOLEODOMEGE-COOLEO`) | 0.60 / 0.88 (1) | 74.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Domingo / Ege Sik (`KXITFDOUBLES-26OCT01COOLEODOMEGE-DOMEGE`) | 0.12 / 0.41 (10) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Emilien Demanet vs Mert Naci Turker -- M15 Monastir R16

ITF (ITF) · Hard · scheduled 2026-10-01T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:125833:212598:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emilien Demanet (`KXITFMATCH-26OCT01DEMTUR-DEM`) | 0.81 / 0.84 (9) | 82.5% | 66.8% | 61.2% | 65.0% [63.1%-66.5%] | -- | -- | -- | -- | PASS | -17.5 pp | HIGH_REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mert Naci Turker (`KXITFMATCH-26OCT01DEMTUR-TUR`) | 0.15 / 0.18 (31) | 16.5% | 33.2% | 38.9% | 35.0% [33.6%-36.9%] | -- | -- | -- | -- | WATCH | +18.5 pp | HIGH_REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2543.0, B 2593.0; serve-point win A 64.3%, B 39.1%; Elo A 1429.3, B 1275.1; model uncertainty 0.0167
* Form inputs: days since last match A 59, B 66; matches on record A 142, B 195; data quality A

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01DEMTUR-TUR  (YES = Mert Naci Turker)
Model: 35%
Kalshi: 16%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: STALE_KALSHI_QUOTE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose -0.014, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Remy Dugardin vs Aziz Ouakaa -- M15 Monastir R16

ITF (ITF) · Hard · scheduled 2026-10-01T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:200297:214112:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Remy Dugardin (`KXITFMATCH-26OCT01DUGOUA-DUG`) | 0.38 / 0.41 (43) | 39.5% | 46.1% | 48.5% | 42.9% [39.8%-46.0%] | 40.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.4 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aziz Ouakaa (`KXITFMATCH-26OCT01DUGOUA-OUA`) | 0.60 / 0.62 (67) | 61.0% | 53.9% | 51.5% | 57.1% [54.0%-60.2%] | 59.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.9 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 604.0, B 3759.0; serve-point win A 62.2%, B 37.0%; Elo A 1294.0, B 1355.5; model uncertainty 0.0307
* Form inputs: days since last match A 171, B 52; matches on record A 12, B 450; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.025, surface_dev_loose +0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tuncay Duran vs Pablo Aunion -- M15 Monastir R16

ITF (ITF) · Hard · scheduled 2026-10-01T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210513:213758:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pablo Aunion (`KXITFMATCH-26OCT01DURAUN-AUN`) | 0.16 / 0.17 (3132) | 16.5% | 21.7% | 19.8% | 21.3% [18.1%-24.6%] | 19.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tuncay Duran (`KXITFMATCH-26OCT01DURAUN-DUR`) | 0.83 / 0.84 (5567) | 83.5% | 78.3% | 80.2% | 78.7% [75.4%-81.9%] | 80.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2317.0, B 473.0; serve-point win A 65.7%, B 40.5%; Elo A 1432.2, B 1209.5; model uncertainty 0.0325
* Form inputs: days since last match A 59, B 129; matches on record A 116, B 10; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.023, surface_pool_high +0.021, surface_dev_loose +0.007, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hoeyeraal / Padgham vs Dong / Jones -- M25 Darwin QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01HOEPADDONJON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dong / Jones (`KXITFDOUBLES-26OCT01HOEPADDONJON-DONJON`) | 0.06 / 0.73 (503) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hoeyeraal / Padgham (`KXITFDOUBLES-26OCT01HOEPADDONJON-HOEPAD`) | 0.06 / 0.94 (610) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Ewen Lumsden vs Jack Loge -- M15 Monastir R16

ITF (ITF) · Hard · scheduled 2026-10-01T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:202077:211504:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jack Loge (`KXITFMATCH-26OCT01LUMLOG-LOG`) | 0.75 / 0.79 (6079) | 77.0% | 68.5% | 73.2% | 69.7% [67.3%-71.9%] | 74.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.3 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ewen Lumsden (`KXITFMATCH-26OCT01LUMLOG-LUM`) | 0.22 / 0.25 (35) | 23.5% | 31.5% | 26.8% | 30.3% [28.1%-32.7%] | 25.7% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +6.8 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1340.0, B 3866.0; serve-point win A 60.7%, B 35.5%; Elo A 1322.3, B 1436.0; model uncertainty 0.023
* Form inputs: days since last match A 157, B 59; matches on record A 98, B 191; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.023, surface_pool_high +0.023, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ella Haavisto vs Sophia Biolay -- W15 Monastir R16

ITF (ITF) · Hard · scheduled 2026-10-01T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:216107:221192:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sophia Biolay (`KXITFWMATCH-26OCT01HAABIO-BIO`) | 0.79 / 0.81 (21) | 80.0% | 69.2% | 86.6% | 68.0% [55.3%-78.5%] | 78.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.0 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ella Haavisto (`KXITFWMATCH-26OCT01HAABIO-HAA`) | 0.19 / 0.21 (3124) | 20.0% | 30.8% | 13.4% | 32.0% [21.5%-44.7%] | 21.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +12.0 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1672.0, B 766.0; serve-point win A 53.8%, B 42.4%; Elo A 1414.5, B 1461.2; model uncertainty 0.1159
* Form inputs: days since last match A 213, B 227; matches on record A 139, B 133; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.019, surface_dev_loose -0.014, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valentina Losciale vs Zi Ying Ruan -- W15 Monastir R16

ITF (ITF) · Hard · scheduled 2026-10-01T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:219331:267462:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valentina Losciale (`KXITFWMATCH-26OCT01LOSRUA-LOS`) | 0.54 / 0.57 (3778) | 55.5% | 50.3% | 57.5% | 48.4% [42.5%-52.7%] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.1 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zi Ying Ruan (`KXITFWMATCH-26OCT01LOSRUA-RUA`) | 0.43 / 0.46 (156) | 44.5% | 49.7% | 42.5% | 51.6% [47.3%-57.5%] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.1 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 938.0, B 832.0; serve-point win A 55.7%, B 44.3%; Elo A 1263.0, B 1312.8; model uncertainty 0.0507
* Form inputs: days since last match A 109, B 290; matches on record A 157, B 48; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.011, surface_dev_loose -0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuka Matsumoto vs Jessica Hinojosa Gomez -- W15 Monastir R16

ITF (ITF) · Hard · scheduled 2026-10-01T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:213739:217643:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jessica Hinojosa Gomez (`KXITFWMATCH-26OCT01MATHIN-HIN`) | 0.71 / 0.73 (1177) | 72.0% | 67.9% | 67.6% | 67.6% [66.6%-69.0%] | 72.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.4 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuka Matsumoto (`KXITFWMATCH-26OCT01MATHIN-MAT`) | 0.26 / 0.28 (4215) | 27.0% | 32.1% | 32.4% | 32.4% [30.9%-33.4%] | 28.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.4 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 206.0, B 1620.0; serve-point win A 53.9%, B 42.6%; Elo A 1192.7, B 1322.6; model uncertainty 0.0121
* Form inputs: days since last match A 276, B 11; matches on record A 24, B 175; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sarina Schnyder vs Astrid Cirotte -- W15 Monastir R16

ITF (ITF) · Hard · scheduled 2026-10-01T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:236980:267446:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Astrid Cirotte (`KXITFWMATCH-26OCT01SCHCIR-CIR`) | 0.46 / 0.49 (2) | 47.5% | 63.0% | 48.9% | 62.5% [61.5%-64.5%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +15.0 pp | HIGH_REVIEW (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Sarina Schnyder (`KXITFWMATCH-26OCT01SCHCIR-SCH`) | 0.50 / 0.53 (81) | 51.5% | 37.0% | 51.1% | 37.5% [35.5%-38.5%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -14.0 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 2379.0; serve-point win A 54.4%, B 43.1%; Elo A 1274.0, B 1366.7; model uncertainty 0.0151
* Form inputs: days since last match A 829, B 171; matches on record A 1, B 227; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01SCHCIR-CIR  (YES = Astrid Cirotte)
Model: 63%
Kalshi: 48%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.020, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Benjamin Hassan / Skander Mansouri vs Gianluca Cadenasso / Massimo Giunta -- ATP Challenger Bari QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T14:50:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01HASMANCADGIU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gianluca Cadenasso / Massimo Giunta (`KXATPCHALLENGERDOUBLES-26OCT01HASMANCADGIU-CADGIU`) | 0.12 / 0.54 (21) | 33.0% | 44.0% | -- | -- [-----] | -- | -- | -- | -- | -- | +11.0 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Benjamin Hassan / Skander Mansouri (`KXATPCHALLENGERDOUBLES-26OCT01HASMANCADGIU-HASMAN`) | 0.46 / 0.88 (21) | 67.0% | 56.0% | -- | -- [-----] | -- | -- | -- | -- | -- | -11.0 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Warnings: DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Rodrigo Alujas vs Calvin Hemery -- M25 Kigali R16

ITF (ITF) · Clay · scheduled 2026-10-01T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:123921:212286:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rodrigo Alujas (`KXITFMATCH-26OCT01ALUHEM-ALU`) | 0.08 / 0.11 (75) | 9.5% | 17.0% | 24.8% | 17.0% [12.9%-19.8%] | -- | -- | -- | -- | WATCH | +7.5 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Calvin Hemery (`KXITFMATCH-26OCT01ALUHEM-HEM`) | 0.85 / 0.91 (2029) | 88.0% | 83.0% | 75.2% | 83.0% [80.2%-87.1%] | -- | -- | -- | -- | PASS | -5.0 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2330.0, B 5909.0; serve-point win A 56.2%, B 36.4%; Elo A 1262.2, B 1670.5; model uncertainty 0.0344
* Form inputs: days since last match A 136, B 10; matches on record A 85, B 938; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.007, surface_dev_loose -0.001, surface_dev_tight +0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bessonov / Gretskiy vs Bult / Kypriotis -- M15 Baku QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01BESGREBULKYP:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bessonov / Gretskiy (`KXITFDOUBLES-26OCT01BESGREBULKYP-BESGRE`) | 0.06 / 0.84 (2162) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bult / Kypriotis (`KXITFDOUBLES-26OCT01BESGREBULKYP-BULKYP`) | 0.07 / 0.79 (1501) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Lorenzo Carboni vs Javier Barranco Cosano -- M25 Zaragoza R16

ITF (ITF) · Clay · scheduled 2026-10-01T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:200266:212077:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Javier Barranco Cosano (`KXITFMATCH-26OCT01CARBAR-BAR`) | 0.59 / 0.62 (38) | 60.5% | 61.5% | 60.5% | 62.0% [61.5%-63.0%] | 60.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.5 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lorenzo Carboni (`KXITFMATCH-26OCT01CARBAR-CAR`) | 0.38 / 0.39 (40) | 38.5% | 38.5% | 39.5% | 38.0% [37.0%-38.5%] | 39.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.5 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3666.0, B 3597.0; serve-point win A 58.8%, B 39.0%; Elo A 1505.1, B 1619.1; model uncertainty 0.0077
* Form inputs: days since last match A 31, B 45; matches on record A 186, B 666; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Michiel De Krom vs Sander Jong -- M25 Zaragoza R16

ITF (ITF) · Clay · scheduled 2026-10-01T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:202148:210093:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michiel De Krom (`KXITFMATCH-26OCT01DEKJON-DEK`) | 0.13 / 0.16 (5279) | 14.5% | 33.0% | 22.2% | 28.7% [25.4%-35.0%] | 17.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +14.2 pp | REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sander Jong (`KXITFMATCH-26OCT01DEKJON-JON`) | 0.84 / 0.87 (5920) | 85.5% | 67.0% | 77.8% | 71.3% [65.0%-74.6%] | 82.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -14.2 pp | REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3414.0, B 1938.0; serve-point win A 58.2%, B 38.4%; Elo A 1401.8, B 1478.4; model uncertainty 0.0479
* Form inputs: days since last match A 122, B 116; matches on record A 322, B 134; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.009, surface_dev_loose -0.009, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Corentin Denolly vs Manuel Plunger -- M25 Kigali R16

ITF (ITF) · Clay · scheduled 2026-10-01T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:144656:211708:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Corentin Denolly (`KXITFMATCH-26OCT01DENPLU-DEN`) | 0.67 / 0.70 (102) | 68.5% | 85.4% | 90.5% | 86.5% [85.2%-88.2%] | 67.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +18.0 pp | HIGH_REVIEW | STALE | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Manuel Plunger (`KXITFMATCH-26OCT01DENPLU-PLU`) | 0.31 / 0.34 (68) | 32.5% | 14.6% | 9.5% | 13.5% [11.8%-14.8%] | 33.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -19.0 pp | HIGH_REVIEW | STALE | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4015.0, B 330.0; serve-point win A 64.0%, B 44.2%; Elo A 1540.6, B 1234.2; model uncertainty 0.0147
* Form inputs: days since last match A 136, B 129; matches on record A 715, B 42; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01DENPLU-DEN  (YES = Corentin Denolly)
Model: 86%
Kalshi: 68%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.009, surface_dev_loose +0.006, surface_dev_tight -0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## TIM Handel vs Pedro Vives Marcos -- M25 Zaragoza R16

ITF (ITF) · Clay · scheduled 2026-10-01T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:134389:206325:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TIM Handel (`KXITFMATCH-26OCT01HANVIV-HAN`) | 0.23 / 0.26 (62) | 24.5% | 26.5% | 21.4% | 25.4% [23.0%-28.4%] | 25.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.9 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pedro Vives Marcos (`KXITFMATCH-26OCT01HANVIV-VIV`) | 0.75 / 0.78 (994) | 76.5% | 73.5% | 78.6% | 74.6% [71.6%-77.0%] | 74.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.9 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2906.0, B 1642.0; serve-point win A 57.5%, B 37.7%; Elo A 1421.8, B 1566.4; model uncertainty 0.0271
* Form inputs: days since last match A 122, B 31; matches on record A 313, B 212; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.012, surface_pool_high +0.013, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hrazdil / Lanik vs Harsh / Singh -- M15 Sharm ElSheikh QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01HRALANHARSIN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Harsh / Singh (`KXITFDOUBLES-26OCT01HRALANHARSIN-HARSIN`) | 0.24 / 0.67 (1) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hrazdil / Lanik (`KXITFDOUBLES-26OCT01HRALANHARSIN-HRALAN`) | 0.07 / 0.76 (583) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Krivoshchekov / Ponomarev vs Delicata / Stamatopoulos -- M15 Baku QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01KRIPONDELSTA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Delicata / Stamatopoulos (`KXITFDOUBLES-26OCT01KRIPONDELSTA-DELSTA`) | 0.06 / 0.94 (2110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Krivoshchekov / Ponomarev (`KXITFDOUBLES-26OCT01KRIPONDELSTA-KRIPON`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Maximilian Neuchrist / David Poljak vs Finn Bass / Scott Duncan -- ATP Challenger Mouilleron-Le-Captif QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01NEUPOLBASDUN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Finn Bass / Scott Duncan (`KXATPCHALLENGERDOUBLES-26OCT01NEUPOLBASDUN-BASDUN`) | 0.34 / 0.43 (20) | 38.5% | 11.7% | -- | -- [-----] | -- | -- | -- | -- | -- | -26.8 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Maximilian Neuchrist / David Poljak (`KXATPCHALLENGERDOUBLES-26OCT01NEUPOLBASDUN-NEUPOL`) | 0.57 / 0.66 (500) | 61.5% | 88.3% | -- | -- [-----] | -- | -- | -- | -- | -- | +26.8 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERDOUBLES-26OCT01NEUPOLBASDUN-NEUPOL  (YES = Maximilian Neuchrist / David Poljak)
Model: 88%
Kalshi: 62%
Gap: +27 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, PLAYER_IDENTITY_RISK, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Warnings: DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Mili Poljicak vs Henrique Rocha -- ATP Challenger Porto 2 R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:209890:210012:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mili Poljicak (`KXATPCHALLENGERMATCH-26OCT01POLROC-POL`) | 0.22 / 0.23 (3471) | 22.5% | 36.2% | 43.0% | 38.1% [33.8%-40.0%] | 24.7% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +15.6 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Henrique Rocha (`KXATPCHALLENGERMATCH-26OCT01POLROC-ROC`) | 0.77 / 0.78 (6040) | 77.5% | 63.8% | 57.0% | 61.9% [60.0%-66.2%] | 75.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.6 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3989.0, B 5037.0; serve-point win A 61.2%, B 36.0%; Elo A 1548.4, B 1721.6; model uncertainty 0.0311
* Form inputs: days since last match A 24, B 24; matches on record A 306, B 353; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT01POLROC-POL  (YES = Mili Poljicak)
Model: 38%
Kalshi: 22%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose -0.004, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Marlon Vankan vs Yshai Oliel -- M25 Kigali R16

ITF (ITF) · Clay · scheduled 2026-10-01T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:200075:207535:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yshai Oliel (`KXITFMATCH-26OCT01VANOLI-OLI`) | 0.35 / 0.47 (505) | 41.0% | 37.1% | 15.3% | 39.2% [27.1%-61.2%] | -- | -- | -- | -- | PASS | -1.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marlon Vankan (`KXITFMATCH-26OCT01VANOLI-VAN`) | 0.38 / 0.63 (506) | 50.5% | 62.9% | 84.7% | 60.8% [38.8%-72.9%] | -- | -- | -- | -- | PASS | +10.2 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2602.0, B 932.0; serve-point win A 61.2%, B 41.4%; Elo A 1381.3, B 1440.0; model uncertainty 0.1707
* Form inputs: days since last match A 129, B 325; matches on record A 230, B 457; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.030, surface_pool_high +0.030, surface_dev_loose +0.010, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Caheer Warik vs Florent Bax -- M25 Kigali R16

ITF (ITF) · Clay · scheduled 2026-10-01T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:202147:212890:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Florent Bax (`KXITFMATCH-26OCT01WARBAX-BAX`) | 0.95 / 0.97 (4636) | 96.0% | 92.9% | 97.2% | 94.2% [93.2%-95.6%] | 95.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Caheer Warik (`KXITFMATCH-26OCT01WARBAX-WAR`) | 0.03 / 0.05 (1568) | 4.0% | 7.1% | 2.8% | 5.8% [4.4%-6.8%] | 4.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 446.0, B 4639.0; serve-point win A 54.2%, B 34.4%; Elo A 1103.3, B 1549.8; model uncertainty 0.0123
* Form inputs: days since last match A 129, B 17; matches on record A 12, B 354; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose -0.004, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elkady / Darta Feldmane vs Ibrahim / Pieroni -- W15 Sharm ElSheikh QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01ELKDARIBRPIE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elkady / Darta Feldmane (`KXITFWDOUBLES-26OCT01ELKDARIBRPIE-ELKDAR`) | 0.52 / 0.88 (2) | 70.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ibrahim / Pieroni (`KXITFWDOUBLES-26OCT01ELKDARIBRPIE-IBRPIE`) | 0.11 / 0.44 (103) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Maddalena Giordano vs Ksenia Smirnova -- W15 Sharm ElSheikh R16

ITF (ITF) · Hard · scheduled 2026-10-01T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220642:269968:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maddalena Giordano (`KXITFWMATCH-26OCT01GIOSMI-GIO`) | 0.12 / 0.14 (3933) | 13.0% | 13.6% | 5.1% | 11.7% [8.0%-15.5%] | -- | -- | -- | -- | PASS | -1.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ksenia Smirnova (`KXITFWMATCH-26OCT01GIOSMI-SMI`) | 0.85 / 0.86 (2) | 85.5% | 86.4% | 95.0% | 88.3% [84.5%-92.0%] | -- | -- | -- | -- | PASS | +2.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1760.0, B 692.0; serve-point win A 51.5%, B 40.2%; Elo A 1179.5, B 1461.8; model uncertainty 0.0373
* Form inputs: days since last match A 157, B 164; matches on record A 144, B 17; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.003, surface_pool_high +0.003, surface_dev_loose -0.010, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Heerae Im vs Isis Louise Van den Broek -- W35 Reims R16

ITF (ITF) · Hard · scheduled 2026-10-01T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:260091:264227:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Heerae Im (`KXITFWMATCH-26OCT01IMXVAN-IMX`) | 0.15 / 0.16 (5636) | 15.5% | 25.9% | 35.8% | 23.8% [21.0%-26.4%] | 16.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +8.3 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Isis Louise Van den Broek (`KXITFWMATCH-26OCT01IMXVAN-VAN`) | 0.84 / 0.87 (310) | 85.5% | 74.1% | 64.2% | 76.2% [73.6%-79.0%] | 83.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.3 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 568.0, B 1856.0; serve-point win A 53.2%, B 41.9%; Elo A 1336.6, B 1579.5; model uncertainty 0.0267
* Form inputs: days since last match A 157, B 157; matches on record A 61, B 103; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose -0.000, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elena Malygina vs Katie Swan -- W75 Quinta do Lago R16

ITF (ITF) · Hard · scheduled 2026-10-01T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:215042:216116:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elena Malygina (`KXITFWMATCH-26OCT01MALSWA-MAL`) | 0.24 / 0.26 (4812) | 25.0% | 36.7% | 42.1% | 39.6% [38.5%-41.1%] | 27.6% | -- | 27.6% | KALSHI_LONE_OUTLIER | WATCH | +14.6 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Katie Swan (`KXITFWMATCH-26OCT01MALSWA-SWA`) | 0.74 / 0.75 (414) | 74.5% | 63.3% | 57.9% | 60.4% [58.9%-61.5%] | 72.4% | -- | 72.4% | KALSHI_LONE_OUTLIER | PASS | -14.1 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2298.0, B 2343.0; serve-point win A 54.4%, B 43.0%; Elo A 1620.5, B 1720.0; model uncertainty 0.0129
* Form inputs: days since last match A 6, B 6; matches on record A 440, B 385; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.000, surface_dev_loose +0.015, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sada Nahimana vs Alina Nesmianovych -- W35 Reims R16

ITF (ITF) · Hard · scheduled 2026-10-01T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:216367:232891:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sada Nahimana (`KXITFWMATCH-26OCT01NAHNES-NAH`) | 0.87 / 0.89 (4081) | 88.0% | 90.2% | 44.2% | 90.2% [88.3%-92.0%] | 84.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.2 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alina Nesmianovych (`KXITFWMATCH-26OCT01NAHNES-NES`) | 0.11 / 0.12 (4242) | 11.5% | 9.8% | 55.8% | 9.8% [8.0%-11.7%] | 15.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.7 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2636.0, B 0.0; serve-point win A 60.6%, B 49.2%; Elo A 1540.8, B 1155.3; model uncertainty 0.0186
* Form inputs: days since last match A 134, B 696; matches on record A 369, B 19; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.017, surface_pool_high -0.019, surface_dev_loose -0.001, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lea Nilsson vs Susan Bandecchi -- W75 Quinta do Lago R16

ITF (ITF) · Hard · scheduled 2026-10-01T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:214826:263909:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Susan Bandecchi (`KXITFWMATCH-26OCT01NILBAN-BAN`) | 0.68 / 0.69 (2003) | 68.5% | 68.9% | 59.5% | 72.5% [64.0%-83.7%] | 65.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +4.0 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lea Nilsson (`KXITFWMATCH-26OCT01NILBAN-NIL`) | 0.31 / 0.32 (4100) | 31.5% | 31.1% | 40.5% | 27.5% [16.3%-36.0%] | 34.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.0 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1096.0, B 3884.0; serve-point win A 53.8%, B 42.4%; Elo A 1469.6, B 1714.3; model uncertainty 0.0985
* Form inputs: days since last match A 87, B 10; matches on record A 33, B 523; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.043, surface_pool_high +0.056, surface_dev_loose +0.000, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Katherine Sebov vs Margaux Rouvroy -- W75 Quinta do Lago R16

ITF (ITF) · Hard · scheduled 2026-10-01T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:214684:221191:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Margaux Rouvroy (`KXITFWMATCH-26OCT01SEBROU-ROU`) | 0.41 / 0.44 (3158) | 42.5% | 42.0% | 44.2% | 43.2% [41.6%-44.7%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.7 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Katherine Sebov (`KXITFWMATCH-26OCT01SEBROU-SEB`) | 0.56 / 0.58 (2) | 57.0% | 58.0% | 55.8% | 56.8% [55.3%-58.4%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3407.0, B 3212.0; serve-point win A 56.5%, B 45.1%; Elo A 1691.9, B 1624.5; model uncertainty 0.0156
* Form inputs: days since last match A 16, B 18; matches on record A 461, B 337; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.016, surface_dev_loose -0.005, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lian Tran vs Diana Martynov -- W35 Reims R16

ITF (ITF) · Hard · scheduled 2026-10-01T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220560:221157:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diana Martynov (`KXITFWMATCH-26OCT01TRAMAR-MAR`) | 0.60 / 0.63 (3969) | 61.5% | 52.3% | 72.3% | 56.9% [47.3%-63.1%] | 61.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.6 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lian Tran (`KXITFWMATCH-26OCT01TRAMAR-TRA`) | 0.37 / 0.40 (163) | 38.5% | 47.7% | 27.7% | 43.1% [36.9%-52.7%] | 38.5% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +4.6 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1204.0, B 1861.0; serve-point win A 55.5%, B 44.1%; Elo A 1505.4, B 1461.8; model uncertainty 0.0791
* Form inputs: days since last match A 157, B 25; matches on record A 307, B 331; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.011, surface_dev_loose -0.031, surface_dev_tight +0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniel Cukierman / Fernando Romboli vs Nicolas Barrientos / Szymon Walkow -- ATP Challenger Porto 2 QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T15:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01CUKROMBARWAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Barrientos / Szymon Walkow (`KXATPCHALLENGERDOUBLES-26OCT01CUKROMBARWAL-BARWAL`) | 0.18 / 0.94 (110) | 56.0% | 49.6% | -- | -- [-----] | -- | -- | -- | -- | -- | -6.4 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Daniel Cukierman / Fernando Romboli (`KXATPCHALLENGERDOUBLES-26OCT01CUKROMBARWAL-CUKROM`) | 0.06 / 0.82 (21) | 44.0% | 50.4% | -- | -- [-----] | -- | -- | -- | -- | -- | +6.4 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Warnings: DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## August Holmgren vs Andrea Guerrieri -- ATP Challenger Porto 2 R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T15:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:200416:200462:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrea Guerrieri (`KXATPCHALLENGERMATCH-26OCT01HOLGUE-GUE`) | 0.59 / 0.60 (2248) | 59.5% | 58.5% | 63.1% | 61.2% [59.3%-62.6%] | 59.2% | 61.2% | 61.2% | MARKETS_AGREE | PASS | +1.7 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| August Holmgren (`KXATPCHALLENGERMATCH-26OCT01HOLGUE-HOL`) | 0.40 / 0.41 (12012) | 40.5% | 41.5% | 36.9% | 38.8% [37.4%-40.7%] | 40.8% | 39.4% | 39.4% | MARKETS_AGREE | PASS | -1.7 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5043.0, B 4580.0; serve-point win A 61.8%, B 36.6%; Elo A 1614.1, B 1659.3; model uncertainty 0.0164
* Form inputs: days since last match A 24, B 10; matches on record A 350, B 417; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose -0.009, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Alessandro Battiston vs Martin VAN DER MEERSCHEN -- M15 Sibenik R16

ITF (ITF) · Clay · scheduled 2026-10-01T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:207592:213557:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alessandro Battiston (`KXITFMATCH-26OCT01BATVAN-BAT`) | 0.19 / 0.20 (5010) | 19.5% | 29.0% | 21.9% | 25.6% [22.3%-27.8%] | 24.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.1 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Martin VAN DER MEERSCHEN (`KXITFMATCH-26OCT01BATVAN-VAN`) | 0.79 / 0.82 (3897) | 80.5% | 71.0% | 78.1% | 74.4% [72.2%-77.7%] | 76.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.1 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 961.0, B 2224.0; serve-point win A 57.8%, B 38.0%; Elo A 1194.2, B 1362.4; model uncertainty 0.0274
* Form inputs: days since last match A 129, B 136; matches on record A 29, B 107; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high -0.000, surface_dev_loose -0.013, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maxime Chazal vs Kris van Wyk -- M15 Monastir R16

ITF (ITF) · Hard · scheduled 2026-10-01T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:106172:144748:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maxime Chazal (`KXITFMATCH-26OCT01CHAVAN-CHA`) | 0.88 / 0.90 (6078) | 89.0% | 71.3% | 91.0% | 83.8% [78.1%-87.1%] | 86.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.2 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kris van Wyk (`KXITFMATCH-26OCT01CHAVAN-VAN`) | 0.10 / 0.12 (391) | 11.0% | 28.7% | 9.0% | 16.2% [12.9%-21.9%] | 13.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.2 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3315.0, B 2787.0; serve-point win A 64.8%, B 39.6%; Elo A 1400.4, B 1308.5; model uncertainty 0.0452
* Form inputs: days since last match A 10, B 122; matches on record A 869, B 330; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.024, surface_dev_loose +0.021, surface_dev_tight -0.024
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carles Hernandez vs Samir Hamza Reguig -- M15 Monastir R16

ITF (ITF) · Hard · scheduled 2026-10-01T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208264:209360:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Samir Hamza Reguig (`KXITFMATCH-26OCT01HERHAM-HAM`) | 0.37 / 0.40 (43) | 38.5% | 56.8% | 64.9% | 61.9% [57.3%-63.4%] | 39.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +23.4 pp | HIGH_REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carles Hernandez (`KXITFMATCH-26OCT01HERHAM-HER`) | 0.60 / 0.63 (68) | 61.5% | 43.2% | 35.1% | 38.1% [36.6%-42.7%] | 60.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -23.4 pp | HIGH_REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2103.0, B 2818.0; serve-point win A 61.9%, B 36.7%; Elo A 1251.7, B 1301.2; model uncertainty 0.0306
* Form inputs: days since last match A 136, B 24; matches on record A 85, B 216; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01HERHAM-HAM  (YES = Samir Hamza Reguig)
Model: 62%
Kalshi: 38%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_KALSHI_QUOTE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high +0.000, surface_dev_loose -0.010, surface_dev_tight +0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mak Mikovic vs Piotr Galus -- M15 Sibenik R16

ITF (ITF) · Clay · scheduled 2026-10-01T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:206893:212951:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Piotr Galus (`KXITFMATCH-26OCT01MIKGAL-GAL`) | 0.42 / 0.43 (43) | 42.5% | 48.6% | 50.5% | 48.9% [47.9%-49.5%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.4 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mak Mikovic (`KXITFMATCH-26OCT01MIKGAL-MIK`) | 0.56 / 0.59 (82) | 57.5% | 51.4% | 49.5% | 51.1% [50.5%-52.1%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.4 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 608.0, B 305.0; serve-point win A 60.0%, B 40.2%; Elo A 1195.3, B 1185.6; model uncertainty 0.008
* Form inputs: days since last match A 122, B 122; matches on record A 16, B 19; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jakub Nicod vs Samuele Seghetti -- M15 Sibenik R16

ITF (ITF) · Clay · scheduled 2026-10-01T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210556:213064:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jakub Nicod (`KXITFMATCH-26OCT01NICSEG-NIC`) | 0.80 / 0.83 (10858) | 81.5% | 83.4% | 89.0% | 88.2% [86.5%-89.7%] | 78.6% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +6.7 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Samuele Seghetti (`KXITFMATCH-26OCT01NICSEG-SEG`) | 0.17 / 0.19 (5) | 18.0% | 16.6% | 11.0% | 11.8% [10.3%-13.5%] | 21.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.2 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1919.0, B 1318.0; serve-point win A 63.7%, B 43.9%; Elo A 1548.3, B 1204.3; model uncertainty 0.0157
* Form inputs: days since last match A 122, B 157; matches on record A 152, B 39; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.016, surface_dev_loose +0.011, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lars Goran Verwerft vs Arjun Rathi -- M15 Monastir R16

ITF (ITF) · Hard · scheduled 2026-10-01T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:213121:213889:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arjun Rathi (`KXITFMATCH-26OCT01VERRAT-RAT`) | 0.35 / 0.38 (40) | 36.5% | 40.2% | 16.2% | 35.6% [27.2%-46.4%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.9 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lars Goran Verwerft (`KXITFMATCH-26OCT01VERRAT-VER`) | 0.62 / 0.65 (26) | 63.5% | 59.8% | 83.8% | 64.4% [53.6%-72.8%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.9 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 832.0, B 1129.0; serve-point win A 63.6%, B 38.4%; Elo A 1225.4, B 1220.6; model uncertainty 0.0959
* Form inputs: days since last match A 129, B 136; matches on record A 20, B 19; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.024, surface_dev_tight -0.025
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jeffrey Von Der Schulenburg vs Michel Hopp -- M15 Sibenik R16

ITF (ITF) · Clay · scheduled 2026-10-01T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:209882:210424:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michel Hopp (`KXITFMATCH-26OCT01VONHOP-HOP`) | 0.32 / 0.33 (28) | 32.5% | 48.1% | 50.0% | 46.3% [45.3%-47.9%] | 30.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.8 pp | REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jeffrey Von Der Schulenburg (`KXITFMATCH-26OCT01VONHOP-VON`) | 0.68 / 0.69 (2) | 68.5% | 51.9% | 50.0% | 53.7% [52.1%-54.7%] | 69.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -14.8 pp | REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1301.0, B 2440.0; serve-point win A 60.1%, B 40.3%; Elo A 1370.3, B 1330.2; model uncertainty 0.013
* Form inputs: days since last match A 45, B 122; matches on record A 102, B 88; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bosman / Maloney vs Blazkova / Paola Marina Pieragostini -- W15 Monastir QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01BOSMALBLAPAO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Blazkova / Paola Marina Pieragostini (`KXITFWDOUBLES-26OCT01BOSMALBLAPAO-BLAPAO`) | 0.07 / 0.92 (100) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bosman / Maloney (`KXITFWDOUBLES-26OCT01BOSMALBLAPAO-BOSMAL`) | 0.06 / 0.94 (210) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Laura Hietaranta vs Amandine Hesse -- W35 Baza R16

ITF (ITF) · Hard · scheduled 2026-10-01T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:203281:222397:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amandine Hesse (`KXITFWMATCH-26OCT01HIEHES-HES`) | 0.72 / 0.74 (1670) | 73.0% | 51.9% | 50.5% | 56.4% [53.2%-60.0%] | 71.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -16.6 pp | HIGH_REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Laura Hietaranta (`KXITFWMATCH-26OCT01HIEHES-HIE`) | 0.25 / 0.27 (923) | 26.0% | 48.1% | 49.5% | 43.6% [40.0%-46.8%] | 28.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +17.6 pp | HIGH_REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2514.0, B 2021.0; serve-point win A 55.5%, B 44.1%; Elo A 1472.0, B 1578.2; model uncertainty 0.034
* Form inputs: days since last match A 164, B 81; matches on record A 244, B 777; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01HIEHES-HIE  (YES = Laura Hietaranta)
Model: 44%
Kalshi: 26%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_KALSHI_QUOTE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.005, surface_dev_loose -0.036, surface_dev_tight +0.032
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matilde Mariani vs Polina Berezina -- W15 Monastir R16

ITF (ITF) · Hard · scheduled 2026-10-01T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220343:269754:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Berezina (`KXITFWMATCH-26OCT01MARBER-BER`) | 0.36 / 0.39 (78) | 37.5% | 51.1% | 53.7% | 51.1% [47.9%-55.3%] | 37.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.6 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matilde Mariani (`KXITFWMATCH-26OCT01MARBER-MAR`) | 0.58 / 0.59 (2) | 58.5% | 48.9% | 46.3% | 48.9% [44.7%-52.1%] | 62.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.6 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 616.0, B 71.0; serve-point win A 55.6%, B 44.2%; Elo A 1368.6, B 1376.6; model uncertainty 0.0374
* Form inputs: days since last match A 171, B 220; matches on record A 146, B 8; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.032, surface_pool_high -0.043, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lan Mi vs Ophelie Boullay -- W15 Monastir R16

ITF (ITF) · Hard · scheduled 2026-10-01T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:260141:267400:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ophelie Boullay (`KXITFWMATCH-26OCT01MIXBOU-BOU`) | 0.26 / 0.27 (3124) | 26.5% | 57.1% | 60.6% | 58.0% [55.4%-60.6%] | 25.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +31.5 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lan Mi (`KXITFWMATCH-26OCT01MIXBOU-MIX`) | 0.73 / 0.75 (754) | 74.0% | 42.9% | 39.4% | 42.0% [39.4%-44.6%] | 74.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -32.0 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2699.0, B 774.0; serve-point win A 55.0%, B 43.6%; Elo A 1444.9, B 1486.1; model uncertainty 0.0263
* Form inputs: days since last match A 157, B 339; matches on record A 89, B 16; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01MIXBOU-BOU  (YES = Ophelie Boullay)
Model: 58%
Kalshi: 26%
Gap: +31 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.011, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kristina Novak vs Nahia Berecoechea -- W35 Baza R16

ITF (ITF) · Hard · scheduled 2026-10-01T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:216038:222171:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nahia Berecoechea (`KXITFWMATCH-26OCT01NOVBER-BER`) | 0.79 / 0.82 (350) | 80.5% | 77.1% | 85.8% | 81.5% [78.1%-84.2%] | 79.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.0 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kristina Novak (`KXITFWMATCH-26OCT01NOVBER-NOV`) | 0.18 / 0.21 (3171) | 19.5% | 22.9% | 14.2% | 18.5% [15.8%-21.9%] | 20.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.0 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 994.0, B 1894.0; serve-point win A 52.9%, B 41.5%; Elo A 1328.8, B 1547.8; model uncertainty 0.0306
* Form inputs: days since last match A 16, B 171; matches on record A 140, B 250; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.007, surface_dev_loose -0.007, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kseniia Ruchkina vs Ekaterina Dotsenko -- W15 Monastir R16

ITF (ITF) · surface ? · scheduled 2026-10-01T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01RUCDOT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Dotsenko (`KXITFWMATCH-26OCT01RUCDOT-DOT`) | 0.57 / 0.63 (45) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kseniia Ruchkina (`KXITFWMATCH-26OCT01RUCDOT-RUC`) | 0.37 / 0.43 (510) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marta Soriano Santiago vs nour sahnoun -- W15 Monastir R16

ITF (ITF) · Hard · scheduled 2026-10-01T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:259105:270375:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| nour sahnoun (`KXITFWMATCH-26OCT01SORSAH-SAH`) | 0.05 / 0.07 (70) | 6.0% | 31.6% | 28.2% | 31.5% [29.6%-32.0%] | 5.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +25.5 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marta Soriano Santiago (`KXITFWMATCH-26OCT01SORSAH-SOR`) | 0.94 / 0.95 (4439) | 94.5% | 68.4% | 71.8% | 68.5% [68.0%-70.4%] | 94.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -26.0 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1358.0, B 185.0; serve-point win A 57.5%, B 46.1%; Elo A 1390.2, B 1255.9; model uncertainty 0.012
* Form inputs: days since last match A 157, B 220; matches on record A 98, B 4; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01SORSAH-SAH  (YES = nour sahnoun)
Model: 31%
Kalshi: 6%
Gap: +25 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.009, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Adrian Boitan / Andrei Golescu vs Chetverikov / Khorozov -- M25 Slobozia QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01ADRANDCHEKHO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Boitan / Andrei Golescu (`KXITFDOUBLES-26OCT01ADRANDCHEKHO-ADRAND`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Chetverikov / Khorozov (`KXITFDOUBLES-26OCT01ADRANDCHEKHO-CHEKHO`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Ehab / El Feky vs Castagnola / Orlando Fellin -- M15 Sharm ElSheikh QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01EHAELFCASORL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Castagnola / Orlando Fellin (`KXITFDOUBLES-26OCT01EHAELFCASORL-CASORL`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ehab / El Feky (`KXITFDOUBLES-26OCT01EHAELFCASORL-EHAELF`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Howse / Pierleoni vs Lorusso / Senn -- M15 Sharm ElSheikh QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01HOWPIELORSEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Howse / Pierleoni (`KXITFDOUBLES-26OCT01HOWPIELORSEN-HOWPIE`) | 0.35 / 0.59 (500) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lorusso / Senn (`KXITFDOUBLES-26OCT01HOWPIELORSEN-LORSEN`) | 0.40 / 0.63 (500) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Ibrahim / Waldner vs Arzhankin / Kunitsyn -- M15 Sharm ElSheikh QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01IBRWALARZKUN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arzhankin / Kunitsyn (`KXITFDOUBLES-26OCT01IBRWALARZKUN-ARZKUN`) | 0.06 / 0.55 (2) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ibrahim / Waldner (`KXITFDOUBLES-26OCT01IBRWALARZKUN-IBRWAL`) | 0.08 / 0.58 (1) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Opitz / Wessels vs Broska / Schaefer -- M25 Slobozia QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01OPIWESBROSCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Broska / Schaefer (`KXITFDOUBLES-26OCT01OPIWESBROSCH-BROSCH`) | 0.07 / 0.68 (1) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Opitz / Wessels (`KXITFDOUBLES-26OCT01OPIWESBROSCH-OPIWES`) | 0.08 / 0.93 (1558) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tessa Johanna Brockmann vs Marine Szostak -- W35 Reims R16

ITF (ITF) · Hard · scheduled 2026-10-01T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:222347:260598:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tessa Johanna Brockmann (`KXITFWMATCH-26OCT01BROSZO-BRO`) | 0.78 / 0.81 (4551) | 79.5% | 66.0% | 59.5% | 64.1% [59.0%-74.4%] | 78.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.4 pp | HIGH_REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marine Szostak (`KXITFWMATCH-26OCT01BROSZO-SZO`) | 0.19 / 0.22 (3153) | 20.5% | 34.0% | 40.5% | 35.9% [25.6%-41.0%] | 21.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +15.4 pp | HIGH_REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3426.0, B 1767.0; serve-point win A 57.2%, B 45.9%; Elo A 1593.9, B 1449.7; model uncertainty 0.0769
* Form inputs: days since last match A 22, B 157; matches on record A 171, B 238; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01BROSZO-SZO  (YES = Marine Szostak)
Model: 36%
Kalshi: 20%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_KALSHI_QUOTE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.049, surface_pool_high -0.051, surface_dev_loose -0.010, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valeria Garnevska vs Adriana Tkachenko -- W15 Varna R16

ITF (ITF) · Clay · scheduled 2026-10-01T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:263751:270109:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valeria Garnevska (`KXITFWMATCH-26OCT01GARTKA-GAR`) | 0.77 / 0.79 (15) | 78.0% | 42.0% | 22.2% | 39.4% [37.9%-41.5%] | 76.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -38.6 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Adriana Tkachenko (`KXITFWMATCH-26OCT01GARTKA-TKA`) | 0.21 / 0.23 (4570) | 22.0% | 58.0% | 77.8% | 60.6% [58.5%-62.1%] | 23.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +38.6 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 149.0, B 1179.0; serve-point win A 53.2%, B 45.2%; Elo A 1261.3, B 1317.2; model uncertainty 0.0182
* Form inputs: days since last match A 367, B 353; matches on record A 5, B 26; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01GARTKA-TKA  (YES = Adriana Tkachenko)
Model: 61%
Kalshi: 22%
Gap: +39 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.021, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Francisca Jorge vs Kylie Collins -- W75 Quinta do Lago R16

ITF (ITF) · Hard · scheduled 2026-10-01T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:216055:220891:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kylie Collins (`KXITFWMATCH-26OCT01JORCOL-COL`) | 0.43 / 0.46 (1) | 44.5% | 31.2% | 29.5% | 26.4% [25.1%-27.7%] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -18.1 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Francisca Jorge (`KXITFWMATCH-26OCT01JORCOL-JOR`) | 0.55 / 0.56 (84) | 55.5% | 68.8% | 70.5% | 73.6% [72.3%-74.9%] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +18.1 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3145.0, B 2145.0; serve-point win A 57.5%, B 46.2%; Elo A 1652.2, B 1438.5; model uncertainty 0.0131
* Form inputs: days since last match A 9, B 10; matches on record A 457, B 126; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01JORCOL-JOR  (YES = Francisca Jorge)
Model: 74%
Kalshi: 56%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.004, surface_dev_loose +0.009, surface_dev_tight -0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Linda Klimovicova vs Alicia Dudeney -- W75 Quinta do Lago R16

ITF (ITF) · Hard · scheduled 2026-10-01T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221626:260206:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alicia Dudeney (`KXITFWMATCH-26OCT01KLIDUD-DUD`) | 0.40 / 0.42 (4227) | 41.0% | 55.1% | 74.0% | 63.3% [47.9%-69.5%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +22.4 pp | HIGH_REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Linda Klimovicova (`KXITFWMATCH-26OCT01KLIDUD-KLI`) | 0.57 / 0.58 (40) | 57.5% | 44.9% | 26.0% | 36.6% [30.5%-52.1%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -20.9 pp | HIGH_REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2873.0, B 3238.0; serve-point win A 55.2%, B 43.8%; Elo A 1725.3, B 1659.9; model uncertainty 0.1082
* Form inputs: days since last match A 36, B 94; matches on record A 261, B 92; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01KLIDUD-DUD  (YES = Alicia Dudeney)
Model: 63%
Kalshi: 41%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: STALE_KALSHI_QUOTE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.020, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Galena Krastenova vs Oana Georgeta Simion -- W15 Varna R16

ITF (ITF) · Clay · scheduled 2026-10-01T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:211646:265603:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Galena Krastenova (`KXITFWMATCH-26OCT01KRASIM-KRA`) | 0.11 / 0.13 (3222) | 12.0% | 19.7% | 29.1% | 20.3% [19.5%-21.8%] | 14.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +8.3 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oana Georgeta Simion (`KXITFWMATCH-26OCT01KRASIM-SIM`) | 0.87 / 0.90 (3358) | 88.5% | 80.3% | 70.9% | 79.7% [78.2%-80.5%] | 85.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.8 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 135.0, B 1762.0; serve-point win A 50.8%, B 42.8%; Elo A 1276.6, B 1520.4; model uncertainty 0.0116
* Form inputs: days since last match A 388, B 178; matches on record A 24, B 543; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.007, surface_dev_loose -0.004, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Manon Leonard vs Clara Vlasselaer -- W35 Reims R16

ITF (ITF) · Hard · scheduled 2026-10-01T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:215807:221003:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Manon Leonard (`KXITFWMATCH-26OCT01LEOVLA-LEO`) | 0.66 / 0.67 (1183) | 66.5% | 66.5% | 69.8% | 70.2% [66.7%-71.5%] | 68.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +3.7 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Clara Vlasselaer (`KXITFWMATCH-26OCT01LEOVLA-VLA`) | 0.32 / 0.33 (3997) | 32.5% | 33.5% | 30.2% | 29.8% [28.5%-33.3%] | 31.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.7 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3201.0, B 1490.0; serve-point win A 57.3%, B 45.9%; Elo A 1629.8, B 1481.5; model uncertainty 0.0235
* Form inputs: days since last match A 108, B 157; matches on record A 347, B 332; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.018, surface_pool_high +0.009, surface_dev_loose +0.004, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lisa Pigato vs Adrienn Nagy -- W75 Quinta do Lago R16

ITF (ITF) · Hard · scheduled 2026-10-01T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:215909:221354:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrienn Nagy (`KXITFWMATCH-26OCT01PIGNAG-NAG`) | 0.12 / 0.13 (58) | 12.5% | 20.6% | 16.2% | 18.3% [16.6%-20.1%] | 13.3% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +5.8 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lisa Pigato (`KXITFWMATCH-26OCT01PIGNAG-PIG`) | 0.86 / 0.88 (10) | 87.0% | 79.4% | 83.8% | 81.7% [79.9%-83.4%] | 86.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4114.0, B 1856.0; serve-point win A 58.8%, B 47.4%; Elo A 1654.6, B 1421.1; model uncertainty 0.0176
* Form inputs: days since last match A 12, B 25; matches on record A 353, B 313; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.017, surface_pool_high -0.018, surface_dev_loose +0.003, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sakellaridi / Vilar vs Veleva / Williams -- W15 Varna QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01SAKVILVELWIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sakellaridi / Vilar (`KXITFWDOUBLES-26OCT01SAKVILVELWIL-SAKVIL`) | 0.62 / 0.67 (3) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Veleva / Williams (`KXITFWDOUBLES-26OCT01SAKVILVELWIL-VELWIL`) | 0.18 / 0.36 (32) | 27.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Isabella Maria Serban vs Marie Weckerle -- W35 Reims R16

ITF (ITF) · Hard · scheduled 2026-10-01T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220946:265197:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isabella Maria Serban (`KXITFWMATCH-26OCT01SERWEC-SER`) | 0.71 / 0.75 (2694) | 73.0% | 47.8% | 39.4% | 42.5% [39.9%-47.3%] | 71.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -30.5 pp | EXTREME (DATA_WARNING) | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marie Weckerle (`KXITFWMATCH-26OCT01SERWEC-WEC`) | 0.26 / 0.29 (3178) | 27.5% | 52.2% | 60.6% | 57.5% [52.7%-60.1%] | 28.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +30.0 pp | EXTREME (DATA_WARNING) | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2134.0, B 1952.0; serve-point win A 55.5%, B 44.1%; Elo A 1459.0, B 1478.0; model uncertainty 0.037
* Form inputs: days since last match A 8, B 157; matches on record A 114, B 223; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01SERWEC-WEC  (YES = Marie Weckerle)
Model: 57%
Kalshi: 28%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_KALSHI_QUOTE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose -0.026, surface_dev_tight +0.026
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tiago Pereira vs Hugo Grenier -- ATP Challenger Porto 2 R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T16:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:126409:211500:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Grenier (`KXATPCHALLENGERMATCH-26OCT01PERGRE-GRE`) | 0.57 / 0.58 (4748) | 57.5% | 59.2% | 45.9% | 51.0% [49.0%-57.6%] | -- | -- | -- | -- | PASS | -6.5 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tiago Pereira (`KXATPCHALLENGERMATCH-26OCT01PERGRE-PER`) | 0.42 / 0.43 (4066) | 42.5% | 40.8% | 54.1% | 49.0% [42.4%-51.0%] | -- | -- | -- | -- | WATCH | +6.5 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5117.0, B 4799.0; serve-point win A 61.7%, B 36.5%; Elo A 1539.0, B 1658.2; model uncertainty 0.0432
* Form inputs: days since last match A 72, B 10; matches on record A 280, B 946; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.015, surface_dev_tight -0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Aleshchev / Dolzhenkov vs Azizov / Mert Ozdemir -- M15 Baku QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T16:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01ALEDOLAZIMER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aleshchev / Dolzhenkov (`KXITFDOUBLES-26OCT01ALEDOLAZIMER-ALEDOL`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Azizov / Mert Ozdemir (`KXITFDOUBLES-26OCT01ALEDOLAZIMER-AZIMER`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Ariel Behar / Joshua Paris vs Alexander Donski / Filip Pieczonka -- ATP Challenger Porto 2 QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T16:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01BEHPARDONPIE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ariel Behar / Joshua Paris (`KXATPCHALLENGERDOUBLES-26OCT01BEHPARDONPIE-BEHPAR`) | 0.42 / 0.50 (50) | 46.0% | 18.7% | -- | -- [-----] | -- | -- | -- | -- | -- | -27.3 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Alexander Donski / Filip Pieczonka (`KXATPCHALLENGERDOUBLES-26OCT01BEHPARDONPIE-DONPIE`) | 0.48 / 0.55 (42) | 51.5% | 81.3% | -- | -- [-----] | -- | -- | -- | -- | -- | +29.8 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERDOUBLES-26OCT01BEHPARDONPIE-DONPIE  (YES = Alexander Donski / Filip Pieczonka)
Model: 81%
Kalshi: 52%
Gap: +30 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, PLAYER_IDENTITY_RISK, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Warnings: DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Pierre Delage vs Ryan Nijboer -- M25 Zaragoza R16

ITF (ITF) · Clay · scheduled 2026-10-01T16:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:207764:208265:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pierre Delage (`KXITFMATCH-26OCT01DELNIJ-DEL`) | 0.32 / 0.34 (3703) | 33.0% | 41.9% | 47.9% | 43.2% [41.1%-45.3%] | 32.5% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +10.2 pp | REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ryan Nijboer (`KXITFMATCH-26OCT01DELNIJ-NIJ`) | 0.66 / 0.69 (11) | 67.5% | 58.1% | 52.1% | 56.8% [54.7%-58.9%] | 67.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -10.7 pp | REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2897.0, B 4005.0; serve-point win A 59.1%, B 39.3%; Elo A 1385.0, B 1482.5; model uncertainty 0.0206
* Form inputs: days since last match A 108, B 10; matches on record A 215, B 484; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nicolas Ifi vs Pedro Rodenas -- M25 Zaragoza R16

ITF (ITF) · Clay · scheduled 2026-10-01T16:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210203:212552:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Ifi (`KXITFMATCH-26OCT01IFIROD-IFI`) | 0.09 / 0.10 (3881) | 9.5% | 18.5% | 12.7% | 15.5% [13.5%-19.4%] | 12.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +6.0 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pedro Rodenas (`KXITFMATCH-26OCT01IFIROD-ROD`) | 0.90 / 0.91 (9096) | 90.5% | 81.5% | 87.3% | 84.5% [80.6%-86.5%] | 87.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.0 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1923.0, B 1623.0; serve-point win A 56.4%, B 36.6%; Elo A 1239.5, B 1490.7; model uncertainty 0.0295
* Form inputs: days since last match A 129, B 311; matches on record A 78, B 98; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.012, surface_pool_high +0.012, surface_dev_loose -0.008, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alejandro Moro Canas vs Bruno Pujol Navarro -- M25 Zaragoza R16

ITF (ITF) · Clay · scheduled 2026-10-01T16:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:207547:208279:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alejandro Moro Canas (`KXITFMATCH-26OCT01MORPUJ-MOR`) | 0.92 / 0.94 (3137) | 93.0% | 93.1% | 91.4% | 92.9% [91.4%-94.4%] | -- | -- | -- | -- | PASS | -0.1 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Bruno Pujol Navarro (`KXITFMATCH-26OCT01MORPUJ-PUJ`) | 0.06 / 0.07 (71) | 6.5% | 6.9% | 8.6% | 7.1% [5.6%-8.6%] | -- | -- | -- | -- | PASS | +0.6 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6297.0, B 250.0; serve-point win A 65.6%, B 45.9%; Elo A 1639.8, B 1188.7; model uncertainty 0.0151
* Form inputs: days since last match A 17, B 234; matches on record A 426, B 126; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.015, surface_dev_loose +0.002, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arthur Reymond / Luca Sanchez vs Stefan Latinovic / Mili Poljicak -- ATP Challenger Porto 2 QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T16:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01REYSANLATPOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefan Latinovic / Mili Poljicak (`KXATPCHALLENGERDOUBLES-26OCT01REYSANLATPOL-LATPOL`) | 0.34 / 0.44 (500) | 39.0% | 77.1% | -- | -- [-----] | -- | -- | -- | -- | -- | +38.1 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Arthur Reymond / Luca Sanchez (`KXATPCHALLENGERDOUBLES-26OCT01REYSANLATPOL-REYSAN`) | 0.56 / 0.66 (500) | 61.0% | 22.9% | -- | -- [-----] | -- | -- | -- | -- | -- | -38.1 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERDOUBLES-26OCT01REYSANLATPOL-LATPOL  (YES = Stefan Latinovic / Mili Poljicak)
Model: 77%
Kalshi: 39%
Gap: +38 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, PLAYER_IDENTITY_RISK, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Warnings: DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Mateus Alves vs Gonzalo Villanueva -- ATP Challenger Curitiba R16

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:106380:127123:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mateus Alves (`KXATPCHALLENGERMATCH-26OCT01ALVVIL-ALV`) | 0.64 / 0.65 (977) | 64.5% | -- | 56.1% | 53.5% [50.5%-55.6%] | -- | -- | -- | -- | PASS | -10.9 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gonzalo Villanueva (`KXATPCHALLENGERMATCH-26OCT01ALVVIL-VIL`) | 0.36 / 0.37 (1145) | 36.5% | -- | 43.9% | 46.5% [44.4%-49.5%] | -- | -- | -- | -- | SHADOW_BET | +9.9 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4869.0, B 5724.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0253
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Bangargi / Chaurasia vs Beckley / Sahtali -- M25 Kigali QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01BANCHABECSAH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bangargi / Chaurasia (`KXITFDOUBLES-26OCT01BANCHABECSAH-BANCHA`) | 0.06 / 0.84 (2065) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Beckley / Sahtali (`KXITFDOUBLES-26OCT01BANCHABECSAH-BECSAH`) | 0.06 / 0.94 (1110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Brown / De Alba vs Gatoto / Shalin Shah -- M25 Kigali QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01BRODEAGATSHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brown / De Alba (`KXITFDOUBLES-26OCT01BRODEAGATSHA-BRODEA`) | 0.06 / 0.74 (3) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gatoto / Shalin Shah (`KXITFDOUBLES-26OCT01BRODEAGATSHA-GATSHA`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Clement Chidekh vs Ugo Blanchet -- ATP Challenger Mouilleron-Le-Captif R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:200259:206889:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ugo Blanchet (`KXATPCHALLENGERMATCH-26OCT01CHIBLA-BLA`) | 0.28 / 0.30 (229) | 29.0% | -- | 31.6% | 34.3% [31.6%-41.0%] | 30.3% | -- | 30.3% | MODEL_LONE_OUTLIER | WATCH | +5.3 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Clement Chidekh (`KXATPCHALLENGERMATCH-26OCT01CHIBLA-CHI`) | 0.69 / 0.71 (6186) | 70.0% | -- | 68.4% | 65.7% [59.0%-68.4%] | 69.7% | -- | 69.7% | MODEL_LONE_OUTLIER | PASS | -4.3 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5365.0, B 4988.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0471
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.018, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Mariano Kestelboim / Marcelo Zormann vs Brandon Perez / Paulo Andre Saraiva Dos Santos -- ATP Challenger Curitiba QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01KESZORPERSAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mariano Kestelboim / Marcelo Zormann (`KXATPCHALLENGERDOUBLES-26OCT01KESZORPERSAR-KESZOR`) | 0.25 / 0.75 (25) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Brandon Perez / Paulo Andre Saraiva Dos Santos (`KXATPCHALLENGERDOUBLES-26OCT01KESZORPERSAR-PERSAR`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Nefve / Schachter vs Lock / John Lock -- M25 Kigali QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01NEFSCHLOCJOH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lock / John Lock (`KXITFDOUBLES-26OCT01NEFSCHLOCJOH-LOCJOH`) | 0.06 / 0.68 (3) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nefve / Schachter (`KXITFDOUBLES-26OCT01NEFSCHLOCJOH-NEFSCH`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Van Herck / Vankan vs Denolly / Plunger -- M25 Kigali QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01VANVANDENPLU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Denolly / Plunger (`KXITFDOUBLES-26OCT01VANVANDENPLU-DENPLU`) | 0.06 / 0.59 (502) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Van Herck / Vankan (`KXITFDOUBLES-26OCT01VANVANDENPLU-VANVAN`) | 0.07 / 0.54 (2) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Akli / Brantmeier vs Da Silva Fick / Voloshchuk -- W75 Quinta do Lago SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01AKLBRADASVOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Akli / Brantmeier (`KXITFWDOUBLES-26OCT01AKLBRADASVOL-AKLBRA`) | 0.51 / 0.77 (43) | 64.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Da Silva Fick / Voloshchuk (`KXITFWDOUBLES-26OCT01AKLBRADASVOL-DASVOL`) | 0.28 / 0.47 (0) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Naiktha Bains vs Polona Hercog -- W75 Quinta do Lago R16

ITF (ITF) · Hard · scheduled 2026-10-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:201555:206362:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naiktha Bains (`KXITFWMATCH-26OCT01BAIHER-BAI`) | 0.44 / 0.45 (45) | 44.5% | 35.6% | 37.3% | 37.8% [36.4%-39.2%] | 43.9% | -- | 43.9% | MODEL_LONE_OUTLIER | PASS | -6.7 pp | NORMAL | STALE | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Polona Hercog (`KXITFWMATCH-26OCT01BAIHER-HER`) | 0.54 / 0.55 (968) | 54.5% | 64.4% | 62.7% | 62.2% [60.8%-63.6%] | 56.1% | -- | 56.1% | MODEL_LONE_OUTLIER | WATCH | +7.7 pp | NORMAL | STALE | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2400.0, B 2590.0; serve-point win A 54.3%, B 42.9%; Elo A 1567.7, B 1647.9; model uncertainty 0.0144
* Form inputs: days since last match A 7, B 10; matches on record A 482, B 863; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.011, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Im / Kim vs Nahimana / Weckerle -- W35 Reims SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01IMXKIMNAHWEC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Im / Kim (`KXITFWDOUBLES-26OCT01IMXKIMNAHWEC-IMXKIM`) | 0.07 / 0.64 (2) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nahimana / Weckerle (`KXITFWDOUBLES-26OCT01IMXKIMNAHWEC-NAHWEC`) | 0.15 / 0.43 (577) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Harmony Tan vs Eva Vedder -- W75 Quinta do Lago R16

ITF (ITF) · Hard · scheduled 2026-10-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:211552:220770:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Harmony Tan (`KXITFWMATCH-26OCT01TANVED-TAN`) | 0.61 / 0.64 (422) | 62.5% | 66.8% | 79.9% | 76.0% [69.2%-78.3%] | 60.6% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +13.5 pp | REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Eva Vedder (`KXITFWMATCH-26OCT01TANVED-VED`) | 0.36 / 0.38 (3814) | 37.0% | 33.2% | 20.1% | 24.0% [21.6%-30.8%] | 39.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.0 pp | REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3731.0, B 3271.0; serve-point win A 57.3%, B 46.0%; Elo A 1712.2, B 1586.1; model uncertainty 0.0458
* Form inputs: days since last match A 7, B 16; matches on record A 649, B 432; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.008, surface_dev_loose +0.011, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Klara Veldman vs Britt Du Pree -- W35 Reims R16

ITF (ITF) · Hard · scheduled 2026-10-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:223418:264228:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Britt Du Pree (`KXITFWMATCH-26OCT01VELDUP-DUP`) | 0.87 / 0.90 (3394) | 88.5% | 82.8% | 89.1% | 85.2% [81.5%-87.8%] | 86.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.3 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Klara Veldman (`KXITFWMATCH-26OCT01VELDUP-VEL`) | 0.10 / 0.13 (3136) | 11.5% | 17.2% | 10.9% | 14.8% [12.2%-18.5%] | 13.3% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +3.3 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1299.0, B 2691.0; serve-point win A 52.1%, B 40.7%; Elo A 1331.3, B 1580.2; model uncertainty 0.0314
* Form inputs: days since last match A 157, B 157; matches on record A 141, B 85; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.003, surface_pool_high +0.006, surface_dev_loose -0.003, surface_dev_tight +0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Romain Arneodo / Benjamin Kittay vs Alexandru Jecan / Szymon Kielan -- ATP Challenger Porto 2 QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T17:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01ARNKITJECKIE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Romain Arneodo / Benjamin Kittay (`KXATPCHALLENGERDOUBLES-26OCT01ARNKITJECKIE-ARNKIT`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexandru Jecan / Szymon Kielan (`KXATPCHALLENGERDOUBLES-26OCT01ARNKITJECKIE-JECKIE`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Adrian Andreescu / Claudiu Schinteie vs Ghetu / Melnic -- M25 Slobozia QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T17:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01ADRCLAGHEMEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Andreescu / Claudiu Schinteie (`KXITFDOUBLES-26OCT01ADRCLAGHEMEL-ADRCLA`) | 0.07 / 0.50 (2) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ghetu / Melnic (`KXITFDOUBLES-26OCT01ADRCLAGHEMEL-GHEMEL`) | 0.06 / 0.64 (2) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Pierluigi Basile vs Martin Krumich -- ATP Challenger Bari R16

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-01T17:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:209322:213003:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pierluigi Basile (`KXATPCHALLENGERMATCH-26OCT01BASKRU-BAS`) | 0.40 / 0.42 (4932) | 41.0% | -- | 25.6% | 29.5% [27.8%-30.8%] | 41.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.5 pp | REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Martin Krumich (`KXATPCHALLENGERMATCH-26OCT01BASKRU-KRU`) | 0.58 / 0.59 (2317) | 58.5% | -- | 74.4% | 70.5% [69.2%-72.2%] | 58.4% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +12.0 pp | REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1898.0, B 5732.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0155
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.009, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Biletic / Kajin vs Behr / Curavic -- M15 Sibenik QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T17:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01BILKAJBEHCUR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Behr / Curavic (`KXITFDOUBLES-26OCT01BILKAJBEHCUR-BEHCUR`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Biletic / Kajin (`KXITFDOUBLES-26OCT01BILKAJBEHCUR-BILKAJ`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Florin Breazu / Cristian Breazu vs Pokorny / Tsitsipas -- M25 Slobozia QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T17:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01FLOCRIPOKTSI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Florin Breazu / Cristian Breazu (`KXITFDOUBLES-26OCT01FLOCRIPOKTSI-FLOCRI`) | 0.07 / 0.90 (1503) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pokorny / Tsitsipas (`KXITFDOUBLES-26OCT01FLOCRIPOKTSI-POKTSI`) | 0.06 / 0.94 (1190) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Kuperstein / Peter Van Noord vs Jeran / Kupcic -- M15 Sibenik QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T17:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01KUPPETJERKUP:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jeran / Kupcic (`KXITFDOUBLES-26OCT01KUPPETJERKUP-JERKUP`) | 0.32 / 0.75 (0) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kuperstein / Peter Van Noord (`KXITFDOUBLES-26OCT01KUPPETJERKUP-KUPPET`) | 0.10 / 0.67 (1) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mashtakov / Savano vs Chayka / Yi Qing -- M15 Sibenik QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T17:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01MASSAVCHAYIQ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chayka / Yi Qing (`KXITFDOUBLES-26OCT01MASSAVCHAYIQ-CHAYIQ`) | 0.07 / 0.91 (235) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mashtakov / Savano (`KXITFDOUBLES-26OCT01MASSAVCHAYIQ-MASSAV`) | 0.06 / 0.94 (292) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Liam Broady / Emile Hudd vs Jarno Jans / Joran Vliegen -- ATP Challenger Mouilleron-Le-Captif QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01BROHUDJANVLI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liam Broady / Emile Hudd (`KXATPCHALLENGERDOUBLES-26OCT01BROHUDJANVLI-BROHUD`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jarno Jans / Joran Vliegen (`KXATPCHALLENGERDOUBLES-26OCT01BROHUDJANVLI-JANVLI`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Garcia Mestre / Naharro vs Giovannini / Maria Giovannini -- M25 Zaragoza QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01GARNAHGIOMAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Garcia Mestre / Naharro (`KXITFDOUBLES-26OCT01GARNAHGIOMAR-GARNAH`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Giovannini / Maria Giovannini (`KXITFDOUBLES-26OCT01GARNAHGIOMAR-GIOMAR`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Lucca Cervantes Tomas / Alejandro Reyes Tirado vs Meneses Perny / Perez socas -- M25 Zaragoza QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01LUCALEMENPER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucca Cervantes Tomas / Alejandro Reyes Tirado (`KXITFDOUBLES-26OCT01LUCALEMENPER-LUCALE`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Meneses Perny / Perez socas (`KXITFDOUBLES-26OCT01LUCALEMENPER-MENPER`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Bryce Nakashima vs Keegan Smith -- ATP Challenger Columbus R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:202333:210416:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bryce Nakashima (`KXATPCHALLENGERMATCH-26OCT01NAKSMI-NAK`) | 0.45 / 0.46 (297) | 45.5% | -- | 15.6% | 14.4% [12.8%-16.3%] | -- | -- | -- | -- | PASS | -31.1 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Keegan Smith (`KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI`) | 0.53 / 0.56 (330) | 54.5% | -- | 84.4% | 85.5% [83.7%-87.2%] | -- | -- | -- | -- | PASS | +31.1 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 451.0, B 5491.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0174
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI  (YES = Keegan Smith)
Model: 86%
Kalshi: 55%
Gap: +31 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.017, surface_pool_high -0.016, surface_dev_loose -0.002, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE

## Alexander Ikenna Okonkwo / Preston Stearns vs Alafia Ayeni / Billy Suarez -- ATP Challenger Columbus QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01OKOSTEAVESUA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alafia Ayeni / Billy Suarez (`KXATPCHALLENGERDOUBLES-26OCT01OKOSTEAVESUA-AVESUA`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexander Ikenna Okonkwo / Preston Stearns (`KXATPCHALLENGERDOUBLES-26OCT01OKOSTEAVESUA-OKOSTE`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Xavi Palomar vs Miguel Damas -- M25 Zaragoza R16

ITF (ITF) · Clay · scheduled 2026-10-01T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:207732:214015:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miguel Damas (`KXITFMATCH-26OCT01PALDAM-DAM`) | 0.88 / 0.92 (3864) | 90.0% | 90.2% | 93.7% | 92.6% [91.2%-94.2%] | 89.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.6 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Xavi Palomar (`KXITFMATCH-26OCT01PALDAM-PAL`) | 0.08 / 0.11 (74) | 9.5% | 9.8% | 6.3% | 7.4% [5.8%-8.8%] | 10.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.1 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 617.0, B 5726.0; serve-point win A 54.9%, B 35.1%; Elo A 1160.8, B 1584.0; model uncertainty 0.0149
* Form inputs: days since last match A 164, B 24; matches on record A 12, B 410; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.004, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andrienko / Georgiana Goina vs Ksandinov / Stamatova -- W15 Varna QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01ANDGEOKSASTA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrienko / Georgiana Goina (`KXITFWDOUBLES-26OCT01ANDGEOKSASTA-ANDGEO`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ksandinov / Stamatova (`KXITFWDOUBLES-26OCT01ANDGEOKSASTA-KSASTA`) | 0.06 / 0.74 (1) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Charo Esquiva Banuls vs Radka Zelnickova -- W35 Baza R16

ITF (ITF) · Hard · scheduled 2026-10-01T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:222092:264962:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charo Esquiva Banuls (`KXITFWMATCH-26OCT01ESQZEL-ESQ`) | 0.72 / 0.75 (105) | 73.5% | 40.6% | 28.1% | 35.6% [33.1%-39.0%] | 72.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -37.9 pp | EXTREME (DATA_WARNING) | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Radka Zelnickova (`KXITFWMATCH-26OCT01ESQZEL-ZEL`) | 0.26 / 0.29 (216) | 27.5% | 59.4% | 72.0% | 64.4% [61.0%-66.9%] | 28.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +36.9 pp | EXTREME (DATA_WARNING) | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1005.0, B 2730.0; serve-point win A 54.8%, B 43.4%; Elo A 1466.2, B 1530.5; model uncertainty 0.0295
* Form inputs: days since last match A 16, B 16; matches on record A 35, B 304; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01ESQZEL-ZEL  (YES = Radka Zelnickova)
Model: 64%
Kalshi: 28%
Gap: +37 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.025, surface_dev_loose -0.019, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ilinca Burcescu / Dorofeeva-Rybas vs Elena Barbulescu / Wanja Brune Olsen -- W15 Varna QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01ILIDORELEWAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elena Barbulescu / Wanja Brune Olsen (`KXITFWDOUBLES-26OCT01ILIDORELEWAN-ELEWAN`) | 0.06 / 0.76 (1) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ilinca Burcescu / Dorofeeva-Rybas (`KXITFWDOUBLES-26OCT01ILIDORELEWAN-ILIDOR`) | 0.06 / 0.79 (4) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Valentina Ivanov vs Alba Maria Coromina Boluda -- W35 Baza R16

ITF (ITF) · Hard · scheduled 2026-10-01T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221173:269270:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alba Maria Coromina Boluda (`KXITFWMATCH-26OCT01IVACOR-COR`) | 0.11 / 0.14 (4697) | 12.5% | 15.0% | 11.4% | 14.4% [11.9%-16.7%] | 14.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valentina Ivanov (`KXITFWMATCH-26OCT01IVACOR-IVA`) | 0.86 / 0.89 (196) | 87.5% | 85.0% | 88.6% | 85.5% [83.3%-88.1%] | 85.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1892.0, B 174.0; serve-point win A 59.6%, B 48.2%; Elo A 1496.4, B 1195.6; model uncertainty 0.0243
* Form inputs: days since last match A 164, B 304; matches on record A 135, B 4; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.009, surface_dev_loose +0.003, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rasim / Velikova vs Mair / Peer -- W15 Varna QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01RASVELMAIPEE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mair / Peer (`KXITFWDOUBLES-26OCT01RASVELMAIPEE-MAIPEE`) | 0.07 / 0.62 (2) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rasim / Velikova (`KXITFWDOUBLES-26OCT01RASVELMAIPEE-RASVEL`) | 0.06 / 0.52 (2) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Samuel Heredia / Miguel Tobon vs Bruno (2002) Oliveira / Natan Rodrigues -- ATP Challenger Curitiba QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T18:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01HERTOBOLIROD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Samuel Heredia / Miguel Tobon (`KXATPCHALLENGERDOUBLES-26OCT01HERTOBOLIROD-HERTOB`) | 0.29 / 0.39 (500) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bruno (2002) Oliveira / Natan Rodrigues (`KXATPCHALLENGERDOUBLES-26OCT01HERTOBOLIROD-OLIROD`) | 0.61 / 0.71 (500) | 66.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Joao Eduardo Schiessl vs Luis Guto Miguel -- ATP Challenger Curitiba R16

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-01T18:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210214:213036:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luis Guto Miguel (`KXATPCHALLENGERMATCH-26OCT01SCHMIG-MIG`) | 0.76 / 0.77 (63) | 76.5% | -- | 64.0% | 51.5% [42.9%-56.6%] | -- | -- | -- | -- | PASS | -25.0 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Joao Eduardo Schiessl (`KXATPCHALLENGERMATCH-26OCT01SCHMIG-SCH`) | 0.21 / 0.24 (181) | 22.5% | -- | 36.0% | 48.5% [43.4%-57.1%] | -- | -- | -- | -- | WATCH | +26.0 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3018.0, B 1185.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0688
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT01SCHMIG-SCH  (YES = Joao Eduardo Schiessl)
Model: 48%
Kalshi: 22%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE

## Colombo / Demanet vs Branger / Dugardin -- M15 Monastir QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T18:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01COLDEMBRADUG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Branger / Dugardin (`KXITFDOUBLES-26OCT01COLDEMBRADUG-BRADUG`) | 0.06 / 0.55 (2) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Colombo / Demanet (`KXITFDOUBLES-26OCT01COLDEMBRADUG-COLDEM`) | 0.06 / 0.61 (2) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Duran / Ouakaa vs Ali Abibsi / Dell'elba -- M15 Monastir QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T18:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01DUROUAALIDEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ali Abibsi / Dell'elba (`KXITFDOUBLES-26OCT01DUROUAALIDEL-ALIDEL`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Duran / Ouakaa (`KXITFDOUBLES-26OCT01DUROUAALIDEL-DUROUA`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Heisnam / Rathi vs Nagoudi / Piatti -- M15 Monastir QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T18:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01HEIRATNAGPIA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Heisnam / Rathi (`KXITFDOUBLES-26OCT01HEIRATNAGPIA-HEIRAT`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nagoudi / Piatti (`KXITFDOUBLES-26OCT01HEIRATNAGPIA-NAGPIA`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Knis / Vildeuil vs Lumsden / Nortey -- M15 Monastir QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T18:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01KNIVILLUMNOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Knis / Vildeuil (`KXITFDOUBLES-26OCT01KNIVILLUMNOR-KNIVIL`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lumsden / Nortey (`KXITFDOUBLES-26OCT01KNIVILLUMNOR-LUMNOR`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Bazderova / Belyaeva vs Biolay / Cirotte -- W15 Monastir QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T18:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01BAZBELBIOCIR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bazderova / Belyaeva (`KXITFWDOUBLES-26OCT01BAZBELBIOCIR-BAZBEL`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Biolay / Cirotte (`KXITFWDOUBLES-26OCT01BAZBELBIOCIR-BIOCIR`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Bhopal / sahnoun vs Kroitor / Mi -- W15 Monastir QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T18:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01BHOSAHKROMIX:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bhopal / sahnoun (`KXITFWDOUBLES-26OCT01BHOSAHKROMIX-BHOSAH`) | 0.06 / 0.74 (1) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kroitor / Mi (`KXITFWDOUBLES-26OCT01BHOSAHKROMIX-KROMIX`) | 0.07 / 0.94 (110) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hinojosa Gomez / Losciale vs Bertacchi / Dibenedetto -- W15 Monastir QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T18:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01HINLOSBERDIB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bertacchi / Dibenedetto (`KXITFWDOUBLES-26OCT01HINLOSBERDIB-BERDIB`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hinojosa Gomez / Losciale (`KXITFWDOUBLES-26OCT01HINLOSBERDIB-HINLOS`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Aidan Mayo vs Colton Smith -- ATP Challenger Columbus R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T19:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208854:212256:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aidan Mayo (`KXATPCHALLENGERMATCH-26OCT01MAYSMI-MAY`) | 0.33 / 0.37 (75) | 35.0% | -- | 46.9% | 40.9% [38.0%-43.9%] | -- | -- | -- | -- | PASS | +5.9 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Colton Smith (`KXATPCHALLENGERMATCH-26OCT01MAYSMI-SMI`) | 0.62 / 0.66 (125) | 64.0% | -- | 53.0% | 59.1% [56.1%-62.0%] | -- | -- | -- | -- | PASS | -4.9 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3962.0, B 3806.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0297
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.010, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Abdullah Shelbayh vs Daniil Ostapenkov -- ATP Challenger Columbus R16

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-01T19:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01SHEOST:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniil Ostapenkov (`KXATPCHALLENGERMATCH-26OCT01SHEOST-OST`) | 0.26 / 0.29 (266) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Abdullah Shelbayh (`KXATPCHALLENGERMATCH-26OCT01SHEOST-SHE`) | 0.70 / 0.73 (201) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Guido Ivan Justo vs Pedro Sakamoto -- ATP Challenger Curitiba R16

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-01T19:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:106203:207815:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Guido Ivan Justo (`KXATPCHALLENGERMATCH-26OCT01JUSSAK-JUS`) | 0.65 / 0.68 (239) | 66.5% | -- | 79.7% | 75.8% [69.8%-78.6%] | -- | -- | -- | -- | WATCH | +9.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pedro Sakamoto (`KXATPCHALLENGERMATCH-26OCT01JUSSAK-SAK`) | 0.32 / 0.35 (175) | 33.5% | -- | 20.3% | 24.2% [21.4%-30.2%] | -- | -- | -- | -- | PASS | -9.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4964.0, B 4530.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0439
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose +0.008, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Franco Roncadelli / Gonzalo Villanueva vs Boris Arias / Ignacio Carou -- ATP Challenger Curitiba QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T19:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01RONVILARICAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Boris Arias / Ignacio Carou (`KXATPCHALLENGERDOUBLES-26OCT01RONVILARICAR-ARICAR`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Franco Roncadelli / Gonzalo Villanueva (`KXATPCHALLENGERDOUBLES-26OCT01RONVILARICAR-RONVIL`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Collins / Tanguilig vs Bayerlova / Gimbrere -- W75 Quinta do Lago SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T19:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01COLTANBAYGIM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bayerlova / Gimbrere (`KXITFWDOUBLES-26OCT01COLTANBAYGIM-BAYGIM`) | 0.06 / 0.53 (2) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Collins / Tanguilig (`KXITFWDOUBLES-26OCT01COLTANBAYGIM-COLTAN`) | 0.06 / 0.64 (2) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Salma Djoubri vs Amandine Monnot -- W35 Reims R16

ITF (ITF) · Hard · scheduled 2026-10-01T19:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220305:221486:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Salma Djoubri (`KXITFWMATCH-26OCT01DJOMON-DJO`) | 0.18 / 0.20 (1062) | 19.0% | 26.6% | 15.7% | 25.3% [23.3%-27.1%] | 20.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amandine Monnot (`KXITFWMATCH-26OCT01DJOMON-MON`) | 0.79 / 0.82 (4234) | 80.5% | 73.4% | 84.3% | 74.7% [72.9%-76.7%] | 79.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 169.0, B 3095.0; serve-point win A 53.3%, B 42.0%; Elo A 1467.4, B 1643.5; model uncertainty 0.019
* Form inputs: days since last match A 318, B 25; matches on record A 168, B 272; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.000, surface_dev_loose -0.004, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carmen Gallardo Guevara vs Celia Cervino Ruiz -- W35 Baza R16

ITF (ITF) · Hard · scheduled 2026-10-01T19:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:216078:222239:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Celia Cervino Ruiz (`KXITFWMATCH-26OCT01GALCER-CER`) | 0.40 / 0.43 (1592) | 41.5% | 46.9% | 39.0% | 46.8% [42.1%-54.8%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +5.3 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carmen Gallardo Guevara (`KXITFWMATCH-26OCT01GALCER-GAL`) | 0.57 / 0.60 (3253) | 58.5% | 53.1% | 61.0% | 53.2% [45.2%-57.9%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.3 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1358.0, B 1450.0; serve-point win A 56.0%, B 44.6%; Elo A 1410.1, B 1439.1; model uncertainty 0.0635
* Form inputs: days since last match A 157, B 9; matches on record A 48, B 265; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.016, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jonah Braswell vs Jordan Lee -- M15 Fayetteville AR R16

ITF (ITF) · Hard · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:211738:214265:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jonah Braswell (`KXITFMATCH-26OCT01BRALEE-BRA`) | 0.22 / 0.24 (1372) | 23.0% | 42.9% | 31.4% | 41.7% [38.6%-42.8%] | 23.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +18.7 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jordan Lee (`KXITFMATCH-26OCT01BRALEE-LEE`) | 0.75 / 0.78 (6187) | 76.5% | 57.1% | 68.6% | 58.3% [57.2%-61.4%] | 76.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -18.2 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 298.0, B 252.0; serve-point win A 61.9%, B 36.7%; Elo A 1291.2, B 1341.1; model uncertainty 0.021
* Form inputs: days since last match A 318, B 36; matches on record A 17, B 8; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01BRALEE-BRA  (YES = Jonah Braswell)
Model: 42%
Kalshi: 23%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Max Dahlin vs Alexander Bernard -- M15 Ann Arbor MI R16

ITF (ITF) · Hard · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:209060:211609:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Bernard (`KXITFMATCH-26OCT01DAHBER-BER`) | 0.20 / 0.23 (50) | 21.5% | 36.8% | 18.8% | 33.6% [28.2%-38.9%] | 21.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +12.1 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Max Dahlin (`KXITFMATCH-26OCT01DAHBER-DAH`) | 0.75 / 0.79 (1) | 77.0% | 63.2% | 81.2% | 66.4% [61.1%-71.8%] | 78.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -10.6 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 583.0, B 797.0; serve-point win A 63.9%, B 38.7%; Elo A 1424.0, B 1355.4; model uncertainty 0.0536
* Form inputs: days since last match A 66, B 325; matches on record A 41, B 108; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.005, surface_dev_loose +0.028, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## John Hallquist Lithen vs Benjamin Azar -- M15 Ann Arbor MI R16

ITF (ITF) · Hard · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208925:214449:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Benjamin Azar (`KXITFMATCH-26OCT01HALAZA-AZA`) | 0.10 / 0.13 (4676) | 11.5% | 32.2% | 14.8% | 31.0% [26.5%-32.9%] | 13.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +19.5 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| John Hallquist Lithen (`KXITFMATCH-26OCT01HALAZA-HAL`) | 0.85 / 0.90 (111) | 87.5% | 67.8% | 85.2% | 69.0% [67.1%-73.5%] | 86.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -18.5 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2695.0, B 108.0; serve-point win A 64.4%, B 39.2%; Elo A 1354.3, B 1225.3; model uncertainty 0.0318
* Form inputs: days since last match A 129, B 206; matches on record A 94, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01HALAZA-AZA  (YES = Benjamin Azar)
Model: 31%
Kalshi: 12%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.018, surface_dev_loose +0.009, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Harold Mayot vs Tristan Schoolkate -- ATP Challenger Mouilleron-Le-Captif R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208004:209262:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Harold Mayot (`KXATPCHALLENGERMATCH-26OCT01MAYSCH-MAY`) | 0.60 / 0.61 (1626) | 60.5% | -- | 60.8% | 59.3% [58.4%-60.3%] | -- | -- | -- | -- | PASS | -1.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tristan Schoolkate (`KXATPCHALLENGERMATCH-26OCT01MAYSCH-SCH`) | 0.39 / 0.40 (976) | 39.5% | -- | 39.2% | 40.7% [39.7%-41.6%] | -- | -- | -- | -- | PASS | +1.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5745.0, B 6276.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0096
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose +0.009, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Dominick Mosejczuk vs Vlado Jankanj -- M15 Fayetteville AR R16

ITF (ITF) · Hard · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:212892:213771:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vlado Jankanj (`KXITFMATCH-26OCT01MOSJAN-JAN`) | 0.23 / 0.25 (59) | 24.0% | 46.9% | 38.2% | 45.3% [43.8%-46.9%] | 25.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +21.3 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dominick Mosejczuk (`KXITFMATCH-26OCT01MOSJAN-MOS`) | 0.74 / 0.77 (3499) | 75.5% | 53.1% | 61.8% | 54.7% [53.1%-56.2%] | 74.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -20.8 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 379.0, B 875.0; serve-point win A 62.9%, B 37.7%; Elo A 1266.4, B 1244.6; model uncertainty 0.0157
* Form inputs: days since last match A 367, B 122; matches on record A 7, B 27; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01MOSJAN-JAN  (YES = Vlado Jankanj)
Model: 45%
Kalshi: 24%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Max Sheldon vs Olaf Pieczkowski -- M15 Ann Arbor MI R16

ITF (ITF) · Hard · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210142:210376:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Olaf Pieczkowski (`KXITFMATCH-26OCT01SHEPIE-PIE`) | 0.63 / 0.69 (3512) | 66.0% | 76.5% | 63.4% | 74.9% [70.6%-79.8%] | 65.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +8.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Max Sheldon (`KXITFMATCH-26OCT01SHEPIE-SHE`) | 0.31 / 0.35 (38) | 33.0% | 23.5% | 36.6% | 25.1% [20.2%-29.4%] | 34.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 264.0, B 2433.0; serve-point win A 59.7%, B 34.5%; Elo A 1229.6, B 1435.1; model uncertainty 0.0457
* Form inputs: days since last match A 486, B 59; matches on record A 13, B 234; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.028, surface_pool_high +0.035, surface_dev_loose -0.000, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Naoto Tomizawa vs Matt Kuhar -- M15 Ann Arbor MI R16

ITF (ITF) · Hard · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208386:214236:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matt Kuhar (`KXITFMATCH-26OCT01TOMKUH-KUH`) | 0.55 / 0.59 (3) | 57.0% | 51.7% | 64.4% | 52.1% [49.0%-55.8%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Naoto Tomizawa (`KXITFMATCH-26OCT01TOMKUH-TOM`) | 0.40 / 0.45 (45) | 42.5% | 48.3% | 35.6% | 47.9% [44.2%-51.0%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.4 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 62.0, B 2542.0; serve-point win A 62.4%, B 37.2%; Elo A 1263.2, B 1274.9; model uncertainty 0.0341
* Form inputs: days since last match A 339, B 129; matches on record A 1, B 139; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.021, surface_dev_loose -0.011, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alvin Nicholas Tudorica vs Neo Niedner -- M15 Fayetteville AR R16

ITF (ITF) · Hard · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210102:212202:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Neo Niedner (`KXITFMATCH-26OCT01TUDNIE-NIE`) | 0.35 / 0.39 (82) | 37.0% | 20.3% | 64.0% | 27.1% [23.2%-31.7%] | 37.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.9 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alvin Nicholas Tudorica (`KXITFMATCH-26OCT01TUDNIE-TUD`) | 0.61 / 0.65 (3578) | 63.0% | 79.7% | 36.0% | 72.9% [68.3%-76.8%] | 62.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +9.9 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1789.0, B 335.0; serve-point win A 65.9%, B 40.7%; Elo A 1409.1, B 1171.4; model uncertainty 0.0425
* Form inputs: days since last match A 206, B 122; matches on record A 106, B 29; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.017, surface_dev_loose -0.004, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Diva Bhatia vs Lourdes Ayala -- W15 Trelew R16

ITF (ITF) · Hard · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:236968:263876:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lourdes Ayala (`KXITFWMATCH-26OCT01BHAAYA-AYA`) | 0.91 / 0.94 (93) | 92.5% | 61.8% | 46.8% | 60.6% [60.6%-62.6%] | 90.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -31.9 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Diva Bhatia (`KXITFWMATCH-26OCT01BHAAYA-BHA`) | 0.06 / 0.10 (139) | 8.0% | 38.2% | 53.2% | 39.4% [37.4%-39.4%] | 9.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +31.4 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 49.0, B 813.0; serve-point win A 54.6%, B 43.2%; Elo A 1132.4, B 1215.8; model uncertainty 0.0102
* Form inputs: days since last match A 381, B 185; matches on record A 19, B 105; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01BHAAYA-BHA  (YES = Diva Bhatia)
Model: 39%
Kalshi: 8%
Gap: +31 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Leyla Fiorella Britez Risso vs Maria Sofia Madrid Rocca -- W15 Trelew R16

ITF (ITF) · Hard · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:222513:237458:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leyla Fiorella Britez Risso (`KXITFWMATCH-26OCT01BRIMAD-BRI`) | 0.92 / 0.95 (3225) | 93.5% | 75.2% | 21.9% | 75.7% [74.9%-75.7%] | -- | -- | -- | -- | PASS | -17.8 pp | HIGH_REVIEW (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Maria Sofia Madrid Rocca (`KXITFWMATCH-26OCT01BRIMAD-MAD`) | 0.05 / 0.07 (70) | 6.0% | 24.8% | 78.1% | 24.3% [24.3%-25.1%] | -- | -- | -- | -- | PASS | +18.3 pp | HIGH_REVIEW (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 257.0, B 0.0; serve-point win A 58.2%, B 46.9%; Elo A 1408.3, B 1215.7; model uncertainty 0.0043
* Form inputs: days since last match A 843, B 1200; matches on record A 44, B 25; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01BRIMAD-MAD  (YES = Maria Sofia Madrid Rocca)
Model: 24%
Kalshi: 6%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.008, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Salma Drugdova vs Carlota Moreno -- W15 Nashville TN R16

ITF (ITF) · surface ? · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:235160:270436:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Salma Drugdova (`KXITFWMATCH-26OCT01DRUMOR-DRU`) | 0.25 / 0.28 (83) | 26.5% | 54.4% | 42.0% | 52.1% [48.9%-53.7%] | 28.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +25.6 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carlota Moreno (`KXITFWMATCH-26OCT01DRUMOR-MOR`) | 0.71 / 0.75 (108) | 73.0% | 45.6% | 58.0% | 47.9% [46.3%-51.1%] | 72.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -25.1 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1429.0, B 350.0; serve-point win A 57.4%, B 43.4%; Elo A 1459.7, B 1429.2; model uncertainty 0.024
* Form inputs: days since last match A 423, B 178; matches on record A 158, B 6; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01DRUMOR-DRU  (YES = Salma Drugdova)
Model: 52%
Kalshi: 26%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valeria Ray vs Chiara Di Genova -- W15 Nashville TN R16

ITF (ITF) · surface ? · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221414:263760:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chiara Di Genova (`KXITFWMATCH-26OCT01RAYDIG-DIG`) | 0.12 / 0.15 (3117) | 13.5% | 37.6% | 50.5% | 38.5% [37.4%-39.5%] | 16.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +25.0 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valeria Ray (`KXITFWMATCH-26OCT01RAYDIG-RAY`) | 0.84 / 0.88 (78) | 86.0% | 62.4% | 49.5% | 61.5% [60.5%-62.6%] | 83.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -24.5 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 223.0, B 146.0; serve-point win A 58.2%, B 44.2%; Elo A 1402.1, B 1314.1; model uncertainty 0.0106
* Form inputs: days since last match A 423, B 500; matches on record A 5, B 69; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01RAYDIG-DIG  (YES = Chiara Di Genova)
Model: 38%
Kalshi: 14%
Gap: +25 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Merna Refaat vs Sophia Webster -- W15 Nashville TN R16

ITF (ITF) · surface ? · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221473:260046:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Merna Refaat (`KXITFWMATCH-26OCT01REFWEB-REF`) | 0.72 / 0.73 (1171) | 72.5% | 55.6% | 47.3% | 55.3% [55.3%-55.3%] | 69.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -17.2 pp | HIGH_REVIEW (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Sophia Webster (`KXITFWMATCH-26OCT01REFWEB-WEB`) | 0.26 / 0.27 (2295) | 26.5% | 44.4% | 52.7% | 44.7% [44.7%-44.7%] | 30.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +18.2 pp | HIGH_REVIEW (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 556.0, B 0.0; serve-point win A 57.5%, B 43.5%; Elo A 1376.3, B 1337.0; model uncertainty 0.0001
* Form inputs: days since last match A 353, B 836; matches on record A 201, B 16; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01REFWEB-WEB  (YES = Sophia Webster)
Model: 45%
Kalshi: 26%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stefani Webb vs Ashton Bowers -- W15 Nashville TN R16

ITF (ITF) · surface ? · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:248665:259567:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ashton Bowers (`KXITFWMATCH-26OCT01WEBBOW-BOW`) | 0.50 / 0.54 (267) | 52.0% | 52.0% | 35.9% | 52.1% [52.1%-52.1%] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.1 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Stefani Webb (`KXITFWMATCH-26OCT01WEBBOW-WEB`) | 0.47 / 0.50 (315) | 48.5% | 48.0% | 64.1% | 47.9% [47.9%-47.9%] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.6 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1878.0, B 0.0; serve-point win A 56.8%, B 42.8%; Elo A 1405.8, B 1419.7; model uncertainty 0.0
* Form inputs: days since last match A 255, B 710; matches on record A 101, B 46; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Liv Zingg vs Luna Maria Cinalli -- W15 Trelew R16

ITF (ITF) · surface ? · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01ZINCIN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luna Maria Cinalli (`KXITFWMATCH-26OCT01ZINCIN-CIN`) | 0.75 / 0.78 (7062) | 76.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Liv Zingg (`KXITFWMATCH-26OCT01ZINCIN-ZIN`) | 0.21 / 0.24 (975) | 22.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stefan Kozlov vs Mitchell Krueger -- ATP Challenger Columbus R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T20:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:106283:111578:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefan Kozlov (`KXATPCHALLENGERMATCH-26OCT01KOZKRU-KOZ`) | 0.49 / 0.52 (40) | 50.5% | -- | 51.0% | 50.5% [47.9%-51.5%] | -- | -- | -- | -- | PASS | +0.0 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mitchell Krueger (`KXATPCHALLENGERMATCH-26OCT01KOZKRU-KRU`) | 0.46 / 0.49 (50) | 47.5% | -- | 49.0% | 49.5% [48.4%-52.1%] | -- | -- | -- | -- | PASS | +2.0 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4126.0, B 5011.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0181
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Daniel Milavsky / Braden Shick vs Matthew Forbes / Denis Petak -- ATP Challenger Columbus QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T20:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01MILSHIFORPET:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthew Forbes / Denis Petak (`KXATPCHALLENGERDOUBLES-26OCT01MILSHIFORPET-FORPET`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daniel Milavsky / Braden Shick (`KXATPCHALLENGERDOUBLES-26OCT01MILSHIFORPET-MILSHI`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Pedro Boscardin Dias vs Genaro Alberto Olivieri -- ATP Challenger Curitiba R16

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-01T20:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:144821:208046:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pedro Boscardin Dias (`KXATPCHALLENGERMATCH-26OCT01BOSOLI-BOS`) | 0.56 / 0.89 (10) | 72.5% | -- | 47.9% | 47.9% [47.9%-48.4%] | -- | -- | -- | -- | PASS | -24.6 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Genaro Alberto Olivieri (`KXATPCHALLENGERMATCH-26OCT01BOSOLI-OLI`) | 0.28 / 0.45 (175) | 36.5% | -- | 52.1% | 52.1% [51.6%-52.1%] | -- | -- | -- | -- | PASS | +15.6 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4852.0, B 5465.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0026
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT01BOSOLI-OLI  (YES = Genaro Alberto Olivieri)
Model: 52%
Kalshi: 36%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Coppez / Tran vs Leonard / Martynov -- W35 Reims SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T20:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01COPTRALEOMAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Coppez / Tran (`KXITFWDOUBLES-26OCT01COPTRALEOMAR-COPTRA`) | 0.06 / 0.64 (2) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Leonard / Martynov (`KXITFWDOUBLES-26OCT01COPTRALEOMAR-LEOMAR`) | 0.06 / 0.54 (2) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Oliver Bonding vs Marko Mesarovic -- M15 Ann Arbor MI R16

ITF (ITF) · Hard · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:211670:212839:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oliver Bonding (`KXITFMATCH-26OCT01BONMES-BON`) | 0.80 / 0.82 (419) | 81.0% | 62.0% | 54.6% | 67.3% [64.0%-69.7%] | 81.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.7 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marko Mesarovic (`KXITFMATCH-26OCT01BONMES-MES`) | 0.16 / 0.19 (4277) | 17.5% | 38.0% | 45.4% | 32.7% [30.3%-36.0%] | 18.6% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +15.2 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1207.0, B 745.0; serve-point win A 63.8%, B 38.6%; Elo A 1440.2, B 1267.9; model uncertainty 0.0282
* Form inputs: days since last match A 38, B 122; matches on record A 42, B 24; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01BONMES-MES  (YES = Marko Mesarovic)
Model: 33%
Kalshi: 18%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.005, surface_dev_loose +0.005, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Micah Braswell vs Hugo Coquelin -- M15 Ann Arbor MI R16

ITF (ITF) · Hard · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:209334:213042:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Micah Braswell (`KXITFMATCH-26OCT01BRACOQ-BRA`) | 0.67 / 0.68 (383) | 67.5% | 79.1% | 74.5% | 78.1% [76.8%-79.4%] | 66.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +10.7 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hugo Coquelin (`KXITFMATCH-26OCT01BRACOQ-COQ`) | 0.31 / 0.32 (846) | 31.5% | 20.9% | 25.5% | 21.9% [20.6%-23.2%] | 33.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.7 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2173.0, B 446.0; serve-point win A 65.8%, B 40.6%; Elo A 1508.7, B 1277.2; model uncertainty 0.0126
* Form inputs: days since last match A 241, B 122; matches on record A 99, B 17; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.008, surface_dev_loose +0.008, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dragos Nicolae Cazacu vs Alexander Rozin -- M15 Fayetteville AR R16

ITF (ITF) · surface ? · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01CAZROZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dragos Nicolae Cazacu (`KXITFMATCH-26OCT01CAZROZ-CAZ`) | 0.17 / 0.21 (32) | 19.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexander Rozin (`KXITFMATCH-26OCT01CAZROZ-ROZ`) | 0.76 / 0.82 (33) | 79.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nikola Djosic vs Thanaphat Boosarawongse -- M15 Ann Arbor MI R16

ITF (ITF) · Hard · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:212149:213051:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thanaphat Boosarawongse (`KXITFMATCH-26OCT01DJOBOO-BOO`) | 0.58 / 0.59 (319) | 58.5% | 39.7% | 29.9% | 38.6% [35.6%-40.2%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -19.9 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nikola Djosic (`KXITFMATCH-26OCT01DJOBOO-DJO`) | 0.39 / 0.41 (5545) | 40.0% | 60.3% | 70.0% | 61.4% [59.8%-64.4%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +21.4 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1313.0, B 249.0; serve-point win A 63.6%, B 38.4%; Elo A 1289.1, B 1216.5; model uncertainty 0.023
* Form inputs: days since last match A 129, B 269; matches on record A 39, B 13; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01DJOBOO-DJO  (YES = Nikola Djosic)
Model: 61%
Kalshi: 40%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Theo Papamalamis vs Tito Chavez -- M15 Fayetteville AR R16

ITF (ITF) · Hard · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210494:214377:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tito Chavez (`KXITFMATCH-26OCT01PAPCHA-CHA`) | 0.31 / 0.33 (92) | 32.0% | 34.7% | 26.2% | 32.1% [30.2%-34.7%] | 33.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.1 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Theo Papamalamis (`KXITFMATCH-26OCT01PAPCHA-PAP`) | 0.64 / 0.68 (259) | 66.0% | 65.3% | 73.8% | 67.9% [65.3%-69.8%] | 66.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.9 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1643.0, B 499.0; serve-point win A 64.1%, B 39.0%; Elo A 1427.8, B 1317.9; model uncertainty 0.0226
* Form inputs: days since last match A 122, B 129; matches on record A 97, B 10; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose +0.019, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Johan Alexander Rodriguez vs Alejandro Melero Kretzer -- M15 Fayetteville AR R16

ITF (ITF) · surface ? · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01RODMEL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alejandro Melero Kretzer (`KXITFMATCH-26OCT01RODMEL-MEL`) | 0.21 / 0.25 (4010) | 23.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Johan Alexander Rodriguez (`KXITFMATCH-26OCT01RODMEL-ROD`) | 0.74 / 0.79 (32) | 76.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Damir Zhalgasbay vs Felix Corwin -- M15 Ann Arbor MI R16

ITF (ITF) · Hard · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:200228:212846:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felix Corwin (`KXITFMATCH-26OCT01ZHACOR-COR`) | 0.50 / 0.54 (54) | 52.0% | 80.5% | 67.7% | 79.2% [77.6%-80.0%] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +27.2 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Damir Zhalgasbay (`KXITFMATCH-26OCT01ZHACOR-ZHA`) | 0.45 / 0.50 (97) | 47.5% | 19.5% | 32.3% | 20.8% [20.0%-22.4%] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -26.7 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 222.0, B 3231.0; serve-point win A 59.2%, B 34.0%; Elo A 1156.7, B 1403.3; model uncertainty 0.0117
* Form inputs: days since last match A 157, B 171; matches on record A 6, B 382; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01ZHACOR-COR  (YES = Felix Corwin)
Model: 79%
Kalshi: 52%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Berecoechea / Candiotto vs Hietaranta / Zelnickova -- W35 Baza SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01BERCANHIEZEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Berecoechea / Candiotto (`KXITFWDOUBLES-26OCT01BERCANHIEZEL-BERCAN`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hietaranta / Zelnickova (`KXITFWDOUBLES-26OCT01BERCANHIEZEL-HIEZEL`) | 0.07 / 0.92 (8) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Pilar Da Silva vs Marina Bulbarella -- W15 Trelew R16

ITF (ITF) · surface ? · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01DASBUL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marina Bulbarella (`KXITFWMATCH-26OCT01DASBUL-BUL`) | 0.48 / 0.51 (194) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pilar Da Silva (`KXITFWMATCH-26OCT01DASBUL-DAS`) | 0.50 / 0.52 (3888) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Emma Kamper vs Kristina Paskauskas -- W15 Nashville TN R16

ITF (ITF) · surface ? · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:241715:258195:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emma Kamper (`KXITFWMATCH-26OCT01KAMPAS-KAM`) | 0.57 / 0.61 (3148) | 59.0% | 38.3% | 78.9% | 47.3% [39.5%-56.9%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.7 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kristina Paskauskas (`KXITFWMATCH-26OCT01KAMPAS-PAS`) | 0.39 / 0.42 (3589) | 40.5% | 61.7% | 21.1% | 52.7% [43.1%-60.6%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +12.2 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 510.0, B 382.0; serve-point win A 55.9%, B 41.9%; Elo A 1354.7, B 1437.4; model uncertainty 0.0873
* Form inputs: days since last match A 332, B 304; matches on record A 33, B 101; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ana Sofia Sanchez vs Florencia Belen Moron -- W15 Trelew R16

ITF (ITF) · Hard · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:204419:260357:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Florencia Belen Moron (`KXITFWMATCH-26OCT01SANMOR-MOR`) | 0.05 / 0.86 (1) | 45.5% | 6.9% | 13.3% | 7.4% [6.0%-8.4%] | -- | -- | -- | -- | PASS | -38.1 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ana Sofia Sanchez (`KXITFWMATCH-26OCT01SANMOR-SAN`) | 0.14 / 0.95 (2131) | 54.5% | 93.1% | 86.7% | 92.6% [91.6%-94.0%] | -- | -- | -- | -- | PASS | +38.1 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3191.0, B 144.0; serve-point win A 61.3%, B 49.9%; Elo A 1573.4, B 1120.4; model uncertainty 0.0117
* Form inputs: days since last match A 19, B 255; matches on record A 856, B 77; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01SANMOR-SAN  (YES = Ana Sofia Sanchez)
Model: 93%
Kalshi: 55%
Gap: +38 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.010, surface_dev_loose +0.002, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## CAIRA DELFINA VEGA GUDINO vs Maria Florencia Urrutia -- W15 Trelew R16

ITF (ITF) · Hard · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220447:270267:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Florencia Urrutia (`KXITFWMATCH-26OCT01VEGURR-URR`) | 0.05 / 0.95 (2142) | 50.0% | 81.5% | 81.2% | 81.9% [81.2%-82.6%] | -- | -- | -- | -- | PASS | +31.9 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| CAIRA DELFINA VEGA GUDINO (`KXITFWMATCH-26OCT01VEGURR-VEG`) | 0.05 / 0.95 (120) | 50.0% | 18.5% | 18.8% | 18.1% [17.4%-18.8%] | -- | -- | -- | -- | PASS | -31.9 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 120.0, B 2454.0; serve-point win A 52.3%, B 40.9%; Elo A 1228.4, B 1486.5; model uncertainty 0.007
* Form inputs: days since last match A 255, B 157; matches on record A 2, B 106; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01VEGURR-URR  (YES = Maria Florencia Urrutia)
Model: 82%
Kalshi: 50%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.007, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ashley Lahey vs Raquel Caballero Chica -- W15 Nashville TN R16

ITF (ITF) · surface ? · scheduled 2026-10-01T21:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:216076:231636:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raquel Caballero Chica (`KXITFWMATCH-26OCT01LAHCAB-CAB`) | 0.21 / 0.22 (53) | 21.5% | 8.4% | 25.0% | 9.3% [8.8%-9.8%] | 21.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.2 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ashley Lahey (`KXITFWMATCH-26OCT01LAHCAB-LAH`) | 0.77 / 0.78 (113) | 77.5% | 91.6% | 75.0% | 90.7% [90.2%-91.2%] | 78.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.2 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1883.0, B 74.0; serve-point win A 62.2%, B 48.2%; Elo A 1627.6, B 1213.5; model uncertainty 0.0048
* Form inputs: days since last match A 381, B 500; matches on record A 239, B 25; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eszter Meri vs Astra Sharma -- W15 Nashville TN R16

ITF (ITF) · surface ? · scheduled 2026-10-01T21:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:206292:221150:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eszter Meri (`KXITFWMATCH-26OCT01MERSHA-MER`) | 0.27 / 0.30 (142) | 28.5% | 31.5% | 48.9% | 35.4% [31.6%-39.0%] | 29.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.9 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Astra Sharma (`KXITFWMATCH-26OCT01MERSHA-SHA`) | 0.68 / 0.74 (320) | 71.0% | 68.5% | 51.1% | 64.6% [61.1%-68.4%] | 70.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.4 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 402.0, B 2800.0; serve-point win A 55.2%, B 41.2%; Elo A 1563.2, B 1698.2; model uncertainty 0.0368
* Form inputs: days since last match A 465, B 15; matches on record A 258, B 423; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rose Marie Nijkamp vs Francesca Mattioli -- W15 Nashville TN R16

ITF (ITF) · surface ? · scheduled 2026-10-01T21:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:260150:260225:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesca Mattioli (`KXITFWMATCH-26OCT01NIJMAT-MAT`) | 0.30 / 0.33 (76) | 31.5% | 49.1% | 39.4% | 46.8% [44.1%-48.9%] | 32.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +15.3 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rose Marie Nijkamp (`KXITFWMATCH-26OCT01NIJMAT-NIJ`) | 0.67 / 0.71 (429) | 69.0% | 50.9% | 60.6% | 53.2% [51.1%-55.9%] | 67.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.8 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1080.0, B 492.0; serve-point win A 57.1%, B 43.1%; Elo A 1482.4, B 1476.0; model uncertainty 0.0241
* Form inputs: days since last match A 164, B 423; matches on record A 54, B 28; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01NIJMAT-MAT  (YES = Francesca Mattioli)
Model: 47%
Kalshi: 32%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Podhajecka / Sharabura vs Pearce / Yamakita -- W15 Nashville TN QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T21:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01PODSHAPEAYAM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pearce / Yamakita (`KXITFWDOUBLES-26OCT01PODSHAPEAYAM-PEAYAM`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Podhajecka / Sharabura (`KXITFWDOUBLES-26OCT01PODSHAPEAYAM-PODSHA`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Ganchev / Maes vs Ifi / Stanke -- M25 Zaragoza QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01GANMAEIFISTA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ganchev / Maes (`KXITFDOUBLES-26OCT01GANMAEIFISTA-GANMAE`) | 0.09 / 0.78 (1) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ifi / Stanke (`KXITFDOUBLES-26OCT01GANMAEIFISTA-IFISTA`) | 0.06 / 0.79 (4) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Horwood / Vrba vs Roddick / Tokac -- M15 Fayetteville AR QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01HORVRBRODTOK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Horwood / Vrba (`KXITFDOUBLES-26OCT01HORVRBRODTOK-HORVRB`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Roddick / Tokac (`KXITFDOUBLES-26OCT01HORVRBRODTOK-RODTOK`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Pawlak / Pujol Navarro vs Lopez Martos / Palomar -- M25 Zaragoza QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01PAWPUJLOPPAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lopez Martos / Palomar (`KXITFDOUBLES-26OCT01PAWPUJLOPPAL-LOPPAL`) | 0.06 / 0.79 (1) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pawlak / Pujol Navarro (`KXITFDOUBLES-26OCT01PAWPUJLOPPAL-PAWPUJ`) | 0.06 / 0.80 (5) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alexander Ritschard vs samuel arauzo martinez -- M25 Zaragoza R16

ITF (ITF) · Clay · scheduled 2026-10-01T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:106310:213124:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| samuel arauzo martinez (`KXITFMATCH-26OCT01RITARA-ARA`) | 0.05 / 0.79 (100) | 42.0% | 4.6% | 16.8% | 4.6% [3.9%-5.4%] | -- | -- | -- | -- | PASS | -37.4 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Alexander Ritschard (`KXITFMATCH-26OCT01RITARA-RIT`) | 0.08 / 0.95 (2138) | 51.5% | 95.4% | 83.2% | 95.4% [94.6%-96.1%] | -- | -- | -- | -- | PASS | +43.9 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 3172.0, B 0.0; serve-point win A 66.5%, B 46.7%; Elo A 1773.1, B 1244.9; model uncertainty 0.0074
* Form inputs: days since last match A 24, B 787; matches on record A 681, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01RITARA-RIT  (YES = Alexander Ritschard)
Model: 95%
Kalshi: 52%
Gap: +44 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.008, surface_dev_loose -0.002, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Charlie Robertson vs Hoyoung Roh -- M15 Fayetteville AR R16

ITF (ITF) · Hard · scheduled 2026-10-01T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:212115:212127:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charlie Robertson (`KXITFMATCH-26OCT01ROBROH-ROB`) | 0.49 / 0.53 (3872) | 51.0% | 52.7% | 56.8% | 54.7% [52.1%-56.8%] | -- | -- | -- | -- | PASS | +3.7 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hoyoung Roh (`KXITFMATCH-26OCT01ROBROH-ROH`) | 0.47 / 0.50 (50) | 48.5% | 47.3% | 43.2% | 45.3% [43.2%-47.9%] | -- | -- | -- | -- | PASS | -3.2 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1222.0, B 1129.0; serve-point win A 62.9%, B 37.7%; Elo A 1348.8, B 1325.4; model uncertainty 0.0236
* Form inputs: days since last match A 178, B 122; matches on record A 38, B 36; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aryan Shah vs Evan Bynoe -- M15 Fayetteville AR R16

ITF (ITF) · Hard · scheduled 2026-10-01T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208466:211325:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Evan Bynoe (`KXITFMATCH-26OCT01SHABYN-BYN`) | 0.24 / 0.27 (26) | 25.5% | 23.5% | 24.6% | 23.8% [22.1%-26.3%] | 26.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.7 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aryan Shah (`KXITFMATCH-26OCT01SHABYN-SHA`) | 0.71 / 0.74 (3) | 72.5% | 76.5% | 75.4% | 76.2% [73.7%-77.9%] | 73.6% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +3.7 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2442.0, B 1889.0; serve-point win A 65.5%, B 40.3%; Elo A 1455.1, B 1243.8; model uncertainty 0.0206
* Form inputs: days since last match A 68, B 143; matches on record A 130, B 102; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.004, surface_dev_loose -0.008, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Juliana Giaccio vs Mathilde Lollia -- W35 Baza R16

ITF (ITF) · Hard · scheduled 2026-10-01T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221443:269835:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juliana Giaccio (`KXITFWMATCH-26OCT01GIALOL-GIA`) | 0.45 / 0.49 (3186) | 47.0% | 29.8% | 26.6% | 26.6% [22.8%-31.1%] | 47.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -20.4 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mathilde Lollia (`KXITFWMATCH-26OCT01GIALOL-LOL`) | 0.51 / 0.54 (94) | 52.5% | 70.2% | 73.4% | 73.4% [68.8%-77.2%] | 52.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +20.9 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 776.0, B 2163.0; serve-point win A 53.7%, B 42.3%; Elo A 1236.6, B 1409.2; model uncertainty 0.0419
* Form inputs: days since last match A 192, B 171; matches on record A 22, B 173; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01GIALOL-LOL  (YES = Mathilde Lollia)
Model: 73%
Kalshi: 52%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.034, surface_pool_high +0.045, surface_dev_loose -0.008, surface_dev_tight +0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Friedman / Sohns vs Bartel / Justine Hejtmanek -- W15 Nashville TN QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T22:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01FRISOHBARJUS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bartel / Justine Hejtmanek (`KXITFWDOUBLES-26OCT01FRISOHBARJUS-BARJUS`) | 0.09 / 0.92 (5) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Friedman / Sohns (`KXITFWDOUBLES-26OCT01FRISOHBARJUS-FRISOH`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Luciana Moyano vs Sofia Meabe -- W15 Trelew R16

ITF (ITF) · Hard · scheduled 2026-10-01T22:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:237454:266446:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Meabe (`KXITFWMATCH-26OCT01MOYMEA-MEA`) | 0.31 / 0.32 (3225) | 31.5% | 40.2% | 21.8% | 37.3% [34.3%-40.4%] | 33.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luciana Moyano (`KXITFWMATCH-26OCT01MOYMEA-MOY`) | 0.67 / 0.70 (170) | 68.5% | 59.8% | 78.2% | 62.7% [59.6%-65.7%] | 66.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2452.0, B 235.0; serve-point win A 56.6%, B 45.2%; Elo A 1405.3, B 1336.4; model uncertainty 0.0305
* Form inputs: days since last match A 157, B 255; matches on record A 106, B 18; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.030, surface_pool_high -0.031, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Emily Zornada vs Ana Victoria Gobbi Monllau -- W15 Trelew R16

ITF (ITF) · Hard · scheduled 2026-10-01T22:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:211600:270329:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ana Victoria Gobbi Monllau (`KXITFWMATCH-26OCT01ZORGOB-GOB`) | 0.50 / 0.51 (567) | 50.5% | 42.5% | 32.4% | 42.0% [41.0%-42.6%] | 52.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.5 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Emily Zornada (`KXITFWMATCH-26OCT01ZORGOB-ZOR`) | 0.47 / 0.49 (74) | 48.0% | 57.5% | 67.6% | 58.0% [57.4%-59.0%] | 47.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +10.0 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 106.0, B 761.0; serve-point win A 56.4%, B 45.0%; Elo A 1299.7, B 1247.0; model uncertainty 0.008
* Form inputs: days since last match A 185, B 192; matches on record A 2, B 108; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Boland / Smillie vs Lestir / Milosavljevic -- M15 Fayetteville AR QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T23:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01BOLSMILESMIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Boland / Smillie (`KXITFDOUBLES-26OCT01BOLSMILESMIL-BOLSMI`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lestir / Milosavljevic (`KXITFDOUBLES-26OCT01BOLSMILESMIL-LESMIL`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Goity Zapico / Valletta vs Arcila / Rozin -- M15 Fayetteville AR QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T23:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01GOIVALARCROZ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arcila / Rozin (`KXITFDOUBLES-26OCT01GOIVALARCROZ-ARCROZ`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Goity Zapico / Valletta (`KXITFDOUBLES-26OCT01GOIVALARCROZ-GOIVAL`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Tatjana Maria vs Lea Ma -- W100 Templeton CA R16

ITF (ITF) · Hard · scheduled 2026-10-01T23:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:213583:221220:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tatjana Maria (`KXITFWMATCH-26OCT01MARMAX-MAR`) | 0.77 / 0.82 (33) | 79.5% | 54.0% | 28.5% | 42.3% [33.5%-65.7%] | -- | -- | -- | -- | PASS | -37.2 pp | EXTREME (DATA_WARNING) | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lea Ma (`KXITFWMATCH-26OCT01MARMAX-MAX`) | 0.18 / 0.23 (25) | 20.5% | 46.0% | 71.5% | 57.7% [34.3%-66.5%] | -- | -- | -- | -- | WATCH | +37.2 pp | EXTREME (DATA_WARNING) | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4444.0, B 2727.0; serve-point win A 56.1%, B 44.7%; Elo A 1749.9, B 1608.9; model uncertainty 0.161
* Form inputs: days since last match A 17, B 19; matches on record A 1257, B 167; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01MARMAX-MAX  (YES = Lea Ma)
Model: 58%
Kalshi: 20%
Gap: +37 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.041, surface_pool_high -0.045, surface_dev_loose -0.015, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Whitney Osuigwe vs Ella McDonald -- W100 Templeton CA R16

ITF (ITF) · Hard · scheduled 2026-10-01T23:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:215992:259591:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ella McDonald (`KXITFWMATCH-26OCT01OSUMCD-MCD`) | 0.44 / 0.48 (240) | 46.0% | 44.2% | 56.9% | 47.9% [39.9%-52.7%] | -- | -- | -- | -- | PASS | +1.9 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Whitney Osuigwe (`KXITFWMATCH-26OCT01OSUMCD-OSU`) | 0.53 / 0.56 (3234) | 54.5% | 55.8% | 43.1% | 52.1% [47.3%-60.1%] | -- | -- | -- | -- | PASS | -2.4 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3327.0, B 1341.0; serve-point win A 56.2%, B 44.9%; Elo A 1644.5, B 1577.9; model uncertainty 0.0637
* Form inputs: days since last match A 18, B 100; matches on record A 411, B 146; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.021, surface_dev_loose -0.021, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Malaika Rapolu vs Akasha Urhobo -- W100 Templeton CA R16

ITF (ITF) · Hard · scheduled 2026-10-01T23:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:222837:259857:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Malaika Rapolu (`KXITFWMATCH-26OCT01RAPURH-RAP`) | 0.55 / 0.58 (59) | 56.5% | 40.9% | 43.1% | 45.2% [40.0%-48.4%] | -- | -- | -- | -- | PASS | -11.3 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Akasha Urhobo (`KXITFWMATCH-26OCT01RAPURH-URH`) | 0.40 / 0.44 (3205) | 42.0% | 59.1% | 56.9% | 54.8% [51.6%-60.0%] | -- | -- | -- | -- | WATCH | +12.8 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1761.0, B 3335.0; serve-point win A 54.8%, B 43.5%; Elo A 1612.4, B 1631.7; model uncertainty 0.0421
* Form inputs: days since last match A 14, B 38; matches on record A 133, B 177; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.042, surface_pool_high +0.032, surface_dev_loose +0.005, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Azar / Cairo vs Klimas / Mikovic -- M15 Ann Arbor MI QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T23:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01AZACAIKLIMIK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Azar / Cairo (`KXITFDOUBLES-26OCT01AZACAIKLIMIK-AZACAI`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Klimas / Mikovic (`KXITFDOUBLES-26OCT01AZACAIKLIMIK-KLIMIK`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Fradkin / Kuhar vs Albieri / Heng -- M15 Ann Arbor MI QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T23:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01FRAKUHALBHEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Albieri / Heng (`KXITFDOUBLES-26OCT01FRAKUHALBHEN-ALBHEN`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fradkin / Kuhar (`KXITFDOUBLES-26OCT01FRAKUHALBHEN-FRAKUH`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Gogineni / Petrovic vs Burnett / Tomizawa -- M15 Ann Arbor MI QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T23:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01GOGPETBURTOM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Burnett / Tomizawa (`KXITFDOUBLES-26OCT01GOGPETBURTOM-BURTOM`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gogineni / Petrovic (`KXITFDOUBLES-26OCT01GOGPETBURTOM-GOGPET`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Sheldon / Swenson vs Matta / Peck -- M15 Ann Arbor MI QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T23:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01SHESWEMATPEC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matta / Peck (`KXITFDOUBLES-26OCT01SHESWEMATPEC-MATPEC`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sheldon / Swenson (`KXITFDOUBLES-26OCT01SHESWEMATPEC-SHESWE`) | 0.06 / 0.80 (5) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Carrocera / Maria Maruca vs Ayala / Fiorella Britez Risso -- W15 Trelew QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T23:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01CARMARAYAFIO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ayala / Fiorella Britez Risso (`KXITFWDOUBLES-26OCT01CARMARAYAFIO-AYAFIO`) | 0.07 / 0.93 (5) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Carrocera / Maria Maruca (`KXITFWDOUBLES-26OCT01CARMARAYAFIO-CARMAR`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Doldan / Celina Sosa vs Ailin Larraya Guidi / Sousa Salazar -- W15 Trelew QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T23:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01DOLCELAILSOU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ailin Larraya Guidi / Sousa Salazar (`KXITFWDOUBLES-26OCT01DOLCELAILSOU-AILSOU`) | 0.08 / 0.92 (13) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Doldan / Celina Sosa (`KXITFWDOUBLES-26OCT01DOLCELAILSOU-DOLCEL`) | 0.06 / 0.94 (210) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Carolina Kuhl vs Kristina Penickova -- W100 Templeton CA R16

ITF (ITF) · Hard · scheduled 2026-10-02T00:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:230882:266381:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carolina Kuhl (`KXITFWMATCH-26OCT01KUHPEN-KUH`) | 0.34 / 0.38 (40) | 36.0% | -- | 28.5% | 36.1% [30.4%-45.8%] | -- | -- | -- | -- | PASS | +0.1 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kristina Penickova (`KXITFWMATCH-26OCT01KUHPEN-PEN`) | 0.62 / 0.66 (27) | 64.0% | -- | 71.5% | 63.9% [54.2%-69.6%] | -- | -- | -- | -- | PASS | -0.1 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1139.0, B 1178.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0769
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.029, surface_dev_loose -0.004, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Francesca Pace vs Amelie Van Impe -- W100 Templeton CA R16

ITF (ITF) · Hard · scheduled 2026-10-02T00:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:228909:256673:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesca Pace (`KXITFWMATCH-26OCT01PACVAN-PAC`) | 0.56 / 0.61 (3300) | 58.5% | -- | 62.0% | 55.3% [50.5%-57.9%] | -- | -- | -- | -- | PASS | -3.2 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amelie Van Impe (`KXITFWMATCH-26OCT01PACVAN-VAN`) | 0.39 / 0.44 (45) | 41.5% | -- | 38.0% | 44.7% [42.1%-49.5%] | -- | -- | -- | -- | PASS | +3.2 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2585.0, B 1949.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0367
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.016, surface_dev_loose +0.026, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Julieta Pareja vs Mary Stoiana -- W100 Templeton CA R16

ITF (ITF) · Hard · scheduled 2026-10-02T00:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:223168:264075:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julieta Pareja (`KXITFWMATCH-26OCT01PARSTO-PAR`) | 0.41 / 0.45 (45) | 43.0% | -- | 35.5% | 36.5% [36.0%-37.5%] | -- | -- | -- | -- | PASS | -6.5 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mary Stoiana (`KXITFWMATCH-26OCT01PARSTO-STO`) | 0.55 / 0.59 (24) | 57.0% | -- | 64.5% | 63.5% [62.5%-64.0%] | -- | -- | -- | -- | WATCH | +6.5 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1273.0, B 2840.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0074
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Broadus / Zamarripa vs Chang / Hu -- W100 Templeton CA QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T01:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01BROZAMCHAHUX:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Broadus / Zamarripa (`KXITFWDOUBLES-26OCT01BROZAMCHAHUX-BROZAM`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Chang / Hu (`KXITFWDOUBLES-26OCT01BROZAMCHAHUX-CHAHUX`) | 0.07 / 0.93 (100) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Madison Brengle vs Arianna Zucchini -- W100 Templeton CA R16

ITF (ITF) · Hard · scheduled 2026-10-02T02:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:201483:222369:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Madison Brengle (`KXITFWMATCH-26OCT01BREZUC-BRE`) | 0.75 / 0.79 (21) | 77.0% | -- | 48.9% | 63.2% [58.0%-75.3%] | -- | -- | -- | -- | PASS | -13.8 pp | REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Arianna Zucchini (`KXITFWMATCH-26OCT01BREZUC-ZUC`) | 0.21 / 0.25 (34) | 23.0% | -- | 51.1% | 36.8% [24.7%-42.0%] | -- | -- | -- | -- | PASS | +13.8 pp | REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2464.0, B 2652.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0866
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.005, surface_dev_loose -0.015, surface_dev_tight +0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hewitt / Strakhova vs Frodin / Sahdiieva -- W100 Templeton CA QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T02:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01HEWSTRFROSAH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Frodin / Sahdiieva (`KXITFWDOUBLES-26OCT01HEWSTRFROSAH-FROSAH`) | 0.06 / 0.93 (1) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hewitt / Strakhova (`KXITFWDOUBLES-26OCT01HEWSTRFROSAH-HEWSTR`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kawano Cho / Tarantola vs Meabe / Florencia Urrutia -- W15 Trelew QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T02:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01KAWTARMEAFLO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kawano Cho / Tarantola (`KXITFWDOUBLES-26OCT01KAWTARMEAFLO-KAWTAR`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Meabe / Florencia Urrutia (`KXITFWDOUBLES-26OCT01KAWTARMEAFLO-MEAFLO`) | 0.07 / 0.93 (9) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Moyano / Sofia Sanchez vs Bhatia / Belen Moron -- W15 Trelew QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T02:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01MOYSOFBHABEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bhatia / Belen Moron (`KXITFWDOUBLES-26OCT01MOYSOFBHABEL-BHABEL`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Moyano / Sofia Sanchez (`KXITFWDOUBLES-26OCT01MOYSOFBHABEL-MOYSOF`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Penickova / Penickova vs Osuigwe / Urhobo -- W100 Templeton CA QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T03:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01PENPENOSUURH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Osuigwe / Urhobo (`KXITFWDOUBLES-26OCT01PENPENOSUURH-OSUURH`) | 0.07 / 0.92 (5) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Penickova / Penickova (`KXITFWDOUBLES-26OCT01PENPENOSUURH-PENPEN`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kyrian Jacquet vs Luciano Darderi -- ATP Tokyo R16

ATP (TOUR_500_250) · Hard · scheduled 2026-10-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208021:209260:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luciano Darderi (`KXATPMATCH-26OCT01JACDAR-DAR`) | 0.06 / 0.90 (50) | 48.0% | -- | 39.2% | 41.6% [37.8%-49.5%] | -- | -- | -- | -- | PASS | -6.4 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kyrian Jacquet (`KXATPMATCH-26OCT01JACDAR-JAC`) | 0.06 / 0.90 (50) | 48.0% | -- | 60.8% | 58.4% [50.5%-62.2%] | -- | -- | -- | -- | PASS | +10.4 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4700.0, B 7374.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0584
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.029, surface_pool_high +0.029, surface_dev_loose +0.038, surface_dev_tight -0.039
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXATPEXACTMATCH-26OCT01JACDAR-DAR21` Will Luciano Darderi win the Kyrian Jacquet vs Luciano Darderi match by a set score of 2-1?: 0.01/0.95 mid 48.0%, model 25.0% (market_conditioned_v1 (model4_board_v1)) -- gap -23.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01JACDAR-JAC20` Will Kyrian Jacquet win the Kyrian Jacquet vs Luciano Darderi match by a set score of 2-0?: 0.01/0.95 mid 48.0%, model 25.0% (market_conditioned_v1 (model4_board_v1)) -- gap -23.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01JACDAR-JAC21` Will Kyrian Jacquet win the Kyrian Jacquet vs Luciano Darderi match by a set score of 2-1?: 0.01/0.95 mid 48.0%, model 25.0% (market_conditioned_v1 (model4_board_v1)) -- gap -23.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01JACDAR-DAR20` Will Luciano Darderi win the Kyrian Jacquet vs Luciano Darderi match by a set score of 2-0?: 0.01/0.88 mid 44.5%, model 25.0% (market_conditioned_v1 (model4_board_v1)) -- gap -19.5 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Jaume Munar vs Jaime Faria -- ATP Tokyo R16

ATP (TOUR_500_250) · Hard · scheduled 2026-10-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144719:210262:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jaime Faria (`KXATPMATCH-26OCT01MUNFAR-FAR`) | 0.06 / 0.90 (50) | 48.0% | -- | 34.1% | 38.8% [35.9%-42.1%] | -- | -- | -- | -- | PASS | -9.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jaume Munar (`KXATPMATCH-26OCT01MUNFAR-MUN`) | 0.08 / 0.90 (50) | 49.0% | -- | 65.9% | 61.2% [57.9%-64.0%] | -- | -- | -- | -- | PASS | +12.2 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4944.0, B 5916.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0306
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.001, surface_dev_tight +0.010
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXATPEXACTMATCH-26OCT01MUNFAR-FAR20` Will Jaime Faria win the Jaume Munar vs Jaime Faria match by a set score of 2-0?: 0.01/0.95 mid 48.0%, model 25.0% (market_conditioned_v1 (model4_board_v1)) -- gap -23.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01MUNFAR-FAR21` Will Jaime Faria win the Jaume Munar vs Jaime Faria match by a set score of 2-1?: 0.01/0.95 mid 48.0%, model 25.0% (market_conditioned_v1 (model4_board_v1)) -- gap -23.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01MUNFAR-MUN20` Will Jaume Munar win the Jaume Munar vs Jaime Faria match by a set score of 2-0?: 0.01/0.95 mid 48.0%, model 25.0% (market_conditioned_v1 (model4_board_v1)) -- gap -23.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01MUNFAR-MUN21` Will Jaume Munar win the Jaume Munar vs Jaime Faria match by a set score of 2-1?: 0.01/0.95 mid 48.0%, model 25.0% (market_conditioned_v1 (model4_board_v1)) -- gap -23.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Alex Molcan vs Karen Khachanov -- ATP Beijing R16

ATP (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111575:144684:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karen Khachanov (`KXATPMATCH-26OCT01MOLKHA-KHA`) | 0.57 / 0.82 (3660) | 69.5% | -- | 70.7% | 71.2% [67.3%-72.3%] | -- | -- | -- | -- | PASS | +1.7 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alex Molcan (`KXATPMATCH-26OCT01MOLKHA-MOL`) | 0.07 / 0.56 (100) | 31.5% | -- | 29.3% | 28.8% [27.7%-32.6%] | -- | -- | -- | -- | PASS | -2.7 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3805.0, B 5981.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0249
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.008, surface_dev_loose -0.012, surface_dev_tight +0.012
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXATPEXACTMATCH-26OCT01MOLKHA-MOL20` Will Alex Molcan win the Alex Molcan vs Karen Khachanov match by a set score of 2-0?: 0.08/0.88 mid 48.0%, model 19.1% (market_conditioned_v1 (model4_board_v1)) -- gap -28.9 pp, EXTREME, DATA_WARNING, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01MOLKHA-MOL21` Will Alex Molcan win the Alex Molcan vs Karen Khachanov match by a set score of 2-1?: 0.08/0.88 mid 48.0%, model 21.5% (market_conditioned_v1 (model4_board_v1)) -- gap -26.5 pp, EXTREME, DATA_WARNING, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01MOLKHA-KHA21` Will Karen Khachanov win the Alex Molcan vs Karen Khachanov match by a set score of 2-1?: 0.01/0.88 mid 44.5%, model 27.7% (market_conditioned_v1 (model4_board_v1)) -- gap -16.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01MOLKHA-KHA20` Will Karen Khachanov win the Alex Molcan vs Karen Khachanov match by a set score of 2-0?: 0.01/0.95 mid 48.0%, model 31.7% (market_conditioned_v1 (model4_board_v1)) -- gap -16.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Yunchaokete Bu vs Novak Djokovic -- ATP Beijing R16

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT01YUNDJO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Novak Djokovic (`KXATPMATCH-26OCT01YUNDJO-DJO`) | 0.74 / 0.76 (15550) | 75.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yunchaokete Bu (`KXATPMATCH-26OCT01YUNDJO-YUN`) | 0.24 / 0.26 (38652) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ekaterina Alexandrova vs Aliaksandra Sasnovich -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:205925:206420:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Alexandrova (`KXWTAMATCH-26OCT01ALESAS-ALE`) | 0.57 / 0.60 (151) | 58.5% | -- | 60.4% | 61.4% [59.9%-64.9%] | 57.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.9 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aliaksandra Sasnovich (`KXWTAMATCH-26OCT01ALESAS-SAS`) | 0.40 / 0.43 (1093) | 41.5% | -- | 39.6% | 38.6% [35.1%-40.1%] | 42.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.9 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4877.0, B 4822.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0251
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.015, surface_dev_loose -0.010, surface_dev_tight +0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01ALESAS-28` Over 27.5 games: 0.18/0.27 mid 22.5%, model 34.4% (market_conditioned_v1 (model4_board_v1)) -- gap +11.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01ALESAS-23` Over 22.5 games: 0.38/0.52 mid 45.0%, model 55.9% (market_conditioned_v1 (model4_board_v1)) -- gap +10.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01ALESAS-18` Over 17.5 games: 0.73/0.86 mid 79.5%, model 88.0% (market_conditioned_v1 (model4_board_v1)) -- gap +8.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD

## Nikola Bartunkova vs Magdalena Frech -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211684:223360:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikola Bartunkova (`KXWTAMATCH-26OCT01BARFRE-BAR`) | 0.57 / 0.59 (38) | 58.0% | -- | 57.8% | 56.3% [50.5%-58.9%] | 58.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.7 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Magdalena Frech (`KXWTAMATCH-26OCT01BARFRE-FRE`) | 0.39 / 0.43 (1438) | 41.0% | -- | 42.2% | 43.7% [41.1%-49.5%] | 41.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.7 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3248.0, B 4552.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0416
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.021, surface_dev_loose +0.005, surface_dev_tight +0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01BARFRE-22` Over 21.5 games: 0.47/0.53 mid 50.0%, model 62.9% (market_conditioned_v1 (model4_board_v1)) -- gap +12.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01BARFRE-27` Over 26.5 games: 0.23/0.32 mid 27.5%, model 39.6% (market_conditioned_v1 (model4_board_v1)) -- gap +12.1 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01BARFRE-17` Over 16.5 games: 0.83/0.91 mid 87.0%, model 94.0% (market_conditioned_v1 (model4_board_v1)) -- gap +7.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD

## Sara Bejlek vs Maddison Inglis -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213666:239383:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Bejlek (`KXWTAMATCH-26OCT01BEJING-BEJ`) | 0.73 / 0.74 (219) | 73.5% | -- | 76.3% | 73.8% [69.7%-74.6%] | 70.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.3 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maddison Inglis (`KXWTAMATCH-26OCT01BEJING-ING`) | 0.26 / 0.27 (35) | 26.5% | -- | 23.7% | 26.2% [25.4%-30.3%] | 29.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.3 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3433.0, B 3027.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0244
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.018, surface_dev_loose +0.009, surface_dev_tight -0.009
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01BEJING-21` Over 20.5 games: 0.46/0.52 mid 49.0%, model 62.1% (market_conditioned_v1 (model4_board_v1)) -- gap +13.1 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01BEJING-26` Over 25.5 games: 0.23/0.31 mid 27.0%, model 39.4% (market_conditioned_v1 (model4_board_v1)) -- gap +12.4 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01BEJING-16` Over 15.5 games: 0.85/0.93 mid 89.0%, model 95.7% (market_conditioned_v1 (model4_board_v1)) -- gap +6.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD

## Linda Fruhvirtova vs Liudmila Samsonova -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214643:222258:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Linda Fruhvirtova (`KXWTAMATCH-26OCT01FRUSAM-FRU`) | 0.19 / 0.22 (150) | 20.5% | -- | 43.7% | 39.6% [28.0%-43.7%] | 22.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +19.1 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Liudmila Samsonova (`KXWTAMATCH-26OCT01FRUSAM-SAM`) | 0.77 / 0.80 (150) | 78.5% | -- | 56.3% | 60.4% [56.3%-72.0%] | 77.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -18.1 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4353.0, B 3968.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0785
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT01FRUSAM-FRU  (YES = Linda Fruhvirtova)
Model: 40%
Kalshi: 20%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.040, surface_pool_high +0.041, surface_dev_loose +0.021, surface_dev_tight -0.020
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01FRUSAM-21` Over 20.5 games: 0.42/0.49 mid 45.5%, model 59.1% (market_conditioned_v1 (model4_board_v1)) -- gap +13.6 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01FRUSAM-26` Over 25.5 games: 0.21/0.28 mid 24.5%, model 36.8% (market_conditioned_v1 (model4_board_v1)) -- gap +12.3 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01FRUSAM-16` Over 15.5 games: 0.84/0.91 mid 87.5%, model 94.9% (market_conditioned_v1 (model4_board_v1)) -- gap +7.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Viktorija Golubic vs Peyton Stearns -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:203530:220548:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Viktorija Golubic (`KXWTAMATCH-26OCT01GOLSTE-GOL`) | 0.38 / 0.40 (133) | 39.0% | -- | 45.8% | 47.4% [46.8%-48.4%] | 39.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +8.4 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Peyton Stearns (`KXWTAMATCH-26OCT01GOLSTE-STE`) | 0.59 / 0.62 (440) | 60.5% | -- | 54.2% | 52.6% [51.6%-53.2%] | 60.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.9 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4714.0, B 4027.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0079
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.011, surface_dev_loose +0.000, surface_dev_tight -0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01GOLSTE-21` Over 20.5 games: 0.47/0.60 mid 53.5%, model 66.6% (market_conditioned_v1 (model4_board_v1)) -- gap +13.1 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01GOLSTE-26` Over 25.5 games: 0.27/0.35 mid 31.0%, model 43.5% (market_conditioned_v1 (model4_board_v1)) -- gap +12.5 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01GOLSTE-16` Over 15.5 games: 0.88/0.97 mid 92.5%, model 96.9% (market_conditioned_v1 (model4_board_v1)) -- gap +4.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ashlyn Krueger vs Ann Li -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215983:221909:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ann Li (`KXWTAMATCH-26OCT01KRUANN-ANN`) | 0.08 / 0.90 (15) | 49.0% | -- | 63.7% | 60.2% [55.7%-61.7%] | -- | -- | -- | -- | PASS | +11.2 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ashlyn Krueger (`KXWTAMATCH-26OCT01KRUANN-KRU`) | 0.09 / 0.89 (33) | 49.0% | -- | 36.3% | 39.8% [38.3%-44.3%] | -- | -- | -- | -- | PASS | -9.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4211.0, B 4567.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0301
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose -0.010, surface_dev_tight +0.010
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Karolina Muchova vs Katie Boulter -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211107:214096:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katie Boulter (`KXWTAMATCH-26OCT01MUCBOU-BOU`) | 0.11 / 0.13 (777) | 12.0% | -- | 24.1% | 22.9% [22.1%-23.7%] | 14.7% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +10.9 pp | REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Karolina Muchova (`KXWTAMATCH-26OCT01MUCBOU-MUC`) | 0.86 / 0.88 (471) | 87.0% | -- | 75.9% | 77.1% [76.3%-77.9%] | 85.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.9 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3972.0, B 3928.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0078
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high +0.000, surface_dev_loose +0.008, surface_dev_tight -0.008
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 2 carry a model probability
  * `KXWTAGTOTAL-26OCT01MUCBOU-19` Over 18.5 games: 0.42/0.50 mid 46.0%, model 68.7% (market_conditioned_v1 (model4_board_v1)) -- gap +22.7 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01MUCBOU-24` Over 23.5 games: 0.17/0.32 mid 24.5%, model 36.5% (market_conditioned_v1 (model4_board_v1)) -- gap +12.0 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD

## Linda Noskova vs Elena-Gabriela Ruse -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211817:222328:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Linda Noskova (`KXWTAMATCH-26OCT01NOSRUS-NOS`) | 0.76 / 0.79 (81) | 77.5% | -- | 64.5% | 67.8% [66.9%-70.5%] | 76.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.7 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elena-Gabriela Ruse (`KXWTAMATCH-26OCT01NOSRUS-RUS`) | 0.20 / 0.23 (604) | 21.5% | -- | 35.5% | 32.2% [29.5%-33.1%] | 23.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +10.7 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4568.0, B 4254.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0182
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.018, surface_dev_loose +0.009, surface_dev_tight -0.004
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01NOSRUS-21` Over 20.5 games: 0.43/0.51 mid 47.0%, model 63.1% (market_conditioned_v1 (model4_board_v1)) -- gap +16.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01NOSRUS-26` Over 25.5 games: 0.21/0.29 mid 25.0%, model 39.9% (market_conditioned_v1 (model4_board_v1)) -- gap +14.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01NOSRUS-16` Over 15.5 games: 0.87/0.94 mid 90.5%, model 96.9% (market_conditioned_v1 (model4_board_v1)) -- gap +6.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jasmine Paolini vs Daria Snigur -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211148:220750:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jasmine Paolini (`KXWTAMATCH-26OCT01PAOSNI-PAO`) | 0.61 / 0.63 (0) | 62.0% | -- | 23.2% | 33.5% [27.4%-53.7%] | 61.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -28.5 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daria Snigur (`KXWTAMATCH-26OCT01PAOSNI-SNI`) | 0.38 / 0.39 (163) | 38.5% | -- | 76.8% | 66.5% [46.3%-72.6%] | 38.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +28.0 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4852.0, B 4190.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.1314
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT01PAOSNI-SNI  (YES = Daria Snigur)
Model: 67%
Kalshi: 38%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.019, surface_dev_loose -0.024, surface_dev_tight +0.029
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01PAOSNI-22` Over 21.5 games: 0.45/0.52 mid 48.5%, model 60.9% (market_conditioned_v1 (model4_board_v1)) -- gap +12.4 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01PAOSNI-27` Over 26.5 games: 0.22/0.30 mid 26.0%, model 37.8% (market_conditioned_v1 (model4_board_v1)) -- gap +11.8 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01PAOSNI-17` Over 16.5 games: 0.80/0.89 mid 84.5%, model 92.5% (market_conditioned_v1 (model4_board_v1)) -- gap +8.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Anastasia Potapova vs Sinja Kraus -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215713:221257:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sinja Kraus (`KXWTAMATCH-26OCT01POTKRA-KRA`) | 0.25 / 0.26 (13) | 25.5% | -- | 54.2% | 45.8% [35.5%-49.5%] | 27.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +20.3 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anastasia Potapova (`KXWTAMATCH-26OCT01POTKRA-POT`) | 0.71 / 0.75 (1938) | 73.0% | -- | 45.8% | 54.2% [50.5%-64.5%] | 72.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -18.8 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4594.0, B 5054.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.07
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT01POTKRA-KRA  (YES = Sinja Kraus)
Model: 46%
Kalshi: 26%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.016
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01POTKRA-15` Over 14.5 games: 0.02/0.99 mid 50.5%, model 98.2% (market_conditioned_v1 (model4_board_v1)) -- gap +47.7 pp, EXTREME, DATA_WARNING, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01POTKRA-20` Over 19.5 games: 0.49/0.57 mid 53.0%, model 67.8% (market_conditioned_v1 (model4_board_v1)) -- gap +14.8 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01POTKRA-25` Over 24.5 games: 0.27/0.35 mid 31.0%, model 42.9% (market_conditioned_v1 (model4_board_v1)) -- gap +11.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD

## Taylah Preston vs Diane Parry -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:220348:223194:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diane Parry (`KXWTAMATCH-26OCT01PREPAR-PAR`) | 0.58 / 0.61 (2987) | 59.5% | -- | 19.4% | 24.8% [19.7%-43.7%] | 59.4% | -- | 59.4% | MODEL_LONE_OUTLIER | PASS | -34.7 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Taylah Preston (`KXWTAMATCH-26OCT01PREPAR-PRE`) | 0.38 / 0.41 (150) | 39.5% | -- | 80.7% | 75.2% [56.3%-80.3%] | 40.6% | -- | 40.6% | MODEL_LONE_OUTLIER | WATCH | +35.7 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5098.0, B 3742.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.1199
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT01PREPAR-PRE  (YES = Taylah Preston)
Model: 75%
Kalshi: 40%
Gap: +36 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.043, surface_pool_high +0.040, surface_dev_loose +0.012, surface_dev_tight -0.012
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01PREPAR-28` Over 27.5 games: 0.19/0.27 mid 23.0%, model 34.9% (market_conditioned_v1 (model4_board_v1)) -- gap +11.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01PREPAR-23` Over 22.5 games: 0.39/0.54 mid 46.5%, model 56.1% (market_conditioned_v1 (model4_board_v1)) -- gap +9.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01PREPAR-18` Over 17.5 games: 0.78/0.84 mid 81.0%, model 88.5% (market_conditioned_v1 (model4_board_v1)) -- gap +7.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Clara Tauson vs Polina Kudermetova -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:220704:221236:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Kudermetova (`KXWTAMATCH-26OCT01TAUKUD-KUD`) | 0.31 / 0.34 (732) | 32.5% | -- | 32.9% | 34.3% [32.4%-40.2%] | 33.6% | -- | 33.6% | MODEL_LONE_OUTLIER | PASS | +1.8 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Clara Tauson (`KXWTAMATCH-26OCT01TAUKUD-TAU`) | 0.66 / 0.69 (2100) | 67.5% | -- | 67.1% | 65.7% [59.8%-67.6%] | 66.4% | -- | 66.4% | MODEL_LONE_OUTLIER | PASS | -1.8 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4452.0, B 4285.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0386
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.009, surface_dev_loose -0.000, surface_dev_tight +0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01TAUKUD-26` Over 25.5 games: 0.25/0.33 mid 29.0%, model 43.6% (market_conditioned_v1 (model4_board_v1)) -- gap +14.6 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01TAUKUD-21` Over 20.5 games: 0.50/0.55 mid 52.5%, model 66.8% (market_conditioned_v1 (model4_board_v1)) -- gap +14.3 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01TAUKUD-16` Over 15.5 games: 0.88/0.97 mid 92.5%, model 97.4% (market_conditioned_v1 (model4_board_v1)) -- gap +4.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; WIDE_SPREAD

## Maria Timofeeva vs Naomi Osaka -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211768:221237:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naomi Osaka (`KXWTAMATCH-26OCT01TIMOSA-OSA`) | 0.77 / 0.81 (1764) | 79.0% | -- | 76.0% | 80.3% [78.0%-81.7%] | 76.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Timofeeva (`KXWTAMATCH-26OCT01TIMOSA-TIM`) | 0.20 / 0.21 (163) | 20.5% | -- | 24.0% | 19.7% [18.3%-22.0%] | 23.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.8 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3737.0, B 2986.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0182
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.004, surface_dev_loose -0.004, surface_dev_tight +0.004
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01TIMOSA-21` Over 20.5 games: 0.41/0.47 mid 44.0%, model 59.4% (market_conditioned_v1 (model4_board_v1)) -- gap +15.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01TIMOSA-26` Over 25.5 games: 0.20/0.27 mid 23.5%, model 36.9% (market_conditioned_v1 (model4_board_v1)) -- gap +13.4 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01TIMOSA-16` Over 15.5 games: 0.87/0.91 mid 89.0%, model 95.3% (market_conditioned_v1 (model4_board_v1)) -- gap +6.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD

## Janice Tjen vs Diana Shnaider -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:222145:223670:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diana Shnaider (`KXWTAMATCH-26OCT01TJESHN-SHN`) | 0.73 / 0.74 (828) | 73.5% | -- | 42.4% | 47.4% [42.4%-63.2%] | 70.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -26.1 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Janice Tjen (`KXWTAMATCH-26OCT01TJESHN-TJE`) | 0.26 / 0.27 (149) | 26.5% | -- | 57.6% | 52.5% [36.8%-57.6%] | 29.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +26.1 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3631.0, B 4846.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.1039
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT01TJESHN-TJE  (YES = Janice Tjen)
Model: 53%
Kalshi: 26%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.041, surface_pool_high +0.041, surface_dev_loose -0.000, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01TJESHN-21` Over 20.5 games: 0.46/0.53 mid 49.5%, model 66.0% (market_conditioned_v1 (model4_board_v1)) -- gap +16.5 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01TJESHN-26` Over 25.5 games: 0.23/0.31 mid 27.0%, model 42.4% (market_conditioned_v1 (model4_board_v1)) -- gap +15.4 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01TJESHN-16` Over 15.5 games: 0.85/0.93 mid 89.0%, model 97.5% (market_conditioned_v1 (model4_board_v1)) -- gap +8.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD

## Dayana Yastremska vs Maja Chwalinska -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215035:216081:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maja Chwalinska (`KXWTAMATCH-26OCT01YASCHW-CHW`) | 0.64 / 0.65 (155159) | 64.5% | -- | 81.1% | 72.6% [59.0%-77.3%] | 65.2% | -- | 65.2% | MODEL_LONE_OUTLIER | WATCH | +8.1 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Dayana Yastremska (`KXWTAMATCH-26OCT01YASCHW-YAS`) | 0.34 / 0.35 (1035) | 34.5% | -- | 18.9% | 27.4% [22.7%-41.0%] | 34.8% | -- | 34.8% | MARKETS_AGREE | PASS | -7.1 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4632.0, B 3543.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0914
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose -0.022, surface_dev_tight +0.027
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01YASCHW-27` Over 26.5 games: 0.21/0.28 mid 24.5%, model 36.8% (market_conditioned_v1 (model4_board_v1)) -- gap +12.3 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01YASCHW-22` Over 21.5 games: 0.41/0.54 mid 47.5%, model 59.8% (market_conditioned_v1 (model4_board_v1)) -- gap +12.3 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01YASCHW-17` Over 16.5 games: 0.80/0.88 mid 84.0%, model 91.9% (market_conditioned_v1 (model4_board_v1)) -- gap +7.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; WIDE_SPREAD

## Yue Yuan vs Mirra Andreeva -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:206294:259799:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mirra Andreeva (`KXWTAMATCH-26OCT01YUAAND-AND`) | 0.90 / 0.91 (2166) | 90.5% | -- | 89.4% | 87.9% [85.1%-88.9%] | 89.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.6 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yue Yuan (`KXWTAMATCH-26OCT01YUAAND-YUA`) | 0.08 / 0.09 (622) | 8.5% | -- | 10.6% | 12.1% [11.1%-14.9%] | 10.9% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +3.6 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4806.0, B 4895.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0192
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.014, surface_dev_loose -0.005, surface_dev_tight +0.008
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 2 carry a model probability
  * `KXWTAGTOTAL-26OCT01YUAAND-19` Over 18.5 games: 0.37/0.43 mid 40.0%, model 61.3% (market_conditioned_v1 (model4_board_v1)) -- gap +21.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01YUAAND-24` Over 23.5 games: 0.11/0.26 mid 18.5%, model 30.9% (market_conditioned_v1 (model4_board_v1)) -- gap +12.4 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Renata Zarazua vs Aryna Sabalenka -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213887:214544:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aryna Sabalenka (`KXWTAMATCH-26OCT01ZARSAB-SAB`) | 0.93 / 0.94 (961) | 93.5% | -- | 95.1% | 95.1% [94.4%-95.5%] | 94.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +1.6 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Renata Zarazua (`KXWTAMATCH-26OCT01ZARSAB-ZAR`) | 0.05 / 0.06 (1530) | 5.5% | -- | 4.9% | 4.9% [4.5%-5.6%] | 6.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.6 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4923.0, B 5768.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0057
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.003, surface_dev_loose -0.002, surface_dev_tight +0.002
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 2 carry a model probability
  * `KXWTAGTOTAL-26OCT01ZARSAB-17` Over 16.5 games: 0.45/0.51 mid 48.0%, model 79.8% (market_conditioned_v1 (model4_board_v1)) -- gap +31.8 pp, EXTREME, DATA_WARNING, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01ZARSAB-22` Over 21.5 games: 0.09/0.24 mid 16.5%, model 35.2% (market_conditioned_v1 (model4_board_v1)) -- gap +18.7 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data LIMITED
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
