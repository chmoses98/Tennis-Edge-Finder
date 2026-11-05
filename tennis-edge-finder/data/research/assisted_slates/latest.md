# ASSISTED SLATE -- 2026-11-05T14:36Z (`SL-20261105T143627Z-2065c219`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

254 open matches not seen started, 618 markets. Skipped: {"first_ball_already_observed": 3, "scheduled_start_over_24h_past": 6}. Sources: shadow board 2026-11-05T14:16:22.551131+00:00, Model 4 2026-11-05T14:17:11.939665+00:00, Gen-1 ledger 2026-11-05T14:16:18.544651+00:00, external 2026-11-05T13:45:33.623494+00:00, capture 20261105T134337Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-11-05 18:00Z**
* Recommended RUN TENNIS time: **2026-11-05 17:15Z**
* Final price/status check time: **2026-11-05 17:50Z**
* Number of matches in window: 2 (Arthur Fils vs Taylor Fritz, Jan-Lennard Struff vs Casper Ruud)

* **4 main-tour match(es) have NO verified start status** (STATUS_AMBIGUOUS): BET blocked until a live status check.

Slate built 2026-11-05T14:36Z. Refresh due by: 2026-11-05 17:15Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 30, "HIGH_REVIEW": 55, "NORMAL": 261, "REVIEW": 49, "UNPRICED": 223}; match winners: {"EXTREME": 29, "HIGH_REVIEW": 52, "NORMAL": 166, "REVIEW": 44, "UNPRICED": 217}; quote freshness at build: {"STALE": 395}.

## Jodie Burrage / Robin Montgomery vs Vaishnavi Adkar / Rutuja Bhosale -- WTA Chennai QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-05 13:28Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-06T05:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-05T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05BURMONADKBHO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vaishnavi Adkar / Rutuja Bhosale (`KXWTADOUBLES-26NOV05BURMONADKBHO-ADKBHO`) | 0.18 / 0.22 (2040) | 20.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jodie Burrage / Robin Montgomery (`KXWTADOUBLES-26NOV05BURMONADKBHO-BURMON`) | 0.78 / 0.82 (326) | 80.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Sorana Cirstea vs Mary Stoiana -- WTA Hong Kong R16

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-11-05 09:00Z
* Current expected start: 2026-11-05 13:25Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-05 13:28Z
* Recommended handicap-by time: 2026-11-05 12:40Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+265_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA (TOUR_500_250) · Hard · scheduled 2026-11-05T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:201514:223168:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sorana Cirstea (`KXWTAMATCH-26NOV05CIRSTO-CIR`) | 0.60 / 0.65 (10) | 62.5% | 68.7% | 84.2% | 80.9% [77.2%-82.3%] | -- | 76.4% | 76.4% | MARKETS_AGREE | SHADOW_BET | +6.2 pp | NORMAL | STALE | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Mary Stoiana (`KXWTAMATCH-26NOV05CIRSTO-STO`) | 0.36 / 0.40 (87) | 38.0% | 31.3% | 15.8% | 19.1% [17.7%-22.8%] | -- | 23.6% | 23.6% | MARKETS_AGREE | PASS | -6.7 pp | NORMAL | STALE | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 4410.0, B 2840.0; serve-point win A 60.6%, B 43.2%; Elo A 2008.5, B 1825.3; model uncertainty 0.0251
* Form inputs: days since last match A 2, B 3; matches on record A 1065, B 146; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.004, surface_dev_loose +0.006, surface_dev_tight -0.007
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTASETWINNER-26NOV05CIRSTO-1-CIR` Will Sorana Cirstea win set 1 in the Sorana Cirstea vs Mary Stoiana match: 0.38/0.39 mid 38.5%, model 62.7% (projection_v2.0 (prediction ledger)) -- gap +24.2 pp, HIGH_REVIEW, DATA_WARNING, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV05CIRSTO-1-STO` Will Mary Stoiana win set 1 in the Sorana Cirstea vs Mary Stoiana match: 0.61/0.62 mid 61.5%, model 37.3% (projection_v2.0 (prediction ledger)) -- gap -24.2 pp, HIGH_REVIEW, DATA_WARNING, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26NOV05CIRSTO-15` Over 14.5 games: 0.72/0.97 mid 84.5%, model 99.1% (projection_v2.0 (prediction ledger)) -- gap +14.6 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV05CIRSTO-20` Over 19.5 games: 0.68/0.69 mid 68.5%, model 72.8% (projection_v2.0 (prediction ledger)) -- gap +4.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV05CIRSTO-25` Over 24.5 games: 0.43/0.45 mid 44.0%, model 47.0% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV05CIRSTO-2-STO` Will Mary Stoiana win set 2 in the Sorana Cirstea vs Mary Stoiana match: 0.35/0.38 mid 36.5%, model 37.3% (projection_v2.0 (prediction ledger)) -- gap +0.8 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV05CIRSTO-2-CIR` Will Sorana Cirstea win set 2 in the Sorana Cirstea vs Mary Stoiana match: 0.62/0.64 mid 63.0%, model 62.7% (projection_v2.0 (prediction ledger)) -- gap -0.3 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Rinky Hijikata vs Tomas Martin Etcheverry -- ATP Paris R16

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-11-05 13:00Z
* Current expected start: 2026-11-05 13:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-05 13:28Z
* Recommended handicap-by time: 2026-11-05 12:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+30_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (MASTERS_1000) · Hard · scheduled 2026-11-05T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144869:208014:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tomas Martin Etcheverry (`KXATPMATCH-26NOV05HIJETC-ETC`) | 0.57 / 0.58 (7271) | 57.5% | 53.1% | 66.7% | 62.1% [57.9%-64.9%] | -- | 57.7% | 57.7% | MODEL_LONE_OUTLIER | WATCH | -4.4 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Rinky Hijikata (`KXATPMATCH-26NOV05HIJETC-HIJ`) | 0.42 / 0.43 (20809) | 42.5% | 46.9% | 33.3% | 37.9% [35.1%-42.1%] | -- | 42.2% | 42.2% | MODEL_LONE_OUTLIER | PASS | +4.4 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5968.0, B 5577.0; serve-point win A 64.5%, B 34.8%; Elo A 1822.5, B 1775.7; model uncertainty 0.0352
* Form inputs: days since last match A 3, B 2; matches on record A 469, B 650; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.004, surface_dev_tight -0.001
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV05HIJETC-24` Over 23.5 games: 0.47/0.48 mid 47.5%, model 55.5% (projection_v2.0 (prediction ledger)) -- gap +8.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05HIJETC-ETC20` Will Tomas Martin Etcheverry win the Rinky Hijikata vs Tomas Martin Etcheverry match by a set score of 2-0?: 0.34/0.36 mid 35.0%, model 27.1% (projection_v2.0 (prediction ledger)) -- gap -7.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV05HIJETC-1-ETC` Will Tomas Martin Etcheverry win set 1 in the Rinky Hijikata vs Tomas Martin Etcheverry match: 0.59/0.60 mid 59.5%, model 52.1% (projection_v2.0 (prediction ledger)) -- gap -7.4 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV05HIJETC-1-HIJ` Will Rinky Hijikata win set 1 in the Rinky Hijikata vs Tomas Martin Etcheverry match: 0.40/0.41 mid 40.5%, model 47.9% (projection_v2.0 (prediction ledger)) -- gap +7.4 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV05HIJETC-19` Over 18.5 games: 0.79/0.88 mid 83.5%, model 89.8% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05HIJETC-HIJ21` Will Rinky Hijikata win the Rinky Hijikata vs Tomas Martin Etcheverry match by a set score of 2-1?: 0.16/0.20 mid 18.0%, model 23.9% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV05HIJETC-ETC2` Will Tomas Martin Etcheverry win at least 1.5 more games than Rinky Hijikata?: 0.49/0.52 mid 50.5%, model 44.9% (projection_v2.0 (prediction ledger)) -- gap -5.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV05HIJETC-29` Over 28.5 games: 0.29/0.36 mid 32.5%, model 37.7% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV05HIJETC-2-HIJ` Will Rinky Hijikata win set 2 in the Rinky Hijikata vs Tomas Martin Etcheverry match: 0.42/0.44 mid 43.0%, model 47.9% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05HIJETC-ETC21` Will Tomas Martin Etcheverry win the Rinky Hijikata vs Tomas Martin Etcheverry match by a set score of 2-1?: 0.21/0.23 mid 22.0%, model 26.0% (projection_v2.0 (prediction ledger)) -- gap +4.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV05HIJETC-2-ETC` Will Tomas Martin Etcheverry win set 2 in the Rinky Hijikata vs Tomas Martin Etcheverry match: 0.55/0.57 mid 56.0%, model 52.1% (projection_v2.0 (prediction ledger)) -- gap -3.9 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV05HIJETC-ETC5` Will Tomas Martin Etcheverry win at least 4.5 more games than Rinky Hijikata?: 0.13/0.25 mid 19.0%, model 16.5% (projection_v2.0 (prediction ledger)) -- gap -2.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05HIJETC-HIJ20` Will Rinky Hijikata win the Rinky Hijikata vs Tomas Martin Etcheverry match by a set score of 2-0?: 0.23/0.27 mid 25.0%, model 22.9% (projection_v2.0 (prediction ledger)) -- gap -2.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV05HIJETC-HIJ2` Will Rinky Hijikata win at least 1.5 more games than Tomas Martin Etcheverry?: 0.35/0.46 mid 40.5%, model 39.7% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Madhurima Sawant vs Noma Noha Akugue -- WTA 125K Luanda R16

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-11-05 14:20Z
* Current expected start: 2026-11-05 13:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-05 13:28Z
* Recommended handicap-by time: 2026-11-05 12:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA125 (WTA_125) · Hard · scheduled 2026-11-05T14:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:223333:261129:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Noma Noha Akugue (`KXWTACHALLENGERMATCH-26NOV05SAWNOH-NOH`) | 0.96 / 0.97 (8345) | 96.5% | 98.1% | 99.1% | 96.7% [93.8%-97.9%] | -- | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.6 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Madhurima Sawant (`KXWTACHALLENGERMATCH-26NOV05SAWNOH-SAW`) | 0.03 / 0.04 (7893) | 3.5% | 1.9% | 0.9% | 3.4% [2.1%-6.2%] | -- | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.6 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1045.0, B 4975.0; serve-point win A 49.3%, B 34.8%; Elo A 1212.8, B 1660.5; model uncertainty 0.0202
* Form inputs: days since last match A 2, B 1; matches on record A 71, B 351; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.011, surface_dev_loose -0.006, surface_dev_tight +0.007
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; NO_EXTERNAL_PRICE; STALE_QUOTE

## Kilian Feldbausch vs Remy Bertola -- ATP Challenger Taranto R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 13:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-05T13:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200329:210005:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Remy Bertola (`KXATPCHALLENGERMATCH-26NOV05FELBER-BER`) | 0.52 / 0.53 (24477) | 52.5% | 44.2% | 30.0% | 37.7% [33.3%-43.3%] | 50.0% | -- | 50.0% | MODEL_LONE_OUTLIER | PASS | -8.3 pp | NORMAL | STALE | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Kilian Feldbausch (`KXATPCHALLENGERMATCH-26NOV05FELBER-FEL`) | 0.47 / 0.48 (18371) | 47.5% | 55.8% | 70.0% | 62.3% [56.7%-66.7%] | 50.0% | -- | 50.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +8.3 pp | NORMAL | STALE | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3610.0, B 4817.0; serve-point win A 59.0%, B 42.1%; Elo A 1692.9, B 1737.5; model uncertainty 0.05
* Form inputs: days since last match A 10, B 8; matches on record A 190, B 472; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STALE_QUOTE

## Maxim Mrva vs Thomas Faurel -- ATP Challenger Taranto R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 13:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-05T13:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211617:212225:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thomas Faurel (`KXATPCHALLENGERMATCH-26NOV05MRVFAU-FAU`) | 0.17 / 0.29 (33) | 23.0% | 41.3% | 58.4% | 50.5% [45.3%-54.2%] | -- | 35.4% | 35.4% | MODEL_LONE_OUTLIER | PASS | +18.3 pp | HIGH_REVIEW | STALE | A / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Maxim Mrva (`KXATPCHALLENGERMATCH-26NOV05MRVFAU-MRV`) | 0.72 / 0.80 (30) | 76.0% | 58.7% | 41.6% | 49.5% [45.8%-54.7%] | -- | 64.1% | 64.1% | MODEL_LONE_OUTLIER | PASS | -17.3 pp | HIGH_REVIEW | STALE | A / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 4552.0, B 3705.0; serve-point win A 57.1%, B 44.5%; Elo A 1726.6, B 1599.4; model uncertainty 0.0448
* Form inputs: days since last match A 17, B 38; matches on record A 144, B 130; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV05MRVFAU-FAU  (YES = Thomas Faurel)
Model: 41%
Kalshi: 23%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: SUPPORTS_MODEL_DIRECTION
Data quality: A (LIMITED)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LEVEL_TRANSFER_RISK, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, SCHEDULED_START_PASSED, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STALE_QUOTE; WIDE_SPREAD

## Sumit Nagal vs Hugo Grenier -- ATP Challenger Taranto R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 13:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-05T13:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111576:126409:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Grenier (`KXATPCHALLENGERMATCH-26NOV05NAGGRE-GRE`) | 0.26 / 0.30 (101) | 28.0% | 43.9% | 44.9% | 44.9% [44.4%-44.9%] | -- | 50.3% | 50.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +15.9 pp | HIGH_REVIEW | STALE | A / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Sumit Nagal (`KXATPCHALLENGERMATCH-26NOV05NAGGRE-NAG`) | 0.70 / 0.73 (26) | 71.5% | 56.1% | 55.1% | 55.1% [55.1%-55.6%] | -- | 49.6% | 49.6% | MODEL_LONE_OUTLIER | PASS | -15.4 pp | HIGH_REVIEW | STALE | A / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 4831.0, B 4320.0; serve-point win A 60.8%, B 40.4%; Elo A 1709.1, B 1666.0; model uncertainty 0.0026
* Form inputs: days since last match A 17, B 10; matches on record A 659, B 793; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV05NAGGRE-GRE  (YES = Hugo Grenier)
Model: 44%
Kalshi: 28%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: SUPPORTS_MODEL_DIRECTION
Data quality: A (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LEVEL_TRANSFER_RISK, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STALE_QUOTE

## Lorenzo Musetti vs Luca Van Assche -- ATP Paris R16

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-11-05 13:00Z
* Current expected start: 2026-11-05 13:43Z
* Source: COURT_PROGRESSION: preceding match on Court Central in progress (set 3 of best-of-5); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-05 13:28Z
* Recommended handicap-by time: 2026-11-05 12:58Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+43_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (MASTERS_1000) · Hard · scheduled 2026-11-05T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207518:209414:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Musetti (`KXATPMATCH-26NOV05MUSVAN-MUS`) | 0.74 / 0.75 (106879) | 74.5% | 71.4% | 71.7% | 71.2% [69.5%-73.8%] | 74.5% | 74.4% | 74.4% | MARKETS_AGREE | PASS | -3.1 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Luca Van Assche (`KXATPMATCH-26NOV05MUSVAN-VAN`) | 0.26 / 0.27 (80795) | 26.5% | 28.6% | 28.3% | 28.7% [26.2%-30.5%] | 25.5% | 25.8% | 25.7% | MARKETS_AGREE | PASS | +2.1 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5227.0, B 6055.0; serve-point win A 64.0%, B 40.5%; Elo A 1959.7, B 1807.2; model uncertainty 0.0215
* Form inputs: days since last match A 3, B 3; matches on record A 491, B 395; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.018, surface_dev_loose +0.004, surface_dev_tight +0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26NOV05MUSVAN-MUS20` Will Lorenzo Musetti win the Lorenzo Musetti vs Luca Van Assche match by a set score of 2-0?: 0.48/0.49 mid 48.5%, model 41.8% (projection_v2.0 (prediction ledger)) -- gap -6.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05MUSVAN-MUS21` Will Lorenzo Musetti win the Lorenzo Musetti vs Luca Van Assche match by a set score of 2-1?: 0.23/0.24 mid 23.5%, model 29.5% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV05MUSVAN-23` Over 22.5 games: 0.48/0.50 mid 49.0%, model 54.7% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV05MUSVAN-28` Over 27.5 games: 0.28/0.32 mid 30.0%, model 35.0% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV05MUSVAN-MUS4` Will Lorenzo Musetti win at least 3.5 more games than Luca Van Assche?: 0.51/0.52 mid 51.5%, model 47.4% (projection_v2.0 (prediction ledger)) -- gap -4.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV05MUSVAN-2-MUS` Will Lorenzo Musetti win set 2 in the Lorenzo Musetti vs Luca Van Assche match: 0.66/0.71 mid 68.5%, model 64.6% (projection_v2.0 (prediction ledger)) -- gap -3.9 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV05MUSVAN-2-VAN` Will Luca Van Assche win set 2 in the Lorenzo Musetti vs Luca Van Assche match: 0.29/0.34 mid 31.5%, model 35.4% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05MUSVAN-VAN21` Will Luca Van Assche win the Lorenzo Musetti vs Luca Van Assche match by a set score of 2-1?: 0.11/0.14 mid 12.5%, model 16.2% (projection_v2.0 (prediction ledger)) -- gap +3.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV05MUSVAN-1-VAN` Will Luca Van Assche win set 1 in the Lorenzo Musetti vs Luca Van Assche match: 0.32/0.33 mid 32.5%, model 35.4% (projection_v2.0 (prediction ledger)) -- gap +2.9 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV05MUSVAN-MUS7` Will Lorenzo Musetti win at least 6.5 more games than Luca Van Assche?: 0.10/0.18 mid 14.0%, model 11.6% (projection_v2.0 (prediction ledger)) -- gap -2.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV05MUSVAN-1-MUS` Will Lorenzo Musetti win set 1 in the Lorenzo Musetti vs Luca Van Assche match: 0.66/0.68 mid 67.0%, model 64.6% (projection_v2.0 (prediction ledger)) -- gap -2.4 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05MUSVAN-VAN20` Will Luca Van Assche win the Lorenzo Musetti vs Luca Van Assche match by a set score of 2-0?: 0.13/0.14 mid 13.5%, model 12.5% (projection_v2.0 (prediction ledger)) -- gap -1.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV05MUSVAN-18` Over 17.5 games: 0.88/0.89 mid 88.5%, model 89.4% (projection_v2.0 (prediction ledger)) -- gap +0.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV05MUSVAN-VAN2` Will Luca Van Assche win at least 1.5 more games than Lorenzo Musetti?: 0.21/0.25 mid 23.0%, model 22.7% (projection_v2.0 (prediction ledger)) -- gap -0.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alam / Eichenseher vs Bessonov / Kharlamov -- M15 Fergana QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05ALAEICBESKHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alam / Eichenseher (`KXITFDOUBLES-26NOV05ALAEICBESKHA-ALAEIC`) | 0.26 / 0.79 (2) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bessonov / Kharlamov (`KXITFDOUBLES-26NOV05ALAEICBESKHA-BESKHA`) | 0.16 / 0.69 (1) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Arcon / Dolzhenkov vs Hrazdil / Lakshmanan -- M15 Fergana QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05ARCDOLHRALAK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arcon / Dolzhenkov (`KXITFDOUBLES-26NOV05ARCDOLHRALAK-ARCDOL`) | 0.04 / 0.69 (1) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hrazdil / Lakshmanan (`KXITFDOUBLES-26NOV05ARCDOLHRALAK-HRALAK`) | 0.26 / 0.95 (4) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Joelle Lilly Sophie Steur vs Lucie Nguyen Tan -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221259:221468:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucie Nguyen Tan (`KXITFWMATCH-26NOV05STENGU-NGU`) | 0.04 / 0.05 (5495) | 4.5% | 31.6% | 31.0% | 31.5% [30.5%-34.4%] | 24.7% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +27.1 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Joelle Lilly Sophie Steur (`KXITFWMATCH-26NOV05STENGU-STE`) | 0.95 / 0.96 (16981) | 95.5% | 68.4% | 69.0% | 68.5% [65.6%-69.5%] | 75.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -27.1 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2592.0, B 1887.0; serve-point win A 54.1%, B 49.5%; Elo A 1564.8, B 1438.0; model uncertainty 0.0194
* Form inputs: days since last match A 21, B 21; matches on record A 223, B 293; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05STENGU-NGU  (YES = Lucie Nguyen Tan)
Model: 32%
Kalshi: 4%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nuno Borges vs Ignacio Buse -- ATP Paris R16

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-11-05 13:00Z
* Current expected start: 2026-11-05 14:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-05 13:28Z
* Recommended handicap-by time: 2026-11-05 13:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+90_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (MASTERS_1000) · Hard · scheduled 2026-11-05T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:132686:209860:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nuno Borges (`KXATPMATCH-26NOV05BORBUS-BOR`) | 0.61 / 0.62 (9289) | 61.5% | 61.6% | 61.9% | 62.3% [61.4%-62.3%] | 60.9% | 61.6% | 61.6% | MARKETS_AGREE | PASS | +0.1 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Ignacio Buse (`KXATPMATCH-26NOV05BORBUS-BUS`) | 0.38 / 0.39 (60084) | 38.5% | 38.4% | 38.1% | 37.7% [37.7%-38.6%] | 39.1% | 38.5% | 38.5% | MARKETS_AGREE | PASS | -0.1 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5796.0, B 5542.0; serve-point win A 64.4%, B 38.0%; Elo A 1865.0, B 1763.6; model uncertainty 0.0048
* Form inputs: days since last match A 2, B 3; matches on record A 556, B 288; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV05BORBUS-25` Over 24.5 games: 0.44/0.45 mid 44.5%, model 52.2% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05BORBUS-BOR21` Will Nuno Borges win the Nuno Borges vs Ignacio Buse match by a set score of 2-1?: 0.21/0.23 mid 22.0%, model 28.2% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV05BORBUS-30` Over 29.5 games: 0.24/0.26 mid 25.0%, model 29.8% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05BORBUS-BOR20` Will Nuno Borges win the Nuno Borges vs Ignacio Buse match by a set score of 2-0?: 0.37/0.38 mid 37.5%, model 33.4% (projection_v2.0 (prediction ledger)) -- gap -4.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05BORBUS-BUS21` Will Ignacio Buse win the Nuno Borges vs Ignacio Buse match by a set score of 2-1?: 0.15/0.18 mid 16.5%, model 20.6% (projection_v2.0 (prediction ledger)) -- gap +4.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV05BORBUS-20` Over 19.5 games: 0.74/0.78 mid 76.0%, model 79.8% (projection_v2.0 (prediction ledger)) -- gap +3.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV05BORBUS-BOR5` Will Nuno Borges win at least 4.5 more games than Ignacio Buse?: 0.25/0.29 mid 27.0%, model 23.2% (projection_v2.0 (prediction ledger)) -- gap -3.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05BORBUS-BUS20` Will Ignacio Buse win the Nuno Borges vs Ignacio Buse match by a set score of 2-0?: 0.20/0.23 mid 21.5%, model 17.8% (projection_v2.0 (prediction ledger)) -- gap -3.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV05BORBUS-BOR2` Will Nuno Borges win at least 1.5 more games than Ignacio Buse?: 0.54/0.56 mid 55.0%, model 53.2% (projection_v2.0 (prediction ledger)) -- gap -1.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV05BORBUS-2-BUS` Will Ignacio Buse win set 2 in the Nuno Borges vs Ignacio Buse match: 0.39/0.42 mid 40.5%, model 42.2% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV05BORBUS-1-BOR` Will Nuno Borges win set 1 in the Nuno Borges vs Ignacio Buse match: 0.56/0.58 mid 57.0%, model 57.8% (projection_v2.0 (prediction ledger)) -- gap +0.8 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV05BORBUS-BUS2` Will Ignacio Buse win at least 1.5 more games than Nuno Borges?: 0.32/0.34 mid 33.0%, model 32.5% (projection_v2.0 (prediction ledger)) -- gap -0.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV05BORBUS-1-BUS` Will Ignacio Buse win set 1 in the Nuno Borges vs Ignacio Buse match: 0.42/0.43 mid 42.5%, model 42.2% (projection_v2.0 (prediction ledger)) -- gap -0.3 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV05BORBUS-2-BOR` Will Nuno Borges win set 2 in the Nuno Borges vs Ignacio Buse match: 0.56/0.60 mid 58.0%, model 57.8% (projection_v2.0 (prediction ledger)) -- gap -0.2 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Philip Henning vs Carlo Alberto Caniato -- ATP Challenger Taranto R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:50Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-05T14:50:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202475:212241:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlo Alberto Caniato (`KXATPCHALLENGERMATCH-26NOV05HENCAN-CAN`) | 0.51 / 0.52 (13936) | 51.5% | 54.0% | 46.5% | 45.6% [45.6%-46.1%] | -- | 49.3% | 49.3% | KALSHI_LONE_OUTLIER | PASS | +2.5 pp | NORMAL | STALE | A / LIMITED | ALL_AGREE | VERIFIED |
| Philip Henning (`KXATPCHALLENGERMATCH-26NOV05HENCAN-HEN`) | 0.49 / 0.50 (3561) | 49.5% | 46.0% | 53.5% | 54.4% [53.9%-54.4%] | -- | 50.5% | 50.5% | MODEL_LONE_OUTLIER | SHADOW_BET | -3.5 pp | NORMAL | STALE | A / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3868.0, B 3539.0; serve-point win A 64.2%, B 35.0%; Elo A 1580.2, B 1542.3; model uncertainty 0.0025
* Form inputs: days since last match A 24, B 17; matches on record A 215, B 154; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Benjamin Kittay / Takeru Yuzuki vs James Hopper / Mark Whitehouse -- ATP Challenger Taranto QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:50Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-05T14:50:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05KITYUZHOPWHI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| James Hopper / Mark Whitehouse (`KXATPCHALLENGERDOUBLES-26NOV05KITYUZHOPWHI-HOPWHI`) | 0.07 / 0.92 (1) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Benjamin Kittay / Takeru Yuzuki (`KXATPCHALLENGERDOUBLES-26NOV05KITYUZHOPWHI-KITYUZ`) | 0.07 / 0.94 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Piotr Pawlak / Marcus Walters vs Ignasi Forcano Aparicio / Rafael Izquierdo Luque -- ATP Challenger Taranto QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 14:50Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-05T14:50:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05PAWWALFORIZQ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ignasi Forcano Aparicio / Rafael Izquierdo Luque (`KXATPCHALLENGERDOUBLES-26NOV05PAWWALFORIZQ-FORIZQ`) | 0.53 / 0.61 (10) | 57.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Piotr Pawlak / Marcus Walters (`KXATPCHALLENGERDOUBLES-26NOV05PAWWALFORIZQ-PAWWAL`) | 0.37 / 0.43 (44) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Momoko Kobori / Peangtarn Plipuech vs Naima Karamoko / Simona Waltert -- WTA Chennai QF

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-05 12:30Z
* Current expected start: 2026-11-05 15:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-05 13:28Z
* Recommended handicap-by time: 2026-11-05 14:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-05T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05KOBPLIKARWAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naima Karamoko / Simona Waltert (`KXWTADOUBLES-26NOV05KOBPLIKARWAL-KARWAL`) | 0.43 / 0.58 (3) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Momoko Kobori / Peangtarn Plipuech (`KXWTADOUBLES-26NOV05KOBPLIKARWAL-KOBPLI`) | 0.41 / 0.51 (3) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Izan Almazan Valiente (`KXITFMATCH-26NOV05ALMRAD-ALM`) | 0.54 / 0.59 (4) | 56.5% | 50.6% | 49.5% | 45.2% [44.2%-47.3%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.9 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Iliyan Radulov (`KXITFMATCH-26NOV05ALMRAD-RAD`) | 0.39 / 0.44 (122) | 41.5% | 49.4% | 50.5% | 54.8% [52.7%-55.8%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +7.9 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2749.0, B 2013.0; serve-point win A 55.0%, B 45.1%; Elo A 1455.6, B 1523.1; model uncertainty 0.0158
* Form inputs: days since last match A 17, B 45; matches on record A 79, B 147; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose -0.005, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
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
| Alberto Barroso Campos (`KXITFMATCH-26NOV05BARMAN-BAR`) | 0.33 / 0.35 (1) | 34.0% | 35.6% | 46.9% | 39.8% [35.4%-44.4%] | 36.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +1.6 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alejandro Manzanera Pertusa (`KXITFMATCH-26NOV05BARMAN-MAN`) | 0.63 / 0.66 (50) | 64.5% | 64.4% | 53.1% | 60.2% [55.6%-64.6%] | 63.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.1 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2471.0, B 1670.0; serve-point win A 58.7%, B 38.5%; Elo A 1325.2, B 1453.7; model uncertainty 0.0448
* Form inputs: days since last match A 38, B 199; matches on record A 365, B 190; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.045, surface_pool_high -0.044, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

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
| Duhan / Murtaza (`KXITFDOUBLES-26NOV05IGNSERDUHMUR-DUHMUR`) | 0.25 / 0.95 (4) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ignatov / Serazhetdinov (`KXITFDOUBLES-26NOV05IGNSERDUHMUR-IGNSER`) | 0.04 / 0.69 (1) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Yshai Oliel (`KXITFMATCH-26NOV05OLIPAR-OLI`) | 0.16 / 0.17 (5355) | 16.5% | 41.8% | 12.8% | 41.7% [28.3%-62.3%] | 36.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +25.3 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ignacio Parisca (`KXITFMATCH-26NOV05OLIPAR-PAR`) | 0.83 / 0.84 (169) | 83.5% | 58.2% | 87.2% | 58.3% [37.7%-71.7%] | 63.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -25.3 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 703.0, B 1927.0; serve-point win A 57.6%, B 40.8%; Elo A 1449.6, B 1383.1; model uncertainty 0.1701
* Form inputs: days since last match A 360, B 66; matches on record A 433, B 98; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV05OLIPAR-OLI  (YES = Yshai Oliel)
Model: 42%
Kalshi: 16%
Gap: +25 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.036, surface_pool_high -0.025, surface_dev_loose -0.010, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
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
| Miguel Damas (`KXITFMATCH-26NOV05TALDAM-DAM`) | 0.69 / 0.73 (9) | 71.0% | 88.2% | 86.1% | 86.4% [84.8%-87.8%] | 68.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +17.2 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luka Talan Lopatic (`KXITFMATCH-26NOV05TALDAM-TAL`) | 0.26 / 0.31 (516) | 28.5% | 11.8% | 13.9% | 13.6% [12.2%-15.2%] | 31.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -16.7 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 927.0, B 5219.0; serve-point win A 51.7%, B 39.3%; Elo A 1239.8, B 1566.6; model uncertainty 0.0147
* Form inputs: days since last match A 339, B 17; matches on record A 16, B 388; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV05TALDAM-DAM  (YES = Miguel Damas)
Model: 88%
Kalshi: 71%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.003, surface_pool_high +0.000, surface_dev_loose -0.008, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Angela Fita Boluda vs Loes Ebeling Koning -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214236:266901:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Loes Ebeling Koning (`KXITFWMATCH-26NOV05FITEBE-EBE`) | 0.50 / 0.51 (6816) | 50.5% | 27.3% | 25.2% | 30.0% [25.6%-34.7%] | 58.1% | -- | 58.1% | MODEL_LONE_OUTLIER | PASS | -23.2 pp | HIGH_REVIEW | STALE | B / LIMITED | ALL_DISAGREE | VERIFIED |
| Angela Fita Boluda (`KXITFWMATCH-26NOV05FITEBE-FIT`) | 0.49 / 0.50 (3690) | 49.5% | 72.7% | 74.8% | 70.0% [65.3%-74.4%] | 41.9% | -- | 41.9% | KALSHI_LONE_OUTLIER | WATCH | +23.2 pp | HIGH_REVIEW | STALE | B / LIMITED | ALL_DISAGREE | VERIFIED |

* Serve evidence (points): A 4603.0, B 1642.0; serve-point win A 60.2%, B 44.5%; Elo A 1544.4, B 1444.0; model uncertainty 0.0455
* Form inputs: days since last match A 51, B 24; matches on record A 483, B 87; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05FITEBE-FIT  (YES = Angela Fita Boluda)
Model: 73%
Kalshi: 50%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: ALL_DISAGREE
Data quality: B (LIMITED)
Reasons: STALE_KALSHI_QUOTE, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.044, surface_pool_high -0.047, surface_dev_loose +0.018, surface_dev_tight -0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carlota Martinez Cirez vs Nuria Brancaccio -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215572:220781:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nuria Brancaccio (`KXITFWMATCH-26NOV05MARBRA-BRA`) | 0.75 / 0.77 (50) | 76.0% | 71.7% | 70.9% | 67.1% [63.7%-70.0%] | 80.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carlota Martinez Cirez (`KXITFWMATCH-26NOV05MARBRA-MAR`) | 0.21 / 0.24 (115) | 22.5% | 28.3% | 29.1% | 32.9% [30.0%-36.3%] | 19.5% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +5.8 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3122.0, B 3905.0; serve-point win A 49.1%, B 46.6%; Elo A 1472.5, B 1536.3; model uncertainty 0.0316
* Form inputs: days since last match A 52, B 21; matches on record A 422, B 487; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.029, surface_pool_high +0.030, surface_dev_loose -0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Raluca Georgiana Serban vs Elena Ruxandra Bertea -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05SERBER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elena Ruxandra Bertea (`KXITFWMATCH-26NOV05SERBER-BER`) | 0.50 / 0.52 (5149) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Raluca Georgiana Serban (`KXITFWMATCH-26NOV05SERBER-SER`) | 0.48 / 0.50 (4364) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Laslo Djere vs Otto Virtanen -- ATP Challenger Bratislava II R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-05T15:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111513:202261:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Laslo Djere (`KXATPCHALLENGERMATCH-26NOV05DJEVIR-DJE`) | 0.33 / 0.34 (13050) | 33.5% | 71.8% | 64.2% | 69.3% [64.7%-73.1%] | 40.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +38.3 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Otto Virtanen (`KXATPCHALLENGERMATCH-26NOV05DJEVIR-VIR`) | 0.66 / 0.67 (10836) | 66.5% | 28.2% | 35.8% | 30.7% [26.9%-35.3%] | 59.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -38.3 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4372.0, B 5269.0; serve-point win A 65.5%, B 39.1%; Elo A 1886.4, B 1613.3; model uncertainty 0.042
* Form inputs: days since last match A 10, B 10; matches on record A 774, B 437; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV05DJEVIR-DJE  (YES = Laslo Djere)
Model: 72%
Kalshi: 34%
Gap: +38 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.045, surface_pool_high +0.038, surface_dev_loose +0.018, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Tom Gentzsch vs Matej Dodig -- ATP Challenger Bratislava II R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 15:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-05T15:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210167:212063:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matej Dodig (`KXATPCHALLENGERMATCH-26NOV05GENDOD-DOD`) | 0.94 / 0.95 (368) | 94.5% | 64.3% | 60.4% | 60.8% [58.9%-61.8%] | 60.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -30.2 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tom Gentzsch (`KXATPCHALLENGERMATCH-26NOV05GENDOD-GEN`) | 0.05 / 0.07 (26745) | 6.0% | 35.7% | 39.6% | 39.2% [38.2%-41.1%] | 39.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +29.7 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5358.0, B 5240.0; serve-point win A 62.5%, B 34.6%; Elo A 1677.7, B 1761.6; model uncertainty 0.0143
* Form inputs: days since last match A 19, B 17; matches on record A 340, B 260; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV05GENDOD-GEN  (YES = Tom Gentzsch)
Model: 36%
Kalshi: 6%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

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
| Mae Malige (`KXITFMATCH-26NOV05MORMAL-MAL`) | 0.09 / 0.10 (10701) | 9.5% | 23.2% | 28.1% | 27.3% [22.8%-30.4%] | 19.5% | -- | 19.5% | MARKETS_AGREE | WATCH | +13.7 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Alejandro Moro Canas (`KXITFMATCH-26NOV05MORMAL-MOR`) | 0.90 / 0.91 (10819) | 90.5% | 76.8% | 71.9% | 72.7% [69.6%-77.2%] | 80.5% | -- | 80.5% | KALSHI_LONE_OUTLIER | PASS | -13.7 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 5775.0, B 2579.0; serve-point win A 60.1%, B 45.5%; Elo A 1635.1, B 1450.4; model uncertainty 0.0382
* Form inputs: days since last match A 17, B 59; matches on record A 362, B 139; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.031, surface_dev_loose -0.004, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Burdet / Senn vs Bennani / Yilmaz -- M15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05BURSENBENYIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bennani / Yilmaz (`KXITFDOUBLES-26NOV05BURSENBENYIL-BENYIL`) | 0.62 / 0.70 (45) | 66.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Burdet / Senn (`KXITFDOUBLES-26NOV05BURSENBENYIL-BURSEN`) | 0.30 / 0.32 (10) | 31.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Jay Clarke / Jeevan Nedunchezhiyan vs Filip Duda / Tiago Pereira -- ATP Challenger Taranto QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05CLANEDDUDPER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jay Clarke / Jeevan Nedunchezhiyan (`KXATPCHALLENGERDOUBLES-26NOV05CLANEDDUDPER-CLANED`) | 0.18 / 0.94 (1) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Filip Duda / Tiago Pereira (`KXATPCHALLENGERDOUBLES-26NOV05CLANEDDUDPER-DUDPER`) | 0.68 / 0.86 (100) | 77.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Enrique Carrascosa Diaz (`KXITFMATCH-26NOV05GULCAR-CAR`) | 0.09 / 0.10 (205) | 9.5% | 10.7% | 14.1% | 14.0% [12.3%-15.3%] | 11.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.2 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Svyatoslav Gulin (`KXITFMATCH-26NOV05GULCAR-GUL`) | 0.90 / 0.91 (156) | 90.5% | 89.3% | 86.0% | 86.0% [84.7%-87.7%] | 88.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.2 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2956.0, B 922.0; serve-point win A 62.0%, B 47.5%; Elo A 1587.3, B 1270.7; model uncertainty 0.0149
* Form inputs: days since last match A 17, B 255; matches on record A 266, B 17; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.003, surface_pool_high +0.006, surface_dev_loose +0.003, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ifi / Stanke vs Bakshi / Purtseladze -- M15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05IFISTABAKPUR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bakshi / Purtseladze (`KXITFDOUBLES-26NOV05IFISTABAKPUR-BAKPUR`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ifi / Stanke (`KXITFDOUBLES-26NOV05IFISTABAKPUR-IFISTA`) | -- / 0.01 (52668) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE

## Kukasian / Plans vs Bocchi / Mugelli -- M15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05KUKPLABOCMUG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bocchi / Mugelli (`KXITFDOUBLES-26NOV05KUKPLABOCMUG-BOCMUG`) | 0.05 / 0.79 (2) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kukasian / Plans (`KXITFDOUBLES-26NOV05KUKPLABOCMUG-KUKPLA`) | 0.14 / 0.89 (2) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Francesco Maestrelli vs Peter Makk -- ATP Challenger Taranto R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207407:208353:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesco Maestrelli (`KXATPCHALLENGERMATCH-26NOV05MAEMAK-MAE`) | 0.73 / 0.74 (3326) | 73.5% | 66.8% | 41.1% | 58.9% [51.0%-68.3%] | 71.6% | 74.1% | 72.9% | MODEL_LONE_OUTLIER | PASS | -6.7 pp | NORMAL | STALE | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Peter Makk (`KXATPCHALLENGERMATCH-26NOV05MAEMAK-MAK`) | 0.26 / 0.27 (5589) | 26.5% | 33.2% | 58.9% | 41.1% [31.7%-49.0%] | 28.4% | 26.4% | 27.4% | MODEL_LONE_OUTLIER | WATCH | +6.7 pp | NORMAL | STALE | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5128.0, B 2061.0; serve-point win A 65.6%, B 37.9%; Elo A 1715.9, B 1480.1; model uncertainty 0.0866
* Form inputs: days since last match A 10, B 47; matches on record A 370, B 82; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Skander Mansouri / Maximilian Neuchrist vs Brian Bozemoj / Stijn Pel -- ATP Challenger Taranto QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05MANNEUBOZPEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brian Bozemoj / Stijn Pel (`KXATPCHALLENGERDOUBLES-26NOV05MANNEUBOZPEL-BOZPEL`) | 0.21 / 0.29 (7) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Skander Mansouri / Maximilian Neuchrist (`KXATPCHALLENGERDOUBLES-26NOV05MANNEUBOZPEL-MANNEU`) | 0.73 / 0.79 (5) | 76.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Samuele Pieri (`KXITFMATCH-26NOV05PIEZIE-PIE`) | 0.69 / 0.72 (325) | 70.5% | 65.5% | 63.9% | 66.4% [65.4%-68.6%] | 68.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.0 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marcel Zielinski (`KXITFMATCH-26NOV05PIEZIE-ZIE`) | 0.27 / 0.28 (34) | 27.5% | 34.5% | 36.1% | 33.6% [31.4%-34.6%] | 31.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +7.0 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3983.0, B 2564.0; serve-point win A 58.2%, B 44.8%; Elo A 1534.6, B 1392.0; model uncertainty 0.016
* Form inputs: days since last match A 17, B 220; matches on record A 208, B 151; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
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
| Ivan Gakhov (`KXITFMATCH-26NOV05PORGAK-GAK`) | 0.67 / 0.68 (9) | 67.5% | 58.7% | 50.0% | 56.8% [54.2%-62.3%] | 65.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Julio Cesar Porras (`KXITFMATCH-26NOV05PORGAK-POR`) | 0.32 / 0.33 (134) | 32.5% | 41.3% | 50.0% | 43.2% [37.7%-45.8%] | 34.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +8.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1554.0, B 4154.0; serve-point win A 56.8%, B 41.6%; Elo A 1499.8, B 1590.5; model uncertainty 0.0406
* Form inputs: days since last match A 346, B 31; matches on record A 115, B 857; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.010, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
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
| Sergi Perez Contri (`KXITFMATCH-26NOV05SHEPER-PER`) | 0.84 / 0.87 (1945) | 85.5% | 85.9% | 90.9% | 87.2% [83.1%-89.5%] | 83.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.4 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Leonid Sheyngezikht (`KXITFMATCH-26NOV05SHEPER-SHE`) | 0.13 / 0.14 (1) | 13.5% | 14.1% | 9.1% | 12.8% [10.4%-16.9%] | 16.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.6 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1472.0, B 3673.0; serve-point win A 49.7%, B 42.3%; Elo A 1212.9, B 1483.0; model uncertainty 0.0323
* Form inputs: days since last match A 220, B 192; matches on record A 130, B 359; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.006, surface_dev_loose -0.013, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Darta Feldmane / Nemcsek vs Breaz / Simionescu -- W15 Antalya QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05DARNEMBRESIM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Breaz / Simionescu (`KXITFWDOUBLES-26NOV05DARNEMBRESIM-BRESIM`) | 0.96 / 0.99 (29) | 97.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Darta Feldmane / Nemcsek (`KXITFWDOUBLES-26NOV05DARNEMBRESIM-DARNEM`) | -- / 0.01 (426) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE

## Pistola / Yemshanova vs Iushchenko / Turkmen -- W15 Antalya QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05PISYEMIUSTUR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iushchenko / Turkmen (`KXITFWDOUBLES-26NOV05PISYEMIUSTUR-IUSTUR`) | 0.98 / 0.99 (1) | 98.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pistola / Yemshanova (`KXITFWDOUBLES-26NOV05PISYEMIUSTUR-PISYEM`) | -- / 0.03 (400) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE; THIN_DISPLAYED_SIZE

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
| Karla Popovic (`KXITFWMATCH-26NOV05ZHIPOP-POP`) | 0.99 / -- (0) | -- | 85.5% | 80.5% | 76.6% [75.7%-78.2%] | -- | -- | -- | -- | PASS | -- | UNPRICED | STALE | F / POOR | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anastasia Zhilina (`KXITFWMATCH-26NOV05ZHIPOP-ZHI`) | -- / 0.01 (14) | -- | 14.5% | 19.5% | 23.4% [21.8%-24.3%] | -- | -- | -- | -- | PASS | -- | UNPRICED | STALE | F / POOR | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 1204.0; serve-point win A 48.1%, B 44.0%; Elo A 1249.1, B 1454.1; model uncertainty 0.0124
* Form inputs: days since last match A 1424, B 192; matches on record A 42, B 82; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.016, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luke Johnson / Ryan Seggerman vs Ivan Liutarevich / Filip Pieczonka -- ATP Challenger Bratislava II QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-05T16:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05JOHSEGLIUPIE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luke Johnson / Ryan Seggerman (`KXATPCHALLENGERDOUBLES-26NOV05JOHSEGLIUPIE-JOHSEG`) | 0.38 / 0.80 (2) | 59.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ivan Liutarevich / Filip Pieczonka (`KXATPCHALLENGERDOUBLES-26NOV05JOHSEGLIUPIE-LIUPIE`) | 0.09 / 0.50 (5) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jurij Rodionov vs Toby Samuel -- ATP Challenger Bratislava II R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 16:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-05T16:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200514:210389:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jurij Rodionov (`KXATPCHALLENGERMATCH-26NOV05RODSAM-ROD`) | 0.44 / 0.45 (7307) | 44.5% | 35.2% | 37.4% | 35.5% [32.2%-39.9%] | 45.9% | 44.5% | 45.2% | MODEL_LONE_OUTLIER | PASS | -9.3 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Toby Samuel (`KXATPCHALLENGERMATCH-26NOV05RODSAM-SAM`) | 0.55 / 0.56 (7239) | 55.5% | 64.8% | 62.6% | 64.5% [60.1%-67.8%] | 54.1% | 55.7% | 54.9% | MODEL_LONE_OUTLIER | SHADOW_BET | +9.3 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5184.0, B 4065.0; serve-point win A 59.6%, B 37.4%; Elo A 1685.1, B 1821.3; model uncertainty 0.0383
* Form inputs: days since last match A 8, B 10; matches on record A 613, B 192; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.009, surface_dev_loose +0.044, surface_dev_tight -0.033
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Carole Monnet vs Leyre Romero Gormaz -- WTA 125K Cali QF

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-05 20:00Z
* Current expected start: 2026-11-05 17:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-05 13:28Z
* Recommended handicap-by time: 2026-11-05 16:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · Clay · scheduled 2026-11-05T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220733:220742:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carole Monnet (`KXWTACHALLENGERMATCH-26NOV05MONROM-MON`) | 0.36 / 0.37 (2488) | 36.5% | 32.5% | 36.9% | 37.9% [36.3%-42.5%] | 36.9% | 35.8% | 36.3% | MODEL_LONE_OUTLIER | PASS | -4.0 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Leyre Romero Gormaz (`KXWTACHALLENGERMATCH-26NOV05MONROM-ROM`) | 0.63 / 0.65 (2844) | 64.0% | 67.5% | 63.1% | 62.1% [57.5%-63.7%] | 63.1% | 64.3% | 63.7% | MODEL_LONE_OUTLIER | PASS | +3.5 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3719.0, B 4018.0; serve-point win A 50.0%, B 46.6%; Elo A 1674.3, B 1745.6; model uncertainty 0.031
* Form inputs: days since last match A 1, B 1; matches on record A 526, B 431; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Julia Riera vs Renata Zarazua -- WTA 125K Cali QF

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-05 20:00Z
* Current expected start: 2026-11-05 17:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-05 13:28Z
* Recommended handicap-by time: 2026-11-05 16:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · Clay · scheduled 2026-11-05T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:213887:220699:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julia Riera (`KXWTACHALLENGERMATCH-26NOV05RIEZAR-RIE`) | 0.50 / 0.51 (1606) | 50.5% | 37.8% | 40.0% | 39.4% [38.9%-40.5%] | 51.0% | 50.7% | 50.8% | MODEL_LONE_OUTLIER | PASS | -12.7 pp | REVIEW | STALE | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Renata Zarazua (`KXWTACHALLENGERMATCH-26NOV05RIEZAR-ZAR`) | 0.49 / 0.50 (2147) | 49.5% | 62.2% | 60.1% | 60.6% [59.5%-61.1%] | 49.0% | 49.2% | 49.1% | MODEL_LONE_OUTLIER | SHADOW_BET | +12.7 pp | REVIEW | STALE | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3855.0, B 4923.0; serve-point win A 51.7%, B 46.0%; Elo A 1727.6, B 1797.1; model uncertainty 0.0077
* Form inputs: days since last match A 1, B 1; matches on record A 391, B 700; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

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
| Gabriele Crivellaro (`KXITFMATCH-26NOV05CRIMAR-CRI`) | 0.69 / 0.70 (279) | 69.5% | 48.9% | 40.7% | 44.3% [40.2%-47.9%] | 53.8% | -- | 53.8% | MODEL_LONE_OUTLIER | PASS | -20.6 pp | HIGH_REVIEW | STALE | C / LIMITED | AGREES_WITH_MODEL | VERIFIED |
| Pietro Marino (`KXITFMATCH-26NOV05CRIMAR-MAR`) | 0.30 / 0.31 (3704) | 30.5% | 51.1% | 59.3% | 55.7% [52.1%-59.8%] | 46.2% | -- | 46.2% | MODEL_LONE_OUTLIER | WATCH | +20.6 pp | HIGH_REVIEW | STALE | C / LIMITED | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 464.0, B 1636.0; serve-point win A 58.6%, B 41.2%; Elo A 1235.5, B 1264.5; model uncertainty 0.0386
* Form inputs: days since last match A 59, B 94; matches on record A 16, B 149; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV05CRIMAR-MAR  (YES = Pietro Marino)
Model: 51%
Kalshi: 30%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_MODEL
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; STALE_QUOTE
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
| Jacopo Berrettini (`KXITFMATCH-26NOV05FERBER-BER`) | 0.66 / 0.67 (15) | 66.5% | 60.4% | 54.1% | 58.2% [56.7%-59.8%] | 53.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.2 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gianmarco Ferrari (`KXITFMATCH-26NOV05FERBER-FER`) | 0.33 / 0.34 (1466) | 33.5% | 39.6% | 45.9% | 41.8% [40.2%-43.3%] | 46.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +6.2 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2506.0, B 3742.0; serve-point win A 58.2%, B 39.8%; Elo A 1474.0, B 1571.4; model uncertainty 0.0153
* Form inputs: days since last match A 59, B 220; matches on record A 294, B 386; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose +0.010, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ganchev / Maes vs Perez Ramos / Wright -- M25 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05GANMAEPERWRI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ganchev / Maes (`KXITFDOUBLES-26NOV05GANMAEPERWRI-GANMAE`) | 0.08 / 0.12 (1615) | 10.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Perez Ramos / Wright (`KXITFDOUBLES-26NOV05GANMAEPERWRI-PERWRI`) | 0.88 / 0.91 (243) | 89.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## G. Capitanio / Tsitsipas vs Neos / Tsitsipas -- M25 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05GCATSINEOTSI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| G. Capitanio / Tsitsipas (`KXITFDOUBLES-26NOV05GCATSINEOTSI-GCATSI`) | 0.06 / 0.10 (77) | 8.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Neos / Tsitsipas (`KXITFDOUBLES-26NOV05GCATSINEOTSI-NEOTSI`) | 0.89 / 0.93 (23) | 91.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Jones / Jones vs Angelini / Gschwendtner -- M25 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05JONJONANGGSC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Angelini / Gschwendtner (`KXITFDOUBLES-26NOV05JONJONANGGSC-ANGGSC`) | 0.30 / 0.31 (528) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jones / Jones (`KXITFDOUBLES-26NOV05JONJONANGGSC-JONJON`) | 0.69 / 0.70 (208) | 69.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

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
| El Sayed / Ezzat (`KXITFWDOUBLES-26NOV05ELSEZZMOUSUS-ELSEZZ`) | 0.53 / 0.95 (2) | 74.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Moutama / Suslova (`KXITFWDOUBLES-26NOV05ELSEZZMOUSUS-MOUSUS`) | -- / 0.29 (125) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Maria Golovina (`KXITFWMATCH-26NOV05GOLHEN-GOL`) | 0.25 / 0.29 (64) | 27.0% | 39.3% | 48.9% | 45.7% [35.4%-51.1%] | -- | -- | -- | -- | WATCH | +12.3 pp | REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Caijsa Wilda Hennemann (`KXITFWMATCH-26NOV05GOLHEN-HEN`) | 0.71 / 0.75 (137) | 73.0% | 60.7% | 51.1% | 54.3% [48.9%-64.6%] | -- | -- | -- | -- | PASS | -12.3 pp | REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2344.0, B 2350.0; serve-point win A 52.5%, B 45.5%; Elo A 1551.0, B 1608.5; model uncertainty 0.0784
* Form inputs: days since last match A 192, B 192; matches on record A 97, B 313; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.042, surface_pool_high +0.053, surface_dev_loose +0.011, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andrej Martin / Lukas Pokorny vs Matej Vocel / Michael Vrbensky -- ATP Challenger Bratislava II QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-05T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05MARPOKVOCVRB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrej Martin / Lukas Pokorny (`KXATPCHALLENGERDOUBLES-26NOV05MARPOKVOCVRB-MARPOK`) | 0.23 / 0.27 (48) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matej Vocel / Michael Vrbensky (`KXATPCHALLENGERDOUBLES-26NOV05MARPOKVOCVRB-VOCVRB`) | 0.70 / 0.75 (29) | 72.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

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
| Tessa Johanna Brockmann (`KXITFWMATCH-26NOV05BROFRI-BRO`) | 0.64 / 0.65 (6532) | 64.5% | 46.1% | 55.2% | 49.0% [44.2%-51.6%] | 46.2% | -- | 46.2% | KALSHI_LONE_OUTLIER | PASS | -18.4 pp | HIGH_REVIEW | STALE | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Anna-Lena Friedsam (`KXITFWMATCH-26NOV05BROFRI-FRI`) | 0.35 / 0.36 (4720) | 35.5% | 53.9% | 44.8% | 51.0% [48.4%-55.8%] | 53.8% | -- | 53.8% | MODEL_LONE_OUTLIER | WATCH | +18.4 pp | HIGH_REVIEW | STALE | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 3426.0, B 3834.0; serve-point win A 58.1%, B 41.1%; Elo A 1598.4, B 1702.3; model uncertainty 0.0367
* Form inputs: days since last match A 23, B 24; matches on record A 169, B 669; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05BROFRI-FRI  (YES = Anna-Lena Friedsam)
Model: 54%
Kalshi: 36%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_MODEL
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE
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
| Oriana Gniewkowska (`KXITFWMATCH-26NOV05GNILOV-GNI`) | 0.03 / 0.04 (5964) | 3.5% | 14.0% | 22.6% | 21.8% [19.5%-25.1%] | 21.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +10.4 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pia Lovric (`KXITFWMATCH-26NOV05GNILOV-LOV`) | 0.96 / 0.97 (2622) | 96.5% | 86.1% | 77.4% | 78.2% [74.9%-80.5%] | 78.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -10.4 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 810.0, B 1631.0; serve-point win A 44.8%, B 47.2%; Elo A 1310.9, B 1535.5; model uncertainty 0.0279
* Form inputs: days since last match A 388, B 25; matches on record A 34, B 300; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.015, surface_dev_loose -0.011, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
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
| Mina Hodzic (`KXITFWMATCH-26NOV05HODRAD-HOD`) | 0.02 / 0.03 (9034) | 2.5% | 30.6% | 26.5% | 29.0% [26.6%-33.3%] | 33.6% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +28.1 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lola Radivojevic (`KXITFWMATCH-26NOV05HODRAD-RAD`) | 0.97 / 0.98 (129) | 97.5% | 69.4% | 73.6% | 71.0% [66.7%-73.4%] | 66.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -28.1 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2700.0, B 3394.0; serve-point win A 58.8%, B 37.3%; Elo A 1489.5, B 1605.3; model uncertainty 0.0335
* Form inputs: days since last match A 23, B 30; matches on record A 288, B 294; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05HODRAD-HOD  (YES = Mina Hodzic)
Model: 31%
Kalshi: 2%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.024, surface_dev_tight +0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
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
| Laura Mair (`KXITFWMATCH-26NOV05MAIMIL-MAI`) | 0.26 / 0.28 (2174) | 27.0% | 53.0% | 41.0% | 45.7% [43.1%-48.9%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +26.0 pp | EXTREME (DATA_WARNING) | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elena Milovanovic (`KXITFWMATCH-26NOV05MAIMIL-MIL`) | 0.72 / 0.73 (12) | 72.5% | 47.0% | 59.0% | 54.3% [51.1%-56.9%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -25.5 pp | EXTREME (DATA_WARNING) | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2387.0, B 2475.0; serve-point win A 54.2%, B 46.4%; Elo A 1460.8, B 1435.0; model uncertainty 0.0292
* Form inputs: days since last match A 8, B 199; matches on record A 243, B 299; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05MAIMIL-MAI  (YES = Laura Mair)
Model: 53%
Kalshi: 27%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_KALSHI_QUOTE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.026, surface_pool_high +0.032, surface_dev_loose +0.027, surface_dev_tight -0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arthur Fils vs Taylor Fritz -- ATP Paris R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-05 22:30Z
* Current expected start: 2026-11-05 18:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-05 13:28Z
* Recommended handicap-by time: 2026-11-05 17:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-270_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-11-05T22:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126203:209950:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arthur Fils (`KXATPMATCH-26NOV05FILFRI-FIL`) | 0.54 / 0.55 (2375) | 54.5% | 47.7% | 40.6% | 42.4% [41.5%-43.8%] | 54.3% | 54.8% | 54.8% | MODEL_LONE_OUTLIER | PASS | -6.8 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Taylor Fritz (`KXATPMATCH-26NOV05FILFRI-FRI`) | 0.45 / 0.46 (154879) | 45.5% | 52.3% | 59.4% | 57.6% [56.2%-58.5%] | 45.7% | 45.1% | 45.1% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.8 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4555.0, B 6763.0; serve-point win A 67.8%, B 31.8%; Elo A 2049.3, B 2058.5; model uncertainty 0.0116
* Form inputs: days since last match A 1, B 1; matches on record A 339, B 770; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.000, surface_dev_loose +0.009, surface_dev_tight -0.009
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26NOV05FILFRI-FIL20` Will Arthur Fils win the Arthur Fils vs Taylor Fritz match by a set score of 2-0?: 0.31/0.32 mid 31.5%, model 23.5% (projection_v2.0 (prediction ledger)) -- gap -8.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV05FILFRI-24` Over 23.5 games: 0.50/0.51 mid 50.5%, model 58.2% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV05FILFRI-FIL5` Will Arthur Fils win at least 4.5 more games than Taylor Fritz?: 0.16/0.20 mid 18.0%, model 10.6% (projection_v2.0 (prediction ledger)) -- gap -7.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV05FILFRI-FIL2` Will Arthur Fils win at least 1.5 more games than Taylor Fritz?: 0.46/0.47 mid 46.5%, model 39.2% (projection_v2.0 (prediction ledger)) -- gap -7.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05FILFRI-FRI21` Will Taylor Fritz win the Arthur Fils vs Taylor Fritz match by a set score of 2-1?: 0.17/0.21 mid 19.0%, model 25.7% (projection_v2.0 (prediction ledger)) -- gap +6.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV05FILFRI-29` Over 28.5 games: 0.35/0.36 mid 35.5%, model 41.8% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV05FILFRI-19` Over 18.5 games: 0.86/0.89 mid 87.5%, model 93.6% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV05FILFRI-2-FRI` Will Taylor Fritz win set 2 in the Arthur Fils vs Taylor Fritz match: 0.44/0.47 mid 45.5%, model 51.5% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV05FILFRI-1-FRI` Will Taylor Fritz win set 1 in the Arthur Fils vs Taylor Fritz match: 0.45/0.48 mid 46.5%, model 51.5% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV05FILFRI-1-FIL` Will Arthur Fils win set 1 in the Arthur Fils vs Taylor Fritz match: 0.52/0.53 mid 52.5%, model 48.5% (projection_v2.0 (prediction ledger)) -- gap -4.0 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV05FILFRI-2-FIL` Will Arthur Fils win set 2 in the Arthur Fils vs Taylor Fritz match: 0.51/0.54 mid 52.5%, model 48.5% (projection_v2.0 (prediction ledger)) -- gap -4.0 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV05FILFRI-FRI2` Will Taylor Fritz win at least 1.5 more games than Arthur Fils?: 0.38/0.42 mid 40.0%, model 43.6% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05FILFRI-FIL21` Will Arthur Fils win the Arthur Fils vs Taylor Fritz match by a set score of 2-1?: 0.19/0.23 mid 21.0%, model 24.2% (projection_v2.0 (prediction ledger)) -- gap +3.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05FILFRI-FRI20` Will Taylor Fritz win the Arthur Fils vs Taylor Fritz match by a set score of 2-0?: 0.25/0.27 mid 26.0%, model 26.5% (projection_v2.0 (prediction ledger)) -- gap +0.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE

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
| Abderrahman / Ouakaa (`KXITFDOUBLES-26NOV05ABDOUANAGRAH-ABDOUA`) | 0.40 / 0.52 (45) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nagoudi / Rahmani (`KXITFDOUBLES-26NOV05ABDOUANAGRAH-NAGRAH`) | 0.48 / 0.58 (9) | 53.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Ali Abibsi / Mondazzi (`KXITFDOUBLES-26NOV05ALIMONBAREHR-ALIMON`) | 0.15 / 0.26 (13) | 20.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Barsukov / Ehrenschneider (`KXITFDOUBLES-26NOV05ALIMONBAREHR-BAREHR`) | 0.69 / 0.81 (49) | 75.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Facundo Bagnis / Gonzalo Villanueva vs Joao Victor Couto Loureiro / Victor Hugo Remondy Pagotto -- ATP Challenger Villa Maria QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-05T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05BAGVILCOUREM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Facundo Bagnis / Gonzalo Villanueva (`KXATPCHALLENGERDOUBLES-26NOV05BAGVILCOUREM-BAGVIL`) | 0.50 / 0.58 (23) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Joao Victor Couto Loureiro / Victor Hugo Remondy Pagotto (`KXATPCHALLENGERDOUBLES-26NOV05BAGVILCOUREM-COUREM`) | 0.42 / 0.46 (52) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

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
| Stepan Baum (`KXITFMATCH-26NOV05BAULAV-BAU`) | 0.35 / 0.41 (25) | 38.0% | 38.3% | 37.1% | 40.1% [39.1%-40.7%] | 37.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Giuseppe La Vela (`KXITFMATCH-26NOV05BAULAV-LAV`) | 0.59 / 0.60 (62) | 59.5% | 61.7% | 62.9% | 59.9% [59.3%-60.9%] | 62.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.2 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 461.0, B 2431.0; serve-point win A 56.2%, B 41.5%; Elo A 1370.5, B 1436.7; model uncertainty 0.0083
* Form inputs: days since last match A 346, B 45; matches on record A 24, B 183; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.005, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
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
| Bouchelaghem / van Wyk (`KXITFDOUBLES-26NOV05NORSAHBOUVAN-BOUVAN`) | 0.44 / 0.49 (466) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nortey / Sahtali (`KXITFDOUBLES-26NOV05NORSAHBOUVAN-NORSAH`) | 0.51 / 0.56 (16) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

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
| Antonio Caruso (`KXITFMATCH-26NOV05SPECAR-CAR`) | 0.13 / 0.15 (4) | 14.0% | 15.7% | 33.1% | 21.0% [20.2%-22.2%] | 17.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.7 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| John Sperle (`KXITFMATCH-26NOV05SPECAR-SPE`) | 0.82 / 0.87 (122) | 84.5% | 84.3% | 66.9% | 79.0% [77.8%-79.8%] | 83.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.2 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2038.0, B 204.0; serve-point win A 60.5%, B 47.2%; Elo A 1418.7, B 1173.6; model uncertainty 0.01
* Form inputs: days since last match A 38, B 416; matches on record A 177, B 37; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.004, surface_dev_loose +0.001, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Juan Bautista Torres vs Ryan Nijboer -- ATP Challenger Villa Maria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-05T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207764:208913:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ryan Nijboer (`KXATPCHALLENGERMATCH-26NOV05TORNIJ-NIJ`) | 0.39 / 0.41 (3658) | 40.0% | 33.4% | 34.0% | 34.0% [34.0%-36.5%] | 40.1% | 40.7% | 40.7% | MODEL_LONE_OUTLIER | PASS | -6.6 pp | NORMAL | STALE | B / LIMITED | EXTERNAL_STALE | VERIFIED |
| Juan Bautista Torres (`KXATPCHALLENGERMATCH-26NOV05TORNIJ-TOR`) | 0.59 / 0.60 (2157) | 59.5% | 66.6% | 66.0% | 66.0% [63.5%-66.0%] | 59.9% | 59.8% | 59.8% | MODEL_LONE_OUTLIER | SHADOW_BET | +7.1 pp | NORMAL | STALE | B / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5064.0, B 3728.0; serve-point win A 56.7%, B 46.5%; Elo A 1604.3, B 1504.2; model uncertainty 0.0128
* Form inputs: days since last match A 192, B 31; matches on record A 360, B 472; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

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
| Arcangioli / Cirotte (`KXITFWDOUBLES-26NOV05BABDELARCCIR-ARCCIR`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Babel / Delaunay (`KXITFWDOUBLES-26NOV05BABDELARCCIR-BABDEL`) | -- / 0.01 (53282) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE

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
| Matylda Burylo (`KXITFWMATCH-26NOV05BURLON-BUR`) | 0.97 / 0.98 (4892) | 97.5% | 41.9% | 61.5% | 50.5% [47.9%-53.2%] | 20.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -55.6 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Romane Longueville (`KXITFWMATCH-26NOV05BURLON-LON`) | 0.02 / 0.03 (15746) | 2.5% | 58.1% | 38.5% | 49.5% [46.8%-52.1%] | 79.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +55.6 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 498.0, B 1160.0; serve-point win A 54.9%, B 43.5%; Elo A 1246.2, B 1266.8; model uncertainty 0.0265
* Form inputs: days since last match A 248, B 234; matches on record A 42, B 68; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05BURLON-LON  (YES = Romane Longueville)
Model: 58%
Kalshi: 2%
Gap: +56 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.011, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
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
| Cassani / Cavelli (`KXITFWDOUBLES-26NOV05CASCAVLIZMAS-CASCAV`) | 0.05 / 0.13 (297) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lizunova / Masiianskaia (`KXITFWDOUBLES-26NOV05CASCAVLIZMAS-LIZMAS`) | 0.87 / 0.95 (2) | 91.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Chiesa / Pedone (`KXITFWDOUBLES-26NOV05CHIPEDGRAYAR-CHIPED`) | 0.87 / 0.92 (451) | 89.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Grammatikopoulou / Yardley (`KXITFWDOUBLES-26NOV05CHIPEDGRAYAR-GRAYAR`) | 0.08 / 0.13 (611) | 10.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

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
| Fernandez / Garcia-Patron Canals (`KXITFWDOUBLES-26NOV05FERGARFUSHUS-FERGAR`) | 0.16 / 0.33 (10) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fusil / Husar (`KXITFWDOUBLES-26NOV05FERGARFUSHUS-FUSHUS`) | 0.63 / 0.77 (20) | 70.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

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
| Lea Fojcik (`KXITFWMATCH-26NOV05FOJSER-FOJ`) | 0.18 / 0.19 (9440) | 18.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Emese Serkedi (`KXITFWMATCH-26NOV05FOJSER-SER`) | 0.81 / 0.82 (9406) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
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
| Georgiana Goina / Molnar (`KXITFWDOUBLES-26NOV05PAWRABGEOMOL-GEOMOL`) | 0.94 / 0.97 (77) | 95.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pawelska / Rabl (`KXITFWDOUBLES-26NOV05PAWRABGEOMOL-PAWRAB`) | 0.01 / 0.06 (43) | 3.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

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
| Lilly Sophie Steur / Van Emst (`KXITFWDOUBLES-26NOV05STOYESLILVAN-LILVAN`) | 0.72 / 0.89 (8) | 80.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stoyanov / Yesypchuk (`KXITFWDOUBLES-26NOV05STOYESLILVAN-STOYES`) | 0.09 / 0.25 (33) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Allen / Karatancheva (`KXITFWDOUBLES-26NOV05SVATICALLKAR-ALLKAR`) | 0.28 / 0.40 (41) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Svatikova / Tichackova (`KXITFWDOUBLES-26NOV05SVATICALLKAR-SVATIC`) | 0.49 / 0.70 (10) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Leolia Jeanjean vs Alice Tubello -- WTA 125K Cali QF

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-05 21:10Z
* Current expected start: 2026-11-05 18:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-05 13:28Z
* Recommended handicap-by time: 2026-11-05 17:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · Clay · scheduled 2026-11-05T21:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:206417:220554:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leolia Jeanjean (`KXWTACHALLENGERMATCH-26NOV05JEATUB-JEA`) | 0.46 / 0.47 (72) | 46.5% | 48.9% | 27.9% | 39.0% [32.5%-55.3%] | 48.0% | 47.2% | 47.2% | MARKETS_AGREE | PASS | +2.5 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Alice Tubello (`KXWTACHALLENGERMATCH-26NOV05JEATUB-TUB`) | 0.52 / 0.53 (124) | 52.5% | 51.0% | 72.1% | 61.0% [44.7%-67.5%] | 52.0% | 53.1% | 53.1% | MARKETS_AGREE | WATCH | -1.4 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4130.0, B 2580.0; serve-point win A 54.9%, B 44.9%; Elo A 1797.1, B 1736.0; model uncertainty 0.1138
* Form inputs: days since last match A 1, B 1; matches on record A 440, B 339; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.015, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

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
| Barroso Campos / Pujol Navarro (`KXITFDOUBLES-26NOV05BARPUJNAHTAL-BARPUJ`) | 0.71 / 0.91 (2) | 81.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Naharro / Talan Lopatic (`KXITFDOUBLES-26NOV05BARPUJNAHTAL-NAHTAL`) | 0.03 / 0.22 (32) | 12.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Garcia Carbajal / Mansilla Diez (`KXITFDOUBLES-26NOV05MILPARGARMAN-GARMAN`) | 0.50 / 0.64 (69) | 57.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Milev / Parisca (`KXITFDOUBLES-26NOV05MILPARGARMAN-MILPAR`) | 0.32 / 0.46 (46) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Luisina Giovannini vs Bianca Andreescu -- WTA 125K Cali QF

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-05 22:00Z
* Current expected start: 2026-11-05 19:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-05 13:28Z
* Recommended handicap-by time: 2026-11-05 18:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · Clay · scheduled 2026-11-05T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:215370:236972:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bianca Andreescu (`KXWTACHALLENGERMATCH-26NOV05GIOAND-AND`) | 0.78 / 0.79 (1208) | 78.5% | 57.3% | 22.2% | 35.1% [28.1%-56.8%] | 76.9% | 74.4% | 75.6% | KALSHI_LONE_OUTLIER | PASS | -21.2 pp | HIGH_REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Luisina Giovannini (`KXWTACHALLENGERMATCH-26NOV05GIOAND-GIO`) | 0.21 / 0.22 (1109) | 21.5% | 42.7% | 77.8% | 64.9% [43.2%-71.9%] | 23.1% | 21.7% | 23.1% | MODEL_LONE_OUTLIER | WATCH | +21.2 pp | HIGH_REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3057.0, B 2877.0; serve-point win A 56.4%, B 42.2%; Elo A 1757.5, B 1842.8; model uncertainty 0.1436
* Form inputs: days since last match A 1, B 1; matches on record A 203, B 378; data quality A

```
DISCREPANCY SANITY CHECK  KXWTACHALLENGERMATCH-26NOV05GIOAND-GIO  (YES = Luisina Giovannini)
Model: 43%
Kalshi: 22%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.019, surface_dev_loose +0.019, surface_dev_tight -0.020
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Johannes Ingildsen / Abdullah Shelbayh vs Trey Hilderbrand / Bogdan Pavel -- ATP Challenger Charlottesville QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-05T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05INGSHEHILPAV:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Trey Hilderbrand / Bogdan Pavel (`KXATPCHALLENGERDOUBLES-26NOV05INGSHEHILPAV-HILPAV`) | 0.56 / 0.60 (18) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Johannes Ingildsen / Abdullah Shelbayh (`KXATPCHALLENGERDOUBLES-26NOV05INGSHEHILPAV-INGSHE`) | 0.37 / 0.41 (43) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Aidan Mayo vs Alastair Gray -- ATP Challenger Charlottesville R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-05T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202400:208854:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alastair Gray (`KXATPCHALLENGERMATCH-26NOV05MAYGRA-GRA`) | 0.36 / 0.37 (31) | 36.5% | 47.4% | 55.0% | 54.0% [51.5%-55.0%] | 37.5% | 37.0% | 37.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +10.9 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Aidan Mayo (`KXATPCHALLENGERMATCH-26NOV05MAYGRA-MAY`) | 0.63 / 0.64 (3111) | 63.5% | 52.6% | 45.0% | 46.0% [45.0%-48.5%] | 62.5% | 63.3% | 62.9% | MODEL_LONE_OUTLIER | PASS | -10.9 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3926.0, B 3694.0; serve-point win A 64.5%, B 36.1%; Elo A 1573.4, B 1580.2; model uncertainty 0.0174
* Form inputs: days since last match A 10, B 52; matches on record A 260, B 326; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Dalibor Svrcina vs Giovanni Mpetshi Perricard -- ATP Challenger Bratislava II R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-05T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207494:208659:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giovanni Mpetshi Perricard (`KXATPCHALLENGERMATCH-26NOV05SVRMPE-MPE`) | 0.56 / 0.57 (2865) | 56.5% | 50.7% | 33.4% | 39.0% [36.7%-42.5%] | 55.4% | 56.5% | 56.5% | MODEL_LONE_OUTLIER | PASS | -5.8 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Dalibor Svrcina (`KXATPCHALLENGERMATCH-26NOV05SVRMPE-SVR`) | 0.42 / 0.43 (62) | 42.5% | 49.3% | 66.6% | 61.0% [57.5%-63.3%] | 44.6% | 43.5% | 43.5% | MODEL_LONE_OUTLIER | WATCH | +6.8 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5261.0, B 4293.0; serve-point win A 62.6%, B 37.3%; Elo A 1728.4, B 1774.2; model uncertainty 0.029
* Form inputs: days since last match A 24, B 9; matches on record A 426, B 328; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose +0.001, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Berta Bonardi vs Sol Ailin Larraya Guidi -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206406:260709:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Berta Bonardi (`KXITFWMATCH-26NOV05BONLAR-BON`) | 0.61 / 0.65 (2346) | 63.0% | 58.6% | 74.5% | 54.8% [49.5%-61.6%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.4 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sol Ailin Larraya Guidi (`KXITFWMATCH-26NOV05BONLAR-LAR`) | 0.35 / 0.38 (6) | 36.5% | 41.4% | 25.5% | 45.2% [38.4%-50.5%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.9 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1960.0, B 409.0; serve-point win A 51.1%, B 50.5%; Elo A 1367.9, B 1373.5; model uncertainty 0.0609
* Form inputs: days since last match A 9, B 220; matches on record A 276, B 66; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.011, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
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

ITF (ITF) · Clay · scheduled 2026-11-05T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206345:266446:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Victoria Bosio (`KXITFWMATCH-26NOV05BOSMEA-BOS`) | 0.79 / 0.80 (9663) | 79.5% | 85.8% | 96.7% | 81.9% [78.9%-85.8%] | 72.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sofia Meabe (`KXITFWMATCH-26NOV05BOSMEA-MEA`) | 0.20 / 0.21 (1417) | 20.5% | 14.2% | 3.3% | 18.1% [14.2%-21.1%] | 27.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3098.0, B 235.0; serve-point win A 56.0%, B 52.0%; Elo A 1566.7, B 1346.8; model uncertainty 0.0348
* Form inputs: days since last match A 10, B 290; matches on record A 565, B 18; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.007, surface_dev_loose +0.007, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
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

ITF (ITF) · Clay · scheduled 2026-11-05T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215807:260541:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Weronika Ewald (`KXITFWMATCH-26NOV05LEOEWA-EWA`) | 0.34 / 0.36 (40) | 35.0% | 81.1% | 66.5% | 71.7% [68.9%-76.1%] | 35.6% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +46.1 pp | EXTREME (DATA_WARNING) | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Manon Leonard (`KXITFWMATCH-26NOV05LEOEWA-LEO`) | 0.60 / 0.66 (133) | 63.0% | 18.9% | 33.5% | 28.3% [23.9%-31.1%] | 64.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -44.1 pp | EXTREME (DATA_WARNING) | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3201.0, B 2476.0; serve-point win A 51.0%, B 42.4%; Elo A 1347.2, B 1581.0; model uncertainty 0.0357
* Form inputs: days since last match A 143, B 192; matches on record A 348, B 129; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05LEOEWA-EWA  (YES = Weronika Ewald)
Model: 81%
Kalshi: 35%
Gap: +46 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_KALSHI_QUOTE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.028, surface_pool_high -0.026, surface_dev_loose -0.044, surface_dev_tight +0.028
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD
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

ITF (ITF) · Clay · scheduled 2026-11-05T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214713:260357:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Florencia Belen Moron (`KXITFWMATCH-26NOV05MORROM-MOR`) | 0.01 / 0.02 (5554) | 1.5% | 9.1% | 36.9% | 19.7% [18.6%-20.4%] | 5.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.6 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Camila Romero (`KXITFWMATCH-26NOV05MORROM-ROM`) | 0.99 / -- (0) | -- | 90.9% | 63.1% | 80.3% [79.6%-81.4%] | 95.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | STALE | D / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 144.0, B 1526.0; serve-point win A 49.5%, B 40.4%; Elo A 1116.0, B 1380.5; model uncertainty 0.0092
* Form inputs: days since last match A 290, B 199; matches on record A 77, B 225; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.007, surface_dev_loose -0.004, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE
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

ITF (ITF) · Clay · scheduled 2026-11-05T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220489:260539:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Josy Daems (`KXITFWMATCH-26NOV05RYSDAE-DAE`) | 0.30 / 0.31 (126) | 30.5% | 43.3% | 65.8% | 59.4% [42.6%-63.9%] | 30.3% | -- | 30.3% | MODEL_LONE_OUTLIER | WATCH | +12.8 pp | REVIEW | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Valentina Ryser (`KXITFWMATCH-26NOV05RYSDAE-RYS`) | 0.68 / 0.69 (80) | 68.5% | 56.7% | 34.2% | 40.6% [36.1%-57.4%] | 69.7% | -- | 69.7% | MODEL_LONE_OUTLIER | PASS | -11.8 pp | REVIEW | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3017.0, B 2580.0; serve-point win A 58.1%, B 43.2%; Elo A 1506.9, B 1490.8; model uncertainty 0.1061
* Form inputs: days since last match A 58, B 234; matches on record A 392, B 103; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.036, surface_pool_high -0.035, surface_dev_loose -0.045, surface_dev_tight +0.036
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Juan Pablo Ficovich vs Murkel Dellien -- ATP Challenger Villa Maria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 19:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-05T19:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:123961:126663:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Murkel Dellien (`KXATPCHALLENGERMATCH-26NOV05FICDEV-DEV`) | 0.36 / 0.38 (3192) | 37.0% | 40.0% | 45.8% | 44.8% [41.7%-45.8%] | 37.5% | 36.7% | 36.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +3.0 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | AMBIGUOUS |
| Juan Pablo Ficovich (`KXATPCHALLENGERMATCH-26NOV05FICDEV-FIC`) | 0.62 / 0.63 (2) | 62.5% | 60.0% | 54.2% | 55.2% [54.2%-58.3%] | 62.5% | 61.5% | -- | INSUFFICIENT_INPUTS | PASS | -2.5 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 4206.0, B 4395.0; serve-point win A 59.0%, B 42.9%; Elo A 1579.8, B 1515.2; model uncertainty 0.0206
* Form inputs: days since last match A 17, B 24; matches on record A 723, B 403; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.010, surface_dev_loose +0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Ignacio Monzon vs Genaro Alberto Olivieri -- ATP Challenger Villa Maria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 19:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-05T19:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:133820:144821:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ignacio Monzon (`KXATPCHALLENGERMATCH-26NOV05MONOLI-MON`) | 0.15 / 0.16 (4771) | 15.5% | 23.6% | 36.4% | 31.6% [27.5%-33.5%] | 17.9% | 15.3% | 15.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +8.1 pp | NORMAL | STALE | A / LIMITED | EXTERNAL_STALE | VERIFIED |
| Genaro Alberto Olivieri (`KXATPCHALLENGERMATCH-26NOV05MONOLI-OLI`) | 0.84 / 0.86 (4331) | 85.0% | 76.4% | 63.5% | 68.4% [66.5%-72.5%] | 82.1% | 85.2% | 85.2% | MODEL_LONE_OUTLIER | PASS | -8.6 pp | NORMAL | STALE | A / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3341.0, B 5035.0; serve-point win A 52.2%, B 42.4%; Elo A 1356.6, B 1586.5; model uncertainty 0.0298
* Form inputs: days since last match A 122, B 10; matches on record A 427, B 609; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.005, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Belkova / Kuharenko vs Shan / Jie Tzeng -- W15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 19:15Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T19:15:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05BELKUHSHAJIE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Belkova / Kuharenko (`KXITFWDOUBLES-26NOV05BELKUHSHAJIE-BELKUH`) | 0.69 / 0.71 (766) | 70.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Shan / Jie Tzeng (`KXITFWDOUBLES-26NOV05BELKUHSHAJIE-SHAJIE`) | 0.31 / 0.32 (586) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Jan-Lennard Struff vs Casper Ruud -- ATP Paris R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-05 18:20Z
* Current expected start: 2026-11-05 19:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-05 13:28Z
* Recommended handicap-by time: 2026-11-05 18:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+70_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-11-05T18:20:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105526:134770:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Casper Ruud (`KXATPMATCH-26NOV05STRRUU-RUU`) | 0.65 / 0.66 (4411) | 65.5% | 66.8% | 60.8% | 61.7% [60.4%-62.7%] | 63.9% | 66.5% | 66.5% | MARKETS_AGREE | PASS | +1.3 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Jan-Lennard Struff (`KXATPMATCH-26NOV05STRRUU-STR`) | 0.34 / 0.35 (39041) | 34.5% | 33.2% | 39.2% | 38.3% [37.3%-39.6%] | 36.1% | 33.5% | 33.5% | MARKETS_AGREE | SHADOW_BET | -1.3 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5653.0, B 5180.0; serve-point win A 66.1%, B 30.2%; Elo A 1846.2, B 1951.6; model uncertainty 0.0116
* Form inputs: days since last match A 1, B 2; matches on record A 1077, B 721; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.000, surface_dev_loose +0.010, surface_dev_tight -0.010
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV05STRRUU-29` Over 28.5 games: 0.31/0.32 mid 31.5%, model 39.3% (projection_v2.0 (prediction ledger)) -- gap +7.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV05STRRUU-RUU6` Will Casper Ruud win at least 5.5 more games than Jan-Lennard Struff?: 0.15/0.18 mid 16.5%, model 9.5% (projection_v2.0 (prediction ledger)) -- gap -7.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV05STRRUU-24` Over 23.5 games: 0.49/0.50 mid 49.5%, model 55.4% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05STRRUU-RUU21` Will Casper Ruud win the Jan-Lennard Struff vs Casper Ruud match by a set score of 2-1?: 0.23/0.24 mid 23.5%, model 29.1% (projection_v2.0 (prediction ledger)) -- gap +5.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV05STRRUU-19` Over 18.5 games: 0.85/0.89 mid 87.0%, model 92.2% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05STRRUU-STR20` Will Jan-Lennard Struff win the Jan-Lennard Struff vs Casper Ruud match by a set score of 2-0?: 0.18/0.20 mid 19.0%, model 14.9% (projection_v2.0 (prediction ledger)) -- gap -4.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV05STRRUU-STR2` Will Jan-Lennard Struff win at least 1.5 more games than Casper Ruud?: 0.28/0.31 mid 29.5%, model 25.8% (projection_v2.0 (prediction ledger)) -- gap -3.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV05STRRUU-RUU3` Will Casper Ruud win at least 2.5 more games than Jan-Lennard Struff?: 0.51/0.52 mid 51.5%, model 48.6% (projection_v2.0 (prediction ledger)) -- gap -2.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05STRRUU-STR21` Will Jan-Lennard Struff win the Jan-Lennard Struff vs Casper Ruud match by a set score of 2-1?: 0.15/0.17 mid 16.0%, model 18.3% (projection_v2.0 (prediction ledger)) -- gap +2.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV05STRRUU-RUU20` Will Casper Ruud win the Jan-Lennard Struff vs Casper Ruud match by a set score of 2-0?: 0.39/0.40 mid 39.5%, model 37.7% (projection_v2.0 (prediction ledger)) -- gap -1.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV05STRRUU-1-RUU` Will Casper Ruud win set 1 in the Jan-Lennard Struff vs Casper Ruud match: 0.59/0.61 mid 60.0%, model 61.4% (projection_v2.0 (prediction ledger)) -- gap +1.4 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV05STRRUU-1-STR` Will Jan-Lennard Struff win set 1 in the Jan-Lennard Struff vs Casper Ruud match: 0.39/0.41 mid 40.0%, model 38.6% (projection_v2.0 (prediction ledger)) -- gap -1.4 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV05STRRUU-2-RUU` Will Casper Ruud win set 2 in the Jan-Lennard Struff vs Casper Ruud match: 0.59/0.62 mid 60.5%, model 61.4% (projection_v2.0 (prediction ledger)) -- gap +0.9 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV05STRRUU-2-STR` Will Jan-Lennard Struff win set 2 in the Jan-Lennard Struff vs Casper Ruud match: 0.36/0.40 mid 38.0%, model 38.6% (projection_v2.0 (prediction ledger)) -- gap +0.6 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE

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
| Biot / Boron (`KXITFWDOUBLES-26NOV05BIOBORKALMIH-BIOBOR`) | 0.04 / 0.85 (1) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kalman / Mihalka (`KXITFWDOUBLES-26NOV05BIOBORKALMIH-KALMIH`) | 0.35 / 0.95 (2) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Biro / Marlies Rothensteiner (`KXITFWDOUBLES-26NOV05BIRMARKARSAL-BIRMAR`) | 0.20 / 0.94 (1) | 57.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kardos / Salaiova (`KXITFWDOUBLES-26NOV05BIRMARKARSAL-KARSAL`) | -- / 0.69 (1) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Bosman / Akasha Ceuca (`KXITFWDOUBLES-26NOV05FENVLABOSAKA-BOSAKA`) | 0.15 / 0.89 (1) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fenyves / Vlajic (`KXITFWDOUBLES-26NOV05FENVLABOSAKA-FENVLA`) | 0.03 / 0.76 (1) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Blaise Bicknell vs Kian Vakili -- M15 Pembroke R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209080:210704:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Blaise Bicknell (`KXITFMATCH-26NOV05BICVAK-BIC`) | 0.94 / 0.96 (875) | 95.0% | 91.2% | 70.9% | 83.5% [82.5%-84.1%] | 94.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kian Vakili (`KXITFMATCH-26NOV05BICVAK-VAK`) | 0.04 / 0.05 (30) | 4.5% | 8.8% | 29.1% | 16.5% [15.9%-17.5%] | 5.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3719.0, B 173.0; serve-point win A 66.5%, B 44.1%; Elo A 1497.2, B 1201.5; model uncertainty 0.008
* Form inputs: days since last match A 38, B 192; matches on record A 233, B 16; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kaipo Marshall vs Nathan Cox -- M15 Pembroke R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209868:213920:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nathan Cox (`KXITFMATCH-26NOV05MARCOX-COX`) | 0.77 / 0.81 (1615) | 79.0% | 74.2% | 49.5% | 68.5% [65.6%-72.4%] | 76.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.8 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kaipo Marshall (`KXITFMATCH-26NOV05MARCOX-MAR`) | 0.20 / 0.21 (368) | 20.5% | 25.8% | 50.5% | 31.6% [27.6%-34.4%] | 23.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.3 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 365.0, B 418.0; serve-point win A 56.9%, B 38.1%; Elo A 1116.1, B 1287.9; model uncertainty 0.0338
* Form inputs: days since last match A 271, B 360; matches on record A 21, B 7; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Noah Schachter vs Gray Voelzke -- M15 Pembroke R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208132:213882:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Noah Schachter (`KXITFMATCH-26NOV05SCHVOE-SCH`) | 0.85 / 0.87 (167) | 86.0% | 71.9% | 71.3% | 68.7% [66.1%-72.3%] | 83.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -14.1 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gray Voelzke (`KXITFMATCH-26NOV05SCHVOE-VOE`) | 0.13 / 0.15 (23) | 14.0% | 28.1% | 28.7% | 31.3% [27.7%-33.9%] | 16.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +14.1 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2699.0, B 817.0; serve-point win A 66.3%, B 38.4%; Elo A 1243.3, B 1115.5; model uncertainty 0.0311
* Form inputs: days since last match A 192, B 185; matches on record A 184, B 16; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Drew Van Orderlain vs Matt Kuhar -- M15 Pembroke R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132018:208386:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matt Kuhar (`KXITFMATCH-26NOV05VANKUH-KUH`) | 0.79 / 0.81 (388) | 80.0% | 75.9% | 78.2% | 75.0% [70.9%-78.2%] | 76.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.1 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Drew Van Orderlain (`KXITFMATCH-26NOV05VANKUH-VAN`) | 0.19 / 0.20 (25) | 19.5% | 24.1% | 21.8% | 25.0% [21.8%-29.1%] | 23.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +4.6 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1474.0, B 2644.0; serve-point win A 54.0%, B 40.7%; Elo A 1084.0, B 1249.2; model uncertainty 0.0367
* Form inputs: days since last match A 192, B 192; matches on record A 73, B 138; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

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
| Appleton / Zaar (`KXITFWDOUBLES-26NOV05APPZAADALJUD-APPZAA`) | 0.50 / 0.73 (210) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dal / Judith Visscher (`KXITFWDOUBLES-26NOV05APPZAADALJUD-DALJUD`) | 0.33 / 0.35 (38) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Melissa Boyden vs Fernanda Labrana -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:219625:222274:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Melissa Boyden (`KXITFWMATCH-26NOV05BOYLAB-BOY`) | 0.04 / 0.05 (171) | 4.5% | 9.1% | 3.1% | 11.2% [6.4%-20.3%] | 6.3% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +4.6 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Fernanda Labrana (`KXITFWMATCH-26NOV05BOYLAB-LAB`) | 0.95 / 0.96 (324) | 95.5% | 90.9% | 96.9% | 88.8% [79.7%-93.6%] | 93.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.6 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 765.0, B 2901.0; serve-point win A 47.4%, B 42.6%; Elo A 1254.1, B 1507.9; model uncertainty 0.0698
* Form inputs: days since last match A 206, B 10; matches on record A 91, B 272; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.010, surface_dev_loose -0.015, surface_dev_tight +0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
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

ITF (ITF) · Clay · scheduled 2026-11-05T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206161:237454:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alisa Danilova (`KXITFWMATCH-26NOV05MOYDAN-DAN`) | 0.05 / 0.07 (114) | 6.0% | 6.6% | 4.5% | 12.7% [9.0%-16.7%] | 8.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.6 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luciana Moyano (`KXITFWMATCH-26NOV05MOYDAN-MOY`) | 0.93 / 0.95 (192) | 94.0% | 93.4% | 95.5% | 87.3% [83.3%-91.0%] | 91.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.6 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2452.0, B 466.0; serve-point win A 55.9%, B 55.4%; Elo A 1454.4, B 1180.2; model uncertainty 0.0386
* Form inputs: days since last match A 192, B 192; matches on record A 106, B 31; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.006, surface_dev_loose +0.013, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
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

ITF (ITF) · Clay · scheduled 2026-11-05T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:254733:269847:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zoe Doldan (`KXITFWMATCH-26NOV05VERDOL-DOL`) | 0.07 / 0.09 (2068) | 8.0% | 4.1% | 29.1% | 16.7% [16.0%-16.7%] | 8.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Antonia Vergara Rivera (`KXITFWMATCH-26NOV05VERDOL-VER`) | 0.92 / 0.93 (92) | 92.5% | 95.9% | 70.9% | 83.3% [83.3%-84.0%] | 91.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.4 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 3116.0, B 0.0; serve-point win A 57.7%, B 55.2%; Elo A 1525.0, B 1244.4; model uncertainty 0.0034
* Form inputs: days since last match A 8, B 745; matches on record A 99, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.007, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nicolai Budkov Kjaer vs Kimmer Coppejans -- ATP Challenger Bratislava II R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 20:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-05T20:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106293:149282:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolai Budkov Kjaer (`KXATPCHALLENGERMATCH-26NOV05BUDCOP-BUD`) | 0.72 / 0.73 (1151) | 72.5% | 58.5% | 49.0% | 49.0% [47.4%-49.5%] | 71.6% | 72.2% | 72.2% | MODEL_LONE_OUTLIER | PASS | -14.0 pp | REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Kimmer Coppejans (`KXATPCHALLENGERMATCH-26NOV05BUDCOP-COP`) | 0.27 / 0.28 (1583) | 27.5% | 41.5% | 51.0% | 51.0% [50.5%-52.6%] | 28.4% | 28.0% | 28.0% | MODEL_LONE_OUTLIER | WATCH | +14.0 pp | REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4323.0, B 4985.0; serve-point win A 59.4%, B 42.3%; Elo A 1677.7, B 1685.3; model uncertainty 0.0104
* Form inputs: days since last match A 10, B 19; matches on record A 182, B 895; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Daniel Milavsky vs Max Hans Rehberg -- ATP Challenger Charlottesville R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 20:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-05T20:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208819:212251:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Milavsky (`KXATPCHALLENGERMATCH-26NOV05MILREH-MIL`) | 0.46 / 0.47 (1635) | 46.5% | 45.7% | 52.9% | 50.5% [45.1%-52.9%] | 46.9% | 47.7% | 47.3% | MODEL_LONE_OUTLIER | WATCH | -0.8 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Max Hans Rehberg (`KXATPCHALLENGERMATCH-26NOV05MILREH-REH`) | 0.53 / 0.54 (2639) | 53.5% | 54.3% | 47.0% | 49.5% [47.0%-54.9%] | 53.1% | 52.5% | 52.8% | MODEL_LONE_OUTLIER | PASS | +0.8 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3885.0, B 3984.0; serve-point win A 64.7%, B 34.4%; Elo A 1557.6, B 1604.4; model uncertainty 0.0394
* Form inputs: days since last match A 10, B 10; matches on record A 124, B 260; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.025, surface_pool_high +0.025, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Miguel Angel Reyes-Varela / Reese Stalder vs Geoffrey Blancaneaux / Michael Zheng -- ATP Challenger Charlottesville QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 20:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-05T20:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05REYSTABLAZHE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Geoffrey Blancaneaux / Michael Zheng (`KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE`) | 0.18 / 0.26 (32) | 22.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Miguel Angel Reyes-Varela / Reese Stalder (`KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-REYSTA`) | 0.63 / 0.77 (87) | 70.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

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
| Charvatova / Munzarova (`KXITFWDOUBLES-26NOV05CHAMUNKOVKRE-CHAMUN`) | 0.05 / 0.87 (400) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kovackova / Krejcova (`KXITFWDOUBLES-26NOV05CHAMUNKOVKRE-KOVKRE`) | 0.86 / 0.90 (1) | 88.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dalma Galfi vs Amandine Hesse -- W75 Petange R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:203281:213646:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dalma Galfi (`KXITFWMATCH-26NOV05GALHES-GAL`) | 0.75 / 0.78 (2) | 76.5% | 81.0% | 73.4% | 72.5% [69.8%-74.2%] | 75.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.5 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amandine Hesse (`KXITFWMATCH-26NOV05GALHES-HES`) | 0.22 / 0.23 (25) | 22.5% | 19.0% | 26.7% | 27.5% [25.8%-30.2%] | 24.7% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -3.5 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4440.0, B 2021.0; serve-point win A 59.1%, B 47.6%; Elo A 1730.1, B 1575.8; model uncertainty 0.0223
* Form inputs: days since last match A 9, B 25; matches on record A 631, B 777; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.017, surface_pool_high -0.027, surface_dev_loose -0.009, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Efremova / Meshcheryakova vs Kurt / Medvedeva -- W15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 20:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T20:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05EFRMESKURMED:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Efremova / Meshcheryakova (`KXITFWDOUBLES-26NOV05EFRMESKURMED-EFRMES`) | 0.01 / 0.90 (1) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kurt / Medvedeva (`KXITFWDOUBLES-26NOV05EFRMESKURMED-KURMED`) | 0.01 / 0.90 (1) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sedenkova / Shmeleva vs Abouelsaad / Wildgruber -- W15 Sharm ElSheikh QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 20:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T20:40:33Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05SEDSHMABOWIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Abouelsaad / Wildgruber (`KXITFWDOUBLES-26NOV05SEDSHMABOWIL-ABOWIL`) | 0.45 / 0.89 (8) | 67.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sedenkova / Shmeleva (`KXITFWDOUBLES-26NOV05SEDSHMABOWIL-SEDSHM`) | 0.35 / 0.90 (1) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Julian Alonso vs Ryan Cozad -- M15 Hilton Head Island SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:103031:213743:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julian Alonso (`KXITFMATCH-26NOV05ALOCOZ-ALO`) | 0.60 / 0.64 (34) | 62.0% | 78.1% | 56.1% | 82.1% [80.0%-83.6%] | -- | -- | -- | -- | PASS | +16.1 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ryan Cozad (`KXITFMATCH-26NOV05ALOCOZ-COZ`) | 0.36 / 0.37 (139) | 36.5% | 21.9% | 43.9% | 17.9% [16.4%-20.0%] | -- | -- | -- | -- | PASS | -14.6 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 791.0, B 157.0; serve-point win A 64.6%, B 41.5%; Elo A 1515.0, B 1228.1; model uncertainty 0.0178
* Form inputs: days since last match A 304, B 206; matches on record A 376, B 3; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV05ALOCOZ-ALO  (YES = Julian Alonso)
Model: 78%
Kalshi: 62%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexander Bernard vs Jacob Brumm -- M15 Pembroke R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:134276:209060:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Bernard (`KXITFMATCH-26NOV05BERBRU-BER`) | 0.55 / 0.58 (278) | 56.5% | 59.7% | 57.3% | 57.3% [57.3%-58.3%] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.2 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jacob Brumm (`KXITFMATCH-26NOV05BERBRU-BRU`) | 0.40 / 0.41 (42) | 40.5% | 40.3% | 42.7% | 42.7% [41.7%-42.7%] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.2 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 733.0, B 2191.0; serve-point win A 59.4%, B 42.4%; Elo A 1377.3, B 1319.0; model uncertainty 0.005
* Form inputs: days since last match A 360, B 192; matches on record A 104, B 213; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Giovanni Branchetti vs Benjamin Torrealba -- M15 Salvador QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05BRATOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giovanni Branchetti (`KXITFMATCH-26NOV05BRATOR-BRA`) | 0.47 / 0.48 (48) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Benjamin Torrealba (`KXITFMATCH-26NOV05BRATOR-TOR`) | 0.49 / 0.51 (141) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Thiago Cigarran / Lucio Ratti vs Ryan Nijboer / Oriol Roca Batalla -- ATP Challenger Villa Maria QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-05T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05CIGRATNIJROC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thiago Cigarran / Lucio Ratti (`KXATPCHALLENGERDOUBLES-26NOV05CIGRATNIJROC-CIGRAT`) | 0.33 / 0.38 (32) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ryan Nijboer / Oriol Roca Batalla (`KXATPCHALLENGERDOUBLES-26NOV05CIGRATNIJROC-NIJROC`) | 0.60 / 0.64 (30) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Ryan Colby vs Santiago Giamichelle -- M15 Hilton Head Island SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210242:213839:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ryan Colby (`KXITFMATCH-26NOV05COLGIA-COL`) | 0.67 / 0.70 (158) | 68.5% | 75.0% | 61.0% | 66.5% [65.5%-67.2%] | 68.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.5 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Santiago Giamichelle (`KXITFMATCH-26NOV05COLGIA-GIA`) | 0.30 / 0.32 (102) | 31.0% | 25.0% | 39.0% | 33.5% [32.8%-34.5%] | 31.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.0 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1404.0, B 263.0; serve-point win A 58.1%, B 47.0%; Elo A 1337.1, B 1212.3; model uncertainty 0.0086
* Form inputs: days since last match A 192, B 346; matches on record A 39, B 5; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Felix Corwin vs Clement Lemire -- M15 Hilton Head Island SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200228:212750:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felix Corwin (`KXITFMATCH-26NOV05CORLEM-COR`) | 0.45 / 0.48 (259) | 46.5% | 69.2% | 53.7% | 66.7% [64.9%-68.1%] | 47.1% | -- | 47.1% | MODEL_LONE_OUTLIER | PASS | +22.6 pp | HIGH_REVIEW | STALE | F / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Clement Lemire (`KXITFMATCH-26NOV05CORLEM-LEM`) | 0.52 / 0.53 (168) | 52.5% | 30.9% | 46.3% | 33.3% [31.9%-35.1%] | 52.9% | -- | 52.9% | MODEL_LONE_OUTLIER | PASS | -21.6 pp | HIGH_REVIEW | STALE | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3058.0, B 177.0; serve-point win A 59.8%, B 44.0%; Elo A 1415.5, B 1282.5; model uncertainty 0.016
* Form inputs: days since last match A 206, B 367; matches on record A 371, B 6; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV05CORLEM-COR  (YES = Felix Corwin)
Model: 69%
Kalshi: 46%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_KALSHI
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Facundo Diaz Acosta vs Filip Misolic -- ATP Challenger Costa do Sauipe R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-05T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207680:209209:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Facundo Diaz Acosta (`KXATPCHALLENGERMATCH-26NOV05DIAMIS-DIA`) | 0.70 / 0.71 (378) | 70.5% | 60.4% | 78.2% | 71.2% [64.2%-74.6%] | 68.8% | 70.0% | 70.0% | MODEL_LONE_OUTLIER | PASS | -10.1 pp | REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Filip Misolic (`KXATPCHALLENGERMATCH-26NOV05DIAMIS-MIS`) | 0.29 / 0.30 (2526) | 29.5% | 39.6% | 21.8% | 28.8% [25.4%-35.8%] | 31.2% | 30.2% | 30.2% | MODEL_LONE_OUTLIER | PASS | +10.1 pp | REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5488.0, B 3412.0; serve-point win A 60.4%, B 41.6%; Elo A 1835.0, B 1817.6; model uncertainty 0.0521
* Form inputs: days since last match A 15, B 17; matches on record A 468, B 330; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.004, surface_dev_loose -0.004, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Jeffrey Fradkin vs Keshav Chopra -- M15 Pembroke R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208844:213376:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Keshav Chopra (`KXITFMATCH-26NOV05FRACHO-CHO`) | 0.89 / 0.90 (2277) | 89.5% | 74.0% | 53.0% | 59.6% [58.1%-61.1%] | 86.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.5 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jeffrey Fradkin (`KXITFMATCH-26NOV05FRACHO-FRA`) | 0.09 / 0.12 (85) | 10.5% | 26.0% | 46.9% | 40.5% [38.9%-41.9%] | 13.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +15.5 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 804.0, B 1264.0; serve-point win A 59.3%, B 35.6%; Elo A 1145.1, B 1232.7; model uncertainty 0.0152
* Form inputs: days since last match A 192, B 73; matches on record A 13, B 89; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV05FRACHO-FRA  (YES = Jeffrey Fradkin)
Model: 26%
Kalshi: 10%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Joao Vitor Goncalves Ceolin vs Victor Bini -- M15 Salvador QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:205825:212192:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Victor Bini (`KXITFMATCH-26NOV05GONBIN-BIN`) | 0.22 / 0.25 (99) | 23.5% | 22.2% | 23.6% | 32.4% [28.7%-34.8%] | 26.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Joao Vitor Goncalves Ceolin (`KXITFMATCH-26NOV05GONBIN-GON`) | 0.73 / 0.76 (2322) | 74.5% | 77.8% | 76.4% | 67.6% [65.2%-71.3%] | 73.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1926.0, B 418.0; serve-point win A 61.4%, B 44.5%; Elo A 1246.4, B 1138.8; model uncertainty 0.0305
* Form inputs: days since last match A 192, B 192; matches on record A 66, B 11; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.005, surface_dev_loose +0.009, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gavin Goode vs Johan Alexander Rodriguez -- M15 Hilton Head Island SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05GOOROD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gavin Goode (`KXITFMATCH-26NOV05GOOROD-GOO`) | 0.30 / 0.32 (197) | 31.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Johan Alexander Rodriguez (`KXITFMATCH-26NOV05GOOROD-ROD`) | 0.67 / 0.69 (101) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Johan Oscar Lien vs Rodrigo Fernandes -- M15 Trois-Rivières R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212075:214231:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rodrigo Fernandes (`KXITFMATCH-26NOV05LIEFER-FER`) | 0.65 / 0.68 (894) | 66.5% | 47.2% | 53.1% | 46.4% [43.8%-47.9%] | 65.2% | -- | 65.2% | MODEL_LONE_OUTLIER | PASS | -19.3 pp | HIGH_REVIEW | STALE | F / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Johan Oscar Lien (`KXITFMATCH-26NOV05LIEFER-LIE`) | 0.31 / 0.34 (146) | 32.5% | 52.8% | 46.9% | 53.6% [52.1%-56.2%] | 34.8% | -- | 34.8% | KALSHI_LONE_OUTLIER | PASS | +20.3 pp | HIGH_REVIEW | STALE | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 812.0, B 685.0; serve-point win A 59.4%, B 41.2%; Elo A 1275.6, B 1228.2; model uncertainty 0.0207
* Form inputs: days since last match A 213, B 444; matches on record A 15, B 37; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV05LIEFER-LIE  (YES = Johan Oscar Lien)
Model: 53%
Kalshi: 32%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_KALSHI
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eduardo Ribeiro / Natan Rodrigues vs Federico Zeballos / Marcelo Zormann -- ATP Challenger Costa do Sauipe QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-05T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05RIBRODZEBZOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eduardo Ribeiro / Natan Rodrigues (`KXATPCHALLENGERDOUBLES-26NOV05RIBRODZEBZOR-RIBROD`) | 0.32 / 0.51 (41) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Federico Zeballos / Marcelo Zormann (`KXATPCHALLENGERDOUBLES-26NOV05RIBRODZEBZOR-ZEBZOR`) | 0.53 / 0.64 (56) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Tariq Simons vs Rohan Sachdev -- M15 Pembroke R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05SIMSAC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rohan Sachdev (`KXITFMATCH-26NOV05SIMSAC-SAC`) | 0.75 / 0.76 (254) | 75.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tariq Simons (`KXITFMATCH-26NOV05SIMSAC-SIM`) | 0.25 / 0.26 (270) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kacper Szymkowiak vs Carel Aubriel Ngounoue -- M15 Pembroke R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05SZYNGO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carel Aubriel Ngounoue (`KXITFMATCH-26NOV05SZYNGO-NGO`) | 0.10 / 0.13 (5) | 11.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kacper Szymkowiak (`KXITFMATCH-26NOV05SZYNGO-SZY`) | 0.85 / 0.90 (898) | 87.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aadarsh Tripathi vs Maxime St-Hilaire -- M15 Trois-Rivières R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212636:213020:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maxime St-Hilaire (`KXITFMATCH-26NOV05TRISTH-STH`) | 0.41 / 0.44 (125) | 42.5% | 28.5% | 43.8% | 34.8% [34.7%-35.8%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -14.0 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aadarsh Tripathi (`KXITFMATCH-26NOV05TRISTH-TRI`) | 0.55 / 0.58 (21) | 56.5% | 71.5% | 56.2% | 65.2% [64.2%-65.3%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +15.0 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 259.0, B 163.0; serve-point win A 61.1%, B 43.2%; Elo A 1305.3, B 1192.9; model uncertainty 0.0056
* Form inputs: days since last match A 444, B 192; matches on record A 9, B 4; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV05TRISTH-TRI  (YES = Aadarsh Tripathi)
Model: 72%
Kalshi: 56%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yara Bartashevich vs Dasha Ivanova -- W35 Orlando FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05BARIVA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yara Bartashevich (`KXITFWMATCH-26NOV05BARIVA-BAR`) | 0.69 / 0.72 (5) | 70.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dasha Ivanova (`KXITFWMATCH-26NOV05BARIVA-IVA`) | 0.27 / 0.29 (105) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Scarlett Fagan vs Abigail Haile -- W15 Hilton Head Island SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05FAGHAI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Scarlett Fagan (`KXITFWMATCH-26NOV05FAGHAI-FAG`) | 0.64 / 0.69 (39) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Abigail Haile (`KXITFWMATCH-26NOV05FAGHAI-HAI`) | 0.31 / 0.34 (55) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Evialina Laskevich vs Aspen Schuman -- W35 Orlando FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222184:260767:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Evialina Laskevich (`KXITFWMATCH-26NOV05LASSCH-LAS`) | 0.74 / 0.76 (2692) | 75.0% | 70.9% | 26.5% | 60.6% [48.4%-73.1%] | 74.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.1 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aspen Schuman (`KXITFWMATCH-26NOV05LASSCH-SCH`) | 0.23 / 0.26 (132) | 24.5% | 29.1% | 73.5% | 39.5% [26.9%-51.6%] | 25.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.6 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 737.0, B 437.0; serve-point win A 55.7%, B 48.4%; Elo A 1625.6, B 1474.8; model uncertainty 0.1234
* Form inputs: days since last match A 262, B 360; matches on record A 167, B 46; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.035, surface_pool_high -0.031, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anita Sahdiieva vs Juliana Nicole Singeorzan -- W15 Hilton Head Island SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221370:270414:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anita Sahdiieva (`KXITFWMATCH-26NOV05SAHSIN-SAH`) | 0.78 / 0.81 (6) | 79.5% | 88.4% | 67.5% | 70.8% [70.3%-72.1%] | -- | -- | -- | -- | PASS | +8.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Juliana Nicole Singeorzan (`KXITFWMATCH-26NOV05SAHSIN-SIN`) | 0.17 / 0.20 (61) | 18.5% | 11.6% | 32.5% | 29.2% [27.9%-29.7%] | -- | -- | -- | -- | PASS | -6.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1325.0, B 123.0; serve-point win A 58.8%, B 50.2%; Elo A 1394.6, B 1242.1; model uncertainty 0.0091
* Form inputs: days since last match A 192, B 262; matches on record A 111, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Margaret Sohns vs Ashley Lahey -- W15 Hilton Head Island SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216076:269734:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ashley Lahey (`KXITFWMATCH-26NOV05SOHLAH-LAH`) | 0.94 / 0.95 (199) | 94.5% | 95.9% | 75.9% | 88.4% [87.0%-89.5%] | 93.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.4 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Margaret Sohns (`KXITFWMATCH-26NOV05SOHLAH-SOH`) | 0.05 / 0.07 (1843) | 6.0% | 4.1% | 24.1% | 11.6% [10.5%-13.0%] | 6.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 287.0, B 1883.0; serve-point win A 48.9%, B 37.9%; Elo A 1245.7, B 1627.6; model uncertainty 0.0122
* Form inputs: days since last match A 213, B 416; matches on record A 9, B 239; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jantje Tilbuerger vs Jensen Diianni -- W15 Hilton Head Island SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221172:270383:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jensen Diianni (`KXITFWMATCH-26NOV05TILDII-DII`) | 0.18 / 0.20 (40) | 19.0% | 17.5% | 33.4% | 21.8% [21.1%-21.9%] | 24.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.5 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Jantje Tilbuerger (`KXITFWMATCH-26NOV05TILDII-TIL`) | 0.76 / 0.81 (64) | 78.5% | 82.5% | 66.6% | 78.2% [78.1%-78.9%] | 75.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.0 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 180.0; serve-point win A 54.9%, B 52.0%; Elo A 1524.6, B 1299.6; model uncertainty 0.0037
* Form inputs: days since last match A 1032, B 262; matches on record A 191, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vivian Wolff vs Edda Mamedova -- W35 Orlando FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215386:239422:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Edda Mamedova (`KXITFWMATCH-26NOV05WOLMAM-MAM`) | 0.38 / 0.41 (134) | 39.5% | 28.7% | 51.1% | 35.8% [28.7%-43.6%] | 40.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -10.8 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Vivian Wolff (`KXITFWMATCH-26NOV05WOLMAM-WOL`) | 0.60 / 0.61 (240) | 60.5% | 71.3% | 48.9% | 64.2% [56.4%-71.3%] | 59.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +10.8 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2229.0, B 879.0; serve-point win A 52.8%, B 51.4%; Elo A 1638.5, B 1473.3; model uncertainty 0.0746
* Form inputs: days since last match A 37, B 262; matches on record A 284, B 91; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.010, surface_dev_loose +0.015, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tom Hands / Matthew Summers vs Jarno Jans / Joran Vliegen -- ATP Challenger Charlottesville QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 21:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-05T21:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05HANSUMJANVLI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tom Hands / Matthew Summers (`KXATPCHALLENGERDOUBLES-26NOV05HANSUMJANVLI-HANSUM`) | 0.33 / 0.91 (55) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jarno Jans / Joran Vliegen (`KXATPCHALLENGERDOUBLES-26NOV05HANSUMJANVLI-JANVLI`) | 0.52 / 0.89 (100) | 70.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Maks Kasnikowski vs Michael Antonius -- ATP Challenger Charlottesville R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 21:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-05T21:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209874:214004:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michael Antonius (`KXATPCHALLENGERMATCH-26NOV05KASANT-ANT`) | 0.29 / 0.30 (49) | 29.5% | 24.7% | 21.3% | 24.0% [21.7%-25.6%] | 30.3% | 29.5% | 29.9% | MODEL_LONE_OUTLIER | PASS | -4.8 pp | NORMAL | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Maks Kasnikowski (`KXATPCHALLENGERMATCH-26NOV05KASANT-KAS`) | 0.69 / 0.71 (3525) | 70.0% | 75.3% | 78.7% | 76.0% [74.5%-78.3%] | 69.7% | 71.2% | 70.4% | MODEL_LONE_OUTLIER | WATCH | +5.3 pp | NORMAL | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4928.0, B 1258.0; serve-point win A 65.5%, B 40.0%; Elo A 1620.4, B 1433.8; model uncertainty 0.0194
* Form inputs: days since last match A 10, B 71; matches on record A 327, B 21; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.023, surface_pool_high -0.016, surface_dev_loose -0.005, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; STALE_QUOTE

## Gajdosova / Petruzelova vs Lovric / Paganetti -- W35 Liberec QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05GAJPETLOVPAG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gajdosova / Petruzelova (`KXITFWDOUBLES-26NOV05GAJPETLOVPAG-GAJPET`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lovric / Paganetti (`KXITFWDOUBLES-26NOV05GAJPETLOVPAG-LOVPAG`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hodzic / Wagner vs Johanna Brockmann / Seidel -- W75 Petange QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05HODWAGJOHSEI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hodzic / Wagner (`KXITFWDOUBLES-26NOV05HODWAGJOHSEI-HODWAG`) | 0.15 / 0.30 (35) | 22.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Johanna Brockmann / Seidel (`KXITFWDOUBLES-26NOV05HODWAGJOHSEI-JOHSEI`) | 0.65 / 0.82 (138) | 73.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Nagy / Zelnickova vs Stusek / Zoldakova -- W35 Liberec QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05NAGZELSTUZOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nagy / Zelnickova (`KXITFWDOUBLES-26NOV05NAGZELSTUZOL-NAGZEL`) | 0.38 / 0.65 (4) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stusek / Zoldakova (`KXITFWDOUBLES-26NOV05NAGZELSTUZOL-STUZOL`) | 0.41 / 0.45 (45) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tomasz Berkieta vs Bor Artnak -- M25 Harlingen TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210107:211530:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bor Artnak (`KXITFMATCH-26NOV05BERART-ART`) | 0.49 / 0.52 (240) | 50.5% | 53.6% | 49.5% | 53.6% [52.1%-54.6%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.1 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tomasz Berkieta (`KXITFMATCH-26NOV05BERART-BER`) | 0.47 / 0.51 (294) | 49.0% | 46.4% | 50.5% | 46.4% [45.4%-47.9%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.6 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1958.0, B 3186.0; serve-point win A 59.0%, B 40.3%; Elo A 1410.9, B 1469.8; model uncertainty 0.0129
* Form inputs: days since last match A 10, B 48; matches on record A 119, B 251; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Theodore Dean vs Romain Gales -- M15 Trois-Rivières R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209273:213932:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theodore Dean (`KXITFMATCH-26NOV05DEAGAL-DEA`) | 0.59 / 0.61 (311) | 60.0% | 60.4% | 53.2% | 64.4% [62.0%-67.2%] | 58.1% | -- | 58.1% | MODEL_LONE_OUTLIER | PASS | +0.4 pp | NORMAL | STALE | F / POOR | ALL_AGREE | VERIFIED |
| Romain Gales (`KXITFMATCH-26NOV05DEAGAL-GAL`) | 0.39 / 0.40 (142) | 39.5% | 39.6% | 46.8% | 35.6% [32.8%-38.0%] | 41.9% | -- | 41.9% | ALL_THREE_DISAGREE | PASS | +0.1 pp | NORMAL | STALE | F / POOR | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 1263.0, B 551.0; serve-point win A 57.4%, B 44.6%; Elo A 1424.3, B 1287.8; model uncertainty 0.0263
* Form inputs: days since last match A 304, B 402; matches on record A 21, B 17; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Raul Garcia vs Max Sheldon -- M15 Hilton Head Island SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207881:210376:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raul Garcia (`KXITFMATCH-26NOV05GARSHE-GAR`) | 0.52 / 0.53 (55) | 52.5% | 45.6% | 36.7% | 44.8% [42.7%-45.9%] | 55.2% | -- | 55.2% | ALL_THREE_DISAGREE | PASS | -6.8 pp | NORMAL | STALE | F / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Max Sheldon (`KXITFMATCH-26NOV05GARSHE-SHE`) | 0.45 / 0.48 (75) | 46.5% | 54.4% | 63.3% | 55.2% [54.1%-57.3%] | 44.8% | -- | 44.8% | MODEL_LONE_OUTLIER | PASS | +7.8 pp | NORMAL | STALE | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 203.0, B 264.0; serve-point win A 57.7%, B 41.5%; Elo A 1212.0, B 1237.2; model uncertainty 0.016
* Form inputs: days since last match A 269, B 521; matches on record A 19, B 13; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vignesh Gogineni vs William Mirarchi -- M15 Hilton Head Island SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213818:213987:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vignesh Gogineni (`KXITFMATCH-26NOV05GOGMIR-GOG`) | 0.74 / 0.76 (59) | 75.0% | 61.2% | 66.8% | 62.9% [62.2%-65.0%] | 73.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.8 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| William Mirarchi (`KXITFMATCH-26NOV05GOGMIR-MIR`) | 0.23 / 0.25 (267) | 24.0% | 38.8% | 33.2% | 37.1% [35.0%-37.8%] | 26.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +14.8 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 277.0, B 228.0; serve-point win A 58.3%, B 43.8%; Elo A 1402.2, B 1311.5; model uncertainty 0.0137
* Form inputs: days since last match A 86, B 318; matches on record A 6, B 5; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jordan Lee vs Keaton Hance -- M25 Harlingen TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213825:214265:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Keaton Hance (`KXITFMATCH-26NOV05LEEHAN-HAN`) | 0.36 / 0.37 (1) | 36.5% | 58.7% | 58.3% | 48.9% [47.9%-51.0%] | 38.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +22.2 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jordan Lee (`KXITFMATCH-26NOV05LEEHAN-LEE`) | 0.61 / 0.62 (165) | 61.5% | 41.3% | 41.7% | 51.0% [48.9%-52.1%] | 61.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -20.2 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 160.0, B 777.0; serve-point win A 57.4%, B 40.9%; Elo A 1323.6, B 1311.3; model uncertainty 0.0156
* Form inputs: days since last match A 71, B 45; matches on record A 6, B 22; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV05LEEHAN-HAN  (YES = Keaton Hance)
Model: 59%
Kalshi: 36%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Henry Lieberman vs Dragos Cazacu -- M15 Hilton Head Island SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05LIECAZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dragos Cazacu (`KXITFMATCH-26NOV05LIECAZ-CAZ`) | 0.70 / 0.74 (749) | 72.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Henry Lieberman (`KXITFMATCH-26NOV05LIECAZ-LIE`) | 0.27 / 0.30 (704) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bryce Nakashima vs Togan Tokac -- M25 Harlingen TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210416:210485:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bryce Nakashima (`KXITFMATCH-26NOV05NAKTOK-NAK`) | 0.89 / 0.91 (37) | 90.0% | 80.1% | 56.6% | 65.0% [63.5%-65.9%] | 88.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Togan Tokac (`KXITFMATCH-26NOV05NAKTOK-TOK`) | 0.09 / 0.12 (824) | 10.5% | 19.9% | 43.4% | 35.0% [34.1%-36.4%] | 11.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +9.4 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 491.0, B 53.0; serve-point win A 64.2%, B 42.4%; Elo A 1302.9, B 1196.1; model uncertainty 0.0119
* Form inputs: days since last match A 10, B 101; matches on record A 47, B 4; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.014, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eliot Nobel vs Mikael Arseneault -- M15 Trois-Rivières R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212530:214052:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mikael Arseneault (`KXITFMATCH-26NOV05NOBARS-ARS`) | 0.75 / 0.77 (402) | 76.0% | 64.2% | 52.6% | 48.9% [48.9%-50.0%] | 73.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.8 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Eliot Nobel (`KXITFMATCH-26NOV05NOBARS-NOB`) | 0.22 / 0.23 (132) | 22.5% | 35.8% | 47.4% | 51.0% [50.0%-51.0%] | 26.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.3 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 63.0, B 759.0; serve-point win A 56.3%, B 40.9%; Elo A 1258.3, B 1251.9; model uncertainty 0.0053
* Form inputs: days since last match A 451, B 108; matches on record A 1, B 33; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anuj Watane vs Noah Lopez Cherubino -- M15 Hilton Head Island SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212106:214482:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Noah Lopez Cherubino (`KXITFMATCH-26NOV05WATLOP-LOP`) | 0.75 / 0.78 (286) | 76.5% | 58.5% | 53.1% | 45.9% [45.9%-46.9%] | 74.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -18.0 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anuj Watane (`KXITFMATCH-26NOV05WATLOP-WAT`) | 0.21 / 0.23 (164) | 22.0% | 41.5% | 46.9% | 54.1% [53.1%-54.1%] | 25.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +19.5 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 69.0, B 888.0; serve-point win A 59.3%, B 39.1%; Elo A 1253.6, B 1229.1; model uncertainty 0.0051
* Form inputs: days since last match A 234, B 353; matches on record A 1, B 16; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV05WATLOP-WAT  (YES = Anuj Watane)
Model: 41%
Kalshi: 22%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Noah Zamora vs Aidan Mchugh -- M25 Harlingen TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202420:212235:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aidan Mchugh (`KXITFMATCH-26NOV05ZAMMCH-MCH`) | 0.67 / 0.70 (595) | 68.5% | 65.5% | 65.6% | 63.7% [61.7%-65.1%] | 67.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.0 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Noah Zamora (`KXITFMATCH-26NOV05ZAMMCH-ZAM`) | 0.30 / 0.34 (411) | 32.0% | 34.5% | 34.4% | 36.3% [34.9%-38.3%] | 32.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.5 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1609.0, B 3842.0; serve-point win A 58.2%, B 38.7%; Elo A 1410.4, B 1488.7; model uncertainty 0.0172
* Form inputs: days since last match A 220, B 304; matches on record A 41, B 477; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose +0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luciana Agudelo vs Josefina Estevez -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260717:270250:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luciana Agudelo (`KXITFWMATCH-26NOV05AGUEST-AGU`) | 0.02 / 0.03 (124) | 2.5% | 33.9% | 29.1% | 44.6% [41.5%-45.7%] | 4.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +31.4 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Josefina Estevez (`KXITFWMATCH-26NOV05AGUEST-EST`) | 0.96 / 0.98 (1761) | 97.0% | 66.1% | 70.9% | 55.4% [54.3%-58.5%] | 95.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -30.9 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 79.0, B 732.0; serve-point win A 47.3%, B 49.6%; Elo A 1262.7, B 1294.6; model uncertainty 0.0211
* Form inputs: days since last match A 374, B 297; matches on record A 2, B 55; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05AGUEST-AGU  (YES = Luciana Agudelo)
Model: 34%
Kalshi: 2%
Gap: +31 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.011, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lani Chang vs Dia Evtimova -- W15 Hilton Head Island SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:201691:270091:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lani Chang (`KXITFWMATCH-26NOV05CHAEVT-CHA`) | 0.91 / 0.93 (255) | 92.0% | 73.5% | 72.2% | 62.6% [60.6%-65.6%] | 89.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -18.5 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dia Evtimova (`KXITFWMATCH-26NOV05CHAEVT-EVT`) | 0.07 / 0.10 (1074) | 8.5% | 26.5% | 27.8% | 37.4% [34.4%-39.4%] | 11.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +18.0 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 310.0, B 654.0; serve-point win A 54.6%, B 50.1%; Elo A 1365.9, B 1288.6; model uncertainty 0.0254
* Form inputs: days since last match A 206, B 199; matches on record A 9, B 1039; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05CHAEVT-EVT  (YES = Dia Evtimova)
Model: 27%
Kalshi: 8%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aya El Aouni vs Charlotte Narti -- W15 Hilton Head Island SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223671:270203:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aya El Aouni (`KXITFWMATCH-26NOV05ELANAR-ELA`) | 0.70 / 0.72 (1) | 71.0% | 87.0% | 55.3% | 70.8% [69.0%-73.0%] | 70.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +16.0 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Charlotte Narti (`KXITFWMATCH-26NOV05ELANAR-NAR`) | 0.26 / 0.29 (43) | 27.5% | 13.0% | 44.7% | 29.2% [27.0%-31.0%] | 29.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -14.5 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 211.0, B 300.0; serve-point win A 57.5%, B 50.9%; Elo A 1481.8, B 1309.0; model uncertainty 0.0204
* Form inputs: days since last match A 535, B 199; matches on record A 111, B 6; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05ELANAR-ELA  (YES = Aya El Aouni)
Model: 87%
Kalshi: 71%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kallista Liu vs Ciara Harding -- W15 Hilton Head Island SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264180:270321:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ciara Harding (`KXITFWMATCH-26NOV05LIUHAR-HAR`) | 0.24 / 0.25 (133) | 24.5% | 27.5% | 56.9% | 45.7% [44.7%-45.7%] | 28.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.0 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kallista Liu (`KXITFWMATCH-26NOV05LIUHAR-LIU`) | 0.73 / 0.74 (61) | 73.5% | 72.5% | 43.1% | 54.3% [54.3%-55.3%] | 72.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.0 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1064.0, B 75.0; serve-point win A 55.6%, B 48.9%; Elo A 1295.7, B 1262.2; model uncertainty 0.0053
* Form inputs: days since last match A 213, B 374; matches on record A 41, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yael Saffar vs Emery Combs -- W15 Hilton Head Island SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:270089:270469:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emery Combs (`KXITFWMATCH-26NOV05SAFCOM-COM`) | 0.77 / 0.80 (162) | 78.5% | 57.8% | 59.5% | 55.3% [54.3%-56.4%] | 78.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -20.7 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yael Saffar (`KXITFWMATCH-26NOV05SAFCOM-SAF`) | 0.21 / 0.22 (449) | 21.5% | 42.2% | 40.5% | 44.7% [43.6%-45.7%] | 21.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +20.7 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 288.0, B 528.0; serve-point win A 53.3%, B 45.2%; Elo A 1353.0, B 1384.8; model uncertainty 0.0106
* Form inputs: days since last match A 199, B 199; matches on record A 4, B 8; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05SAFCOM-SAF  (YES = Yael Saffar)
Model: 42%
Kalshi: 22%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofia Simon Padros vs Justina Maria Gonzalez Daniele -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260708:270327:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Justina Maria Gonzalez Daniele (`KXITFWMATCH-26NOV05SIMGON-GON`) | 0.97 / 0.98 (2707) | 97.5% | 92.9% | 85.9% | 75.8% [74.0%-79.4%] | 95.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.6 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sofia Simon Padros (`KXITFWMATCH-26NOV05SIMGON-SIM`) | 0.02 / 0.03 (232) | 2.5% | 7.1% | 14.1% | 24.2% [20.6%-26.0%] | 4.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.6 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 54.0, B 2911.0; serve-point win A 45.6%, B 43.5%; Elo A 1244.6, B 1445.0; model uncertainty 0.0268
* Form inputs: days since last match A 367, B 192; matches on record A 1, B 154; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.017, surface_pool_high -0.024, surface_dev_loose -0.004, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luis Felipe Miguel / Luis Guto Miguel vs Zdenek Kolar / Santiago Rodriguez Taverna -- ATP Challenger Costa do Sauipe QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-05T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05MIGMIGKOLROD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zdenek Kolar / Santiago Rodriguez Taverna (`KXATPCHALLENGERDOUBLES-26NOV05MIGMIGKOLROD-KOLROD`) | 0.40 / 0.44 (35) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luis Felipe Miguel / Luis Guto Miguel (`KXATPCHALLENGERDOUBLES-26NOV05MIGMIGKOLROD-MIGMIG`) | 0.53 / 0.59 (49) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Thiago Monteiro vs Marco Cecchinato -- ATP Challenger Costa do Sauipe R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-05T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106065:106329:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marco Cecchinato (`KXATPCHALLENGERMATCH-26NOV05MONCEC-CEC`) | 0.42 / 0.44 (1509) | 43.0% | 48.8% | 59.3% | 55.9% [51.0%-58.3%] | 42.8% | 43.3% | 43.1% | MODEL_LONE_OUTLIER | SHADOW_BET | +5.8 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Thiago Monteiro (`KXATPCHALLENGERMATCH-26NOV05MONCEC-MON`) | 0.56 / 0.57 (124) | 56.5% | 51.2% | 40.7% | 44.1% [41.7%-49.0%] | 57.2% | 56.9% | 57.0% | MODEL_LONE_OUTLIER | PASS | -5.2 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5161.0, B 5742.0; serve-point win A 64.9%, B 35.4%; Elo A 1715.7, B 1685.2; model uncertainty 0.0366
* Form inputs: days since last match A 17, B 17; matches on record A 948, B 995; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.019, surface_dev_loose -0.005, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Joao Lucas Reis Da Silva vs Elmer Moller -- ATP Challenger Costa do Sauipe R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-05T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206307:209284:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elmer Moller (`KXATPCHALLENGERMATCH-26NOV05REIMOL-MOL`) | 0.61 / 0.62 (133) | 61.5% | 48.0% | 46.9% | 50.0% [47.9%-53.1%] | 62.5% | 62.0% | 62.0% | MODEL_LONE_OUTLIER | PASS | -13.5 pp | REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Joao Lucas Reis Da Silva (`KXATPCHALLENGERMATCH-26NOV05REIMOL-REI`) | 0.38 / 0.39 (2328) | 38.5% | 52.0% | 53.1% | 50.0% [46.9%-52.1%] | 37.5% | 38.4% | 38.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +13.5 pp | REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4979.0, B 4766.0; serve-point win A 57.2%, B 43.2%; Elo A 1668.4, B 1732.1; model uncertainty 0.0263
* Form inputs: days since last match A 10, B 17; matches on record A 483, B 314; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Jo-Yee Chan vs Cadence Brace -- W50 Huamantla R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223335:270125:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cadence Brace (`KXITFWMATCH-26NOV05CHABRA-BRA`) | 0.69 / 0.71 (100) | 70.0% | 88.2% | 76.1% | 78.5% [77.7%-79.3%] | 69.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +18.2 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jo-Yee Chan (`KXITFWMATCH-26NOV05CHABRA-CHA`) | 0.27 / 0.28 (34) | 27.5% | 11.8% | 23.9% | 21.4% [20.7%-22.3%] | 30.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.7 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 531.0, B 2165.0; serve-point win A 48.1%, B 43.0%; Elo A 1410.0, B 1646.4; model uncertainty 0.0079
* Form inputs: days since last match A 458, B 50; matches on record A 8, B 222; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05CHABRA-BRA  (YES = Cadence Brace)
Model: 88%
Kalshi: 70%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.004, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jana Hossam Salah vs Briana Szabo -- W35 Orlando FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223120:266764:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jana Hossam Salah (`KXITFWMATCH-26NOV05HOSSZA-HOS`) | 0.63 / 0.65 (44) | 64.0% | 41.3% | 51.6% | 48.4% [47.9%-49.5%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -22.7 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Briana Szabo (`KXITFWMATCH-26NOV05HOSSZA-SZA`) | 0.34 / 0.37 (115) | 35.5% | 58.7% | 48.4% | 51.6% [50.5%-52.1%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +23.2 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 378.0, B 1762.0; serve-point win A 54.8%, B 43.5%; Elo A 1371.0, B 1384.0; model uncertainty 0.008
* Form inputs: days since last match A 318, B 101; matches on record A 19, B 212; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05HOSSZA-SZA  (YES = Briana Szabo)
Model: 59%
Kalshi: 36%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.005, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofia Johnson vs Jessica Hinojosa Gomez -- W50 Huamantla R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213739:260338:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jessica Hinojosa Gomez (`KXITFWMATCH-26NOV05JOHHIN-HIN`) | 0.12 / 0.14 (55) | 13.0% | 16.2% | 17.4% | 22.6% [18.1%-27.8%] | 17.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +3.2 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sofia Johnson (`KXITFWMATCH-26NOV05JOHHIN-JOH`) | 0.84 / 0.87 (2758) | 85.5% | 83.8% | 82.6% | 77.4% [72.2%-81.9%] | 82.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.7 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1199.0, B 1620.0; serve-point win A 55.5%, B 51.9%; Elo A 1493.3, B 1324.9; model uncertainty 0.0484
* Form inputs: days since last match A 9, B 10; matches on record A 46, B 177; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.004, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lisa Pigato vs Greet Minnen -- W75 Petange R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213889:221354:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Greet Minnen (`KXITFWMATCH-26NOV05PIGMIN-MIN`) | 0.63 / 0.64 (69) | 63.5% | 69.8% | 39.5% | 48.9% [44.2%-59.5%] | 63.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.3 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lisa Pigato (`KXITFWMATCH-26NOV05PIGMIN-PIG`) | 0.33 / 0.36 (100) | 34.5% | 30.2% | 60.5% | 51.1% [40.5%-55.8%] | 36.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -4.3 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4114.0, B 3970.0; serve-point win A 53.9%, B 42.1%; Elo A 1633.3, B 1802.8; model uncertainty 0.0763
* Form inputs: days since last match A 7, B 73; matches on record A 353, B 599; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.005, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Janae Preston vs Brooke Black -- W35 Orlando FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05PREBLA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brooke Black (`KXITFWMATCH-26NOV05PREBLA-BLA`) | 0.26 / 0.29 (0) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Janae Preston (`KXITFWMATCH-26NOV05PREBLA-PRE`) | 0.71 / 0.74 (263) | 72.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lavinia Tanasie vs Whitney Osuigwe -- W35 Orlando FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215992:245094:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Whitney Osuigwe (`KXITFWMATCH-26NOV05TANOSU-OSU`) | 0.82 / 0.85 (395) | 83.5% | 69.0% | 34.4% | 47.9% [39.9%-64.2%] | 82.2% | -- | 82.2% | MODEL_LONE_OUTLIER | PASS | -14.5 pp | REVIEW | STALE | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Lavinia Tanasie (`KXITFWMATCH-26NOV05TANOSU-TAN`) | 0.14 / 0.16 (15) | 15.0% | 31.0% | 65.6% | 52.1% [35.8%-60.1%] | 17.8% | -- | 17.8% | KALSHI_LONE_OUTLIER | PASS | +16.0 pp | HIGH_REVIEW | STALE | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1526.0, B 3327.0; serve-point win A 46.2%, B 50.1%; Elo A 1578.7, B 1663.8; model uncertainty 0.1211
* Form inputs: days since last match A 360, B 53; matches on record A 206, B 400; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05TANOSU-TAN  (YES = Lavinia Tanasie)
Model: 31%
Kalshi: 15%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_KALSHI
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.021, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anastasia Tikhonova vs Valeriya Strakhova -- W50 Huamantla R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211063:221073:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valeriya Strakhova (`KXITFWMATCH-26NOV05TIKSTR-STR`) | 0.25 / 0.28 (28) | 26.5% | 32.7% | 43.6% | 38.5% [35.5%-41.0%] | 27.6% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +6.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anastasia Tikhonova (`KXITFWMATCH-26NOV05TIKSTR-TIK`) | 0.71 / 0.74 (124) | 72.5% | 67.3% | 56.4% | 61.5% [59.0%-64.5%] | 72.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2660.0, B 2323.0; serve-point win A 56.8%, B 46.6%; Elo A 1574.6, B 1432.7; model uncertainty 0.0279
* Form inputs: days since last match A 32, B 6; matches on record A 387, B 770; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.026, surface_pool_high +0.030, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bravo / Vakili vs Gurenko / Peter Van Noord -- M15 Pembroke QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05BRAVAKGURPET:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bravo / Vakili (`KXITFDOUBLES-26NOV05BRAVAKGURPET-BRAVAK`) | 0.04 / 0.20 (31) | 12.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gurenko / Peter Van Noord (`KXITFDOUBLES-26NOV05BRAVAKGURPET-GURPET`) | 0.58 / 0.90 (1) | 74.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Federico Coria vs Valerio Aboian -- ATP Challenger Villa Maria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-05T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105948:209254:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valerio Aboian (`KXATPCHALLENGERMATCH-26NOV05CORABO-ABO`) | 0.53 / 0.54 (2858) | 53.5% | 46.4% | 49.5% | 43.2% [40.1%-45.8%] | 52.0% | 52.8% | 52.8% | MODEL_LONE_OUTLIER | PASS | -7.1 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Federico Coria (`KXATPCHALLENGERMATCH-26NOV05CORABO-COR`) | 0.46 / 0.47 (25) | 46.5% | 53.6% | 50.5% | 56.8% [54.2%-59.9%] | 48.0% | 47.2% | 47.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +7.1 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3047.0, B 4857.0; serve-point win A 57.6%, B 43.1%; Elo A 1695.4, B 1559.0; model uncertainty 0.0284
* Form inputs: days since last match A 10, B 10; matches on record A 1069, B 372; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.010, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Agustin Eduardo Cuellar Lorberg vs Julian Cundom -- M15 Salvador QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208273:208424:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Agustin Eduardo Cuellar Lorberg (`KXITFMATCH-26NOV05CUECUN-CUE`) | 0.48 / 0.49 (49) | 48.5% | 23.9% | 48.9% | 36.4% [33.4%-39.4%] | -- | -- | -- | -- | PASS | -24.6 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Julian Cundom (`KXITFMATCH-26NOV05CUECUN-CUN`) | 0.48 / 0.51 (11) | 49.5% | 76.1% | 51.1% | 63.6% [60.6%-66.6%] | -- | -- | -- | -- | PASS | +26.6 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 169.0, B 948.0; serve-point win A 50.5%, B 44.2%; Elo A 1097.6, B 1203.3; model uncertainty 0.0301
* Form inputs: days since last match A 346, B 150; matches on record A 8, B 49; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV05CUECUN-CUN  (YES = Julian Cundom)
Model: 76%
Kalshi: 50%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.031, surface_pool_high -0.030, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alec Deckers vs Connor Henry Van Schalkwyk -- M25 Harlingen TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207793:210227:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alec Deckers (`KXITFMATCH-26NOV05DECVAN-DEC`) | 0.66 / 0.69 (29) | 67.5% | 75.4% | 73.7% | 72.9% [72.1%-74.0%] | 65.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.9 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Connor Henry Van Schalkwyk (`KXITFMATCH-26NOV05DECVAN-VAN`) | 0.30 / 0.33 (35) | 31.5% | 24.6% | 26.3% | 27.1% [26.0%-27.9%] | 34.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.9 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2380.0, B 56.0; serve-point win A 69.0%, B 36.6%; Elo A 1451.9, B 1282.3; model uncertainty 0.0094
* Form inputs: days since last match A 73, B 164; matches on record A 184, B 14; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose -0.001, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Fradkin / Voelzke vs Dobek / Van Orderlain -- M15 Pembroke QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05FRAVOEDOBVAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dobek / Van Orderlain (`KXITFDOUBLES-26NOV05FRAVOEDOBVAN-DOBVAN`) | 0.06 / 0.12 (28) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fradkin / Voelzke (`KXITFDOUBLES-26NOV05FRAVOEDOBVAN-FRAVOE`) | 0.84 / 0.90 (1) | 87.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Oscar Jose Gutierrez vs Joao Vitor Scramin do Lago -- M15 Salvador QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-05T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:121264:213969:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oscar Jose Gutierrez (`KXITFMATCH-26NOV05GUTSCR-GUT`) | 0.94 / 0.96 (452) | 95.0% | 77.8% | 84.4% | 80.6% [75.3%-83.8%] | 94.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -17.1 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Joao Vitor Scramin do Lago (`KXITFMATCH-26NOV05GUTSCR-SCR`) | 0.04 / 0.06 (849) | 5.0% | 22.1% | 15.6% | 19.4% [16.2%-24.6%] | 5.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +17.1 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2766.0, B 1464.0; serve-point win A 57.8%, B 48.0%; Elo A 1315.8, B 1111.9; model uncertainty 0.0422
* Form inputs: days since last match A 206, B 192; matches on record A 606, B 31; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV05GUTSCR-SCR  (YES = Joao Vitor Scramin do Lago)
Model: 22%
Kalshi: 5%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.015, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hunter Heck vs Kevin Edengren -- M25 Harlingen TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209067:210570:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kevin Edengren (`KXITFMATCH-26NOV05HECEDE-EDE`) | 0.19 / 0.21 (163) | 20.0% | 10.3% | 12.7% | 12.9% [10.9%-14.4%] | 23.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.7 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hunter Heck (`KXITFMATCH-26NOV05HECEDE-HEC`) | 0.78 / 0.80 (414) | 79.0% | 89.7% | 87.3% | 87.1% [85.6%-89.1%] | 76.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +10.7 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1168.0, B 488.0; serve-point win A 64.1%, B 45.7%; Elo A 1455.7, B 1125.1; model uncertainty 0.0177
* Form inputs: days since last match A 52, B 360; matches on record A 63, B 30; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high +0.000, surface_dev_loose +0.008, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Erik Schiessl vs Kaylan Bigun -- M25 Harlingen TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210744:213672:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kaylan Bigun (`KXITFMATCH-26NOV05SCHBIG-BIG`) | 0.67 / 0.70 (267) | 68.5% | 70.4% | 46.4% | 56.2% [54.1%-57.2%] | 67.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Erik Schiessl (`KXITFMATCH-26NOV05SCHBIG-SCH`) | 0.30 / 0.31 (208) | 30.5% | 29.6% | 53.6% | 43.8% [42.8%-45.9%] | 32.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 2101.0; serve-point win A 56.9%, B 39.0%; Elo A 1262.4, B 1302.1; model uncertainty 0.0154
* Form inputs: days since last match A 717, B 10; matches on record A 1, B 95; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.021, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sebastian Dominguez Collado / Gomez Osorio vs Marshall / Slocombe -- M15 Pembroke QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05SEBGOMMARSLO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marshall / Slocombe (`KXITFDOUBLES-26NOV05SEBGOMMARSLO-MARSLO`) | 0.65 / 0.80 (125) | 72.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sebastian Dominguez Collado / Gomez Osorio (`KXITFDOUBLES-26NOV05SEBGOMMARSLO-SEBGOM`) | 0.17 / 0.32 (36) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Moyano / Romero vs Doldan / Celina Sosa -- W15 Neuquén QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05MOYROMDOLCEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Doldan / Celina Sosa (`KXITFWDOUBLES-26NOV05MOYROMDOLCEL-DOLCEL`) | 0.04 / 0.05 (150) | 4.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Moyano / Romero (`KXITFWDOUBLES-26NOV05MOYROMDOLCEL-MOYROM`) | 0.92 / 0.95 (66) | 93.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Sofia Madrid Rocca / Morini vs Labrana / Vergara Rivera -- W15 Neuquén QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-05T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05SOFMORLABVER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Labrana / Vergara Rivera (`KXITFWDOUBLES-26NOV05SOFMORLABVER-LABVER`) | 0.05 / 0.90 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sofia Madrid Rocca / Morini (`KXITFWDOUBLES-26NOV05SOFMORLABVER-SOFMOR`) | 0.05 / 0.90 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Isis Louise Van den Broek vs Anna Siskova -- W75 Petange R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216074:264227:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Siskova (`KXITFWMATCH-26NOV05VANSIS-SIS`) | 0.74 / 0.78 (424) | 76.0% | 72.9% | 83.9% | 75.3% [68.0%-78.2%] | 75.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.1 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Isis Louise Van den Broek (`KXITFWMATCH-26NOV05VANSIS-VAN`) | 0.22 / 0.25 (127) | 23.5% | 27.1% | 16.1% | 24.7% [21.8%-32.0%] | 24.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.6 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1856.0, B 3067.0; serve-point win A 50.1%, B 45.3%; Elo A 1579.5, B 1658.8; model uncertainty 0.0506
* Form inputs: days since last match A 192, B 23; matches on record A 103, B 435; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.026, surface_dev_loose -0.017, surface_dev_tight +0.026
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Viktor Markov vs Daniel De Jonge -- M15 Trois-Rivières R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 23:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207893:210722:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel De Jonge (`KXITFMATCH-26NOV05MARDEJ-DEJ`) | 0.72 / 0.75 (100) | 73.5% | 67.6% | 82.1% | 69.1% [64.4%-73.9%] | -- | -- | -- | -- | PASS | -5.9 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Viktor Markov (`KXITFMATCH-26NOV05MARDEJ-MAR`) | 0.22 / 0.28 (100) | 25.0% | 32.4% | 17.9% | 30.9% [26.1%-35.6%] | -- | -- | -- | -- | PASS | +7.4 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 549.0, B 1867.0; serve-point win A 59.4%, B 37.0%; Elo A 1261.4, B 1359.3; model uncertainty 0.0477
* Form inputs: days since last match A 353, B 122; matches on record A 23, B 147; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.018, surface_pool_high +0.009, surface_dev_loose -0.009, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eric David Verdes vs Antoine Genereux -- M15 Trois-Rivières R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 23:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-05T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05VERGEN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Antoine Genereux (`KXITFMATCH-26NOV05VERGEN-GEN`) | 0.09 / 0.12 (87) | 10.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eric David Verdes (`KXITFMATCH-26NOV05VERGEN-VER`) | 0.88 / 0.90 (279) | 89.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oceane Dodin vs Fiona Crawley -- W75 Petange R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 23:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206219:220680:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fiona Crawley (`KXITFWMATCH-26NOV05DODCRA-CRA`) | 0.50 / 0.52 (23) | 51.0% | 59.6% | 71.7% | 62.8% [53.7%-67.2%] | 50.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +8.6 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oceane Dodin (`KXITFWMATCH-26NOV05DODCRA-DOD`) | 0.47 / 0.49 (149) | 48.0% | 40.4% | 28.3% | 37.2% [32.9%-46.3%] | 50.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.6 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1969.0, B 2695.0; serve-point win A 57.5%, B 40.7%; Elo A 1748.1, B 1754.6; model uncertainty 0.0673
* Form inputs: days since last match A 43, B 27; matches on record A 714, B 131; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ingrid Carolina Millan Acosta vs Malaika Rapolu -- W50 Huamantla R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 23:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216311:222837:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ingrid Carolina Millan Acosta (`KXITFWMATCH-26NOV05MILRAP-MIL`) | 0.03 / 0.04 (329) | 3.5% | 4.1% | 7.6% | 10.6% [8.8%-13.3%] | 4.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.6 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Malaika Rapolu (`KXITFWMATCH-26NOV05MILRAP-RAP`) | 0.95 / 0.97 (360) | 96.0% | 95.9% | 92.4% | 89.4% [86.7%-91.2%] | 95.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.1 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 792.0, B 1761.0; serve-point win A 43.9%, B 43.1%; Elo A 1280.9, B 1619.4; model uncertainty 0.0225
* Form inputs: days since last match A 241, B 49; matches on record A 18, B 134; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose -0.007, surface_dev_tight +0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zuzanna Pawlikowska vs Misa Malkin -- W50 Huamantla R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 23:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222509:264187:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Misa Malkin (`KXITFWMATCH-26NOV05PAWMAL-MAL`) | 0.09 / 0.10 (101) | 9.5% | 22.0% | 34.8% | 33.8% [30.5%-36.3%] | 11.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +12.5 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zuzanna Pawlikowska (`KXITFWMATCH-26NOV05PAWMAL-PAW`) | 0.88 / 0.91 (100) | 89.5% | 78.0% | 65.2% | 66.2% [63.7%-69.5%] | 89.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.5 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2671.0, B 892.0; serve-point win A 53.0%, B 52.7%; Elo A 1482.3, B 1364.5; model uncertainty 0.0292
* Form inputs: days since last match A 9, B 241; matches on record A 146, B 39; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.025, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Victoria Rodriguez vs Maria Sholokhova -- W50 Huamantla R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 23:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-05T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211874:233718:2026-11-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Victoria Rodriguez (`KXITFWMATCH-26NOV05RODSHO-ROD`) | 0.30 / 0.33 (5) | 31.5% | 36.6% | 1.8% | 18.8% [7.6%-53.8%] | 34.3% | -- | 34.3% | ALL_THREE_DISAGREE | PASS | +5.1 pp | NORMAL | STALE | D / POOR | AGREES_WITH_MODEL | VERIFIED |
| Maria Sholokhova (`KXITFWMATCH-26NOV05RODSHO-SHO`) | 0.66 / 0.68 (194) | 67.0% | 63.4% | 98.2% | 81.2% [46.2%-92.4%] | 65.7% | -- | 65.7% | MODEL_LONE_OUTLIER | PASS | -3.6 pp | NORMAL | STALE | D / POOR | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 2050.0, B 1181.0; serve-point win A 47.2%, B 50.2%; Elo A 1548.0, B 1517.5; model uncertainty 0.2307
* Form inputs: days since last match A 9, B 465; matches on record A 576, B 85; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.000, surface_dev_loose -0.021, surface_dev_tight +0.030
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Diego Hidalgo / Andres Molteni vs Mateus Alves / Lucas Andrade Da Silva -- ATP Challenger Costa do Sauipe QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 23:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-05T23:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05HIDMOLALVAND:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mateus Alves / Lucas Andrade Da Silva (`KXATPCHALLENGERDOUBLES-26NOV05HIDMOLALVAND-ALVAND`) | 0.25 / 0.28 (28) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Diego Hidalgo / Andres Molteni (`KXATPCHALLENGERDOUBLES-26NOV05HIDMOLALVAND-HIDMOL`) | 0.68 / 0.75 (102) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Igor Marcondes / Felipe Meligeni Alves vs Guido Ivan Justo / Lautaro Midon -- ATP Challenger Costa do Sauipe QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-05 23:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-05T23:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05MARMELJUSMID:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Guido Ivan Justo / Lautaro Midon (`KXATPCHALLENGERDOUBLES-26NOV05MARMELJUSMID-JUSMID`) | 0.16 / 0.23 (25) | 19.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Igor Marcondes / Felipe Meligeni Alves (`KXATPCHALLENGERDOUBLES-26NOV05MARMELJUSMID-MARMEL`) | 0.77 / 0.84 (25) | 80.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Almeida / Vega vs Colby / Dollenberg -- M15 Hilton Head Island SC QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05ALMVEGCOLDOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Almeida / Vega (`KXITFDOUBLES-26NOV05ALMVEGCOLDOL-ALMVEG`) | 0.05 / 0.90 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Colby / Dollenberg (`KXITFDOUBLES-26NOV05ALMVEGCOLDOL-COLDOL`) | 0.05 / 0.90 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## C Pignaton / Novakovic vs Colombo / Gaines Jr -- M15 Hilton Head Island SC QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05CPINOVCOLGAI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Colombo / Gaines Jr (`KXITFDOUBLES-26NOV05CPINOVCOLGAI-COLGAI`) | 0.06 / 0.18 (30) | 12.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| C Pignaton / Novakovic (`KXITFDOUBLES-26NOV05CPINOVCOLGAI-CPINOV`) | 0.77 / 0.90 (1) | 83.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ailin Larraya Guidi / Meabe vs Simon Padros / Simon Padros -- W15 Neuquén QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05AILMEASIMSIM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ailin Larraya Guidi / Meabe (`KXITFWDOUBLES-26NOV05AILMEASIMSIM-AILMEA`) | 0.89 / 0.93 (3) | 91.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Simon Padros / Simon Padros (`KXITFWDOUBLES-26NOV05AILMEASIMSIM-SIMSIM`) | 0.05 / 0.07 (26) | 6.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Bartashevich / Kamper vs Penickova / Penickova -- W35 Orlando FL QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05BARKAMPENPEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bartashevich / Kamper (`KXITFWDOUBLES-26NOV05BARKAMPENPEN-BARKAM`) | 0.21 / 0.39 (40) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Penickova / Penickova (`KXITFWDOUBLES-26NOV05BARKAMPENPEN-PENPEN`) | 0.57 / 0.74 (96) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Buchnik / Dunyon vs Diianni / Drame -- W15 Hilton Head Island SC QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05BUCDUNDIIDRA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Buchnik / Dunyon (`KXITFWDOUBLES-26NOV05BUCDUNDIIDRA-BUCDUN`) | 0.06 / 0.73 (92) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Diianni / Drame (`KXITFWDOUBLES-26NOV05BUCDUNDIIDRA-DIIDRA`) | 0.22 / 0.39 (40) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Carrocera / Maria Maruca vs Boyden / Victoria Gobbi Monllau -- W15 Neuquén QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05CARMARBOYVIC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Boyden / Victoria Gobbi Monllau (`KXITFWDOUBLES-26NOV05CARMARBOYVIC-BOYVIC`) | 0.05 / 0.90 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Carrocera / Maria Maruca (`KXITFWDOUBLES-26NOV05CARMARBOYVIC-CARMAR`) | 0.05 / 0.90 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Catanzarite / Sharabura vs Manchala / Schaefbauer -- W15 Hilton Head Island SC QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05CATSHAMANSCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Catanzarite / Sharabura (`KXITFWDOUBLES-26NOV05CATSHAMANSCH-CATSHA`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Manchala / Schaefbauer (`KXITFWDOUBLES-26NOV05CATSHAMANSCH-MANSCH`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Aishi Das vs Ashton Bowers -- W35 Orlando FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-06T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:248665:261133:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ashton Bowers (`KXITFWMATCH-26NOV05DASBOW-BOW`) | 0.53 / 0.56 (156) | 54.5% | 59.7% | 36.4% | 55.3% [52.1%-59.5%] | -- | -- | -- | -- | PASS | +5.2 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Aishi Das (`KXITFWMATCH-26NOV05DASBOW-DAS`) | 0.42 / 0.45 (50) | 43.5% | 40.3% | 63.6% | 44.7% [40.5%-47.9%] | -- | -- | -- | -- | PASS | -3.2 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 979.0, B 0.0; serve-point win A 51.8%, B 46.4%; Elo A 1334.4, B 1375.1; model uncertainty 0.037
* Form inputs: days since last match A 192, B 745; matches on record A 30, B 46; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.042, surface_pool_high +0.032, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sloane Stephens vs Luciana Perry -- W35 Orlando FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-06T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:201585:267920:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luciana Perry (`KXITFWMATCH-26NOV05STEPER-PER`) | 0.08 / 0.09 (3) | 8.5% | 1.5% | 28.8% | 6.2% [3.8%-8.0%] | -- | -- | -- | -- | PASS | -7.0 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sloane Stephens (`KXITFWMATCH-26NOV05STEPER-STE`) | 0.90 / 0.91 (100) | 90.5% | 98.5% | 71.2% | 93.8% [92.0%-96.2%] | -- | -- | -- | -- | PASS | +8.0 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2061.0, B 141.0; serve-point win A 63.2%, B 53.2%; Elo A 1865.6, B 1351.9; model uncertainty 0.021
* Form inputs: days since last match A 48, B 521; matches on record A 685, B 4; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.014, surface_dev_loose +0.002, surface_dev_tight +0.002
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hernan Casanova / Franco Ribero vs Mateo Del Pino / Maximo Zeitune -- ATP Challenger Villa Maria QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 00:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-06T00:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05CASRIBDELZEI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hernan Casanova / Franco Ribero (`KXATPCHALLENGERDOUBLES-26NOV05CASRIBDELZEI-CASRIB`) | 0.56 / 0.58 (35) | 57.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mateo Del Pino / Maximo Zeitune (`KXATPCHALLENGERDOUBLES-26NOV05CASRIBDELZEI-DELZEI`) | 0.37 / 0.44 (61) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Braga / Mouilleron Salvo vs Souza / Sverzut Corsini -- M15 Salvador QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 00:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05BRAMOUSOUSVE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Braga / Mouilleron Salvo (`KXITFDOUBLES-26NOV05BRAMOUSOUSVE-BRAMOU`) | 0.05 / 0.90 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Souza / Sverzut Corsini (`KXITFDOUBLES-26NOV05BRAMOUSOUSVE-SOUSVE`) | 0.05 / 0.90 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Vieira Alves Malacarne Bruno / Rodrigues Longobardi vs Braga / Lima -- M15 Salvador QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 00:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05VIERODBRALIM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Braga / Lima (`KXITFDOUBLES-26NOV05VIERODBRALIM-BRALIM`) | 0.05 / 0.90 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vieira Alves Malacarne Bruno / Rodrigues Longobardi (`KXITFDOUBLES-26NOV05VIERODBRALIM-VIEROD`) | 0.05 / 0.90 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ipek Oz vs Diletta Cherubini -- W50 Huamantla R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 00:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-06T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213998:221000:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diletta Cherubini (`KXITFWMATCH-26NOV05OZXCHE-CHE`) | 0.20 / 0.22 (26) | 21.0% | 43.4% | 55.3% | 51.1% [45.8%-54.2%] | -- | -- | -- | -- | WATCH | +22.4 pp | HIGH_REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ipek Oz (`KXITFWMATCH-26NOV05OZXCHE-OZX`) | 0.76 / 0.80 (263) | 78.0% | 56.6% | 44.7% | 48.9% [45.8%-54.2%] | -- | -- | -- | -- | PASS | -21.4 pp | HIGH_REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2398.0, B 2494.0; serve-point win A 55.8%, B 45.4%; Elo A 1480.2, B 1445.5; model uncertainty 0.0425
* Form inputs: days since last match A 58, B 6; matches on record A 487, B 315; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05OZXCHE-CHE  (YES = Diletta Cherubini)
Model: 43%
Kalshi: 21%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: STALE_KALSHI_QUOTE, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.016, surface_dev_loose +0.005, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexandru Chirita / Velcz vs Djakouris / Djakouris -- M25 Harlingen TX QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05ALEVELDJADJA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandru Chirita / Velcz (`KXITFDOUBLES-26NOV05ALEVELDJADJA-ALEVEL`) | 0.05 / 0.90 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Djakouris / Djakouris (`KXITFDOUBLES-26NOV05ALEVELDJADJA-DJADJA`) | 0.05 / 0.90 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Thiago Seyboth Wild vs Franco Roncadelli -- ATP Challenger Costa do Sauipe R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-06T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:205734:208364:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Franco Roncadelli (`KXATPCHALLENGERMATCH-26NOV05SEYRON-RON`) | 0.10 / 0.11 (1354) | 10.5% | 19.4% | 17.9% | 19.6% [18.5%-21.1%] | -- | -- | -- | -- | SHADOW_BET | +8.9 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Thiago Seyboth Wild (`KXATPCHALLENGERMATCH-26NOV05SEYRON-SEY`) | 0.89 / 0.90 (100) | 89.5% | 80.6% | 82.1% | 80.4% [78.9%-81.5%] | -- | -- | -- | -- | PASS | -8.9 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4921.0, B 4155.0; serve-point win A 62.8%, B 43.9%; Elo A 1772.0, B 1580.7; model uncertainty 0.0128
* Form inputs: days since last match A 24, B 10; matches on record A 510, B 324; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.004, surface_dev_loose +0.011, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Maria Jose Portillo Ramirez vs Miriam Bianca Bulgaru -- W50 Huamantla R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-06T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214480:215019:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miriam Bianca Bulgaru (`KXITFWMATCH-26NOV05PORBUL-BUL`) | 0.55 / 0.59 (294) | 57.0% | 59.9% | 60.5% | 53.7% [50.5%-55.9%] | -- | -- | -- | -- | PASS | +2.9 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Jose Portillo Ramirez (`KXITFWMATCH-26NOV05PORBUL-POR`) | 0.40 / 0.42 (4) | 41.0% | 40.1% | 39.5% | 46.3% [44.1%-49.5%] | -- | -- | -- | -- | WATCH | -0.9 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 916.0, B 3417.0; serve-point win A 53.0%, B 45.1%; Elo A 1502.2, B 1497.5; model uncertainty 0.0266
* Form inputs: days since last match A 199, B 192; matches on record A 326, B 517; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.016, surface_dev_loose -0.011, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valerio Aboian / Bruno Fernandez vs Murkel Dellien / Arklon Huertas Del Pino Cordova -- ATP Challenger Villa Maria QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 01:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-06T01:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05ABOFERDEVHUE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valerio Aboian / Bruno Fernandez (`KXATPCHALLENGERDOUBLES-26NOV05ABOFERDEVHUE-ABOFER`) | 0.05 / 0.92 (5) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Murkel Dellien / Arklon Huertas Del Pino Cordova (`KXATPCHALLENGERDOUBLES-26NOV05ABOFERDEVHUE-DEVHUE`) | 0.20 / 0.94 (125) | 57.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Bynoe / Hammond vs Dean / Tripathi -- M15 Trois-Rivières QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05BYNHAMDEATRI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bynoe / Hammond (`KXITFDOUBLES-26NOV05BYNHAMDEATRI-BYNHAM`) | 0.06 / 0.12 (28) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dean / Tripathi (`KXITFDOUBLES-26NOV05BYNHAMDEATRI-DEATRI`) | 0.69 / 0.90 (1) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Cazacu / Alexander Rodriguez vs Delattre / Mirarchi -- M15 Hilton Head Island SC QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05CAZALEDELMIR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cazacu / Alexander Rodriguez (`KXITFDOUBLES-26NOV05CAZALEDELMIR-CAZALE`) | 0.05 / 0.90 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Delattre / Mirarchi (`KXITFDOUBLES-26NOV05CAZALEDELMIR-DELMIR`) | 0.05 / 0.90 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Krall / Watane vs Lieberman / Sheldon -- M15 Hilton Head Island SC QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05KRAWATLIESHE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Krall / Watane (`KXITFDOUBLES-26NOV05KRAWATLIESHE-KRAWAT`) | 0.09 / 0.28 (34) | 18.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lieberman / Sheldon (`KXITFDOUBLES-26NOV05KRAWATLIESHE-LIESHE`) | 0.67 / 0.88 (208) | 77.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Joshua Peck vs Nikola Slavic -- M15 Trois-Rivières R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-06T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200234:208302:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joshua Peck (`KXITFMATCH-26NOV05PECSLA-PEC`) | 0.24 / 0.26 (167) | 25.0% | 30.5% | 36.5% | 34.3% [30.8%-36.1%] | -- | -- | -- | -- | WATCH | +5.5 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nikola Slavic (`KXITFMATCH-26NOV05PECSLA-SLA`) | 0.73 / 0.77 (682) | 75.0% | 69.5% | 63.5% | 65.7% [63.9%-69.2%] | -- | -- | -- | -- | PASS | -5.5 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1103.0, B 2270.0; serve-point win A 63.3%, B 32.5%; Elo A 1149.6, B 1277.3; model uncertainty 0.0264
* Form inputs: days since last match A 192, B 116; matches on record A 78, B 65; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.027, surface_pool_high +0.018, surface_dev_loose -0.004, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Adams / Szabo vs Drugdova / Zucchini -- W35 Orlando FL QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 01:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05ADASZADRUZUC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adams / Szabo (`KXITFWDOUBLES-26NOV05ADASZADRUZUC-ADASZA`) | 0.54 / 0.73 (92) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Drugdova / Zucchini (`KXITFWDOUBLES-26NOV05ADASZADRUZUC-DRUZUC`) | 0.22 / 0.42 (43) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Bohrer Martins / Burgic vs Hossam Salah / Korpanec Davies -- W35 Orlando FL QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 01:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05BOHBURHOSKOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bohrer Martins / Burgic (`KXITFWDOUBLES-26NOV05BOHBURHOSKOR-BOHBUR`) | 0.58 / 0.78 (113) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hossam Salah / Korpanec Davies (`KXITFWDOUBLES-26NOV05BOHBURHOSKOR-HOSKOR`) | 0.19 / 0.36 (39) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Chan / Hinojosa Gomez vs Castillo Meza / Odorizzi -- W50 Huamantla QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 01:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05CHAHINCASODO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Castillo Meza / Odorizzi (`KXITFWDOUBLES-26NOV05CHAHINCASODO-CASODO`) | 0.20 / 0.21 (31) | 20.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Chan / Hinojosa Gomez (`KXITFWDOUBLES-26NOV05CHAHINCASODO-CHAHIN`) | 0.34 / 0.86 (1) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## El Aouni / Saffar vs Davtyan / Liu -- W15 Hilton Head Island SC QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 01:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05ELASAFDAVLIU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Davtyan / Liu (`KXITFWDOUBLES-26NOV05ELASAFDAVLIU-DAVLIU`) | 0.24 / 0.42 (43) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| El Aouni / Saffar (`KXITFWDOUBLES-26NOV05ELASAFDAVLIU-ELASAF`) | 0.50 / 0.71 (86) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Evtimova / Harding vs Shumate / Williams -- W15 Hilton Head Island SC QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 01:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05EVTHARSHUWIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Evtimova / Harding (`KXITFWDOUBLES-26NOV05EVTHARSHUWIL-EVTHAR`) | 0.20 / 0.68 (10) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Shumate / Williams (`KXITFWDOUBLES-26NOV05EVTHARSHUWIL-SHUWIL`) | 0.29 / 0.75 (1) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Fouad / Kuhl vs Black / Jauffret -- W35 Orlando FL QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 01:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05FOUKUHBLAJAU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Black / Jauffret (`KXITFWDOUBLES-26NOV05FOUKUHBLAJAU-BLAJAU`) | 0.13 / 0.69 (80) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fouad / Kuhl (`KXITFWDOUBLES-26NOV05FOUKUHBLAJAU-FOUKUH`) | 0.26 / 0.46 (46) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Luis Carlos Alvarez Valdes vs Maxwell McKennon -- M25 Guadalajara QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-06T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208297:211468:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luis Carlos Alvarez Valdes (`KXITFMATCH-26NOV05ALVMCK-ALV`) | 0.78 / 0.82 (15) | 80.0% | 56.8% | 56.6% | 55.6% [53.0%-58.1%] | -- | -- | -- | -- | PASS | -23.2 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maxwell McKennon (`KXITFMATCH-26NOV05ALVMCK-MCK`) | 0.16 / 0.20 (26) | 18.0% | 43.2% | 43.4% | 44.4% [41.9%-47.0%] | -- | -- | -- | -- | PASS | +25.2 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 923.0, B 3096.0; serve-point win A 62.3%, B 39.0%; Elo A 1421.8, B 1386.5; model uncertainty 0.0253
* Form inputs: days since last match A 374, B 192; matches on record A 45, B 140; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV05ALVMCK-MCK  (YES = Maxwell McKennon)
Model: 43%
Kalshi: 18%
Gap: +25 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.005, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andres Andrade vs James Kent Trotter -- ATP Challenger Charlottesville R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-06T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200748:208801:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andres Andrade (`KXATPCHALLENGERMATCH-26NOV05ANDTRO-AND`) | 0.51 / 0.52 (423) | 51.5% | 73.6% | 55.1% | 66.9% [58.1%-73.2%] | -- | -- | -- | -- | PASS | +22.1 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| James Kent Trotter (`KXATPCHALLENGERMATCH-26NOV05ANDTRO-TRO`) | 0.47 / 0.49 (1274) | 48.0% | 26.4% | 44.9% | 33.1% [26.8%-41.9%] | -- | -- | -- | -- | PASS | -21.6 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4704.0, B 223.0; serve-point win A 63.6%, B 41.3%; Elo A 1638.6, B 1506.0; model uncertainty 0.0758
* Form inputs: days since last match A 10, B 234; matches on record A 302, B 28; data quality D

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV05ANDTRO-AND  (YES = Andres Andrade)
Model: 74%
Kalshi: 52%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.045, surface_pool_high -0.058, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE

## Cundom / Jose Escurra Isnardi vs Barbieri Renner / Wendler Filho -- M15 Salvador QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05CUNJOSBARWEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barbieri Renner / Wendler Filho (`KXITFDOUBLES-26NOV05CUNJOSBARWEN-BARWEN`) | 0.05 / 0.90 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cundom / Jose Escurra Isnardi (`KXITFDOUBLES-26NOV05CUNJOSBARWEN-CUNJOS`) | 0.05 / 0.90 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jesse Flores vs Rodrigo Pacheco Mendez -- M25 Guadalajara QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-06T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132374:210202:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jesse Flores (`KXITFMATCH-26NOV05FLOPAC-FLO`) | 0.05 / 0.06 (399) | 5.5% | 14.7% | 28.2% | 22.1% [14.2%-25.5%] | -- | -- | -- | -- | WATCH | +9.2 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rodrigo Pacheco Mendez (`KXITFMATCH-26NOV05FLOPAC-PAC`) | 0.92 / 0.94 (3) | 93.0% | 85.3% | 71.8% | 77.9% [74.5%-85.8%] | -- | -- | -- | -- | PASS | -7.7 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2047.0, B 4259.0; serve-point win A 61.5%, B 29.9%; Elo A 1350.9, B 1651.3; model uncertainty 0.0565
* Form inputs: days since last match A 192, B 10; matches on record A 190, B 218; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.022, surface_dev_loose +0.004, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexis Galarneau / Hans Hach Verdugo vs Daniel Milavsky / Braden Shick -- ATP Challenger Charlottesville QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-06T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05GALHACMILSHI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexis Galarneau / Hans Hach Verdugo (`KXATPCHALLENGERDOUBLES-26NOV05GALHACMILSHI-GALHAC`) | 0.29 / 0.33 (5) | 31.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daniel Milavsky / Braden Shick (`KXATPCHALLENGERDOUBLES-26NOV05GALHACMILSHI-MILSHI`) | 0.64 / 0.71 (94) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Pereira Xavier / Pinheiro da Cruz Junior vs Augusto Garcia Finetto / Rodrigues -- M15 Salvador QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05PERPINAUGROD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Augusto Garcia Finetto / Rodrigues (`KXITFDOUBLES-26NOV05PERPINAUGROD-AUGROD`) | 0.36 / 0.58 (59) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pereira Xavier / Pinheiro da Cruz Junior (`KXITFDOUBLES-26NOV05PERPINAUGROD-PERPIN`) | 0.36 / 0.58 (59) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Samir Banerjee vs Max Wiskandt -- M25 Harlingen TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 03:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-06T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208328:209079:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Samir Banerjee (`KXITFMATCH-26NOV05BANWIS-BAN`) | 0.62 / 0.66 (28) | 64.0% | 74.2% | 85.7% | 77.9% [68.0%-82.2%] | -- | -- | -- | -- | PASS | +10.2 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Max Wiskandt (`KXITFMATCH-26NOV05BANWIS-WIS`) | 0.32 / 0.36 (31) | 34.0% | 25.8% | 14.3% | 22.1% [17.8%-32.0%] | -- | -- | -- | -- | PASS | -8.2 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1864.0, B 3286.0; serve-point win A 61.4%, B 43.6%; Elo A 1569.0, B 1451.5; model uncertainty 0.0713
* Form inputs: days since last match A 360, B 24; matches on record A 107, B 237; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.008, surface_dev_loose +0.011, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chunduru / Chunduru vs Foster / Jeff Planinsek -- M25 Harlingen TX QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 03:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05CHUCHUFOSJEF:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chunduru / Chunduru (`KXITFDOUBLES-26NOV05CHUCHUFOSJEF-CHUCHU`) | 0.04 / 0.90 (1) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Foster / Jeff Planinsek (`KXITFDOUBLES-26NOV05CHUCHUFOSJEF-FOSJEF`) | 0.04 / 0.90 (1) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Schiessl / Henry Van Schalkwyk vs Lothringer / Lovern -- M25 Harlingen TX QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 03:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05SCHHENLOTLOV:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lothringer / Lovern (`KXITFDOUBLES-26NOV05SCHHENLOTLOV-LOTLOV`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Schiessl / Henry Van Schalkwyk (`KXITFDOUBLES-26NOV05SCHHENLOTLOV-SCHHEN`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Blu Baker vs Rafael De Alba -- M25 Guadalajara QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 03:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-06T03:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208908:209124:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Blu Baker (`KXITFMATCH-26NOV05BAKDEA-BAK`) | 0.83 / 0.85 (20) | 84.0% | 75.4% | 83.2% | 77.0% [72.7%-81.3%] | -- | -- | -- | -- | PASS | -8.6 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rafael De Alba (`KXITFMATCH-26NOV05BAKDEA-DEA`) | 0.15 / 0.17 (152) | 16.0% | 24.6% | 16.8% | 23.0% [18.7%-27.3%] | -- | -- | -- | -- | WATCH | +8.6 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1707.0, B 1439.0; serve-point win A 59.0%, B 46.2%; Elo A 1343.1, B 1191.5; model uncertainty 0.0426
* Form inputs: days since last match A 206, B 192; matches on record A 119, B 35; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.012, surface_dev_loose +0.000, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nobel / St-Hilaire vs Fernandes / David Verdes -- M15 Trois-Rivières QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 03:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T03:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05NOBSTHFERDAV:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fernandes / David Verdes (`KXITFDOUBLES-26NOV05NOBSTHFERDAV-FERDAV`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nobel / St-Hilaire (`KXITFDOUBLES-26NOV05NOBSTHFERDAV-NOBSTH`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Oskar Brostrom Poulsen vs Tiago Pires -- M15 Trois-Rivières R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-06T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211355:211772:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tiago Pires (`KXITFMATCH-26NOV05POUPIR-PIR`) | 0.32 / 0.35 (488) | 33.5% | 24.9% | 48.0% | 30.8% [29.8%-31.8%] | -- | -- | -- | -- | PASS | -8.6 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Oskar Brostrom Poulsen (`KXITFMATCH-26NOV05POUPIR-POU`) | 0.62 / 0.63 (130) | 62.5% | 75.0% | 52.0% | 69.2% [68.2%-70.2%] | -- | -- | -- | -- | PASS | +12.6 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1822.0, B 0.0; serve-point win A 66.4%, B 39.0%; Elo A 1368.5, B 1224.9; model uncertainty 0.0101
* Form inputs: days since last match A 192, B 850; matches on record A 37, B 7; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose -0.001, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Fuchs / Perez vs Carlos Alvarez Valdes / Flores -- M25 Guadalajara SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 05:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T05:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05FUCPERCARFLO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlos Alvarez Valdes / Flores (`KXITFDOUBLES-26NOV05FUCPERCARFLO-CARFLO`) | 0.40 / 0.63 (1) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fuchs / Perez (`KXITFDOUBLES-26NOV05FUCPERCARFLO-FUCPER`) | 0.30 / 0.54 (54) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Heck / Zamora vs Artnak / Snitari -- M25 Harlingen TX QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 05:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T05:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05HECZAMARTSNI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Artnak / Snitari (`KXITFDOUBLES-26NOV05HECZAMARTSNI-ARTSNI`) | 0.24 / 0.49 (49) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Heck / Zamora (`KXITFDOUBLES-26NOV05HECZAMARTSNI-HECZAM`) | 0.45 / 0.71 (86) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Zeynep Sonmez vs Claire Liu -- WTA Hong Kong QF

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-06 09:00Z
* Current expected start: 2026-11-06 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-05 13:28Z
* Recommended handicap-by time: 2026-11-06 05:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-11-06T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214906:220309:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Claire Liu (`KXWTAMATCH-26NOV06SONLIU-LIU`) | 0.44 / 0.49 (177) | 46.5% | 40.3% | 36.9% | 38.0% [36.4%-42.6%] | -- | 46.4% | -- | INSUFFICIENT_INPUTS | PASS | -6.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zeynep Sonmez (`KXWTAMATCH-26NOV06SONLIU-SON`) | 0.50 / 0.52 (1361) | 51.0% | 59.7% | 63.1% | 62.1% [57.4%-63.6%] | -- | 53.4% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +8.7 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4355.0, B 3837.0; serve-point win A 55.4%, B 46.5%; Elo A 1835.5, B 1775.1; model uncertainty 0.0308
* Form inputs: days since last match A 0, B 1; matches on record A 433, B 461; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.010
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26NOV06SONLIU-1-LIU` Will Claire Liu win set 1 in the Zeynep Sonmez vs Claire Liu match: 0.45/0.50 mid 47.5%, model 43.5% (projection_v2.0 (prediction ledger)) -- gap -4.0 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV06SONLIU-1-SON` Will Zeynep Sonmez win set 1 in the Zeynep Sonmez vs Claire Liu match: 0.50/0.55 mid 52.5%, model 56.5% (projection_v2.0 (prediction ledger)) -- gap +4.0 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV06SONLIU-2-LIU` Will Claire Liu win set 2 in the Zeynep Sonmez vs Claire Liu match: 0.44/0.51 mid 47.5%, model 43.5% (projection_v2.0 (prediction ledger)) -- gap -4.0 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV06SONLIU-2-SON` Will Zeynep Sonmez win set 2 in the Zeynep Sonmez vs Claire Liu match: 0.49/0.56 mid 52.5%, model 56.5% (projection_v2.0 (prediction ledger)) -- gap +4.0 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Rengifo / Esteban Rico Arias vs Alujas / Benson -- M25 Guadalajara SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV05RENESTALUBEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alujas / Benson (`KXITFDOUBLES-26NOV05RENESTALUBEN-ALUBEN`) | 0.56 / 0.79 (1) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rengifo / Esteban Rico Arias (`KXITFDOUBLES-26NOV05RENESTALUBEN-RENEST`) | 0.16 / 0.38 (1) | 27.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Makoto Ninomiya / Ying (1998) Zhang vs Hao-Ching Chan / Miyu (1994) Kato -- WTA Hong Kong QF

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-06 09:30Z
* Current expected start: 2026-11-06 06:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-05 13:28Z
* Recommended handicap-by time: 2026-11-06 05:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-06T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV06NINZHACHAKAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hao-Ching Chan / Miyu (1994) Kato (`KXWTADOUBLES-26NOV06NINZHACHAKAT-CHAKAT`) | 0.62 / 0.66 (41) | 64.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Makoto Ninomiya / Ying (1998) Zhang (`KXWTADOUBLES-26NOV06NINZHACHAKAT-NINZHA`) | 0.31 / 0.38 (25) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Alan Fernando Rubio Fierros vs Lorenzo Claverie -- M25 Guadalajara QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-06T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200214:209936:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Claverie (`KXITFMATCH-26NOV05RUBCLA-CLA`) | 0.66 / 0.69 (1013) | 67.5% | 43.5% | 44.0% | 41.5% [40.5%-44.4%] | 66.4% | -- | 66.4% | MODEL_LONE_OUTLIER | PASS | -24.1 pp | HIGH_REVIEW | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Alan Fernando Rubio Fierros (`KXITFMATCH-26NOV05RUBCLA-RUB`) | 0.30 / 0.34 (142) | 32.0% | 56.5% | 56.0% | 58.5% [55.6%-59.5%] | 33.6% | -- | 33.6% | MODEL_LONE_OUTLIER | WATCH | +24.6 pp | HIGH_REVIEW | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1893.0, B 484.0; serve-point win A 63.9%, B 37.4%; Elo A 1403.1, B 1342.4; model uncertainty 0.0195
* Form inputs: days since last match A 46, B 10; matches on record A 179, B 99; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV05RUBCLA-RUB  (YES = Alan Fernando Rubio Fierros)
Model: 57%
Kalshi: 32%
Gap: +25 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_KALSHI
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.025, surface_pool_high +0.010, surface_dev_loose +0.009, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kanon Sawashiro vs Mio Mushika -- W35 Hamamatsu QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Carpet · scheduled 2026-11-06T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222986:263905:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mio Mushika (`KXITFWMATCH-26NOV05SAWMUS-MUS`) | 0.42 / 0.49 (149) | 45.5% | 67.6% | 70.4% | 68.5% [66.6%-69.4%] | -- | -- | -- | -- | PASS | +22.1 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kanon Sawashiro (`KXITFWMATCH-26NOV05SAWMUS-SAW`) | 0.49 / 0.56 (143) | 52.5% | 32.4% | 29.6% | 31.5% [30.6%-33.4%] | -- | -- | -- | -- | PASS | -20.1 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 827.0, B 2224.0; serve-point win A 51.8%, B 44.8%; Elo A 1351.6, B 1475.3; model uncertainty 0.0143
* Form inputs: days since last match A 19, B 199; matches on record A 37, B 201; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05SAWMUS-MUS  (YES = Mio Mushika)
Model: 68%
Kalshi: 46%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.019, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ayano Shimizu vs Tiana Tian Deng -- W35 Hamamatsu QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Carpet · scheduled 2026-11-06T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215550:260528:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tiana Tian Deng (`KXITFWMATCH-26NOV05SHIDEN-DEN`) | 0.44 / 0.49 (149) | 46.5% | 10.8% | 32.0% | 16.5% [13.1%-20.0%] | -- | -- | -- | -- | PASS | -35.7 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ayano Shimizu (`KXITFWMATCH-26NOV05SHIDEN-SHI`) | 0.49 / 0.56 (170) | 52.5% | 89.2% | 68.0% | 83.5% [80.0%-86.9%] | -- | -- | -- | -- | PASS | +36.7 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1770.0, B 853.0; serve-point win A 58.2%, B 51.1%; Elo A 1677.5, B 1297.9; model uncertainty 0.0344
* Form inputs: days since last match A 192, B 122; matches on record A 430, B 41; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05SHIDEN-SHI  (YES = Ayano Shimizu)
Model: 89%
Kalshi: 52%
Gap: +37 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.003, surface_pool_high +0.003, surface_dev_loose +0.006, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Han Shi vs Berfu Cengiz -- W100 Incheon QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 08:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-06T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214507:222559:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Berfu Cengiz (`KXITFWMATCH-26NOV05SHICEN-CEN`) | 0.23 / 0.31 (128) | 27.0% | 38.7% | 25.6% | 34.9% [28.7%-48.4%] | -- | -- | -- | -- | PASS | +11.7 pp | REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Han Shi (`KXITFWMATCH-26NOV05SHICEN-SHI`) | 0.64 / 0.72 (100) | 68.0% | 61.3% | 74.4% | 65.1% [51.6%-71.3%] | -- | -- | -- | -- | PASS | -6.7 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3226.0, B 1612.0; serve-point win A 54.0%, B 48.1%; Elo A 1600.6, B 1571.0; model uncertainty 0.0986
* Form inputs: days since last match A 192, B 37; matches on record A 228, B 455; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.035, surface_pool_high +0.034, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Katie Swan vs Xinxin Yao -- W100 Incheon QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 08:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-06T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215042:252587:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katie Swan (`KXITFWMATCH-26NOV05SWAYAO-SWA`) | 0.71 / 0.79 (219) | 75.0% | 74.3% | 86.4% | 80.9% [74.3%-84.6%] | -- | -- | -- | -- | PASS | -0.7 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Xinxin Yao (`KXITFWMATCH-26NOV05SWAYAO-YAO`) | 0.17 / 0.24 (133) | 20.5% | 25.7% | 13.6% | 19.1% [15.4%-25.7%] | -- | -- | -- | -- | PASS | +5.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2343.0, B 2972.0; serve-point win A 58.3%, B 46.6%; Elo A 1722.0, B 1573.7; model uncertainty 0.0516
* Form inputs: days since last match A 41, B 31; matches on record A 387, B 320; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.011, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Koharu Ito vs Chia Yi Tsao -- W35 Hamamatsu QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Carpet · scheduled 2026-11-06T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259623:270096:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Koharu Ito (`KXITFWMATCH-26NOV05ITOTSA-ITO`) | 0.06 / 0.11 (9) | 8.5% | 5.5% | 19.9% | 20.6% [20.0%-20.6%] | -- | -- | -- | -- | PASS | -3.0 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Chia Yi Tsao (`KXITFWMATCH-26NOV05ITOTSA-TSA`) | 0.85 / 0.92 (173) | 88.5% | 94.5% | 80.1% | 79.4% [79.4%-80.0%] | -- | -- | -- | -- | PASS | +6.0 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 31.0, B 824.0; serve-point win A 50.2%, B 37.6%; Elo A 1247.1, B 1478.6; model uncertainty 0.0034
* Form inputs: days since last match A 367, B 199; matches on record A 2, B 145; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Shiho Tsujioka vs Kurea Hayasaka -- W35 Hamamatsu QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Carpet · scheduled 2026-11-06T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:263801:263865:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kurea Hayasaka (`KXITFWMATCH-26NOV05TSUHAY-HAY`) | 0.49 / 0.56 (146) | 52.5% | 21.6% | 41.5% | 33.5% [31.5%-34.9%] | -- | -- | -- | -- | PASS | -30.9 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Shiho Tsujioka (`KXITFWMATCH-26NOV05TSUHAY-TSU`) | 0.44 / 0.49 (149) | 46.5% | 78.4% | 58.5% | 66.5% [65.1%-68.5%] | -- | -- | -- | -- | PASS | +31.9 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1131.0, B 337.0; serve-point win A 57.2%, B 48.6%; Elo A 1368.7, B 1231.3; model uncertainty 0.0172
* Form inputs: days since last match A 12, B 206; matches on record A 43, B 9; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05TSUHAY-TSU  (YES = Shiho Tsujioka)
Model: 78%
Kalshi: 46%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Priska Madelyn Nugroho vs Yeonwoo Ku -- W100 Incheon QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 09:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-06T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05NUGKUX:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yeonwoo Ku (`KXITFWMATCH-26NOV05NUGKUX-KUX`) | 0.53 / 0.64 (52) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Priska Madelyn Nugroho (`KXITFWMATCH-26NOV05NUGKUX-NUG`) | 0.30 / 0.41 (43) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maria Pankratova vs Yingqun Sun -- W15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 09:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-06T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV05PANSUN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Pankratova (`KXITFWMATCH-26NOV05PANSUN-PAN`) | 0.06 / 0.93 (22) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yingqun Sun (`KXITFWMATCH-26NOV05PANSUN-SUN`) | 0.06 / 0.94 (125) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sara Saito vs JiaYi Wang -- W100 Incheon QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 09:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-06T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260170:265692:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Saito (`KXITFWMATCH-26NOV05SAIWAN-SAI`) | 0.17 / 0.67 (1) | 42.0% | 55.4% | 27.3% | 39.4% [32.9%-56.9%] | -- | -- | -- | -- | PASS | +13.4 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| JiaYi Wang (`KXITFWMATCH-26NOV05SAIWAN-WAN`) | 0.26 / 0.73 (5) | 49.5% | 44.6% | 72.7% | 60.6% [43.1%-67.1%] | -- | -- | -- | -- | PASS | -4.9 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3341.0, B 2216.0; serve-point win A 53.5%, B 47.5%; Elo A 1574.9, B 1510.1; model uncertainty 0.12
* Form inputs: days since last match A 38, B 37; matches on record A 198, B 72; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.021, surface_dev_loose -0.015, surface_dev_tight +0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yushan Shao vs Yuhan Wang -- W15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 09:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-06T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264205:269253:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yushan Shao (`KXITFWMATCH-26NOV05SHAWAN-SHA`) | 0.04 / 0.94 (10) | 49.0% | 50.2% | 64.6% | 54.3% [46.8%-58.5%] | -- | -- | -- | -- | PASS | +1.2 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuhan Wang (`KXITFWMATCH-26NOV05SHAWAN-WAN`) | 0.04 / 0.93 (200) | 48.5% | 49.8% | 35.4% | 45.7% [41.5%-53.2%] | -- | -- | -- | -- | PASS | +1.3 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1123.0, B 1724.0; serve-point win A 52.7%, B 47.3%; Elo A 1398.2, B 1428.1; model uncertainty 0.0585
* Form inputs: days since last match A 30, B 35; matches on record A 29, B 44; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jiaqi Wang vs Alina Tikhonova -- W15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 09:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-06T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221181:270431:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alina Tikhonova (`KXITFWMATCH-26NOV05WANTIK-TIK`) | 0.04 / 0.94 (10) | 49.0% | 34.9% | 43.6% | 38.9% [36.4%-42.0%] | -- | -- | -- | -- | PASS | -14.1 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jiaqi Wang (`KXITFWMATCH-26NOV05WANTIK-WAN`) | 0.04 / 0.93 (5) | 48.5% | 65.1% | 56.4% | 61.1% [58.0%-63.6%] | -- | -- | -- | -- | PASS | +16.6 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2849.0, B 349.0; serve-point win A 54.2%, B 48.7%; Elo A 1543.7, B 1453.2; model uncertainty 0.0282
* Form inputs: days since last match A 192, B 276; matches on record A 250, B 5; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05WANTIK-WAN  (YES = Jiaqi Wang)
Model: 65%
Kalshi: 48%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ikumi Yamazaki vs Anna Yang -- W15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 09:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-06T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221265:264242:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ikumi Yamazaki (`KXITFWMATCH-26NOV05YAMYAN-YAM`) | 0.41 / 0.94 (10) | 67.5% | 86.0% | 58.9% | 70.7% [64.0%-78.8%] | -- | -- | -- | -- | PASS | +18.5 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anna Yang (`KXITFWMATCH-26NOV05YAMYAN-YAN`) | 0.07 / 0.28 (34) | 17.5% | 14.0% | 41.1% | 29.3% [21.2%-36.0%] | -- | -- | -- | -- | PASS | -3.5 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1933.0, B 270.0; serve-point win A 59.4%, B 48.7%; Elo A 1477.0, B 1302.6; model uncertainty 0.074
* Form inputs: days since last match A 192, B 374; matches on record A 215, B 21; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV05YAMYAN-YAM  (YES = Ikumi Yamazaki)
Model: 86%
Kalshi: 68%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.060, surface_pool_high -0.062, surface_dev_loose +0.004, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aliaksandra Sasnovich vs Maria Sakkari -- WTA Hong Kong QF

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-06 09:00Z
* Current expected start: 2026-11-06 10:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-05 13:28Z
* Recommended handicap-by time: 2026-11-06 09:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+90_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-11-06T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:205925:206289:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Sakkari (`KXWTAMATCH-26NOV06SASSAK-SAK`) | 0.56 / 0.57 (1613) | 56.5% | 55.6% | 47.9% | 52.1% [50.5%-58.4%] | 56.6% | 57.3% | 56.9% | MARKETS_AGREE | PASS | -0.9 pp | NORMAL | STALE | A / LIMITED | ALL_AGREE | VERIFIED |
| Aliaksandra Sasnovich (`KXWTAMATCH-26NOV06SASSAK-SAS`) | 0.42 / 0.44 (4763) | 43.0% | 44.4% | 52.1% | 47.9% [41.6%-49.5%] | 43.4% | 43.0% | 43.2% | MARKETS_AGREE | WATCH | +1.4 pp | NORMAL | STALE | A / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4822.0, B 3640.0; serve-point win A 56.2%, B 42.7%; Elo A 1856.9, B 1939.2; model uncertainty 0.0393
* Form inputs: days since last match A 1, B 1; matches on record A 800, B 864; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.005, surface_dev_tight -0.011
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV06SASSAK-23` Over 22.5 games: 0.44/0.45 mid 44.5%, model 56.3% (projection_v2.0 (prediction ledger)) -- gap +11.8 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26NOV06SASSAK-28` Over 27.5 games: 0.22/0.30 mid 26.0%, model 34.7% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26NOV06SASSAK-2-SAS` Will Aliaksandra Sasnovich win set 2 in the Aliaksandra Sasnovich vs Maria Sakkari match: 0.02/0.99 mid 50.5%, model 46.2% (projection_v2.0 (prediction ledger)) -- gap -4.3 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26NOV06SASSAK-18` Over 17.5 games: 0.73/0.96 mid 84.5%, model 88.2% (projection_v2.0 (prediction ledger)) -- gap +3.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26NOV06SASSAK-2-SAK` Will Maria Sakkari win set 2 in the Aliaksandra Sasnovich vs Maria Sakkari match: 0.02/0.99 mid 50.5%, model 53.8% (projection_v2.0 (prediction ledger)) -- gap +3.3 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV06SASSAK-1-SAK` Will Maria Sakkari win set 1 in the Aliaksandra Sasnovich vs Maria Sakkari match: 0.54/0.57 mid 55.5%, model 53.8% (projection_v2.0 (prediction ledger)) -- gap -1.7 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV06SASSAK-1-SAS` Will Aliaksandra Sasnovich win set 1 in the Aliaksandra Sasnovich vs Maria Sakkari match: 0.43/0.46 mid 44.5%, model 46.2% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dmitry Bessonov vs Oleg Kolninov -- M15 Fergana QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 10:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-06T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212809:213614:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dmitry Bessonov (`KXITFMATCH-26NOV05BESKOL-BES`) | 0.02 / 0.94 (125) | 48.0% | 36.9% | 18.4% | 30.3% [30.3%-30.4%] | -- | -- | -- | -- | PASS | -11.1 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Oleg Kolninov (`KXITFMATCH-26NOV05BESKOL-KOL`) | 0.02 / 0.94 (125) | 48.0% | 63.1% | 81.6% | 69.7% [69.6%-69.7%] | -- | -- | -- | -- | PASS | +15.1 pp | HIGH_REVIEW (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 961.0, B 0.0; serve-point win A 59.4%, B 38.0%; Elo A 1137.5, B 1284.0; model uncertainty 0.0004
* Form inputs: days since last match A 206, B 948; matches on record A 25, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV05BESKOL-KOL  (YES = Oleg Kolninov)
Model: 63%
Kalshi: 48%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chirag Duhan vs Adrian Arcon -- M15 Fergana QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 10:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-06T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210003:210417:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Arcon (`KXITFMATCH-26NOV05DUHARC-ARC`) | 0.02 / 0.94 (125) | 48.0% | 15.7% | 27.4% | 20.4% [18.6%-22.4%] | -- | -- | -- | -- | PASS | -32.3 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Chirag Duhan (`KXITFMATCH-26NOV05DUHARC-DUH`) | 0.02 / 0.94 (125) | 48.0% | 84.3% | 72.7% | 79.6% [77.6%-81.4%] | -- | -- | -- | -- | PASS | +36.3 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1525.0, B 522.0; serve-point win A 67.5%, B 40.6%; Elo A 1258.0, B 997.6; model uncertainty 0.019
* Form inputs: days since last match A 227, B 185; matches on record A 96, B 22; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV05DUHARC-DUH  (YES = Chirag Duhan)
Model: 84%
Kalshi: 48%
Gap: +36 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Millen Hurrion vs Xirui Han -- M15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-06T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209140:212472:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xirui Han (`KXITFMATCH-26NOV06HURHAN-HAN`) | 0.06 / 0.86 (10) | 46.0% | 12.0% | 14.3% | 15.8% [14.2%-17.2%] | -- | -- | -- | -- | PASS | -34.0 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Millen Hurrion (`KXITFMATCH-26NOV06HURHAN-HUR`) | 0.40 / 0.94 (125) | 67.0% | 88.0% | 85.7% | 84.2% [82.8%-85.8%] | -- | -- | -- | -- | PASS | +21.0 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2993.0, B 542.0; serve-point win A 61.0%, B 47.9%; Elo A 1434.9, B 1153.8; model uncertainty 0.0152
* Form inputs: days since last match A 94, B 381; matches on record A 179, B 15; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV06HURHAN-HUR  (YES = Millen Hurrion)
Model: 88%
Kalshi: 67%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.006, surface_pool_high -0.006, surface_dev_loose +0.010, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniil Sarksian vs Seongchan Hong -- M15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-06T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV06SARHON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Seongchan Hong (`KXITFMATCH-26NOV06SARHON-HON`) | 0.46 / 0.94 (10) | 70.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daniil Sarksian (`KXITFMATCH-26NOV06SARHON-SAR`) | 0.05 / 0.82 (200) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rigele Te vs Tianhui Zhang -- M15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-06T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144751:212221:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rigele Te (`KXITFMATCH-26NOV06TEXZHA-TEX`) | 0.06 / 0.94 (10) | 50.0% | 63.6% | 51.0% | 56.5% [54.0%-60.0%] | -- | -- | -- | -- | PASS | +13.6 pp | REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tianhui Zhang (`KXITFMATCH-26NOV06TEXZHA-ZHA`) | 0.05 / 0.94 (10) | 49.5% | 36.4% | 49.0% | 43.5% [40.0%-46.0%] | -- | -- | -- | -- | PASS | -13.1 pp | REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1492.0, B 1273.0; serve-point win A 64.0%, B 38.7%; Elo A 1414.4, B 1331.9; model uncertainty 0.0301
* Form inputs: days since last match A 10, B 10; matches on record A 319, B 78; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose +0.020, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maxim Zhukov vs Kristjan Tamm -- M15 Maanshan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-06T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144932:210393:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kristjan Tamm (`KXITFMATCH-26NOV06ZHUTAM-TAM`) | 0.30 / 0.64 (69) | 47.0% | 21.0% | 18.8% | 21.3% [19.2%-24.4%] | -- | -- | -- | -- | PASS | -26.0 pp | EXTREME (DATA_WARNING) | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maxim Zhukov (`KXITFMATCH-26NOV06ZHUTAM-ZHU`) | 0.28 / 0.62 (65) | 45.0% | 79.0% | 81.2% | 78.7% [75.6%-80.8%] | -- | -- | -- | -- | PASS | +34.0 pp | EXTREME (DATA_WARNING) | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2791.0, B 1552.0; serve-point win A 65.8%, B 40.6%; Elo A 1452.3, B 1248.5; model uncertainty 0.026
* Form inputs: days since last match A 87, B 48; matches on record A 199, B 257; data quality A

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV06ZHUTAM-ZHU  (YES = Maxim Zhukov)
Model: 79%
Kalshi: 45%
Gap: +34 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.004, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Guo / Shi vs Ovcharenko / Savinykh -- W100 Incheon SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV06GUOSHIOVCSAV:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Guo / Shi (`KXITFWDOUBLES-26NOV06GUOSHIOVCSAV-GUOSHI`) | 0.41 / 0.74 (96) | 57.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ovcharenko / Savinykh (`KXITFWDOUBLES-26NOV06GUOSHIOVCSAV-OVCSAV`) | 0.19 / 0.51 (51) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Shimizu / Yoshioka vs Arakawa / Katsumi -- W35 Hamamatsu SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-06T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV06SHIYOSARAKAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arakawa / Katsumi (`KXITFWDOUBLES-26NOV06SHIYOSARAKAT-ARAKAT`) | 0.05 / 0.80 (40) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Shimizu / Yoshioka (`KXITFWDOUBLES-26NOV06SHIYOSARAKAT-SHIYOS`) | 0.24 / 0.90 (1) | 57.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Edoardo Cherie Ligniere vs David Eichenseher -- M15 Fergana QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-06T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212122:212631:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Edoardo Cherie Ligniere (`KXITFMATCH-26NOV06CHEEIC-CHE`) | 0.02 / 0.94 (125) | 48.0% | 53.1% | 66.2% | 52.6% [50.0%-54.7%] | -- | -- | -- | -- | PASS | +5.1 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| David Eichenseher (`KXITFMATCH-26NOV06CHEEIC-EIC`) | 0.02 / 0.94 (125) | 48.0% | 46.9% | 33.8% | 47.4% [45.3%-50.0%] | -- | -- | -- | -- | PASS | -1.1 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 266.0, B 1106.0; serve-point win A 59.0%, B 41.6%; Elo A 1192.7, B 1191.7; model uncertainty 0.0234
* Form inputs: days since last match A 192, B 192; matches on record A 17, B 30; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Digvijay Pratap Singh vs Aristarkh Safonov -- M15 Fergana QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-06T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV06SINSAF:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aristarkh Safonov (`KXITFMATCH-26NOV06SINSAF-SAF`) | 0.02 / 0.94 (10) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Digvijay Pratap Singh (`KXITFMATCH-26NOV06SINSAF-SIN`) | 0.02 / 0.94 (10) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mai Hontama vs Magda Linette -- WTA Chennai QF

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-06 12:30Z
* Current expected start: 2026-11-06 12:30Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: 2026-11-06 11:45Z

* Status notes: NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source)

WTA (TOUR_500_250) · Hard · scheduled 2026-11-06T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202663:215988:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mai Hontama (`KXWTAMATCH-26NOV06HONLIN-HON`) | 0.04 / 0.43 (5) | 23.5% | 36.1% | 43.2% | 38.1% [31.2%-40.1%] | -- | -- | -- | -- | PASS | +12.6 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Magda Linette (`KXWTAMATCH-26NOV06HONLIN-LIN`) | 0.51 / 0.94 (10) | 72.5% | 63.9% | 56.8% | 61.9% [59.9%-68.8%] | -- | -- | -- | -- | PASS | -8.6 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4001.0, B 4278.0; serve-point win A 55.7%, B 41.6%; Elo A 1682.7, B 1880.3; model uncertainty 0.0443
* Form inputs: days since last match A 0, B 0; matches on record A 494, B 915; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight -0.005
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26NOV06HONLIN-1-LIN` Will Magda Linette win set 1 in the Mai Hontama vs Magda Linette match: 0.02/0.94 mid 48.0%, model 59.4% (projection_v2.0 (prediction ledger)) -- gap +11.4 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV06HONLIN-1-HON` Will Mai Hontama win set 1 in the Mai Hontama vs Magda Linette match: 0.02/0.94 mid 48.0%, model 40.6% (projection_v2.0 (prediction ledger)) -- gap -7.4 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Robin Montgomery vs Maaya Rajeshwaran Revathi -- WTA Chennai QF

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-06 12:30Z
* Current expected start: 2026-11-06 12:30Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-05 13:28Z
* Recommended handicap-by time: 2026-11-06 11:45Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-06T05:00:00+00:00 as not a valid time; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-11-06T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:221905:266722:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Robin Montgomery (`KXWTAMATCH-26NOV06MONRAJ-MON`) | 0.83 / 0.85 (1802) | 84.0% | 88.9% | 82.2% | 86.8% [84.5%-89.8%] | 82.7% | 84.1% | 83.4% | MODEL_LONE_OUTLIER | WATCH | +4.9 pp | NORMAL | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Maaya Rajeshwaran Revathi (`KXWTAMATCH-26NOV06MONRAJ-RAJ`) | 0.15 / 0.17 (5489) | 16.0% | 11.1% | 17.8% | 13.2% [10.2%-15.5%] | 17.3% | 16.0% | 16.7% | MODEL_LONE_OUTLIER | PASS | -4.9 pp | NORMAL | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2060.0, B 796.0; serve-point win A 63.9%, B 45.5%; Elo A 1845.0, B 1511.5; model uncertainty 0.0269
* Form inputs: days since last match A 1, B 1; matches on record A 252, B 25; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.023, surface_dev_loose +0.007, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV06MONRAJ-15` Over 14.5 games: 0.03/0.93 mid 48.0%, model 97.3% (projection_v2.0 (prediction ledger)) -- gap +49.3 pp, EXTREME, DATA_WARNING, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26NOV06MONRAJ-20` Over 19.5 games: 0.47/0.48 mid 47.5%, model 57.8% (projection_v2.0 (prediction ledger)) -- gap +10.3 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26NOV06MONRAJ-25` Over 24.5 games: 0.23/0.28 mid 25.5%, model 32.4% (projection_v2.0 (prediction ledger)) -- gap +6.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26NOV06MONRAJ-1-RAJ` Will Maaya Rajeshwaran Revathi win set 1 in the Robin Montgomery vs Maaya Rajeshwaran Revathi match: 0.22/0.24 mid 23.0%, model 20.7% (projection_v2.0 (prediction ledger)) -- gap -2.3 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV06MONRAJ-1-MON` Will Robin Montgomery win set 1 in the Robin Montgomery vs Maaya Rajeshwaran Revathi match: 0.76/0.79 mid 77.5%, model 79.3% (projection_v2.0 (prediction ledger)) -- gap +1.8 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV06MONRAJ-2-MON` Will Robin Montgomery win set 2 in the Robin Montgomery vs Maaya Rajeshwaran Revathi match: 0.76/0.82 mid 79.0%, model 79.3% (projection_v2.0 (prediction ledger)) -- gap +0.3 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV06MONRAJ-2-RAJ` Will Maaya Rajeshwaran Revathi win set 2 in the Robin Montgomery vs Maaya Rajeshwaran Revathi match: 0.18/0.24 mid 21.0%, model 20.7% (projection_v2.0 (prediction ledger)) -- gap -0.3 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; LOW_DATA_QUALITY; STALE_QUOTE; WIDE_SPREAD

## Janice Tjen vs Polina Kudermetova -- WTA Chennai QF

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-06 12:30Z
* Current expected start: 2026-11-06 12:30Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-05 13:28Z
* Recommended handicap-by time: 2026-11-06 11:45Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-06T05:00:00+00:00 as not a valid time; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-11-06T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:221236:222145:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Kudermetova (`KXWTAMATCH-26NOV06TJEKUD-KUD`) | 0.37 / 0.38 (4770) | 37.5% | 48.6% | 31.7% | 34.0% [30.8%-43.8%] | 37.7% | 38.0% | 37.9% | MODEL_LONE_OUTLIER | PASS | +11.1 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Janice Tjen (`KXWTAMATCH-26NOV06TJEKUD-TJE`) | 0.62 / 0.63 (20) | 62.5% | 51.4% | 68.3% | 66.0% [56.2%-69.2%] | 62.3% | 62.5% | 62.4% | MODEL_LONE_OUTLIER | WATCH | -11.1 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3631.0, B 4285.0; serve-point win A 60.6%, B 39.7%; Elo A 1895.3, B 1814.1; model uncertainty 0.0649
* Form inputs: days since last match A 1, B 1; matches on record A 188, B 394; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.024, surface_pool_high +0.023, surface_dev_loose -0.005, surface_dev_tight +0.010
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV06TJEKUD-22` Over 21.5 games: 0.49/0.50 mid 49.5%, model 65.9% (projection_v2.0 (prediction ledger)) -- gap +16.4 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV06TJEKUD-27` Over 26.5 games: 0.26/0.31 mid 28.5%, model 42.2% (projection_v2.0 (prediction ledger)) -- gap +13.7 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV06TJEKUD-1-TJE` Will Janice Tjen win set 1 in the Janice Tjen vs Polina Kudermetova match: 0.58/0.62 mid 60.0%, model 50.9% (projection_v2.0 (prediction ledger)) -- gap -9.1 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV06TJEKUD-1-KUD` Will Polina Kudermetova win set 1 in the Janice Tjen vs Polina Kudermetova match: 0.39/0.42 mid 40.5%, model 49.1% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV06TJEKUD-2-TJE` Will Janice Tjen win set 2 in the Janice Tjen vs Polina Kudermetova match: 0.56/0.63 mid 59.5%, model 50.9% (projection_v2.0 (prediction ledger)) -- gap -8.6 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26NOV06TJEKUD-17` Over 16.5 games: 0.85/0.91 mid 88.0%, model 95.9% (projection_v2.0 (prediction ledger)) -- gap +7.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV06TJEKUD-2-KUD` Will Polina Kudermetova win set 2 in the Janice Tjen vs Polina Kudermetova match: 0.40/0.44 mid 42.0%, model 49.1% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STALE_QUOTE; WIDE_SPREAD

## Robert Cash / Brandon Nakashima vs Christian Harrison / Neal Skupski -- ATP Paris QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-05 13:28Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-06T05:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-06T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV06CASNAKHARSKU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Robert Cash / Brandon Nakashima (`KXATPDOUBLES-26NOV06CASNAKHARSKU-CASNAK`) | 0.25 / 0.32 (62) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Christian Harrison / Neal Skupski (`KXATPDOUBLES-26NOV06CASNAKHARSKU-HARSKU`) | 0.68 / 0.73 (49) | 70.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Lucas Miedler / Neil Oberleitner vs Petr Nouza / Michael Venus -- ATP Paris QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-06 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-05 13:28Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-06T05:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-06T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV06MIEOBENOUVEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucas Miedler / Neil Oberleitner (`KXATPDOUBLES-26NOV06MIEOBENOUVEN-MIEOBE`) | 0.57 / 0.64 (25) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Petr Nouza / Michael Venus (`KXATPDOUBLES-26NOV06MIEOBENOUVEN-NOUVEN`) | 0.36 / 0.43 (25) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Antonia Ruzic vs Alexandra Eala -- WTA Hong Kong QF

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-06 14:40Z
* Current expected start: 2026-11-06 14:40Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: 2026-11-06 13:55Z

* Status notes: NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source)

WTA (TOUR_500_250) · Hard · scheduled 2026-11-06T14:40:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:222045:223253:2026-11-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandra Eala (`KXWTAMATCH-26NOV06RUZEAL-EAL`) | 0.68 / 0.92 (11) | 80.0% | 70.3% | 61.5% | 62.5% [61.5%-66.0%] | -- | -- | -- | -- | PASS | -9.7 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Antonia Ruzic (`KXWTAMATCH-26NOV06RUZEAL-RUZ`) | 0.05 / 0.35 (4) | 20.0% | 29.7% | 38.5% | 37.5% [34.1%-38.5%] | -- | -- | -- | -- | PASS | +9.7 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4066.0, B 4541.0; serve-point win A 54.1%, B 41.9%; Elo A 1850.3, B 1962.4; model uncertainty 0.0224
* Form inputs: days since last match A 0, B 0; matches on record A 365, B 372; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.010, surface_dev_loose -0.005, surface_dev_tight -0.000
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
